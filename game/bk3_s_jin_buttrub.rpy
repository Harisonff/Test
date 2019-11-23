






init:
    $ jin_buttrub_face = 'side'


image tojb tojb01 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/jin/buttrub/body_shadow.png",
    (0, 0), ConditionSwitch( 
        "jin_buttrub_face == 'side'", "bk3/jin/buttrub/head_side.png",
        "jin_buttrub_face == 'blink'", "bk3/jin/buttrub/head_blink.png",
        "jin_buttrub_face == 'back'", "bk3/jin/buttrub/head_back.png"), 
    (0, 0), "bk3/jin/buttrub/body_upper.png",
    (0, 0), "bk3/jin/buttrub/body_1.png",
    )


image tojb tojb11 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/jin/buttrub/body_shadow.png",
    (0, -4), ConditionSwitch( 
        "jin_buttrub_face == 'side'", "bk3/jin/buttrub/head_side.png",
        "jin_buttrub_face == 'blink'", "bk3/jin/buttrub/head_blink.png",
        "jin_buttrub_face == 'back'", "bk3/jin/buttrub/head_back.png"), 
    (0, 0), "bk3/jin/buttrub/body_upper.png",
    (0, 0), "bk3/jin/buttrub/body_1.png",
    (0, 0), "bk3/jin/buttrub/dick_1.png",
    )
image tojb tojb12 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/jin/buttrub/body_shadow.png",
    (0, -3), ConditionSwitch( 
        "jin_buttrub_face == 'side'", "bk3/jin/buttrub/head_side.png",
        "jin_buttrub_face == 'blink'", "bk3/jin/buttrub/head_blink.png",
        "jin_buttrub_face == 'back'", "bk3/jin/buttrub/head_back.png"), 
    (0, 0), "bk3/jin/buttrub/body_upper.png",
    (0, 0), "bk3/jin/buttrub/body_2.png",
    (0, 0), "bk3/jin/buttrub/dick_2.png",
    )
image tojb tojb13 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/jin/buttrub/body_shadow.png",
    (0, -2), ConditionSwitch( 
        "jin_buttrub_face == 'side'", "bk3/jin/buttrub/head_side.png",
        "jin_buttrub_face == 'blink'", "bk3/jin/buttrub/head_blink.png",
        "jin_buttrub_face == 'back'", "bk3/jin/buttrub/head_back.png"), 
    (0, 0), "bk3/jin/buttrub/body_upper.png",
    (0, 0), "bk3/jin/buttrub/body_3.png",
    (0, 0), "bk3/jin/buttrub/dick_3.png",
    )
image tojb tojb14 = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/jin/buttrub/body_shadow.png",
    (0, -1), ConditionSwitch( 
        "jin_buttrub_face == 'side'", "bk3/jin/buttrub/head_side.png",
        "jin_buttrub_face == 'blink'", "bk3/jin/buttrub/head_blink.png",
        "jin_buttrub_face == 'back'", "bk3/jin/buttrub/head_back.png"), 
    (0, 0), "bk3/jin/buttrub/body_upper.png",
    (0, 0), "bk3/jin/buttrub/body_4.png",
    (0, 0), "bk3/jin/buttrub/dick_4.png",
    )





image tojb_solodick = "bk3/jin/buttrub/solodick.png"

image tojb_sperm1 = "bk3/jin/buttrub/sperm1.png"
image tojb_sperm2 = "bk3/jin/buttrub/sperm2.png"
image tojb_sperm3 = "bk3/jin/buttrub/sperm3.png"

image tojb_spermshot = "bk3/jin/buttrub/spermshot.png"



image tojb tojb100:
    "tojb tojb11"
    0.3
    "tojb tojb12"
    0.3
    "tojb tojb13"
    0.3
    "tojb tojb14"
    0.3
    "tojb tojb13"
    0.3
    "tojb tojb12"
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
