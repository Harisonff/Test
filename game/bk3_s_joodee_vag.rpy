






init:
    $ joodee_vag_titpull = False


image tojv tojv01 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (5, 0), "bk3/joodee/vaginal/leg_closed.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), "bk3/joodee/vaginal/face_eyesup.png",
    (5, 0), "tojv_blink_ani",
    )

image tojv tojv02 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), "bk3/joodee/vaginal/face_eyesup.png",
    (5, 0), "tojv_blink_ani",
    )

image tojv tojv03 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), "bk3/joodee/vaginal/solodick.png",
    )

image tojv tojv05 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), "bk3/joodee/vaginal/penetrate_1.png",
    )

image tojv tojv05_1 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), "bk3/joodee/vaginal/face_shock.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "bk3/joodee/vaginal/face_shock.png",
        "joodee_vag_titpull == False", "transparent.png"), 
    
    (5, 0), "bk3/joodee/vaginal/penetrate_1.png",
    )

image tojv tojv06 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), "bk3/joodee/vaginal/penetrate_2.png",
    )

image tojv tojv06_1 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), "bk3/joodee/vaginal/face_shock.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "bk3/joodee/vaginal/face_shock.png",
        "joodee_vag_titpull == False", "transparent.png"), 
    (5, 0), "bk3/joodee/vaginal/penetrate_2.png",
    )

image tojv tojv07 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",    
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), "bk3/joodee/vaginal/penetrate_3.png",
    )

image tojv tojv07_1 = LiveComposite(
    (1000, 720),
    (5, 0), "bk3/joodee/vaginal/body.png",    
    (655, 0), "bk3/joodee/vaginal/leg_open.png",
    (5, 0), "bk3/joodee/vaginal/face_shock.png",
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (5, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "bk3/joodee/vaginal/face_shock.png",
        "joodee_vag_titpull == False", "transparent.png"), 
    (5, 0), "bk3/joodee/vaginal/penetrate_3.png",
    )

image tojv tojv08 = LiveComposite(
    (1000, 720),
    (2, 0), "bk3/joodee/vaginal/body.png",       
    (647, 0), "bk3/joodee/vaginal/leg_open.png",
    (2, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_2.png"), 
    
    (2, 0), "bk3/joodee/vaginal/penetrate_4.png",
    )

image tojv tojv08_1 = LiveComposite(
    (1000, 720),
    (2, 0), "bk3/joodee/vaginal/body.png",       
    (647, 0), "bk3/joodee/vaginal/leg_open.png",
    (2, 0), "bk3/joodee/vaginal/face_shock.png",
    (2, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_2.png"), 
    
    (2, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "bk3/joodee/vaginal/face_shock.png",
        "joodee_vag_titpull == False", "transparent.png"), 
    (2, 0), "bk3/joodee/vaginal/penetrate_4.png",
    )

image tojv tojv09 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/joodee/vaginal/body.png",
    (672, 0), "bk3/joodee/vaginal/leg_open_2.png",
    (0, 0), "bk3/joodee/vaginal/face_shock.png",
    (0, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_3.png"), 
    
    (0, 0), "bk3/joodee/vaginal/penetrate_5.png",
    )

image tojv tojv09_1 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/joodee/vaginal/body.png",
    (672, 0), "bk3/joodee/vaginal/leg_open_2.png",
    (0, 0), "bk3/joodee/vaginal/face_shock.png",
    (0, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_3.png"), 
    (0, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "bk3/joodee/vaginal/face_shock.png",
        "joodee_vag_titpull == False", "transparent.png"), 
    
    (0, 0), "bk3/joodee/vaginal/penetrate_5.png",
    )


image tojv tojv15 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/joodee/vaginal/body.png",
    (672, 0), "bk3/joodee/vaginal/leg_open_2.png",
    (0, 0), ConditionSwitch(        
        "joodee_vag_titpull == True", "tojv_titpull_ani_2",
        "joodee_vag_titpull == False", "bk3/joodee/vaginal/tits_1.png"), 
    
    (0, 0), "tojv_vag_ani",
    (0, 0), "tojv_blink_ani",
    )

image tojv tojv16 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/joodee/vaginal/body.png",
    (672, 0), "bk3/joodee/vaginal/leg_open_2.png", 
    (0, 0), "tojv_titpull_ani",
    (0, 0), "tojv_vag_ani",
    (0, 0), "tojv_blink_ani",
    )









image tojv tojv100:
    "tojv tojv05"
    0.3
    "tojv tojv06"
    0.3
    "tojv tojv07"
    0.2
    "tojv tojv08"
    0.2
    "tojv tojv09"
    0.3
    "tojv tojv08"
    0.5
    "tojv tojv07"
    0.4
    "tojv tojv06"
    0.3

    repeat

image tojv tojv101:
    "tojv tojv05"
    0.3
    "tojv tojv09" with hpunch
    1.2
    "tojv tojv08"
    0.3
    "tojv tojv07"
    0.3
    "tojv tojv06"
    0.3
    repeat

image tojv tojv102:
    "tojv tojv05_1"
    0.3
    "tojv tojv06_1"
    0.05
    "tojv tojv09_1" with vshake
    0.6
    "tojv tojv08_1"
    0.15
    "tojv tojv07_1"
    0.05
    "tojv tojv06_1"
    0.08
    repeat

image tojv tojv103:
    "tojv tojv05_1"
    0.1
    "tojv tojv06_1"
    0.05
    "tojv tojv09_1" with vshake
    0.4
    "tojv tojv08_1"
    0.1
    "tojv tojv07_1"
    0.05
    "tojv tojv06_1"
    0.05
    repeat

image tojv_vag_ani:
    "bk3/joodee/vaginal/penetrate_1.png"
    0.3
    "bk3/joodee/vaginal/penetrate_2.png"
    0.3
    "bk3/joodee/vaginal/penetrate_3.png"
    0.3
    "bk3/joodee/vaginal/penetrate_4.png"
    0.3
    "bk3/joodee/vaginal/penetrate_5.png"
    0.3
    "bk3/joodee/vaginal/penetrate_4.png"
    0.3
    "bk3/joodee/vaginal/penetrate_3.png"
    0.3
    "bk3/joodee/vaginal/penetrate_2.png"
    0.3
    repeat

image tojv_titpull_ani:
    "bk3/joodee/vaginal/titpull_0.png"
    0.6
    block:
        "bk3/joodee/vaginal/titpull_2.png"
        1.4
        "bk3/joodee/vaginal/titpull_1.png"
        1.4
        repeat

image tojv_titpull_ani_2:
    "bk3/joodee/vaginal/titpull_2.png"
    0.4
    "bk3/joodee/vaginal/titpull_1.png"
    1.4
    repeat

image tojv_spermshot:
    "bk3/joodee/vaginal/spermshot.png"
    0.1
    "transparent.png"
    0.5

image tojv_blink_ani:
    "transparent.png"
    2
    "bk3/joodee/vaginal/blink.png"
    0.2
    "transparent.png"
    3
    "bk3/joodee/vaginal/blink.png"
    0.2
    "transparent.png"
    7
    "bk3/joodee/vaginal/blink.png"
    0.2
    "transparent.png"
    9
    "bk3/joodee/vaginal/blink.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
