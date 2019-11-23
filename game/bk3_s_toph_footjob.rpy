







init:
    $ toph_footjob2_nude = False
    $ toph_footjob = "dirt"
    $ toph_footjob_barechest = False



image tofj tofj05 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/leg_left_ground.png", 
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),    
    
    (0, 0), "bk3/toph/footjob/arms_nosee.png",
    )

image tofj tofj06 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/leg_left_ground.png",   
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/arms_chin.png",
    )

image tofj tofj08 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_right.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/leg_left_ground.png",
    )
image tofj tofj09 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/leg_left_ground.png",
    )

image tofj tofj10 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/leg_left_raised.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/leg_left_raised_dirt.png",),
    )

image tofj tofj11 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/leg_left_raised_2.png",
    (0, 0), ConditionSwitch(  
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/leg_left_raised_2_dirt.png",),
    )



image tofj tofj15 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/footjob1.png",
    (0, 0), ConditionSwitch(  
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/footjob1_dirt.png",),
    )
image tofj tofj16 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/footjob2.png",
    (0, 0), ConditionSwitch(  
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/footjob2_dirt.png",),
    )
image tofj tofj17 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/footjob3.png",
    (0, 0), ConditionSwitch(    
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/footjob3_dirt.png",),
    )
image tofj tofj18 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/footjob4.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/footjob4_dirt.png",),
    )

image tofj tofj19 = LiveComposite( 
    (1000, 720),
    (0, 0), "bk3/toph/footjob/body_0.png",
    (0, 0), "bk3/toph/footjob/head_front.png",
    (0, 0), "bk3/toph/footjob/arms_back.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob_barechest == False","transparent.png",
        "toph_footjob_barechest == True", "bk3/toph/footjob/barechest.png"),
    (0, 0), "bk3/toph/footjob/footjob5.png",
    
    (0, 0), ConditionSwitch( 
        "toph_footjob == 'clean'", "transparent.png",
        "toph_footjob == 'dirt'", "bk3/toph/footjob/footjob4_dirt.png",),
    )


image tofj tofj50 = LiveComposite( 
    (1000, 720),
    (0, 0), "bk3/toph/footjob2/body.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/clothes.png",
        "toph_footjob2_nude == True", "transparent.png"),
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/legs0_cloth.png",
        "toph_footjob2_nude == True", "bk3/toph/footjob2/legs0_nude.png"),
    )

image tofj tofj51 = LiveComposite( 
    (1000, 720),
    (0, 0), "bk3/toph/footjob2/body.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/clothes.png",
        "toph_footjob2_nude == True", "transparent.png"),
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/legs1_cloth.png",
        "toph_footjob2_nude == True", "bk3/toph/footjob2/legs1_nude.png"),
    )
image tofj tofj52 = LiveComposite( 
    (1000, 720),
    (0, 0), "bk3/toph/footjob2/body.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/clothes.png",
        "toph_footjob2_nude == True", "transparent.png"),
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/legs2_cloth.png",
        "toph_footjob2_nude == True", "bk3/toph/footjob2/legs2_nude.png"),
    )
image tofj tofj53 = LiveComposite( 
    (1000, 720),
    (0, 0), "bk3/toph/footjob2/body.png",
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/clothes.png",
        "toph_footjob2_nude == True", "transparent.png"),
    (0, 0), ConditionSwitch( 
        "toph_footjob2_nude == False","bk3/toph/footjob2/legs3_cloth.png",
        "toph_footjob2_nude == True", "bk3/toph/footjob2/legs3_nude.png"),
    )








image tofj_blink = "bk3/toph/footjob/blink.png"
image tofj_blush = "bk3/toph/footjob/blush.png"
image tofj_solodick = "bk3/toph/footjob/solodick.png"
image tofj_angry = "bk3/toph/footjob/front_angry.png"
image tofj_smile = "bk3/toph/footjob/front_smile.png"
image tofj_doubt = "bk3/toph/footjob/front_doubt.png"
image tofj_smirk = "bk3/toph/footjob/front_smirk.png"

image tofj2_solodick = "bk3/toph/footjob2/solodick.png"
image tofj2_lewd = "bk3/toph/footjob2/lewd.png"
image tofj2_blink = "bk3/toph/footjob2/blink.png"
image tofj2_uncertain = "bk3/toph/footjob2/uncertain.png"




image tofj_sperm0 = "bk3/toph/footjob/sperm0.png"
image tofj_sperm1 = "bk3/toph/footjob/sperm1.png"
image tofj_sperm2 = "bk3/toph/footjob/sperm2.png"
image tofj_sperm3 = "bk3/toph/footjob/sperm3.png"



