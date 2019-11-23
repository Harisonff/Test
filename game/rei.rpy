



image rei_c = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png")

image rei_ce = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_blink.png",
    )

image rei:
    "rei_c"
    5
    "rei_ce"
    0.08
    repeat

image rei_angry = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_angry.png",
    )

image rei_angry_e = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_angry.png",
    (0, 0), "captain/c_idle_fl_blink.png",
    )

image rei_smile = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_smile.png",
    )

image rei_smile_e = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_smile.png",
    (0, 0), "captain/c_idle_fl_blink.png",
    )

image rei_frown = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_frown.png",
    )

image rei_frown_left = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_frown.png",
    (0, 0), "captain/c_idle_fl_lookingleft.png",
    )

image rei_frown_e = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_frown.png",
    (0, 0), "captain/c_idle_fl_blink.png",
    )

image rei_left = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_lookingleft.png",
    )

image rei_sur = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_clothed.png",
    (0, 0), "captain/c_idle_fl_surprised.png",
    )





image rnude_be = LiveComposite(
    (1000, 720),
    (0, 0), "captain/c_idle_fl_nude.png",
    (0, 0), "captain/c_idle_fl_blush.png",
    (0, 0), "captain/c_idle_fl_blink.png",
    (0, 0), ConditionSwitch(
        "rei_bush == 'bush'", "captain/c_idle_fl_pubes.png",
        "rei_bush == 'nobush'", "transparent.png",
        "rei_bush == 'none'", "transparent.png",
        ),)







image rbj1 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_angry.png",
    )

image rbj2 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    )

image rbj3 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_dick_straight.png",
    )

image rbj4 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_dick_left.png",
    )

image rbj5 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_dick_right.png",
    )

image rbj_rub:
    "rbj3" with Dissolve(0.2)
    0.55
    "rbj4" with Dissolve(0.2)
    0.55
    "rbj3" with Dissolve(0.2)
    0.55
    "rbj5" with Dissolve(0.2)
    0.55
    repeat

image rbj6 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_blink.png",
    (0, 0), "captain/c_blowjob_dick_straight.png",
    )

image rbj7 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_01.png",
    )

image rbj8 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_02.png",
    )

image rbj9 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_03.png",
    )

image rbj_an1:
    "rbj7" with Dissolve(0.2)
    0.7
    "rbj8" with Dissolve(0.2)
    0.7
    repeat

image rbj_an2:
    "rbj7"
    0.35
    "rbj8"
    0.15
    "rbj9"
    0.3
    "rbj8"
    0.15
    repeat

image rbj_an3:
    "rbj10" with Dissolve(0.1)
    0.35
    "rbj11" with Dissolve(0.1)
    0.3
    repeat

image rbj10 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_01.png",
    (0, 0), "captain/c_blowjob_blink.png",
    )

image rbj11 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_03.png",
    (0, 57), "captain/c_blowjob_blink.png",

    )

image rbj_an4:
    "rbj10" with Dissolve(0.1)
    0.35
    "rbj12" with ushake
    0.3
    repeat

image rbj12 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_04.png",
    (0, 0), "captain/c_blowjob_blink.png",
    )

image rbj_an5:
    "rbj7" with Dissolve(0.1)
    0.35
    "rbj13" with ushake
    0.3
    repeat

image rbj13 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_04.png",
    )

image rbj14 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_sperm_0.png",
    )

image rbj15 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_sperm_1.png",
    )

image rbj16 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_watchtower_floor.jpg",
    (0, 0), "captain/c_blowjob_stance_00.png",
    (0, 0), "captain/c_blowjob_openmouth.png",
    (0, 0), "captain/c_blowjob_sperm_2.png",
    )








image rrcg rrcg01 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    )

image rrcg rrcg02 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_01.png", 
    )

image rrcg rrcg03 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_02.png", 
    )

image rrcg rrcg04 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_03.png", 
    )

image rrcg rrcg05 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_fluid.png", 
    )

image rrcg rrcg06 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    
    )


image rrcg rrcg07 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_finger_01.png", 
    )

image rrcg rrcg08 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_finger_02.png", 
    )

image rrcg rrcg09 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_finger_03.png", 
    )



image rrcg rrcg10 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_sperminside_01.png", 
    )

image rrcg rrcg11 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_sperminside_02.png", 
    )

image rrcg rrcg12 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_sperminside_03.png", 
    )

image rrcg rrcg13 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_01.png", 
    (0, 0), "captain/c_fuck_sperminside_04.png", 
    )




image rrcg rrcg14 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_sperminside_03.png",
    (0, 0), "captain/c_fuck_finger_01.png",
    )

image rrcg rrcg15 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_sperminside_03.png",
    (0, 0), "captain/c_fuck_finger_02.png",
    )

image rrcg rrcg16 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_04.png", 
    (0, 0), "captain/c_fuck_sperminside_03.png",
    (0, 0), "captain/c_fuck_finger_03.png",
    )





image rrcg rrcg17 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_01.png",
    (0, 0), "captain/c_fuck_spermoutside_01.png",
    )

image rrcg rrcg18 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_01.png",
    (0, 0), "captain/c_fuck_spermoutside_02.png",
    )

image rrcg rrcg19 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a watchtower_day.jpg",
    (0, 0), "captain/c_fuck_playerbody.png",
    (0, 0), "captain/c_fuck_stance_01.png",
    (0, 0), "captain/c_fuck_spermoutside_03.png",
    )








image rrcg rrcg100:

    "rrcg rrcg03"
    0.3
    "rrcg rrcg04"
    0.2
    "rrcg rrcg06"
    0.3
    "rrcg rrcg04"
    0.2

    repeat

image rrcg rrcg100_1:

    "rrcg rrcg03" with Dissolve(0.2)
    0.8
    "rrcg rrcg04" with Dissolve(0.2)
    0.8
    repeat

image rrcg rrcg100_2:

    "rrcg rrcg03"
    0.3
    "rrcg rrcg04"
    0.08
    "rrcg rrcg06"
    0.3
    "rrcg rrcg04"
    0.08

    repeat

image rrcg rrcg101:



    "rrcg rrcg04"
    0.4
    "rrcg rrcg06"
    0.4



    repeat


image rrcg rrcg102:

    "rrcg rrcg03"
    0.7


    "rrcg rrcg05" with vpunch
    0.9



    repeat

image rrcg rrcg102_1:

    "rrcg rrcg03"
    0.4


    "rrcg rrcg05" with vpunch
    0.6



    repeat

image rrcg rrcg103:



    "rrcg rrcg08"
    0.4
    "rrcg rrcg09"
    0.4



    repeat

image rrcg rrcg104:



    "rrcg rrcg15"
    0.4
    "rrcg rrcg16"
    0.4



    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
