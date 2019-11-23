


init:
    define bk3c = Character("Just some guy", color="#070000",show_side_image = Image("bk3/suki/barblow/customer.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)




image toxc toxc00 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png",
    (0, 0), "bk3/suki/barblow/arm_down.png",
    (531, 187), "toxc_blink",    
    )


image toxc toxc01 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png",
    (531, 187), "bk3/suki/barblow/dick_up.png",     
    (0, 0), "bk3/suki/barblow/arm_down.png",
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    (531, 187), "toxc_blink",    
    )

image toxc toxc02 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png", 
    (531, 187), "bk3/suki/barblow/dick_up.png",    
    (0, 0), "bk3/suki/barblow/arm_down.png",    
    (531, 187), "bk3/suki/barblow/mouth_open.png", 
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    (531, 187), "toxc_blink",  
    )

image toxc toxc02_1 = LiveComposite(
    (1000, 720),    
    (540, 190), "bk3/suki/barblow/body_0.png", 
    (531, 187), "bk3/suki/barblow/dick_eyeless.png",    
    (9, 3), "bk3/suki/barblow/arm_down.png",    
    (540, 190), "bk3/suki/barblow/mouth_open.png", 
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    )

image toxc toxc02_2 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png", 
    (531, 187), "bk3/suki/barblow/dick_up.png",    
    (0, 0), "bk3/suki/barblow/arm_down.png",    
    (531, 187), "bk3/suki/barblow/mouth_open.png", 
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    )

image toxc toxc02_3 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png", 
    (531, 187), "bk3/suki/barblow/dick_eyeless.png",    
    (0, 0), "bk3/suki/barblow/arm_down.png",    
    (531, 187), "bk3/suki/barblow/mouth_open.png", 
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    )


image toxc toxc03 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png",      
    (531, 187), "bk3/suki/barblow/dick_tipin.png", 
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
  
    (531, 187), "toxc_blink",
    )

image toxc toxc04 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_1.png",
    (15, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
    
    )

image toxc toxc05 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_2.png",
    (10, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    )

image toxc toxc06 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_3.png",
    (10, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
    
    )

image toxc toxc07a = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_4.png",    
    (531, 187), "bk3/suki/barblow/body_4_haira.png",  
    (10, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    )

image toxc toxc07b = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_4.png",  
    (531, 187), "bk3/suki/barblow/body_4_hairb.png", 
    (10, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
    
    
    )

image toxc toxc08 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png",
    (0, 0), "bk3/suki/barblow/arm_solodick.png",
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    (0, 0), "bk3/suki/barblow/arm_holddick.png",
    (531, 187), "toxc_blink",
    )

image toxc toxc08_1 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png",
    (531, 187), "bk3/suki/barblow/mouth_open.png", 
    (0, 0), "bk3/suki/barblow/arm_solodick.png",
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    (0, 0), "bk3/suki/barblow/arm_holddick.png",
    )

image toxc toxc08_2 = LiveComposite(
    (1000, 720),    
    (531, 187), "bk3/suki/barblow/body_0.png",
    (531, 187), "bk3/suki/barblow/mouth_open.png", 
    (0, 0), "bk3/suki/barblow/arm_solodick.png",
    (0, 0), "bk3/suki/barblow/arm_down.png",    
    (20, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    )

image toxc toxc09 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/suki/barblow/floor.jpg",
    (0, 50), "bk3/suki/barblow/floor_body.png",    
    )


image toxc_playbody = LiveComposite(
    (1000, 720),    
    (-80, 0), ConditionSwitch(
        "bk3_su_bb_player == 'True'", "bk3/suki/barblow/playerbody_0.png",
        "bk3_su_bb_player == 'False'", "transparent.png"),
   
    (-80, 0), "bk3/suki/barblow/arm_solodick.png",     
    )

image toxc_servedrink:
    "bk3/suki/barblow/glass_hand.png"
    2.0
    "bk3/suki/barblow/glass.png"
    3.0


