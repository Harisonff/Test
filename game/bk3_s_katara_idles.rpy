







image toki toki01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hanging.png",
    )

image toki toki02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_crossed.png",
    )

image toki toki03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hug.png",
    )

image toki toki04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_face.png",
    )

image toki toki_smile = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hanging.png",
    (0, 0), "bk3/katara/idle/smile.png",
    )

image toki toki_angry = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hanging.png",
    (0, 0), "bk3/katara/idle/angry.png",
    )

image toki toki_angry_blink = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hanging.png",
    (0, 0), "bk3/katara/idle/angry.png",
    (0, 0), "bk3/katara/idle/blink.png",
    )

image toki toki_surprise = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hanging.png",
    (0, 0), "bk3/katara/idle/surprise.png",
    )

image toki toki_blink = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/idle/idle_body.png",
    (0, 0), "bk3/katara/idle/arms_hanging.png",
    (0, 0), "bk3/katara/idle/blink.png",
    )




image toki_angry = "bk3/katara/idle/angry.png"
image toki_smile = "bk3/katara/idle/smile.png"
image toki_blink = "bk3/katara/idle/blink.png"
image toki_surprised = "bk3/katara/idle/surprise.png"














init:
    $ katara_top_nude = False
    $ katara_bottom_nude = False

image toki toki10 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/swim_idle/sbody.png",
    
    (0, 0), ConditionSwitch( 
        "katara_bottom_nude == False","bk3/katara/swim_idle/spants.png",  
        "katara_bottom_nude == True","transparent.png"), 
    
    (0, 0), "bk3/katara/swim_idle/sarms_side.png",
    (0, 0), ConditionSwitch( 
        "katara_top_nude == False","bk3/katara/swim_idle/swim_top.png",
        "boobs == 'big'", "bk3/katara/swim_idle/bigboobs.png",
        "boobs == 'medium'", "bk3/katara/swim_idle/mediboobs.png",
        "boobs == 'small'", "bk3/katara/swim_idle/smallboobs.png"), 
    )

image toki toki11 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/swim_idle/sbody.png",
    
    (0, 0), ConditionSwitch( 
        "katara_bottom_nude == False","bk3/katara/swim_idle/spants.png",  
        "katara_bottom_nude == True","transparent.png"), 
    
    (0, 0), "bk3/katara/swim_idle/sarms_avoid_water.png",
    (0, 0), ConditionSwitch( 
        "katara_top_nude == False","bk3/katara/swim_idle/swim_top.png",
        "boobs == 'big'", "bk3/katara/swim_idle/bigboobs.png",
        "boobs == 'medium'", "bk3/katara/swim_idle/mediboobs.png",
        "boobs == 'small'", "bk3/katara/swim_idle/smallboobs.png"), 
    )

image toki toki12 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/katara/swim_idle/sbody.png",
    (0, 0), "bk3/katara/swim_idle/sarms_swoop_back.png",
    
    (0, 0), ConditionSwitch( 
        "katara_bottom_nude == False","bk3/katara/swim_idle/spants.png",  
        "katara_bottom_nude == True","transparent.png"), 
    
    
    (0, 0), ConditionSwitch( 
        "katara_top_nude == False","bk3/katara/swim_idle/swim_top.png",
        "boobs == 'big'", "bk3/katara/swim_idle/bigboobs.png",
        "boobs == 'medium'", "bk3/katara/swim_idle/mediboobs.png",
        "boobs == 'small'", "bk3/katara/swim_idle/smallboobs.png"), 
    
    (0, 0), "bk3/katara/swim_idle/sarms_swoop_front.png",
    )

image toki toki110:
    "toki toki10"
    1.5
    "toki toki12"
    1
    repeat

image toki_wave:
    "transparent"
    1.5
    "bk3/katara/swim_idle/splash.png"
    xpos 500
    linear 0.5 xpos -200
    0.5
    repeat


image toki_swim_angry = "bk3/katara/swim_idle/angry.png"
image toki_swim_smile = "bk3/katara/swim_idle/smile.png"
image toki_swim_blink = "bk3/katara/swim_idle/blink.png"
image toki_swim_surprised = "bk3/katara/swim_idle/surprise.png"
image toki_swim_lookleft = "bk3/katara/swim_idle/eyes_leftlook.png"
image toki_swim_oneeye = "bk3/katara/swim_idle/eyes_oneeye.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
