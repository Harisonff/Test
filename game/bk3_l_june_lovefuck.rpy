


init:

    $ totp_preg = False

image totp totp00 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/body_0.png", 
    (0, 0), "bk3/june/lovefuck/head_eyeonplayer.png",    
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_0.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"), 
    (516, 139), "totp_blink",
    )

image totp totp01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/body_1.png", 
    (0, 0), "bk3/june/lovefuck/body_upper_1.png",    
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_1.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"), 
    (516, 139), "totp_blink",
    )


image totp totp02 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/june/lovefuck/body_2.png",
    (0, 0), "bk3/june/lovefuck/body_upper_1.png",     
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_1.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"),  
    (516, 139), "totp_blink",
    )


image totp totp03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/lovefuck/body_2.png",
    (0, 0), "bk3/june/lovefuck/body_upper_2.png",
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_2.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"),
    (516, 139), "totp_blink",
    )


image totp totp04 = LiveComposite(
    (1000, 720),   
    (0, -100), "bk3/june/lovefuck/bg_bed.jpg",
    (0, 0), "bk3/june/lovefuck/body_3.png",
    (0, 0), "bk3/june/lovefuck/body_upper_2.png",    
    (0, 0), "bk3/june/lovefuck/head_shock.png",   
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/fuckp_6.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/fuck_6.png"), 
       
    )

image totp totp04_1 = LiveComposite(
    (1000, 720),   
    (0, -100), "bk3/june/lovefuck/bg_bed.jpg",
    (0, 0), "bk3/june/lovefuck/body_3.png",
    (0, 0), "bk3/june/lovefuck/body_upper_2.png",    
    (0, 0), "bk3/june/lovefuck/head_shock_2.png",   
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/fuckp_6.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/fuck_6.png"), 
       
    )

image totp totp04_2 = LiveComposite(
    (1000, 720),   
    (0, -100), "bk3/june/lovefuck/bg_bed.jpg",
    (0, 0), "bk3/june/lovefuck/body_3.png",
    (0, 0), "bk3/june/lovefuck/body_upper_2.png",    
    (0, 0), "bk3/june/lovefuck/head_shock_3.png",   
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/fuckp_6.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/fuck_6.png"), 
       
    )

image totp totp05 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/lovefuck/body_2.png",
    (0, 0), "bk3/june/lovefuck/body_upper_2.png",
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_2.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"),
    (0, 0), "bk3/june/lovefuck/head_shock_2.png", 
    (516, 139), "bk3/june/lovefuck/blink.png",
    )

image totp totp06 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/lovefuck/body_2.png",
    (0, 0), "bk3/june/lovefuck/body_upper_2.png",
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_2.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"),
    (0, 0), "bk3/june/lovefuck/head_shock_2.png",     
    )

image totp totp07 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/lovefuck/body_1.png",
    (0, 0), "bk3/june/lovefuck/body_upper_1.png",
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "bk3/june/lovefuck/pubes_1.png",        
        "june_pubes == 'shaven'", "bk3/june/lovefuck/minipixel.png"),
    (0, 0), "bk3/june/lovefuck/head_shock_3.png",     
    )

image totp_sex totp_stare = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/june/lovefuck/head_eyeonplayer.png", 
    (516, 139), "totp_blink",
    )



image totp_sex totp_fuck = LiveComposite(
    (1000, 720),    
    
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "totp_fuckp",        
        "june_pubes == 'shaven'", "totp_fuck"),    
    )

image totp_sex totp_rub = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "totp_rubp",        
        "june_pubes == 'shaven'", "totp_rub"),    
    )

image totp_sex totp_fuckhard = LiveComposite(
    (1000, 720), 
    (0, 0), "totp totp03",    
    (0, 0), ConditionSwitch(        
        "june_pubes == 'bush'", "totp_fuckp2",        
        "june_pubes == 'shaven'", "totp_fuck2"),    
    )








image totp_shock1 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_1.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock2 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_2.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock3 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_3.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock4 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_4.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock5 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_5.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")

image totp_medium1 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_1.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium2 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_2.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium3 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_3.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium4 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_4.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium5 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_5.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")

image totp_mild1 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_1.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild2 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_2.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild3 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_3.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild4 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_4.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild5 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuck_5.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")


