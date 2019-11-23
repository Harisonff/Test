


image bfay bfay00 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/backgrounds/bg_hangkorra.jpg",  
    (0, 0), "bk4/korra/bj/hangkorra.png",    
    )

image bfay bfay01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/armbod.png",  
    (0, 0), "bfay_korra", 
    (0, 0), "bfay_blink",
    (0, 0), "bfay_player", 
    (0, 0), "bk4/korra/bj/arm_solo.png",
    )

image bfay bfay02 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png",     
    )

image bfay bfay03 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png",     
    (0, 0), "bk4/korra/bj/playerbod_0.png",    
    )
image bfay bfay03a = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png",     
    (0, 0), "bk4/korra/bj/playerbod_0.png",    
    (0, 0), "bk4/korra/bj/cryface.png",   
    (0, 0), "bfay_blink",  
    )

image bfay bfay04 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png", 
    (0, 0), "bk4/korra/bj/dick_solo.png",
    (0, 0), "bk4/korra/bj/playerbod_0.png",
    )

image bfay bfay04a = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png", 
    (0, 0), "bk4/korra/bj/jack2.png",
    (0, 0), "bk4/korra/bj/cryface.png",
    (0, 0), "bfay_blink",
    (0, 0), "bk4/korra/bj/playerbod_0.png",
    )

image bfay bfay05 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/armbod.png",   
    (0, 0), "bk4/korra/bj/korrabod_1.png",   
    (0, 0), "bfay_blink",   
    (0, 0), "bk4/korra/bj/playerbod_1.png",
    (0, 0), "bk4/korra/bj/arm_solo.png",    
    )


image bfay bfay06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png", 
    (0, 0), "bfay_jack",
    (0, 0), "bk4/korra/bj/cryface.png",
    (0, 0), "bfay_blink", 
    (0, 0), "bk4/korra/bj/playerbod_0.png",
    )

image bfay bfay06a = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/korrabod_0.png", 
    (0, 0), "bk4/korra/bj/jack2.png",
    (0, 0), "bk4/korra/bj/cryface.png",
    (0, 0), "bk4/korra/bj/playerbod_0.png",
    )

image bfay bfay07 = LiveComposite(
    (1000, 720), 
    (40, 0), "bk4/korra/bj/armbod.png",
    (40, 0), "bk4/korra/bj/korrabod_4.png", 
    (40, 0), "bk4/korra/bj/blinkhard.png",
    (40, 0), "bk4/korra/bj/playerbod_4.png",
    (40, 0), "bk4/korra/bj/arm_solo.png",    
    )




image bfay bfay08a = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/armbod.png",  
    (0, 0), "bk4/korra/bj/korrabod_1.png",
    (0, 0), "bk4/korra/bj/playerbod_1.png", 
    (0, 0), "bk4/korra/bj/arm_solo.png",
    )
image bfay bfay08b = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/armbod.png",  
    (0, 0), "bk4/korra/bj/korrabod_1.png",
    (0, 0), "bk4/korra/bj/playerbod_2.png", 
    (0, 0), "bk4/korra/bj/arm_solo.png",
    )
image bfay bfay08c = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/korra/bj/armbod.png",  
    (0, 0), "bk4/korra/bj/korrabod_1.png",
    (0, 0), "bk4/korra/bj/playerbod_3.png", 
    (0, 0), "bk4/korra/bj/arm_solo.png",
    )


image bfay bfay08:
    "bfay bfay08c"
    0.15
    "bfay bfay08b"
    0.15
    "bfay bfay08a"
    0.15
    "bfay bfay07" with hpunch
    0.6
    repeat


image bfay_shock:
    "bk4/korra/bj/shock1.png" with hpunch
    0.8
    "bk4/korra/bj/shock2.png"
    1.0

image bfay_spermshot:
    "bk4/korra/bj/spermshot.png"
    0.2
    "bk4/misc/minipixel.png"
    1.0


image bfay_blink:
    parallel:
        "bk4/korra/bj/blink.png"
        0.2
        "bk4/misc/minipixel.png"
        0.2
        "bk4/korra/bj/blink.png"
        0.2
        "bk4/misc/minipixel.png"
        0.2
        "bk4/korra/bj/blink.png"
        0.2
        "bk4/misc/minipixel.png"
        0.2
    parallel:
        "bk4/korra/bj/blink.png"
        0.3
        "bk4/misc/minipixel.png"
        6.0
        "bk4/korra/bj/blink.png"
        0.3
        "bk4/misc/minipixel.png"
        6.0
        repeat

image bfay_jack:
    "bk4/korra/bj/jack1.png"
    0.07
    "bk4/korra/bj/jack2.png"
    0.07
    "bk4/korra/bj/jack3.png"
    0.07
    "bk4/korra/bj/jack2.png"
    0.07
    repeat

image bfay_korra:
    "bk4/korra/bj/korrabod_1.png"
    0.2
    "bk4/korra/bj/korrabod_2.png"
    0.2
    "bk4/korra/bj/korrabod_3.png"
    0.2
    "bk4/korra/bj/korrabod_4.png"
    0.2
    "bk4/korra/bj/korrabod_3.png"
    0.2
    "bk4/korra/bj/korrabod_2.png"
    0.2
    repeat

image bfay_player:
    "bk4/korra/bj/playerbod_1.png"
    0.2
    "bk4/korra/bj/playerbod_2.png"
    0.2
    "bk4/korra/bj/playerbod_3.png"
    0.2
    "bk4/korra/bj/playerbod_4.png"
    0.2
    "bk4/korra/bj/playerbod_3.png"
    0.2
    "bk4/korra/bj/playerbod_2.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
