label switch_crab1:
    if crab1_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab1_active = True
        $ crab_standin_health = crab1_temp_hp
        $ crab_max_health = crab1_hp
        $ crab_name = crab1_name
        $ crab_level = crab1_level
        $ crab_element = crab1_element
        $ crab_att = crab1_att
        $ crab_def = crab1_def
        $ crab_acc = crab1_acc
        $ crab_type = crab1_type

        if not crab1_exp:
            $ crabs_getting_exp += 1
            $ crab1_exp = True

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

        show crab1_shuffle:
            xpos -250 ypos -200

        "go [crab1_name]!"

    jump enemy_crab_turn

label switch_crab2:
    if crab2_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab2_active = True
        $ crab_standin_health = crab2_temp_hp
        $ crab_max_health = crab2_hp
        $ crab_name = crab2_name
        $ crab_level = crab2_level
        $ crab_element = crab2_element
        $ crab_att = crab2_att
        $ crab_def = crab2_def
        $ crab_acc = crab2_acc
        $ crab_type = crab2_type

        if not crab2_exp:
            $ crabs_getting_exp += 1
            $ crab2_exp = True

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

        show crab2_shuffle:
            xpos -250 ypos -200

        "go [crab2_name]!"

    jump enemy_crab_turn

label switch_crab3:
    if crab3_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab3_active = True
        $ crab_standin_health = crab3_temp_hp
        $ crab_max_health = crab3_hp
        $ crab_name = crab3_name
        $ crab_level = crab3_level
        $ crab_element = crab3_element
        $ crab_att = crab3_att
        $ crab_def = crab3_def
        $ crab_acc = crab3_acc
        $ crab_type = crab3_type

        if not crab3_exp:
            $ crabs_getting_exp += 1
            $ crab3_exp = True

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

        show crab3_shuffle:
            xpos -250 ypos -200

        "go [crab3_name]!"

    jump enemy_crab_turn

label switch_crab4:
    if crab4_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab4_active = True
        $ crab_standin_health = crab4_temp_hp
        $ crab_max_health = crab4_hp
        $ crab_name = crab4_name
        $ crab_level = crab4_level
        $ crab_element = crab4_element
        $ crab_att = crab4_att
        $ crab_def = crab4_def
        $ crab_acc = crab4_acc
        $ crab_type = crab4_type

        if not crab4_exp:
            $ crabs_getting_exp += 1
            $ crab4_exp = True

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

        show crab4_shuffle:
            xpos -250 ypos -200

        "go [crab4_name]!"

    jump enemy_crab_turn

label switch_crab5:
    if crab5_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab5_active = True
        $ crab_standin_health = crab5_temp_hp
        $ crab_max_health = crab5_hp
        $ crab_name = crab5_name
        $ crab_level = crab5_level
        $ crab_element = crab5_element
        $ crab_att = crab5_att
        $ crab_def = crab5_def
        $ crab_acc = crab5_acc
        $ crab_type = crab5_type

        if not crab5_exp:
            $ crabs_getting_exp += 1
            $ crab5_exp = True

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

        show crab5_shuffle:
            xpos -250 ypos -200

        "go [crab5_name]!"

    jump enemy_crab_turn

label switch_crab6:
    if crab6_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab6_active = True
        $ crab_standin_health = crab6_temp_hp
        $ crab_max_health = crab6_hp
        $ crab_name = crab6_name
        $ crab_level = crab6_level
        $ crab_element = crab6_element
        $ crab_att = crab6_att
        $ crab_def = crab6_def
        $ crab_acc = crab6_acc
        $ crab_type = crab6_type

        if not crab6_exp:
            $ crabs_getting_exp += 1
            $ crab6_exp = True

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

        show crab6_shuffle:
            xpos -250 ypos -200

        "go [crab6_name]!"

    jump enemy_crab_turn

label switch_crab7:
    if crab7_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab7_active = True
        $ crab_standin_health = crab7_temp_hp
        $ crab_max_health = crab7_hp
        $ crab_name = crab7_name
        $ crab_level = crab7_level
        $ crab_element = crab7_element
        $ crab_att = crab7_att
        $ crab_def = crab7_def
        $ crab_acc = crab7_acc
        $ crab_type = crab7_type

        if not crab7_exp:
            $ crabs_getting_exp += 1
            $ crab7_exp = True

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

        show crab7_shuffle:
            xpos -250 ypos -200

        "go [crab7_name]!"

    jump enemy_crab_turn

label switch_crab8:
    if crab8_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab8_active = True
        $ crab_standin_health = crab8_temp_hp
        $ crab_max_health = crab8_hp
        $ crab_name = crab8_name
        $ crab_level = crab8_level
        $ crab_element = crab8_element
        $ crab_att = crab8_att
        $ crab_def = crab8_def
        $ crab_acc = crab8_acc
        $ crab_type = crab8_type

        if not crab8_exp:
            $ crabs_getting_exp += 1
            $ crab8_exp = True

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

        show crab8_shuffle:
            xpos -250 ypos -200

        "go [crab8_name]!"

    jump enemy_crab_turn

