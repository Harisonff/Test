







image aztf tf01 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_thronefuck.jpg",
    (0, 0), "azula/thronefuck/a_thronefuck_sololeg.png",
    (0, 0), "azula/thronefuck/a_thronefuck_azula_1.png",    
    (0, 0), ConditionSwitch(
        "apub_outfit == 'norm'", "azula/thronefuck/a_thronefuck_azula_1_norm.png",
        "apub_outfit == 'dom'", "azula/thronefuck/a_thronefuck_azula_1_dom.png",
        "apub_outfit >= 'none'", "transparent.png"),
    (0, 0), "azula/thronefuck/a_thronefuck_girl_1.png",
    )

image aztf tf02 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_thronefuck.jpg",
    (0, 0), "azula/thronefuck/a_thronefuck_sololeg.png",
    (0, 0), "azula/thronefuck/a_thronefuck_azula_2.png",    
    (0, 0), ConditionSwitch(
        "apub_outfit == 'norm'", "azula/thronefuck/a_thronefuck_azula_2_norm.png",
        "apub_outfit == 'dom'", "azula/thronefuck/a_thronefuck_azula_2_dom.png",
        "apub_outfit >= 'none'", "transparent.png"),
    (0, 0), "azula/thronefuck/a_thronefuck_girl_2.png",
    (0, 0), "azula/thronefuck/a_thronefuck_girl_2_fluid_1.png",
    )





image aztf tf03 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_thronefuck.jpg",    
    (0, 0), "azula/thronefuck/a_thronefuck_azula_1.png",    
    (0, 0), ConditionSwitch(
        "apub_outfit == 'norm'", "azula/thronefuck/a_thronefuck_azula_1_norm.png",
        "apub_outfit == 'dom'", "azula/thronefuck/a_thronefuck_azula_1_dom.png",
        "apub_outfit >= 'none'", "transparent.png"),    
    )

image aztf tf04 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_thronefuck.jpg",    
    (0, 0), "azula/thronefuck/a_thronefuck_azula_2.png",    
    (0, 0), ConditionSwitch(
        "apub_outfit == 'norm'", "azula/thronefuck/a_thronefuck_azula_2_norm.png",
        "apub_outfit == 'dom'", "azula/thronefuck/a_thronefuck_azula_2_dom.png",
        "apub_outfit >= 'none'", "transparent.png"),       
    )



image aztf tf05 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_thronefuck.jpg",
    (0, 0), "azula/thronefuck/a_thronefuck_girl_solo.png",
    )













image aztf tf100:

    "aztf tf01"
    0.5
    "aztf tf02" with ushake
    0.5

    repeat

image aztf tf101:

    "aztf tf03"
    0.5
    "aztf tf04"
    0.5

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
