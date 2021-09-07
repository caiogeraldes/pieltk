alpha_to_polytonicgreek = (
   # Reordering diacritics
   # Bringing breathings and diairesis first, then accents, then subscript iota
    (r"([\\/=])(\|)?([()+])?", r"\3\1\2"),

    (r"S|\*s", "Σ"),
    (r"B|\*b", "Β"),
    (r"G|\*g", "Γ"),
    (r"D|\*d", "Δ"),
    (r"Z|\*z", "Ζ"),
    (r"Q|\*q", "Θ"),
    (r"K|\*k", "Κ"),
    (r"L|\*l", "Λ"),
    (r"M|\*m", "Μ"),
    (r"N|\*n", "Ν"),
    (r"J|\*j", "Ξ"),
    (r"P|\*p", "Π"),
    (r"R|\*r", "Ρ"),
    (r"T|\*t", "Τ"),
    (r"C|\*c", "Ψ"),
    (r"X|\*x", "Χ"),
    (r"F|\*f", "Φ"),
    (r"A|\*a", "Α"),
    (r"E|\*e", "Ε"),
    (r"H|\*h", "Η"),
    (r"I|\*i", "Ι"),
    (r"O|\*o", "Ο"),
    (r"U|\*u", "Υ"),
    (r"W|\*w", "Ω"),

    (r"s([ ,.;])", r"ς\1"),
    (r"s", "σ"),
    (r"b", "β"),
    (r"g", "γ"),
    (r"d", "δ"),
    (r"z", "ζ"),
    (r"q", "θ"),
    (r"k", "κ"),
    (r"l", "λ"),
    (r"m", "μ"),
    (r"n", "ν"),
    (r"j", "ξ"),
    (r"p", "π"),
    (r"t", "τ"),
    (r"c", "ψ"),
    (r"x", "χ"),
    (r"f", "φ"),
    (r"r", "ρ"),
    (r"a", "α"),
    (r"e", "ε"),
    (r"h", "η"),
    (r"i", "ι"),
    (r"o", "ο"),
    (r"u", "υ"),
    (r"w", "ω"),

   # others
   # lunate sigma
    (r"σ3", "\u03f2"),
    (r"Σ3", "\u03f9"),
   # fixed σ
    (r"σ2", "σ"),
   # koppa
    (r"\*#2", "\u03de"),
    (r"#2", "\u03df"),
   # koppa (archaic)
    (r"\*#3", "\u03d8"),
    (r"#3", "\u03d9"),
   # sampi
    (r"\*#4", "\u03e0"),
    (r"#4", "\u03e1"),

   # Diacritics
   # breathings
    (r"\)", "\u0313"),
    (r"\(", "\u0314"),
    (r"\+", "\u0308"),
   # accents
    (r"\\", "\u0300"),
    (r"\/", "\u0301"),
    (r"=", "\u0342"),
   # subscript iota
    (r"\|", "\u0345"),
   # dot below
    (r"\?", "\u0323"),
   # breve
    (r"%27", "\u0306"),
   # longa / macron
    (r"%26", "\u0304"),

   # Punctuation
   # middle dot
    (r":", "\u00b7"),
    (r"'", "\u02bc"),
)