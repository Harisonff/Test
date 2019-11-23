






init:
    $ june_pubes = 'shaven'

image toju toju01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body.png",
    (0, 0), "bk3/june/idles/arms_side.png",
    (0, 0), "bk3/june/idles/tits_covered.png",
    )
image toju toju02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body.png",
    (0, 0), "bk3/june/idles/arms_side.png",
    (0, 0), "bk3/june/idles/tits_covered.png",
    (0, 0), "bk3/june/idles/smile.png",
    )
image toju toju03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body.png",
    (0, 0), "bk3/june/idles/arms_whip.png",
    (0, 0), "bk3/june/idles/tits_covered.png",
    (0, 0), "bk3/june/idles/angry.png",
    )

image toju toju04 = LiveComposite(
    (1000, 720),   
    (0, 0), "bk3/june/idles/arms_straight.png",
    (0, 0), "bk3/june/idles/body.png",
    (0, 0), "bk3/june/idles/tits_covered.png",
    (0, 0), "bk3/june/idles/surprise.png",
    )



image toju toju08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_side.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",
    (0, 0), "bk3/june/idles/surprise.png",    
    )

image toju toju09 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_side.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",    
    )

image toju toju10 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_straight.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",    
    )

image toju toju11 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_straight.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",
    (0, 0), "bk3/june/idles/angry.png",
    )
image toju toju12 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_straight.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",
    (0, 0), "bk3/june/idles/smile.png",
    )

image toju toju13 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_pushup0.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",
    (0, 0), "bk3/june/idles/arms_pushup4.png",
    (0, 0), "bk3/june/idles/smile.png",
    )

image toju toju14 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_pushup0.png",
    (0, 0), "bk3/june/idles/arms_pushup2.png",
    (0, 0), "bk3/june/idles/smile.png",
    )
image toju toju15 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_pushup0.png",
    (0, 0), "bk3/june/idles/arms_pushup3.png",
    (0, 0), "bk3/june/idles/smile.png",
    )
image toju toju16 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_straight.png",
    (0, 0), "bk3/june/idles/bare_tits.png",
    (0, 0), "bk3/june/idles/smile.png",
    )

image toju toju17 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_pushup0.png",
    (0, 0), "bk3/june/idles/arms_pushup1.png",
    (0, 0), "bk3/june/idles/smile.png",
    )


image toju toju18 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_pushup0.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",
    (0, 0), "bk3/june/idles/arms_skirtup.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'shaven'","transparent.png",
        "june_pubes == 'bush'", "bk3/june/idles/pubes.png"),
    (0, 0), "bk3/june/idles/smile.png",
    )





image toju toju19 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body_nude.png",  
    (0, 0), ConditionSwitch( 
        "june_pubes == 'shaven'","transparent.png",
        "june_pubes == 'bush'", "bk3/june/idles/pubes.png"),
    (0, 0), "bk3/june/idles/arms_straight.png",
    (0, 0), "bk3/june/idles/tits_nude.png",
    )
image toju toju20 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body_nude.png",    
    (0, 0), "bk3/june/idles/arms_side.png",
    (0, 0), "bk3/june/idles/tits_nude.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'shaven'","transparent.png",
        "june_pubes == 'bush'", "bk3/june/idles/pubes.png"),
    )

image toju toju21 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body_nude1.png", 
    (0, 0), "bk3/june/idles/tits_nude.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'shaven'","transparent.png",
        "june_pubes == 'bush'", "bk3/june/idles/pubes.png"),
    (0, 0), "bk3/june/idles/arms_straight.png",
    )
image toju toju22 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/body_nude1.png",    
    (0, 0), "bk3/june/idles/arms_side.png",
    (0, 0), "bk3/june/idles/tits_nude.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'shaven'","transparent.png",
        "june_pubes == 'bush'", "bk3/june/idles/pubes.png"),
    )

image toju toju23 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/idles/wbody.png",
    (0, 0), "bk3/june/idles/arms_pushup0.png",
    (0, 0), "bk3/june/idles/tits_halfcovered.png",
    (0, 0), "bk3/june/idles/arms_skirtup1.png",
    (0, 0), "bk3/june/idles/smile.png",
    (0, 0), ConditionSwitch( 
        "june_pubes == 'shaven'","transparent.png",
        "june_pubes == 'bush'", "bk3/june/idles/pubes.png"),
    )









image toju_hypno_eyes = "bk3/june/idles/hypno_eye.png"
image toju_blink = "bk3/june/idles/blink.png"
image toju_blush = "bk3/june/idles/blush.png"
image toju_panties = "bk3/june/idles/panties.png"
image toju_pantiesperm = "bk3/june/idles/panties_sperm.png"





image toju toju100:
    "toju toju14"
    0.3
    "toju toju15"
    0.3
    "toju toju17"
    0.1

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
