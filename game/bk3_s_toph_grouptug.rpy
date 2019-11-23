






init:
    $ tott_head = 'smile'
    $ tott_tits = 'small'

image tott tott01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/group1.png",  
    (0, 0), "bk3/toph/grouptug/group1_tug1.png",    
    )
image tott tott02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/group1.png",  
    (0, 0), "tott_tugjob",    
    )

image tott tott05 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/body_aang.png",  
    (0, 0), "bk3/toph/grouptug/fuck1.png",   
    (0, 0), "bk3/toph/grouptug/arms.png", 
    (0, 0), "tott_torso",
    (440, 0), "tott_head",
    )
image tott tott06 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/body_aang.png",  
    (0, 0), "bk3/toph/grouptug/fuck2.png",   
    (0, 4), "bk3/toph/grouptug/arms.png", 
    (0, 10), "tott_torso",
    (440, 15), "tott_head",
    )
image tott tott07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/body_aang.png",  
    (0, 0), "bk3/toph/grouptug/fuck3.png",   
    (0, 10), "bk3/toph/grouptug/arms.png", 
    (0, 15), "tott_torso",
    (440, 30), "tott_head",
    )
image tott tott08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/body_aang.png",  
    (0, 0), "bk3/toph/grouptug/fuck4.png",   
    (0, 10), "bk3/toph/grouptug/arms.png", 
    (0, 20), "tott_torso",
    (440, 40), "tott_head",
    )
image tott tott10 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/grouptug/body_aang.png",  
    (0, 0), "bk3/toph/grouptug/spermstand.png",   
    
    )

image tott_head = LiveComposite(
    (257, 268),   
    
    (0, 0), ConditionSwitch(        
        "tott_head == 'smile'", "bk3/toph/grouptug/head.png",
        "tott_head == 'unsure'", "bk3/toph/grouptug/head_unsure.png",
        "tott_head == 'lewd'", "bk3/toph/grouptug/head_lewd.png",
        "tott_head == 'angry'",  "bk3/toph/grouptug/head_angry.png"),   
    (0, 0), "tott_blink",
    )
image tott_torso = LiveComposite(
    (1000, 720),      
    (0, 0), ConditionSwitch(        
        "tott_tits == 'small'","bk3/toph/grouptug/torso.png",    
        "tott_tits == 'big'",  "bk3/toph/grouptug/torsotits.png"), 
    )







image tott_blink:
    "transparent.png"
    4.0
    "bk3/toph/grouptug/blink.png"
    0.3
    "transparent.png"
    8.0
    "bk3/toph/grouptug/blink.png"
    0.3
    repeat

image tott_tugjob:
    "bk3/toph/grouptug/group1_tug1.png"
    0.3
    "bk3/toph/grouptug/group1_tug2.png"
    0.3
    "bk3/toph/grouptug/group1_tug3.png"
    0.3
    "bk3/toph/grouptug/group1_tug4.png"
    0.3
    "bk3/toph/grouptug/group1_tug3.png"
    0.3
    "bk3/toph/grouptug/group1_tug2.png"
    0.3
    repeat

image tott tott100:
    "tott tott05"
    0.3
    "tott tott06"
    0.3
    "tott tott07"
    0.3
    "tott tott08"
    0.3
    "tott tott07"
    0.3
    "tott tott06"
    0.3
    repeat

image tott tott101:

    "tott tott06"
    1.3
    "tott tott07"
    0.3
    "tott tott08"
    0.3
    "tott tott05" with vpunch
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
