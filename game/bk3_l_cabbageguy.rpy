







image toxa toxa01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/cabbages/cart.png",
    (420, 120), "bk3/cabbages/walk_1.png",
    )
image toxa toxa02 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/cabbages/cart.png",
    (420, 120), "bk3/cabbages/walk_2.png",
    )
image toxa toxa03 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/cabbages/cart.png",
    (420, 120), "bk3/cabbages/walk_3.png",
    )
image toxa toxa04 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/cabbages/cart.png",
    (420, 120), "bk3/cabbages/walk_4.png",
    )

image toxa toxa05 = LiveComposite(
    (1000, 720), 
    (0, 0), "toxa_cart_ani",
    (30, 360), "toxa_wheel_ani",
    )

image toxa toxa06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk3/cabbages/cart.png",
    (60, 400),"bk3/cabbages/wheel.png",  
    )

image toxa_wheel_ani:

    "bk3/cabbages/wheel.png"
    rotate 0
    linear 3.0 rotate -360
    repeat

image toxa_cart_ani:
    "toxa toxa01"
    0.3
    "toxa toxa02"
    0.3
    "toxa toxa03"
    0.3
    "toxa toxa04"
    0.3
    "toxa toxa03"
    0.3
    "toxa toxa02"
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
