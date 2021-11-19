import pytest

def test_long_text(et_tokenizer):
    # Excerpt: European Convention on Human Rights
    text = """
Konventsioonile allakirjutanud Euroopa Nõukogu liikmesriikide
valitsused,
arvestades inimõiguste ülddeklaratsiooni, mille kuulutas
välja Ühinenud Rahvaste Organisatsiooni Peaassamblee
10. detsembril 1948;
arvestades, et nimetatud deklaratsiooni eesmärk on tagada selles
kuulutatud õiguste üldine ja tõhus tunnustamine ning järgimine;
arvestades, et Euroopa Nõukogu eesmärk on saavutada tema
liikmete suurem ühtsus ning et üheks selle eesmärgi saavutamise
vahendiks on inimõiguste ja põhivabaduste järgimine ning
elluviimine;
taaskinnitades oma sügavat usku neisse põhivabadustesse, mis
on õigluse ja rahu aluseks maailmas ning mida kõige paremini
tagab ühelt poolt tõhus poliitiline demokraatia ning teiselt poolt
inimõiguste, millest nad sõltuvad, üldine mõistmine ja järgimine;
"""
    tokens = et_tokenizer(text)
    assert len(tokens) == 122