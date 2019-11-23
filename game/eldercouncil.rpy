



image ec1 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_ec_sittingdown.jpg",
    (0, 0), "eldercouncil/ec_sitonground.png",
    (0, 0), "eldercouncil/ec_sitonground_fireshad_1.png",
    )

image ec2 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_ec_sittingdown.jpg",
    (0, 0), "eldercouncil/ec_sitonground.png",
    (0, 0), "eldercouncil/ec_sitonground_fireshad_2.png",
    )

image ec3 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_ec_sittingdown.jpg",
    (0, 0), "eldercouncil/ec_sitonground.png",
    (0, 0), "eldercouncil/ec_sitonground_fireshad_3.png",
    )


image ec:
    "ec1" with dissolve
    0.5
    "ec2" with dissolve
    0.5
    "ec3" with dissolve
    0.5
    "ec2" with dissolve
    0.5
    repeat






image ec4 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_ec_sittingdown.jpg",
    (0, 0), "eldercouncil/ec_sitonground_alone.png",
    (0, 0), "eldercouncil/ec1_sitonground_fireshad_1.png",
    )

image ec5 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_ec_sittingdown.jpg",
    (0, 0), "eldercouncil/ec_sitonground_alone.png",
    (0, 0), "eldercouncil/ec1_sitonground_fireshad_2.png",
    )

image ec6 = LiveComposite(
    (1000, 720),
    (0, 0), "backgrounds/bg_ec_sittingdown.jpg",
    (0, 0), "eldercouncil/ec_sitonground_alone.png",
    (0, 0), "eldercouncil/ec1_sitonground_fireshad_3.png",
    )

image eca:
    "ec4" with dissolve
    0.5
    "ec5" with dissolve
    0.5
    "ec6" with dissolve
    0.5
    "ec5" with dissolve
    0.5
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
