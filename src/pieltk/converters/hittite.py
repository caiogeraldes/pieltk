"""
Implements Hittite converter.
"""

ALPHA_TO_HITTITE_CUNEIFORM = [
    (r"'d", "๐ญ"),
    (r"'m", "๐น"),
    (r"gloss", "๐ฑ"),



    (r"GURUSH", "๐"),
    (r"DINGIR", "๐ญ"),
    (r"BABBAR", "๐"),



    (r"รRIN", "๐"),
    (r"sal|MUNUS|'f", "๐ฉ"),
    (r"URUDU", "๐"),
    (r"GรSPU|GESPU2", "๐๐ฝ๐ฝ"),
    (r"Pร|TรL|tรบl|GรGIR|PU2|tul2|GIGIR2", "๐ฅ"),
    (r"ISKUR", "๐"),
    (r"LUGAL", "๐"),
    (r"MUSEN", "๐ท"),
    (r"EZEN4", "๔"),
    (r"GASAN", "๐ฝ"),
    (r"NINDA", "๐ป"),

    (r"ANSE", "๐ฒ"),
    (r"KARAS", "๐ ๐๐"),
    (r"GรR|GIR3", "๐"),
    (r"EGIR", "๐"),
    (r"GIS|iz", "๐"),
    (r"DUMU", "๐"),
    (r"SE12", "๐บ"),
    (r"GADA", "๐ฐ"),
    (r"SIG7", "๐"),
    (r"BรD|BAD3", "๐ฆ"),
    (r"TUG2|TรG", "๐"),
    (r"tas3|tร s", "๐พ"),
    (r"tรฉn|ten2|DIN", "๐ท"),


    (r"ANA", "๐๐พ"),
    (r"INA", "๐ฟ๐พ"),
    (r"รD|ID2", "๐๐"),
    (r"MES", "๐ฉ"),
    (r"SUM", "๐ง"),
    (r"sar|SAR", "๐ฌ"),
    (r"UTU|tam|pir", "๐"),
    (r"dam", "๐ฎ"),
    (r"Sร|SA3", "๐ฎ"),
    (r"lis", "๐บ"),
    (r"GE6", "๐ช"),
    (r"GIG", "๐ช๐ญ"),
    (r"UGU", "๐๐"),
    (r"gul", "๐ข"),
    (r"KUS", "๐ข"),
    (r"kis", "๐ง"),
    (r"UDU", "๐ป"),
    (r"NIR", "๐ช"),
    (r"UZU", "๐"),
    (r"dur", "๐"),
    (r"kal|dan", "๐"),
    (r"mar", "๐ฅ"),
    (r"gur", "๐ฅ"),
    (r"hat", "๐บ"),
    (r"DUG", "๐"),
    (r"GIM", "๐ถ"),
    (r"GU4|GUD", "๐"),
    (r"kum", "๐ฃ"),
    (r"hรฉ|he2", "๐ถ"),
    (r"SES", "๐"),
    (r"ARAD", "๐ด"),
    (r"zรฉ|ze2", "๐ข"),
    (r"pรญ|pi2", "๐"),
    (r"kรกn|kan2", "๐ท"),
    (r"pรกt|pat2", "๐"),
    (r"pรกr|par2", "๐"),
    (r"tรกk|tak2", "๐"),
    (r"SรG|SIG", "๐ "),
    (r"pal|BAL", "๐"),
    (r"GรL|[ie]k", "๐"),
    (r"Mร|ME3", "๐"),
    (r"az|AS\.", "๐"),
    (r"ABI", "๐๐"),
    (r"ABU", "๐๐"),
    (r"GAL", "๐ฒ"),
    (r"GAM", "๐ต"),
    (r"pur", "๐"),
    (r"ISH", "๐"),
    (r"KUR", "๐ณ"),
    (r"KรR", "๐ฝ"),
    (r"LIM", "๐"),
    (r"SAG", "๐"),
    (r"URU", "๐ท"),
    (r"ZAG", "๐ "),
    (r"BAT", "๐"),
    (r"AMA", "๐ผ"),
    (r"h[ae]r|mur", "๐ฏ"),
    (r"mas", "๐"),
    (r"s[ie]r", "๐"),
    (r"tar", "๐ป"),
    (r"ker", "๐ซ"),
    (r"kas", "๐"),
    (r"kat", "๐ฐ"),
    (r"hal", "๐ฌ"),
    (r"ka4", "๐ก"),
    (r"wi5", "๐พ"),
    (r"rat", "๐ฅ"),
    (r"nam", "๐"),
    (r"lam", "๐ด"),
    (r"lum", "๐"),
    (r"GAG|DU3|Dร", "๐"),
    (r"kam|TU7", "๐ฐ"),



    (r"um|UM", "๐"),
    (r"in", "๐"),
    (r"pu", "๐"),
    (r"se", "๐บ"),
    (r"[ie]m", "๐"),
    (r"ut", "๐"),
    (r"uz", "๐ป"),
    (r"gu", "๐"),
    (r"ul", "๐"),
    (r"zu", "๐ช"),
    (r"ba", "๐"),
    (r"al", "๐ "),
    (r"am", "๐"),
    (r"du", "๐บ"),
    (r"uk", "๐"),
    (r"BE", "๐"),
    (r"รS", "๐"),
    (r"รR", "๐ด"),
    (r"BI", "๐"),
    (r"DU", "๐"),
    (r"GU", "๐"),
    (r"HI", "๐ญ"),
    (r"IA", "๐"),
    (r"IM", "๐"),
    (r"Lร", "๐ฝ"),
    (r"MA", "๐ "),
    (r"UL", "๐"),
    (r"UR", "๐จ"),
    (r"SI", "๐ "),
    (r"ZA", "๐"),
    (r"Qร", "๐ "),
    (r"as|Rร", "๐ธ"),
    (r"ni|Lร", "๐"),
    (r"en|EN", "๐"),
    (r"NA4", "๐๐"),
    (r"Kร", "๐ฌ"),
    (r"ip", "๐"),
    (r"gi", "๐"),
    (r"qa", "๐ก"),
    (r"[aeiu]h", "๐ด"),
    (r"ak", "๐"),
    (r"an", "๐ญ"),
    (r"ar", "๐"),
    (r"at", "๐"),
    (r"da", "๐"),
    (r"di", "๐ฒ"),
    (r"es", "๐"),
    (r"ga", "๐ต"),
    (r"ha", "๐ฉ"),
    (r"he", "๐ญ"),
    (r"hi", "๐ญ"),
    (r"hu", "๐ท"),
    (r"ia", "๐"),
    (r"[ie]r", "๐"),
    (r"is", "๐"),
    (r"[ei]t", "๐"),
    (r"ka", "๐"),
    (r"k[ie]", "๐ "),
    (r"ku", "๐ช"),
    (r"la", "๐ท"),
    (r"ap", "๐"),
    (r"l[ie]", "๐ท"),
    (r"lu", "๐ป"),
    (r"ma", "๐ "),
    (r"me", "๐จ"),
    (r"mi", "๐ช"),
    (r"mu", "๐ฌ"),
    (r"na", "๐พ"),
    (r"ne", "๐"),
    (r"nu", "๐ก"),
    (r"pa", "๐บ"),
    (r"ra", "๐"),
    (r"ri", "๐"),
    (r"ru", "๐"),
    (r"sa", "๐"),
    (r"si", "๐"),
    (r"su|SU", "๐"),
    (r"ta", "๐ซ"),
    (r"te", "๐ผ"),
    (r"ti", "๐พ"),
    (r"tu", "๐"),
    (r"un", "๐ฆ"),
    (r"up", "๐"),
    (r"us", "๐"),
    (r"wa", "๐ฟ"),
    (r"za", "๐"),
    (r"zi", "๐ฃ"),
    (r"ur", "๐จ"),
    (r"BI", "๐"),
    (r"BU", "๐"),


    (r"a|A", "๐"),
    (r"e", "๐"),
    (r"i|I", "๐ฟ"),
    (r"รบ", "๐"),
    (r"ร|u", "๐"),
    (r"ร", "๐"),




    (r"1(\d)", r"๐\1"),
    (r"2", "๐ซ"),
    (r"3", "๐"),
    (r"4", "๐"),
    (r"5", "๐"),
    (r"6", "๐"),
    (r"7", "๐"),
    (r"8", "๐"),
    (r"9", "๐"),

    (r"-", "")]
