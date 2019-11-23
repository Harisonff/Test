label crab1_trap_get:
    if rand_crab1_type ==1:
        $ crab1_type = "1"
        $ crab1_title = "slasher"
        $ crab1_element = "fire"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 20
            $ crab1_starting_att = 23
            $ crab1_starting_def = 17
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*4)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*3)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 26
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 24
            $ crab1_starting_att = 27
            $ crab1_starting_def = 21
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 24

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*7)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)



    if rand_crab1_type ==2:
        $ crab1_type = "2"
        $ crab1_title = "reacher"
        $ crab1_element = "water"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 20
            $ crab1_starting_att = 20
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 17

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*4)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*3)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 23
            $ crab1_starting_def = 23
            $ crab1_starting_acc = 26
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 24
            $ crab1_starting_att = 24
            $ crab1_starting_def = 24
            $ crab1_starting_acc = 27
            $ crab1_starting_ev = 21

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*7)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)



    if rand_crab1_type ==3:
        $ crab1_type = "3"
        $ crab1_title = "jacko"
        $ crab1_element = "earth"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 17
            $ crab1_starting_def = 17
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*3)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*3)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 26
            $ crab1_starting_att = 20
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 26
            $ crab1_starting_ev = 26

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 27
            $ crab1_starting_att = 21
            $ crab1_starting_def = 21
            $ crab1_starting_acc = 27
            $ crab1_starting_ev = 27

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*7)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*7)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*7)

    if rand_crab1_type ==4:
        $ crab1_type = "4"
        $ crab1_title = "julienne"
        $ crab1_element = "air"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 20
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 26
            $ crab1_starting_att = 23
            $ crab1_starting_def = 23
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 27
            $ crab1_starting_att = 24
            $ crab1_starting_def = 24
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 24

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*7)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)

    if rand_crab1_type ==5:
        $ crab1_type = "5"
        $ crab1_title = "slycer"
        $ crab1_element = "fire"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 17
            $ crab1_starting_att = 23
            $ crab1_starting_def = 17
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*3)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*3)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 20
            $ crab1_starting_att = 26
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*4)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 21
            $ crab1_starting_att = 27
            $ crab1_starting_def = 21
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 24

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*7)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)

    if rand_crab1_type ==6:
        $ crab1_type = "6"
        $ crab1_title = "clypper"
        $ crab1_element = "earth"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 20
            $ crab1_starting_att = 17
            $ crab1_starting_def = 23
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 17

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*4)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*3)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*3)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 20
            $ crab1_starting_def = 26
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 24
            $ crab1_starting_att = 21
            $ crab1_starting_def = 27
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 21

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*7)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

    if rand_crab1_type ==7:
        $ crab1_type = "7"
        $ crab1_title = "barnakel"
        $ crab1_element = "water"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 17
            $ crab1_starting_def = 26
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 17

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*3)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*3)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 26
            $ crab1_starting_att = 20
            $ crab1_starting_def = 29
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*7)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 27
            $ crab1_starting_att = 21
            $ crab1_starting_def = 30
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 21

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*7)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*8)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

    if rand_crab1_type ==8:
        $ crab1_type = "8"
        $ crab1_title = "doo'ahlai"
        $ crab1_element = "air"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 23
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 17

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*3)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 26
            $ crab1_starting_att = 26
            $ crab1_starting_def = 23
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 27
            $ crab1_starting_att = 27
            $ crab1_starting_def = 24
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 21

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*7)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*7)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

    if rand_crab1_type ==9:
        $ crab1_type = "9"
        $ crab1_title = "clawp"
        $ crab1_element = "water"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 20
            $ crab1_starting_att = 20
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*4)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 23
            $ crab1_starting_def = 23
            $ crab1_starting_acc = 23
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 24
            $ crab1_starting_att = 24
            $ crab1_starting_def = 24
            $ crab1_starting_acc = 24
            $ crab1_starting_ev = 24

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*6)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)

    if rand_crab1_type ==10:
        $ crab1_type = "10"
        $ crab1_title = "bampy"
        $ crab1_element = "earth"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 20
            $ crab1_starting_att = 17
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 17
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*4)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*3)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*3)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 20
            $ crab1_starting_def = 23
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 26

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*4)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 24
            $ crab1_starting_att = 21
            $ crab1_starting_def = 24
            $ crab1_starting_acc = 21
            $ crab1_starting_ev = 27

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*6)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*7)

    if rand_crab1_type ==11:
        $ crab1_type = "11"
        $ crab1_title = "grappy"
        $ crab1_element = "fire"
        if crab1_rarity == "n":
            $ crab1_starting_hp = 23
            $ crab1_starting_att = 23
            $ crab1_starting_def = 17
            $ crab1_starting_acc = 17
            $ crab1_starting_ev = 20

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*5)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*5)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*3)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*3)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*4)

        if crab1_rarity == "r":
            $ crab1_starting_hp = 26
            $ crab1_starting_att = 26
            $ crab1_starting_def = 20
            $ crab1_starting_acc = 20
            $ crab1_starting_ev = 23

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*6)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*6)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*4)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*4)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*5)

        if crab1_rarity == "e":
            $ crab1_starting_hp = 27
            $ crab1_starting_att = 27
            $ crab1_starting_def = 21
            $ crab1_starting_acc = 21
            $ crab1_starting_ev = 24

            $ crab1_hp = crab1_starting_hp + ((crab1_level-1)*7)
            $ crab1_att = crab1_starting_att + ((crab1_level-1)*7)
            $ crab1_def = crab1_starting_def + ((crab1_level-1)*5)
            $ crab1_acc = crab1_starting_acc + ((crab1_level-1)*5)
            $ crab1_ev = crab1_starting_ev + ((crab1_level-1)*6)
    show crab1_shuffle:
        ypos -200
    with flash

    if crab1_rarity =="n":
        "you got a normal {b}[crab1_title]{/b}!"
    if crab1_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab1_title]{/b}!"
    if crab1_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab1_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab1_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab1_name = crab1_name.strip()
            if crab1_name == "":
                $ crab1_name= crab1_title
            y "how about... [crab1_name]."
        "[crab1_title]":

            $ crab1_name = crab1_title

    jump after_crab_get

label crab2_trap_get:
    if rand_crab2_type ==1:
        $ crab2_type = "1"
        $ crab2_title = "slasher"
        $ crab2_element = "fire"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 20
            $ crab2_starting_att = 23
            $ crab2_starting_def = 17
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*4)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*3)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 26
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 24
            $ crab2_starting_att = 27
            $ crab2_starting_def = 21
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 24

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*7)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)



    if rand_crab2_type ==2:
        $ crab2_type = "2"
        $ crab2_title = "reacher"
        $ crab2_element = "water"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 20
            $ crab2_starting_att = 20
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 17

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*4)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ _ev = crab2_starting_ev + ((crab2_level-1)*3)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 23
            $ crab2_starting_def = 23
            $ crab2_starting_acc = 26
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 24
            $ crab2_starting_att = 24
            $ crab2_starting_def = 24
            $ crab2_starting_acc = 27
            $ crab2_starting_ev = 21

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*7)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)



    if rand_crab2_type ==3:
        $ crab2_type = "3"
        $ crab2_title = "jacko"
        $ crab2_element = "earth"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 17
            $ crab2_starting_def = 17
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*3)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*3)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 26
            $ crab2_starting_att = 20
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 26
            $ crab2_starting_ev = 26

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 27
            $ crab2_starting_att = 21
            $ crab2_starting_def = 21
            $ crab2_starting_acc = 27
            $ crab2_starting_ev = 27

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*7)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*7)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*7)

    if rand_crab2_type ==4:
        $ crab2_type = "4"
        $ crab2_title = "julienne"
        $ crab2_element = "air"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 20
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 26
            $ crab2_starting_att = 23
            $ crab2_starting_def = 23
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 27
            $ crab2_starting_att = 24
            $ crab2_starting_def = 24
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 24

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*7)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)

    if rand_crab2_type ==5:
        $ crab2_type = "5"
        $ crab2_title = "slycer"
        $ crab2_element = "fire"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 17
            $ crab2_starting_att = 23
            $ crab2_starting_def = 17
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*3)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*3)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 20
            $ crab2_starting_att = 26
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*4)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 21
            $ crab2_starting_att = 27
            $ crab2_starting_def = 21
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 24

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*7)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)

    if rand_crab2_type ==6:
        $ crab2_type = "6"
        $ crab2_title = "clypper"
        $ crab2_element = "earth"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 20
            $ crab2_starting_att = 17
            $ crab2_starting_def = 23
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 17

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*4)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*3)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*3)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 20
            $ crab2_starting_def = 26
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 24
            $ crab2_starting_att = 21
            $ crab2_starting_def = 27
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 21

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*7)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

    if rand_crab2_type ==7:
        $ crab2_type = "7"
        $ crab2_title = "barnakel"
        $ crab2_element = "water"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 17
            $ crab2_starting_def = 26
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 17

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*3)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*3)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 26
            $ crab2_starting_att = 20
            $ crab2_starting_def = 29
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*7)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 27
            $ crab2_starting_att = 21
            $ crab2_starting_def = 30
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 21

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*7)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*8)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

    if rand_crab2_type ==8:
        $ crab2_type = "8"
        $ crab2_title = "doo'ahlai"
        $ crab2_element = "air"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 23
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 17

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*3)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 26
            $ crab2_starting_att = 26
            $ crab2_starting_def = 23
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 27
            $ crab2_starting_att = 27
            $ crab2_starting_def = 24
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 21

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*7)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*7)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

    if rand_crab2_type ==9:
        $ crab2_type = "9"
        $ crab2_title = "clawp"
        $ crab2_element = "water"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 20
            $ crab2_starting_att = 20
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*4)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 23
            $ crab2_starting_def = 23
            $ crab2_starting_acc = 23
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 24
            $ crab2_starting_att = 24
            $ crab2_starting_def = 24
            $ crab2_starting_acc = 24
            $ crab2_starting_ev = 24

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*6)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)

    if rand_crab2_type ==10:
        $ crab2_type = "10"
        $ crab2_title = "bampy"
        $ crab2_element = "earth"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 20
            $ crab2_starting_att = 17
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 17
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*4)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*3)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*3)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 20
            $ crab2_starting_def = 23
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 26

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*4)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 24
            $ crab2_starting_att = 21
            $ crab2_starting_def = 24
            $ crab2_starting_acc = 21
            $ crab2_starting_ev = 27

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*6)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*7)

    if rand_crab2_type ==11:
        $ crab2_type = "11"
        $ crab2_title = "grappy"
        $ crab2_element = "fire"
        if crab2_rarity == "n":
            $ crab2_starting_hp = 23
            $ crab2_starting_att = 23
            $ crab2_starting_def = 17
            $ crab2_starting_acc = 17
            $ crab2_starting_ev = 20

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*5)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*5)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*3)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*3)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*4)

        if crab2_rarity == "r":
            $ crab2_starting_hp = 26
            $ crab2_starting_att = 26
            $ crab2_starting_def = 20
            $ crab2_starting_acc = 20
            $ crab2_starting_ev = 23

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*6)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*6)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*4)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*4)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*5)

        if crab2_rarity == "e":
            $ crab2_starting_hp = 27
            $ crab2_starting_att = 27
            $ crab2_starting_def = 21
            $ crab2_starting_acc = 21
            $ crab2_starting_ev = 24

            $ crab2_hp = crab2_starting_hp + ((crab2_level-1)*7)
            $ crab2_att = crab2_starting_att + ((crab2_level-1)*7)
            $ crab2_def = crab2_starting_def + ((crab2_level-1)*5)
            $ crab2_acc = crab2_starting_acc + ((crab2_level-1)*5)
            $ crab2_ev = crab2_starting_ev + ((crab2_level-1)*6)

    show crab2_shuffle:
        ypos -200
    with flash

    if crab2_rarity =="n":
        "you got a normal {b}[crab2_title]{/b}!"
    if crab2_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab2_title]{/b}!"
    if crab2_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab2_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab2_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab2_name = crab2_name.strip()
            if crab2_name == "":
                $ crab2_name= crab2_title
            y "how about... [crab2_name]."
        "[crab2_title]":

            $ crab2_name = crab2_title

    jump after_crab_get

label crab3_trap_get:
    if rand_crab3_type ==1:
        $ crab3_type = "1"
        $ crab3_title = "slasher"
        $ crab3_element = "fire"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 20
            $ crab3_starting_att = 23
            $ crab3_starting_def = 17
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*4)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*3)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 26
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 24
            $ crab3_starting_att = 27
            $ crab3_starting_def = 21
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 24

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*7)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)



    if rand_crab3_type ==2:
        $ crab3_type = "2"
        $ crab3_title = "reacher"
        $ crab3_element = "water"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 20
            $ crab3_starting_att = 20
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 17

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*4)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*3)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 23
            $ crab3_starting_def = 23
            $ crab3_starting_acc = 26
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 24
            $ crab3_starting_att = 24
            $ crab3_starting_def = 24
            $ crab3_starting_acc = 27
            $ crab3_starting_ev = 21

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*7)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)



    if rand_crab3_type ==3:
        $ crab3_type = "3"
        $ crab3_title = "jacko"
        $ crab3_element = "earth"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 17
            $ crab3_starting_def = 17
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*3)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*3)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 26
            $ crab3_starting_att = 20
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 26
            $ crab3_starting_ev = 26

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 27
            $ crab3_starting_att = 21
            $ crab3_starting_def = 21
            $ crab3_starting_acc = 27
            $ crab3_starting_ev = 27

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*7)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*7)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*7)

    if rand_crab3_type ==4:
        $ crab3_type = "4"
        $ crab3_title = "julienne"
        $ crab3_element = "air"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 20
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 26
            $ crab3_starting_att = 23
            $ crab3_starting_def = 23
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 27
            $ crab3_starting_att = 24
            $ crab3_starting_def = 24
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 24

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*7)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)

    if rand_crab3_type ==5:
        $ crab3_type = "5"
        $ crab3_title = "slycer"
        $ crab3_element = "fire"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 17
            $ crab3_starting_att = 23
            $ crab3_starting_def = 17
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*3)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*3)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 20
            $ crab3_starting_att = 26
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*4)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 21
            $ crab3_starting_att = 27
            $ crab3_starting_def = 21
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 24

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*7)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)

    if rand_crab3_type ==6:
        $ crab3_type = "6"
        $ crab3_title = "clypper"
        $ crab3_element = "earth"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 20
            $ crab3_starting_att = 17
            $ crab3_starting_def = 23
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 17

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*4)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*3)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*3)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 20
            $ crab3_starting_def = 26
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 24
            $ crab3_starting_att = 21
            $ crab3_starting_def = 27
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 21

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*7)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

    if rand_crab3_type ==7:
        $ crab3_type = "7"
        $ crab3_title = "barnakel"
        $ crab3_element = "water"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 17
            $ crab3_starting_def = 26
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 17

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*3)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*3)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 26
            $ crab3_starting_att = 20
            $ crab3_starting_def = 29
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*7)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 27
            $ crab3_starting_att = 21
            $ crab3_starting_def = 30
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 21

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*7)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*8)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

    if rand_crab3_type ==8:
        $ crab3_type = "8"
        $ crab3_title = "doo'ahlai"
        $ crab3_element = "air"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 23
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 17

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*3)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 26
            $ crab3_starting_att = 26
            $ crab3_starting_def = 23
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 27
            $ crab3_starting_att = 27
            $ crab3_starting_def = 24
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 21

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*7)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*7)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

    if rand_crab3_type ==9:
        $ crab3_type = "9"
        $ crab3_title = "clawp"
        $ crab3_element = "water"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 20
            $ crab3_starting_att = 20
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*4)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 23
            $ crab3_starting_def = 23
            $ crab3_starting_acc = 23
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 24
            $ crab3_starting_att = 24
            $ crab3_starting_def = 24
            $ crab3_starting_acc = 24
            $ crab3_starting_ev = 24

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*6)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)

    if rand_crab3_type ==10:
        $ crab3_type = "10"
        $ crab3_title = "bampy"
        $ crab3_element = "earth"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 20
            $ crab3_starting_att = 17
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 17
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*4)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*3)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*3)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 20
            $ crab3_starting_def = 23
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 26

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*4)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 24
            $ crab3_starting_att = 21
            $ crab3_starting_def = 24
            $ crab3_starting_acc = 21
            $ crab3_starting_ev = 27

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*6)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*7)

    if rand_crab3_type ==11:
        $ crab3_type = "11"
        $ crab3_title = "grappy"
        $ crab3_element = "fire"
        if crab3_rarity == "n":
            $ crab3_starting_hp = 23
            $ crab3_starting_att = 23
            $ crab3_starting_def = 17
            $ crab3_starting_acc = 17
            $ crab3_starting_ev = 20

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*5)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*5)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*3)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*3)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*4)

        if crab3_rarity == "r":
            $ crab3_starting_hp = 26
            $ crab3_starting_att = 26
            $ crab3_starting_def = 20
            $ crab3_starting_acc = 20
            $ crab3_starting_ev = 23

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*6)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*6)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*4)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*4)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*5)

        if crab3_rarity == "e":
            $ crab3_starting_hp = 27
            $ crab3_starting_att = 27
            $ crab3_starting_def = 21
            $ crab3_starting_acc = 21
            $ crab3_starting_ev = 24

            $ crab3_hp = crab3_starting_hp + ((crab3_level-1)*7)
            $ crab3_att = crab3_starting_att + ((crab3_level-1)*7)
            $ crab3_def = crab3_starting_def + ((crab3_level-1)*5)
            $ crab3_acc = crab3_starting_acc + ((crab3_level-1)*5)
            $ crab3_ev = crab3_starting_ev + ((crab3_level-1)*6)
    show crab3_shuffle:
        ypos -200
    with flash

    if crab3_rarity =="n":
        "you got a normal {b}[crab3_title]{/b}!"
    if crab3_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab3_title]{/b}!"
    if crab3_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab3_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab3_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab3_name = crab3_name.strip()
            if crab3_name == "":
                $ crab3_name= crab3_title
            y "how about... [crab3_name]."
        "[crab3_title]":

            $ crab3_name = crab3_title
    jump after_crab_get

label crab4_trap_get:
    if rand_crab4_type ==1:
        $ crab4_type = "1"
        $ crab4_title = "slasher"
        $ crab4_element = "fire"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 20
            $ crab4_starting_att = 23
            $ crab4_starting_def = 17
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*4)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*3)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 26
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 24
            $ crab4_starting_att = 27
            $ crab4_starting_def = 21
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 24

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*7)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)



    if rand_crab4_type ==2:
        $ crab4_type = "2"
        $ crab4_title = "reacher"
        $ crab4_element = "water"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 20
            $ crab4_starting_att = 20
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 17

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*4)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*3)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 23
            $ crab4_starting_def = 23
            $ crab4_starting_acc = 26
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 24
            $ crab4_starting_att = 24
            $ crab4_starting_def = 24
            $ crab4_starting_acc = 27
            $ crab4_starting_ev = 21

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*7)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)



    if rand_crab4_type ==3:
        $ crab4_type = "3"
        $ crab4_title = "jacko"
        $ crab4_element = "earth"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 17
            $ crab4_starting_def = 17
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*3)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*3)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 26
            $ crab4_starting_att = 20
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 26
            $ crab4_starting_ev = 26

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 27
            $ crab4_starting_att = 21
            $ crab4_starting_def = 21
            $ crab4_starting_acc = 27
            $ crab4_starting_ev = 27

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*7)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*7)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*7)

    if rand_crab4_type ==4:
        $ crab4_type = "4"
        $ crab4_title = "julienne"
        $ crab4_element = "air"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 20
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 26
            $ crab4_starting_att = 23
            $ crab4_starting_def = 23
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 27
            $ crab4_starting_att = 24
            $ crab4_starting_def = 24
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 24

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*7)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)

    if rand_crab4_type ==5:
        $ crab4_type = "5"
        $ crab4_title = "slycer"
        $ crab4_element = "fire"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 17
            $ crab4_starting_att = 23
            $ crab4_starting_def = 17
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*3)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*3)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 20
            $ crab4_starting_att = 26
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*4)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 21
            $ crab4_starting_att = 27
            $ crab4_starting_def = 21
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 24

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*7)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)

    if rand_crab4_type ==6:
        $ crab4_type = "6"
        $ crab4_title = "clypper"
        $ crab4_element = "earth"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 20
            $ crab4_starting_att = 17
            $ crab4_starting_def = 23
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 17

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*4)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*3)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*3)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 20
            $ crab4_starting_def = 26
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 24
            $ crab4_starting_att = 21
            $ crab4_starting_def = 27
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 21

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*7)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

    if rand_crab4_type ==7:
        $ crab4_type = "7"
        $ crab4_title = "barnakel"
        $ crab4_element = "water"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 17
            $ crab4_starting_def = 26
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 17

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*3)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*3)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 26
            $ crab4_starting_att = 20
            $ crab4_starting_def = 29
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*7)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 27
            $ crab4_starting_att = 21
            $ crab4_starting_def = 30
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 21

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*7)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*8)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

    if rand_crab4_type ==8:
        $ crab4_type = "8"
        $ crab4_title = "doo'ahlai"
        $ crab4_element = "air"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 23
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 17

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*3)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 26
            $ crab4_starting_att = 26
            $ crab4_starting_def = 23
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 27
            $ crab4_starting_att = 27
            $ crab4_starting_def = 24
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 21

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*7)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*7)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

    if rand_crab4_type ==9:
        $ crab4_type = "9"
        $ crab4_title = "clawp"
        $ crab4_element = "water"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 20
            $ crab4_starting_att = 20
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*4)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 23
            $ crab4_starting_def = 23
            $ crab4_starting_acc = 23
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 24
            $ crab4_starting_att = 24
            $ crab4_starting_def = 24
            $ crab4_starting_acc = 24
            $ crab4_starting_ev = 24

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*6)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)

    if rand_crab4_type ==10:
        $ crab4_type = "10"
        $ crab4_title = "bampy"
        $ crab4_element = "earth"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 20
            $ crab4_starting_att = 17
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 17
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*4)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*3)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*3)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 20
            $ crab4_starting_def = 23
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 26

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*4)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 24
            $ crab4_starting_att = 21
            $ crab4_starting_def = 24
            $ crab4_starting_acc = 21
            $ crab4_starting_ev = 27

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*6)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*7)

    if rand_crab4_type ==11:
        $ crab4_type = "11"
        $ crab4_title = "grappy"
        $ crab4_element = "fire"
        if crab4_rarity == "n":
            $ crab4_starting_hp = 23
            $ crab4_starting_att = 23
            $ crab4_starting_def = 17
            $ crab4_starting_acc = 17
            $ crab4_starting_ev = 20

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*5)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*5)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*3)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*3)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*4)

        if crab4_rarity == "r":
            $ crab4_starting_hp = 26
            $ crab4_starting_att = 26
            $ crab4_starting_def = 20
            $ crab4_starting_acc = 20
            $ crab4_starting_ev = 23

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*6)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*6)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*4)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*4)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*5)

        if crab4_rarity == "e":
            $ crab4_starting_hp = 27
            $ crab4_starting_att = 27
            $ crab4_starting_def = 21
            $ crab4_starting_acc = 21
            $ crab4_starting_ev = 24

            $ crab4_hp = crab4_starting_hp + ((crab4_level-1)*7)
            $ crab4_att = crab4_starting_att + ((crab4_level-1)*7)
            $ crab4_def = crab4_starting_def + ((crab4_level-1)*5)
            $ crab4_acc = crab4_starting_acc + ((crab4_level-1)*5)
            $ crab4_ev = crab4_starting_ev + ((crab4_level-1)*6)
    show crab4_shuffle:
        ypos -200
    with flash

    if crab4_rarity =="n":
        "you got a normal {b}[crab4_title]{/b}!"
    if crab4_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab4_title]{/b}!"
    if crab4_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab4_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab4_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab4_name = crab4_name.strip()
            if crab4_name == "":
                $ crab4_name= crab4_title
            y "how about... [crab4_name]."
        "[crab4_title]":

            $ crab4_name = crab4_title

    jump after_crab_get

