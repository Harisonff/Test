


init:
    $ totu_maingirl = 'neutral'
    $ totu_winggirls = 'neutral'
    $ totu_redface = 'neutral'




image totu_red = LiveComposite(  
    (1000, 720),
    (0, 0), "bk3/meangirls/reward/red_body.png",    
    (0, 0), ConditionSwitch(        
        "totu_redgirl == 'neutral'"    ,"bk3/meangirls/reward/red_hands.png", 
        "totu_redgirl == 'spread'"     ,"bk3/meangirls/reward/red_pussy.png",        
        "totu_redgirl == 'sperm'"      ,"bk3/meangirls/reward/red_sperm.png",
        "totu_redgirl == 'piss'"       ,"totu_red_piss",
        "totu_redgirl == 'masturbate'" ,"totu_red_masturbate"),    
    (441, 129), ConditionSwitch(        
        "totu_redface == 'neutral'"    ,"bk3/meangirls/reward/minipixel.png",
        "totu_redface == 'shock'" ,     "bk3/meangirls/reward/red_shock.png"),   
    (441, 129), "totu_red_blink",  
    )

image totu_white = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/meangirls/reward/white_body.png",
    (0, 0), ConditionSwitch(        
        "totu_whitegirl == 'neutral'"    , "bk3/meangirls/reward/white_hands.png",
        "totu_whitegirl == 'spread'"     , "bk3/meangirls/reward/white_pussy.png",
        "totu_whitegirl == 'sperm'"     , "bk3/meangirls/reward/white_sperm.png",
        "totu_whitegirl == 'piss'"       , "totu_white_piss",
        "totu_whitegirl == 'masturbate'" , "totu_white_masturbate"), 
    )

image totu_pink = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/meangirls/reward/pink_body.png",
    (0, 0), ConditionSwitch(        
        "totu_pinkgirl == 'neutral'"    , "bk3/meangirls/reward/pink_hands.png",
        "totu_pinkgirl == 'spread'"     , "bk3/meangirls/reward/pink_pussy.png",
        "totu_pinkgirl == 'sperm'"     , "bk3/meangirls/reward/pink_sperm.png",
        "totu_pinkgirl == 'piss'"       , "totu_pink_piss",
        "totu_pinkgirl == 'masturbate'" , "totu_pink_masturbate"), 
    )

image totu totu01 = LiveComposite(
    (1000, 720),
    (0, 140), "totu_red",
    (-300, 0), "totu_white",
    (300, 0), "totu_pink",
    )


image totu totu02 = LiveComposite(
    (1000, 720),    
    (-200, 150), "totu_white",
    (200, 150), "totu_pink",
    (0, -270), "totu_red_flipped",
    )

image totu totu03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/meangirls/reward/idle_clothes.png",
    (0, 0), "bk3/meangirls/reward/idle_heads.png",  
    (584, 220), "totu_idleblink",  
    
    )

image totu totu04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/meangirls/reward/idle_nude.png",
    (0, 0), "bk3/meangirls/reward/idle_heads_2.png", 
    (584, 220), "totu_idleblink",  
    )

image totu_red_flipped:
    yzoom -1 ypos -150
    "totu_red"


image totu_idleblink:
    "bk3/meangirls/reward/minipixel.png"
    0.3
    "bk3/meangirls/reward/blink_idle.png"
    0.3
    "bk3/meangirls/reward/minipixel.png"
    9.0
    "bk3/meangirls/reward/blink_idle.png"
    0.3
    "bk3/meangirls/reward/minipixel.png"
    4.0
    "bk3/meangirls/reward/blink_idle.png"
    0.3
    "bk3/meangirls/reward/minipixel.png"
    7.0

    repeat

image totu_red_blink:
    "bk3/meangirls/reward/minipixel.png"
    0.3
    "bk3/meangirls/reward/red_blink.png"
    0.3
    "bk3/meangirls/reward/minipixel.png"
    0.3
    "bk3/meangirls/reward/red_blink.png"
    0.3
    "bk3/meangirls/reward/minipixel.png"
    4.0
    "bk3/meangirls/reward/red_blink.png"
    0.3
    "bk3/meangirls/reward/minipixel.png"
    7.0

    repeat


image totu_red_masturbate:
    "bk3/meangirls/reward/red_mastur1.png"
    0.3
    "bk3/meangirls/reward/red_mastur2.png"
    0.3
    "bk3/meangirls/reward/red_mastur3.png"
    0.3
    "bk3/meangirls/reward/red_mastur4.png"
    0.3
    "bk3/meangirls/reward/red_mastur3.png"
    0.3
    "bk3/meangirls/reward/red_mastur2.png"
    0.3
    repeat

image totu_red_piss:
    "bk3/meangirls/reward/red_piss1.png"
    0.3
    "bk3/meangirls/reward/red_piss2.png"
    0.3
    "bk3/meangirls/reward/red_piss3.png"
    0.3
    "bk3/meangirls/reward/red_piss2.png"
    0.3
    repeat

image totu_white_masturbate:
    "bk3/meangirls/reward/white_mastur1.png"
    0.3
    "bk3/meangirls/reward/white_mastur2.png"
    0.3
    "bk3/meangirls/reward/white_mastur3.png"
    0.3
    "bk3/meangirls/reward/white_mastur4.png"
    0.3
    "bk3/meangirls/reward/white_mastur3.png"
    0.3
    "bk3/meangirls/reward/white_mastur2.png"
    0.3
    repeat

image totu_white_piss:
    "bk3/meangirls/reward/white_piss1.png"
    0.3
    "bk3/meangirls/reward/white_piss2.png"
    0.3
    "bk3/meangirls/reward/white_piss3.png"
    0.3
    "bk3/meangirls/reward/white_piss2.png"
    0.3
    repeat

image totu_pink_masturbate:
    "bk3/meangirls/reward/pink_mastur1.png"
    0.3
    "bk3/meangirls/reward/pink_mastur2.png"
    0.3
    "bk3/meangirls/reward/pink_mastur3.png"
    0.3
    "bk3/meangirls/reward/pink_mastur4.png"
    0.3
    "bk3/meangirls/reward/pink_mastur3.png"
    0.3
    "bk3/meangirls/reward/pink_mastur2.png"
    0.3
    repeat

image totu_pink_piss:
    "bk3/meangirls/reward/pink_piss1.png"
    0.3
    "bk3/meangirls/reward/pink_piss2.png"
    0.3
    "bk3/meangirls/reward/pink_piss3.png"
    0.3
    "bk3/meangirls/reward/pink_piss2.png"
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
