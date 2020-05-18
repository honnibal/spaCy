import pytest
from spacy.ml.models.defaults import default_parser, default_tok2vec
from spacy.vocab import Vocab
from spacy.syntax.arc_eager import ArcEager
from spacy.syntax.nn_parser import Parser
from spacy.ml.tb_framework import TransitionModel
from spacy.tokens.doc import Doc
from spacy.gold import GoldParse


@pytest.fixture
def vocab():
    return Vocab()


@pytest.fixture
def arc_eager(vocab):
    actions = ArcEager.get_actions(left_labels=["L"], right_labels=["R"])
    return ArcEager(vocab.strings, actions)


@pytest.fixture
def tok2vec():
    tok2vec = default_tok2vec()
    tok2vec.initialize()
    return tok2vec


@pytest.fixture
def parser(vocab, arc_eager):
    return Parser(vocab, model=default_parser(), moves=arc_eager)


@pytest.fixture
def model(arc_eager, tok2vec, vocab):
    model = default_parser()
    model.resize_output(arc_eager.n_moves)
    model.initialize()
    return model


@pytest.fixture
def doc(vocab):
    return Doc(vocab, words=["a", "b", "c"])


@pytest.fixture
def gold(doc):
    return GoldParse(doc, heads=[1, 1, 1], deps=["L", "ROOT", "R"])


def test_can_init_nn_parser(parser):
    assert isinstance(parser.model, TransitionModel)


def test_build_model(parser, vocab):
    parser.model = Parser(vocab, model=default_parser(), moves=parser.moves).model
    assert parser.model is not None


def test_predict_doc(parser, tok2vec, model, doc):
    doc.tensor = tok2vec.predict([doc])[0]
    parser.model = model
    parser(doc)


def test_update_doc(parser, model, doc, gold):
    parser.model = model

    def optimize(key, weights, gradient):
        weights -= 0.001 * gradient
        return weights, gradient

    parser.update((doc, gold), sgd=optimize)


@pytest.mark.xfail
def test_predict_doc_beam(parser, model, doc):
    parser.model = model
    parser(doc, beam_width=32, beam_density=0.001)


@pytest.mark.xfail
def test_update_doc_beam(parser, model, doc, gold):
    parser.model = model

    def optimize(weights, gradient, key=None):
        weights -= 0.001 * gradient

    parser.update_beam((doc, gold), sgd=optimize)
