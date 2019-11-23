



image snm1 = LiveComposite(
    (374, 600),
    (0, 0), "nami/n_stance01_medium.png",
    (0, 0), "nami/n_stance01_medium_gloweye.png"
    )

image sum1 = LiveComposite(
    (374, 600),
    (0, 0), "una/u_stance01_medium.png",
    (0, 0), "una/u_stance01_medium_gloweye.png"
    )

image sk1 = LiveComposite(
    (374, 600),
    (0, 0), "katara/k_idle_fl_sgear.png",
    (0, 0), "katara/k_idle_fl_gloweye.png",
    )

image sk2 = LiveComposite(
    (374, 600),
    (0, 0), "katara/k_idle_ff_sgear.png",
    (0, 0), "katara/k_idle_ff_gloweye.png",
    )

image sk3 = LiveComposite(
    (374, 600),
    (0, 0), ConditionSwitch(
        "boobs == 'small'", "katara/k_idle_shwtit_sgear_tits_sm.png",
        "boobs == 'medium'", "katara/k_idle_shwtit_sgear_tits_me.png",
        "boobs == 'big'", "katara/k_idle_shwtit_sgear_tits_bi.png",
        ),
    (0, 0), "katara/k_idle_shwtit_sgear.png",
    (0, 0), "katara/k_idle_ff_gloweye.png",
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
