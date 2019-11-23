





init:
    $ nagachibi_head = 'down'

image tonc tonc00 = LiveComposite(
    (1000, 720),   
    (0, 0), "bk3/naga/titjob/body_aang.png",    
    )

image tonc tonc01 = LiveComposite(
    (1000, 720),   
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 0), "bk3/naga/titjob/claw_down.png",
    (582, 205), "bk3/naga/titjob/tits1.png",
    (530, 50), ConditionSwitch(        
        "nagachibi_head == 'up'", "bk3/naga/titjob/head_up.png",
        "nagachibi_head == 'down'", "bk3/naga/titjob/head_down.png"),    
    )

image tonc tonc02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 3), "bk3/naga/titjob/claw_down.png",
    (582, 208), "bk3/naga/titjob/tits1.png",    
    (530, 52), ConditionSwitch(        
        "nagachibi_head == 'up'", "bk3/naga/titjob/head_up.png",
        "nagachibi_head == 'down'", "bk3/naga/titjob/head_down.png"),
    )
image tonc tonc03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 6), "bk3/naga/titjob/claw_down1.png",
    (582, 215), "bk3/naga/titjob/tits2.png",
    (530, 56), ConditionSwitch(        
        "nagachibi_head == 'up'", "bk3/naga/titjob/head_up.png",
        "nagachibi_head == 'down'", "bk3/naga/titjob/head_down.png"),
    )
image tonc tonc04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 9), "bk3/naga/titjob/claw_down1.png",
    (582, 220), "bk3/naga/titjob/tits3.png",
    (530, 67), ConditionSwitch(        
        "nagachibi_head == 'up'", "bk3/naga/titjob/head_up.png",
        "nagachibi_head == 'down'", "bk3/naga/titjob/head_down.png"),
    )

image tonc tonc06 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 1), "bk3/naga/titjob/claw_down2.png",
    
    )

image tonc tonc07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 1), "bk3/naga/titjob/claw_down2.png",
    (530, 67), ConditionSwitch(        
        "nagachibi_head == 'up'", "bk3/naga/titjob/head_up.png",
        "nagachibi_head == 'down'", "bk3/naga/titjob/head_down.png"),
    )
image tonc tonc08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 1), "bk3/naga/titjob/claw_down2.png",
    (1, 1), "bk3/naga/titjob/tongue_down.png",    
    (530,60), "bk3/naga/titjob/head_tongue.png",
    )
image tonc tonc09 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 2), "bk3/naga/titjob/claw_down2.png",
    (1, 2), "bk3/naga/titjob/tongue_down.png",    
    (530,70), "bk3/naga/titjob/head_tongue.png",
    )
image tonc tonc10 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/body_aang.png",
    (0, 3), "bk3/naga/titjob/claw_down2.png",    
    (1, 3), "bk3/naga/titjob/tongue_down.png",    
    (530,80), "bk3/naga/titjob/head_tongue.png",
    )

image tonc tonc15 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/float1.png",
    (0, 0), "bk3/naga/titjob/fatbelly.png",
    )
image tonc tonc16 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/naga/titjob/float2.png",
    (0, 0), "bk3/naga/titjob/fatbelly.png",
    )





image tonc_tail:
    "bk3/naga/titjob/tail.png"
    0.4
    "bk3/naga/titjob/taila.png"
    0.4
    "bk3/naga/titjob/tailb.png"
    0.4
    "bk3/naga/titjob/taila.png"
    0.4
    repeat




image tonc tonc100:
    "tonc tonc02"
    0.4
    "tonc tonc03"
    0.4
    "tonc tonc04"
    0.4
    "tonc tonc03"
    0.4
    repeat

image tonc tonc101:
    "tonc tonc10"
    0.4
    "tonc tonc09"
    0.4
    "tonc tonc08"
    0.4
    "tonc tonc09"
    0.4
    repeat

image tonc_floats:
    "bk3/naga/titjob/float1.png"
    0.8
    "bk3/naga/titjob/float2.png"
    0.8
    repeat

image tonc_floats_fatbelly:
    "tonc tonc15"
    0.8
    "tonc tonc16"
    0.8
    repeat


image tonc_floats_sperm:
    "bk3/naga/titjob/spermedon.png"
    0.8
    "bk3/naga/titjob/spermedon1.png"
    0.9
    repeat

image tonc_floats_spermedon = LiveComposite(
    (1000, 720),    
    (0, 0), "tonc_floats",
    (0, 0), "tonc_floats_sperm",
    )

image tonc_swallows:
    "bk3/naga/titjob/head_swallow.png"
    0.5
    "bk3/naga/titjob/head_swallow1.png"
    0.8
    repeat

image tonc_swallows2:
    "bk3/naga/titjob/head_swallow2.png"
    0.5
    "bk3/naga/titjob/head_swallow3.png"
    0.8
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
