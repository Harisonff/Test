






image tonb tonb01 = LiveComposite(
    (1000, 720),
    (300, 0), "tonb_tail",
    (0, 0), "bk3/naga/bj/head_0.png",
    (0, 0), "tonb_gloweyes",
    )

image tonb tonb02 = LiveComposite(
    (1000, 720),
    (300, 0), "tonb_tail",
    (0, 0), "bk3/naga/bj/head_0.png",
    )

image tonb tonb03 = LiveComposite(
    (1000, 720),
    (300, 0), "tonb_tail",
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_1.png",
    (0, 0), "bk3/naga/bj/head_1.png",
    (0, 0), "tonb_gloweyes",
    )

image tonb tonb04 = LiveComposite(
    (1000, 720),
    (300, 0), "tonb_tail",
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_1.png",
    (0, 0), "bk3/naga/bj/head_1.png",
    )

image tonb tonb05 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_1.png",
    (0, 0), "bk3/naga/bj/head_2.png",
    )

image tonb tonb06 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_2.png",
    )
image tonb tonb07 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_3.png",    
    )

image tonb tonb07_1 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/bg_dream.jpg",
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_3.png",    
    )

image tonb tonb08 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/body_backlayer.png",
    (0, 0), "bk3/naga/bj/bod_4.png",
    )

image tonb tonb10 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/hair1.png",
    (0, 0), "bk3/naga/bj/bod_0.png",    
    )

image tonb tonb10_1 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/bg_dream.jpg",
    (0, 0), "bk3/naga/bj/hair1.png",
    (0, 0), "bk3/naga/bj/bod_0.png",    
    )

image tonb tonb11 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/hair2.png",
    (0, 0), "bk3/naga/bj/bod_0.png",    
    )

image tonb tonb11_1 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/naga/bj/bg_dream.jpg",
    (0, 0), "bk3/naga/bj/hair2.png",
    (0, 0), "bk3/naga/bj/bod_0.png",    
    )










image tonb_tail:
    "bk3/naga/bj/tail.png"
    2.3
    im.Flip("bk3/naga/bj/tail.png", horizontal = True)
    2.3
    repeat

image tonb tonb100:
    "tonb tonb05"
    0.4
    "tonb tonb06"
    0.4
    "tonb tonb07"
    0.4
    "tonb tonb08"
    0.4
    "tonb tonb07"
    0.4
    "tonb tonb06"
    0.4
    repeat



image tonb tonb101:
    "tonb tonb10"
    1.4
    "tonb tonb11"
    1.4
    "tonb tonb07"
    repeat

image tonb tonb101_1:
    "tonb tonb10_1"
    1.4
    "tonb tonb11_1"
    1.4
    "tonb tonb07_1"
    repeat

image tonb tonb102:
    "tonb tonb05"
    0.4
    "tonb tonb06"
    0.2
    "tonb tonb07"
    0.2
    "tonb tonb08"
    0.4
    "tonb tonb07"
    0.2
    "tonb tonb06"
    0.2
    repeat

image tonb_gloweyes:
    "bk3/naga/bj/gloweyes.png"
    alpha 1.0
    linear 1.0 alpha 0.4
    linear 1.0 alpha 1.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
