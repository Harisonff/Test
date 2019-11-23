






init:
    $ tokh_face = 'none'
    $ tokh_titsize = 'medium'

image tokh tokh01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat.png", 
    (0, 0), "bk3/katara/handjob/kat_arm_0.png",
    (0, 0), "tokh_tits",   
    )


image tokh tokh02 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat.png", 
    (0, 0), "bk3/katara/handjob/kat_arm_0.png",
    (0, 0), "bk3/katara/handjob/body_aang.png",
     (0, 0), "bk3/katara/handjob/aang_solodick.png",        
    (0, 0), "tokh_tits",
    )
image tokh tokh04 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat.png",
    (0, 0), "bk3/katara/handjob/body_aang.png",
    (402, 297), "bk3/katara/handjob/kat_arm_1.png",
    (0, 0), "tokh_tits",    
    
    )
image tokh tokh05 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat.png",
    (0, 0), "bk3/katara/handjob/body_aang.png",
    (402, 297), "bk3/katara/handjob/kat_arm_2.png",
    (0, 0), "tokh_tits",    

    )
image tokh tokh06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat.png", 
    (0, 0), "bk3/katara/handjob/body_aang.png",
    (402, 297), "bk3/katara/handjob/kat_arm_3.png",
    (0, 0), "tokh_tits",    
    )

image tokh tokh10 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat_stand.png",  
    (0, 0), "bk3/katara/handjob/panties_on.png",
    (0, 0), "bk3/katara/handjob/body_aang.png",
    (0, 0), "bk3/katara/handjob/aang_solodick.png",        
    )
image tokh tokh11 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat_stand.png",  
    (0, 0), "bk3/katara/handjob/panties_off.png",
    (0, 0), "bk3/katara/handjob/body_aang.png",
    (0, 0), "bk3/katara/handjob/aang_solodick.png",        
    )
image tokh tokh12 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/katara/handjob/body_kat_stand.png",  
    (0, 0), "bk3/katara/handjob/panties_off.png",
    (0, 0), "bk3/katara/handjob/body_aang.png",
    (0, 0), "bk3/katara/handjob/aang_solodick.png",   
    (0, 0), "bk3/katara/handjob/jackhand.png",  
    )


image tokh_head_1 = LiveComposite(
    (260, 302), 
    (0, 0), "bk3/katara/handjob/kat_head.png",
    (0, 0), ConditionSwitch(        
        "tokh_face == 'lewd'", "bk3/katara/handjob/face_lewd.png",
        "tokh_face == 'eyesoncock'", "bk3/katara/handjob/face_eyeoncock.png",
        "tokh_face == 'worried'", "bk3/katara/handjob/face_worried.png",        
        "tokh_face == 'none'", "transparent.png"), 
    (0, 0), "tokh_blink_ani",    
    (0, 0), "bk3/katara/handjob/kat_bang_1.png",
    )
image tokh_head_2 = LiveComposite(
    (260, 302), 
    (0, 0), "bk3/katara/handjob/kat_head.png",
    (0, 0), ConditionSwitch(        
        "tokh_face == 'lewd'", "bk3/katara/handjob/face_lewd.png",
        "tokh_face == 'eyesoncock'", "bk3/katara/handjob/face_eyeoncock.png",
        "tokh_face == 'worried'", "bk3/katara/handjob/face_worried.png",        
        "tokh_face == 'none'", "transparent.png"), 
    (0, 0), "tokh_blink_ani",    
    (0, 0), "tokh_bangs",
    )

image tokh_tits = LiveComposite(
    (1000, 720), 
    
    (0, 0), ConditionSwitch(        
        "tokh_titsize == 'small'", "bk3/katara/handjob/kat_tits_small.png",
        "tokh_titsize == 'medium'", "bk3/katara/handjob/kat_tits_medium.png",                
        "tokh_titsize == 'big'",    "bk3/katara/handjob/kat_tits_big.png"),     
    )











image tokh_bangs:
    "bk3/katara/handjob/kat_bang_1.png"
    1.0
    "bk3/katara/handjob/kat_bang_2.png"
    1.0
    repeat

image tokh tokh100:
    "tokh tokh04"
    0.4
    "tokh tokh05"
    0.4
    "tokh tokh06"
    0.4
    "tokh tokh05"
    0.4
    repeat

image tokh tokh101:
    "tokh tokh04"
    0.3
    "tokh tokh05"
    0.3
    "tokh tokh06"
    0.3
    "tokh tokh05"
    0.3
    repeat

image tokh_blink_ani:
    "bk3/katara/handjob/transparent.png"
    1.0
    "bk3/katara/handjob/blink.png"
    0.3
    "bk3/katara/handjob/transparent.png"
    6.0
    "bk3/katara/handjob/blink.png"
    0.3
    repeat

image tokh arm_hj:
    "bk3/katara/handjob/kat_arm_4.png"
    .5
    "bk3/katara/handjob/kat_arm_5.png"
    .5
    "bk3/katara/handjob/kat_arm_6.png"
    .5
    "bk3/katara/handjob/kat_arm_5.png"
    .5
    repeat

image tokh arm_hj2:
    "bk3/katara/handjob/kat_arm_4.png"
    .3
    "bk3/katara/handjob/kat_arm_5.png"
    .3
    "bk3/katara/handjob/kat_arm_6.png"
    .3
    "bk3/katara/handjob/kat_arm_5.png"
    .3
    repeat

image tokh arm_hj3:
    "bk3/katara/handjob/kat_arm_4.png"
    .2
    "bk3/katara/handjob/kat_arm_5.png"
    .15
    "bk3/katara/handjob/kat_arm_6.png"
    .2
    "bk3/katara/handjob/kat_arm_5.png"
    .15
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
