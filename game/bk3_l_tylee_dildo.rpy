



init:
    $ toxd_transparent = 'false'
    $ toxd_fuck = False





image toxd toxd00a = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_1.png",
    (0, 0), "bk3/tylee/lovedildo/body_1_armside.png",
    )
image toxd toxd00b = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_1.png",
    (0, 0), "bk3/tylee/lovedildo/body_1_armside.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_0.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/solodildo.png"), 
    
    )
image toxd toxd00c = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_1.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_1.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_1.png"),     
    (0, 0), "bk3/tylee/lovedildo/body_1_armdildo.png",
    )

image toxd toxd00d = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_1.png",
    (0, 0), "bk3/tylee/lovedildo/playerbody_6.png",       
    )


image toxd toxd01 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_1.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_1.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_1.png"), 
    
    (0, 0), "bk3/tylee/lovedildo/body_1_armside.png",
    (0, 0), ConditionSwitch(        
        "toxd_transparent == 'false'",  "bk3/tylee/lovedildo/minipixel.png",
        "toxd_transparent == 'dick'",  "bk3/tylee/lovedildo/xray_dick1.png",
        "toxd_transparent == 'dildo'",   "bk3/tylee/lovedildo/body_1_tp.png"), 
    (0, 0), "toxd_head lewd",
    )

image toxd toxd02 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_2.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_2.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_2.png"),
    (0, 0), ConditionSwitch(        
        "toxd_transparent == 'false'",  "bk3/tylee/lovedildo/minipixel.png",
        "toxd_transparent == 'dick'",  "bk3/tylee/lovedildo/xray_dick2.png",
        "toxd_transparent == 'dildo'",   "bk3/tylee/lovedildo/body_2_tp.png"), 
    (0, 3), "toxd_head lewd",
    )

image toxd toxd03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_3.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_3.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_3.png"),
    (0, 0), ConditionSwitch(        
        "toxd_transparent == 'false'",  "bk3/tylee/lovedildo/minipixel.png",
        "toxd_transparent == 'dick'",  "bk3/tylee/lovedildo/xray_dick3.png",
        "toxd_transparent == 'dildo'",   "bk3/tylee/lovedildo/body_3_tp.png"), 
    (0, 6), "toxd_head lewd",
    )
image toxd toxd04 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/body_4.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_4.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_4.png"),
    (0, 0), ConditionSwitch(        
        "toxd_transparent == 'false'",  "bk3/tylee/lovedildo/minipixel.png",
        "toxd_transparent == 'dick'",  "bk3/tylee/lovedildo/xray_dick4.png",
        "toxd_transparent == 'dildo'",   "bk3/tylee/lovedildo/body_4_tp.png"), 
    (0, 9), "toxd_head lewd",
    )

image toxd toxd05a = LiveComposite(
    (1000, 720),
    (0, -40), "bk3/tylee/lovedildo/body_5.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_5.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_5.png"), 
    (0, 0), ConditionSwitch(        
        "toxd_transparent == 'false'",  "bk3/tylee/lovedildo/minipixel.png",
        "toxd_transparent == 'dick'",  "bk3/tylee/lovedildo/xray_dick5.png",
        "toxd_transparent == 'dildo'",   "bk3/tylee/lovedildo/body_5_tp.png"), 
    (0, 12), "toxd_head lewd",
    )

image toxd toxd05b = LiveComposite(
    (1000, 720),
    (0, -40), "bk3/tylee/lovedildo/body_5.png",
    (0, 0), ConditionSwitch(        
        "toxd_dildo == False",  "bk3/tylee/lovedildo/playerbody_5.png",
        "toxd_dildo == True",   "bk3/tylee/lovedildo/dildo_5.png"),
    (0, 0), ConditionSwitch(        
        "toxd_transparent == 'false'",  "bk3/tylee/lovedildo/minipixel.png",
        "toxd_transparent == 'dick'",  "bk3/tylee/lovedildo/xray_dick5.png",
        "toxd_transparent == 'dildo'",   "bk3/tylee/lovedildo/body_5_tp.png"),  
    (0, 0), "bk3/tylee/lovedildo/face_shock.png",    
    )




image toxd toxd06 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/afterdildo_body.png",
    (0, 0), "bk3/tylee/lovedildo/afterdildo_dildo.png",      
    )
image toxd toxd07 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/afterdildo_body.png",
    (0, 0), "bk3/tylee/lovedildo/afterdildo_dildo2.png",      
    )
image toxd toxd08 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/afterdildo_body.png",          
    (0, 0), "bk3/tylee/lovedildo/arm_spreadlips.png",         
    )





image toxd_head eyesdown = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/head_solo.png",
    (0, 0), "toxd_blink",
    )
image toxd_head lewd = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/head_solo.png",
    (0, 0), "bk3/tylee/lovedildo/face_lewd.png",   
    )

image toxd_head eyeshalf = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/head_solo.png",
    (0, 0), "bk3/tylee/lovedildo/face_lewd2.png",   
    )

image toxd_head eyesfront = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/tylee/lovedildo/head_solo.png",
    (0, 0), "bk3/tylee/lovedildo/face_eyesfront.png",
    (0, 0), "toxd_blink",
    )

image toxd_blink:
    "bk3/tylee/lovedildo/minipixel.png"
    1.0
    "bk3/tylee/lovedildo/face_blink.png"
    0.3
    "bk3/tylee/lovedildo/minipixel.png"
    7.0
    "bk3/tylee/lovedildo/face_blink.png"
    0.3
    "bk3/tylee/lovedildo/minipixel.png"
    3.0
    "bk3/tylee/lovedildo/face_blink.png"
    0.3
    "bk3/tylee/lovedildo/minipixel.png"
    6.0
    repeat

image toxd_spermgush:
    "bk3/tylee/lovedildo/sperm_gush1.png"
    0.3
    "bk3/tylee/lovedildo/sperm_gush2.png"
    0.3
    "bk3/tylee/lovedildo/sperm_gush3.png"
    0.3
    repeat


image toxd toxd100:
    "toxd toxd01"
    0.3
    "toxd toxd02"
    0.3
    "toxd toxd03"
    0.3
    "toxd toxd04"
    0.3
    "toxd toxd05a"
    0.3
    "toxd toxd04"
    0.3
    "toxd toxd03"
    0.3
    "toxd toxd02"
    0.3

    repeat

image toxd toxd101:
    "toxd toxd01"
    0.5
    "toxd toxd05b" with vpunch
    1.0
    "toxd toxd04"
    0.2
    "toxd toxd03"
    0.2
    "toxd toxd02"
    0.2

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
