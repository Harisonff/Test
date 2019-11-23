


init:
    $ toff_clotheson = True





image toff toff00 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body", 
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/legs_solo_cloth.png",        
        "toff_clotheson == False","bk3/toph/footjob3/legs_solo.png"), 
    (287, 0), "toff_blink", 
    )

image toff toff01 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body", 
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/legs_solo2_cloth.png",        
        "toff_clotheson == False", "bk3/toph/footjob3/legs_solo2.png"), 
    
    (287, 0), "toff_blink", 
    )
image toff toff02 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body", 
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/legs_solo_cloth.png",        
        "toff_clotheson == False","bk3/toph/footjob3/legs_solo.png"), 
    (0, 0), "bk3/toph/footjob3/solodick.png", 
    (0, 0), "bk3/toph/footjob3/body_player.png",
    (287, 0), "toff_blink",         
    )

image toff toff03 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body",  
    (462, 0), "bk3/toph/footjob3/footjob_1.png", 
    (0, 0), "bk3/toph/footjob3/body_player.png", 
    (287, 0), "toff_blink", 
    )

image toff toff04 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body", 
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/cloth_solo.png",        
        "toff_clotheson == False","bk3/toph/footjob3/minipixel.png"), 
    (462, 0), "toff_footjob",     
    (0, 0), "bk3/toph/footjob3/body_player.png",
    (287, 0), "toff_blink", 
    )

image toff toff05 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body",  
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/cloth_solo.png",        
        "toff_clotheson == False","bk3/toph/footjob3/minipixel.png"), 
    (462, 0), "toff_footjob_fast", 
    (0, 0), "bk3/toph/footjob3/body_player.png", 
    (287, 0), "toff_blink", 
    )

image toff toff06 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body",  
    (558, 0), "toff_footjob2",
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/cloth_solo_2.png",        
        "toff_clotheson == False","bk3/toph/footjob3/minipixel.png"), 
    (0, 0), "bk3/toph/footjob3/body_player.png", 
    (288, 0), "toff_blink", 
    )

image toff toff07 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body",  
    (558, 0), "toff_footjob2_fast", 
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/cloth_solo_2.png",        
        "toff_clotheson == False","bk3/toph/footjob3/minipixel.png"), 
    (0, 0), "bk3/toph/footjob3/body_player.png", 
    (287, 0), "toff_blink", 
    )

image toff toff08 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body",  
    (558, 0), "bk3/toph/footjob3/footjob_11.png",
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/cloth_solo_2.png",        
        "toff_clotheson == False","bk3/toph/footjob3/minipixel.png"), 
    (0, 0), "bk3/toph/footjob3/body_player.png", 
    (287, 0), "toff_blink", 
    )

image toff toff09 = LiveComposite(
    (1000, 720),    
    (0, 0), "toff_body",  
    (558, 0), "bk3/toph/footjob3/footjob_10.png",
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/cloth_solo_2.png",        
        "toff_clotheson == False","bk3/toph/footjob3/minipixel.png"), 
    (0, 0), "bk3/toph/footjob3/body_player.png", 
    (287, 0), "toff_blink", 
    )









image toff_body = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/footjob3/body_toph.png",
    (0, 0), ConditionSwitch(        
        "toff_clotheson == True", "bk3/toph/footjob3/body_toph_clothes.png",        
        "toff_clotheson == False", "bk3/toph/footjob3/minipixel.png"),  

    )


image toff_lewd = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/footjob3/lewd.png",
    (287, 0), "toff_blink", 
    )


image toff_footjob:
    "bk3/toph/footjob3/footjob_1.png"
    0.3
    "bk3/toph/footjob3/footjob_2.png"
    0.3
    "bk3/toph/footjob3/footjob_3.png"
    0.3
    "bk3/toph/footjob3/footjob_4.png"
    0.3
    "bk3/toph/footjob3/footjob_3.png"
    0.3
    "bk3/toph/footjob3/footjob_2.png"
    0.3
    repeat

image toff_footjob_fast:
    "bk3/toph/footjob3/footjob_1.png"
    0.1
    "bk3/toph/footjob3/footjob_2.png"
    0.2
    "bk3/toph/footjob3/footjob_3.png"
    0.2
    "bk3/toph/footjob3/footjob_4.png"
    0.1
    "bk3/toph/footjob3/footjob_3.png"
    0.2
    "bk3/toph/footjob3/footjob_2.png"
    0.2
    repeat

image toff_footjob2:
    "bk3/toph/footjob3/footjob_11.png"
    0.2
    "bk3/toph/footjob3/footjob_12.png"
    0.2
    "bk3/toph/footjob3/footjob_13.png"
    0.2
    "bk3/toph/footjob3/footjob_14.png"
    0.2
    "bk3/toph/footjob3/footjob_15.png"
    0.2
    "bk3/toph/footjob3/footjob_14.png"
    0.2
    "bk3/toph/footjob3/footjob_13.png"
    0.2
    "bk3/toph/footjob3/footjob_12.png"
    0.2
    repeat

image toff_footjob2_fast:
    "bk3/toph/footjob3/footjob_11.png"
    0.1
    "bk3/toph/footjob3/footjob_13.png"
    0.1
    "bk3/toph/footjob3/footjob_14.png"
    0.1
    "bk3/toph/footjob3/footjob_15.png"
    0.2
    "bk3/toph/footjob3/footjob_12.png"
    0.2
    repeat

image toff_blink:
    "bk3/toph/footjob3/blink.png"
    0.3
    "bk3/toph/footjob3/minipixel.png"
    9.0
    "bk3/toph/footjob3/blink.png"
    0.3
    "bk3/toph/footjob3/minipixel.png"
    0.3
    "bk3/toph/footjob3/blink.png"
    0.3
    "bk3/toph/footjob3/minipixel.png"
    6.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
