









image b2az b2az01 = LiveComposite(
    (1000, 720),
    
    (0, 0), "bk2end/badend/az_idle_body.png",
    (0, 0), ConditionSwitch( 
        "azula_preg == False", "transparent.png",
        "azula_preg == True", "bk2end/badend/az_idle_body_preg.png"),
    (0, 0), "bk2end/badend/az_idle_arms_down.png",
    )

image b2az b2az02 = LiveComposite(
    (1000, 720),
    
    (0, 0), "bk2end/badend/az_idle_body.png",
    (0, 0), ConditionSwitch( 
        "azula_preg == False", "transparent.png",
        "azula_preg == True", "bk2end/badend/az_idle_body_preg.png"),
    (0, 0), "bk2end/badend/az_idle_arms_up.png",
    )

image b2az b2az03 = LiveComposite(
    (1000, 720),
    
    (0, 0), "bk2end/badend/az_down.png",
    (0, 0), ConditionSwitch( 
        "azula_preg == False", "transparent.png",
        "azula_preg == True", "bk2end/badend/az_down_preg.png"),    
    )

image b2az b2az04 = LiveComposite(
    (1000, 720),
    
    (0, 0), "bk2end/badend/az_knee_body.png",
    (0, 0), ConditionSwitch( 
        "azula_preg == False", "transparent.png",
        "azula_preg == True", "bk2end/badend/az_knee_body_preg.png"),    
    )




image b2az_solodick = "bk2end/badend/az_knee_d0.png"
image b2az_blink = "bk2end/badend/az_knee_blink.png"
image b2az_openmouth = "bk2end/badend/az_knee_openmouth.png"
image b2az_concern = "bk2end/badend/az_knee_concern.png"
image b2az_blush = "bk2end/badend/az_knee_blush.png"
image b2az_handson = "bk2end/badend/az_knee_hands.png"
image b2az_nagashadow = "bk2end/badend/az_down_shadownaga.png"

image b2az_idleanger = "bk2end/badend/az_idle_body_anger.png"
image b2az_idleblink = "bk2end/badend/az_idle_body_blink.png"
image b2az_treeline = "bk2end/badend/treeline.png"





image b2az_blink_ani:
    "b2az_blink"
    0.2
    "transparent.png"
    0.4
    "b2az_blink"
    0.2
    "transparent.png"
    4
    "b2az_blink"
    0.3
    "transparent.png"
    7
    "b2az_blink"
    0.3
    "transparent.png"
    2


    repeat



image b2az_bj_ani:
    "bk2end/badend/az_knee_d0.png"
    0.4
    "bk2end/badend/az_knee_d1.png"
    0.4
    "bk2end/badend/az_knee_d2.png"
    0.4
    "bk2end/badend/az_knee_d3.png"
    0.4
    "bk2end/badend/az_knee_d4.png"
    0.4
    "bk2end/badend/az_knee_d3.png"
    0.4
    "bk2end/badend/az_knee_d2.png"
    0.4
    "bk2end/badend/az_knee_d1.png"
    0.4

    repeat

image b2az_bj_ani2:
    "bk2end/badend/az_knee_d0.png"
    0.2
    "bk2end/badend/az_knee_d1.png"
    0.2
    "bk2end/badend/az_knee_d2.png"
    0.2
    "bk2end/badend/az_knee_d3.png"
    0.2
    "bk2end/badend/az_knee_d4.png"
    0.2
    "bk2end/badend/az_knee_d3.png"
    0.2
    "bk2end/badend/az_knee_d2.png"
    0.2
    "bk2end/badend/az_knee_d1.png"
    0.2

    repeat

image b2az_bj_ani3:
    "bk2end/badend/az_knee_d1.png"
    0.2
    "bk2end/badend/az_knee_d2.png"
    0.13
    "bk2end/badend/az_knee_d3.png"
    0.13
    "bk2end/badend/az_knee_d4.png"
    0.2
    "bk2end/badend/az_knee_d3.png"
    0.13
    "bk2end/badend/az_knee_d2.png"
    0.13

    repeat

image b2az_bj_ani4:
    "bk2end/badend/az_knee_d2.png"
    0.13
    "bk2end/badend/az_knee_d3.png"
    0.13
    "bk2end/badend/az_knee_d4.png"
    0.2
    "bk2end/badend/az_knee_d3.png"
    0.13

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
