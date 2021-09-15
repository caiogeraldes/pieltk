"""
Unicode converter from PROIEL's romanization of Classical Armenian to
Unicode Armenian Script.
"""

import re
from typing import List, Tuple

PROEIL_ACCENTS: List[Tuple[str, str]] = [
        (r"á", r"a"),
        (r"ı̈", r"i"),
        (r"í", r"i"),
        (r"ḗ", r"ē"),
        (r"ó", r"o"),
        (r"Á", r"A"),
        (r"Ï", r"I"),
        (r"Í", r"I"),
        (r"Ḗ", r"Ē"),
        (r"Ó", r"O")
        ]

PROIEL_ARMENIAN: List[Tuple[str, str]] = [
        (r"r̄", r"ռ"),
        (r"kʻ", r"ք"),
        (r"cʻ", r"ց"),
        (r"tʻ", r"թ"),
        (r"čʻ", r"չ"),
        (r"pʻ", r"փ"),
        (r"e", r"ե"),
        (r"ə", r"ը"),
        (r"a", r"ա"),
        (r"o", r"ո"),
        (r"w", r"ւ"),
        (r"i", r"ի"),
        (r"ē", r"է"),
        (r"z", r"զ"),
        (r"t", r"տ"),
        (r"l", r"լ"),
        (r"s", r"ս"),
        (r"ł", r"ղ"),
        (r"d", r"դ"),
        (r"r", r"ր"),
        (r"n", r"ն"),
        (r"ž", r"ժ"),
        (r"v", r"վ"),
        (r"b", r"բ"),
        (r"m", r"մ"),
        (r"š", r"շ"),
        (r"k", r"կ"),
        (r"g", r"գ"),
        (r"h", r"հ"),
        (r"y", r"յ"),
        (r"x", r"խ"),
        (r"c", r"ծ"),
        (r"č", r"ճ"),
        (r"j", r"ձ"),
        (r"ǰ", r"ջ"),
        (r"f", r"ֆ"),

        (r"R̄", r"Ռ"),
        (r"Kʻ", r"Ք"),
        (r"Cʻ", r"Ց"),
        (r"Tʻ", r"Թ"),
        (r"Čʻ", r"Չ"),
        (r"Pʻ", r"Փ"),
        (r"E", r"Ե"),
        (r"Ə", r"Ը"),
        (r"A", r"Ա"),
        (r"O", r"Ո"),
        (r"W", r"Ւ"),
        (r"I", r"Ի"),
        (r"Ē", r"Է"),
        (r"Z", r"Զ"),
        (r"T", r"Տ"),
        (r"L", r"Լ"),
        (r"S", r"Ս"),
        (r"Ł", r"Ղ"),
        (r"D", r"Դ"),
        (r"R", r"Ր"),
        (r"N", r"Ն"),
        (r"Ž", r"Ժ"),
        (r"V", r"Վ"),
        (r"B", r"Բ"),
        (r"M", r"Մ"),
        (r"Š", r"Շ"),
        (r"K", r"Կ"),
        (r"G", r"Գ"),
        (r"H", r"Հ"),
        (r"Y", r"Յ"),
        (r"X", r"Խ"),
        (r"C", r"Ծ"),
        (r"Č", r"Ճ"),
        (r"J", r"Ձ"),
        (r"ǰ", r"Ջ"),
        (r"F", r"Ֆ"),
]


def unaccented_proiel(proiel_text: str) -> str:
    """
    Cleanup the accents from PROIEL text since it is not clear what how it
    would be represented on Armenian Script.
    """
    unaccented_text: str = proiel_text
    for pair in PROEIL_ACCENTS:
        unaccented_text = re.sub(pair[0], pair[1], unaccented_text)
    return unaccented_text


def proiel_to_armenian(proiel_text: str) -> str:
    """
    Outputs an armenian script version of PROIEL's text.
    """
    unaccented_text: str = unaccented_proiel(proiel_text)

    armenian_text: str = unaccented_text
    for pair in PROIEL_ARMENIAN:
        armenian_text = re.sub(pair[0], pair[1], armenian_text)

    return armenian_text


def armenian_to_proiel(armenian_text: str) -> str:
    """
    Outputs an unaccented version of PROIEL text from an Armenian entry.
    """
    proiel_text: str = armenian_text

    for pair in PROIEL_ARMENIAN:
        proiel_text = re.sub(pair[1], pair[0], proiel_text)

    return proiel_text
