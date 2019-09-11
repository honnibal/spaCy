# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA, PRON_LEMMA

# Several entries here look pretty suspicious. These will get the POS SCONJ
# given the tag IN, when an adpositional reading seems much more likely for
# a lot of these prepositions. I'm not sure what I was running in 04395ffa4
# when I did this? It doesn't seem right.
_subordinating_conjunctions = [
    "that",
    "if",
    "as",
    "because",
    #"of",
    #"for",
    #"before",
    #"in",
    "while",
    #"after",
    "since",
    "like",
    #"with",
    "so",
    #"to",
    #"by",
    #"on",
    #"about",
    "than",
    "whether",
    "although",
    #"from",
    "though",
    #"until",
    "unless",
    "once",
    #"without",
    #"at",
    #"into",
    "cause",
    #"over",
    "upon",
    "till",
    "whereas",
    #"beyond",
    "whilst",
    "except",
    "despite",
    "wether",
    #"then",
    "but",
    "becuse",
    "whie",
    #"below",
    #"against",
    "it",
    "w/out",
    #"toward",
    "albeit",
    "save",
    "besides",
    "becouse",
    "coz",
    "til",
    "ask",
    "i'd",
    "out",
    "near",
    "seince",
    #"towards",
    "tho",
    "sice",
    "will",
]

# This seems kind of wrong too?
#_relative_pronouns = ["this", "that", "those", "these"]

MORPH_RULES = {
    #"DT": {word: {"POS": "PRON"} for word in _relative_pronouns},
    "IN": {word: {"POS": "SCONJ"} for word in _subordinating_conjunctions},
    "NN": {
        "something": {"POS": "PRON"},
        "anyone": {"POS": "PRON"},
        "anything": {"POS": "PRON"},
        "nothing": {"POS": "PRON"},
        "someone": {"POS": "PRON"},
        "everything": {"POS": "PRON"},
        "everyone": {"POS": "PRON"},
        "everybody": {"POS": "PRON"},
        "nobody": {"POS": "PRON"},
        "somebody": {"POS": "PRON"},
        "anybody": {"POS": "PRON"},
        "any1": {"POS": "PRON"},
    },
    "PRP": {
        "I": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Sing",
            "Case": "Nom",
        },
        "me": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Sing",
            "Case": "Acc",
        },
        "you": {LEMMA: PRON_LEMMA, "POS": "PRON", "PronType": "Prs", "Person": "Two"},
        "he": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Masc",
            "Case": "Nom",
        },
        "him": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Masc",
            "Case": "Acc",
        },
        "she": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Fem",
            "Case": "Nom",
        },
        "her": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Fem",
            "Case": "Acc",
        },
        "it": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Neut",
        },
        "we": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Plur",
            "Case": "Nom",
        },
        "us": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Plur",
            "Case": "Acc",
        },
        "they": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Plur",
            "Case": "Nom",
        },
        "them": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Plur",
            "Case": "Acc",
        },
        "mine": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Sing",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "his": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Masc",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "hers": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Fem",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "its": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Neut",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "ours": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Plur",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "yours": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Two",
            "Number": "Plur",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "theirs": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Plur",
            "Poss": "Yes",
            "Reflex": "Yes",
        },
        "myself": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Sing",
            "Case": "Acc",
            "Reflex": "Yes",
        },
        "yourself": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Two",
            "Case": "Acc",
            "Reflex": "Yes",
        },
        "himself": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Case": "Acc",
            "Gender": "Masc",
            "Reflex": "Yes",
        },
        "herself": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Case": "Acc",
            "Gender": "Fem",
            "Reflex": "Yes",
        },
        "itself": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Case": "Acc",
            "Gender": "Neut",
            "Reflex": "Yes",
        },
        "themself": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Sing",
            "Case": "Acc",
            "Reflex": "Yes",
        },
        "ourselves": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "One",
            "Number": "Plur",
            "Case": "Acc",
            "Reflex": "Yes",
        },
        "yourselves": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Two",
            "Case": "Acc",
            "Reflex": "Yes",
        },
        "themselves": {
            LEMMA: PRON_LEMMA,
            "POS": "PRON",
            "PronType": "Prs",
            "Person": "Three",
            "Number": "Plur",
            "Case": "Acc",
            "Reflex": "Yes",
        },
    },
    "PRP$": {
        "my": {
            LEMMA: PRON_LEMMA,
            "Person": "One",
            "Number": "Sing",
            "PronType": "Prs",
            "Poss": "Yes",
        },
        "your": {LEMMA: PRON_LEMMA, "Person": "Two", "PronType": "Prs", "Poss": "Yes"},
        "his": {
            LEMMA: PRON_LEMMA,
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Masc",
            "PronType": "Prs",
            "Poss": "Yes",
        },
        "her": {
            LEMMA: PRON_LEMMA,
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Fem",
            "PronType": "Prs",
            "Poss": "Yes",
        },
        "its": {
            LEMMA: PRON_LEMMA,
            "Person": "Three",
            "Number": "Sing",
            "Gender": "Neut",
            "PronType": "Prs",
            "Poss": "Yes",
        },
        "our": {
            LEMMA: PRON_LEMMA,
            "Person": "One",
            "Number": "Plur",
            "PronType": "Prs",
            "Poss": "Yes",
        },
        "their": {
            LEMMA: PRON_LEMMA,
            "Person": "Three",
            "Number": "Plur",
            "PronType": "Prs",
            "Poss": "Yes",
        },
    },
    "RB": {word: {"POS": "PART"} for word in ["not", "n't", "nt", "n’t"]},
    "VB": {
        word: {"POS": "AUX"}
        for word in ["be", "have", "do", "get", "of", "am", "are", "'ve"]
    },
    "VBN": {"been": {LEMMA: "be", "POS": "AUX"}},
    "VBG": {"being": {LEMMA: "be", "POS": "AUX"}},
    "VBZ": {
        "am": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Person": "One",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "are": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Person": "Two",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "is": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Person": "Three",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "'re": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Person": "Two",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "'s": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Person": "Three",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "has": {LEMMA: "have", "POS": "AUX"},
        "does": {LEMMA: "do", "POS": "AUX"},
    },
    "VBP": {
        "are": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "'re": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "am": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Person": "One",
            "Tense": "Pres",
            "Mood": "Ind",
        },
        "do": {"POS": "AUX"},
        "have": {"POS": "AUX"},
        "'m": {"POS": "AUX", LEMMA: "be"},
        "'ve": {"POS": "AUX"},
        "'s": {"POS": "AUX"},
        "is": {"POS": "AUX"},
        "'d": {"POS": "AUX"},
    },
    "VBD": {
        "was": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Tense": "Past",
            "Number": "Sing",
        },
        "were": {
            LEMMA: "be",
            "POS": "AUX",
            "VerbForm": "Fin",
            "Tense": "Past",
            "Number": "Plur",
        },
        "did": {LEMMA: "do", "POS": "AUX"},
        "had": {LEMMA: "have", "POS": "AUX"},
        "'d": {LEMMA: "have", "POS": "AUX"},
    },
}


for tag, rules in MORPH_RULES.items():
    for key, attrs in dict(rules).items():
        rules[key.title()] = attrs
