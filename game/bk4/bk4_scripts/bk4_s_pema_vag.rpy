



init:
    $ bfax_top = True

image bfax bfax01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bfax_torso_up", 
    (0, 0), "bk4/pema/vag/hips_0.png",
    (0, 0), "bk4/pema/vag/eyes_front.png",
    )

image bfax bfax02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bfax_torso_up", 
    (0, 0), "bk4/pema/vag/hips_0.png",    
    (0, 0), "bk4/pema/vag/ani_0.png",
    )

image bfax bfax03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bfax_torso_up", 
    (0, 0), "bfax_anileg",
    (0, 0), "bk4/pema/vag/blink.png",    
    )


image bfax bfax04 = LiveComposite(
    (1000, 720),    
    (20, 0), "bfax_torso_up",     
    (20, 0), "bk4/pema/vag/ani_6.png",
    (20, 0), "bk4/pema/vag/head_lewd.png", 
    (0, 0), "bfax_shocklines",     
    
    
  
    )

image bfax bfax05 = LiveComposite(
    (1000, 720),    
    (40, 0), "bfax_torso_half",     
    (40, 0), "bfax_anileg_2", 
    )

image bfax bfax06:
    "bfax bfax05"
    1.0
    "bfax bfax04"
    0.8
    repeat


image bfax bfax07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bfax_torso_up", 
    (0, 0), "bk4/pema/vag/legs_flat.png",       
    (0, 0), "bk4/pema/vag/eyes_front.png",     
    )

image bfax bfax08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bfax_torso_up", 
    (0, 0), "bk4/pema/vag/legs_panties.png",       
    )

image bfax bfax09 = LiveComposite(
    (1000, 720),    
    (20, 0), "bfax_torso_half", 
    (20, 0), "bfax_anileg_3",
    )

image bfax bfax10 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/pema/vag/sperm_inside.png",       
    )

image bfax bfax11 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/pema/vag/sperm_outside.png",
    (0, 0), ConditionSwitch(        
        "bfax_top == False  ", "bk4/misc/minipixel.png",
        "bfax_top == True ", "bk4/pema/vag/sperm_outside_top.png"),
    )

image bfax_torso_up = LiveComposite(
    (1000, 720),    
    (0, 0), "bk4/pema/vag/torso_up.png", 
    (0, 0), ConditionSwitch(        
        "bfax_top == False ",  "bk4/misc/minipixel.png",
        "bfax_top == True",  "bk4/pema/vag/torso_up_top.png"),        
    )

image bfax_torso_half = LiveComposite(
    (1000, 720),    
    (0, 0), "bk4/pema/vag/torso_half.png", 
    (0, 0), ConditionSwitch(        
        "bfax_top == False  ", "bk4/misc/minipixel.png",
        "bfax_top == True ", "bk4/pema/vag/torso_half_top.png"),
    )


image bfax_piss:
    "bk4/pema/vag/piss1.png"
    0.2
    "bk4/pema/vag/piss2.png"
    0.2
    "bk4/pema/vag/piss3.png"
    0.2
    "bk4/pema/vag/piss2.png"
    0.2
    repeat

image bfax_shocklines:
    "bk4/pema/vag/shocklines.png"
    0.2
    "bk4/pema/vag/shocklines2.png"
    0.2
    "bk4/misc/minipixel.png"
    0.5

image bfax_spermshot:
    "bk4/pema/vag/spermshot.png"
    0.3
    "bk4/misc/minipixel.png"
    0.2
    "bk4/pema/vag/spermout_blink.png"
    0.2
    "bk4/misc/minipixel.png"
    0.2
    "bk4/pema/vag/spermout_blink.png"
    0.2
    "bk4/misc/minipixel.png"
    0.2

image bfax_anileg_3:
    "bk4/pema/vag/ani_5.png"
    0.15
    "bk4/pema/vag/ani_4.png"
    0.15
    "bk4/pema/vag/ani_3.png"
    0.15
    repeat

image bfax_anileg_2:
    "bk4/pema/vag/ani_5.png"
    0.2
    "bk4/pema/vag/ani_4.png"
    0.2
    "bk4/pema/vag/ani_3.png"
    0.2
    "bk4/pema/vag/ani_2.png"
    0.2
    "bk4/pema/vag/ani_1.png"
    0.2
    repeat

image bfax_anileg:
    "bk4/pema/vag/ani_1.png"
    0.2
    "bk4/pema/vag/ani_2.png"
    0.2
    "bk4/pema/vag/ani_3.png"
    0.2
    "bk4/pema/vag/ani_4.png"
    0.2
    "bk4/pema/vag/ani_5.png"
    0.2
    "bk4/pema/vag/ani_4.png"
    0.2
    "bk4/pema/vag/ani_3.png"
    0.2
    "bk4/pema/vag/ani_2.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
