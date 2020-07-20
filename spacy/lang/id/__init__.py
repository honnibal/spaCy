from thinc.config import Config

from .stop_words import STOP_WORDS
from .punctuation import TOKENIZER_SUFFIXES, TOKENIZER_PREFIXES, TOKENIZER_INFIXES
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .lex_attrs import LEX_ATTRS
from .syntax_iterators import SYNTAX_ITERATORS

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...language import Language
from ...attrs import LANG
from ...util import update_exc


DEFAULT_CONFIG = """
[nlp]
lang = "id"

[nlp.lemmatizer]
@lemmatizers = "spacy.Lemmatizer.v1"

[nlp.lemmatizer.data_paths]
@assets = "spacy-lookups-data"
lang = ${nlp:lang}
"""


class IndonesianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: "id"
    lex_attr_getters.update(LEX_ATTRS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    prefixes = TOKENIZER_PREFIXES
    suffixes = TOKENIZER_SUFFIXES
    infixes = TOKENIZER_INFIXES
    syntax_iterators = SYNTAX_ITERATORS


class Indonesian(Language):
    lang = "id"
    Defaults = IndonesianDefaults
    default_config = Config().from_str(DEFAULT_CONFIG)


__all__ = ["Indonesian"]
