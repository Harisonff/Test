



image coversbj1 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_insidetent_02",
    (0, 0), "insidetent_silhouette_2",
    )

image coversbj2 = LiveComposite(
    (1000, 720),
    (0, 0), "bg_k_insidetent_02",
    (0, 0), "insidetent_silhouette_1",
    )

image coversbj:
    "coversbj2" with Dissolve(0.4)
    0.8
    "coversbj1" with Dissolve(0.4)
    0.8
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
