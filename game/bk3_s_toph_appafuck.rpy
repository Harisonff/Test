







init:
    $ appafuck_cum = 'outside'


image toaf toaf10 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legup1.png",
    (439, 145), "toaf_blink",
    )
image toaf toaf11 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legup2.png",
    (439, 145), "toaf_blink",
    )
image toaf toaf12 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legshock1.png",
    (439, 145), "toaf_blink",
    )
image toaf toaf13 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (439, 145), "toaf_blink",
    )


image toaf toaf15 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (439, 145), "toaf_blink",
    )

image toaf toaf16 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (0, 0), "bk3/toph/appafuck/openpussy.png",
    (439, 145), "toaf_blink",
    )

image toaf toaf17 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head1.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (0, 0), "bk3/toph/appafuck/openpussy_dry.png",
    (439, 145), "toaf_blink",
    )


image toaf toaf21 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/face_lewd.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (0, 0), "bk3/toph/appafuck/dickin1.png",
    )
image toaf toaf22 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/face_lewd.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (0, 0), "bk3/toph/appafuck/dickin2.png",
    )
image toaf toaf23 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/face_lewd.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (0, 0), "bk3/toph/appafuck/dickin3.png",
    )
image toaf toaf24 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/face_lewd.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",
    (0, 0), "bk3/toph/appafuck/dickin4.png",
    )
image toaf toaf25 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",
    (0, 0), "bk3/toph/appafuck/head_back.png",
    (0, 0), "bk3/toph/appafuck/legshock1.png",
    (0, 0), "bk3/toph/appafuck/dickin5.png",    
    )


image toaf toaf26 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",    
    (0, -43), "bk3/toph/appafuck/face_shock.png",
    (0, 0), "bk3/toph/appafuck/legshock2.png",  
    (0, 0), "bk3/toph/appafuck/openpussy_dry.png",    
    (0, 0), ConditionSwitch( 
        "appafuck_cum == 'inside'", "bk3/toph/appafuck/openpussy.png", 
        "appafuck_cum == 'outside'",   "bk3/toph/appafuck/sperm3.png"),
    (439, 145), "toaf_blink",   
    )
image toaf toaf27 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/body.png",    
    (0, 0), "bk3/toph/appafuck/legshock2.png",  
    (0, 0), "bk3/toph/appafuck/openpussy_dry.png",    
    (0, 0), ConditionSwitch( 
        "appafuck_cum == 'inside'", "bk3/toph/appafuck/openpussy.png", 
        "appafuck_cum == 'outside'",   "bk3/toph/appafuck/sperm3.png"),
    (439, 145), "toaf_blink",   
    )




image toaf_flying = "bk3/toph/appafuck/flying.png"



image toaf_shockface = LiveComposite(
    (1000, 720),
    (0, -43), "bk3/toph/appafuck/face_shock.png",
    (439, 145), "toaf_blink",    
    )

image toaf_lewdface = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/appafuck/face_lewd.png",
    (439, 145), "toaf_blink",    
    )

image toaf_nod:
    "bk3/toph/appafuck/head_back.png"
    0.3
    "bk3/toph/appafuck/head1.png"
    0.3
    "bk3/toph/appafuck/head_back.png"
    0.3
    "bk3/toph/appafuck/head1.png"
    2.3
    repeat

image toaf_appahead = "bk3/toph/appafuck/appahead.png"
image toaf_holdrope = "bk3/toph/appafuck/holdrope.png"

image toaf_blink:

    "bk3/toph/appafuck/blink.png"
    0.3
    "transparent.png"
    8.0
    "bk3/toph/appafuck/blink.png"
    0.3
    "transparent.png"
    7.0
    repeat





image toaf toaf100:

    "toaf toaf10"
    0.4
    "toaf toaf11"
    0.4
    "toaf toaf10"
    3.0
    "toaf toaf11"
    4.0
    repeat

image toaf toaf101:

    "toaf toaf12"
    0.4
    "toaf toaf13"
    0.4
    "toaf toaf12"
    3.0
    "toaf toaf13"
    4.0
    repeat

image toaf toaf102:

    "toaf toaf25" with vpunch
    1.2
    "toaf toaf24" with Dissolve(0.1)
    0.3
    "toaf toaf23"
    0.3
    "toaf toaf21"
    0.6


    repeat

image toaf toaf103:
    "toaf toaf10"
    0.4
    "toaf toaf11"
    0.4
    "toaf toaf10"
    1.2
    "toaf toaf11"
    4.0
    repeat


image toaf_pussfuck:

    "bk3/toph/appafuck/dickin1.png"
    0.4
    "bk3/toph/appafuck/dickin2.png"
    0.4
    "bk3/toph/appafuck/dickin3.png"
    0.4
    "bk3/toph/appafuck/dickin4.png"
    0.4
    "bk3/toph/appafuck/dickin5.png"
    0.4
    "bk3/toph/appafuck/dickin4.png"
    0.4
    "bk3/toph/appafuck/dickin3.png"
    0.4
    "bk3/toph/appafuck/dickin2.png"
    0.4
    repeat


    repeat

image toaf_dickrub:
    "bk3/toph/appafuck/solodick.png"
    ypos 700 xpos 500
    linear 1 ypos 600
    linear 1 ypos 700

    repeat

image toaf_appafly:
    "bk3/toph/appafuck/appa_fly1.png"
    1.5
    "bk3/toph/appafuck/appa_fly2.png"
    1.5
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
