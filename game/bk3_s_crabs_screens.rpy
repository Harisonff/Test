
screen bk3_crabstats1:
    frame:
        xminimum 350
        has vbox
        text "[enemy_crab_name] - level [enemy_crab_level] ([opp_element])":
            xpos 45
        text "{b}hp: [crab_health]/[enemy_crab_health_max]":
            xpos 120
        hbox:

            bar range enemy_crab_health_max value crab_health xmaximum 400

        text "[opp_name]'s crabs: [total_enemy_crabs]":
            xpos 85


    frame:
        xminimum 405
        xalign 1.0
        yalign 0.5
        has vbox

        if not crab_standin:
            text "[povname]":
                xpos 100
            text "{b}hp: [crab_player_health]/[crab_player_max_health]":
                xpos 100
        if crab_standin:
            text "[crab_name] - level [crab_level] ([crab_element])":
                xpos 70
            text "{b}hp: [crab_standin_health]/[crab_max_health]":
                xpos 115
            hbox:

                bar range crab_max_health value crab_standin_health xmaximum 400

        text "[povname]'s crabs: [crabs_alive]":
            xpos 100










screen arena_battle:

    hbox:
        xalign 0.7
        yalign 0.7
        textbutton "fight" action Jump("arena_fight")

screen arena_battle_buttons:
    frame:
        xminimum 315
        yminimum 150
        xalign 0.85
        yalign 0.78
        vbox


    if arena_active:

        hbox:
            xalign 0.705
            yalign 0.7
            textbutton " fight  " action Jump("arena_fight")
        hbox:
            xalign 0.705
            yalign 0.76
            textbutton "switch" action Jump("arena_switch")
        hbox:
            xalign 0.82
            yalign 0.7
            textbutton " item  " action Jump("arena_item")
        hbox:
            xalign 0.82
            yalign 0.76
            textbutton " run  " action Jump("arena_run")

    if arena_fighting:
        hbox:
            xalign 0.705
            yalign 0.7
            if crab1_active:
                if crab1_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab1_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab1_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab1_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab1_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab1_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab1_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab1_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab1_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab1_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab1_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab2_active:
                if crab2_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab2_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab2_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab2_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab2_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab2_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab2_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab2_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab2_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab2_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab2_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab3_active:
                if crab3_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab3_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab3_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab3_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab3_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab3_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab3_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab3_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab3_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab3_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab3_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab4_active:
                if crab4_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab4_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab4_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab4_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab4_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab4_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab4_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab4_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab4_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab4_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab4_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab5_active:
                if crab5_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab5_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab5_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab5_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab5_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab5_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab5_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab5_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab5_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab5_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab5_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab6_active:
                if crab6_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab6_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab6_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab6_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab6_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab6_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab6_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab6_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab6_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab6_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab6_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab7_active:
                if crab7_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab7_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab7_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab7_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab7_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab7_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab7_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab7_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab7_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab7_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab7_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab8_active:
                if crab8_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab8_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab8_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab8_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab8_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab8_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab8_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab8_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab8_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab8_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab8_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab9_active:
                if crab9_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab9_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab9_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab9_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab9_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab9_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab9_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab9_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab9_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab9_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab9_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab10_active:
                if crab10_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab10_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab10_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab10_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab10_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab10_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab10_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab10_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab10_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab10_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab10_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab11_active:
                if crab11_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab11_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab11_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab11_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab11_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab11_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab11_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab11_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab11_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab11_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab11_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab12_active:
                if crab12_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab12_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab12_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab12_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab12_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab12_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab12_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab12_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab12_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab12_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab12_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab13_active:
                if crab13_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab13_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab13_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab13_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab13_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab13_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab13_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab13_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab13_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab13_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab13_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab14_active:
                if crab14_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab14_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab14_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab14_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab14_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab14_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab14_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab14_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab14_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab14_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab14_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab15_active:
                if crab15_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab15_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab15_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab15_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab15_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab15_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab15_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab15_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab15_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab15_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab15_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab16_active:
                if crab16_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab16_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab16_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab16_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab16_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab16_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab16_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab16_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab16_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab16_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab16_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab17_active:
                if crab17_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab17_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab17_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab17_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab17_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab17_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab17_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab17_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab17_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab17_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab17_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab18_active:
                if crab18_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab18_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab18_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab18_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab18_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab18_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab18_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab18_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab18_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab18_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab18_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab19_active:
                if crab19_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab19_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab19_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab19_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab19_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab19_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab19_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab19_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab19_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab19_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab19_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab20_active:
                if crab20_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab20_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab20_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab20_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab20_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab20_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab20_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab20_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab20_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab20_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab20_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab21_active:
                if crab21_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab21_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab21_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab21_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab21_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab21_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab21_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab21_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab21_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab21_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab21_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab22_active:
                if crab22_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab22_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab22_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab22_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab22_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab22_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab22_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab22_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab22_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab22_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab22_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab23_active:
                if crab23_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab23_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab23_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab23_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab23_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab23_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab23_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab23_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab23_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab23_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab23_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab24_active:
                if crab24_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab24_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab24_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab24_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab24_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab24_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab24_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab24_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab24_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab24_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab24_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab25_active:
                if crab25_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab25_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab25_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab25_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab25_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab25_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab25_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab25_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab25_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab25_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab25_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab26_active:
                if crab26_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab26_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab26_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab26_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab26_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab26_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab26_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab26_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab26_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab26_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab26_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab27_active:
                if crab27_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab27_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab27_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab27_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab27_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab27_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab27_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab27_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab27_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab27_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab27_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab28_active:
                if crab28_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab28_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab28_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab28_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab28_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab28_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab28_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab28_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab28_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab28_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab28_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab29_active:
                if crab29_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab29_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab29_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab29_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab29_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab29_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab29_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab29_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab29_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab29_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab29_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")
            if crab30_active:
                if crab30_type == "1":
                    textbutton "slash" action Jump("arena_regular_attack")
                if crab30_type == "2":
                    textbutton "reach" action Jump("arena_regular_attack")
                if crab30_type == "3":
                    textbutton "grip" action Jump("arena_regular_attack")
                if crab30_type == "4":
                    textbutton "slice" action Jump("arena_regular_attack")
                if crab30_type == "5":
                    textbutton "dope fade" action Jump("arena_regular_attack")
                if crab30_type == "6":
                    textbutton "nibble" action Jump("arena_regular_attack")
                if crab30_type == "7":
                    textbutton "spike" action Jump("arena_regular_attack")
                if crab30_type == "8":
                    textbutton "stare" action Jump("arena_regular_attack")
                if crab30_type == "9":
                    textbutton "clamp" action Jump("arena_regular_attack")
                if crab30_type == "10":
                    textbutton "bump" action Jump("arena_regular_attack")
                if crab30_type == "11":
                    textbutton "grapple" action Jump("arena_regular_attack")

        hbox:
            xalign 0.705
            yalign 0.76
            if crab1_active:
                if not crab1_move2:
                    text "--------"
                if crab1_move2:
                    if crab1_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab1_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab1_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab1_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab1_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab1_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab1_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab1_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab1_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab1_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab1_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab2_active:
                if not crab2_move2:
                    text "--------"
                if crab2_move2:
                    if crab2_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab2_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab2_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab2_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab2_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab2_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab2_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab2_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab2_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab2_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab2_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab3_active:
                if not crab3_move2:
                    text "--------"
                if crab3_move2:
                    if crab3_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab3_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab3_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab3_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab3_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab3_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab3_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab3_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab3_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab3_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab3_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab4_active:
                if not crab4_move2:
                    text "--------"
                if crab4_move2:
                    if crab4_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab4_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab4_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab4_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab4_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab4_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab4_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab4_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab4_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab4_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab4_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab5_active:
                if not crab5_move2:
                    text "--------"
                if crab5_move2:
                    if crab5_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab5_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab5_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab5_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab5_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab5_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab5_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab5_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab5_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab5_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab5_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab6_active:
                if not crab6_move2:
                    text "--------"
                if crab6_move2:
                    if crab6_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab6_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab6_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab6_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab6_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab6_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab6_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab6_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab6_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab6_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab6_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab7_active:
                if not crab7_move2:
                    text "--------"
                if crab7_move2:
                    if crab7_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab7_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab7_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab7_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab7_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab7_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab7_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab7_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab7_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab7_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab7_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab8_active:
                if not crab8_move2:
                    text "--------"
                if crab8_move2:
                    if crab8_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab8_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab8_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab8_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab8_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab8_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab8_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab8_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab8_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab8_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab8_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab9_active:
                if not crab9_move2:
                    text "--------"
                if crab9_move2:
                    if crab9_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab9_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab9_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab9_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab9_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab9_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab9_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab9_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab9_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab9_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab9_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab10_active:
                if not crab10_move2:
                    text "--------"
                if crab10_move2:
                    if crab10_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab10_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab10_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab10_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab10_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab10_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab10_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab10_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab10_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab10_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab10_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab11_active:
                if not crab11_move2:
                    text "--------"
                if crab11_move2:
                    if crab11_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab11_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab11_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab11_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab11_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab11_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab11_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab11_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab11_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab11_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab11_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab12_active:
                if not crab12_move2:
                    text "--------"
                if crab12_move2:
                    if crab12_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab12_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab12_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab12_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab12_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab12_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab12_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab12_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab12_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab12_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab12_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab13_active:
                if not crab13_move2:
                    text "--------"
                if crab13_move2:
                    if crab13_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab13_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab13_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab13_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab13_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab13_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab13_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab13_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab13_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab13_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab13_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab14_active:
                if not crab14_move2:
                    text "--------"
                if crab14_move2:
                    if crab14_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab14_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab14_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab14_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab14_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab14_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab14_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab14_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab14_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab14_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab14_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab15_active:
                if not crab15_move2:
                    text "--------"
                if crab15_move2:
                    if crab15_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab15_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab15_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab15_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab15_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab15_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab15_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab15_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab15_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab15_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab15_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab16_active:
                if not crab16_move2:
                    text "--------"
                if crab16_move2:
                    if crab16_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab16_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab16_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab16_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab16_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab16_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab16_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab16_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab16_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab16_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab16_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab17_active:
                if not crab17_move2:
                    text "--------"
                if crab17_move2:
                    if crab17_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab17_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab17_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab17_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab17_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab17_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab17_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab17_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab17_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab17_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab17_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab18_active:
                if not crab18_move2:
                    text "--------"
                if crab18_move2:
                    if crab18_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab18_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab18_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab18_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab18_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab18_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab18_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab18_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab18_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab18_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab18_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab19_active:
                if not crab19_move2:
                    text "--------"
                if crab19_move2:
                    if crab19_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab19_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab19_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab19_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab19_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab19_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab19_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab19_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab19_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab19_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab19_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab20_active:
                if not crab20_move2:
                    text "--------"
                if crab20_move2:
                    if crab20_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab20_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab20_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab20_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab20_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab20_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab20_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab20_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab20_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab20_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab20_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab21_active:
                if not crab21_move2:
                    text "--------"
                if crab21_move2:
                    if crab21_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab21_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab21_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab21_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab21_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab21_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab21_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab21_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab21_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab21_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab21_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab22_active:
                if not crab22_move2:
                    text "--------"
                if crab22_move2:
                    if crab22_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab22_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab22_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab22_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab22_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab22_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab22_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab22_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab22_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab22_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab22_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab23_active:
                if not crab23_move2:
                    text "--------"
                if crab23_move2:
                    if crab23_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab23_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab23_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab23_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab23_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab23_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab23_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab23_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab23_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab23_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab23_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab24_active:
                if not crab24_move2:
                    text "--------"
                if crab24_move2:
                    if crab24_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab24_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab24_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab24_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab24_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab24_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab24_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab24_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab24_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab24_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab24_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab25_active:
                if not crab25_move2:
                    text "--------"
                if crab25_move2:
                    if crab25_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab25_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab25_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab25_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab25_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab25_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab25_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab25_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab25_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab25_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab25_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab26_active:
                if not crab26_move2:
                    text "--------"
                if crab26_move2:
                    if crab26_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab26_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab26_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab26_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab26_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab26_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab26_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab26_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab26_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab26_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab26_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab27_active:
                if not crab27_move2:
                    text "--------"
                if crab27_move2:
                    if crab27_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab27_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab27_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab27_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab27_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab27_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab27_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab27_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab27_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab27_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab27_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab28_active:
                if not crab28_move2:
                    text "--------"
                if crab28_move2:
                    if crab28_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab28_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab28_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab28_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab28_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab28_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab28_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab28_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab28_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab28_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab28_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab29_active:
                if not crab29_move2:
                    text "--------"
                if crab29_move2:
                    if crab29_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab29_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab29_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab29_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab29_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab29_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab29_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab29_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab29_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab29_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab29_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")
            if crab30_active:
                if not crab30_move2:
                    text "--------"
                if crab30_move2:
                    if crab30_type == "1":
                        textbutton "knife-gun" action Jump("arena_charge_attack")
                    if crab30_type == "2":
                        textbutton "squeegee" action Jump("arena_boost_attack")
                    if crab30_type == "3":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab30_type == "4":
                        textbutton "dice" action Jump("arena_charge_attack")
                    if crab30_type == "5":
                        textbutton "belittle" action Jump("arena_boost_attack")
                    if crab30_type == "6":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab30_type == "7":
                        textbutton "impale" action Jump("arena_charge_attack")
                    if crab30_type == "8":
                        textbutton "sight" action Jump("arena_boost_attack")
                    if crab30_type == "9":
                        textbutton "poison" action Jump("arena_special_attack")
                    if crab30_type == "10":
                        textbutton "jostle" action Jump("arena_charge_attack")
                    if crab30_type == "11":
                        textbutton "choke hold" action Jump("arena_boost_attack")


        hbox:
            xalign 0.88
            yalign 0.7
            if crab1_active:
                if not crab1_move3:
                    text "--------"
                if crab1_move3:
                    if crab1_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab1_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab1_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab1_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab1_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab1_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab1_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab1_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab1_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab1_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab1_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab2_active:
                if not crab2_move3:
                    text "--------"
                if crab2_move3:
                    if crab2_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab2_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab2_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab2_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab2_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab2_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab2_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab2_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab2_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab2_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab2_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab3_active:
                if not crab3_move3:
                    text "--------"
                if crab3_move3:
                    if crab3_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab3_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab3_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab3_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab3_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab3_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab3_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab3_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab3_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab3_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab3_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab4_active:
                if not crab4_move3:
                    text "--------"
                if crab4_move3:
                    if crab4_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab4_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab4_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab4_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab4_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab4_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab4_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab4_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab4_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab4_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab4_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab5_active:
                if not crab5_move3:
                    text "--------"
                if crab5_move3:
                    if crab5_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab5_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab5_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab5_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab5_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab5_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab5_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab5_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab5_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab5_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab5_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab6_active:
                if not crab6_move3:
                    text "--------"
                if crab6_move3:
                    if crab6_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab6_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab6_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab6_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab6_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab6_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab6_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab6_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab6_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab6_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab6_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab7_active:
                if not crab7_move3:
                    text "--------"
                if crab7_move3:
                    if crab7_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab7_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab7_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab7_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab7_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab7_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab7_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab7_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab7_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab7_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab7_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab8_active:
                if not crab8_move3:
                    text "--------"
                if crab8_move3:
                    if crab8_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab8_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab8_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab8_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab8_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab8_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab8_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab8_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab8_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab8_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab8_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab9_active:
                if not crab9_move3:
                    text "--------"
                if crab9_move3:
                    if crab9_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab9_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab9_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab9_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab9_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab9_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab9_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab9_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab9_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab9_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab9_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab10_active:
                if not crab10_move3:
                    text "--------"
                if crab10_move3:
                    if crab10_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab10_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab10_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab10_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab10_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab10_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab10_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab10_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab10_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab10_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab10_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab11_active:
                if not crab11_move3:
                    text "--------"
                if crab11_move3:
                    if crab11_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab11_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab11_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab11_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab11_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab11_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab11_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab11_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab11_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab11_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab11_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab12_active:
                if not crab12_move3:
                    text "--------"
                if crab12_move3:
                    if crab12_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab12_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab12_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab12_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab12_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab12_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab12_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab12_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab12_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab12_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab12_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab13_active:
                if not crab13_move3:
                    text "--------"
                if crab13_move3:
                    if crab13_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab13_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab13_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab13_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab13_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab13_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab13_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab13_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab13_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab13_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab13_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab14_active:
                if not crab14_move3:
                    text "--------"
                if crab14_move3:
                    if crab14_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab14_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab14_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab14_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab14_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab14_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab14_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab14_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab14_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab14_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab14_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab15_active:
                if not crab15_move3:
                    text "--------"
                if crab15_move3:
                    if crab15_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab15_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab15_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab15_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab15_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab15_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab15_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab15_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab15_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab15_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab15_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab16_active:
                if not crab16_move3:
                    text "--------"
                if crab16_move3:
                    if crab16_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab16_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab16_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab16_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab16_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab16_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab16_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab16_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab16_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab16_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab16_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab17_active:
                if not crab17_move3:
                    text "--------"
                if crab17_move3:
                    if crab17_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab17_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab17_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab17_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab17_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab17_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab17_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab17_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab17_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab17_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab17_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab18_active:
                if not crab18_move3:
                    text "--------"
                if crab18_move3:
                    if crab18_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab18_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab18_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab18_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab18_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab18_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab18_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab18_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab18_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab18_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab18_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab19_active:
                if not crab19_move3:
                    text "--------"
                if crab19_move3:
                    if crab19_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab19_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab19_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab19_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab19_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab19_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab19_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab19_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab19_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab19_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab19_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab20_active:
                if not crab20_move3:
                    text "--------"
                if crab20_move3:
                    if crab20_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab20_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab20_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab20_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab20_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab20_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab20_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab20_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab20_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab20_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab20_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab21_active:
                if not crab21_move3:
                    text "--------"
                if crab21_move3:
                    if crab21_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab21_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab21_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab21_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab21_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab21_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab21_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab21_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab21_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab21_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab21_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab22_active:
                if not crab22_move3:
                    text "--------"
                if crab22_move3:
                    if crab22_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab22_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab22_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab22_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab22_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab22_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab22_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab22_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab22_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab22_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab22_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab23_active:
                if not crab23_move3:
                    text "--------"
                if crab23_move3:
                    if crab23_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab23_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab23_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab23_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab23_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab23_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab23_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab23_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab23_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab23_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab23_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab24_active:
                if not crab24_move3:
                    text "--------"
                if crab24_move3:
                    if crab24_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab24_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab24_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab24_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab24_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab24_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab24_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab24_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab24_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab24_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab24_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab25_active:
                if not crab25_move3:
                    text "--------"
                if crab25_move3:
                    if crab25_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab25_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab25_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab25_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab25_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab25_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab25_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab25_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab25_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab25_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab25_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab26_active:
                if not crab26_move3:
                    text "--------"
                if crab26_move3:
                    if crab26_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab26_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab26_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab26_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab26_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab26_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab26_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab26_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab26_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab26_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab26_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab27_active:
                if not crab27_move3:
                    text "--------"
                if crab27_move3:
                    if crab27_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab27_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab27_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab27_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab27_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab27_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab27_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab27_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab27_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab27_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab27_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab28_active:
                if not crab28_move3:
                    text "--------"
                if crab28_move3:
                    if crab28_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab28_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab28_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab28_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab28_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab28_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab28_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab28_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab28_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab28_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab28_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab29_active:
                if not crab29_move3:
                    text "--------"
                if crab29_move3:
                    if crab29_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab29_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab29_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab29_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab29_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab29_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab29_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab29_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab29_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab29_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab29_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")
            if crab30_active:
                if not crab30_move3:
                    text "--------"
                if crab30_move3:
                    if crab30_type == "1":
                        textbutton "double-edge" action Jump("arena_boost_attack")
                    if crab30_type == "2":
                        textbutton "skissors" action Jump("arena_charge_attack")
                    if crab30_type == "3":
                        textbutton "jerk" action Jump("arena_charge_attack")
                    if crab30_type == "4":
                        textbutton "puree" action Jump("arena_boost_attack")
                    if crab30_type == "5":
                        textbutton "rapier" action Jump("arena_charge_attack")
                    if crab30_type == "6":
                        textbutton "clip" action Jump("arena_charge_attack")
                    if crab30_type == "7":
                        textbutton "barnacles" action Jump("arena_boost_attack")
                    if crab30_type == "8":
                        textbutton "double tap" action Jump("arena_charge_attack")
                    if crab30_type == "9":
                        textbutton "squeeze" action Jump("arena_charge_attack")
                    if crab30_type == "10":
                        textbutton "shield" action Jump("arena_boost_attack")
                    if crab30_type == "11":
                        textbutton "rassle" action Jump("arena_charge_attack")



        hbox:
            xalign 0.88
            yalign 0.76
            if crab1_active:
                if not crab1_move4:
                    text "--------"
                if crab1_move4:
                    if crab1_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab1_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab1_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab1_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab1_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab1_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab1_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab1_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab1_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab1_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab1_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab2_active:
                if not crab2_move4:
                    text "--------"
                if crab2_move4:
                    if crab2_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab2_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab2_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab2_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab2_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab2_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab2_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab2_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab2_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab2_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab2_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab3_active:
                if not crab3_move4:
                    text "--------"
                if crab3_move4:
                    if crab3_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab3_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab3_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab3_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab3_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab3_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab3_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab3_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab3_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab3_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab3_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab4_active:
                if not crab4_move4:
                    text "--------"
                if crab4_move4:
                    if crab4_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab4_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab4_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab4_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab4_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab4_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab4_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab4_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab4_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab4_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab4_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab5_active:
                if not crab5_move4:
                    text "--------"
                if crab5_move4:
                    if crab5_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab5_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab5_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab5_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab5_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab5_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab5_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab5_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab5_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab5_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab5_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab6_active:
                if not crab6_move4:
                    text "--------"
                if crab6_move4:
                    if crab6_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab6_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab6_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab6_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab6_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab6_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab6_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab6_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab6_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab6_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab6_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab7_active:
                if not crab7_move4:
                    text "--------"
                if crab7_move4:
                    if crab7_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab7_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab7_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab7_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab7_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab7_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab7_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab7_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab7_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab7_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab7_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab8_active:
                if not crab8_move4:
                    text "--------"
                if crab8_move4:
                    if crab8_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab8_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab8_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab8_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab8_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab8_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab8_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab8_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab8_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab8_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab8_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab9_active:
                if not crab9_move4:
                    text "--------"
                if crab9_move4:
                    if crab9_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab9_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab9_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab9_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab9_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab9_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab9_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab9_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab9_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab9_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab9_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab10_active:
                if not crab10_move4:
                    text "--------"
                if crab10_move4:
                    if crab10_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab10_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab10_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab10_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab10_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab10_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab10_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab10_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab10_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab10_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab10_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab11_active:
                if not crab11_move4:
                    text "--------"
                if crab11_move4:
                    if crab11_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab11_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab11_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab11_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab11_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab11_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab11_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab11_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab11_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab11_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab11_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab12_active:
                if not crab12_move4:
                    text "--------"
                if crab12_move4:
                    if crab12_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab12_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab12_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab12_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab12_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab12_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab12_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab12_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab12_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab12_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab12_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab13_active:
                if not crab13_move4:
                    text "--------"
                if crab13_move4:
                    if crab13_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab13_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab13_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab13_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab13_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab13_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab13_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab13_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab13_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab13_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab13_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab14_active:
                if not crab14_move4:
                    text "--------"
                if crab14_move4:
                    if crab14_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab14_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab14_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab14_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab14_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab14_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab14_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab14_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab14_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab14_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab14_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab15_active:
                if not crab15_move4:
                    text "--------"
                if crab15_move4:
                    if crab15_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab15_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab15_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab15_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab15_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab15_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab15_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab15_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab15_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab15_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab15_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab16_active:
                if not crab16_move4:
                    text "--------"
                if crab16_move4:
                    if crab16_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab16_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab16_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab16_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab16_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab16_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab16_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab16_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab16_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab16_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab16_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab17_active:
                if not crab17_move4:
                    text "--------"
                if crab17_move4:
                    if crab17_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab17_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab17_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab17_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab17_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab17_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab17_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab17_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab17_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab17_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab17_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab18_active:
                if not crab18_move4:
                    text "--------"
                if crab18_move4:
                    if crab18_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab18_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab18_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab18_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab18_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab18_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab18_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab18_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab18_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab18_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab18_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab19_active:
                if not crab19_move4:
                    text "--------"
                if crab19_move4:
                    if crab19_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab19_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab19_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab19_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab19_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab19_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab19_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab19_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab19_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab19_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab19_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab20_active:
                if not crab20_move4:
                    text "--------"
                if crab20_move4:
                    if crab20_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab20_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab20_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab20_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab20_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab20_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab20_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab20_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab20_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab20_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab20_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab21_active:
                if not crab21_move4:
                    text "--------"
                if crab21_move4:
                    if crab21_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab21_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab21_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab21_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab21_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab21_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab21_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab21_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab21_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab21_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab21_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab22_active:
                if not crab22_move4:
                    text "--------"
                if crab22_move4:
                    if crab22_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab22_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab22_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab22_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab22_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab22_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab22_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab22_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab22_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab22_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab22_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab23_active:
                if not crab23_move4:
                    text "--------"
                if crab23_move4:
                    if crab23_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab23_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab23_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab23_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab23_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab23_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab23_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab23_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab23_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab23_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab23_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab24_active:
                if not crab24_move4:
                    text "--------"
                if crab24_move4:
                    if crab24_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab24_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab24_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab24_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab24_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab24_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab24_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab24_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab24_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab24_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab24_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab25_active:
                if not crab25_move4:
                    text "--------"
                if crab25_move4:
                    if crab25_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab25_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab25_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab25_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab25_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab25_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab25_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab25_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab25_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab25_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab25_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab26_active:
                if not crab26_move4:
                    text "--------"
                if crab26_move4:
                    if crab26_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab26_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab26_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab26_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab26_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab26_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab26_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab26_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab26_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab26_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab26_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab27_active:
                if not crab27_move4:
                    text "--------"
                if crab27_move4:
                    if crab27_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab27_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab27_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab27_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab27_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab27_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab27_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab27_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab27_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab27_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab27_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab28_active:
                if not crab28_move4:
                    text "--------"
                if crab28_move4:
                    if crab28_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab28_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab28_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab28_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab28_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab28_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab28_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab28_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab28_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab28_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab28_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab29_active:
                if not crab29_move4:
                    text "--------"
                if crab29_move4:
                    if crab29_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab29_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab29_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab29_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab29_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab29_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab29_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab29_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab29_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab29_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab29_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")
            if crab30_active:
                if not crab30_move4:
                    text "--------"
                if crab30_move4:
                    if crab30_type == "1":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab30_type == "2":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab30_type == "3":
                        textbutton "pump" action Jump("arena_boost_attack")
                    if crab30_type == "4":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab30_type == "5":
                        textbutton "weak" action Jump("arena_special_attack")
                    if crab30_type == "6":
                        textbutton "sculpt" action Jump("arena_boost_attack")
                    if crab30_type == "7":
                        textbutton "bind" action Jump("arena_special_attack")
                    if crab30_type == "8":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab30_type == "9":
                        textbutton "milk" action Jump("arena_boost_attack")
                    if crab30_type == "10":
                        textbutton "confuse" action Jump("arena_special_attack")
                    if crab30_type == "11":
                        textbutton "weak" action Jump("arena_special_attack")

        hbox:
            xalign 0.78
            yalign 0.82
            textbutton "  cancel   " action Jump("arena_battle_screen")







