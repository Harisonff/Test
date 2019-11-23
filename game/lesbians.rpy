



image les0 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_k_school_night.jpg",
    (0, 0), "lesbians/schoolnight_lesbos.png",
    )

image les1 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_k_school_night.jpg",
    (0, 0), "lesbians/schoolnight_lesbos.png",
    (0, 0), "lesbians/schoolnight_bluelight.png",
    )

image les2 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_k_school_night.jpg",
    (0, 0), "lesbians/schoolnight_lesbos.png",
    (0, 0), "lesbians/schoolnight_greenlight.png",
    )

image les3 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_k_school_night.jpg",
    (0, 0), "lesbians/schoolnight_lesbos.png",
    (0, 0), "lesbians/schoolnight_redlight.png",
    )

image les:
    "les1" with Dissolve(0.8)
    1.3
    "les2" with Dissolve(0.8)
    1.3
    "les3" with Dissolve(0.8)
    1.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
