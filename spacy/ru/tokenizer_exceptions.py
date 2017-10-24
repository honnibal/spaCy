# encoding: utf8

#
#   Developed by Expasoft Ltd.
#   Website: https://expasoft.ru/
#
#   Developer: Alexey Kim
#   GitHub: @yuukos
#

from __future__ import unicode_literals

from ..symbols import *


TOKENIZER_EXCEPTIONS = {
    "Пн.": [
        {ORTH: "Пн.", LEMMA: "Понедельник"}
    ],
    "Вт.": [
        {ORTH: "Вт.", LEMMA: "Вторник"}
    ],
    "Ср.": [
        {ORTH: "Ср.", LEMMA: "Среда"}
    ],
    "Чт.": [
        {ORTH: "Чт.", LEMMA: "Четверг"}
    ],
    "Пт.": [
        {ORTH: "Пт.", LEMMA: "Пятница"}
    ],
    "Сб.": [
        {ORTH: "Сб.", LEMMA: "Суббота"}
    ],
    "Вс.": [
        {ORTH: "Вс.", LEMMA: "Воскресенье"}
    ],
}