label crab5_trap_get:
    if rand_crab5_type ==1:
        $ crab5_type = "1"
        $ crab5_title = "slasher"
        $ crab5_element = "fire"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 20
            $ crab5_starting_att = 23
            $ crab5_starting_def = 17
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*4)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*3)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 26
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 24
            $ crab5_starting_att = 27
            $ crab5_starting_def = 21
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 24

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*7)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)



    if rand_crab5_type ==2:
        $ crab5_type = "2"
        $ crab5_title = "reacher"
        $ crab5_element = "water"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 20
            $ crab5_starting_att = 20
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 17

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*4)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*3)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 23
            $ crab5_starting_def = 23
            $ crab5_starting_acc = 26
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 24
            $ crab5_starting_att = 24
            $ crab5_starting_def = 24
            $ crab5_starting_acc = 27
            $ crab5_starting_ev = 21

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*7)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)



    if rand_crab5_type ==3:
        $ crab5_type = "3"
        $ crab5_title = "jacko"
        $ crab5_element = "earth"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 17
            $ crab5_starting_def = 17
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*3)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*3)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 26
            $ crab5_starting_att = 20
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 26
            $ crab5_starting_ev = 26

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 27
            $ crab5_starting_att = 21
            $ crab5_starting_def = 21
            $ crab5_starting_acc = 27
            $ crab5_starting_ev = 27

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*7)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*7)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*7)

    if rand_crab5_type ==4:
        $ crab5_type = "4"
        $ crab5_title = "julienne"
        $ crab5_element = "air"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 20
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 26
            $ crab5_starting_att = 23
            $ crab5_starting_def = 23
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 27
            $ crab5_starting_att = 24
            $ crab5_starting_def = 24
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 24

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*7)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)

    if rand_crab5_type ==5:
        $ crab5_type = "5"
        $ crab5_title = "slycer"
        $ crab5_element = "fire"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 17
            $ crab5_starting_att = 23
            $ crab5_starting_def = 17
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*3)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*3)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 20
            $ crab5_starting_att = 26
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*4)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 21
            $ crab5_starting_att = 27
            $ crab5_starting_def = 21
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 24

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*7)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)

    if rand_crab5_type ==6:
        $ crab5_type = "6"
        $ crab5_title = "clypper"
        $ crab5_element = "earth"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 20
            $ crab5_starting_att = 17
            $ crab5_starting_def = 23
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 17

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*4)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*3)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*3)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 20
            $ crab5_starting_def = 26
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 24
            $ crab5_starting_att = 21
            $ crab5_starting_def = 27
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 21

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*7)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

    if rand_crab5_type ==7:
        $ crab5_type = "7"
        $ crab5_title = "barnakel"
        $ crab5_element = "water"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 17
            $ crab5_starting_def = 26
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 17

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*3)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*3)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 26
            $ crab5_starting_att = 20
            $ crab5_starting_def = 29
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*7)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 27
            $ crab5_starting_att = 21
            $ crab5_starting_def = 30
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 21

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*7)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*8)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

    if rand_crab5_type ==8:
        $ crab5_type = "8"
        $ crab5_title = "doo'ahlai"
        $ crab5_element = "air"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 23
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 17

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*3)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 26
            $ crab5_starting_att = 26
            $ crab5_starting_def = 23
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 27
            $ crab5_starting_att = 27
            $ crab5_starting_def = 24
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 21

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*7)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*7)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

    if rand_crab5_type ==9:
        $ crab5_type = "9"
        $ crab5_title = "clawp"
        $ crab5_element = "water"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 20
            $ crab5_starting_att = 20
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*4)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 23
            $ crab5_starting_def = 23
            $ crab5_starting_acc = 23
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 24
            $ crab5_starting_att = 24
            $ crab5_starting_def = 24
            $ crab5_starting_acc = 24
            $ crab5_starting_ev = 24

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*6)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)

    if rand_crab5_type ==10:
        $ crab5_type = "10"
        $ crab5_title = "bampy"
        $ crab5_element = "earth"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 20
            $ crab5_starting_att = 17
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 17
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*4)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*3)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*3)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 20
            $ crab5_starting_def = 23
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 26

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*4)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 24
            $ crab5_starting_att = 21
            $ crab5_starting_def = 24
            $ crab5_starting_acc = 21
            $ crab5_starting_ev = 27

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*6)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*7)

    if rand_crab5_type ==11:
        $ crab5_type = "11"
        $ crab5_title = "grappy"
        $ crab5_element = "fire"
        if crab5_rarity == "n":
            $ crab5_starting_hp = 23
            $ crab5_starting_att = 23
            $ crab5_starting_def = 17
            $ crab5_starting_acc = 17
            $ crab5_starting_ev = 20

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*5)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*5)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*3)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*3)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*4)

        if crab5_rarity == "r":
            $ crab5_starting_hp = 26
            $ crab5_starting_att = 26
            $ crab5_starting_def = 20
            $ crab5_starting_acc = 20
            $ crab5_starting_ev = 23

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*6)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*6)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*4)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*4)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*5)

        if crab5_rarity == "e":
            $ crab5_starting_hp = 27
            $ crab5_starting_att = 27
            $ crab5_starting_def = 21
            $ crab5_starting_acc = 21
            $ crab5_starting_ev = 24

            $ crab5_hp = crab5_starting_hp + ((crab5_level-1)*7)
            $ crab5_att = crab5_starting_att + ((crab5_level-1)*7)
            $ crab5_def = crab5_starting_def + ((crab5_level-1)*5)
            $ crab5_acc = crab5_starting_acc + ((crab5_level-1)*5)
            $ crab5_ev = crab5_starting_ev + ((crab5_level-1)*6)
    show crab5_shuffle:
        ypos -200
    with flash

    if crab5_rarity =="n":
        "you got a normal {b}[crab5_title]{/b}!"
    if crab5_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab5_title]{/b}!"
    if crab5_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab5_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab5_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab5_name = crab5_name.strip()
            if crab5_name == "":
                $ crab5_name= crab5_title
            y "how about... [crab5_name]."
        "[crab5_title]":

            $ crab5_name = crab5_title

    jump after_crab_get

label crab6_trap_get:
    if rand_crab6_type ==1:
        $ crab6_type = "1"
        $ crab6_title = "slasher"
        $ crab6_element = "fire"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 20
            $ crab6_starting_att = 23
            $ crab6_starting_def = 17
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*4)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*3)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 26
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 24
            $ crab6_starting_att = 27
            $ crab6_starting_def = 21
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 24

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*7)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)



    if rand_crab6_type ==2:
        $ crab6_type = "2"
        $ crab6_title = "reacher"
        $ crab6_element = "water"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 20
            $ crab6_starting_att = 20
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 17

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*4)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*3)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 23
            $ crab6_starting_def = 23
            $ crab6_starting_acc = 26
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 24
            $ crab6_starting_att = 24
            $ crab6_starting_def = 24
            $ crab6_starting_acc = 27
            $ crab6_starting_ev = 21

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*7)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)



    if rand_crab6_type ==3:
        $ crab6_type = "3"
        $ crab6_title = "jacko"
        $ crab6_element = "earth"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 17
            $ crab6_starting_def = 17
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*3)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*3)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 26
            $ crab6_starting_att = 20
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 26
            $ crab6_starting_ev = 26

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 27
            $ crab6_starting_att = 21
            $ crab6_starting_def = 21
            $ crab6_starting_acc = 27
            $ crab6_starting_ev = 27

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*7)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*7)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*7)

    if rand_crab6_type ==4:
        $ crab6_type = "4"
        $ crab6_title = "julienne"
        $ crab6_element = "air"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 20
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 26
            $ crab6_starting_att = 23
            $ crab6_starting_def = 23
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 27
            $ crab6_starting_att = 24
            $ crab6_starting_def = 24
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 24

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*7)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)

    if rand_crab6_type ==5:
        $ crab6_type = "5"
        $ crab6_title = "slycer"
        $ crab6_element = "fire"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 17
            $ crab6_starting_att = 23
            $ crab6_starting_def = 17
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*3)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*3)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 20
            $ crab6_starting_att = 26
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*4)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 21
            $ crab6_starting_att = 27
            $ crab6_starting_def = 21
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 24

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*7)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)

    if rand_crab6_type ==6:
        $ crab6_type = "6"
        $ crab6_title = "clypper"
        $ crab6_element = "earth"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 20
            $ crab6_starting_att = 17
            $ crab6_starting_def = 23
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 17

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*4)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*3)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*3)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 20
            $ crab6_starting_def = 26
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 24
            $ crab6_starting_att = 21
            $ crab6_starting_def = 27
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 21

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*7)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

    if rand_crab6_type ==7:
        $ crab6_type = "7"
        $ crab6_title = "barnakel"
        $ crab6_element = "water"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 17
            $ crab6_starting_def = 26
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 17

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*3)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*3)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 26
            $ crab6_starting_att = 20
            $ crab6_starting_def = 29
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*7)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 27
            $ crab6_starting_att = 21
            $ crab6_starting_def = 30
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 21

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*7)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*8)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

    if rand_crab6_type ==8:
        $ crab6_type = "8"
        $ crab6_title = "doo'ahlai"
        $ crab6_element = "air"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 23
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 17

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*3)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 26
            $ crab6_starting_att = 26
            $ crab6_starting_def = 23
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 27
            $ crab6_starting_att = 27
            $ crab6_starting_def = 24
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 21

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*7)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*7)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

    if rand_crab6_type ==9:
        $ crab6_type = "9"
        $ crab6_title = "clawp"
        $ crab6_element = "water"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 20
            $ crab6_starting_att = 20
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*4)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 23
            $ crab6_starting_def = 23
            $ crab6_starting_acc = 23
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 24
            $ crab6_starting_att = 24
            $ crab6_starting_def = 24
            $ crab6_starting_acc = 24
            $ crab6_starting_ev = 24

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*6)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)

    if rand_crab6_type ==10:
        $ crab6_type = "10"
        $ crab6_title = "bampy"
        $ crab6_element = "earth"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 20
            $ crab6_starting_att = 17
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 17
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*4)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*3)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*3)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 20
            $ crab6_starting_def = 23
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 26

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*4)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 24
            $ crab6_starting_att = 21
            $ crab6_starting_def = 24
            $ crab6_starting_acc = 21
            $ crab6_starting_ev = 27

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*6)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*7)

    if rand_crab6_type ==11:
        $ crab6_type = "11"
        $ crab6_title = "grappy"
        $ crab6_element = "fire"
        if crab6_rarity == "n":
            $ crab6_starting_hp = 23
            $ crab6_starting_att = 23
            $ crab6_starting_def = 17
            $ crab6_starting_acc = 17
            $ crab6_starting_ev = 20

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*5)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*5)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*3)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*3)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*4)

        if crab6_rarity == "r":
            $ crab6_starting_hp = 26
            $ crab6_starting_att = 26
            $ crab6_starting_def = 20
            $ crab6_starting_acc = 20
            $ crab6_starting_ev = 23

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*6)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*6)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*4)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*4)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*5)

        if crab6_rarity == "e":
            $ crab6_starting_hp = 27
            $ crab6_starting_att = 27
            $ crab6_starting_def = 21
            $ crab6_starting_acc = 21
            $ crab6_starting_ev = 24

            $ crab6_hp = crab6_starting_hp + ((crab6_level-1)*7)
            $ crab6_att = crab6_starting_att + ((crab6_level-1)*7)
            $ crab6_def = crab6_starting_def + ((crab6_level-1)*5)
            $ crab6_acc = crab6_starting_acc + ((crab6_level-1)*5)
            $ crab6_ev = crab6_starting_ev + ((crab6_level-1)*6)
    show crab6_shuffle:
        ypos -200
    with flash

    if crab6_rarity =="n":
        "you got a normal {b}[crab6_title]{/b}!"
    if crab6_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab6_title]{/b}!"
    if crab6_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab6_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab6_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab6_name = crab6_name.strip()
            if crab6_name == "":
                $ crab6_name= crab6_title
            y "how about... [crab6_name]."
        "[crab6_title]":

            $ crab6_name = crab6_title

    jump after_crab_get

label crab7_trap_get:
    if rand_crab7_type ==1:
        $ crab7_type = "1"
        $ crab7_title = "slasher"
        $ crab7_element = "fire"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 20
            $ crab7_starting_att = 23
            $ crab7_starting_def = 17
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*4)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*3)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 26
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 24
            $ crab7_starting_att = 27
            $ crab7_starting_def = 21
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 24

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*7)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)



    if rand_crab7_type ==2:
        $ crab7_type = "2"
        $ crab7_title = "reacher"
        $ crab7_element = "water"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 20
            $ crab7_starting_att = 20
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 17

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*4)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*3)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 23
            $ crab7_starting_def = 23
            $ crab7_starting_acc = 26
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 24
            $ crab7_starting_att = 24
            $ crab7_starting_def = 24
            $ crab7_starting_acc = 27
            $ crab7_starting_ev = 21

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*7)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)



    if rand_crab7_type ==3:
        $ crab7_type = "3"
        $ crab7_title = "jacko"
        $ crab7_element = "earth"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 17
            $ crab7_starting_def = 17
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*3)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*3)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 26
            $ crab7_starting_att = 20
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 26
            $ crab7_starting_ev = 26

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 27
            $ crab7_starting_att = 21
            $ crab7_starting_def = 21
            $ crab7_starting_acc = 27
            $ crab7_starting_ev = 27

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*7)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*7)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*7)

    if rand_crab7_type ==4:
        $ crab7_type = "4"
        $ crab7_title = "julienne"
        $ crab7_element = "air"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 20
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 26
            $ crab7_starting_att = 23
            $ crab7_starting_def = 23
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 27
            $ crab7_starting_att = 24
            $ crab7_starting_def = 24
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 24

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*7)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)

    if rand_crab7_type ==5:
        $ crab7_type = "5"
        $ crab7_title = "slycer"
        $ crab7_element = "fire"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 17
            $ crab7_starting_att = 23
            $ crab7_starting_def = 17
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*3)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*3)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 20
            $ crab7_starting_att = 26
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*4)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 21
            $ crab7_starting_att = 27
            $ crab7_starting_def = 21
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 24

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*7)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)

    if rand_crab7_type ==6:
        $ crab7_type = "6"
        $ crab7_title = "clypper"
        $ crab7_element = "earth"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 20
            $ crab7_starting_att = 17
            $ crab7_starting_def = 23
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 17

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*4)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*3)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*3)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 20
            $ crab7_starting_def = 26
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 24
            $ crab7_starting_att = 21
            $ crab7_starting_def = 27
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 21

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*7)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

    if rand_crab7_type ==7:
        $ crab7_type = "7"
        $ crab7_title = "barnakel"
        $ crab7_element = "water"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 17
            $ crab7_starting_def = 26
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 17

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*3)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*3)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 26
            $ crab7_starting_att = 20
            $ crab7_starting_def = 29
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*7)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 27
            $ crab7_starting_att = 21
            $ crab7_starting_def = 30
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 21

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*7)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*8)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

    if rand_crab7_type ==8:
        $ crab7_type = "8"
        $ crab7_title = "doo'ahlai"
        $ crab7_element = "air"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 23
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 17

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*3)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 26
            $ crab7_starting_att = 26
            $ crab7_starting_def = 23
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 27
            $ crab7_starting_att = 27
            $ crab7_starting_def = 24
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 21

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*7)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*7)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

    if rand_crab7_type ==9:
        $ crab7_type = "9"
        $ crab7_title = "clawp"
        $ crab7_element = "water"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 20
            $ crab7_starting_att = 20
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*4)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 23
            $ crab7_starting_def = 23
            $ crab7_starting_acc = 23
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 24
            $ crab7_starting_att = 24
            $ crab7_starting_def = 24
            $ crab7_starting_acc = 24
            $ crab7_starting_ev = 24

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*6)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)

    if rand_crab7_type ==10:
        $ crab7_type = "10"
        $ crab7_title = "bampy"
        $ crab7_element = "earth"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 20
            $ crab7_starting_att = 17
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 17
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*4)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*3)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*3)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 20
            $ crab7_starting_def = 23
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 26

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*4)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 24
            $ crab7_starting_att = 21
            $ crab7_starting_def = 24
            $ crab7_starting_acc = 21
            $ crab7_starting_ev = 27

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*6)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*7)

    if rand_crab7_type ==11:
        $ crab7_type = "11"
        $ crab7_title = "grappy"
        $ crab7_element = "fire"
        if crab7_rarity == "n":
            $ crab7_starting_hp = 23
            $ crab7_starting_att = 23
            $ crab7_starting_def = 17
            $ crab7_starting_acc = 17
            $ crab7_starting_ev = 20

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*5)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*5)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*3)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*3)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*4)

        if crab7_rarity == "r":
            $ crab7_starting_hp = 26
            $ crab7_starting_att = 26
            $ crab7_starting_def = 20
            $ crab7_starting_acc = 20
            $ crab7_starting_ev = 23

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*6)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*6)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*4)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*4)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*5)

        if crab7_rarity == "e":
            $ crab7_starting_hp = 27
            $ crab7_starting_att = 27
            $ crab7_starting_def = 21
            $ crab7_starting_acc = 21
            $ crab7_starting_ev = 24

            $ crab7_hp = crab7_starting_hp + ((crab7_level-1)*7)
            $ crab7_att = crab7_starting_att + ((crab7_level-1)*7)
            $ crab7_def = crab7_starting_def + ((crab7_level-1)*5)
            $ crab7_acc = crab7_starting_acc + ((crab7_level-1)*5)
            $ crab7_ev = crab7_starting_ev + ((crab7_level-1)*6)
    show crab7_shuffle:
        ypos -200
    with flash

    if crab7_rarity =="n":
        "you got a normal {b}[crab7_title]{/b}!"
    if crab7_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab7_title]{/b}!"
    if crab7_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab7_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab7_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab7_name = crab7_name.strip()
            if crab7_name == "":
                $ crab7_name= crab7_title
            y "how about... [crab7_name]."
        "[crab7_title]":

            $ crab7_name = crab7_title

    jump after_crab_get

label crab8_trap_get:
    if rand_crab8_type ==1:
        $ crab8_type = "1"
        $ crab8_title = "slasher"
        $ crab8_element = "fire"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 20
            $ crab8_starting_att = 23
            $ crab8_starting_def = 17
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*4)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*3)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 26
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 24
            $ crab8_starting_att = 27
            $ crab8_starting_def = 21
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 24

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*7)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)



    if rand_crab8_type ==2:
        $ crab8_type = "2"
        $ crab8_title = "reacher"
        $ crab8_element = "water"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 20
            $ crab8_starting_att = 20
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 17

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*4)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*3)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 23
            $ crab8_starting_def = 23
            $ crab8_starting_acc = 26
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 24
            $ crab8_starting_att = 24
            $ crab8_starting_def = 24
            $ crab8_starting_acc = 27
            $ crab8_starting_ev = 21

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*7)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)



    if rand_crab8_type ==3:
        $ crab8_type = "3"
        $ crab8_title = "jacko"
        $ crab8_element = "earth"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 17
            $ crab8_starting_def = 17
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*3)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*3)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 26
            $ crab8_starting_att = 20
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 26
            $ crab8_starting_ev = 26

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 27
            $ crab8_starting_att = 21
            $ crab8_starting_def = 21
            $ crab8_starting_acc = 27
            $ crab8_starting_ev = 27

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*7)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*7)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*7)

    if rand_crab8_type ==4:
        $ crab8_type = "4"
        $ crab8_title = "julienne"
        $ crab8_element = "air"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 20
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 26
            $ crab8_starting_att = 23
            $ crab8_starting_def = 23
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 27
            $ crab8_starting_att = 24
            $ crab8_starting_def = 24
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 24

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*7)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)

    if rand_crab8_type ==5:
        $ crab8_type = "5"
        $ crab8_title = "slycer"
        $ crab8_element = "fire"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 17
            $ crab8_starting_att = 23
            $ crab8_starting_def = 17
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*3)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*3)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 20
            $ crab8_starting_att = 26
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*4)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 21
            $ crab8_starting_att = 27
            $ crab8_starting_def = 21
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 24

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*7)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)

    if rand_crab8_type ==6:
        $ crab8_type = "6"
        $ crab8_title = "clypper"
        $ crab8_element = "earth"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 20
            $ crab8_starting_att = 17
            $ crab8_starting_def = 23
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 17

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*4)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*3)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*3)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 20
            $ crab8_starting_def = 26
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 24
            $ crab8_starting_att = 21
            $ crab8_starting_def = 27
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 21

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*7)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

    if rand_crab8_type ==7:
        $ crab8_type = "7"
        $ crab8_title = "barnakel"
        $ crab8_element = "water"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 17
            $ crab8_starting_def = 26
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 17

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*3)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*3)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 26
            $ crab8_starting_att = 20
            $ crab8_starting_def = 29
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*7)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 27
            $ crab8_starting_att = 21
            $ crab8_starting_def = 30
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 21

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*7)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*8)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

    if rand_crab8_type ==8:
        $ crab8_type = "8"
        $ crab8_title = "doo'ahlai"
        $ crab8_element = "air"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 23
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 17

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*3)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 26
            $ crab8_starting_att = 26
            $ crab8_starting_def = 23
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 27
            $ crab8_starting_att = 27
            $ crab8_starting_def = 24
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 21

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*7)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*7)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

    if rand_crab8_type ==9:
        $ crab8_type = "9"
        $ crab8_title = "clawp"
        $ crab8_element = "water"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 20
            $ crab8_starting_att = 20
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*4)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 23
            $ crab8_starting_def = 23
            $ crab8_starting_acc = 23
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 24
            $ crab8_starting_att = 24
            $ crab8_starting_def = 24
            $ crab8_starting_acc = 24
            $ crab8_starting_ev = 24

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*6)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)

    if rand_crab8_type ==10:
        $ crab8_type = "10"
        $ crab8_title = "bampy"
        $ crab8_element = "earth"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 20
            $ crab8_starting_att = 17
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 17
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*4)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*3)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*3)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 20
            $ crab8_starting_def = 23
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 26

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*4)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 24
            $ crab8_starting_att = 21
            $ crab8_starting_def = 24
            $ crab8_starting_acc = 21
            $ crab8_starting_ev = 27

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*6)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*7)

    if rand_crab8_type ==11:
        $ crab8_type = "11"
        $ crab8_title = "grappy"
        $ crab8_element = "fire"
        if crab8_rarity == "n":
            $ crab8_starting_hp = 23
            $ crab8_starting_att = 23
            $ crab8_starting_def = 17
            $ crab8_starting_acc = 17
            $ crab8_starting_ev = 20

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*5)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*5)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*3)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*3)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*4)

        if crab8_rarity == "r":
            $ crab8_starting_hp = 26
            $ crab8_starting_att = 26
            $ crab8_starting_def = 20
            $ crab8_starting_acc = 20
            $ crab8_starting_ev = 23

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*6)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*6)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*4)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*4)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*5)

        if crab8_rarity == "e":
            $ crab8_starting_hp = 27
            $ crab8_starting_att = 27
            $ crab8_starting_def = 21
            $ crab8_starting_acc = 21
            $ crab8_starting_ev = 24

            $ crab8_hp = crab8_starting_hp + ((crab8_level-1)*7)
            $ crab8_att = crab8_starting_att + ((crab8_level-1)*7)
            $ crab8_def = crab8_starting_def + ((crab8_level-1)*5)
            $ crab8_acc = crab8_starting_acc + ((crab8_level-1)*5)
            $ crab8_ev = crab8_starting_ev + ((crab8_level-1)*6)
    show crab8_shuffle:
        ypos -200
    with flash

    if crab8_rarity =="n":
        "you got a normal {b}[crab8_title]{/b}!"
    if crab8_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab8_title]{/b}!"
    if crab8_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab8_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab8_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab8_name = crab8_name.strip()
            if crab8_name == "":
                $ crab8_name= crab8_title
            y "how about... [crab8_name]."
        "[crab8_title]":

            $ crab8_name = crab8_title

    jump after_crab_get

