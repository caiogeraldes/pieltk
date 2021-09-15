from pieltk.converters.xcl.proiel import proiel_to_armenian, armenian_to_proiel, unaccented_proiel

proiel_strings: list[str] = ["""Ew teseal zžołovowrdsn el ı̈ leár̄n ew ibrew nstaw and mateán ar̄ na ašakertkʻn nora""",
            """Ew bacʻeal zberan iwr owsowcʻanḗr znosa ew asēr""",
            """Eraní ałkʻatacʻ hogwov zi nocʻa ē arkʻayowtʻiwn erknicʻ""",
            """Eraní sgaworacʻ zi nokʻa mxitʻarescʻin""",
            """Eraní or kʻałcʻeal ew carawi icʻen ardarowtʻean zi nokʻa yagescʻin""",
            """Eraní ołormacacʻ zi nokʻa ołormowtʻiwn gtcʻen""",
            """Eraní aynocʻik or sowrb en srtiwkʻ zi nokʻa zAstowác tescʻen""",
            """Eraní xałałararacʻ zi nokʻa ordikʻ Astowacoy kočʻescʻin""",
            """Eraní or halaceal icʻen vasn ardarowtʻean zi nocʻa ē arkʻayowtʻiwn erknicʻ""",
            """Aył ays amenayn ełew zi lcʻcʻi or asacʻawn i Tear̄nē ı̈ jer̄n Ēsayay margarēi"""
            ]
arm_strings: list[str] = ["""Եւ տեսեալ զժողովուրդսն ել ի լեառն եւ իբրեւ նստաւ անդ մատեան առ նա աշակերտքն նորա""",
            """Եւ բացեալ զբերան իւր ուսուցանէր զնոսա եւ ասէր""",
            """Երանի աղքատաց հոգւով զի նոցա է արքայութիւն երկնից""",
            """Երանի սգաւորաց զի նոքա մխիթարեսցին""",
            """Երանի որ քաղցեալ եւ ծարաւի իցեն արդարութեան զի նոքա յագեսցին""",
            """Երանի ողորմածաց զի նոքա ողորմութիւն գտցեն""",
            """Երանի այնոցիկ որ սուրբ են սրտիւք զի նոքա զԱստուած տեսցեն""",
            """Երանի խաղաղարարաց զի նոքա որդիք Աստուածոյ կոչեսցին""",
            """Երանի որ հալածեալ իցեն վասն արդարութեան զի նոցա է արքայութիւն երկնից""",
            """Այղ այս ամենայն եղեւ զի լցցի որ ասացաւն ի Տեառնէ ի ձեռն Էսայայ մարգարէի"""
            ]

def test_proiel_to_armenian() -> None:
    for index, value in enumerate(proiel_strings):
        assert proiel_to_armenian(value) == arm_strings[index]


def test_armenian_to_proiel() -> None:
    for index, value in enumerate(arm_strings):
        assert armenian_to_proiel(value) == unaccented_proiel(proiel_strings[index])


