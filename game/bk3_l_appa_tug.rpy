








image toxi toxi01 = LiveComposite(
    (1000, 720),    
    (500, 0), "bk3/appa/tug/idle.png",
    (500, 0), "bk3/appa/tug/idle_armsdown.png", 
    (500, 0), "bk3/appa/tug/idle_head.png", 
    )

image toxi toxi01a = LiveComposite(
    (1000, 720),    
    (500, 0), im.Flip("bk3/appa/tug/idle.png", horizontal=True),
    (500, 0), im.Flip("bk3/appa/tug/idle_armsdown.png", horizontal=True),  
    (500, 0), "bk3/appa/tug/idle_head.png", 
    )

image toxi toxi02 = LiveComposite(
    (1000, 720),    
    (500, 0), "bk3/appa/tug/idle.png",
    (500, 0), "bk3/appa/tug/idle_head.png", 
    (500, 0), "bk3/appa/tug/idle_armsup.png", 
    )

image toxi toxi03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/appa/tug/body_sit.png",    
    (0, 0), "bk3/appa/tug/bodysit_armopen.png", 
    (0, 0), "bk3/appa/tug/legdick2.png",
    )

image toxi toxi04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/appa/tug/body_sit.png",
    (0, 0), "bk3/appa/tug/legdick1.png",
    (590, 0), "bk3/appa/tug/tug4.png", 
    )

image toxi toxi05 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/appa/tug/body_sit.png",
    (0, 0), "bk3/appa/tug/legdick1.png",
    (590, 0), "toxi_tug_slow", 
    )
image toxi toxi06 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/appa/tug/body_sit.png",
    (0, 0), "bk3/appa/tug/legdick1.png",
    (590, 0), "toxi_tug_fast", 
    )

image toxi toxi07 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/appa/tug/flystart.png",     
    )

image toxi toxi08 = LiveComposite(
    (1000, 720),    
    (0, 0), "maze/appa_bg_hatch.jpg",     
    (0, 0), "maze/appa_bg_air.png",     
    )

image toxi toxi09a = LiveComposite(
    (1000, 720),    
    (500, 0), im.Flip("bk3/appa/tug/idleback.png", horizontal=True),    
    )

image toxi toxi09b = LiveComposite(
    (1000, 720),    
    (500, 0), "bk3/appa/tug/idleback.png",    
    )

image toxi toxi10 = LiveComposite(
    (1000, 720),    
    (500, 0), "bk3/appa/tug/idle.png",
    (500, 0), "bk3/appa/tug/idle_armsdown.png", 
    (500, 0), "bk3/appa/tug/idle_hatlesshead.png", 
    )


image toxi_appahat = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/appa/tug/appa_tughead.png",
    (0, 0), "bk3/appa/tug/appa_hat.png", 
    
    )

image toxi_appafly:
    "bk3/appa/tug/appa_fly1.png"
    1.2
    "bk3/appa/tug/appa_fly2.png"
    1.2
    repeat


image toxi toxi100:
    "toxi toxi03"
    0.7
    "toxi toxi04"
    0.7
    repeat

image toxi toxi101:
    "toxi toxi01a"
    0.4
    "toxi toxi01"
    0.4
    repeat

image toxi toxi102:
    "toxi toxi09a"
    0.4
    "toxi toxi09b"
    0.4
    repeat

image toxi_tug_slow:
    "bk3/appa/tug/tug1.png"
    0.3
    "bk3/appa/tug/tug2.png"
    0.3
    "bk3/appa/tug/tug3.png"
    0.3
    "bk3/appa/tug/tug4.png"
    0.3
    "bk3/appa/tug/tug3.png"
    0.3
    "bk3/appa/tug/tug2.png"
    0.3
    repeat

image toxi_tug_fast:
    "bk3/appa/tug/tug2.png"
    0.1
    "bk3/appa/tug/tug4.png"
    0.1
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