label switch_crab9:
    if crab9_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab9_active = True
        $ crab_standin_health = crab9_temp_hp
        $ crab_max_health = crab9_hp
        $ crab_name = crab9_name
        $ crab_level = crab9_level
        $ crab_element = crab9_element
        $ crab_att = crab9_att
        $ crab_def = crab9_def
        $ crab_acc = crab9_acc
        $ crab_type = crab9_type

        if not crab9_exp:
            $ crabs_getting_exp += 1
            $ crab9_exp = True

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

        show crab9_shuffle:
            xpos -250 ypos -200

        "go [crab9_name]!"

    jump enemy_crab_turn

label switch_crab10:
    if crab10_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab10_active = True
        $ crab_standin_health = crab10_temp_hp
        $ crab_max_health = crab10_hp
        $ crab_name = crab10_name
        $ crab_level = crab10_level
        $ crab_element = crab10_element
        $ crab_att = crab10_att
        $ crab_def = crab10_def
        $ crab_acc = crab10_acc
        $ crab_type = crab10_type

        if not crab10_exp:
            $ crabs_getting_exp += 1
            $ crab10_exp = True

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

        show crab10_shuffle:
            xpos -250 ypos -200

        "go [crab10_name]!"

    jump enemy_crab_turn

label switch_crab11:
    if crab11_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab11_active = True
        $ crab_standin_health = crab11_temp_hp
        $ crab_max_health = crab11_hp
        $ crab_name = crab11_name
        $ crab_level = crab11_level
        $ crab_element = crab11_element
        $ crab_att = crab11_att
        $ crab_def = crab11_def
        $ crab_acc = crab11_acc
        $ crab_type = crab11_type

        if not crab11_exp:
            $ crabs_getting_exp += 1
            $ crab11_exp = True

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

        show crab11_shuffle:
            xpos -250 ypos -200

        "go [crab11_name]!"

    jump enemy_crab_turn

label switch_crab12:
    if crab12_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab12_active = True
        $ crab_standin_health = crab12_temp_hp
        $ crab_max_health = crab12_hp
        $ crab_name = crab12_name
        $ crab_level = crab12_level
        $ crab_element = crab12_element
        $ crab_att = crab12_att
        $ crab_def = crab12_def
        $ crab_acc = crab12_acc
        $ crab_type = crab12_type

        if not crab12_exp:
            $ crabs_getting_exp += 1
            $ crab12_exp = True

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

        show crab12_shuffle:
            xpos -250 ypos -200

        "go [crab12_name]!"

    jump enemy_crab_turn

label switch_crab13:
    if crab13_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab13_active = True
        $ crab_standin_health = crab13_temp_hp
        $ crab_max_health = crab13_hp
        $ crab_name = crab13_name
        $ crab_level = crab13_level
        $ crab_element = crab13_element
        $ crab_att = crab13_att
        $ crab_def = crab13_def
        $ crab_acc = crab13_acc
        $ crab_type = crab13_type

        if not crab13_exp:
            $ crabs_getting_exp += 1
            $ crab13_exp = True

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

        show crab13_shuffle:
            xpos -250 ypos -200

        "go [crab13_name]!"

    jump enemy_crab_turn

label switch_crab14:
    if crab14_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab14_active = True
        $ crab_standin_health = crab14_temp_hp
        $ crab_max_health = crab14_hp
        $ crab_name = crab14_name
        $ crab_level = crab14_level
        $ crab_element = crab14_element
        $ crab_att = crab14_att
        $ crab_def = crab14_def
        $ crab_acc = crab14_acc
        $ crab_type = crab14_type

        if not crab14_exp:
            $ crabs_getting_exp += 1
            $ crab14_exp = True

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

        show crab14_shuffle:
            xpos -250 ypos -200

        "go [crab14_name]!"

    jump enemy_crab_turn

label switch_crab15:
    if crab15_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab15_active = True
        $ crab_standin_health = crab15_temp_hp
        $ crab_max_health = crab15_hp
        $ crab_name = crab15_name
        $ crab_level = crab15_level
        $ crab_element = crab15_element
        $ crab_att = crab15_att
        $ crab_def = crab15_def
        $ crab_acc = crab15_acc
        $ crab_type = crab15_type

        if not crab15_exp:
            $ crabs_getting_exp += 1
            $ crab15_exp = True

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

        show crab15_shuffle:
            xpos -250 ypos -200

        "go [crab15_name]!"

    jump enemy_crab_turn

