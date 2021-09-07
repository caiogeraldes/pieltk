import re

ASCII_TO_CARIAN_SCRIPT = (
    (r"a", "𐊠"),
    (r"e2", "𐋏"),
    (r"r2", "𐋉"),
    (r"z2", "𐋂"),
    (r"l", "𐊣"),
    (r"y3", "𐋈"),
    (r"y2", "𐋐"),
    (r"y'", "𐊻"),
    (r"y", "𐊤"),
    (r"r", "𐊥"),
    (r"L2", "𐋎"),
    (r"L", "𐊦"),
    (r"A2", "𐊧"),
    (r"q", "𐊨"),
    (r"o", "𐊫"),
    (r"D2", "𐊬"),
    (r"t", "𐊭"),
    (r"sh2", "𐊯"),
    (r"sh", "𐊮"),
    (r"s'", "𐊸"),
    (r"s", "𐊰"),
    (r"18", "𐊱"),
    (r"u", "𐊲"),
    (r"N", "𐊳"),
    (r"c", "𐊴"),
    (r"T2", "𐊶"),
    (r"p", "𐊷"),
    (r"i", "𐊹"),
    (r"e", "𐊺"),
    (r"k2", "𐊽"),
    (r"k", "𐊼"),
    (r"dh", "𐊾"),
    (r"d", "𐊢"),
    (r"w", "𐊿"),
    (r"G2", "𐋁"),
    (r"G", "𐋀"),
    (r"z", "𐋃"),
    (r"ng", "𐋄"),
    (r"n", "𐊵"),
    (r"j", "𐋅"),
    (r"39", "𐋆"),
    (r"T", "𐋇"),
    (r"mb2", "𐋋"),
    (r"mb3", "𐋌"),
    (r"mb4", "𐋍"),
    (r"mb", "𐋊"),
    (r"b'", "𐊡"),
    (r"b", "𐊩"),
    (r"m", "𐊪"),
)


class AsciiConverter:
    """
    Replace ASCII notation with an Unicode transliteration scheme for
    Carian.

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

    converter (self, ascii_string)
        Converts a ascii string to the converter's scheme.

        Parameters
        ----------
            ascii_string : str
                String with the text to be converted in ASCII notation.

    >>> carian = AsciiConverter()
    >>> string = "s'jas: san tur"
    >>> carian.converter(string)
    "𐊸𐋅𐊠𐊰: 𐊰𐊠𐊵 𐊭𐊲𐊥"
    """

    def __init__(self, scheme="script"):
        self.scheme = "script"
        self.script_set = ASCII_TO_CARIAN_SCRIPT

    def converter(self, ascii_text):
        output = ascii_text

        for pair in self.script_set:
            output = re.sub(pair[0], pair[1], output)
        return output


if __name__ == "__main__":
    carian = AsciiConverter()
    string = "s'jas: san tur"
    print(carian.converter(string))
