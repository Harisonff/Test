
image enemy_crab_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "enemy_crab_type == '1'", "emberisland/crab_1.png",
        "enemy_crab_type == '2'", "emberisland/strongcrab_1.png",
        "enemy_crab_type == '3'", "emberisland/legendcrab_1.png",
        "enemy_crab_type == '4'", "emberisland/bessiecrab_1.png",
        "enemy_crab_type == '5'", "emberisland/muskycrab_1.png",
        "enemy_crab_type == '6'", "emberisland/stankcrab_1.png",
        "enemy_crab_type == '7'", "emberisland/aqua1.png",
        "enemy_crab_type == '8'", "emberisland/gray1.png",
        "enemy_crab_type == '9'", "emberisland/green1.png",
        "enemy_crab_type == '10'", "emberisland/orange1.png",
        "enemy_crab_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "enemy_crab_rarity == 'n'", "transparent.png",
        "enemy_crab_rarity == 'r'", "misc/rare_star.png",
        "enemy_crab_rarity == 'e'", "misc/epic_star.png",
        "enemy_crab_rarity == 'l'", "misc/legend_star.png",
        ),
    )


image enemy_crab_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "enemy_crab_type == '1'", "emberisland/crab_2.png",
        "enemy_crab_type == '2'", "emberisland/strongcrab_2.png",
        "enemy_crab_type == '3'", "emberisland/legendcrab_2.png",
        "enemy_crab_type == '4'", "emberisland/bessiecrab_2.png",
        "enemy_crab_type == '5'", "emberisland/muskycrab_2.png",
        "enemy_crab_type == '6'", "emberisland/stankcrab_2.png",
        "enemy_crab_type == '7'", "emberisland/aqua2.png",
        "enemy_crab_type == '8'", "emberisland/gray2.png",
        "enemy_crab_type == '9'", "emberisland/green2.png",
        "enemy_crab_type == '10'", "emberisland/orange2.png",
        "enemy_crab_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "enemy_crab_rarity == 'n'", "transparent.png",
        "enemy_crab_rarity == 'r'", "misc/rare_star.png",
        "enemy_crab_rarity == 'e'", "misc/epic_star.png",
        "enemy_crab_rarity == 'l'", "misc/legend_star.png",
        ),
    )

image enemy_crab_shuffle:
    "enemy_crab_crab1"
    0.4
    "enemy_crab_crab2"
    0.4
    repeat


image crab1_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab1_type == '1'", "emberisland/crab_1.png",
        "crab1_type == '2'", "emberisland/strongcrab_1.png",
        "crab1_type == '3'", "emberisland/legendcrab_1.png",
        "crab1_type == '4'", "emberisland/bessiecrab_1.png",
        "crab1_type == '5'", "emberisland/muskycrab_1.png",
        "crab1_type == '6'", "emberisland/stankcrab_1.png",
        "crab1_type == '7'", "emberisland/aqua1.png",
        "crab1_type == '8'", "emberisland/gray1.png",
        "crab1_type == '9'", "emberisland/green1.png",
        "crab1_type == '10'", "emberisland/orange1.png",
        "crab1_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab1_rarity == 'n'", "transparent.png",
        "crab1_rarity == 'r'", "misc/rare_star.png",
        "crab1_rarity == 'e'", "misc/epic_star.png",
        "crab1_rarity == 'l'", "misc/legend_star.png",)
    )


image crab1_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab1_type == '1'", "emberisland/crab_2.png",
        "crab1_type == '2'", "emberisland/strongcrab_2.png",
        "crab1_type == '3'", "emberisland/legendcrab_2.png",
        "crab1_type == '4'", "emberisland/bessiecrab_2.png",
        "crab1_type == '5'", "emberisland/muskycrab_2.png",
        "crab1_type == '6'", "emberisland/stankcrab_2.png",
        "crab1_type == '7'", "emberisland/aqua2.png",
        "crab1_type == '8'", "emberisland/gray2.png",
        "crab1_type == '9'", "emberisland/green2.png",
        "crab1_type == '10'", "emberisland/orange2.png",
        "crab1_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab1_rarity == 'n'", "transparent.png",
        "crab1_rarity == 'r'", "misc/rare_star.png",
        "crab1_rarity == 'e'", "misc/epic_star.png",
        "crab1_rarity == 'l'", "misc/legend_star.png",)
    )

image crab1_shuffle:
    "crab1_crab1"
    0.4
    "crab1_crab2"
    0.4
    repeat

image crab2_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab2_type == '1'", "emberisland/crab_1.png",
        "crab2_type == '2'", "emberisland/strongcrab_1.png",
        "crab2_type == '3'", "emberisland/legendcrab_1.png",
        "crab2_type == '4'", "emberisland/bessiecrab_1.png",
        "crab2_type == '5'", "emberisland/muskycrab_1.png",
        "crab2_type == '6'", "emberisland/stankcrab_1.png",
        "crab2_type == '7'", "emberisland/aqua1.png",
        "crab2_type == '8'", "emberisland/gray1.png",
        "crab2_type == '9'", "emberisland/green1.png",
        "crab2_type == '10'", "emberisland/orange1.png",
        "crab2_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab2_rarity == 'n'", "transparent.png",
        "crab2_rarity == 'r'", "misc/rare_star.png",
        "crab2_rarity == 'e'", "misc/epic_star.png",
        "crab2_rarity == 'l'", "misc/legend_star.png",)    
    )


image crab2_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab2_type == '1'", "emberisland/crab_2.png",
        "crab2_type == '2'", "emberisland/strongcrab_2.png",
        "crab2_type == '3'", "emberisland/legendcrab_2.png",
        "crab2_type == '4'", "emberisland/bessiecrab_2.png",
        "crab2_type == '5'", "emberisland/muskycrab_2.png",
        "crab2_type == '6'", "emberisland/stankcrab_2.png",
        "crab2_type == '7'", "emberisland/aqua2.png",
        "crab2_type == '8'", "emberisland/gray2.png",
        "crab2_type == '9'", "emberisland/green2.png",
        "crab2_type == '10'", "emberisland/orange2.png",
        "crab2_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab2_rarity == 'n'", "transparent.png",
        "crab2_rarity == 'r'", "misc/rare_star.png",
        "crab2_rarity == 'e'", "misc/epic_star.png",
        "crab2_rarity == 'l'", "misc/legend_star.png",)  
    )

image crab2_shuffle:
    "crab2_crab1"
    0.4
    "crab2_crab2"
    0.4
    repeat

image crab3_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab3_type == '1'", "emberisland/crab_1.png",
        "crab3_type == '2'", "emberisland/strongcrab_1.png",
        "crab3_type == '3'", "emberisland/legendcrab_1.png",
        "crab3_type == '4'", "emberisland/bessiecrab_1.png",
        "crab3_type == '5'", "emberisland/muskycrab_1.png",
        "crab3_type == '6'", "emberisland/stankcrab_1.png",
        "crab3_type == '7'", "emberisland/aqua1.png",
        "crab3_type == '8'", "emberisland/gray1.png",
        "crab3_type == '9'", "emberisland/green1.png",
        "crab3_type == '10'", "emberisland/orange1.png",
        "crab3_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab3_rarity == 'n'", "transparent.png",
        "crab3_rarity == 'r'", "misc/rare_star.png",
        "crab3_rarity == 'e'", "misc/epic_star.png",
        "crab3_rarity == 'l'", "misc/legend_star.png",)  
    )


image crab3_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab3_type == '1'", "emberisland/crab_2.png",
        "crab3_type == '2'", "emberisland/strongcrab_2.png",
        "crab3_type == '3'", "emberisland/legendcrab_2.png",
        "crab3_type == '4'", "emberisland/bessiecrab_2.png",
        "crab3_type == '5'", "emberisland/muskycrab_2.png",
        "crab3_type == '6'", "emberisland/stankcrab_2.png",
        "crab3_type == '7'", "emberisland/aqua2.png",
        "crab3_type == '8'", "emberisland/gray2.png",
        "crab3_type == '9'", "emberisland/green2.png",
        "crab3_type == '10'", "emberisland/orange2.png",
        "crab3_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab3_rarity == 'n'", "transparent.png",
        "crab3_rarity == 'r'", "misc/rare_star.png",
        "crab3_rarity == 'e'", "misc/epic_star.png",
        "crab3_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab3_shuffle:
    "crab3_crab1"
    0.4
    "crab3_crab2"
    0.4
    repeat

image crab4_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab4_type == '1'", "emberisland/crab_1.png",
        "crab4_type == '2'", "emberisland/strongcrab_1.png",
        "crab4_type == '3'", "emberisland/legendcrab_1.png",
        "crab4_type == '4'", "emberisland/bessiecrab_1.png",
        "crab4_type == '5'", "emberisland/muskycrab_1.png",
        "crab4_type == '6'", "emberisland/stankcrab_1.png",
        "crab4_type == '7'", "emberisland/aqua1.png",
        "crab4_type == '8'", "emberisland/gray1.png",
        "crab4_type == '9'", "emberisland/green1.png",
        "crab4_type == '10'", "emberisland/orange1.png",
        "crab4_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab4_rarity == 'n'", "transparent.png",
        "crab4_rarity == 'r'", "misc/rare_star.png",
        "crab4_rarity == 'e'", "misc/epic_star.png",
        "crab4_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab4_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab4_type == '1'", "emberisland/crab_2.png",
        "crab4_type == '2'", "emberisland/strongcrab_2.png",
        "crab4_type == '3'", "emberisland/legendcrab_2.png",
        "crab4_type == '4'", "emberisland/bessiecrab_2.png",
        "crab4_type == '5'", "emberisland/muskycrab_2.png",
        "crab4_type == '6'", "emberisland/stankcrab_2.png",
        "crab4_type == '7'", "emberisland/aqua2.png",
        "crab4_type == '8'", "emberisland/gray2.png",
        "crab4_type == '9'", "emberisland/green2.png",
        "crab4_type == '10'", "emberisland/orange2.png",
        "crab4_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab4_rarity == 'n'", "transparent.png",
        "crab4_rarity == 'r'", "misc/rare_star.png",
        "crab4_rarity == 'e'", "misc/epic_star.png",
        "crab4_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab4_shuffle:
    "crab4_crab1"
    0.4
    "crab4_crab2"
    0.4
    repeat

image crab5_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab5_type == '1'", "emberisland/crab_1.png",
        "crab5_type == '2'", "emberisland/strongcrab_1.png",
        "crab5_type == '3'", "emberisland/legendcrab_1.png",
        "crab5_type == '4'", "emberisland/bessiecrab_1.png",
        "crab5_type == '5'", "emberisland/muskycrab_1.png",
        "crab5_type == '6'", "emberisland/stankcrab_1.png",
        "crab5_type == '7'", "emberisland/aqua1.png",
        "crab5_type == '8'", "emberisland/gray1.png",
        "crab5_type == '9'", "emberisland/green1.png",
        "crab5_type == '10'", "emberisland/orange1.png",
        "crab5_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab5_rarity == 'n'", "transparent.png",
        "crab5_rarity == 'r'", "misc/rare_star.png",
        "crab5_rarity == 'e'", "misc/epic_star.png",
        "crab5_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab5_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab5_type == '1'", "emberisland/crab_2.png",
        "crab5_type == '2'", "emberisland/strongcrab_2.png",
        "crab5_type == '3'", "emberisland/legendcrab_2.png",
        "crab5_type == '4'", "emberisland/bessiecrab_2.png",
        "crab5_type == '5'", "emberisland/muskycrab_2.png",
        "crab5_type == '6'", "emberisland/stankcrab_2.png",
        "crab5_type == '7'", "emberisland/aqua2.png",
        "crab5_type == '8'", "emberisland/gray2.png",
        "crab5_type == '9'", "emberisland/green2.png",
        "crab5_type == '10'", "emberisland/orange2.png",
        "crab5_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab5_rarity == 'n'", "transparent.png",
        "crab5_rarity == 'r'", "misc/rare_star.png",
        "crab5_rarity == 'e'", "misc/epic_star.png",
        "crab5_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab5_shuffle:
    "crab5_crab1"
    0.4
    "crab5_crab2"
    0.4
    repeat

image crab6_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab6_type == '1'", "emberisland/crab_1.png",
        "crab6_type == '2'", "emberisland/strongcrab_1.png",
        "crab6_type == '3'", "emberisland/legendcrab_1.png",
        "crab6_type == '4'", "emberisland/bessiecrab_1.png",
        "crab6_type == '5'", "emberisland/muskycrab_1.png",
        "crab6_type == '6'", "emberisland/stankcrab_1.png",
        "crab6_type == '7'", "emberisland/aqua1.png",
        "crab6_type == '8'", "emberisland/gray1.png",
        "crab6_type == '9'", "emberisland/green1.png",
        "crab6_type == '10'", "emberisland/orange1.png",
        "crab6_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab6_rarity == 'n'", "transparent.png",
        "crab6_rarity == 'r'", "misc/rare_star.png",
        "crab6_rarity == 'e'", "misc/epic_star.png",
        "crab6_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab6_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab6_type == '1'", "emberisland/crab_2.png",
        "crab6_type == '2'", "emberisland/strongcrab_2.png",
        "crab6_type == '3'", "emberisland/legendcrab_2.png",
        "crab6_type == '4'", "emberisland/bessiecrab_2.png",
        "crab6_type == '5'", "emberisland/muskycrab_2.png",
        "crab6_type == '6'", "emberisland/stankcrab_2.png",
        "crab6_type == '7'", "emberisland/aqua2.png",
        "crab6_type == '8'", "emberisland/gray2.png",
        "crab6_type == '9'", "emberisland/green2.png",
        "crab6_type == '10'", "emberisland/orange2.png",
        "crab6_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab6_rarity == 'n'", "transparent.png",
        "crab6_rarity == 'r'", "misc/rare_star.png",
        "crab6_rarity == 'e'", "misc/epic_star.png",
        "crab6_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab6_shuffle:
    "crab6_crab1"
    0.4
    "crab6_crab2"
    0.4
    repeat


image crab7_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab7_type == '1'", "emberisland/crab_1.png",
        "crab7_type == '2'", "emberisland/strongcrab_1.png",
        "crab7_type == '3'", "emberisland/legendcrab_1.png",
        "crab7_type == '4'", "emberisland/bessiecrab_1.png",
        "crab7_type == '5'", "emberisland/muskycrab_1.png",
        "crab7_type == '6'", "emberisland/stankcrab_1.png",
        "crab7_type == '7'", "emberisland/aqua1.png",
        "crab7_type == '8'", "emberisland/gray1.png",
        "crab7_type == '9'", "emberisland/green1.png",
        "crab7_type == '10'", "emberisland/orange1.png",
        "crab7_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab7_rarity == 'n'", "transparent.png",
        "crab7_rarity == 'r'", "misc/rare_star.png",
        "crab7_rarity == 'e'", "misc/epic_star.png",
        "crab7_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab7_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab7_type == '1'", "emberisland/crab_2.png",
        "crab7_type == '2'", "emberisland/strongcrab_2.png",
        "crab7_type == '3'", "emberisland/legendcrab_2.png",
        "crab7_type == '4'", "emberisland/bessiecrab_2.png",
        "crab7_type == '5'", "emberisland/muskycrab_2.png",
        "crab7_type == '6'", "emberisland/stankcrab_2.png",
        "crab7_type == '7'", "emberisland/aqua2.png",
        "crab7_type == '8'", "emberisland/gray2.png",
        "crab7_type == '9'", "emberisland/green2.png",
        "crab7_type == '10'", "emberisland/orange2.png",
        "crab7_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab7_rarity == 'n'", "transparent.png",
        "crab7_rarity == 'r'", "misc/rare_star.png",
        "crab7_rarity == 'e'", "misc/epic_star.png",
        "crab7_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab7_shuffle:
    "crab7_crab1"
    0.4
    "crab7_crab2"
    0.4
    repeat

image crab8_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab8_type == '1'", "emberisland/crab_1.png",
        "crab8_type == '2'", "emberisland/strongcrab_1.png",
        "crab8_type == '3'", "emberisland/legendcrab_1.png",
        "crab8_type == '4'", "emberisland/bessiecrab_1.png",
        "crab8_type == '5'", "emberisland/muskycrab_1.png",
        "crab8_type == '6'", "emberisland/stankcrab_1.png",
        "crab8_type == '7'", "emberisland/aqua1.png",
        "crab8_type == '8'", "emberisland/gray1.png",
        "crab8_type == '9'", "emberisland/green1.png",
        "crab8_type == '10'", "emberisland/orange1.png",
        "crab8_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab8_rarity == 'n'", "transparent.png",
        "crab8_rarity == 'r'", "misc/rare_star.png",
        "crab8_rarity == 'e'", "misc/epic_star.png",
        "crab8_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab8_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab8_type == '1'", "emberisland/crab_2.png",
        "crab8_type == '2'", "emberisland/strongcrab_2.png",
        "crab8_type == '3'", "emberisland/legendcrab_2.png",
        "crab8_type == '4'", "emberisland/bessiecrab_2.png",
        "crab8_type == '5'", "emberisland/muskycrab_2.png",
        "crab8_type == '6'", "emberisland/stankcrab_2.png",
        "crab8_type == '7'", "emberisland/aqua2.png",
        "crab8_type == '8'", "emberisland/gray2.png",
        "crab8_type == '9'", "emberisland/green2.png",
        "crab8_type == '10'", "emberisland/orange2.png",
        "crab8_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab8_rarity == 'n'", "transparent.png",
        "crab8_rarity == 'r'", "misc/rare_star.png",
        "crab8_rarity == 'e'", "misc/epic_star.png",
        "crab8_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab8_shuffle:
    "crab8_crab1"
    0.4
    "crab8_crab2"
    0.4
    repeat

image crab9_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab9_type == '1'", "emberisland/crab_1.png",
        "crab9_type == '2'", "emberisland/strongcrab_1.png",
        "crab9_type == '3'", "emberisland/legendcrab_1.png",
        "crab9_type == '4'", "emberisland/bessiecrab_1.png",
        "crab9_type == '5'", "emberisland/muskycrab_1.png",
        "crab9_type == '6'", "emberisland/stankcrab_1.png",
        "crab9_type == '7'", "emberisland/aqua1.png",
        "crab9_type == '8'", "emberisland/gray1.png",
        "crab9_type == '9'", "emberisland/green1.png",
        "crab9_type == '10'", "emberisland/orange1.png",
        "crab9_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab9_rarity == 'n'", "transparent.png",
        "crab9_rarity == 'r'", "misc/rare_star.png",
        "crab9_rarity == 'e'", "misc/epic_star.png",
        "crab9_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab9_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab9_type == '1'", "emberisland/crab_2.png",
        "crab9_type == '2'", "emberisland/strongcrab_2.png",
        "crab9_type == '3'", "emberisland/legendcrab_2.png",
        "crab9_type == '4'", "emberisland/bessiecrab_2.png",
        "crab9_type == '5'", "emberisland/muskycrab_2.png",
        "crab9_type == '6'", "emberisland/stankcrab_2.png",
        "crab9_type == '7'", "emberisland/aqua2.png",
        "crab9_type == '8'", "emberisland/gray2.png",
        "crab9_type == '9'", "emberisland/green2.png",
        "crab9_type == '10'", "emberisland/orange2.png",
        "crab9_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab9_rarity == 'n'", "transparent.png",
        "crab9_rarity == 'r'", "misc/rare_star.png",
        "crab9_rarity == 'e'", "misc/epic_star.png",
        "crab9_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab9_shuffle:
    "crab9_crab1"
    0.4
    "crab9_crab2"
    0.4
    repeat

image crab10_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab10_type == '1'", "emberisland/crab_1.png",
        "crab10_type == '2'", "emberisland/strongcrab_1.png",
        "crab10_type == '3'", "emberisland/legendcrab_1.png",
        "crab10_type == '4'", "emberisland/bessiecrab_1.png",
        "crab10_type == '5'", "emberisland/muskycrab_1.png",
        "crab10_type == '6'", "emberisland/stankcrab_1.png",
        "crab10_type == '7'", "emberisland/aqua1.png",
        "crab10_type == '8'", "emberisland/gray1.png",
        "crab10_type == '9'", "emberisland/green1.png",
        "crab10_type == '10'", "emberisland/orange1.png",
        "crab10_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab10_rarity == 'n'", "transparent.png",
        "crab10_rarity == 'r'", "misc/rare_star.png",
        "crab10_rarity == 'e'", "misc/epic_star.png",
        "crab10_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab10_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab10_type == '1'", "emberisland/crab_2.png",
        "crab10_type == '2'", "emberisland/strongcrab_2.png",
        "crab10_type == '3'", "emberisland/legendcrab_2.png",
        "crab10_type == '4'", "emberisland/bessiecrab_2.png",
        "crab10_type == '5'", "emberisland/muskycrab_2.png",
        "crab10_type == '6'", "emberisland/stankcrab_2.png",
        "crab10_type == '7'", "emberisland/aqua2.png",
        "crab10_type == '8'", "emberisland/gray2.png",
        "crab10_type == '9'", "emberisland/green2.png",
        "crab10_type == '10'", "emberisland/orange2.png",
        "crab10_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab10_rarity == 'n'", "transparent.png",
        "crab10_rarity == 'r'", "misc/rare_star.png",
        "crab10_rarity == 'e'", "misc/epic_star.png",
        "crab10_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab10_shuffle:
    "crab10_crab1"
    0.4
    "crab10_crab2"
    0.4
    repeat

image crab11_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab11_type == '1'", "emberisland/crab_1.png",
        "crab11_type == '2'", "emberisland/strongcrab_1.png",
        "crab11_type == '3'", "emberisland/legendcrab_1.png",
        "crab11_type == '4'", "emberisland/bessiecrab_1.png",
        "crab11_type == '5'", "emberisland/muskycrab_1.png",
        "crab11_type == '6'", "emberisland/stankcrab_1.png",
        "crab11_type == '7'", "emberisland/aqua1.png",
        "crab11_type == '8'", "emberisland/gray1.png",
        "crab11_type == '9'", "emberisland/green1.png",
        "crab11_type == '10'", "emberisland/orange1.png",
        "crab11_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab11_rarity == 'n'", "transparent.png",
        "crab11_rarity == 'r'", "misc/rare_star.png",
        "crab11_rarity == 'e'", "misc/epic_star.png",
        "crab11_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab11_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab11_type == '1'", "emberisland/crab_2.png",
        "crab11_type == '2'", "emberisland/strongcrab_2.png",
        "crab11_type == '3'", "emberisland/legendcrab_2.png",
        "crab11_type == '4'", "emberisland/bessiecrab_2.png",
        "crab11_type == '5'", "emberisland/muskycrab_2.png",
        "crab11_type == '6'", "emberisland/stankcrab_2.png",
        "crab11_type == '7'", "emberisland/aqua2.png",
        "crab11_type == '8'", "emberisland/gray2.png",
        "crab11_type == '9'", "emberisland/green2.png",
        "crab11_type == '10'", "emberisland/orange2.png",
        "crab11_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab11_rarity == 'n'", "transparent.png",
        "crab11_rarity == 'r'", "misc/rare_star.png",
        "crab11_rarity == 'e'", "misc/epic_star.png",
        "crab11_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab11_shuffle:
    "crab11_crab1"
    0.4
    "crab11_crab2"
    0.4
    repeat

image crab12_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab12_type == '1'", "emberisland/crab_1.png",
        "crab12_type == '2'", "emberisland/strongcrab_1.png",
        "crab12_type == '3'", "emberisland/legendcrab_1.png",
        "crab12_type == '4'", "emberisland/bessiecrab_1.png",
        "crab12_type == '5'", "emberisland/muskycrab_1.png",
        "crab12_type == '6'", "emberisland/stankcrab_1.png",
        "crab12_type == '7'", "emberisland/aqua1.png",
        "crab12_type == '8'", "emberisland/gray1.png",
        "crab12_type == '9'", "emberisland/green1.png",
        "crab12_type == '10'", "emberisland/orange1.png",
        "crab12_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab12_rarity == 'n'", "transparent.png",
        "crab12_rarity == 'r'", "misc/rare_star.png",
        "crab12_rarity == 'e'", "misc/epic_star.png",
        "crab12_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab12_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab12_type == '1'", "emberisland/crab_2.png",
        "crab12_type == '2'", "emberisland/strongcrab_2.png",
        "crab12_type == '3'", "emberisland/legendcrab_2.png",
        "crab12_type == '4'", "emberisland/bessiecrab_2.png",
        "crab12_type == '5'", "emberisland/muskycrab_2.png",
        "crab12_type == '6'", "emberisland/stankcrab_2.png",
        "crab12_type == '7'", "emberisland/aqua2.png",
        "crab12_type == '8'", "emberisland/gray2.png",
        "crab12_type == '9'", "emberisland/green2.png",
        "crab12_type == '10'", "emberisland/orange2.png",
        "crab12_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab12_rarity == 'n'", "transparent.png",
        "crab12_rarity == 'r'", "misc/rare_star.png",
        "crab12_rarity == 'e'", "misc/epic_star.png",
        "crab12_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab12_shuffle:
    "crab12_crab1"
    0.4
    "crab12_crab2"
    0.4
    repeat

image crab13_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab13_type == '1'", "emberisland/crab_1.png",
        "crab13_type == '2'", "emberisland/strongcrab_1.png",
        "crab13_type == '3'", "emberisland/legendcrab_1.png",
        "crab13_type == '4'", "emberisland/bessiecrab_1.png",
        "crab13_type == '5'", "emberisland/muskycrab_1.png",
        "crab13_type == '6'", "emberisland/stankcrab_1.png",
        "crab13_type == '7'", "emberisland/aqua1.png",
        "crab13_type == '8'", "emberisland/gray1.png",
        "crab13_type == '9'", "emberisland/green1.png",
        "crab13_type == '10'", "emberisland/orange1.png",
        "crab13_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab13_rarity == 'n'", "transparent.png",
        "crab13_rarity == 'r'", "misc/rare_star.png",
        "crab13_rarity == 'e'", "misc/epic_star.png",
        "crab13_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab13_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab13_type == '1'", "emberisland/crab_2.png",
        "crab13_type == '2'", "emberisland/strongcrab_2.png",
        "crab13_type == '3'", "emberisland/legendcrab_2.png",
        "crab13_type == '4'", "emberisland/bessiecrab_2.png",
        "crab13_type == '5'", "emberisland/muskycrab_2.png",
        "crab13_type == '6'", "emberisland/stankcrab_2.png",
        "crab13_type == '7'", "emberisland/aqua2.png",
        "crab13_type == '8'", "emberisland/gray2.png",
        "crab13_type == '9'", "emberisland/green2.png",
        "crab13_type == '10'", "emberisland/orange2.png",
        "crab13_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab13_rarity == 'n'", "transparent.png",
        "crab13_rarity == 'r'", "misc/rare_star.png",
        "crab13_rarity == 'e'", "misc/epic_star.png",
        "crab13_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab13_shuffle:
    "crab13_crab1"
    0.4
    "crab13_crab2"
    0.4
    repeat

image crab14_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab14_type == '1'", "emberisland/crab_1.png",
        "crab14_type == '2'", "emberisland/strongcrab_1.png",
        "crab14_type == '3'", "emberisland/legendcrab_1.png",
        "crab14_type == '4'", "emberisland/bessiecrab_1.png",
        "crab14_type == '5'", "emberisland/muskycrab_1.png",
        "crab14_type == '6'", "emberisland/stankcrab_1.png",
        "crab14_type == '7'", "emberisland/aqua1.png",
        "crab14_type == '8'", "emberisland/gray1.png",
        "crab14_type == '9'", "emberisland/green1.png",
        "crab14_type == '10'", "emberisland/orange1.png",
        "crab14_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab14_rarity == 'n'", "transparent.png",
        "crab14_rarity == 'r'", "misc/rare_star.png",
        "crab14_rarity == 'e'", "misc/epic_star.png",
        "crab14_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab14_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab14_type == '1'", "emberisland/crab_2.png",
        "crab14_type == '2'", "emberisland/strongcrab_2.png",
        "crab14_type == '3'", "emberisland/legendcrab_2.png",
        "crab14_type == '4'", "emberisland/bessiecrab_2.png",
        "crab14_type == '5'", "emberisland/muskycrab_2.png",
        "crab14_type == '6'", "emberisland/stankcrab_2.png",
        "crab14_type == '7'", "emberisland/aqua2.png",
        "crab14_type == '8'", "emberisland/gray2.png",
        "crab14_type == '9'", "emberisland/green2.png",
        "crab14_type == '10'", "emberisland/orange2.png",
        "crab14_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab14_rarity == 'n'", "transparent.png",
        "crab14_rarity == 'r'", "misc/rare_star.png",
        "crab14_rarity == 'e'", "misc/epic_star.png",
        "crab14_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab14_shuffle:
    "crab14_crab1"
    0.4
    "crab14_crab2"
    0.4
    repeat

image crab15_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab15_type == '1'", "emberisland/crab_1.png",
        "crab15_type == '2'", "emberisland/strongcrab_1.png",
        "crab15_type == '3'", "emberisland/legendcrab_1.png",
        "crab15_type == '4'", "emberisland/bessiecrab_1.png",
        "crab15_type == '5'", "emberisland/muskycrab_1.png",
        "crab15_type == '6'", "emberisland/stankcrab_1.png",
        "crab15_type == '7'", "emberisland/aqua1.png",
        "crab15_type == '8'", "emberisland/gray1.png",
        "crab15_type == '9'", "emberisland/green1.png",
        "crab15_type == '10'", "emberisland/orange1.png",
        "crab15_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab15_rarity == 'n'", "transparent.png",
        "crab15_rarity == 'r'", "misc/rare_star.png",
        "crab15_rarity == 'e'", "misc/epic_star.png",
        "crab15_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab15_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab15_type == '1'", "emberisland/crab_2.png",
        "crab15_type == '2'", "emberisland/strongcrab_2.png",
        "crab15_type == '3'", "emberisland/legendcrab_2.png",
        "crab15_type == '4'", "emberisland/bessiecrab_2.png",
        "crab15_type == '5'", "emberisland/muskycrab_2.png",
        "crab15_type == '6'", "emberisland/stankcrab_2.png",
        "crab15_type == '7'", "emberisland/aqua2.png",
        "crab15_type == '8'", "emberisland/gray2.png",
        "crab15_type == '9'", "emberisland/green2.png",
        "crab15_type == '10'", "emberisland/orange2.png",
        "crab15_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab15_rarity == 'n'", "transparent.png",
        "crab15_rarity == 'r'", "misc/rare_star.png",
        "crab15_rarity == 'e'", "misc/epic_star.png",
        "crab15_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab15_shuffle:
    "crab15_crab1"
    0.4
    "crab15_crab2"
    0.4
    repeat

image crab16_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab16_type == '1'", "emberisland/crab_1.png",
        "crab16_type == '2'", "emberisland/strongcrab_1.png",
        "crab16_type == '3'", "emberisland/legendcrab_1.png",
        "crab16_type == '4'", "emberisland/bessiecrab_1.png",
        "crab16_type == '5'", "emberisland/muskycrab_1.png",
        "crab16_type == '6'", "emberisland/stankcrab_1.png",
        "crab16_type == '7'", "emberisland/aqua1.png",
        "crab16_type == '8'", "emberisland/gray1.png",
        "crab16_type == '9'", "emberisland/green1.png",
        "crab16_type == '10'", "emberisland/orange1.png",
        "crab16_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab16_rarity == 'n'", "transparent.png",
        "crab16_rarity == 'r'", "misc/rare_star.png",
        "crab16_rarity == 'e'", "misc/epic_star.png",
        "crab16_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab16_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab16_type == '1'", "emberisland/crab_2.png",
        "crab16_type == '2'", "emberisland/strongcrab_2.png",
        "crab16_type == '3'", "emberisland/legendcrab_2.png",
        "crab16_type == '4'", "emberisland/bessiecrab_2.png",
        "crab16_type == '5'", "emberisland/muskycrab_2.png",
        "crab16_type == '6'", "emberisland/stankcrab_2.png",
        "crab16_type == '7'", "emberisland/aqua2.png",
        "crab16_type == '8'", "emberisland/gray2.png",
        "crab16_type == '9'", "emberisland/green2.png",
        "crab16_type == '10'", "emberisland/orange2.png",
        "crab16_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab16_rarity == 'n'", "transparent.png",
        "crab16_rarity == 'r'", "misc/rare_star.png",
        "crab16_rarity == 'e'", "misc/epic_star.png",
        "crab16_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab16_shuffle:
    "crab16_crab1"
    0.4
    "crab16_crab2"
    0.4
    repeat

image crab17_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab17_type == '1'", "emberisland/crab_1.png",
        "crab17_type == '2'", "emberisland/strongcrab_1.png",
        "crab17_type == '3'", "emberisland/legendcrab_1.png",
        "crab17_type == '4'", "emberisland/bessiecrab_1.png",
        "crab17_type == '5'", "emberisland/muskycrab_1.png",
        "crab17_type == '6'", "emberisland/stankcrab_1.png",
        "crab17_type == '7'", "emberisland/aqua1.png",
        "crab17_type == '8'", "emberisland/gray1.png",
        "crab17_type == '9'", "emberisland/green1.png",
        "crab17_type == '10'", "emberisland/orange1.png",
        "crab17_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab17_rarity == 'n'", "transparent.png",
        "crab17_rarity == 'r'", "misc/rare_star.png",
        "crab17_rarity == 'e'", "misc/epic_star.png",
        "crab17_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab17_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab17_type == '1'", "emberisland/crab_2.png",
        "crab17_type == '2'", "emberisland/strongcrab_2.png",
        "crab17_type == '3'", "emberisland/legendcrab_2.png",
        "crab17_type == '4'", "emberisland/bessiecrab_2.png",
        "crab17_type == '5'", "emberisland/muskycrab_2.png",
        "crab17_type == '6'", "emberisland/stankcrab_2.png",
        "crab17_type == '7'", "emberisland/aqua2.png",
        "crab17_type == '8'", "emberisland/gray2.png",
        "crab17_type == '9'", "emberisland/green2.png",
        "crab17_type == '10'", "emberisland/orange2.png",
        "crab17_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab17_rarity == 'n'", "transparent.png",
        "crab17_rarity == 'r'", "misc/rare_star.png",
        "crab17_rarity == 'e'", "misc/epic_star.png",
        "crab17_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab17_shuffle:
    "crab17_crab1"
    0.4
    "crab17_crab2"
    0.4
    repeat

image crab18_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab18_type == '1'", "emberisland/crab_1.png",
        "crab18_type == '2'", "emberisland/strongcrab_1.png",
        "crab18_type == '3'", "emberisland/legendcrab_1.png",
        "crab18_type == '4'", "emberisland/bessiecrab_1.png",
        "crab18_type == '5'", "emberisland/muskycrab_1.png",
        "crab18_type == '6'", "emberisland/stankcrab_1.png",
        "crab18_type == '7'", "emberisland/aqua1.png",
        "crab18_type == '8'", "emberisland/gray1.png",
        "crab18_type == '9'", "emberisland/green1.png",
        "crab18_type == '10'", "emberisland/orange1.png",
        "crab18_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab18_rarity == 'n'", "transparent.png",
        "crab18_rarity == 'r'", "misc/rare_star.png",
        "crab18_rarity == 'e'", "misc/epic_star.png",
        "crab18_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab18_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab18_type == '1'", "emberisland/crab_2.png",
        "crab18_type == '2'", "emberisland/strongcrab_2.png",
        "crab18_type == '3'", "emberisland/legendcrab_2.png",
        "crab18_type == '4'", "emberisland/bessiecrab_2.png",
        "crab18_type == '5'", "emberisland/muskycrab_2.png",
        "crab18_type == '6'", "emberisland/stankcrab_2.png",
        "crab18_type == '7'", "emberisland/aqua2.png",
        "crab18_type == '8'", "emberisland/gray2.png",
        "crab18_type == '9'", "emberisland/green2.png",
        "crab18_type == '10'", "emberisland/orange2.png",
        "crab18_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab18_rarity == 'n'", "transparent.png",
        "crab18_rarity == 'r'", "misc/rare_star.png",
        "crab18_rarity == 'e'", "misc/epic_star.png",
        "crab18_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab18_shuffle:
    "crab18_crab1"
    0.4
    "crab18_crab2"
    0.4
    repeat

image crab19_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab19_type == '1'", "emberisland/crab_1.png",
        "crab19_type == '2'", "emberisland/strongcrab_1.png",
        "crab19_type == '3'", "emberisland/legendcrab_1.png",
        "crab19_type == '4'", "emberisland/bessiecrab_1.png",
        "crab19_type == '5'", "emberisland/muskycrab_1.png",
        "crab19_type == '6'", "emberisland/stankcrab_1.png",
        "crab19_type == '7'", "emberisland/aqua1.png",
        "crab19_type == '8'", "emberisland/gray1.png",
        "crab19_type == '9'", "emberisland/green1.png",
        "crab19_type == '10'", "emberisland/orange1.png",
        "crab19_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab19_rarity == 'n'", "transparent.png",
        "crab19_rarity == 'r'", "misc/rare_star.png",
        "crab19_rarity == 'e'", "misc/epic_star.png",
        "crab19_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab19_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab19_type == '1'", "emberisland/crab_2.png",
        "crab19_type == '2'", "emberisland/strongcrab_2.png",
        "crab19_type == '3'", "emberisland/legendcrab_2.png",
        "crab19_type == '4'", "emberisland/bessiecrab_2.png",
        "crab19_type == '5'", "emberisland/muskycrab_2.png",
        "crab19_type == '6'", "emberisland/stankcrab_2.png",
        "crab19_type == '7'", "emberisland/aqua2.png",
        "crab19_type == '8'", "emberisland/gray2.png",
        "crab19_type == '9'", "emberisland/green2.png",
        "crab19_type == '10'", "emberisland/orange2.png",
        "crab19_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab19_rarity == 'n'", "transparent.png",
        "crab19_rarity == 'r'", "misc/rare_star.png",
        "crab19_rarity == 'e'", "misc/epic_star.png",
        "crab19_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab19_shuffle:
    "crab19_crab1"
    0.4
    "crab19_crab2"
    0.4
    repeat

image crab20_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab20_type == '1'", "emberisland/crab_1.png",
        "crab20_type == '2'", "emberisland/strongcrab_1.png",
        "crab20_type == '3'", "emberisland/legendcrab_1.png",
        "crab20_type == '4'", "emberisland/bessiecrab_1.png",
        "crab20_type == '5'", "emberisland/muskycrab_1.png",
        "crab20_type == '6'", "emberisland/stankcrab_1.png",
        "crab20_type == '7'", "emberisland/aqua1.png",
        "crab20_type == '8'", "emberisland/gray1.png",
        "crab20_type == '9'", "emberisland/green1.png",
        "crab20_type == '10'", "emberisland/orange1.png",
        "crab20_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab20_rarity == 'n'", "transparent.png",
        "crab20_rarity == 'r'", "misc/rare_star.png",
        "crab20_rarity == 'e'", "misc/epic_star.png",
        "crab20_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab20_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab20_type == '1'", "emberisland/crab_2.png",
        "crab20_type == '2'", "emberisland/strongcrab_2.png",
        "crab20_type == '3'", "emberisland/legendcrab_2.png",
        "crab20_type == '4'", "emberisland/bessiecrab_2.png",
        "crab20_type == '5'", "emberisland/muskycrab_2.png",
        "crab20_type == '6'", "emberisland/stankcrab_2.png",
        "crab20_type == '7'", "emberisland/aqua2.png",
        "crab20_type == '8'", "emberisland/gray2.png",
        "crab20_type == '9'", "emberisland/green2.png",
        "crab20_type == '10'", "emberisland/orange2.png",
        "crab20_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab20_rarity == 'n'", "transparent.png",
        "crab20_rarity == 'r'", "misc/rare_star.png",
        "crab20_rarity == 'e'", "misc/epic_star.png",
        "crab20_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab20_shuffle:
    "crab20_crab1"
    0.4
    "crab20_crab2"
    0.4
    repeat

image crab21_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab21_type == '1'", "emberisland/crab_1.png",
        "crab21_type == '2'", "emberisland/strongcrab_1.png",
        "crab21_type == '3'", "emberisland/legendcrab_1.png",
        "crab21_type == '4'", "emberisland/bessiecrab_1.png",
        "crab21_type == '5'", "emberisland/muskycrab_1.png",
        "crab21_type == '6'", "emberisland/stankcrab_1.png",
        "crab21_type == '7'", "emberisland/aqua1.png",
        "crab21_type == '8'", "emberisland/gray1.png",
        "crab21_type == '9'", "emberisland/green1.png",
        "crab21_type == '10'", "emberisland/orange1.png",
        "crab21_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab21_rarity == 'n'", "transparent.png",
        "crab21_rarity == 'r'", "misc/rare_star.png",
        "crab21_rarity == 'e'", "misc/epic_star.png",
        "crab21_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab21_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab21_type == '1'", "emberisland/crab_2.png",
        "crab21_type == '2'", "emberisland/strongcrab_2.png",
        "crab21_type == '3'", "emberisland/legendcrab_2.png",
        "crab21_type == '4'", "emberisland/bessiecrab_2.png",
        "crab21_type == '5'", "emberisland/muskycrab_2.png",
        "crab21_type == '6'", "emberisland/stankcrab_2.png",
        "crab21_type == '7'", "emberisland/aqua2.png",
        "crab21_type == '8'", "emberisland/gray2.png",
        "crab21_type == '9'", "emberisland/green2.png",
        "crab21_type == '10'", "emberisland/orange2.png",
        "crab21_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab21_rarity == 'n'", "transparent.png",
        "crab21_rarity == 'r'", "misc/rare_star.png",
        "crab21_rarity == 'e'", "misc/epic_star.png",
        "crab21_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab21_shuffle:
    "crab21_crab1"
    0.4
    "crab21_crab2"
    0.4
    repeat

image crab22_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab22_type == '1'", "emberisland/crab_1.png",
        "crab22_type == '2'", "emberisland/strongcrab_1.png",
        "crab22_type == '3'", "emberisland/legendcrab_1.png",
        "crab22_type == '4'", "emberisland/bessiecrab_1.png",
        "crab22_type == '5'", "emberisland/muskycrab_1.png",
        "crab22_type == '6'", "emberisland/stankcrab_1.png",
        "crab22_type == '7'", "emberisland/aqua1.png",
        "crab22_type == '8'", "emberisland/gray1.png",
        "crab22_type == '9'", "emberisland/green1.png",
        "crab22_type == '10'", "emberisland/orange1.png",
        "crab22_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab22_rarity == 'n'", "transparent.png",
        "crab22_rarity == 'r'", "misc/rare_star.png",
        "crab22_rarity == 'e'", "misc/epic_star.png",
        "crab22_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab22_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab22_type == '1'", "emberisland/crab_2.png",
        "crab22_type == '2'", "emberisland/strongcrab_2.png",
        "crab22_type == '3'", "emberisland/legendcrab_2.png",
        "crab22_type == '4'", "emberisland/bessiecrab_2.png",
        "crab22_type == '5'", "emberisland/muskycrab_2.png",
        "crab22_type == '6'", "emberisland/stankcrab_2.png",
        "crab22_type == '7'", "emberisland/aqua2.png",
        "crab22_type == '8'", "emberisland/gray2.png",
        "crab22_type == '9'", "emberisland/green2.png",
        "crab22_type == '10'", "emberisland/orange2.png",
        "crab22_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab22_rarity == 'n'", "transparent.png",
        "crab22_rarity == 'r'", "misc/rare_star.png",
        "crab22_rarity == 'e'", "misc/epic_star.png",
        "crab22_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab22_shuffle:
    "crab22_crab1"
    0.4
    "crab22_crab2"
    0.4
    repeat

image crab23_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab23_type == '1'", "emberisland/crab_1.png",
        "crab23_type == '2'", "emberisland/strongcrab_1.png",
        "crab23_type == '3'", "emberisland/legendcrab_1.png",
        "crab23_type == '4'", "emberisland/bessiecrab_1.png",
        "crab23_type == '5'", "emberisland/muskycrab_1.png",
        "crab23_type == '6'", "emberisland/stankcrab_1.png",
        "crab23_type == '7'", "emberisland/aqua1.png",
        "crab23_type == '8'", "emberisland/gray1.png",
        "crab23_type == '9'", "emberisland/green1.png",
        "crab23_type == '10'", "emberisland/orange1.png",
        "crab23_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab23_rarity == 'n'", "transparent.png",
        "crab23_rarity == 'r'", "misc/rare_star.png",
        "crab23_rarity == 'e'", "misc/epic_star.png",
        "crab23_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab23_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab23_type == '1'", "emberisland/crab_2.png",
        "crab23_type == '2'", "emberisland/strongcrab_2.png",
        "crab23_type == '3'", "emberisland/legendcrab_2.png",
        "crab23_type == '4'", "emberisland/bessiecrab_2.png",
        "crab23_type == '5'", "emberisland/muskycrab_2.png",
        "crab23_type == '6'", "emberisland/stankcrab_2.png",
        "crab23_type == '7'", "emberisland/aqua2.png",
        "crab23_type == '8'", "emberisland/gray2.png",
        "crab23_type == '9'", "emberisland/green2.png",
        "crab23_type == '10'", "emberisland/orange2.png",
        "crab23_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab23_rarity == 'n'", "transparent.png",
        "crab23_rarity == 'r'", "misc/rare_star.png",
        "crab23_rarity == 'e'", "misc/epic_star.png",
        "crab23_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab23_shuffle:
    "crab23_crab1"
    0.4
    "crab23_crab2"
    0.4
    repeat

image crab24_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab24_type == '1'", "emberisland/crab_1.png",
        "crab24_type == '2'", "emberisland/strongcrab_1.png",
        "crab24_type == '3'", "emberisland/legendcrab_1.png",
        "crab24_type == '4'", "emberisland/bessiecrab_1.png",
        "crab24_type == '5'", "emberisland/muskycrab_1.png",
        "crab24_type == '6'", "emberisland/stankcrab_1.png",
        "crab24_type == '7'", "emberisland/aqua1.png",
        "crab24_type == '8'", "emberisland/gray1.png",
        "crab24_type == '9'", "emberisland/green1.png",
        "crab24_type == '10'", "emberisland/orange1.png",
        "crab24_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab24_rarity == 'n'", "transparent.png",
        "crab24_rarity == 'r'", "misc/rare_star.png",
        "crab24_rarity == 'e'", "misc/epic_star.png",
        "crab24_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab24_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab24_type == '1'", "emberisland/crab_2.png",
        "crab24_type == '2'", "emberisland/strongcrab_2.png",
        "crab24_type == '3'", "emberisland/legendcrab_2.png",
        "crab24_type == '4'", "emberisland/bessiecrab_2.png",
        "crab24_type == '5'", "emberisland/muskycrab_2.png",
        "crab24_type == '6'", "emberisland/stankcrab_2.png",
        "crab24_type == '7'", "emberisland/aqua2.png",
        "crab24_type == '8'", "emberisland/gray2.png",
        "crab24_type == '9'", "emberisland/green2.png",
        "crab24_type == '10'", "emberisland/orange2.png",
        "crab24_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab24_rarity == 'n'", "transparent.png",
        "crab24_rarity == 'r'", "misc/rare_star.png",
        "crab24_rarity == 'e'", "misc/epic_star.png",
        "crab24_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab24_shuffle:
    "crab24_crab1"
    0.4
    "crab24_crab2"
    0.4
    repeat


image crab25_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab25_type == '1'", "emberisland/crab_1.png",
        "crab25_type == '2'", "emberisland/strongcrab_1.png",
        "crab25_type == '3'", "emberisland/legendcrab_1.png",
        "crab25_type == '4'", "emberisland/bessiecrab_1.png",
        "crab25_type == '5'", "emberisland/muskycrab_1.png",
        "crab25_type == '6'", "emberisland/stankcrab_1.png",
        "crab25_type == '7'", "emberisland/aqua1.png",
        "crab25_type == '8'", "emberisland/gray1.png",
        "crab25_type == '9'", "emberisland/green1.png",
        "crab25_type == '10'", "emberisland/orange1.png",
        "crab25_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab25_rarity == 'n'", "transparent.png",
        "crab25_rarity == 'r'", "misc/rare_star.png",
        "crab25_rarity == 'e'", "misc/epic_star.png",
        "crab25_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab25_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab25_type == '1'", "emberisland/crab_2.png",
        "crab25_type == '2'", "emberisland/strongcrab_2.png",
        "crab25_type == '3'", "emberisland/legendcrab_2.png",
        "crab25_type == '4'", "emberisland/bessiecrab_2.png",
        "crab25_type == '5'", "emberisland/muskycrab_2.png",
        "crab25_type == '6'", "emberisland/stankcrab_2.png",
        "crab25_type == '7'", "emberisland/aqua2.png",
        "crab25_type == '8'", "emberisland/gray2.png",
        "crab25_type == '9'", "emberisland/green2.png",
        "crab25_type == '10'", "emberisland/orange2.png",
        "crab25_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab25_rarity == 'n'", "transparent.png",
        "crab25_rarity == 'r'", "misc/rare_star.png",
        "crab25_rarity == 'e'", "misc/epic_star.png",
        "crab25_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab25_shuffle:
    "crab25_crab1"
    0.4
    "crab25_crab2"
    0.4
    repeat


image crab26_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab26_type == '1'", "emberisland/crab_1.png",
        "crab26_type == '2'", "emberisland/strongcrab_1.png",
        "crab26_type == '3'", "emberisland/legendcrab_1.png",
        "crab26_type == '4'", "emberisland/bessiecrab_1.png",
        "crab26_type == '5'", "emberisland/muskycrab_1.png",
        "crab26_type == '6'", "emberisland/stankcrab_1.png",
        "crab26_type == '7'", "emberisland/aqua1.png",
        "crab26_type == '8'", "emberisland/gray1.png",
        "crab26_type == '9'", "emberisland/green1.png",
        "crab26_type == '10'", "emberisland/orange1.png",
        "crab26_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab26_rarity == 'n'", "transparent.png",
        "crab26_rarity == 'r'", "misc/rare_star.png",
        "crab26_rarity == 'e'", "misc/epic_star.png",
        "crab26_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab26_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab26_type == '1'", "emberisland/crab_2.png",
        "crab26_type == '2'", "emberisland/strongcrab_2.png",
        "crab26_type == '3'", "emberisland/legendcrab_2.png",
        "crab26_type == '4'", "emberisland/bessiecrab_2.png",
        "crab26_type == '5'", "emberisland/muskycrab_2.png",
        "crab26_type == '6'", "emberisland/stankcrab_2.png",
        "crab26_type == '7'", "emberisland/aqua2.png",
        "crab26_type == '8'", "emberisland/gray2.png",
        "crab26_type == '9'", "emberisland/green2.png",
        "crab26_type == '10'", "emberisland/orange2.png",
        "crab26_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab26_rarity == 'n'", "transparent.png",
        "crab26_rarity == 'r'", "misc/rare_star.png",
        "crab26_rarity == 'e'", "misc/epic_star.png",
        "crab26_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab26_shuffle:
    "crab26_crab1"
    0.4
    "crab26_crab2"
    0.4
    repeat

image crab27_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab27_type == '1'", "emberisland/crab_1.png",
        "crab27_type == '2'", "emberisland/strongcrab_1.png",
        "crab27_type == '3'", "emberisland/legendcrab_1.png",
        "crab27_type == '4'", "emberisland/bessiecrab_1.png",
        "crab27_type == '5'", "emberisland/muskycrab_1.png",
        "crab27_type == '6'", "emberisland/stankcrab_1.png",
        "crab27_type == '7'", "emberisland/aqua1.png",
        "crab27_type == '8'", "emberisland/gray1.png",
        "crab27_type == '9'", "emberisland/green1.png",
        "crab27_type == '10'", "emberisland/orange1.png",
        "crab27_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab27_rarity == 'n'", "transparent.png",
        "crab27_rarity == 'r'", "misc/rare_star.png",
        "crab27_rarity == 'e'", "misc/epic_star.png",
        "crab27_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab27_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab27_type == '1'", "emberisland/crab_2.png",
        "crab27_type == '2'", "emberisland/strongcrab_2.png",
        "crab27_type == '3'", "emberisland/legendcrab_2.png",
        "crab27_type == '4'", "emberisland/bessiecrab_2.png",
        "crab27_type == '5'", "emberisland/muskycrab_2.png",
        "crab27_type == '6'", "emberisland/stankcrab_2.png",
        "crab27_type == '7'", "emberisland/aqua2.png",
        "crab27_type == '8'", "emberisland/gray2.png",
        "crab27_type == '9'", "emberisland/green2.png",
        "crab27_type == '10'", "emberisland/orange2.png",
        "crab27_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab27_rarity == 'n'", "transparent.png",
        "crab27_rarity == 'r'", "misc/rare_star.png",
        "crab27_rarity == 'e'", "misc/epic_star.png",
        "crab27_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab27_shuffle:
    "crab27_crab1"
    0.4
    "crab27_crab2"
    0.4
    repeat

image crab28_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab28_type == '1'", "emberisland/crab_1.png",
        "crab28_type == '2'", "emberisland/strongcrab_1.png",
        "crab28_type == '3'", "emberisland/legendcrab_1.png",
        "crab28_type == '4'", "emberisland/bessiecrab_1.png",
        "crab28_type == '5'", "emberisland/muskycrab_1.png",
        "crab28_type == '6'", "emberisland/stankcrab_1.png",
        "crab28_type == '7'", "emberisland/aqua1.png",
        "crab28_type == '8'", "emberisland/gray1.png",
        "crab28_type == '9'", "emberisland/green1.png",
        "crab28_type == '10'", "emberisland/orange1.png",
        "crab28_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab28_rarity == 'n'", "transparent.png",
        "crab28_rarity == 'r'", "misc/rare_star.png",
        "crab28_rarity == 'e'", "misc/epic_star.png",
        "crab28_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab28_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab28_type == '1'", "emberisland/crab_2.png",
        "crab28_type == '2'", "emberisland/strongcrab_2.png",
        "crab28_type == '3'", "emberisland/legendcrab_2.png",
        "crab28_type == '4'", "emberisland/bessiecrab_2.png",
        "crab28_type == '5'", "emberisland/muskycrab_2.png",
        "crab28_type == '6'", "emberisland/stankcrab_2.png",
        "crab28_type == '7'", "emberisland/aqua2.png",
        "crab28_type == '8'", "emberisland/gray2.png",
        "crab28_type == '9'", "emberisland/green2.png",
        "crab28_type == '10'", "emberisland/orange2.png",
        "crab28_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab28_rarity == 'n'", "transparent.png",
        "crab28_rarity == 'r'", "misc/rare_star.png",
        "crab28_rarity == 'e'", "misc/epic_star.png",
        "crab28_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab28_shuffle:
    "crab28_crab1"
    0.4
    "crab28_crab2"
    0.4
    repeat

image crab29_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab29_type == '1'", "emberisland/crab_1.png",
        "crab29_type == '2'", "emberisland/strongcrab_1.png",
        "crab29_type == '3'", "emberisland/legendcrab_1.png",
        "crab29_type == '4'", "emberisland/bessiecrab_1.png",
        "crab29_type == '5'", "emberisland/muskycrab_1.png",
        "crab29_type == '6'", "emberisland/stankcrab_1.png",
        "crab29_type == '7'", "emberisland/aqua1.png",
        "crab29_type == '8'", "emberisland/gray1.png",
        "crab29_type == '9'", "emberisland/green1.png",
        "crab29_type == '10'", "emberisland/orange1.png",
        "crab29_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab29_rarity == 'n'", "transparent.png",
        "crab29_rarity == 'r'", "misc/rare_star.png",
        "crab29_rarity == 'e'", "misc/epic_star.png",
        "crab29_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab29_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab29_type == '1'", "emberisland/crab_2.png",
        "crab29_type == '2'", "emberisland/strongcrab_2.png",
        "crab29_type == '3'", "emberisland/legendcrab_2.png",
        "crab29_type == '4'", "emberisland/bessiecrab_2.png",
        "crab29_type == '5'", "emberisland/muskycrab_2.png",
        "crab29_type == '6'", "emberisland/stankcrab_2.png",
        "crab29_type == '7'", "emberisland/aqua2.png",
        "crab29_type == '8'", "emberisland/gray2.png",
        "crab29_type == '9'", "emberisland/green2.png",
        "crab29_type == '10'", "emberisland/orange2.png",
        "crab29_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab29_rarity == 'n'", "transparent.png",
        "crab29_rarity == 'r'", "misc/rare_star.png",
        "crab29_rarity == 'e'", "misc/epic_star.png",
        "crab29_rarity == 'l'", "misc/legend_star.png",)     )

image crab29_shuffle:
    "crab29_crab1"
    0.4
    "crab29_crab2"
    0.4
    repeat

image crab30_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab30_type == '1'", "emberisland/crab_1.png",
        "crab30_type == '2'", "emberisland/strongcrab_1.png",
        "crab30_type == '3'", "emberisland/legendcrab_1.png",
        "crab30_type == '4'", "emberisland/bessiecrab_1.png",
        "crab30_type == '5'", "emberisland/muskycrab_1.png",
        "crab30_type == '6'", "emberisland/stankcrab_1.png",
        "crab30_type == '7'", "emberisland/aqua1.png",
        "crab30_type == '8'", "emberisland/gray1.png",
        "crab30_type == '9'", "emberisland/green1.png",
        "crab30_type == '10'", "emberisland/orange1.png",
        "crab30_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab30_rarity == 'n'", "transparent.png",
        "crab30_rarity == 'r'", "misc/rare_star.png",
        "crab30_rarity == 'e'", "misc/epic_star.png",
        "crab30_rarity == 'l'", "misc/legend_star.png",) 
    )


image crab30_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab30_type == '1'", "emberisland/crab_2.png",
        "crab30_type == '2'", "emberisland/strongcrab_2.png",
        "crab30_type == '3'", "emberisland/legendcrab_2.png",
        "crab30_type == '4'", "emberisland/bessiecrab_2.png",
        "crab30_type == '5'", "emberisland/muskycrab_2.png",
        "crab30_type == '6'", "emberisland/stankcrab_2.png",
        "crab30_type == '7'", "emberisland/aqua2.png",
        "crab30_type == '8'", "emberisland/gray2.png",
        "crab30_type == '9'", "emberisland/green2.png",
        "crab30_type == '10'", "emberisland/orange2.png",
        "crab30_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab30_rarity == 'n'", "transparent.png",
        "crab30_rarity == 'r'", "misc/rare_star.png",
        "crab30_rarity == 'e'", "misc/epic_star.png",
        "crab30_rarity == 'l'", "misc/legend_star.png",) 
    )

image crab30_shuffle:
    "crab30_crab1"
    0.4
    "crab30_crab2"
    0.4
    repeat

transform q:
    alpha 0.0 xalign .51 yalign .45
    ease 1 alpha 1.0 yalign .33
    ease 1 alpha 0.0 yalign .31



init:
    $ enemy_opp_name = "shady"
    $ opp_name = "shady"

    $ crab1_level = 2
    $ crab2_level = 2
    $ crab3_level = 2
    $ crab4_level = 2
    $ crab5_level = 2
    $ crab6_level = 2
    $ crab7_level = 2
    $ crab8_level = 2
    $ crab9_level = 2
    $ crab10_level = 2
    $ crab11_level = 2
    $ crab12_level = 2
    $ crab13_level = 2
    $ crab14_level = 2
    $ crab15_level = 2
    $ crab16_level = 2
    $ crab17_level = 2
    $ crab18_level = 2
    $ crab19_level = 2
    $ crab20_level = 2
    $ crab21_level = 2
    $ crab22_level = 2
    $ crab23_level = 2
    $ crab24_level = 2
    $ crab25_level = 2
    $ crab26_level = 2
    $ crab27_level = 2
    $ crab28_level = 2
    $ crab29_level = 2
    $ crab30_level = 2































    $ crab1 = False
    $ crab2 = False
    $ crab3 = False
    $ crab4 = False
    $ crab5 = False
    $ crab6 = False
    $ crab7 = False
    $ crab8 = False
    $ crab9 = False
    $ crab10 = False
    $ crab11 = False
    $ crab12 = False
    $ crab13 = False
    $ crab14 = False
    $ crab15 = False
    $ crab16 = False
    $ crab17 = False
    $ crab18 = False
    $ crab19 = False
    $ crab20 = False
    $ crab21 = False
    $ crab22 = False
    $ crab23 = False
    $ crab24 = False
    $ crab25 = False
    $ crab26 = False
    $ crab27 = False
    $ crab28 = False
    $ crab29 = False
    $ crab30 = False


    $ crab_spot1 = 0
    $ crab_spot2 = 0
    $ crab_spot3 = 0
    $ crab_spot4 = 0
    $ crab_spot5 = 0
    $ crab_spot1_chosen = False
    $ crab_spot2_chosen = False
    $ crab_spot3_chosen = False
    $ crab_spot4_chosen = False
    $ crab_spot5_chosen = False
    $ crab1_name = "bill"

    $ crab2_name = "2"
    $ crab3_name = "3"
    $ crab4_name = "4"
    $ crab5_name = "5"
    $ crab6_name = "6"
    $ crab7_name = "7"
    $ crab8_name = "8"
    $ crab9_name = "9"
    $ crab10_name = "10"
    $ crab11_name = "11"
    $ crab12_name = "12"
    $ crab13_name = "13"
    $ crab14_name = "14"
    $ crab15_name = "15"
    $ crab16_name = "16"
    $ crab17_name = "17"
    $ crab18_name = "18"
    $ crab19_name = "19"
    $ crab20_name = "20"
    $ crab21_name = "21"
    $ crab22_name = "22"
    $ crab23_name = "23"
    $ crab24_name = "24"
    $ crab25_name = "25"
    $ crab26_name = "26"
    $ crab27_name = "27"
    $ crab28_name = "28"
    $ crab29_name = "29"
    $ crab30_name = "30"


    $ enemy_crab_name = "slasher"
    $ enemy_crab_level = 1

    $ crabs_selected = False

    $ crab1_set = False
    $ crab2_set = False
    $ crab3_set = False
    $ crab4_set = False
    $ crab5_set = False
    $ crab6_set = False
    $ crab7_set = False
    $ crab8_set = False
    $ crab9_set = False
    $ crab10_set = False
    $ crab11_set = False
    $ crab12_set = False
    $ crab13_set = False
    $ crab14_set = False
    $ crab15_set = False
    $ crab16_set = False
    $ crab17_set = False
    $ crab18_set = False
    $ crab19_set = False
    $ crab20_set = False
    $ crab21_set = False
    $ crab22_set = False
    $ crab23_set = False
    $ crab24_set = False
    $ crab25_set = False
    $ crab26_set = False
    $ crab27_set = False
    $ crab28_set = False
    $ crab29_set = False
    $ crab30_set = False

    $ crabs_current =0
    $ crabs_total =0

    $ not_happening = False

    $ enemy_crab_health_max = 20
    $ crab_health = 20
    $ crab_max_health = 20
    $ crab1_max_health = 20
    $ crab_standin_health = 20
    $ crab_player_max_health = 40
    $ crab_player_health = 40

    $ arena_xpos_lifebar_player = 390-((crab_player_health*390)/crab_player_max_health)
    $ arena_xpos_lifebar_crab = 390-((crab_standin_health*390)/crab_max_health)
    $ arena_xpos_lifebar_enemy = -(360-((crab_health*360)/enemy_crab_health_max))

    $ crab1_element = "none"
    $ crab2_element = "none"
    $ crab3_element = "none"
    $ crab4_element = "none"
    $ crab5_element = "none"
    $ crab6_element = "none"
    $ crab7_element = "none"
    $ crab8_element = "none"
    $ crab9_element = "none"
    $ crab10_element = "none"
    $ crab11_element = "none"
    $ crab12_element = "none"
    $ crab13_element = "none"
    $ crab14_element = "none"
    $ crab15_element = "none"
    $ crab16_element = "none"
    $ crab17_element = "none"
    $ crab18_element = "none"
    $ crab19_element = "none"
    $ crab20_element = "none"
    $ crab21_element = "none"
    $ crab22_element = "none"
    $ crab23_element = "none"
    $ crab24_element = "none"
    $ crab25_element = "none"
    $ crab26_element = "none"
    $ crab27_element = "none"
    $ crab28_element = "none"
    $ crab29_element = "none"
    $ crab30_element = "none"

    $ crab1_move2 = False
    $ crab1_move3 = False
    $ crab1_move4 = False
    $ crab2_move2 = False
    $ crab2_move3 = False
    $ crab2_move4 = False
    $ crab3_move2 = False
    $ crab3_move3 = False
    $ crab3_move4 = False
    $ crab4_move2 = False
    $ crab4_move3 = False
    $ crab4_move4 = False
    $ crab5_move2 = False
    $ crab5_move3 = False
    $ crab5_move4 = False
    $ crab6_move2 = False
    $ crab6_move3 = False
    $ crab6_move4 = False
    $ crab7_move2 = False
    $ crab7_move3 = False
    $ crab7_move4 = False
    $ crab8_move2 = False
    $ crab8_move3 = False
    $ crab8_move4 = False
    $ crab9_move2 = False
    $ crab9_move3 = False
    $ crab9_move4 = False
    $ crab10_move2 = False
    $ crab10_move3 = False
    $ crab10_move4 = False
    $ crab11_move2 = False
    $ crab11_move3 = False
    $ crab11_move4 = False
    $ crab12_move2 = False
    $ crab12_move3 = False
    $ crab12_move4 = False
    $ crab13_move2 = False
    $ crab13_move3 = False
    $ crab13_move4 = False
    $ crab14_move2 = False
    $ crab14_move3 = False
    $ crab14_move4 = False
    $ crab15_move2 = False
    $ crab15_move3 = False
    $ crab15_move4 = False
    $ crab16_move2 = False
    $ crab16_move3 = False
    $ crab16_move4 = False
    $ crab17_move2 = False
    $ crab17_move3 = False
    $ crab17_move4 = False
    $ crab18_move2 = False
    $ crab18_move3 = False
    $ crab18_move4 = False
    $ crab19_move2 = False
    $ crab19_move3 = False
    $ crab19_move4 = False
    $ crab20_move2 = False
    $ crab20_move3 = False
    $ crab20_move4 = False
    $ crab21_move2 = False
    $ crab21_move3 = False
    $ crab21_move4 = False
    $ crab22_move2 = False
    $ crab22_move3 = False
    $ crab22_move4 = False
    $ crab23_move2 = False
    $ crab23_move3 = False
    $ crab23_move4 = False
    $ crab24_move2 = False
    $ crab24_move3 = False
    $ crab24_move4 = False
    $ crab25_move2 = False
    $ crab25_move3 = False
    $ crab25_move4 = False
    $ crab26_move2 = False
    $ crab26_move3 = False
    $ crab26_move4 = False
    $ crab27_move2 = False
    $ crab27_move3 = False
    $ crab27_move4 = False
    $ crab28_move2 = False
    $ crab28_move3 = False
    $ crab28_move4 = False
    $ crab29_move2 = False
    $ crab29_move3 = False
    $ crab29_move4 = False
    $ crab30_move2 = False
    $ crab30_move3 = False
    $ crab30_move4 = False

    $ crab1_active = False
    $ crab2_active = False
    $ crab3_active = False
    $ crab4_active = False
    $ crab5_active = False
    $ crab6_active = False
    $ crab7_active = False
    $ crab8_active = False
    $ crab9_active = False
    $ crab10_active = False
    $ crab11_active = False
    $ crab12_active = False
    $ crab13_active = False
    $ crab14_active = False
    $ crab15_active = False
    $ crab16_active = False
    $ crab17_active = False
    $ crab18_active = False
    $ crab19_active = False
    $ crab20_active = False
    $ crab21_active = False
    $ crab22_active = False
    $ crab23_active = False
    $ crab24_active = False
    $ crab25_active = False
    $ crab26_active = False
    $ crab27_active = False
    $ crab28_active = False
    $ crab29_active = False
    $ crab30_active = False

    $ arena_active = True
    $ arena_fighting = False

    $ arena_enemy = 1

    $ crab1_exp = False
    $ crab2_exp = False
    $ crab3_exp = False
    $ crab4_exp = False
    $ crab5_exp = False
    $ crab6_exp = False
    $ crab7_exp = False
    $ crab8_exp = False
    $ crab9_exp = False
    $ crab10_exp = False
    $ crab11_exp = False
    $ crab12_exp = False
    $ crab13_exp = False
    $ crab14_exp = False
    $ crab15_exp = False
    $ crab16_exp = False
    $ crab17_exp = False
    $ crab18_exp = False
    $ crab19_exp = False
    $ crab20_exp = False
    $ crab21_exp = False
    $ crab22_exp = False
    $ crab23_exp = False
    $ crab24_exp = False
    $ crab25_exp = False
    $ crab26_exp = False
    $ crab27_exp = False
    $ crab28_exp = False
    $ crab29_exp = False
    $ crab30_exp = False

    $ crab1_total_exp = 0
    $ crab2_total_exp = 0
    $ crab3_total_exp = 0
    $ crab4_total_exp = 0
    $ crab5_total_exp = 0
    $ crab6_total_exp = 0
    $ crab7_total_exp = 0
    $ crab8_total_exp = 0
    $ crab9_total_exp = 0
    $ crab10_total_exp = 0
    $ crab11_total_exp = 0
    $ crab12_total_exp = 0
    $ crab13_total_exp = 0
    $ crab14_total_exp = 0
    $ crab15_total_exp = 0
    $ crab16_total_exp = 0
    $ crab17_total_exp = 0
    $ crab18_total_exp = 0
    $ crab19_total_exp = 0
    $ crab20_total_exp = 0
    $ crab21_total_exp = 0
    $ crab22_total_exp = 0
    $ crab23_total_exp = 0
    $ crab24_total_exp = 0
    $ crab25_total_exp = 0
    $ crab26_total_exp = 0
    $ crab27_total_exp = 0
    $ crab28_total_exp = 0
    $ crab29_total_exp = 0
    $ crab30_total_exp = 0

    $ enemy_move2 = False
    $ enemy_move3 = False
    $ enemy_move4 = False


    $ crab2_type = "0"
    $ crab3_type = "0"
    $ crab4_type = "0"
    $ crab5_type = "0"
    $ crab6_type = "0"
    $ crab7_type = "0"
    $ crab8_type = "0"
    $ crab9_type = "0"
    $ crab10_type = "0"
    $ crab11_type = "0"
    $ crab12_type = "0"
    $ crab13_type = "0"
    $ crab14_type = "0"
    $ crab15_type = "0"
    $ crab16_type = "0"
    $ crab17_type = "0"
    $ crab18_type = "0"
    $ crab19_type = "0"
    $ crab20_type = "0"
    $ crab21_type = "0"
    $ crab22_type = "0"
    $ crab23_type = "0"
    $ crab24_type = "0"
    $ crab25_type = "0"
    $ crab26_type = "0"
    $ crab27_type = "0"
    $ crab28_type = "0"
    $ crab29_type = "0"
    $ crab30_type = "0"

    $ enemy_crab_charge = False
    $ crab_charge = False
    $ crab_hunt = False
    $ ultimate_arena_battle = False

    $ enemy_crab1_type = "0"
    $ enemy_crab2_type = "0"
    $ enemy_crab3_type = "0"
    $ enemy_crab4_type = "0"
    $ enemy_crab5_type = "0"

    $ xloc = 0
    $ yloc = 0
    $ xbound = 9
    $ ybound = 9

    $ arena_direction = "left"
    $ shady_intro = 0
    $ shady_hunt_explain = False

    $ e_poison = 0
    $ e_bind = 0
    $ e_confuse = 0
    $ e_weak = 0
    $ a_poison = 0
    $ a_bind = 0
    $ a_confuse = 0
    $ a_weak = 0
    $ bind_chance = 0
    $ confusion_chance = 0

    $ deck_crabs = 0

    $ arena_potion = 0
    $ cureall = 0
    $ crapples = 0
    $ arena_pocket = 0

    $ pixellate = Pixellate(2, 20)

    $ crab1_hp = 0
    $ crab2_hp = 0
    $ crab3_hp = 0
    $ crab4_hp = 0
    $ crab5_hp = 0
    $ crab6_hp = 0
    $ crab7_hp = 0
    $ crab8_hp = 0
    $ crab9_hp = 0
    $ crab10_hp = 0
    $ crab11_hp = 0
    $ crab12_hp = 0
    $ crab13_hp = 0
    $ crab14_hp = 0
    $ crab15_hp = 0
    $ crab16_hp = 0
    $ crab17_hp = 0
    $ crab18_hp = 0
    $ crab19_hp = 0
    $ crab20_hp = 0
    $ crab21_hp = 0
    $ crab22_hp = 0
    $ crab23_hp = 0
    $ crab24_hp = 0
    $ crab25_hp = 0
    $ crab26_hp = 0
    $ crab27_hp = 0
    $ crab28_hp = 0
    $ crab29_hp = 0
    $ crab30_hp = 0

    $ crab1_temp_hp = crab1_hp
    $ crab2_temp_hp = crab2_hp
    $ crab3_temp_hp = crab3_hp
    $ crab4_temp_hp = crab4_hp
    $ crab5_temp_hp = crab5_hp
    $ crab6_temp_hp = crab6_hp
    $ crab7_temp_hp = crab7_hp
    $ crab8_temp_hp = crab8_hp
    $ crab9_temp_hp = crab9_hp
    $ crab10_temp_hp = crab10_hp
    $ crab11_temp_hp = crab11_hp
    $ crab12_temp_hp = crab12_hp
    $ crab13_temp_hp = crab13_hp
    $ crab14_temp_hp = crab14_hp
    $ crab15_temp_hp = crab15_hp
    $ crab16_temp_hp = crab16_hp
    $ crab17_temp_hp = crab17_hp
    $ crab18_temp_hp = crab18_hp
    $ crab19_temp_hp = crab19_hp
    $ crab20_temp_hp = crab20_hp
    $ crab21_temp_hp = crab21_hp
    $ crab22_temp_hp = crab22_hp
    $ crab23_temp_hp = crab23_hp
    $ crab24_temp_hp = crab24_hp
    $ crab25_temp_hp = crab25_hp
    $ crab26_temp_hp = crab26_hp
    $ crab27_temp_hp = crab27_hp
    $ crab28_temp_hp = crab28_hp
    $ crab29_temp_hp = crab29_hp
    $ crab30_temp_hp = crab30_hp

init -2 python:
    class Coordinate:
        def __init__(self,x,y,xmin,ymin,xmax,ymax):
            
            self.x,self.y,self.xmin,self.ymin,self.xmax,self.ymax=x,y,xmin,ymin,xmax,ymax
            
            self.xoffset,self.yoffset=0,0
            return
        
        def transform(self,d,show_time,animate_time):
            
            self.x+=self.xoffset
            self.y+=self.yoffset
            self.xoffset,self.yoffset=0,0
            
            if self.x<self.xmin:
                self.x=self.xmin
            if self.y<self.ymin:
                self.y=self.ymin
            if self.x>self.xmax:
                self.x=self.xmax
            if self.y>self.ymax:
                self.y=self.ymax
            
            d.pos=(self.x,self.y)
            
            return 0
    tiny_dude1_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)


image tiny_dude1 loc = ConditionSwitch(
    "arena_direction == 'left'", "misc/tiny_dude1.png",
    "arena_direction == 'right'", "misc/tiny_dude2.png",
    "True", "misc/tiny_dude1.png",)


screen tiny_dude1_cage:
    add "misc/arena_walls.png"

    add "misc/grass1.png"

    add "misc/tiny_girl.png":
        xpos 750 ypos 150

    add "tiny_dude1 loc" anchor (0.5,0.5) at Transform(function=tiny_dude1_coordinate.transform)

    key "focus_left" action If(xloc<xbound, 
            true=[SetField(tiny_dude1_coordinate,"xoffset",-0.05), SetVariable('xloc', xloc+1), SetVariable('arena_direction', "left"), Return()],
                false=NullAction())

    key "focus_right" action If(xloc>(-xbound), 
        true=[SetField(tiny_dude1_coordinate,"xoffset", +0.05), SetVariable('xloc', xloc-1), SetVariable('arena_direction', "right"), Return()],
            false=NullAction())

    key "focus_down" action If(yloc>(-ybound), 
        true=[SetField(tiny_dude1_coordinate,"yoffset",+0.05), SetVariable('yloc', yloc-1), Return()],
            false=NullAction())

    key "focus_up" action If(yloc<ybound, 
        true=[SetField(tiny_dude1_coordinate,"yoffset",-0.05), SetVariable('yloc', yloc+1), Return()],
            false=NullAction())



    textbutton "return" action Jump("begin_stuff"):
        xpos 05 ypos 05



screen tiny_dude1_cage2:
    add "misc/tiny_anka.png":
        xpos 750 ypos 150

    add "misc/arena_walls2.png"

    add "misc/grass1.png"

    add "tiny_dude1 loc" anchor (0.5,0.5) at Transform(function=tiny_dude1_coordinate.transform)

    key "focus_left" action If(xloc<xbound, 
            true=[SetField(tiny_dude1_coordinate,"xoffset",-0.05), SetVariable('xloc', xloc+1), SetVariable('arena_direction', "left"), Return()],
                false=NullAction())

    key "focus_right" action If(xloc>(-xbound), 
        true=[SetField(tiny_dude1_coordinate,"xoffset", +0.05), SetVariable('xloc', xloc-1), SetVariable('arena_direction', "right"), Return()],
            false=NullAction())

    key "focus_down" action If(yloc>(-ybound), 
        true=[SetField(tiny_dude1_coordinate,"yoffset",+0.05), SetVariable('yloc', yloc-1), Return()],
            false=NullAction())

    key "focus_up" action If(yloc<ybound, 
        true=[SetField(tiny_dude1_coordinate,"yoffset",-0.05), SetVariable('yloc', yloc+1), Return()],
            false=NullAction())



    textbutton "return" action Jump("begin_stuff"):
        xpos 05 ypos 05

label bk3_arena_start_shit:

    if crab1:
        if crab1_rarity == "1":
            $ crab1_rarity = "n"
        if crab1_rarity == "2":
            $ crab1_rarity = "r"
        if crab1_rarity == "3":
            $ crab1_rarity = "e"
        if crab1_rarity == "4":
            $ crab1_rarity = "l"
    if crab2:
        if crab2_rarity == "1":
            $ crab2_rarity = "n"
        if crab2_rarity == "2":
            $ crab2_rarity = "r"
        if crab2_rarity == "3":
            $ crab2_rarity = "e"
        if crab2_rarity == "4":
            $ crab2_rarity = "l"
    if crab3:
        if crab3_rarity == "1":
            $ crab3_rarity = "n"
        if crab3_rarity == "2":
            $ crab3_rarity = "r"
        if crab3_rarity == "3":
            $ crab3_rarity = "e"
        if crab3_rarity == "4":
            $ crab3_rarity = "l"
    if crab4:
        if crab4_rarity == "1":
            $ crab4_rarity = "n"
        if crab4_rarity == "2":
            $ crab4_rarity = "r"
        if crab4_rarity == "3":
            $ crab4_rarity = "e"
        if crab4_rarity == "4":
            $ crab4_rarity = "l"
    if crab5:
        if crab5_rarity == "1":
            $ crab5_rarity = "n"
        if crab5_rarity == "2":
            $ crab5_rarity = "r"
        if crab5_rarity == "3":
            $ crab5_rarity = "e"
        if crab5_rarity == "4":
            $ crab5_rarity = "l"
    if crab6:
        if crab6_rarity == "1":
            $ crab6_rarity = "n"
        if crab6_rarity == "2":
            $ crab6_rarity = "r"
        if crab6_rarity == "3":
            $ crab6_rarity = "e"
        if crab6_rarity == "4":
            $ crab6_rarity = "l"
    if crab7:
        if crab7_rarity == "1":
            $ crab7_rarity = "n"
        if crab7_rarity == "2":
            $ crab7_rarity = "r"
        if crab7_rarity == "3":
            $ crab7_rarity = "e"
        if crab7_rarity == "4":
            $ crab7_rarity = "l"
    if crab8:
        if crab8_rarity == "1":
            $ crab8_rarity = "n"
        if crab8_rarity == "2":
            $ crab8_rarity = "r"
        if crab8_rarity == "3":
            $ crab8_rarity = "e"
        if crab8_rarity == "4":
            $ crab8_rarity = "l"
    if crab9:
        if crab9_rarity == "1":
            $ crab9_rarity = "n"
        if crab9_rarity == "2":
            $ crab9_rarity = "r"
        if crab9_rarity == "3":
            $ crab9_rarity = "e"
        if crab9_rarity == "4":
            $ crab9_rarity = "l"
    if crab10:
        if crab10_rarity == "1":
            $ crab10_rarity = "n"
        if crab10_rarity == "2":
            $ crab10_rarity = "r"
        if crab10_rarity == "3":
            $ crab10_rarity = "e"
        if crab10_rarity == "4":
            $ crab10_rarity = "l"
    if crab11:
        if crab11_rarity == "1":
            $ crab11_rarity = "n"
        if crab11_rarity == "2":
            $ crab11_rarity = "r"
        if crab11_rarity == "3":
            $ crab11_rarity = "e"
        if crab11_rarity == "4":
            $ crab11_rarity = "l"
    if crab12:
        if crab12_rarity == "1":
            $ crab12_rarity = "n"
        if crab12_rarity == "2":
            $ crab12_rarity = "r"
        if crab12_rarity == "3":
            $ crab12_rarity = "e"
        if crab12_rarity == "4":
            $ crab12_rarity = "l"
    if crab13:
        if crab13_rarity == "1":
            $ crab13_rarity = "n"
        if crab13_rarity == "2":
            $ crab13_rarity = "r"
        if crab13_rarity == "3":
            $ crab13_rarity = "e"
        if crab13_rarity == "4":
            $ crab13_rarity = "l"
    if crab14:
        if crab14_rarity == "1":
            $ crab14_rarity = "n"
        if crab14_rarity == "2":
            $ crab14_rarity = "r"
        if crab14_rarity == "3":
            $ crab14_rarity = "e"
        if crab14_rarity == "4":
            $ crab14_rarity = "l"
    if crab15:
        if crab15_rarity == "1":
            $ crab15_rarity = "n"
        if crab15_rarity == "2":
            $ crab15_rarity = "r"
        if crab15_rarity == "3":
            $ crab15_rarity = "e"
        if crab15_rarity == "4":
            $ crab15_rarity = "l"
    if crab16:
        if crab16_rarity == "1":
            $ crab16_rarity = "n"
        if crab16_rarity == "2":
            $ crab16_rarity = "r"
        if crab16_rarity == "3":
            $ crab16_rarity = "e"
        if crab16_rarity == "4":
            $ crab16_rarity = "l"
    if crab17:
        if crab17_rarity == "1":
            $ crab17_rarity = "n"
        if crab17_rarity == "2":
            $ crab17_rarity = "r"
        if crab17_rarity == "3":
            $ crab17_rarity = "e"
        if crab17_rarity == "4":
            $ crab17_rarity = "l"
    if crab18:
        if crab18_rarity == "1":
            $ crab18_rarity = "n"
        if crab18_rarity == "2":
            $ crab18_rarity = "r"
        if crab18_rarity == "3":
            $ crab18_rarity = "e"
        if crab18_rarity == "4":
            $ crab18_rarity = "l"
    if crab19:
        if crab19_rarity == "1":
            $ crab19_rarity = "n"
        if crab19_rarity == "2":
            $ crab19_rarity = "r"
        if crab19_rarity == "3":
            $ crab19_rarity = "e"
        if crab19_rarity == "4":
            $ crab19_rarity = "l"
    if crab20:
        if crab20_rarity == "1":
            $ crab20_rarity = "n"
        if crab20_rarity == "2":
            $ crab20_rarity = "r"
        if crab20_rarity == "3":
            $ crab20_rarity = "e"
        if crab20_rarity == "4":
            $ crab20_rarity = "l"
    if crab21:
        if crab21_rarity == "1":
            $ crab21_rarity = "n"
        if crab21_rarity == "2":
            $ crab21_rarity = "r"
        if crab21_rarity == "3":
            $ crab21_rarity = "e"
        if crab21_rarity == "4":
            $ crab21_rarity = "l"
    if crab22:
        if crab22_rarity == "1":
            $ crab22_rarity = "n"
        if crab22_rarity == "2":
            $ crab22_rarity = "r"
        if crab22_rarity == "3":
            $ crab22_rarity = "e"
        if crab22_rarity == "4":
            $ crab22_rarity = "l"
    if crab23:
        if crab23_rarity == "1":
            $ crab23_rarity = "n"
        if crab23_rarity == "2":
            $ crab23_rarity = "r"
        if crab23_rarity == "3":
            $ crab23_rarity = "e"
        if crab23_rarity == "4":
            $ crab23_rarity = "l"
    if crab24:
        if crab24_rarity == "1":
            $ crab24_rarity = "n"
        if crab24_rarity == "2":
            $ crab24_rarity = "r"
        if crab24_rarity == "3":
            $ crab24_rarity = "e"
        if crab24_rarity == "4":
            $ crab24_rarity = "l"
    if crab25:
        if crab25_rarity == "1":
            $ crab25_rarity = "n"
        if crab25_rarity == "2":
            $ crab25_rarity = "r"
        if crab25_rarity == "3":
            $ crab25_rarity = "e"
        if crab25_rarity == "4":
            $ crab25_rarity = "l"
    if crab26:
        if crab26_rarity == "1":
            $ crab26_rarity = "n"
        if crab26_rarity == "2":
            $ crab26_rarity = "r"
        if crab26_rarity == "3":
            $ crab26_rarity = "e"
        if crab26_rarity == "4":
            $ crab26_rarity = "l"
    if crab27:
        if crab27_rarity == "1":
            $ crab27_rarity = "n"
        if crab27_rarity == "2":
            $ crab27_rarity = "r"
        if crab27_rarity == "3":
            $ crab27_rarity = "e"
        if crab27_rarity == "4":
            $ crab27_rarity = "l"
    if crab28:
        if crab28_rarity == "1":
            $ crab28_rarity = "n"
        if crab28_rarity == "2":
            $ crab28_rarity = "r"
        if crab28_rarity == "3":
            $ crab28_rarity = "e"
        if crab28_rarity == "4":
            $ crab28_rarity = "l"
    if crab29:
        if crab29_rarity == "1":
            $ crab29_rarity = "n"
        if crab29_rarity == "2":
            $ crab29_rarity = "r"
        if crab29_rarity == "3":
            $ crab29_rarity = "e"
        if crab29_rarity == "4":
            $ crab29_rarity = "l"
    if crab30:
        if crab30_rarity == "1":
            $ crab30_rarity = "n"
        if crab30_rarity == "2":
            $ crab30_rarity = "r"
        if crab30_rarity == "3":
            $ crab30_rarity = "e"
        if crab30_rarity == "4":
            $ crab30_rarity = "l"

    if iroh_fun_battle:
        jump crab_battle_menu

    jump begin_stuff

label begin_stuff:
    $ tiny_dude1_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)
    $ xloc = 0
    $ yloc = 0
    hide crab1_shuffle
    hide crab2_shuffle
    hide crab3_shuffle
    hide crab4_shuffle
    hide crab5_shuffle
    hide crab6_shuffle
    hide crab7_shuffle
    hide crab8_shuffle
    hide crab9_shuffle
    hide crab10_shuffle
    hide crab11_shuffle
    hide crab12_shuffle
    hide crab13_shuffle
    hide crab14_shuffle
    hide crab15_shuffle
    hide crab16_shuffle
    hide crab17_shuffle
    hide crab18_shuffle
    hide crab19_shuffle
    hide crab20_shuffle
    hide crab21_shuffle
    hide crab22_shuffle
    hide crab23_shuffle
    hide crab24_shuffle
    hide crab25_shuffle
    hide crab26_shuffle
    hide crab27_shuffle
    hide crab28_shuffle
    hide crab29_shuffle
    hide crab30_shuffle

    hide screen earth_money_date

    if suki_tylee >=5 and not love_bk3_map:
        if shady_obsidian and shop_building <3:
            show shadyguy_grin with dissolve
            sg "you should really go upgrade the shop, my man."
            hide shadyguy_grin with dissolve

        if shop_building ==3 and not love_bk3_map:
            if shady_battle_talk and first_arena_fought:
                sg "......"
                sg "okay!"
                sg "here you go!"
                play sound "audio/win2.mp3"
                $ jd_map = True
                show map_dungeonentry with dissolve
                "you got a dungeon map!"
                y "wow this would have been helpful in the beginning."
                sg "that's not how mazes work in games!"
                sg "you get the map after you go through all the stuff."
                y "no, i get it."
                y "i'm just saying."
                show ctc
                pause
                hide ctc
                hide map_dungeonentry with dissolve
                sg "good luck."
                $ love_bk3_map = True
                $ bk3_jd_dungeon = True
                jump love_basingse_day1

            if shady_battle_talk and not first_arena_fought:
                show shadyguy_grin with dissolve
                sg "come on, man - just a quick game and you'll get your map!"
                hide shadyguy_grin with dissolve
            else:

                show shadyguy_grin with dissolve
                sg "hey buddy!"
                sg "thanks for upgrading the shop!"
                y "it's fine, it was easy."
                y "now about that map..."
                sg "right."
                sg "well..."
                if not first_arena_fought:
                    sg "one more thing."
                    y "....are you fucking serious?"
                    sg "relax, it's quick and easy."
                    sg "like me."
                    sg "heh."
                    y "what is it?"
                    sg "you gotta play one game of pocket crabs with me."
                    sg "doesn't matter who wins."
                    sg "play a quick round and you can get your map and be on your way."
                    y "alright, let's do it."
                    $ shady_battle_talk = True
                else:
                    $ shady_battle_talk = True
                    sg "......"
                    sg "okay!"
                    sg "here you go!"
                    play sound "audio/win2.mp3"
                    $ jd_map = True
                    show map_dungeonentry with dissolve
                    "you got a dungeon map!"
                    y "wow this would have been helpful in the beginning."
                    sg "that's not how mazes work in games!"
                    sg "you get the map after you go through all the stuff."
                    y "no, i get it."
                    y "i'm just saying."
                    show ctc
                    pause
                    hide ctc
                    hide map_dungeonentry with dissolve
                    sg "good luck."
                    $ love_bk3_map = True
                    $ bk3_jd_dungeon = True
                    jump love_basingse_day1

        if not shady_obsidian:
            $ shady_obsidian = True
            show shadyguy_grin with dissolve
            sg "howdy."
            y "hey man, do you have a map of the tunnels beneath lake laogai?"
            sg "i might..."
            y "i don't have time for that."
            y "do you or don't you?"
            sg "...i do."
            y "great, can i have it?"
            sg "........"
            sg "................."
            sg "fully upgrade the shop and you've got it."
            y "damn it, really?"
            sg "yeah."
            sg "but i'll make your life a little easier."
            sg "here."
            play sound "audio/win2.mp3"
            $ obsidian +=1
            "you got 1 obsidian!"
            y "....."
            y "how long have you had this?"
            sg "what, obsidian?"
            sg "got tons of it."
            sg "honestly don't know what to do with it all."
            y "....i fucking hate you."
            sg "aw."
            sg "go upgrade the shop and come back."
            y "fine."
            jump love_basingse_day1


    $ crab_hunt = False
    $ crab_hunt2 = False
    if shady_intro == 0:
        show shadyguy_grin with dissolve
        sg "alright, let's get started."
        sg "you can check stats/deposit/withdraw/release/set up your arsenal by going to \"manage your crabs\"."
        sg "or hunt for wild crabs that you can grind or catch by clicking \"hunt wild crabs\"."
        sg "you can also battle trainers for crapples and... other... rewards by clicking \"battle!\"."
        sg "each crab has it's own strengths and weaknesses, and the rarer the crab, the more powerful."
        sg "there are also elemental bonuses: fire>water>earth>fire, and air is neutral."
        sg "as your crabs get stronger, they'll automatically learn new moves."
        sg "good luck, bro."
        $ shady_intro = 3
        hide shadyguy_grin with dissolve

    menu:
        "manage your crabs" if crab1:
            jump crab_manager

            label crab_manager:
                menu:
                    "tutorial":
                        show shadyguy_grin with dissolve
                        sg "alright, let's walk through it."
                        sg "what do you wanna know about?"
                        jump tutorial_menu

                        label tutorial_menu:
                            menu:
                                "tell me about..."
                                "getting and carrying crabs":

                                    sg "you can capture crabs in \"wild crab blast\" or buy them using crapples."
                                    sg "you get crapples by winning trainer matches."
                                    sg "when you get a crab, they automatically go into storage, so you'll have to withdraw them before you can use them."
                                    sg "you can only carry 5 crabs at a time, so if you wanna switch, you'll need to deposit one first."
                                    jump tutorial_menu
                                "removing crabs":
                                    sg "you can only have 30 crabs total."
                                    sg "if you want to get more, you'll need to release previous ones."
                                    jump tutorial_menu
                                "element advantages":
                                    sg "fire is effective against water, water is effective against earth, earth is effective against fire."
                                    sg "air has no advantage, but not weakness either."
                                    jump tutorial_menu
                                "rarities":
                                    sg "there are four rarity levels - normal, rare, epic, and legendary."
                                    sg "legendary crabs must be evolved from epic crabs, there is no other way to get them."
                                    jump tutorial_menu
                                "leveling up":
                                    sg "your crabs will level up as they gain experience defeating or catching crabs."
                                    sg "wild crab blast is the best way to level up, especially in the beginning."
                                    sg "you can level up multiple crabs per battle by sending them out to fight and recalling them."
                                    sg "defeating (or catching) higher rarities give more experience than lower rarities."
                                    sg "catching a crab will give half of the experience that defeating it would give."
                                    jump tutorial_menu
                                "wild crab blast":
                                    sg "battle and capture wild crabs here."
                                    sg "Crabs of various levels and rarity hide in the grass."
                                    sg "you can defeat crabs for experience, or capture them for half the experience."
                                    jump tutorial_menu
                                "crabble royale":
                                    sg "this is where you'll battle trainers."
                                    sg "mostly me, especially at first."
                                    sg "as you win fights, they'll get more difficult."
                                    sg "you can win crapples here."
                                    jump tutorial_menu
                                "items":
                                    sg "you can use pockets to capture crabs."
                                    sg "some items cure status effects, of which there are four: poison, confusion, weak, and bind."
                                    jump tutorial_menu
                                "status effects":
                                    sg "status effects hit the whole team, but only hurt the {b}active crab{/b}, so switching won't help."
                                    sg "there are four status effects: poison, confusion, weak, and bind."
                                    sg "they each last for 3 turns."
                                    sg "poison hurts the active crab at the start of its turn."
                                    sg "confusion might make the active crab hurt itself, but it might not."
                                    sg "weak makes the active crab only use their standard attack; they won't be able to use special attacks."
                                    sg "bind might prevent the active crab from attacking."
                                    jump tutorial_menu
                                "exit":
                                    hide shadyguy_grin with dissolve
                                    jump crab_manager
                    "crab stats":

                        jump crab_stats_page1

                        label crab_stats_page1:
                            hide screen crabs_stats
                            $ crab1_stat_select = False
                            $ crab2_stat_select = False
                            $ crab3_stat_select = False
                            $ crab4_stat_select = False
                            $ crab5_stat_select = False
                            $ crab6_stat_select = False
                            $ crab7_stat_select = False
                            $ crab8_stat_select = False
                            $ crab9_stat_select = False
                            $ crab10_stat_select = False
                            $ crab11_stat_select = False
                            $ crab12_stat_select = False
                            $ crab13_stat_select = False
                            $ crab14_stat_select = False
                            $ crab15_stat_select = False
                            $ crab16_stat_select = False
                            $ crab17_stat_select = False
                            $ crab18_stat_select = False
                            $ crab19_stat_select = False
                            $ crab20_stat_select = False
                            $ crab21_stat_select = False
                            $ crab22_stat_select = False
                            $ crab23_stat_select = False
                            $ crab24_stat_select = False
                            $ crab25_stat_select = False
                            $ crab26_stat_select = False
                            $ crab27_stat_select = False
                            $ crab28_stat_select = False
                            $ crab29_stat_select = False
                            $ crab30_stat_select = False


                            menu:
                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab1:
                                    $ crab1_stat_select = True
                                    $ crab_stat_name = crab1_name
                                    $ crab_stat_level = crab1_level
                                    $ crab_stat_hp = crab1_hp
                                    $ crab_stat_att = crab1_att
                                    $ crab_stat_def = crab1_def
                                    $ crab_stat_acc = crab1_acc

                                    $ crab_stat_type = crab1_type
                                    $ crab_stat_move2 = crab1_move2
                                    $ crab_stat_move3 = crab1_move3
                                    $ crab_stat_move4 = crab1_move4
                                    $ crab_stat_element = crab1_element
                                    if crab1_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab1_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab1_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab1_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab2:
                                    $ crab2_stat_select = True
                                    $ crab_stat_name = crab2_name
                                    $ crab_stat_level = crab2_level
                                    $ crab_stat_hp = crab2_hp
                                    $ crab_stat_att = crab2_att
                                    $ crab_stat_def = crab2_def
                                    $ crab_stat_acc = crab2_acc

                                    $ crab_stat_type = crab2_type
                                    $ crab_stat_move2 = crab2_move2
                                    $ crab_stat_move3 = crab2_move3
                                    $ crab_stat_move4 = crab2_move4
                                    $ crab_stat_element = crab2_element
                                    if crab2_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab2_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab2_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab2_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab3:
                                    $ crab3_stat_select = True
                                    $ crab_stat_name = crab3_name
                                    $ crab_stat_level = crab3_level
                                    $ crab_stat_hp = crab3_hp
                                    $ crab_stat_att = crab3_att
                                    $ crab_stat_def = crab3_def
                                    $ crab_stat_acc = crab3_acc

                                    $ crab_stat_type = crab3_type
                                    $ crab_stat_move2 = crab3_move2
                                    $ crab_stat_move3 = crab3_move3
                                    $ crab_stat_move4 = crab3_move4
                                    $ crab_stat_element = crab3_element
                                    if crab3_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab3_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab3_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab3_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab4:
                                    $ crab4_stat_select = True
                                    $ crab_stat_name = crab4_name
                                    $ crab_stat_level = crab4_level
                                    $ crab_stat_hp = crab4_hp
                                    $ crab_stat_att = crab4_att
                                    $ crab_stat_def = crab4_def
                                    $ crab_stat_acc = crab4_acc

                                    $ crab_stat_type = crab4_type
                                    $ crab_stat_move2 = crab4_move2
                                    $ crab_stat_move3 = crab4_move3
                                    $ crab_stat_move4 = crab4_move4
                                    $ crab_stat_element = crab4_element
                                    if crab4_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab4_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab4_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab4_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab5:
                                    $ crab5_stat_select = True
                                    $ crab_stat_name = crab5_name
                                    $ crab_stat_level = crab5_level
                                    $ crab_stat_hp = crab5_hp
                                    $ crab_stat_att = crab5_att
                                    $ crab_stat_def = crab5_def
                                    $ crab_stat_acc = crab5_acc

                                    $ crab_stat_type = crab5_type
                                    $ crab_stat_move2 = crab5_move2
                                    $ crab_stat_move3 = crab5_move3
                                    $ crab_stat_move4 = crab5_move4
                                    $ crab_stat_element = crab5_element
                                    if crab5_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab5_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab5_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab5_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab6:
                                    $ crab6_stat_select = True
                                    $ crab_stat_name = crab6_name
                                    $ crab_stat_level = crab6_level
                                    $ crab_stat_hp = crab6_hp
                                    $ crab_stat_att = crab6_att
                                    $ crab_stat_def = crab6_def
                                    $ crab_stat_acc = crab6_acc

                                    $ crab_stat_type = crab6_type
                                    $ crab_stat_move2 = crab6_move2
                                    $ crab_stat_move3 = crab6_move3
                                    $ crab_stat_move4 = crab6_move4
                                    $ crab_stat_element = crab6_element
                                    if crab6_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab6_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab6_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab6_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab7:
                                    $ crab7_stat_select = True
                                    $ crab_stat_name = crab7_name
                                    $ crab_stat_level = crab7_level
                                    $ crab_stat_hp = crab7_hp
                                    $ crab_stat_att = crab7_att
                                    $ crab_stat_def = crab7_def
                                    $ crab_stat_acc = crab7_acc

                                    $ crab_stat_type = crab7_type
                                    $ crab_stat_move2 = crab7_move2
                                    $ crab_stat_move3 = crab7_move3
                                    $ crab_stat_move4 = crab7_move4
                                    $ crab_stat_element = crab7_element
                                    if crab7_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab7_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab7_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab7_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab8:
                                    $ crab8_stat_select = True
                                    $ crab_stat_name = crab8_name
                                    $ crab_stat_level = crab8_level
                                    $ crab_stat_hp = crab8_hp
                                    $ crab_stat_att = crab8_att
                                    $ crab_stat_def = crab8_def
                                    $ crab_stat_acc = crab8_acc

                                    $ crab_stat_type = crab8_type
                                    $ crab_stat_move2 = crab8_move2
                                    $ crab_stat_move3 = crab8_move3
                                    $ crab_stat_move4 = crab8_move4
                                    $ crab_stat_element = crab8_element
                                    if crab8_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab8_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab8_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab8_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab9:
                                    $ crab9_stat_select = True
                                    $ crab_stat_name = crab9_name
                                    $ crab_stat_level = crab9_level
                                    $ crab_stat_hp = crab9_hp
                                    $ crab_stat_att = crab9_att
                                    $ crab_stat_def = crab9_def
                                    $ crab_stat_acc = crab9_acc

                                    $ crab_stat_type = crab9_type
                                    $ crab_stat_move2 = crab9_move2
                                    $ crab_stat_move3 = crab9_move3
                                    $ crab_stat_move4 = crab9_move4
                                    $ crab_stat_element = crab9_element
                                    if crab9_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab9_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab9_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab9_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab10:
                                    $ crab10_stat_select = True
                                    $ crab_stat_name = crab10_name
                                    $ crab_stat_level = crab10_level
                                    $ crab_stat_hp = crab10_hp
                                    $ crab_stat_att = crab10_att
                                    $ crab_stat_def = crab10_def
                                    $ crab_stat_acc = crab10_acc

                                    $ crab_stat_type = crab10_type
                                    $ crab_stat_move2 = crab10_move2
                                    $ crab_stat_move3 = crab10_move3
                                    $ crab_stat_move4 = crab10_move4
                                    $ crab_stat_element = crab10_element
                                    if crab10_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab10_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab10_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab10_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab11:
                                    $ crab11_stat_select = True
                                    $ crab_stat_name = crab11_name
                                    $ crab_stat_level = crab11_level
                                    $ crab_stat_hp = crab11_hp
                                    $ crab_stat_att = crab11_att
                                    $ crab_stat_def = crab11_def
                                    $ crab_stat_acc = crab11_acc

                                    $ crab_stat_type = crab11_type
                                    $ crab_stat_move2 = crab11_move2
                                    $ crab_stat_move3 = crab11_move3
                                    $ crab_stat_move4 = crab11_move4
                                    $ crab_stat_element = crab11_element
                                    if crab11_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab11_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab11_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab11_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab12:
                                    $ crab12_stat_select = True
                                    $ crab_stat_name = crab12_name
                                    $ crab_stat_level = crab12_level
                                    $ crab_stat_hp = crab12_hp
                                    $ crab_stat_att = crab12_att
                                    $ crab_stat_def = crab12_def
                                    $ crab_stat_acc = crab12_acc

                                    $ crab_stat_type = crab12_type
                                    $ crab_stat_move2 = crab12_move2
                                    $ crab_stat_move3 = crab12_move3
                                    $ crab_stat_move4 = crab12_move4
                                    $ crab_stat_element = crab12_element
                                    if crab12_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab12_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab12_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab12_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab13:
                                    $ crab13_stat_select = True
                                    $ crab_stat_name = crab13_name
                                    $ crab_stat_level = crab13_level
                                    $ crab_stat_hp = crab13_hp
                                    $ crab_stat_att = crab13_att
                                    $ crab_stat_def = crab13_def
                                    $ crab_stat_acc = crab13_acc

                                    $ crab_stat_type = crab13_type
                                    $ crab_stat_move2 = crab13_move2
                                    $ crab_stat_move3 = crab13_move3
                                    $ crab_stat_move4 = crab13_move4
                                    $ crab_stat_element = crab13_element
                                    if crab13_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab13_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab13_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab13_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab14:
                                    $ crab14_stat_select = True
                                    $ crab_stat_name = crab14_name
                                    $ crab_stat_level = crab14_level
                                    $ crab_stat_hp = crab14_hp
                                    $ crab_stat_att = crab14_att
                                    $ crab_stat_def = crab14_def
                                    $ crab_stat_acc = crab14_acc

                                    $ crab_stat_type = crab14_type
                                    $ crab_stat_move2 = crab14_move2
                                    $ crab_stat_move3 = crab14_move3
                                    $ crab_stat_move4 = crab14_move4
                                    $ crab_stat_element = crab14_element
                                    if crab14_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab14_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab14_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab14_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab15:
                                    $ crab15_stat_select = True
                                    $ crab_stat_name = crab15_name
                                    $ crab_stat_level = crab15_level
                                    $ crab_stat_hp = crab15_hp
                                    $ crab_stat_att = crab15_att
                                    $ crab_stat_def = crab15_def
                                    $ crab_stat_acc = crab15_acc

                                    $ crab_stat_type = crab15_type
                                    $ crab_stat_move2 = crab15_move2
                                    $ crab_stat_move3 = crab15_move3
                                    $ crab_stat_move4 = crab15_move4
                                    $ crab_stat_element = crab15_element
                                    if crab15_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab15_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab15_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab15_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab16:
                                    $ crab16_stat_select = True
                                    $ crab_stat_name = crab16_name
                                    $ crab_stat_level = crab16_level
                                    $ crab_stat_hp = crab16_hp
                                    $ crab_stat_att = crab16_att
                                    $ crab_stat_def = crab16_def
                                    $ crab_stat_acc = crab16_acc

                                    $ crab_stat_type = crab16_type
                                    $ crab_stat_move2 = crab16_move2
                                    $ crab_stat_move3 = crab16_move3
                                    $ crab_stat_move4 = crab16_move4
                                    $ crab_stat_element = crab16_element
                                    if crab16_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab16_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab16_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab16_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab17:
                                    $ crab17_stat_select = True
                                    $ crab_stat_name = crab17_name
                                    $ crab_stat_level = crab17_level
                                    $ crab_stat_hp = crab17_hp
                                    $ crab_stat_att = crab17_att
                                    $ crab_stat_def = crab17_def
                                    $ crab_stat_acc = crab17_acc

                                    $ crab_stat_type = crab17_type
                                    $ crab_stat_move2 = crab17_move2
                                    $ crab_stat_move3 = crab17_move3
                                    $ crab_stat_move4 = crab17_move4
                                    $ crab_stat_element = crab17_element
                                    if crab17_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab17_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab17_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab17_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab18:
                                    $ crab18_stat_select = True
                                    $ crab_stat_name = crab18_name
                                    $ crab_stat_level = crab18_level
                                    $ crab_stat_hp = crab18_hp
                                    $ crab_stat_att = crab18_att
                                    $ crab_stat_def = crab18_def
                                    $ crab_stat_acc = crab18_acc

                                    $ crab_stat_type = crab18_type
                                    $ crab_stat_move2 = crab18_move2
                                    $ crab_stat_move3 = crab18_move3
                                    $ crab_stat_move4 = crab18_move4
                                    $ crab_stat_element = crab18_element
                                    if crab18_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab18_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab18_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab18_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab19:
                                    $ crab19_stat_select = True
                                    $ crab_stat_name = crab19_name
                                    $ crab_stat_level = crab19_level
                                    $ crab_stat_hp = crab19_hp
                                    $ crab_stat_att = crab19_att
                                    $ crab_stat_def = crab19_def
                                    $ crab_stat_acc = crab19_acc

                                    $ crab_stat_type = crab19_type
                                    $ crab_stat_move2 = crab19_move2
                                    $ crab_stat_move3 = crab19_move3
                                    $ crab_stat_move4 = crab19_move4
                                    $ crab_stat_element = crab19_element
                                    if crab19_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab19_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab19_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab19_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab20:
                                    $ crab20_stat_select = True
                                    $ crab_stat_name = crab20_name
                                    $ crab_stat_level = crab20_level
                                    $ crab_stat_hp = crab20_hp
                                    $ crab_stat_att = crab20_att
                                    $ crab_stat_def = crab20_def
                                    $ crab_stat_acc = crab20_acc

                                    $ crab_stat_type = crab20_type
                                    $ crab_stat_move2 = crab20_move2
                                    $ crab_stat_move3 = crab20_move3
                                    $ crab_stat_move4 = crab20_move4
                                    $ crab_stat_element = crab20_element
                                    if crab20_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab20_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab20_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab20_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab21:
                                    $ crab21_stat_select = True
                                    $ crab_stat_name = crab21_name
                                    $ crab_stat_level = crab21_level
                                    $ crab_stat_hp = crab21_hp
                                    $ crab_stat_att = crab21_att
                                    $ crab_stat_def = crab21_def
                                    $ crab_stat_acc = crab21_acc

                                    $ crab_stat_type = crab21_type
                                    $ crab_stat_move2 = crab21_move2
                                    $ crab_stat_move3 = crab21_move3
                                    $ crab_stat_move4 = crab21_move4
                                    $ crab_stat_element = crab21_element
                                    if crab21_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab21_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab21_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab21_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab22:
                                    $ crab22_stat_select = True
                                    $ crab_stat_name = crab22_name
                                    $ crab_stat_level = crab22_level
                                    $ crab_stat_hp = crab22_hp
                                    $ crab_stat_att = crab22_att
                                    $ crab_stat_def = crab22_def
                                    $ crab_stat_acc = crab22_acc

                                    $ crab_stat_type = crab22_type
                                    $ crab_stat_move2 = crab22_move2
                                    $ crab_stat_move3 = crab22_move3
                                    $ crab_stat_move4 = crab22_move4
                                    $ crab_stat_element = crab22_element
                                    if crab22_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab22_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab22_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab22_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab23:
                                    $ crab23_stat_select = True
                                    $ crab_stat_name = crab23_name
                                    $ crab_stat_level = crab23_level
                                    $ crab_stat_hp = crab23_hp
                                    $ crab_stat_att = crab23_att
                                    $ crab_stat_def = crab23_def
                                    $ crab_stat_acc = crab23_acc

                                    $ crab_stat_type = crab23_type
                                    $ crab_stat_move2 = crab23_move2
                                    $ crab_stat_move3 = crab23_move3
                                    $ crab_stat_move4 = crab23_move4
                                    $ crab_stat_element = crab23_element
                                    if crab23_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab23_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab23_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab23_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab24:
                                    $ crab24_stat_select = True
                                    $ crab_stat_name = crab24_name
                                    $ crab_stat_level = crab24_level
                                    $ crab_stat_hp = crab24_hp
                                    $ crab_stat_att = crab24_att
                                    $ crab_stat_def = crab24_def
                                    $ crab_stat_acc = crab24_acc

                                    $ crab_stat_type = crab24_type
                                    $ crab_stat_move2 = crab24_move2
                                    $ crab_stat_move3 = crab24_move3
                                    $ crab_stat_move4 = crab24_move4
                                    $ crab_stat_element = crab24_element
                                    if crab24_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab24_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab24_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab24_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab25:
                                    $ crab25_stat_select = True
                                    $ crab_stat_name = crab25_name
                                    $ crab_stat_level = crab25_level
                                    $ crab_stat_hp = crab25_hp
                                    $ crab_stat_att = crab25_att
                                    $ crab_stat_def = crab25_def
                                    $ crab_stat_acc = crab25_acc

                                    $ crab_stat_type = crab25_type
                                    $ crab_stat_move2 = crab25_move2
                                    $ crab_stat_move3 = crab25_move3
                                    $ crab_stat_move4 = crab25_move4
                                    $ crab_stat_element = crab25_element
                                    if crab25_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab25_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab25_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab25_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab26:
                                    $ crab26_stat_select = True
                                    $ crab_stat_name = crab26_name
                                    $ crab_stat_level = crab26_level
                                    $ crab_stat_hp = crab26_hp
                                    $ crab_stat_att = crab26_att
                                    $ crab_stat_def = crab26_def
                                    $ crab_stat_acc = crab26_acc

                                    $ crab_stat_type = crab26_type
                                    $ crab_stat_move2 = crab26_move2
                                    $ crab_stat_move3 = crab26_move3
                                    $ crab_stat_move4 = crab26_move4
                                    $ crab_stat_element = crab26_element
                                    if crab26_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab26_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab26_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab26_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab27:
                                    $ crab27_stat_select = True
                                    $ crab_stat_name = crab27_name
                                    $ crab_stat_level = crab27_level
                                    $ crab_stat_hp = crab27_hp
                                    $ crab_stat_att = crab27_att
                                    $ crab_stat_def = crab27_def
                                    $ crab_stat_acc = crab27_acc

                                    $ crab_stat_type = crab27_type
                                    $ crab_stat_move2 = crab27_move2
                                    $ crab_stat_move3 = crab27_move3
                                    $ crab_stat_move4 = crab27_move4
                                    $ crab_stat_element = crab27_element
                                    if crab27_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab27_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab27_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab27_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab28:
                                    $ crab28_stat_select = True
                                    $ crab_stat_name = crab28_name
                                    $ crab_stat_level = crab28_level
                                    $ crab_stat_hp = crab28_hp
                                    $ crab_stat_att = crab28_att
                                    $ crab_stat_def = crab28_def
                                    $ crab_stat_acc = crab28_acc

                                    $ crab_stat_type = crab28_type
                                    $ crab_stat_move2 = crab28_move2
                                    $ crab_stat_move3 = crab28_move3
                                    $ crab_stat_move4 = crab28_move4
                                    $ crab_stat_element = crab28_element
                                    if crab28_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab28_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab28_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab28_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab29:
                                    $ crab29_stat_select = True
                                    $ crab_stat_name = crab29_name
                                    $ crab_stat_level = crab29_level
                                    $ crab_stat_hp = crab29_hp
                                    $ crab_stat_att = crab29_att
                                    $ crab_stat_def = crab29_def
                                    $ crab_stat_acc = crab29_acc

                                    $ crab_stat_type = crab29_type
                                    $ crab_stat_move2 = crab29_move2
                                    $ crab_stat_move3 = crab29_move3
                                    $ crab_stat_move4 = crab29_move4
                                    $ crab_stat_element = crab29_element
                                    if crab29_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab29_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab29_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab29_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen

                                "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab30:
                                    $ crab30_stat_select = True
                                    $ crab_stat_name = crab30_name
                                    $ crab_stat_level = crab30_level
                                    $ crab_stat_hp = crab30_hp
                                    $ crab_stat_att = crab30_att
                                    $ crab_stat_def = crab30_def
                                    $ crab_stat_acc = crab30_acc

                                    $ crab_stat_type = crab30_type
                                    $ crab_stat_move2 = crab30_move2
                                    $ crab_stat_move3 = crab30_move3
                                    $ crab_stat_move4 = crab30_move4
                                    $ crab_stat_element = crab30_element
                                    if crab30_rarity == "n":
                                        $ crab_stat_rarity = "normal"
                                    if crab30_rarity == "r":
                                        $ crab_stat_rarity = "rare"
                                    if crab30_rarity == "e":
                                        $ crab_stat_rarity = "epic"
                                    if crab30_rarity == "l":
                                        $ crab_stat_rarity = "legendary"
                                    jump crab_stat_screen
                                "cancel":

                                    jump crab_manager

                                    label crab_stat_screen:
                                        show screen crabs_stats
                                        pause
                                        jump crab_stat_screen
                    "deposit crabs":


                        jump deposit_crabs

                        label deposit_crabs:
                            if not crab_spot2_chosen and not crab_spot3_chosen and not crab_spot4_chosen and not crab_spot5_chosen:
                                "you can't deposit your last crab!"
                                jump crab_manager
                            if not crab_spot1_chosen and not crab_spot3_chosen and not crab_spot4_chosen and not crab_spot5_chosen:
                                "you can't deposit your last crab!"
                                jump crab_manager
                            if not crab_spot1_chosen and not crab_spot2_chosen and not crab_spot4_chosen and not crab_spot5_chosen:
                                "you can't deposit your last crab!"
                                jump crab_manager
                            if not crab_spot1_chosen and not crab_spot2_chosen and not crab_spot3_chosen and not crab_spot5_chosen:
                                "you can't deposit your last crab!"
                                jump crab_manager
                            if not crab_spot1_chosen and not crab_spot2_chosen and not crab_spot3_chosen and not crab_spot4_chosen:
                                "you can't deposit your last crab!"
                                jump crab_manager

                            menu:
                                "-----------" if not crab_spot1_chosen:
                                    "you don't have a crab set here!"
                                    jump deposit_crabs

                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot1 ==1:
                                    show crab1_shuffle:
                                        ypos -450
                                    with dissolve
                                    menu:
                                        "would you like to deposit {b}[crab1_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab1_set = False
                                            $ crab_spot1 = 0
                                            hide crab1_shuffle with dissolve
                                            "{b}[crab1_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":
                                            hide crab1_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot1 ==2:
                                    show crab2_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab2_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab2_set = False
                                            $ crab_spot1 = 0
                                            hide crab2_shuffle with dissolve
                                            "{b}[crab2_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab2_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot1 ==3:
                                    show crab3_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab3_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab3_set = False
                                            $ crab_spot1 = 0
                                            hide crab3_shuffle with dissolve
                                            "{b}[crab3_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab3_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot1 ==4:
                                    show crab4_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab4_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab4_set = False
                                            $ crab_spot1 = 0
                                            hide crab4_shuffle with dissolve
                                            "{b}[crab4_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab4_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot1 ==5:
                                    show crab5_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab5_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab5_set = False
                                            $ crab_spot1 = 0
                                            hide crab5_shuffle with dissolve
                                            "{b}[crab5_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab5_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot1 ==6:
                                    show crab6_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab6_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab6_set = False
                                            $ crab_spot1 = 0
                                            hide crab6_shuffle with dissolve
                                            "{b}[crab6_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab6_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot1 ==7:
                                    show crab7_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab7_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab7_set = False
                                            $ crab_spot1 = 0
                                            hide crab7_shuffle with dissolve
                                            "{b}[crab7_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab7_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot1 ==8:
                                    show crab8_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab8_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab8_set = False
                                            $ crab_spot1 = 0
                                            hide crab8_shuffle with dissolve
                                            "{b}[crab8_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab8_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot1 ==9:
                                    show crab9_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab9_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab9_set = False
                                            $ crab_spot1 = 0
                                            hide crab9_shuffle with dissolve
                                            "{b}[crab9_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab9_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot1 ==10:
                                    show crab10_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab10_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab10_set = False
                                            $ crab_spot1 = 0
                                            hide crab10_shuffle with dissolve
                                            "{b}[crab10_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab10_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot1 ==11:
                                    show crab11_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab11_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab11_set = False
                                            $ crab_spot1 = 0
                                            hide crab11_shuffle with dissolve
                                            "{b}[crab11_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab11_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot1 ==12:
                                    show crab12_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab12_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab12_set = False
                                            $ crab_spot1 = 0
                                            hide crab12_shuffle with dissolve
                                            "{b}[crab12_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab12_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot1 ==13:
                                    show crab13_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab13_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab13_set = False
                                            $ crab_spot1 = 0
                                            hide crab13_shuffle with dissolve
                                            "{b}[crab13_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab13_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot1 ==14:
                                    show crab14_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab14_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab14_set = False
                                            $ crab_spot1 = 0
                                            hide crab14_shuffle with dissolve
                                            "{b}[crab14_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab14_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot1 ==15:
                                    show crab15_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab15_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab15_set = False
                                            $ crab_spot1 = 0
                                            hide crab15_shuffle with dissolve
                                            "{b}[crab15_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab15_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot1 ==16:
                                    show crab16_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab16_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab16_set = False
                                            $ crab_spot1 = 0
                                            hide crab16_shuffle with dissolve
                                            "{b}[crab16_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab16_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot1 ==17:
                                    show crab17_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab17_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab17_set = False
                                            $ crab_spot1 = 0
                                            hide crab17_shuffle with dissolve
                                            "{b}[crab17_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab17_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot1 ==18:
                                    show crab18_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab18_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab18_set = False
                                            $ crab_spot1 = 0
                                            hide crab18_shuffle with dissolve
                                            "{b}[crab18_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab18_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot1 ==19:
                                    show crab19_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab19_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab19_set = False
                                            $ crab_spot1 = 0
                                            hide crab19_shuffle with dissolve
                                            "{b}[crab19_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab19_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot1 ==20:
                                    show crab20_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab20_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab20_set = False
                                            $ crab_spot1 = 0
                                            hide crab20_shuffle with dissolve
                                            "{b}[crab20_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab20_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot1 ==21:
                                    show crab21_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab21_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab21_set = False
                                            $ crab_spot1 = 0
                                            hide crab21_shuffle with dissolve
                                            "{b}[crab21_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab21_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot1 ==22:
                                    show crab22_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab22_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab22_set = False
                                            $ crab_spot1 = 0
                                            hide crab22_shuffle with dissolve
                                            "{b}[crab22_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab22_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot1 ==23:
                                    show crab23_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab23_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab23_set = False
                                            $ crab_spot1 = 0
                                            hide crab23_shuffle with dissolve
                                            "{b}[crab23_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab23_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot1 ==24:
                                    show crab24_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab24_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab24_set = False
                                            $ crab_spot1 = 0
                                            hide crab24_shuffle with dissolve
                                            "{b}[crab24_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab24_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot1 ==25:
                                    show crab25_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab25_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab25_set = False
                                            $ crab_spot1 = 0
                                            hide crab25_shuffle with dissolve
                                            "{b}[crab25_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab25_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot1 ==26:
                                    show crab26_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab26_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab26_set = False
                                            $ crab_spot1 = 0
                                            hide crab26_shuffle with dissolve
                                            "{b}[crab26_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab26_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot1 ==27:
                                    show crab27_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab27_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab27_set = False
                                            $ crab_spot1 = 0
                                            hide crab27_shuffle with dissolve
                                            "{b}[crab27_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab27_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot1 ==28:
                                    show crab28_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab28_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab28_set = False
                                            $ crab_spot1 = 0
                                            hide crab28_shuffle with dissolve
                                            "{b}[crab28_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab28_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot1 ==29:
                                    show crab29_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab29_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab29_set = False
                                            $ crab_spot1 = 0
                                            hide crab29_shuffle with dissolve
                                            "{b}[crab29_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab29_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot1 ==30:
                                    show crab30_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab30_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot1_chosen = False
                                            $ crab30_set = False
                                            $ crab_spot1 = 0
                                            hide crab30_shuffle with dissolve
                                            "{b}[crab30_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab30_shuffle with dissolve
                                            jump deposit_crabs

                                "-----------" if not crab_spot2_chosen:
                                    "you don't have a crab set here!"
                                    jump deposit_crabs

                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot2 ==1:
                                    show crab1_shuffle:
                                        ypos -450
                                    with dissolve
                                    menu:
                                        "would you like to deposit {b}[crab1_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab1_set = False
                                            $ crab_spot2 = 0
                                            hide crab1_shuffle with dissolve
                                            "{b}[crab1_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":
                                            hide crab1_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot2 ==2:
                                    show crab2_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab2_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab2_set = False
                                            $ crab_spot2 = 0
                                            hide crab2_shuffle with dissolve
                                            "{b}[crab2_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab2_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot2 ==3:
                                    show crab3_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab3_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab3_set = False
                                            $ crab_spot2 = 0
                                            hide crab3_shuffle with dissolve
                                            "{b}[crab3_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab3_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot2 ==4:
                                    show crab4_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab4_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab4_set = False
                                            $ crab_spot2 = 0
                                            hide crab4_shuffle with dissolve
                                            "{b}[crab4_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab4_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot2 ==5:
                                    show crab5_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab5_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab5_set = False
                                            $ crab_spot2 = 0
                                            hide crab5_shuffle with dissolve
                                            "{b}[crab5_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab5_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot2 ==6:
                                    show crab6_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab6_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab6_set = False
                                            $ crab_spot2 = 0
                                            hide crab6_shuffle with dissolve
                                            "{b}[crab6_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab6_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot2 ==7:
                                    show crab7_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab7_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab7_set = False
                                            $ crab_spot2 = 0
                                            hide crab7_shuffle with dissolve
                                            "{b}[crab7_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab7_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot2 ==8:
                                    show crab8_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab8_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab8_set = False
                                            $ crab_spot2 = 0
                                            hide crab8_shuffle with dissolve
                                            "{b}[crab8_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab8_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot2 ==9:
                                    show crab9_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab9_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab9_set = False
                                            $ crab_spot2 = 0
                                            hide crab9_shuffle with dissolve
                                            "{b}[crab9_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab9_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot2 ==10:
                                    show crab10_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab10_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab10_set = False
                                            $ crab_spot2 = 0
                                            hide crab10_shuffle with dissolve
                                            "{b}[crab10_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab10_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot2 ==11:
                                    show crab11_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab11_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab11_set = False
                                            $ crab_spot2 = 0
                                            hide crab11_shuffle with dissolve
                                            "{b}[crab11_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab11_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot2 ==12:
                                    show crab12_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab12_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab12_set = False
                                            $ crab_spot2 = 0
                                            hide crab12_shuffle with dissolve
                                            "{b}[crab12_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab12_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot2 ==13:
                                    show crab13_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab13_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab13_set = False
                                            $ crab_spot2 = 0
                                            hide crab13_shuffle with dissolve
                                            "{b}[crab13_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab13_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot2 ==14:
                                    show crab14_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab14_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab14_set = False
                                            $ crab_spot2 = 0
                                            hide crab14_shuffle with dissolve
                                            "{b}[crab14_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab14_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot2 ==15:
                                    show crab15_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab15_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab15_set = False
                                            $ crab_spot2 = 0
                                            hide crab15_shuffle with dissolve
                                            "{b}[crab15_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab15_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot2 ==16:
                                    show crab16_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab16_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab16_set = False
                                            $ crab_spot2 = 0
                                            hide crab16_shuffle with dissolve
                                            "{b}[crab16_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab16_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot2 ==17:
                                    show crab17_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab17_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab17_set = False
                                            $ crab_spot2 = 0
                                            hide crab17_shuffle with dissolve
                                            "{b}[crab17_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab17_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot2 ==18:
                                    show crab18_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab18_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab18_set = False
                                            $ crab_spot2 = 0
                                            hide crab18_shuffle with dissolve
                                            "{b}[crab18_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab18_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot2 ==19:
                                    show crab19_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab19_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab19_set = False
                                            $ crab_spot2 = 0
                                            hide crab19_shuffle with dissolve
                                            "{b}[crab19_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab19_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot2 ==20:
                                    show crab20_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab20_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab20_set = False
                                            $ crab_spot2 = 0
                                            hide crab20_shuffle with dissolve
                                            "{b}[crab20_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab20_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot2 ==21:
                                    show crab21_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab21_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab21_set = False
                                            $ crab_spot2 = 0
                                            hide crab21_shuffle with dissolve
                                            "{b}[crab21_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab21_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot2 ==22:
                                    show crab22_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab22_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab22_set = False
                                            $ crab_spot2 = 0
                                            hide crab22_shuffle with dissolve
                                            "{b}[crab22_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab22_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot2 ==23:
                                    show crab23_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab23_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab23_set = False
                                            $ crab_spot2 = 0
                                            hide crab23_shuffle with dissolve
                                            "{b}[crab23_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab23_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot2 ==24:
                                    show crab24_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab24_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab24_set = False
                                            $ crab_spot2 = 0
                                            hide crab24_shuffle with dissolve
                                            "{b}[crab24_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab24_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot2 ==25:
                                    show crab25_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab25_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab25_set = False
                                            $ crab_spot2 = 0
                                            hide crab25_shuffle with dissolve
                                            "{b}[crab25_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab25_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot2 ==26:
                                    show crab26_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab26_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab26_set = False
                                            $ crab_spot2 = 0
                                            hide crab26_shuffle with dissolve
                                            "{b}[crab26_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab26_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot2 ==27:
                                    show crab27_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab27_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab27_set = False
                                            $ crab_spot2 = 0
                                            hide crab27_shuffle with dissolve
                                            "{b}[crab27_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab27_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot2 ==28:
                                    show crab28_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab28_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab28_set = False
                                            $ crab_spot2 = 0
                                            hide crab28_shuffle with dissolve
                                            "{b}[crab28_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab28_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot2 ==29:
                                    show crab29_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab29_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab29_set = False
                                            $ crab_spot2 = 0
                                            hide crab29_shuffle with dissolve
                                            "{b}[crab29_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab29_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot2 ==30:
                                    show crab30_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab30_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot2_chosen = False
                                            $ crab30_set = False
                                            $ crab_spot2 = 0
                                            hide crab30_shuffle with dissolve
                                            "{b}[crab30_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab30_shuffle with dissolve
                                            jump deposit_crabs

                                "-----------" if not crab_spot3_chosen:
                                    "you don't have a crab set here!"
                                    jump deposit_crabs

                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot3 ==1:
                                    show crab1_shuffle:
                                        ypos -450
                                    with dissolve
                                    menu:
                                        "would you like to deposit {b}[crab1_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab1_set = False
                                            $ crab_spot3 = 0
                                            hide crab1_shuffle with dissolve
                                            "{b}[crab1_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":
                                            hide crab1_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot3 ==2:
                                    show crab2_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab2_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab2_set = False
                                            $ crab_spot3 = 0
                                            hide crab2_shuffle with dissolve
                                            "{b}[crab2_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab2_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot3 ==3:
                                    show crab3_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab3_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab3_set = False
                                            $ crab_spot3 = 0
                                            hide crab3_shuffle with dissolve
                                            "{b}[crab3_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab3_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot3 ==4:
                                    show crab4_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab4_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab4_set = False
                                            $ crab_spot3 = 0
                                            hide crab4_shuffle with dissolve
                                            "{b}[crab4_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab4_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot3 ==5:
                                    show crab5_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab5_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab5_set = False
                                            $ crab_spot3 = 0
                                            hide crab5_shuffle with dissolve
                                            "{b}[crab5_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab5_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot3 ==6:
                                    show crab6_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab6_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab6_set = False
                                            $ crab_spot3 = 0
                                            hide crab6_shuffle with dissolve
                                            "{b}[crab6_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab6_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot3 ==7:
                                    show crab7_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab7_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab7_set = False
                                            $ crab_spot3 = 0
                                            hide crab7_shuffle with dissolve
                                            "{b}[crab7_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab7_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot3 ==8:
                                    show crab8_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab8_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab8_set = False
                                            $ crab_spot3 = 0
                                            hide crab8_shuffle with dissolve
                                            "{b}[crab8_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab8_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot3 ==9:
                                    show crab9_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab9_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab9_set = False
                                            $ crab_spot3 = 0
                                            hide crab9_shuffle with dissolve
                                            "{b}[crab9_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab9_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot3 ==10:
                                    show crab10_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab10_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab10_set = False
                                            $ crab_spot3 = 0
                                            hide crab10_shuffle with dissolve
                                            "{b}[crab10_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab10_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot3 ==11:
                                    show crab11_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab11_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab11_set = False
                                            $ crab_spot3 = 0
                                            hide crab11_shuffle with dissolve
                                            "{b}[crab11_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab11_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot3 ==12:
                                    show crab12_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab12_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab12_set = False
                                            $ crab_spot3 = 0
                                            hide crab12_shuffle with dissolve
                                            "{b}[crab12_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab12_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot3 ==13:
                                    show crab13_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab13_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab13_set = False
                                            $ crab_spot3 = 0
                                            hide crab13_shuffle with dissolve
                                            "{b}[crab13_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab13_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot3 ==14:
                                    show crab14_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab14_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab14_set = False
                                            $ crab_spot3 = 0
                                            hide crab14_shuffle with dissolve
                                            "{b}[crab14_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab14_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot3 ==15:
                                    show crab15_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab15_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab15_set = False
                                            $ crab_spot3 = 0
                                            hide crab15_shuffle with dissolve
                                            "{b}[crab15_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab15_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot3 ==16:
                                    show crab16_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab16_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab16_set = False
                                            $ crab_spot3 = 0
                                            hide crab16_shuffle with dissolve
                                            "{b}[crab16_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab16_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot3 ==17:
                                    show crab17_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab17_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab17_set = False
                                            $ crab_spot3 = 0
                                            hide crab17_shuffle with dissolve
                                            "{b}[crab17_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab17_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot3 ==18:
                                    show crab18_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab18_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab18_set = False
                                            $ crab_spot3 = 0
                                            hide crab18_shuffle with dissolve
                                            "{b}[crab18_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab18_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot3 ==19:
                                    show crab19_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab19_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab19_set = False
                                            $ crab_spot3 = 0
                                            hide crab19_shuffle with dissolve
                                            "{b}[crab19_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab19_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot3 ==20:
                                    show crab20_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab20_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab20_set = False
                                            $ crab_spot3 = 0
                                            hide crab20_shuffle with dissolve
                                            "{b}[crab20_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab20_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot3 ==21:
                                    show crab21_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab21_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab21_set = False
                                            $ crab_spot3 = 0
                                            hide crab21_shuffle with dissolve
                                            "{b}[crab21_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab21_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot3 ==22:
                                    show crab22_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab22_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab22_set = False
                                            $ crab_spot3 = 0
                                            hide crab22_shuffle with dissolve
                                            "{b}[crab22_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab22_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot3 ==23:
                                    show crab23_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab23_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab23_set = False
                                            $ crab_spot3 = 0
                                            hide crab23_shuffle with dissolve
                                            "{b}[crab23_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab23_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot3 ==24:
                                    show crab24_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab24_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab24_set = False
                                            $ crab_spot3 = 0
                                            hide crab24_shuffle with dissolve
                                            "{b}[crab24_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab24_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot3 ==25:
                                    show crab25_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab25_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab25_set = False
                                            $ crab_spot3 = 0
                                            hide crab25_shuffle with dissolve
                                            "{b}[crab25_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab25_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot3 ==26:
                                    show crab26_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab26_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab26_set = False
                                            $ crab_spot3 = 0
                                            hide crab26_shuffle with dissolve
                                            "{b}[crab26_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab26_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot3 ==27:
                                    show crab27_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab27_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab27_set = False
                                            $ crab_spot3 = 0
                                            hide crab27_shuffle with dissolve
                                            "{b}[crab27_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab27_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot3 ==28:
                                    show crab28_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab28_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab28_set = False
                                            $ crab_spot3 = 0
                                            hide crab28_shuffle with dissolve
                                            "{b}[crab28_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab28_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot3 ==29:
                                    show crab29_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab29_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab29_set = False
                                            $ crab_spot3 = 0
                                            hide crab29_shuffle with dissolve
                                            "{b}[crab29_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab29_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot3 ==30:
                                    show crab30_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab30_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot3_chosen = False
                                            $ crab30_set = False
                                            $ crab_spot3 = 0
                                            hide crab30_shuffle with dissolve
                                            "{b}[crab30_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab30_shuffle with dissolve
                                            jump deposit_crabs

                                "-----------" if not crab_spot4_chosen:
                                    "you don't have a crab set here!"
                                    jump deposit_crabs

                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot4 ==1:
                                    show crab1_shuffle:
                                        ypos -450
                                    with dissolve
                                    menu:
                                        "would you like to deposit {b}[crab1_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab1_set = False
                                            $ crab_spot4 = 0
                                            hide crab1_shuffle with dissolve
                                            "{b}[crab1_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":
                                            hide crab1_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot4 ==2:
                                    show crab2_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab2_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab2_set = False
                                            $ crab_spot4 = 0
                                            hide crab2_shuffle with dissolve
                                            "{b}[crab2_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab2_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot4 ==3:
                                    show crab3_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab3_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab3_set = False
                                            $ crab_spot4 = 0
                                            hide crab3_shuffle with dissolve
                                            "{b}[crab3_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab3_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot4 ==4:
                                    show crab4_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab4_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab4_set = False
                                            $ crab_spot4 = 0
                                            hide crab4_shuffle with dissolve
                                            "{b}[crab4_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab4_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot4 ==5:
                                    show crab5_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab5_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab5_set = False
                                            $ crab_spot4 = 0
                                            hide crab5_shuffle with dissolve
                                            "{b}[crab5_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab5_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot4 ==6:
                                    show crab6_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab6_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab6_set = False
                                            $ crab_spot4 = 0
                                            hide crab6_shuffle with dissolve
                                            "{b}[crab6_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab6_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot4 ==7:
                                    show crab7_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab7_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab7_set = False
                                            $ crab_spot4 = 0
                                            hide crab7_shuffle with dissolve
                                            "{b}[crab7_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab7_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot4 ==8:
                                    show crab8_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab8_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab8_set = False
                                            $ crab_spot4 = 0
                                            hide crab8_shuffle with dissolve
                                            "{b}[crab8_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab8_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot4 ==9:
                                    show crab9_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab9_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab9_set = False
                                            $ crab_spot4 = 0
                                            hide crab9_shuffle with dissolve
                                            "{b}[crab9_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab9_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot4 ==10:
                                    show crab10_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab10_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab10_set = False
                                            $ crab_spot4 = 0
                                            hide crab10_shuffle with dissolve
                                            "{b}[crab10_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab10_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot4 ==11:
                                    show crab11_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab11_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab11_set = False
                                            $ crab_spot4 = 0
                                            hide crab11_shuffle with dissolve
                                            "{b}[crab11_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab11_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot4 ==12:
                                    show crab12_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab12_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab12_set = False
                                            $ crab_spot4 = 0
                                            hide crab12_shuffle with dissolve
                                            "{b}[crab12_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab12_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot4 ==13:
                                    show crab13_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab13_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab13_set = False
                                            $ crab_spot4 = 0
                                            hide crab13_shuffle with dissolve
                                            "{b}[crab13_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab13_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot4 ==14:
                                    show crab14_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab14_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab14_set = False
                                            $ crab_spot4 = 0
                                            hide crab14_shuffle with dissolve
                                            "{b}[crab14_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab14_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot4 ==15:
                                    show crab15_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab15_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab15_set = False
                                            $ crab_spot4 = 0
                                            hide crab15_shuffle with dissolve
                                            "{b}[crab15_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab15_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot4 ==16:
                                    show crab16_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab16_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab16_set = False
                                            $ crab_spot4 = 0
                                            hide crab16_shuffle with dissolve
                                            "{b}[crab16_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab16_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot4 ==17:
                                    show crab17_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab17_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab17_set = False
                                            $ crab_spot4 = 0
                                            hide crab17_shuffle with dissolve
                                            "{b}[crab17_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab17_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot4 ==18:
                                    show crab18_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab18_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab18_set = False
                                            $ crab_spot4 = 0
                                            hide crab18_shuffle with dissolve
                                            "{b}[crab18_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab18_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot4 ==19:
                                    show crab19_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab19_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab19_set = False
                                            $ crab_spot4 = 0
                                            hide crab19_shuffle with dissolve
                                            "{b}[crab19_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab19_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot4 ==20:
                                    show crab20_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab20_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab20_set = False
                                            $ crab_spot4 = 0
                                            hide crab20_shuffle with dissolve
                                            "{b}[crab20_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab20_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot4 ==21:
                                    show crab21_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab21_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab21_set = False
                                            $ crab_spot4 = 0
                                            hide crab21_shuffle with dissolve
                                            "{b}[crab21_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab21_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot4 ==22:
                                    show crab22_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab22_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab22_set = False
                                            $ crab_spot4 = 0
                                            hide crab22_shuffle with dissolve
                                            "{b}[crab22_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab22_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot4 ==23:
                                    show crab23_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab23_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab23_set = False
                                            $ crab_spot4 = 0
                                            hide crab23_shuffle with dissolve
                                            "{b}[crab23_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab23_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot4 ==24:
                                    show crab24_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab24_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab24_set = False
                                            $ crab_spot4 = 0
                                            hide crab24_shuffle with dissolve
                                            "{b}[crab24_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab24_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot4 ==25:
                                    show crab25_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab25_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab25_set = False
                                            $ crab_spot4 = 0
                                            hide crab25_shuffle with dissolve
                                            "{b}[crab25_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab25_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot4 ==26:
                                    show crab26_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab26_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab26_set = False
                                            $ crab_spot4 = 0
                                            hide crab26_shuffle with dissolve
                                            "{b}[crab26_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab26_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot4 ==27:
                                    show crab27_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab27_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab27_set = False
                                            $ crab_spot4 = 0
                                            hide crab27_shuffle with dissolve
                                            "{b}[crab27_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab27_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot4 ==28:
                                    show crab28_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab28_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab28_set = False
                                            $ crab_spot4 = 0
                                            hide crab28_shuffle with dissolve
                                            "{b}[crab28_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab28_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot4 ==29:
                                    show crab29_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab29_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab29_set = False
                                            $ crab_spot4 = 0
                                            hide crab29_shuffle with dissolve
                                            "{b}[crab29_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab29_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot4 ==30:
                                    show crab30_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab30_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot4_chosen = False
                                            $ crab30_set = False
                                            $ crab_spot4 = 0
                                            hide crab30_shuffle with dissolve
                                            "{b}[crab30_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab30_shuffle with dissolve
                                            jump deposit_crabs

                                "-----------" if not crab_spot5_chosen:
                                    "you don't have a crab set here!"
                                    jump deposit_crabs

                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot5 ==1:
                                    show crab1_shuffle:
                                        ypos -450
                                    with dissolve
                                    menu:
                                        "would you like to deposit {b}[crab1_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab1_set = False
                                            $ crab_spot5 = 0
                                            hide crab1_shuffle with dissolve
                                            "{b}[crab1_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":
                                            hide crab1_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot5 ==2:
                                    show crab2_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab2_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab2_set = False
                                            $ crab_spot5 = 0
                                            hide crab2_shuffle with dissolve
                                            "{b}[crab2_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab2_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot5 ==3:
                                    show crab3_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab3_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab3_set = False
                                            $ crab_spot5 = 0
                                            hide crab3_shuffle with dissolve
                                            "{b}[crab3_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab3_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot5 ==4:
                                    show crab4_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab4_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab4_set = False
                                            $ crab_spot5 = 0
                                            hide crab4_shuffle with dissolve
                                            "{b}[crab4_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab4_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot5 ==5:
                                    show crab5_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab5_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab5_set = False
                                            $ crab_spot5 = 0
                                            hide crab5_shuffle with dissolve
                                            "{b}[crab5_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab5_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot5 ==6:
                                    show crab6_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab6_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab6_set = False
                                            $ crab_spot5 = 0
                                            hide crab6_shuffle with dissolve
                                            "{b}[crab6_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab6_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot5 ==7:
                                    show crab7_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab7_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab7_set = False
                                            $ crab_spot5 = 0
                                            hide crab7_shuffle with dissolve
                                            "{b}[crab7_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab7_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot5 ==8:
                                    show crab8_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab8_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab8_set = False
                                            $ crab_spot5 = 0
                                            hide crab8_shuffle with dissolve
                                            "{b}[crab8_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab8_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot5 ==9:
                                    show crab9_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab9_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab9_set = False
                                            $ crab_spot5 = 0
                                            hide crab9_shuffle with dissolve
                                            "{b}[crab9_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab9_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot5 ==10:
                                    show crab10_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab10_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab10_set = False
                                            $ crab_spot5 = 0
                                            hide crab10_shuffle with dissolve
                                            "{b}[crab10_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab10_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot5 ==11:
                                    show crab11_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab11_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab11_set = False
                                            $ crab_spot5 = 0
                                            hide crab11_shuffle with dissolve
                                            "{b}[crab11_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab11_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot5 ==12:
                                    show crab12_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab12_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab12_set = False
                                            $ crab_spot5 = 0
                                            hide crab12_shuffle with dissolve
                                            "{b}[crab12_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab12_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot5 ==13:
                                    show crab13_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab13_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab13_set = False
                                            $ crab_spot5 = 0
                                            hide crab13_shuffle with dissolve
                                            "{b}[crab13_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab13_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot5 ==14:
                                    show crab14_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab14_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab14_set = False
                                            $ crab_spot5 = 0
                                            hide crab14_shuffle with dissolve
                                            "{b}[crab14_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab14_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot5 ==15:
                                    show crab15_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab15_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab15_set = False
                                            $ crab_spot5 = 0
                                            hide crab15_shuffle with dissolve
                                            "{b}[crab15_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab15_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot5 ==16:
                                    show crab16_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab16_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab16_set = False
                                            $ crab_spot5 = 0
                                            hide crab16_shuffle with dissolve
                                            "{b}[crab16_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab16_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot5 ==17:
                                    show crab17_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab17_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab17_set = False
                                            $ crab_spot5 = 0
                                            hide crab17_shuffle with dissolve
                                            "{b}[crab17_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab17_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot5 ==18:
                                    show crab18_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab18_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab18_set = False
                                            $ crab_spot5 = 0
                                            hide crab18_shuffle with dissolve
                                            "{b}[crab18_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab18_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot5 ==19:
                                    show crab19_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab19_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab19_set = False
                                            $ crab_spot5 = 0
                                            hide crab19_shuffle with dissolve
                                            "{b}[crab19_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab19_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot5 ==20:
                                    show crab20_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab20_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab20_set = False
                                            $ crab_spot5 = 0
                                            hide crab20_shuffle with dissolve
                                            "{b}[crab20_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab20_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot5 ==21:
                                    show crab21_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab21_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab21_set = False
                                            $ crab_spot5 = 0
                                            hide crab21_shuffle with dissolve
                                            "{b}[crab21_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab21_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot5 ==22:
                                    show crab22_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab22_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab22_set = False
                                            $ crab_spot5 = 0
                                            hide crab22_shuffle with dissolve
                                            "{b}[crab22_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab22_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot5 ==23:
                                    show crab23_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab23_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab23_set = False
                                            $ crab_spot5 = 0
                                            hide crab23_shuffle with dissolve
                                            "{b}[crab23_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab23_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot5 ==24:
                                    show crab24_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab24_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab24_set = False
                                            $ crab_spot5 = 0
                                            hide crab24_shuffle with dissolve
                                            "{b}[crab24_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab24_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot5 ==25:
                                    show crab25_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab25_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab25_set = False
                                            $ crab_spot5 = 0
                                            hide crab25_shuffle with dissolve
                                            "{b}[crab25_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab25_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot5 ==26:
                                    show crab26_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab26_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab26_set = False
                                            $ crab_spot5 = 0
                                            hide crab26_shuffle with dissolve
                                            "{b}[crab26_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab26_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot5 ==27:
                                    show crab27_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab27_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab27_set = False
                                            $ crab_spot5 = 0
                                            hide crab27_shuffle with dissolve
                                            "{b}[crab27_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab27_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot5 ==28:
                                    show crab28_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab28_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab28_set = False
                                            $ crab_spot5 = 0
                                            hide crab28_shuffle with dissolve
                                            "{b}[crab28_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab28_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot5 ==29:
                                    show crab29_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab29_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab29_set = False
                                            $ crab_spot5 = 0
                                            hide crab29_shuffle with dissolve
                                            "{b}[crab29_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab29_shuffle with dissolve
                                            jump deposit_crabs

                                "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot5 ==30:
                                    show crab30_shuffle:
                                        ypos -450
                                    menu:
                                        "would you like to deposit {b}[crab30_name]{/b} for now?"
                                        "deposit":
                                            $ deck_crabs -=1
                                            $ deck_crabs -=1
                                            $ crab_spot5_chosen = False
                                            $ crab30_set = False
                                            $ crab_spot5 = 0
                                            hide crab30_shuffle with dissolve
                                            "{b}[crab30_name]{/b} was deposited!"
                                            jump deposit_crabs
                                        "nevermind":

                                            hide crab30_shuffle with dissolve
                                            jump deposit_crabs
                                "cancel":

                                    jump crab_manager
                    "withdraw crabs":

                        jump withdraw_crabs

                        label withdraw_crabs:
                            menu:
                                "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab1 and not crab1_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 1
                                        $ crabs_selected = True
                                        $ crab1_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 1
                                        $ crabs_selected = True
                                        $ crab1_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 1
                                        $ crabs_selected = True
                                        $ crab1_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 1
                                        $ crabs_selected = True
                                        $ crab1_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 1
                                        $ crabs_selected = True
                                        $ crab1_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    "you withdrew [crab1_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs

                                "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab2 and not crab2_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 2
                                        $ crabs_selected = True
                                        $ crab2_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 2
                                        $ crabs_selected = True
                                        $ crab2_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 2
                                        $ crabs_selected = True
                                        $ crab2_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 2
                                        $ crabs_selected = True
                                        $ crab2_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 2
                                        $ crabs_selected = True
                                        $ crab2_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    "you withdrew [crab2_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs

                                "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab3 and not crab3_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 3
                                        $ crabs_selected = True
                                        $ crab3_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 3
                                        $ crabs_selected = True
                                        $ crab3_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 3
                                        $ crabs_selected = True
                                        $ crab3_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 3
                                        $ crabs_selected = True
                                        $ crab3_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 3
                                        $ crabs_selected = True
                                        $ crab3_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    "you withdrew [crab3_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs

                                "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab4 and not crab4_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 4
                                        $ crabs_selected = True
                                        $ crab4_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 4
                                        $ crabs_selected = True
                                        $ crab4_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 4
                                        $ crabs_selected = True
                                        $ crab4_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 4
                                        $ crabs_selected = True
                                        $ crab4_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 4
                                        $ crabs_selected = True
                                        $ crab4_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    "you withdrew [crab4_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs

                                "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab5 and not crab5_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 5
                                        $ crabs_selected = True
                                        $ crab5_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 5
                                        $ crabs_selected = True
                                        $ crab5_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 5
                                        $ crabs_selected = True
                                        $ crab5_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 5
                                        $ crabs_selected = True
                                        $ crab5_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 5
                                        $ crabs_selected = True
                                        $ crab5_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    "you withdrew [crab5_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs

                                "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab6 and not crab6_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 6
                                        $ crabs_selected = True
                                        $ crab6_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 6
                                        $ crabs_selected = True
                                        $ crab6_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 6
                                        $ crabs_selected = True
                                        $ crab6_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 6
                                        $ crabs_selected = True
                                        $ crab6_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 6
                                        $ crabs_selected = True
                                        $ crab6_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    "you withdrew [crab6_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs

                                "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab7 and not crab7_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 7
                                        $ crabs_selected = True
                                        $ crab7_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 7
                                        $ crabs_selected = True
                                        $ crab7_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 7
                                        $ crabs_selected = True
                                        $ crab7_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 7
                                        $ crabs_selected = True
                                        $ crab7_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 7
                                        $ crabs_selected = True
                                        $ crab7_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    $ deck_crabs +=1
                                    "you withdrew [crab7_name]!"
                                    $ deck_crabs +=1
                                    jump withdraw_crabs
                                "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab8 and not crab8_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 8
                                        $ crabs_selected = True
                                        $ crab8_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 8
                                        $ crabs_selected = True
                                        $ crab8_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 8
                                        $ crabs_selected = True
                                        $ crab8_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 8
                                        $ crabs_selected = True
                                        $ crab8_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 8
                                        $ crabs_selected = True
                                        $ crab8_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    $ deck_crabs +=1
                                    "you withdrew [crab8_name]!"
                                    jump withdraw_crabs
                                "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab9 and not crab9_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 9
                                        $ crabs_selected = True
                                        $ crab9_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 9
                                        $ crabs_selected = True
                                        $ crab9_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 9
                                        $ crabs_selected = True
                                        $ crab9_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 9
                                        $ crabs_selected = True
                                        $ crab9_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 9
                                        $ crabs_selected = True
                                        $ crab9_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    $ deck_crabs +=1
                                    "you withdrew [crab9_name]!"
                                    jump withdraw_crabs
                                "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab10 and not crab10_set:
                                    if not crab_spot1_chosen:
                                        $ crab_spot1_chosen = True
                                        $ crab_spot1 = 10
                                        $ crabs_selected = True
                                        $ crab10_set = True
                                    elif not crab_spot2_chosen:
                                        $ crab_spot2_chosen = True
                                        $ crab_spot2 = 10
                                        $ crabs_selected = True
                                        $ crab10_set = True
                                    elif not crab_spot3_chosen:
                                        $ crab_spot3_chosen = True
                                        $ crab_spot3 = 10
                                        $ crabs_selected = True
                                        $ crab10_set = True
                                    elif not crab_spot4_chosen:
                                        $ crab_spot4_chosen = True
                                        $ crab_spot4 = 10
                                        $ crabs_selected = True
                                        $ crab10_set = True
                                    elif not crab_spot5_chosen:
                                        $ crab_spot5_chosen = True
                                        $ crab_spot5 = 10
                                        $ crabs_selected = True
                                        $ crab10_set = True
                                    else:
                                        "you need to deposit a crab first!"
                                        jump withdraw_crabs

                                    $ deck_crabs +=1
                                    "you withdrew [crab10_name]!"
                                    jump withdraw_crabs
                                "more ->" if crabs_total >=11:
                                    jump withdraw_page2

                                    label withdraw_page2:

                                        menu:

                                            "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab11 and not crab11_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 11
                                                    $ crabs_selected = True
                                                    $ crab11_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 11
                                                    $ crabs_selected = True
                                                    $ crab11_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 11
                                                    $ crabs_selected = True
                                                    $ crab11_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 11
                                                    $ crabs_selected = True
                                                    $ crab11_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 11
                                                    $ crabs_selected = True
                                                    $ crab11_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab11_name]!"
                                                jump withdraw_crabs
                                            "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab12 and not crab12_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 12
                                                    $ crabs_selected = True
                                                    $ crab12_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 12
                                                    $ crabs_selected = True
                                                    $ crab12_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 12
                                                    $ crabs_selected = True
                                                    $ crab12_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 12
                                                    $ crabs_selected = True
                                                    $ crab12_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 12
                                                    $ crabs_selected = True
                                                    $ crab12_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab12_name]!"
                                                jump withdraw_crabs

                                            "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab13 and not crab13_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 13
                                                    $ crabs_selected = True
                                                    $ crab13_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 13
                                                    $ crabs_selected = True
                                                    $ crab13_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 13
                                                    $ crabs_selected = True
                                                    $ crab13_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 13
                                                    $ crabs_selected = True
                                                    $ crab13_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 13
                                                    $ crabs_selected = True
                                                    $ crab13_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab13_name]!"
                                                jump withdraw_crabs

                                            "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab14 and not crab14_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 14
                                                    $ crabs_selected = True
                                                    $ crab14_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 14
                                                    $ crabs_selected = True
                                                    $ crab14_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 14
                                                    $ crabs_selected = True
                                                    $ crab14_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 14
                                                    $ crabs_selected = True
                                                    $ crab14_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 14
                                                    $ crabs_selected = True
                                                    $ crab14_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab14_name]!"
                                                jump withdraw_crabs

                                            "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab15 and not crab15_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 15
                                                    $ crabs_selected = True
                                                    $ crab15_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 15
                                                    $ crabs_selected = True
                                                    $ crab15_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 15
                                                    $ crabs_selected = True
                                                    $ crab15_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 15
                                                    $ crabs_selected = True
                                                    $ crab15_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 15
                                                    $ crabs_selected = True
                                                    $ crab15_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab15_name]!"
                                                jump withdraw_crabs

                                            "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab16 and not crab16_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 16
                                                    $ crabs_selected = True
                                                    $ crab16_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 16
                                                    $ crabs_selected = True
                                                    $ crab16_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 16
                                                    $ crabs_selected = True
                                                    $ crab16_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 16
                                                    $ crabs_selected = True
                                                    $ crab16_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 16
                                                    $ crabs_selected = True
                                                    $ crab16set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab16_name]!"
                                                jump withdraw_crabs

                                            "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab17 and not crab17_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 17
                                                    $ crabs_selected = True
                                                    $ crab17_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 17
                                                    $ crabs_selected = True
                                                    $ crab17_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 17
                                                    $ crabs_selected = True
                                                    $ crab17_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 17
                                                    $ crabs_selected = True
                                                    $ crab17_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 17
                                                    $ crabs_selected = True
                                                    $ crab17_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab17_name]!"
                                                jump withdraw_crabs

                                            "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab18 and not crab18_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 18
                                                    $ crabs_selected = True
                                                    $ crab18_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 18
                                                    $ crabs_selected = True
                                                    $ crab18_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 18
                                                    $ crabs_selected = True
                                                    $ crab18_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 18
                                                    $ crabs_selected = True
                                                    $ crab18_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 18
                                                    $ crabs_selected = True
                                                    $ crab18_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab18_name]!"
                                                jump withdraw_crabs

                                            "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab19 and not crab19_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 19
                                                    $ crabs_selected = True
                                                    $ crab19_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 19
                                                    $ crabs_selected = True
                                                    $ crab19_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 19
                                                    $ crabs_selected = True
                                                    $ crab19_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 19
                                                    $ crabs_selected = True
                                                    $ crab19_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 19
                                                    $ crabs_selected = True
                                                    $ crab19_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab19_name]!"
                                                jump withdraw_crabs

                                            "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab20 and not crab20_set:
                                                if not crab_spot1_chosen:
                                                    $ crab_spot1_chosen = True
                                                    $ crab_spot1 = 20
                                                    $ crabs_selected = True
                                                    $ crab20_set = True
                                                elif not crab_spot2_chosen:
                                                    $ crab_spot2_chosen = True
                                                    $ crab_spot2 = 20
                                                    $ crabs_selected = True
                                                    $ crab20_set = True
                                                elif not crab_spot3_chosen:
                                                    $ crab_spot3_chosen = True
                                                    $ crab_spot3 = 20
                                                    $ crabs_selected = True
                                                    $ crab20_set = True
                                                elif not crab_spot4_chosen:
                                                    $ crab_spot4_chosen = True
                                                    $ crab_spot4 = 20
                                                    $ crabs_selected = True
                                                    $ crab20_set = True
                                                elif not crab_spot5_chosen:
                                                    $ crab_spot5_chosen = True
                                                    $ crab_spot5 = 20
                                                    $ crabs_selected = True
                                                    $ crab20_set = True
                                                else:
                                                    "you need to deposit a crab first!"
                                                    jump withdraw_crabs

                                                $ deck_crabs +=1
                                                "you withdrew [crab20_name]!"
                                                jump withdraw_crabs

                                            "more ->" if crabs_total >=21:
                                                jump withdraw_page3

                                                label withdraw_page3:
                                                    menu:
                                                        "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab21 and not crab21_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 21
                                                                $ crabs_selected = True
                                                                $ crab21_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 21
                                                                $ crabs_selected = True
                                                                $ crab21_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 21
                                                                $ crabs_selected = True
                                                                $ crab21_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 21
                                                                $ crabs_selected = True
                                                                $ crab21_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 21
                                                                $ crabs_selected = True
                                                                $ crab21_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab21_name]!"
                                                            jump withdraw_crabs

                                                        "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab22 and not crab22_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 22
                                                                $ crabs_selected = True
                                                                $ crab22_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 22
                                                                $ crabs_selected = True
                                                                $ crab22_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 22
                                                                $ crabs_selected = True
                                                                $ crab22_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 22
                                                                $ crabs_selected = True
                                                                $ crab22_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 22
                                                                $ crabs_selected = True
                                                                $ crab22_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab22_name]!"
                                                            jump withdraw_crabs

                                                        "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab23 and not crab23_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 23
                                                                $ crabs_selected = True
                                                                $ crab23_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 23
                                                                $ crabs_selected = True
                                                                $ crab23_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 23
                                                                $ crabs_selected = True
                                                                $ crab23_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 23
                                                                $ crabs_selected = True
                                                                $ crab23_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 23
                                                                $ crabs_selected = True
                                                                $ crab23_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab23_name]!"
                                                            jump withdraw_crabs

                                                        "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab24 and not crab24_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 24
                                                                $ crabs_selected = True
                                                                $ crab24_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 24
                                                                $ crabs_selected = True
                                                                $ crab24_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 24
                                                                $ crabs_selected = True
                                                                $ crab24_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 24
                                                                $ crabs_selected = True
                                                                $ crab24_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 24
                                                                $ crabs_selected = True
                                                                $ crab24_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab24_name]!"
                                                            jump withdraw_crabs

                                                        "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab25 and not crab25_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 25
                                                                $ crabs_selected = True
                                                                $ crab25_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 25
                                                                $ crabs_selected = True
                                                                $ crab25_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 25
                                                                $ crabs_selected = True
                                                                $ crab25_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 25
                                                                $ crabs_selected = True
                                                                $ crab25_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 25
                                                                $ crabs_selected = True
                                                                $ crab25_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab25_name]!"
                                                            jump withdraw_crabs

                                                        "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab26 and not crab26_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 26
                                                                $ crabs_selected = True
                                                                $ crab26_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 26
                                                                $ crabs_selected = True
                                                                $ crab26_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 26
                                                                $ crabs_selected = True
                                                                $ crab26_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 26
                                                                $ crabs_selected = True
                                                                $ crab26_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 26
                                                                $ crabs_selected = True
                                                                $ crab26_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab26_name]!"
                                                            jump withdraw_crabs

                                                        "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab27 and not crab27_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 27
                                                                $ crabs_selected = True
                                                                $ crab27_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 27
                                                                $ crabs_selected = True
                                                                $ crab27_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 27
                                                                $ crabs_selected = True
                                                                $ crab27_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 27
                                                                $ crabs_selected = True
                                                                $ crab27_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 27
                                                                $ crabs_selected = True
                                                                $ crab27_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab27_name]!"
                                                            jump withdraw_crabs

                                                        "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab28 and not crab28_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 28
                                                                $ crabs_selected = True
                                                                $ crab28_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 28
                                                                $ crabs_selected = True
                                                                $ crab28_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 28
                                                                $ crabs_selected = True
                                                                $ crab28_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 28
                                                                $ crabs_selected = True
                                                                $ crab28_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 28
                                                                $ crabs_selected = True
                                                                $ crab28_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab28_name]!"
                                                            jump withdraw_crabs

                                                        "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab29 and not crab29_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 29
                                                                $ crabs_selected = True
                                                                $ crab29_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 29
                                                                $ crabs_selected = True
                                                                $ crab29_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 29
                                                                $ crabs_selected = True
                                                                $ crab29_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 29
                                                                $ crabs_selected = True
                                                                $ crab29_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 29
                                                                $ crabs_selected = True
                                                                $ crab29_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab29_name]!"
                                                            jump withdraw_crabs

                                                        "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab30 and not crab30_set:
                                                            if not crab_spot1_chosen:
                                                                $ crab_spot1_chosen = True
                                                                $ crab_spot1 = 30
                                                                $ crabs_selected = True
                                                                $ crab30_set = True
                                                            elif not crab_spot2_chosen:
                                                                $ crab_spot2_chosen = True
                                                                $ crab_spot2 = 30
                                                                $ crabs_selected = True
                                                                $ crab30_set = True
                                                            elif not crab_spot3_chosen:
                                                                $ crab_spot3_chosen = True
                                                                $ crab_spot3 = 30
                                                                $ crabs_selected = True
                                                                $ crab30_set = True
                                                            elif not crab_spot4_chosen:
                                                                $ crab_spot4_chosen = True
                                                                $ crab_spot4 = 30
                                                                $ crabs_selected = True
                                                                $ crab30_set = True
                                                            elif not crab_spot5_chosen:
                                                                $ crab_spot5_chosen = True
                                                                $ crab_spot5 = 30
                                                                $ crabs_selected = True
                                                                $ crab30_set = True
                                                            else:
                                                                "you need to deposit a crab first!"
                                                                jump withdraw_crabs

                                                            $ deck_crabs +=1
                                                            "you withdrew [crab30_name]!"
                                                            jump withdraw_crabs
                                                        "<- back":

                                                            jump withdraw_page2
                                                        "cancel":

                                                            jump crab_manager
                                            "<- back":

                                                jump withdraw_crabs
                                            "cancel":

                                                jump crab_manager
                                "cancel":

                                    jump crab_manager
                    "release":

                        jump release_crabs

                        label release_crabs:
                            menu:
                                "[crab1_name] - L[crab1_level]" if crab1 and not crab1_set:
                                    "you can't release your first crab!"
                                    jump release_crabs

                                "[crab2_name] - L[crab2_level]" if crab2 and not crab2_set:
                                    "releasing [crab2_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab2 = False
                                            $ crab2_level = 1
                                            "[crab2_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs

                                "[crab3_name] - L[crab3_level]" if crab3 and not crab3_set:
                                    "releasing [crab3_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab3 = False
                                            $ crab3_level = 1
                                            "[crab3_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs

                                "[crab4_name] - L[crab4_level]" if crab4 and not crab4_set:
                                    "releasing [crab4_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab4 = False
                                            $ crab4_level = 1
                                            "[crab4_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs

                                "[crab5_name] - L[crab5_level]" if crab5 and not crab5_set:
                                    "releasing [crab5_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab5 = False
                                            $ crab5_level = 1
                                            "[crab5_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs

                                "[crab6_name] - L[crab6_level]" if crab6 and not crab6_set:
                                    "releasing [crab6_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab6 = False
                                            $ crab6_level = 1
                                            "[crab6_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs

                                "[crab7_name] - L[crab7_level]" if crab7 and not crab7_set:
                                    "releasing [crab7_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab7 = False
                                            $ crab7_level = 1
                                            "[crab7_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs
                                "[crab8_name] - L[crab8_level]" if crab8 and not crab8_set:
                                    "releasing [crab8_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab8 = False
                                            $ crab8_level = 1
                                            "[crab8_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs
                                "[crab9_name] - L[crab9_level]" if crab9 and not crab9_set:
                                    "releasing [crab9_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab9 = False
                                            $ crab9_level = 1
                                            "[crab9_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs
                                "[crab10_name] - L[crab10_level]" if crab10 and not crab10_set:
                                    "releasing [crab10_name] will make it disappear forever."
                                    menu:
                                        "release":
                                            $ crab10 = False
                                            $ crab10_level = 1
                                            "[crab10_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                            jump release_crabs
                                        "cancel":

                                            jump release_crabs
                                "more ->" if crabs_total >=11:
                                    jump release_page2

                                    label release_page2:

                                        menu:
                                            "[crab11_name]" if crab11 and not crab11_set:
                                                "releasing [crab11_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab11 = False
                                                        $ crab11_level = 1
                                                        "[crab11_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs
                                            "[crab12_name]" if crab12 and not crab12_set:
                                                "releasing [crab12_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab12 = False
                                                        $ crab12_level = 1
                                                        "[crab12_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab13_name]" if crab13 and not crab13_set:
                                                "releasing [crab13_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab13 = False
                                                        $ crab13_level = 1
                                                        "[crab13_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab14_name]" if crab14 and not crab14_set:
                                                "releasing [crab14_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab14 = False
                                                        $ crab14_level = 1
                                                        "[crab14_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab15_name]" if crab15 and not crab15_set:
                                                "releasing [crab15_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab15 = False
                                                        $ crab15_level = 1
                                                        "[crab15_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab16_name]" if crab16 and not crab16_set:
                                                "releasing [crab16_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab16 = False
                                                        $ crab16_level = 1
                                                        "[crab16_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab17_name]" if crab17 and not crab17_set:
                                                "releasing [crab17_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab17 = False
                                                        $ crab17_level = 1
                                                        "[crab17_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab18_name]" if crab18 and not crab18_set:
                                                "releasing [crab18_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab18 = False
                                                        $ crab18_level = 1
                                                        "[crab18_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "[crab19_name]" if crab19 and not crab19_set:
                                                "releasing [crab19_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab19 = False
                                                        $ crab19_level = 1
                                                        "[crab19_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs
                                            "[crab20_name]" if crab20 and not crab20_set:
                                                "releasing [crab20_name] will make it disappear forever."
                                                menu:
                                                    "release":
                                                        $ crab20 = False
                                                        $ crab20_level = 1
                                                        "[crab20_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                        jump release_crabs
                                                    "cancel":

                                                        jump release_crabs

                                            "more ->" if crabs_total >=21:
                                                jump release_page3

                                                label release_page3:
                                                    menu:
                                                        "[crab21_name]" if crab21 and not crab21_set:
                                                            "releasing [crab21_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab21 = False
                                                                    $ crab21_level = 1
                                                                    "[crab21_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab22_name]" if crab22 and not crab22_set:
                                                            "releasing [crab22_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab22 = False
                                                                    $ crab22_level = 1
                                                                    "[crab22_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab23_name]" if crab23 and not crab23_set:
                                                            "releasing [crab23_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab23 = False
                                                                    $ crab23_level = 1
                                                                    "[crab23_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab24_name]" if crab24 and not crab24_set:
                                                            "releasing [crab24_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab24 = False
                                                                    $ crab24_level = 1
                                                                    "[crab24_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab25_name]" if crab25 and not crab25_set:
                                                            "releasing [crab25_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab25 = False
                                                                    $ crab25_level = 1
                                                                    "[crab25_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab26_name]" if crab26 and not crab26_set:
                                                            "releasing [crab26_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab26 = False
                                                                    $ crab26_level = 1
                                                                    "[crab26_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab27_name]" if crab27 and not crab27_set:
                                                            "releasing [crab27_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab27 = False
                                                                    $ crab27_level = 1
                                                                    "[crab27_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab28_name]" if crab28 and not crab28_set:
                                                            "releasing [crab28_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab28 = False
                                                                    $ crab28_level = 1
                                                                    "[crab28_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab29_name]" if crab29 and not crab29_set:
                                                            "releasing [crab29_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab29 = False
                                                                    $ crab29_level = 1
                                                                    "[crab29_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs

                                                        "[crab30_name]" if crab30 and not crab30_set:
                                                            "releasing [crab30_name] will make it disappear forever."
                                                            menu:
                                                                "release":
                                                                    $ crab30 = False
                                                                    $ crab30_level = 1
                                                                    "[crab30_name] scuttles off forever, shellebrating his freedom. Goodbye!"
                                                                    jump release_crabs
                                                                "cancel":

                                                                    jump release_crabs
                                                        "<- back":

                                                            jump release_page2
                                                        "cancel":

                                                            jump crab_manager
                                            "<- back":

                                                jump release_crabs
                                            "cancel":

                                                jump crab_manager
                                "cancel":

                                    jump crab_manager
                    "cancel":

                        jump begin_stuff
        "wild crab blast":




























































































































































































































































































































































            if not shady_hunt_explain:
                show shadyguy_grin with dissolve
                sg "you can find wild crabs in the grassy areas."
                sg "there should probably be more grass."
                sg "good luck!"
                $ shady_hunt_explain = True
                hide shadyguy_grin with dissolve
            jump enter_arena
        "crabble royale":

            jump crab_battle_menu
        "exit":

            jump basingse_day1

label crab_battle_menu:
    $ crabs_alive = deck_crabs

    $ total_arena_exp = 0

    $ crab1_active = False
    $ crab2_active = False
    $ crab3_active = False
    $ crab4_active = False
    $ crab5_active = False
    $ crab6_active = False
    $ crab7_active = False
    $ crab8_active = False
    $ crab9_active = False
    $ crab10_active = False
    $ crab11_active = False
    $ crab12_active = False
    $ crab13_active = False
    $ crab14_active = False
    $ crab15_active = False
    $ crab16_active = False
    $ crab17_active = False
    $ crab18_active = False
    $ crab19_active = False
    $ crab20_active = False
    $ crab21_active = False
    $ crab22_active = False
    $ crab23_active = False
    $ crab24_active = False
    $ crab25_active = False
    $ crab26_active = False
    $ crab27_active = False
    $ crab28_active = False
    $ crab29_active = False
    $ crab30_active = False
    if crab_spot1_chosen:
        if crab_spot1 == 1:
            $ crab_standin_health = crab1_hp
            $ crab_max_health = crab1_hp
            $ crab_name = crab1_name
            $ crab_level = crab1_level






            $ crab1_active = True

            show crab1_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 2:
            $ crab_standin_health = crab2_hp
            $ crab_max_health = crab2_hp
            $ crab_name = crab2_name
            $ crab_level = crab2_level

            $ crab2_active = True

            show crab2_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 3:
            $ crab_standin_health = crab3_hp
            $ crab_max_health = crab3_hp
            $ crab_name = crab3_name
            $ crab_level = crab3_level
            $ crab3_active = True
            show crab3_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 4:
            $ crab_standin_health = crab4_hp
            $ crab_max_health = crab4_hp
            $ crab_name = crab4_name
            $ crab_level = crab4_level
            $ crab4_active = True
            show crab4_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 5:
            $ crab_standin_health = crab5_hp
            $ crab_max_health = crab5_hp
            $ crab_name = crab5_name
            $ crab_level = crab5_level
            $ crab5_active = True
            show crab5_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 6:
            $ crab_standin_health = crab6_hp
            $ crab_max_health = crab6_hp
            $ crab_name = crab6_name
            $ crab_level = crab6_level
            $ crab6_active = True
            show crab6_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 7:
            $ crab_standin_health = crab7_hp
            $ crab_max_health = crab7_hp
            $ crab_name = crab7_name
            $ crab_level = crab7_level
            $ crab7_active = True
            show crab7_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 8:
            $ crab_standin_health = crab8_hp
            $ crab_max_health = crab8_hp
            $ crab_name = crab8_name
            $ crab_level = crab8_level
            $ crab8_active = True
            show crab8_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 9:
            $ crab_standin_health = crab9_hp
            $ crab_max_health = crab9_hp
            $ crab_name = crab9_name
            $ crab_level = crab9_level
            $ crab9_active = True
            show crab9_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 10:
            $ crab_standin_health = crab10_hp
            $ crab_max_health = crab10_hp
            $ crab_name = crab10_name
            $ crab_level = crab10_level
            $ crab10_active = True
            show crab10_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 11:
            $ crab_standin_health = crab11_hp
            $ crab_max_health = crab11_max_hp
            $ crab_name = crab11_name
            $ crab_level = crab11_level
            $ crab11_active = True
            show crab11_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 12:
            $ crab_standin_health = crab12_hp
            $ crab_max_health = crab12_hp
            $ crab_name = crab12_name
            $ crab_level = crab12_level
            $ crab12_active = True
            show crab12_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 13:
            $ crab_standin_health = crab13_hp
            $ crab_max_health = crab13_hp
            $ crab_name = crab13_name
            $ crab_level = crab13_level
            $ crab13_active = True
            show crab13_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 14:
            $ crab_standin_health = crab14_hp
            $ crab_max_health = crab14_hp
            $ crab_name = crab14_name
            $ crab_level = crab14_level
            $ crab14_active = True
            show crab14_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 15:
            $ crab_standin_health = crab15_hp
            $ crab_max_health = crab15_hp
            $ crab_name = crab15_name
            $ crab_level = crab15_level
            $ crab15_active = True
            show crab15_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 16:
            $ crab_standin_health = crab16_hp
            $ crab_max_health = crab16_hp
            $ crab_name = crab16_name
            $ crab_level = crab16_level
            $ crab16_active = True
            show crab16_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 17:
            $ crab_standin_health = crab17_hp
            $ crab_max_health = crab17_hp
            $ crab_name = crab17_name
            $ crab_level = crab17_level
            $ crab17_active = True
            show crab17_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 18:
            $ crab_standin_health = crab18_hp
            $ crab_max_health = crab18_hp
            $ crab_name = crab18_name
            $ crab_level = crab18_level
            $ crab8_active = True
            show crab18_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 19:
            $ crab_standin_health = crab19_hp
            $ crab_max_health = crab19_hp
            $ crab_name = crab19_name
            $ crab_level = crab19_level
            $ crab19_active = True
            show crab19_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 20:
            $ crab_standin_health = crab20_hp
            $ crab_max_health = crab20_hp
            $ crab_name = crab20_name
            $ crab_level = crab20_level
            $ crab20_active = True
            show crab20_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 21:
            $ crab_standin_health = crab21_hp
            $ crab_max_health = crab21_hp
            $ crab_name = crab21_name
            $ crab_level = crab21_level
            $ crab21_active = True
            show crab21_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 22:
            $ crab_standin_health = crab22_hp
            $ crab_max_health = crab22_hp
            $ crab_name = crab22_name
            $ crab_level = crab22_level
            $ crab22_active = True
            show crab22_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 23:
            $ crab_standin_health = crab23_hp
            $ crab_max_health = crab23_hp
            $ crab_name = crab23_name
            $ crab_level = crab23_level
            $ crab23_active = True
            show crab23_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 24:
            $ crab_standin_health = crab24_hp
            $ crab_max_health = crab24_hp
            $ crab_name = crab24_name
            $ crab_level = crab24_level
            $ crab24_active = True
            show crab24_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 25:
            $ crab_standin_health = crab25_hp
            $ crab_max_health = crab25_hp
            $ crab_name = crab25_name
            $ crab_level = crab25_level
            $ crab25_active = True
            show crab25_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 26:
            $ crab_standin_health = crab26_hp
            $ crab_max_health = crab26_hp
            $ crab_name = crab26_name
            $ crab_level = crab26_level
            $ crab26_active = True
            show crab26_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 27:
            $ crab_standin_health = crab27_hp
            $ crab_max_health = crab27_hp
            $ crab_name = crab27_name
            $ crab_level = crab27_level
            $ crab27_active = True
            show crab27_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 28:
            $ crab_standin_health = crab28_hp
            $ crab_max_health = crab28_hp
            $ crab_name = crab28_name
            $ crab_level = crab28_level
            $ crab28_active = True
            show crab28_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 29:
            $ crab_standin_health = crab29_hp
            $ crab_max_health = crab29_hp
            $ crab_name = crab29_name
            $ crab_level = crab29_level
            $ crab29_active = True
            show crab29_shuffle:
                xpos -250 ypos -200
        if crab_spot1 == 30:
            $ crab_standin_health = crab30_hp
            $ crab_max_health = crab30_hp
            $ crab_name = crab30_name
            $ crab_level = crab30_level
            $ crab30_active = True
            show crab30_shuffle:
                xpos -250 ypos -200
    elif crab_spot2_chosen:
        if crab_spot2 == 1:
            $ crab_standin_health = crab1_hp
            $ crab_max_health = crab1_hp
            $ crab_name = crab1_name
            $ crab_level = crab1_level
            $ crab1_active = True
            show crab1_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 2:
            $ crab_standin_health = crab2_hp
            $ crab_max_health = crab2_hp
            $ crab_name = crab2_name
            $ crab_level = crab2_level
            $ crab2_active = True
            show crab2_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 3:
            $ crab_standin_health = crab3_hp
            $ crab_max_health = crab3_hp
            $ crab_name = crab3_name
            $ crab_level = crab3_level
            $ crab3_active = True
            show crab3_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 4:
            $ crab_standin_health = crab4_hp
            $ crab_max_health = crab4_hp
            $ crab_name = crab4_name
            $ crab_level = crab4_level
            $ crab4_active = True
            show crab4_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 5:
            $ crab_standin_health = crab5_hp
            $ crab_max_health = crab5_hp
            $ crab_name = crab5_name
            $ crab_level = crab5_level
            $ crab5_active = True
            show crab5_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 6:
            $ crab_standin_health = crab6_hp
            $ crab_max_health = crab6_hp
            $ crab_name = crab6_name
            $ crab_level = crab6_level
            $ crab6_active = True
            show crab6_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 7:
            $ crab_standin_health = crab7_hp
            $ crab_max_health = crab7_hp
            $ crab_name = crab7_name
            $ crab_level = crab7_level
            $ crab7_active = True
            show crab7_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 8:
            $ crab_standin_health = crab8_hp
            $ crab_max_health = crab8_hp
            $ crab_name = crab8_name
            $ crab_level = crab8_level
            $ crab8_active = True
            show crab8_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 9:
            $ crab_standin_health = crab9_hp
            $ crab_max_health = crab9_hp
            $ crab_name = crab9_name
            $ crab_level = crab9_level
            $ crab9_active = True
            show crab9_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 10:
            $ crab_standin_health = crab10_hp
            $ crab_max_health = crab10_hp
            $ crab_name = crab10_name
            $ crab_level = crab10_level
            $ crab10_active = True
            show crab10_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 11:
            $ crab_standin_health = crab11_hp
            $ crab_max_health = crab11_hp
            $ crab_name = crab11_name
            $ crab_level = crab11_level
            $ crab11_active = True
            show crab11_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 12:
            $ crab_standin_health = crab12_hp
            $ crab_max_health = crab12_hp
            $ crab_name = crab12_name
            $ crab_level = crab12_level
            $ crab12_active = True
            show crab12_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 13:
            $ crab_standin_health = crab13_hp
            $ crab_max_health = crab13_hp
            $ crab_name = crab13_name
            $ crab_level = crab13_level
            $ crab13_active = True
            show crab13_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 14:
            $ crab_standin_health = crab14_hp
            $ crab_max_health = crab14_hp
            $ crab_name = crab14_name
            $ crab_level = crab14_level
            $ crab14_active = True
            show crab14_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 15:
            $ crab_standin_health = crab15_hp
            $ crab_max_health = crab15_hp
            $ crab_name = crab15_name
            $ crab_level = crab15_level
            $ crab15_active = True
            show crab15_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 16:
            $ crab_standin_health = crab16_hp
            $ crab_max_health = crab16_hp
            $ crab_name = crab16_name
            $ crab_level = crab16_level
            $ crab16_active = True
            show crab16_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 17:
            $ crab_standin_health = crab17_hp
            $ crab_max_health = crab17_hp
            $ crab_name = crab17_name
            $ crab_level = crab17_level
            $ crab17_active = True
            show crab17_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 18:
            $ crab_standin_health = crab18_hp
            $ crab_max_health = crab18_hp
            $ crab_name = crab18_name
            $ crab_level = crab18_level
            $ crab18_active = True
            show crab18_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 19:
            $ crab_standin_health = crab19_hp
            $ crab_max_health = crab19_hp
            $ crab_name = crab19_name
            $ crab_level = crab19_level
            $ crab19_active = True
            show crab19_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 20:
            $ crab_standin_health = crab20_hp
            $ crab_max_health = crab20_hp
            $ crab_name = crab20_name
            $ crab_level = crab20_level
            $ crab20_active = True
            show crab20_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 21:
            $ crab_standin_health = crab21_hp
            $ crab_max_health = crab21_hp
            $ crab_name = crab21_name
            $ crab_level = crab21_level
            $ crab21_active = True
            show crab21_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 22:
            $ crab_standin_health = crab22_hp
            $ crab_max_health = crab22_hp
            $ crab_name = crab22_name
            $ crab_level = crab22_level
            $ crab22_active = True
            show crab22_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 23:
            $ crab_standin_health = crab23_hp
            $ crab_max_health = crab23_hp
            $ crab_name = crab23_name
            $ crab_level = crab23_level
            $ crab23_active = True
            show crab23_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 24:
            $ crab_standin_health = crab24_hp
            $ crab_max_health = crab24_hp
            $ crab_name = crab24_name
            $ crab_level = crab24_level
            $ crab24_active = True
            show crab24_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 25:
            $ crab_standin_health = crab25_hp
            $ crab_max_health = crab25_hp
            $ crab_name = crab25_name
            $ crab_level = crab25_level
            $ crab25_active = True
            show crab25_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 26:
            $ crab_standin_health = crab26_hp
            $ crab_max_health = crab26_hp
            $ crab_name = crab26_name
            $ crab_level = crab26_level
            $ crab26_active = True
            show crab26_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 27:
            $ crab_standin_health = crab27_hp
            $ crab_max_health = crab27_hp
            $ crab_name = crab27_name
            $ crab_level = crab27_level
            $ crab27_active = True
            show crab27_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 28:
            $ crab_standin_health = crab28_hp
            $ crab_max_health = crab28_hp
            $ crab_name = crab28_name
            $ crab_level = crab28_level
            $ crab28_active = True
            show crab28_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 29:
            $ crab_standin_health = crab29_hp
            $ crab_max_health = crab29_hp
            $ crab_name = crab29_name
            $ crab_level = crab29_level
            $ crab29_active = True
            show crab29_shuffle:
                xpos -250 ypos -200
        if crab_spot2 == 30:
            $ crab_standin_health = crab30_hp
            $ crab_max_health = crab30_hp
            $ crab_name = crab30_name
            $ crab_level = crab30_level
            $ crab30_active = True
            show crab30_shuffle:
                xpos -250 ypos -200

    elif crab_spot3_chosen:
        if crab_spot3 == 1:
            $ crab_standin_health = crab1_hp
            $ crab_max_health = crab1_hp
            $ crab_name = crab1_name
            $ crab_level = crab1_level
            $ crab1_active = True
            show crab1_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 2:
            $ crab_standin_health = crab2_hp
            $ crab_max_health = crab2_hp
            $ crab_name = crab2_name
            $ crab_level = crab2_level
            $ crab2_active = True
            show crab2_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 3:
            $ crab_standin_health = crab3_hp
            $ crab_max_health = crab3_hp
            $ crab_name = crab3_name
            $ crab_level = crab3_level
            $ crab3_active = True
            show crab3_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 4:
            $ crab_standin_health = crab4_hp
            $ crab_max_health = crab4_hp
            $ crab_name = crab4_name
            $ crab_level = crab4_level
            $ crab4_active = True
            show crab4_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 5:
            $ crab_standin_health = crab5_hp
            $ crab_max_health = crab5_hp
            $ crab_name = crab5_name
            $ crab_level = crab5_level
            $ crab5_active = True
            show crab5_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 6:
            $ crab_standin_health = crab6_hp
            $ crab_max_health = crab6_hp
            $ crab_name = crab6_name
            $ crab_level = crab6_level
            $ crab6_active = True
            show crab6_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 7:
            $ crab_standin_health = crab7_hp
            $ crab_max_health = crab7_hp
            $ crab_name = crab7_name
            $ crab_level = crab7_level
            $ crab7_active = True
            show crab7_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 8:
            $ crab_standin_health = crab8_hp
            $ crab_max_health = crab8_hp
            $ crab_name = crab8_name
            $ crab_level = crab8_level
            $ crab8_active = True
            show crab8_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 9:
            $ crab_standin_health = crab9_hp
            $ crab_max_health = crab9_hp
            $ crab_name = crab9_name
            $ crab_level = crab9_level
            $ crab9_active = True
            show crab9_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 10:
            $ crab_standin_health = crab10_hp
            $ crab_max_health = crab10_hp
            $ crab_name = crab10_name
            $ crab_level = crab10_level
            $ crab10_active = True
            show crab10_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 11:
            $ crab_standin_health = crab11_hp
            $ crab_max_health = crab11_hp
            $ crab_name = crab11_name
            $ crab_level = crab11_level
            $ crab11_active = True
            show crab11_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 12:
            $ crab_standin_health = crab12_hp
            $ crab_max_health = crab12_hp
            $ crab_name = crab12_name
            $ crab_level = crab12_level
            $ crab12_active = True
            show crab12_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 13:
            $ crab_standin_health = crab13_hp
            $ crab_max_health = crab13_hp
            $ crab_name = crab13_name
            $ crab_level = crab13_level
            $ crab13_active = True
            show crab13_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 14:
            $ crab_standin_health = crab14_hp
            $ crab_max_health = crab14_hp
            $ crab_name = crab14_name
            $ crab_level = crab14_level
            $ crab4_active = True
            show crab14_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 15:
            $ crab_standin_health = crab15_hp
            $ crab_max_health = crab15_hp
            $ crab_name = crab15_name
            $ crab_level = crab15_level
            $ crab15_active = True
            show crab15_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 16:
            $ crab_standin_health = crab16_hp
            $ crab_max_health = crab16_hp
            $ crab_name = crab16_name
            $ crab_level = crab16_level
            $ crab16_active = True
            show crab16_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 17:
            $ crab_standin_health = crab17_hp
            $ crab_max_health = crab17_hp
            $ crab_name = crab17_name
            $ crab_level = crab17_level
            $ crab17_active = True
            show crab17_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 18:
            $ crab_standin_health = crab18_hp
            $ crab_max_health = crab18_hp
            $ crab_name = crab18_name
            $ crab_level = crab18_level
            $ crab18_active = True
            show crab18_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 19:
            $ crab_standin_health = crab19_hp
            $ crab_max_health = crab19_hp
            $ crab_name = crab19_name
            $ crab_level = crab19_level
            $ crab19_active = True
            show crab19_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 20:
            $ crab_standin_health = crab20_hp
            $ crab_max_health = crab20_hp
            $ crab_name = crab20_name
            $ crab_level = crab20_level
            $ crab20_active = True
            show crab20_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 21:
            $ crab_standin_health = crab21_hp
            $ crab_max_health = crab21_hp
            $ crab_name = crab21_name
            $ crab_level = crab21_level
            $ crab21_active = True
            show crab21_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 22:
            $ crab_standin_health = crab22_hp
            $ crab_max_health = crab22_hp
            $ crab_name = crab22_name
            $ crab_level = crab22_level
            $ crab22_active = True
            show crab22_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 23:
            $ crab_standin_health = crab23_hp
            $ crab_max_health = crab23_hp
            $ crab_name = crab23_name
            $ crab_level = crab23_level
            $ crab23_active = True
            show crab23_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 24:
            $ crab_standin_health = crab24_hp
            $ crab_max_health = crab24_hp
            $ crab_name = crab24_name
            $ crab_level = crab24_level
            $ crab24_active = True
            show crab24_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 25:
            $ crab_standin_health = crab25_hp
            $ crab_max_health = crab25_hp
            $ crab_name = crab25_name
            $ crab_level = crab25_level
            $ crab25_active = True
            show crab25_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 26:
            $ crab_standin_health = crab26_hp
            $ crab_max_health = crab26_hp
            $ crab_name = crab26_name
            $ crab_level = crab26_level
            $ crab26_active = True
            show crab26_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 27:
            $ crab_standin_health = crab27_hp
            $ crab_max_health = crab27_hp
            $ crab_name = crab27_name
            $ crab_level = crab27_level
            $ crab27_active = True
            show crab27_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 28:
            $ crab_standin_health = crab28_hp
            $ crab_max_health = crab28_hp
            $ crab_name = crab28_name
            $ crab_level = crab28_level
            $ crab28_active = True
            show crab28_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 29:
            $ crab_standin_health = crab29_hp
            $ crab_max_health = crab29_hp
            $ crab_name = crab29_name
            $ crab_level = crab29_level
            $ crab29_active = True
            show crab29_shuffle:
                xpos -250 ypos -200
        if crab_spot3 == 30:
            $ crab_standin_health = crab30_hp
            $ crab_max_health = crab30_hp
            $ crab_name = crab30_name
            $ crab_level = crab30_level
            $ crab30_active = True
            show crab30_shuffle:
                xpos -250 ypos -200
    elif crab_spot4_chosen:
        if crab_spot4 == 1:
            $ crab_standin_health = crab1_hp
            $ crab_max_health = crab1_hp
            $ crab_name = crab1_name
            $ crab_level = crab1_level
            $ crab1_active = True
            show crab1_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 2:
            $ crab_standin_health = crab2_hp
            $ crab_max_health = crab2_hp
            $ crab_name = crab2_name
            $ crab_level = crab2_level
            $ crab2_active = True
            show crab2_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 3:
            $ crab_standin_health = crab3_hp
            $ crab_max_health = crab3_hp
            $ crab_name = crab3_name
            $ crab_level = crab3_level
            $ crab3_active = True
            show crab3_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 4:
            $ crab_standin_health = crab4_hp
            $ crab_max_health = crab4_hp
            $ crab_name = crab4_name
            $ crab_level = crab4_level
            $ crab4_active = True
            show crab4_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 5:
            $ crab_standin_health = crab5_hp
            $ crab_max_health = crab5_hp
            $ crab_name = crab5_name
            $ crab_level = crab5_level
            $ crab5_active = True
            show crab5_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 6:
            $ crab_standin_health = crab6_hp
            $ crab_max_health = crab6_hp
            $ crab_name = crab6_name
            $ crab_level = crab6_level
            $ crab6_active = True
            show crab6_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 7:
            $ crab_standin_health = crab7_hp
            $ crab_max_health = crab7_hp
            $ crab_name = crab7_name
            $ crab_level = crab7_level
            $ crab7_active = True
            show crab7_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 8:
            $ crab_standin_health = crab8_hp
            $ crab_max_health = crab8_hp
            $ crab_name = crab8_name
            $ crab_level = crab8_level
            $ crab8_active = True
            show crab8_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 9:
            $ crab_standin_health = crab9_hp
            $ crab_max_health = crab9_hp
            $ crab_name = crab9_name
            $ crab_level = crab9_level
            $ crab9_active = True
            show crab9_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 10:
            $ crab_standin_health = crab10_hp
            $ crab_max_health = crab10_hp
            $ crab_name = crab10_name
            $ crab_level = crab10_level
            $ crab10_active = True
            show crab10_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 11:
            $ crab_standin_health = crab11_hp
            $ crab_max_health = crab11_hp
            $ crab_name = crab11_name
            $ crab_level = crab11_level
            $ crab11_active = True
            show crab11_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 12:
            $ crab_standin_health = crab12_hp
            $ crab_max_health = crab12_hp
            $ crab_name = crab12_name
            $ crab_level = crab12_level
            $ crab12_active = True
            show crab12_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 13:
            $ crab_standin_health = crab13_hp
            $ crab_max_health = crab13_hp
            $ crab_name = crab13_name
            $ crab_level = crab13_level
            $ crab13_active = True
            show crab13_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 14:
            $ crab_standin_health = crab14_hp
            $ crab_max_health = crab14_hp
            $ crab_name = crab14_name
            $ crab_level = crab14_level
            $ crab14_active = True
            show crab14_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 15:
            $ crab_standin_health = crab15_hp
            $ crab_max_health = crab15_hp
            $ crab_name = crab15_name
            $ crab_level = crab15_level
            $ crab15_active = True
            show crab15_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 16:
            $ crab_standin_health = crab16_hp
            $ crab_max_health = crab16_hp
            $ crab_name = crab16_name
            $ crab_level = crab16_level
            $ crab16_active = True
            show crab16_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 17:
            $ crab_standin_health = crab17_hp
            $ crab_max_health = crab17_hp
            $ crab_name = crab17_name
            $ crab_level = crab17_level
            $ crab17_active = True
            show crab17_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 18:
            $ crab_standin_health = crab18_hp
            $ crab_max_health = crab18_hp
            $ crab_name = crab18_name
            $ crab_level = crab18_level
            $ crab18_active = True
            show crab18_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 19:
            $ crab_standin_health = crab19_hp
            $ crab_max_health = crab19_hp
            $ crab_name = crab19_name
            $ crab_level = crab19_level
            $ crab19_active = True
            show crab19_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 20:
            $ crab_standin_health = crab20_hp
            $ crab_max_health = crab20_hp
            $ crab_name = crab20_name
            $ crab_level = crab20_level
            $ crab20_active = True
            show crab20_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 21:
            $ crab_standin_health = crab21_hp
            $ crab_max_health = crab21_hp
            $ crab_name = crab21_name
            $ crab_level = crab21_level
            $ crab21_active = True
            show crab21_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 22:
            $ crab_standin_health = crab22_hp
            $ crab_max_health = crab22_hp
            $ crab_name = crab22_name
            $ crab_level = crab22_level
            $ crab22_active = True
            show crab22_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 23:
            $ crab_standin_health = crab23_hp
            $ crab_max_health = crab23_hp
            $ crab_name = crab23_name
            $ crab_level = crab23_level
            $ crab23_active = True
            show crab23_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 24:
            $ crab_standin_health = crab24_hp
            $ crab_max_health = crab24_hp
            $ crab_name = crab24_name
            $ crab_level = crab24_level
            $ crab24_active = True
            show crab24_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 25:
            $ crab_standin_health = crab25_hp
            $ crab_max_health = crab25_hp
            $ crab_name = crab25_name
            $ crab_level = crab25_level
            $ crab25_active = True
            show crab25_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 26:
            $ crab_standin_health = crab26_hp
            $ crab_max_health = crab26_hp
            $ crab_name = crab26_name
            $ crab_level = crab26_level
            $ crab26_active = True
            show crab26_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 27:
            $ crab_standin_health = crab27_hp
            $ crab_max_health = crab27_hp
            $ crab_name = crab27_name
            $ crab_level = crab27_level
            $ crab27_active = True
            show crab27_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 28:
            $ crab_standin_health = crab28_hp
            $ crab_max_health = crab28_hp
            $ crab_name = crab28_name
            $ crab_level = crab28_level
            $ crab28_active = True
            show crab28_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 29:
            $ crab_standin_health = crab29_hp
            $ crab_max_health = crab29_hp
            $ crab_name = crab29_name
            $ crab_level = crab29_level
            $ crab29_active = True
            show crab29_shuffle:
                xpos -250 ypos -200
        if crab_spot4 == 30:
            $ crab_standin_health = crab30_hp
            $ crab_max_health = crab30_hp
            $ crab_name = crab30_name
            $ crab_level = crab30_level
            $ crab30_active = True
            show crab30_shuffle:
                xpos -250 ypos -200
    elif crab_spot5_chosen:
        if crab_spot5 == 1:
            $ crab_standin_health = crab1_hp
            $ crab_max_health = crab1_hp
            $ crab_name = crab1_name
            $ crab_level = crab1_level
            $ crab1_active = True
            show crab1_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 2:
            $ crab_standin_health = crab2_hp
            $ crab_max_health = crab2_hp
            $ crab_name = crab2_name
            $ crab_level = crab2_level
            $ crab2_active = True
            show crab2_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 3:
            $ crab_standin_health = crab3_hp
            $ crab_max_health = crab3_hp
            $ crab_name = crab3_name
            $ crab_level = crab3_level
            $ crab3_active = True
            show crab3_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 4:
            $ crab_standin_health = crab4_hp
            $ crab_max_health = crab4_hp
            $ crab_name = crab4_name
            $ crab_level = crab4_level
            $ crab4_active = True
            show crab4_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 5:
            $ crab_standin_health = crab5_hp
            $ crab_max_health = crab5_hp
            $ crab_name = crab5_name
            $ crab_level = crab5_level
            $ crab5_active = True
            show crab5_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 6:
            $ crab_standin_health = crab6_hp
            $ crab_max_health = crab6_hp
            $ crab_name = crab6_name
            $ crab_level = crab6_level
            $ crab6_active = True
            show crab6_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 7:
            $ crab_standin_health = crab7_hp
            $ crab_max_health = crab7_hp
            $ crab_name = crab7_name
            $ crab_level = crab7_level
            $ crab7_active = True
            show crab7_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 8:
            $ crab_standin_health = crab8_hp
            $ crab_max_health = crab8_hp
            $ crab_name = crab8_name
            $ crab_level = crab8_level
            $ crab8_active = True
            show crab8_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 9:
            $ crab_standin_health = crab9_hp
            $ crab_max_health = crab9_hp
            $ crab_name = crab9_name
            $ crab_level = crab9_level
            $ crab9_active = True
            show crab9_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 10:
            $ crab_standin_health = crab10_hp
            $ crab_max_health = crab10_hp
            $ crab_name = crab10_name
            $ crab_level = crab10_level
            $ crab10_active = True
            show crab10_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 11:
            $ crab_standin_health = crab11_hp
            $ crab_max_health = crab11_hp
            $ crab_name = crab11_name
            $ crab_level = crab11_level
            $ crab11_active = True
            show crab11_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 12:
            $ crab_standin_health = crab12_hp
            $ crab_max_health = crab12_hp
            $ crab_name = crab12_name
            $ crab_level = crab12_level
            $ crab12_active = True
            show crab12_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 13:
            $ crab_standin_health = crab13_hp
            $ crab_max_health = crab13_hp
            $ crab_name = crab13_name
            $ crab_level = crab13_level
            $ crab13_active = True
            show crab13_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 14:
            $ crab_standin_health = crab14_hp
            $ crab_max_health = crab14_hp
            $ crab_name = crab14_name
            $ crab_level = crab14_level
            $ crab14_active = True
            show crab14_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 15:
            $ crab_standin_health = crab15_hp
            $ crab_max_health = crab15_hp
            $ crab_name = crab15_name
            $ crab_level = crab15_level
            $ crab15_active = True
            show crab15_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 16:
            $ crab_standin_health = crab16_hp
            $ crab_max_health = crab16_hp
            $ crab_name = crab16_name
            $ crab_level = crab16_level
            $ crab16_active = True
            show crab16_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 17:
            $ crab_standin_health = crab17_hp
            $ crab_max_health = crab17_hp
            $ crab_name = crab17_name
            $ crab_level = crab17_level
            $ crab17_active = True
            show crab17_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 18:
            $ crab_standin_health = crab18_hp
            $ crab_max_health = crab18_hp
            $ crab_name = crab18_name
            $ crab_level = crab18_level
            $ crab18_active = True
            show crab18_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 19:
            $ crab_standin_health = crab19_hp
            $ crab_max_health = crab19_hp
            $ crab_name = crab19_name
            $ crab_level = crab19_level
            $ crab19_active = True
            show crab19_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 20:
            $ crab_standin_health = crab20_hp
            $ crab_max_health = crab20_hp
            $ crab_name = crab20_name
            $ crab_level = crab20_level
            $ crab20_active = True
            show crab20_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 21:
            $ crab_standin_health = crab21_hp
            $ crab_max_health = crab21_hp
            $ crab_name = crab21_name
            $ crab_level = crab21_level
            $ crab21_active = True
            show crab21_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 22:
            $ crab_standin_health = crab22_hp
            $ crab_max_health = crab22_hp
            $ crab_name = crab22_name
            $ crab_level = crab22_level
            $ crab22_active = True
            show crab22_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 23:
            $ crab_standin_health = crab23_hp
            $ crab_max_health = crab23_hp
            $ crab_name = crab23_name
            $ crab_level = crab23_level
            $ crab23_active = True
            show crab23_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 24:
            $ crab_standin_health = crab24_hp
            $ crab_max_health = crab24_hp
            $ crab_name = crab24_name
            $ crab_level = crab24_level
            $ crab24_active = True
            show crab24_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 25:
            $ crab_standin_health = crab25_hp
            $ crab_max_health = crab25_hp
            $ crab_name = crab25_name
            $ crab_level = crab25_level
            $ crab25_active = True
            show crab25_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 26:
            $ crab_standin_health = crab26_hp
            $ crab_max_health = crab26_hp
            $ crab_name = crab26_name
            $ crab_level = crab26_level
            $ crab26_active = True
            show crab26_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 27:
            $ crab_standin_health = crab27_hp
            $ crab_max_health = crab27_hp
            $ crab_name = crab27_name
            $ crab_level = crab27_level
            $ crab27_active = True
            show crab27_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 28:
            $ crab_standin_health = crab28_hp
            $ crab_max_health = crab28_hp
            $ crab_name = crab28_name
            $ crab_level = crab28_level
            $ crab28_active = True
            show crab28_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 29:
            $ crab_standin_health = crab29_hp
            $ crab_max_health = crab29_hp
            $ crab_name = crab29_name
            $ crab_level = crab29_level
            $ crab29_active = True
            show crab29_shuffle:
                xpos -250 ypos -200
        if crab_spot5 == 30:
            $ crab_standin_health = crab30_hp
            $ crab_max_health = crab30_hp
            $ crab_name = crab30_name
            $ crab_level = crab30_level
            $ crab30_active = True
            show crab30_shuffle:
                xpos -250 ypos -200
    else:


        "you need crabs in order to battle!"
        jump arena_crab_battle
        "you don't have any crabs, so you square up like fuckin' rambo."
        ya "suck my nuts, crabs!"
        yc "....i hope nobody heard that."
        ya "it's go time!"
        $ crab_standin = False
        jump arena_crab_battle

    $ crabs_getting_exp = 1

    if crab1_active:
        $ crab1_exp = True
        $ crab_element = crab1_element
        $ crab_att = crab1_att
        $ crab_def = crab1_def
        $ crab_acc = crab1_acc
        $ crab_type = crab1_type
    if crab2_active:
        $ crab2_exp = True
        $ crab_element = crab2_element
        $ crab_att = crab2_att
        $ crab_def = crab2_def
        $ crab_acc = crab2_acc
        $ crab_type = crab2_type
    if crab3_active:
        $ crab3_exp = True
        $ crab_element = crab3_element
        $ crab_att = crab3_att
        $ crab_def = crab3_def
        $ crab_acc = crab3_acc
        $ crab_type = crab3_type
    if crab4_active:
        $ crab4_exp = True
        $ crab_element = crab4_element
        $ crab_att = crab4_att
        $ crab_def = crab4_def
        $ crab_acc = crab4_acc
        $ crab_type = crab4_type
    if crab5_active:
        $ crab5_exp = True
        $ crab_element = crab5_element
        $ crab_att = crab5_att
        $ crab_def = crab5_def
        $ crab_acc = crab5_acc
        $ crab_type = crab5_type
    if crab6_active:
        $ crab6_exp = True
        $ crab_element = crab6_element
        $ crab_att = crab6_att
        $ crab_def = crab6_def
        $ crab_acc = crab6_acc
        $ crab_type = crab6_type
    if crab7_active:
        $ crab7_exp = True
        $ crab_element = crab7_element
        $ crab_att = crab7_att
        $ crab_def = crab7_def
        $ crab_acc = crab7_acc
        $ crab_type = crab7_type
    if crab8_active:
        $ crab8_exp = True
        $ crab_element = crab8_element
        $ crab_att = crab8_att
        $ crab_def = crab8_def
        $ crab_acc = crab8_acc
        $ crab_type = crab8_type
    if crab9_active:
        $ crab9_exp = True
        $ crab_element = crab9_element
        $ crab_att = crab9_att
        $ crab_def = crab9_def
        $ crab_acc = crab9_acc
        $ crab_type = crab9_type
    if crab10_active:
        $ crab10_exp = True
        $ crab_element = crab10_element
        $ crab_att = crab10_att
        $ crab_def = crab10_def
        $ crab_acc = crab10_acc
        $ crab_type = crab10_type
    if crab11_active:
        $ crab11_exp = True
        $ crab_element = crab11_element
        $ crab_att = crab11_att
        $ crab_def = crab11_def
        $ crab_acc = crab11_acc
        $ crab_type = crab11_type
    if crab12_active:
        $ crab12_exp = True
        $ crab_element = crab12_element
        $ crab_att = crab12_att
        $ crab_def = crab12_def
        $ crab_acc = crab12_acc
        $ crab_type = crab12_type
    if crab13_active:
        $ crab13_exp = True
        $ crab_element = crab13_element
        $ crab_att = crab13_att
        $ crab_def = crab13_def
        $ crab_acc = crab13_acc
        $ crab_type = crab13_type
    if crab14_active:
        $ crab14_exp = True
        $ crab_element = crab14_element
        $ crab_att = crab14_att
        $ crab_def = crab14_def
        $ crab_acc = crab14_acc
        $ crab_type = crab14_type
    if crab15_active:
        $ crab15_exp = True
        $ crab_element = crab15_element
        $ crab_att = crab15_att
        $ crab_def = crab15_def
        $ crab_acc = crab15_acc
        $ crab_type = crab15_type
    if crab16_active:
        $ crab16_exp = True
        $ crab_element = crab16_element
        $ crab_att = crab16_att
        $ crab_def = crab16_def
        $ crab_acc = crab16_acc
        $ crab_type = crab16_type
    if crab17_active:
        $ crab17_exp = True
        $ crab_element = crab17_element
        $ crab_att = crab17_att
        $ crab_def = crab17_def
        $ crab_acc = crab17_acc
        $ crab_type = crab17_type
    if crab18_active:
        $ crab18_exp = True
        $ crab_element = crab18_element
        $ crab_att = crab18_att
        $ crab_def = crab18_def
        $ crab_acc = crab18_acc
        $ crab_type = crab18_type
    if crab19_active:
        $ crab19_exp = True
        $ crab_element = crab19_element
        $ crab_att = crab19_att
        $ crab_def = crab19_def
        $ crab_acc = crab19_acc
        $ crab_type = crab19_type
    if crab20_active:
        $ crab20_exp = True
        $ crab_element = crab20_element
        $ crab_att = crab20_att
        $ crab_def = crab20_def
        $ crab_acc = crab20_acc
        $ crab_type = crab20_type
    if crab21_active:
        $ crab21_exp = True
        $ crab_element = crab21_element
        $ crab_att = crab21_att
        $ crab_def = crab21_def
        $ crab_acc = crab21_acc
        $ crab_type = crab21_type
    if crab22_active:
        $ crab22_exp = True
        $ crab_element = crab22_element
        $ crab_att = crab22_att
        $ crab_def = crab22_def
        $ crab_acc = crab22_acc
        $ crab_type = crab22_type
    if crab23_active:
        $ crab23_exp = True
        $ crab_element = crab23_element
        $ crab_att = crab23_att
        $ crab_def = crab23_def
        $ crab_acc = crab23_acc
        $ crab_type = crab23_type
    if crab24_active:
        $ crab24_exp = True
        $ crab_element = crab24_element
        $ crab_att = crab24_att
        $ crab_def = crab24_def
        $ crab_acc = crab24_acc
        $ crab_type = crab24_type
    if crab25_active:
        $ crab25_exp = True
        $ crab_element = crab25_element
        $ crab_att = crab25_att
        $ crab_def = crab25_def
        $ crab_acc = crab25_acc
        $ crab_type = crab25_type
    if crab26_active:
        $ crab26_exp = True
        $ crab_element = crab26_element
        $ crab_att = crab26_att
        $ crab_def = crab26_def
        $ crab_acc = crab26_acc
        $ crab_type = crab26_type
    if crab27_active:
        $ crab27_exp = True
        $ crab_element = crab27_element
        $ crab_att = crab27_att
        $ crab_def = crab27_def
        $ crab_acc = crab27_acc
        $ crab_type = crab27_type
    if crab28_active:
        $ crab28_exp = True
        $ crab_element = crab28_element
        $ crab_att = crab28_att
        $ crab_def = crab28_def
        $ crab_acc = crab28_acc
        $ crab_type = crab28_type
    if crab29_active:
        $ crab29_exp = True
        $ crab_element = crab29_element
        $ crab_att = crab29_att
        $ crab_def = crab29_def
        $ crab_acc = crab29_acc
        $ crab_type = crab29_type
    if crab30_active:
        $ crab30_exp = True
        $ crab_element = crab30_element
        $ crab_att = crab30_att
        $ crab_def = crab30_def
        $ crab_acc = crab30_acc
        $ crab_type = crab30_type

    $ crab_standin = True

    $ crab1_temp_hp = crab1_hp
    $ crab2_temp_hp = crab2_hp
    $ crab3_temp_hp = crab3_hp
    $ crab4_temp_hp = crab4_hp
    $ crab5_temp_hp = crab5_hp
    $ crab6_temp_hp = crab6_hp
    $ crab7_temp_hp = crab7_hp
    $ crab8_temp_hp = crab8_hp
    $ crab9_temp_hp = crab9_hp
    $ crab10_temp_hp = crab10_hp
    $ crab11_temp_hp = crab11_hp
    $ crab12_temp_hp = crab12_hp
    $ crab13_temp_hp = crab13_hp
    $ crab14_temp_hp = crab14_hp
    $ crab15_temp_hp = crab15_hp
    $ crab16_temp_hp = crab16_hp
    $ crab17_temp_hp = crab17_hp
    $ crab18_temp_hp = crab18_hp
    $ crab19_temp_hp = crab19_hp
    $ crab20_temp_hp = crab20_hp
    $ crab21_temp_hp = crab21_hp
    $ crab22_temp_hp = crab22_hp
    $ crab23_temp_hp = crab23_hp
    $ crab24_temp_hp = crab24_hp
    $ crab25_temp_hp = crab25_hp
    $ crab26_temp_hp = crab26_hp
    $ crab27_temp_hp = crab27_hp
    $ crab28_temp_hp = crab28_hp
    $ crab29_temp_hp = crab29_hp
    $ crab30_temp_hp = crab30_hp

    jump arena_crab_battle

label arena_crab_battle:
    $ enemy_crab1_hp = 0
    $ enemy_crab2_hp = 0
    $ enemy_crab3_hp = 0
    $ enemy_crab4_hp = 0
    $ enemy_crab5_hp = 0
    if crab_hunt2:
        if anka_arena_battle:
            $ opp_name = "anka"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 10
            $ enemy_crab1_type = "6"
            $ enemy_crab1_rarity = "e"


            $ enemy_crab2_level = 15
            $ enemy_crab2_type = "3"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 20
            $ enemy_crab3_type = "10"
            $ enemy_crab3_rarity = "e"

            jump arena_crab_battle_cont
        else:

            $ arena_crab = 1
            $ total_enemy_crabs = 1
            $ opp_name = "wild crab"
            $ rand_enemy_crab1_type = renpy.random.randint(1,11)
            $ enemy_crab1_rarity = WeightedChoice([("n", 0.5), ("r", 0.4), ("e", 0.1)])
            $ enemy_crab1_level = renpy.random.randint(5,15)
            if rand_enemy_crab1_type == 1:
                $ enemy_crab1_type = "1"
            if rand_enemy_crab1_type == 2:
                $ enemy_crab1_type = "2"
            if rand_enemy_crab1_type == 3:
                $ enemy_crab1_type = "3"
            if rand_enemy_crab1_type == 4:
                $ enemy_crab1_type = "4"
            if rand_enemy_crab1_type == 5:
                $ enemy_crab1_type = "5"
            if rand_enemy_crab1_type == 6:
                $ enemy_crab1_type = "6"
            if rand_enemy_crab1_type == 7:
                $ enemy_crab1_type = "7"
            if rand_enemy_crab1_type == 8:
                $ enemy_crab1_type = "8"
            if rand_enemy_crab1_type == 9:
                $ enemy_crab1_type = "9"
            if rand_enemy_crab1_type == 10:
                $ enemy_crab1_type = "10"
            if rand_enemy_crab1_type == 11:
                $ enemy_crab1_type = "11"

            jump arena_crab_battle_cont

    if crab_hunt:
        if ultimate_arena_battle:
            $ opp_name = "girl"
            $ arena_crab = 1
            $ total_enemy_crabs = 1


            $ enemy_crab1_level = 99
            $ enemy_crab1_type = "11"
            $ enemy_crab1_rarity = "l"
        else:


















            $ arena_crab = 1
            $ total_enemy_crabs = 1
            $ opp_name = "wild crab"
            $ rand_enemy_crab1_type = renpy.random.randint(1,11)
            $ enemy_crab1_rarity = WeightedChoice([("n", 0.5), ("r", 0.4), ("e", 0.1)])
            $ enemy_crab1_level = renpy.random.randint(1,5)
            if rand_enemy_crab1_type == 1:
                $ enemy_crab1_type = "1"
            if rand_enemy_crab1_type == 2:
                $ enemy_crab1_type = "2"
            if rand_enemy_crab1_type == 3:
                $ enemy_crab1_type = "3"
            if rand_enemy_crab1_type == 4:
                $ enemy_crab1_type = "4"
            if rand_enemy_crab1_type == 5:
                $ enemy_crab1_type = "5"
            if rand_enemy_crab1_type == 6:
                $ enemy_crab1_type = "6"
            if rand_enemy_crab1_type == 7:
                $ enemy_crab1_type = "7"
            if rand_enemy_crab1_type == 8:
                $ enemy_crab1_type = "8"
            if rand_enemy_crab1_type == 9:
                $ enemy_crab1_type = "9"
            if rand_enemy_crab1_type == 10:
                $ enemy_crab1_type = "10"
            if rand_enemy_crab1_type == 11:
                $ enemy_crab1_type = "11"
    else:











        if iroh_fun_battle:
            if iroh_battle_count ==0:
                $ opp_name = "iroh"
                $ arena_crab = 1
                $ total_enemy_crabs = 1


                $ enemy_crab1_level = 6
                $ enemy_crab1_type = "8"
                $ enemy_crab1_rarity = "e"
                jump arena_crab_battle_cont

            if iroh_battle_count ==1:
                $ opp_name = "iroh"
                $ arena_crab = 1
                $ total_enemy_crabs = 1


                $ enemy_crab1_level = 9
                $ enemy_crab1_type = "8"
                $ enemy_crab1_rarity = "e"
                jump arena_crab_battle_cont

            if iroh_battle_count ==2:
                $ opp_name = "iroh"
                $ arena_crab = 1
                $ total_enemy_crabs = 2


                $ enemy_crab1_level = 14
                $ enemy_crab1_type = "8"
                $ enemy_crab1_rarity = "e"


                $ enemy_crab2_level = 5
                $ enemy_crab2_type = "9"
                $ enemy_crab2_rarity = "e"
                jump arena_crab_battle_cont

            if iroh_battle_count ==3:
                $ opp_name = "iroh"
                $ arena_crab = 1
                $ total_enemy_crabs = 3


                $ enemy_crab1_level = 18
                $ enemy_crab1_type = "8"
                $ enemy_crab1_rarity = "e"


                $ enemy_crab2_level = 12
                $ enemy_crab2_type = "9"
                $ enemy_crab2_rarity = "e"


                $ enemy_crab3_level = 9
                $ enemy_crab3_type = "10"
                $ enemy_crab3_rarity = "e"
                jump arena_crab_battle_cont

            if iroh_battle_count ==4:
                $ opp_name = "iroh"
                $ arena_crab = 1
                $ total_enemy_crabs = 3


                $ enemy_crab1_level = 22
                $ enemy_crab1_type = "8"
                $ enemy_crab1_rarity = "e"


                $ enemy_crab2_level = 18
                $ enemy_crab2_type = "9"
                $ enemy_crab2_rarity = "e"


                $ enemy_crab3_level = 16
                $ enemy_crab3_type = "10"
                $ enemy_crab3_rarity = "e"
                jump arena_crab_battle_cont

            if iroh_battle_count ==5:
                $ opp_name = "iroh"
                $ arena_crab = 1
                $ total_enemy_crabs = 4


                $ enemy_crab1_level = 28
                $ enemy_crab1_type = "8"
                $ enemy_crab1_rarity = "e"


                $ enemy_crab2_level = 24
                $ enemy_crab2_type = "9"
                $ enemy_crab2_rarity = "e"


                $ enemy_crab3_level = 20
                $ enemy_crab3_type = "10"
                $ enemy_crab3_rarity = "e"


                $ enemy_crab4_level = 18
                $ enemy_crab4_type = "7"
                $ enemy_crab4_rarity = "e"
                jump arena_crab_battle_cont

        if arena_enemy == 1:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 1


            $ enemy_crab1_level = 2
            $ enemy_crab1_type = "6"
            $ enemy_crab1_rarity = "n"










            $ enemy_crab2_level = 2
            $ enemy_crab2_type = "9"
            $ enemy_crab2_rarity = "n"




















        if arena_enemy == 2:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 2


            $ enemy_crab1_level = 2
            $ enemy_crab1_type = "4"
            $ enemy_crab1_rarity = "n"


            $ enemy_crab2_level = 4
            $ enemy_crab2_type = "9"
            $ enemy_crab2_rarity = "n"

        if arena_enemy == 3:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 2


            $ enemy_crab1_level = 3
            $ enemy_crab1_type = "4"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 4
            $ enemy_crab2_type = "2"
            $ enemy_crab2_rarity = "n"

        if arena_enemy == 4:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 2


            $ enemy_crab1_level = 4
            $ enemy_crab1_type = "9"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 5
            $ enemy_crab2_type = "8"
            $ enemy_crab2_rarity = "r"

        if arena_enemy == 5:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 1


            $ enemy_crab1_level = 8
            $ enemy_crab1_type = "10"
            $ enemy_crab1_rarity = "r"

        if arena_enemy == 6:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 2


            $ enemy_crab1_level = 6
            $ enemy_crab1_type = "5"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 8
            $ enemy_crab2_type = "11"
            $ enemy_crab2_rarity = "n"

        if arena_enemy == 7:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 2


            $ enemy_crab1_level = 9
            $ enemy_crab1_type = "9"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 8
            $ enemy_crab2_type = "8"
            $ enemy_crab2_rarity = "r"

        if arena_enemy == 8:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 6
            $ enemy_crab1_type = "6"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 3
            $ enemy_crab2_type = "3"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 6
            $ enemy_crab3_type = "6"
            $ enemy_crab3_rarity = "n"

        if arena_enemy ==9:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 10
            $ enemy_crab1_type = "6"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 4
            $ enemy_crab2_type = "3"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 8
            $ enemy_crab3_type = "6"
            $ enemy_crab3_rarity = "n"

        if arena_enemy ==10:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 14
            $ enemy_crab1_type = "3"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 7
            $ enemy_crab2_type = "1"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 12
            $ enemy_crab3_type = "6"
            $ enemy_crab3_rarity = "n"

        if arena_enemy ==11:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 15
            $ enemy_crab1_type = "9"
            $ enemy_crab1_rarity = "n"


            $ enemy_crab2_level = 8
            $ enemy_crab2_type = "7"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 10
            $ enemy_crab3_type = "6"
            $ enemy_crab3_rarity = "r"

        if arena_enemy ==12:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 20
            $ enemy_crab1_type = "10"
            $ enemy_crab1_rarity = "n"


            $ enemy_crab2_level = 10
            $ enemy_crab2_type = "5"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 14
            $ enemy_crab3_type = "8"
            $ enemy_crab3_rarity = "r"

        if arena_enemy ==13:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 2


            $ enemy_crab1_level = 15
            $ enemy_crab1_type = "2"
            $ enemy_crab1_rarity = "e"


            $ enemy_crab2_level = 15
            $ enemy_crab2_type = "3"
            $ enemy_crab2_rarity = "e"

        if arena_enemy ==14:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 4


            $ enemy_crab1_level = 15
            $ enemy_crab1_type = "10"
            $ enemy_crab1_rarity = "e"


            $ enemy_crab2_level = 10
            $ enemy_crab2_type = "6"
            $ enemy_crab2_rarity = "r"


            $ enemy_crab3_level = 14
            $ enemy_crab3_type = "11"
            $ enemy_crab3_rarity = "r"

            $ enemy_crab3_level = 23
            $ enemy_crab3_type = "4"
            $ enemy_crab3_rarity = "r"

        if arena_enemy ==14:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 20
            $ enemy_crab1_type = "6"
            $ enemy_crab1_rarity = "e"


            $ enemy_crab2_level = 13
            $ enemy_crab2_type = "6"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 25
            $ enemy_crab3_type = "7"
            $ enemy_crab3_rarity = "r"

        if arena_enemy ==15:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 20
            $ enemy_crab1_type = "1"
            $ enemy_crab1_rarity = "e"


            $ enemy_crab2_level = 18
            $ enemy_crab2_type = "3"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 32
            $ enemy_crab3_type = "8"
            $ enemy_crab3_rarity = "r"

        if arena_enemy ==16:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 4


            $ enemy_crab1_level = 34
            $ enemy_crab1_type = "9"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 18
            $ enemy_crab2_type = "10"
            $ enemy_crab2_rarity = "r"


            $ enemy_crab3_level = 25
            $ enemy_crab3_type = "4"
            $ enemy_crab3_rarity = "e"

            $ enemy_crab3_level = 50
            $ enemy_crab3_type = "10"
            $ enemy_crab3_rarity = "n"

        if arena_enemy ==17:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 4


            $ enemy_crab1_level = 40
            $ enemy_crab1_type = "9"
            $ enemy_crab1_rarity = "r"


            $ enemy_crab2_level = 22
            $ enemy_crab2_type = "10"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 30
            $ enemy_crab3_type = "4"
            $ enemy_crab3_rarity = "e"

            $ enemy_crab3_level = 45
            $ enemy_crab3_type = "1"
            $ enemy_crab3_rarity = "n"

        if arena_enemy ==17:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ total_enemy_crabs = 3


            $ enemy_crab1_level = 25
            $ enemy_crab1_type = "6"
            $ enemy_crab1_rarity = "e"


            $ enemy_crab2_level = 22
            $ enemy_crab2_type = "7"
            $ enemy_crab2_rarity = "e"


            $ enemy_crab3_level = 30
            $ enemy_crab3_type = "2"
            $ enemy_crab3_rarity = "e"

        if arena_enemy >=18 and arena_enemy <=30:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ rand_enemy_crabs = renpy.random.randint(2, 5)
            $ total_enemy_crabs = rand_enemy_crabs


            $ enemy_crab1_level = renpy.random.randint(20, 40)

            $ enemy_crab1_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])

            $ enemy_crab1_rarity = WeightedChoice([("n", 0.25), ("r", 0.375), ("e", 0.375)])


            if total_enemy_crabs >=2:

                $ enemy_crab2_level = renpy.random.randint(20, 40)
                $ enemy_crab2_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab2_rarity = WeightedChoice([("n", 0.25), ("r", 0.375), ("e", 0.375)])

            if total_enemy_crabs >=3:

                $ enemy_crab3_level = renpy.random.randint(20, 40)
                $ enemy_crab3_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab3_rarity = WeightedChoice([("n", 0.25), ("r", 0.375), ("e", 0.375)])

            if total_enemy_crabs >=4:

                $ enemy_crab4_level = renpy.random.randint(20, 40)
                $ enemy_crab4_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab4_rarity = WeightedChoice([("n", 0.25), ("r", 0.375), ("e", 0.375)])

            if total_enemy_crabs >=5:

                $ enemy_crab5_level = renpy.random.randint(20, 40)
                $ enemy_crab5_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab5_rarity = WeightedChoice([("n", 0.25), ("r", 0.375), ("e", 0.375)])


        if arena_enemy >= 31:
            $ opp_name = "shady"
            $ arena_crab = 1
            $ rand_enemy_crabs = renpy.random.randint(3, 5)
            $ total_enemy_crabs = rand_enemy_crabs


            $ enemy_crab1_level = renpy.random.randint(40, 99)
            $ enemy_crab1_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
            $ enemy_crab1_rarity = WeightedChoice([("n", 0.15), ("r", 0.3), ("e", 0.55)])

            if total_enemy_crabs >=2:

                $ enemy_crab2_level = renpy.random.randint(40, 99)
                $ enemy_crab2_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab2_rarity = WeightedChoice([("n", 0.15), ("r", 0.3), ("e", 0.55)])

            if total_enemy_crabs >=3:

                $ enemy_crab3_level = renpy.random.randint(40, 99)
                $ enemy_crab3_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab3_rarity = WeightedChoice([("n", 0.15), ("r", 0.3), ("e", 0.55)])

            if total_enemy_crabs >=4:

                $ enemy_crab4_level = renpy.random.randint(40, 99)
                $ enemy_crab4_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab4_rarity = WeightedChoice([("n", 0.15), ("r", 0.3), ("e", 0.55)])

            if total_enemy_crabs >=5:

                $ enemy_crab5_level = renpy.random.randint(40, 99)
                $ enemy_crab5_type = WeightedChoice([("1", 0.09), ("2", 0.09), ("3", 0.09), ("4", 0.09), ("5", 0.1), ("6", 0.09), ("7", 0.09), ("8", 0.09), ("9", 0.09), ("10", 0.09), ("11", 0.09),])
                $ enemy_crab5_rarity = WeightedChoice([("n", 0.15), ("r", 0.3), ("e", 0.55)])

    jump arena_crab_battle_cont

label arena_crab_battle_cont:
    if enemy_crab1_type =="1":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_health_max = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_element_crab1 = "fire"
            $ opp_def_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_name = "slasher"
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "slasher"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "slasher"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 24 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "slasher"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 25 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="2":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "reacher"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "reacher"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "reacher"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 24 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "reacher"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 25 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="3":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "jacko"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_def_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_att_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "jacko"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 26 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "jacko"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 27 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "jacko"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 28 + ((enemy_crab1_level-1)*8)
            $ opp_def_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="4":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "julienne"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "julienne"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 26 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_def_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "julienne"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 27 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_def_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "julienne"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 28 + ((enemy_crab1_level-1)*8)
            $ enemy_crab1_hp = enemy_crab1_health_max
            $ opp_def_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
    if enemy_crab1_type =="5":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "slycer"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 17 + ((enemy_crab1_level-1)*3)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "slycer"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "slycer"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 21 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "slycer"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 22 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ opp_def_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="6":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "clypper"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_def_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "clypper"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_def_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "clypper"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 24 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "clypper"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 25 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="7":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "barnakel"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_def_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "barnakel"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 26 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_def_crab1 = 29 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "barnakel"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 27 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 30 + ((enemy_crab1_level-1)*8)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "barnakel"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 28 + ((enemy_crab1_level-1)*8)
            $ opp_att_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 31 + ((enemy_crab1_level-1)*9)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="8":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "doo'ahlai"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "doo'ahlai"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 26 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "doo'ahlai"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 27 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "doo'ahlai"
            $ opp_element_crab1 = "air"
            $ enemy_crab1_health_max = 28 + ((enemy_crab1_level-1)*8)
            $ opp_att_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ opp_def_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="9":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "clawp"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "clawp"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "clawp"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 24 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "clawp"
            $ opp_element_crab1 = "water"
            $ enemy_crab1_health_max = 25 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="10":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "bampy"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 20 + ((enemy_crab1_level-1)*4)
            $ opp_att_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "bampy"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_def_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "bampy"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 24 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 24 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "bampy"
            $ opp_element_crab1 = "earth"
            $ enemy_crab1_health_max = 21 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 25 + ((enemy_crab1_level-1)*7)
            $ opp_acc_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max
    if enemy_crab1_type =="11":
        if enemy_crab1_rarity == "n":
            $ enemy_crab1_name = "grappy"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 23 + ((enemy_crab1_level-1)*5)
            $ opp_att_crab1 = 23 + ((enemy_crab1_level-1)*5)
            $ opp_def_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ opp_acc_crab1 = 17 + ((enemy_crab1_level-1)*3)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "r":
            $ enemy_crab1_name = "grappy"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 26 + ((enemy_crab1_level-1)*6)
            $ opp_att_crab1 = 26 + ((enemy_crab1_level-1)*6)
            $ opp_def_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ opp_acc_crab1 = 20 + ((enemy_crab1_level-1)*4)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "e":
            $ enemy_crab1_name = "grappy"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 27 + ((enemy_crab1_level-1)*7)
            $ opp_att_crab1 = 27 + ((enemy_crab1_level-1)*7)
            $ opp_def_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ opp_acc_crab1 = 21 + ((enemy_crab1_level-1)*5)
            $ enemy_crab1_hp = enemy_crab1_health_max
        if enemy_crab1_rarity == "l":
            $ enemy_crab1_name = "grappy"
            $ opp_element_crab1 = "fire"
            $ enemy_crab1_health_max = 28 + ((enemy_crab1_level-1)*8)
            $ opp_att_crab1 = 28 + ((enemy_crab1_level-1)*8)
            $ opp_def_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ opp_acc_crab1 = 22 + ((enemy_crab1_level-1)*6)
            $ enemy_crab1_hp = enemy_crab1_health_max


    if enemy_crab2_type =="1":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_health_max = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_element_crab2 = "fire"
            $ opp_def_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_name = "slasher"
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "slasher"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "slasher"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 24 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "slasher"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 25 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="2":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "reacher"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "reacher"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "reacher"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 24 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "reacher"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 25 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="3":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "jacko"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_def_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_att_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "jacko"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 26 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "jacko"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 27 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "jacko"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 28 + ((enemy_crab2_level-1)*8)
            $ opp_def_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="4":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "julienne"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "julienne"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 26 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_def_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "julienne"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 27 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_def_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "julienne"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 28 + ((enemy_crab2_level-1)*8)
            $ enemy_crab2_hp = enemy_crab2_health_max
            $ opp_def_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
    if enemy_crab2_type =="5":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "slycer"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 17 + ((enemy_crab2_level-1)*3)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "slycer"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "slycer"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 21 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "slycer"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 22 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ opp_def_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="6":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "clypper"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_def_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "clypper"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_def_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "clypper"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 24 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "clypper"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 25 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="7":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "barnakel"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_def_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "barnakel"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 26 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_def_crab2 = 29 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "barnakel"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 27 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 30 + ((enemy_crab2_level-1)*8)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "barnakel"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 28 + ((enemy_crab2_level-1)*8)
            $ opp_att_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 31 + ((enemy_crab2_level-1)*9)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="8":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "doo'ahlai"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "doo'ahlai"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 26 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "doo'ahlai"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 27 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "doo'ahlai"
            $ opp_element_crab2 = "air"
            $ enemy_crab2_health_max = 28 + ((enemy_crab2_level-1)*8)
            $ opp_att_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ opp_def_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="9":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "clawp"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "clawp"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "clawp"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 24 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "clawp"
            $ opp_element_crab2 = "water"
            $ enemy_crab2_health_max = 25 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="10":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "bampy"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 20 + ((enemy_crab2_level-1)*4)
            $ opp_att_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "bampy"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_def_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "bampy"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 24 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 24 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "bampy"
            $ opp_element_crab2 = "earth"
            $ enemy_crab2_health_max = 21 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 25 + ((enemy_crab2_level-1)*7)
            $ opp_acc_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max
    if enemy_crab2_type =="11":
        if enemy_crab2_rarity == "n":
            $ enemy_crab2_name = "grappy"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 23 + ((enemy_crab2_level-1)*5)
            $ opp_att_crab2 = 23 + ((enemy_crab2_level-1)*5)
            $ opp_def_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ opp_acc_crab2 = 17 + ((enemy_crab2_level-1)*3)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "r":
            $ enemy_crab2_name = "grappy"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 26 + ((enemy_crab2_level-1)*6)
            $ opp_att_crab2 = 26 + ((enemy_crab2_level-1)*6)
            $ opp_def_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ opp_acc_crab2 = 20 + ((enemy_crab2_level-1)*4)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "e":
            $ enemy_crab2_name = "grappy"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 27 + ((enemy_crab2_level-1)*7)
            $ opp_att_crab2 = 27 + ((enemy_crab2_level-1)*7)
            $ opp_def_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ opp_acc_crab2 = 21 + ((enemy_crab2_level-1)*5)
            $ enemy_crab2_hp = enemy_crab2_health_max
        if enemy_crab2_rarity == "l":
            $ enemy_crab2_name = "grappy"
            $ opp_element_crab2 = "fire"
            $ enemy_crab2_health_max = 28 + ((enemy_crab2_level-1)*8)
            $ opp_att_crab2 = 28 + ((enemy_crab2_level-1)*8)
            $ opp_def_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ opp_acc_crab2 = 22 + ((enemy_crab2_level-1)*6)
            $ enemy_crab2_hp = enemy_crab2_health_max

    if enemy_crab3_type =="1":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_health_max = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_element_crab3 = "fire"
            $ opp_def_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_name = "slasher"
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "slasher"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "slasher"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 24 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "slasher"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 25 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="2":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "reacher"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "reacher"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "reacher"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 24 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "reacher"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 25 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="3":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "jacko"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_def_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_att_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "jacko"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 26 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "jacko"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 27 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "jacko"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 28 + ((enemy_crab3_level-1)*8)
            $ opp_def_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="4":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "julienne"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "julienne"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 26 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_def_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "julienne"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 27 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_def_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "julienne"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 28 + ((enemy_crab3_level-1)*8)
            $ enemy_crab3_hp = enemy_crab3_health_max
            $ opp_def_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
    if enemy_crab3_type =="5":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "slycer"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 17 + ((enemy_crab3_level-1)*3)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "slycer"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "slycer"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 21 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "slycer"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 22 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ opp_def_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="6":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "clypper"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_def_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "clypper"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_def_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "clypper"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 24 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "clypper"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 25 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="7":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "barnakel"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_def_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "barnakel"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 26 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_def_crab3 = 29 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "barnakel"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 27 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 30 + ((enemy_crab3_level-1)*8)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "barnakel"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 28 + ((enemy_crab3_level-1)*8)
            $ opp_att_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 31 + ((enemy_crab3_level-1)*9)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="8":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "doo'ahlai"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "doo'ahlai"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 26 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "doo'ahlai"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 27 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "doo'ahlai"
            $ opp_element_crab3 = "air"
            $ enemy_crab3_health_max = 28 + ((enemy_crab3_level-1)*8)
            $ opp_att_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ opp_def_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="9":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "clawp"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "clawp"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "clawp"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 24 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "clawp"
            $ opp_element_crab3 = "water"
            $ enemy_crab3_health_max = 25 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="10":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "bampy"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 20 + ((enemy_crab3_level-1)*4)
            $ opp_att_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "bampy"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_def_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "bampy"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 24 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 24 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "bampy"
            $ opp_element_crab3 = "earth"
            $ enemy_crab3_health_max = 21 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 25 + ((enemy_crab3_level-1)*7)
            $ opp_acc_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max
    if enemy_crab3_type =="11":
        if enemy_crab3_rarity == "n":
            $ enemy_crab3_name = "grappy"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 23 + ((enemy_crab3_level-1)*5)
            $ opp_att_crab3 = 23 + ((enemy_crab3_level-1)*5)
            $ opp_def_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ opp_acc_crab3 = 17 + ((enemy_crab3_level-1)*3)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "r":
            $ enemy_crab3_name = "grappy"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 26 + ((enemy_crab3_level-1)*6)
            $ opp_att_crab3 = 26 + ((enemy_crab3_level-1)*6)
            $ opp_def_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ opp_acc_crab3 = 20 + ((enemy_crab3_level-1)*4)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "e":
            $ enemy_crab3_name = "grappy"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 27 + ((enemy_crab3_level-1)*7)
            $ opp_att_crab3 = 27 + ((enemy_crab3_level-1)*7)
            $ opp_def_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ opp_acc_crab3 = 21 + ((enemy_crab3_level-1)*5)
            $ enemy_crab3_hp = enemy_crab3_health_max
        if enemy_crab3_rarity == "l":
            $ enemy_crab3_name = "grappy"
            $ opp_element_crab3 = "fire"
            $ enemy_crab3_health_max = 28 + ((enemy_crab3_level-1)*8)
            $ opp_att_crab3 = 28 + ((enemy_crab3_level-1)*8)
            $ opp_def_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ opp_acc_crab3 = 22 + ((enemy_crab3_level-1)*6)
            $ enemy_crab3_hp = enemy_crab3_health_max

    if enemy_crab4_type =="1":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_health_max = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_element_crab4 = "fire"
            $ opp_def_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_name = "slasher"
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "slasher"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "slasher"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 24 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "slasher"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 25 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="2":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "reacher"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "reacher"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "reacher"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 24 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "reacher"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 25 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="3":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "jacko"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_def_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_att_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "jacko"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 26 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "jacko"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 27 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "jacko"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 28 + ((enemy_crab4_level-1)*8)
            $ opp_def_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="4":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "julienne"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "julienne"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 26 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_def_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "julienne"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 27 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_def_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "julienne"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 28 + ((enemy_crab4_level-1)*8)
            $ enemy_crab4_hp = enemy_crab4_health_max
            $ opp_def_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
    if enemy_crab4_type =="5":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "slycer"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 17 + ((enemy_crab4_level-1)*3)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "slycer"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "slycer"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 21 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "slycer"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 22 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ opp_def_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="6":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "clypper"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_def_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "clypper"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_def_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "clypper"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 24 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "clypper"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 25 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="7":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "barnakel"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_def_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "barnakel"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 26 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_def_crab4 = 29 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "barnakel"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 27 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 30 + ((enemy_crab4_level-1)*8)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "barnakel"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 28 + ((enemy_crab4_level-1)*8)
            $ opp_att_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 31 + ((enemy_crab4_level-1)*9)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="8":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "doo'ahlai"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "doo'ahlai"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 26 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "doo'ahlai"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 27 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "doo'ahlai"
            $ opp_element_crab4 = "air"
            $ enemy_crab4_health_max = 28 + ((enemy_crab4_level-1)*8)
            $ opp_att_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ opp_def_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="9":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "clawp"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "clawp"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "clawp"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 24 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "clawp"
            $ opp_element_crab4 = "water"
            $ enemy_crab4_health_max = 25 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="10":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "bampy"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 20 + ((enemy_crab4_level-1)*4)
            $ opp_att_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "bampy"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_def_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "bampy"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 24 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 24 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "bampy"
            $ opp_element_crab4 = "earth"
            $ enemy_crab4_health_max = 21 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 25 + ((enemy_crab4_level-1)*7)
            $ opp_acc_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max
    if enemy_crab4_type =="11":
        if enemy_crab4_rarity == "n":
            $ enemy_crab4_name = "grappy"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 23 + ((enemy_crab4_level-1)*5)
            $ opp_att_crab4 = 23 + ((enemy_crab4_level-1)*5)
            $ opp_def_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ opp_acc_crab4 = 17 + ((enemy_crab4_level-1)*3)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "r":
            $ enemy_crab4_name = "grappy"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 26 + ((enemy_crab4_level-1)*6)
            $ opp_att_crab4 = 26 + ((enemy_crab4_level-1)*6)
            $ opp_def_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ opp_acc_crab4 = 20 + ((enemy_crab4_level-1)*4)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "e":
            $ enemy_crab4_name = "grappy"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 27 + ((enemy_crab4_level-1)*7)
            $ opp_att_crab4 = 27 + ((enemy_crab4_level-1)*7)
            $ opp_def_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ opp_acc_crab4 = 21 + ((enemy_crab4_level-1)*5)
            $ enemy_crab4_hp = enemy_crab4_health_max
        if enemy_crab4_rarity == "l":
            $ enemy_crab4_name = "grappy"
            $ opp_element_crab4 = "fire"
            $ enemy_crab4_health_max = 28 + ((enemy_crab4_level-1)*8)
            $ opp_att_crab4 = 28 + ((enemy_crab4_level-1)*8)
            $ opp_def_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ opp_acc_crab4 = 22 + ((enemy_crab4_level-1)*6)
            $ enemy_crab4_hp = enemy_crab4_health_max

    if enemy_crab5_type =="1":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_health_max = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_element_crab5 = "fire"
            $ opp_def_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_name = "slasher"
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "slasher"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "slasher"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 24 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "slasher"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 25 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="2":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "reacher"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "reacher"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "reacher"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 24 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "reacher"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 25 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="3":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "jacko"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_def_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_att_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "jacko"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 26 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "jacko"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 27 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "jacko"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 28 + ((enemy_crab5_level-1)*8)
            $ opp_def_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="4":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "julienne"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "julienne"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 26 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_def_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "julienne"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 27 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_def_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "julienne"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 28 + ((enemy_crab5_level-1)*8)
            $ enemy_crab5_hp = enemy_crab5_health_max
            $ opp_def_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
    if enemy_crab5_type =="5":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "slycer"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 17 + ((enemy_crab5_level-1)*3)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "slycer"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "slycer"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 21 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "slycer"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 22 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ opp_def_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="6":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "clypper"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_def_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "clypper"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_def_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "clypper"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 24 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "clypper"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 25 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="7":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "barnakel"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_def_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "barnakel"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 26 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_def_crab5 = 29 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "barnakel"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 27 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 30 + ((enemy_crab5_level-1)*8)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "barnakel"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 28 + ((enemy_crab5_level-1)*8)
            $ opp_att_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 31 + ((enemy_crab5_level-1)*9)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="8":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "doo'ahlai"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "doo'ahlai"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 26 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "doo'ahlai"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 27 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "doo'ahlai"
            $ opp_element_crab5 = "air"
            $ enemy_crab5_health_max = 28 + ((enemy_crab5_level-1)*8)
            $ opp_att_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ opp_def_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="9":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "clawp"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "clawp"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "clawp"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 24 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "clawp"
            $ opp_element_crab5 = "water"
            $ enemy_crab5_health_max = 25 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="10":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "bampy"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 20 + ((enemy_crab5_level-1)*4)
            $ opp_att_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "bampy"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_def_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "bampy"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 24 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 24 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "bampy"
            $ opp_element_crab5 = "earth"
            $ enemy_crab5_health_max = 21 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 25 + ((enemy_crab5_level-1)*7)
            $ opp_acc_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max
    if enemy_crab5_type =="11":
        if enemy_crab5_rarity == "n":
            $ enemy_crab5_name = "grappy"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 23 + ((enemy_crab5_level-1)*5)
            $ opp_att_crab5 = 23 + ((enemy_crab5_level-1)*5)
            $ opp_def_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ opp_acc_crab5 = 17 + ((enemy_crab5_level-1)*3)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "r":
            $ enemy_crab5_name = "grappy"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 26 + ((enemy_crab5_level-1)*6)
            $ opp_att_crab5 = 26 + ((enemy_crab5_level-1)*6)
            $ opp_def_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ opp_acc_crab5 = 20 + ((enemy_crab5_level-1)*4)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "e":
            $ enemy_crab5_name = "grappy"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 27 + ((enemy_crab5_level-1)*7)
            $ opp_att_crab5 = 27 + ((enemy_crab5_level-1)*7)
            $ opp_def_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ opp_acc_crab5 = 21 + ((enemy_crab5_level-1)*5)
            $ enemy_crab5_hp = enemy_crab5_health_max
        if enemy_crab5_rarity == "l":
            $ enemy_crab5_name = "grappy"
            $ opp_element_crab5 = "fire"
            $ enemy_crab5_health_max = 28 + ((enemy_crab5_level-1)*8)
            $ opp_att_crab5 = 28 + ((enemy_crab5_level-1)*8)
            $ opp_def_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ opp_acc_crab5 = 22 + ((enemy_crab5_level-1)*6)
            $ enemy_crab5_hp = enemy_crab5_health_max

    $ enemy_crab_type = enemy_crab1_type
    $ enemy_crab_rarity = enemy_crab1_rarity
    $ enemy_crab_health_max = enemy_crab1_health_max
    $ enemy_crab_level = enemy_crab1_level
    $ crab_health = enemy_crab1_hp
    $ opp_element = opp_element_crab1
    $ opp_def = opp_def_crab1
    $ opp_att = opp_att_crab1
    $ opp_acc = opp_acc_crab1
    $ enemy_crab_name = enemy_crab1_name

    if ultimate_arena_battle:
        $ enemy_crab1_name = "the beast"
        $ enemy_crab_name = enemy_crab1_name

    show screen bk3_crabstats1




    show enemy_crab_shuffle:
        xpos 180 ypos -400
    with dissolve

    if not crab_hunt and not crab_hunt2:
        "opponent [opp_name] sends out [enemy_crab_name]!"

    jump arena_crab_battle_player2


    if crab_player_health <=0:
        "you lose!"
        jump arena_crab_battle_lose
    else:
        if crab_acc >= opp_acc:
            jump arena_crab_battle_player2
        else:
            "enemy [enemy_crab_name] is faster! they move first!"
            jump enemy_crab_turn

label arena_crab_battle_player2:
    if crab_standin_health <=0:
        $ crab_charge = False
        $ crabs_alive -=1


        $ bk3_crabsalive_list = [0, crab1_temp_hp, crab2_temp_hp, crab3_temp_hp, crab4_temp_hp, crab5_temp_hp,
                            crab6_temp_hp, crab7_temp_hp, crab8_temp_hp, crab9_temp_hp, crab10_temp_hp,
                            
                            crab11_temp_hp, crab12_temp_hp, crab13_temp_hp, crab14_temp_hp, crab15_temp_hp,
                            crab16_temp_hp, crab17_temp_hp, crab18_temp_hp, crab19_temp_hp, crab20_temp_hp,
                            
                            crab21_temp_hp, crab22_temp_hp, crab23_temp_hp, crab24_temp_hp, crab25_temp_hp,
                            crab26_temp_hp, crab27_temp_hp, crab28_temp_hp, crab29_temp_hp, crab30_temp_hp]
        $ crabs_alive = 0

        if crab_spot1_chosen == True:
            if bk3_crabsalive_list[crab_spot1] >0:
                $ crabs_alive += 1
        if crab_spot2_chosen == True:
            if bk3_crabsalive_list[crab_spot2] >0:
                $ crabs_alive += 1
        if crab_spot3_chosen == True:
            if bk3_crabsalive_list[crab_spot3] >0:
                $ crabs_alive += 1
        if crab_spot4_chosen == True:
            if bk3_crabsalive_list[crab_spot4] >0:
                $ crabs_alive += 1
        if crab_spot5_chosen == True:
            if bk3_crabsalive_list[crab_spot5] >0:
                $ crabs_alive += 1



        if crabs_alive <= 0:
            jump arena_game_over
        else:
            jump arena_switch

    $ arena_active = True
    $ arena_fighting = False

    if a_poison >=1:
        $ a_poison -=1
        $ poison_hurt = math.ceil(enemy_crab_health_max*.1)
        $ crab_standin_health -= poison_hurt
        if crab1_active:
            $ crab1_temp_hp -= poison_hurt
        if crab2_active:
            $ crab2_temp_hp -= poison_hurt
        if crab3_active:
            $ crab3_temp_hp -= poison_hurt
        if crab4_active:
            $ crab4_temp_hp -= poison_hurt
        if crab5_active:
            $ crab5_temp_hp -= poison_hurt
        if crab6_active:
            $ crab6_temp_hp -= poison_hurt
        if crab7_active:
            $ crab7_temp_hp -= poison_hurt
        if crab8_active:
            $ crab8_temp_hp -= poison_hurt
        if crab9_active:
            $ crab9_temp_hp -= poison_hurt
        if crab10_active:
            $ crab10_temp_hp -= poison_hurt
        if crab11_active:
            $ crab11_temp_hp -= poison_hurt
        if crab12_active:
            $ crab12_temp_hp -= poison_hurt
        if crab13_active:
            $ crab13_temp_hp -= poison_hurt
        if crab14_active:
            $ crab14_temp_hp -= poison_hurt
        if crab15_active:
            $ crab15_temp_hp -= poison_hurt
        if crab16_active:
            $ crab16_temp_hp -= poison_hurt
        if crab17_active:
            $ crab17_temp_hp -= poison_hurt
        if crab18_active:
            $ crab18_temp_hp -= poison_hurt
        if crab19_active:
            $ crab19_temp_hp -= poison_hurt
        if crab20_active:
            $ crab20_temp_hp -= poison_hurt
        if crab21_active:
            $ crab21_temp_hp -= poison_hurt
        if crab22_active:
            $ crab22_temp_hp -= poison_hurt
        if crab23_active:
            $ crab23_temp_hp -= poison_hurt
        if crab24_active:
            $ crab24_temp_hp -= poison_hurt
        if crab25_active:
            $ crab25_temp_hp -= poison_hurt
        if crab26_active:
            $ crab26_temp_hp -= poison_hurt
        if crab27_active:
            $ crab27_temp_hp -= poison_hurt
        if crab28_active:
            $ crab28_temp_hp -= poison_hurt
        if crab29_active:
            $ crab29_temp_hp -= poison_hurt
        if crab30_active:
            $ crab30_temp_hp -= poison_hurt
        with vshake
        $ renpy.pause(0.25)
        "[crab_name] took poison damage!"
        if crab_standin_health <=0:
            jump arena_crab_battle_player2

    if a_bind >=1:
        $ a_bind -=1
        $ bind_chance = renpy.random.randint(1, 2)
        "[crab_name] is bound! they struggle against it!"
        with vshake
        $ renpy.pause(0.25)
        if bind_chance ==1:
            "[crab_name] broke through!"
        if bind_chance ==2:
            "[crab_name] can't move!"
            $ crab_charge = False

    if a_confuse >=1:
        $ a_confuse -=1
        $ confusion_chance = renpy.random.randint(1, 2)
        "[crab_name] is confused!"

        $ renpy.pause(0.25)
        if confusion_chance ==1:
            if bind_chance ==2:
                "[crab_name] is bound and can't move!"
            else:
                pass
        if confusion_chance ==2:
            $ a_confused = True









    if a_weak >=1:
        $ a_weak -=1
        "[crab_name] is weak!"
        $ crab_charge = False
        $ a_weakened = True

    if crab_charge:
        jump arena_charge_check

    jump arena_battle_screen

label arena_battle_screen:
    $ arena_active = True
    $ arena_fighting = False
    call screen arena_battle_buttons

label arena_crab_battle_next:


    $ enemy_crab1_type = "7"
    $ enemy_crab1_rarity = "n"
    $ enemy_crab1_health_max = 20
    $ enemy_crab1_hp = 20
    $ opp_element_crab1 = "water"
    $ opp_def_crab1 = 20
    $ enemy_crab1_level = 2


    $ enemy_crab2_type = "7"
    $ enemy_crab2_rarity = "n"
    $ enemy_crab2_health_max = 20
    $ enemy_crab2_hp = 20
    $ opp_element_crab2 = "water"
    $ opp_def_crab2 = 20
    $ enemy_crab2_level = 2

    if arena_crab ==1:
        $ enemy_crab_type = enemy_crab1_type
        $ enemy_crab_rarity = enemy_crab1_rarity
        $ enemy_crab_health_max = enemy_crab1_health_max
        $ enemy_crab_level = enemy_crab1_level
        $ crab_health = enemy_crab1_hp
        $ opp_element = opp_element_crab1
        $ opp_def = opp_def_crab1
    if arena_crab ==2:
        $ enemy_crab_type = enemy_crab2_type
        $ enemy_crab_rarity = enemy_crab2_rarity
        $ enemy_crab_health_max = enemy_crab2_health_max
        $ enemy_crab_level = enemy_crab2_level
        $ crab_health = enemy_crab2_hp
        $ opp_element = opp_element_crab2
        $ opp_def = opp_def_crab2
    if arena_crab ==3:
        $ enemy_crab_type = enemy_crab3_type
        $ enemy_crab_rarity = enemy_crab3_rarity
        $ enemy_crab_health_max = enemy_crab3_health_max
        $ enemy_crab_level = enemy_crab3_level
        $ crab_health = enemy_crab3_hp
        $ opp_element = opp_element_crab3
        $ opp_def = opp_def_crab3
    if arena_crab ==4:
        $ enemy_crab_type = enemy_crab4_type
        $ enemy_crab_rarity = enemy_crab4_rarity
        $ enemy_crab_health_max = enemy_crab4_health_max
        $ enemy_crab_level = enemy_crab4_level
        $ crab_health = enemy_crab4_hp
        $ opp_element = opp_element_crab4
        $ opp_def = opp_def_crab4
    if arena_crab ==5:
        $ enemy_crab_type = enemy_crab5_type
        $ enemy_crab_rarity = enemy_crab5_rarity
        $ enemy_crab_health_max = enemy_crab5_health_max
        $ enemy_crab_level = enemy_crab5_level
        $ crab_health = enemy_crab5_hp
        $ opp_element = opp_element_crab5
        $ opp_def = opp_def_crab5

    jump arena_crab_battle_player2

label arena_fight:
    if a_confused:
        $ a_confused = False
        with vshake
        $ confuse_hurt = math.ceil(enemy_crab_health_max*.1)
        $ crab_standin_health -= confuse_hurt
        if crab1_active:
            $ crab1_temp_hp -= confuse_hurt
        if crab2_active:
            $ crab2_temp_hp -= confuse_hurt
        if crab3_active:
            $ crab3_temp_hp -= confuse_hurt
        if crab4_active:
            $ crab4_temp_hp -= confuse_hurt
        if crab5_active:
            $ crab5_temp_hp -= confuse_hurt
        if crab6_active:
            $ crab6_temp_hp -= confuse_hurt
        if crab7_active:
            $ crab7_temp_hp -= confuse_hurt
        if crab8_active:
            $ crab8_temp_hp -= confuse_hurt
        if crab9_active:
            $ crab9_temp_hp -= confuse_hurt
        if crab10_active:
            $ crab10_temp_hp -= confuse_hurt
        if crab11_active:
            $ crab11_temp_hp -= confuse_hurt
        if crab12_active:
            $ crab12_temp_hp -= confuse_hurt
        if crab13_active:
            $ crab13_temp_hp -= confuse_hurt
        if crab14_active:
            $ crab14_temp_hp -= confuse_hurt
        if crab15_active:
            $ crab15_temp_hp -= confuse_hurt
        if crab16_active:
            $ crab16_temp_hp -= confuse_hurt
        if crab17_active:
            $ crab17_temp_hp -= confuse_hurt
        if crab18_active:
            $ crab18_temp_hp -= confuse_hurt
        if crab19_active:
            $ crab19_temp_hp -= confuse_hurt
        if crab20_active:
            $ crab20_temp_hp -= confuse_hurt
        if crab21_active:
            $ crab21_temp_hp -= confuse_hurt
        if crab22_active:
            $ crab22_temp_hp -= confuse_hurt
        if crab23_active:
            $ crab23_temp_hp -= confuse_hurt
        if crab24_active:
            $ crab24_temp_hp -= confuse_hurt
        if crab25_active:
            $ crab25_temp_hp -= confuse_hurt
        if crab26_active:
            $ crab26_temp_hp -= confuse_hurt
        if crab27_active:
            $ crab27_temp_hp -= confuse_hurt
        if crab28_active:
            $ crab28_temp_hp -= confuse_hurt
        if crab29_active:
            $ crab29_temp_hp -= confuse_hurt
        if crab30_active:
            $ crab30_temp_hp -= confuse_hurt
        $ crab_charge = False
        "[crab_name] is confused! it hurt itself in its confusion!"
        if crab_standin_health <=0:
            jump arena_crab_battle_player2
        else:
            jump enemy_crab_turn

    if a_weakened:
        with vshake
        "[crab_name] is weak!"
        jump arena_regular_attack

    $ arena_active = False
    $ arena_fighting = True
    call screen arena_battle_buttons



label arena_regular_attack:
    $ element_bonus = 1

    if crab_element == "earth" and opp_element == "fire":
        $ element_bonus = 1.3
    elif crab_element == "fire" and opp_element == "water":
        $ element_bonus = 1.3
    elif crab_element == "water" and opp_element == "earth":
        $ element_bonus = 1.3
    $ hit_chance = ((crab_acc - (crab_acc * (1 - ((crab_acc/4)*0.03))))*.01)

    $ level_ratio = (crab_level-enemy_crab_level)
    $ level_ratio2 = (enemy_crab_level-crab_level)

















    if level_ratio >=4:
        $ hit = math.ceil((((crab_att-level_ratio) - (opp_def+(level_ratio*5)))*element_bonus))
    if level_ratio >=0 and level_ratio <4:
        $ hit = math.ceil((((crab_att-level_ratio) - (opp_def+(level_ratio*4)))*element_bonus))
    else:
        if level_ratio2 <=-4:
            $ hit = math.ceil((((crab_att+(level_ratio2*5)) - (opp_def-level_ratio2))*element_bonus))
        else:
            $ hit = math.ceil((((crab_att+(level_ratio2*4)) - (opp_def-level_ratio2))*element_bonus))

    $ hit = math.ceil(((crab_att+opp_def)/opp_def)*(crab_level))
    if hit <=1:
        $ hit = 2


















































































































































































































































































































    jump arena_regular_attack_cont1

label arena_regular_attack_cont1:


    if hit_chance <=0.32:
        $ rand_accuracy = WeightedChoice([("low", 0.15), ("mediocre", 0.85)])
        if rand_accuracy == "low":
            $ arena_player_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.36:
        $ rand_accuracy = WeightedChoice([("low", 0.10), ("mediocre", 0.90)])
        if rand_accuracy == "low":
            $ arena_player_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.4:
        $ rand_accuracy = WeightedChoice([("low", 0.10), ("mediocre", 0.90)])
        if rand_accuracy == "low":
            $ arena_player_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.44:
        $ rand_accuracy = WeightedChoice([("high", 0.10), ("mediocre", 0.90)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.48:
        $ rand_accuracy = WeightedChoice([("high", 0.20), ("mediocre", 0.80)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.52:
        $ rand_accuracy = WeightedChoice([("high", 0.30), ("mediocre", 0.70)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.56:
        $ rand_accuracy = WeightedChoice([("high", 0.40), ("mediocre", 0.60)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.6:
        $ rand_accuracy = WeightedChoice([("high", 0.50), ("mediocre", 0.50)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.64:
        $ rand_accuracy = WeightedChoice([("high", 0.60), ("mediocre", 0.40)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.68:
        $ rand_accuracy = WeightedChoice([("high", 0.70), ("mediocre", 0.30)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.72:
        $ rand_accuracy = WeightedChoice([("high", 0.80), ("mediocre", 0.20)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.76:
        $ rand_accuracy = WeightedChoice([("high", 0.90), ("mediocre", 0.10)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_player_attack_chance = "mediocre"

    elif hit_chance <=0.8:
        $ rand_accuracy = WeightedChoice([("high", 0.90), ("ultimate", 0.10)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_player_attack_chance = "ultimate"

    elif hit_chance <=0.84:
        $ rand_accuracy = WeightedChoice([("high", 0.80), ("ultimate", 0.20)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_player_attack_chance = "ultimate"

    elif hit_chance <=0.88:
        $ rand_accuracy = WeightedChoice([("high", 0.70), ("ultimate", 0.30)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_player_attack_chance = "ultimate"

    elif hit_chance <=0.92:
        $ rand_accuracy = WeightedChoice([("high", 0.60), ("ultimate", 0.40)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_player_attack_chance = "ultimate"

    elif hit_chance <=0.96:
        $ rand_accuracy = WeightedChoice([("high", 0.50), ("ultimate", 0.50)])
        if rand_accuracy == "high":
            $ arena_player_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_player_attack_chance = "ultimate"
    else:

        $ arena_player_attack_chance = "ultimate"

    jump regular_arena_attack_cont2

label regular_arena_attack_cont2:

    if arena_player_attack_chance == "none":
        $ rand_arena_attack = renpy.random.choice(['miss'])

    elif arena_player_attack_chance == "low":
        $ rand_arena_attack = renpy.random.choice(['hit', 'miss', 'miss'])

    elif arena_player_attack_chance == "mediocre":
        $ rand_arena_attack = renpy.random.choice(['hit','hit', 'miss'])

    elif arena_player_attack_chance == "high":
        $ rand_arena_attack = renpy.random.choice(['hit','hit','hit', 'miss'])

    elif arena_player_attack_chance == "ultimate":
        $ rand_arena_attack = renpy.random.choice(['hit'])

    if rand_arena_attack == 'hit':
        show arena_swipe:
            xpos 400 ypos -100
        with dissolve
        $ renpy.pause(0.3)
        hide arena_swipe with dissolve
        $ renpy.pause(0.3)

        if arena_crab ==1:
            $ enemy_crab1_hp -= hit
            $ crab_health = enemy_crab1_hp

        if arena_crab ==2:
            $ enemy_crab2_hp -= hit
            $ crab_health = enemy_crab2_hp

        if arena_crab ==3:
            $ enemy_crab3_hp -= hit
            $ crab_health = enemy_crab3_hp

        if arena_crab ==4:
            $ enemy_crab4_hp -= hit
            $ crab_health = enemy_crab4_hp

        if arena_crab ==5:
            $ enemy_crab5_hp -= hit
            $ crab_health = enemy_crab5_hp

        $ arena_xpos_lifebar_enemy = -(360-((crab_health*360)/enemy_crab_health_max))


    if rand_arena_attack == 'miss':
        "[crab_name] missed!"

    jump enemy_crab_turn

label arena_charge_attack:
    $ crab_charge = True
    "[crab_name] charges its attack!"
    jump enemy_crab_turn

label arena_charge_check:
    $ element_bonus = 1

    if crab_element == "earth" and opp_element == "fire":
        $ element_bonus = 1.3
    elif crab_element == "fire" and opp_element == "water":
        $ element_bonus = 1.3
    elif crab_element == "water" and opp_element == "earth":
        $ element_bonus = 1.3
    $ crab_charge = False
    show arena_swipe:
        xpos 400 ypos -100
    with dissolve
    $ renpy.pause(0.3)
    hide arena_swipe with dissolve
    $ renpy.pause(0.3)
    $ level_ratio = (crab_level-enemy_crab_level)
    $ level_ratio2 = (enemy_crab_level-crab_level)

    if level_ratio >=4:
        $ charge_hit = math.ceil((((crab_att-level_ratio) - (opp_def+(level_ratio*5)))*element_bonus))
    if level_ratio >=0 and level_ratio <4:
        $ charge_hit = math.ceil((((crab_att-level_ratio) - (opp_def+(level_ratio*4)))*element_bonus))
    else:
        if level_ratio2 <=-4:
            $ charge_hit = math.ceil((((crab_att+(level_ratio2*5)) - (opp_def-level_ratio2))*element_bonus))
        else:
            $ charge_hit = math.ceil((((crab_att+(level_ratio2*4)) - (opp_def-level_ratio2))*element_bonus))




    if charge_hit <=1:
        $ charge_hit = 3
    $ charge_hit +=1
    $ charge_hit2 = math.ceil(charge_hit*1.8)

    if arena_crab ==1:
        $ enemy_crab1_hp -= charge_hit2
        $ crab_health = enemy_crab1_hp

    if arena_crab ==2:
        $ enemy_crab2_hp -= charge_hit2
        $ crab_health = enemy_crab2_hp

    if arena_crab ==3:
        $ enemy_crab3_hp -= charge_hit2
        $ crab_health = enemy_crab3_hp

    if arena_crab ==4:
        $ enemy_crab4_hp -= charge_hit2
        $ crab_health = enemy_crab4_hp

    if arena_crab ==5:
        $ enemy_crab5_hp -= charge_hit2
        $ crab_health = enemy_crab5_hp


    "[crab_name]'s charged attack hit enemy [enemy_crab_name]!"
    jump enemy_crab_turn

label arena_boost_attack:
    if crab_type == "1":
        $ crab_att +=8
        $ crab_def -=8
        "[crab_name]'s att went up!"
        "[crab_name]'s def went down!"
    if crab_type == "2":
        $ crab_def +=8
        "[crab_name]'s def went up!"
    if crab_type == "3":
        $ crab_att -=8
        $ crab_def +=8
        "[crab_name]'s def went up!"
        "[crab_name]'s att went down!"
    if crab_type == "4":
        $ crab_att +=8
        $ crab_hurt_self = math.ceil(crab_max_health*0.1)
        $ crab_standin_health -= crab_hurt_self
        "[crab_name]'s att went up!"
        "[crab_name]'s hp went down!"
    if crab_type == "5":
        $ crab_acc +=8
        "[crab_name]'s acc went up!"
    if crab_type == "6":
        $ crab_acc +=8
        $ crab_def +=8
        "[crab_name]'s acc went up!"
        "[crab_name]'s def went up!"
    if crab_type == "7":
        $ crab_def +=8
        "[crab_name]'s def went up!"
    if crab_type == "8":
        $ crab_acc +=8
        $ crab_att -=8
        "[crab_name]'s acc went up!"
        "[crab_name]'s att went down!"
    if crab_type == "9":
        $ crab_acc -=8
        $ crab_att +=8
        "[crab_name]'s att went up!"
        "[crab_name]'s acc went down!"
    if crab_type == "10":
        $ crab_acc +=8
        $ crab_def +=8
        "[crab_name]'s acc went up!"
        "[crab_name]'s def went up!"
    if crab_type == "11":
        $ crab_acc -=8
        $ crab_att +=8
        "[crab_name]'s att went up!"
        "[crab_name]'s acc went down!"

    jump enemy_crab_turn

label arena_special_attack:
    if crab_type == "1":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used bind!"
        with vshake
        $ renpy.pause(0.3)
        if e_bind >=1:
            "enemy [enemy_crab_name] is already bound!"
        elif special_roll == "1":
            $ e_bind = 3
            "enemy [enemy_crab_name] was bound! they may not be able to attack!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "2":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used bind!"
        with vshake
        $ renpy.pause(0.3)
        if e_bind >=1:
            "enemy [enemy_crab_name] is already bound!"
        elif special_roll == "1":
            $ e_bind = 3
            "enemy [enemy_crab_name] is bound! they may not be able to attack!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "3":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used poison!"
        with vshake
        $ renpy.pause(0.3)
        if e_poison >=1:
            "enemy [enemy_crab_name] is already poisoned!"
        elif special_roll == "1":
            $ e_poison = 3
            "enemy [enemy_crab_name] is poisoned!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "4":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used confuse!"
        with vshake
        $ renpy.pause(0.3)
        if e_confuse >=1:
            "enemy [enemy_crab_name] is already confused!"
        elif special_roll == "1":
            $ e_confuse = 3
            "enemy [enemy_crab_name] is confused! they may hurt themselves!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "5":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used weak!"
        with vshake
        $ renpy.pause(0.3)
        if e_weak >=1:
            "enemy [enemy_crab_name] is already weak!"
        elif special_roll == "1":
            $ e_weak = 3
            "enemy [enemy_crab_name] is weakened! they can only use their regular attack!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "6":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used poison!"
        with vshake
        $ renpy.pause(0.3)
        if e_poison >=1:
            "enemy [enemy_crab_name] is already poisoned!"
        elif special_roll == "1":
            $ e_poison = 3
            "enemy [enemy_crab_name] is poisoned!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "7":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used bind!"
        with vshake
        $ renpy.pause(0.3)
        if e_bind >=1:
            "enemy [enemy_crab_name] is already bound!"
        elif special_roll == "1":
            $ e_bind = 3
            "enemy [enemy_crab_name] is bound! they may not be able to attack!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "8":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used confuse!"
        with vshake
        $ renpy.pause(0.3)
        if e_confuse >=1:
            "enemy [enemy_crab_name] is already confused!"
        elif special_roll == "1":
            $ e_confuse = 3
            "enemy [enemy_crab_name] is confused! they may hurt themselves!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "9":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used poison!"
        with vshake
        $ renpy.pause(0.3)
        if e_poison >=1:
            "enemy [enemy_crab_name] is already poisoned!"
        elif special_roll == "1":
            $ e_poison = 3
            "enemy [enemy_crab_name] is poisoned!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "10":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used confuse!"
        with vshake
        $ renpy.pause(0.3)
        if e_confuse >=1:
            "enemy [enemy_crab_name] is already confused!"
        elif special_roll == "1":
            $ e_confuse = 3
            "enemy [enemy_crab_name] is confused! they may hurt themselves!"
        elif special_roll == "2":
            "[crab_name] missed!"

    if crab_type == "11":
        $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
        "[crab_name] used weak!"
        with vshake
        $ renpy.pause(0.3)
        if e_weak >=1:
            "enemy [enemy_crab_name] is already weak!"
        elif special_roll == "1":
            $ e_weak = 3
            "enemy [enemy_crab_name] is weakened! they can only use their regular attack!"
        elif special_roll == "2":
            "[crab_name] missed!"

    jump enemy_crab_turn

label arena_switch:
    if crab_standin_health <=0:
        if crab1_active:
            $ crab1_hp = 0
        if crab2_active:
            $ crab2_hp = 0
        if crab3_active:
            $ crab3_hp = 0
        if crab4_active:
            $ crab4_hp = 0
        if crab5_active:
            $ crab5_hp = 0
        if crab6_active:
            $ crab6_hp = 0
        if crab7_active:
            $ crab7_hp = 0
        if crab8_active:
            $ crab8_hp = 0
        if crab9_active:
            $ crab9_hp = 0
        if crab10_active:
            $ crab10_hp = 0
        if crab11_active:
            $ crab11_hp = 0
        if crab12_active:
            $ crab12_hp = 0
        if crab13_active:
            $ crab13_hp = 0
        if crab14_active:
            $ crab14_hp = 0
        if crab15_active:
            $ crab15_hp = 0
        if crab16_active:
            $ crab16_hp = 0
        if crab17_active:
            $ crab17_hp = 0
        if crab18_active:
            $ crab18_hp = 0
        if crab19_active:
            $ crab19_hp = 0
        if crab20_active:
            $ crab20_hp = 0
        if crab21_active:
            $ crab21_hp = 0
        if crab22_active:
            $ crab22_hp = 0
        if crab23_active:
            $ crab23_hp = 0
        if crab24_active:
            $ crab24_hp = 0
        if crab25_active:
            $ crab25_hp = 0
        if crab26_active:
            $ crab26_hp = 0
        if crab27_active:
            $ crab27_hp = 0
        if crab28_active:
            $ crab28_hp = 0
        if crab29_active:
            $ crab29_hp = 0
        if crab30_active:
            $ crab30_hp = 0

        hide crab1_shuffle
        hide crab2_shuffle
        hide crab3_shuffle
        hide crab4_shuffle
        hide crab5_shuffle
        hide crab6_shuffle
        hide crab7_shuffle
        hide crab8_shuffle
        hide crab9_shuffle
        hide crab10_shuffle
        hide crab11_shuffle
        hide crab12_shuffle
        hide crab13_shuffle
        hide crab14_shuffle
        hide crab15_shuffle
        hide crab16_shuffle
        hide crab17_shuffle
        hide crab18_shuffle
        hide crab19_shuffle
        hide crab20_shuffle
        hide crab21_shuffle
        hide crab22_shuffle
        hide crab23_shuffle
        hide crab24_shuffle
        hide crab25_shuffle
        hide crab26_shuffle
        hide crab27_shuffle
        hide crab28_shuffle
        hide crab29_shuffle
        hide crab30_shuffle
        "send out another crab!"

    menu:
        "-----------" if not crab_spot1_chosen:
            "you don't have a crab set here!"
            jump arena_switch

        "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot1 ==1:
            jump switch_crab1

        "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot1 ==2:
            jump switch_crab2

        "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot1 ==3:
            jump switch_crab3

        "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot1 ==4:
            jump switch_crab4

        "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot1 ==5:
            jump switch_crab5

        "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot1 ==6:
            jump switch_crab6

        "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot1 ==7:
            jump switch_crab7

        "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot1 ==8:
            jump switch_crab8

        "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot1 ==9:
            jump switch_crab9

        "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot1 ==10:
            jump switch_crab10

        "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot1 ==11:
            jump switch_crab11

        "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot1 ==12:
            jump switch_crab12

        "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot1 ==13:
            jump switch_crab13

        "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot1 ==14:
            jump switch_crab14

        "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot1 ==15:
            jump switch_crab15

        "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot1 ==16:
            jump switch_crab16

        "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot1 ==17:
            jump switch_crab17

        "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot1 ==18:
            jump switch_crab18

        "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot1 ==19:
            jump switch_crab19

        "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot1 ==20:
            jump switch_crab20

        "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot1 ==21:
            jump switch_crab21

        "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot1 ==22:
            jump switch_crab22

        "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot1 ==23:
            jump switch_crab23

        "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot1 ==24:
            jump switch_crab24

        "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot1 ==25:
            jump switch_crab25

        "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot1 ==26:
            jump switch_crab26

        "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot1 ==27:
            jump switch_crab27

        "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot1 ==28:
            jump switch_crab28

        "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot1 ==29:
            jump switch_crab29

        "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot1 ==30:
            jump switch_crab30

        "-----------" if not crab_spot2_chosen:
            "you don't have a crab set here!"
            jump arena_switch

        "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot2 ==1:
            jump switch_crab1

        "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot2 ==2:
            jump switch_crab2

        "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot2 ==3:
            jump switch_crab3

        "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot2 ==4:
            jump switch_crab4

        "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot2 ==5:
            jump switch_crab5

        "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot2 ==6:
            jump switch_crab6

        "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot2 ==7:
            jump switch_crab7

        "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot2 ==8:
            jump switch_crab8

        "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot2 ==9:
            jump switch_crab9

        "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot2 ==10:
            jump switch_crab10

        "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot2 ==11:
            jump switch_crab11

        "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot2 ==12:
            jump switch_crab12

        "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot2 ==13:
            jump switch_crab13

        "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot2 ==14:
            jump switch_crab14

        "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot2 ==15:
            jump switch_crab15

        "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot2 ==16:
            jump switch_crab16

        "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot2 ==17:
            jump switch_crab17

        "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot2 ==18:
            jump switch_crab18

        "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot2 ==19:
            jump switch_crab19

        "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot2 ==20:
            jump switch_crab20

        "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot2 ==21:
            jump switch_crab21

        "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot2 ==22:
            jump switch_crab22

        "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot2 ==23:
            jump switch_crab23

        "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot2 ==24:
            jump switch_crab24

        "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot2 ==25:
            jump switch_crab25

        "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot2 ==26:
            jump switch_crab26

        "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot2 ==27:
            jump switch_crab27

        "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot2 ==28:
            jump switch_crab28

        "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot2 ==29:
            jump switch_crab29

        "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot2 ==30:
            jump switch_crab30

        "-----------" if not crab_spot3_chosen:
            "you don't have a crab set here!"
            jump arena_switch

        "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot3 ==1:
            jump switch_crab1

        "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot3 ==2:
            jump switch_crab2

        "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot3 ==3:
            jump switch_crab3

        "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot3 ==4:
            jump switch_crab4

        "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot3 ==5:
            jump switch_crab5

        "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot3 ==6:
            jump switch_crab6

        "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot3 ==7:
            jump switch_crab7

        "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot3 ==8:
            jump switch_crab8

        "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot3 ==9:
            jump switch_crab9

        "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot3 ==10:
            jump switch_crab10

        "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot3 ==11:
            jump switch_crab11

        "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot3 ==12:
            jump switch_crab12

        "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot3 ==13:
            jump switch_crab13

        "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot3 ==14:
            jump switch_crab14

        "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot3 ==15:
            jump switch_crab15

        "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot3 ==16:
            jump switch_crab16

        "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot3 ==17:
            jump switch_crab17

        "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot3 ==18:
            jump switch_crab18

        "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot3 ==19:
            jump switch_crab19

        "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot3 ==20:
            jump switch_crab20

        "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot3 ==21:
            jump switch_crab21

        "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot3 ==22:
            jump switch_crab22

        "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot3 ==23:
            jump switch_crab23

        "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot3 ==24:
            jump switch_crab24

        "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot3 ==25:
            jump switch_crab25

        "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot3 ==26:
            jump switch_crab26

        "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot3 ==27:
            jump switch_crab27

        "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot3 ==28:
            jump switch_crab28

        "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot3 ==29:
            jump switch_crab29

        "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot3 ==30:
            jump switch_crab30


        "-----------" if not crab_spot4_chosen:
            "you don't have a crab set here!"
            jump arena_switch

        "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot4 ==1:
            jump switch_crab1

        "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot4 ==2:
            jump switch_crab2

        "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot4 ==3:
            jump switch_crab3

        "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot4 ==4:
            jump switch_crab4

        "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot4 ==5:
            jump switch_crab5

        "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot4 ==6:
            jump switch_crab6

        "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot4 ==7:
            jump switch_crab7

        "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot4 ==8:
            jump switch_crab8

        "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot4 ==9:
            jump switch_crab9

        "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot4 ==10:
            jump switch_crab10

        "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot4 ==11:
            jump switch_crab11

        "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot4 ==12:
            jump switch_crab12

        "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot4 ==13:
            jump switch_crab13

        "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot4 ==14:
            jump switch_crab14

        "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot4 ==15:
            jump switch_crab15

        "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot4 ==16:
            jump switch_crab16

        "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot4 ==17:
            jump switch_crab17

        "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot4 ==18:
            jump switch_crab18

        "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot4 ==19:
            jump switch_crab19

        "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot4 ==20:
            jump switch_crab20

        "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot4 ==21:
            jump switch_crab21

        "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot4 ==22:
            jump switch_crab22

        "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot4 ==23:
            jump switch_crab23

        "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot4 ==24:
            jump switch_crab24

        "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot4 ==25:
            jump switch_crab25

        "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot4 ==26:
            jump switch_crab26

        "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot4 ==27:
            jump switch_crab27

        "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot4 ==28:
            jump switch_crab28

        "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot4 ==29:
            jump switch_crab29

        "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot4 ==30:
            jump switch_crab30


        "-----------" if not crab_spot5_chosen:
            "you don't have a crab set here!"
            jump arena_switch

        "([crab1_rarity]) [crab1_name] - L[crab1_level]" if crab_spot5 ==1:
            jump switch_crab1

        "([crab2_rarity]) [crab2_name] - L[crab2_level]" if crab_spot5 ==2:
            jump switch_crab2

        "([crab3_rarity]) [crab3_name] - L[crab3_level]" if crab_spot5 ==3:
            jump switch_crab3

        "([crab4_rarity]) [crab4_name] - L[crab4_level]" if crab_spot5 ==4:
            jump switch_crab4

        "([crab5_rarity]) [crab5_name] - L[crab5_level]" if crab_spot5 ==5:
            jump switch_crab5

        "([crab6_rarity]) [crab6_name] - L[crab6_level]" if crab_spot5 ==6:
            jump switch_crab6

        "([crab7_rarity]) [crab7_name] - L[crab7_level]" if crab_spot5 ==7:
            jump switch_crab7

        "([crab8_rarity]) [crab8_name] - L[crab8_level]" if crab_spot5 ==8:
            jump switch_crab8

        "([crab9_rarity]) [crab9_name] - L[crab9_level]" if crab_spot5 ==9:
            jump switch_crab9

        "([crab10_rarity]) [crab10_name] - L[crab10_level]" if crab_spot5 ==10:
            jump switch_crab10

        "([crab11_rarity]) [crab11_name] - L[crab11_level]" if crab_spot5 ==11:
            jump switch_crab11

        "([crab12_rarity]) [crab12_name] - L[crab12_level]" if crab_spot5 ==12:
            jump switch_crab12

        "([crab13_rarity]) [crab13_name] - L[crab13_level]" if crab_spot5 ==13:
            jump switch_crab13

        "([crab14_rarity]) [crab14_name] - L[crab14_level]" if crab_spot5 ==14:
            jump switch_crab14

        "([crab15_rarity]) [crab15_name] - L[crab15_level]" if crab_spot5 ==15:
            jump switch_crab15

        "([crab16_rarity]) [crab16_name] - L[crab16_level]" if crab_spot5 ==16:
            jump switch_crab16

        "([crab17_rarity]) [crab17_name] - L[crab17_level]" if crab_spot5 ==17:
            jump switch_crab17

        "([crab18_rarity]) [crab18_name] - L[crab18_level]" if crab_spot5 ==18:
            jump switch_crab18

        "([crab19_rarity]) [crab19_name] - L[crab19_level]" if crab_spot5 ==19:
            jump switch_crab19

        "([crab20_rarity]) [crab20_name] - L[crab20_level]" if crab_spot5 ==20:
            jump switch_crab20

        "([crab21_rarity]) [crab21_name] - L[crab21_level]" if crab_spot5 ==21:
            jump switch_crab21

        "([crab22_rarity]) [crab22_name] - L[crab22_level]" if crab_spot5 ==22:
            jump switch_crab22

        "([crab23_rarity]) [crab23_name] - L[crab23_level]" if crab_spot5 ==23:
            jump switch_crab23

        "([crab24_rarity]) [crab24_name] - L[crab24_level]" if crab_spot5 ==24:
            jump switch_crab24

        "([crab25_rarity]) [crab25_name] - L[crab25_level]" if crab_spot5 ==25:
            jump switch_crab25

        "([crab26_rarity]) [crab26_name] - L[crab26_level]" if crab_spot5 ==26:
            jump switch_crab26

        "([crab27_rarity]) [crab27_name] - L[crab27_level]" if crab_spot5 ==27:
            jump switch_crab27

        "([crab28_rarity]) [crab28_name] - L[crab28_level]" if crab_spot5 ==28:
            jump switch_crab28

        "([crab29_rarity]) [crab29_name] - L[crab29_level]" if crab_spot5 ==29:
            jump switch_crab29

        "([crab30_rarity]) [crab30_name] - L[crab30_level]" if crab_spot5 ==30:
            jump switch_crab30
        "cancel":


            if crab_standin_health <=0:
                "you need to pick a replacement crab!"
                jump arena_switch
            else:
                jump arena_battle_screen

label arena_item:
    menu:
        "------(locked)" if arena_potion ==0:
            "test"
        "potion ([arena_potion])" if arena_potion >=1:
            $ arena_potion -=1
            $ potion_calc = math.ceil(crab_max_health*.5)
            $ crab_standin_health += potion_calc
            if crab_standin_health >= crab_max_health:
                $ crab_standin_health = crab_max_health
            jump enemy_crab_turn

        "------(locked)" if arena_salts ==0:
            "test"
        "smelling salts ([arena_salts])" if arena_salts >=1:
            if a_confuse ==0:
                "[crab_name] isn't confused!"
                jump arena_battle_screen
            else:
                $ arena_salts -=1
                $ a_confuse = 0
                $ a_confused = False
                "[crab_name]'s confusion was cured!"
                jump enemy_crab_turn

        "------(locked)" if arena_antidote ==0:
            "test"
        "antidote ([arena_antidote])" if arena_antidote >=1:
            if a_poison ==0:
                "[crab_name] isn't poisoned!"
                jump arena_battle_screen
            else:
                $ arena_antidote -=1
                $ a_poison = 0
                "[crab_name]'s poison was cured!"
                jump enemy_crab_turn

        "------(locked)" if arena_steroid ==0:
            "test"
        "steroids ([arena_steroid])" if arena_steroid >=1:
            if a_weak ==0:
                "[crab_name] isn't weak!"
                jump arena_battle_screen
            else:
                $ arena_steroid -=1
                $ a_weak = 0
                $ a_weakened = False
                "[crab_name]'s weak was cured!"
                jump enemy_crab_turn
        "------(locked)" if cureall ==0:
            "test"
        "cure-all ([cureall])" if cureall >=1:
            $ cureall -=1
            $ a_poison = 0
            $ a_confuse = 0
            $ a_bind = 0
            $ a_weak = 0
            $ a_confused = False
            $ a_weakened = False
            "you cured your crabs of all status effects!"
            jump enemy_crab_turn

        "------(locked)" if arena_pocket ==0:
            "test"
        "pocket ([arena_pocket])" if arena_pocket >=1:
            if not crab_hunt and not crab_hunt2:
                "you can't capture an enemy's crabs!"
                jump arena_battle_screen
            else:
                if ultimate_arena_battle:
                    "you can't capture an enemy's crabs!"
                    jump arena_battle_screen

                if anka_arena_battle:
                    "you can't capture an enemy's crabs!"
                    jump arena_battle_screen

                if arena_pocket >=1:
                    $ arena_pocket -=1
                    if crab_health <=20:
                        $ catch_chance = WeightedChoice([("1", 0.75), ("2", 0.25)])
                        if catch_chance == "1":
                            $ crabs_current +=1
                            $ crabs_total +=1
                            with vshake
                            hide enemy_crab_shuffle with dissolve
                            "you caught a [enemy_crab_name]!"
                            "it went into storage!"

                            if enemy_crab_rarity == "n":
                                $ catch_arena_exp_math = enemy_crab_level*(enemy_crab_level/1.5)
                            if enemy_crab_rarity == "r":
                                $ catch_arena_exp_math = enemy_crab_level*(enemy_crab_level/1.2)
                            if enemy_crab_rarity == "e":
                                $ catch_arena_exp_math = enemy_crab_level*enemy_crab_level
                            if enemy_crab_rarity == "l":
                                $ catch_arena_exp_math = enemy_crab_level*(enemy_crab_level/0.8)

                            $ arena_exp_math = math.ceil(catch_arena_exp_math/2)
                            $ total_arena_exp += arena_exp_math
                            "you got [total_arena_exp] exp!"
                            jump wild_crab_catch
                        else:
                            with vshake
                            "you missed!"
                            jump enemy_crab_turn
                    else:
                        $ catch_chance = WeightedChoice([("1", 0.4), ("2", 0.6)])
                        if catch_chance == "1":
                            $ crabs_current +=1
                            $ crabs_total +=1
                            with vshake
                            hide enemy_crab_shuffle with dissolve
                            "you caught a [enemy_crab_name]!"
                            "it went into storage!"
                            if enemy_crab_rarity == "n":
                                $ catch_arena_exp_math = enemy_crab_level*(enemy_crab_level/1.5)
                            if enemy_crab_rarity == "r":
                                $ catch_arena_exp_math = enemy_crab_level*(enemy_crab_level/1.2)
                            if enemy_crab_rarity == "e":
                                $ catch_arena_exp_math = enemy_crab_level*enemy_crab_level
                            if enemy_crab_rarity == "l":
                                $ catch_arena_exp_math = enemy_crab_level*(enemy_crab_level/0.8)

                            $ arena_exp_math = math.ceil(catch_arena_exp_math/2)
                            $ total_arena_exp += arena_exp_math
                            "you got [total_arena_exp] exp!"
                            jump wild_crab_catch
                        else:
                            with vshake
                            "you missed!"
                            jump enemy_crab_turn
                else:

                    "you don't have any pockets!"
                    jump arena_battle_screen
        "cancel":

            jump arena_battle_screen

label arena_run:
    if not crab_hunt and not crab_hunt2:


        jump arena_end_level_check
    else:
        jump arena_end_level_check

label enemy_crab_turn:
    if crab_health <=0:
        hide enemy_crab_shuffle with dissolve
        $ renpy.pause(0.3)



        if enemy_crab_rarity == "n":
            $ arena_exp_math = enemy_crab_level*(enemy_crab_level/1.5)
        if enemy_crab_rarity == "r":
            $ arena_exp_math = enemy_crab_level*(enemy_crab_level/1.2)
        if enemy_crab_rarity == "e":
            $ arena_exp_math = enemy_crab_level*enemy_crab_level
        if enemy_crab_rarity == "l":
            $ arena_exp_math = enemy_crab_level*(enemy_crab_level/0.8)

        $ total_arena_exp += arena_exp_math

        $ total_enemy_crabs -=1
        $ enemy_move2 = False
        $ enemy_move3 = False
        $ enemy_move4 = False
        if total_enemy_crabs <=0:
            if iroh_fun_battle:
                $ iroh_battle_count +=1
                play sound "audio/money.mp3"
                $ emoney +=25
                "you got 25 coins!"
                jump arena_end_level_check
            if not crab_hunt and not crab_hunt2:
                play sound "audio/win2.mp3"
                "you got {b}1 crapple{/b}!"
                $ crapples +=1
                $ arena_enemy +=1
                $ emoney +=20
                "you got 20 coins!"
                jump arena_end_level_check
            if crab_hunt or crab_hunt2:
                play sound "audio/money.mp3"
                $ emoney +=15
                "you found 15 coins!"
                jump arena_end_level_check
        else:
            if arena_crab ==1:
                $ enemy_crab1_hp = 0
                if enemy_crab2_hp >=1:
                    $ arena_crab = 2
                    $ enemy_crab_type = enemy_crab2_type
                    $ enemy_crab_rarity = enemy_crab2_rarity
                    $ enemy_crab_health_max = enemy_crab2_health_max
                    $ enemy_crab_level = enemy_crab2_level
                    $ crab_health = enemy_crab2_hp
                    $ opp_element = opp_element_crab2
                    $ opp_def = opp_def_crab2
                    $ opp_att = opp_att_crab2
                    $ opp_acc = opp_acc_crab2
                    $ enemy_crab_name = enemy_crab2_name
                elif enemy_crab3_hp >=1:
                    $ arena_crab = 3
                    $ enemy_crab_type = enemy_crab3_type
                    $ enemy_crab_rarity = enemy_crab3_rarity
                    $ enemy_crab_health_max = enemy_crab3_health_max
                    $ enemy_crab_level = enemy_crab3_level
                    $ crab_health = enemy_crab3_hp
                    $ opp_element = opp_element_crab3
                    $ opp_def = opp_def_crab3
                    $ opp_att = opp_att_crab3
                    $ opp_acc = opp_acc_crab3
                    $ enemy_crab_name = enemy_crab3_name
                elif enemy_crab4_hp >=1:
                    $ arena_crab = 4
                    $ enemy_crab_type = enemy_crab4_type
                    $ enemy_crab_rarity = enemy_crab4_rarity
                    $ enemy_crab_health_max = enemy_crab4_health_max
                    $ enemy_crab_level = enemy_crab4_level
                    $ crab_health = enemy_crab4_hp
                    $ opp_element = opp_element_crab4
                    $ opp_def = opp_def_crab4
                    $ opp_att = opp_att_crab4
                    $ opp_acc = opp_acc_crab4
                    $ enemy_crab_name = enemy_crab4_name
                elif enemy_crab5_hp >=1:
                    $ arena_crab = 5
                    $ enemy_crab_type = enemy_crab5_type
                    $ enemy_crab_rarity = enemy_crab5_rarity
                    $ enemy_crab_health_max = enemy_crab5_health_max
                    $ enemy_crab_level = enemy_crab5_level
                    $ crab_health = enemy_crab5_hp
                    $ opp_element = opp_element_crab5
                    $ opp_def = opp_def_crab5
                    $ opp_att = opp_att_crab5
                    $ opp_acc = opp_acc_crab5
                    $ enemy_crab_name = enemy_crab5_name
            elif arena_crab ==2:
                $ enemy_crab2_hp = 0
                if enemy_crab1_hp >=1:
                    $ arena_crab = 1
                    $ enemy_crab_type = enemy_crab1_type
                    $ enemy_crab_rarity = enemy_crab1_rarity
                    $ enemy_crab_health_max = enemy_crab1_health_max
                    $ enemy_crab_level = enemy_crab1_level
                    $ crab_health = enemy_crab1_hp
                    $ opp_element = opp_element_crab1
                    $ opp_def = opp_def_crab1
                    $ opp_att = opp_att_crab1
                    $ opp_acc = opp_acc_crab1
                    $ enemy_crab_name = enemy_crab1_name
                elif enemy_crab3_hp >=1:
                    $ arena_crab = 3
                    $ enemy_crab_type = enemy_crab3_type
                    $ enemy_crab_rarity = enemy_crab3_rarity
                    $ enemy_crab_health_max = enemy_crab3_health_max
                    $ enemy_crab_level = enemy_crab3_level
                    $ crab_health = enemy_crab3_hp
                    $ opp_element = opp_element_crab3
                    $ opp_def = opp_def_crab3
                    $ opp_att = opp_att_crab3
                    $ opp_acc = opp_acc_crab3
                    $ enemy_crab_name = enemy_crab3_name
                elif enemy_crab4_hp >=1:
                    $ arena_crab = 4
                    $ enemy_crab_type = enemy_crab4_type
                    $ enemy_crab_rarity = enemy_crab4_rarity
                    $ enemy_crab_health_max = enemy_crab4_health_max
                    $ enemy_crab_level = enemy_crab4_level
                    $ crab_health = enemy_crab4_hp
                    $ opp_element = opp_element_crab4
                    $ opp_def = opp_def_crab4
                    $ opp_att = opp_att_crab4
                    $ opp_acc = opp_acc_crab4
                    $ enemy_crab_name = enemy_crab4_name
                elif enemy_crab5_hp >=1:
                    $ arena_crab = 5
                    $ enemy_crab_type = enemy_crab5_type
                    $ enemy_crab_rarity = enemy_crab5_rarity
                    $ enemy_crab_health_max = enemy_crab5_health_max
                    $ enemy_crab_level = enemy_crab5_level
                    $ crab_health = enemy_crab5_hp
                    $ opp_element = opp_element_crab5
                    $ opp_def = opp_def_crab5
                    $ opp_att = opp_att_crab5
                    $ opp_acc = opp_acc_crab5
                    $ enemy_crab_name = enemy_crab5_name
            elif arena_crab ==3:
                $ enemy_crab3_hp = 0
                if enemy_crab1_hp >=1:
                    $ arena_crab = 1
                    $ enemy_crab_type = enemy_crab1_type
                    $ enemy_crab_rarity = enemy_crab1_rarity
                    $ enemy_crab_health_max = enemy_crab1_health_max
                    $ enemy_crab_level = enemy_crab1_level
                    $ crab_health = enemy_crab1_hp
                    $ opp_element = opp_element_crab1
                    $ opp_def = opp_def_crab1
                    $ opp_att = opp_att_crab1
                    $ opp_acc = opp_acc_crab1
                    $ enemy_crab_name = enemy_crab1_name
                elif enemy_crab2_hp >=1:
                    $ arena_crab = 2
                    $ enemy_crab_type = enemy_crab2_type
                    $ enemy_crab_rarity = enemy_crab2_rarity
                    $ enemy_crab_health_max = enemy_crab2_health_max
                    $ enemy_crab_level = enemy_crab2_level
                    $ crab_health = enemy_crab2_hp
                    $ opp_element = opp_element_crab2
                    $ opp_def = opp_def_crab2
                    $ opp_att = opp_att_crab2
                    $ opp_acc = opp_acc_crab2
                    $ enemy_crab_name = enemy_crab2_name
                elif enemy_crab4_hp >=1:
                    $ arena_crab = 4
                    $ enemy_crab_type = enemy_crab4_type
                    $ enemy_crab_rarity = enemy_crab4_rarity
                    $ enemy_crab_health_max = enemy_crab4_health_max
                    $ enemy_crab_level = enemy_crab4_level
                    $ crab_health = enemy_crab4_hp
                    $ opp_element = opp_element_crab4
                    $ opp_def = opp_def_crab4
                    $ opp_att = opp_att_crab4
                    $ opp_acc = opp_acc_crab4
                    $ enemy_crab_name = enemy_crab4_name
                elif enemy_crab5_hp >=1:
                    $ arena_crab = 5
                    $ enemy_crab_type = enemy_crab5_type
                    $ enemy_crab_rarity = enemy_crab5_rarity
                    $ enemy_crab_health_max = enemy_crab5_health_max
                    $ enemy_crab_level = enemy_crab5_level
                    $ crab_health = enemy_crab5_hp
                    $ opp_element = opp_element_crab5
                    $ opp_def = opp_def_crab5
                    $ opp_att = opp_att_crab5
                    $ opp_acc = opp_acc_crab5
                    $ enemy_crab_name = enemy_crab5_name
            elif arena_crab ==4:
                $ enemy_crab4_hp = 0
                if enemy_crab1_hp >=1:
                    $ arena_crab = 1
                    $ enemy_crab_type = enemy_crab1_type
                    $ enemy_crab_rarity = enemy_crab1_rarity
                    $ enemy_crab_health_max = enemy_crab1_health_max
                    $ enemy_crab_level = enemy_crab1_level
                    $ crab_health = enemy_crab1_hp
                    $ opp_element = opp_element_crab1
                    $ opp_def = opp_def_crab1
                    $ opp_att = opp_att_crab1
                    $ opp_acc = opp_acc_crab1
                    $ enemy_crab_name = enemy_crab1_name
                elif enemy_crab2_hp >=1:
                    $ arena_crab = 2
                    $ enemy_crab_type = enemy_crab2_type
                    $ enemy_crab_rarity = enemy_crab2_rarity
                    $ enemy_crab_health_max = enemy_crab2_health_max
                    $ enemy_crab_level = enemy_crab2_level
                    $ crab_health = enemy_crab2_hp
                    $ opp_element = opp_element_crab2
                    $ opp_def = opp_def_crab2
                    $ opp_att = opp_att_crab2
                    $ opp_acc = opp_acc_crab2
                    $ enemy_crab_name = enemy_crab2_name
                elif enemy_crab3_hp >=1:
                    $ arena_crab = 3
                    $ enemy_crab_type = enemy_crab3_type
                    $ enemy_crab_rarity = enemy_crab3_rarity
                    $ enemy_crab_health_max = enemy_crab3_health_max
                    $ enemy_crab_level = enemy_crab3_level
                    $ crab_health = enemy_crab3_hp
                    $ opp_element = opp_element_crab3
                    $ opp_def = opp_def_crab3
                    $ opp_att = opp_att_crab3
                    $ opp_acc = opp_acc_crab3
                    $ enemy_crab_name = enemy_crab3_name
                elif enemy_crab5_hp >=1:
                    $ arena_crab = 5
                    $ enemy_crab_type = enemy_crab5_type
                    $ enemy_crab_rarity = enemy_crab5_rarity
                    $ enemy_crab_health_max = enemy_crab5_health_max
                    $ enemy_crab_level = enemy_crab5_level
                    $ crab_health = enemy_crab5_hp
                    $ opp_element = opp_element_crab5
                    $ opp_def = opp_def_crab5
                    $ opp_att = opp_att_crab5
                    $ opp_acc = opp_acc_crab5
                    $ enemy_crab_name = enemy_crab5_name
            elif arena_crab ==5:
                $ enemy_crab5_hp = 0
                if enemy_crab1_hp >=1:
                    $ arena_crab = 1
                    $ enemy_crab_type = enemy_crab1_type
                    $ enemy_crab_rarity = enemy_crab1_rarity
                    $ enemy_crab_health_max = enemy_crab1_health_max
                    $ enemy_crab_level = enemy_crab1_level
                    $ crab_health = enemy_crab1_hp
                    $ opp_element = opp_element_crab1
                    $ opp_def = opp_def_crab1
                    $ opp_att = opp_att_crab1
                    $ opp_acc = opp_acc_crab1
                    $ enemy_crab_name = enemy_crab1_name
                elif enemy_crab2_hp >=1:
                    $ arena_crab = 2
                    $ enemy_crab_type = enemy_crab2_type
                    $ enemy_crab_rarity = enemy_crab2_rarity
                    $ enemy_crab_health_max = enemy_crab2_health_max
                    $ enemy_crab_level = enemy_crab2_level
                    $ crab_health = enemy_crab2_hp
                    $ opp_element = opp_element_crab2
                    $ opp_def = opp_def_crab2
                    $ opp_att = opp_att_crab2
                    $ opp_acc = opp_acc_crab2
                    $ enemy_crab_name = enemy_crab2_name
                elif enemy_crab3_hp >=1:
                    $ arena_crab = 3
                    $ enemy_crab_type = enemy_crab3_type
                    $ enemy_crab_rarity = enemy_crab3_rarity
                    $ enemy_crab_health_max = enemy_crab3_health_max
                    $ enemy_crab_level = enemy_crab3_level
                    $ crab_health = enemy_crab3_hp
                    $ opp_element = opp_element_crab3
                    $ opp_def = opp_def_crab3
                    $ opp_att = opp_att_crab3
                    $ opp_acc = opp_acc_crab3
                    $ enemy_crab_name = enemy_crab3_name
                elif enemy_crab4_hp >=1:
                    $ arena_crab = 4
                    $ enemy_crab_type = enemy_crab4_type
                    $ enemy_crab_rarity = enemy_crab4_rarity
                    $ enemy_crab_health_max = enemy_crab4_health_max
                    $ enemy_crab_level = enemy_crab4_level
                    $ crab_health = enemy_crab4_hp
                    $ opp_element = opp_element_crab4
                    $ opp_def = opp_def_crab4
                    $ opp_att = opp_att_crab4
                    $ opp_acc = opp_acc_crab4
                    $ enemy_crab_name = enemy_crab4_name
            else:
                jump arena_end_level_check

            show enemy_crab_shuffle:
                xpos 180 ypos -400
            with dissolve
            "the opponent sent out enemy [enemy_crab_name]!"
            jump arena_crab_battle_player2

    jump enemy_move























label enemy_move:
    if e_poison >=1:
        $ e_poison -=1
        $ poison_hurt = math.ceil(enemy_crab_health_max*.1)

        if arena_crab ==1:
            $ enemy_crab1_hp -= poison_hurt
            $ crab_health = enemy_crab1_hp

        if arena_crab ==2:
            $ enemy_crab2_hp -= poison_hurt
            $ crab_health = enemy_crab2_hp

        if arena_crab ==3:
            $ enemy_crab3_hp -= poison_hurt
            $ crab_health = enemy_crab3_hp

        if arena_crab ==4:
            $ enemy_crab4_hp -= poison_hurt
            $ crab_health = enemy_crab4_hp

        if arena_crab ==5:
            $ enemy_crab5_hp -= poison_hurt
            $ crab_health = enemy_crab5_hp

        $ arena_xpos_lifebar_enemy = -(360-((crab_health*360)/enemy_crab_health_max))


        with vshake
        $ renpy.pause(0.25)
        "enemy [enemy_crab_name] took poison damage!"
        if crab_health <=0:
            jump enemy_crab_turn

    if e_bind >=1:
        $ e_bind -=1
        $ bind_chance = renpy.random.randint(1, 2)
        "enemy [enemy_crab_name] is bound! they struggle against it!"
        with vshake
        $ renpy.pause(0.25)
        if bind_chance ==1:
            "enemy [enemy_crab_name] broke through!"
        if bind_chance ==2:
            "enemy [enemy_crab_name] can't move!"
            $ enemy_crab_charge = False

    if e_confuse >=1:
        $ e_confuse -=1
        $ confusion_chance = renpy.random.randint(1, 2)
        "enemy [enemy_crab_name] is confused!"
        with vshake
        $ renpy.pause(0.25)
        if confusion_chance ==1:
            if bind_chance ==2:
                "enemy [enemy_crab_name] is bound and can't move!"
            else:
                pass
        if confusion_chance ==2:
            $ confuse_hurt = math.ceil(enemy_crab_health_max*.1)


            if arena_crab ==1:
                $ enemy_crab1_hp -= confuse_hurt
                $ crab_health = enemy_crab1_hp

            if arena_crab ==2:
                $ enemy_crab2_hp -= confuse_hurt
                $ crab_health = enemy_crab2_hp

            if arena_crab ==3:
                $ enemy_crab3_hp -= confuse_hurt
                $ crab_health = enemy_crab3_hp

            if arena_crab ==4:
                $ enemy_crab4_hp -= confuse_hurt
                $ crab_health = enemy_crab4_hp

            if arena_crab ==5:
                $ enemy_crab5_hp -= confuse_hurt
                $ crab_health = enemy_crab5_hp

            $ enemy_crab_charge = False
            "enemy [enemy_crab_name] hurt itself in its confusion!"
            if crab_health <=0:
                jump arena_crab_battle_player2
            else:
                jump enemy_crab_turn

    if e_weak >=1:
        $ e_weak -=1
        "enemy [enemy_crab_name] is weak!"
        $ enemy_crab_charge = False
        jump enemy_regular_attack

    if enemy_crab_charge:
        $ enemy_crab_charge = False

        $ enemy_level_ratio = (enemy_crab_level - crab_level)
        $ enemy_level_ratio2 = (crab_level - enemy_crab_level)

        if enemy_level_ratio >=4:
            $ enemy_charge_hit = math.ceil((((opp_att-enemy_level_ratio) - (crab_def+(enemy_level_ratio*5)))))
        if enemy_level_ratio >=0 and enemy_level_ratio <4:
            $ enemy_charge_hit = math.ceil((((opp_att-enemy_level_ratio) - (crab_def+(enemy_level_ratio*4)))))
        else:
            if enemy_level_ratio2 <=-4:
                $ enemy_charge_hit = math.ceil((((opp_att+(enemy_level_ratio2*5)) - (crab_def-enemy_level_ratio2))))
            else:
                $ enemy_charge_hit = math.ceil((((opp_att+(enemy_level_ratio2*4)) - (crab_def-enemy_level_ratio2))))





        if enemy_charge_hit <=1:
            $ enemy_charge_hit = 3
        $ enemy_charge_hit +=1
        $ enemy_charge_hit2 = math.ceil(enemy_charge_hit*1.8)

        $ crab_standin_health -= enemy_charge_hit2

        if crab1_active:
            $ crab1_temp_hp -= enemy_charge_hit2
        if crab2_active:
            $ crab2_temp_hp -= enemy_charge_hit2
        if crab3_active:
            $ crab3_temp_hp -= enemy_charge_hit2
        if crab4_active:
            $ crab4_temp_hp -= enemy_charge_hit2
        if crab5_active:
            $ crab5_temp_hp -= enemy_charge_hit2
        if crab6_active:
            $ crab6_temp_hp -= enemy_charge_hit2
        if crab7_active:
            $ crab7_temp_hp -= enemy_charge_hit2
        if crab8_active:
            $ crab8_temp_hp -= enemy_charge_hit2
        if crab9_active:
            $ crab9_temp_hp -= enemy_charge_hit2
        if crab10_active:
            $ crab10_temp_hp -= enemy_charge_hit2
        if crab11_active:
            $ crab11_temp_hp -= enemy_charge_hit2
        if crab12_active:
            $ crab12_temp_hp -= enemy_charge_hit2
        if crab13_active:
            $ crab13_temp_hp -= enemy_charge_hit2
        if crab14_active:
            $ crab14_temp_hp -= enemy_charge_hit2
        if crab15_active:
            $ crab15_temp_hp -= enemy_charge_hit2
        if crab16_active:
            $ crab16_temp_hp -= enemy_charge_hit2
        if crab17_active:
            $ crab17_temp_hp -= enemy_charge_hit2
        if crab18_active:
            $ crab18_temp_hp -= enemy_charge_hit2
        if crab19_active:
            $ crab19_temp_hp -= enemy_charge_hit2
        if crab20_active:
            $ crab20_temp_hp -= enemy_charge_hit2
        if crab21_active:
            $ crab21_temp_hp -= enemy_charge_hit2
        if crab22_active:
            $ crab22_temp_hp -= enemy_charge_hit2
        if crab23_active:
            $ crab23_temp_hp -= enemy_charge_hit2
        if crab24_active:
            $ crab24_temp_hp -= enemy_charge_hit2
        if crab25_active:
            $ crab25_temp_hp -= enemy_charge_hit2
        if crab26_active:
            $ crab26_temp_hp -= enemy_charge_hit2
        if crab27_active:
            $ crab27_temp_hp -= enemy_charge_hit2
        if crab28_active:
            $ crab28_temp_hp -= enemy_charge_hit2
        if crab29_active:
            $ crab29_temp_hp -= enemy_charge_hit2
        if crab30_active:
            $ crab30_temp_hp -= enemy_charge_hit2

        "enemy [enemy_crab_name]'s charged attack hit [crab_name]!"
        jump arena_crab_battle_player2

    if enemy_crab_rarity == "n":
        if enemy_crab_level >=5:
            $ enemy_move2 = True
        if enemy_crab_level >=10:
            $ enemy_move3 = True
        if enemy_crab_level >=15:
            $ enemy_move4 = True
    if enemy_crab_rarity == "r":
        if enemy_crab_level >=8:
            $ enemy_move2 = True
        if enemy_crab_level >=14:
            $ enemy_move3 = True
        if enemy_crab_level >=18:
            $ enemy_move4 = True
    if enemy_crab_rarity == "e":
        if enemy_crab_level >=12:
            $ enemy_move2 = True
        if enemy_crab_level >=16:
            $ enemy_move3 = True
        if enemy_crab_level >=22:
            $ enemy_move4 = True



    if enemy_move2 and enemy_move3 and enemy_move4:
        $ randcrabattack = renpy.random.randint(1, 4)

    if enemy_move2 and enemy_move3 and not enemy_move4:
        $ randcrabattack = renpy.random.randint(1, 3)

    if enemy_move2 and not enemy_move3 and not enemy_move4:
        $ randcrabattack = renpy.random.randint(1, 2)

    if not enemy_move2 and not enemy_move3 and not enemy_move4:
        $ randcrabattack = 1


    if randcrabattack ==1:
        jump enemy_regular_attack

    if randcrabattack ==2:
        if enemy_crab_type == "1":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "2":
            $ opp_def +=8
            "enemy [enemy_crab_name]'s def went up!"
        if enemy_crab_type == "3":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used poison!"
            with vshake
            $ renpy.pause(0.3)
            if a_poison >=1:
                "[crab_name] is already poisoned!"
            elif special_roll == "1":
                $ a_poison = 3
                "[crab_name] is poisoned!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "4":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "5":
            $ opp_acc +=8
            "enemy [enemy_crab_name]'s acc went up!"
        if enemy_crab_type == "6":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used poison!"
            with vshake
            $ renpy.pause(0.3)
            if a_poison >=1:
                "[crab_name] is already poisoned!"
            elif special_roll == "1":
                $ a_poison = 3
                "[crab_name] is poisoned!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"
        if enemy_crab_type == "7":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "8":
            $ opp_acc +=8
            $ opp_att -=8
            "enemy [enemy_crab_name]'s acc went up!"
            "enemy [enemy_crab_name]'s att went down!"
        if enemy_crab_type == "9":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used poison!"
            with vshake
            $ renpy.pause(0.3)
            if a_poison >=1:
                "[crab_name] is already poisoned!"
            elif special_roll == "1":
                $ a_poison = 3
                "[crab_name] is poisoned!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"
        if enemy_crab_type == "10":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "11":
            $ opp_acc -=8
            $ opp_att +=8
            "enemy [enemy_crab_name]'s att went up!"
            "enemy [enemy_crab_name]'s acc went down!"

        jump arena_crab_battle_player2

    if randcrabattack ==3:
        if enemy_crab_type == "1":
            $ opp_att +=8
            $ opp_def -=8
            "enemy [enemy_crab_name]'s att went up!"
            "enemy [enemy_crab_name]'s def went down!"
        if enemy_crab_type == "2":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "3":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "4":
            $ opp_att +=8
            $ crab_hurt_self = math.ceil(crab_max_health*0.1)


            if arena_crab ==1:
                $ enemy_crab1_hp -= crab_hurt_self
                $ crab_health = enemy_crab1_hp

            if arena_crab ==2:
                $ enemy_crab2_hp -= crab_hurt_self
                $ crab_health = enemy_crab2_hp

            if arena_crab ==3:
                $ enemy_crab3_hp -= crab_hurt_self
                $ crab_health = enemy_crab3_hp

            if arena_crab ==4:
                $ enemy_crab4_hp -= crab_hurt_self
                $ crab_health = enemy_crab4_hp

            if arena_crab ==5:
                $ enemy_crab5_hp -= crab_hurt_self
                $ crab_health = enemy_crab5_hp

            "enemy [enemy_crab_name]'s att went up!"
            "enemy [enemy_crab_name]'s hp went down!"
        if enemy_crab_type == "5":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "6":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "7":
            $ opp_def +=8
            "enemy [enemy_crab_name]'s def went up!"
        if enemy_crab_type == "8":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "9":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        if enemy_crab_type == "10":
            $ opp_acc +=8
            $ opp_def +=8
            "enemy [enemy_crab_name]'s acc went up!"
            "enemy [enemy_crab_name]'s def went up!"
        if enemy_crab_type == "11":
            $ enemy_crab_charge = True
            "enemy [enemy_crab_name] charges its attack!"
        jump arena_crab_battle_player2

    if randcrabattack ==4:
        if enemy_crab_type == "1":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used bind!"
            with vshake
            $ renpy.pause(0.3)
            if a_bind >=1:
                "[crab_name] is already bound!"
            elif special_roll == "1":
                $ a_bind = 3
                "[crab_name] was bound! they may not be able to attack!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "2":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used bind!"
            with vshake
            $ renpy.pause(0.3)
            if a_bind >=1:
                "[crab_name] is already bound!"
            elif special_roll == "1":
                $ a_bind = 3
                "[crab_name] is bound! they may not be able to attack!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "3":
            $ opp_att -=8
            $ opp_def +=8
            "enemy [enemy_crab_name]'s def went up!"
            "enemy [enemy_crab_name]'s att went down!"

        if enemy_crab_type == "4":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used confuse!"
            with vshake
            $ renpy.pause(0.3)
            if a_confuse >=1:
                "[crab_name] is already confused!"
            elif special_roll == "1":
                $ a_confuse = 3
                "[crab_name] is confused! they may hurt themselves!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "5":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used weak!"
            with vshake
            $ renpy.pause(0.3)
            if a_weak >=1:
                "[crab_name] is already weak!"
            elif special_roll == "1":
                $ a_weak = 3
                "[crab_name] is weakened! they can only use their regular attack!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "6":
            $ opp_acc +=8
            $ opp_def +=8
            "enemy [enemy_crab_name]'s acc went up!"
            "enemy [enemy_crab_name]'s def went up!"

        if enemy_crab_type == "7":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used bind!"
            with vshake
            $ renpy.pause(0.3)
            if a_bind >=1:
                "[crab_name] is already bound!"
            elif special_roll == "1":
                $ a_bind = 3
                "[crab_name] is bound! they may not be able to attack!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "8":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used confuse!"
            with vshake
            $ renpy.pause(0.3)
            if a_confuse >=1:
                "[crab_name] is already confused!"
            elif special_roll == "1":
                $ a_confuse = 3
                "[crab_name] is confused! they may hurt themselves!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "9":
            $ opp_acc -=8
            $ opp_att +=8
            "enemy [enemy_crab_name]'s att went up!"
            "enemy [enemy_crab_name]'s acc went down!"

        if enemy_crab_type == "10":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used confuse!"
            with vshake
            $ renpy.pause(0.3)
            if a_confuse >=1:
                "[crab_name] is already confused!"
            elif special_roll == "1":
                $ a_confuse = 3
                "[crab_name] is confused! they may hurt themselves!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        if enemy_crab_type == "11":
            $ special_roll = WeightedChoice([("1", 0.75), ("2", 0.25)])
            "enemy [enemy_crab_name] used weak!"
            with vshake
            $ renpy.pause(0.3)
            if a_weak >=1:
                "[crab_name] is already weak!"
            elif special_roll == "1":
                $ a_weak = 3
                "[crab_name] is weakened! they can only use their regular attack!"
            elif special_roll == "2":
                "enemy [enemy_crab_name] missed!"

        jump arena_crab_battle_player2

label enemy_regular_attack:
    if enemy_crab_type == "1":
        "enemy [enemy_crab_name] used slash!"
    if enemy_crab_type == "2":
        "enemy [enemy_crab_name] used reach!"
    if enemy_crab_type == "3":
        "enemy [enemy_crab_name] used grip!"
    if enemy_crab_type == "4":
        "enemy [enemy_crab_name] used slice!"
    if enemy_crab_type == "5":
        "enemy [enemy_crab_name] used dope fade!"
    if enemy_crab_type == "6":
        "enemy [enemy_crab_name] used nibble!"
    if enemy_crab_type == "7":
        "enemy [enemy_crab_name] used spike!"
    if enemy_crab_type == "8":
        "enemy [enemy_crab_name] used stare!"
    if enemy_crab_type == "9":
        "enemy [enemy_crab_name] used clamp!"
    if enemy_crab_type == "10":
        "enemy [enemy_crab_name] used bump!"
    if enemy_crab_type == "11":
        "enemy [enemy_crab_name] used grapple!"

    $ enemy_hit_chance = (opp_acc - (opp_acc * (1 - ((opp_acc/4)*0.02))))


    if hit_chance <=0.2:
        $ rand_accuracy = WeightedChoice([("low", 0.50), ("mediocre", 0.50)])
        if rand_accuracy == "low":
            $ arena_enemy_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_enemy_attack_chance = "mediocre"

    elif hit_chance <=0.28:
        $ rand_accuracy = WeightedChoice([("low", 0.30), ("mediocre", 0.70)])
        if rand_accuracy == "low":
            $ arena_enemy_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_enemy_attack_chance = "mediocre"

    elif hit_chance <=0.32:
        $ rand_accuracy = WeightedChoice([("low", 0.20), ("mediocre", 0.80)])
        if rand_accuracy == "low":
            $ arena_enemy_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_enemy_attack_chance = "mediocre"

    elif hit_chance <=0.36:
        $ rand_accuracy = WeightedChoice([("low", 0.10), ("mediocre", 0.90)])
        if rand_accuracy == "low":
            $ arena_enemy_attack_chance = "low"
        if rand_accuracy == "mediocre":
            $ arena_enemy_attack_chance = "mediocre"

    elif hit_chance <=0.52:
        $ rand_accuracy = WeightedChoice([("high", 0.10), ("mediocre", 0.90)])
        if rand_accuracy == "high":
            $ arena_enemy_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_enemy_attack_chance = "mediocre"

    elif hit_chance <=0.72:
        $ rand_accuracy = WeightedChoice([("high", 0.20), ("mediocre", 0.80)])
        if rand_accuracy == "high":
            $ arena_enemy_attack_chance = "high"
        if rand_accuracy == "mediocre":
            $ arena_enemy_attack_chance = "mediocre"
    elif hit_chance <=1:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.80), ("ultimate", 0.20)])
        if rand_accuracy == "high":
            $ arena_enemy_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_enemy_attack_chance = "ultimate"

    elif hit_chance > 1:
        $ rand_accuracy = WeightedChoice([("high", 0.70), ("ultimate", 0.30)])
        if rand_accuracy == "high":
            $ arena_enemy_attack_chance = "high"
        if rand_accuracy == "ultimate":
            $ arena_enemy_attack_chance = "ultimate"

    jump enemy_attack_chance

label enemy_attack_chance:

    if arena_enemy_attack_chance == "none":
        $ rand_arena_attack = renpy.random.choice(['hit'])

    elif arena_enemy_attack_chance == "low":
        $ rand_arena_attack = renpy.random.choice(['hit', 'hit', 'hit', 'hit','miss'])

    elif arena_enemy_attack_chance == "mediocre":
        $ rand_arena_attack = renpy.random.choice(['hit','hit', 'hit','miss', 'miss'])

    elif arena_enemy_attack_chance == "high":
        $ rand_arena_attack = renpy.random.choice(['hit','hit','miss','miss','miss'])

    elif arena_enemy_attack_chance == "ultimate":
        $ rand_arena_attack = renpy.random.choice(['hit','miss'])

    if rand_arena_attack == 'hit':
        show arena_swipe:
            xpos 30 ypos 150
        with dissolve
        $ renpy.pause(0.3)
        hide arena_swipe with dissolve
        $ renpy.pause(0.3)




        $ enemy_level_ratio = (enemy_crab_level - crab_level)
        $ enemy_level_ratio2 = (crab_level - enemy_crab_level)







        if enemy_level_ratio >=4:
            $ pain = math.ceil((((opp_att-enemy_level_ratio) - (crab_def+(enemy_level_ratio*5)))))
        if enemy_level_ratio >=0 and enemy_level_ratio <4:
            $ pain = math.ceil((((opp_att-enemy_level_ratio) - (crab_def+(enemy_level_ratio*4)))))
        else:
            if enemy_level_ratio2 <=-4:
                $ pain = math.ceil((((opp_att+(enemy_level_ratio2*5)) - (crab_def-enemy_level_ratio2))))
            else:
                $ pain = math.ceil((((opp_att+(enemy_level_ratio2*4)) - (crab_def-enemy_level_ratio2))))


        $ pain = math.ceil(((opp_att+crab_def)/crab_def)*(enemy_crab_level))

        if pain <=1:
            $ pain = 2



        $ pain +=1
        $ crab_standin_health -= pain

        if crab1_active:
            $ crab1_temp_hp -= pain
        if crab2_active:
            $ crab2_temp_hp -= pain
        if crab3_active:
            $ crab3_temp_hp -= pain
        if crab4_active:
            $ crab4_temp_hp -= pain
        if crab5_active:
            $ crab5_temp_hp -= pain
        if crab6_active:
            $ crab6_temp_hp -= pain
        if crab7_active:
            $ crab7_temp_hp -= pain
        if crab8_active:
            $ crab8_temp_hp -= pain
        if crab9_active:
            $ crab9_temp_hp -= pain
        if crab10_active:
            $ crab10_temp_hp -= pain
        if crab11_active:
            $ crab11_temp_hp -= pain
        if crab12_active:
            $ crab12_temp_hp -= pain
        if crab13_active:
            $ crab13_temp_hp -= pain
        if crab14_active:
            $ crab14_temp_hp -= pain
        if crab15_active:
            $ crab15_temp_hp -= pain
        if crab16_active:
            $ crab16_temp_hp -= pain
        if crab17_active:
            $ crab17_temp_hp -= pain
        if crab18_active:
            $ crab18_temp_hp -= pain
        if crab19_active:
            $ crab19_temp_hp -= pain
        if crab20_active:
            $ crab20_temp_hp -= pain
        if crab21_active:
            $ crab21_temp_hp -= pain
        if crab22_active:
            $ crab22_temp_hp -= pain
        if crab23_active:
            $ crab23_temp_hp -= pain
        if crab24_active:
            $ crab24_temp_hp -= pain
        if crab25_active:
            $ crab25_temp_hp -= pain
        if crab26_active:
            $ crab26_temp_hp -= pain
        if crab27_active:
            $ crab27_temp_hp -= pain
        if crab28_active:
            $ crab28_temp_hp -= pain
        if crab29_active:
            $ crab29_temp_hp -= pain
        if crab30_active:
            $ crab30_temp_hp -= pain

        $ arena_xpos_lifebar_player = (360-((crab_health*360)/enemy_crab_health_max))


    if rand_arena_attack == 'miss':
        "enemy [enemy_crab_name] missed!"

    jump arena_crab_battle_player2



























































































label arena_end_level_check:
    $ first_arena_fought = True

    $ shared_arena_exp = math.ceil(total_arena_exp/crabs_getting_exp)

    if crab1_exp:
        $ crab1_total_exp += shared_arena_exp
        "[crab1_name] got [shared_arena_exp] exp!"
        if crab1_level <=98:
            jump crab1_leveling_check
            label crab1_leveling_check:
                $ crab1_exp_check = ((crab1_level*crab1_level*crab1_level)/4)
                if crab1_total_exp >= crab1_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab1_level +=1
                    "[crab1_name] reached level [crab1_level]!"
                    if crab1_rarity == "n":
                        if crab1_level >=5 and not crab1_move2:
                            "[crab1_name] learned a new move!"
                            $ crab1_move2 = True
                        if crab1_level >=10 and not crab1_move3:
                            "[crab1_name] learned a new move!"
                            $ crab1_move3 = True
                        if crab1_level >=15 and not crab1_move4:
                            "[crab1_name] learned a new move!"
                            $ crab1_move4 = True
                    if crab1_rarity == "r":
                        if crab1_level >=8 and not crab1_move2:
                            "[crab1_name] learned a new move!"
                            $ crab1_move2 = True
                        if crab1_level >=14 and not crab1_move3:
                            "[crab1_name] learned a new move!"
                            $ crab1_move3 = True
                        if crab1_level >=18 and not crab1_move4:
                            "[crab1_name] learned a new move!"
                            $ crab1_move4 = True
                    if crab1_rarity == "e":
                        if crab1_level >=12 and not crab1_move2:
                            "[crab1_name] learned a new move!"
                            $ crab1_move2 = True
                        if crab1_level >=16 and not crab1_move3:
                            "[crab1_name] learned a new move!"
                            $ crab1_move3 = True
                        if crab1_level >=22 and not crab1_move4:
                            "[crab1_name] learned a new move!"
                            $ crab1_move4 = True
                    if crab1_rarity == "l":
                        if crab1_level >=14 and not crab1_move2:
                            "[crab1_name] learned a new move!"
                            $ crab1_move2 = True
                        if crab1_level >=20 and not crab1_move3:
                            "[crab1_name] learned a new move!"
                            $ crab1_move3 = True
                        if crab1_level >=25 and not crab1_move4:
                            "[crab1_name] learned a new move!"
                            $ crab1_move4 = True

                    jump crab1_leveling_check
    if crab2_exp:
        $ crab2_total_exp += shared_arena_exp
        "[crab2_name] got [shared_arena_exp] exp!"
        if crab2_level <=98:
            jump crab2_leveling_check
            label crab2_leveling_check:
                $ crab2_exp_check = ((crab2_level*crab2_level*crab2_level)/4)
                if crab2_total_exp >= crab2_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab2_level +=1
                    "[crab2_name] reached level [crab2_level]!"
                    if crab2_rarity == "n":
                        if crab2_level >=5 and not crab2_move2:
                            "[crab2_name] learned a new move!"
                            $ crab2_move2 = True
                        if crab2_level >=10 and not crab2_move3:
                            "[crab2_name] learned a new move!"
                            $ crab2_move3 = True
                        if crab2_level >=15 and not crab2_move4:
                            "[crab2_name] learned a new move!"
                            $ crab2_move4 = True
                    if crab2_rarity == "r":
                        if crab2_level >=8 and not crab2_move2:
                            "[crab2_name] learned a new move!"
                            $ crab2_move2 = True
                        if crab2_level >=14 and not crab2_move3:
                            "[crab2_name] learned a new move!"
                            $ crab2_move3 = True
                        if crab2_level >=18 and not crab2_move4:
                            "[crab2_name] learned a new move!"
                            $ crab2_move4 = True
                    if crab2_rarity == "e":
                        if crab2_level >=12 and not crab2_move2:
                            "[crab2_name] learned a new move!"
                            $ crab2_move2 = True
                        if crab2_level >=16 and not crab2_move3:
                            "[crab2_name] learned a new move!"
                            $ crab2_move3 = True
                        if crab2_level >=22 and not crab2_move4:
                            "[crab2_name] learned a new move!"
                            $ crab2_move4 = True
                    if crab2_rarity == "l":
                        if crab2_level >=14 and not crab2_move2:
                            "[crab2_name] learned a new move!"
                            $ crab2_move2 = True
                        if crab2_level >=20 and not crab2_move3:
                            "[crab2_name] learned a new move!"
                            $ crab2_move3 = True
                        if crab2_level >=25 and not crab2_move4:
                            "[crab2_name] learned a new move!"
                            $ crab2_move4 = True
                    jump crab2_leveling_check
    if crab3_exp:
        $ crab3_total_exp += shared_arena_exp
        "[crab3_name] got [shared_arena_exp] exp!"
        if crab3_level <=98:
            jump crab3_leveling_check
            label crab3_leveling_check:
                $ crab3_exp_check = ((crab3_level*crab3_level*crab3_level)/4)
                if crab3_total_exp >= crab3_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab3_level +=1
                    "[crab3_name] reached level [crab3_level]!"
                    if crab3_rarity == "n":
                        if crab3_level >=5 and not crab3_move2:
                            "[crab3_name] learned a new move!"
                            $ crab3_move2 = True
                        if crab3_level >=10 and not crab3_move3:
                            "[crab3_name] learned a new move!"
                            $ crab3_move3 = True
                        if crab3_level >=15 and not crab3_move4:
                            "[crab3_name] learned a new move!"
                            $ crab3_move4 = True
                    if crab3_rarity == "r":
                        if crab3_level >=8 and not crab3_move2:
                            "[crab3_name] learned a new move!"
                            $ crab3_move2 = True
                        if crab3_level >=14 and not crab3_move3:
                            "[crab3_name] learned a new move!"
                            $ crab3_move3 = True
                        if crab3_level >=18 and not crab3_move4:
                            "[crab3_name] learned a new move!"
                            $ crab3_move4 = True
                    if crab3_rarity == "e":
                        if crab3_level >=12 and not crab3_move2:
                            "[crab3_name] learned a new move!"
                            $ crab3_move2 = True
                        if crab3_level >=16 and not crab3_move3:
                            "[crab3_name] learned a new move!"
                            $ crab3_move3 = True
                        if crab3_level >=22 and not crab3_move4:
                            "[crab3_name] learned a new move!"
                            $ crab3_move4 = True
                    if crab3_rarity == "l":
                        if crab3_level >=14 and not crab3_move2:
                            "[crab3_name] learned a new move!"
                            $ crab3_move2 = True
                        if crab3_level >=20 and not crab3_move3:
                            "[crab3_name] learned a new move!"
                            $ crab3_move3 = True
                        if crab3_level >=25 and not crab3_move4:
                            "[crab3_name] learned a new move!"
                            $ crab3_move4 = True
                    jump crab3_leveling_check
    if crab4_exp:
        $ crab4_total_exp += shared_arena_exp
        "[crab4_name] got [shared_arena_exp] exp!"
        if crab4_level <=98:
            jump crab4_leveling_check
            label crab4_leveling_check:
                $ crab4_exp_check = ((crab4_level*crab4_level*crab4_level)/4)
                if crab4_total_exp >= crab4_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab4_level +=1
                    "[crab4_name] reached level [crab4_level]!"
                    if crab4_rarity == "n":
                        if crab4_level >=5 and not crab4_move2:
                            "[crab4_name] learned a new move!"
                            $ crab4_move2 = True
                        if crab4_level >=10 and not crab4_move3:
                            "[crab4_name] learned a new move!"
                            $ crab4_move3 = True
                        if crab4_level >=15 and not crab4_move4:
                            "[crab4_name] learned a new move!"
                            $ crab4_move4 = True
                    if crab4_rarity == "r":
                        if crab4_level >=8 and not crab4_move2:
                            "[crab4_name] learned a new move!"
                            $ crab4_move2 = True
                        if crab4_level >=14 and not crab4_move3:
                            "[crab4_name] learned a new move!"
                            $ crab4_move3 = True
                        if crab4_level >=18 and not crab4_move4:
                            "[crab4_name] learned a new move!"
                            $ crab4_move4 = True
                    if crab4_rarity == "e":
                        if crab4_level >=12 and not crab4_move2:
                            "[crab4_name] learned a new move!"
                            $ crab4_move2 = True
                        if crab4_level >=16 and not crab4_move3:
                            "[crab4_name] learned a new move!"
                            $ crab4_move3 = True
                        if crab4_level >=22 and not crab4_move4:
                            "[crab4_name] learned a new move!"
                            $ crab4_move4 = True
                    if crab4_rarity == "l":
                        if crab4_level >=14 and not crab4_move2:
                            "[crab4_name] learned a new move!"
                            $ crab4_move2 = True
                        if crab4_level >=20 and not crab4_move3:
                            "[crab4_name] learned a new move!"
                            $ crab4_move3 = True
                        if crab4_level >=25 and not crab4_move4:
                            "[crab4_name] learned a new move!"
                            $ crab4_move4 = True
                    jump crab4_leveling_check
    if crab5_exp:
        $ crab5_total_exp += shared_arena_exp
        "[crab5_name] got [shared_arena_exp] exp!"
        if crab5_level <=98:
            jump crab5_leveling_check
            label crab5_leveling_check:
                $ crab5_exp_check = ((crab5_level*crab5_level*crab5_level)/4)
                if crab5_total_exp >= crab5_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab5_level +=1
                    "[crab5_name] reached level [crab5_level]!"
                    if crab5_rarity == "n":
                        if crab5_level >=5 and not crab5_move2:
                            "[crab5_name] learned a new move!"
                            $ crab5_move2 = True
                        if crab5_level >=10 and not crab5_move3:
                            "[crab5_name] learned a new move!"
                            $ crab5_move3 = True
                        if crab5_level >=15 and not crab5_move4:
                            "[crab5_name] learned a new move!"
                            $ crab5_move4 = True
                    if crab5_rarity == "r":
                        if crab5_level >=8 and not crab5_move2:
                            "[crab5_name] learned a new move!"
                            $ crab5_move2 = True
                        if crab5_level >=14 and not crab5_move3:
                            "[crab5_name] learned a new move!"
                            $ crab5_move3 = True
                        if crab5_level >=18 and not crab5_move4:
                            "[crab5_name] learned a new move!"
                            $ crab5_move4 = True
                    if crab5_rarity == "e":
                        if crab5_level >=12 and not crab5_move2:
                            "[crab5_name] learned a new move!"
                            $ crab5_move2 = True
                        if crab5_level >=16 and not crab5_move3:
                            "[crab5_name] learned a new move!"
                            $ crab5_move3 = True
                        if crab5_level >=22 and not crab5_move4:
                            "[crab5_name] learned a new move!"
                            $ crab5_move4 = True
                    if crab5_rarity == "l":
                        if crab5_level >=14 and not crab5_move2:
                            "[crab5_name] learned a new move!"
                            $ crab5_move2 = True
                        if crab5_level >=20 and not crab5_move3:
                            "[crab5_name] learned a new move!"
                            $ crab5_move3 = True
                        if crab5_level >=25 and not crab5_move4:
                            "[crab5_name] learned a new move!"
                            $ crab5_move4 = True
                    jump crab5_leveling_check
    if crab6_exp:
        $ crab6_total_exp += shared_arena_exp
        "[crab6_name] got [shared_arena_exp] exp!"
        if crab6_level <=98:
            jump crab6_leveling_check
            label crab6_leveling_check:
                $ crab6_exp_check = ((crab6_level*crab6_level*crab6_level)/4)
                if crab6_total_exp >= crab6_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab6_level +=1
                    "[crab6_name] reached level [crab6_level]!"
                    if crab6_rarity == "n":
                        if crab6_level >=5 and not crab6_move2:
                            "[crab6_name] learned a new move!"
                            $ crab6_move2 = True
                        if crab6_level >=10 and not crab6_move3:
                            "[crab6_name] learned a new move!"
                            $ crab6_move3 = True
                        if crab6_level >=15 and not crab6_move4:
                            "[crab6_name] learned a new move!"
                            $ crab6_move4 = True
                    if crab6_rarity == "r":
                        if crab6_level >=8 and not crab6_move2:
                            "[crab6_name] learned a new move!"
                            $ crab6_move2 = True
                        if crab6_level >=14 and not crab6_move3:
                            "[crab6_name] learned a new move!"
                            $ crab6_move3 = True
                        if crab6_level >=18 and not crab6_move4:
                            "[crab6_name] learned a new move!"
                            $ crab6_move4 = True
                    if crab6_rarity == "e":
                        if crab6_level >=12 and not crab6_move2:
                            "[crab6_name] learned a new move!"
                            $ crab6_move2 = True
                        if crab6_level >=16 and not crab6_move3:
                            "[crab6_name] learned a new move!"
                            $ crab6_move3 = True
                        if crab6_level >=22 and not crab6_move4:
                            "[crab6_name] learned a new move!"
                            $ crab6_move4 = True
                    if crab6_rarity == "l":
                        if crab6_level >=14 and not crab6_move2:
                            "[crab6_name] learned a new move!"
                            $ crab6_move2 = True
                        if crab6_level >=20 and not crab6_move3:
                            "[crab6_name] learned a new move!"
                            $ crab6_move3 = True
                        if crab6_level >=25 and not crab6_move4:
                            "[crab6_name] learned a new move!"
                            $ crab6_move4 = True
                    jump crab6_leveling_check
    if crab7_exp:
        $ crab7_total_exp += shared_arena_exp
        "[crab7_name] got [shared_arena_exp] exp!"
        if crab7_level <=98:
            jump crab7_leveling_check
            label crab7_leveling_check:
                $ crab7_exp_check = ((crab7_level*crab7_level*crab7_level)/4)
                if crab7_total_exp >= crab7_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab7_level +=1
                    "[crab7_name] reached level [crab7_level]!"
                    if crab7_rarity == "n":
                        if crab7_level >=5 and not crab7_move2:
                            "[crab7_name] learned a new move!"
                            $ crab7_move2 = True
                        if crab7_level >=10 and not crab7_move3:
                            "[crab7_name] learned a new move!"
                            $ crab7_move3 = True
                        if crab7_level >=15 and not crab7_move4:
                            "[crab7_name] learned a new move!"
                            $ crab7_move4 = True
                    if crab7_rarity == "r":
                        if crab7_level >=8 and not crab7_move2:
                            "[crab7_name] learned a new move!"
                            $ crab7_move2 = True
                        if crab7_level >=14 and not crab7_move3:
                            "[crab7_name] learned a new move!"
                            $ crab7_move3 = True
                        if crab7_level >=18 and not crab7_move4:
                            "[crab7_name] learned a new move!"
                            $ crab7_move4 = True
                    if crab7_rarity == "e":
                        if crab7_level >=12 and not crab7_move2:
                            "[crab7_name] learned a new move!"
                            $ crab7_move2 = True
                        if crab7_level >=16 and not crab7_move3:
                            "[crab7_name] learned a new move!"
                            $ crab7_move3 = True
                        if crab7_level >=22 and not crab7_move4:
                            "[crab7_name] learned a new move!"
                            $ crab7_move4 = True
                    if crab7_rarity == "l":
                        if crab7_level >=14 and not crab7_move2:
                            "[crab7_name] learned a new move!"
                            $ crab7_move2 = True
                        if crab7_level >=20 and not crab7_move3:
                            "[crab7_name] learned a new move!"
                            $ crab7_move3 = True
                        if crab7_level >=25 and not crab7_move4:
                            "[crab7_name] learned a new move!"
                            $ crab7_move4 = True
                    jump crab7_leveling_check
    if crab8_exp:
        $ crab8_total_exp += shared_arena_exp
        "[crab8_name] got [shared_arena_exp] exp!"
        if crab8_level <=98:
            jump crab8_leveling_check
            label crab8_leveling_check:
                $ crab8_exp_check = ((crab8_level*crab8_level*crab8_level)/4)
                if crab8_total_exp >= crab8_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab8_level +=1
                    "[crab8_name] reached level [crab8_level]!"
                    if crab8_rarity == "n":
                        if crab8_level >=5 and not crab8_move2:
                            "[crab8_name] learned a new move!"
                            $ crab8_move2 = True
                        if crab8_level >=10 and not crab8_move3:
                            "[crab8_name] learned a new move!"
                            $ crab8_move3 = True
                        if crab8_level >=15 and not crab8_move4:
                            "[crab8_name] learned a new move!"
                            $ crab8_move4 = True
                    if crab8_rarity == "r":
                        if crab8_level >=8 and not crab8_move2:
                            "[crab8_name] learned a new move!"
                            $ crab8_move2 = True
                        if crab8_level >=14 and not crab8_move3:
                            "[crab8_name] learned a new move!"
                            $ crab8_move3 = True
                        if crab8_level >=18 and not crab8_move4:
                            "[crab8_name] learned a new move!"
                            $ crab8_move4 = True
                    if crab8_rarity == "e":
                        if crab8_level >=12 and not crab8_move2:
                            "[crab8_name] learned a new move!"
                            $ crab8_move2 = True
                        if crab8_level >=16 and not crab8_move3:
                            "[crab8_name] learned a new move!"
                            $ crab8_move3 = True
                        if crab8_level >=22 and not crab8_move4:
                            "[crab8_name] learned a new move!"
                            $ crab8_move4 = True
                    if crab8_rarity == "l":
                        if crab8_level >=14 and not crab8_move2:
                            "[crab8_name] learned a new move!"
                            $ crab8_move2 = True
                        if crab8_level >=20 and not crab8_move3:
                            "[crab8_name] learned a new move!"
                            $ crab8_move3 = True
                        if crab8_level >=25 and not crab8_move4:
                            "[crab8_name] learned a new move!"
                            $ crab8_move4 = True
                    jump crab8_leveling_check
    if crab9_exp:
        $ crab9_total_exp += shared_arena_exp
        "[crab9_name] got [shared_arena_exp] exp!"
        if crab9_level <=98:
            jump crab9_leveling_check
            label crab9_leveling_check:
                $ crab9_exp_check = ((crab9_level*crab9_level*crab9_level)/4)
                if crab9_total_exp >= crab9_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab9_level +=1
                    "[crab9_name] reached level [crab9_level]!"
                    if crab9_rarity == "n":
                        if crab9_level >=5 and not crab9_move2:
                            "[crab9_name] learned a new move!"
                            $ crab9_move2 = True
                        if crab9_level >=10 and not crab9_move3:
                            "[crab9_name] learned a new move!"
                            $ crab9_move3 = True
                        if crab9_level >=15 and not crab9_move4:
                            "[crab9_name] learned a new move!"
                            $ crab9_move4 = True
                    if crab9_rarity == "r":
                        if crab9_level >=8 and not crab9_move2:
                            "[crab9_name] learned a new move!"
                            $ crab9_move2 = True
                        if crab9_level >=14 and not crab9_move3:
                            "[crab9_name] learned a new move!"
                            $ crab9_move3 = True
                        if crab9_level >=18 and not crab9_move4:
                            "[crab9_name] learned a new move!"
                            $ crab9_move4 = True
                    if crab9_rarity == "e":
                        if crab9_level >=12 and not crab9_move2:
                            "[crab9_name] learned a new move!"
                            $ crab9_move2 = True
                        if crab9_level >=16 and not crab9_move3:
                            "[crab9_name] learned a new move!"
                            $ crab9_move3 = True
                        if crab9_level >=22 and not crab9_move4:
                            "[crab9_name] learned a new move!"
                            $ crab9_move4 = True
                    if crab9_rarity == "l":
                        if crab9_level >=14 and not crab9_move2:
                            "[crab9_name] learned a new move!"
                            $ crab9_move2 = True
                        if crab9_level >=20 and not crab9_move3:
                            "[crab9_name] learned a new move!"
                            $ crab9_move3 = True
                        if crab9_level >=25 and not crab9_move4:
                            "[crab9_name] learned a new move!"
                            $ crab9_move4 = True
                    jump crab9_leveling_check
    if crab10_exp:
        $ crab10_total_exp += shared_arena_exp
        "[crab10_name] got [shared_arena_exp] exp!"
        if crab10_level <=98:
            jump crab10_leveling_check
            label crab10_leveling_check:
                $ crab10_exp_check = ((crab10_level*crab10_level*crab10_level)/4)
                if crab10_total_exp >= crab10_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab10_level +=1
                    "[crab10_name] reached level [crab10_level]!"
                    if crab10_rarity == "n":
                        if crab10_level >=5 and not crab10_move2:
                            "[crab10_name] learned a new move!"
                            $ crab10_move2 = True
                        if crab10_level >=10 and not crab10_move3:
                            "[crab10_name] learned a new move!"
                            $ crab10_move3 = True
                        if crab10_level >=15 and not crab10_move4:
                            "[crab10_name] learned a new move!"
                            $ crab10_move4 = True
                    if crab10_rarity == "r":
                        if crab10_level >=8 and not crab10_move2:
                            "[crab10_name] learned a new move!"
                            $ crab10_move2 = True
                        if crab10_level >=14 and not crab10_move3:
                            "[crab10_name] learned a new move!"
                            $ crab10_move3 = True
                        if crab10_level >=18 and not crab10_move4:
                            "[crab10_name] learned a new move!"
                            $ crab10_move4 = True
                    if crab10_rarity == "e":
                        if crab10_level >=12 and not crab10_move2:
                            "[crab10_name] learned a new move!"
                            $ crab10_move2 = True
                        if crab10_level >=16 and not crab10_move3:
                            "[crab10_name] learned a new move!"
                            $ crab10_move3 = True
                        if crab10_level >=22 and not crab10_move4:
                            "[crab10_name] learned a new move!"
                            $ crab10_move4 = True
                    if crab10_rarity == "l":
                        if crab10_level >=14 and not crab10_move2:
                            "[crab10_name] learned a new move!"
                            $ crab10_move2 = True
                        if crab10_level >=20 and not crab10_move3:
                            "[crab10_name] learned a new move!"
                            $ crab10_move3 = True
                        if crab10_level >=25 and not crab10_move4:
                            "[crab10_name] learned a new move!"
                            $ crab10_move4 = True
                    jump crab10_leveling_check
    if crab11_exp:
        $ crab11_total_exp += shared_arena_exp
        "[crab11_name] got [shared_arena_exp] exp!"
        if crab11_level <=98:
            jump crab11_leveling_check
            label crab11_leveling_check:
                $ crab11_exp_check = ((crab11_level*crab11_level*crab11_level)/4)
                if crab11_total_exp >= crab11_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab11_level +=1
                    "[crab11_name] reached level [crab11_level]!"
                    if crab11_rarity == "n":
                        if crab11_level >=5 and not crab11_move2:
                            "[crab11_name] learned a new move!"
                            $ crab11_move2 = True
                        if crab11_level >=10 and not crab11_move3:
                            "[crab11_name] learned a new move!"
                            $ crab11_move3 = True
                        if crab11_level >=15 and not crab11_move4:
                            "[crab11_name] learned a new move!"
                            $ crab11_move4 = True
                    if crab11_rarity == "r":
                        if crab11_level >=8 and not crab11_move2:
                            "[crab11_name] learned a new move!"
                            $ crab11_move2 = True
                        if crab11_level >=14 and not crab11_move3:
                            "[crab11_name] learned a new move!"
                            $ crab11_move3 = True
                        if crab11_level >=18 and not crab11_move4:
                            "[crab11_name] learned a new move!"
                            $ crab11_move4 = True
                    if crab11_rarity == "e":
                        if crab11_level >=12 and not crab11_move2:
                            "[crab11_name] learned a new move!"
                            $ crab11_move2 = True
                        if crab11_level >=16 and not crab11_move3:
                            "[crab11_name] learned a new move!"
                            $ crab11_move3 = True
                        if crab11_level >=22 and not crab11_move4:
                            "[crab11_name] learned a new move!"
                            $ crab11_move4 = True
                    if crab11_rarity == "l":
                        if crab11_level >=14 and not crab11_move2:
                            "[crab11_name] learned a new move!"
                            $ crab11_move2 = True
                        if crab11_level >=20 and not crab11_move3:
                            "[crab11_name] learned a new move!"
                            $ crab11_move3 = True
                        if crab11_level >=25 and not crab11_move4:
                            "[crab11_name] learned a new move!"
                            $ crab11_move4 = True
                    jump crab11_leveling_check
    if crab12_exp:
        $ crab12_total_exp += shared_arena_exp
        "[crab12_name] got [shared_arena_exp] exp!"
        if crab12_level <=98:
            jump crab12_leveling_check
            label crab12_leveling_check:
                $ crab12_exp_check = ((crab12_level*crab12_level*crab12_level)/4)
                if crab12_total_exp >= crab12_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab12_level +=1
                    "[crab12_name] reached level [crab12_level]!"
                    if crab12_rarity == "n":
                        if crab12_level >=5 and not crab12_move2:
                            "[crab12_name] learned a new move!"
                            $ crab12_move2 = True
                        if crab12_level >=10 and not crab12_move3:
                            "[crab12_name] learned a new move!"
                            $ crab12_move3 = True
                        if crab12_level >=15 and not crab12_move4:
                            "[crab12_name] learned a new move!"
                            $ crab12_move4 = True
                    if crab12_rarity == "r":
                        if crab12_level >=8 and not crab12_move2:
                            "[crab12_name] learned a new move!"
                            $ crab12_move2 = True
                        if crab12_level >=14 and not crab12_move3:
                            "[crab12_name] learned a new move!"
                            $ crab12_move3 = True
                        if crab12_level >=18 and not crab12_move4:
                            "[crab12_name] learned a new move!"
                            $ crab12_move4 = True
                    if crab12_rarity == "e":
                        if crab12_level >=12 and not crab12_move2:
                            "[crab12_name] learned a new move!"
                            $ crab12_move2 = True
                        if crab12_level >=16 and not crab12_move3:
                            "[crab12_name] learned a new move!"
                            $ crab12_move3 = True
                        if crab12_level >=22 and not crab12_move4:
                            "[crab12_name] learned a new move!"
                            $ crab12_move4 = True
                    if crab12_rarity == "l":
                        if crab12_level >=14 and not crab12_move2:
                            "[crab12_name] learned a new move!"
                            $ crab12_move2 = True
                        if crab12_level >=20 and not crab12_move3:
                            "[crab12_name] learned a new move!"
                            $ crab12_move3 = True
                        if crab12_level >=25 and not crab12_move4:
                            "[crab12_name] learned a new move!"
                            $ crab12_move4 = True
                    jump crab12_leveling_check
    if crab13_exp:
        $ crab13_total_exp += shared_arena_exp
        "[crab13_name] got [shared_arena_exp] exp!"
        if crab13_level <=98:
            jump crab13_leveling_check
            label crab13_leveling_check:
                $ crab13_exp_check = ((crab13_level*crab13_level*crab13_level)/4)
                if crab13_total_exp >= crab13_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab13_level +=1
                    "[crab13_name] reached level [crab13_level]!"
                    if crab13_rarity == "n":
                        if crab13_level >=5 and not crab13_move2:
                            "[crab13_name] learned a new move!"
                            $ crab13_move2 = True
                        if crab13_level >=10 and not crab13_move3:
                            "[crab13_name] learned a new move!"
                            $ crab13_move3 = True
                        if crab13_level >=15 and not crab13_move4:
                            "[crab13_name] learned a new move!"
                            $ crab13_move4 = True
                    if crab13_rarity == "r":
                        if crab13_level >=8 and not crab13_move2:
                            "[crab13_name] learned a new move!"
                            $ crab13_move2 = True
                        if crab13_level >=14 and not crab13_move3:
                            "[crab13_name] learned a new move!"
                            $ crab13_move3 = True
                        if crab13_level >=18 and not crab13_move4:
                            "[crab13_name] learned a new move!"
                            $ crab13_move4 = True
                    if crab13_rarity == "e":
                        if crab13_level >=12 and not crab13_move2:
                            "[crab13_name] learned a new move!"
                            $ crab13_move2 = True
                        if crab13_level >=16 and not crab13_move3:
                            "[crab13_name] learned a new move!"
                            $ crab13_move3 = True
                        if crab13_level >=22 and not crab13_move4:
                            "[crab13_name] learned a new move!"
                            $ crab13_move4 = True
                    if crab13_rarity == "l":
                        if crab13_level >=14 and not crab13_move2:
                            "[crab13_name] learned a new move!"
                            $ crab13_move2 = True
                        if crab13_level >=20 and not crab13_move3:
                            "[crab13_name] learned a new move!"
                            $ crab13_move3 = True
                        if crab13_level >=25 and not crab13_move4:
                            "[crab13_name] learned a new move!"
                            $ crab13_move4 = True
                    jump crab13_leveling_check
    if crab14_exp:
        $ crab14_total_exp += shared_arena_exp
        "[crab14_name] got [shared_arena_exp] exp!"
        if crab14_level <=98:
            jump crab14_leveling_check
            label crab14_leveling_check:
                $ crab14_exp_check = ((crab14_level*crab14_level*crab14_level)/4)
                if crab14_total_exp >= crab14_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab14_level +=1
                    "[crab14_name] reached level [crab14_level]!"
                    if crab14_rarity == "n":
                        if crab14_level >=5 and not crab14_move2:
                            "[crab14_name] learned a new move!"
                            $ crab14_move2 = True
                        if crab14_level >=10 and not crab14_move3:
                            "[crab14_name] learned a new move!"
                            $ crab14_move3 = True
                        if crab14_level >=15 and not crab14_move4:
                            "[crab14_name] learned a new move!"
                            $ crab14_move4 = True
                    if crab14_rarity == "r":
                        if crab14_level >=8 and not crab14_move2:
                            "[crab14_name] learned a new move!"
                            $ crab14_move2 = True
                        if crab14_level >=14 and not crab14_move3:
                            "[crab14_name] learned a new move!"
                            $ crab14_move3 = True
                        if crab14_level >=18 and not crab14_move4:
                            "[crab14_name] learned a new move!"
                            $ crab14_move4 = True
                    if crab14_rarity == "e":
                        if crab14_level >=12 and not crab14_move2:
                            "[crab14_name] learned a new move!"
                            $ crab14_move2 = True
                        if crab14_level >=16 and not crab14_move3:
                            "[crab14_name] learned a new move!"
                            $ crab14_move3 = True
                        if crab14_level >=22 and not crab14_move4:
                            "[crab14_name] learned a new move!"
                            $ crab14_move4 = True
                    if crab14_rarity == "l":
                        if crab14_level >=14 and not crab14_move2:
                            "[crab14_name] learned a new move!"
                            $ crab14_move2 = True
                        if crab14_level >=20 and not crab14_move3:
                            "[crab14_name] learned a new move!"
                            $ crab14_move3 = True
                        if crab14_level >=25 and not crab14_move4:
                            "[crab14_name] learned a new move!"
                            $ crab14_move4 = True
                    jump crab14_leveling_check
    if crab15_exp:
        $ crab15_total_exp += shared_arena_exp
        "[crab15_name] got [shared_arena_exp] exp!"
        if crab15_level <=98:
            jump crab15_leveling_check
            label crab15_leveling_check:
                $ crab15_exp_check = ((crab15_level*crab15_level*crab15_level)/4)
                if crab15_total_exp >= crab15_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab15_level +=1
                    "[crab15_name] reached level [crab15_level]!"
                    if crab15_rarity == "n":
                        if crab15_level >=5 and not crab15_move2:
                            "[crab15_name] learned a new move!"
                            $ crab15_move2 = True
                        if crab15_level >=10 and not crab15_move3:
                            "[crab15_name] learned a new move!"
                            $ crab15_move3 = True
                        if crab15_level >=15 and not crab15_move4:
                            "[crab15_name] learned a new move!"
                            $ crab15_move4 = True
                    if crab15_rarity == "r":
                        if crab15_level >=8 and not crab15_move2:
                            "[crab15_name] learned a new move!"
                            $ crab15_move2 = True
                        if crab15_level >=14 and not crab15_move3:
                            "[crab15_name] learned a new move!"
                            $ crab15_move3 = True
                        if crab15_level >=18 and not crab15_move4:
                            "[crab15_name] learned a new move!"
                            $ crab15_move4 = True
                    if crab15_rarity == "e":
                        if crab15_level >=12 and not crab15_move2:
                            "[crab15_name] learned a new move!"
                            $ crab15_move2 = True
                        if crab15_level >=16 and not crab15_move3:
                            "[crab15_name] learned a new move!"
                            $ crab15_move3 = True
                        if crab15_level >=22 and not crab15_move4:
                            "[crab15_name] learned a new move!"
                            $ crab15_move4 = True
                    if crab15_rarity == "l":
                        if crab15_level >=14 and not crab15_move2:
                            "[crab15_name] learned a new move!"
                            $ crab15_move2 = True
                        if crab15_level >=20 and not crab15_move3:
                            "[crab15_name] learned a new move!"
                            $ crab15_move3 = True
                        if crab15_level >=25 and not crab15_move4:
                            "[crab15_name] learned a new move!"
                            $ crab15_move4 = True
                    jump crab15_leveling_check
    if crab16_exp:
        $ crab16_total_exp += shared_arena_exp
        "[crab16_name] got [shared_arena_exp] exp!"
        if crab16_level <=98:
            jump crab16_leveling_check
            label crab16_leveling_check:
                $ crab16_exp_check = ((crab16_level*crab16_level*crab16_level)/4)
                if crab16_total_exp >= crab16_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab16_level +=1
                    "[crab16_name] reached level [crab16_level]!"
                    if crab16_rarity == "n":
                        if crab16_level >=5 and not crab16_move2:
                            "[crab16_name] learned a new move!"
                            $ crab16_move2 = True
                        if crab16_level >=10 and not crab16_move3:
                            "[crab16_name] learned a new move!"
                            $ crab16_move3 = True
                        if crab16_level >=15 and not crab16_move4:
                            "[crab16_name] learned a new move!"
                            $ crab16_move4 = True
                    if crab16_rarity == "r":
                        if crab16_level >=8 and not crab16_move2:
                            "[crab16_name] learned a new move!"
                            $ crab16_move2 = True
                        if crab16_level >=14 and not crab16_move3:
                            "[crab16_name] learned a new move!"
                            $ crab16_move3 = True
                        if crab16_level >=18 and not crab16_move4:
                            "[crab16_name] learned a new move!"
                            $ crab16_move4 = True
                    if crab16_rarity == "e":
                        if crab16_level >=12 and not crab16_move2:
                            "[crab16_name] learned a new move!"
                            $ crab16_move2 = True
                        if crab16_level >=16 and not crab16_move3:
                            "[crab16_name] learned a new move!"
                            $ crab16_move3 = True
                        if crab16_level >=22 and not crab16_move4:
                            "[crab16_name] learned a new move!"
                            $ crab16_move4 = True
                    if crab16_rarity == "l":
                        if crab16_level >=14 and not crab16_move2:
                            "[crab16_name] learned a new move!"
                            $ crab16_move2 = True
                        if crab16_level >=20 and not crab16_move3:
                            "[crab16_name] learned a new move!"
                            $ crab16_move3 = True
                        if crab16_level >=25 and not crab16_move4:
                            "[crab16_name] learned a new move!"
                            $ crab16_move4 = True
                    jump crab16_leveling_check
    if crab17_exp:
        $ crab17_total_exp += shared_arena_exp
        "[crab17_name] got [shared_arena_exp] exp!"
        if crab17_level <=98:
            jump crab17_leveling_check
            label crab17_leveling_check:
                $ crab17_exp_check = ((crab17_level*crab17_level*crab17_level)/4)
                if crab17_total_exp >= crab17_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab17_level +=1
                    "[crab17_name] reached level [crab17_level]!"
                    if crab17_rarity == "n":
                        if crab17_level >=5 and not crab17_move2:
                            "[crab17_name] learned a new move!"
                            $ crab17_move2 = True
                        if crab17_level >=10 and not crab17_move3:
                            "[crab17_name] learned a new move!"
                            $ crab17_move3 = True
                        if crab17_level >=15 and not crab17_move4:
                            "[crab17_name] learned a new move!"
                            $ crab17_move4 = True
                    if crab17_rarity == "r":
                        if crab17_level >=8 and not crab17_move2:
                            "[crab17_name] learned a new move!"
                            $ crab17_move2 = True
                        if crab17_level >=14 and not crab17_move3:
                            "[crab17_name] learned a new move!"
                            $ crab17_move3 = True
                        if crab17_level >=18 and not crab17_move4:
                            "[crab17_name] learned a new move!"
                            $ crab17_move4 = True
                    if crab17_rarity == "e":
                        if crab17_level >=12 and not crab17_move2:
                            "[crab17_name] learned a new move!"
                            $ crab17_move2 = True
                        if crab17_level >=16 and not crab17_move3:
                            "[crab17_name] learned a new move!"
                            $ crab17_move3 = True
                        if crab17_level >=22 and not crab17_move4:
                            "[crab17_name] learned a new move!"
                            $ crab17_move4 = True
                    if crab17_rarity == "l":
                        if crab17_level >=14 and not crab17_move2:
                            "[crab17_name] learned a new move!"
                            $ crab17_move2 = True
                        if crab17_level >=20 and not crab17_move3:
                            "[crab17_name] learned a new move!"
                            $ crab17_move3 = True
                        if crab17_level >=25 and not crab17_move4:
                            "[crab17_name] learned a new move!"
                            $ crab17_move4 = True
                    jump crab17_leveling_check
    if crab18_exp:
        $ crab18_total_exp += shared_arena_exp
        "[crab18_name] got [shared_arena_exp] exp!"
        if crab18_level <=98:
            jump crab18_leveling_check
            label crab18_leveling_check:
                $ crab18_exp_check = ((crab18_level*crab18_level*crab18_level)/4)
                if crab18_total_exp >= crab18_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab18_level +=1
                    "[crab18_name] reached level [crab18_level]!"
                    if crab18_rarity == "n":
                        if crab18_level >=5 and not crab18_move2:
                            "[crab18_name] learned a new move!"
                            $ crab18_move2 = True
                        if crab18_level >=10 and not crab18_move3:
                            "[crab18_name] learned a new move!"
                            $ crab18_move3 = True
                        if crab18_level >=15 and not crab18_move4:
                            "[crab18_name] learned a new move!"
                            $ crab18_move4 = True
                    if crab18_rarity == "r":
                        if crab18_level >=8 and not crab18_move2:
                            "[crab18_name] learned a new move!"
                            $ crab18_move2 = True
                        if crab18_level >=14 and not crab18_move3:
                            "[crab18_name] learned a new move!"
                            $ crab18_move3 = True
                        if crab18_level >=18 and not crab18_move4:
                            "[crab18_name] learned a new move!"
                            $ crab18_move4 = True
                    if crab18_rarity == "e":
                        if crab18_level >=12 and not crab18_move2:
                            "[crab18_name] learned a new move!"
                            $ crab18_move2 = True
                        if crab18_level >=16 and not crab18_move3:
                            "[crab18_name] learned a new move!"
                            $ crab18_move3 = True
                        if crab18_level >=22 and not crab18_move4:
                            "[crab18_name] learned a new move!"
                            $ crab18_move4 = True
                    if crab18_rarity == "l":
                        if crab18_level >=14 and not crab18_move2:
                            "[crab18_name] learned a new move!"
                            $ crab18_move2 = True
                        if crab18_level >=20 and not crab18_move3:
                            "[crab18_name] learned a new move!"
                            $ crab18_move3 = True
                        if crab18_level >=25 and not crab18_move4:
                            "[crab18_name] learned a new move!"
                            $ crab18_move4 = True
                    jump crab18_leveling_check
    if crab19_exp:
        $ crab19_total_exp += shared_arena_exp
        "[crab19_name] got [shared_arena_exp] exp!"
        if crab19_level <=98:
            jump crab19_leveling_check
            label crab19_leveling_check:
                $ crab19_exp_check = ((crab19_level*crab19_level*crab19_level)/4)
                if crab19_total_exp >= crab19_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab19_level +=1
                    "[crab19_name] reached level [crab19_level]!"
                    if crab19_rarity == "n":
                        if crab19_level >=5 and not crab19_move2:
                            "[crab19_name] learned a new move!"
                            $ crab19_move2 = True
                        if crab19_level >=10 and not crab19_move3:
                            "[crab19_name] learned a new move!"
                            $ crab19_move3 = True
                        if crab19_level >=15 and not crab19_move4:
                            "[crab19_name] learned a new move!"
                            $ crab19_move4 = True
                    if crab19_rarity == "r":
                        if crab19_level >=8 and not crab19_move2:
                            "[crab19_name] learned a new move!"
                            $ crab19_move2 = True
                        if crab19_level >=14 and not crab19_move3:
                            "[crab19_name] learned a new move!"
                            $ crab19_move3 = True
                        if crab19_level >=18 and not crab19_move4:
                            "[crab19_name] learned a new move!"
                            $ crab19_move4 = True
                    if crab19_rarity == "e":
                        if crab19_level >=12 and not crab19_move2:
                            "[crab19_name] learned a new move!"
                            $ crab19_move2 = True
                        if crab19_level >=16 and not crab19_move3:
                            "[crab19_name] learned a new move!"
                            $ crab19_move3 = True
                        if crab19_level >=22 and not crab19_move4:
                            "[crab19_name] learned a new move!"
                            $ crab19_move4 = True
                    if crab19_rarity == "l":
                        if crab19_level >=14 and not crab19_move2:
                            "[crab19_name] learned a new move!"
                            $ crab19_move2 = True
                        if crab19_level >=20 and not crab19_move3:
                            "[crab19_name] learned a new move!"
                            $ crab19_move3 = True
                        if crab19_level >=25 and not crab19_move4:
                            "[crab19_name] learned a new move!"
                            $ crab19_move4 = True
                    jump crab19_leveling_check
    if crab20_exp:
        $ crab20_total_exp += shared_arena_exp
        "[crab20_name] got [shared_arena_exp] exp!"
        if crab20_level <=98:
            jump crab20_leveling_check
            label crab20_leveling_check:
                $ crab20_exp_check = ((crab20_level*crab20_level*crab20_level)/4)
                if crab20_total_exp >= crab20_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab20_level +=1
                    "[crab20_name] reached level [crab20_level]!"
                    if crab20_rarity == "n":
                        if crab20_level >=5 and not crab20_move2:
                            "[crab20_name] learned a new move!"
                            $ crab20_move2 = True
                        if crab20_level >=10 and not crab20_move3:
                            "[crab20_name] learned a new move!"
                            $ crab20_move3 = True
                        if crab20_level >=15 and not crab20_move4:
                            "[crab20_name] learned a new move!"
                            $ crab20_move4 = True
                    if crab20_rarity == "r":
                        if crab20_level >=8 and not crab20_move2:
                            "[crab20_name] learned a new move!"
                            $ crab20_move2 = True
                        if crab20_level >=14 and not crab20_move3:
                            "[crab20_name] learned a new move!"
                            $ crab20_move3 = True
                        if crab20_level >=18 and not crab20_move4:
                            "[crab20_name] learned a new move!"
                            $ crab20_move4 = True
                    if crab20_rarity == "e":
                        if crab20_level >=12 and not crab20_move2:
                            "[crab20_name] learned a new move!"
                            $ crab20_move2 = True
                        if crab20_level >=16 and not crab20_move3:
                            "[crab20_name] learned a new move!"
                            $ crab20_move3 = True
                        if crab20_level >=22 and not crab20_move4:
                            "[crab20_name] learned a new move!"
                            $ crab20_move4 = True
                    if crab20_rarity == "l":
                        if crab20_level >=14 and not crab20_move2:
                            "[crab20_name] learned a new move!"
                            $ crab20_move2 = True
                        if crab20_level >=20 and not crab20_move3:
                            "[crab20_name] learned a new move!"
                            $ crab20_move3 = True
                        if crab20_level >=25 and not crab20_move4:
                            "[crab20_name] learned a new move!"
                            $ crab20_move4 = True
                    jump crab20_leveling_check
    if crab21_exp:
        $ crab21_total_exp += shared_arena_exp
        "[crab21_name] got [shared_arena_exp] exp!"
        if crab21_level <=98:
            jump crab21_leveling_check
            label crab21_leveling_check:
                $ crab21_exp_check = ((crab21_level*crab21_level*crab21_level)/4)
                if crab21_total_exp >= crab21_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab21_level +=1
                    "[crab21_name] reached level [crab21_level]!"
                    if crab21_rarity == "n":
                        if crab21_level >=5 and not crab21_move2:
                            "[crab21_name] learned a new move!"
                            $ crab21_move2 = True
                        if crab21_level >=10 and not crab21_move3:
                            "[crab21_name] learned a new move!"
                            $ crab21_move3 = True
                        if crab21_level >=15 and not crab21_move4:
                            "[crab21_name] learned a new move!"
                            $ crab21_move4 = True
                    if crab21_rarity == "r":
                        if crab21_level >=8 and not crab21_move2:
                            "[crab21_name] learned a new move!"
                            $ crab21_move2 = True
                        if crab21_level >=14 and not crab21_move3:
                            "[crab21_name] learned a new move!"
                            $ crab21_move3 = True
                        if crab21_level >=18 and not crab21_move4:
                            "[crab21_name] learned a new move!"
                            $ crab21_move4 = True
                    if crab21_rarity == "e":
                        if crab21_level >=12 and not crab21_move2:
                            "[crab21_name] learned a new move!"
                            $ crab21_move2 = True
                        if crab21_level >=16 and not crab21_move3:
                            "[crab21_name] learned a new move!"
                            $ crab21_move3 = True
                        if crab21_level >=22 and not crab21_move4:
                            "[crab21_name] learned a new move!"
                            $ crab21_move4 = True
                    if crab21_rarity == "l":
                        if crab21_level >=14 and not crab21_move2:
                            "[crab21_name] learned a new move!"
                            $ crab21_move2 = True
                        if crab21_level >=20 and not crab21_move3:
                            "[crab21_name] learned a new move!"
                            $ crab21_move3 = True
                        if crab21_level >=25 and not crab21_move4:
                            "[crab21_name] learned a new move!"
                            $ crab21_move4 = True
                    jump crab21_leveling_check
    if crab22_exp:
        $ crab22_total_exp += shared_arena_exp
        "[crab22_name] got [shared_arena_exp] exp!"
        if crab22_level <=98:
            jump crab22_leveling_check
            label crab22_leveling_check:
                $ crab22_exp_check = ((crab22_level*crab22_level*crab22_level)/4)
                if crab22_total_exp >= crab22_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab22_level +=1
                    "[crab22_name] reached level [crab22_level]!"
                    if crab22_rarity == "n":
                        if crab22_level >=5 and not crab22_move2:
                            "[crab22_name] learned a new move!"
                            $ crab22_move2 = True
                        if crab22_level >=10 and not crab22_move3:
                            "[crab22_name] learned a new move!"
                            $ crab22_move3 = True
                        if crab22_level >=15 and not crab22_move4:
                            "[crab22_name] learned a new move!"
                            $ crab22_move4 = True
                    if crab22_rarity == "r":
                        if crab22_level >=8 and not crab22_move2:
                            "[crab22_name] learned a new move!"
                            $ crab22_move2 = True
                        if crab22_level >=14 and not crab22_move3:
                            "[crab22_name] learned a new move!"
                            $ crab22_move3 = True
                        if crab22_level >=18 and not crab22_move4:
                            "[crab22_name] learned a new move!"
                            $ crab22_move4 = True
                    if crab22_rarity == "e":
                        if crab22_level >=12 and not crab22_move2:
                            "[crab22_name] learned a new move!"
                            $ crab22_move2 = True
                        if crab22_level >=16 and not crab22_move3:
                            "[crab22_name] learned a new move!"
                            $ crab22_move3 = True
                        if crab22_level >=22 and not crab22_move4:
                            "[crab22_name] learned a new move!"
                            $ crab22_move4 = True
                    if crab22_rarity == "l":
                        if crab22_level >=14 and not crab22_move2:
                            "[crab22_name] learned a new move!"
                            $ crab22_move2 = True
                        if crab22_level >=20 and not crab22_move3:
                            "[crab22_name] learned a new move!"
                            $ crab22_move3 = True
                        if crab22_level >=25 and not crab22_move4:
                            "[crab22_name] learned a new move!"
                            $ crab22_move4 = True
                    jump crab22_leveling_check
    if crab23_exp:
        $ crab23_total_exp += shared_arena_exp
        "[crab23_name] got [shared_arena_exp] exp!"
        if crab23_level <=98:
            jump crab23_leveling_check
            label crab23_leveling_check:
                $ crab23_exp_check = ((crab23_level*crab23_level*crab23_level)/4)
                if crab23_total_exp >= crab23_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab23_level +=1
                    "[crab23_name] reached level [crab23_level]!"
                    if crab23_rarity == "n":
                        if crab23_level >=5 and not crab23_move2:
                            "[crab23_name] learned a new move!"
                            $ crab23_move2 = True
                        if crab23_level >=10 and not crab23_move3:
                            "[crab23_name] learned a new move!"
                            $ crab23_move3 = True
                        if crab23_level >=15 and not crab23_move4:
                            "[crab23_name] learned a new move!"
                            $ crab23_move4 = True
                    if crab23_rarity == "r":
                        if crab23_level >=8 and not crab23_move2:
                            "[crab23_name] learned a new move!"
                            $ crab23_move2 = True
                        if crab23_level >=14 and not crab23_move3:
                            "[crab23_name] learned a new move!"
                            $ crab23_move3 = True
                        if crab23_level >=18 and not crab23_move4:
                            "[crab23_name] learned a new move!"
                            $ crab23_move4 = True
                    if crab23_rarity == "e":
                        if crab23_level >=12 and not crab23_move2:
                            "[crab23_name] learned a new move!"
                            $ crab23_move2 = True
                        if crab23_level >=16 and not crab23_move3:
                            "[crab23_name] learned a new move!"
                            $ crab23_move3 = True
                        if crab23_level >=22 and not crab23_move4:
                            "[crab23_name] learned a new move!"
                            $ crab23_move4 = True
                    if crab23_rarity == "l":
                        if crab23_level >=14 and not crab23_move2:
                            "[crab23_name] learned a new move!"
                            $ crab23_move2 = True
                        if crab23_level >=20 and not crab23_move3:
                            "[crab23_name] learned a new move!"
                            $ crab23_move3 = True
                        if crab23_level >=25 and not crab23_move4:
                            "[crab23_name] learned a new move!"
                            $ crab23_move4 = True
                    jump crab23_leveling_check
    if crab24_exp:
        $ crab24_total_exp += shared_arena_exp
        "[crab24_name] got [shared_arena_exp] exp!"
        if crab24_level <=98:
            jump crab24_leveling_check
            label crab24_leveling_check:
                $ crab24_exp_check = ((crab24_level*crab24_level*crab24_level)/4)
                if crab24_total_exp >= crab24_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab24_level +=1
                    "[crab24_name] reached level [crab24_level]!"
                    if crab24_rarity == "n":
                        if crab24_level >=5 and not crab24_move2:
                            "[crab24_name] learned a new move!"
                            $ crab24_move2 = True
                        if crab24_level >=10 and not crab24_move3:
                            "[crab24_name] learned a new move!"
                            $ crab24_move3 = True
                        if crab24_level >=15 and not crab24_move4:
                            "[crab24_name] learned a new move!"
                            $ crab24_move4 = True
                    if crab24_rarity == "r":
                        if crab24_level >=8 and not crab24_move2:
                            "[crab24_name] learned a new move!"
                            $ crab24_move2 = True
                        if crab24_level >=14 and not crab24_move3:
                            "[crab24_name] learned a new move!"
                            $ crab24_move3 = True
                        if crab24_level >=18 and not crab24_move4:
                            "[crab24_name] learned a new move!"
                            $ crab24_move4 = True
                    if crab24_rarity == "e":
                        if crab24_level >=12 and not crab24_move2:
                            "[crab24_name] learned a new move!"
                            $ crab24_move2 = True
                        if crab24_level >=16 and not crab24_move3:
                            "[crab24_name] learned a new move!"
                            $ crab24_move3 = True
                        if crab24_level >=22 and not crab24_move4:
                            "[crab24_name] learned a new move!"
                            $ crab24_move4 = True
                    if crab24_rarity == "l":
                        if crab24_level >=14 and not crab24_move2:
                            "[crab24_name] learned a new move!"
                            $ crab24_move2 = True
                        if crab24_level >=20 and not crab24_move3:
                            "[crab24_name] learned a new move!"
                            $ crab24_move3 = True
                        if crab24_level >=25 and not crab24_move4:
                            "[crab24_name] learned a new move!"
                            $ crab24_move4 = True
                    jump crab24_leveling_check
    if crab25_exp:
        $ crab25_total_exp += shared_arena_exp
        "[crab25_name] got [shared_arena_exp] exp!"
        if crab25_level <=98:
            jump crab25_leveling_check
            label crab25_leveling_check:
                $ crab25_exp_check = ((crab25_level*crab25_level*crab25_level)/4)
                if crab25_total_exp >= crab25_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab25_level +=1
                    "[crab25_name] reached level [crab25_level]!"
                    if crab25_rarity == "n":
                        if crab25_level >=5 and not crab25_move2:
                            "[crab25_name] learned a new move!"
                            $ crab25_move2 = True
                        if crab25_level >=10 and not crab25_move3:
                            "[crab25_name] learned a new move!"
                            $ crab25_move3 = True
                        if crab25_level >=15 and not crab25_move4:
                            "[crab25_name] learned a new move!"
                            $ crab25_move4 = True
                    if crab25_rarity == "r":
                        if crab25_level >=8 and not crab25_move2:
                            "[crab25_name] learned a new move!"
                            $ crab25_move2 = True
                        if crab25_level >=14 and not crab25_move3:
                            "[crab25_name] learned a new move!"
                            $ crab25_move3 = True
                        if crab25_level >=18 and not crab25_move4:
                            "[crab25_name] learned a new move!"
                            $ crab25_move4 = True
                    if crab25_rarity == "e":
                        if crab25_level >=12 and not crab25_move2:
                            "[crab25_name] learned a new move!"
                            $ crab25_move2 = True
                        if crab25_level >=16 and not crab25_move3:
                            "[crab25_name] learned a new move!"
                            $ crab25_move3 = True
                        if crab25_level >=22 and not crab25_move4:
                            "[crab25_name] learned a new move!"
                            $ crab25_move4 = True
                    if crab25_rarity == "l":
                        if crab25_level >=14 and not crab25_move2:
                            "[crab25_name] learned a new move!"
                            $ crab25_move2 = True
                        if crab25_level >=20 and not crab25_move3:
                            "[crab25_name] learned a new move!"
                            $ crab25_move3 = True
                        if crab25_level >=25 and not crab25_move4:
                            "[crab25_name] learned a new move!"
                            $ crab25_move4 = True
                    jump crab25_leveling_check
    if crab26_exp:
        $ crab26_total_exp += shared_arena_exp
        "[crab26_name] got [shared_arena_exp] exp!"
        if crab26_level <=98:
            jump crab26_leveling_check
            label crab26_leveling_check:
                $ crab26_exp_check = ((crab26_level*crab26_level*crab26_level)/4)
                if crab26_total_exp >= crab26_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab26_level +=1
                    "[crab26_name] reached level [crab26_level]!"
                    if crab26_rarity == "n":
                        if crab26_level >=5 and not crab26_move2:
                            "[crab26_name] learned a new move!"
                            $ crab26_move2 = True
                        if crab26_level >=10 and not crab26_move3:
                            "[crab26_name] learned a new move!"
                            $ crab26_move3 = True
                        if crab26_level >=15 and not crab26_move4:
                            "[crab26_name] learned a new move!"
                            $ crab26_move4 = True
                    if crab26_rarity == "r":
                        if crab26_level >=8 and not crab26_move2:
                            "[crab26_name] learned a new move!"
                            $ crab26_move2 = True
                        if crab26_level >=14 and not crab26_move3:
                            "[crab26_name] learned a new move!"
                            $ crab26_move3 = True
                        if crab26_level >=18 and not crab26_move4:
                            "[crab26_name] learned a new move!"
                            $ crab26_move4 = True
                    if crab26_rarity == "e":
                        if crab26_level >=12 and not crab26_move2:
                            "[crab26_name] learned a new move!"
                            $ crab26_move2 = True
                        if crab26_level >=16 and not crab26_move3:
                            "[crab26_name] learned a new move!"
                            $ crab26_move3 = True
                        if crab26_level >=22 and not crab26_move4:
                            "[crab26_name] learned a new move!"
                            $ crab26_move4 = True
                    if crab26_rarity == "l":
                        if crab26_level >=14 and not crab26_move2:
                            "[crab26_name] learned a new move!"
                            $ crab26_move2 = True
                        if crab26_level >=20 and not crab26_move3:
                            "[crab26_name] learned a new move!"
                            $ crab26_move3 = True
                        if crab26_level >=25 and not crab26_move4:
                            "[crab26_name] learned a new move!"
                            $ crab26_move4 = True
                    jump crab26_leveling_check
    if crab27_exp:
        $ crab27_total_exp += shared_arena_exp
        "[crab27_name] got [shared_arena_exp] exp!"
        if crab27_level <=98:
            jump crab27_leveling_check
            label crab27_leveling_check:
                $ crab27_exp_check = ((crab27_level*crab27_level*crab27_level)/4)
                if crab27_total_exp >= crab27_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab27_level +=1
                    "[crab27_name] reached level [crab27_level]!"
                    if crab27_rarity == "n":
                        if crab27_level >=5 and not crab27_move2:
                            "[crab27_name] learned a new move!"
                            $ crab27_move2 = True
                        if crab27_level >=10 and not crab27_move3:
                            "[crab27_name] learned a new move!"
                            $ crab27_move3 = True
                        if crab27_level >=15 and not crab27_move4:
                            "[crab27_name] learned a new move!"
                            $ crab27_move4 = True
                    if crab27_rarity == "r":
                        if crab27_level >=8 and not crab27_move2:
                            "[crab27_name] learned a new move!"
                            $ crab27_move2 = True
                        if crab27_level >=14 and not crab27_move3:
                            "[crab27_name] learned a new move!"
                            $ crab27_move3 = True
                        if crab27_level >=18 and not crab27_move4:
                            "[crab27_name] learned a new move!"
                            $ crab27_move4 = True
                    if crab27_rarity == "e":
                        if crab27_level >=12 and not crab27_move2:
                            "[crab27_name] learned a new move!"
                            $ crab27_move2 = True
                        if crab27_level >=16 and not crab27_move3:
                            "[crab27_name] learned a new move!"
                            $ crab27_move3 = True
                        if crab27_level >=22 and not crab27_move4:
                            "[crab27_name] learned a new move!"
                            $ crab27_move4 = True
                    if crab27_rarity == "l":
                        if crab27_level >=14 and not crab27_move2:
                            "[crab27_name] learned a new move!"
                            $ crab27_move2 = True
                        if crab27_level >=20 and not crab27_move3:
                            "[crab27_name] learned a new move!"
                            $ crab27_move3 = True
                        if crab27_level >=25 and not crab27_move4:
                            "[crab27_name] learned a new move!"
                            $ crab27_move4 = True
                    jump crab27_leveling_check
    if crab28_exp:
        $ crab28_total_exp += shared_arena_exp
        "[crab28_name] got [shared_arena_exp] exp!"
        if crab28_level <=98:
            jump crab28_leveling_check
            label crab28_leveling_check:
                $ crab28_exp_check = ((crab28_level*crab28_level*crab28_level)/4)
                if crab28_total_exp >= crab28_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab28_level +=1
                    "[crab28_name] reached level [crab28_level]!"
                    if crab28_rarity == "n":
                        if crab28_level >=5 and not crab28_move2:
                            "[crab28_name] learned a new move!"
                            $ crab28_move2 = True
                        if crab28_level >=10 and not crab28_move3:
                            "[crab28_name] learned a new move!"
                            $ crab28_move3 = True
                        if crab28_level >=15 and not crab28_move4:
                            "[crab28_name] learned a new move!"
                            $ crab28_move4 = True
                    if crab28_rarity == "r":
                        if crab28_level >=8 and not crab28_move2:
                            "[crab28_name] learned a new move!"
                            $ crab28_move2 = True
                        if crab28_level >=14 and not crab28_move3:
                            "[crab28_name] learned a new move!"
                            $ crab28_move3 = True
                        if crab28_level >=18 and not crab28_move4:
                            "[crab28_name] learned a new move!"
                            $ crab28_move4 = True
                    if crab28_rarity == "e":
                        if crab28_level >=12 and not crab28_move2:
                            "[crab28_name] learned a new move!"
                            $ crab28_move2 = True
                        if crab28_level >=16 and not crab28_move3:
                            "[crab28_name] learned a new move!"
                            $ crab28_move3 = True
                        if crab28_level >=22 and not crab28_move4:
                            "[crab28_name] learned a new move!"
                            $ crab28_move4 = True
                    if crab28_rarity == "l":
                        if crab28_level >=14 and not crab28_move2:
                            "[crab28_name] learned a new move!"
                            $ crab28_move2 = True
                        if crab28_level >=20 and not crab28_move3:
                            "[crab28_name] learned a new move!"
                            $ crab28_move3 = True
                        if crab28_level >=25 and not crab28_move4:
                            "[crab28_name] learned a new move!"
                            $ crab28_move4 = True
                    jump crab28_leveling_check
    if crab29_exp:
        $ crab29_total_exp += shared_arena_exp
        "[crab29_name] got [shared_arena_exp] exp!"
        if crab29_level <=98:
            jump crab29_leveling_check
            label crab29_leveling_check:
                $ crab29_exp_check = ((crab29_level*crab29_level*crab29_level)/4)
                if crab29_total_exp >= crab29_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab29_level +=1
                    "[crab29_name] reached level [crab29_level]!"
                    if crab29_rarity == "n":
                        if crab29_level >=5 and not crab29_move2:
                            "[crab29_name] learned a new move!"
                            $ crab29_move2 = True
                        if crab29_level >=10 and not crab29_move3:
                            "[crab29_name] learned a new move!"
                            $ crab29_move3 = True
                        if crab29_level >=15 and not crab29_move4:
                            "[crab29_name] learned a new move!"
                            $ crab29_move4 = True
                    if crab29_rarity == "r":
                        if crab29_level >=8 and not crab29_move2:
                            "[crab29_name] learned a new move!"
                            $ crab29_move2 = True
                        if crab29_level >=14 and not crab29_move3:
                            "[crab29_name] learned a new move!"
                            $ crab29_move3 = True
                        if crab29_level >=18 and not crab29_move4:
                            "[crab29_name] learned a new move!"
                            $ crab29_move4 = True
                    if crab29_rarity == "e":
                        if crab29_level >=12 and not crab29_move2:
                            "[crab29_name] learned a new move!"
                            $ crab29_move2 = True
                        if crab29_level >=16 and not crab29_move3:
                            "[crab29_name] learned a new move!"
                            $ crab29_move3 = True
                        if crab29_level >=22 and not crab29_move4:
                            "[crab29_name] learned a new move!"
                            $ crab29_move4 = True
                    if crab29_rarity == "l":
                        if crab29_level >=14 and not crab29_move2:
                            "[crab29_name] learned a new move!"
                            $ crab29_move2 = True
                        if crab29_level >=20 and not crab29_move3:
                            "[crab29_name] learned a new move!"
                            $ crab29_move3 = True
                        if crab29_level >=25 and not crab29_move4:
                            "[crab29_name] learned a new move!"
                            $ crab29_move4 = True
                    jump crab29_leveling_check
    if crab30_exp:
        $ crab30_total_exp += shared_arena_exp
        "[crab30_name] got [shared_arena_exp] exp!"
        if crab30_level <=98:
            jump crab30_leveling_check
            label crab30_leveling_check:
                $ crab30_exp_check = ((crab30_level*crab30_level*crab30_level)/4)
                if crab30_total_exp >= crab30_exp_check:
                    play sound "audio/win2.mp3"
                    $ crab30_level +=1
                    "[crab30_name] reached level [crab30_level]!"
                    if crab30_rarity == "n":
                        if crab30_level >=5 and not crab30_move2:
                            "[crab30_name] learned a new move!"
                            $ crab30_move2 = True
                        if crab30_level >=10 and not crab30_move3:
                            "[crab30_name] learned a new move!"
                            $ crab30_move3 = True
                        if crab30_level >=15 and not crab30_move4:
                            "[crab30_name] learned a new move!"
                            $ crab30_move4 = True
                    if crab30_rarity == "r":
                        if crab30_level >=8 and not crab30_move2:
                            "[crab30_name] learned a new move!"
                            $ crab30_move2 = True
                        if crab30_level >=14 and not crab30_move3:
                            "[crab30_name] learned a new move!"
                            $ crab30_move3 = True
                        if crab30_level >=18 and not crab30_move4:
                            "[crab30_name] learned a new move!"
                            $ crab30_move4 = True
                    if crab30_rarity == "e":
                        if crab30_level >=12 and not crab30_move2:
                            "[crab30_name] learned a new move!"
                            $ crab30_move2 = True
                        if crab30_level >=16 and not crab30_move3:
                            "[crab30_name] learned a new move!"
                            $ crab30_move3 = True
                        if crab30_level >=22 and not crab30_move4:
                            "[crab30_name] learned a new move!"
                            $ crab30_move4 = True
                    if crab30_rarity == "l":
                        if crab30_level >=14 and not crab30_move2:
                            "[crab30_name] learned a new move!"
                            $ crab30_move2 = True
                        if crab30_level >=20 and not crab30_move3:
                            "[crab30_name] learned a new move!"
                            $ crab30_move3 = True
                        if crab30_level >=25 and not crab30_move4:
                            "[crab30_name] learned a new move!"
                            $ crab30_move4 = True
                    jump crab30_leveling_check

    $ total_arena_exp = 0
    $ crabs_getting_exp = 1

    $ crab1_exp = False
    $ crab2_exp = False
    $ crab3_exp = False
    $ crab4_exp = False
    $ crab5_exp = False
    $ crab6_exp = False
    $ crab7_exp = False
    $ crab8_exp = False
    $ crab9_exp = False
    $ crab10_exp = False
    $ crab11_exp = False
    $ crab12_exp = False
    $ crab13_exp = False
    $ crab14_exp = False
    $ crab15_exp = False
    $ crab16_exp = False
    $ crab17_exp = False
    $ crab18_exp = False
    $ crab19_exp = False
    $ crab20_exp = False
    $ crab21_exp = False
    $ crab22_exp = False
    $ crab23_exp = False
    $ crab24_exp = False
    $ crab25_exp = False
    $ crab26_exp = False
    $ crab27_exp = False
    $ crab28_exp = False
    $ crab29_exp = False
    $ crab30_exp = False

    jump after_arena_end_level_check

label after_level_check:


    hide enemy_crab_shuffle
    hide crab1_shuffle
    hide crab2_shuffle
    hide crab3_shuffle
    hide crab4_shuffle
    hide crab5_shuffle
    hide crab6_shuffle
    hide crab7_shuffle
    hide crab8_shuffle
    hide crab9_shuffle
    hide crab10_shuffle
    hide crab11_shuffle
    hide crab12_shuffle
    hide crab13_shuffle
    hide crab14_shuffle
    hide crab15_shuffle
    hide crab1_shuffle
    hide crab17_shuffle
    hide crab18_shuffle
    hide crab19_shuffle
    hide crab20_shuffle
    hide crab21_shuffle
    hide crab22_shuffle
    hide crab23_shuffle
    hide crab24_shuffle
    hide crab25_shuffle
    hide crab26_shuffle
    hide crab27_shuffle
    hide crab28_shuffle
    hide crab29_shuffle
    hide crab30_shuffle
    hide screen bk3_crabstats1
    show black
    with dissolve
    "well done!"
    "let's just heal those crabs..."
    ".................."
    "done!"
    $ enemy_crab1_type = "0"
    $ enemy_crab2_type = "0"
    $ enemy_crab3_type = "0"
    $ enemy_crab4_type = "0"
    $ enemy_crab5_type = "0"
    $ ultimate_arena_battle = False
    $ anka_arena_battle = False
    $ a_weakened = False
    $ a_confused = False
    hide black
    if crab_hunt or crab_hunt2:
        $ crab_hunt = False
        $ crab_hunt2 = False
        jump begin_stuff
    else:
        if iroh_fun_battle:
            $ iroh_fun_battle = False
            if bk3_loveroute:
                jump love_bk3_jasmine
            else:
                jump bk3_jasmine
        else:
            jump begin_stuff

label arena_game_over:
    jump arena_end_level_check
















label enter_arena:
    $ crab_hunt = True
    $ crab_hunt2 = False
    while 1:
        call screen tiny_dude1_cage


        if xloc == -5 and yloc == 3:
            show thankful_girl with dissolve
            "Girl" "hey. um."
            "girl" "i thought i'd give this a try but i've only caught one so far."
            "girl" "we can battle if you want..."
            menu:
                "battle the girl?"
                "check out her crabs":
                    hide thankful_girl with dissolve
                    jump ultimate_crab_battle
                "i don't need yo crabs girl":
                    "girl" "oh. okay. i'll keep looking for more crabs."
                    "girl" "maybe then I can be competitive."
                    hide thankful_girl with dissolve
                    pass

        if xloc == -9 and yloc ==0:
            $ tiny_dude1_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)
            $ xloc = 0
            $ yloc = 0
            jump enter_arena2
        if xloc == -9 and yloc ==1:
            $ tiny_dude1_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)
            $ xloc = 0
            $ yloc = 0
            jump enter_arena2
        if xloc == 2 and yloc ==-4:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 3 and yloc ==-4:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 4 and yloc ==-4:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 3 and yloc ==1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 2 and yloc ==1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 1 and yloc ==1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 1 and yloc ==2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 2 and yloc ==2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 3 and yloc ==2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -3 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -4 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -3 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -5 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -4 and yloc ==-2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -3 and yloc ==-2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu

            call screen tiny_dude1_cage


label enter_arena2:
    $ crab_hunt = False
    $ crab_hunt2 = True
    while 1:
        call screen tiny_dude1_cage2


        if xloc == -5 and yloc == 3:
            show an_idle_02 with dissolve
            anka "ready to do this?"
            if not bk3_anka:
                y "you look familiar... have i seen you before?"
                anka "i don't think so...."
                anka "oh, you're that shorty avatar."
                anka "guess you made it from the village fine."
                anka "i'm anka, if you don't remember."
                y "the village.... oh shit, you were a carpenter or something, right?"
                anka "yup. bored with the selection in the village, came up this way."
                y "the... selection?"
                anka "of girls."
                anka "are we doing this or not?"
                $ bk3_anka = True

            menu:
                "battle anka?"
                "battle":
                    hide an_idle_02 with dissolve
                    jump anka_crab_battle
                "nevermind":
                    anka "fine."
                    hide an_idle_02 with dissolve
                    pass

        if xloc == 9 and yloc ==0:
            $ tiny_dude1_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)
            $ xloc = 0
            $ yloc = 0
            jump enter_arena
        if xloc == 9 and yloc ==1:
            $ tiny_dude1_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)
            $ xloc = 0
            $ yloc = 0
            jump enter_arena

        if xloc == 2 and yloc ==-4:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 3 and yloc ==-4:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 4 and yloc ==-4:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 3 and yloc ==1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 2 and yloc ==1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 1 and yloc ==1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 1 and yloc ==2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 2 and yloc ==2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == 3 and yloc ==2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -3 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -4 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -3 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -5 and yloc ==-1:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -4 and yloc ==-2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu
        if xloc == -3 and yloc ==-2:
            $ rand_encounter_chance = renpy.random.randint(1, 5)
            if rand_encounter_chance ==5:
                with pixellate
                jump crab_battle_menu

            call screen tiny_dude1_cage2

label ultimate_crab_battle:
    $ ultimate_arena_battle = True
    jump crab_battle_menu

label anka_crab_battle:
    $ anka_arena_battle = True
    jump crab_battle_menu

label wild_crab_catch:
    hide enemy_crab_shuffle
    hide crab1_shuffle
    hide crab2_shuffle
    hide crab3_shuffle
    hide crab4_shuffle
    hide crab5_shuffle
    hide crab6_shuffle
    hide crab7_shuffle
    hide crab8_shuffle
    hide crab9_shuffle
    hide crab10_shuffle
    hide crab11_shuffle
    hide crab12_shuffle
    hide crab13_shuffle
    hide crab14_shuffle
    hide crab15_shuffle
    hide crab1_shuffle
    hide crab17_shuffle
    hide crab18_shuffle
    hide crab19_shuffle
    hide crab20_shuffle
    hide crab21_shuffle
    hide crab22_shuffle
    hide crab23_shuffle
    hide crab24_shuffle
    hide crab25_shuffle
    hide crab26_shuffle
    hide crab27_shuffle
    hide crab28_shuffle
    hide crab29_shuffle
    hide crab30_shuffle
    hide screen bk3_crabstats1

    if not crab2:
        $ crab2 = True
        $ crab2_type = enemy_crab_type
        $ crab2_rarity = enemy_crab_rarity
        $ crab2_level = enemy_crab1_level
        if crab2_type == "1":
            $ rand_crab2_type = 1
        if crab2_type == "2":
            $ rand_crab2_type = 2
        if crab2_type == "3":
            $ rand_crab2_type = 3
        if crab2_type == "4":
            $ rand_crab2_type = 4
        if crab2_type == "5":
            $ rand_crab2_type = 5
        if crab2_type == "6":
            $ rand_crab2_type = 6
        if crab2_type == "7":
            $ rand_crab2_type = 7
        if crab2_type == "8":
            $ rand_crab2_type = 8
        if crab2_type == "9":
            $ rand_crab2_type = 9
        if crab2_type == "10":
            $ rand_crab2_type = 10
        if crab2_type == "11":
            $ rand_crab2_type = 11
        jump crab2_trap_get

    if not crab3:
        $ crab3 = True
        $ crab3_type = enemy_crab_type
        $ crab3_rarity = enemy_crab_rarity
        $ crab3_level = enemy_crab1_level
        if crab3_type == "1":
            $ rand_crab3_type = 1
        if crab3_type == "2":
            $ rand_crab3_type = 2
        if crab3_type == "3":
            $ rand_crab3_type = 3
        if crab3_type == "4":
            $ rand_crab3_type = 4
        if crab3_type == "5":
            $ rand_crab3_type = 5
        if crab3_type == "6":
            $ rand_crab3_type = 6
        if crab3_type == "7":
            $ rand_crab3_type = 7
        if crab3_type == "8":
            $ rand_crab3_type = 8
        if crab3_type == "9":
            $ rand_crab3_type = 9
        if crab3_type == "10":
            $ rand_crab3_type = 10
        if crab3_type == "11":
            $ rand_crab3_type = 11
        jump crab3_trap_get

    if not crab4:
        $ crab4 = True
        $ crab4_type = enemy_crab_type
        $ crab4_rarity = enemy_crab_rarity
        $ crab4_level = enemy_crab1_level
        if crab4_type == "1":
            $ rand_crab4_type = 1
        if crab4_type == "2":
            $ rand_crab4_type = 2
        if crab4_type == "3":
            $ rand_crab4_type = 3
        if crab4_type == "4":
            $ rand_crab4_type = 4
        if crab4_type == "5":
            $ rand_crab4_type = 5
        if crab4_type == "6":
            $ rand_crab4_type = 6
        if crab4_type == "7":
            $ rand_crab4_type = 7
        if crab4_type == "8":
            $ rand_crab4_type = 8
        if crab4_type == "9":
            $ rand_crab4_type = 9
        if crab4_type == "10":
            $ rand_crab4_type = 10
        if crab4_type == "11":
            $ rand_crab4_type = 11
        jump crab4_trap_get

    if not crab5:
        $ crab5 = True
        $ crab5_type = enemy_crab_type
        $ crab5_rarity = enemy_crab_rarity
        $ crab5_level = enemy_crab1_level
        if crab5_type == "1":
            $ rand_crab5_type = 1
        if crab5_type == "2":
            $ rand_crab5_type = 2
        if crab5_type == "3":
            $ rand_crab5_type = 3
        if crab5_type == "4":
            $ rand_crab5_type = 4
        if crab5_type == "5":
            $ rand_crab5_type = 5
        if crab5_type == "6":
            $ rand_crab5_type = 6
        if crab5_type == "7":
            $ rand_crab5_type = 7
        if crab5_type == "8":
            $ rand_crab5_type = 8
        if crab5_type == "9":
            $ rand_crab5_type = 9
        if crab5_type == "10":
            $ rand_crab5_type = 10
        if crab5_type == "11":
            $ rand_crab5_type = 11
        jump crab5_trap_get

    if not crab6:
        $ crab6 = True
        $ crab6_type = enemy_crab_type
        $ crab6_rarity = enemy_crab_rarity
        $ crab6_level = enemy_crab1_level
        if crab6_type == "1":
            $ rand_crab6_type = 1
        if crab6_type == "2":
            $ rand_crab6_type = 2
        if crab6_type == "3":
            $ rand_crab6_type = 3
        if crab6_type == "4":
            $ rand_crab6_type = 4
        if crab6_type == "5":
            $ rand_crab6_type = 5
        if crab6_type == "6":
            $ rand_crab6_type = 6
        if crab6_type == "7":
            $ rand_crab6_type = 7
        if crab6_type == "8":
            $ rand_crab6_type = 8
        if crab6_type == "9":
            $ rand_crab6_type = 9
        if crab6_type == "10":
            $ rand_crab6_type = 10
        if crab6_type == "11":
            $ rand_crab6_type = 11
        jump crab6_trap_get

    if not crab7:
        $ crab7 = True
        $ crab7_type = enemy_crab_type
        $ crab7_rarity = enemy_crab_rarity
        $ crab7_level = enemy_crab1_level
        if crab7_type == "1":
            $ rand_crab7_type = 1
        if crab7_type == "2":
            $ rand_crab7_type = 2
        if crab7_type == "3":
            $ rand_crab7_type = 3
        if crab7_type == "4":
            $ rand_crab7_type = 4
        if crab7_type == "5":
            $ rand_crab7_type = 5
        if crab7_type == "6":
            $ rand_crab7_type = 6
        if crab7_type == "7":
            $ rand_crab7_type = 7
        if crab7_type == "8":
            $ rand_crab7_type = 8
        if crab7_type == "9":
            $ rand_crab7_type = 9
        if crab7_type == "10":
            $ rand_crab7_type = 10
        if crab7_type == "11":
            $ rand_crab7_type = 11
        jump crab7_trap_get

    if not crab8:
        $ crab8 = True
        $ crab8_type = enemy_crab_type
        $ crab8_rarity = enemy_crab_rarity
        $ crab8_level = enemy_crab1_level
        if crab8_type == "1":
            $ rand_crab8_type = 1
        if crab8_type == "2":
            $ rand_crab8_type = 2
        if crab8_type == "3":
            $ rand_crab8_type = 3
        if crab8_type == "4":
            $ rand_crab8_type = 4
        if crab8_type == "5":
            $ rand_crab8_type = 5
        if crab8_type == "6":
            $ rand_crab8_type = 6
        if crab8_type == "7":
            $ rand_crab8_type = 7
        if crab8_type == "8":
            $ rand_crab8_type = 8
        if crab8_type == "9":
            $ rand_crab8_type = 9
        if crab8_type == "10":
            $ rand_crab8_type = 10
        if crab8_type == "11":
            $ rand_crab8_type = 11
        jump crab8_trap_get

    if not crab9:
        $ crab9 = True
        $ crab9_type = enemy_crab_type
        $ crab9_rarity = enemy_crab_rarity
        $ crab9_level = enemy_crab1_level
        if crab9_type == "1":
            $ rand_crab9_type = 1
        if crab9_type == "2":
            $ rand_crab9_type = 2
        if crab9_type == "3":
            $ rand_crab9_type = 3
        if crab9_type == "4":
            $ rand_crab9_type = 4
        if crab9_type == "5":
            $ rand_crab9_type = 5
        if crab9_type == "6":
            $ rand_crab9_type = 6
        if crab9_type == "7":
            $ rand_crab9_type = 7
        if crab9_type == "8":
            $ rand_crab9_type = 8
        if crab9_type == "9":
            $ rand_crab9_type = 9
        if crab9_type == "10":
            $ rand_crab9_type = 10
        if crab9_type == "11":
            $ rand_crab9_type = 11
        jump crab9_trap_get

    if not crab10:
        $ crab10 = True
        $ crab10_type = enemy_crab_type
        $ crab10_rarity = enemy_crab_rarity
        $ crab10_level = enemy_crab1_level
        if crab10_type == "1":
            $ rand_crab10_type = 1
        if crab10_type == "2":
            $ rand_crab10_type = 2
        if crab10_type == "3":
            $ rand_crab10_type = 3
        if crab10_type == "4":
            $ rand_crab10_type = 4
        if crab10_type == "5":
            $ rand_crab10_type = 5
        if crab10_type == "6":
            $ rand_crab10_type = 6
        if crab10_type == "7":
            $ rand_crab10_type = 7
        if crab10_type == "8":
            $ rand_crab10_type = 8
        if crab10_type == "9":
            $ rand_crab10_type = 9
        if crab10_type == "10":
            $ rand_crab10_type = 10
        if crab10_type == "11":
            $ rand_crab10_type = 11
        jump crab10_trap_get

    if not crab11:
        $ crab11 = True
        $ crab11_type = enemy_crab_type
        $ crab11_rarity = enemy_crab_rarity
        $ crab11_level = enemy_crab1_level
        if crab11_type == "1":
            $ rand_crab11_type = 1
        if crab11_type == "2":
            $ rand_crab11_type = 2
        if crab11_type == "3":
            $ rand_crab11_type = 3
        if crab11_type == "4":
            $ rand_crab11_type = 4
        if crab11_type == "5":
            $ rand_crab11_type = 5
        if crab11_type == "6":
            $ rand_crab11_type = 6
        if crab11_type == "7":
            $ rand_crab11_type = 7
        if crab11_type == "8":
            $ rand_crab11_type = 8
        if crab11_type == "9":
            $ rand_crab11_type = 9
        if crab11_type == "10":
            $ rand_crab11_type = 10
        if crab11_type == "11":
            $ rand_crab11_type = 11
        jump crab11_trap_get

    if not crab12:
        $ crab12 = True
        $ crab12_type = enemy_crab_type
        $ crab12_rarity = enemy_crab_rarity
        $ crab12_level = enemy_crab1_level
        if crab12_type == "1":
            $ rand_crab12_type = 1
        if crab12_type == "2":
            $ rand_crab12_type = 2
        if crab12_type == "3":
            $ rand_crab12_type = 3
        if crab12_type == "4":
            $ rand_crab12_type = 4
        if crab12_type == "5":
            $ rand_crab12_type = 5
        if crab12_type == "6":
            $ rand_crab12_type = 6
        if crab12_type == "7":
            $ rand_crab12_type = 7
        if crab12_type == "8":
            $ rand_crab12_type = 8
        if crab12_type == "9":
            $ rand_crab12_type = 9
        if crab12_type == "10":
            $ rand_crab12_type = 10
        if crab12_type == "11":
            $ rand_crab12_type = 11
        jump crab12_trap_get

    if not crab13:
        $ crab13 = True
        $ crab13_type = enemy_crab_type
        $ crab13_rarity = enemy_crab_rarity
        $ crab13_level = enemy_crab1_level
        if crab13_type == "1":
            $ rand_crab13_type = 1
        if crab13_type == "2":
            $ rand_crab13_type = 2
        if crab13_type == "3":
            $ rand_crab13_type = 3
        if crab13_type == "4":
            $ rand_crab13_type = 4
        if crab13_type == "5":
            $ rand_crab13_type = 5
        if crab13_type == "6":
            $ rand_crab13_type = 6
        if crab13_type == "7":
            $ rand_crab13_type = 7
        if crab13_type == "8":
            $ rand_crab13_type = 8
        if crab13_type == "9":
            $ rand_crab13_type = 9
        if crab13_type == "10":
            $ rand_crab13_type = 10
        if crab13_type == "11":
            $ rand_crab13_type = 11
        jump crab13_trap_get

    if not crab14:
        $ crab14 = True
        $ crab14_type = enemy_crab_type
        $ crab14_rarity = enemy_crab_rarity
        $ crab14_level = enemy_crab1_level
        if crab14_type == "1":
            $ rand_crab14_type = 1
        if crab14_type == "2":
            $ rand_crab14_type = 2
        if crab14_type == "3":
            $ rand_crab14_type = 3
        if crab14_type == "4":
            $ rand_crab14_type = 4
        if crab14_type == "5":
            $ rand_crab14_type = 5
        if crab14_type == "6":
            $ rand_crab14_type = 6
        if crab14_type == "7":
            $ rand_crab14_type = 7
        if crab14_type == "8":
            $ rand_crab14_type = 8
        if crab14_type == "9":
            $ rand_crab14_type = 9
        if crab14_type == "10":
            $ rand_crab14_type = 10
        if crab14_type == "11":
            $ rand_crab14_type = 11
        jump crab14_trap_get

    if not crab15:
        $ crab15 = True
        $ crab15_type = enemy_crab_type
        $ crab15_rarity = enemy_crab_rarity
        $ crab15_level = enemy_crab1_level
        if crab15_type == "1":
            $ rand_crab15_type = 1
        if crab15_type == "2":
            $ rand_crab15_type = 2
        if crab15_type == "3":
            $ rand_crab15_type = 3
        if crab15_type == "4":
            $ rand_crab15_type = 4
        if crab15_type == "5":
            $ rand_crab15_type = 5
        if crab15_type == "6":
            $ rand_crab15_type = 6
        if crab15_type == "7":
            $ rand_crab15_type = 7
        if crab15_type == "8":
            $ rand_crab15_type = 8
        if crab15_type == "9":
            $ rand_crab15_type = 9
        if crab15_type == "10":
            $ rand_crab15_type = 10
        if crab15_type == "11":
            $ rand_crab15_type = 11
        jump crab15_trap_get

    if not crab16:
        $ crab16 = True
        $ crab16_type = enemy_crab_type
        $ crab16_rarity = enemy_crab_rarity
        $ crab16_level = enemy_crab1_level
        if crab16_type == "1":
            $ rand_crab16_type = 1
        if crab16_type == "2":
            $ rand_crab16_type = 2
        if crab16_type == "3":
            $ rand_crab16_type = 3
        if crab16_type == "4":
            $ rand_crab16_type = 4
        if crab16_type == "5":
            $ rand_crab16_type = 5
        if crab16_type == "6":
            $ rand_crab16_type = 6
        if crab16_type == "7":
            $ rand_crab16_type = 7
        if crab16_type == "8":
            $ rand_crab16_type = 8
        if crab16_type == "9":
            $ rand_crab16_type = 9
        if crab16_type == "10":
            $ rand_crab16_type = 10
        if crab16_type == "11":
            $ rand_crab16_type = 11
        jump crab16_trap_get

    if not crab17:
        $ crab17 = True
        $ crab17_type = enemy_crab_type
        $ crab17_rarity = enemy_crab_rarity
        $ crab17_level = enemy_crab1_level
        if crab17_type == "1":
            $ rand_crab17_type = 1
        if crab17_type == "2":
            $ rand_crab17_type = 2
        if crab17_type == "3":
            $ rand_crab17_type = 3
        if crab17_type == "4":
            $ rand_crab17_type = 4
        if crab17_type == "5":
            $ rand_crab17_type = 5
        if crab17_type == "6":
            $ rand_crab17_type = 6
        if crab17_type == "7":
            $ rand_crab17_type = 7
        if crab17_type == "8":
            $ rand_crab17_type = 8
        if crab17_type == "9":
            $ rand_crab17_type = 9
        if crab17_type == "10":
            $ rand_crab17_type = 10
        if crab17_type == "11":
            $ rand_crab17_type = 11
        jump crab17_trap_get

    if not crab18:
        $ crab18 = True
        $ crab18_type = enemy_crab_type
        $ crab18_rarity = enemy_crab_rarity
        $ crab18_level = enemy_crab1_level
        if crab18_type == "1":
            $ rand_crab18_type = 1
        if crab18_type == "2":
            $ rand_crab18_type = 2
        if crab18_type == "3":
            $ rand_crab18_type = 3
        if crab18_type == "4":
            $ rand_crab18_type = 4
        if crab18_type == "5":
            $ rand_crab18_type = 5
        if crab18_type == "6":
            $ rand_crab18_type = 6
        if crab18_type == "7":
            $ rand_crab18_type = 7
        if crab18_type == "8":
            $ rand_crab18_type = 8
        if crab18_type == "9":
            $ rand_crab18_type = 9
        if crab18_type == "10":
            $ rand_crab18_type = 10
        if crab18_type == "11":
            $ rand_crab18_type = 11
        jump crab18_trap_get

    if not crab19:
        $ crab19 = True
        $ crab19_type = enemy_crab_type
        $ crab19_rarity = enemy_crab_rarity
        $ crab19_level = enemy_crab1_level
        if crab19_type == "1":
            $ rand_crab19_type = 1
        if crab19_type == "2":
            $ rand_crab19_type = 2
        if crab19_type == "3":
            $ rand_crab19_type = 3
        if crab19_type == "4":
            $ rand_crab19_type = 4
        if crab19_type == "5":
            $ rand_crab19_type = 5
        if crab19_type == "6":
            $ rand_crab19_type = 6
        if crab19_type == "7":
            $ rand_crab19_type = 7
        if crab19_type == "8":
            $ rand_crab19_type = 8
        if crab19_type == "9":
            $ rand_crab19_type = 9
        if crab19_type == "10":
            $ rand_crab19_type = 10
        if crab19_type == "11":
            $ rand_crab19_type = 11
        jump crab19_trap_get

    if not crab20:
        $ crab20 = True
        $ crab20_type = enemy_crab_type
        $ crab20_rarity = enemy_crab_rarity
        $ crab20_level = enemy_crab1_level
        if crab20_type == "1":
            $ rand_crab20_type = 1
        if crab20_type == "2":
            $ rand_crab20_type = 2
        if crab20_type == "3":
            $ rand_crab20_type = 3
        if crab20_type == "4":
            $ rand_crab20_type = 4
        if crab20_type == "5":
            $ rand_crab20_type = 5
        if crab20_type == "6":
            $ rand_crab20_type = 6
        if crab20_type == "7":
            $ rand_crab20_type = 7
        if crab20_type == "8":
            $ rand_crab20_type = 8
        if crab20_type == "9":
            $ rand_crab20_type = 9
        if crab20_type == "10":
            $ rand_crab20_type = 10
        if crab20_type == "11":
            $ rand_crab20_type = 11
        jump crab20_trap_get

    if not crab21:
        $ crab21 = True
        $ crab21_type = enemy_crab_type
        $ crab21_rarity = enemy_crab_rarity
        $ crab21_level = enemy_crab1_level
        if crab21_type == "1":
            $ rand_crab21_type = 1
        if crab21_type == "2":
            $ rand_crab21_type = 2
        if crab21_type == "3":
            $ rand_crab21_type = 3
        if crab21_type == "4":
            $ rand_crab21_type = 4
        if crab21_type == "5":
            $ rand_crab21_type = 5
        if crab21_type == "6":
            $ rand_crab21_type = 6
        if crab21_type == "7":
            $ rand_crab21_type = 7
        if crab21_type == "8":
            $ rand_crab21_type = 8
        if crab21_type == "9":
            $ rand_crab21_type = 9
        if crab21_type == "10":
            $ rand_crab21_type = 10
        if crab21_type == "11":
            $ rand_crab21_type = 11
        jump crab21_trap_get

    if not crab22:
        $ crab22 = True
        $ crab22_type = enemy_crab_type
        $ crab22_rarity = enemy_crab_rarity
        $ crab22_level = enemy_crab1_level
        if crab22_type == "1":
            $ rand_crab22_type = 1
        if crab22_type == "2":
            $ rand_crab22_type = 2
        if crab22_type == "3":
            $ rand_crab22_type = 3
        if crab22_type == "4":
            $ rand_crab22_type = 4
        if crab22_type == "5":
            $ rand_crab22_type = 5
        if crab22_type == "6":
            $ rand_crab22_type = 6
        if crab22_type == "7":
            $ rand_crab22_type = 7
        if crab22_type == "8":
            $ rand_crab22_type = 8
        if crab22_type == "9":
            $ rand_crab22_type = 9
        if crab22_type == "10":
            $ rand_crab22_type = 10
        if crab22_type == "11":
            $ rand_crab22_type = 11
        jump crab22_trap_get

    if not crab23:
        $ crab23 = True
        $ crab23_type = enemy_crab_type
        $ crab23_rarity = enemy_crab_rarity
        $ crab23_level = enemy_crab1_level
        if crab23_type == "1":
            $ rand_crab23_type = 1
        if crab23_type == "2":
            $ rand_crab23_type = 2
        if crab23_type == "3":
            $ rand_crab23_type = 3
        if crab23_type == "4":
            $ rand_crab23_type = 4
        if crab23_type == "5":
            $ rand_crab23_type = 5
        if crab23_type == "6":
            $ rand_crab23_type = 6
        if crab23_type == "7":
            $ rand_crab23_type = 7
        if crab23_type == "8":
            $ rand_crab23_type = 8
        if crab23_type == "9":
            $ rand_crab23_type = 9
        if crab23_type == "10":
            $ rand_crab23_type = 10
        if crab23_type == "11":
            $ rand_crab23_type = 11
        jump crab23_trap_get

    if not crab24:
        $ crab24 = True
        $ crab24_type = enemy_crab_type
        $ crab24_rarity = enemy_crab_rarity
        $ crab24_level = enemy_crab1_level
        if crab24_type == "1":
            $ rand_crab24_type = 1
        if crab24_type == "2":
            $ rand_crab24_type = 2
        if crab24_type == "3":
            $ rand_crab24_type = 3
        if crab24_type == "4":
            $ rand_crab24_type = 4
        if crab24_type == "5":
            $ rand_crab24_type = 5
        if crab24_type == "6":
            $ rand_crab24_type = 6
        if crab24_type == "7":
            $ rand_crab24_type = 7
        if crab24_type == "8":
            $ rand_crab24_type = 8
        if crab24_type == "9":
            $ rand_crab24_type = 9
        if crab24_type == "10":
            $ rand_crab24_type = 10
        if crab24_type == "11":
            $ rand_crab24_type = 11
        jump crab24_trap_get

    if not crab25:
        $ crab25 = True
        $ crab25_type = enemy_crab_type
        $ crab25_rarity = enemy_crab_rarity
        $ crab25_level = enemy_crab1_level
        if crab25_type == "1":
            $ rand_crab25_type = 1
        if crab25_type == "2":
            $ rand_crab25_type = 2
        if crab25_type == "3":
            $ rand_crab25_type = 3
        if crab25_type == "4":
            $ rand_crab25_type = 4
        if crab25_type == "5":
            $ rand_crab25_type = 5
        if crab25_type == "6":
            $ rand_crab25_type = 6
        if crab25_type == "7":
            $ rand_crab25_type = 7
        if crab25_type == "8":
            $ rand_crab25_type = 8
        if crab25_type == "9":
            $ rand_crab25_type = 9
        if crab25_type == "10":
            $ rand_crab25_type = 10
        if crab25_type == "11":
            $ rand_crab25_type = 11
        jump crab25_trap_get

    if not crab26:
        $ crab26 = True
        $ crab26_type = enemy_crab_type
        $ crab26_rarity = enemy_crab_rarity
        $ crab26_level = enemy_crab1_level
        if crab26_type == "1":
            $ rand_crab26_type = 1
        if crab26_type == "2":
            $ rand_crab26_type = 2
        if crab26_type == "3":
            $ rand_crab26_type = 3
        if crab26_type == "4":
            $ rand_crab26_type = 4
        if crab26_type == "5":
            $ rand_crab26_type = 5
        if crab26_type == "6":
            $ rand_crab26_type = 6
        if crab26_type == "7":
            $ rand_crab26_type = 7
        if crab26_type == "8":
            $ rand_crab26_type = 8
        if crab26_type == "9":
            $ rand_crab26_type = 9
        if crab26_type == "10":
            $ rand_crab26_type = 10
        if crab26_type == "11":
            $ rand_crab26_type = 11
        jump crab26_trap_get

    if not crab27:
        $ crab27 = True
        $ crab27_type = enemy_crab_type
        $ crab27_rarity = enemy_crab_rarity
        $ crab27_level = enemy_crab1_level
        if crab27_type == "1":
            $ rand_crab27_type = 1
        if crab27_type == "2":
            $ rand_crab27_type = 2
        if crab27_type == "3":
            $ rand_crab27_type = 3
        if crab27_type == "4":
            $ rand_crab27_type = 4
        if crab27_type == "5":
            $ rand_crab27_type = 5
        if crab27_type == "6":
            $ rand_crab27_type = 6
        if crab27_type == "7":
            $ rand_crab27_type = 7
        if crab27_type == "8":
            $ rand_crab27_type = 8
        if crab27_type == "9":
            $ rand_crab27_type = 9
        if crab27_type == "10":
            $ rand_crab27_type = 10
        if crab27_type == "11":
            $ rand_crab27_type = 11
        jump crab27_trap_get

    if not crab28:
        $ crab28 = True
        $ crab28_type = enemy_crab_type
        $ crab28_rarity = enemy_crab_rarity
        $ crab28_level = enemy_crab1_level
        if crab28_type == "1":
            $ rand_crab28_type = 1
        if crab28_type == "2":
            $ rand_crab28_type = 2
        if crab28_type == "3":
            $ rand_crab28_type = 3
        if crab28_type == "4":
            $ rand_crab28_type = 4
        if crab28_type == "5":
            $ rand_crab28_type = 5
        if crab28_type == "6":
            $ rand_crab28_type = 6
        if crab28_type == "7":
            $ rand_crab28_type = 7
        if crab28_type == "8":
            $ rand_crab28_type = 8
        if crab28_type == "9":
            $ rand_crab28_type = 9
        if crab28_type == "10":
            $ rand_crab28_type = 10
        if crab28_type == "11":
            $ rand_crab28_type = 11
        jump crab28_trap_get

    if not crab29:
        $ crab29 = True
        $ crab29_type = enemy_crab_type
        $ crab29_rarity = enemy_crab_rarity
        $ crab29_level = enemy_crab1_level
        if crab29_type == "1":
            $ rand_crab29_type = 1
        if crab29_type == "2":
            $ rand_crab29_type = 2
        if crab29_type == "3":
            $ rand_crab29_type = 3
        if crab29_type == "4":
            $ rand_crab29_type = 4
        if crab29_type == "5":
            $ rand_crab29_type = 5
        if crab29_type == "6":
            $ rand_crab29_type = 6
        if crab29_type == "7":
            $ rand_crab29_type = 7
        if crab29_type == "8":
            $ rand_crab29_type = 8
        if crab29_type == "9":
            $ rand_crab29_type = 9
        if crab29_type == "10":
            $ rand_crab29_type = 10
        if crab29_type == "11":
            $ rand_crab29_type = 11
        jump crab29_trap_get

    if not crab30:
        $ crab30 = True
        $ crab30_type = enemy_crab_type
        $ crab30_rarity = enemy_crab_rarity
        $ crab30_level = enemy_crab1_level
        if crab30_type == "1":
            $ rand_crab30_type = 1
        if crab30_type == "2":
            $ rand_crab30_type = 2
        if crab30_type == "3":
            $ rand_crab30_type = 3
        if crab30_type == "4":
            $ rand_crab30_type = 4
        if crab30_type == "5":
            $ rand_crab30_type = 5
        if crab30_type == "6":
            $ rand_crab30_type = 6
        if crab30_type == "7":
            $ rand_crab30_type = 7
        if crab30_type == "8":
            $ rand_crab30_type = 8
        if crab30_type == "9":
            $ rand_crab30_type = 9
        if crab30_type == "10":
            $ rand_crab30_type = 10
        if crab30_type == "11":
            $ rand_crab30_type = 11
        jump crab30_trap_get

label rarity_evolve:
    if rarity_stones <=0:
        y "i don't have any rarity stones...."
        jump crab_stat_screen

    "using a rarity stone will evolve this crab's rarity and revert it to level 2."
    "continue?"
    menu:
        "use rarity stone":
            jump rarity_evolve_cont
        "cancel":

            jump crab_stat_screen

label rarity_evolve_cont:
    $ rarity_happening = True

    hide screen crabs_stats

    if crab1_stat_select:
        if crab1_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab1_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab1_level >=30:
            $ rarity_stones -=1
            if crab1_rarity == "n":
                $ crab1_rarity = "r"
                $ crab1_level = 2
                jump after_rarity_check
            if crab1_rarity == "r":
                $ crab1_rarity = "e"
                $ crab1_level = 2
                jump after_rarity_check
            if crab1_rarity == "e":
                $ crab1_rarity = "l"
                $ crab1_level = 2
                jump after_rarity_check

    if crab2_stat_select:
        if crab2_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab2_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab2_level >=30:
            $ rarity_stones -=1
            if crab2_rarity == "n":
                $ crab2_rarity = "r"
                $ crab2_level = 2
                jump after_rarity_check
                jump after_rarity_check
            if crab2_rarity == "r":
                $ crab2_rarity = "e"
                $ crab2_level = 2
                jump after_rarity_check
            if crab2_rarity == "e":
                $ crab2_rarity = "l"
                $ crab2_level = 2
                jump after_rarity_check

    if crab3_stat_select:
        if crab3_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab3_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab3_level >=30:
            $ rarity_stones -=1
            if crab3_rarity == "n":
                $ crab3_rarity = "r"
                $ crab3_level = 2
                jump after_rarity_check
            if crab3_rarity == "r":
                $ crab3_rarity = "e"
                $ crab3_level = 2
                jump after_rarity_check
            if crab3_rarity == "e":
                $ crab3_rarity = "l"
                $ crab3_level = 2
                jump after_rarity_check

    if crab4_stat_select:
        if crab4_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab4_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab4_level >=30:
            $ rarity_stones -=1
            if crab4_rarity == "n":
                $ crab4_rarity = "r"
                $ crab4_level = 2
                jump after_rarity_check
            if crab4_rarity == "r":
                $ crab4_rarity = "e"
                $ crab4_level = 2
                jump after_rarity_check
            if crab4_rarity == "e":
                $ crab4_rarity = "l"
                $ crab4_level = 2
                jump after_rarity_check

    if crab5_stat_select:
        if crab5_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab5_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab5_level >=30:
            $ rarity_stones -=1
            if crab5_rarity == "n":
                $ crab5_rarity = "r"
                $ crab5_level = 2
                jump after_rarity_check
            if crab5_rarity == "r":
                $ crab5_rarity = "e"
                $ crab5_level = 2
                jump after_rarity_check
            if crab5_rarity == "e":
                $ crab5_rarity = "l"
                $ crab5_level = 2
                jump after_rarity_check

    if crab6_stat_select:
        if crab6_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab6_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab6_level >=30:
            $ rarity_stones -=1
            if crab6_rarity == "n":
                $ crab6_rarity = "r"
                $ crab6_level = 2
                jump after_rarity_check
            if crab6_rarity == "r":
                $ crab6_rarity = "e"
                $ crab6_level = 2
                jump after_rarity_check
            if crab6_rarity == "e":
                $ crab6_rarity = "l"
                $ crab6_level = 2
                jump after_rarity_check

    if crab7_stat_select:
        if crab7_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab7_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab7_level >=30:
            $ rarity_stones -=1
            if crab7_rarity == "n":
                $ crab7_rarity = "r"
                $ crab7_level = 2
                jump after_rarity_check
            if crab7_rarity == "r":
                $ crab7_rarity = "e"
                $ crab7_level = 2
                jump after_rarity_check
            if crab7_rarity == "e":
                $ crab7_rarity = "l"
                $ crab7_level = 2
                jump after_rarity_check

    if crab8_stat_select:
        if crab8_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab8_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab8_level >=30:
            $ rarity_stones -=1
            if crab8_rarity == "n":
                $ crab8_rarity = "r"
                $ crab8_level = 2
                jump after_rarity_check
            if crab8_rarity == "r":
                $ crab8_rarity = "e"
                $ crab8_level = 2
                jump after_rarity_check
            if crab8_rarity == "e":
                $ crab8_rarity = "l"
                $ crab8_level = 2
                jump after_rarity_check

    if crab9_stat_select:
        if crab9_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab9_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab9_level >=30:
            $ rarity_stones -=1
            if crab9_rarity == "n":
                $ crab9_rarity = "r"
                $ crab9_level = 2
                jump after_rarity_check
            if crab9_rarity == "r":
                $ crab9_rarity = "e"
                $ crab9_level = 2
                jump after_rarity_check
            if crab9_rarity == "e":
                $ crab9_rarity = "l"
                $ crab9_level = 2
                jump after_rarity_check

    if crab10_stat_select:
        if crab10_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab10_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab10_level >=30:
            $ rarity_stones -=1
            if crab10_rarity == "n":
                $ crab10_rarity = "r"
                $ crab10_level = 2
                jump after_rarity_check
            if crab10_rarity == "r":
                $ crab10_rarity = "e"
                $ crab10_level = 2
                jump after_rarity_check
            if crab10_rarity == "e":
                $ crab10_rarity = "l"
                $ crab10_level = 2
                jump after_rarity_check

    if crab11_stat_select:
        if crab11_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab11_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab11_level >=30:
            $ rarity_stones -=1
            if crab11_rarity == "n":
                $ crab11_rarity = "r"
                $ crab11_level = 2
                jump after_rarity_check
            if crab11_rarity == "r":
                $ crab11_rarity = "e"
                $ crab11_level = 2
                jump after_rarity_check
            if crab11_rarity == "e":
                $ crab11_rarity = "l"
                $ crab11_level = 2
                jump after_rarity_check

    if crab12_stat_select:
        if crab12_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab12_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab12_level >=30:
            $ rarity_stones -=1
            if crab12_rarity == "n":
                $ crab12_rarity = "r"
                $ crab12_level = 2
                jump after_rarity_check
            if crab12_rarity == "r":
                $ crab12_rarity = "e"
                $ crab12_level = 2
                jump after_rarity_check
            if crab12_rarity == "e":
                $ crab12_rarity = "l"
                $ crab12_level = 2
                jump after_rarity_check

    if crab13_stat_select:
        if crab13_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab13_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab13_level >=30:
            $ rarity_stones -=1
            if crab13_rarity == "n":
                $ crab13_rarity = "r"
                $ crab13_level = 2
                jump after_rarity_check
            if crab13_rarity == "r":
                $ crab13_rarity = "e"
                $ crab13_level = 2
                jump after_rarity_check
            if crab13_rarity == "e":
                $ crab13_rarity = "l"
                $ crab13_level = 2
                jump after_rarity_check

    if crab14_stat_select:
        if crab14_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab14_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab14_level >=30:
            $ rarity_stones -=1
            if crab14_rarity == "n":
                $ crab14_rarity = "r"
                $ crab14_level = 2
                jump after_rarity_check
            if crab14_rarity == "r":
                $ crab14_rarity = "e"
                $ crab14_level = 2
                jump after_rarity_check
            if crab14_rarity == "e":
                $ crab14_rarity = "l"
                $ crab14_level = 2
                jump after_rarity_check

    if crab15_stat_select:
        if crab15_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab15_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab15_level >=30:
            $ rarity_stones -=1
            if crab15_rarity == "n":
                $ crab15_rarity = "r"
                $ crab15_level = 2
                jump after_rarity_check
            if crab15_rarity == "r":
                $ crab15_rarity = "e"
                $ crab15_level = 2
                jump after_rarity_check
            if crab15_rarity == "e":
                $ crab15_rarity = "l"
                $ crab15_level = 2
                jump after_rarity_check

    if crab16_stat_select:
        if crab16_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab16_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab16_level >=30:
            $ rarity_stones -=1
            if crab16_rarity == "n":
                $ crab16_rarity = "r"
                $ crab16_level = 2
                jump after_rarity_check
            if crab16_rarity == "r":
                $ crab16_rarity = "e"
                $ crab16_level = 2
                jump after_rarity_check
            if crab16_rarity == "e":
                $ crab16_rarity = "l"
                $ crab16_level = 2
                jump after_rarity_check

    if crab17_stat_select:
        if crab17_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab17_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab17_level >=30:
            $ rarity_stones -=1
            if crab17_rarity == "n":
                $ crab17_rarity = "r"
                $ crab17_level = 2
                jump after_rarity_check
            if crab17_rarity == "r":
                $ crab17_rarity = "e"
                $ crab17_level = 2
                jump after_rarity_check
            if crab17_rarity == "e":
                $ crab17_rarity = "l"
                $ crab17_level = 2
                jump after_rarity_check

    if crab18_stat_select:
        if crab18_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab18_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab18_level >=30:
            $ rarity_stones -=1
            if crab18_rarity == "n":
                $ crab18_rarity = "r"
                $ crab18_level = 2
                jump after_rarity_check
            if crab18_rarity == "r":
                $ crab18_rarity = "e"
                $ crab18_level = 2
                jump after_rarity_check
            if crab18_rarity == "e":
                $ crab18_rarity = "l"
                $ crab18_level = 2
                jump after_rarity_check

    if crab19_stat_select:
        if crab19_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab19_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab19_level >=30:
            $ rarity_stones -=1
            if crab19_rarity == "n":
                $ crab19_rarity = "r"
                $ crab19_level = 2
                jump after_rarity_check
            if crab19_rarity == "r":
                $ crab19_rarity = "e"
                $ crab19_level = 2
                jump after_rarity_check
            if crab19_rarity == "e":
                $ crab19_rarity = "l"
                $ crab19_level = 2
                jump after_rarity_check

    if crab20_stat_select:
        if crab20_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab20_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab20_level >=30:
            $ rarity_stones -=1
            if crab20_rarity == "n":
                $ crab20_rarity = "r"
                $ crab20_level = 2
                jump after_rarity_check
            if crab20_rarity == "r":
                $ crab20_rarity = "e"
                $ crab20_level = 2
                jump after_rarity_check
            if crab20_rarity == "e":
                $ crab20_rarity = "l"
                $ crab20_level = 2
                jump after_rarity_check

    if crab21_stat_select:
        if crab21_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab21_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab21_level >=30:
            $ rarity_stones -=1
            if crab21_rarity == "n":
                $ crab21_rarity = "r"
                $ crab21_level = 2
                jump after_rarity_check
            if crab21_rarity == "r":
                $ crab21_rarity = "e"
                $ crab21_level = 2
                jump after_rarity_check
            if crab21_rarity == "e":
                $ crab21_rarity = "l"
                $ crab21_level = 2
                jump after_rarity_check

    if crab22_stat_select:
        if crab22_rarity == "l":
            "this crab is fully evolved!"
            jump after_rarity_check
        if crab22_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab22_level >=30:
            $ rarity_stones -=1
            if crab22_rarity == "n":
                $ crab22_rarity = "r"
                $ crab22_level = 2
                jump after_rarity_check
            if crab22_rarity == "r":
                $ crab22_rarity = "e"
                $ crab22_level = 2
                jump after_rarity_check
            if crab22_rarity == "e":
                $ crab22_rarity = "l"
                $ crab22_level = 2
                jump after_rarity_check

    if crab23_stat_select:
        if crab23_rarity == "l":
            "this crab is fully evolved!"
        if crab23_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab23_level >=30:
            $ rarity_stones -=1
            if crab23_rarity == "n":
                $ crab23_rarity = "r"
                $ crab23_level = 2
                jump after_rarity_check
            if crab23_rarity == "r":
                $ crab23_rarity = "e"
                $ crab23_level = 2
                jump after_rarity_check
            if crab23_rarity == "e":
                $ crab23_rarity = "l"
                $ crab23_level = 2
                jump after_rarity_check

    if crab24_stat_select:
        if crab24_rarity == "l":
            "this crab is fully evolved!"
        if crab24_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab24_level >=30:
            $ rarity_stones -=1
            if crab24_rarity == "n":
                $ crab24_rarity = "r"
                $ crab24_level = 2
                jump after_rarity_check
            if crab24_rarity == "r":
                $ crab24_rarity = "e"
                $ crab24_level = 2
                jump after_rarity_check
            if crab24_rarity == "e":
                $ crab24_rarity = "l"
                $ crab24_level = 2
                jump after_rarity_check

    if crab25_stat_select:
        if crab25_rarity == "l":
            "this crab is fully evolved!"
        if crab25_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab25_level >=30:
            $ rarity_stones -=1
            if crab25_rarity == "n":
                $ crab25_rarity = "r"
                $ crab25_level = 2
                jump after_rarity_check
            if crab25_rarity == "r":
                $ crab25_rarity = "e"
                $ crab25_level = 2
                jump after_rarity_check
            if crab25_rarity == "e":
                $ crab25_rarity = "l"
                $ crab25_level = 2
                jump after_rarity_check

    if crab26_stat_select:
        if crab26_rarity == "l":
            "this crab is fully evolved!"
        if crab26_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab26_level >=30:
            $ rarity_stones -=1
            if crab26_rarity == "n":
                $ crab26_rarity = "r"
                $ crab26_level = 2
                jump after_rarity_check
            if crab26_rarity == "r":
                $ crab26_rarity = "e"
                $ crab26_level = 2
                jump after_rarity_check
            if crab26_rarity == "e":
                $ crab26_rarity = "l"
                $ crab26_level = 2
                jump after_rarity_check

    if crab27_stat_select:
        if crab27_rarity == "l":
            "this crab is fully evolved!"
        if crab27_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab27_level >=30:
            $ rarity_stones -=1
            if crab27_rarity == "n":
                $ crab27_rarity = "r"
                $ crab27_level = 2
                jump after_rarity_check
            if crab27_rarity == "r":
                $ crab27_rarity = "e"
                $ crab27_level = 2
                jump after_rarity_check
            if crab27_rarity == "e":
                $ crab27_rarity = "l"
                $ crab27_level = 2
                jump after_rarity_check

    if crab28_stat_select:
        if crab28_rarity == "l":
            "this crab is fully evolved!"
        if crab28_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab28_level >=30:
            $ rarity_stones -=1
            if crab28_rarity == "n":
                $ crab28_rarity = "r"
                $ crab28_level = 2
                jump after_rarity_check
            if crab28_rarity == "r":
                $ crab28_rarity = "e"
                $ crab28_level = 2
                jump after_rarity_check
            if crab28_rarity == "e":
                $ crab28_rarity = "l"
                $ crab28_level = 2
                jump after_rarity_check

    if crab29_stat_select:
        if crab29_rarity == "l":
            "this crab is fully evolved!"
        if crab29_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab29_level >=30:
            $ rarity_stones -=1
            if crab29_rarity == "n":
                $ crab29_rarity = "r"
                $ crab29_level = 2
                jump after_rarity_check
            if crab29_rarity == "r":
                $ crab29_rarity = "e"
                $ crab29_level = 2
                jump after_rarity_check
            if crab29_rarity == "e":
                $ crab29_rarity = "l"
                $ crab29_level = 2
                jump after_rarity_check

    if crab30_stat_select:
        if crab30_rarity == "l":
            "this crab is fully evolved!"
        if crab30_level <30:
            "your crab needs to be at least level 30 to evolve."
            $ rarity_happening = False
            jump crab_stats_page1
        if crab30_level >=30:
            $ rarity_stones -=1
            if crab30_rarity == "n":
                $ crab30_rarity = "r"
                $ crab30_level = 2
                jump after_rarity_check
            if crab30_rarity == "r":
                $ crab30_rarity = "e"
                $ crab30_level = 2
                jump after_rarity_check
            if crab30_rarity == "e":
                $ crab30_rarity = "l"
                $ crab30_level = 2
                jump after_rarity_check

label after_rarity_check:

    $ crab1_stat_select = False
    $ crab2_stat_select = False
    $ crab3_stat_select = False
    $ crab4_stat_select = False
    $ crab5_stat_select = False
    $ crab6_stat_select = False
    $ crab7_stat_select = False
    $ crab8_stat_select = False
    $ crab9_stat_select = False
    $ crab10_stat_select = False
    $ crab11_stat_select = False
    $ crab12_stat_select = False
    $ crab13_stat_select = False
    $ crab14_stat_select = False
    $ crab15_stat_select = False
    $ crab16_stat_select = False
    $ crab17_stat_select = False
    $ crab18_stat_select = False
    $ crab19_stat_select = False
    $ crab20_stat_select = False
    $ crab21_stat_select = False
    $ crab22_stat_select = False
    $ crab23_stat_select = False
    $ crab24_stat_select = False
    $ crab25_stat_select = False
    $ crab26_stat_select = False
    $ crab27_stat_select = False
    $ crab28_stat_select = False
    $ crab29_stat_select = False
    $ crab30_stat_select = False

    jump after_arena_end_level_check
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
