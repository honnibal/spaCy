# coding: utf-8
from __future__ import unicode_literals

import pytest


# fmt: off
TOKENIZER_TESTS = [
    ("서울 타워 근처에 살고 있습니다.", "서울 타워 근처 에 살 고 있 습니다 ."),
    ("영등포구청역에 있는 맛집 좀 알려주세요.", "영등포구청역 에 있 는 맛집 좀 알려 주 세요 ."
]

TAG_TESTS = [
    ("서울 타워 근처에 살고 있습니다.", "NNP NNG NNG JKB VV EC VX EF SF"),
    ("영등포구청역에 있는 맛집 좀 알려주세요.", "NNP JKB VV ETM NNG MAG VV+EC VX EP+EF SF")
]

POS_TESTS = [
    ("서울 타워 근처에 살고 있습니다.", "PROPN NOUN NOUN ADP VERB X VX X PUNCT"),
    ("영등포구청역에 있는 맛집 좀 알려주세요.", "PROPN ADP VERB X NOUN ADV VERB AUX X PUNCT")
]
# fmt: on


@pytest.mark.parametrize("text,expected_tokens", TOKENIZER_TESTS)
def test_ja_tokenizer(ja_tokenizer, text, expected_tokens):
    tokens = [token.text for token in ja_tokenizer(text)]
    assert tokens == expected_tokens.split()


@pytest.mark.parametrize("text,expected_tags", TAG_TESTS)
def test_ja_tokenizer_tags(ja_tokenizer, text, expected_tags):
    tags = [token.tag_ for token in ja_tokenizer(text)]
    assert tags == expected_tags.split()


@pytest.mark.parametrize("text,expected_pos", POS_TESTS)
def test_ja_tokenizer_pos(ja_tokenizer, text, expected_pos):
    pos = [token.pos_ for token in ja_tokenizer(text)]
    assert pos == expected_pos.split()