label crab9_trap_get:
    if rand_crab9_type ==1:
        $ crab9_type = "1"
        $ crab9_title = "slasher"
        $ crab9_element = "fire"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 20
            $ crab9_starting_att = 23
            $ crab9_starting_def = 17
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*4)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*3)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 26
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 24
            $ crab9_starting_att = 27
            $ crab9_starting_def = 21
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 24

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*7)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)



    if rand_crab9_type ==2:
        $ crab9_type = "2"
        $ crab9_title = "reacher"
        $ crab9_element = "water"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 20
            $ crab9_starting_att = 20
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 17

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*4)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*3)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 23
            $ crab9_starting_def = 23
            $ crab9_starting_acc = 26
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 24
            $ crab9_starting_att = 24
            $ crab9_starting_def = 24
            $ crab9_starting_acc = 27
            $ crab9_starting_ev = 21

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*7)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)



    if rand_crab9_type ==3:
        $ crab9_type = "3"
        $ crab9_title = "jacko"
        $ crab9_element = "earth"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 17
            $ crab9_starting_def = 17
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*3)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*3)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 26
            $ crab9_starting_att = 20
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 26
            $ crab9_starting_ev = 26

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 27
            $ crab9_starting_att = 21
            $ crab9_starting_def = 21
            $ crab9_starting_acc = 27
            $ crab9_starting_ev = 27

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*7)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*7)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*7)

    if rand_crab9_type ==4:
        $ crab9_type = "4"
        $ crab9_title = "julienne"
        $ crab9_element = "air"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 20
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 26
            $ crab9_starting_att = 23
            $ crab9_starting_def = 23
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 27
            $ crab9_starting_att = 24
            $ crab9_starting_def = 24
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 24

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*7)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)

    if rand_crab9_type ==5:
        $ crab9_type = "5"
        $ crab9_title = "slycer"
        $ crab9_element = "fire"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 17
            $ crab9_starting_att = 23
            $ crab9_starting_def = 17
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*3)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*3)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 20
            $ crab9_starting_att = 26
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*4)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 21
            $ crab9_starting_att = 27
            $ crab9_starting_def = 21
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 24

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*7)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)

    if rand_crab9_type ==6:
        $ crab9_type = "6"
        $ crab9_title = "clypper"
        $ crab9_element = "earth"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 20
            $ crab9_starting_att = 17
            $ crab9_starting_def = 23
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 17

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*4)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*3)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*3)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 20
            $ crab9_starting_def = 26
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 24
            $ crab9_starting_att = 21
            $ crab9_starting_def = 27
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 21

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*7)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

    if rand_crab9_type ==7:
        $ crab9_type = "7"
        $ crab9_title = "barnakel"
        $ crab9_element = "water"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 17
            $ crab9_starting_def = 26
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 17

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*3)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*3)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 26
            $ crab9_starting_att = 20
            $ crab9_starting_def = 29
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*7)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 27
            $ crab9_starting_att = 21
            $ crab9_starting_def = 30
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 21

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*7)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*8)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

    if rand_crab9_type ==8:
        $ crab9_type = "8"
        $ crab9_title = "doo'ahlai"
        $ crab9_element = "air"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 23
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 17

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*3)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 26
            $ crab9_starting_att = 26
            $ crab9_starting_def = 23
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 27
            $ crab9_starting_att = 27
            $ crab9_starting_def = 24
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 21

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*7)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*7)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

    if rand_crab9_type ==9:
        $ crab9_type = "9"
        $ crab9_title = "clawp"
        $ crab9_element = "water"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 20
            $ crab9_starting_att = 20
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*4)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 23
            $ crab9_starting_def = 23
            $ crab9_starting_acc = 23
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 24
            $ crab9_starting_att = 24
            $ crab9_starting_def = 24
            $ crab9_starting_acc = 24
            $ crab9_starting_ev = 24

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*6)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)

    if rand_crab9_type ==10:
        $ crab9_type = "10"
        $ crab9_title = "bampy"
        $ crab9_element = "earth"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 20
            $ crab9_starting_att = 17
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 17
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*4)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*3)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*3)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 20
            $ crab9_starting_def = 23
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 26

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*4)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 24
            $ crab9_starting_att = 21
            $ crab9_starting_def = 24
            $ crab9_starting_acc = 21
            $ crab9_starting_ev = 27

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*6)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*7)

    if rand_crab9_type ==11:
        $ crab9_type = "11"
        $ crab9_title = "grappy"
        $ crab9_element = "fire"
        if crab9_rarity == "n":
            $ crab9_starting_hp = 23
            $ crab9_starting_att = 23
            $ crab9_starting_def = 17
            $ crab9_starting_acc = 17
            $ crab9_starting_ev = 20

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*5)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*5)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*3)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*3)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*4)

        if crab9_rarity == "r":
            $ crab9_starting_hp = 26
            $ crab9_starting_att = 26
            $ crab9_starting_def = 20
            $ crab9_starting_acc = 20
            $ crab9_starting_ev = 23

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*6)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*6)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*4)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*4)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*5)

        if crab9_rarity == "e":
            $ crab9_starting_hp = 27
            $ crab9_starting_att = 27
            $ crab9_starting_def = 21
            $ crab9_starting_acc = 21
            $ crab9_starting_ev = 24

            $ crab9_hp = crab9_starting_hp + ((crab9_level-1)*7)
            $ crab9_att = crab9_starting_att + ((crab9_level-1)*7)
            $ crab9_def = crab9_starting_def + ((crab9_level-1)*5)
            $ crab9_acc = crab9_starting_acc + ((crab9_level-1)*5)
            $ crab9_ev = crab9_starting_ev + ((crab9_level-1)*6)
    show crab9_shuffle:
        ypos -200
    with flash

    if crab9_rarity =="n":
        "you got a normal {b}[crab9_title]{/b}!"
    if crab9_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab9_title]{/b}!"
    if crab9_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab9_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab9_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab9_name = crab9_name.strip()
            if crab9_name == "":
                $ crab9_name= crab9_title
            y "how about... [crab9_name]."
        "[crab9_title]":

            $ crab9_name = crab9_title

    jump after_crab_get

label crab10_trap_get:
    if rand_crab10_type ==1:
        $ crab10_type = "1"
        $ crab10_title = "slasher"
        $ crab10_element = "fire"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 20
            $ crab10_starting_att = 23
            $ crab10_starting_def = 17
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*4)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*3)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 26
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 24
            $ crab10_starting_att = 27
            $ crab10_starting_def = 21
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 24

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*7)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)



    if rand_crab10_type ==2:
        $ crab10_type = "2"
        $ crab10_title = "reacher"
        $ crab10_element = "water"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 20
            $ crab10_starting_att = 20
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 17

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*4)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*3)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 23
            $ crab10_starting_def = 23
            $ crab10_starting_acc = 26
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 24
            $ crab10_starting_att = 24
            $ crab10_starting_def = 24
            $ crab10_starting_acc = 27
            $ crab10_starting_ev = 21

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*7)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)



    if rand_crab10_type ==3:
        $ crab10_type = "3"
        $ crab10_title = "jacko"
        $ crab10_element = "earth"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 17
            $ crab10_starting_def = 17
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*3)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*3)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 26
            $ crab10_starting_att = 20
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 26
            $ crab10_starting_ev = 26

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 27
            $ crab10_starting_att = 21
            $ crab10_starting_def = 21
            $ crab10_starting_acc = 27
            $ crab10_starting_ev = 27

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*7)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*7)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*7)

    if rand_crab10_type ==4:
        $ crab10_type = "4"
        $ crab10_title = "julienne"
        $ crab10_element = "air"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 20
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 26
            $ crab10_starting_att = 23
            $ crab10_starting_def = 23
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 27
            $ crab10_starting_att = 24
            $ crab10_starting_def = 24
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 24

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*7)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)

    if rand_crab10_type ==5:
        $ crab10_type = "5"
        $ crab10_title = "slycer"
        $ crab10_element = "fire"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 17
            $ crab10_starting_att = 23
            $ crab10_starting_def = 17
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*3)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*3)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 20
            $ crab10_starting_att = 26
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*4)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 21
            $ crab10_starting_att = 27
            $ crab10_starting_def = 21
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 24

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*7)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)

    if rand_crab10_type ==6:
        $ crab10_type = "6"
        $ crab10_title = "clypper"
        $ crab10_element = "earth"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 20
            $ crab10_starting_att = 17
            $ crab10_starting_def = 23
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 17

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*4)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*3)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*3)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 20
            $ crab10_starting_def = 26
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 24
            $ crab10_starting_att = 21
            $ crab10_starting_def = 27
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 21

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*7)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

    if rand_crab10_type ==7:
        $ crab10_type = "7"
        $ crab10_title = "barnakel"
        $ crab10_element = "water"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 17
            $ crab10_starting_def = 26
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 17

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*3)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*3)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 26
            $ crab10_starting_att = 20
            $ crab10_starting_def = 29
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*7)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 27
            $ crab10_starting_att = 21
            $ crab10_starting_def = 30
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 21

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*7)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*8)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

    if rand_crab10_type ==8:
        $ crab10_type = "8"
        $ crab10_title = "doo'ahlai"
        $ crab10_element = "air"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 23
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 17

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*3)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 26
            $ crab10_starting_att = 26
            $ crab10_starting_def = 23
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 27
            $ crab10_starting_att = 27
            $ crab10_starting_def = 24
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 21

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*7)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*7)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

    if rand_crab10_type ==9:
        $ crab10_type = "9"
        $ crab10_title = "clawp"
        $ crab10_element = "water"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 20
            $ crab10_starting_att = 20
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*4)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 23
            $ crab10_starting_def = 23
            $ crab10_starting_acc = 23
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 24
            $ crab10_starting_att = 24
            $ crab10_starting_def = 24
            $ crab10_starting_acc = 24
            $ crab10_starting_ev = 24

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*6)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)

    if rand_crab10_type ==10:
        $ crab10_type = "10"
        $ crab10_title = "bampy"
        $ crab10_element = "earth"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 20
            $ crab10_starting_att = 17
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 17
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*4)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*3)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*3)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 20
            $ crab10_starting_def = 23
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 26

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*4)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 24
            $ crab10_starting_att = 21
            $ crab10_starting_def = 24
            $ crab10_starting_acc = 21
            $ crab10_starting_ev = 27

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*6)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*7)

    if rand_crab10_type ==11:
        $ crab10_type = "11"
        $ crab10_title = "grappy"
        $ crab10_element = "fire"
        if crab10_rarity == "n":
            $ crab10_starting_hp = 23
            $ crab10_starting_att = 23
            $ crab10_starting_def = 17
            $ crab10_starting_acc = 17
            $ crab10_starting_ev = 20

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*5)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*5)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*3)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*3)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*4)

        if crab10_rarity == "r":
            $ crab10_starting_hp = 26
            $ crab10_starting_att = 26
            $ crab10_starting_def = 20
            $ crab10_starting_acc = 20
            $ crab10_starting_ev = 23

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*6)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*6)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*4)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*4)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*5)

        if crab10_rarity == "e":
            $ crab10_starting_hp = 27
            $ crab10_starting_att = 27
            $ crab10_starting_def = 21
            $ crab10_starting_acc = 21
            $ crab10_starting_ev = 24

            $ crab10_hp = crab10_starting_hp + ((crab10_level-1)*7)
            $ crab10_att = crab10_starting_att + ((crab10_level-1)*7)
            $ crab10_def = crab10_starting_def + ((crab10_level-1)*5)
            $ crab10_acc = crab10_starting_acc + ((crab10_level-1)*5)
            $ crab10_ev = crab10_starting_ev + ((crab10_level-1)*6)
    show crab10_shuffle:
        ypos -200
    with flash

    if crab10_rarity =="n":
        "you got a normal {b}[crab10_title]{/b}!"
    if crab10_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab10_title]{/b}!"
    if crab10_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab10_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab10_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab10_name = crab10_name.strip()
            if crab10_name == "":
                $ crab10_name= crab10_title
            y "how about... [crab10_name]."
        "[crab10_title]":

            $ crab10_name = crab10_title

    jump after_crab_get

label crab11_trap_get:
    if rand_crab11_type ==1:
        $ crab11_type = "1"
        $ crab11_title = "slasher"
        $ crab11_element = "fire"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 20
            $ crab11_starting_att = 23
            $ crab11_starting_def = 17
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*4)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*3)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 26
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 24
            $ crab11_starting_att = 27
            $ crab11_starting_def = 21
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 24

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*7)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)



    if rand_crab11_type ==2:
        $ crab11_type = "2"
        $ crab11_title = "reacher"
        $ crab11_element = "water"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 20
            $ crab11_starting_att = 20
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 17

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*4)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*3)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 23
            $ crab11_starting_def = 23
            $ crab11_starting_acc = 26
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 24
            $ crab11_starting_att = 24
            $ crab11_starting_def = 24
            $ crab11_starting_acc = 27
            $ crab11_starting_ev = 21

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*7)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)



    if rand_crab11_type ==3:
        $ crab11_type = "3"
        $ crab11_title = "jacko"
        $ crab11_element = "earth"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 17
            $ crab11_starting_def = 17
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*3)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*3)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 26
            $ crab11_starting_att = 20
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 26
            $ crab11_starting_ev = 26

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 27
            $ crab11_starting_att = 21
            $ crab11_starting_def = 21
            $ crab11_starting_acc = 27
            $ crab11_starting_ev = 27

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*7)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*7)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*7)

    if rand_crab11_type ==4:
        $ crab11_type = "4"
        $ crab11_title = "julienne"
        $ crab11_element = "air"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 20
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 26
            $ crab11_starting_att = 23
            $ crab11_starting_def = 23
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 27
            $ crab11_starting_att = 24
            $ crab11_starting_def = 24
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 24

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*7)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)

    if rand_crab11_type ==5:
        $ crab11_type = "5"
        $ crab11_title = "slycer"
        $ crab11_element = "fire"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 17
            $ crab11_starting_att = 23
            $ crab11_starting_def = 17
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*3)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*3)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 20
            $ crab11_starting_att = 26
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*4)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 21
            $ crab11_starting_att = 27
            $ crab11_starting_def = 21
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 24

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*7)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)

    if rand_crab11_type ==6:
        $ crab11_type = "6"
        $ crab11_title = "clypper"
        $ crab11_element = "earth"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 20
            $ crab11_starting_att = 17
            $ crab11_starting_def = 23
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 17

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*4)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*3)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*3)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 20
            $ crab11_starting_def = 26
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 24
            $ crab11_starting_att = 21
            $ crab11_starting_def = 27
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 21

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*7)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

    if rand_crab11_type ==7:
        $ crab11_type = "7"
        $ crab11_title = "barnakel"
        $ crab11_element = "water"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 17
            $ crab11_starting_def = 26
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 17

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*3)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*3)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 26
            $ crab11_starting_att = 20
            $ crab11_starting_def = 29
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*7)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 27
            $ crab11_starting_att = 21
            $ crab11_starting_def = 30
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 21

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*7)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*8)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

    if rand_crab11_type ==8:
        $ crab11_type = "8"
        $ crab11_title = "doo'ahlai"
        $ crab11_element = "air"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 23
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 17

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*3)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 26
            $ crab11_starting_att = 26
            $ crab11_starting_def = 23
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 27
            $ crab11_starting_att = 27
            $ crab11_starting_def = 24
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 21

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*7)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*7)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

    if rand_crab11_type ==9:
        $ crab11_type = "9"
        $ crab11_title = "clawp"
        $ crab11_element = "water"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 20
            $ crab11_starting_att = 20
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*4)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 23
            $ crab11_starting_def = 23
            $ crab11_starting_acc = 23
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 24
            $ crab11_starting_att = 24
            $ crab11_starting_def = 24
            $ crab11_starting_acc = 24
            $ crab11_starting_ev = 24

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*6)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)

    if rand_crab11_type ==10:
        $ crab11_type = "10"
        $ crab11_title = "bampy"
        $ crab11_element = "earth"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 20
            $ crab11_starting_att = 17
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 17
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*4)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*3)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*3)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 20
            $ crab11_starting_def = 23
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 26

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*4)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 24
            $ crab11_starting_att = 21
            $ crab11_starting_def = 24
            $ crab11_starting_acc = 21
            $ crab11_starting_ev = 27

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*6)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*7)

    if rand_crab11_type ==11:
        $ crab11_type = "11"
        $ crab11_title = "grappy"
        $ crab11_element = "fire"
        if crab11_rarity == "n":
            $ crab11_starting_hp = 23
            $ crab11_starting_att = 23
            $ crab11_starting_def = 17
            $ crab11_starting_acc = 17
            $ crab11_starting_ev = 20

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*5)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*5)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*3)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*3)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*4)

        if crab11_rarity == "r":
            $ crab11_starting_hp = 26
            $ crab11_starting_att = 26
            $ crab11_starting_def = 20
            $ crab11_starting_acc = 20
            $ crab11_starting_ev = 23

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*6)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*6)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*4)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*4)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*5)

        if crab11_rarity == "e":
            $ crab11_starting_hp = 27
            $ crab11_starting_att = 27
            $ crab11_starting_def = 21
            $ crab11_starting_acc = 21
            $ crab11_starting_ev = 24

            $ crab11_hp = crab11_starting_hp + ((crab11_level-1)*7)
            $ crab11_att = crab11_starting_att + ((crab11_level-1)*7)
            $ crab11_def = crab11_starting_def + ((crab11_level-1)*5)
            $ crab11_acc = crab11_starting_acc + ((crab11_level-1)*5)
            $ crab11_ev = crab11_starting_ev + ((crab11_level-1)*6)
    show crab11_shuffle:
        ypos -200
    with flash

    if crab11_rarity =="n":
        "you got a normal {b}[crab11_title]{/b}!"
    if crab11_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab11_title]{/b}!"
    if crab11_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab11_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab11_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab11_name = crab11_name.strip()
            if crab11_name == "":
                $ crab11_name= crab11_title
            y "how about... [crab11_name]."
        "[crab11_title]":

            $ crab11_name = crab11_title

    jump after_crab_get

