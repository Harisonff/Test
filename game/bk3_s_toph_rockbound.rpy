





init:
    $ tots_head = 'none'


image tots tots00 = LiveComposite(
    (1000, 720),
    
    (0, -20), "tots_head",
    (0, -20), "tots_blink",
    (0, -35), "bk3/toph/rockbound/hair_1.png",
    )

image tots tots01 = LiveComposite(
    (1000, 720),
    
    (0, -20), "tots_head",
    (0, -20), "tots_blink",
    (0, 0), "bk3/toph/rockbound/solodick.png",
    (0, -35), "bk3/toph/rockbound/hair_1.png",
    )

image tots tots05 = LiveComposite(
    (1000, 720),
    
    (0, 0), "tots_head",
    (0, -20), "bk3/toph/rockbound/dick_1.png",
    (0, -20), "bk3/toph/rockbound/hair_1.png",
    )

image tots tots08 = LiveComposite(
    (1000, 720),
    
    (0, 53), "tots_head",
    (0, -16), "bk3/toph/rockbound/dick_4.png",
    (0, -20), "bk3/toph/rockbound/hair_4.png",
    )
image tots tots09 = LiveComposite(
    (1000, 720),
    
    (0, 53), "tots_head",
    (0, -16), "bk3/toph/rockbound/dick_4.png",
    (0, 0), "bk3/toph/rockbound/hair_3.png",
    )

image tots tots10 = LiveComposite(
    (1000, 720),
    
    (0, 53), "tots_head",
    (0, -16), "bk3/toph/rockbound/dick_4.png",
    (0, 20), "bk3/toph/rockbound/hair_2.png",
    )
image tots tots11 = LiveComposite(
    (1000, 720),
    
    (0, 35), "tots_head",
    (0, -20), "bk3/toph/rockbound/dick_3.png",
    (0, 20), "bk3/toph/rockbound/hair_1.png",
    )
image tots tots12 = LiveComposite(
    (1000, 720),
    
    (0, 20), "tots_head",
    (0, -20), "bk3/toph/rockbound/dick_2.png",
    (0, 0), "bk3/toph/rockbound/hair_1.png",
    )

image tots tots14 = LiveComposite(
    (1000, 720),
    
    (0, -20), "tots_head",
    (0, -20), "tots_blink",
    (0, 20), "bk3/toph/rockbound/solodick.png",   
    (0, -40), "bk3/toph/rockbound/hair_1.png",
    )

image tots tots15 = LiveComposite(
    (1000, 720),
    
    (0, -20), "tots_head",

    (0, -20), "bk3/toph/rockbound/wipeaway_2.png",
    
    )

image tots_head = LiveComposite(
    (1000, 720),   
    (0, 0), "bk3/toph/rockbound/head_1.png",
    (0, 0), ConditionSwitch(        
        "tots_head == 'none'",  "transparent.png", 
        "tots_head == 'angry'",  "bk3/toph/rockbound/angry.png", 
        "tots_head == 'blink'",  "bk3/toph/rockbound/blink.png",),    
    )






image tots tots100:
    "tots tots05"
    0.3
    "tots tots08"
    0.3
    "tots tots09"
    0.3
    "tots tots10"
    0.3
    "tots tots11"
    0.3
    "tots tots12"
    0.3
    repeat

image tots_blink:
    "transparent.png"
    0.3
    "bk3/toph/rockbound/blink.png"
    0.3
    "transparent.png"
    6.0
    "bk3/toph/rockbound/blink.png"
    0.3
    "transparent.png"
    8.0
    "bk3/toph/rockbound/blink.png"
    0.3
    repeat


image tots_sacksuck:
    "bk3/toph/rockbound/tug1.png"
    0.3
    "bk3/toph/rockbound/tug2.png"
    0.3
    "bk3/toph/rockbound/tug3.png"
    0.3
    "bk3/toph/rockbound/tug2.png"
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
