


init:
    $ toxh_preg = False
    $ toxh_upperbody = 'up_default'




image toxh toxh00 = LiveComposite(
    (1000, 720),    
    (0, 0), "toxh_upperbody", 
    (0, 0), "bk3/katara/pregfuck/fuck0.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg0.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )

image toxh toxh01 = LiveComposite(
    (1000, 720),    
    (0, 0), "toxh_upperbody", 
    (0, 0), "bk3/katara/pregfuck/fuck1.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg0.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )
image toxh toxh02 = LiveComposite(
    (1000, 720),    
    (0, 0), "toxh_upperbody", 
    (0, 0), "bk3/katara/pregfuck/fuck2.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg2.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )
image toxh toxh03 = LiveComposite(
    (1000, 720),    
    (-1, 0), "toxh_upperbody", 
    (0, 0), "bk3/katara/pregfuck/fuck3.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg3.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )
image toxh toxh04 = LiveComposite(
    (1000, 720),    
    (-2, 0), "toxh_upperbody", 
    (0, 0), "bk3/katara/pregfuck/fuck4.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg3.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )

image toxh toxh05 = LiveComposite(
    (1000, 720),    
    (-2, 0), "toxh_upperbody",
    (50, 0), "bk3/katara/pregfuck/fuck5.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg3.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )

image toxh toxh05a = LiveComposite(
    (1000, 720),    
    (-27, 0), "bk3/katara/pregfuck/body_up_2.png",
    (25, 0), "bk3/katara/pregfuck/fuck5.png",
    (-25, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg3.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )

image toxh toxh05b = LiveComposite(
    (1000, 720),    
    (-27, 0), "bk3/katara/pregfuck/body_up_3.png",
    (25, 0), "bk3/katara/pregfuck/fuck5.png",
    (-25, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg3.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )

image toxh toxh06 = LiveComposite(
    (1000, 720),    
    (0, 0), "toxh_upperbody",
    (0, 0), "bk3/katara/pregfuck/legs_closed.png",
    (0, 0), "bk3/katara/pregfuck/eyes_lookat.png",   
    )
image toxh toxh07 = LiveComposite(
    (1000, 720),    
    (0, 0), "toxh_upperbody",
    (0, 0), "bk3/katara/pregfuck/legs_open.png",
    (0, 0), "bk3/katara/pregfuck/eyes_lookat.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg0.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )
image toxh toxh08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/body_downkiss.png",
    (0, 0), "bk3/katara/pregfuck/legs_open.png",    
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/preg0.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"), 
    )

image toxh toxh09 = LiveComposite( 
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/idle_body_cloth.png",    
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/idle_preg_cloth.png",
        "toxh_preg == False", "bk3/katara/pregfuck/idle_arms_cloth.png"), 
    (0, 0), "toxh_idleblink", 
    )

image toxh toxh10 = LiveComposite( 
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/idle_body_nude.png",    
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/idle_preg_nude.png",
        "toxh_preg == False", "bk3/katara/pregfuck/idle_arms_nude.png"),
    (0, 0), "toxh_idleblink", 
    )

image toxh toxh11 = LiveComposite( 
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/front_body.png", 
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/front_preg.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"),
    )
image toxh toxh12 = LiveComposite( 
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/front_body.png",
    (0, 0), "bk3/katara/pregfuck/front_spread.png",
    (0, 0), ConditionSwitch(        
        "toxh_preg == True", "bk3/katara/pregfuck/front_preg.png",
        "toxh_preg == False", "bk3/katara/pregfuck/minipixel.png"),
    )

image toxh_upperbody = LiveComposite(
    (1000, 720),  
    (0, 0), ConditionSwitch(        
        "toxh_upperbody == 'up_default'", "toxh_head_default",
        "toxh_upperbody == 'up_lewd'", "toxh_head_lewd",
        "toxh_upperbody == 'up_blink'", "toxh_head_blink",
        "toxh_upperbody == 'down'", "bk3/katara/pregfuck/body_down.png"), 
    )


image toxh_head_default = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/body_up.png",
    (0, 0), "bk3/katara/pregfuck/head_default.png", 
    
    )
image toxh_head_lewd = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/body_up.png",
    (0, 0), "bk3/katara/pregfuck/head_lewd.png", 
    )
image toxh_head_blink = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/pregfuck/body_up.png",
    (0, 0), "bk3/katara/pregfuck/head_lewd.png", 
    (0, 0), "bk3/katara/pregfuck/head_blink.png", 
    )
image toxh_spermshot:
    "bk3/katara/pregfuck/spermshot.png"
    0.3
    "bk3/katara/pregfuck/minipixel.png"
    0.3

image toxh_idleblink:
    "bk3/katara/pregfuck/idle_blink.png"
    0.3
    "bk3/katara/pregfuck/minipixel.png"
    2.0
    "bk3/katara/pregfuck/idle_blink.png"
    0.3
    "bk3/katara/pregfuck/minipixel.png"
    5.0
    "bk3/katara/pregfuck/idle_blink.png"
    0.3
    "bk3/katara/pregfuck/minipixel.png"
    7.0
    repeat

image toxh toxh100:
    "toxh toxh01"
    0.3
    "toxh toxh02"
    0.3
    "toxh toxh03"
    0.3
    "toxh toxh04"
    0.3
    "toxh toxh05"
    0.3
    "toxh toxh04"
    0.3
    "toxh toxh03"
    0.3
    "toxh toxh02"
    0.3
    repeat

image toxh toxh101:

    "toxh toxh05a" with hpunch
    1.0
    "toxh toxh05b"
    0.1
    "toxh toxh03"
    0.3
    "toxh toxh02"
    0.3
    "toxh toxh01"
    0.8
    repeat

image toxh_tongue:

    "bk3/katara/pregfuck/ton1.png"
    0.2
    "bk3/katara/pregfuck/ton2.png"
    0.2
    "bk3/katara/pregfuck/ton3.png"
    0.2
    "bk3/katara/pregfuck/ton4.png"
    0.2
    "bk3/katara/pregfuck/ton5.png"
    0.2
    "bk3/katara/pregfuck/ton6.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
