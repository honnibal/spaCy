from typing import Optional, Dict, List, Union, Sequence
from timeit import default_timer as timer

import srsly
from pydantic import BaseModel, FilePath
import plac
import tqdm
from pathlib import Path
from wasabi import msg
import thinc
import thinc.schedules
from thinc.api import Model, use_pytorch_for_gpu_memory
import random

from ..gold import GoldCorpus
from ..lookups import Lookups
from .. import util
from ..errors import Errors
from ..ml import models  # don't remove - required to load the built-in architectures

registry = util.registry

CONFIG_STR = """
[training]
patience = 10
eval_frequency = 10
dropout = 0.2
init_tok2vec = null
max_epochs = 100
orth_variant_level = 0.0
gold_preproc = false
max_length = 0
use_gpu = 0
scores = ["ents_p",  "ents_r", "ents_f"]
score_weights = {"ents_f": 1.0}
limit = 0

[training.batch_size]
@schedules = "compounding.v1"
start = 100
stop = 1000
compound = 1.001

[optimizer]
@optimizers = "Adam.v1"
learn_rate = 0.001
beta1 = 0.9
beta2 = 0.999

[nlp]
lang = "en"
vectors = null

[nlp.pipeline.tok2vec]
factory = "tok2vec"

[nlp.pipeline.ner]
factory = "ner"

[nlp.pipeline.ner.model]
@architectures = "spacy.TransitionBasedParser.v1"
nr_feature_tokens = 3
hidden_width = 64
maxout_pieces = 3

[nlp.pipeline.ner.model.tok2vec]
@architectures = "spacy.Tok2VecTensors.v1"
width = ${nlp.pipeline.tok2vec.model:width}

[nlp.pipeline.tok2vec.model]
@architectures = "spacy.HashEmbedCNN.v1"
pretrained_vectors = null
width = 128
depth = 4
window_size = 1
embed_size = 10000
maxout_pieces = 3
subword_features = true
"""


class PipelineComponent(BaseModel):
    factory: str
    model: Model

    class Config:
        arbitrary_types_allowed = True


class ConfigSchema(BaseModel):
    optimizer: Optional["Optimizer"]

    class training(BaseModel):
        patience: int = 10
        eval_frequency: int = 100
        dropout: float = 0.2
        init_tok2vec: Optional[FilePath] = None
        max_epochs: int = 100
        orth_variant_level: float = 0.0
        gold_preproc: bool = False
        max_length: int = 0
        use_gpu: int = 0
        scores: List[str] = ["ents_p", "ents_r", "ents_f"]
        score_weights: Dict[str, Union[int, float]] = {"ents_f": 1.0}
        limit: int = 0
        batch_size: Union[Sequence[int], int]

    class nlp(BaseModel):
        lang: str
        vectors: Optional[str]
        pipeline: Optional[Dict[str, PipelineComponent]]

    class Config:
        extra = "allow"