label crab12_trap_get:
    if rand_crab12_type ==1:
        $ crab12_type = "1"
        $ crab12_title = "slasher"
        $ crab12_element = "fire"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 20
            $ crab12_starting_att = 23
            $ crab12_starting_def = 17
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*4)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*3)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 26
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 24
            $ crab12_starting_att = 27
            $ crab12_starting_def = 21
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 24

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*7)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)



    if rand_crab12_type ==2:
        $ crab12_type = "2"
        $ crab12_title = "reacher"
        $ crab12_element = "water"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 20
            $ crab12_starting_att = 20
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 17

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*4)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*3)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 23
            $ crab12_starting_def = 23
            $ crab12_starting_acc = 26
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 24
            $ crab12_starting_att = 24
            $ crab12_starting_def = 24
            $ crab12_starting_acc = 27
            $ crab12_starting_ev = 21

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*7)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)



    if rand_crab12_type ==3:
        $ crab12_type = "3"
        $ crab12_title = "jacko"
        $ crab12_element = "earth"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 17
            $ crab12_starting_def = 17
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*3)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*3)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 26
            $ crab12_starting_att = 20
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 26
            $ crab12_starting_ev = 26

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 27
            $ crab12_starting_att = 21
            $ crab12_starting_def = 21
            $ crab12_starting_acc = 27
            $ crab12_starting_ev = 27

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*7)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*7)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*7)

    if rand_crab12_type ==4:
        $ crab12_type = "4"
        $ crab12_title = "julienne"
        $ crab12_element = "air"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 20
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 26
            $ crab12_starting_att = 23
            $ crab12_starting_def = 23
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 27
            $ crab12_starting_att = 24
            $ crab12_starting_def = 24
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 24

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*7)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)

    if rand_crab12_type ==5:
        $ crab12_type = "5"
        $ crab12_title = "slycer"
        $ crab12_element = "fire"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 17
            $ crab12_starting_att = 23
            $ crab12_starting_def = 17
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*3)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*3)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 20
            $ crab12_starting_att = 26
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*4)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 21
            $ crab12_starting_att = 27
            $ crab12_starting_def = 21
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 24

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*7)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)

    if rand_crab12_type ==6:
        $ crab12_type = "6"
        $ crab12_title = "clypper"
        $ crab12_element = "earth"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 20
            $ crab12_starting_att = 17
            $ crab12_starting_def = 23
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 17

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*4)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*3)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*3)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 20
            $ crab12_starting_def = 26
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 24
            $ crab12_starting_att = 21
            $ crab12_starting_def = 27
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 21

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*7)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

    if rand_crab12_type ==7:
        $ crab12_type = "7"
        $ crab12_title = "barnakel"
        $ crab12_element = "water"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 17
            $ crab12_starting_def = 26
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 17

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*3)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*3)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 26
            $ crab12_starting_att = 20
            $ crab12_starting_def = 29
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*7)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 27
            $ crab12_starting_att = 21
            $ crab12_starting_def = 30
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 21

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*7)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*8)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

    if rand_crab12_type ==8:
        $ crab12_type = "8"
        $ crab12_title = "doo'ahlai"
        $ crab12_element = "air"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 23
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 17

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*3)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 26
            $ crab12_starting_att = 26
            $ crab12_starting_def = 23
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 27
            $ crab12_starting_att = 27
            $ crab12_starting_def = 24
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 21

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*7)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*7)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

    if rand_crab12_type ==9:
        $ crab12_type = "9"
        $ crab12_title = "clawp"
        $ crab12_element = "water"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 20
            $ crab12_starting_att = 20
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*4)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 23
            $ crab12_starting_def = 23
            $ crab12_starting_acc = 23
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 24
            $ crab12_starting_att = 24
            $ crab12_starting_def = 24
            $ crab12_starting_acc = 24
            $ crab12_starting_ev = 24

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*6)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)

    if rand_crab12_type ==10:
        $ crab12_type = "10"
        $ crab12_title = "bampy"
        $ crab12_element = "earth"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 20
            $ crab12_starting_att = 17
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 17
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*4)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*3)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*3)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 20
            $ crab12_starting_def = 23
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 26

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*4)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 24
            $ crab12_starting_att = 21
            $ crab12_starting_def = 24
            $ crab12_starting_acc = 21
            $ crab12_starting_ev = 27

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*6)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*7)

    if rand_crab12_type ==11:
        $ crab12_type = "11"
        $ crab12_title = "grappy"
        $ crab12_element = "fire"
        if crab12_rarity == "n":
            $ crab12_starting_hp = 23
            $ crab12_starting_att = 23
            $ crab12_starting_def = 17
            $ crab12_starting_acc = 17
            $ crab12_starting_ev = 20

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*5)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*5)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*3)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*3)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*4)

        if crab12_rarity == "r":
            $ crab12_starting_hp = 26
            $ crab12_starting_att = 26
            $ crab12_starting_def = 20
            $ crab12_starting_acc = 20
            $ crab12_starting_ev = 23

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*6)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*6)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*4)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*4)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*5)

        if crab12_rarity == "e":
            $ crab12_starting_hp = 27
            $ crab12_starting_att = 27
            $ crab12_starting_def = 21
            $ crab12_starting_acc = 21
            $ crab12_starting_ev = 24

            $ crab12_hp = crab12_starting_hp + ((crab12_level-1)*7)
            $ crab12_att = crab12_starting_att + ((crab12_level-1)*7)
            $ crab12_def = crab12_starting_def + ((crab12_level-1)*5)
            $ crab12_acc = crab12_starting_acc + ((crab12_level-1)*5)
            $ crab12_ev = crab12_starting_ev + ((crab12_level-1)*6)
    show crab12_shuffle:
        ypos -200
    with flash

    if crab12_rarity =="n":
        "you got a normal {b}[crab12_title]{/b}!"
    if crab12_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab12_title]{/b}!"
    if crab12_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab12_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab12_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab12_name = crab12_name.strip()
            if crab12_name == "":
                $ crab12_name= crab12_title
            y "how about... [crab12_name]."
        "[crab12_title]":

            $ crab12_name = crab12_title

    jump after_crab_get

label crab13_trap_get:
    if rand_crab13_type ==1:
        $ crab13_type = "1"
        $ crab13_title = "slasher"
        $ crab13_element = "fire"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 20
            $ crab13_starting_att = 23
            $ crab13_starting_def = 17
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*4)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*3)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 26
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 24
            $ crab13_starting_att = 27
            $ crab13_starting_def = 21
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 24

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*7)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)



    if rand_crab13_type ==2:
        $ crab13_type = "2"
        $ crab13_title = "reacher"
        $ crab13_element = "water"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 20
            $ crab13_starting_att = 20
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 17

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*4)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*3)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 23
            $ crab13_starting_def = 23
            $ crab13_starting_acc = 26
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 24
            $ crab13_starting_att = 24
            $ crab13_starting_def = 24
            $ crab13_starting_acc = 27
            $ crab13_starting_ev = 21

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*7)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)



    if rand_crab13_type ==3:
        $ crab13_type = "3"
        $ crab13_title = "jacko"
        $ crab13_element = "earth"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 17
            $ crab13_starting_def = 17
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*3)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*3)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 26
            $ crab13_starting_att = 20
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 26
            $ crab13_starting_ev = 26

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 27
            $ crab13_starting_att = 21
            $ crab13_starting_def = 21
            $ crab13_starting_acc = 27
            $ crab13_starting_ev = 27

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*7)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*7)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*7)

    if rand_crab13_type ==4:
        $ crab13_type = "4"
        $ crab13_title = "julienne"
        $ crab13_element = "air"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 20
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 26
            $ crab13_starting_att = 23
            $ crab13_starting_def = 23
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 27
            $ crab13_starting_att = 24
            $ crab13_starting_def = 24
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 24

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*7)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)

    if rand_crab13_type ==5:
        $ crab13_type = "5"
        $ crab13_title = "slycer"
        $ crab13_element = "fire"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 17
            $ crab13_starting_att = 23
            $ crab13_starting_def = 17
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*3)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*3)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 20
            $ crab13_starting_att = 26
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*4)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 21
            $ crab13_starting_att = 27
            $ crab13_starting_def = 21
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 24

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*7)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)

    if rand_crab13_type ==6:
        $ crab13_type = "6"
        $ crab13_title = "clypper"
        $ crab13_element = "earth"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 20
            $ crab13_starting_att = 17
            $ crab13_starting_def = 23
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 17

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*4)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*3)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*3)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 20
            $ crab13_starting_def = 26
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 24
            $ crab13_starting_att = 21
            $ crab13_starting_def = 27
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 21

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*7)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

    if rand_crab13_type ==7:
        $ crab13_type = "7"
        $ crab13_title = "barnakel"
        $ crab13_element = "water"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 17
            $ crab13_starting_def = 26
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 17

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*3)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*3)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 26
            $ crab13_starting_att = 20
            $ crab13_starting_def = 29
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*7)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 27
            $ crab13_starting_att = 21
            $ crab13_starting_def = 30
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 21

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*7)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*8)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

    if rand_crab13_type ==8:
        $ crab13_type = "8"
        $ crab13_title = "doo'ahlai"
        $ crab13_element = "air"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 23
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 17

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*3)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 26
            $ crab13_starting_att = 26
            $ crab13_starting_def = 23
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 27
            $ crab13_starting_att = 27
            $ crab13_starting_def = 24
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 21

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*7)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*7)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

    if rand_crab13_type ==9:
        $ crab13_type = "9"
        $ crab13_title = "clawp"
        $ crab13_element = "water"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 20
            $ crab13_starting_att = 20
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*4)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 23
            $ crab13_starting_def = 23
            $ crab13_starting_acc = 23
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 24
            $ crab13_starting_att = 24
            $ crab13_starting_def = 24
            $ crab13_starting_acc = 24
            $ crab13_starting_ev = 24

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*6)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)

    if rand_crab13_type ==10:
        $ crab13_type = "10"
        $ crab13_title = "bampy"
        $ crab13_element = "earth"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 20
            $ crab13_starting_att = 17
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 17
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*4)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*3)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*3)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 20
            $ crab13_starting_def = 23
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 26

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*4)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 24
            $ crab13_starting_att = 21
            $ crab13_starting_def = 24
            $ crab13_starting_acc = 21
            $ crab13_starting_ev = 27

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*6)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*7)

    if rand_crab13_type ==11:
        $ crab13_type = "11"
        $ crab13_title = "grappy"
        $ crab13_element = "fire"
        if crab13_rarity == "n":
            $ crab13_starting_hp = 23
            $ crab13_starting_att = 23
            $ crab13_starting_def = 17
            $ crab13_starting_acc = 17
            $ crab13_starting_ev = 20

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*5)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*5)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*3)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*3)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*4)

        if crab13_rarity == "r":
            $ crab13_starting_hp = 26
            $ crab13_starting_att = 26
            $ crab13_starting_def = 20
            $ crab13_starting_acc = 20
            $ crab13_starting_ev = 23

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*6)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*6)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*4)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*4)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*5)

        if crab13_rarity == "e":
            $ crab13_starting_hp = 27
            $ crab13_starting_att = 27
            $ crab13_starting_def = 21
            $ crab13_starting_acc = 21
            $ crab13_starting_ev = 24

            $ crab13_hp = crab13_starting_hp + ((crab13_level-1)*7)
            $ crab13_att = crab13_starting_att + ((crab13_level-1)*7)
            $ crab13_def = crab13_starting_def + ((crab13_level-1)*5)
            $ crab13_acc = crab13_starting_acc + ((crab13_level-1)*5)
            $ crab13_ev = crab13_starting_ev + ((crab13_level-1)*6)
    show crab13_shuffle:
        ypos -200
    with flash

    if crab13_rarity =="n":
        "you got a normal {b}[crab13_title]{/b}!"
    if crab13_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab13_title]{/b}!"
    if crab13_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab13_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab13_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab13_name = crab13_name.strip()
            if crab13_name == "":
                $ crab13_name= crab13_title
            y "how about... [crab13_name]."
        "[crab13_title]":

            $ crab13_name = crab13_title

    jump after_crab_get

label crab14_trap_get:
    if rand_crab14_type ==1:
        $ crab14_type = "1"
        $ crab14_title = "slasher"
        $ crab14_element = "fire"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 20
            $ crab14_starting_att = 23
            $ crab14_starting_def = 17
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*4)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*3)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 26
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 24
            $ crab14_starting_att = 27
            $ crab14_starting_def = 21
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 24

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*7)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)



    if rand_crab14_type ==2:
        $ crab14_type = "2"
        $ crab14_title = "reacher"
        $ crab14_element = "water"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 20
            $ crab14_starting_att = 20
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 17

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*4)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*3)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 23
            $ crab14_starting_def = 23
            $ crab14_starting_acc = 26
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 24
            $ crab14_starting_att = 24
            $ crab14_starting_def = 24
            $ crab14_starting_acc = 27
            $ crab14_starting_ev = 21

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*7)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)



    if rand_crab14_type ==3:
        $ crab14_type = "3"
        $ crab14_title = "jacko"
        $ crab14_element = "earth"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 17
            $ crab14_starting_def = 17
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*3)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*3)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 26
            $ crab14_starting_att = 20
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 26
            $ crab14_starting_ev = 26

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 27
            $ crab14_starting_att = 21
            $ crab14_starting_def = 21
            $ crab14_starting_acc = 27
            $ crab14_starting_ev = 27

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*7)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*7)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*7)

    if rand_crab14_type ==4:
        $ crab14_type = "4"
        $ crab14_title = "julienne"
        $ crab14_element = "air"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 20
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 26
            $ crab14_starting_att = 23
            $ crab14_starting_def = 23
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 27
            $ crab14_starting_att = 24
            $ crab14_starting_def = 24
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 24

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*7)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)

    if rand_crab14_type ==5:
        $ crab14_type = "5"
        $ crab14_title = "slycer"
        $ crab14_element = "fire"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 17
            $ crab14_starting_att = 23
            $ crab14_starting_def = 17
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*3)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*3)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 20
            $ crab14_starting_att = 26
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*4)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 21
            $ crab14_starting_att = 27
            $ crab14_starting_def = 21
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 24

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*7)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)

    if rand_crab14_type ==6:
        $ crab14_type = "6"
        $ crab14_title = "clypper"
        $ crab14_element = "earth"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 20
            $ crab14_starting_att = 17
            $ crab14_starting_def = 23
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 17

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*4)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*3)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*3)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 20
            $ crab14_starting_def = 26
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 24
            $ crab14_starting_att = 21
            $ crab14_starting_def = 27
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 21

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*7)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

    if rand_crab14_type ==7:
        $ crab14_type = "7"
        $ crab14_title = "barnakel"
        $ crab14_element = "water"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 17
            $ crab14_starting_def = 26
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 17

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*3)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*3)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 26
            $ crab14_starting_att = 20
            $ crab14_starting_def = 29
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*7)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 27
            $ crab14_starting_att = 21
            $ crab14_starting_def = 30
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 21

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*7)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*8)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

    if rand_crab14_type ==8:
        $ crab14_type = "8"
        $ crab14_title = "doo'ahlai"
        $ crab14_element = "air"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 23
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 17

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*3)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 26
            $ crab14_starting_att = 26
            $ crab14_starting_def = 23
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 27
            $ crab14_starting_att = 27
            $ crab14_starting_def = 24
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 21

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*7)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*7)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

    if rand_crab14_type ==9:
        $ crab14_type = "9"
        $ crab14_title = "clawp"
        $ crab14_element = "water"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 20
            $ crab14_starting_att = 20
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*4)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 23
            $ crab14_starting_def = 23
            $ crab14_starting_acc = 23
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 24
            $ crab14_starting_att = 24
            $ crab14_starting_def = 24
            $ crab14_starting_acc = 24
            $ crab14_starting_ev = 24

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*6)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)

    if rand_crab14_type ==10:
        $ crab14_type = "10"
        $ crab14_title = "bampy"
        $ crab14_element = "earth"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 20
            $ crab14_starting_att = 17
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 17
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*4)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*3)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*3)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 20
            $ crab14_starting_def = 23
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 26

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*4)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 24
            $ crab14_starting_att = 21
            $ crab14_starting_def = 24
            $ crab14_starting_acc = 21
            $ crab14_starting_ev = 27

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*6)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*7)

    if rand_crab14_type ==11:
        $ crab14_type = "11"
        $ crab14_title = "grappy"
        $ crab14_element = "fire"
        if crab14_rarity == "n":
            $ crab14_starting_hp = 23
            $ crab14_starting_att = 23
            $ crab14_starting_def = 17
            $ crab14_starting_acc = 17
            $ crab14_starting_ev = 20

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*5)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*5)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*3)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*3)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*4)

        if crab14_rarity == "r":
            $ crab14_starting_hp = 26
            $ crab14_starting_att = 26
            $ crab14_starting_def = 20
            $ crab14_starting_acc = 20
            $ crab14_starting_ev = 23

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*6)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*6)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*4)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*4)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*5)

        if crab14_rarity == "e":
            $ crab14_starting_hp = 27
            $ crab14_starting_att = 27
            $ crab14_starting_def = 21
            $ crab14_starting_acc = 21
            $ crab14_starting_ev = 24

            $ crab14_hp = crab14_starting_hp + ((crab14_level-1)*7)
            $ crab14_att = crab14_starting_att + ((crab14_level-1)*7)
            $ crab14_def = crab14_starting_def + ((crab14_level-1)*5)
            $ crab14_acc = crab14_starting_acc + ((crab14_level-1)*5)
            $ crab14_ev = crab14_starting_ev + ((crab14_level-1)*6)
    show crab14_shuffle:
        ypos -200
    with flash

    if crab14_rarity =="n":
        "you got a normal {b}[crab14_title]{/b}!"
    if crab14_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab14_title]{/b}!"
    if crab14_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab14_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab14_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab14_name = crab14_name.strip()
            if crab14_name == "":
                $ crab14_name= crab14_title
            y "how about... [crab14_name]."
        "[crab14_title]":

            $ crab14_name = crab14_title

    jump after_crab_get

label crab15_trap_get:
    if rand_crab15_type ==1:
        $ crab15_type = "1"
        $ crab15_title = "slasher"
        $ crab15_element = "fire"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 20
            $ crab15_starting_att = 23
            $ crab15_starting_def = 17
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*4)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*3)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 26
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 24
            $ crab15_starting_att = 27
            $ crab15_starting_def = 21
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 24

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*7)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)



    if rand_crab15_type ==2:
        $ crab15_type = "2"
        $ crab15_title = "reacher"
        $ crab15_element = "water"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 20
            $ crab15_starting_att = 20
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 17

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*4)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*3)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 23
            $ crab15_starting_def = 23
            $ crab15_starting_acc = 26
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 24
            $ crab15_starting_att = 24
            $ crab15_starting_def = 24
            $ crab15_starting_acc = 27
            $ crab15_starting_ev = 21

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*7)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)



    if rand_crab15_type ==3:
        $ crab15_type = "3"
        $ crab15_title = "jacko"
        $ crab15_element = "earth"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 17
            $ crab15_starting_def = 17
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*3)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*3)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 26
            $ crab15_starting_att = 20
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 26
            $ crab15_starting_ev = 26

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 27
            $ crab15_starting_att = 21
            $ crab15_starting_def = 21
            $ crab15_starting_acc = 27
            $ crab15_starting_ev = 27

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*7)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*7)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*7)

    if rand_crab15_type ==4:
        $ crab15_type = "4"
        $ crab15_title = "julienne"
        $ crab15_element = "air"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 20
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 26
            $ crab15_starting_att = 23
            $ crab15_starting_def = 23
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 27
            $ crab15_starting_att = 24
            $ crab15_starting_def = 24
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 24

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*7)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)

    if rand_crab15_type ==5:
        $ crab15_type = "5"
        $ crab15_title = "slycer"
        $ crab15_element = "fire"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 17
            $ crab15_starting_att = 23
            $ crab15_starting_def = 17
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*3)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*3)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 20
            $ crab15_starting_att = 26
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*4)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 21
            $ crab15_starting_att = 27
            $ crab15_starting_def = 21
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 24

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*7)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)

    if rand_crab15_type ==6:
        $ crab15_type = "6"
        $ crab15_title = "clypper"
        $ crab15_element = "earth"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 20
            $ crab15_starting_att = 17
            $ crab15_starting_def = 23
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 17

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*4)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*3)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*3)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 20
            $ crab15_starting_def = 26
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 24
            $ crab15_starting_att = 21
            $ crab15_starting_def = 27
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 21

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*7)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

    if rand_crab15_type ==7:
        $ crab15_type = "7"
        $ crab15_title = "barnakel"
        $ crab15_element = "water"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 17
            $ crab15_starting_def = 26
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 17

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*3)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*3)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 26
            $ crab15_starting_att = 20
            $ crab15_starting_def = 29
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*7)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 27
            $ crab15_starting_att = 21
            $ crab15_starting_def = 30
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 21

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*7)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*8)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

    if rand_crab15_type ==8:
        $ crab15_type = "8"
        $ crab15_title = "doo'ahlai"
        $ crab15_element = "air"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 23
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 17

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*3)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 26
            $ crab15_starting_att = 26
            $ crab15_starting_def = 23
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 27
            $ crab15_starting_att = 27
            $ crab15_starting_def = 24
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 21

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*7)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*7)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

    if rand_crab15_type ==9:
        $ crab15_type = "9"
        $ crab15_title = "clawp"
        $ crab15_element = "water"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 20
            $ crab15_starting_att = 20
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*4)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 23
            $ crab15_starting_def = 23
            $ crab15_starting_acc = 23
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 24
            $ crab15_starting_att = 24
            $ crab15_starting_def = 24
            $ crab15_starting_acc = 24
            $ crab15_starting_ev = 24

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*6)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)

    if rand_crab15_type ==10:
        $ crab15_type = "10"
        $ crab15_title = "bampy"
        $ crab15_element = "earth"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 20
            $ crab15_starting_att = 17
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 17
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*4)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*3)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*3)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 20
            $ crab15_starting_def = 23
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 26

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*4)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 24
            $ crab15_starting_att = 21
            $ crab15_starting_def = 24
            $ crab15_starting_acc = 21
            $ crab15_starting_ev = 27

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*6)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*7)

    if rand_crab15_type ==11:
        $ crab15_type = "11"
        $ crab15_title = "grappy"
        $ crab15_element = "fire"
        if crab15_rarity == "n":
            $ crab15_starting_hp = 23
            $ crab15_starting_att = 23
            $ crab15_starting_def = 17
            $ crab15_starting_acc = 17
            $ crab15_starting_ev = 20

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*5)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*5)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*3)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*3)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*4)

        if crab15_rarity == "r":
            $ crab15_starting_hp = 26
            $ crab15_starting_att = 26
            $ crab15_starting_def = 20
            $ crab15_starting_acc = 20
            $ crab15_starting_ev = 23

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*6)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*6)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*4)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*4)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*5)

        if crab15_rarity == "e":
            $ crab15_starting_hp = 27
            $ crab15_starting_att = 27
            $ crab15_starting_def = 21
            $ crab15_starting_acc = 21
            $ crab15_starting_ev = 24

            $ crab15_hp = crab15_starting_hp + ((crab15_level-1)*7)
            $ crab15_att = crab15_starting_att + ((crab15_level-1)*7)
            $ crab15_def = crab15_starting_def + ((crab15_level-1)*5)
            $ crab15_acc = crab15_starting_acc + ((crab15_level-1)*5)
            $ crab15_ev = crab15_starting_ev + ((crab15_level-1)*6)
    show crab15_shuffle:
        ypos -200
    with flash

    if crab15_rarity =="n":
        "you got a normal {b}[crab15_title]{/b}!"
    if crab15_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab15_title]{/b}!"
    if crab15_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab15_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab15_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab15_name = crab15_name.strip()
            if crab15_name == "":
                $ crab15_name= crab15_title
            y "how about... [crab15_name]."
        "[crab15_title]":

            $ crab15_name = crab15_title
    jump after_crab_get

