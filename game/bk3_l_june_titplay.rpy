



init:
    $ totz_emote = 'neutral'


    define bk3_fg1 = Character("Guard 1", color="#000000",show_side_image = Image("bk3/june/titplay/guard1.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)
    define bk3_fg2 = Character("Guard 2", color="#000000",show_side_image = Image("bk3/june/titplay/guard2.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)





image totz totz00 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_down_1.png",     
    )

image totz totz01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_down_1.png", 
    (0, 0), "bk3/june/titplay/tits_solo.png", 
    )

image totz totz02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_down_1.png", 
    (0, 0), "totz_knead", 
    )

image totz totz03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_down_1.png", 
    (0, 0), "bk3/june/titplay/nipopen_1.png", 
    )

image totz totz04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_down_1.png", 
    (0, 0), "totz_nipopen", 
    )

image totz totz05 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_down_0.png",    
    )





image totz totz40 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_up_0.png",    
    )

image totz totz41 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_up_1.png",
    (0, 0), "bk3/june/titplay/tits_solo.png",
    (506, 112), "totz_face",
    (506, 112), "totz_blink",
    )

image totz totz42 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_up_1.png", 
    (506, 112), "totz_face",
    (506, 112), "totz_blink",
    )



image totz totz43 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_up_1.png",
    (0, 0), "totz_knead",
    (506, 112), "totz_face",
    (506, 112), "totz_blink",    
    )

image totz totz44 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/june/titplay/body_up_1.png", 
    (0, 0), "totz_nipopen",
    (506, 112), "totz_face",
    (506, 112), "totz_blink",   
    )





image totz_face = LiveComposite(
    (200, 209), 
    (0, 0), ConditionSwitch(        
        "totz_emote == 'shock'", "bk3/june/titplay/face_shock.png",       
        "totz_emote == 'neutral'", "bk3/june/titplay/minipixel.png"),  
    )


image totz_knead:


    "bk3/june/titplay/knead_2.png"
    0.3
    "bk3/june/titplay/knead_3.png"
    0.3
    "bk3/june/titplay/knead_4.png"
    0.3
    "bk3/june/titplay/knead_5.png"
    0.3
    "bk3/june/titplay/knead_4.png"
    0.3
    "bk3/june/titplay/knead_3.png"
    0.3

    repeat

image totz_hit:
    "bk3/june/titplay/tithit_1.png"
    0.2
    "bk3/june/titplay/tithit_2.png"
    0.1
    "bk3/june/titplay/tithit_3.png"
    0.3
    "bk3/june/titplay/tithit_4.png"
    0.3
    "bk3/june/titplay/tits_solo.png"
    0.3
    repeat

image totz_nipopen:
    "bk3/june/titplay/nipopen_1.png"
    0.4
    "bk3/june/titplay/nipopen_2.png"
    0.4
    "bk3/june/titplay/nipopen_3.png"
    0.4
    "bk3/june/titplay/nipopen_2.png"
    0.4
    "bk3/june/titplay/nipopen_1.png"
    0.4
    "bk3/june/titplay/nipopen_2.png"
    0.4
    "bk3/june/titplay/nipopen_3.png"
    3.0
    "bk3/june/titplay/nipopen_2.png"
    0.2
    repeat

image totz_blink:
    "bk3/june/titplay/face_blink.png"
    0.3
    "bk3/june/titplay/minipixel.png"
    2.0
    "bk3/june/titplay/face_blink.png"
    0.3
    "bk3/june/titplay/minipixel.png"
    0.3
    "bk3/june/titplay/face_blink.png"
    0.3
    "bk3/june/titplay/minipixel.png"
    6.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
