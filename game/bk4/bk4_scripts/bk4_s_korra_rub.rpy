



init:
    $ bfag_clothes = True


image bfag bfag00 = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/body2.png", 
        "bfag_clothes == True", "bk4/korra/rub/body1.png"),     
    )


image bfag bfag01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"), 
    (0, 0), "bk4/korra/rub/head_shock.png",
    )

image bfag bfag01a = LiveComposite(    
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body3.png",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes3.png"), 
    (0, 0), "bk4/korra/rub/head_shock.png",
    )

image bfag bfag02 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (562, 195), "bfag_rub",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"),     
    (0, 0), "bk4/korra/rub/head_right.png",
    (475, 112), "bfag_blink",
    )

image bfag bfag03 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (562, 195), "bfag_rub",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"), 
    (0, 0), "bk4/korra/rub/head_up.png",
    )



image bfag bfag04 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"), 
    (0, 0), "bk4/korra/rub/head_right.png",
    (475, 112), "bfag_blink",
    )


image bfag bfag05 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"), 
    (0, 0), "bk4/korra/rub/head_angry.png",
    (475, 112), "bfag_blink",
    )

image bfag bfag06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (562, 195), "bfag_rub",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"), 
    (0, 0), "bk4/korra/rub/head_angry.png",
    (475, 112), "bfag_blink",
    )



image bfag bfag07 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (0, 0), "bk4/korra/rub/arm_fingerup.png",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"), 
    (0, 0), "bk4/korra/rub/head_angry.png", 
    (0, 0), "bk4/korra/rub/arm_fingerup_juice.png",
    )

image bfag bfag08 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (562, 195), "bfag_rubfast",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"),     
    (0, 0), "bk4/korra/rub/head_right.png",
    (475, 112), "bk4/korra/rub/blink.png",
    )

image bfag bfag09 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (562, 195), "bfag_rubfast",
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"),     
    (0, 0), "bk4/korra/rub/head_lewd.png",
    (490, 117), "bfag_blink_lewd",      
    )

image bfag bfag10 = LiveComposite(    
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",
    (562, 195), "bk4/korra/rub/rub3.png",   
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"),     
    (0, 0), "bk4/korra/rub/head_up.png", 
       
    )

image bfag bfag11 = LiveComposite(    
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body.png",    
    (0, 0), ConditionSwitch(        
        "bfag_clothes == False",  "bk4/korra/rub/tits.png", 
        "bfag_clothes == True", "bk4/korra/rub/clothes.png"),     
    (0, 0), "bk4/korra/rub/head_lewd.png", 
    (490, 117), "bfag_blink_lewd",
    (0, 0), "bk4/korra/rub/fluid.png",    
    )

image bfag bfag12 = LiveComposite(    
    (1000, 720), 
    (0, 0), "bk4/korra/rub/body0.png",    
    )



image bfag_rub:
    "bk4/korra/rub/rub1.png"
    0.2
    "bk4/korra/rub/rub2.png"
    0.2
    "bk4/korra/rub/rub3.png"
    0.2
    "bk4/korra/rub/rub2.png"
    0.2
    repeat

image bfag_rubfast:
    "bk4/korra/rub/rub1.png"
    0.1
    "bk4/korra/rub/rub2.png"
    0.1
    "bk4/korra/rub/rub3.png"
    0.1
    repeat

image bfag_blink:
    "bk4/korra/rub/blink.png"
    0.25
    "bk4/misc/minipixel.png"
    3.0
    "bk4/korra/rub/blink.png"
    0.25
    "bk4/misc/minipixel.png"
    8.0
    repeat

image bfag_blink_lewd:
    "bk4/korra/rub/blink_lewd.png"
    3.0
    "bk4/misc/minipixel.png"
    0.5
    "bk4/korra/rub/blink_lewd.png"
    0.4
    "bk4/misc/minipixel.png"
    0.5
    "bk4/korra/rub/blink_lewd.png"
    5.0
    "bk4/misc/minipixel.png"
    0.5
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