label crab16_trap_get:
    if rand_crab16_type ==1:
        $ crab16_type = "1"
        $ crab16_title = "slasher"
        $ crab16_element = "fire"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 20
            $ crab16_starting_att = 23
            $ crab16_starting_def = 17
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*4)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*3)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 26
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 24
            $ crab16_starting_att = 27
            $ crab16_starting_def = 21
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 24

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*7)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)



    if rand_crab16_type ==2:
        $ crab16_type = "2"
        $ crab16_title = "reacher"
        $ crab16_element = "water"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 20
            $ crab16_starting_att = 20
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 17

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*4)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*3)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 23
            $ crab16_starting_def = 23
            $ crab16_starting_acc = 26
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 24
            $ crab16_starting_att = 24
            $ crab16_starting_def = 24
            $ crab16_starting_acc = 27
            $ crab16_starting_ev = 21

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*7)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)



    if rand_crab16_type ==3:
        $ crab16_type = "3"
        $ crab16_title = "jacko"
        $ crab16_element = "earth"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 17
            $ crab16_starting_def = 17
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*3)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*3)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 26
            $ crab16_starting_att = 20
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 26
            $ crab16_starting_ev = 26

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 27
            $ crab16_starting_att = 21
            $ crab16_starting_def = 21
            $ crab16_starting_acc = 27
            $ crab16_starting_ev = 27

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*7)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*7)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*7)

    if rand_crab16_type ==4:
        $ crab16_type = "4"
        $ crab16_title = "julienne"
        $ crab16_element = "air"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 20
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 26
            $ crab16_starting_att = 23
            $ crab16_starting_def = 23
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 27
            $ crab16_starting_att = 24
            $ crab16_starting_def = 24
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 24

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*7)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)

    if rand_crab16_type ==5:
        $ crab16_type = "5"
        $ crab16_title = "slycer"
        $ crab16_element = "fire"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 17
            $ crab16_starting_att = 23
            $ crab16_starting_def = 17
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*3)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*3)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 20
            $ crab16_starting_att = 26
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*4)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 21
            $ crab16_starting_att = 27
            $ crab16_starting_def = 21
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 24

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*7)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)

    if rand_crab16_type ==6:
        $ crab16_type = "6"
        $ crab16_title = "clypper"
        $ crab16_element = "earth"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 20
            $ crab16_starting_att = 17
            $ crab16_starting_def = 23
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 17

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*4)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*3)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*3)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 20
            $ crab16_starting_def = 26
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 24
            $ crab16_starting_att = 21
            $ crab16_starting_def = 27
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 21

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*7)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

    if rand_crab16_type ==7:
        $ crab16_type = "7"
        $ crab16_title = "barnakel"
        $ crab16_element = "water"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 17
            $ crab16_starting_def = 26
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 17

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*3)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*3)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 26
            $ crab16_starting_att = 20
            $ crab16_starting_def = 29
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*7)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 27
            $ crab16_starting_att = 21
            $ crab16_starting_def = 30
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 21

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*7)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*8)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

    if rand_crab16_type ==8:
        $ crab16_type = "8"
        $ crab16_title = "doo'ahlai"
        $ crab16_element = "air"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 23
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 17

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*3)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 26
            $ crab16_starting_att = 26
            $ crab16_starting_def = 23
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 27
            $ crab16_starting_att = 27
            $ crab16_starting_def = 24
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 21

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*7)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*7)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

    if rand_crab16_type ==9:
        $ crab16_type = "9"
        $ crab16_title = "clawp"
        $ crab16_element = "water"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 20
            $ crab16_starting_att = 20
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*4)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 23
            $ crab16_starting_def = 23
            $ crab16_starting_acc = 23
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 24
            $ crab16_starting_att = 24
            $ crab16_starting_def = 24
            $ crab16_starting_acc = 24
            $ crab16_starting_ev = 24

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*6)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)

    if rand_crab16_type ==10:
        $ crab16_type = "10"
        $ crab16_title = "bampy"
        $ crab16_element = "earth"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 20
            $ crab16_starting_att = 17
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 17
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*4)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*3)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*3)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 20
            $ crab16_starting_def = 23
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 26

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*4)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 24
            $ crab16_starting_att = 21
            $ crab16_starting_def = 24
            $ crab16_starting_acc = 21
            $ crab16_starting_ev = 27

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*6)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*7)

    if rand_crab16_type ==11:
        $ crab16_type = "11"
        $ crab16_title = "grappy"
        $ crab16_element = "fire"
        if crab16_rarity == "n":
            $ crab16_starting_hp = 23
            $ crab16_starting_att = 23
            $ crab16_starting_def = 17
            $ crab16_starting_acc = 17
            $ crab16_starting_ev = 20

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*5)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*5)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*3)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*3)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*4)

        if crab16_rarity == "r":
            $ crab16_starting_hp = 26
            $ crab16_starting_att = 26
            $ crab16_starting_def = 20
            $ crab16_starting_acc = 20
            $ crab16_starting_ev = 23

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*6)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*6)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*4)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*4)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*5)

        if crab16_rarity == "e":
            $ crab16_starting_hp = 27
            $ crab16_starting_att = 27
            $ crab16_starting_def = 21
            $ crab16_starting_acc = 21
            $ crab16_starting_ev = 24

            $ crab16_hp = crab16_starting_hp + ((crab16_level-1)*7)
            $ crab16_att = crab16_starting_att + ((crab16_level-1)*7)
            $ crab16_def = crab16_starting_def + ((crab16_level-1)*5)
            $ crab16_acc = crab16_starting_acc + ((crab16_level-1)*5)
            $ crab16_ev = crab16_starting_ev + ((crab16_level-1)*6)
    show crab16_shuffle:
        ypos -200
    with flash

    if crab16_rarity =="n":
        "you got a normal {b}[crab16_title]{/b}!"
    if crab16_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab16_title]{/b}!"
    if crab16_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab16_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab16_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab16_name = crab16_name.strip()
            if crab16_name == "":
                $ crab16_name= crab16_title
            y "how about... [crab16_name]."
        "[crab16_title]":

            $ crab16_name = crab16_title

    jump after_crab_get

label crab17_trap_get:
    if rand_crab17_type ==1:
        $ crab17_type = "1"
        $ crab17_title = "slasher"
        $ crab17_element = "fire"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 20
            $ crab17_starting_att = 23
            $ crab17_starting_def = 17
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*4)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*3)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 26
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 24
            $ crab17_starting_att = 27
            $ crab17_starting_def = 21
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 24

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*7)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)



    if rand_crab17_type ==2:
        $ crab17_type = "2"
        $ crab17_title = "reacher"
        $ crab17_element = "water"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 20
            $ crab17_starting_att = 20
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 17

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*4)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*3)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 23
            $ crab17_starting_def = 23
            $ crab17_starting_acc = 26
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 24
            $ crab17_starting_att = 24
            $ crab17_starting_def = 24
            $ crab17_starting_acc = 27
            $ crab17_starting_ev = 21

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*7)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)



    if rand_crab17_type ==3:
        $ crab17_type = "3"
        $ crab17_title = "jacko"
        $ crab17_element = "earth"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 17
            $ crab17_starting_def = 17
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*3)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*3)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 26
            $ crab17_starting_att = 20
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 26
            $ crab17_starting_ev = 26

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 27
            $ crab17_starting_att = 21
            $ crab17_starting_def = 21
            $ crab17_starting_acc = 27
            $ crab17_starting_ev = 27

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*7)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*7)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*7)

    if rand_crab17_type ==4:
        $ crab17_type = "4"
        $ crab17_title = "julienne"
        $ crab17_element = "air"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 20
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 26
            $ crab17_starting_att = 23
            $ crab17_starting_def = 23
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 27
            $ crab17_starting_att = 24
            $ crab17_starting_def = 24
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 24

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*7)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)

    if rand_crab17_type ==5:
        $ crab17_type = "5"
        $ crab17_title = "slycer"
        $ crab17_element = "fire"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 17
            $ crab17_starting_att = 23
            $ crab17_starting_def = 17
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*3)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*3)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 20
            $ crab17_starting_att = 26
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*4)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 21
            $ crab17_starting_att = 27
            $ crab17_starting_def = 21
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 24

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*7)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)

    if rand_crab17_type ==6:
        $ crab17_type = "6"
        $ crab17_title = "clypper"
        $ crab17_element = "earth"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 20
            $ crab17_starting_att = 17
            $ crab17_starting_def = 23
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 17

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*4)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*3)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*3)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 20
            $ crab17_starting_def = 26
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 24
            $ crab17_starting_att = 21
            $ crab17_starting_def = 27
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 21

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*7)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

    if rand_crab17_type ==7:
        $ crab17_type = "7"
        $ crab17_title = "barnakel"
        $ crab17_element = "water"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 17
            $ crab17_starting_def = 26
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 17

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*3)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*3)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 26
            $ crab17_starting_att = 20
            $ crab17_starting_def = 29
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*7)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 27
            $ crab17_starting_att = 21
            $ crab17_starting_def = 30
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 21

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*7)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*8)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

    if rand_crab17_type ==8:
        $ crab17_type = "8"
        $ crab17_title = "doo'ahlai"
        $ crab17_element = "air"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 23
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 17

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*3)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 26
            $ crab17_starting_att = 26
            $ crab17_starting_def = 23
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 27
            $ crab17_starting_att = 27
            $ crab17_starting_def = 24
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 21

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*7)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*7)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

    if rand_crab17_type ==9:
        $ crab17_type = "9"
        $ crab17_title = "clawp"
        $ crab17_element = "water"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 20
            $ crab17_starting_att = 20
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*4)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 23
            $ crab17_starting_def = 23
            $ crab17_starting_acc = 23
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 24
            $ crab17_starting_att = 24
            $ crab17_starting_def = 24
            $ crab17_starting_acc = 24
            $ crab17_starting_ev = 24

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*6)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)

    if rand_crab17_type ==10:
        $ crab17_type = "10"
        $ crab17_title = "bampy"
        $ crab17_element = "earth"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 20
            $ crab17_starting_att = 17
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 17
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*4)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*3)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*3)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 20
            $ crab17_starting_def = 23
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 26

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*4)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 24
            $ crab17_starting_att = 21
            $ crab17_starting_def = 24
            $ crab17_starting_acc = 21
            $ crab17_starting_ev = 27

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*6)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*7)

    if rand_crab17_type ==11:
        $ crab17_type = "11"
        $ crab17_title = "grappy"
        $ crab17_element = "fire"
        if crab17_rarity == "n":
            $ crab17_starting_hp = 23
            $ crab17_starting_att = 23
            $ crab17_starting_def = 17
            $ crab17_starting_acc = 17
            $ crab17_starting_ev = 20

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*5)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*5)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*3)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*3)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*4)

        if crab17_rarity == "r":
            $ crab17_starting_hp = 26
            $ crab17_starting_att = 26
            $ crab17_starting_def = 20
            $ crab17_starting_acc = 20
            $ crab17_starting_ev = 23

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*6)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*6)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*4)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*4)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*5)

        if crab17_rarity == "e":
            $ crab17_starting_hp = 27
            $ crab17_starting_att = 27
            $ crab17_starting_def = 21
            $ crab17_starting_acc = 21
            $ crab17_starting_ev = 24

            $ crab17_hp = crab17_starting_hp + ((crab17_level-1)*7)
            $ crab17_att = crab17_starting_att + ((crab17_level-1)*7)
            $ crab17_def = crab17_starting_def + ((crab17_level-1)*5)
            $ crab17_acc = crab17_starting_acc + ((crab17_level-1)*5)
            $ crab17_ev = crab17_starting_ev + ((crab17_level-1)*6)
    show crab17_shuffle:
        ypos -200
    with flash

    if crab17_rarity =="n":
        "you got a normal {b}[crab17_title]{/b}!"
    if crab17_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab17_title]{/b}!"
    if crab17_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab17_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab17_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab17_name = crab17_name.strip()
            if crab17_name == "":
                $ crab17_name= crab17_title
            y "how about... [crab17_name]."
        "[crab17_title]":

            $ crab17_name = crab17_title

    jump after_crab_get

label crab18_trap_get:
    if rand_crab18_type ==1:
        $ crab18_type = "1"
        $ crab18_title = "slasher"
        $ crab18_element = "fire"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 20
            $ crab18_starting_att = 23
            $ crab18_starting_def = 17
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*4)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*3)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 26
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 24
            $ crab18_starting_att = 27
            $ crab18_starting_def = 21
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 24

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*7)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)



    if rand_crab18_type ==2:
        $ crab18_type = "2"
        $ crab18_title = "reacher"
        $ crab18_element = "water"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 20
            $ crab18_starting_att = 20
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 17

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*4)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*3)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 23
            $ crab18_starting_def = 23
            $ crab18_starting_acc = 26
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 24
            $ crab18_starting_att = 24
            $ crab18_starting_def = 24
            $ crab18_starting_acc = 27
            $ crab18_starting_ev = 21

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*7)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)



    if rand_crab18_type ==3:
        $ crab18_type = "3"
        $ crab18_title = "jacko"
        $ crab18_element = "earth"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 17
            $ crab18_starting_def = 17
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*3)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*3)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 26
            $ crab18_starting_att = 20
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 26
            $ crab18_starting_ev = 26

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 27
            $ crab18_starting_att = 21
            $ crab18_starting_def = 21
            $ crab18_starting_acc = 27
            $ crab18_starting_ev = 27

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*7)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*7)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*7)

    if rand_crab18_type ==4:
        $ crab18_type = "4"
        $ crab18_title = "julienne"
        $ crab18_element = "air"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 20
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 26
            $ crab18_starting_att = 23
            $ crab18_starting_def = 23
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 27
            $ crab18_starting_att = 24
            $ crab18_starting_def = 24
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 24

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*7)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)

    if rand_crab18_type ==5:
        $ crab18_type = "5"
        $ crab18_title = "slycer"
        $ crab18_element = "fire"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 17
            $ crab18_starting_att = 23
            $ crab18_starting_def = 17
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*3)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*3)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 20
            $ crab18_starting_att = 26
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*4)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 21
            $ crab18_starting_att = 27
            $ crab18_starting_def = 21
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 24

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*7)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)

    if rand_crab18_type ==6:
        $ crab18_type = "6"
        $ crab18_title = "clypper"
        $ crab18_element = "earth"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 20
            $ crab18_starting_att = 17
            $ crab18_starting_def = 23
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 17

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*4)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*3)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*3)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 20
            $ crab18_starting_def = 26
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 24
            $ crab18_starting_att = 21
            $ crab18_starting_def = 27
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 21

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*7)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

    if rand_crab18_type ==7:
        $ crab18_type = "7"
        $ crab18_title = "barnakel"
        $ crab18_element = "water"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 17
            $ crab18_starting_def = 26
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 17

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*3)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*3)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 26
            $ crab18_starting_att = 20
            $ crab18_starting_def = 29
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*7)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 27
            $ crab18_starting_att = 21
            $ crab18_starting_def = 30
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 21

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*7)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*8)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

    if rand_crab18_type ==8:
        $ crab18_type = "8"
        $ crab18_title = "doo'ahlai"
        $ crab18_element = "air"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 23
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 17

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*3)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 26
            $ crab18_starting_att = 26
            $ crab18_starting_def = 23
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 27
            $ crab18_starting_att = 27
            $ crab18_starting_def = 24
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 21

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*7)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*7)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

    if rand_crab18_type ==9:
        $ crab18_type = "9"
        $ crab18_title = "clawp"
        $ crab18_element = "water"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 20
            $ crab18_starting_att = 20
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*4)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 23
            $ crab18_starting_def = 23
            $ crab18_starting_acc = 23
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 24
            $ crab18_starting_att = 24
            $ crab18_starting_def = 24
            $ crab18_starting_acc = 24
            $ crab18_starting_ev = 24

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*6)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)

    if rand_crab18_type ==10:
        $ crab18_type = "10"
        $ crab18_title = "bampy"
        $ crab18_element = "earth"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 20
            $ crab18_starting_att = 17
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 17
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*4)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*3)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*3)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 20
            $ crab18_starting_def = 23
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 26

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*4)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 24
            $ crab18_starting_att = 21
            $ crab18_starting_def = 24
            $ crab18_starting_acc = 21
            $ crab18_starting_ev = 27

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*6)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*7)

    if rand_crab18_type ==11:
        $ crab18_type = "11"
        $ crab18_title = "grappy"
        $ crab18_element = "fire"
        if crab18_rarity == "n":
            $ crab18_starting_hp = 23
            $ crab18_starting_att = 23
            $ crab18_starting_def = 17
            $ crab18_starting_acc = 17
            $ crab18_starting_ev = 20

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*5)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*5)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*3)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*3)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*4)

        if crab18_rarity == "r":
            $ crab18_starting_hp = 26
            $ crab18_starting_att = 26
            $ crab18_starting_def = 20
            $ crab18_starting_acc = 20
            $ crab18_starting_ev = 23

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*6)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*6)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*4)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*4)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*5)

        if crab18_rarity == "e":
            $ crab18_starting_hp = 27
            $ crab18_starting_att = 27
            $ crab18_starting_def = 21
            $ crab18_starting_acc = 21
            $ crab18_starting_ev = 24

            $ crab18_hp = crab18_starting_hp + ((crab18_level-1)*7)
            $ crab18_att = crab18_starting_att + ((crab18_level-1)*7)
            $ crab18_def = crab18_starting_def + ((crab18_level-1)*5)
            $ crab18_acc = crab18_starting_acc + ((crab18_level-1)*5)
            $ crab18_ev = crab18_starting_ev + ((crab18_level-1)*6)
    show crab18_shuffle:
        ypos -200
    with flash

    if crab18_rarity =="n":
        "you got a normal {b}[crab18_title]{/b}!"
    if crab18_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab18_title]{/b}!"
    if crab18_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab18_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab18_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab18_name = crab18_name.strip()
            if crab18_name == "":
                $ crab18_name= crab18_title
            y "how about... [crab18_name]."
        "[crab18_title]":

            $ crab18_name = crab18_title

    jump after_crab_get

label crab19_trap_get:
    if rand_crab19_type ==1:
        $ crab19_type = "1"
        $ crab19_title = "slasher"
        $ crab19_element = "fire"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 20
            $ crab19_starting_att = 23
            $ crab19_starting_def = 17
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*4)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*3)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 26
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 24
            $ crab19_starting_att = 27
            $ crab19_starting_def = 21
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 24

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*7)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)



    if rand_crab19_type ==2:
        $ crab19_type = "2"
        $ crab19_title = "reacher"
        $ crab19_element = "water"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 20
            $ crab19_starting_att = 20
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 17

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*4)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*3)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 23
            $ crab19_starting_def = 23
            $ crab19_starting_acc = 26
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 24
            $ crab19_starting_att = 24
            $ crab19_starting_def = 24
            $ crab19_starting_acc = 27
            $ crab19_starting_ev = 21

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*7)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)



    if rand_crab19_type ==3:
        $ crab19_type = "3"
        $ crab19_title = "jacko"
        $ crab19_element = "earth"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 17
            $ crab19_starting_def = 17
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*3)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*3)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 26
            $ crab19_starting_att = 20
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 26
            $ crab19_starting_ev = 26

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 27
            $ crab19_starting_att = 21
            $ crab19_starting_def = 21
            $ crab19_starting_acc = 27
            $ crab19_starting_ev = 27

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*7)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*7)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*7)

    if rand_crab19_type ==4:
        $ crab19_type = "4"
        $ crab19_title = "julienne"
        $ crab19_element = "air"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 20
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 26
            $ crab19_starting_att = 23
            $ crab19_starting_def = 23
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 27
            $ crab19_starting_att = 24
            $ crab19_starting_def = 24
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 24

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*7)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)

    if rand_crab19_type ==5:
        $ crab19_type = "5"
        $ crab19_title = "slycer"
        $ crab19_element = "fire"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 17
            $ crab19_starting_att = 23
            $ crab19_starting_def = 17
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*3)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*3)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 20
            $ crab19_starting_att = 26
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*4)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 21
            $ crab19_starting_att = 27
            $ crab19_starting_def = 21
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 24

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*7)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)

    if rand_crab19_type ==6:
        $ crab19_type = "6"
        $ crab19_title = "clypper"
        $ crab19_element = "earth"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 20
            $ crab19_starting_att = 17
            $ crab19_starting_def = 23
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 17

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*4)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*3)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*3)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 20
            $ crab19_starting_def = 26
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 24
            $ crab19_starting_att = 21
            $ crab19_starting_def = 27
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 21

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*7)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

    if rand_crab19_type ==7:
        $ crab19_type = "7"
        $ crab19_title = "barnakel"
        $ crab19_element = "water"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 17
            $ crab19_starting_def = 26
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 17

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*3)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*3)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 26
            $ crab19_starting_att = 20
            $ crab19_starting_def = 29
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*7)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 27
            $ crab19_starting_att = 21
            $ crab19_starting_def = 30
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 21

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*7)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*8)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

    if rand_crab19_type ==8:
        $ crab19_type = "8"
        $ crab19_title = "doo'ahlai"
        $ crab19_element = "air"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 23
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 17

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*3)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 26
            $ crab19_starting_att = 26
            $ crab19_starting_def = 23
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 27
            $ crab19_starting_att = 27
            $ crab19_starting_def = 24
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 21

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*7)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*7)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

    if rand_crab19_type ==9:
        $ crab19_type = "9"
        $ crab19_title = "clawp"
        $ crab19_element = "water"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 20
            $ crab19_starting_att = 20
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*4)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 23
            $ crab19_starting_def = 23
            $ crab19_starting_acc = 23
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 24
            $ crab19_starting_att = 24
            $ crab19_starting_def = 24
            $ crab19_starting_acc = 24
            $ crab19_starting_ev = 24

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*6)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)

    if rand_crab19_type ==10:
        $ crab19_type = "10"
        $ crab19_title = "bampy"
        $ crab19_element = "earth"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 20
            $ crab19_starting_att = 17
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 17
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*4)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*3)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*3)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 20
            $ crab19_starting_def = 23
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 26

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*4)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 24
            $ crab19_starting_att = 21
            $ crab19_starting_def = 24
            $ crab19_starting_acc = 21
            $ crab19_starting_ev = 27

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*6)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*7)

    if rand_crab19_type ==11:
        $ crab19_type = "11"
        $ crab19_title = "grappy"
        $ crab19_element = "fire"
        if crab19_rarity == "n":
            $ crab19_starting_hp = 23
            $ crab19_starting_att = 23
            $ crab19_starting_def = 17
            $ crab19_starting_acc = 17
            $ crab19_starting_ev = 20

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*5)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*5)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*3)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*3)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*4)

        if crab19_rarity == "r":
            $ crab19_starting_hp = 26
            $ crab19_starting_att = 26
            $ crab19_starting_def = 20
            $ crab19_starting_acc = 20
            $ crab19_starting_ev = 23

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*6)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*6)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*4)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*4)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*5)

        if crab19_rarity == "e":
            $ crab19_starting_hp = 27
            $ crab19_starting_att = 27
            $ crab19_starting_def = 21
            $ crab19_starting_acc = 21
            $ crab19_starting_ev = 24

            $ crab19_hp = crab19_starting_hp + ((crab19_level-1)*7)
            $ crab19_att = crab19_starting_att + ((crab19_level-1)*7)
            $ crab19_def = crab19_starting_def + ((crab19_level-1)*5)
            $ crab19_acc = crab19_starting_acc + ((crab19_level-1)*5)
            $ crab19_ev = crab19_starting_ev + ((crab19_level-1)*6)
    show crab19_shuffle:
        ypos -200
    with flash

    if crab19_rarity =="n":
        "you got a normal {b}[crab19_title]{/b}!"
    if crab19_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab19_title]{/b}!"
    if crab19_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab19_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab19_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab19_name = crab19_name.strip()
            if crab19_name == "":
                $ crab19_name= crab19_title
            y "how about... [crab19_name]."
        "[crab19_title]":

            $ crab19_name = crab19_title
    jump after_crab_get