image toxc_blink:
    "bk3/suki/barblow/minipixel.png"
    0.3
    "bk3/suki/barblow/blink.png"
    0.3
    "bk3/suki/barblow/minipixel.png"
    0.3
    "bk3/suki/barblow/blink.png"
    0.3
    "bk3/suki/barblow/minipixel.png"
    6.0
    "bk3/suki/barblow/blink.png"
    0.3
    "bk3/suki/barblow/minipixel.png"
    8.0
    repeat

image toxc toxc100:
    "toxc toxc03"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc06"
    0.2
    "toxc toxc07a"
    0.2
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    repeat

image toxc toxc101:
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc03"
    0.2
    "toxc toxc07b"
    0.2
    "toxc toxc07a" with hpunch
    1.2


    repeat

image toxc toxc102:
    "toxc toxc03"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc06"
    0.2
    "toxc toxc07a"
    0.2
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2

image toxc toxc103:
    "toxc toxc07b"
    0.13
    "toxc toxc07a" with hpunch
    .5
    "toxc toxc06"
    0.17
    "toxc toxc05"
    0.17
    "toxc toxc04"
    0.17
    "toxc toxc05"
    0.13
    repeat


image toxc toxc104:
    "toxc toxc06"
    0.13
    "toxc toxc05"
    0.13
    "toxc toxc04"
    0.13
    "toxc toxc07b"
    0.2
    "toxc toxc07a" with hpunch
    .6
    repeat


image toxc toxc105:
    "toxc toxc05"
    0.15
    "toxc toxc06"
    0.1
    "toxc toxc07b"
    0.2
    "toxc toxc07a" with hpunch
    .3
    "toxc toxc06"
    0.15
    repeat

image toxc toxc106:
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.3
    "toxc toxc05"
    0.2
    "toxc toxc06"
    0.5
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.3
    "toxc toxc05"
    0.2
    "toxc toxc06"
    0.5
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc07b"
    0.2
    "toxc toxc07a" with hpunch
    1
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc07b"
    0.2
    "toxc toxc07a" with hpunch
    1
    "toxc toxc07a" with ushake
    1
    "toxc toxc07a" with ushake
    .25
    "toxc toxc07a" with vshake
    .25
    "toxc toxc04"
    0.15
    "toxc toxc03"
    0.15
    "toxc toxc02_1"
    0.5
    "toxc toxc02_3" with Dissolve(.2)
    0.5
    "toxc toxc02_1" with Dissolve(.2)
    0.5
    "toxc toxc02_3" with Dissolve(.2)
    0.5
    "toxc toxc02_1" with Dissolve(.2)
    0.5
    "toxc toxc02_3" with Dissolve(.2)
    0.5
    "toxc toxc02_1" with Dissolve(.2)
    0.4
    "toxc toxc03" with Dissolve(.2)
    0.4
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc06"
    0.5
    repeat

image toxc toxc107:
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.15
    "toxc toxc07a" with hpunch
    0.5
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.15
    "toxc toxc07a" with hpunch
    0.5
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.15
    "toxc toxc07a" with hpunch
    0.5
    "toxc toxc06"
    0.2
    "toxc toxc05"
    0.2
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.15
    "toxc toxc07b"
    0.2
    "toxc toxc07a" with hpunch
    .75
    "toxc toxc07a" with ushake
    .5
    "toxc toxc07a" with ushake
    .25
    "toxc toxc07a" with vshake
    .25
    "toxc toxc04"
    0.15
    "toxc toxc03"
    0.15
    "toxc toxc02_1"
    0.5
    "toxc toxc02_3" with Dissolve(.2)
    0.5
    "toxc toxc02_1" with Dissolve(.2)
    0.5
    "toxc toxc02_3" with Dissolve(.2)
    0.5
    "toxc toxc02_1" with Dissolve(.2)
    0.5
    "toxc toxc03" with Dissolve(.2)
    0.4
    "toxc toxc04"
    0.2
    "toxc toxc05"
    0.15
    "toxc toxc07a" with hpunch
    0.5
    "toxc toxc06"
    0.2
    repeat


screen toxc_player_body:
    if bk3_su_bb_player == "True":
        textbutton "hide body" action SetVariable("bk3_su_bb_player", "False"):
            xpos 0 ypos 0
    if bk3_su_bb_player == "False":
        textbutton "show body" action SetVariable("bk3_su_bb_player", "True"):
            xpos 0 ypos 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
