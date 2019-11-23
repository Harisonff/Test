





image tocs_bg 0 = LiveComposite(
    (1250, 720),
    (0, 0), "bk3/toph/cave/bg_cave.jpg",   
    (0, 0), "tocs_rain",
    (250, 0), "tocs tocs01",
    )

image tocs_bg 1 = LiveComposite(
    (1000, 720),
    (-250, 0), "bk3/toph/cave/bg_cave.jpg",   
    (-250, 0), "tocs_rain",    
    )

image tocs_bg 2 = LiveComposite(
    (1000, 720),
    (-250, 0), "bk3/toph/cave/bg_cave.jpg", 
    )

image tocs tocs01 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/cave/body_1.png", 
    (0, 0), "bk3/toph/cave/leg_1.png",   
    (0, 0), "bk3/toph/cave/clothes_on.png",
    (746, 174), "tocs_blink",
    )

image tocs tocs02 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/cave/body_1.png", 
    (0, 0), "bk3/toph/cave/leg_1.png",
    (727, 260), "tocs_armrub",
    (746, 174), "tocs_blink",
    )

image tocs tocs03 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/cave/body_1.png",   
    (0, 0), "bk3/toph/cave/leg_1.png",
    (0, 0), "bk3/toph/cave/arms_reach.png", 
    (561, 156), "tocs_light",
    (746, 174), "tocs_blink",
    )
image tocs tocs04 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/cave/body_1.png",   
    (0, 0), "bk3/toph/cave/leg_2.png",
    (746, 174), "tocs_blink",
    )

image tocs tocs05 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/toph/cave/body_1.png", 
    (0, 0), "bk3/toph/cave/leg_1.png",
    (727, 260), "bk3/toph/cave/rub1.png",
    (746, 174), "tocs_blink",
    )




image tocs_rain:
    "bk3/toph/cave/rain1.png"
    0.3
    "bk3/toph/cave/rain2.png"
    0.3
    repeat

image tocs_smoke:
    "bk3/toph/cave/smoke.png"
    0.4
    im.Flip("bk3/toph/cave/smoke.png", horizontal = True)
    0.4
    repeat

image tocs_fire:
    alpha 0.7
    "bk3/toph/cave/fire1.png"
    0.4
    "bk3/toph/cave/fire2.png"
    0.4
    im.Flip("bk3/toph/cave/fire1.png", horizontal = True)
    0.4
    "bk3/toph/cave/fire2.png"
    0.4
    repeat

image tocs_fire2:
    alpha 0.7
    "bk3/toph/cave/fire3.png"
    0.4
    "bk3/toph/cave/fire4.png"
    0.4
    im.Flip("bk3/toph/cave/fire3.png", horizontal = True)
    0.4
    "bk3/toph/cave/fire4.png"
    0.4
    repeat

image tocs_light:
    "bk3/toph/cave/light1.png"
    0.4
    "bk3/toph/cave/light2.png"
    0.3
    "bk3/toph/cave/light3.png"
    0.4
    "bk3/toph/cave/light2.png"
    0.4
    repeat

image tocs_armrub:
    "bk3/toph/cave/rub1.png"
    0.3
    "bk3/toph/cave/rub2.png"
    0.3
    "bk3/toph/cave/rub3.png"
    0.3
    "bk3/toph/cave/rub2.png"
    0.3
    "bk3/toph/cave/rub1.png"
    0.3
    "bk3/toph/cave/rub2.png"
    0.3
    "bk3/toph/cave/rub3.png"
    0.3
    "bk3/toph/cave/rub2.png"
    0.3
    "bk3/toph/cave/rub1.png"
    5
    repeat

image tocs_blink:
    "bk3/toph/cave/minipixel.png"
    0.3
    "bk3/toph/cave/blink.png"
    0.3
    "bk3/toph/cave/minipixel.png"
    0.3
    "bk3/toph/cave/blink.png"
    0.3
    "bk3/toph/cave/minipixel.png"
    7.0
    repeat

image tocs_face angry = "bk3/toph/cave/angry.png"

image tocs_face ashamed = "bk3/toph/cave/ashamed.png"

image tocs_face realize = "bk3/toph/cave/realize.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