@plac.annotations(
    # fmt: off
    train_path=("Location of JSON-formatted training data", "positional", None, Path),
    dev_path=("Location of JSON-formatted development data", "positional", None, Path),
    config_path=("Path to config file", "positional", None, Path),
    output_path=("Output directory to store model in", "option", "o", Path),
    meta_path=("Optional path to meta.json to use as base.", "option", "m", Path),
    init_tok2vec=(
    "Path to pretrained weights for the tok2vec components. See 'spacy pretrain'. Experimental.", "option", "t2v",
    Path),
    raw_text=("Path to jsonl file with unlabelled text documents.", "option", "rt", Path),
    verbose=("Display more information for debugging purposes", "flag", "VV", bool),
    use_gpu=("Use GPU", "option", "g", int),
    tag_map_path=("Location of JSON-formatted tag map", "option", "tm", Path),
    omit_extra_lookups=("Don't include extra lookups in model", "flag", "OEL", bool),
    # fmt: on
)
def train_cli(
    train_path,
    dev_path,
    config_path,
    output_path=None,
    meta_path=None,
    init_tok2vec=None,
    raw_text=None,
    verbose=False,
    use_gpu=-1,
    tag_map_path=None,
    omit_extra_lookups=False,
):
    """
    Train or update a spaCy model. Requires data to be formatted in spaCy's
    JSON format. To convert data from other formats, use the `spacy convert`
    command.
    """
    util.set_env_log(verbose)

    # Make sure all files and paths exists if they are needed
    if not config_path or not config_path.exists():
        msg.fail("Config file not found", config_path, exits=1)
    if not train_path or not train_path.exists():
        msg.fail("Training data not found", train_path, exits=1)
    if not dev_path or not dev_path.exists():
        msg.fail("Development data not found", dev_path, exits=1)
    if meta_path is not None and not meta_path.exists():
        msg.fail("Can't find model meta.json", meta_path, exits=1)
    if output_path is not None and not output_path.exists():
        output_path.mkdir()
        msg.good(f"Created output directory: {output_path}")
    elif output_path.exists() and [p for p in output_path.iterdir() if p.is_dir()]:
        msg.warn(
            "Output directory is not empty.",
            "This can lead to unintended side effects when saving the model. "
            "Please use an empty directory or a different path instead. If "
            "the specified output path doesn't exist, the directory will be "
            "created for you.",
        )
    if raw_text is not None:
        raw_text = list(srsly.read_jsonl(raw_text))
    tag_map = {}
    if tag_map_path is not None:
        tag_map = srsly.read_json(tag_map_path)

    weights_data = None
    if init_tok2vec is not None:
        if not init_tok2vec.exists():
            msg.fail("Can't find pretrained tok2vec", init_tok2vec, exits=1)
        with init_tok2vec.open("rb") as file_:
            weights_data = file_.read()

    if use_gpu >= 0:
        msg.info("Using GPU: {use_gpu}")
        util.use_gpu(use_gpu)
    else:
        msg.info("Using CPU")

    train(
        config_path,
        {"train": train_path, "dev": dev_path},
        output_path=output_path,
        meta_path=meta_path,
        raw_text=raw_text,
        tag_map=tag_map,
        weights_data=weights_data,
        omit_extra_lookups=omit_extra_lookups,
    )


def train(
    config_path,
    data_paths,
    raw_text=None,
    meta_path=None,
    output_path=None,
    tag_map=None,
    weights_data=None,
    omit_extra_lookups=False,
):
    msg.info(f"Loading config from: {config_path}")
    # Read the config first without creating objects, to get to the original nlp_config
    config = util.load_config(config_path, create_objects=False)
    util.fix_random_seed(config["training"]["seed"])
    if config["training"]["use_pytorch_for_gpu_memory"]:
        use_pytorch_for_gpu_memory()
    nlp_config = config["nlp"]
    config = util.load_config(config_path, create_objects=True)
    msg.info("Creating nlp from config")
    nlp = util.load_model_from_config(nlp_config)
    training = config["training"]
    optimizer = training["optimizer"]
    limit = training["limit"]
    msg.info("Loading training corpus")
    corpus = GoldCorpus(data_paths["train"], data_paths["dev"], limit=limit)
    msg.info("Initializing the nlp pipeline")
    nlp.begin_training(
        lambda: corpus.train_examples
    )  # TODO: what if existing (base) model ?
    meta = srsly.read_json(meta_path) if meta_path else {}

    # Update tag map with provided mapping
    nlp.vocab.morphology.tag_map.update(tag_map)

    # Create empty extra lexeme tables so the data from spacy-lookups-data
    # isn't loaded if these features are accessed
    if omit_extra_lookups:
        nlp.vocab.lookups_extra = Lookups()
        nlp.vocab.lookups_extra.add_table("lexeme_cluster")
        nlp.vocab.lookups_extra.add_table("lexeme_prob")
        nlp.vocab.lookups_extra.add_table("lexeme_settings")

    # Verify textcat config
    if nlp_config["pipeline"].get("textcat", {}).get("positive_label", None):
        textcat_labels = nlp.get_pipe("textcat").cfg.get("labels", [])
        pos_label = nlp_config["pipeline"]["textcat"]["positive_label"]
        if pos_label not in textcat_labels:
            msg.fail(
                f"The textcat's 'positive_label' config setting '{pos_label}' "
                f"does not match any label in the training data.",
                exits=1,
            )
        if len(textcat_labels) != 2:
            msg.fail(
                f"A textcat 'positive_label' '{pos_label}' was "
                f"provided for training data that does not appear to be a "
                f"binary classification problem with two labels.",
                exits=1,
            )

    # Load a pretrained tok2vec model - cf. CLI command 'pretrain'
    if weights_data is not None:
        tok2vec_path = config.get("pretraining", {}).get("tok2vec_model", None)
        if tok2vec_path is None:
            msg.fail(
                f"To use a pretrained tok2vec model, the config needs to specify which "
                f"tok2vec layer to load in the setting [pretraining.tok2vec_model].",
                exits=1,
            )
        tok2vec = config
        for subpath in tok2vec_path.split("."):
            tok2vec = tok2vec.get(subpath)
        tok2vec.from_bytes(weights_data)

    train_batches = create_train_batches(nlp, corpus, training)
    evaluate = create_evaluation_callback(nlp, optimizer, corpus, training)

    # Create iterator, which yields out info after each optimization step.
    msg.info("Start training")
    training_step_iterator = train_while_improving(
        nlp,
        optimizer,
        train_batches,
        evaluate,
        dropout=training["dropout"],
        accumulate_gradient=training["accumulate_gradient"],
        patience=training.get("patience", 0),
        max_steps=training.get("max_steps", 0),
        eval_frequency=training["eval_frequency"],
    )

    msg.info(f"Training. Initial learn rate: {optimizer.learn_rate}")
    print_row = setup_printer(training, nlp)

    try:
        progress = tqdm.tqdm(total=training["eval_frequency"], leave=False)
        for batch, info, is_best_checkpoint in training_step_iterator:
            progress.update(1)
            if is_best_checkpoint is not None:
                progress.close()
                print_row(info)
                if is_best_checkpoint and output_path is not None:
                    nlp.to_disk(output_path)
                progress = tqdm.tqdm(total=training["eval_frequency"], leave=False)
            # Clean up the objects to faciliate garbage collection.
            for eg in batch:
                eg.doc = None
                eg.goldparse = None
                eg.doc_annotation = None
                eg.token_annotation = None
    finally:
        if output_path is not None:
            final_model_path = output_path / "model-final"
            if optimizer.averages:
                with nlp.use_params(optimizer.averages):
                    nlp.to_disk(final_model_path)
            else:
                nlp.to_disk(final_model_path)
            msg.good("Saved model to output directory", final_model_path)


