"""
An ASCII system of transliteration for Avestan does not seem to have
been established yet.

TODO: Add tests
TODO: Propose puctuation scheme

"""

from pieltk.converters.general import AsciiConverter

__author__ = ["Caio Geraldes <caio.geraldes@usp.br"]


ASCII_TO_AVESTAN_SCRIPT = [
    # Complex
    (r"a'",         "\U00010B02"),  # 𐬂  AVESTAN LETTER AO
    (r"A'",         "\U00010B03"),  # 𐬃  AVESTAN LETTER AAO
    (r"a~",         "\U00010B04"),  # 𐬄  AVESTAN LETTER AN
    (r"A~",         "\U00010B05"),  # 𐬅  AVESTAN LETTER AAN
    (r"a\.",        "\U00010B06"),  # 𐬆  AVESTAN LETTER AE
    (r"A\.",        "\U00010B07"),  # 𐬇  AVESTAN LETTER AEE
    (r"x'",         "\U00010B12"),  # 𐬒 AVESTAN LETTER XYE
    (r"xv",         "\U00010B13"),  # 𐬓 AVESTAN LETTER XVE
    (r"th",         "\U00010B1A"),  # 𐬚 AVESTAN LETTER THE
    (r"dh",         "\U00010B1C"),  # 𐬜 AVESTAN LETTER DHE
    (r"bh",         "\U00010B21"),  # 𐬡 AVESTAN LETTER BHE
    (r"ngv",        "\U00010B24"),  # 𐬤 AVESTAN LETTER NGVE
    (r"ng'",        "\U00010B23"),  # 𐬣 AVESTAN LETTER NGYE
    (r"ng",         "\U00010B22"),  # 𐬢 AVESTAN LETTER NGE
    (r"n'",         "\U00010B26"),  # 𐬦 AVESTAN LETTER NYE
    (r"gh",         "\U00010B16"),  # 𐬖 AVESTAN LETTER GHE
    (r"sh'",        "\U00010B33"),  # 𐬳 AVESTAN LETTER SHYE
    (r"sh",         "\U00010B31"),  # 𐬱 AVESTAN LETTER SHE
    (r"zh",         "\U00010B32"),  # 𐬲 AVESTAN LETTER ZHE
    (r"Sh",         "\U00010B34"),  # 𐬴 AVESTAN LETTER SSHE
    (r"g'",         "\U00010B15"),  # 𐬕 AVESTAN LETTER GGE

    (r"a",          "\U00010B00"),  # 𐬀  AVESTAN LETTER A
    (r"A",          "\U00010B01"),  # 𐬁  AVESTAN LETTER AA
    (r"e",          "\U00010B08"),  # 𐬈  AVESTAN LETTER E
    (r"E",          "\U00010B09"),  # 𐬉  AVESTAN LETTER EE
    (r"o",          "\U00010B0A"),  # 𐬊  AVESTAN LETTER O
    (r"O",          "\U00010B0B"),  # 𐬋  AVESTAN LETTER OO
    (r"i",          "\U00010B0C"),  # 𐬌  AVESTAN LETTER I
    (r"I",          "\U00010B0D"),  # 𐬍  AVESTAN LETTER II
    (r"u",          "\U00010B0E"),  # 𐬎  AVESTAN LETTER U
    (r"U",          "\U00010B0F"),  # 𐬏  AVESTAN LETTER UU
    (r"k",          "\U00010B10"),  # 𐬐 AVESTAN LETTER KE
    (r"x",          "\U00010B11"),  # 𐬑 AVESTAN LETTER XE
    (r"g",          "\U00010B14"),  # 𐬔 AVESTAN LETTER GE
    (r"G",          "\U00010B15"),  # 𐬕 AVESTAN LETTER GGE
    (r"c",          "\U00010B17"),  # 𐬗 AVESTAN LETTER CE
    (r"j",          "\U00010B18"),  # 𐬘 AVESTAN LETTER JE
    (r"t",          "\U00010B19"),  # 𐬙 AVESTAN LETTER TE
    (r"d",          "\U00010B1B"),  # 𐬛 AVESTAN LETTER DE
    (r"T",          "\U00010B1D"),  # 𐬝 AVESTAN LETTER TTE
    (r"p",          "\U00010B1E"),  # 𐬞 AVESTAN LETTER PE
    (r"f",          "\U00010B1F"),  # 𐬟 AVESTAN LETTER FE
    (r"b",          "\U00010B20"),  # 𐬠 AVESTAN LETTER BE
    (r"n",          "\U00010B25"),  # 𐬥 AVESTAN LETTER NE
    (r"N",          "\U00010B27"),  # 𐬧 AVESTAN LETTER NNE
    (r"m",          "\U00010B28"),  # 𐬨 AVESTAN LETTER ME
    (r"M",          "\U00010B29"),  # 𐬩 AVESTAN LETTER HME
    (r"Y",          "\U00010B2A"),  # 𐬪 AVESTAN LETTER YYE
    (r"y",          "\U00010B2B"),  # 𐬫 AVESTAN LETTER YE
    (r"v",          "\U00010B2C"),  # 𐬬 AVESTAN LETTER VE
    (r"r",          "\U00010B2D"),  # 𐬭 AVESTAN LETTER RE
    (r"l",          "\U00010B2E"),  # 𐬮 AVESTAN LETTER LE
    (r"s",          "\U00010B2F"),  # 𐬯 AVESTAN LETTER SE
    (r"z",          "\U00010B30"),  # 𐬰 AVESTAN LETTER ZE
    (r"h",          "\U00010B35"),  # 𐬵 AVESTAN LETTER HE
    # (r"",       "\U00010B39"), # 𐬹 AVESTAN ABBREVIATION MARK
    # (r"",       "\U00010B3A"), # 𐬺 TINY TWO DOTS OVER ONE DOT PUNCTUATION
    # (r"",       "\U00010B3B"), # 𐬻 SMALL TWO DOTS OVER ONE DOT PUNCTUATION
    # (r"",       "\U00010B3C"), # 𐬼 LARGE TWO DOTS OVER ONE DOT PUNCTUATION
    # (r"",       "\U00010B3D"), # 𐬽 LARGE ONE DOT OVER TWO DOTS PUNCTUATION
    # (r"",       "\U00010B3E"), # 𐬾 LARGE TWO RINGS OVER ONE RING PUNCTUATION
    # (r"",       "\U00010B3F")  # 𐬿 LARGE ONE RING OVER TWO RINGS PUNCTUATION
]


