from pieltk.converters import vedic

def test_deva() -> None:
    ascii_replace = vedic.AsciiConverter(scheme="hk_to_deva",
            udatta_to_anudatta=True)
    deva = "अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म्"
    hk = "agni/mILe puro/hitaM yajJa/sya deva/mRtvi/jam"
    assert ascii_replace.converter(hk) == deva
