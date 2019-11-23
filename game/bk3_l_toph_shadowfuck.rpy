







init:
    $ totx_head = 'happy'



image totx totx01 = LiveComposite(
    (1000, 720),    
    (0, 8), "bk3/toph/shadowfuck/body_1.png", 
    (425, -2), "totx_face", 
    (0, 8), "bk3/toph/shadowfuck/fuck_1.png",     
    )

image totx totx02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_2.png", 
    (425, -50), "totx_face", 
    (0, 0), "bk3/toph/shadowfuck/fuck_2.png",     
    )

image totx totx03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_3.png", 
    (425, -70), "totx_face", 
    (0, 0), "bk3/toph/shadowfuck/fuck_3.png",     
    )

image totx totx04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_4.png", 
    (425, -110), "totx_face", 
    (0, 0), "bk3/toph/shadowfuck/fuck_4.png",     
    )

image totx totx05 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_1.png", 
    (425, -10), "totx_face", 
    (0, 0), "bk3/toph/shadowfuck/dick_solo.png",     
    )
image totx totx06 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_4.png", 
    (425, -110), "totx_face", 
    (0, 0), "bk3/toph/shadowfuck/dick_solo.png",     
    )

image totx totx07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_5.png",
    )

image totx totx08 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/toph/shadowfuck/body_0.png",
    )






image totx_face = LiveComposite(
    (277, 300),       
    (0, 0), ConditionSwitch(        
        "totx_head == 'happy'", "bk3/toph/shadowfuck/head_happy.png",  
        "totx_head == 'careful'", "bk3/toph/shadowfuck/head_careful.png",
        "totx_head == 'shock'", "bk3/toph/shadowfuck/head_shock.png",
        "totx_head == 'lewd'", "bk3/toph/shadowfuck/head_lewd.png",
        "totx_head == 'worried'", "bk3/toph/shadowfuck/head_worried.png"), 
    (0, 0), "totx_blink",  
    )

image totx_blink:
    "bk3/toph/shadowfuck/blink.png"
    0.3
    "bk3/toph/shadowfuck/minipixel.png"
    4.0
    repeat









image totx_spermdrip:
    "bk3/toph/shadowfuck/spermdrip_1.png"
    0.3
    "bk3/toph/shadowfuck/spermdrip_2.png"
    0.3
    "bk3/toph/shadowfuck/spermdrip_3.png"
    0.3
    "bk3/toph/shadowfuck/spermdrip_2.png"
    0.3
    repeat


image totx totx100:
    "totx  totx01"
    0.3
    "totx  totx02"
    0.3
    "totx  totx03"
    0.3
    "totx  totx04"
    0.3
    "totx  totx03"
    0.3
    "totx  totx02"
    repeat

image totx totx101:
    "totx  totx04"
    0.3
    "totx  totx01" with vpunch
    1.3
    "totx  totx02"
    0.3
    "totx  totx03"
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