ASCII_TO_AVESTAN_HOFFMAN = [
    # Complex
    (r"a'",         "å"),  # 𐬂  AVESTAN LETTER AOV
    (r"A'",         "ā̊"),  # 𐬃  AVESTAN LETTER AAO
    (r"a~",         "ą"),  # 𐬄  AVESTAN LETTER AN
    (r"A~",         "ą̇"),  # 𐬅  AVESTAN LETTER AAN
    (r"a\.",        "ə"),  # 𐬆  AVESTAN LETTER AE
    (r"A\.",        "ə̄"),  # 𐬇  AVESTAN LETTER AEE
    (r"x'",         "x́"),  # 𐬒 AVESTAN LETTER XYE
    (r"xv",         "xᵛ"),  # 𐬓 AVESTAN LETTER XVE
    (r"th",         "ϑ"),  # 𐬚 AVESTAN LETTER THE
    (r"dh",         "δ"),  # 𐬜 AVESTAN LETTER DHE
    (r"bh",         "β"),  # 𐬡 AVESTAN LETTER BHE
    (r"ngv",        "ŋᵛ"),  # 𐬤 AVESTAN LETTER NGVE
    (r"ng'",        "ŋ́"),  # 𐬣 AVESTAN LETTER NGYE
    (r"ng",         "ŋ"),  # 𐬢 AVESTAN LETTER NGE
    (r"n'",         "ń"),  # 𐬦 AVESTAN LETTER NYE
    (r"gh",         "γ"),  # 𐬖 AVESTAN LETTER GHE
    (r"sh'",        "š́"),  # 𐬳 AVESTAN LETTER SHYE
    (r"sh",         "š"),  # 𐬱 AVESTAN LETTER SHE
    (r"zh",         "ž"),  # 𐬲 AVESTAN LETTER ZHE
    (r"Sh",         "ṣ̌"),  # 𐬴 AVESTAN LETTER SSHE
    (r"g'",         "ġ"),  # 𐬕 AVESTAN LETTER GGE

    (r"A",          "ā"),  # 𐬁  AVESTAN LETTER AA
    (r"E",          "ē"),  # 𐬉  AVESTAN LETTER EE
    (r"O",          "ō"),  # 𐬋  AVESTAN LETTER OO
    (r"I",          "ī"),  # 𐬍  AVESTAN LETTER II
    (r"U",          "ū"),  # 𐬏  AVESTAN LETTER UU
    (r"G",          "ġ"),  # 𐬕 AVESTAN LETTER GGE
    (r"T",          "t̰"),  # 𐬝 AVESTAN LETTER TTE
    (r"N",          "ṇ"),  # 𐬧 AVESTAN LETTER NNE
    (r"M",          "m̨"),  # 𐬩 AVESTAN LETTER HME
    (r"Y",          "ẏ"),  # 𐬪 AVESTAN LETTER YYE
]


class AsciiAvestan(AsciiConverter):
    """
    Replace ASCII notation with an Unicode transliteration scheme for
    Avestan.

    Attributes
    ----------
    scheme : str
        String with the name of the transliteration scheme to be used.

    script_set: list
        List with correspondences to be used in the conversion method.

    Methods
    -------
    __init__(self, scheme)
        Constructs the converter with the transliteration scheme.

        Parameters
        -----------
            scheme : str
                String with the name of the transliteration scheme to be used.
                Options: "script" and "roman-hoffman"

    rules (self)
        Return the conversion rules of the converter

    converter (self, ascii_string)
        Converts a ascii string to the converter's scheme.

        Parameters
        ----------
            ascii_string : str
                String with the text to be converted in ASCII notation.

    >>> from cltk.alphabet.ave.ascii_to_unicode import AsciiConverter
    >>> ascii_replace = AsciiConverter()
    >>> string = "ahiiA. yAsA na.manghA. ustAnazastO."
    >>> ascii_replace.converter(string)
    """

    def __init__(self, scheme="script"):
        super().__init__(scheme)
        if scheme == "roman-hoffman":
            self.scheme = "roman-hoffman"
            self.script_set = ASCII_TO_AVESTAN_HOFFMAN
        else:
            self.scheme = "script"
            self.script_set = ASCII_TO_AVESTAN_SCRIPT


if __name__ == "__main__":
    ascii_replace = AsciiAvestan()
    STRING = "ahiiA. yAsA na.manghA. ustAnazastO."
    print(ascii_replace.converter(STRING))
    ascii_replace = AsciiAvestan("roman-hoffman")
    print(ascii_replace.converter(STRING))