label crab20_trap_get:
    if rand_crab20_type ==1:
        $ crab20_type = "1"
        $ crab20_title = "slasher"
        $ crab20_element = "fire"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 20
            $ crab20_starting_att = 23
            $ crab20_starting_def = 17
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*4)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*3)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 26
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 24
            $ crab20_starting_att = 27
            $ crab20_starting_def = 21
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 24

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*7)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)



    if rand_crab20_type ==2:
        $ crab20_type = "2"
        $ crab20_title = "reacher"
        $ crab20_element = "water"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 20
            $ crab20_starting_att = 20
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 17

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*4)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*3)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 23
            $ crab20_starting_def = 23
            $ crab20_starting_acc = 26
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 24
            $ crab20_starting_att = 24
            $ crab20_starting_def = 24
            $ crab20_starting_acc = 27
            $ crab20_starting_ev = 21

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*7)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)



    if rand_crab20_type ==3:
        $ crab20_type = "3"
        $ crab20_title = "jacko"
        $ crab20_element = "earth"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 17
            $ crab20_starting_def = 17
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*3)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*3)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 26
            $ crab20_starting_att = 20
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 26
            $ crab20_starting_ev = 26

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 27
            $ crab20_starting_att = 21
            $ crab20_starting_def = 21
            $ crab20_starting_acc = 27
            $ crab20_starting_ev = 27

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*7)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*7)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*7)

    if rand_crab20_type ==4:
        $ crab20_type = "4"
        $ crab20_title = "julienne"
        $ crab20_element = "air"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 20
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 26
            $ crab20_starting_att = 23
            $ crab20_starting_def = 23
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 27
            $ crab20_starting_att = 24
            $ crab20_starting_def = 24
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 24

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*7)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)

    if rand_crab20_type ==5:
        $ crab20_type = "5"
        $ crab20_title = "slycer"
        $ crab20_element = "fire"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 17
            $ crab20_starting_att = 23
            $ crab20_starting_def = 17
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*3)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*3)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 20
            $ crab20_starting_att = 26
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*4)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 21
            $ crab20_starting_att = 27
            $ crab20_starting_def = 21
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 24

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*7)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)

    if rand_crab20_type ==6:
        $ crab20_type = "6"
        $ crab20_title = "clypper"
        $ crab20_element = "earth"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 20
            $ crab20_starting_att = 17
            $ crab20_starting_def = 23
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 17

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*4)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*3)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*3)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 20
            $ crab20_starting_def = 26
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 24
            $ crab20_starting_att = 21
            $ crab20_starting_def = 27
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 21

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*7)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

    if rand_crab20_type ==7:
        $ crab20_type = "7"
        $ crab20_title = "barnakel"
        $ crab20_element = "water"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 17
            $ crab20_starting_def = 26
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 17

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*3)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*3)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 26
            $ crab20_starting_att = 20
            $ crab20_starting_def = 29
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*7)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 27
            $ crab20_starting_att = 21
            $ crab20_starting_def = 30
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 21

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*7)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*8)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

    if rand_crab20_type ==8:
        $ crab20_type = "8"
        $ crab20_title = "doo'ahlai"
        $ crab20_element = "air"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 23
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 17

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*3)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 26
            $ crab20_starting_att = 26
            $ crab20_starting_def = 23
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 27
            $ crab20_starting_att = 27
            $ crab20_starting_def = 24
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 21

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*7)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*7)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

    if rand_crab20_type ==9:
        $ crab20_type = "9"
        $ crab20_title = "clawp"
        $ crab20_element = "water"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 20
            $ crab20_starting_att = 20
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*4)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 23
            $ crab20_starting_def = 23
            $ crab20_starting_acc = 23
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 24
            $ crab20_starting_att = 24
            $ crab20_starting_def = 24
            $ crab20_starting_acc = 24
            $ crab20_starting_ev = 24

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*6)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)

    if rand_crab20_type ==10:
        $ crab20_type = "10"
        $ crab20_title = "bampy"
        $ crab20_element = "earth"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 20
            $ crab20_starting_att = 17
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 17
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*4)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*3)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*3)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 20
            $ crab20_starting_def = 23
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 26

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*4)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 24
            $ crab20_starting_att = 21
            $ crab20_starting_def = 24
            $ crab20_starting_acc = 21
            $ crab20_starting_ev = 27

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*6)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*7)

    if rand_crab20_type ==11:
        $ crab20_type = "11"
        $ crab20_title = "grappy"
        $ crab20_element = "fire"
        if crab20_rarity == "n":
            $ crab20_starting_hp = 23
            $ crab20_starting_att = 23
            $ crab20_starting_def = 17
            $ crab20_starting_acc = 17
            $ crab20_starting_ev = 20

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*5)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*5)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*3)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*3)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*4)

        if crab20_rarity == "r":
            $ crab20_starting_hp = 26
            $ crab20_starting_att = 26
            $ crab20_starting_def = 20
            $ crab20_starting_acc = 20
            $ crab20_starting_ev = 23

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*6)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*6)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*4)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*4)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*5)

        if crab20_rarity == "e":
            $ crab20_starting_hp = 27
            $ crab20_starting_att = 27
            $ crab20_starting_def = 21
            $ crab20_starting_acc = 21
            $ crab20_starting_ev = 24

            $ crab20_hp = crab20_starting_hp + ((crab20_level-1)*7)
            $ crab20_att = crab20_starting_att + ((crab20_level-1)*7)
            $ crab20_def = crab20_starting_def + ((crab20_level-1)*5)
            $ crab20_acc = crab20_starting_acc + ((crab20_level-1)*5)
            $ crab20_ev = crab20_starting_ev + ((crab20_level-1)*6)
    show crab20_shuffle:
        ypos -200
    with flash

    if crab20_rarity =="n":
        "you got a normal {b}[crab20_title]{/b}!"
    if crab20_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab20_title]{/b}!"
    if crab20_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab20_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab20_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab20_name = crab20_name.strip()
            if crab20_name == "":
                $ crab20_name= crab20_title
            y "how about... [crab20_name]."
        "[crab20_title]":

            $ crab20_name = crab20_title

    jump after_crab_get

label crab21_trap_get:
    if rand_crab21_type ==1:
        $ crab21_type = "1"
        $ crab21_title = "slasher"
        $ crab21_element = "fire"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 20
            $ crab21_starting_att = 23
            $ crab21_starting_def = 17
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*4)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*3)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 26
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 24
            $ crab21_starting_att = 27
            $ crab21_starting_def = 21
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 24

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*7)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)



    if rand_crab21_type ==2:
        $ crab21_type = "2"
        $ crab21_title = "reacher"
        $ crab21_element = "water"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 20
            $ crab21_starting_att = 20
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 17

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*4)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*3)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 23
            $ crab21_starting_def = 23
            $ crab21_starting_acc = 26
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 24
            $ crab21_starting_att = 24
            $ crab21_starting_def = 24
            $ crab21_starting_acc = 27
            $ crab21_starting_ev = 21

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*7)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)



    if rand_crab21_type ==3:
        $ crab21_type = "3"
        $ crab21_title = "jacko"
        $ crab21_element = "earth"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 17
            $ crab21_starting_def = 17
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*3)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*3)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 26
            $ crab21_starting_att = 20
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 26
            $ crab21_starting_ev = 26

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 27
            $ crab21_starting_att = 21
            $ crab21_starting_def = 21
            $ crab21_starting_acc = 27
            $ crab21_starting_ev = 27

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*7)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*7)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*7)

    if rand_crab21_type ==4:
        $ crab21_type = "4"
        $ crab21_title = "julienne"
        $ crab21_element = "air"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 20
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 26
            $ crab21_starting_att = 23
            $ crab21_starting_def = 23
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 27
            $ crab21_starting_att = 24
            $ crab21_starting_def = 24
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 24

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*7)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)

    if rand_crab21_type ==5:
        $ crab21_type = "5"
        $ crab21_title = "slycer"
        $ crab21_element = "fire"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 17
            $ crab21_starting_att = 23
            $ crab21_starting_def = 17
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*3)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*3)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 20
            $ crab21_starting_att = 26
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*4)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 21
            $ crab21_starting_att = 27
            $ crab21_starting_def = 21
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 24

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*7)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)

    if rand_crab21_type ==6:
        $ crab21_type = "6"
        $ crab21_title = "clypper"
        $ crab21_element = "earth"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 20
            $ crab21_starting_att = 17
            $ crab21_starting_def = 23
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 17

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*4)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*3)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*3)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 20
            $ crab21_starting_def = 26
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 24
            $ crab21_starting_att = 21
            $ crab21_starting_def = 27
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 21

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*7)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

    if rand_crab21_type ==7:
        $ crab21_type = "7"
        $ crab21_title = "barnakel"
        $ crab21_element = "water"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 17
            $ crab21_starting_def = 26
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 17

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*3)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*3)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 26
            $ crab21_starting_att = 20
            $ crab21_starting_def = 29
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*7)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 27
            $ crab21_starting_att = 21
            $ crab21_starting_def = 30
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 21

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*7)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*8)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

    if rand_crab21_type ==8:
        $ crab21_type = "8"
        $ crab21_title = "doo'ahlai"
        $ crab21_element = "air"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 23
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 17

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*3)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 26
            $ crab21_starting_att = 26
            $ crab21_starting_def = 23
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 27
            $ crab21_starting_att = 27
            $ crab21_starting_def = 24
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 21

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*7)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*7)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

    if rand_crab21_type ==9:
        $ crab21_type = "9"
        $ crab21_title = "clawp"
        $ crab21_element = "water"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 20
            $ crab21_starting_att = 20
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*4)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 23
            $ crab21_starting_def = 23
            $ crab21_starting_acc = 23
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 24
            $ crab21_starting_att = 24
            $ crab21_starting_def = 24
            $ crab21_starting_acc = 24
            $ crab21_starting_ev = 24

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*6)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)

    if rand_crab21_type ==10:
        $ crab21_type = "10"
        $ crab21_title = "bampy"
        $ crab21_element = "earth"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 20
            $ crab21_starting_att = 17
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 17
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*4)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*3)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*3)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 20
            $ crab21_starting_def = 23
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 26

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*4)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 24
            $ crab21_starting_att = 21
            $ crab21_starting_def = 24
            $ crab21_starting_acc = 21
            $ crab21_starting_ev = 27

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*6)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*7)

    if rand_crab21_type ==11:
        $ crab21_type = "11"
        $ crab21_title = "grappy"
        $ crab21_element = "fire"
        if crab21_rarity == "n":
            $ crab21_starting_hp = 23
            $ crab21_starting_att = 23
            $ crab21_starting_def = 17
            $ crab21_starting_acc = 17
            $ crab21_starting_ev = 20

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*5)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*5)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*3)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*3)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*4)

        if crab21_rarity == "r":
            $ crab21_starting_hp = 26
            $ crab21_starting_att = 26
            $ crab21_starting_def = 20
            $ crab21_starting_acc = 20
            $ crab21_starting_ev = 23

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*6)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*6)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*4)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*4)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*5)

        if crab21_rarity == "e":
            $ crab21_starting_hp = 27
            $ crab21_starting_att = 27
            $ crab21_starting_def = 21
            $ crab21_starting_acc = 21
            $ crab21_starting_ev = 24

            $ crab21_hp = crab21_starting_hp + ((crab21_level-1)*7)
            $ crab21_att = crab21_starting_att + ((crab21_level-1)*7)
            $ crab21_def = crab21_starting_def + ((crab21_level-1)*5)
            $ crab21_acc = crab21_starting_acc + ((crab21_level-1)*5)
            $ crab21_ev = crab21_starting_ev + ((crab21_level-1)*6)
    show crab21_shuffle:
        ypos -200
    with flash

    if crab21_rarity =="n":
        "you got a normal {b}[crab21_title]{/b}!"
    if crab21_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab21_title]{/b}!"
    if crab21_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab21_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab21_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab21_name = crab21_name.strip()
            if crab21_name == "":
                $ crab21_name= crab21_title
            y "how about... [crab21_name]."
        "[crab21_title]":

            $ crab21_name = crab21_title

    jump after_crab_get

label crab22_trap_get:
    if rand_crab22_type ==1:
        $ crab22_type = "1"
        $ crab22_title = "slasher"
        $ crab22_element = "fire"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 20
            $ crab22_starting_att = 23
            $ crab22_starting_def = 17
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*4)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*3)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 26
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 24
            $ crab22_starting_att = 27
            $ crab22_starting_def = 21
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 24

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*7)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)



    if rand_crab22_type ==2:
        $ crab22_type = "2"
        $ crab22_title = "reacher"
        $ crab22_element = "water"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 20
            $ crab22_starting_att = 20
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 17

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*4)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*3)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 23
            $ crab22_starting_def = 23
            $ crab22_starting_acc = 26
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 24
            $ crab22_starting_att = 24
            $ crab22_starting_def = 24
            $ crab22_starting_acc = 27
            $ crab22_starting_ev = 21

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*7)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)



    if rand_crab22_type ==3:
        $ crab22_type = "3"
        $ crab22_title = "jacko"
        $ crab22_element = "earth"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 17
            $ crab22_starting_def = 17
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*3)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*3)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 26
            $ crab22_starting_att = 20
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 26
            $ crab22_starting_ev = 26

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 27
            $ crab22_starting_att = 21
            $ crab22_starting_def = 21
            $ crab22_starting_acc = 27
            $ crab22_starting_ev = 27

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*7)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*7)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*7)

    if rand_crab22_type ==4:
        $ crab22_type = "4"
        $ crab22_title = "julienne"
        $ crab22_element = "air"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 20
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 26
            $ crab22_starting_att = 23
            $ crab22_starting_def = 23
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 27
            $ crab22_starting_att = 24
            $ crab22_starting_def = 24
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 24

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*7)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)

    if rand_crab22_type ==5:
        $ crab22_type = "5"
        $ crab22_title = "slycer"
        $ crab22_element = "fire"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 17
            $ crab22_starting_att = 23
            $ crab22_starting_def = 17
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*3)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*3)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 20
            $ crab22_starting_att = 26
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*4)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 21
            $ crab22_starting_att = 27
            $ crab22_starting_def = 21
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 24

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*7)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)

    if rand_crab22_type ==6:
        $ crab22_type = "6"
        $ crab22_title = "clypper"
        $ crab22_element = "earth"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 20
            $ crab22_starting_att = 17
            $ crab22_starting_def = 23
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 17

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*4)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*3)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*3)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 20
            $ crab22_starting_def = 26
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 24
            $ crab22_starting_att = 21
            $ crab22_starting_def = 27
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 21

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*7)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

    if rand_crab22_type ==7:
        $ crab22_type = "7"
        $ crab22_title = "barnakel"
        $ crab22_element = "water"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 17
            $ crab22_starting_def = 26
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 17

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*3)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*3)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 26
            $ crab22_starting_att = 20
            $ crab22_starting_def = 29
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*7)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 27
            $ crab22_starting_att = 21
            $ crab22_starting_def = 30
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 21

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*7)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*8)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

    if rand_crab22_type ==8:
        $ crab22_type = "8"
        $ crab22_title = "doo'ahlai"
        $ crab22_element = "air"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 23
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 17

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*3)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 26
            $ crab22_starting_att = 26
            $ crab22_starting_def = 23
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 27
            $ crab22_starting_att = 27
            $ crab22_starting_def = 24
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 21

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*7)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*7)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

    if rand_crab22_type ==9:
        $ crab22_type = "9"
        $ crab22_title = "clawp"
        $ crab22_element = "water"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 20
            $ crab22_starting_att = 20
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*4)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 23
            $ crab22_starting_def = 23
            $ crab22_starting_acc = 23
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 24
            $ crab22_starting_att = 24
            $ crab22_starting_def = 24
            $ crab22_starting_acc = 24
            $ crab22_starting_ev = 24

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*6)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)

    if rand_crab22_type ==10:
        $ crab22_type = "10"
        $ crab22_title = "bampy"
        $ crab22_element = "earth"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 20
            $ crab22_starting_att = 17
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 17
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*4)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*3)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*3)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 20
            $ crab22_starting_def = 23
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 26

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*4)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 24
            $ crab22_starting_att = 21
            $ crab22_starting_def = 24
            $ crab22_starting_acc = 21
            $ crab22_starting_ev = 27

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*6)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*7)

    if rand_crab22_type ==11:
        $ crab22_type = "11"
        $ crab22_title = "grappy"
        $ crab22_element = "fire"
        if crab22_rarity == "n":
            $ crab22_starting_hp = 23
            $ crab22_starting_att = 23
            $ crab22_starting_def = 17
            $ crab22_starting_acc = 17
            $ crab22_starting_ev = 20

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*5)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*5)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*3)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*3)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*4)

        if crab22_rarity == "r":
            $ crab22_starting_hp = 26
            $ crab22_starting_att = 26
            $ crab22_starting_def = 20
            $ crab22_starting_acc = 20
            $ crab22_starting_ev = 23

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*6)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*6)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*4)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*4)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*5)

        if crab22_rarity == "e":
            $ crab22_starting_hp = 27
            $ crab22_starting_att = 27
            $ crab22_starting_def = 21
            $ crab22_starting_acc = 21
            $ crab22_starting_ev = 24

            $ crab22_hp = crab22_starting_hp + ((crab22_level-1)*7)
            $ crab22_att = crab22_starting_att + ((crab22_level-1)*7)
            $ crab22_def = crab22_starting_def + ((crab22_level-1)*5)
            $ crab22_acc = crab22_starting_acc + ((crab22_level-1)*5)
            $ crab22_ev = crab22_starting_ev + ((crab22_level-1)*6)
    show crab22_shuffle:
        ypos -200
    with flash

    if crab22_rarity =="n":
        "you got a normal {b}[crab22_title]{/b}!"
    if crab22_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab22_title]{/b}!"
    if crab22_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab22_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab22_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab22_name = crab22_name.strip()
            if crab22_name == "":
                $ crab22_name= crab22_title
            y "how about... [crab22_name]."
        "[crab22_title]":

            $ crab22_name = crab22_title

    jump after_crab_get

label crab23_trap_get:
    if rand_crab23_type ==1:
        $ crab23_type = "1"
        $ crab23_title = "slasher"
        $ crab23_element = "fire"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 20
            $ crab23_starting_att = 23
            $ crab23_starting_def = 17
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*4)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*3)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 26
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 24
            $ crab23_starting_att = 27
            $ crab23_starting_def = 21
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 24

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*7)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)



    if rand_crab23_type ==2:
        $ crab23_type = "2"
        $ crab23_title = "reacher"
        $ crab23_element = "water"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 20
            $ crab23_starting_att = 20
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 17

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*4)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*3)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 23
            $ crab23_starting_def = 23
            $ crab23_starting_acc = 26
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 24
            $ crab23_starting_att = 24
            $ crab23_starting_def = 24
            $ crab23_starting_acc = 27
            $ crab23_starting_ev = 21

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*7)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)



    if rand_crab23_type ==3:
        $ crab23_type = "3"
        $ crab23_title = "jacko"
        $ crab23_element = "earth"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 17
            $ crab23_starting_def = 17
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*3)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*3)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 26
            $ crab23_starting_att = 20
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 26
            $ crab23_starting_ev = 26

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 27
            $ crab23_starting_att = 21
            $ crab23_starting_def = 21
            $ crab23_starting_acc = 27
            $ crab23_starting_ev = 27

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*7)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*7)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*7)

    if rand_crab23_type ==4:
        $ crab23_type = "4"
        $ crab23_title = "julienne"
        $ crab23_element = "air"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 20
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 26
            $ crab23_starting_att = 23
            $ crab23_starting_def = 23
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 27
            $ crab23_starting_att = 24
            $ crab23_starting_def = 24
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 24

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*7)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)

    if rand_crab23_type ==5:
        $ crab23_type = "5"
        $ crab23_title = "slycer"
        $ crab23_element = "fire"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 17
            $ crab23_starting_att = 23
            $ crab23_starting_def = 17
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*3)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*3)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 20
            $ crab23_starting_att = 26
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*4)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 21
            $ crab23_starting_att = 27
            $ crab23_starting_def = 21
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 24

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*7)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)

    if rand_crab23_type ==6:
        $ crab23_type = "6"
        $ crab23_title = "clypper"
        $ crab23_element = "earth"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 20
            $ crab23_starting_att = 17
            $ crab23_starting_def = 23
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 17

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*4)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*3)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*3)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 20
            $ crab23_starting_def = 26
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 24
            $ crab23_starting_att = 21
            $ crab23_starting_def = 27
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 21

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*7)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

    if rand_crab23_type ==7:
        $ crab23_type = "7"
        $ crab23_title = "barnakel"
        $ crab23_element = "water"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 17
            $ crab23_starting_def = 26
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 17

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*3)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*3)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 26
            $ crab23_starting_att = 20
            $ crab23_starting_def = 29
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*7)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 27
            $ crab23_starting_att = 21
            $ crab23_starting_def = 30
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 21

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*7)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*8)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

    if rand_crab23_type ==8:
        $ crab23_type = "8"
        $ crab23_title = "doo'ahlai"
        $ crab23_element = "air"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 23
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 17

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*3)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 26
            $ crab23_starting_att = 26
            $ crab23_starting_def = 23
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 27
            $ crab23_starting_att = 27
            $ crab23_starting_def = 24
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 21

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*7)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*7)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

    if rand_crab23_type ==9:
        $ crab23_type = "9"
        $ crab23_title = "clawp"
        $ crab23_element = "water"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 20
            $ crab23_starting_att = 20
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*4)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 23
            $ crab23_starting_def = 23
            $ crab23_starting_acc = 23
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 24
            $ crab23_starting_att = 24
            $ crab23_starting_def = 24
            $ crab23_starting_acc = 24
            $ crab23_starting_ev = 24

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*6)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)

    if rand_crab23_type ==10:
        $ crab23_type = "10"
        $ crab23_title = "bampy"
        $ crab23_element = "earth"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 20
            $ crab23_starting_att = 17
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 17
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*4)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*3)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*3)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 20
            $ crab23_starting_def = 23
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 26

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*4)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 24
            $ crab23_starting_att = 21
            $ crab23_starting_def = 24
            $ crab23_starting_acc = 21
            $ crab23_starting_ev = 27

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*6)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*7)

    if rand_crab23_type ==11:
        $ crab23_type = "11"
        $ crab23_title = "grappy"
        $ crab23_element = "fire"
        if crab23_rarity == "n":
            $ crab23_starting_hp = 23
            $ crab23_starting_att = 23
            $ crab23_starting_def = 17
            $ crab23_starting_acc = 17
            $ crab23_starting_ev = 20

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*5)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*5)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*3)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*3)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*4)

        if crab23_rarity == "r":
            $ crab23_starting_hp = 26
            $ crab23_starting_att = 26
            $ crab23_starting_def = 20
            $ crab23_starting_acc = 20
            $ crab23_starting_ev = 23

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*6)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*6)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*4)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*4)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*5)

        if crab23_rarity == "e":
            $ crab23_starting_hp = 27
            $ crab23_starting_att = 27
            $ crab23_starting_def = 21
            $ crab23_starting_acc = 21
            $ crab23_starting_ev = 24

            $ crab23_hp = crab23_starting_hp + ((crab23_level-1)*7)
            $ crab23_att = crab23_starting_att + ((crab23_level-1)*7)
            $ crab23_def = crab23_starting_def + ((crab23_level-1)*5)
            $ crab23_acc = crab23_starting_acc + ((crab23_level-1)*5)
            $ crab23_ev = crab23_starting_ev + ((crab23_level-1)*6)
    show crab23_shuffle:
        ypos -200
    with flash

    if crab23_rarity =="n":
        "you got a normal {b}[crab23_title]{/b}!"
    if crab23_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab23_title]{/b}!"
    if crab23_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab23_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab23_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab23_name = crab23_name.strip()
            if crab23_name == "":
                $ crab23_name= crab23_title
            y "how about... [crab23_name]."
        "[crab23_title]":

            $ crab23_name = crab23_title

    jump after_crab_get

