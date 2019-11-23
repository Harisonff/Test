


init:
    $ tojc_face = 'blindfold'




image tojc tojc00 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0), "bk3/jin/shackles/body1.png",
    )

image tojc tojc01 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0), "bk3/jin/shackles/body1.png",
    (800, 0), "bk3/jin/shackles/fuck1.png",
    )

image tojc tojc02 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0), "bk3/jin/shackles/body1.png",   
    (800, 0), "bk3/jin/shackles/fuck2.png",   
    )

image tojc tojc03 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0), "bk3/jin/shackles/body1.png",   
    (800, 0), "bk3/jin/shackles/fuck3.png",
    )

image tojc tojc04 = LiveComposite(
    (1000, 720),
    (154, 255), "tojc_head",
    (362, 0), "bk3/jin/shackles/body2.png",   
    (800, 0), "bk3/jin/shackles/fuck4.png",
    )

image tojc tojc05 = LiveComposite(
    (1000, 720),
    (156, 255), "tojc_head",
    (355, 0), "bk3/jin/shackles/body3.png",  
    (797, 0), "bk3/jin/shackles/fuck5.png",
    )
image tojc tojc06 = LiveComposite(
    (1000, 720),
    (156, 255), "tojc_head",
    (355, 0), "bk3/jin/shackles/body3.png",  
    (797, 0), "bk3/jin/shackles/fuck6.png",
    )

image tojc tojc07 = LiveComposite(
    (1000, 720),
    (0, 0),"bk3/jin/shackles/fl_body.png" ,
    )

image tojc tojc08 = LiveComposite(
    (1000, 720),
    (0, 0),"bk3/jin/shackles/big_pussy.png" ,
    (0, 0),"bk3/jin/shackles/big_xray0.png" ,
    )
image tojc tojc09 = LiveComposite(
    (1000, 720),
    (0, 0),"bk3/jin/shackles/big_pussy.png" ,
    (0, 0),"bk3/jin/shackles/big_xray.png" ,
    )
image tojc tojc10 = LiveComposite(
    (1000, 720),
    (0, 0),"bk3/jin/shackles/big_pussy.png" ,
    (0, 0),"bk3/jin/shackles/big_enddick.png" ,
    )

image tojc tojc11 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0),"bk3/jin/shackles/body3.png",
    (10, 0),"tojc_dildo",
    )
image tojc tojc12 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0),"bk3/jin/shackles/body3.png",
    (10, 0),"tojc_dildo",
    )

image tojc tojc13 = LiveComposite(
    (1000, 720),
    (151, 255), "tojc_head",
    (362, 0),"bk3/jin/shackles/body3.png",
    (10, 0),"tojc_dildo_2",
    )

image tojc tojc14 = LiveComposite(
    (1000, 720),
    (0, 0),"bk3/jin/shackles/bg.jpg",
    (151, 255), "tojc_head",
    (362, 0),"bk3/jin/shackles/body1.png",
    (10, 0),"bk3/jin/shackles/dildo5.png",
    )
image tojc tojc15 = LiveComposite(
    (1000, 720),
    (0, 0),"bk3/jin/shackles/big_pussy.png" ,
    (0, 0),"bk3/jin/shackles/big_enddildo.png" ,
    )




image tojc_head = LiveComposite(
    (267, 411),
    (0, 0), "bk3/jin/shackles/head.png", 
    (0, 0), ConditionSwitch( 
        "tojc_face == 'neutral'", "bk3/jin/shackles/head.png", 
        "tojc_face == 'lookdown'", "bk3/jin/shackles/head_lookdown.png", 
        "tojc_face == 'blindfold'", "bk3/jin/shackles/head_blindfold.png",       
        "tojc_face == 'lusty'", "bk3/jin/shackles/head_lusty.png"), 
    (0, 0), "tojc_blink", 
    (0, 0), ConditionSwitch( 
        "tojc_face == 'neutral'", "bk3/jin/shackles/minipixel.png", 
        "tojc_face == 'lookdown'", "bk3/jin/shackles/minipixel.png", 
        "tojc_face == 'blindfold'", "bk3/jin/shackles/head_blindfold.png",       
        "tojc_face == 'lusty'", "bk3/jin/shackles/minipixel.png"), 
    )

image tojc_blink:
    "bk3/jin/shackles/minipixel.png"
    0.3
    "bk3/jin/shackles/blink.png"
    0.3
    "bk3/jin/shackles/minipixel.png"
    4.0
    "bk3/jin/shackles/blink.png"
    0.3
    "bk3/jin/shackles/minipixel.png"
    7.0
    repeat

image tojc_dildo:
    "bk3/jin/shackles/dildo1.png"
    0.3
    "bk3/jin/shackles/dildo2.png"
    0.3
    "bk3/jin/shackles/dildo3.png"
    0.3
    "bk3/jin/shackles/dildo4.png"
    0.3
    "bk3/jin/shackles/dildo5.png"
    0.3
    "bk3/jin/shackles/dildo4.png"
    0.3
    "bk3/jin/shackles/dildo3.png"
    0.3
    "bk3/jin/shackles/dildo2.png"
    0.3
    repeat

image tojc_dildo_2:
    "bk3/jin/shackles/dildo1.png"
    0.3
    "tojc tojc14" with hpunch
    1.3
    "bk3/jin/shackles/dildo4.png"
    0.3
    "bk3/jin/shackles/dildo3.png"
    0.3
    "bk3/jin/shackles/dildo2.png"
    0.3
    repeat


image tojc tojc100:

    "tojc tojc01"
    0.2
    "tojc tojc02"
    0.2
    "tojc tojc03"
    0.2
    "tojc tojc04"
    0.2
    "tojc tojc05"
    0.2
    "tojc tojc04"
    0.2
    "tojc tojc03"
    0.2
    "tojc tojc02"
    0.2
    repeat

image tojc tojc101:

    "tojc tojc01"
    0.2
    "tojc tojc06" with hpunch
    1.2
    "tojc tojc05"
    0.2
    "tojc tojc04"
    0.2
    "tojc tojc03"
    0.2
    "tojc tojc02"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
