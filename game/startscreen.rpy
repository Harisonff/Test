



image start1 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_start.jpg",
    (0, 0), "p_console_hands_01.png",
    )

image start2 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_start.jpg",
    (0, 0), "p_console_hands_02.png",
    )

image start_an:
    "start1" with Dissolve(0.4)
    0.8
    "start2" with Dissolve(0.4)
    0.8
    repeat

image start_an1:
    "start1" with Dissolve(0.3)
    0.4
    "start2" with Dissolve(0.3)
    0.4
    repeat


image start_an2:
    "start2" with dissolve
    1.0
    "start1" with dissolve
    1.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
