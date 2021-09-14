"""
Implements a general class for AsciiConverters.
"""

from typing import Tuple, List
import re


class AsciiConverter:
    """
    Replace ASCII notation with an Unicode transliteration scheme.

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

    rules (self)
        Return the conversion rules of the converter

    converter (self, ascii_string)
        Converts a ascii string to the converter's scheme.

        Parameters
        ----------
            ascii_string : str
                String with the text to be converted in ASCII notation.
    """

    def __init__(self, scheme: str):
        self.scheme = scheme
        self.script_set: List[Tuple[str, str]] = []

    def converter(self, ascii_text):
        """
        Covert ascii_text to unicode text according to the rules of self.
        """
        output = ascii_text

        for pair in self.script_set:
            output = re.sub(pair[0], pair[1], output)
        return output

    @property
    def rules(self):
        """
        Return the conversion rules of the converter
        """
        return self.script_set


AEGEAN_NUMERALS = [
    (r"1(\d\d\d\d)", r"𐄫\1"),
    (r"2(\d\d\d\d)", r"𐄬\1"),
    (r"3(\d\d\d\d)", r"𐄭\1"),
    (r"4(\d\d\d\d)", r"𐄮\1"),
    (r"5(\d\d\d\d)", r"𐄯\1"),
    (r"6(\d\d\d\d)", r"𐄰\1"),
    (r"7(\d\d\d\d)", r"𐄱\1"),
    (r"8(\d\d\d\d)", r"𐄲\1"),
    (r"9(\d\d\d\d)", r"𐄳\1"),
    (r"1(\d\d\d)", r"𐄢\1"),
    (r"2(\d\d\d)", r"𐄣\1"),
    (r"3(\d\d\d)", r"𐄤\1"),
    (r"4(\d\d\d)", r"𐄥\1"),
    (r"5(\d\d\d)", r"𐄦\1"),
    (r"6(\d\d\d)", r"𐄧\1"),
    (r"7(\d\d\d)", r"𐄨\1"),
    (r"8(\d\d\d)", r"𐄩\1"),
    (r"9(\d\d\d)", r"𐄪\1"),

    (r"1(\d\d)", r"𐄙\1"),
    (r"2(\d\d)", r"𐄚\1"),
    (r"3(\d\d)", r"𐄛\1"),
    (r"4(\d\d)", r"𐄜\1"),
    (r"5(\d\d)", r"𐄝\1"),
    (r"6(\d\d)", r"𐄞\1"),
    (r"7(\d\d)", r"𐄟\1"),
    (r"8(\d\d)", r"𐄠\1"),
    (r"9(\d\d)", r"𐄡\1"),

    (r"1(\d)", r"𐄐\1"),
    (r"2(\d)", r"𐄑\1"),
    (r"3(\d)", r"𐄒\1"),
    (r"4(\d)", r"𐄓\1"),
    (r"5(\d)", r"𐄔\1"),
    (r"6(\d)", r"𐄕\1"),
    (r"7(\d)", r"𐄖\1"),
    (r"8(\d)", r"𐄗\1"),
    (r"9(\d)", r"𐄘\1"),
    (r"0", r""),
    (r"1", r"𐄇"),
    (r"2", r"𐄈"),
    (r"3", r"𐄉"),
    (r"4", r"𐄊"),
    (r"5", r"𐄋"),
    (r"6", r"𐄌"),
    (r"7", r"𐄍"),
    (r"8", r"𐄎"),
    (r"9", r"𐄏"),
    (r"V", r"𐄾"),
    (r"M", r"𐄸"),
    (r"N", r"𐄹"),
    (r"T", r"𐄼"),
    (r"P", r"𐄺"),
    (r"Q", r"𐄻"),
    (r"L", r"𐄷"),
    (r"S", r"𐄽"),
    (r"Z", r"𐄿")]