label crab24_trap_get:
    if rand_crab24_type ==1:
        $ crab24_type = "1"
        $ crab24_title = "slasher"
        $ crab24_element = "fire"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 20
            $ crab24_starting_att = 23
            $ crab24_starting_def = 17
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*4)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*3)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 26
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 24
            $ crab24_starting_att = 27
            $ crab24_starting_def = 21
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 24

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*7)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)



    if rand_crab24_type ==2:
        $ crab24_type = "2"
        $ crab24_title = "reacher"
        $ crab24_element = "water"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 20
            $ crab24_starting_att = 20
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 17

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*4)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*3)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 23
            $ crab24_starting_def = 23
            $ crab24_starting_acc = 26
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 24
            $ crab24_starting_att = 24
            $ crab24_starting_def = 24
            $ crab24_starting_acc = 27
            $ crab24_starting_ev = 21

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*7)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)



    if rand_crab24_type ==3:
        $ crab24_type = "3"
        $ crab24_title = "jacko"
        $ crab24_element = "earth"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 17
            $ crab24_starting_def = 17
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*3)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*3)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 26
            $ crab24_starting_att = 20
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 26
            $ crab24_starting_ev = 26

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 27
            $ crab24_starting_att = 21
            $ crab24_starting_def = 21
            $ crab24_starting_acc = 27
            $ crab24_starting_ev = 27

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*7)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*7)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*7)

    if rand_crab24_type ==4:
        $ crab24_type = "4"
        $ crab24_title = "julienne"
        $ crab24_element = "air"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 20
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 26
            $ crab24_starting_att = 23
            $ crab24_starting_def = 23
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 27
            $ crab24_starting_att = 24
            $ crab24_starting_def = 24
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 24

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*7)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)

    if rand_crab24_type ==5:
        $ crab24_type = "5"
        $ crab24_title = "slycer"
        $ crab24_element = "fire"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 17
            $ crab24_starting_att = 23
            $ crab24_starting_def = 17
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*3)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*3)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 20
            $ crab24_starting_att = 26
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*4)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 21
            $ crab24_starting_att = 27
            $ crab24_starting_def = 21
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 24

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*7)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)

    if rand_crab24_type ==6:
        $ crab24_type = "6"
        $ crab24_title = "clypper"
        $ crab24_element = "earth"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 20
            $ crab24_starting_att = 17
            $ crab24_starting_def = 23
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 17

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*4)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*3)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*3)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 20
            $ crab24_starting_def = 26
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 24
            $ crab24_starting_att = 21
            $ crab24_starting_def = 27
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 21

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*7)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

    if rand_crab24_type ==7:
        $ crab24_type = "7"
        $ crab24_title = "barnakel"
        $ crab24_element = "water"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 17
            $ crab24_starting_def = 26
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 17

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*3)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*3)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 26
            $ crab24_starting_att = 20
            $ crab24_starting_def = 29
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*7)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 27
            $ crab24_starting_att = 21
            $ crab24_starting_def = 30
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 21

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*7)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*8)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

    if rand_crab24_type ==8:
        $ crab24_type = "8"
        $ crab24_title = "doo'ahlai"
        $ crab24_element = "air"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 23
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 17

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*3)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 26
            $ crab24_starting_att = 26
            $ crab24_starting_def = 23
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 27
            $ crab24_starting_att = 27
            $ crab24_starting_def = 24
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 21

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*7)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*7)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

    if rand_crab24_type ==9:
        $ crab24_type = "9"
        $ crab24_title = "clawp"
        $ crab24_element = "water"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 20
            $ crab24_starting_att = 20
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*4)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 23
            $ crab24_starting_def = 23
            $ crab24_starting_acc = 23
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 24
            $ crab24_starting_att = 24
            $ crab24_starting_def = 24
            $ crab24_starting_acc = 24
            $ crab24_starting_ev = 24

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*6)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)

    if rand_crab24_type ==10:
        $ crab24_type = "10"
        $ crab24_title = "bampy"
        $ crab24_element = "earth"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 20
            $ crab24_starting_att = 17
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 17
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*4)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*3)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*3)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 20
            $ crab24_starting_def = 23
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 26

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*4)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 24
            $ crab24_starting_att = 21
            $ crab24_starting_def = 24
            $ crab24_starting_acc = 21
            $ crab24_starting_ev = 27

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*6)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*7)

    if rand_crab24_type ==11:
        $ crab24_type = "11"
        $ crab24_title = "grappy"
        $ crab24_element = "fire"
        if crab24_rarity == "n":
            $ crab24_starting_hp = 23
            $ crab24_starting_att = 23
            $ crab24_starting_def = 17
            $ crab24_starting_acc = 17
            $ crab24_starting_ev = 20

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*5)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*5)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*3)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*3)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*4)

        if crab24_rarity == "r":
            $ crab24_starting_hp = 26
            $ crab24_starting_att = 26
            $ crab24_starting_def = 20
            $ crab24_starting_acc = 20
            $ crab24_starting_ev = 23

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*6)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*6)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*4)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*4)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*5)

        if crab24_rarity == "e":
            $ crab24_starting_hp = 27
            $ crab24_starting_att = 27
            $ crab24_starting_def = 21
            $ crab24_starting_acc = 21
            $ crab24_starting_ev = 24

            $ crab24_hp = crab24_starting_hp + ((crab24_level-1)*7)
            $ crab24_att = crab24_starting_att + ((crab24_level-1)*7)
            $ crab24_def = crab24_starting_def + ((crab24_level-1)*5)
            $ crab24_acc = crab24_starting_acc + ((crab24_level-1)*5)
            $ crab24_ev = crab24_starting_ev + ((crab24_level-1)*6)
    show crab24_shuffle:
        ypos -200
    with flash

    if crab24_rarity =="n":
        "you got a normal {b}[crab24_title]{/b}!"
    if crab24_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab24_title]{/b}!"
    if crab24_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab24_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab24_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab24_name = crab24_name.strip()
            if crab24_name == "":
                $ crab24_name= crab24_title
            y "how about... [crab24_name]."
        "[crab24_title]":

            $ crab24_name = crab24_title

    jump after_crab_get

label crab25_trap_get:
    if rand_crab25_type ==1:
        $ crab25_type = "1"
        $ crab25_title = "slasher"
        $ crab25_element = "fire"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 20
            $ crab25_starting_att = 23
            $ crab25_starting_def = 17
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*4)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*3)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 26
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 24
            $ crab25_starting_att = 27
            $ crab25_starting_def = 21
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 24

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*7)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)



    if rand_crab25_type ==2:
        $ crab25_type = "2"
        $ crab25_title = "reacher"
        $ crab25_element = "water"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 20
            $ crab25_starting_att = 20
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 17

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*4)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*3)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 23
            $ crab25_starting_def = 23
            $ crab25_starting_acc = 26
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 24
            $ crab25_starting_att = 24
            $ crab25_starting_def = 24
            $ crab25_starting_acc = 27
            $ crab25_starting_ev = 21

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*7)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)



    if rand_crab25_type ==3:
        $ crab25_type = "3"
        $ crab25_title = "jacko"
        $ crab25_element = "earth"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 17
            $ crab25_starting_def = 17
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*3)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*3)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 26
            $ crab25_starting_att = 20
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 26
            $ crab25_starting_ev = 26

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 27
            $ crab25_starting_att = 21
            $ crab25_starting_def = 21
            $ crab25_starting_acc = 27
            $ crab25_starting_ev = 27

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*7)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*7)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*7)

    if rand_crab25_type ==4:
        $ crab25_type = "4"
        $ crab25_title = "julienne"
        $ crab25_element = "air"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 20
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 26
            $ crab25_starting_att = 23
            $ crab25_starting_def = 23
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 27
            $ crab25_starting_att = 24
            $ crab25_starting_def = 24
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 24

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*7)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)

    if rand_crab25_type ==5:
        $ crab25_type = "5"
        $ crab25_title = "slycer"
        $ crab25_element = "fire"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 17
            $ crab25_starting_att = 23
            $ crab25_starting_def = 17
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*3)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*3)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 20
            $ crab25_starting_att = 26
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*4)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 21
            $ crab25_starting_att = 27
            $ crab25_starting_def = 21
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 24

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*7)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)

    if rand_crab25_type ==6:
        $ crab25_type = "6"
        $ crab25_title = "clypper"
        $ crab25_element = "earth"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 20
            $ crab25_starting_att = 17
            $ crab25_starting_def = 23
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 17

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*4)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*3)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*3)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 20
            $ crab25_starting_def = 26
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 24
            $ crab25_starting_att = 21
            $ crab25_starting_def = 27
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 21

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*7)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

    if rand_crab25_type ==7:
        $ crab25_type = "7"
        $ crab25_title = "barnakel"
        $ crab25_element = "water"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 17
            $ crab25_starting_def = 26
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 17

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*3)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*3)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 26
            $ crab25_starting_att = 20
            $ crab25_starting_def = 29
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*7)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 27
            $ crab25_starting_att = 21
            $ crab25_starting_def = 30
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 21

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*7)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*8)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

    if rand_crab25_type ==8:
        $ crab25_type = "8"
        $ crab25_title = "doo'ahlai"
        $ crab25_element = "air"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 23
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 17

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*3)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 26
            $ crab25_starting_att = 26
            $ crab25_starting_def = 23
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 27
            $ crab25_starting_att = 27
            $ crab25_starting_def = 24
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 21

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*7)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*7)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

    if rand_crab25_type ==9:
        $ crab25_type = "9"
        $ crab25_title = "clawp"
        $ crab25_element = "water"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 20
            $ crab25_starting_att = 20
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*4)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 23
            $ crab25_starting_def = 23
            $ crab25_starting_acc = 23
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 24
            $ crab25_starting_att = 24
            $ crab25_starting_def = 24
            $ crab25_starting_acc = 24
            $ crab25_starting_ev = 24

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*6)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)

    if rand_crab25_type ==10:
        $ crab25_type = "10"
        $ crab25_title = "bampy"
        $ crab25_element = "earth"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 20
            $ crab25_starting_att = 17
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 17
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*4)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*3)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*3)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 20
            $ crab25_starting_def = 23
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 26

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*4)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 24
            $ crab25_starting_att = 21
            $ crab25_starting_def = 24
            $ crab25_starting_acc = 21
            $ crab25_starting_ev = 27

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*6)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*7)

    if rand_crab25_type ==11:
        $ crab25_type = "11"
        $ crab25_title = "grappy"
        $ crab25_element = "fire"
        if crab25_rarity == "n":
            $ crab25_starting_hp = 23
            $ crab25_starting_att = 23
            $ crab25_starting_def = 17
            $ crab25_starting_acc = 17
            $ crab25_starting_ev = 20

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*5)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*5)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*3)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*3)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*4)

        if crab25_rarity == "r":
            $ crab25_starting_hp = 26
            $ crab25_starting_att = 26
            $ crab25_starting_def = 20
            $ crab25_starting_acc = 20
            $ crab25_starting_ev = 23

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*6)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*6)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*4)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*4)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*5)

        if crab25_rarity == "e":
            $ crab25_starting_hp = 27
            $ crab25_starting_att = 27
            $ crab25_starting_def = 21
            $ crab25_starting_acc = 21
            $ crab25_starting_ev = 24

            $ crab25_hp = crab25_starting_hp + ((crab25_level-1)*7)
            $ crab25_att = crab25_starting_att + ((crab25_level-1)*7)
            $ crab25_def = crab25_starting_def + ((crab25_level-1)*5)
            $ crab25_acc = crab25_starting_acc + ((crab25_level-1)*5)
            $ crab25_ev = crab25_starting_ev + ((crab25_level-1)*6)
    show crab25_shuffle:
        ypos -200
    with flash

    if crab25_rarity =="n":
        "you got a normal {b}[crab25_title]{/b}!"
    if crab25_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab25_title]{/b}!"
    if crab25_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab25_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab25_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab25_name = crab25_name.strip()
            if crab25_name == "":
                $ crab25_name= crab25_title
            y "how about... [crab25_name]."
        "[crab25_title]":

            $ crab25_name = crab25_title

    jump after_crab_get

label crab26_trap_get:
    if rand_crab26_type ==1:
        $ crab26_type = "1"
        $ crab26_title = "slasher"
        $ crab26_element = "fire"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 20
            $ crab26_starting_att = 23
            $ crab26_starting_def = 17
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*4)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*3)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 26
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 24
            $ crab26_starting_att = 27
            $ crab26_starting_def = 21
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 24

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*7)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)



    if rand_crab26_type ==2:
        $ crab26_type = "2"
        $ crab26_title = "reacher"
        $ crab26_element = "water"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 20
            $ crab26_starting_att = 20
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 17

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*4)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*3)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 23
            $ crab26_starting_def = 23
            $ crab26_starting_acc = 26
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 24
            $ crab26_starting_att = 24
            $ crab26_starting_def = 24
            $ crab26_starting_acc = 27
            $ crab26_starting_ev = 21

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*7)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)



    if rand_crab26_type ==3:
        $ crab26_type = "3"
        $ crab26_title = "jacko"
        $ crab26_element = "earth"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 17
            $ crab26_starting_def = 17
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*3)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*3)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 26
            $ crab26_starting_att = 20
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 26
            $ crab26_starting_ev = 26

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 27
            $ crab26_starting_att = 21
            $ crab26_starting_def = 21
            $ crab26_starting_acc = 27
            $ crab26_starting_ev = 27

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*7)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*7)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*7)

    if rand_crab26_type ==4:
        $ crab26_type = "4"
        $ crab26_title = "julienne"
        $ crab26_element = "air"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 20
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 26
            $ crab26_starting_att = 23
            $ crab26_starting_def = 23
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 27
            $ crab26_starting_att = 24
            $ crab26_starting_def = 24
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 24

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*7)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)

    if rand_crab26_type ==5:
        $ crab26_type = "5"
        $ crab26_title = "slycer"
        $ crab26_element = "fire"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 17
            $ crab26_starting_att = 23
            $ crab26_starting_def = 17
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*3)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*3)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 20
            $ crab26_starting_att = 26
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*4)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 21
            $ crab26_starting_att = 27
            $ crab26_starting_def = 21
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 24

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*7)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)

    if rand_crab26_type ==6:
        $ crab26_type = "6"
        $ crab26_title = "clypper"
        $ crab26_element = "earth"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 20
            $ crab26_starting_att = 17
            $ crab26_starting_def = 23
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 17

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*4)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*3)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*3)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 20
            $ crab26_starting_def = 26
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 24
            $ crab26_starting_att = 21
            $ crab26_starting_def = 27
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 21

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*7)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

    if rand_crab26_type ==7:
        $ crab26_type = "7"
        $ crab26_title = "barnakel"
        $ crab26_element = "water"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 17
            $ crab26_starting_def = 26
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 17

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*3)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*3)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 26
            $ crab26_starting_att = 20
            $ crab26_starting_def = 29
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*7)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 27
            $ crab26_starting_att = 21
            $ crab26_starting_def = 30
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 21

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*7)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*8)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

    if rand_crab26_type ==8:
        $ crab26_type = "8"
        $ crab26_title = "doo'ahlai"
        $ crab26_element = "air"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 23
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 17

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*3)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 26
            $ crab26_starting_att = 26
            $ crab26_starting_def = 23
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 27
            $ crab26_starting_att = 27
            $ crab26_starting_def = 24
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 21

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*7)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*7)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

    if rand_crab26_type ==9:
        $ crab26_type = "9"
        $ crab26_title = "clawp"
        $ crab26_element = "water"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 20
            $ crab26_starting_att = 20
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*4)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 23
            $ crab26_starting_def = 23
            $ crab26_starting_acc = 23
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 24
            $ crab26_starting_att = 24
            $ crab26_starting_def = 24
            $ crab26_starting_acc = 24
            $ crab26_starting_ev = 24

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*6)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)

    if rand_crab26_type ==10:
        $ crab26_type = "10"
        $ crab26_title = "bampy"
        $ crab26_element = "earth"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 20
            $ crab26_starting_att = 17
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 17
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*4)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*3)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*3)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 20
            $ crab26_starting_def = 23
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 26

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*4)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 24
            $ crab26_starting_att = 21
            $ crab26_starting_def = 24
            $ crab26_starting_acc = 21
            $ crab26_starting_ev = 27

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*6)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*7)

    if rand_crab26_type ==11:
        $ crab26_type = "11"
        $ crab26_title = "grappy"
        $ crab26_element = "fire"
        if crab26_rarity == "n":
            $ crab26_starting_hp = 23
            $ crab26_starting_att = 23
            $ crab26_starting_def = 17
            $ crab26_starting_acc = 17
            $ crab26_starting_ev = 20

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*5)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*5)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*3)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*3)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*4)

        if crab26_rarity == "r":
            $ crab26_starting_hp = 26
            $ crab26_starting_att = 26
            $ crab26_starting_def = 20
            $ crab26_starting_acc = 20
            $ crab26_starting_ev = 23

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*6)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*6)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*4)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*4)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*5)

        if crab26_rarity == "e":
            $ crab26_starting_hp = 27
            $ crab26_starting_att = 27
            $ crab26_starting_def = 21
            $ crab26_starting_acc = 21
            $ crab26_starting_ev = 24

            $ crab26_hp = crab26_starting_hp + ((crab26_level-1)*7)
            $ crab26_att = crab26_starting_att + ((crab26_level-1)*7)
            $ crab26_def = crab26_starting_def + ((crab26_level-1)*5)
            $ crab26_acc = crab26_starting_acc + ((crab26_level-1)*5)
            $ crab26_ev = crab26_starting_ev + ((crab26_level-1)*6)
    show crab26_shuffle:
        ypos -200
    with flash

    if crab26_rarity =="n":
        "you got a normal {b}[crab26_title]{/b}!"
    if crab26_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab26_title]{/b}!"
    if crab26_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab26_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab26_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab26_name = crab26_name.strip()
            if crab26_name == "":
                $ crab26_name= crab26_title
            y "how about... [crab26_name]."
        "[crab26_title]":

            $ crab26_name = crab26_title

    jump after_crab_get

