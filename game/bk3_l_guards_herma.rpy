







init:
    $ totq_fucked = 'krystal'
    $ totq_fucked_with = 'realdick'

image totq totq00 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/bg_zoom.jpg",
    (0, 0), "bk3/guards/herma/bodies_both.png", 
    )

image totq totq01 = LiveComposite(
    (1000, 720),    
    (552, 0), "bk3/guards/herma/ani_1.png", 
    (454,340), "bk3/guards/herma/body_down1.png", 
    (540, 430), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/krystal_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/peanut_big.png"),   
    (545, 60), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/peanut_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/krystal_big.png"),   
         
    )
image totq totq02 = LiveComposite(
    (1000, 720),    
    (552, 0), "bk3/guards/herma/ani_2.png", 
    (454,340), "bk3/guards/herma/body_down1.png", 
    (540, 430), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/krystal_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/peanut_big.png"),      
    (545, 40), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/peanut_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/krystal_big.png"),     
    )
image totq totq03 = LiveComposite(
    (1000, 720),    
    (552, 0), "bk3/guards/herma/ani_3.png", 
    (454,340), "bk3/guards/herma/body_down1.png", 
    (540, 430), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/krystal_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/peanut_big.png"),      
    (545, 20), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/peanut_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/krystal_big.png"),     
    )


image totq totq04 = LiveComposite(
    (1000, 720),    
    (552, 0), "bk3/guards/herma/ani_4.png", 
    (454,340), "bk3/guards/herma/body_down1.png", 
    (540, 430), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/krystal_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/peanut_big.png"),         
    (545, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/peanut_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/krystal_big.png"),     
    )

image totq totq04b = LiveComposite(
    (1000, 720),    
    (552, 0), "bk3/guards/herma/ani_4.png", 
    (454,340), "bk3/guards/herma/body_down2.png", 
    (540, 430), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/krystal_headdown.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/peanut_headdown.png"),
    (545, 00), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/peanut_big.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/krystal_big.png"),   
    )


image totq_other = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/guards/herma/bg_fuck.jpg",
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_peanut.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_krystal.png"),
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_ani_0.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",   
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_ani_0.png"),    
    
    )

image totq totq10 = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_krystal.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_peanut.png"), 
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "totq_fuck",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",       
        "totq_fucked == 'peanut'", "totq_fuck"),    
    )

image totq totq11 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_krystal_2.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_peanut_2.png"), 
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_ani_6.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",   
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_ani_6.png"),    
    )
image totq totq12 = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_krystal.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_peanut.png"), 
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_ani_4.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",   
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_ani_4.png"),    
    )
image totq totq13 = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_krystal.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_peanut.png"), 
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_ani_3.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",   
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_ani_3.png"),    
    )

image totq totq14 = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_krystal.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_peanut.png"), 
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_ani_2.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",   
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_ani_2.png"),    
    )

image totq totq15 = LiveComposite(
    (1000, 720), 
    (0, 0), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_body_krystal.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_body_peanut.png"), 
    (600, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'", "bk3/guards/herma/2_ani_1.png",       
        "totq_fucked == 'peanut'", "bk3/guards/herma/minipixel.png"),    
    (210, 250), ConditionSwitch(        
        "totq_fucked == 'krystal'","bk3/guards/herma/minipixel.png",   
        "totq_fucked == 'peanut'", "bk3/guards/herma/2_ani_1.png"),    
    )

image totq totq16:
    "totq totq11" with vpunch
    1.2
    "totq totq12"
    0.3
    "totq totq13"
    0.3
    "totq totq14"
    0.3
    "totq totq15"
    0.3
    repeat

image totq totq17 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/guards/herma/2_body_krystal.png", 
    (0, 0), "bk3/guards/herma/2_body_peanut.png", 
    (600, 250), "bk3/guards/herma/2_ani_0.png", 
    (210, 250), "bk3/guards/herma/2_ani_0.png",
    )


image totq totq18:



    "totq totq15"
    0.5
    "totq totq11" with vpunch
    1.2
    "totq totq12"
    0.3
    "totq totq13"
    0.3
    "totq totq14"
    0.3
    repeat



image totq totq50 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/ddildo_2.png",
    )
image totq totq51 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/ddildo_4.png",
    (0, 0), "bk3/guards/herma/ddildo_3.png",
    (0, 0), "bk3/guards/herma/ddildo_5.png",
    )
image totq totq52 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/ddildo_4.png",
    (0, 0), "bk3/guards/herma/ddildo_3.png",
    )

image totq totq54 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    )
image totq totq55 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/growdick1.png",
    )
image totq totq56 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/growdick2.png",
    )
image totq totq57 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/growdick3.png",
    )
image totq totq58 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/ddildo_1.png",
    (0, 0), "bk3/guards/herma/growdick4.png",
    )

image totq totq59 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/guards/herma/bg_zoom.jpg",
    (0, 0), "bk3/guards/herma/spermdrip_bodies.png",
    (0, 0), "totq_spermdrip",
    )












image totq_spermdrip:
    "bk3/guards/herma/spermdrip1.png"
    0.2
    "bk3/guards/herma/spermdrip2.png"
    0.2
    "bk3/guards/herma/spermdrip3.png"
    0.2

    repeat


image totq totq100:
    "totq totq01"
    0.2
    "totq totq02"
    0.2
    "totq totq03"
    0.2
    "totq totq04"
    0.2
    "totq totq03"
    0.2
    "totq totq02"
    0.2
    repeat

image totq totq101:
    "totq totq01"
    0.2
    "totq totq04b" with vpunch
    1.2
    "totq totq03"
    0.2
    "totq totq02"
    0.2

    repeat

image totq_fuck:
    "bk3/guards/herma/2_ani_1.png"
    0.2
    "bk3/guards/herma/2_ani_2.png"
    0.2
    "bk3/guards/herma/2_ani_3.png"
    0.2
    "bk3/guards/herma/2_ani_4.png"
    0.2
    "bk3/guards/herma/2_ani_5.png"
    0.2
    "bk3/guards/herma/2_ani_4.png"
    0.2
    "bk3/guards/herma/2_ani_3.png"
    0.2
    "bk3/guards/herma/2_ani_2.png"
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
