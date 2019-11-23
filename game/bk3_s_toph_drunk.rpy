






init:
    $ toph_drunk = 'smile'

image totd totd00 = "bk3/toph/drunk/body_4.png"

image totd totd01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_0.png",
    (0, 0), "bk3/toph/drunk/arm_bottle.png",
    (0, 0), ConditionSwitch(        
        "toph_drunk == 'sad'"  , "bk3/toph/drunk/sad.png",
        "toph_drunk == 'smile'", "transparent.png",
        "toph_drunk == 'angry'", "bk3/toph/drunk/angry.png"), 
    (0, 0), "totd_blink", 
    )

image totd totd02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_2.png",
    (0, 0), "bk3/toph/drunk/clothes_2.png",
    (0, 0), "totd_wine",
    )

image totd totd03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_0.png",
    (0, 0), "bk3/toph/drunk/arm_bottle.png",
    (0, 0), ConditionSwitch(        
        "toph_drunk == 'sad'"  , "bk3/toph/drunk/sad.png",
        "toph_drunk == 'smile'", "transparent.png",
        "toph_drunk == 'angry'", "bk3/toph/drunk/angry.png"), 
    (0, 0), "bk3/toph/drunk/eyes_drunk.png",
    (0, 0), "totd_blink", 
    )

image totd totd04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_2.png",
    (0, 0), "bk3/toph/drunk/clothes_2.png",
    )

image totd totd05 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_1.png",    
    (0, 0), ConditionSwitch(        
        "toph_drunk == 'sad'"  , "bk3/toph/drunk/sad.png",
        "toph_drunk == 'smile'", "transparent.png",
        "toph_drunk == 'angry'", "bk3/toph/drunk/angry.png"),
    (0, 0), "bk3/toph/drunk/eyes_drunk.png",
    (0, 0), "totd_blink", 
    )

image totd totd06 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_2.png",
    (0, 0), "totd_wine",
    )

image totd totd07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_1.png",    
    (0, 0), ConditionSwitch(        
        "toph_drunk == 'sad'"  , "bk3/toph/drunk/sad.png",
        "toph_drunk == 'smile'", "transparent.png",
        "toph_drunk == 'angry'", "bk3/toph/drunk/angry.png"),    
    (0, 0), "totd_blink", 
    )

image totd totd10 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_0.png",
    (0, 0), "bk3/toph/drunk/arm_glass_down.png",
    (0, 0), ConditionSwitch(        
        "toph_drunk == 'sad'"  , "bk3/toph/drunk/sad.png",
        "toph_drunk == 'smile'", "transparent.png",
        "toph_drunk == 'angry'", "bk3/toph/drunk/angry.png"),    
    (0, 0), "totd_blink", 
    )
image totd totd11 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/body_0.png", 
    (0, 0), ConditionSwitch(        
        "toph_drunk == 'sad'"  , "bk3/toph/drunk/sad.png",
        "toph_drunk == 'smile'", "transparent.png",
        "toph_drunk == 'angry'", "bk3/toph/drunk/angry.png"),  
    (0, 0), "bk3/toph/drunk/arm_glass_up.png",
    (0, 0), "totd_blink", 
    )





image totd totd20 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/suki_body.png",   
    (0, 0), "bk3/toph/drunk/suki_tits1.png",
   
    )
image totd totd21 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/suki_body.png",   
    (0, 0), "bk3/toph/drunk/suki_tits2.png",
    
    )
image totd totd22 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/suki_body.png",   
    (0, 0), "bk3/toph/drunk/suki_tits3.png",
    
    )
image totd totd25 = LiveComposite(
    (1000, 720),    
    (0, 0), "totd totd110",  
    (0, 0), "bk3/toph/drunk/suki_head_side1.png",
    (0, 0), "bk3/toph/drunk/suki_sideblink.png",    
    )
image totd totd26 = LiveComposite(
    (1000, 720),    
    (0, 0), "totd totd110",   
    (0, 0), "bk3/toph/drunk/suki_head_front1.png",
    (0, 0), "bk3/toph/drunk/suki_frontblink.png",
    )
image totd totd30 = LiveComposite(
    (1000, 720),    
    (0, 0), "totd totd110",   
    (0, 0), "bk3/toph/drunk/suki_head_side1.png",    
    )
image totd totd31 = LiveComposite(
    (1000, 720),    
    (0, 0), "totd totd110",   
    (0, 0), "bk3/toph/drunk/suki_head_front1.png",    
    )

image totd totd35 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/zoom_tavern.jpg",   
    (0, 0), "bk3/toph/drunk/body_5.png",    
    )
image totd totd36 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/zoom_tavern.jpg",   
    (0, 0), "bk3/toph/drunk/body_5.png", 
    (0, 0), "bk3/toph/drunk/pussy.png", 
    (0, 0), "bk3/toph/drunk/body_6.png",  
    )
image totd totd37 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/zoom_tavern.jpg",   
    (0, 0), "bk3/toph/drunk/body_5.png", 
    (0, 0), "bk3/toph/drunk/pussy.png", 
    (550, 240), "totd_tongue",
    (0, 0), "bk3/toph/drunk/body_6.png",  
    )
image totd totd38 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/drunk/zoom_tavern.jpg",   
    (0, 0), "bk3/toph/drunk/body_5.png",    
    (0, 0), "bk3/toph/drunk/pussy_juice.png",    
    )





image totd_crowd = "bk3/toph/drunk/crowd.png"




image totd_blink:
    "bk3/toph/drunk/blink.png"
    0.3
    "transparent.png"
    2
    "bk3/toph/drunk/blink.png"
    0.3
    "transparent.png"
    8
    repeat

image totd_pourwine:
    "bk3/toph/drunk/pour_drink1.png"
    0.3
    "bk3/toph/drunk/pour_drink2.png"
    0.3

    repeat


image totd_wine:
    "bk3/toph/drunk/wine_1.png"
    0.3
    "bk3/toph/drunk/wine_2.png"
    0.3
    "bk3/toph/drunk/wine_3.png"
    0.3
    repeat

image totd totd100:
    "totd totd05"
    1.0
    "totd totd06"
    1.8
    "totd totd05"
    9.0
    "totd totd06"
    1.8
    "totd totd05"
    6.0
    repeat

image totd totd101:
    "bk3/toph/drunk/dance_1.png"
    0.3
    "bk3/toph/drunk/dance_2.png"
    0.3
    "bk3/toph/drunk/dance_3.png"
    0.3
    "bk3/toph/drunk/dance_4.png"
    0.3
    "bk3/toph/drunk/dance_3.png"
    0.3
    "bk3/toph/drunk/dance_2.png"
    0.3
    repeat
image totd totd102:
    "totd totd02"
    ypos 720
    linear 0.5 ypos 725
    linear 0.4 ypos 720
    repeat

image totd totd110:
    "totd totd20"
    xzoom 1.0
    0.2
    "totd totd21"
    0.2
    "totd totd22"
    0.2
    "totd totd21"
    0.2
    "totd totd20"
    0.2
    "totd totd20"
    xzoom -1.0
    0.2
    "totd totd21"
    0.2
    "totd totd22"
    0.2
    "totd totd21"
    0.2
    repeat

image totd_tongue:
    "bk3/toph/drunk/tongue1.png"
    0.2
    "bk3/toph/drunk/tongue2.png"
    0.2
    "bk3/toph/drunk/tongue3.png"
    0.2
    "bk3/toph/drunk/tongue4.png"
    0.2
    "bk3/toph/drunk/tongue5.png"
    0.3
    "bk3/toph/drunk/tongue2.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