image tofj2_spermshot = "bk3/toph/footjob2/spermshot.png"
image tofj2_sperm1 = "bk3/toph/footjob2/sperm1.png"
image tofj2_sperm2 = "bk3/toph/footjob2/sperm2.png"
image tofj2_sperm3 = "bk3/toph/footjob2/sperm3.png"




image tofj_blink_ani:

    "bk3/toph/footjob/blink.png"
    0.2
    "transparent.png"
    0.2
    "bk3/toph/footjob/blink.png"
    0.2
    "transparent.png"
    5.0
    "bk3/toph/footjob/blink.png"
    0.2
    "transparent.png"
    5.0
    "bk3/toph/footjob/blink.png"
    0.2
    "transparent.png"
    0.2
    "bk3/toph/footjob/blink.png"
    0.2
    "transparent.png"
    8.0
    "bk3/toph/footjob/blink.png"
    0.2
    "transparent.png"
    3.0
    repeat

image tofj_jack_1:
    "bk3/toph/footjob/jack01.png"
    0.3
    "bk3/toph/footjob/jack02.png"
    0.3
    "bk3/toph/footjob/jack03.png"
    0.3
    "bk3/toph/footjob/jack02.png"
    0.3
    repeat

image tofj_jack_slow:
    "bk3/toph/footjob/jack03.png"
    0.4
    "bk3/toph/footjob/jack04.png"
    0.4
    "bk3/toph/footjob/jack05.png"
    0.4
    "bk3/toph/footjob/jack04.png"
    0.4
    repeat

image tofj_jack_fast:
    "bk3/toph/footjob/jack03.png"
    0.2
    "bk3/toph/footjob/jack05.png"
    0.2

    repeat


image tofj_jack_2:
    "bk3/toph/footjob/jack01.png"
    0.3
    "bk3/toph/footjob/jack02.png"
    0.3
    "bk3/toph/footjob/jack03.png"
    0.3
    "bk3/toph/footjob/jack04.png"
    0.4
    "bk3/toph/footjob/jack05.png"
    0.4
    "bk3/toph/footjob/jack04.png"
    0.4
    "bk3/toph/footjob/jack03.png"
    0.3
    "bk3/toph/footjob/jack02.png"
    0.3
    repeat



image tofj tofj100:

    "tofj tofj01"
    0.4
    "tofj tofj02"
    0.3
    "tofj tofj01"
    0.5
    "tofj tofj02"
    0.3
    "tofj tofj01"
    0.5
    "tofj tofj02"
    0.3
    "tofj tofj01"
    0.5
    "tofj tofj02"
    0.5
    "tofj tofj04"
    0.2
    "tofj tofj03"
    0.5
    "tofj tofj01"
    2.4
    "tofj tofj02"
    0.7

    repeat


image tofj tofj101:

    "tofj tofj15"
    0.4
    "tofj tofj16"
    0.4
    "tofj tofj17"
    0.4
    "tofj tofj18"
    0.4
    "tofj tofj17"
    0.4
    "tofj tofj16"
    0.4
    repeat

image tofj tofj101_1:

    "tofj tofj15"
    0.25
    "tofj tofj16"
    0.25
    "tofj tofj17"
    0.25
    "tofj tofj18"
    0.25
    "tofj tofj17"
    0.25
    "tofj tofj16"
    0.25
    repeat

image tofj tofj101_2:

    "tofj tofj15"
    0.15
    "tofj tofj16"
    0.15
    "tofj tofj17"
    0.15
    "tofj tofj18"
    0.15
    "tofj tofj17"
    0.15
    "tofj tofj16"
    0.15
    repeat

image tofj tofj101_3:

    "tofj tofj15"
    0.2
    "tofj tofj16"
    0.2
    "tofj tofj17"
    0.2
    "tofj tofj18"
    0.2
    "tofj tofj17"
    0.2
    "tofj tofj16"
    0.2
    repeat

image tofj tofj102:

    "tofj tofj15"
    0.4
    "tofj tofj19"
    0.2


    repeat

image tofj tofj102_1:

    "tofj tofj15"
    0.28
    "tofj tofj19"
    0.2


    repeat

image tofj tofj103:

    "tofj tofj10"
    0.5

    "tofj tofj11"
    0.5

    repeat

image tofj tofj105:
    "tofj tofj51"
    0.3
    "tofj tofj52"
    0.3
    "tofj tofj53"
    0.3
    "tofj tofj52"
    0.3
    repeat

image tofj tofj106:
    "tofj tofj51"
    0.23
    "tofj tofj52"
    0.23
    "tofj tofj53"
    0.23
    "tofj tofj52"
    0.23
    repeat

image tofj tofj107:
    "tofj tofj51"
    0.18
    "tofj tofj52"
    0.18
    "tofj tofj53"
    0.18
    "tofj tofj52"
    0.18
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
