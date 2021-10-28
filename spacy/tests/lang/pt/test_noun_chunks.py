from spacy.tokens import Doc
import pytest


# fmt: off
@pytest.mark.parametrize(
    "words,heads,deps,pos,chunk_offsets",
    [
        # um cachorro -> "um cachorro"   determiner + noun
        (
            ["um", "cachorro"],
            [1, 1],
            ["det", "ROOT"],
            ["DET", "NOUN"],
            [(0, 2)],
        ),
        # meu o pai -> "meu o pai"   two determiners + noun
        (
            ["meu", "o", "pai"],
            [2, 2, 2],
            ["det", "det", "ROOT"],
            ["DET", "DET", "NOUN"],
            [(0, 3)],
        ),
        # todos essos caros -> "todos essos caros"   two determiners + noun
        (
            ["todos", "essos", "caros"],
            [2, 2, 2],
            ["det", "det", "ROOT"],
            ["DET", "DET", "NOUN"],
            [(0, 3)],
        ),
        # um irmão meu -> "um irmão meu"   two determiners, one is after noun
        (
            ["um", "irmão", "meu"],
            [1, 1, 1],
            ["det", "ROOT", "det"],
            ["DET", "NOUN", "DET"],
            [(0, 3)],
        ),
        # o meu pai -> "o meu pai"   two determiners + noun
        (
            ["o", "meu", "pai"],
            [2, 2, 2],
            ["det","det", "ROOT"],
            ["DET", "DET", "NOUN"],
            [(0, 3)],
        ),
        #  A bicicleta essa está estragada -> A bicicleta    relative pronoun
        (
            ['A', 'bicicleta', 'essa', 'está', 'estragada'],
            [1, 4, 1, 4, 4],
            ['det', 'nsubj', 'det', 'cop', 'ROOT'],
            ['DET', 'NOUN', 'PRON', 'AUX', 'ADJ'],
            [(0,2)]
        ),
        #  o computador que comprou -> o computador    relative subclause
        (
            ['o', 'computador', 'que', 'comprou'],
            [1, 1, 3, 1],
            ['det', 'ROOT', 'nsubj', 'acl:relcl'],
            ['DET', 'NOUN', 'PRON', 'VERB'],
            [(0, 2), (2, 3)]
        ),
        # O cachorro marrom  -> "O cachorro marrom "  det + noun + adj
        (
            ["O", "cachorro", "marrom"],
            [1, 1, 1],
            ["det", "ROOT", "amod"],
            ["DET", "NOUN", "ADJ"],
            [(0, 3)],
        ),
        # As calças baratas  -> "As calças baratas "  det + noun + adj plural
        (
            ["As", "calças", "baratas"],
            [1, 1, 1],
            ["det", "ROOT", "amod"],
            ["DET", "NOUN", "ADJ"],
            [(0, 3)],
        ),
        # Uma boa ideia -> Uma boa ideia       det + adj + noun
        (
            ['uma', 'boa', 'ideia'],
            [2, 2, 2],
            ["det", "amod", "ROOT"],
            ["DET", "ADJ", "NOUN"],
            [(0,3)]
        ),
        # Uma garota esperta e inteligente -> Uma garota esperta e inteligente  multiple adjectives
        (
            ["Uma", "garota", "esperta", "e", "inteligente"],
            [1, 1, 1, 4, 2],
            ["det", "ROOT", "amod", "cc", "conj"],
            ["DET", "NOUN", "ADJ", "CCONJ", "ADJ"],
            [(0,5)]
        ),
        # Eu tenho um cachorro e um gato  -> um cacharo, um gato        Two NPs conjuncted
        ( 
            ["Eu", "tenho", "um", "cachorro", "e", "um", "gato"],
            [0, 2, 0, 5, 5, 0],
            ["ROOT", "det", "obj", "cc", "det", "conj"],
            ["VERB", "DET", "NOUN", "CCONJ", "DET", "NOUN"],
            [(1,3), (4,6)]
         
        ),
        # Dom Pedro II -> Dom Pedro II              Noun compound, person name and titles
        (
            ["Dom", "Pedro", "II"],
            [0, 0, 0],
            ["ROOT", "flat:name", "flat:name"],
            ["PROPN", "PROPN", "PROPN"],
            [(0,3)]
        ),
        # os Estados Unidos -> os Estados Unidos     Noun compound created by flat
        (
            ["os", "Estados", "Unidos"],
            [1, 1, 1],
            ["det", "ROOT", "flat:name"],
            ["DET", "PROPN", "PROPN"],
            [(0,3)]
        ),
        # a destruição da cidade -> a destruição, cidade
        (
            ['a', 'destruição', 'da', 'cidade'],
            [1, 1, 3, 1],
            ['det', 'ROOT', 'case', 'nmod'],
            ['DET', 'NOUN', 'ADP', 'NOUN'],
            [(0,2), (3,4)]
        ),
        # a primeira fábrica de medicamentos do governo -> a primeira fábrica, medicamentos, governo  Compounding by nmod, several NPs chained together
        (
            ["a primeira fábrica", "medicamentos", "governo"],
            [2, 2, 2, 4, 2, 6, 2],
            ['det', 'amod', 'ROOT', 'case', 'nmod', 'case', 'nmod',
            ['DET', 'ADJ', 'NOUN', 'ADP', 'NOUN', 'ADP', 'NOUN'],
            [(0, 3), (4, 5), (6, 7)]
        ),
        # Tradução da reportagem de Susana -> Tradução, reportagem, Susana   several NPs
        (
            ['Tradução', 'da', 'reportagem', 'de', 'Susana'],
            [0, 2, 0, 4, 2],
            ['ROOT', 'case', 'nmod', 'case', 'nmod'],
            ['NOUN', 'ADP', 'NOUN', 'ADP', 'PROPN'],
            [(0,1), (2,3), (4,5)]  
       
        ),
        # O gato gordo da Susana e seu amigo -> O gato gordo, Susana, seu amigo    several NPs
        (  
            ['O', 'gato', 'gordo', 'da', 'Susana', 'e', 'seu', 'amigo'],
            [1, 1, 1, 4, 1, 7, 7, 1],
            ['det', 'ROOT', 'amod', 'case', 'nmod', 'cc', 'det', 'conj'],
            ['DET', 'NOUN', 'ADJ', 'ADP', 'PROPN', 'CCONJ', 'DET', 'NOUN'],
            [(0,3), (4,5), (6,8)]
        ),
        # 
        (
        ),
        # 
        (
        ),
        # 
        (
        ),
        # 
        (
        ),
    ],
)
# fmt: on
def test_pt_noun_chunks(pt_vocab, words, heads, deps, pos, chunk_offsets):
    doc = Doc(pt_vocab, words=words, heads=heads, deps=deps, pos=pos)
    assert [(c.start, c.end) for c in doc.noun_chunks] == chunk_offsets


def test_noun_chunks_is_parsed_pt(pt_tokenizer):
    """Test that noun_chunks raises Value Error for 'pt' language if Doc is not parsed."""
    doc = pt_tokenizer("en Oxford este verano")
    with pytest.raises(ValueError):
        list(doc.noun_chunks)

