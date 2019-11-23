


image kwave1 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_waving",
    (0, 0), "k_waving_01",
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_waving_tits_sm.png",
        "boobs == 'medium'", "katara/k_waving_tits_me.png",
        "boobs == 'big'", "katara/k_waving_tits_bi.png",)
    )

image kwave2 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_waving",
    (0, 0), "k_waving_02",
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_waving_tits_sm.png",
        "boobs == 'medium'", "katara/k_waving_tits_me.png",
        "boobs == 'big'", "katara/k_waving_tits_bi.png",)
    )

image kwave3 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_waving",
    (0, 0), "k_waving_03",
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_waving_tits_sm.png",
        "boobs == 'medium'", "katara/k_waving_tits_me.png",
        "boobs == 'big'", "katara/k_waving_tits_bi.png",)
    )

image kwave_an:
    "kwave1" with Dissolve(0.25)
    0.3
    "kwave2" with Dissolve(0.25)
    0.3
    "kwave3" with Dissolve(0.25)
    0.3
    "kwave2" with Dissolve(0.25)
    0.3
    repeat

image kwave11 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_waving",
    (0, 0), "k_waving_01",
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_waving_tits_sm.png",
        "boobs == 'medium'", "katara/k_waving_tits_me.png",
        "boobs == 'big'", "katara/k_waving_tits_bi.png",),
    (0, 0), "k_waving_sperm_xtra",
    )

image kwave12 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_waving",
    (0, 0), "k_waving_02",
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_waving_tits_sm.png",
        "boobs == 'medium'", "katara/k_waving_tits_me.png",
        "boobs == 'big'", "katara/k_waving_tits_bi.png",),
    (0, 0), "k_waving_sperm_xtra",
    )

image kwave13 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_waving",
    (0, 0), "k_waving_03",
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_waving_tits_sm.png",
        "boobs == 'medium'", "katara/k_waving_tits_me.png",
        "boobs == 'big'", "katara/k_waving_tits_bi.png",),
    (0, 0), "k_waving_sperm_xtra",
    )

image kwave_an1:
    "kwave11" with Dissolve(0.15)
    0.3
    "kwave12" with Dissolve(0.15)
    0.3
    "kwave13" with Dissolve(0.15)
    0.3
    "kwave12" with Dissolve(0.15)
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