image totp_shock1p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_1.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock2p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_2.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock3p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_3.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock4p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_4.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")
image totp_shock5p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_5.png",
    (0, 0), "bk3/june/lovefuck/head_shock.png")

image totp_medium1p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_1.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium2p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_2.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium3p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_3.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium4p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_4.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")
image totp_medium5p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_5.png",
    (0, 0), "bk3/june/lovefuck/head_shock_2.png")

image totp_mild1p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_1.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild2p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_2.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild3p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_3.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild4p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_4.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")
image totp_mild5p = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/june/lovefuck/fuckp_5.png",
    (0, 0), "bk3/june/lovefuck/head_shock_3.png")



image totp_fuck2:
    "bk3/june/lovefuck/fuck_1.png"
    0.2
    "totp totp04" with vpunch
    1.2
    "bk3/june/lovefuck/fuck_5.png"
    0.2
    "bk3/june/lovefuck/fuck_4.png"
    0.2
    "bk3/june/lovefuck/fuck_3.png"
    0.2
    "bk3/june/lovefuck/fuck_2.png"
    0.2
    repeat

image totp_fuck2_1:
    "totp totp04" with vpunch
    1.2
    "totp_shock5"
    0.19
    "totp_medium4"
    0.19
    "totp_medium3"
    0.19
    "totp_medium2"
    0.19
    "totp_medium1"
    0.2
    repeat

image totp_fuck2_2:
    "totp_shock5"
    0.16
    "totp_medium4"
    0.16
    "totp_medium3"
    0.16
    "totp_medium2"
    0.16
    "totp_medium1"
    0.18
    "totp totp04" with vpunch
    1
    repeat

image totp_fuck2_3:
    "totp totp04_1" with vpunch
    1.2
    "totp_medium5"
    0.19
    "totp_medium4"
    0.19
    "totp_medium3"
    0.19
    "totp_medium2"
    0.19
    "totp_medium1"
    0.2
    repeat

image totp_fuck2_3_1:
    "totp totp04_1" with vpunch
    0.8
    "totp_medium5"
    0.14
    "totp_medium4"
    0.14
    "totp_medium3"
    0.14
    "totp_medium2"
    0.14
    "totp_medium1"
    0.18
    repeat

image totp_fuck2_4:
    "totp totp04_2" with vpunch
    1.2
    "totp_mild5"
    0.19
    "totp_mild4"
    0.19
    "totp_mild3"
    0.19
    "totp_mild2"
    0.19
    "totp_mild1"
    0.2
    repeat

image totp_fuck2_4_1:
    "totp totp04_2" with vpunch
    0.7
    "totp_mild5"
    0.13
    "totp_mild4"
    0.13
    "totp_mild3"
    0.13
    "totp_mild2"
    0.13
    "totp_mild1"
    0.17
    repeat



image totp_fuck2_1p:
    "totp totp04" with vpunch
    1.2
    "totp_shock5p"
    0.19
    "totp_medium4p"
    0.19
    "totp_medium3p"
    0.19
    "totp_medium2p"
    0.19
    "totp_medium1p"
    0.2
    repeat

image totp_fuck2_2p:
    "totp_shock5p"
    0.16
    "totp_medium4p"
    0.16
    "totp_medium3p"
    0.16
    "totp_medium2p"
    0.16
    "totp_medium1p"
    0.18
    "totp totp04" with vpunch
    1
    repeat

image totp_fuck2_3p:
    "totp totp04_1" with vpunch
    1.2
    "totp_medium5p"
    0.19
    "totp_medium4p"
    0.19
    "totp_medium3p"
    0.19
    "totp_medium2p"
    0.19
    "totp_medium1p"
    0.2
    repeat

image totp_fuck2_3_1p:
    "totp totp04_1" with vpunch
    0.8
    "totp_medium5p"
    0.14
    "totp_medium4p"
    0.14
    "totp_medium3p"
    0.14
    "totp_medium2p"
    0.14
    "totp_medium1p"
    0.18
    repeat

image totp_fuck2_4p:
    "totp totp04_2" with vpunch
    1.2
    "totp_mild5p"
    0.19
    "totp_mild4p"
    0.19
    "totp_mild3p"
    0.19
    "totp_mild2p"
    0.19
    "totp_mild1p"
    0.2
    repeat

