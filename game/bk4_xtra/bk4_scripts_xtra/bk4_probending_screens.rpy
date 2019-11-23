label bk4_post_fight_check:
    hide expression bk4_arena_circle
    hide expression bk4_arena_opp_element
    "enemy: [bk4_arena_korra_score] \nteam avatar: [bk4_arena_score]"





    if bk4_arena_korra_score > bk4_arena_score:
        kn "that... isn't good."
        scene black with dissolve
        "you lost the probending match."
        $ probending_won = False
        $ pb_money_got =20

    if bk4_arena_score >= bk4_arena_korra_score:

        if bk4_arena_korra_score == 0:
            $ pb_money_got =60
            kn "Pah. That was easy!"
        elif bk4_arena_korra_score >75:
            $ pb_money_got =25
            kn "*Pant...* you got off lucky."
        elif bk4_arena_korra_score <=25:
            $ pb_money_got =40
            kn "Poor suckers."
        elif bk4_arena_korra_score <= 50:
            $ pb_money_got =35
            kn "You landed a little damage, I suppose."
        elif bk4_arena_korra_score <= 75:
            $ pb_money_got =30
            kn "just a scratch."

        scene black with dissolve
        "you won the probending match!"
        $ probending_won = True

    $ bk4_arena_score = 0
    $ bk4_arena_korra_score = 0
    $ bk4_arena_attacks = 0
    jump bk4_after_probending



label bk4_post_fight_check2:



    if bk4_arena_korra_score > bk4_arena_score:
        kn "Pfft... I went easy on you."

    if bk4_arena_score > bk4_arena_korra_score:
        kn "I win again!"

    jump start

label probending_game_over_man:
    $ pb_money_got = 15

    jump bk4_after_probending

return

screen bk4_arena_1:
    use bk4_arena_stats
    use bk4_arena_elements

    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_blue_near.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_near.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_green_near.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_near.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_red_near.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_near.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_blue_mid.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_mid.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_green_mid.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_mid.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_red_mid.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_mid.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_blue_far.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_far.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_green_far.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_far.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]
    if bk4_arena_circle == "bk4_xtra/probending/enemies/bk4_red_far.png":
        imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_far.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_1"), SetVariable("bk4_arena_clicked", True), Return()]

    timer rand_time action [Hide("bk4_arena_1"), SetVariable("bk4_arena_korra_score", bk4_arena_korra_score+20), Return()]


screen bk4_arena_stats:
    frame:
        xminimum 150
        has vbox
        text "enemy: [bk4_arena_korra_score]"
        text "team avatar: [bk4_arena_score]"


screen bk4_arena_elements:
    add "bk4_xtra/probending/enemies/bk4_arena_key.png"
    if bk4_arena_player_element == "water":
        add "bk4_xtra/probending/enemies/bk4_arena_key_1.png"
    if bk4_arena_player_element == "earth":
        add "bk4_xtra/probending/enemies/bk4_arena_key_2.png"
    if bk4_arena_player_element == "fire":
        add "bk4_xtra/probending/enemies/bk4_arena_key_3.png"

    key "1" action [SetVariable("bk4_arena_player_element","water")]
    key "2" action [SetVariable("bk4_arena_player_element","earth")]
    key "3" action [SetVariable("bk4_arena_player_element","fire")]


    imagemap:
        idle "bk4_xtra/probending/enemies/idle_arena_keys.png"
        hotspot (300, 582, 136, 135) action [SetVariable("bk4_arena_player_element", "water")]
        hotspot (435, 583, 131, 135) action [SetVariable("bk4_arena_player_element", "earth")]
        hotspot (566, 584, 135, 132) action [SetVariable("bk4_arena_player_element", "fire")]



screen bk4_arena_elements2:
    add "bk4_xtra/probending/enemies/bk4_arena_key.png"
    if bk4_arena_player_element == "water":
        add "bk4_xtra/probending/enemies/bk4_arena_key_1.png"
    if bk4_arena_player_element == "earth":
        add "bk4_xtra/probending/enemies/bk4_arena_key_2.png"
    if bk4_arena_player_element == "fire":
        add "bk4_xtra/probending/enemies/bk4_arena_key_3.png"

    key "1" action [SetVariable("bk4_arena_player_element2","water")]
    key "2" action [SetVariable("bk4_arena_player_element2","earth")]
    key "3" action [SetVariable("bk4_arena_player_element2","fire")]


    imagemap:
        idle "bk4_xtra/probending/enemies/idle_arena_keys.png"
        hotspot (300, 582, 136, 135) action [SetVariable("bk4_arena_player_element2", "water")]
        hotspot (435, 583, 131, 135) action [SetVariable("bk4_arena_player_element2", "earth")]
        hotspot (566, 584, 135, 132) action [SetVariable("bk4_arena_player_element2", "fire")]


screen bk4_arena_elements_2:
    add "bk4_xtra/probending/enemies/bk4_arena_key.png"
    if bk4_arena_player_element == "water":
        add "bk4_xtra/probending/enemies/bk4_arena_key_1.png"
    if bk4_arena_player_element == "earth":
        add "bk4_xtra/probending/enemies/bk4_arena_key_2.png"
    if bk4_arena_player_element == "fire":
        add "bk4_xtra/probending/enemies/bk4_arena_key_3.png"


screen bk4_arena_elements_3:
    add "bk4_xtra/probending/enemies/bk4_arena_key.png"
    if bk4_arena_player_element == "water":
        add "bk4_xtra/probending/enemies/bk4_arena_key_1.png"
    if bk4_arena_player_element == "earth":
        add "bk4_xtra/probending/enemies/bk4_arena_key_2.png"
    if bk4_arena_player_element == "fire":
        add "bk4_xtra/probending/enemies/bk4_arena_key_3.png"

    key "1" action [SetVariable("bk4_arena_player_element","water")]
    key "2" action [SetVariable("bk4_arena_player_element","earth")]
    key "3" action [SetVariable("bk4_arena_player_element","fire")]


    imagemap:
        idle "bk4_xtra/probending/enemies/idle_arena_keys.png"
        hotspot (300, 582, 136, 135) action [SetVariable("bk4_arena_player_element", "water")]
        hotspot (435, 583, 131, 135) action [SetVariable("bk4_arena_player_element", "earth")]
        hotspot (566, 584, 135, 132) action [SetVariable("bk4_arena_player_element", "fire")]


    imagebutton idle "transparent.png" hover "bk4_xtra/probending/enemies/bk4_hit_near.png" xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos action [Hide("bk4_arena_elements3"), Return()]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
