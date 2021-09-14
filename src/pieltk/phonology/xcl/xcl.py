"""
Classical Armenian Phonology. Sources:
- `<https://www.unicode.org/charts/PDF/U0530.pdf>`_
- Macack, Martin (2017) The phonology of Classical Armenian in Klein, Joseph
  and Friz. (2017) Handbook of Comparative and Historical Linguistics, 41.2.

"""

__author__ = ["Caio Geraldes <caio.geraldes@usp.br>"]


MONOPHTONGS = [
    "\u0561",  # a
    "\u0565",  # e
    "\u0568",  # schwa
    "\u056B",  # i
    "\u0578",  # o
    "\u0585"  # o:
]

DIPHTONGS = [
    "\u0567",        # ey
    "\u0578\u0575",   # oy
    "\u0561\u0575",  # ay
    "\u0561\u0582",  # aw
    "\u0565\u0582",  # ew
    "\u056B\u0582",  # iw
    "\u0565\u0561",  # ea


]

GLIDES = [
    "\u0575",  # yod
    "\u0582",  # waw
    "\u057E",  # v
]


STOPS = [
    "\u0562",  # b
    "\u0563",  # g
    "\u0564",  # d
    "\u0569",  # th
    "\u056F",  # k
    "\u057A",  # p
    "\u057F",  # t
    "\u0583",  # ph
    "\u0584",  # kh
]

LIQUIDS = [
    "\u056C",  # l
    "\u0572",  # ł
    "\u0580",  # R
    "\u057C",  # r
]

AFFRICATES = [
    "\u056E",  # ts
    "\u0571",  # dz
    "\u0573",  # ճ ARMENIAN SMALL LETTER CHEH
    "\u0579",  # չ ARMENIAN SMALL LETTER CHA
    "\u057B",  # ջ ARMENIAN SMALL LETTER JHEH
    "\u0581",  # c'
]

FRICATIVES = [
    "\u057D",  # s
    "\u0566",  # z
    "\u056A",  # zh
    "\u056D",  # xh
    "\u0570",  # h
    "\u0577",  # sh
    "\u0586"  # f
]


NASALS = [
    "\u0574",  # m
    "\u0576",  # n
]


CONSONANTS_LOWER = STOPS +\
        AFFRICATES +\
        FRICATIVES +\
        LIQUIDS +\
        GLIDES +\
        NASALS

CONSONANTS = CONSONANTS_LOWER + [x.upper() for x in CONSONANTS_LOWER]

RESONANTS_LOWER = NASALS + LIQUIDS + GLIDES
RESONANTS = RESONANTS_LOWER + [x.upper() for x in RESONANTS_LOWER]

VOWELS_LOWER = MONOPHTONGS + DIPHTONGS
VOWELS = VOWELS_LOWER + [x.upper() for x in VOWELS_LOWER]
