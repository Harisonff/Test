







image tojl tojl01 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/headlock/small_sit.png",
    )

image tojl tojl02 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/headlock/big_sit.png",     
    (0, 0), ConditionSwitch( 
        "june_pubes == 'bush'", "bk3/june/headlock/pubes.png",        
        "june_pubes == 'shaven'", "transparent.png"), 
    (0, 0), "tojl_jiggle_headlock", 
    )

image tojl tojl03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/headlock/big_sit.png", 
    (0, 0), "bk3/june/headlock/big_armsfree.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'bush'", "bk3/june/headlock/pubes.png",        
        "june_pubes == 'shaven'", "transparent.png"),      
    )

image tojl tojl04 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/headlock/big_cum.png",
    (0, 0), "bk3/june/headlock/big_cum_armsbound.png", 
    (0, 0), ConditionSwitch( 
        "june_pubes == 'bush'", "bk3/june/headlock/pubes_front.png",        
        "june_pubes == 'shaven'", "transparent.png"), 
    (749, 177), "tojl_blink_cum ",
    )
image tojl tojl05 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/june/headlock/big_cum.png", 
    (0, 0), "bk3/june/headlock/big_cum_armsfree.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'bush'", "bk3/june/headlock/pubes_front.png",        
        "june_pubes == 'shaven'", "transparent.png"),     
    (749, 177), "tojl_blink_cum ", 
    )





image tojl_tug:
    xpos 795 ypos 720
    "bk3/june/headlock/tug1.png"
    0.3
    "bk3/june/headlock/tug2.png"
    0.3
    "bk3/june/headlock/tug3.png"
    0.3
    "bk3/june/headlock/tug2.png"
    0.3
    repeat

image tojl_jiggle_headlock:
    "bk3/june/headlock/big_armsbound1.png"
    0.3
    "bk3/june/headlock/big_armsbound2.png"
    0.3
    "bk3/june/headlock/big_armsbound1.png"
    0.3
    "bk3/june/headlock/big_armsbound2.png"
    5.3
    repeat

image tojl_blink_cum:
    "bk3/june/headlock/blink.png"
    0.3
    "bk3/june/headlock/transparent_small.png"
    0.3
    "bk3/june/headlock/blink.png"
    0.3
    "bk3/june/headlock/transparent_small.png"
    8.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
