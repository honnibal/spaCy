from thinc.api import Config

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .punctuation import TOKENIZER_INFIXES, TOKENIZER_SUFFIXES
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...language import Language
from ...attrs import LANG
from ...util import update_exc


DEFAULT_CONFIG = """
[nlp]
lang = "da"

[nlp.lemmatizer]
@lemmatizers = "spacy.Lemmatizer.v1"

[nlp.lemmatizer.data_paths]
@assets = "spacy-lookups-data"
lang = ${nlp:lang}
"""


class DanishDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "da"
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    infixes = TOKENIZER_INFIXES
    suffixes = TOKENIZER_SUFFIXES
    stop_words = STOP_WORDS


class Danish(Language):
    lang = "da"
    Defaults = DanishDefaults
    default_config = Config().from_str(DEFAULT_CONFIG)


__all__ = ["Danish"]
