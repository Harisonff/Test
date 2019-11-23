


init:
    $ totw_clothes_sitondick = True




image totw totw00 = LiveComposite(
    (1000, 720),    
    (680, 100), "bk3/toph/walk/idle_side.png",      
    )

image totw totw01 = LiveComposite(
    (1000, 720),    
    (680, 100), "bk3/toph/walk/idle.png",
    (680, 100), "bk3/toph/walk/arms_side.png",
    (680, 100), "bk3/toph/walk/nightshine_armsdown.png",   
    )

image totw totw02 = LiveComposite(
    (1000, 720),       
    (0, 0), "bk3/toph/walk/idle_halfdark.png", 
    (0, 0), "totw_blink", 
    )

image totw totw03 = LiveComposite(
    (1000, 720),    
    (680, 100), "bk3/toph/walk/idle.png",     
    (680, 100), "bk3/toph/walk/angry_point.png",
    (680, 100), "bk3/toph/walk/nightshine_point.png", 
    )
image totw totw04 = LiveComposite(
    (1000, 720),    
    (680, 100), "bk3/toph/walk/idle.png",
    (680, 100), "bk3/toph/walk/arms_side.png",   
    (680, 100), "bk3/toph/walk/face_smile.png",
    (680, 100), "bk3/toph/walk/nightshine_armsdown.png",
    )

image totw totw05 = LiveComposite(
    (1000, 720),       
    (0, 0), "bk3/toph/walk/idle_halfdark.png", 
    (0, 0), "bk3/toph/walk/blink_halfdark.png", 
    )

image totw totw06 = LiveComposite(
    (1000, 720),       
    (0, 0), "bk3/toph/walk/body_nude.png",
    )


image totw totw09 = LiveComposite(
    (1000, 720),       
    (0, 0), "bk3/toph/walk/idle_halfdark.png", 
    (0, 0), "bk3/toph/walk/face_blush.png", 
    )
image totw totw10 = LiveComposite(
    (1000, 720),       
    (0, 0), "bk3/toph/walk/armpit_up.png", 
    (0, 0), "bk3/toph/walk/armpit_cover.png", 
    )
image totw totw11 = LiveComposite(
    (1000, 720),       
    (0, 0), "bk3/toph/walk/armpit_up.png", 
    )

image totw totw12 = LiveComposite(
    (1000, 720),       
    (100, 0), "bk3/toph/walk/rockdick_big.png",
    (0, 0), "bk3/toph/walk/toph_sitondick.png",    
    (0, 0), ConditionSwitch(        
        "totw_clothes_sitondick == True", "bk3/toph/walk/toph_sitondick_clothes.png",        
        "totw_clothes_sitondick == False", "bk3/june/tug/minipixel.png"),
    )
image totw totw13 = LiveComposite(
    (1000, 720),       
    (-200, 0), "bk3/toph/walk/rockdick_big.png",    
    )
image totw totw14 = LiveComposite(
    (1000, 720),       
    (100, 0), "bk3/toph/walk/rockdick_big.png",    
    )





image totw totw100:
    "bk3/toph/walk/run1.png",
    0.2
    "bk3/toph/walk/run2.png",
    0.2
    "bk3/toph/walk/run3.png",
    0.2
    "bk3/toph/walk/run4.png",
    0.2
    repeat

image totw_blink:
    "bk3/toph/walk/blink_halfdark.png",
    0.3
    "bk3/toph/walk/minipixel.png",
    0.3
    "bk3/toph/walk/blink_halfdark.png",
    0.3
    "bk3/toph/walk/minipixel.png",
    9.3
    repeat

image totw_lick:
    "bk3/toph/walk/armpit_lickstart.png",
    0.5
    "bk3/toph/walk/armpit_lickmiddle.png",
    0.3
    "bk3/toph/walk/armpit_lickend.png",
    0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
