
















image hypno_ball = "bk3/hypno/ball1.png"
image hypno_rail = "bk3/hypno/frontrail.png"



init:
    $ tohy_junedress_on = False










image tohy joodee01 = LiveComposite(

    (1000, 720),

    (0, 0), "bk3/hypno/joodee/sclera.png",

    (0, 0), "bk3/hypno/joodee/eyes_norm.png", 

    (0, 0), "bk3/hypno/joodee/body1.png", 

    (690, 164), "tohy_joodee_blink",

    )



image tohy joodee02 = LiveComposite(

    (1000, 720),

    (0, 0), "bk3/hypno/joodee/body1.png",

    (0, 0), "bk3/hypno/joodee/eyes_hypno.png", 

    (690, 164), "tohy_joodee_blink",

    )



image tohy joodee03 = LiveComposite(

    (1000, 720),

    (0, 0), "bk3/hypno/joodee/body2.png",

    (0, 0), "bk3/hypno/joodee/eyes_hypno.png",     

    )



image tohy joodee04 = LiveComposite(

    (1000, 720),

    (0, 0), "bk3/hypno/joodee/body2.png",

    (0, 0), "bk3/hypno/joodee/eyes_hypno.png",

    (0, 0), "bk3/hypno/joodee/underwear.png",    

    )



image tohy_joodee_blink:

    "bk3/hypno/joodee/blink.png"

    0.2

    "bk3/hypno/joodee/minipixel.png"

    0.2

    "bk3/hypno/joodee/blink.png"

    0.2

    "bk3/hypno/joodee/minipixel.png"

    3.0

    "bk3/hypno/joodee/blink.png"

    0.2

    "bk3/hypno/joodee/minipixel.png"

    6.0

    repeat



image tohy_joodee_eyewest:

    "bk3/hypno/joodee/eye_west.png"

    xpos 718 ypos 200

    linear 2.0 xpos 707

    linear 2.0 xpos 718

    repeat



image tohy_joodee_eyeeast:

    "bk3/hypno/joodee/eye_east.png"

    xpos 773 ypos 200

    linear 2.0 xpos 755

    linear 2.0 xpos 773

    repeat



image tohy suki01 = "bk3/hypno/suki/body1.png"

image tohy suki02 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/suki/body1.png",
    (0, 0), "bk3/hypno/suki/eyes_hypno.png", 
    )

image tohy suki03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/suki/body2.png",
    (0, 0), "bk3/hypno/suki/eyes_hypno.png", 
    )

image tohy suki04 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/suki/body2.png",
    (0, 0), "bk3/hypno/suki/eyes_hypno.png",
    (0, 0), "bk3/hypno/suki/underwear.png",
    )

image tohy suki05 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/suki/body2.png",
    (0, 0), "bk3/hypno/suki/underwear.png",
    )

image tohy suki06 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/suki/body2.png",
    )

image tohy_suki_blink:
    xpos 690 ypos 178
    "bk3/hypno/suki/blink.png"
    0.2
    "transparent.png"
    0.2
    "bk3/hypno/suki/blink.png"
    0.2
    "transparent.png"
    3.0
    "bk3/hypno/suki/blink.png"
    0.2
    "transparent.png"
    6.0
    repeat


image tohy_suki_eyewest:
    "bk3/hypno/suki/eye_west.png"
    xpos 710 ypos 195
    linear 2.0 xpos 700
    linear 2.0 xpos 710
    repeat

image tohy_suki_eyeeast:
    "bk3/hypno/suki/eye_east.png"
    xpos 764 ypos 200
    linear 2.0 xpos 750
    linear 2.0 xpos 764
    repeat














image tohy june01 = LiveComposite(
    (1000,720),
    (0, 0), ConditionSwitch(        
        "tohy_junedress_on == True", "bk3/hypno/june/body_dress.png",       
        "tohy_junedress_on == False","bk3/hypno/june/body1.png"),   
    )

image tohy june02 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(        
        "tohy_junedress_on == True", "bk3/hypno/june/body_dress.png",       
        "tohy_junedress_on == False","bk3/hypno/june/body1.png"),   
    (0, 0), "bk3/hypno/june/eyes_hypno.png", 
    )

image tohy june03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/june/body2.png",
    (0, 0), "bk3/hypno/june/eyes_hypno.png", 
    )


image tohy_june_blink:
    xpos 695 ypos 175
    "bk3/hypno/june/blink.png"
    0.2
    "transparent.png"
    0.2
    "bk3/hypno/june/blink.png"
    0.2
    "transparent.png"
    3.0
    "bk3/hypno/june/blink.png"
    0.2
    "transparent.png"
    6.0
    repeat

image tohy_june_eyesnorm:
    "bk3/hypno/june/eyes_norm.png"
    xpos 695 ypos 175


image tohy_june_eyeshypno:
    "tohy_june_blink"
    0.3
    xpos 697 ypos 177
    "bk3/hypno/june/eyes_hypno.png"
    alpha 0.5


image tohy_june_eyeeast:
    "bk3/hypno/june/eye_east.png"
    xpos 768 ypos 197
    linear 2.0 xpos 755
    linear 2.0 xpos 768
    repeat




image tohy jin01 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/jin/body2.png",
    (0, 0), "bk3/hypno/jin/body1.png",
    )

image tojn_hypno_eyes = "bk3/hypno/jin/eyes_hypno_idle.png"

image tohy jin02 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/jin/body2.png",
    (0, 0), "bk3/hypno/jin/body1.png",
    (0, 0), "bk3/hypno/jin/eyes_hypno.png", 
    )

image tohy jin03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/jin/body2.png",
    (0, 0), "bk3/hypno/jin/eyes_hypno.png", 
    )

image tohy jin04 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/hypno/jin/body2.png",
    (0, 0), "bk3/hypno/jin/eyes_hypno.png",
    
    )





image tohy_jin_blink:
    xpos 690 ypos 178
    "bk3/hypno/jin/blink.png"
    0.2
    "transparent.png"
    0.2
    "bk3/hypno/suki/blink.png"
    0.2
    "transparent.png"
    3.0
    "bk3/hypno/suki/blink.png"
    0.2
    "transparent.png"
    6.0
    repeat


image tohy_jin_eyewest:
    "bk3/hypno/jin/eye_west.png"
    xpos 709 ypos 199
    linear 2.0 xpos 698
    linear 2.0 xpos 709
    repeat

image tohy_jin_eyeeast:
    "bk3/hypno/jin/eye_east.png"
    xpos 764 ypos 198
    linear 2.0 xpos 750
    linear 2.0 xpos 764
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
