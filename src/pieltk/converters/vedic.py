"""
Implements Devanagari converters.
"""

import re
from typing import Tuple, List
from pieltk.converters.general import AsciiConverter

ASCII_HK_TO_DEVA = [
    (r"([\n ]|^)ai", r"\1ऐ"),
    (r"([\n ]|^)au", r"\1औ"),
    (r"([\n ]|^)a", r"\1अ"),
    (r"([\n ]|^)A", r"\1आ"),
    (r"([\n ]|^)i", r"\1इ"),
    (r"([\n ]|^)I", r"\1ई"),
    (r"([\n ]|^)u", r"\1उ"),
    (r"([\n ]|^)U", r"\1ऊ"),
    (r"([\n ]|^)e", r"\1ए"),
    (r"([\n ]|^)o", r"\1ओ"),
    (r"([\n ]|^)lR", r"\1लृ"),
    (r"([\n ]|^)lRR", r"\1लॄ"),
    (r"([\n ]|^)RR", r"\1ॠ"),
    (r"([\n ]|^)R", r"\1ऋ"),
    (r"ai", "V ै ै"),
    (r"au", "V ौ"),
    (r"a", "V "),
    (r"A", "V ा"),
    (r"i", "V ि"),
    (r"I", "V ी"),
    (r"u", "V ु"),
    (r"U", "V ू"),
    (r"e", "V े"),
    (r"o", "V ो"),
    (r"lRR", "V ॣ"),
    (r"lR", "V ॢ"),
    (r"RR", "V ॄ"),
    (r"R", "V ृ"),
    (r"khV ", "ख"),
    (r"ghV ", "घ"),
    (r"chV ", "छ"),
    (r"jhV ", "झ"),
    (r"ThV ", "ठ"),
    (r"DhV ", "ढ"),
    (r"thV ", "थ"),
    (r"dhV ", "ध"),
    (r"phV ", "फ"),
    (r"bhV ", "भ"),
    (r"kV ", "क"),
    (r"gV ", "ग"),
    (r"GV ", "ङ"),
    (r"cV ", "च"),
    (r"jV ", "ज"),
    (r"JV ", "ञ"),
    (r"TV ", "ट"),
    (r"DV ", "ड"),
    (r"NV ", "ण"),
    (r"tV ", "त"),
    (r"dV ", "द"),
    (r"nV ", "न"),
    (r"pV ", "प"),
    (r"bV ", "ब"),
    (r"mV ", "म"),
    (r"yV ", "य"),
    (r"rV ", "र"),
    (r"lV ", "ल"),
    (r"vV ", "व"),
    (r"zV ", "श"),
    (r"SV ", "ष"),
    (r"sV ", "स"),
    (r"LLV ", "ऴ"),
    (r"LV ", "ळ"),
    (r"hV ", "ह"),
    (r"kh", "ख्"),
    (r"gh", "घ्"),
    (r"ch", "छ्"),
    (r"jh", "झ्"),
    (r"Th", "ठ्"),
    (r"Dh", "ढ्"),
    (r"th", "थ्"),
    (r"dh", "ध्"),
    (r"ph", "फ्"),
    (r"bh", "भ्"),
    (r"k", "क्"),
    (r"g", "ग्"),
    (r"G", "ङ्"),
    (r"c", "च्"),
    (r"j", "ज्"),
    (r"J", "ञ्"),
    (r"T", "ट्"),
    (r"D", "ड्"),
    (r"N", "ण्"),
    (r"t", "त्"),
    (r"d", "द्"),
    (r"n", "न्"),
    (r"p", "प्"),
    (r"b", "ब्"),
    (r"m", "म्"),
    (r"y", "य्"),
    (r"r", "र्"),
    (r"l", "ल्"),
    (r"v", "व्"),
    (r"z", "श्"),
    (r"S", "ष्"),
    (r"s", "स्"),
    (r"LL", "ऴ्"),
    (r"L", "ळ्"),
    (r"h", "ह्"),

    (r"M", "\u0902"),
    (r"H", "\u0903"),
    (r"\\", "\u0951"),
    (r"=", "\u0952"),
    (r"&", "\u0901"),
    (r"'", "ऽ"),

    (r"V ", " "),

    (r"1", "१"),
    (r"2", "२"),
    (r"3", "३"),
    (r"4", "४"),
    (r"5", "५"),
    (r"6", "६"),
    (r"7", "७"),
    (r"8", "८"),
    (r"9", "९"),
    (r"0", "०"),

    (r"\|\|", "॥"),
    (r"\|", "।"),

    (r"(\u094d)[\u0951\u0952]\\", r"\1"),
    (r"\/[\u0951\u0952]", r""),
]


ASCII_HK_TO_IAST = [
    (r"A", "ā"),
    (r"I", "ī"),
    (r"U", "ū"),
    (r"lRR", "ḹ"),
    (r"lR", "ḷ"),
    (r"RR", "ṝ"),
    (r"R", "ṛ"),
    (r"T", "ṭ"),
    (r"D", "ḍ"),
    (r"G", "ṅ"),
    (r"J", "ñ"),
    (r"N", "ṇ"),
    (r"z", "ś"),
    (r"S", "ṣ"),
    (r"L", "l̠"),
    (r"\\", "\u0300"),
    (r"/", "\u0301"),
    (r"MM", "ṁ"),
    (r"M", "ṃ"),
    (r"H", "ḥ"),
    (r"&", "m̐")
]