def create_train_batches(nlp, corpus, cfg):
    epochs_todo = cfg.get("max_epochs", 0)
    while True:
        train_examples = list(
            corpus.train_dataset(
                nlp,
                noise_level=0.0,
                orth_variant_level=cfg["orth_variant_level"],
                gold_preproc=cfg["gold_preproc"],
                max_length=cfg["max_length"],
                ignore_misaligned=True,
            )
        )
        if len(train_examples) == 0:
            raise ValueError(Errors.E988)
        random.shuffle(train_examples)
        batches = util.minibatch_by_words(
            train_examples,
            size=cfg["batch_size"],
            discard_oversize=cfg["discard_oversize"],
        )
        # make sure the minibatch_by_words result is not empty, or we'll have an infinite training loop
        try:
            first = next(batches)
            yield first
        except StopIteration:
            raise ValueError(Errors.E986)
        for batch in batches:
            yield batch
        epochs_todo -= 1
        # We intentionally compare exactly to 0 here, so that max_epochs < 1
        # will not break.
        if epochs_todo == 0:
            break


def create_evaluation_callback(nlp, optimizer, corpus, cfg):
    def evaluate():
        dev_examples = list(
            corpus.dev_dataset(
                nlp, gold_preproc=cfg["gold_preproc"], ignore_misaligned=True
            )
        )
        n_words = sum(len(ex.doc) for ex in dev_examples)
        start_time = timer()

        if optimizer.averages:
            with nlp.use_params(optimizer.averages):
                scorer = nlp.evaluate(dev_examples, batch_size=32)
        else:
            scorer = nlp.evaluate(dev_examples, batch_size=32)
        end_time = timer()
        wps = n_words / (end_time - start_time)
        scores = scorer.scores
        # Calculate a weighted sum based on score_weights for the main score
        weights = cfg["score_weights"]
        weighted_score = sum(scores[s] * weights.get(s, 0.0) for s in weights)
        scores["speed"] = wps
        return weighted_score, scores

    return evaluate


