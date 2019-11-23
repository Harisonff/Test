



init:
    $ june_pubes = 'bush'
    $ totj_hairlock = 'on'





image totj totj00 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headfront_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    )

image totj totj01 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headside_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    )

image totj totj02 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headside_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png",    
    )

image totj totj03 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headside_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    (0, 0), "bk3/june/tug/solodick.png", 
    )

image totj totj04 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",   
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headside_lock", 
    (607, 194), "bk3/june/tug/tug_left1.png", 
    )

image totj totj05 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",    
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headside_lock", 
    (607, 194), "totj_tug_left", 
    )

image totj totj13 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",    
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headside_lock", 
    (607, 194), "totj_tug_left_fast", 
    )


image totj totj06 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/tug/body.png",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headfront_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    )

image totj totj07 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",    
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headfront_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    (0, 0), "bk3/june/tug/arm_right_rest.png",
    (0, 0), "bk3/june/tug/solodick.png",
    )


image totj totj08 = LiveComposite(  
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "bk3/june/tug/head_front_eyesup.png",
    (597, 197), "totj_frontblink",
    (0, 0), ConditionSwitch(        
        "totj_hairlock == 'on'", "bk3/june/tug/head_front_lockon.png",        
        "totj_hairlock == 'off'", "bk3/june/tug/head_front_lockoff.png"),
    (0, 0), "bk3/june/tug/arm_left_rest.png",     
    )

image totj totj09 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",      
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    (518, 334), "totj_tug_right", 
    (0, 0), "totj_headfront_lock", 
    )

image totj totj10 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",      
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    (518, 334), "totj_tug_right_fast",   
    (0, 0), "totj_headfront_lock", 
    )

image totj totj11 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "totj_headfront_lock", 
    (0, 0), "bk3/june/tug/arm_left_rest.png", 
    (518, 334), "bk3/june/tug/tug_right1.png", 
    )

image totj totj12 = LiveComposite(
    (1000, 720),
    (0, 0), "totj_body",  
    (0, 0), "bk3/june/tug/arm_right_rest.png", 
    (0, 0), "totj_headsuck", 
    (0, 0), "bk3/june/tug/arm_left_rest.png",    
    )




















image totj_tug_left:
    "bk3/june/tug/tug_left1.png"
    0.2
    "bk3/june/tug/tug_left2.png",
    0.2
    "bk3/june/tug/tug_left3.png",
    0.2
    "bk3/june/tug/tug_left4.png",
    0.2
    "bk3/june/tug/tug_left5.png",
    0.2
    "bk3/june/tug/tug_left4.png",
    0.2
    "bk3/june/tug/tug_left3.png",
    0.2
    "bk3/june/tug/tug_left2.png",
    0.2
    repeat

image totj_tug_left_fast:
    "bk3/june/tug/tug_left1.png"
    0.1
    "bk3/june/tug/tug_left2.png",
    0.1
    "bk3/june/tug/tug_left4.png",
    0.1
    "bk3/june/tug/tug_left5.png",
    0.1
    "bk3/june/tug/tug_left4.png",
    0.1
    "bk3/june/tug/tug_left3.png",
    0.1
    "bk3/june/tug/tug_left2.png",
    0.1
    repeat

image totj_tug_right:
    "bk3/june/tug/tug_right1.png"
    0.3
    "bk3/june/tug/tug_right2.png",
    0.2
    "bk3/june/tug/tug_right3.png",
    0.3
    "bk3/june/tug/tug_right2.png",
    0.2
    repeat

image totj_tug_right_fast:
    "bk3/june/tug/tug_right1.png"
    0.1


    "bk3/june/tug/tug_right3.png",
    0.1
    "bk3/june/tug/tug_right2.png",
    0.1
    repeat

image totj_sideblink:
    "bk3/june/tug/sideblink.png"
    0.2
    "bk3/june/tug/minipixel.png"
    5.0
    repeat

image totj_headside_lockon = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/tug/head_side.png",
    (571, 193), "totj_sideblink", 
    (0, 0), "bk3/june/tug/head_side_lockon.png",    
    )

image totj_headside_lock = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/tug/head_side.png",
    (571, 193), "totj_sideblink", 
    (0, 0), ConditionSwitch(        
        "totj_hairlock == 'on'", "bk3/june/tug/head_side_lockon.png",        
        "totj_hairlock == 'off'", "bk3/june/tug/head_side_lockoff.png"),  
    )

image totj_frontblink:
    "bk3/june/tug/frontblink.png"
    0.2
    "bk3/june/tug/minipixel.png"
    0.3
    "bk3/june/tug/frontblink.png"
    0.2
    "bk3/june/tug/minipixel.png"
    7.0
    "bk3/june/tug/frontblink.png"
    0.2
    "bk3/june/tug/minipixel.png"
    8.0
    repeat


image totj_headfront_lock = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/tug/head_front.png",
    (597, 197), "totj_frontblink", 
    (0, 0), ConditionSwitch(        
        "totj_hairlock == 'on'", "bk3/june/tug/head_front_lockon.png",        
        "totj_hairlock == 'off'", "bk3/june/tug/head_front_lockoff.png"),
    )

image totj_headsuck = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/tug/head_suck.png",    
    (5, 45), ConditionSwitch(        
        "totj_hairlock == 'on'", "bk3/june/tug/head_front_lockon.png",        
        "totj_hairlock == 'off'", "bk3/june/tug/head_front_lockoff.png"),
    )

image totj_body = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/june/tug/body.png",  
    (0, 0), ConditionSwitch(        
        "june_pubes == 'shaven'", "bk3/june/tug/minipixel.png",        
        "june_pubes == 'bush'", "bk3/june/tug/pubes.png"),
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
