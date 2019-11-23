



image bfac bfac01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/pema/idles/body_0.png")


image bfac bfac02 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/pema/idles/body_1.png",
    (0, 0), "bk4/pema/idles/arms_hang.png",
    (0, 0), "bk4/pema/idles/head_neutral.png",
    (700, 100), "bfac_blink_neutral")

image bfac bfac03 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/pema/idles/body_1.png",
    (0, 0), "bk4/pema/idles/arms_holdbelly.png",
    (0, 0), "bk4/pema/idles/head_angry.png")


image bfac bfac04 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/pema/idles/body_2.png", 
    (0, 0), "bk4/pema/idles/head_neutral.png",
    (700, 100), "bfac_blink_neutral"
    )

image bfac bfac05 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/pema/idles/body_2.png",   
    (0, 0), "bk4/pema/idles/head_angry.png",
    )

image bfac bfac06 = LiveComposite(
    (1000, 720), 
    (500, 0), "bk4/pema/idles/body_1.png",
    (0, 0), "bk4/pema/idles/arms_hang.png",
    (0, 0), "bk4/pema/idles/head_unsure.png",
   )

image bfac bfac07 = LiveComposite(
    (1000, 720), 
    (185, 0), "bk4/pema/idles/body_undress.png",    
    (0, 0), "bk4/pema/idles/head_neutral.png",
   )


image bfac_blink_neutral:
    "bk4/pema/idles/blink_neutral.png"
    0.2
    "bk4/misc/minipixel.png"
    0.2
    "bk4/pema/idles/blink_neutral.png"
    0.2
    "bk4/misc/minipixel.png"
    4.2
    "bk4/pema/idles/blink_neutral.png"
    0.2
    "bk4/misc/minipixel.png"
    8.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