def train_while_improving(
    nlp,
    optimizer,
    train_data,
    evaluate,
    *,
    dropout,
    eval_frequency,
    accumulate_gradient=1,
    patience=0,
    max_steps=0,
):
    """Train until an evaluation stops improving. Works as a generator,
    with each iteration yielding a tuple `(batch, info, is_best_checkpoint)`,
    where info is a dict, and is_best_checkpoint is in [True, False, None] --
    None indicating that the iteration was not evaluated as a checkpoint.
    The evaluation is conducted by calling the evaluate callback, which should

    Positional arguments:
        nlp: The spaCy pipeline to evaluate.
        optimizer: The optimizer callable.
        train_data (Iterable[Batch]): A generator of batches, with the training
            data. Each batch should be a Sized[Tuple[Input, Annot]]. The training
            data iterable needs to take care of iterating over the epochs and
            shuffling.
        evaluate (Callable[[], Tuple[float, Any]]): A callback to perform evaluation.
            The callback should take no arguments and return a tuple
            `(main_score, other_scores)`. The main_score should be a float where
            higher is better. other_scores can be any object.

    Every iteration, the function yields out a tuple with:

    * batch: A zipped sequence of Tuple[Doc, GoldParse] pairs.
    * info: A dict with various information about the last update (see below).
    * is_best_checkpoint: A value in None, False, True, indicating whether this
        was the best evaluation so far. You should use this to save the model
        checkpoints during training. If None, evaluation was not conducted on
        that iteration. False means evaluation was conducted, but a previous
        evaluation was better.

    The info dict provides the following information:

        epoch (int): How many passes over the data have been completed.
        step (int): How many steps have been completed.
        score (float): The main score form the last evaluation.
        other_scores: : The other scores from the last evaluation.
        loss: The accumulated losses throughout training.
        checkpoints: A list of previous results, where each result is a
            (score, step, epoch) tuple.
    """
    if isinstance(dropout, float):
        dropouts = thinc.schedules.constant(dropout)
    else:
        dropouts = dropout
    results = []
    losses = {}
    to_enable = [name for name, proc in nlp.pipeline if hasattr(proc, "model")]
    msg.info(f"Training components: {to_enable}")

    for step, batch in enumerate(train_data):
        dropout = next(dropouts)
        with nlp.select_pipes(enable=to_enable):
            for subbatch in subdivide_batch(batch, accumulate_gradient):
                nlp.update(subbatch, drop=dropout, losses=losses, sgd=False)
            for name, proc in nlp.pipeline:
                if hasattr(proc, "model"):
                    proc.model.finish_update(optimizer)
        optimizer.step_schedules()
        if not (step % eval_frequency):
            score, other_scores = evaluate()
            results.append((score, step))
            is_best_checkpoint = score == max(results)[0]
        else:
            score, other_scores = (None, None)
            is_best_checkpoint = None
        info = {
            "step": step,
            "score": score,
            "other_scores": other_scores,
            "losses": losses,
            "checkpoints": results,
        }
        yield batch, info, is_best_checkpoint
        if is_best_checkpoint is not None:
            losses = {}
        # Stop if no improvement in `patience` updates (if specified)
        best_score, best_step = max(results)
        if patience and (step - best_step) >= patience:
            break
        # Stop if we've exhausted our max steps (if specified)
        if max_steps and (step * accumulate_gradient) >= max_steps:
            break


def subdivide_batch(batch, accumulate_gradient):
    batch = list(batch)
    batch.sort(key=lambda eg: len(eg.doc))
    sub_len = len(batch) // accumulate_gradient
    start = 0
    for i in range(accumulate_gradient):
        subbatch = batch[start : start + sub_len]
        if subbatch:
            yield subbatch
        start += len(subbatch)
    subbatch = batch[start:]
    if subbatch:
        yield subbatch


def setup_printer(training, nlp):
    score_cols = training["scores"]
    score_widths = [max(len(col), 6) for col in score_cols]
    loss_cols = [f"Loss {pipe}" for pipe in nlp.pipe_names]
    loss_widths = [max(len(col), 8) for col in loss_cols]
    table_header = ["#"] + loss_cols + score_cols + ["Score"]
    table_header = [col.upper() for col in table_header]
    table_widths = [6] + loss_widths + score_widths + [6]
    table_aligns = ["r" for _ in table_widths]

    msg.row(table_header, widths=table_widths)
    msg.row(["-" * width for width in table_widths])

    def print_row(info):
        losses = [
            "{0:.2f}".format(float(info["losses"].get(pipe_name, 0.0)))
            for pipe_name in nlp.pipe_names
        ]
        scores = [
            "{0:.2f}".format(float(info["other_scores"].get(col, 0.0)))
            for col in score_cols
        ]
        data = (
            [info["step"]] + losses + scores + ["{0:.2f}".format(float(info["score"]))]
        )
        msg.row(data, widths=table_widths, aligns=table_aligns)

    return print_row