screen arena_lifebars:

    if not crab_standin:
        add "misc/arena_player_lifebar3.png":
            xpos arena_xpos_lifebar_player
    if crab_standin:
        add "misc/arena_player_lifebar3.png":
            xpos arena_xpos_lifebar_crab

    add "misc/arena_enemy_lifebar3.png":
        xpos arena_xpos_lifebar_enemy ypos -2

screen crabs_stats:
    add "misc/bk3_scroll.jpg"

    hbox:
        xalign 0.2
        yalign 0.1
        text "[crab_stat_rarity] [crab_stat_name] - L[crab_stat_level]"
    hbox:
        xalign 0.2
        yalign 0.17
        text "element: [crab_stat_element]"
    hbox:
        xalign 0.2
        yalign 0.24
        text "hp: [crab_stat_hp]"
    hbox:
        xalign 0.2
        yalign 0.31
        text "att: [crab_stat_att]"
    hbox:
        xalign 0.2
        yalign 0.38
        text "def: [crab_stat_def]"
    hbox:
        xalign 0.2
        yalign 0.45
        text "acc: [crab_stat_acc]"




    if crab_stat_type == "1":
        hbox:
            xalign 0.2
            yalign 0.59
            text "slash: slashes an enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "knife gun: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "double-edge: attack+, defense-"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "bind: chance the enemy can't attack"

    if crab_stat_type == "2":
        hbox:
            xalign 0.2
            yalign 0.59
            text "reach: reaches out quickly at an enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "squeegee: defense+"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "skissors: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "bind: chance the enemy can't attack"

    if crab_stat_type == "3":
        hbox:
            xalign 0.2
            yalign 0.59
            text "grip: grips an enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "poison: damage to enemy at beginning of their turn"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "jerk: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "pump: defense+, attack-"

    if crab_stat_type == "4":
        hbox:
            xalign 0.2
            yalign 0.59
            text "slice: slices an enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "dice: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "puree: attack+, but hurt self"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "confuse: chance for enemy to hurt self"

    if crab_stat_type == "5":
        hbox:
            xalign 0.2
            yalign 0.59
            text "dope fade: say no more fam"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "belittle: accuracy+, evasion+"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "rapier: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "weak: enemy can’t use charged moves"

    if crab_stat_type == "6":
        hbox:
            xalign 0.2
            yalign 0.59
            text "nibble: bite the enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "poison: damage to enemy at beginning of their turn"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "clip: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "sculpt: defense+, accuracy+"

    if crab_stat_type == "7":
        hbox:
            xalign 0.2
            yalign 0.59
            text "spike: stab the enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "impale: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "barnacles: defense+, hurts enemy when attacked"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "bind: chance for enemy to not attack"

    if crab_stat_type == "8":
        hbox:
            xalign 0.2
            yalign 0.59
            text "stare: glower, like, super hard"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "sight: accuracy+, attack-"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "double tap: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "confuse: chance to hurt self"

    if crab_stat_type == "9":
        hbox:
            xalign 0.2
            yalign 0.59
            text "clamp: clamp down on enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "poison: damage to enemy at beginning of their turn"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "squeeze: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "milk: attack+, accuracy-"

    if crab_stat_type == "10":
        hbox:
            xalign 0.2
            yalign 0.59
            text "bump: bump the enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "jostle: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "shield: defense+, evasion+"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "confuse: chance for enemy to hurt self"

    if crab_stat_type == "11":
        hbox:
            xalign 0.2
            yalign 0.59
            text "grapple: grab the enemy"
        if not crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "---------"
        if crab_stat_move2:
            hbox:
                xalign 0.2
                yalign 0.66
                text "choke hold: attack+, evasion-"
        if not crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "---------"
        if crab_stat_move3:
            hbox:
                xalign 0.2
                yalign 0.73
                text "rassle: takes a turn to charge, but has increased accuracy and power"
        if not crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "---------"
        if crab_stat_move4:
            hbox:
                xalign 0.2
                yalign 0.8
                text "weak: enemy can't use charged moves"

    if crab1_stat_select:
        add "crab1_shuffle":
            xpos 0.2 ypos -0.3
    if crab2_stat_select:
        add "crab2_shuffle":
            xpos 0.2 ypos -0.3
    if crab3_stat_select:
        add "crab3_shuffle":
            xpos 0.2 ypos -0.3
    if crab4_stat_select:
        add "crab4_shuffle":
            xpos 0.2 ypos -0.3
    if crab5_stat_select:
        add "crab5_shuffle":
            xpos 0.2 ypos -0.3
    if crab6_stat_select:
        add "crab6_shuffle":
            xpos 0.2 ypos -0.3
    if crab7_stat_select:
        add "crab7_shuffle":
            xpos 0.2 ypos -0.3
    if crab8_stat_select:
        add "crab8_shuffle":
            xpos 0.2 ypos -0.3
    if crab9_stat_select:
        add "crab9_shuffle":
            xpos 0.2 ypos -0.3
    if crab10_stat_select:
        add "crab10_shuffle":
            xpos 0.2 ypos -0.3
    if crab11_stat_select:
        add "crab11_shuffle":
            xpos 0.2 ypos -0.3
    if crab12_stat_select:
        add "crab12_shuffle":
            xpos 0.2 ypos -0.3
    if crab13_stat_select:
        add "crab13_shuffle":
            xpos 0.2 ypos -0.3
    if crab14_stat_select:
        add "crab14_shuffle":
            xpos 0.2 ypos -0.3
    if crab15_stat_select:
        add "crab15_shuffle":
            xpos 0.2 ypos -0.3
    if crab16_stat_select:
        add "crab16_shuffle":
            xpos 0.2 ypos -0.3
    if crab17_stat_select:
        add "crab17_shuffle":
            xpos 0.2 ypos -0.3
    if crab18_stat_select:
        add "crab18_shuffle":
            xpos 0.2 ypos -0.3
    if crab19_stat_select:
        add "crab19_shuffle":
            xpos 0.2 ypos -0.3
    if crab20_stat_select:
        add "crab20_shuffle":
            xpos 0.2 ypos -0.3
    if crab21_stat_select:
        add "crab21_shuffle":
            xpos 0.2 ypos -0.3
    if crab22_stat_select:
        add "crab22_shuffle":
            xpos 0.2 ypos -0.3
    if crab23_stat_select:
        add "crab23_shuffle":
            xpos 0.2 ypos -0.3
    if crab24_stat_select:
        add "crab24_shuffle":
            xpos 0.2 ypos -0.3
    if crab25_stat_select:
        add "crab25_shuffle":
            xpos 0.2 ypos -0.3
    if crab26_stat_select:
        add "crab26_shuffle":
            xpos 0.2 ypos -0.3
    if crab27_stat_select:
        add "crab27_shuffle":
            xpos 0.2 ypos -0.3
    if crab28_stat_select:
        add "crab28_shuffle":
            xpos 0.2 ypos -0.3
    if crab29_stat_select:
        add "crab29_shuffle":
            xpos 0.2 ypos -0.3
    if crab30_stat_select:
        add "crab30_shuffle":
            xpos 0.2 ypos -0.3

    textbutton "return" action Jump("crab_stats_page1"):
        xpos 650 ypos 550

    textbutton "use rarity stone" action Jump("rarity_evolve"):
        xpos 600 ypos 150
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
