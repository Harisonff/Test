







init:
    $ tojp_jinhead = 'none'






image tojp tojp01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (270, 0), "tojp_head_1", 
    (0, 0), "bk3/jin/fuck/body_jin_1.png",
    (0, 0), "bk3/jin/fuck/dick_1.png", 
    )
image tojp tojp02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (250, -15), "tojp_head_1", 
    (0, 0), "bk3/jin/fuck/body_jin_2.png",
    (0, 0), "bk3/jin/fuck/dick_2.png", 
    )
image tojp tojp03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (200, -50), "tojp_head_1", 
    (0, 0), "bk3/jin/fuck/body_jin_3.png",
    (0, 0), "bk3/jin/fuck/dick_3.png", 
    )
image tojp tojp04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (170, -70), "tojp_head_1", 
    (0, 0), "bk3/jin/fuck/body_jin_4.png",
    (0, 0), "bk3/jin/fuck/dick_4.png", 
    )

image tojp tojp06 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (200, -50), "bk3/jin/fuck/braids.png",
    (200, -50), "tojp_head_2", 
    (0, 0), "bk3/jin/fuck/body_jin_3.png",
    (0, 0), "bk3/jin/fuck/dick_3.png", 
    )
image tojp tojp07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (260, -40), "bk3/jin/fuck/braids2.png",
    (250, -15), "tojp_head_2", 
    (0, 0), "bk3/jin/fuck/body_jin_2.png",
    (0, 0), "bk3/jin/fuck/dick_2.png", 
    )
image tojp tojp08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (310, -30), "bk3/jin/fuck/braids3.png",
    (270, 0), "tojp_head_2", 
    (0, 0), "bk3/jin/fuck/body_jin_1.png",
    (0, 0), "bk3/jin/fuck/dick_1.png", 
    )

image tojp tojp11 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (0, 0), "bk3/jin/fuck/dick_upright.png",     
    )

image tojp tojp12 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (170, -70), "tojp_head_1",  
    (0, 0), "bk3/jin/fuck/body_jin_4.png",
    (0, 0), "bk3/jin/fuck/dick_upright.png",
    )
image tojp tojp13 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",
    (170, -70), "tojp_head_1",  
    (0, 0), "bk3/jin/fuck/body_jin_4.png",
    (0, 0), "bk3/jin/fuck/dick_cum_outside.png",
    )


image tojp tojp15 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",   
    (0, 0), "bk3/jin/fuck/body_jin_0.png",
    (0, 0), "bk3/jin/fuck/arm.png",
    (0, 0), "tojp_head_b",
    (0, 0), "bk3/jin/fuck/dick_upright.png",
    )

image tojp tojp16 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",   
    (0, 0), "bk3/jin/fuck/body_jin_0.png",
    (0, 0), "bk3/jin/fuck/arm.png",
    (0, 0), "tojp_head_b",
    (0, 0), "bk3/jin/fuck/dick_cum_outside.png",
    )

image tojp tojp17 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",   
    (0, 0), "bk3/jin/fuck/body_jin_0.png",
    (0, 2), "bk3/jin/fuck/arm.png",
    (8, 14), "tojp_head_b",
    (0, 0), "bk3/jin/fuck/suck1.png",
    )
image tojp tojp18 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",   
    (0, 0), "bk3/jin/fuck/body_jin_0.png",
    (1, 5), "bk3/jin/fuck/arm.png",
    (5,35), "tojp_head_b",
    (0, 0), "bk3/jin/fuck/suck2.png",
    )
image tojp tojp19 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/aang_body.png",   
    (0, 0), "bk3/jin/fuck/body_jin_0.png",
    (2, 7), "bk3/jin/fuck/arm.png",
    (17, 55), "tojp_head_b",
    (0, 0), "bk3/jin/fuck/suck3.png",
    )




image tojp_head_1 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/head_1.png",
    (0, 0), ConditionSwitch(        
        "tojp_jinhead == 'none'",  "transparent.png",  
        "tojp_jinhead == 'lusty'",  "bk3/jin/fuck/face_lusty.png",
        "tojp_jinhead == 'blink'",  "bk3/jin/fuck/blink.png",),
     (0, 0), "tojp_blink_ani",
    )

image tojp_head_2 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/head_2.png",    
    (0, 0), ConditionSwitch(        
        "tojp_jinhead == 'none'",  "transparent.png",
        "tojp_jinhead == 'lusty'",  "bk3/jin/fuck/face_lusty.png", 
        "tojp_jinhead == 'blink'",  "bk3/jin/fuck/blink.png",),
    (0, 0), "bk3/jin/fuck/head_bangs.png",
    (0, 0), "tojp_blink_ani",
    
    )

image tojp_head_b = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/jin/fuck/headb_1.png",    
    (0, 0), ConditionSwitch(        
        "tojp_jinhead == 'none'",  "transparent.png", 
        "tojp_jinhead == 'front'",  "bk3/jin/fuck/eyefrontb.png", 
        "tojp_jinhead == 'blink'", "bk3/jin/fuck/blinkb.png",),
        
    )




image tojp tojp100:

    "tojp tojp01"
    0.3
    "tojp tojp02"
    0.3
    "tojp tojp03"
    0.3
    "tojp tojp04"
    0.3
    "tojp tojp06"
    0.3
    "tojp tojp07"
    0.2
    "tojp tojp08"
    0.3
    repeat

image tojp tojp101:
    "tojp tojp01"
    0.3
    "tojp tojp02"
    0.3
    "tojp tojp03"
    0.3
    "tojp tojp04"
    0.3
    "tojp tojp08" with hpunch
    1.2
    repeat

image tojp tojp101_1:
    "tojp tojp01"
    0.2
    "tojp tojp02"
    0.2
    "tojp tojp03"
    0.2
    "tojp tojp04"
    0.2
    "tojp tojp08" with hpunch
    0.8
    repeat

image tojp tojp102:

    "tojp tojp01"
    0.3
    "tojp tojp02"
    0.3
    "tojp tojp03"
    0.3
    "tojp tojp02"
    0.3
    repeat

image tojp tojp103:

    "tojp tojp17"
    0.3
    "tojp tojp18"
    0.3
    "tojp tojp19"
    0.3
    "tojp tojp18"
    0.3
    repeat

image tojp tojp103_1:

    "tojp tojp17"
    0.2
    "tojp tojp18"
    0.15
    "tojp tojp19"
    0.2
    "tojp tojp18"
    0.15
    repeat

image tojp_blink_ani:
    "transparent.png"
    2.0
    "bk3/jin/fuck/blink.png"
    0.3
    "transparent.png"
    8.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
