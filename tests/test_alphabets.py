from pieltk.alphabet import ave


def test_avestan_vowels() -> None:
    assert ave.VOWELS[0] == "𐬀"
