







image toxb toxb01 = LiveComposite(
    (1000, 720), 
    (200, 0), "bk3/toph/melonlord/body_0.png",
    (200, 0), "bk3/toph/melonlord/arms_crossed.png",
    (200, 0), "bk3/toph/melonlord/face_grin.png",
    )

image toxb toxb02 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/toph/melonlord/body_0.png",
    (0, 0), "bk3/toph/melonlord/arms_up.png",
    (0, 0), "bk3/toph/melonlord/face_evilgrin.png",
    )

image toxb toxb03 = LiveComposite(
    (1000, 720), 
    (200, 0), "bk3/toph/melonlord/body_0.png",
    (200, 0), "bk3/toph/melonlord/arms_crossed.png",
    (200, 0), "bk3/toph/melonlord/face_unhappy.png",
    )

image toxb toxb04 = LiveComposite(
    (1000, 720), 
    (200, 0), "bk3/toph/melonlord/body_0.png",
    (200, 0), "bk3/toph/melonlord/arms_crossed.png",
    (200, 0), "bk3/toph/melonlord/face_angry.png",
    )

image toxb toxb05 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/toph/melonlord/n_body.png",
    (0, 0), "bk3/toph/melonlord/n_arms_up.png",
    (0, 4), "bk3/toph/melonlord/n_head.png",
    )

image toxb toxb06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/toph/melonlord/n_body.png",
    (0, 0), "bk3/toph/melonlord/n_arms_pinch1.png",
    (0, 0), "bk3/toph/melonlord/n_head.png",
    )

image toxb toxb07 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/toph/melonlord/n_body.png",
    (0, 0), "bk3/toph/melonlord/n_arms_pinch2.png",
    (0, 0), "bk3/toph/melonlord/n_head.png",
    )

image toxb toxb08 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/toph/melonlord/n_body.png",
    (0, 0), "bk3/toph/melonlord/n_arms_cup.png",
    (0, 0), "bk3/toph/melonlord/n_head.png",
    )


image toxb toxb100:
    "toxb toxb06"
    1.0
    "toxb toxb07"
    1.0
    repeat

image toxb_rockburn:
    "bk3/toph/melonlord/rock_burn1.png"
    0.2
    "bk3/toph/melonlord/rock_burn2.png"
    0.2
    repeat

image toxb_rockburn_1:
    "toxb_rockburn"
    xpos 0 ypos -200
    linear 4.0 ypos 1100
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