ASCII_HK_TO_ISO = [
    (r"A", "ā"),
    (r"I", "ī"),
    (r"U", "ū"),
    (r"e", "ē"),
    (r"o", "ō"),
    (r"lRR", "l̥̄"),
    (r"lR", "l̥"),
    (r"RR", "r̥̄"),
    (r"R", "r̥"),
    (r"T", "ṭ"),
    (r"D", "ḍ"),
    (r"G", "ṅ"),
    (r"J", "ñ"),
    (r"N", "ṇ"),
    (r"z", "ś"),
    (r"S", "ṣ"),
    (r"L", "ḷ"),

    (r"MM", "ṃ"),
    (r"M", "ṁ"),
    (r"H", "ḥ"),
    (r"\\", "\u0300"),
    (r"/", "\u0301"),
    (r"&", "m̐")
]


def hk_ud_to_hk_anu(hk_ud_str):
    """
    Converts HK entry with marked udattas to HK text with marked
    anudattas and svaritas.
    """
    hk_syllab = hk_to_syllables(hk_ud_str)
    hk_acc = hk_accentuation(hk_syllab)

    hk_syllab_array = hk_syllab.split(".")
    hk_anu_acc = list(ud_to_anu(hk_acc))

    hk_anu_str = map(anudatta_apply, hk_anu_acc, hk_syllab_array)

    return "".join(list(hk_anu_str))


def anudatta_apply(accent, syllabe):
    """
    Apply the accentuation with anudatta and svarita to syllable.
    """
    out_syllab = ""
    if accent == "A":
        out_syllab = syllabe + "="
    elif accent == "S":
        out_syllab = syllabe + "\\"
    else:
        out_syllab = syllabe.replace("/", "")
    return out_syllab


def hk_to_syllables(hk_str):
    """
    Split syllables from HK entry.
    """
    hk_syllab = hk_str
    hk_syllab = re.sub(r"([aeiouAEIOUR])", r"\1.", hk_syllab)
    hk_syllab = re.sub(r"a\.([ui])\.", r"a\1.", hk_syllab)
    hk_syllab = re.sub(r"\.\/", r"/.", hk_syllab)
    hk_syllab = re.sub(r"\.([HM&])", r"\1.", hk_syllab)
    hk_syllab = re.sub(r"R\.R", r"RR", hk_syllab)

    hk_syllab = re.sub(r"\.$", "", hk_syllab)

    return hk_syllab


def hk_accentuation(hk_syllab):
    """
    Map accentuation of HK entry.
    """
    hk_acc = []
    hk_syllab_list = hk_syllab.split(".")

    for syllabe in hk_syllab_list:
        if "/" in syllabe:
            hk_acc.append("U")
        else:
            hk_acc.append("B")
    return "".join(hk_acc)


def ud_to_anu(ud_str):
    """
     Converts a string of udatta marked syllables to
     an anudatta marked one. Notation:
     U = udatta
     A = anudatta
     S = svarita
     B = unmarked in udatta notation
     D = unmarked in anudatta notation

     Example:
     >>> ud_to_anu('BBUBBUUB')
     "AADSADDS"
    """

    anu_str = ud_str

    anu_str = re.sub(r"BU",  "AU", anu_str)
    anu_str = re.sub(r"UB",  "US", anu_str)
    anu_str = re.sub(r"U",   "D", anu_str)

    while ("BA" in anu_str or "BD" in anu_str):
        anu_str = re.sub(r"^(B*)[BD](A)",    r"\1A\2", anu_str)
        anu_str = re.sub(r"\n(B*)[BD](A)",   r"\1A\2", anu_str)
        anu_str = re.sub(r"([ADSB])B([AD])", r"\1D\2", anu_str)
        anu_str = re.sub(r"B$", "D", anu_str)

    return anu_str


class AsciiDevanagari(AsciiConverter):
    """
    Implement ASCII to Unicode Devanagari converter with given schemes.
    """
    def __init__(self, scheme: str = "hk_to_deva", udatta_to_anudatta: bool = True):
        super().__init__(scheme)
        self.udata_to_anudatta = udatta_to_anudatta
        if scheme == "hk_to_deva":
            self.scheme = "hk_to_deva"
            self.script_set: List[Tuple[str, str]] = ASCII_HK_TO_DEVA
        elif scheme == "hk_to_iast":
            self.scheme = "hk_to_iast"
            self.script_set = ASCII_HK_TO_IAST
            self.udata_to_anudatta = False
        elif scheme == "hk_to_iso":
            self.scheme = "hk_to_iso"
            self.script_set = ASCII_HK_TO_ISO
            self.udata_to_anudatta = False

    def converter(self, ascii_text):
        """
        Modifies the AsciiConverter.converter() method to work with
        vedic accents.
        """
        if self.udata_to_anudatta and self.scheme == "hk_to_deva":
            output = hk_ud_to_hk_anu(ascii_text)
        elif self.scheme == "hk_to_deva":
            output = "".join((filter(lambda x: x not in ["/"], ascii_text)))
        else:
            output = ascii_text

        for pair in self.script_set:
            output = re.sub(pair[0], pair[1], output)
        return output


if __name__ == "__main__":
    DEVA = "अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म्"
    HK = "agni/mILe puro/hitaM yajJa/sya deva/mRtvi/jam"

    ascii_replace = AsciiDevanagari(
        scheme="hk_to_deva", udatta_to_anudatta=True)
    print(ascii_replace.converter(HK))
    print(ascii_replace.converter(HK) == DEVA)
    ascii_replace = AsciiDevanagari(
        scheme="hk_to_deva", udatta_to_anudatta=False
        )
    print(ascii_replace.converter(HK))
