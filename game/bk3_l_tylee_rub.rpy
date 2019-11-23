


init:
    $ pinkflash = Fade(.5, 0.8, .5, color="#FFB6C1")



image toxj toxj00 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/pov_up.png", 
    (0, 0), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/pov_up_bikini.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),    
    (0, 0), ConditionSwitch(        
        "toxj_rub == 'dick'",  "bk3/tylee/tyrub/dick1.png",
        "toxj_rub == 'face'", "bk3/tylee/tyrub/minipixel.png"),
    )

image toxj toxj01 = LiveComposite(
    (1000, 720),    
    (0, 0), "toxj_upperbody", 
    (0, 0), "bk3/tylee/tyrub/tits1.png",
    (0, 0), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/biki1.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/legs1.png", 
    (0, 0), ConditionSwitch(        
        "toxj_rub == 'dick'",  "bk3/tylee/tyrub/dick1.png",
        "toxj_rub == 'face'", "bk3/tylee/tyrub/minipixel.png"),
    )

image toxj toxj02 = LiveComposite(
    (1000, 720),    
    (0, -4), "toxj_upperbody", 
    (0, -4), "bk3/tylee/tyrub/tits2.png",
    (0, -4), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/biki2.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/legs2.png", 
    (0, 0), ConditionSwitch(        
        "toxj_rub == 'dick'",  "bk3/tylee/tyrub/dick2.png",
        "toxj_rub == 'face'", "bk3/tylee/tyrub/minipixel.png"),
    )

image toxj toxj03 = LiveComposite(
    (1000, 720),    
    (0, -8), "toxj_upperbody", 
    (0, -8), "bk3/tylee/tyrub/tits3.png",
    (0, -8), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/biki3.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/legs3.png", 
    (0, 0), ConditionSwitch(        
        "toxj_rub == 'dick'",  "bk3/tylee/tyrub/dick3.png",
        "toxj_rub == 'face'", "bk3/tylee/tyrub/minipixel.png"),
    )
image toxj toxj04 = LiveComposite(
    (1000, 720),    
    (0, -12), "toxj_upperbody", 
    (0, -12), "bk3/tylee/tyrub/tits4.png",
    (0, -12), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/biki4.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/legs4.png",    
    (0, 0), ConditionSwitch(        
        "toxj_rub == 'dick'",  "bk3/tylee/tyrub/dick4.png",
        "toxj_rub == 'face'", "bk3/tylee/tyrub/minipixel.png"),
    )
image toxj toxj05 = LiveComposite(
    (1000, 720),    
    (0, -16), "toxj_upperbody", 
    (0, -16), "bk3/tylee/tyrub/tits5.png",
    (0, -16), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/biki5.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/legs5.png",    
    (0, 0), ConditionSwitch(        
        "toxj_rub == 'dick'",  "bk3/tylee/tyrub/dick5.png",
        "toxj_rub == 'face'", "bk3/tylee/tyrub/minipixel.png"),
    )




image toxj_ty01 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/idle_tylee.png",    
    
    (0, 0), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/idle_swimsuit.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/idle_tylee_armdown.png", 
    )

image toxj_ty02 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/idle_tylee.png",     
    (0, 0), "bk3/tylee/tyrub/idle_tylee_armup.png",
    (0, 0), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/idle_swimsuit.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    )
image toxj_ty03 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/idle_tylee.png",
    (0, 0), "bk3/tylee/tyrub/idle_tylee_anger.png",
    (0, 0), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/idle_swimsuit.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),
    (0, 0), "bk3/tylee/tyrub/idle_tylee_armdown.png", 
    )

image toxj_ty04 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/idle_tylee.png",
    (0, 0), "bk3/tylee/tyrub/idle_tylee_eyeleft.png",
    (0, 0), ConditionSwitch(        
        "toxj_bikini == 'on'",  "bk3/tylee/tyrub/idle_swimsuit.png",
        "toxj_bikini == 'off'", "bk3/tylee/tyrub/minipixel.png"),    
    (0, 0), "bk3/tylee/tyrub/idle_tylee_armdown.png", 
    )
image toxj_ty05 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/idle_tylee.png",
    (0, 0), "bk3/tylee/tyrub/idle_bikini.png",
    (0, 0), "bk3/tylee/tyrub/idle_tylee_armdown.png", 
    )




image toxj_az01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/tylee/tyrub/idle_azula_armdown.png",
    (0, 0), "bk3/tylee/tyrub/idle_azula.png",          
    )

image toxj_az02 = LiveComposite(
    (1000, 720),  
    (0, 0), "bk3/tylee/tyrub/idle_azula.png", 
    (0, 0), "bk3/tylee/tyrub/idle_azula_armpoint.png",     
    )

image toxj_mai01 = LiveComposite(
    (1000, 720),  
    (738, 0), "bk3/tylee/tyrub/idle_mai.png",          
    )





image toxj_upperbody = LiveComposite(
    (1000, 720),  
    (0, 0), ConditionSwitch(        
        "toxj_arms == 'up'",  "bk3/tylee/tyrub/armsup.png",
        "toxj_arms == 'down'", "bk3/tylee/tyrub/armsdown.png"),   
    (0, 0), ConditionSwitch(        
        "toxj_face == 'lewd'",  "bk3/tylee/tyrub/face_lewd.png",
        "toxj_face == 'normal'", "bk3/tylee/tyrub/face_normal.png"),
    )








image toxj toxj100:
    "toxj toxj01"
    0.2
    "toxj toxj02"
    0.2
    "toxj toxj03"
    0.2
    "toxj toxj04"
    0.2
    "toxj toxj05"
    0.2
    "toxj toxj04"
    0.2
    "toxj toxj03"
    0.2
    "toxj toxj02"
    0.2
    repeat

image toxj toxj101:
    "toxj toxj02" with vpunch
    0.5
    "toxj toxj03"
    0.2
    "toxj toxj04"
    0.2
    repeat


image toxj_dickrub:
    "bk3/tylee/tyrub/armsup.png"
    0.2
    "toxj toxj02"
    0.2
    "toxj toxj03"
    0.2
    "toxj toxj04"
    0.2
    "toxj toxj05"
    0.2
    "toxj toxj04"
    0.2
    "toxj toxj03"
    0.2
    "toxj toxj02"
    0.2
    repeat

image toxj_tongue:

    "bk3/tylee/tyrub/ton1.png"
    0.2
    "bk3/tylee/tyrub/ton2.png"
    0.2
    "bk3/tylee/tyrub/ton3.png"
    0.2
    "bk3/tylee/tyrub/ton4.png"
    0.2
    "bk3/tylee/tyrub/ton5.png"
    0.2
    "bk3/tylee/tyrub/ton6.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