label switch_crab16:
    if crab16_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab16_active = True
        $ crab_standin_health = crab16_temp_hp
        $ crab_max_health = crab16_hp
        $ crab_name = crab16_name
        $ crab_level = crab16_level
        $ crab_element = crab16_element
        $ crab_att = crab16_att
        $ crab_def = crab16_def
        $ crab_acc = crab16_acc
        $ crab_type = crab16_type

        if not crab16_exp:
            $ crabs_getting_exp += 1
            $ crab16_exp = True

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

        show crab16_shuffle:
            xpos -250 ypos -200

        "go [crab16_name]!"

    jump enemy_crab_turn

label switch_crab17:
    if crab17_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab17_active = True
        $ crab_standin_health = crab17_temp_hp
        $ crab_max_health = crab17_hp
        $ crab_name = crab17_name
        $ crab_level = crab17_level
        $ crab_element = crab17_element
        $ crab_att = crab17_att
        $ crab_def = crab17_def
        $ crab_acc = crab17_acc
        $ crab_type = crab17_type

        if not crab17_exp:
            $ crabs_getting_exp += 1
            $ crab17_exp = True

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

        show crab17_shuffle:
            xpos -250 ypos -200

        "go [crab17_name]!"

    jump enemy_crab_turn

label switch_crab18:
    if crab18_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab18_active = True
        $ crab_standin_health = crab18_temp_hp
        $ crab_max_health = crab18_hp
        $ crab_name = crab18_name
        $ crab_level = crab18_level
        $ crab_element = crab18_element
        $ crab_att = crab18_att
        $ crab_def = crab18_def
        $ crab_acc = crab18_acc
        $ crab_type = crab18_type

        if not crab18_exp:
            $ crabs_getting_exp += 1
            $ crab18_exp = True

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

        show crab18_shuffle:
            xpos -250 ypos -200

        "go [crab18_name]!"

    jump enemy_crab_turn

label switch_crab19:
    if crab19_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab19_active = True
        $ crab_standin_health = crab19_temp_hp
        $ crab_max_health = crab19_hp
        $ crab_name = crab19_name
        $ crab_level = crab19_level
        $ crab_element = crab19_element
        $ crab_att = crab19_att
        $ crab_def = crab19_def
        $ crab_acc = crab19_acc
        $ crab_type = crab19_type

        if not crab19_exp:
            $ crabs_getting_exp += 1
            $ crab19_exp = True

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

        show crab19_shuffle:
            xpos -250 ypos -200

        "go [crab19_name]!"

    jump enemy_crab_turn

label switch_crab20:
    if crab20_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab20_active = True
        $ crab_standin_health = crab20_temp_hp
        $ crab_max_health = crab20_hp
        $ crab_name = crab20_name
        $ crab_level = crab20_level
        $ crab_element = crab20_element
        $ crab_att = crab20_att
        $ crab_def = crab20_def
        $ crab_acc = crab20_acc
        $ crab_type = crab20_type

        if not crab20_exp:
            $ crabs_getting_exp += 1
            $ crab20_exp = True

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

        show crab20_shuffle:
            xpos -250 ypos -200

        "go [crab20_name]!"

    jump enemy_crab_turn

label switch_crab21:
    if crab21_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab21_active = True
        $ crab_standin_health = crab21_temp_hp
        $ crab_max_health = crab21_hp
        $ crab_name = crab21_name
        $ crab_level = crab21_level
        $ crab_element = crab21_element
        $ crab_att = crab21_att
        $ crab_def = crab21_def
        $ crab_acc = crab21_acc
        $ crab_type = crab21_type

        if not crab21_exp:
            $ crabs_getting_exp += 1
            $ crab21_exp = True

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

        show crab21_shuffle:
            xpos -250 ypos -200

        "go [crab21_name]!"

    jump enemy_crab_turn

label switch_crab22:
    if crab22_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab22_active = True
        $ crab_standin_health = crab22_temp_hp
        $ crab_max_health = crab22_hp
        $ crab_name = crab22_name
        $ crab_level = crab22_level
        $ crab_element = crab22_element
        $ crab_att = crab22_att
        $ crab_def = crab22_def
        $ crab_acc = crab22_acc
        $ crab_type = crab22_type

        if not crab22_exp:
            $ crabs_getting_exp += 1
            $ crab22_exp = True

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

        show crab22_shuffle:
            xpos -250 ypos -200

        "go [crab22_name]!"

    jump enemy_crab_turn

label switch_crab23:
    if crab23_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab23_active = True
        $ crab_standin_health = crab23_temp_hp
        $ crab_max_health = crab23_hp
        $ crab_name = crab23_name
        $ crab_level = crab23_level
        $ crab_element = crab23_element
        $ crab_att = crab23_att
        $ crab_def = crab23_def
        $ crab_acc = crab23_acc
        $ crab_type = crab23_type

        if not crab23_exp:
            $ crabs_getting_exp += 1
            $ crab23_exp = True

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

        show crab23_shuffle:
            xpos -250 ypos -200

        "go [crab23_name]!"

    jump enemy_crab_turn