label crab27_trap_get:
    if rand_crab27_type ==1:
        $ crab27_type = "1"
        $ crab27_title = "slasher"
        $ crab27_element = "fire"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 20
            $ crab27_starting_att = 23
            $ crab27_starting_def = 17
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*4)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*3)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 26
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 24
            $ crab27_starting_att = 27
            $ crab27_starting_def = 21
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 24

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*7)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)



    if rand_crab27_type ==2:
        $ crab27_type = "2"
        $ crab27_title = "reacher"
        $ crab27_element = "water"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 20
            $ crab27_starting_att = 20
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 17

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*4)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*3)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 23
            $ crab27_starting_def = 23
            $ crab27_starting_acc = 26
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 24
            $ crab27_starting_att = 24
            $ crab27_starting_def = 24
            $ crab27_starting_acc = 27
            $ crab27_starting_ev = 21

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*7)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)



    if rand_crab27_type ==3:
        $ crab27_type = "3"
        $ crab27_title = "jacko"
        $ crab27_element = "earth"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 17
            $ crab27_starting_def = 17
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*3)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*3)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 26
            $ crab27_starting_att = 20
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 26
            $ crab27_starting_ev = 26

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 27
            $ crab27_starting_att = 21
            $ crab27_starting_def = 21
            $ crab27_starting_acc = 27
            $ crab27_starting_ev = 27

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*7)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*7)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*7)

    if rand_crab27_type ==4:
        $ crab27_type = "4"
        $ crab27_title = "julienne"
        $ crab27_element = "air"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 20
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 26
            $ crab27_starting_att = 23
            $ crab27_starting_def = 23
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 27
            $ crab27_starting_att = 24
            $ crab27_starting_def = 24
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 24

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*7)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)

    if rand_crab27_type ==5:
        $ crab27_type = "5"
        $ crab27_title = "slycer"
        $ crab27_element = "fire"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 17
            $ crab27_starting_att = 23
            $ crab27_starting_def = 17
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*3)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*3)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 20
            $ crab27_starting_att = 26
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*4)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 21
            $ crab27_starting_att = 27
            $ crab27_starting_def = 21
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 24

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*7)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)

    if rand_crab27_type ==6:
        $ crab27_type = "6"
        $ crab27_title = "clypper"
        $ crab27_element = "earth"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 20
            $ crab27_starting_att = 17
            $ crab27_starting_def = 23
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 17

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*4)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*3)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*3)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 20
            $ crab27_starting_def = 26
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 24
            $ crab27_starting_att = 21
            $ crab27_starting_def = 27
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 21

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*7)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

    if rand_crab27_type ==7:
        $ crab27_type = "7"
        $ crab27_title = "barnakel"
        $ crab27_element = "water"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 17
            $ crab27_starting_def = 26
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 17

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*3)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*3)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 26
            $ crab27_starting_att = 20
            $ crab27_starting_def = 29
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*7)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 27
            $ crab27_starting_att = 21
            $ crab27_starting_def = 30
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 21

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*7)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*8)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

    if rand_crab27_type ==8:
        $ crab27_type = "8"
        $ crab27_title = "doo'ahlai"
        $ crab27_element = "air"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 23
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 17

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*3)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 26
            $ crab27_starting_att = 26
            $ crab27_starting_def = 23
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 27
            $ crab27_starting_att = 27
            $ crab27_starting_def = 24
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 21

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*7)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*7)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

    if rand_crab27_type ==9:
        $ crab27_type = "9"
        $ crab27_title = "clawp"
        $ crab27_element = "water"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 20
            $ crab27_starting_att = 20
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*4)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 23
            $ crab27_starting_def = 23
            $ crab27_starting_acc = 23
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 24
            $ crab27_starting_att = 24
            $ crab27_starting_def = 24
            $ crab27_starting_acc = 24
            $ crab27_starting_ev = 24

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*6)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)

    if rand_crab27_type ==10:
        $ crab27_type = "10"
        $ crab27_title = "bampy"
        $ crab27_element = "earth"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 20
            $ crab27_starting_att = 17
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 17
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*4)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*3)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*3)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 20
            $ crab27_starting_def = 23
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 26

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*4)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 24
            $ crab27_starting_att = 21
            $ crab27_starting_def = 24
            $ crab27_starting_acc = 21
            $ crab27_starting_ev = 27

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*6)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*7)

    if rand_crab27_type ==11:
        $ crab27_type = "11"
        $ crab27_title = "grappy"
        $ crab27_element = "fire"
        if crab27_rarity == "n":
            $ crab27_starting_hp = 23
            $ crab27_starting_att = 23
            $ crab27_starting_def = 17
            $ crab27_starting_acc = 17
            $ crab27_starting_ev = 20

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*5)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*5)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*3)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*3)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*4)

        if crab27_rarity == "r":
            $ crab27_starting_hp = 26
            $ crab27_starting_att = 26
            $ crab27_starting_def = 20
            $ crab27_starting_acc = 20
            $ crab27_starting_ev = 23

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*6)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*6)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*4)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*4)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*5)

        if crab27_rarity == "e":
            $ crab27_starting_hp = 27
            $ crab27_starting_att = 27
            $ crab27_starting_def = 21
            $ crab27_starting_acc = 21
            $ crab27_starting_ev = 24

            $ crab27_hp = crab27_starting_hp + ((crab27_level-1)*7)
            $ crab27_att = crab27_starting_att + ((crab27_level-1)*7)
            $ crab27_def = crab27_starting_def + ((crab27_level-1)*5)
            $ crab27_acc = crab27_starting_acc + ((crab27_level-1)*5)
            $ crab27_ev = crab27_starting_ev + ((crab27_level-1)*6)
    show crab27_shuffle:
        ypos -200
    with flash

    if crab27_rarity =="n":
        "you got a normal {b}[crab27_title]{/b}!"
    if crab27_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab27_title]{/b}!"
    if crab27_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab27_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab27_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab27_name = crab27_name.strip()
            if crab27_name == "":
                $ crab27_name= crab27_title
            y "how about... [crab27_name]."
        "[crab27_title]":

            $ crab27_name = crab27_title
    jump after_crab_get

label crab28_trap_get:
    if rand_crab28_type ==1:
        $ crab28_type = "1"
        $ crab28_title = "slasher"
        $ crab28_element = "fire"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 20
            $ crab28_starting_att = 23
            $ crab28_starting_def = 17
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*4)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*3)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 26
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 24
            $ crab28_starting_att = 27
            $ crab28_starting_def = 21
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 24

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*7)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)



    if rand_crab28_type ==2:
        $ crab28_type = "2"
        $ crab28_title = "reacher"
        $ crab28_element = "water"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 20
            $ crab28_starting_att = 20
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 17

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*4)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*3)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 23
            $ crab28_starting_def = 23
            $ crab28_starting_acc = 26
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 24
            $ crab28_starting_att = 24
            $ crab28_starting_def = 24
            $ crab28_starting_acc = 27
            $ crab28_starting_ev = 21

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*7)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)



    if rand_crab28_type ==3:
        $ crab28_type = "3"
        $ crab28_title = "jacko"
        $ crab28_element = "earth"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 17
            $ crab28_starting_def = 17
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*3)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*3)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 26
            $ crab28_starting_att = 20
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 26
            $ crab28_starting_ev = 26

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 27
            $ crab28_starting_att = 21
            $ crab28_starting_def = 21
            $ crab28_starting_acc = 27
            $ crab28_starting_ev = 27

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*7)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*7)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*7)

    if rand_crab28_type ==4:
        $ crab28_type = "4"
        $ crab28_title = "julienne"
        $ crab28_element = "air"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 20
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 26
            $ crab28_starting_att = 23
            $ crab28_starting_def = 23
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 27
            $ crab28_starting_att = 24
            $ crab28_starting_def = 24
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 24

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*7)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)

    if rand_crab28_type ==5:
        $ crab28_type = "5"
        $ crab28_title = "slycer"
        $ crab28_element = "fire"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 17
            $ crab28_starting_att = 23
            $ crab28_starting_def = 17
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*3)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*3)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 20
            $ crab28_starting_att = 26
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*4)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 21
            $ crab28_starting_att = 27
            $ crab28_starting_def = 21
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 24

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*7)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)

    if rand_crab28_type ==6:
        $ crab28_type = "6"
        $ crab28_title = "clypper"
        $ crab28_element = "earth"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 20
            $ crab28_starting_att = 17
            $ crab28_starting_def = 23
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 17

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*4)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*3)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*3)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 20
            $ crab28_starting_def = 26
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 24
            $ crab28_starting_att = 21
            $ crab28_starting_def = 27
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 21

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*7)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

    if rand_crab28_type ==7:
        $ crab28_type = "7"
        $ crab28_title = "barnakel"
        $ crab28_element = "water"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 17
            $ crab28_starting_def = 26
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 17

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*3)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*3)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 26
            $ crab28_starting_att = 20
            $ crab28_starting_def = 29
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*7)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 27
            $ crab28_starting_att = 21
            $ crab28_starting_def = 30
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 21

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*7)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*8)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

    if rand_crab28_type ==8:
        $ crab28_type = "8"
        $ crab28_title = "doo'ahlai"
        $ crab28_element = "air"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 23
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 17

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*3)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 26
            $ crab28_starting_att = 26
            $ crab28_starting_def = 23
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 27
            $ crab28_starting_att = 27
            $ crab28_starting_def = 24
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 21

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*7)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*7)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

    if rand_crab28_type ==9:
        $ crab28_type = "9"
        $ crab28_title = "clawp"
        $ crab28_element = "water"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 20
            $ crab28_starting_att = 20
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*4)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 23
            $ crab28_starting_def = 23
            $ crab28_starting_acc = 23
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 24
            $ crab28_starting_att = 24
            $ crab28_starting_def = 24
            $ crab28_starting_acc = 24
            $ crab28_starting_ev = 24

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*6)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)

    if rand_crab28_type ==10:
        $ crab28_type = "10"
        $ crab28_title = "bampy"
        $ crab28_element = "earth"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 20
            $ crab28_starting_att = 17
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 17
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*4)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*3)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*3)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 20
            $ crab28_starting_def = 23
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 26

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*4)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 24
            $ crab28_starting_att = 21
            $ crab28_starting_def = 24
            $ crab28_starting_acc = 21
            $ crab28_starting_ev = 27

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*6)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*7)

    if rand_crab28_type ==11:
        $ crab28_type = "11"
        $ crab28_title = "grappy"
        $ crab28_element = "fire"
        if crab28_rarity == "n":
            $ crab28_starting_hp = 23
            $ crab28_starting_att = 23
            $ crab28_starting_def = 17
            $ crab28_starting_acc = 17
            $ crab28_starting_ev = 20

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*5)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*5)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*3)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*3)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*4)

        if crab28_rarity == "r":
            $ crab28_starting_hp = 26
            $ crab28_starting_att = 26
            $ crab28_starting_def = 20
            $ crab28_starting_acc = 20
            $ crab28_starting_ev = 23

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*6)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*6)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*4)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*4)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*5)

        if crab28_rarity == "e":
            $ crab28_starting_hp = 27
            $ crab28_starting_att = 27
            $ crab28_starting_def = 21
            $ crab28_starting_acc = 21
            $ crab28_starting_ev = 24

            $ crab28_hp = crab28_starting_hp + ((crab28_level-1)*7)
            $ crab28_att = crab28_starting_att + ((crab28_level-1)*7)
            $ crab28_def = crab28_starting_def + ((crab28_level-1)*5)
            $ crab28_acc = crab28_starting_acc + ((crab28_level-1)*5)
            $ crab28_ev = crab28_starting_ev + ((crab28_level-1)*6)
    show crab28_shuffle:
        ypos -200
    with flash

    if crab28_rarity =="n":
        "you got a normal {b}[crab28_title]{/b}!"
    if crab28_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab28_title]{/b}!"
    if crab28_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab28_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab28_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab28_name = crab28_name.strip()
            if crab28_name == "":
                $ crab28_name= crab28_title
            y "how about... [crab28_name]."
        "[crab28_title]":

            $ crab28_name = crab28_title

    jump after_crab_get

label crab29_trap_get:
    if rand_crab29_type ==1:
        $ crab29_type = "1"
        $ crab29_title = "slasher"
        $ crab29_element = "fire"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 20
            $ crab29_starting_att = 23
            $ crab29_starting_def = 17
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*4)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*3)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 26
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 24
            $ crab29_starting_att = 27
            $ crab29_starting_def = 21
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 24

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*7)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)



    if rand_crab29_type ==2:
        $ crab29_type = "2"
        $ crab29_title = "reacher"
        $ crab29_element = "water"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 20
            $ crab29_starting_att = 20
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 17

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*4)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*3)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 23
            $ crab29_starting_def = 23
            $ crab29_starting_acc = 26
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 24
            $ crab29_starting_att = 24
            $ crab29_starting_def = 24
            $ crab29_starting_acc = 27
            $ crab29_starting_ev = 21

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*7)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)



    if rand_crab29_type ==3:
        $ crab29_type = "3"
        $ crab29_title = "jacko"
        $ crab29_element = "earth"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 17
            $ crab29_starting_def = 17
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*3)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*3)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 26
            $ crab29_starting_att = 20
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 26
            $ crab29_starting_ev = 26

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 27
            $ crab29_starting_att = 21
            $ crab29_starting_def = 21
            $ crab29_starting_acc = 27
            $ crab29_starting_ev = 27

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*7)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*7)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*7)

    if rand_crab29_type ==4:
        $ crab29_type = "4"
        $ crab29_title = "julienne"
        $ crab29_element = "air"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 20
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 26
            $ crab29_starting_att = 23
            $ crab29_starting_def = 23
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 27
            $ crab29_starting_att = 24
            $ crab29_starting_def = 24
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 24

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*7)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)

    if rand_crab29_type ==5:
        $ crab29_type = "5"
        $ crab29_title = "slycer"
        $ crab29_element = "fire"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 17
            $ crab29_starting_att = 23
            $ crab29_starting_def = 17
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*3)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*3)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 20
            $ crab29_starting_att = 26
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*4)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 21
            $ crab29_starting_att = 27
            $ crab29_starting_def = 21
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 24

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*7)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)

    if rand_crab29_type ==6:
        $ crab29_type = "6"
        $ crab29_title = "clypper"
        $ crab29_element = "earth"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 20
            $ crab29_starting_att = 17
            $ crab29_starting_def = 23
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 17

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*4)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*3)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*3)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 20
            $ crab29_starting_def = 26
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 24
            $ crab29_starting_att = 21
            $ crab29_starting_def = 27
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 21

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*7)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

    if rand_crab29_type ==7:
        $ crab29_type = "7"
        $ crab29_title = "barnakel"
        $ crab29_element = "water"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 17
            $ crab29_starting_def = 26
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 17

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*3)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*3)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 26
            $ crab29_starting_att = 20
            $ crab29_starting_def = 29
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*7)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 27
            $ crab29_starting_att = 21
            $ crab29_starting_def = 30
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 21

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*7)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*8)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

    if rand_crab29_type ==8:
        $ crab29_type = "8"
        $ crab29_title = "doo'ahlai"
        $ crab29_element = "air"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 23
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 17

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*3)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 26
            $ crab29_starting_att = 26
            $ crab29_starting_def = 23
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 27
            $ crab29_starting_att = 27
            $ crab29_starting_def = 24
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 21

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*7)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*7)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

    if rand_crab29_type ==9:
        $ crab29_type = "9"
        $ crab29_title = "clawp"
        $ crab29_element = "water"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 20
            $ crab29_starting_att = 20
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*4)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 23
            $ crab29_starting_def = 23
            $ crab29_starting_acc = 23
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 24
            $ crab29_starting_att = 24
            $ crab29_starting_def = 24
            $ crab29_starting_acc = 24
            $ crab29_starting_ev = 24

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*6)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)

    if rand_crab29_type ==10:
        $ crab29_type = "10"
        $ crab29_title = "bampy"
        $ crab29_element = "earth"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 20
            $ crab29_starting_att = 17
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 17
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*4)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*3)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*3)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 20
            $ crab29_starting_def = 23
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 26

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*4)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 24
            $ crab29_starting_att = 21
            $ crab29_starting_def = 24
            $ crab29_starting_acc = 21
            $ crab29_starting_ev = 27

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*6)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*7)

    if rand_crab29_type ==11:
        $ crab29_type = "11"
        $ crab29_title = "grappy"
        $ crab29_element = "fire"
        if crab29_rarity == "n":
            $ crab29_starting_hp = 23
            $ crab29_starting_att = 23
            $ crab29_starting_def = 17
            $ crab29_starting_acc = 17
            $ crab29_starting_ev = 20

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*5)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*5)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*3)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*3)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*4)

        if crab29_rarity == "r":
            $ crab29_starting_hp = 26
            $ crab29_starting_att = 26
            $ crab29_starting_def = 20
            $ crab29_starting_acc = 20
            $ crab29_starting_ev = 23

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*6)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*6)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*4)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*4)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*5)

        if crab29_rarity == "e":
            $ crab29_starting_hp = 27
            $ crab29_starting_att = 27
            $ crab29_starting_def = 21
            $ crab29_starting_acc = 21
            $ crab29_starting_ev = 24

            $ crab29_hp = crab29_starting_hp + ((crab29_level-1)*7)
            $ crab29_att = crab29_starting_att + ((crab29_level-1)*7)
            $ crab29_def = crab29_starting_def + ((crab29_level-1)*5)
            $ crab29_acc = crab29_starting_acc + ((crab29_level-1)*5)
            $ crab29_ev = crab29_starting_ev + ((crab29_level-1)*6)
    show crab29_shuffle:
        ypos -200
    with flash

    if crab29_rarity =="n":
        "you got a normal {b}[crab29_title]{/b}!"
    if crab29_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab29_title]{/b}!"
    if crab29_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab29_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab29_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab29_name = crab29_name.strip()
            if crab29_name == "":
                $ crab29_name= crab29_title
            y "how about... [crab29_name]."
        "[crab29_title]":

            $ crab29_name = crab29_title

    jump after_crab_get

label crab30_trap_get:
    if rand_crab30_type ==1:
        $ crab30_type = "1"
        $ crab30_title = "slasher"
        $ crab30_element = "fire"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 20
            $ crab30_starting_att = 23
            $ crab30_starting_def = 17
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*4)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*3)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 26
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 24
            $ crab30_starting_att = 27
            $ crab30_starting_def = 21
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 24

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*7)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)



    if rand_crab30_type ==2:
        $ crab30_type = "2"
        $ crab30_title = "reacher"
        $ crab30_element = "water"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 20
            $ crab30_starting_att = 20
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 17

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*4)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*3)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 23
            $ crab30_starting_def = 23
            $ crab30_starting_acc = 26
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 24
            $ crab30_starting_att = 24
            $ crab30_starting_def = 24
            $ crab30_starting_acc = 27
            $ crab30_starting_ev = 21

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*7)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)



    if rand_crab30_type ==3:
        $ crab30_type = "3"
        $ crab30_title = "jacko"
        $ crab30_element = "earth"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 17
            $ crab30_starting_def = 17
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*3)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*3)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 26
            $ crab30_starting_att = 20
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 26
            $ crab30_starting_ev = 26

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 27
            $ crab30_starting_att = 21
            $ crab30_starting_def = 21
            $ crab30_starting_acc = 27
            $ crab30_starting_ev = 27

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*7)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*7)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*7)

    if rand_crab30_type ==4:
        $ crab30_type = "4"
        $ crab30_title = "julienne"
        $ crab30_element = "air"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 20
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 26
            $ crab30_starting_att = 23
            $ crab30_starting_def = 23
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 27
            $ crab30_starting_att = 24
            $ crab30_starting_def = 24
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 24

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*7)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)

    if rand_crab30_type ==5:
        $ crab30_type = "5"
        $ crab30_title = "slycer"
        $ crab30_element = "fire"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 17
            $ crab30_starting_att = 23
            $ crab30_starting_def = 17
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*3)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*3)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 20
            $ crab30_starting_att = 26
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*4)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 21
            $ crab30_starting_att = 27
            $ crab30_starting_def = 21
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 24

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*7)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)

    if rand_crab30_type ==6:
        $ crab30_type = "6"
        $ crab30_title = "clypper"
        $ crab30_element = "earth"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 20
            $ crab30_starting_att = 17
            $ crab30_starting_def = 23
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 17

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*4)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*3)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*3)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 20
            $ crab30_starting_def = 26
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 24
            $ crab30_starting_att = 21
            $ crab30_starting_def = 27
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 21

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*7)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

    if rand_crab30_type ==7:
        $ crab30_type = "7"
        $ crab30_title = "barnakel"
        $ crab30_element = "water"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 17
            $ crab30_starting_def = 26
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 17

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*3)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*3)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 26
            $ crab30_starting_att = 20
            $ crab30_starting_def = 29
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*7)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 27
            $ crab30_starting_att = 21
            $ crab30_starting_def = 30
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 21

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*7)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*8)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

    if rand_crab30_type ==8:
        $ crab30_type = "8"
        $ crab30_title = "doo'ahlai"
        $ crab30_element = "air"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 23
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 17

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*3)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 26
            $ crab30_starting_att = 26
            $ crab30_starting_def = 23
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 27
            $ crab30_starting_att = 27
            $ crab30_starting_def = 24
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 21

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*7)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*7)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

    if rand_crab30_type ==9:
        $ crab30_type = "9"
        $ crab30_title = "clawp"
        $ crab30_element = "water"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 20
            $ crab30_starting_att = 20
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*4)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 23
            $ crab30_starting_def = 23
            $ crab30_starting_acc = 23
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 24
            $ crab30_starting_att = 24
            $ crab30_starting_def = 24
            $ crab30_starting_acc = 24
            $ crab30_starting_ev = 24

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*6)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)

    if rand_crab30_type ==10:
        $ crab30_type = "10"
        $ crab30_title = "bampy"
        $ crab30_element = "earth"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 20
            $ crab30_starting_att = 17
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 17
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*4)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*3)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*3)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 20
            $ crab30_starting_def = 23
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 26

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*4)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 24
            $ crab30_starting_att = 21
            $ crab30_starting_def = 24
            $ crab30_starting_acc = 21
            $ crab30_starting_ev = 27

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*6)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*7)

    if rand_crab30_type ==11:
        $ crab30_type = "11"
        $ crab30_title = "grappy"
        $ crab30_element = "fire"
        if crab30_rarity == "n":
            $ crab30_starting_hp = 23
            $ crab30_starting_att = 23
            $ crab30_starting_def = 17
            $ crab30_starting_acc = 17
            $ crab30_starting_ev = 20

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*5)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*5)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*3)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*3)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*4)

        if crab30_rarity == "r":
            $ crab30_starting_hp = 26
            $ crab30_starting_att = 26
            $ crab30_starting_def = 20
            $ crab30_starting_acc = 20
            $ crab30_starting_ev = 23

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*6)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*6)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*4)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*4)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*5)

        if crab30_rarity == "e":
            $ crab30_starting_hp = 27
            $ crab30_starting_att = 27
            $ crab30_starting_def = 21
            $ crab30_starting_acc = 21
            $ crab30_starting_ev = 24

            $ crab30_hp = crab30_starting_hp + ((crab30_level-1)*7)
            $ crab30_att = crab30_starting_att + ((crab30_level-1)*7)
            $ crab30_def = crab30_starting_def + ((crab30_level-1)*5)
            $ crab30_acc = crab30_starting_acc + ((crab30_level-1)*5)
            $ crab30_ev = crab30_starting_ev + ((crab30_level-1)*6)
    show crab30_shuffle:
        ypos -200
    with flash

    if crab30_rarity =="n":
        "you got a normal {b}[crab30_title]{/b}!"
    if crab30_rarity =="r":
        show text "rare" at q
        "wow! you got a {color=#ff0000}rare{/color} {b}[crab30_title]{/b}!"
    if crab30_rarity =="e":
        show text "epic" at q
        "wow! you got an {color=#800080}epic{/color} {b}[crab30_title]{/b}!"


    "do you want to name it?"
    menu:
        "user input":
            $ crab30_name = renpy.input("(enter name)", allow=None, exclude='{}', length=20, with_none=None, pixel_width=None)
            $ crab30_name = crab30_name.strip()
            if crab30_name == "":
                $ crab30_name= crab30_title
            y "how about... [crab30_name]."
        "[crab30_title]":

            $ crab30_name = crab30_title

    jump after_crab_get

label after_crab_get:
    "that's a great name!"
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
    with dissolve
    if crabs_total ==1:
        "the crab scuttles into your pocket."
    if crabs_total >=2:
        "the crab went into your storage!"
    if crab_hunt or crab_hunt2:
        $ crab_hunt = False
        $ crab_hunt2 = False
        jump arena_end_level_check
    else:
        jump bk3_village_shop_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
