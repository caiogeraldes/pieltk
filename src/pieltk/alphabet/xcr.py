"""The Carian alphabet. Sources:

- `<https://www.unicode.org/charts/PDF/U102A0.pdf>`
- Adiego, Ignacio, J. (2007) The Carian Language

"""

__author__ = [
    "Caio Geraldes <caio.geraldes@usp.br>"]

VOWELS = [
    "\U000102A0",  # 𐊠 CARIAN LETTER A
    "\U000102A7",  # 𐊧 CARIAN LETTER A2
    "\U000102AB",  # 𐊫 CARIAN LETTER O
    "\U000102B2",  # 𐊲 CARIAN LETTER U
    "\U000102B9",  # 𐊹 CARIAN LETTER I
    "\U000102BA",  # 𐊺 CARIAN LETTER E
    "\U000102BF",  # 𐊿 CARIAN LETTER UU
    "\U000102C5",  # 𐋅 CARIAN LETTER II
    "\U000102C8",  # 𐋈 CARIAN LETTER UUU2
    "\U000102CF",  # 𐋏 CARIAN LETTER E2
    "\U000102D0",  # 𐋐 CARIAN LETTER UUU3

]

CONSONANTS = [
    "\U000102A1",  # 𐊡 CARIAN LETTER P2
    "\U000102A2",  # 𐊢 CARIAN LETTER D
    "\U000102A3",  # 𐊣 CARIAN LETTER L
    "\U000102A4",  # 𐊤 CARIAN LETTER UUU
    "\U000102A5",  # 𐊥 CARIAN LETTER R
    "\U000102A6",  # 𐊦 CARIAN LETTER LD
    "\U000102A8",  # 𐊨 CARIAN LETTER Q
    "\U000102A9",  # 𐊩 CARIAN LETTER B
    "\U000102AA",  # 𐊪 CARIAN LETTER M
    "\U000102AC",  # 𐊬 CARIAN LETTER D2
    "\U000102AD",  # 𐊭 CARIAN LETTER T
    "\U000102AE",  # 𐊮 CARIAN LETTER SH
    "\U000102AF",  # 𐊯 CARIAN LETTER SH2
    "\U000102B0",  # 𐊰 CARIAN LETTER S
    "\U000102B1",  # 𐊱 CARIAN LETTER C-18
    "\U000102B3",  # 𐊳 CARIAN LETTER NN
    "\U000102B4",  # 𐊴 CARIAN LETTER X
    "\U000102B5",  # 𐊵 CARIAN LETTER N
    "\U000102B6",  # 𐊶 CARIAN LETTER TT2
    "\U000102B7",  # 𐊷 CARIAN LETTER P
    "\U000102B8",  # 𐊸 CARIAN LETTER SS
    "\U000102BB",  # 𐊻 CARIAN LETTER UUUU
    "\U000102BC",  # 𐊼 CARIAN LETTER K
    "\U000102BD",  # 𐊽 CARIAN LETTER K2
    "\U000102BE",  # 𐊾 CARIAN LETTER ND
    "\U000102C0",  # 𐋀 CARIAN LETTER G
    "\U000102C1",  # 𐋁 CARIAN LETTER G2
    "\U000102C2",  # 𐋂 CARIAN LETTER ST
    "\U000102C3",  # 𐋃 CARIAN LETTER ST2
    "\U000102C4",  # 𐋄 CARIAN LETTER NG
    "\U000102C6",  # 𐋆 CARIAN LETTER C-39
    "\U000102C7",  # 𐋇 CARIAN LETTER TT
    "\U000102C9",  # 𐋉 CARIAN LETTER RR
    "\U000102CA",  # 𐋊 CARIAN LETTER MB
    "\U000102CB",  # 𐋋 CARIAN LETTER MB2
    "\U000102CC",  # 𐋌 CARIAN LETTER MB3
    "\U000102CD",  # 𐋍 CARIAN LETTER MB4
    "\U000102CE",  # 𐋎 CARIAN LETTER LD2
]

# The i and r used at Hyllarima are not represented as a glyph
# of their own yet.
HYLLARIMA = [
    "\U000102A0",  # 𐊠 a
    "\U000102A2",  # 𐊢 d
    "\U000102A3",  # 𐊣 l
    "\U000102A4",  # 𐊤 y
    "\U000102A5",  # 𐊥 r
    "\U000102CE",  # 𐋎 λ
    "\U000102A8",  # 𐊨 q
    "\U000102A9",  # 𐊩 b
    "\U000102AA",  # 𐊪 m
    "\U000102AB",  # 𐊫 o
    "\U000102AD",  # 𐊭 t
    "\U000102AE",  # 𐊮 sh
    "\U000102B0",  # 𐊰 s
    "\U000102B2",  # 𐊲 u
    "\U000102B3",  # 𐊳 ñ
    "\U000102B5",  # 𐊵 n
    "\U000102B7",  # 𐊷 p
    "\U000102B8",  # 𐊸 ś
    "\U000102B9",  # 𐊹 i
    "\U000102CF",  # 𐋏 e
    "\U000102BD",  # 𐊽 k
    "\U000102BE",  # 𐊾 δ
    "\U000102C3",  # 𐋃 z
    "\U000102C7",  # 𐋇 τ
]

