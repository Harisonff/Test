







init:
    $ truend_fluid = False

image b2te b2te01 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bk2_floortruend.jpg",
    (0, 0),  "bk2end/truend/az_body.png"
    )
image b2te b2te02 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",    
    )

image b2te b2te03 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick1.png", 
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick1_fluid.png"),
    )
image b2te b2te04 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick2.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick2_fluid.png"),
    )
image b2te b2te05 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",  
    (0, 0), "bk2end/truend/tylee_mouth.png",
    (0, 0), "bk2end/truend/dick3.png", 
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )
image b2te b2te06 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick4.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick4_fluid.png"),
    )
image b2te b2te07 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )


image b2te b2te10 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",    
    )
image b2te b2te11 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick1.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick1_fluid.png"),
    )

image b2te b2te11_1 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/dick1.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick1_fluid.png"),
    )

image b2te b2te12 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick2.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick2_fluid.png"),
    )
image b2te b2te13 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png", 
    (0, 0), "bk2end/truend/mai_mouth.png",
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )
image b2te b2te14 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick4.png", 
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick4_fluid.png"),
    )

image b2te b2te15 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )



image b2te_b2te01 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bk2_floortruend.jpg",
    (0, 0),  "bk2end/truend/az_body.png"
    )
image b2te_b2te02 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",    
    )
image b2te_b2te03 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick1.png", 
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick1_fluid.png"),
    )
image b2te_b2te04 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick2.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick2_fluid.png"),
    )
image b2te_b2te05 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",  
    (0, 0), "bk2end/truend/tylee_mouth.png",
    (0, 0), "bk2end/truend/dick3.png", 
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )
image b2te_b2te06 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick4.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick4_fluid.png"),
    )
image b2te_b2te07 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/tylee_body.png",   
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )


image b2te_b2te10 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",    
    )

image b2te_b2te10_1 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    )

image b2te_b2te11 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick1.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick1_fluid.png"),
    )

image b2te_b2te11_1 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/dick1.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick1_fluid.png"),
    )

image b2te_b2te12 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick2.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick2_fluid.png"),
    )

image b2te_b2te12_1 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/dick2.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick2_fluid.png"),
    )

image b2te_b2te13 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png", 
    (0, 0), "bk2end/truend/mai_mouth.png",
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )
image b2te_b2te14 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick4.png", 
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick4_fluid.png"),
    )

image b2te_b2te15 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/mai_body.png",   
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )

image b2te_b2te15_1 = LiveComposite(
    (1000, 720),
    (0, 0),"fbackgrounds/bk2_floortruend.jpg",
    (0, 0), "bk2end/truend/az_body.png",
    (0, 0), "bk2end/truend/dick3.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick3_fluid.png"),
    )







image b2te_maiblink = "bk2end/truend/mai_blink.png"
image b2te_tyleeblink = "bk2end/truend/tylee_blink.png"
image b2te_azblink = "bk2end/truend/az_blink.png"
image b2te_azcumface = "bk2end/truend/az_cumface.png"

image b2te_azeyesonyou = "bk2end/truend/az_body_eyeonplayer.png"

image b2te_maimouth = "bk2end/truend/mai_mouth.png"
image b2te_tyleemouth = "bk2end/truend/tylee_mouth.png"

image b2te_sperm1 = "bk2end/truend/sperm1.png"

image b2te_sperm2 = "bk2end/truend/sperm2.png"

image b2te_sperm3 = "bk2end/truend/sperm3.png"
image b2te_spermshot = "bk2end/truend/spermshot.png"
image b2te_solodick = LiveComposite(
    (1000, 720),
    (0, 0), "bk2end/truend/dick5.png",
    (0, 0), ConditionSwitch( 
        "truend_fluid == False", "transparent.png",
        "truend_fluid == True", "bk2end/truend/dick4_fluid.png"),
    )






image b2te_maiblink_ani:
    "bk2end/truend/mai_blink.png"
    0.2
    "transparent"
    0.2
    "bk2end/truend/mai_blink.png"
    0.2
    "transparent"
    6.0
    "bk2end/truend/mai_blink.png"
    0.2
    "transparent"
    9.0
    "bk2end/truend/mai_blink.png"
    0.2
    "transparent"
    2.5
    repeat


image b2te_tyleeblink_ani:
    "bk2end/truend/tylee_blink.png"
    0.2
    "transparent"
    0.2
    "bk2end/truend/tylee_blink.png"
    0.2
    "transparent"
    6.0
    "bk2end/truend/tylee_blink.png"
    0.2
    "transparent"
    9.0
    "bk2end/truend/tylee_blink.png"
    0.2
    "transparent"
    2.5
    repeat


image b2te_azblink_ani:
    "bk2end/truend/az_blink.png"
    0.2
    "transparent"
    0.2
    "bk2end/truend/az_blink.png"
    0.2
    "transparent"
    6.0
    "bk2end/truend/az_blink.png"
    0.2
    "transparent"
    9.0
    "bk2end/truend/az_blink.png"
    0.2
    "transparent"
    2.5
    repeat

image b2te b2te100:
    "b2te_b2te02"
    0.3
    "b2te_b2te03"
    0.2
    "b2te_b2te04"
    0.2
    "b2te_b2te05"
    0.2
    "b2te_b2te06"
    0.3
    "b2te_b2te05"
    0.2
    "b2te_b2te04"
    0.2
    "b2te_b2te03"
    0.2
    repeat

image b2te b2te101:
    "b2te b2te10"
    0.3
    "b2te b2te11"
    0.2
    "b2te b2te12"
    0.2
    "b2te b2te13"
    0.2
    "b2te b2te14"
    0.3
    "b2te b2te13"
    0.2
    "b2te b2te12"
    0.2
    "b2te b2te11"
    0.2
    repeat

image b2te b2te102:
    "b2te b2te10"
    0.2
    "b2te b2te11"
    0.2
    "b2te b2te12"
    0.2
    "b2te b2te15"
    0.2
    "b2te b2te12"
    0.2
    "b2te b2te11"
    0.2
    repeat

image b2te b2te103:
    "b2te b2te02"
    0.2
    "b2te b2te03"
    0.2
    "b2te b2te04"
    0.2
    "b2te b2te07"
    0.2
    "b2te b2te04"
    0.2
    "b2te b2te03"
    0.2
    repeat


image b2te b2te104:
    "b2te_b2te10_1"
    0.25
    "b2te_b2te11_1"
    0.25
    "b2te_b2te12_1"
    0.25
    "b2te_b2te15_1"
    0.25
    "b2te_b2te12_1"
    0.25
    "b2te_b2te11_1"
    0.25
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
