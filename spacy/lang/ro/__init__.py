from typing import Set, Dict, Callable, Any
from thinc.api import Config

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .punctuation import TOKENIZER_PREFIXES, TOKENIZER_INFIXES
from .punctuation import TOKENIZER_SUFFIXES
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...language import Language
from ...util import update_exc, registry

# Lemma data note:
# Original pairs downloaded from http://www.lexiconista.com/datasets/lemmatization/
# Replaced characters using cedillas with the correct ones (ș and ț)


DEFAULT_CONFIG = """
[nlp]
lang = "ro"
stop_words = {"@language_data": "spacy.ro.stop_words"}
lex_attr_getters = {"@language_data": "spacy.ro.lex_attr_getters"}

[nlp.lemmatizer]
@lemmatizers = "spacy.Lemmatizer.v1"

[nlp.lemmatizer.data_paths]
@language_data = "spacy-lookups-data"
lang = ${nlp:lang}
"""


@registry.language_data("spacy.ro.stop_words")
def stop_words() -> Set[str]:
    return STOP_WORDS


@registry.language_data("spacy.ro.lex_attr_getters")
def lex_attr_getters() -> Dict[int, Callable[[str], Any]]:
    return LEX_ATTRS


class RomanianDefaults(Language.Defaults):
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    prefixes = TOKENIZER_PREFIXES
    suffixes = TOKENIZER_SUFFIXES
    infixes = TOKENIZER_INFIXES


class Romanian(Language):
    lang = "ro"
    Defaults = RomanianDefaults
    default_config = Config().from_str(DEFAULT_CONFIG)


__all__ = ["Romanian"]