# The q and r used at Euromos are not represented as a glyph of their own yet.
EUROMOS = [
    "\U000102A0",  # 𐊠 a
    "\U000102A2",  # 𐊢 d
    "\U000102A3",  # 𐊣 l
    "\U000102A4",  # 𐊤 y
    "\U000102A5",  # 𐊥 r
    "\U000102CE",  # 𐋎 λ
    "\U000102A8",  # 𐊨 q
    "\U000102A9",  # 𐊩 b
    "\U000102AA",  # 𐊪 m
    "\U000102AB",  # 𐊫 o
    "\U000102AD",  # 𐊭 t
    "\U000102B0",  # 𐊰 s
    "\U000102B2",  # 𐊲 u
    "\U000102B4",  # 𐊴 ḱ
    "\U000102B5",  # 𐊵 n
    "\U000102B8",  # 𐊸 ś
    "\U000102B9",  # 𐊹 i
    "\U000102CF",  # 𐋏 e
    "\U000102BD",  # 𐊽 k
    "\U000102BC",  # 𐊼 k2
    "\U000102BE",  # 𐊾 δ
    "\U000102C3",  # 𐋃 z
]

# The β, i, q and z used at Mylasa are not represented as a glyph
# of their own yet.
MYLASA = [
    "\U000102A0",  # 𐊠 a
    "\U000102A2",  # 𐊢 d
    "\U000102A3",  # 𐊣 l
    "\U000102D0",  # 𐋐 y
    "\U000102A5",  # 𐊥 r
    "\U000102A8",  # 𐊨 q
    "\U000102A9",  # 𐊩 b
    "\U000102AA",  # 𐊪 m
    "\U000102AB",  # 𐊫 o
    "\U000102AD",  # 𐊭 t
    "\U000102AE",  # 𐊮 sh
    "\U000102B0",  # 𐊰 s
    "\U000102B2",  # 𐊲 u
    "\U000102B4",  # 𐊴 ḱ
    "\U000102B5",  # 𐊵 n
    "\U000102B7",  # 𐊷 p
    "\U000102B8",  # 𐊸 ś
    "\U000102B9",  # 𐊹 i
    "\U000102CF",  # 𐋏 e
    "\U000102BD",  # 𐊽 k
    "\U000102BE",  # 𐊾 δ
    "\U000102C3",  # 𐋃 z
]


# The ḱ and β used at Stratonikeia are not represented as a glyph
# of their own yet.
STRATONIKEIA = [
    "\U000102A0",  # 𐊠 a
    "\U000102A2",  # 𐊢 d
    "\U000102A3",  # 𐊣 l
    "\U000102A4",  # 𐊤 y
    "\U000102A5",  # 𐊥 r
    "\U000102A6",  # 𐊦 λ
    "\U000102A8",  # 𐊨 q
    "\U000102AA",  # 𐊪 m
    "\U000102AB",  # 𐊫 o
    "\U000102AD",  # 𐊭 t
    "\U000102AE",  # 𐊮 sh
    "\U000102B0",  # 𐊰 s
    "\U000102B1",  # 𐊱 ?
    "\U000102B2",  # 𐊲 u
    "\U000102B3",  # 𐊳 ñ
    "\U000102B4",  # 𐊴 ḱ
    "\U000102B5",  # 𐊵 n
    "\U000102B7",  # 𐊷 p
    "\U000102B8",  # 𐊸 ś
    "\U000102B9",  # 𐊹 i
    "\U000102BA",  # 𐊺 e
    "\U000102BD",  # 𐊽 k
    "\U000102BE",  # 𐊾 δ
    "\U000102C3",  # 𐋃 z
]


# The a used at Sinuri-Kildara is not represented as a glyph of its own yet.
SINURI_KILDARA = [
    "\U000102A0",  # 𐊠 a
    "\U000102A2",  # 𐊢 d
    "\U000102A3",  # 𐊣 l
    "\U000102D0",  # 𐋐 y
    "\U000102A5",  # 𐊥 r
    "\U000102A6",  # 𐊦 λ
    "\U000102A8",  # 𐊨 q
    "\U000102A9",  # 𐊩 b
    "\U000102AA",  # 𐊪 m
    "\U000102AB",  # 𐊫 o
    "\U000102AD",  # 𐊭 t
    "\U000102AE",  # 𐊮 sh
    "\U000102B0",  # 𐊰 s
    "\U000102B1",  # 𐊱 ?
    "\U000102B2",  # 𐊲 u
    "\U000102B3",  # 𐊳 ñ
    "\U000102B4",  # 𐊴 ḱ
    "\U000102B5",  # 𐊵 n
    "\U000102B7",  # 𐊷 p
    "\U000102B8",  # 𐊸 ś
    "\U000102B9",  # 𐊹 i
    "\U000102BA",  # 𐊺 e
    "\U000102BC",  # 𐊼 k
    "\U000102BE",  # 𐊾 δ
    "\U000102C3",  # 𐋃 z
    "\U000102C4",  # 𐋄 ŋ?
]

# TODO: Kaunos, C.series, Memphis
