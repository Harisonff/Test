






init:
    $ jin_suck_eyesleft = False

image tojs tojs01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/jin/sucks/body_0.png",
    (0, 0), ConditionSwitch(        
        "jin_suck_eyesleft == True", "bk3/jin/sucks/eyes_left.png",
        "jin_suck_eyesleft == False", "transparent.png"), 
    (0, 0), "tojs_blink",    
    )

image tojs tojs02 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/jin/sucks/body_0.png",
    (0, 0), "bk3/jin/sucks/face_surprise.png",
    (0, 0), ConditionSwitch(        
        "jin_suck_eyesleft == True", "bk3/jin/sucks/eyes_left.png",
        "jin_suck_eyesleft == False", "transparent.png"), 
    (0, 0), "tojs_blink",    
    )

image tojs tojs03 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/jin/sucks/body_0.png",
    (0, 0), "bk3/jin/sucks/face_angry.png",
    (0, 0), ConditionSwitch(        
        "jin_suck_eyesleft == True", "bk3/jin/sucks/eyes_left.png",
        "jin_suck_eyesleft == False", "transparent.png"), 
    (0, 0), "tojs_blink",    
    )
image tojs tojs04 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/jin/sucks/body_1.png",
    )
image tojs tojs05 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/jin/sucks/body_2.png",
    )
image tojs tojs06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/jin/sucks/body_3.png",
    )






image tojs_smallhole = "bk3/jin/sucks/smallhole.png"
image tojs_wallhole = "bk3/jin/sucks/hole.png"
image tojs_mouth = "bk3/jin/sucks/bigmouth.png"
image tojs_eyesleft = "bk3/jin/sucks/eyes_left.png"







image tojs tojs100:
    "bk3/jin/sucks/body_1.png"
    0.3
    "bk3/jin/sucks/body_2.png"
    0.3
    "bk3/jin/sucks/body_3.png"
    0.3
    "bk3/jin/sucks/body_2.png"
    0.3
    repeat

image tojs tojs101:
    xzoom -1 xpos 1035
    "bk3/jin/sucks/body_1.png"
    0.3
    "bk3/jin/sucks/body_2.png"
    0.3
    "bk3/jin/sucks/body_3.png"
    0.3
    "bk3/jin/sucks/body_2.png"
    0.3
    repeat
image tojs tojs102:
    xzoom -1 xpos 1035
    "bk3/jin/sucks/body_1.png"
    0.3
    "bk3/jin/sucks/body_3.png"
    1.3
    "bk3/jin/sucks/body_2.png"
    0.3
    repeat

image tojs tojs103:
    xzoom -1 xpos 1035
    "tojs tojs04"
    0.25
    "tojs tojs05"
    0.05
    "tojs tojs06"
    0.8
    "tojs tojs05"
    0.1
    repeat

image tojs tojs104:
    xzoom -1 xpos 1035
    "tojs tojs05"
    0.3
    "tojs tojs06"
    0.3
    repeat

image tojs_blink:
    "bk3/jin/sucks/blink.png"
    0.3
    "transparent.png"
    3.0
    "bk3/jin/sucks/blink.png"
    0.3
    "transparent.png"
    8.0
    "bk3/jin/sucks/blink.png"
    0.3
    "transparent.png"
    0.3
    "bk3/jin/sucks/blink.png"
    0.3
    "transparent.png"
    5.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