image totp_fuck2_4_1p:
    "totp totp04_2" with vpunch
    0.7
    "totp_mild5p"
    0.13
    "totp_mild4p"
    0.13
    "totp_mild3p"
    0.13
    "totp_mild2p"
    0.13
    "totp_mild1p"
    0.17
    repeat




image totp_fuckp2:
    "bk3/june/lovefuck/fuckp_1.png"
    0.2
    "totp totp04" with vpunch
    1.2
    "bk3/june/lovefuck/fuckp_5.png"
    0.2
    "bk3/june/lovefuck/fuckp_4.png"
    0.2
    "bk3/june/lovefuck/fuckp_3.png"
    0.2
    "bk3/june/lovefuck/fuckp_2.png"
    0.2
    repeat

image totp_fuck:
    "bk3/june/lovefuck/fuck_1.png"
    0.2
    "bk3/june/lovefuck/fuck_2.png"
    0.2
    "bk3/june/lovefuck/fuck_3.png"
    0.2
    "bk3/june/lovefuck/fuck_4.png"
    0.2
    "bk3/june/lovefuck/fuck_5.png"
    0.2
    "bk3/june/lovefuck/fuck_6.png"
    0.2
    "bk3/june/lovefuck/fuck_5.png"
    0.2
    "bk3/june/lovefuck/fuck_4.png"
    0.2
    "bk3/june/lovefuck/fuck_3.png"
    0.2
    "bk3/june/lovefuck/fuck_2.png"
    0.2
    repeat

image totp_fuckp:
    "bk3/june/lovefuck/fuckp_1.png"
    0.2
    "bk3/june/lovefuck/fuckp_2.png"
    0.2
    "bk3/june/lovefuck/fuckp_3.png"
    0.2
    "bk3/june/lovefuck/fuckp_4.png"
    0.2
    "bk3/june/lovefuck/fuckp_5.png"
    0.2
    "bk3/june/lovefuck/fuckp_6.png"
    0.2
    "bk3/june/lovefuck/fuckp_5.png"
    0.2
    "bk3/june/lovefuck/fuckp_4.png"
    0.2
    "bk3/june/lovefuck/fuckp_3.png"
    0.2
    "bk3/june/lovefuck/fuckp_2.png"
    0.2
    repeat

image totp_rub:
    "bk3/june/lovefuck/rub_1.png"
    0.2
    "bk3/june/lovefuck/rub_2.png"
    0.2
    "bk3/june/lovefuck/rub_3.png"
    0.2
    "bk3/june/lovefuck/rub_4.png"
    0.2
    "bk3/june/lovefuck/rub_5.png"
    0.2
    "bk3/june/lovefuck/rub_6.png"
    0.2
    "bk3/june/lovefuck/rub_5.png"
    0.2
    "bk3/june/lovefuck/rub_4.png"
    0.2
    "bk3/june/lovefuck/rub_3.png"
    0.2
    "bk3/june/lovefuck/rub_2.png"
    0.2
    repeat

image totp_rubp:
    "bk3/june/lovefuck/rubp_1.png"
    0.2
    "bk3/june/lovefuck/rubp_2.png"
    0.2
    "bk3/june/lovefuck/rubp_3.png"
    0.2
    "bk3/june/lovefuck/rubp_4.png"
    0.2
    "bk3/june/lovefuck/rubp_5.png"
    0.2
    "bk3/june/lovefuck/rubp_6.png"
    0.2
    "bk3/june/lovefuck/rubp_5.png"
    0.2
    "bk3/june/lovefuck/rubp_4.png"
    0.2
    "bk3/june/lovefuck/rubp_3.png"
    0.2
    "bk3/june/lovefuck/rubp_2.png"
    0.2
    repeat

image totp_blink:
    "bk3/june/lovefuck/minipixel.png"
    1.0
    "bk3/june/lovefuck/blink.png"
    0.3
    "bk3/june/lovefuck/minipixel.png"
    1.0
    "bk3/june/lovefuck/blink.png"
    0.3
    "bk3/june/lovefuck/minipixel.png"
    3.0
    "bk3/june/lovefuck/blink.png"
    0.3
    "bk3/june/lovefuck/minipixel.png"
    9.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
