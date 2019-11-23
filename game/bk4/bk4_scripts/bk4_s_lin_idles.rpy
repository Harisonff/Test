



init:
    $ bfaa_face = "neutral"

image bfaa bfaa00 = LiveComposite(  
    (1000, 720), 
    (0, 0), "bk4/lin/idles/body_0.png")


image bfaa bfaa01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/lin/idles/behind_desk.png")

image bfaa bfaa02 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",
    (0, 0), "bk4/lin/idles/arms_side.png",
    (0, 0), "bk4/lin/idles/head_neutral.png",
    (704, 100), "bk4/lin/idles/blink.png")

image bfaa bfaa03 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",
    (0, 0), "bk4/lin/idles/arms_side.png",
    (0, 0), "bk4/lin/idles/head_neutral.png",
    (704, 100), "bfaa_blink")

image bfaa bfaa04 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",
    (0, 0), "bk4/lin/idles/arms_crossed.png",
    (0, 0), "bk4/lin/idles/head_angry.png")

image bfaa bfaa05 = LiveComposite(   
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",    
    (0, 0), "bk4/lin/idles/head_angry.png",
    (0, 0), "bk4/lin/idles/arms_point.png")

image bfaa bfaa06 = LiveComposite(   
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",    
    (0, 0), "bk4/lin/idles/head_angry.png",
    (0, 0), "bk4/lin/idles/arms_facepalm.png")

image bfaa bfaa07 = LiveComposite(    
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",    
    (0, 0), "bk4/lin/idles/head_neutral.png",
    (0, 0), "bk4/lin/idles/arms_tithold.png",
    (704, 100), "bfaa_blink")

image bfaa bfaa08 = LiveComposite(    
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",    
    (0, 0), "bk4/lin/idles/head_shy.png",
    (0, 0), "bk4/lin/idles/arms_tithold.png")

image bfaa bfaa09 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_1.png",
    (0, 0), "bk4/lin/idles/arms_hang.png",
    (0, 0), "bk4/lin/idles/head_shy.png")

image bfaa bfaa10 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/lin/idles/body_shirt.png",
    (0, 0), "bk4/lin/idles/arms_side_nude.png",
    (0, 0), "bk4/lin/idles/head_neutral.png",
    )

image bfaa_blink:
    "bk4/lin/idles/blink.png"
    0.2
    "bk4/misc/minipixel.png"
    0.2
    "bk4/lin/idles/blink.png"
    0.2
    "bk4/misc/minipixel.png"
    4.2
    "bk4/lin/idles/blink.png"
    0.2
    "bk4/misc/minipixel.png"
    8.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
