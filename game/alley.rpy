



image cat1 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_k_alleycats.jpg",
    (0, 0), "waternation_group/alley_cats_01.png",
    )

image cat2 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_k_alleycats.jpg",
    (0, 0), "waternation_group/alley_cats_02.png",
    )

image cat:
    "cat1" with Dissolve(.3)
    0.8
    "cat2" with Dissolve(.3)
    0.8
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
