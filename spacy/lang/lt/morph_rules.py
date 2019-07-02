# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA, PRON_LEMMA


_coordinating_conjunctions = [
    'ar', 'arba', 'bei', 'beigi', 'bet', 'betgi', 'ir', 'kadangi',
    'kuo', 'ne', 'o', 'tad', 'tai', 'tačiau', 'tegul', 'tik', 'visgi'
]

_subordinating_conjunctions = [
    'jei', 'jeigu', 'jog', 'kad', 'kai', 'kaip', 'kol', 'lyg',
    'nebent', 'negu', 'nei', 'nes', 'nors', 'tarsi', 'tuo', 'užuot'
]

MORPH_RULES = {
    'Cg': dict(
        [(word, {"POS": "CCONJ"}) for word in _coordinating_conjunctions] +
        [(word, {"POS": "SCONJ"}) for word in _subordinating_conjunctions]
    ),
    'Pg--an': {
        'keletą': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'PronType': 'Ind'
        },
        'save': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'PronType': 'Prs',
            'Reflex': 'Yes'
        }
    },
    'Pg--dn': {
        'sau': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'PronType': 'Prs',
            'Reflex': 'Yes'
        }
    },
    'Pg--gn': {
        'keleto': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'PronType': 'Ind'
        },
        'savo': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'PronType': 'Prs',
            'Reflex': 'Yes'
        },
        'savęs': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'PronType': 'Prs',
            'Reflex': 'Yes'
        }
    },
    'Pg--in': {
        'savimi': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'PronType': 'Prs',
            'Reflex': 'Yes'
        }
    },
    'Pg--nn': {
        'keletas': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'PronType': 'Ind'
        }
    },
    'Pg-dnn': {
        'mudu': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Number': 'Dual',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pg-pa-': {
        'jus': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-pan': {
        'jus': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'mus': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Number': 'Plur',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pg-pdn': {
        'jums': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'mums': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Number': 'Plur',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pg-pgn': {
        'jūsų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'mūsų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Number': 'Plur',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pg-pin': {
        'jumis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'mumis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Number': 'Plur',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pg-pln': {
        'jumyse': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-pnn': {
        'jūs': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'mes': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Number': 'Plur',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pg-san': {
        'mane': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'tave': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-sd-': {
        'tau': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-sdn': {
        'man': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'sau': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Number': 'Sing',
            'PronType': 'Prs',
            'Reflex': 'Yes'
        },
        'tau': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-sgn': {
        'mano': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'manęs': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'tavo': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        },
        'tavęs': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-sin': {
        'manimi': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'tavim': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        },
        'tavimi': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-sln': {
        'manyje': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'tavyje': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pg-snn': {
        'aš': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Number': 'Sing',
            'Person': '1',
            'PronType': 'Prs'
        },
        'tu': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Number': 'Sing',
            'Person': '2',
            'PronType': 'Prs'
        }
    },
    'Pgf-an': {
        'kelias': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'PronType': 'Ind'
        }
    },
    'Pgf-dn': {
        'kelioms': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Fem',
            'PronType': 'Ind'
        }
    },
    'Pgf-nn': {
        'kelios': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'PronType': 'Ind'
        }
    },
    'Pgfdn-': {
        'abi': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Dual',
            'PronType': 'Ind'
        }
    },
    'Pgfpan': {
        'jas': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kelias': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kitas': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokias': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'kurias': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'savas': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'tas': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tokias': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgfpdn': {
        'joms': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitoms': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kurioms': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'tokioms': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgfpgn': {
        'jokių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Neg'
        },
        'jų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kelių': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kitų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kurių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'pačių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tokių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tų': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgfpin': {
        'jomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitokiomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kitomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokiomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'kuriomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'pačiomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tomis': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgfpln': {
        'jose': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitose': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kuriose': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'tokiose': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tose': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgfpnn': {
        'jos': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitokios': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kitos': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'kurios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'pačios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tokios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tos': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgfsan': {
        'ją': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvieną': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kitokią': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kitą': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kokią': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kurią': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'pačią': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'tokią': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tą': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgfsdn': {
        'jai': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvienai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kitai': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'pačiai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Emp'
        }
    },
    'Pgfsgn': {
        'jokios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Neg'
        },
        'jos': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvienos': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kokios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kurios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'pačios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'tokios': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tos': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgfsin': {
        'ja': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekviena': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kita': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kuria': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'ta': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tokia': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgfsln': {
        'joje': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvienoje': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kitoje': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kurioje': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'toje': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tokioje': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgfsnn': {
        'ji': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekviena': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kita': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kokia': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kuri': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'pati': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'sava': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'ta': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tokia': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgfsny': {
        'jinai': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'toji': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgfsny-': {
        'jinai': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        }
    },
    'Pgm-a-': {
        'kelis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'PronType': 'Ind'
        }
    },
    'Pgm-an': {
        'kelis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'PronType': 'Ind'
        }
    },
    'Pgm-dn': {
        'keliems': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Masc',
            'PronType': 'Ind'
        }
    },
    'Pgm-gn': {
        'kelių': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'PronType': 'Ind'
        }
    },
    'Pgm-nn': {
        'keli': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'PronType': 'Ind'
        }
    },
    'Pgmdan': {
        'mudu': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Dual',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pgmdgn': {
        'mudviejų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Dual',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pgmdnn': {
        'jiedu': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Dual',
            'Person': '3',
            'PronType': 'Prs'
        },
        'mudu': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Dual',
            'Person': '1',
            'PronType': 'Prs'
        }
    },
    'Pgmpan': {
        'juos': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'jus': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'kitus': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokius': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'kuriuos': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'pačius': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tokius': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tuos': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgmpan-': {
        'juos': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        }
    },
    'Pgmpdn': {
        'jiems': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitiems': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kuriems': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'patiems': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tiems': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgmpgn': {
        'jokių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Neg'
        },
        'jų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitų': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'kurių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'pačių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tokių': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tų': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgmpin': {
        'jais': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'jokiais': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Neg'
        },
        'kitais': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokiais': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'savais': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'tais': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tokiais': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgmpln': {
        'juose': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kituose': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        }
    },
    'Pgmpnn': {
        'jie': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '3',
            'PronType': 'Prs'
        },
        'jūs': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Person': '2',
            'PronType': 'Prs'
        },
        'kiti': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Ind'
        },
        'kokie': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'kurie': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Int'
        },
        'patys': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Emp'
        },
        'tie': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        },
        'tokie': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Plur',
            'PronType': 'Dem'
        }
    },
    'Pgmsan': {
        'jį': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvieną': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kitokį': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kitą': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kokį': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kurį': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'tokį': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tą': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Acc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgmsdn': {
        'jam': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvienam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kitam': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kokiam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kuriam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'pačiam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'tam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgmsgn': {
        'jo': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'jokio': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Neg'
        },
        'kiekvieno': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kito': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kokio': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kurio': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'paties': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'savo': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'to': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tokio': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Gen',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgmsin': {
        'juo': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kitu': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kokiu': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kuriuo': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'pačiu': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'tokiu': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'tuo': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Ins',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgmsln': {
        'jame': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'kiekvienam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kokiame': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kuriame': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'tame': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Loc',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgmsnn': {
        'jis': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Person': '3',
            'PronType': 'Prs'
        },
        'joks': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Neg'
        },
        'kiekvienas': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Tot'
        },
        'kitas': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'kitoks': {
            LEMMA: PRON_LEMMA,
            'POS': 'PRON',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Ind'
        },
        'koks': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'kuris': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Int'
        },
        'pats': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'tas': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'toks': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgmsny': {
        'patsai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Emp'
        },
        'tasai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        },
        'toksai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Nom',
            'Gender': 'Masc',
            'Number': 'Sing',
            'PronType': 'Dem'
        }
    },
    'Pgn--n': {
        'tai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Gender': 'Neut',
            'PronType': 'Dem'
        }
    },
    'Pgnn--n': {
        'tai': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Gender': 'Neut',
            'PronType': 'Dem'
        }
    },
    'Pgsmdn': {
        'tam': {
            LEMMA: PRON_LEMMA,
            'POS': 'DET',
            'Case': 'Dat',
            'PronType': 'Dem'
        }
    },
    'Qg': {
        'tai': {
            LEMMA: 'tas',
            'POS': 'PART'
        }
    },
    'Vgap----n--n--': {
        'esant': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Ger'
        },
        'turint': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Ger'
        }
    },
    'Vgh--pm-n--n--': {
        'būdami': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'VerbForm': 'Conv'
        }
    },
    'Vgh--sm-n--n--': {
        'būdamas': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'VerbForm': 'Conv'
        }
    },
    'Vgi-----n--n--': {
        'būti': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Polarity': 'POS',
            'VerbForm': 'Inf'
        },
        'daryti': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Polarity': 'POS',
            'VerbForm': 'Inf'
        },
        'turėti': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Polarity': 'POS',
            'VerbForm': 'Inf'
        }
    },
    'Vgm-1p--n--ns-': {
        'turėtume': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Plur',
            'Person': '1',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgm-2p--n--nm-': {
        'būkite': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Imp',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        },
        'darykit': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Imp',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        },
        'darykite': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Imp',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        },
        'turėkite': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Imp',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgm-2p--n--ns-': {
        'turėtumėte': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgm-2s--n--ns-': {
        'turėtum': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Sing',
            'Person': '2',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgm-3---n--ns-': {
        'būtų': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Person': '3',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        },
        'turėtų': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Person': '3',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgm-3p--n--ns-': {
        'būtų': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        },
        'turėtų': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgm-3s--n--ns-': {
        'būtų': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        },
        'turėtų': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Cnd',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'VerbForm': 'Fin'
        }
    },
    'Vgma1p--n--ni-': {
        'turėjom': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgma1s--n--ni-': {
        'turėjau': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgma3---n--ni-': {
        'buvo': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        },
        'turėjo': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgma3p--n--ni-': {
        'buvo': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        },
        'darė': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        },
        'turėjo': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgma3s--n--ni-': {
        'buvo': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        },
        'darė': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        },
        'turėjo': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgmf1s--n--ni-': {
        'turėsiu': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        }
    },
    'Vgmf2p--n--ni-': {
        'būsite': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        },
        'darysite': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        },
        'turėsite': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        }
    },
    'Vgmf3---n--ni-': {
        'bus': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        }
    },
    'Vgmf3p--n--ni-': {
        'bus': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        },
        'darys': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        },
        'turės': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        }
    },
    'Vgmf3s--n--ni-': {
        'bus': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        },
        'turės': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp1p--n--ni-': {
        'darome': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'esame': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turime': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp1s--n--ni-': {
        'būnu': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'esu': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turiu': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '1',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp2p--n--ni-': {
        'esate': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turite': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp2s--n--ni-': {
        'esi': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turi': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp3---n--ni-': {
        'būna': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turi': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'yra': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp3p--n--ni-': {
        'būna': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'daro': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turi': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'yra': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Plur',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmp3s--n--ni-': {
        'būna': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'daro': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'turi': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        },
        'yra': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Fin'
        }
    },
    'Vgmq2s--n--ni-': {
        'turėdavai': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Aspect': 'Hab',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '2',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgmq3---n--ni-': {
        'būdavo': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Aspect': 'Hab',
            'Mood': 'Ind',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgmq3s--n--ni-': {
        'turėdavo': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Aspect': 'Hab',
            'Mood': 'Ind',
            'Number': 'Sing',
            'Person': '3',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Fin'
        }
    },
    'Vgp--pfnnnnn-p': {
        'darytinos': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'VerbForm': 'Part'
        }
    },
    'Vgpa--nann-n-p': {
        'buvę': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Degree': 'POS',
            'Gender': 'Neut',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpa-pmanngn-p': {
        'buvusių': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Gen',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpa-smanngn-p': {
        'buvusio': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Gen',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpa-smannnn-p': {
        'buvęs': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Act'
        },
        'turėjęs': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpa-smanyin-p': {
        'buvusiuoju': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Ins',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpf-smpnnan-p': {
        'būsimą': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Acc',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpf-smpnndn-p': {
        'būsimam': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Dat',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Fut',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp--npnn-n-p': {
        'esama': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Degree': 'POS',
            'Gender': 'Neut',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp-pfannan-p': {
        'esančias': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Acc',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pfanndn-p': {
        'turinčioms': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Dat',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pfannin-p': {
        'esančiomis': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Ins',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pfpnnan-p': {
        'daromas': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Case': 'Acc',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        },
        'turimas': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Acc',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp-pfpnnin-p': {
        'turimomis': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Ins',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp-pmannan-p': {
        'turinčius': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Acc',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pmanngn-p': {
        'esančių': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Gen',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pmannin-p': {
        'esančiais': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Ins',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pmannnn-p': {
        'esantys': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-pmpnnan-p': {
        'turimus': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Acc',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp-pmpnngn-p': {
        'esamų': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Gen',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp-sfanngn-p': {
        'turinčios': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Gen',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-sfannln-p': {
        'esančioje': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Loc',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-sfannnn-p': {
        'esanti': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-sfpnnnn-p': {
        'daroma': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Fem',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgpp-smanngn-p': {
        'esančio': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Gen',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgpp-smannnn-p': {
        'esantis': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        },
        'esąs': {
            LEMMA: 'būti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        },
        'turintis': {
            LEMMA: 'turėti',
            'POS': 'VERB',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Sing',
            'Polarity': 'POS',
            'Tense': 'Pres',
            'VerbForm': 'Part',
            'Voice': 'Act'
        }
    },
    'Vgps--npnn-n-p': {
        'daryta': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Aspect': 'Perf',
            'Degree': 'POS',
            'Gender': 'Neut',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    },
    'Vgps-pmpnnnn-p': {
        'daryti': {
            LEMMA: 'daryti',
            'POS': 'VERB',
            'Aspect': 'Perf',
            'Case': 'Nom',
            'Degree': 'POS',
            'Gender': 'Masc',
            'Number': 'Plur',
            'Polarity': 'POS',
            'Tense': 'Past',
            'VerbForm': 'Part',
            'Voice': 'Pass'
        }
    }
}


for tag, rules in MORPH_RULES.items():
    for key, attrs in dict(rules).items():
        rules[key.title()] = attrs