label switch_crab24:
    if crab24_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab24_active = True
        $ crab_standin_health = crab24_temp_hp
        $ crab_max_health = crab24_hp
        $ crab_name = crab24_name
        $ crab_level = crab24_level
        $ crab_element = crab24_element
        $ crab_att = crab24_att
        $ crab_def = crab24_def
        $ crab_acc = crab24_acc
        $ crab_type = crab24_type

        if not crab24_exp:
            $ crabs_getting_exp += 1
            $ crab24_exp = True

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

        show crab24_shuffle:
            xpos -250 ypos -200

        "go [crab24_name]!"

    jump enemy_crab_turn

label switch_crab25:
    if crab25_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab25_active = True
        $ crab_standin_health = crab25_temp_hp
        $ crab_max_health = crab25_hp
        $ crab_name = crab25_name
        $ crab_level = crab25_level
        $ crab_element = crab25_element
        $ crab_att = crab25_att
        $ crab_def = crab25_def
        $ crab_acc = crab25_acc
        $ crab_type = crab25_type

        if not crab25_exp:
            $ crabs_getting_exp += 1
            $ crab25_exp = True

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

        show crab25_shuffle:
            xpos -250 ypos -200

        "go [crab25_name]!"

    jump enemy_crab_turn

label switch_crab26:
    if crab26_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab26_active = True
        $ crab_standin_health = crab26_temp_hp
        $ crab_max_health = crab26_hp
        $ crab_name = crab26_name
        $ crab_level = crab26_level
        $ crab_element = crab26_element
        $ crab_att = crab26_att
        $ crab_def = crab26_def
        $ crab_acc = crab26_acc
        $ crab_type = crab26_type

        if not crab26_exp:
            $ crabs_getting_exp += 1
            $ crab26_exp = True

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

        show crab26_shuffle:
            xpos -250 ypos -200

        "go [crab26_name]!"

    jump enemy_crab_turn

label switch_crab27:
    if crab27_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab27_active = True
        $ crab_standin_health = crab27_temp_hp
        $ crab_max_health = crab27_hp
        $ crab_name = crab27_name
        $ crab_level = crab27_level
        $ crab_element = crab27_element
        $ crab_att = crab27_att
        $ crab_def = crab27_def
        $ crab_acc = crab27_acc
        $ crab_type = crab27_type

        if not crab27_exp:
            $ crabs_getting_exp += 1
            $ crab27_exp = True

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

        show crab27_shuffle:
            xpos -250 ypos -200

        "go [crab27_name]!"

    jump enemy_crab_turn

label switch_crab28:
    if crab28_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab28_active = True
        $ crab_standin_health = crab28_temp_hp
        $ crab_max_health = crab28_hp
        $ crab_name = crab28_name
        $ crab_level = crab28_level
        $ crab_element = crab28_element
        $ crab_att = crab28_att
        $ crab_def = crab28_def
        $ crab_acc = crab28_acc
        $ crab_type = crab28_type

        if not crab28_exp:
            $ crabs_getting_exp += 1
            $ crab28_exp = True

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

        show crab28_shuffle:
            xpos -250 ypos -200

        "go [crab28_name]!"

    jump enemy_crab_turn

label switch_crab29:
    if crab29_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab29_active = True
        $ crab_standin_health = crab29_temp_hp
        $ crab_max_health = crab29_hp
        $ crab_name = crab29_name
        $ crab_level = crab29_level
        $ crab_element = crab29_element
        $ crab_att = crab29_att
        $ crab_def = crab29_def
        $ crab_acc = crab29_acc
        $ crab_type = crab29_type

        if not crab29_exp:
            $ crabs_getting_exp += 1
            $ crab29_exp = True

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

        show crab29_shuffle:
            xpos -250 ypos -200

        "go [crab29_name]!"

    jump enemy_crab_turn

label switch_crab30:
    if crab30_temp_hp <=0:
        "this crab is unconscious!"
        jump arena_switch
    else:
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

        $ crab30_active = True
        $ crab_standin_health = crab30_hp
        $ crab_max_health = crab30_hp
        $ crab_name = crab30_name
        $ crab_level = crab30_level
        $ crab_element = crab30_element
        $ crab_att = crab30_att
        $ crab_def = crab30_def
        $ crab_acc = crab30_acc
        $ crab_type = crab30_type

        if not crab30_exp:
            $ crabs_getting_exp += 1
            $ crab30_exp = True

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

        show crab30_shuffle:
            xpos -250 ypos -200

        "go [crab30_name]!"

    jump enemy_crab_turn
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
