init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", { 'default' : [ ('images/mouse.png', 15, 0)] })
        elif type == "mustache":
            setattr(config, "mouse", {"default": [("images/emberisland/devilmarks.png", 0, 0)]})
        elif type == "knife":
            setattr(config, "mouse", {"default": [("images/emberisland/knife_whole.png", 0, 0)]})


    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)


image crabshuffle:
    "emberisland/crab_1.png"
    0.4
    "emberisland/crab_2.png"
    0.4
    repeat

image strongcrabshuffle:
    "emberisland/strongcrab_1.png"
    0.4
    "emberisland/strongcrab_2.png"
    0.4
    repeat

image legendcrabshuffle:
    "emberisland/legendcrab_1.png"
    0.4
    "emberisland/legendcrab_2.png"
    0.4
    repeat

image bessiecrabshuffle:
    "emberisland/bessiecrab_1.png"
    0.4
    "emberisland/bessiecrab_2.png"
    0.4
    repeat

image muskycrabshuffle:
    "emberisland/muskycrab_1.png"
    0.4
    "emberisland/muskycrab_2.png"
    0.4
    repeat

image stankcrabshuffle:
    "emberisland/stankcrab_1.png"
    0.4
    "emberisland/stankcrab_2.png"
    0.4
    repeat

screen emberisland_map_day1:

    imagemap:
        ground "emberisland/bg_island_day.jpg"
        hover "emberisland/emberisland_shine.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_day1")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_day1")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_day1")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_day1")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_day1")
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_day2:

    imagemap:
        ground "emberisland/bg_island_day.jpg"
        hover "emberisland/emberisland_shine.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_day2")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_day2")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_day2")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_day2")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_day2")
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_day3:

    imagemap:
        ground "emberisland/bg_island_day.jpg"
        hover "emberisland/emberisland_shine.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_day3")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_day3")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_day3")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_day3")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_day3")
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_day4:

    imagemap:
        ground "emberisland/bg_island_day.jpg"
        hover "emberisland/emberisland_shine.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_day4")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_day4")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_day4")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_day4")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_day4")
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_night1:

    imagemap:
        ground "emberisland/bg_island_night.jpg"
        hover "emberisland/emberisland_shine_night.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_night1")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_night1")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_night1")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_night1")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_night1")


        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_night2:

    imagemap:
        ground "emberisland/bg_island_night.jpg"
        hover "emberisland/emberisland_shine_night.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_night2")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_night2")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_night2")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_night2")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_night2")


        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_night3:

    imagemap:
        ground "emberisland/bg_island_night.jpg"
        hover "emberisland/emberisland_shine_night.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_night3")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_night3")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_night3")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_night3")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_night3")


        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

screen emberisland_map_night_boat1:

    imagemap:
        ground "emberisland/bg_island_night.jpg"
        hover "emberisland/emberisland_shine_night.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("ember_party_night_boat1")
        hotspot (413, 220, 119, 119) clicked Jump("ember_shop_night_boat1")
        hotspot (355, 348, 142, 114) clicked Jump("ember_beach_night_boat1")

        hotspot (617, 446, 166, 149) clicked Jump("ember_water_night_boat1")
        hotspot (795, 275, 125, 125) clicked Jump("ember_shack_night_boat1")


        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[fmoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ember_day]"

image emberisland_cloud:
    "emberisland/emberisland_cloud.png"
    xpos 1200
    linear 7.0 xpos -720
    repeat


label ember_island_start:

    $ yn = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_neutral.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    scene white with dissolve
    show text "Ember Island\n\nfirst day"
    $ renpy.pause (1.5, hard=True)
    scene white with dissolve
    scene bg_a_island_hutday
    with dissolve
    "you carry the suitcases into the shack."
    yd "ugh, it smells like old lady."
    jump suitcase_sort

label suitcase_sort:
    $ azula_softpink = False
    $ azula_softblack = False
    $ azula_trunkred = False
    $ azula_softblue = False
    $ azula_trunkpink = False
    $ mai_softpink = False
    $ mai_softblack = False
    $ mai_trunkred = False
    $ mai_softblue = False
    $ mai_trunkpink = False
    $ ty_softpink = False
    $ ty_softblack = False
    $ ty_trunkred = False
    $ ty_softblue = False
    $ ty_trunkpink = False
    $ softpink = False
    $ softblack = False
    $ trunkred = False
    $ softblue = False
    $ trunkpink = False
    yd "alright, i've got 5 suitcases here. which should i put in azula's room?"
    menu:
        "soft bag, pink" if not softpink:
            $ softpink = True
            $ azula_softpink = True
            yd "i think this is it?"
            jump mai_suitcase_menu
        "soft bag, black" if not softblack:
            $ softblack = True
            $ azula_softblack = True
            yd "i think this is it?"
            jump mai_suitcase_menu
        "trunk, red" if not trunkred:
            $ trunkred = True
            $ azula_trunkred = True
            yd "i think this is it?"
            jump mai_suitcase_menu
        "soft bag, blue" if not softblue:
            $ softblue = True
            $ azula_softblue = True
            yd "i think this is it?"
            jump mai_suitcase_menu
        "trunk, pink" if not trunkpink:
            $ trunkpink = True
            $ azula_trunkpink = True
            yd "i think this is it?"
            jump mai_suitcase_menu

label mai_suitcase_menu:
    yd "which should i put in mai's room?"
    menu:
        "soft bag, pink" if not softpink:
            $ softpink = True
            $ mai_softpink = True
            yd "i think this is it?"
            jump ty_suitcase_menu
        "soft bag, black" if not softblack:
            $ softblack = True
            $ mai_softblack = True
            yd "i think this is it?"
            jump ty_suitcase_menu
        "trunk, red" if not trunkred:
            $ trunkred = True
            $ mai_trunkred = True
            yd "i think this is it?"
            jump ty_suitcase_menu
        "soft bag, blue" if not softblue:
            $ softblue = True
            $ mai_softblue = True
            yd "i think this is it?"
            jump ty_suitcase_menu
        "trunk, pink" if not trunkpink:
            $ trunkpink = True
            $ mai_trunkpink = True
            yd "i think this is it?"
            jump ty_suitcase_menu

label ty_suitcase_menu:
    yd "which suitcase should i put in ty lee's room?"
    menu:
        "soft bag, pink" if not softpink:
            $ softpink = True
            $ ty_softpink = True
            yd "i think this is it?"
            jump final_suitcase_menu
        "soft bag, black" if not softblack:
            $ softblack = True
            $ ty_softblack = True
            yd "i think this is it?"
            jump final_suitcase_menu
        "trunk, red" if not trunkred:
            $ trunkred = True
            $ ty_trunkred = True
            yd "i think this is it?"
            jump final_suitcase_menu
        "soft bag, blue" if not softblue:
            $ softblue = True
            $ ty_softblue = True
            yd "i think this is it?"
            jump final_suitcase_menu
        "trunk, pink" if not trunkpink:
            $ trunkpink = True
            $ ty_trunkpink = True
            yd "i think this is it?"
            jump final_suitcase_menu

label final_suitcase_menu:
    if azula_softpink:
        y "in azula's room, i've put the soft pink bag."
    if azula_softblack:
        y "in azula's room, i've put the soft black bag."
    if azula_trunkred:
        y "in azula's room, i've put the red trunk."
    if azula_softblue:
        y "in azula's room, i've put the soft blue bag."
    if azula_trunkpink:
        y "in azula's room, i've put the pink trunk."

    if mai_softpink:
        y "in mai's room, i've put the soft pink bag."
    if mai_softblack:
        y "in mai's room, i've put the soft black bag."
    if mai_trunkred:
        y "in mai's room, i've put the red trunk."
    if mai_softblue:
        y "in mai's room, i've put the soft blue bag."
    if mai_trunkpink:
        y "in mai's room, i've put the pink trunk."

    if ty_softpink:
        y "in ty lee's room, i've put the soft pink bag."
    if ty_softblack:
        y "in ty lee's room, i've put the soft black bag."
    if ty_trunkred:
        y "in ty lee's room, i've put the red trunk."
    if ty_softblue:
        y "in ty lee's room, i've put the soft blue bag."
    if ty_trunkpink:
        y "in ty lee's room, i've put the pink trunk."

    y "is this right?"
    menu:
        "reorganize the bags":
            jump suitcase_sort
        "accept":

            y "yeah, i'm done with this."
            if azula_trunkred and ty_softpink and mai_softblack:
                $ suitcases_correct = True

    y "they can sort this out later."
    y "where should i go now?"
    jump ember_first_house_menu

label ember_first_house_menu:
    menu:
        "shack":
            y "i'm currently here, and i've got to say, there's not much going on."
            y "Just me. i guess i could masturbate?"
            menu:
                "masturbate":
                    y "i'll rub one out super quick."
                    scene black with dissolve
                    "you head into a closet and try to jack off."
                    ya "ugh it smells like moth balls!"
                    "you go at your genitals furiously anyway, and finish on an old coat."
                    scene bg_a_island_hutday
                    with dissolve
                    y "whew. that was fun."
                    y "hope no one goes in there."
                    $ masturbate_in_closet = True
                    y "where to now?"
                    menu:
                        "check out island":

                            y "guess i'll check out the island."
                            jump emberday
                "check out island":

                    jump emberday
        "check out island":

            y "guess i'll check out the island."
            jump emberday


label ember_beach:
    scene bg_a_beach_01 with dissolve
    yd "now where did they-"
    y "oh, i see them."
    show asun asun02
    show asun_azulablink
    with dissolve
    y "hey girls."
    hide asun_azulablink with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "welcome, zuzu."
    a "have you come to join in the fun?"
    show asun asun01
    show asun_azulablink
    with dissolve
    a "*yaaawn*"
    a "i sure hope you didn't come here to just to watch us sunbathe."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yd "it's just a nice day."
    hide asun_azulablink with dissolve
    a "it is, isn't it..."
    show asun_tyleeblink with dissolve
    t "aahhh... i needed this!"
    m "...."
    show asun_maiblink with dissolve
    m "it's nice, i guess."
    hide asun_tyleeblink with dissolve
    t "yay! even mai's having fun!"
    show asun asun02 with dissolve
    a "i can't even remember the last time we just relaxed."
    show asun asun24 with dissolve
    a "just enjoyed the beach and the fresh air..."
    t "yeah, there's always something."
    show asun asun20 with dissolve
    stop music fadeout 2
    play music "audio/Unwritten Return.mp3"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "but how about you, zuzu?"
    a "enjoying the weather?"
    y "yeah-"
    show asun asun21 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "um..."
    show asun asun100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "zuko? what's wrong?"
    a "did you see something?"
    show asun asun24
    hide asun_maiblink
    with dissolve
    m "your face is a little red. you okay?"
    y "i'm uh..."
    show asun asun25 with dissolve
    a "yes, is something the matter, brother?"
    m "there's nothing wrong with getting a little sunburn."
    t "you burn quick, prince!"
    show asun asun26
    show asun_maiblink
    with dissolve
    yg "I'm firm... i mean, fine."
    a "yes, brother, it is a little {i}hot{/i}, isn't it?"
    y "well, uh-"
    show asun asun27 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "you seem distracted."
    a "are you sure you don't need to get {i}wet{/i}?"
    a "i certainly don't need to get any wetter."
    show asun asun101
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    hide asun_maiblink with dissolve
    m "what?"
    show asun asun23 with dissolve
    a "remember when i stepped into the water?"
    a "it only went up to my ankles, but that was plenty for the moment."
    a "i don't want to get my new suit all wet."
    t "that's what it's for though!"
    show asun asun100 with dissolve
    a "maybe some other time."
    a "i'm enjoying myself immensely right now."
    t "princess azula, you won't get a proper tan that way!"
    show asun asun20 with dissolve
    a "you know, you're absolutely right."
    show asun_azulablink with dissolve
    a "it's important to maintain even exposure."
    show asun asun27 with dissolve
    a "and expose as much skin as possible."
    a "isn't that right?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "ahh... that sun..."
    t "that's right, but..."
    a "I feel {i}very{/i} good right now..."
    m "what's wrong, zuko? you're practically drooling."
    a "what's he doing?"
    m "staring at something... intently."
    a "mmmm... good."
    t "oh! umm... princess azula... your... um..."
    a "there isn't a {i}problem{/i} is there, ty lee?"
    t "just that you're showing... i mean your... um... is on display... um...."
    t "........."
    t "it's nothing!"
    t "...it's pretty though."
    t "...but it's nothing!"
    t "oh! mai, i meant to tell you... your boobs look great!"
    m "...really?"
    t "are you kidding? i'm like, super jealous right now!"
    m "why? your breasts are nice."
    t "yeah, but yours are perky... mine are just rounder..."
    m "who's do you think are better, zuko?"
    menu:
        "mai's are better":
            $ mai_aff +=1
            y "it's close, but i like mai's."
            show asun_tyleeblink with dissolve
            t "of course you do!"
            t "you two are such a couple."
            m "...."
        "ty lee's are better":


            $ mai_aff -=1
            y "i think ty lee has the better ones, to be honest."
            m "hmph."
            m "why don't you date her, then."
            show asun_tyleeblink with dissolve
            t "well i like yours better, mai."
        "they're both great":

            y "they're both excellent."
            m "what a cop out."
            t "aw, that's no fun, prince."

    show asun asun02 with dissolve
    a "i think that's enough bickering, girls."
    show asun asun01
    hide asun_azulablink
    with dissolve
    a "besides, I know who has the best tits of the three of us."
    t "no question, your highness!"
    show asun asun02 with dissolve
    a "wait, are they..."
    show asun asun20 with dissolve
    a "i think they're playing volleyball."
    show asun asun24 with dissolve
    a "that looks interesting..."
    a "i'm going over there."
    y "i might wander a bit."
    a "don't go far, zuko."
    a "we might need you."
    $ ember = 1
    jump emberday

label volleyball:

    scene black
    scene bg_a_beach_01
    show volleyball_net
    with dissolve
    if after_beachrub:
        stop music fadeout 2
        play music "audio/District Four.mp3"
        "click on the volleyball when it appears to score a point."
        "move too slowly and the other team will score a point."
        "first team to 15 points wins!"
        show screen vstats
        $ opp_score = 0
        $ your_score = 0
        jump volleyball_game
    if ember ==3:
        show azula_idle_fl_beach with dissolve
        a "zuko! we have been challenged."
        yd "what?"
        a "to a sport!"
        yd ".....you mean volleyball?"
        a "yes, let's go."
        yd "where's mai?"
        a "i'll tell you if you play another round."
        y "....."
        y "alright."
        hide azula_idle_fl_beach with dissolve
        stop music fadeout 2
        play music "audio/District Four.mp3"
        "click on the volleyball when it appears to score a point."
        "move too slowly and the other team will score a point."
        "first team to 15 points wins!"
        show screen vstats
        $ opp_score = 0
        $ your_score = 0
        jump volleyball_game
    if ember >=11:
        show azula_idle_fl_beach with dissolve
        yd "up for a round of volleyball?"
        a "let's kill."
        hide azula_idle_fl_beach with dissolve
        stop music fadeout 2
        play music "audio/District Four.mp3"
        "click on the volleyball when it appears to score a point."
        "move too slowly and the other team will score a point."
        "first team to 15 points wins!"
        show screen vstats
        $ opp_score = 0
        $ your_score = 0
        jump volleyball_game
    else:

        show azula_idle_fl_beach with dissolve
        a "zuko. good, you're back."
        a "i want to play some volleyball."
        a "hey, beachbums! we're playing next."
        a "ty lee! get over here now!"
        hide azula_idle_fl_beach
        show azula_idle_ff_beach
        with dissolve
        a "now for our opponents..."
        a "see that girl with the silly pigtails?"
        a "when she runs towards the ball, there's the slightest hesitation of her left foot."
        show a_idle_ff_face_blink with dissolve
        a "i'm willing to bet a childhood injury has weakened her."
        show a_idle_ff_face_anger
        hide a_idle_ff_face_blink
        with dissolve
        a "keep serving the ball to her left and we'll destroy her and the rest of her team."
        hide a_idle_ff_face_anger with dissolve
        a "dismissed."
        hide azula_idle_ff_beach with dissolve
        stop music fadeout 2
        play music "audio/District Four.mp3"
        "click on the volleyball when it appears to score a point."
        "move too slowly and the other team will score a point."
        "first team to 15 points wins!"
        show screen vstats
        jump volleyball_game

label volleyball_game:
    $ randvolly = renpy.random.randint(1,7)

    if randvolly ==1:
        call screen volly1
    if randvolly ==2:
        call screen volly2
    if randvolly ==3:
        call screen volly3
    if randvolly ==4:
        call screen volly4
    if randvolly ==5:
        call screen volly5
    if randvolly ==6:
        call screen volly6
    if randvolly ==7:
        call screen volly7

label opp_scores:
    show azula_idle_fl_beach
    show a_idle_fl_face_anger
    with dissolve
    if opp_score >=15:
        a "no!"
        if after_beachrub and ember <=10:
            jump after_second_volly_lose
        if ember ==3:
            hide volleyball_net with dissolve
            jump ember3vollylose
        if ember >=11:
            hide volleyball_net with dissolve
            jump ember11vollylose
        else:
            jump volly_lose

    if opp_score ==1:
        a "zuko! get it together!"
    if opp_score ==2:
        a "your victory is temporary!"
    if opp_score ==3:
        a "that was pure luck!"
    if opp_score ==4:
        a "we let you have that out of pity!"
    if opp_score ==5:
        a "enjoy it while you can!"
    if opp_score ==6:
        a "you won't win!"
    if opp_score ==7:
        a "lucky shot!"
    if opp_score ==8:
        a "zuko, you miserable failing clod!"
    if opp_score ==9:
        a "get it together, team! i will not lose!"
    if opp_score ==10:
        a "i refuse to be beaten by these peasants!"
    if opp_score ==11:
        a "we will win this!"
    if opp_score ==12:
        a "that's enough!"
    if opp_score ==13:
        y "balls!"
        a "this is your fault!"
    if opp_score ==14:
        a "there's no more room for error, zuko! score!"

    hide azula_idle_fl_beach
    hide a_idle_fl_face_anger
    with dissolve
    jump volleyball_game

label you_scores:
    play sound "audio/air.wav"
    show azula_idle_fl_beach with dissolve
    if your_score >=15:
        $ vollywins +=1
        if after_beachrub and ember <=10:
            jump after_second_volly_win
        if ember ==3:
            hide volleyball_net with dissolve
            jump ember3vollywin
        if ember >=11:
            hide volleyball_net with dissolve
            jump ember11vollywin
        else:
            play sound "audio/whoosh.wav"
            show flamespiral
            hide volleyball_net
            with dissolve
            hide flamespiral with dissolve
            a "yes! we win!"
            jump volly_win

    if your_score ==1:
        a "take that, weaklings!"
    if your_score ==2:
        a "face our fury!"
    if your_score ==3:
        a "you will never survive this battle!"
    if your_score ==4:
        a "hah! that's what you get!"
    if your_score ==5:
        a "pathetic!"
    if your_score ==6:
        a "we will be victorious!"
    if your_score ==7:
        a "your defeat will be humiliating!"
    if your_score ==8:
        a "you will bow before us!"
    if your_score ==9:
        a "all shall burn!"
    if your_score ==10:
        a "we are unstoppable!"
    if your_score ==11:
        a "enjoy eating our dust!"
        a "er... sand!"
    if your_score ==12:
        ys "your whole team's ugly!"
        a "no, i'm doing the taunting."
        yd "can't we both-"
        a "no! and you ruined it."
        a "just serve."
    if your_score ==13:
        a "sock my cuck!"
        yd "what?"
        a "isn't that a thing?"
        y "it's \"suck my...\" nevermind."
        a "suck my cuck!"
        yd "no, that's not..."
        y "it's fine. whatever."
    if your_score ==14:
        a "your doom is imminent!"
    hide azula_idle_fl_beach with dissolve
    jump volleyball_game

label volly_win:
    $ vollywin = True
    hide screen vstats
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg"
    show a_idle_fl_face_anger with dissolve
    a "yes! we defeated you for all time!"
    a "you will never rise from the ashes of your shame and humiliation!"
    hide a_idle_fl_face_anger with dissolve
    yd "...."
    a "well, that was fun."

    yc "you... hit the ball so hard it exploded."
    yd "you exploded the net, too."
    yd "everything exploded."
    yd "that's not normal. we're not normal."
    show a_idle_fl_face_blink with dissolve
    a "of course we're not normal."
    a "we're powerful."
    hide a_idle_fl_face_blink with dissolve
    a "so. what next?"
    show tylee_idle_ff_beach:
        xpos -250
    with dissolve
    t "hey! a couple guys just invited us to a party tomorrow night!"
    show mai_fl_flip:
        xpos 100
    with dissolve
    m "it looked like they were just inviting ty lee."
    show a_idle_fl_face_blink with dissolve
    a "obviously, you're disoriented from that match."
    a "they were clearly inviting me."
    a "but i'm happy to let you all tag along."
    t "that's great! we're gonna have fun!"
    t "but... there's some cute boys over there..."
    t "I think i'm gonna sunbathe some more."
    hide a_idle_fl_face_blink with dissolve
    a "i'll join you. i might even let them fan me."
    t "fun!"
    hide tylee_idle_ff_beach
    show a_idle_fl_face_blink
    with dissolve
    a "have fun, you two..."
    hide a_idle_fl_face_blink
    hide azula_idle_fl_beach
    with dissolve
    hide mai_fl_flip
    show mai_idle_ff_beach
    with dissolve
    m "well, that was... um."
    y "yeah."
    m "so... what do you want to do now?"
    m "want to talk for a bit?"
    y "sure."
    m "..........."
    m ".........."
    y "are... you going to talk?"
    show mai_idle_ff_blush
    m "i'm just... not very good at it i guess."
    m "i mean, what do people normally talk about?"
    yd "themselves, i guess."
    y "tell you what, my memory is still bad... why don't you tell me about yourself?"

    if not_interested_mai:
        m "I thought you weren't interested in me..."
        y "Look, I'm sorry about that. I was just... really agitated at the time."
        y "But it's just the two of us here now on a sunny beach so why not try and enjoy ourselves?"
        m "fine, but there's really not much to tell."
    else:
        "there's not much."

    jump mai_convo_questions

label mai_convo_questions:
    if mai_convo_question1 and mai_convo_question2 and mai_convo_question3:
        jump after_mai_convo_questions
    else:
        menu:
            "ask her what she likes" if not mai_convo_question1:
                y "well, what do you like?"
                m "not much. i don't really go in for the cutsie things like ty lee."
                m "i guess i over-analyze sometimes..."
                m "i don't know, i'm not very interesting."
                m "maybe we should just sit here."
                $ mai_convo_question1 = True
                jump mai_convo_questions

            "ask about the shop" if not mai_convo_question2:
                y "um... how's the shop?"
                m "it's fine."
                m "i'd like to expand at some point maybe, but that's not likely."
                y "why not?"
                m "don't have the money."
                yd "don't you come from one of the richest families in the fire nation?"
                m "yeah, but... i'm trying to make it on my own. do something for myself."
                m "branch out."
                m "i hate feeling like i'm stuck."
                m "like i owe it to someone to stay still."
                m "i want to see the world..."
                m "that's partly why i travel with azula."
                y "oh."
                $ mai_convo_question2 = True
                jump mai_convo_questions

            "ask her about guys" if not mai_convo_question3:
                y "so... what do you want in a guy?"
                m "someone to just... be with."
                m "makes life slightly less boring."
                m "isn't into me just for my looks or whatever."
                y "sure."
                $ mai_convo_question3 = True
                jump mai_convo_questions

label after_mai_convo_questions:
    y "huh."
    m "what?"
    y "nothing. i just... don't have anything else to say."
    y "it's nice to have your company."
    y "i'm glad we all came out here."
    m "..........."
    m "..........."
    yd "what?"

    if not_interested_mai:
        m "Maybe... "
        m "Maybe... this little trip is exactly what we needed."
    else:
        m "you like me, right?"
        y "obviously."

    m "i have a favor to ask, but if you don't want to, that's fine..."
    yd "what is it?"
    m "i've never..."
    yd "what?"
    m "...i've never had someone be romantic with me."
    yd "......"
    show mai_idle_ff_blink with dissolve
    m "would you get me a flower, zuko?"
    menu:
        "of course":
            y "seriously?"
            y "sure, i can do that."
            hide mai_idle_ff_blink
            hide mai_idle_ff_blush
            show mai_idle_ff_smile
            show mai_idle_ff_blush
            with dissolve
            m "really?"
            m "well, i'll, um... be over there. under the umbrella."
            m "i'm getting tired of all this sun."
            hide mai_idle_ff_smile
            hide mai_idle_ff_blush
            hide mai_idle_ff_beach
            with dissolve
            jump mai_flower_hunt
        "no, that's lame":

            y "hahaha, yeah, right."
            yd "oh, you're serious?"
            y "no, not happening."
            show mai_idle_ff_angry with dissolve
            m "you're horrible."
            m "i can't believe i was going to......."
            m "you can forget it now!!"
            m "big mistake, zuko."
            hide mai_idle_ff_blush
            hide mai_idle_ff_angry
            hide mai_idle_ff_beach
            hide mai_idle_ff_blink
            with dissolve
            jump not_mai_flower_hunt


label volly_lose:
    hide screen vstats
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg"
    show a_idle_fl_face_anger with dissolve
    a "that was not a test of skill, but of luck."
    a "we let them win."
    hide a_idle_fl_face_anger
    with dissolve
    a "well, what next then?"
    show tylee_idle_ff_beach:
        xpos -200
    with dissolve
    t "hey! a couple guys just invited us to a party tomorrow night!"
    show mai_fl_flip:
        xpos 200
    with dissolve
    m "it looked like they were just inviting ty lee."
    show a_idle_fl_face_blink with dissolve
    a "obviously, you're disoriented from that match."
    a "they were clearly inviting me."
    a "but i'm happy to let you all tag along."
    t "that's great! we're gonna have fun!"
    t "but... there's some cute boys over there..."
    t "I think i'm gonna sunbathe some more."
    hide a_idle_fl_face_blink with dissolve
    a "i'll join you. i might even let them fan me."
    t "fun!"
    hide tylee_idle_ff_beach
    show a_idle_fl_face_blink
    with dissolve
    a "have fun, you two..."
    hide a_idle_fl_face_blink
    hide azula_idle_fl_beach
    with dissolve
    hide mai_fl_flip
    show mai_idle_ff_beach
    with dissolve
    m "well, that was... um."
    y "yeah."
    m "so... what do you want to do now?"
    m "want to talk for a bit?"
    y "sure."
    m "..........."
    m ".........."
    y "are... you going to talk?"
    show mai_idle_ff_blush
    m "i'm just... not very good at it i guess."
    m "i mean, what do people normally talk about?"
    yd "themselves, i guess."
    y "tell you what, my memory is still bad... why don't you tell me about yourself?"
    m "there's not much."
    jump mai_convo_questions

label mai_flower_hunt:
    yd "hmm... wonder where i should look for this flower?"
    $ ember = 2
    jump emberday


label not_mai_flower_hunt:
    y "don't really have anything to do, now..."
    y "maybe i should get a flower for her..."
    menu:
        "look for a flower":
            jump mai_flower_hunt
        "don't look for a flower":

            jump really_not_mai_flower_hunt

label really_not_mai_flower_hunt:
    y "nah, i really don't like her."
    y "I'll just chill on the beach until evening..."
    scene black with dissolve
    "you hang out on the beach until it's dark."
    "you get the sense that you missed out on something awesome, but have no idea what."
    "you also feel like you're going to miss out on a lot of good things that were to come."
    "but that's the cost of free will."
    "you can fuck up tremendously."
    yc "*sigh...* shit."
    "you run into mai as you walk down the beach."
    scene bg_a_beach_01
    show background_fade_purpleish
    show blackveil
    show mai_idle_fl_beach
    with dissolve
    m "hey."
    y "hi."
    m "they're waiting on us."
    hide mai_idle_fl_beach with dissolve
    "you follow mai to where azula and ty lee are already sitting."
    jump ember_first_night

label ember11vollylose:
    hide screen vstats
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg"
    show a_idle_fl_face_anger with dissolve
    a "we lost!"
    a "we let them win."
    hide a_idle_fl_face_anger
    with dissolve
    a "well, whatever."
    a "up for another match?"
    menu:
        "play again":
            jump volleyball
        "don't play again":

            y "no thanks."
            jump ember_beach_day3

label ember11vollywin:
    hide screen vstats
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg"
    if volleybutt_start:
        $ volleybutt +=1
    menu:
        "play again":
            jump volleyball
        "don't play again":

            y "no thanks."
            jump ember_beach_day3

label ember3vollylose:
    hide screen vstats
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg"
    show a_idle_fl_face_anger with dissolve
    a "we lost!"
    a "we let them win."
    hide a_idle_fl_face_anger
    with dissolve
    a "well, what did you want again?"
    y "where's mai?"
    a "oh, she's a little farther down the beach."
    yd "why didn't you just say so?"
    a "because i don't have to do anything, zuko."
    hide azula_idle_fl_beach with dissolve
    $ ember = 4
    menu:
        "go look down the beach for mai":
            jump mai_first_bj

label ember3vollywin:
    hide screen vstats
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg"
    a "we won!"
    a "which was inevitable."
    a "well, what did you want again?"
    y "where's mai?"
    a "oh, she's a little farther down the beach."
    yd "why didn't you just say so?"
    a "because i don't have to do anything, zuko."
    hide azula_idle_fl_beach with dissolve
    $ ember = 4
    menu:
        "go look down the beach for mai":
            jump mai_first_bj

label mai_first_bj:
    show mai_idle_fl_beach with dissolve
    y "hey! i was looking for you!"
    m "...why?"
    y "i got you a flower."
    "you give mai the flower."
    show mai_idle_fl_smile
    show mai_idle_fl_blush
    with dissolve
    m "........"
    m "you can be sweet when you try, zuko."
    hide mai_idle_fl_smile
    hide mai_idle_fl_blush
    hide mai_idle_fl_beach
    show mai_idle_ff_beach
    show mai_idle_ff_smile
    show mai_idle_ff_blush
    with dissolve
    m "so i decided that if you did bring me a flower..."
    m "i'd do something for you."
    m "but first..."
    m "can you... say something sweet?"
    menu:
        "you're hot":
            y "you are one sexy mama."
            hide mai_idle_ff_smile with dissolve
            $ mai_romance_questions =0
            m "is that the best you can do?"
            jump mai_romance1
        "the stars aligned and created you with their glow":

            y "you shine like you're out of this world."
            hide mai_idle_ff_smile with dissolve
            $ mai_romance_questions =0
            m "come on, that's too sugary."
            m "...it's like you don't know me at all."
            jump mai_romance1
        "things suck less when you're around":

            y "i hate things less when i see you."
            $ mai_romance_questions =1
            m "same here!"
            jump mai_romance1

label mai_romance1:
    m "what else?"
    menu:
        "your spontaneity and love of life always surprises me":
            y "you're wild and joyful, and i admire that."
            hide mai_idle_ff_blush
            show mai_idle_ff_angry
            show mai_idle_ff_blush
            with dissolve
            m "i'm not crazy or wild, zuko."
            m "i'm certainly not joyful."
            jump mai_romance2
        "your violence scares and excites me... we could become outlaws":

            y "we could commit crimes together."
            hide mai_idle_ff_blush
            show mai_idle_ff_angry
            show mai_idle_ff_blush
            with dissolve
            m "think carefully, zuko."
            m "have i ever actually hurt anyone?"
            m "no. and i serve azula, the princess."
            m "i'm not interested in either of those."
            m "i got good at throwing knives for fun."
            jump mai_romance2
        "i've always admired your love of freedom and adventure":

            $ mai_romance_questions +=1
            y "your desire for freedom and adventure has always appealed to me."
            hide mai_idle_ff_blush
            show mai_idle_ff_smile
            show mai_idle_ff_blush
            with dissolve
            m "it's true, i hate the idea of being captive."
            jump mai_romance2

label mai_romance2:
    if mai_romance_questions ==2:
        $ mai_aff +=2
        m "you almost know me better than i know myself."
    if mai_romance_questions ==1:
        m "you don't know me as well as I'd hoped... but that's really okay, i know you have amnesia."
        m "you still know me pretty well."
    if mai_romance_questions ==0:
        m "you don't know me at all."
        m "That amnesia really did a number on you."
        m "Much worse than I had feared."
        m "Well, we'll just have to take the time we have here on this island to get to know each other again."

    m "now {i}i'm{/i} going to do something... nice."
    show mai_idle_ff_blink with dissolve
    m "i want you to..."
    hide mai_idle_ff_smile
    hide mai_idle_ff_blink
    with dissolve
    m ".........."
    m "take off your pants, zuko."
    y "really?"
    with vshake
    yn "{size=+6}done!"
    show mai_idle_ff_smile
    hide mai_idle_ff_blush
    show mai_idle_ff_blush
    with dissolve
    m "that was fast..."
    m "now... sit."
    stop music fadeout 2
    play music "audio/Unwritten Return.mp3" fadein 2
    scene black
    show mabj mabj22
    with dissolve
    m "*deep breath*"
    m "here we go..."
    show mabj mabj23 with dissolve
    m_l "i hope no one sees..."
    scene black with dissolve
    "mai lays down in the sand in front of you..."
    show mabj mabj01 with Dissolve(0.8)
    m "{size=-4}(...i can't believe it...it's perfect...)"
    show mabj_eyesup with dissolve
    m "zuko..."
    m "i'm..."
    hide mabj_eyesup with dissolve
    m "...happy i'm here with you."
    m "this almost doesn't seem real, does it?"
    show mabj_eyesup with dissolve
    m "we've been dancing around this for years..."
    m ".........."
    hide mabj_eyesup
    show mabj mabj02
    with dissolve
    m "i've wanted to try this for so long."
    m "today it all starts coming true..."
    show mabj mabj100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "have you..."
    show mabj_unsure with dissolve
    m "thought about me, too?"
    m "like this?"
    ynd "are you kidding?!"
    yn "since i first saw you!"
    show mabj_smile
    hide mabj_unsure
    with dissolve
    m "oh, zuko..."
    m "i've stayed... true. waiting for you."
    show mabj_unsure
    hide mabj_smile
    with dissolve
    m "you have too, right...?"
    menu:
        "pure as snow, baby":
            $ mai_aff+=1
            yn "of course."
            yn "it's you and me, you know that."
            hide mabj_unsure
            show mabj_smile
            with dissolve
            m "oh, zuko..."
        "maybe?":

            $ mai_aff -=1
            yn "kind of... hard to remember?"
            yn "we've also been apart for a long time..."
            show mabj_angry
            hide mabj_unsure
            with dissolve
            m "what?"
            yn "i'm kidding."
            yn "except about the memory thing."
            m "...you're such an asshole."
            yn "but i'm your asshole."
            hide mabj_angry
            show mabj_unsure
            with dissolve
            m "...."
            hide mabj_unsure
            show mabj_smile
            with dissolve
            m "you are, aren't you?"

    show mabj mabj05
    hide mabj_smile
    with dissolve
    m "....."
    play sound "audio/lick_b.mp3"
    m "*lick*"
    m "......"
    play sound "audio/gulp2.mp3"
    show mabj mabj06 with dissolve
    m "*gulp*"
    show mabj mabj101
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "*slurp* *gulp*"
    ync "hnngh..."
    m "*mmmmmm*"
    ync "your mouth feels incredible, mai...."
    m "*mmmm* *sluurp* *gltch*"
    m "*slurp* *gulp* *slurp*"
    ync "i've wanted to fuck your mouth for so long...."
    m "'ee 'oo..."
    show mabj mabj102
    m "how's it 'eel, prince?"
    yn "unbelieveable!"
    m "'ood..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "hgh..."
    yn "how are you so good at this?"
    m "i 'acticed on toys..."
    m "'or years...."
    m "*slurrp* *gulp* *slurrp*"
    m "'aiting..."
    m "'or you..."
    yn "you're sucking it right out--"
    show mabj mabj103
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yna "fuck, mai!"
    m "you like this right?"
    show mabj_unsure with dissolve
    m "boys like girls jacking their... cocks, right?"
    m "am i milking you right?"
    show mabj_angry
    hide mabj_unsure
    with dissolve
    m "i'm going to get this cum out."
    m "you're going to be mine, zuko."
    m "no one else's."
    show mabj_unsure
    hide mabj_angry
    with dissolve
    m "right?"
    ync "hhgngh..."
    m "this feels great, right? and you'll just be mine, right?"
    ync "y-yes..."
    hide mabj_unsure with dissolve
    m "fine."
    show mabj mabj104
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "'um 'or 'ee!"
    yn "w-what?"
    m "'um!"
    yn "i don't..."
    m "{size=+4}cum!!"
    m "'um in my 'outh!"
    m "i 'ant it!"
    m "i'll suck it 'ight out!!"
    yn "oh, shit... i think... i think some people are watching..."
    m "'um 'ickly!"
    m "*mmmmmm!!!*"
    "mai relentlessly bobs and gulps on your cock, determined to suck the load out of you..."
    "her lips and tongue slide lightly down your shaft and {i}sluuurp{/i} hard on the way up."
    m "*slurrrp* *slurrp* *gltch* *slurp* *gulp*"
    "she forces your cock down her throat without break as her wet, sloppy suction brings you to the brink."
    m "*gulp* *slurp* *sluuurrrp*"
    yna "ohhh... here it comes!"
    "as a little of her spit dribbles down your shaft, mai moans and sucks mercilessly, repeatedly plunging your full length into her mouth."
    yna "i'm gonna fucking nut!"
    m "*mmmm!!!* *mmmmmmm!!!!!!*"
    menu:
        "cum in mouth":
            show mabj mabj08 with Dissolve(0.2)
            show mabj mabj09 with Dissolve(0.2)
            show mabj mabj10 with Dissolve(0.2)
            show mabj mabj11 with Dissolve(0.2)
            yna "ngh!"
            play sound "audio/splurt2.ogg"
            show mabj mabj12
            with flash
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp*"
            play sound "audio/splurt3.ogg"
            show mabj mabj13
            with flash
            play sound "audio/gulp2.mp3"
            m "*mmmm!!!!!*"
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp* *gulp* *gulp*"
            play sound "audio/splurt3.ogg"
            show mabj mabj14
            with flash
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            play sound "audio/splurt1.ogg"
            with flash
            yna "fuck! i can't stop!"
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp* *gulp* *gulp*"
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp*"
            m "...................."
            show mabj mabj15 with dissolve
            m "*gasp*"
            m "so 'uch 'um!"
            m "can't breathe...."
            show mabj_blink with Dissolve(0.2)
            play sound "audio/gulp2.mp3"
            m "{size=+5}*gulp!*"
            show mabj_eyesup
            hide mabj_blink
            with dissolve
            m "that... was so much..."
            m "i wasn't... i didn't... i wasn't expecting that..."
            show mabj mabj15_1 with dissolve
            m "do you... feel better?"
            m "did i do well?"
            yn "that was amazing...."
            show mabj mabj15_3 with dissolve
            m "good."
            show mabj mabj15_4
            with dissolve
            m "don't expect that all the time, though!"
            ynd "what?"
            m "i'm not a slut!"
            show mabj mabj15_1
            with dissolve
            m "i'm just... i'm not a slut and i don't want you to think less of me."
            yn "but i won't!"
            yn "i'll think better of you!"
            hide mabj_eyesup
            show mabj mabj15
            with dissolve
            m "you're sweet zuko, but... let's just take it a little slower, okay?"
            yn "is this because you almost drowned in cum?"
            m "no..."
            scene black
            with dissolve
            "mai gets dressed and wipes the cum off her face."
            scene bg_a_beach_01
            show blackveil
            show mai_idle_fl_beach
            show mai_idle_fl_blush
            with dissolve
            m "we've been gone awhile. let's go meet the others."
            ync "wait..."
            ynd "what did you mean by the \"going slower\" thing?"
            hide mai_idle_fl_blush
            hide mai_idle_fl_beach
            show mai_idle_ff_beach
            show mai_idle_ff_blush
            with dissolve
            m "let's not do this now. you just came, didn't you? you had fun, right?"
            ynd "well, yeah..."
            m "well, just keep that memory."
            show mai_idle_fl_beach
            show mai_idle_fl_blush
            hide mai_idle_ff_beach
            hide mai_idle_ff_blush
            with dissolve
            m "come on, it's getting late."
            hide mai_idle_fl_beach
            hide mai_idle_fl_blush
            with dissolve
            $ ember = 5
            jump embernight
        "cum on face":

            show mabj mabj103
            m "are you-"
            yna "ngh!"
            play sound "audio/splurt2.ogg"
            show mabj mabj16
            with flash
            m "oh!"
            play sound "audio/splurt3.ogg"
            show mabj mabj17
            with flash
            m "*mmmmm* ....that's it, my prince..."
            m "get it all out..."
            m "use my face... like..."
            m "...like a cumrag, zuko!"
            play sound "audio/splurt3.ogg"
            show mabj mabj18
            with flash
            play sound "audio/splurt3.ogg"
            show mabj mabj18
            with flash
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            yna "fuck! it's so good!"
            m "...................."
            show mabj_eyesup
            with dissolve
            m "there's... so much on me..."
            m "i wasn't... i didn't... i wasn't expecting that..."
            m "it's... so warm. and sticky."
            m "...i can feel it dripping down my cheeks."
            show mabj mabj15_2 with dissolve
            m "do you... feel better?"
            m "did i do well?"
            yn "that was amazing...."
            show mabj mabj15_5 with dissolve
            m "good."
            show mabj mabj15_6
            with dissolve
            m "don't expect that all the time, though!"
            ynd "what?"
            m "i'm not a slut!"
            show mabj mabj15_2
            with dissolve
            m "i'm just... i'm not a slut and i don't want you to think less of me."
            yn "but i won't!"
            yn "i'll think better of you!"
            hide mabj_eyesup
            show mabj mabj15_7
            with dissolve
            m "you're sweet zuko, but... let's just take it a little slower, okay?"
            ynd "is this because you're soaked in cum?"
            m "no..."
            scene black with dissolve
            "mai gets dressed and wipes the cum off her face."
            scene bg_a_beach_01
            show blackveil
            show mai_idle_fl_beach
            show mai_idle_fl_blush
            with dissolve
            m "we've been gone awhile. let's go meet the others."
            ync "wait..."
            ynd "what did you mean by the \"going slower\" thing?"
            hide mai_idle_fl_blush
            hide mai_idle_fl_beach
            show mai_idle_ff_beach
            show mai_idle_ff_blush
            with dissolve
            m "let's not do this now. you just came, didn't you? you had fun, right?"
            ynd "well, yeah..."
            m "well, just keep that memory."
            show mai_idle_fl_beach
            show mai_idle_fl_blush
            hide mai_idle_ff_beach
            hide mai_idle_ff_blush
            with dissolve
            m "come on, it's getting late."
            hide mai_idle_fl_beach
            hide mai_idle_fl_blush
            with dissolve
            $ ember = 5
            jump embernight

label ember_first_night:
    menu:
        "explore the island a little more":
            $ ember = 5
            jump embernight
        "find the girls":

            jump ember_first_night_cont

label ember_first_night_cont:
    stop music fadeout 2
    scene black
    show azft azft03
    with dissolve
    play music "audio/Doctor_Turtle_-_04_-_Im_What_Youd_Be_Without_Her_Long_Version.mp3"
    t "it's about time you slowpokes got here!"
    a_beach "it is, isn't it? i wonder what kept you?"
    m_ "tell them, zuko."
    menu:
        "fish":
            y "trout."
            t "neat!"
            a_beach "what?"
            m_ "what?"
            y "we were... fishing?"
            y "and, uh, this big one just came out and slapped mai."
            m_ "zuko...."
            ya "and i was all \"agh! damn you fish! you can't do that to mai!\""
            y "so i got ready to punch it, all lying there smugly on the sand..."
            y "but mai grabbed my arms all \"it's not worth it!\" and i was all \"it's totally worth it for you, babe!\""
            ya "\"i'd fight any fish! tuna, bass, you name it! i'm not letting it get away with that!\""
            y "but of course mai was gripping my hands, so i did what any reasonable man would do..."
            y "and i kneeled down and beat that bastard trout to death with my bait and tackle."
            m_ ".........."
            t "your... literal bait and tackle? like from a tacklebox?"
            yg "no."
            t "......that poor fish."
            m_ "it didn't happen, zuko is an idiot."
            m_ "we just went for a walk."
        "wind":

            y "i was getting blown."
            m_ "zuk-"
            y "by the wind."
            m_ "....."
            a_beach "you don't say?"
            y "yeah, it got a little wild out there, my body was thrusting like crazy."
            t "oh, no!"
            y "yeah... took a load out of me, blowing like that."
            m_ "............."
            y "at one point, i got snagged on a tree."
            y "but eventually i got off."
            y "i came as quick as i could."
            y "and now we're here."
            a_beach "what an interesting tale. anything to add, mai?"
            m_ "......."
            m_ "just that zuko is an idiot."
            m_ "we just went for a walk."

    a_beach "very interesting."
    a_beach "mai, come get some more firewood with me."
    m_ "well, i-"
    a_beach "i wasn't asking."
    show azft azft04 with dissolve
    "mai and azula get up and walk off."
    y "uh... hey, ty lee. guess it's just us for the moment, huh?"
    y "how's your trip going?"
    t "great!"
    t "i'm having so much fun here!"
    t "we never get to go to the beach!"
    t "i love travelling with princess azula, but it's usually to really boring places."
    t "or like... swampy."
    t "so this is great!"
    t "how about you?"
    y "i'm good. i wonder what they're talking about?"
    t "i don't know."
    y "well i'm bored."
    t "oh... um... we could... hey! wanna play a game?"
    menu:
        "play":
            y "sure, why not?"
        "don't play":

            y "nah, maybe some other time."
            t "aw, okay..."
            jump after_ty_guess

    t "i'm thinking of a number between 1 and 5."
    t "guess the number!"
    yd "that's not a game."
    t "come on..."
    y "well, alright."
    $ rand_tynumber = renpy.random.randint(1, 5)
    menu:
        "1":
            y "is it 1?"
            if rand_tynumber ==1:
                t "yes! how did you know?"
                jump ty_guess_win
            else:
                t "aw, no. tough luck."
                jump after_ty_guess
        "2":
            y "is it 2?"
            if rand_tynumber ==2:
                t "yes! how did you know?"
                jump ty_guess_win
            else:
                t "aw, no. tough luck."
                jump after_ty_guess
        "3":
            y "is it 3?"
            if rand_tynumber ==3:
                t "yes! how did you know?"
                jump ty_guess_win
            else:
                t "aw, no. tough luck."
                jump after_ty_guess
        "4":

            y "is it 4?"
            if rand_tynumber ==4:
                t "yes! how did you know?"
                jump ty_guess_win
            else:
                t "aw, no. tough luck."
                jump after_ty_guess
        "5":
            y "is it 5?"
            if rand_tynumber ==5:
                t "yes! how did you know?"
                jump ty_guess_win
            else:
                t "aw, no. tough luck."
                jump after_ty_guess

label ty_guess_win:
    y "great! so what do i win?"
    t "um... win?"
    y "yeah."
    t "i don't know."
    t "umm...."
    t "well..."
    t "i could give you some information..."
    t "...or you could see my tits?"
    t "which would you prefer?"
    menu:
        "information":
            t "okay!"
            t "well... ever since i was a little girl, i had trouble sleeping."
            t "so i use a... sleep aid."
            t "i can't sleep without it."
            yd "huh. what, uh... what's your \"sleep aid\" look like?"
            t "well... it's purple..."
            yg "nice."
            t "since you won, it's only fair that i remind you again..."
            t "i can't sleep without it."
            t "so if i'm asleep..."
            t "well, use that information how you'd like!"
            jump after_ty_guess
        "tits":

            t "okay!"
            t "you probably shouldn't tell mai though."
            t "she might get mad."
            t "well..."
            t "um..."
            t "here i go..."
            t "or, here {i}they{/i} go, i guess..."
            show azft azft04_1 with dissolve
            t "so? what do you think?"
            t "they're great, right?"
            y "yeah."
            t "believe it or not, azula plays with them all the time."
            t "oh! they're coming back!"
            show azft azft04 with dissolve
            jump after_ty_guess

label after_ty_guess:
    a_beach "well... that was a very {i}informative{/i} talk, mai."
    m_ "but-"
    show azft azft03 with dissolve
    a_beach "you've talked enough, i think."
    a_beach "zuko? come with me."
    yd "where's the firewood?"
    a_beach "what?"
    yd "you said-"
    a_beach "there wasn't any. now come with me."
    show azft azft03_1 with dissolve
    "as you pass mai, she gives you an inscrutable look."
    show azft azft03_2 with dissolve
    "you can tell she means something, but have no idea what."
    scene black
    with dissolve
    "you walk to where azula is waiting."
    scene bg_a_beach_01
    show background_fade_purpleish
    show blackveil
    show azula_idle_fl_beach
    with dissolve
    a "so."
    a "mai told me all about it."
    y "all about what?"
    show a_idle_fl_face_blink with dissolve
    a "don't be coy, brother."
    a "you do it terribly."
    hide a_idle_fl_face_blink with dissolve
    a "so, would you like to confess to your little sister?"
    y "why are you so interested?"
    show a_idle_fl_face_unsure with dissolve
    a "who says i'm interested?"
    hide a_idle_fl_face_unsure
    show a_idle_fl_face_blink
    with dissolve
    a "i'm just trying to keep our little party playing by the same rules."
    a "besides, i already know everything."
    a "did you forget that i spoke with mai already?"
    a "tell me, and i'll..."
    a "...i'll let you see my breasts."
    a "how's that for incentive?"
    if mai_flower_got:
        menu:
            "confess":
                y "alright, you wanna know what happened?"
                y "mai sucked me off. right there on the beach."
                show a_idle_fl_face_anger with dissolve
                a "i knew it!"
                a "mai wouldn't say anything, but i could tell!"
                a "that whore!"
                a "you're off with her..."
                hide a_idle_fl_face_anger with dissolve
                a "....which is fine, of course."
                a "i was just curious is all."
                a "well."
                a "lets get back to the party, hmm?"
                y "what about your tits?"
                a "are you sure you want that?"
                y "...yeah."
                a "say, \"please take your top off for me, sister.\""
                yd "...please take your top off for me... sister."
                a "very well. but only because you asked so nicely."
                hide azula_idle_fl_beach
                show a_idle_fl_nude
                show azula_idle_fl_beach_bottoms
                with dissolve
                show ctcblink
                $ renpy.pause()
                hide ctcblink
                a "finished leering at my bare chest, brother?"
                a "done staring at your little sister's tits?"
                a "i think you've had enough for now."
                show azula_idle_fl_beach
                hide a_idle_fl_nude
                hide azula_idle_fl_beach_bottoms
                with dissolve
                a "time to get back."

                $ told_azula_about_mai = True
                jump after_azula_inquisition
            "play dumb":

                y "nothing happened."
                show a_idle_fl_face_anger with dissolve
                a "i know it did!"
                a "mai didn't say anything either, but i can tell!"
                a "that whore!"
                a "you're off with her..."
                hide a_idle_fl_face_anger with dissolve
                a "....which is fine, of course."
                a "i'm just curious is all."
                a "well."
                a "lets get back to the party, hmm?"
                jump after_azula_inquisition
    else:
        yd "nothing happened."
        yd "really."
        show a_idle_fl_face_anger with dissolve
        a "i know it did!"
        a "mai didn't say anything either, but i can tell!"
        a "that whore!"
        a "you're off with her..."
        hide a_idle_fl_face_anger with dissolve
        a "....which is fine, of course."
        a "i'm just curious is all."
        a "well."
        a "lets get back to the party, hmm?"
        jump after_azula_inquisition



label after_azula_inquisition:
    if mai_flower_got:
        scene black with dissolve
        "as you return to the fire, mai greets you quickly."
        scene bg_a_beach_01
        show background_fade_purpleish
        show blackveil
        show mai_idle_ff_beach
        with dissolve
        m "you didn't say anything, did you?"
        if told_azula_about_mai:
            y "oh. um."
            y "i... might have."
            show mai_idle_ff_angry with dissolve
            m "you jerk!"
            y "look, it's not a big deal."
            y "she suspected anyway."
            yd "kind of angrily..."
            y "but nothing i could have said would have convinced her otherwise."
            m "......"
            m "i guess...."
            m "but i still wish you hadn't."
            m "oh, well."
            m "let's go sit."
            $ mai_aff -=1
        else:
            y "no, of course not!"
            show mai_idle_ff_smile with dissolve
            m "oh. good."
            y "not that it really matters, she suspects anyway."
            yd "kind of angrily...."
            y "but anyway."
            m "i'm glad you kept it secret, even if it doesn't affect anything."
            m "you cared enough to protect my privacy, and i really appreciate that, zuko."
            m "let's go sit."

    show azft azft04 with dissolve
    show azft azft03 with dissolve
    a_beach "well, we're all back."
    t "you guys were gone forever."
    t "quit leaving me!"
    a_beach "don't be impatient, ty lee."
    a_beach "some things have come to my attention that had to be addressed."
    t "like what?"
    a_beach "nothing you need to worry about."
    a_beach "why are we sitting around an unlit fire?"
    a_beach "what are we, peasants? here."
    play sound "audio/whoosh.wav"
    show azft_fireshadows
    stop music
    play music "audio/Fire2.mp3"
    yd "whoa!"
    a_beach "isn't that better?"
    y "oh, yeah... warming my tootsies right up."
    m_ "....what?"
    a_beach "...anyway..."
    a_beach "how's everyone enjoying themselves?"

    if mai_flower_got:
        m_l "it's been... nice so far."
    else:
        m_ "it's been... boring."

    y "yeah, it has."
    a_beach "........."

    if mai_flower_got:
        a_beach "that's enough!"
        yd "...what?"
        a_beach "i think we've all had enough of this awful sand haven't we?"
    else:
        a_beach "Lies..."
        yd "...what?"
        a_beach "This fire is attracting flies, annoying little flies.."

    a_beach "i'm going back."
    a_beach "you should all join me."
    a_beach "ty lee?"
    t "i'm happy here for a bit longer, your highness!"
    a_beach "fine!"
    play sound "audio/whoosh.wav"
    hide azft_fireshadows
    show azft_firesmoke
    stop music
    play music "audio/Doctor_Turtle_-_04_-_Im_What_Youd_Be_Without_Her_Long_Version.mp3"
    a_beach "if you're all so happy, then you don't need the fire!"
    show azft azft03_1 with dissolve
    "azula gets up and stomps off towards the house by herself."
    yd "well that was strange."
    t "you don't think i upset her, do you?"
    y "nah, she's been acting weird since we got back."
    t "still... i guess i'll go make sure she's okay..."
    show azft azft06 with dissolve
    m "this has been a crazy day."
    y "no kidding."
    y "how much longer are we going to be on the island?"
    m "after tonight? two more nights."
    y "so... three nights total, and we'll leave on the fourth day."
    m "that's what i said."
    if mai_flower_got:
        y "speaking of things you said..."
        y "when you mentioned \"taking it slow\"--"
        m "ugh. zuko... you don't get women at all, do you?"
        yg "well, apparently i do."
        yd "actually, my dick is still sandy from getting {i}you{/i}."
        m "......."
        yd "i didn't want to mention it, but the handjob was a little... gritty."
        yd "not a lot... but like..."
        yd "enough."
        y "man that was fun."
        yd "what were we talking about?"
        m "you were mostly just talking to yourself."
        y "oh, right--"
        m "are you even still horny?"
        y "i'm always horny."
        m "ugh."
    else:
        y "speaking of things you said..."
        y "i know i didn't get you a flower, but-"
        m "ugh. zuko... i don't want to talk about it."
        m "you know what?"

    m "i think i need some space."

    if not_interested_mai and mai_flower_got == False:
        yd "..fine."
    else:
        yd "are we... already breaking up?"
        m "what?"
        m "no, i'm just going to bed."
        m "we haven't even had the... dating talk."
        m "which we should do tomorrow."
        m "i'm glad you brought that up."
        yd "hmm."

    m "goodnight, zuko."
    yc "wait-"
    show azft azft01 with dissolve
    "mai leaves for the house as well, leaving you alone on the beach."
    yd "......"
    ya "well i'm not just gonna fucking sit here!"
    $ ember = 6
    jump embernight

label after_first_fire:
    scene bg_a_island_hutnight with dissolve
    yd "hello?"
    yd "anyone here?"
    ya "it's not funny anymore guys."
    ya "i'm really starting to get creeped-"
    show azms azms01 with vshake
    ya "dicks!"
    yd "oh."
    ya "i thought you were a fucking ghost!"
    yd "you're... not, right?"
    m ".............."
    yc "oh, fuck you are."
    yc "look, if you promise not to possess me and make me fuck dudes, i'll let you look at my... stuff."
    m ".............."
    y "guess you're... not ready for jokes, yet."
    m ".............."
    menu:
        "apologize":
            y "look, i'm... sorry i was so difficult."
            $ mai_aff +=1
        "be firm":

            y "look, i didn't do anything wrong."
            $ mai_aff -=1

    m "............."
    show alnt with dissolve
    a "what's going-"
    show a_idle_fl_face_disdain
    with dissolve
    a "oh, it's a little lover's spat."
    a "how adorable."
    m "no. it's really not."
    hide azms azms01
    hide a_idle_fl_face_disdain
    with dissolve
    a "interesting...."
    a "what was that about?"
    y "nothing, it's dumb."
    y "what are you doing?"
    a "what's it look like? i just got out of a bath."
    show a_idle_fl_face_disdain
    with dissolve
    a "i smelled like... {i}ocean{/i}. ugh."
    hide a_idle_fl_face_disdain
    with dissolve
    a "don't take this the wrong way, brother..."
    a "but you might need a bath yourself."
    y "i'm not in the mood. which room is mine?"
    a "that one."
    y "let me just stick my head in and..."
    scene bg_a_farm_singlegirl with dissolve
    ya "oh hell no."
    ya "i get the room with the hay? fucking hay?"
    ya "i'm a prince!"
    scene black
    show bg_a_island_hutnight
    hide alnt
    show alnt
    with dissolve
    a "more like a baby. or a prima donna."
    yd "it just seems incrediby unfair that you all get sleeping rolls and i get a pile of hay."
    yd "what the hell."
    show a_idle_fl_face_blink with dissolve
    a "there aren't enough beds and you got here last."
    hide a_idle_fl_face_blink
    show a_idle_fl_face_unsure
    with dissolve
    a "you wouldn't make one of us girls sleep on the hay, would you?"
    yd "......."
    ya "fuck yes i would!"
    ya "i need my rest!"
    hide a_idle_fl_face_unsure
    show a_idle_fl_face_blink
    with dissolve
    a "*sigh*"
    a "i can tell you're going to be annoying about this."
    a "well... if you're a good big brother and sleep here..."
    a "when we get back to the fire nation, i'll-"
    if suitcases_correct:
        t "thanks for getting my suitcase right, prince!"
        m "*mumble grumble*"
        t "mai thanks you, too!"
        m "no, i don't!"
        y "at least you're talking to me!"
        m "no, i'm not!"
        y "you just did!"
        m ".........."
        y "yeah, that did it."
        t "your suitcase is correct as well, your highness!"
        a "hmm... well done on those, brother."
        a "for getting all of our luggage correct, and being so {i}willing{/i} to sleep on the hay..."
        a "i'll give you a special \"treat\" when we get back to the city."
        yd "...fine."
        a "how gracious of you."
        hide a_idle_fl_face_blink with dissolve
        a "sweet dreams, brother."
        a "don't let the bed bugs - of which i assume there are plenty - bite."
        hide alnt with dissolve
        yd "...fuck."
        jump ember_first_night2
    else:

        if not mai_softblack:
            m "who's suitcase is this?"

        if not ty_softpink:
            t "this isn't mine!"

        if not azula_trunkred:
            t "your highness, your suitcase isn't right!"

        m "genius here messed up."
        hide a_idle_fl_face_blink with dissolve
        a "really, zuko."
        a "you couldn't handle the simple task of sorting luggage?"
        a "well then you certainly don't deserve a reward."
        a "instead, sleeping on this hay will be punishment."
        ya "i will kick your-"
        show a_idle_fl_face_blink with dissolve
        a "don't try me, brother."
        a "we both know who's stronger."
        hide a_idle_fl_face_blink with dissolve
        a "besides, i have mai and ty lee."
        a "who do you think will win in a fight?"
        ya "..........."
        show a_idle_fl_face_blink with dissolve
        a "it's unfortunate you're so negative, brother."
        a "we were having such a good time."
        a "oh well."
        hide a_idle_fl_face_blink with dissolve
        a "sweet dreams."
        a "don't let the bed bugs - of which i assume there are plenty - bite."
        hide alnt with dissolve
        yd "...fuck."
        jump ember_first_night2

label ember_first_night2:
    scene black with dissolve
    "you head to your pile of hay and try to sleep..."
    "you toss and turn deep into the night."
    scene bg_a_farm_singlegirl
    show blackveil
    with dissolve
    ynd "ugh."
    ynd "hmgh."
    ync "i can't sleep at all."
    ync "so damn itchy..."
    ync "i wonder if anyone else is awake..."
    scene bg_a_island_hutnight with dissolve
    menu:
        "mai and azula's room":
            jump ember_first_night3
        "ty lee's room":

            scene bg_a_island_1bed
            show blackveil
            with dissolve
            ynd "what the..."
            ynd "where is she?"
            "you look around but don't see a trace of ty lee."
            ynd "maybe she went for a late night swim or something?"
            scene bg_a_island_hutnight with dissolve
            menu:
                "mai and azula's room":
                    jump ember_first_night3

label ember_first_night3:
    show amsl amsl01 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yn "damn..."
    yn "azula's basically busting out of that top..."
    yn "she really does have the best tits around."
    yn "and mai... is it weird i just want to bite her thighs?"
    yn "the things i'd do to..."
    show amsl amsl02 with dissolve
    a "do to whom, brother?"
    ync "fuck."
    ync "uh."
    ync "I'm not-"
    show amsl amsl01 with dissolve
    a "aw, is zuzu shy?"
    a "i've caught you peeping."
    show amsl amsl02 with dissolve
    a "you were staring at mai, weren't you?"
    ync "well... uh..."
    a "come on... let's take a look."
    a "wanna see a bit while she's asleep?"
    a "i know you want to..."
    a "i can tell you it's worth it."
    menu:
        "look":
            ynd "...."
            yn "yeah, go ahead."
            a "i knew it, you fucking pervert."
            show amsl amsl25 with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            yn "hot damn."
            a "it's pretty little body, don't you think?"
            yc "is... she going to wake up?"
            a "no... mai is the deepest sleeper i've ever known."
            a "she can sleep through anything."
            a "so come on... whip your cock out."
            ynd "what??"
            a "i know you want to."
            a "don't you want to look at us and work that big handsome cock for me?"
            ynd "......"
            menu:
                "masturbate":
                    yn "you want it, sis?"
                    a "mmmm...."
                    yn "here you go."
                    show azsl_masturbate_1
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "that's it..."
                    a "look at me... look in my fucking eyes, brother!"
                    ync "sshhh!!!"
                    a "now i want you to look at her pussy."
                    a "she doesn't know, brother..."
                    a "and she won't know..."
                    a "and this pretty little tit... firm... and her nipple's perky in the cool air."
                    a "don't you want a taste?"
                    ync "yes... yes... *pant* *pant*"
                    a "well, then...."
                    show amsl amsl02
                    with dissolve
                    a "i think that's enough."
                    hide azsl_masturbate_1 with dissolve
                    ynd "um... what?"
                    a "well, you don't want to make a mess, do you?"
                    a "besides, this can be our little secret."
                    ynd "...."
                    yna "i don't want a secret! i want to cum!"
                    show amsl amsl01 with dissolve
                    a "don't be a child, zuko."
                    a "now close the door on your way out."
                    yna "i-"
                    a "goodnight."
                    ynd "...."
                    yna "fine."
                    jump ember_first_night4
                "don't masturbate":

                    ynd "i'm going to pass on that."
                    a "your loss."
                    show amsl amsl01 with dissolve
                    a "close the door on your way out."
                    ync "but-"
                    a "goodnight."
                    yn "...."
                    jump ember_first_night4
        "don't look":

            ync "i... don't want to get caught."
            a "your loss."
            show amsl amsl01 with dissolve
            a "close the door on your way out."
            ync "but-"
            a "goodnight."
            yn "...."
            jump ember_first_night4

label ember_first_night4:
    scene black with dissolve
    "this time, you fall asleep quickly and deeply. before your head even reaches the bed."
    stop music
    play music "audio/Fire2.mp3"
    ync "what... is that sound?"
    show azft_fireshadows with Dissolve(1.0)
    "{b}welcome. you must be tired."
    "{b}we, too, have come a long way."
    "{b}sit."
    "without any prompting on your part, your body automatically sits where you are."
    "you seem to land in a chair."
    ynd "that... is fortunate."
    "{b}is it?"
    "{b}why are you here?"
    ynd "why am... i'm..."
    ync "wait... where am i?"
    ynd "oh, and that's great. just perfect. i'm naked."
    ynd "of course."
    ynd "you know, you seem... very familiar."
    "{b}he has forgotten."
    "{b}we should help him remember."
    "{b}indeed."
    "{b}i wonder how we appear to him?"
    ync "wait... is this a dream?"
    "{b}what is your name?"
    ynd "i'm zuko..."
    ync "no, that... that doesn't feel right."
    ynd "....why are we around a campfire, anyway?"
    "{b}are we?"
    ynd "i mean, that's what it looks like."
    "{b}then let us tell you a story."
    "{b}there was once a prince."
    ynd "...."
    "{b}this prince was a man of honor. of pride. of self-doubt."
    "{b}full of inner turmoil and longing for validation, he sought to aid his father and defeat the avatar."
    ynd "this sounds familiar. have i met this guy?"
    "{b}but this prince faced many trials along the way."
    "{b}trials not just of strength, but of character. of will. of purpose."
    "{b}of understanding."
    ynd "Okay....?"
    "{b}a long time later, there was a boy."
    "{b}this boy grew up in the city founded by that prince."
    "{b}that boy was the avatar."
    ynd "oh, right. that was... aang? right?"
    "{b}no."
    "{b}this boy became a beacon. a beacon for spirits."
    "{b}for one spirit in particular."
    "{b}the spirits were restless and one reached out... asking for his aid."
    "{b}which one are you?"
    ynd "wait... i'm one of these?"
    ynd "ohhh.... i'm the prince! right. my bad."
    with sshake
    "a low rumbling shakes you as the voices seem to growl."
    "{b}let's play a game."
    "{b}you answer \"true\" or \"false\"."
    "{b}ready?"
    menu:
        "play":
            "{b}your name is zuko."
            ynd "i already tried to answer that, i don't-"
            with sshake
            "{size=+5}{b}false!"
            ynd "oh, i get it. you're pretty strict... figments of my imagination."
            "{b}you have a sister named azula."
            menu:
                "answer":
                    ynd "well, i-"
                    with sshake
                    "{size=+5}{b}false!"
                    ynd "it's not much of a \"question and answer\" thing if you do both sides of it."
                    jump ember_first_night5
                "don't answer":

                    with sshake
                    yna "aahhh!!"
                    "you try not to answer, but your body is wracked with pain."
                    "{b}you have a sister named azula."
                    menu:
                        "answer":
                            ynd "well, i-"
                            with sshake
                            "{size=+5}{b}false!"
                            ynd "it's not much of a \"question and answer\" thing if you do both sides of it."
                            jump ember_first_night5
        "don't play":

            ync "i don't really think-"
            with sshake
            "{size=+5}{b}you {i}will{/i} play!"
            ync "i... okay..."
            "{b}your name is zuko."
            ynd "i already tried to answer that, i don't-"
            with sshake
            "{size=+5}{b}false!"
            ynd "oh, i get it. you're pretty strict... figments of my imagination."
            "{b}you have a sister named azula."
            menu:
                "answer":
                    ynd "well, i-"
                    with sshake
                    "{size=+5}{b}false!"
                    ynd "it's not much of a \"question and answer\" thing if you do both sides of it."
                    jump ember_first_night5
                "don't answer":

                    with sshake
                    yna "aahhh!!"
                    "you try not to answer, but your body is wracked with pain."
                    "{b}you have a sister named azula."
                    menu:
                        "answer":
                            ynd "well, i-"
                            with sshake
                            "{size=+5}{b}false!"
                            ynd "it's not much of a \"question and answer\" thing if you do both sides of it."
                            jump ember_first_night5


label ember_first_night5:
    "{b}pathetic. you waste our time."
    ync "what... even are you?"
    "{b}you can think of us as... ghosts."
    "{b}fading spirits."
    "{b}we are here to impart wisdom on your sorry ass."
    ynd "excuse me?"
    "{b}we have come to you, as you have come to us."
    "{b}remember."
    ynd "remember what?"
    "{size=-4}{b}remember."
    ynd "oh, come on."
    "{size=-8}{b}remember...."
    ync "wait.... {size=+6}wait!"
    ync "{size=+6}no!"
    scene black with Dissolve(1.0)
    jump memorydream1

label after_first_memory_dream:
    $ ember_day = 2
    scene black
    scene kday with flash
    show kw at Position (xpos = 0.9, xanchor=0.5, ypos=0.6, yanchor=0.5)
    with dissolve
    k "hey aang!"
    yn "who-"
    hide kw with dissolve
    show knbe at Position (xpos = 0.9, xanchor=0.5, ypos=.6, yanchor=0.5)
    with dissolve
    k "how do i look?"
    yn "great... but who are-"
    hide knbe with dissolve
    show ktju with flash
    yn "whoa! what am i-"
    show k_bj5 with flash
    k "'oo 'on ee emer?"
    hide ktju
    yn "... i don't know what you're saying, but-"
    scene light
    show pgfull
    with flash
    s "return, avatar!"
    s "there is no time!"
    play sound "audio/hiss.wav"
    scene black with Dissolve(1.0)
    stop music
    scene white with dissolve
    show text "Ember Island\n\nsecond day"
    $ renpy.pause (1.5, hard=True)
    scene white with dissolve
    play music "audio/Bassa Island Game Loop.ogg"
    scene bg_a_farm_singlegirl with Dissolve(1.0)
    ync "what the... what the {i}hell{/i}."
    ync "i don't even... i have no idea... just..."
    ync "what the {i}hell{/i}."
    "your head is spinning with bits of new, unfamiliar memories."
    ync "was there a girl...?"
    scene bg_a_island_hutday with dissolve
    ync "ugh..."
    ync "does anyone have any aspirin?"
    show azula_idle_ff_beach with dissolve
    a "what is that?"
    ynd "what is what?"
    yna "oh, shit i'm naked!"
    a "well, yes, but i meant-"
    "you hurry to your room and get changed."
    y "right, okay. what was i saying?"
    a "you were asking for a pin, i believe?"
    yd "what... oh, right. aspirin. do we have any here?"
    a "I don't know what that is."
    yd "you know, little pill, helps with headaches?"
    a "pill? i don't know what that is."
    a "you need to steam your head and sniff some strong herbs."
    yd "how do you not know what-"
    yd "wait. how do i know what-"
    yd "what is aspirin?"
    yd "(is that... from a different memory?)"
    a "I have no idea. sounds like futuristic fantasy."
    a "now go wake up mai."
    yd "are you sure that's a good idea? she's kind of... peeved with me."
    a "oh, i'm very sure."
    a "i've already got my outfit on, i'm ready to leave now."
    a "*sigh*... it's difficult being the punctual one."
    hide azula_idle_ff_beach with dissolve
    "just as you open the door to mai's room, azula yells."
    a "mai! wake up!"
    "you scuttle back quickly so she doesn't think you were just watching her."
    show azms azms01_1
    show azms_yawn
    with dissolve
    "mai wanders out half-asleep."
    hide azms_yawn with dissolve
    m "what's going..."
    m "hold on..."
    show azms azms04_1 with dissolve
    m "*yaaawnn*"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "i want that. i want to lick, eat, kiss, pound that."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show azms azms01_1 with dissolve
    m "zuko?"
    m "what's going on?"
    y "we're just, uh... getting ready for the day."
    m "alright, let me get changed..."
    scene black
    scene bg_a_island_hutday
    with dissolve
    show mai_fl_flip:
        xpos 100
    with dissolve
    m "there..."
    show azula_idle_fl_beach with dissolve
    a "are you ready yet?"
    m "...yes?"
    a "good. it's about time."
    a "ty lee's still asleep."
    hide azula_idle_fl_beach
    show azula_idle_ff_beach
    with dissolve
    a "go wake her, would you zuko?"
    m "i can do it-"
    show a_idle_ff_face_blink with dissolve
    a "no, i think zuko should have the pleasure."
    yd "the... pleasure?"
    m "...azula..."
    hide a_idle_ff_face_blink with dissolve
    a "yes, mai?"
    m ".....nothing."
    hide azula_idle_ff_beach
    hide mai_fl_flip
    with dissolve
    "as you walk to ty lee's door, you hear an strange noise coming from her room."
    yd "what the...?"
    show azst azst01 with dissolve
    "{i}zzzt! zzzt! zzzt!"
    yd "what is that?"
    menu:
        "lift blanket":
            show azst azst02
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "hot damn."
            "{i}zzzt! zzzt! zzzt!"
            "the toy continues to vibrate and move in her pussy, clearly lulling her to sleep."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            yg "guess she can't sleep without it."
            yg "or she came really hard last night and forgot to take it out."
            yd "i wonder if i should come back-"
            show azst_eyesopen with dissolve
            t "oh! hello, prince."
            t "watcha doing down there?"
            yc "oh, uh, good morning... ty lee."
            yc "azula... um, sent me to wake you."
            t "that was nice of her!"
            t "I guess i'll get up now."
            t "now if you'll be so kind..."
            yd "what?"
            yc "oh. right. sorry."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "......"
            t "you're still looking."
            yc "sorry!"
            show azst azst01 with dissolve
            y "i'll uh... see you in a bit."
            t "yup!"
            scene black
            scene bg_a_island_hutday
            show mai_fl_flip:
                xpos 100
            show azula_idle_ff_beach
            with dissolve
            a "well? did you have fun?"
            y "I, uh..."
            m "did you?"
            y "no."
            y "no fun whatsoever."
            y "boy do i hate fun."
            m "......"
            a "well, i can see you and mai have a healthy relationship."
            a "you guys should spend more time together!"
            yd "really?"
            a "of course! i was being... ridiculous yesterday."
            a "no idea what came over me."
            a "i'm perfectly fine now."
            a "in fact, i'm the one that's trying to get you to together!"
            a "it'd be ridiculous if that enraged me."
            m "...i suppose."
            show tylee_idle_ff_topless:
                xpos -250
            with dissolve
            t "i'm ready! let's get some sun!"
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            a "...ty lee, dear, do you think you've forgotten something?"
            t "wha- oh!"
            t "heehee!"
            hide tylee_idle_ff_topless with dissolve
            show tylee_idle_ff_beach:
                xpos -250
            with dissolve
            t "now i'm ready."
            yd "right. cool. i'm not rock hard or anything."
            yd "i'm going to... walk behind you guys if that's cool."
            yd "i'll also be bent over."
            ya "don't look at me!"
            m ".....let's just meet you there."
            yd "that might... be for the breast."
            yc "i mean \"breast\"."
            ya "\"best\"!"
            a "....why don't you figure that out, and we'll see you later."
            hide tylee_idle_ff_beach
            hide azula_idle_ff_beach
            hide mai_fl_flip
            with dissolve
            jump emberday
        "wake her normally":

            y "time to get up, ty lee."
            show azst_eyesopen with dissolve
            t "oh! hello, prince."
            t "what's up?"
            yc "azula... um, sent me to wake you."
            t "that was nice of her!"
            t "I guess i'll get up now."
            t "now if you'll be so kind..."
            yd "what?"
            yc "oh. right. sorry."
            y "i'll uh... see you in a bit."
            t "yup!"
            scene black
            scene bg_a_island_hutday
            show mai_fl_flip:
                xpos 100
            show azula_idle_ff_beach
            with dissolve
            a "well? did you have fun?"
            y "I, uh..."
            m "did you?"
            y "no."
            y "no fun whatsoever."
            y "boy do i hate fun."
            m "......"
            a "well, i can see you and mai have a healthy relationship."
            a "you guys should spend more time together!"
            yd "really?"
            a "of course! i was being... ridiculous yesterday."
            a "no idea what came over me."
            a "i'm perfectly fine now."
            a "in fact, i'm the one that's trying to get you to together!"
            a "it'd be ridiculous if that enraged me."
            m "...i suppose."
            show tylee_idle_ff_topless:
                xpos -250
            with dissolve
            t "i'm ready! let's get some sun!"
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            a "...ty lee, dear, do you think you've forgotten something?"
            t "wha- oh!"
            t "heehee!"
            hide tylee_idle_ff_topless with dissolve
            show tylee_idle_ff_beach:
                xpos -250
            with dissolve
            t "now i'm ready."
            yd "right. cool. i'm not rock hard or anything."
            yd "i'm going to... walk behind you guys if that's cool."
            yd "i'll also be bent over."
            ya "don't look at me!"
            m ".....let's just meet you there."
            yd "that might... be for the breast."
            yc "i mean \"breast\"."
            ya "\"best\"!"
            a "....why don't you figure that out, and we'll see you later."
            hide tylee_idle_ff_beach
            hide azula_idle_ff_beach
            hide mai_fl_flip
            with dissolve
            jump emberday

label ember_second_day:
    scene black
    scene bg_a_beach_01
    show azula_idle_fl_beach
    with dissolve
    a "took you long enough."
    a "oh, it looks like there's someone in our chairs."
    a "i'll go reason with them."
    hide azula_idle_fl_beach with dissolve
    y "what is she-"
    play sound "audio/whoosh.wav"
    with oflash
    victim "aahhh!!"
    play sound "audio/whoosh.wav"
    with oflash
    victim "why are you doing this?!"
    play sound "audio/whoosh.wav"
    with oflash
    victim "aaaahhhhhhhhhhhhh!!!!"
    show azula_idle_fl_beach with dissolve
    a "seats are free."
    yd "...you are terrifying."
    a "and yet i have the softest skin."
    a "let's go."
    hide azula_idle_fl_beach with dissolve


    show asun asun02
    with dissolve
    a "ahh... nothing like a well deserved soak in the sun."
    t "I could do this forever."
    show asun asun01
    show asun_azulablink
    with dissolve
    a "*stretch*"
    a "*mmmmm...*"
    show asun asun100_1 with dissolve
    a "i almost want to never go back."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "hey, mai..."

    m "...yes, zuko?"
    y "you got udders to make a cow jealous, girl."
    m "..."
    y "i mean... you look pretty today."
    m "you think so?"
    y "yeah."
    show asun asun101
    hide asun_azulablink
    with dissolve
    a "and what about me, brother?"
    a "did you forget about me?"
    y "you're... pretty too, azula."
    show asun asun27
    show asun_tyleeblink
    with dissolve
    t "aahhh... i needed this!"
    m "...."
    m "I think i might go for a swim."
    m "zuko... do you want to come?"
    y "ye-"
    show asun asun24 with dissolve
    a "no!"
    a "i mean, no, zuko has to do something with me."
    m "what?"
    yd "yeah... what?"
    a "it's a brother-sister thing."
    t "i'll go with you mai."
    m "alright."
    scene black
    scene bg_a_beach_02
    show azula_idle_fl_beach
    with dissolve
    yd "so what's up?"
    y "oh, hey. a lawnchair. sweet."
    show azbr_playerbody
    with vshake
    y "nothing like laying out, am i right?"
    a "we never just talk anymore, zuzu."
    y "...."
    yd "did we ever?"
    show a_idle_fl_face_disdain
    with dissolve
    a "why do you have to be so difficult? i'm trying to..."
    hide a_idle_fl_face_disdain
    show a_idle_fl_face_unsure
    with dissolve
    a "we've been having fun, haven't we?"
    a "it's been nice... almost like a family again."
    a "right?"
    menu:
        "i'm enjoying myself":
            y "yeah, i'm having fun."
            hide a_idle_fl_face_unsure
            show a_idle_fl_face_blink
            with dissolve
            a "oh, good."
            a "me, too."
            hide a_idle_fl_face_blink
            show a_idle_fl_face_unsure
            with dissolve
            jump abeachrub
        "no, it's fucked up":


            yd "honestly, it's fucking chaos."
            yd "you're a hot mess."
            y "emphasis on hot, though."
            yd "...and mess."
            yd "both, really."
            a "oh."
            jump abeachrub

label abeachrub:
    a "......"
    a "how... are battles going?"
    show a_idle_fl_face_anger
    hide a_idle_fl_face_unsure
    with dissolve
    a "you're winning, right?"
    yd "we're... on an island."
    yd "i'm not fighting anyone at the moment."
    hide a_idle_fl_face_anger
    show a_idle_fl_face_unsure
    with dissolve
    a "oh. right."
    hide a_idle_fl_face_unsure
    show a_idle_fl_face_blink
    with dissolve
    a "well, you're lucky i'm so magnanimous."
    a "letting you take a vacation."
    yd "we're... both taking a vacation."
    hide a_idle_fl_face_blink
    show a_idle_fl_face_unsure
    with dissolve
    yd "can you not talk about anything normal?"
    a "....."
    a "i... can."
    a "of course."
    a "how is..."
    a "how is, um..."
    hide a_idle_fl_face_unsure
    with dissolve
    a "how is it being a failure?"
    ya "what?"
    show a_idle_fl_face_unsure
    with dissolve
    a "i didn't mean..."
    a "i don't know how..."
    a "i'm... sorry."
    a "..."
    show a_idle_fl_face_blink
    with dissolve
    a "watching you and mai..."
    a "and ty lee with all the boys..."
    a "i want... something..."
    yd "really?"
    hide a_idle_fl_face_blink
    hide a_idle_fl_face_unsure
    show a_idle_fl_face_anger
    with dissolve
    a "is that so hard to believe?"
    a "because i'm not normal?"
    a "because i'm strong?"
    a "i hear it, you know!"
    a "\"azula the monster.\""
    hide a_idle_fl_face_anger
    with dissolve
    a "i enjoy it, actually."
    show a_idle_fl_face_unsure
    with dissolve
    a "still... i wish someone saw me as more..."
    a "that i had someone to depend on."
    a "and who can you depend on if not family?"
    a "you came back to us after that debacle with the avatar."
    show a_idle_fl_face_blink with dissolve
    a "i'd rather you not leave again."
    hide a_idle_fl_face_blink with dissolve
    a "do you understand, zuko?"
    a "it's not like i can turn to father."
    a "and there's no one i can trust."
    a "and... i worry."
    a "the earth kingdom is... more difficult than ever."
    a "and i expect to rule."
    y "...but i'm the firstborn. and a son."
    y "i'll inherit the crown."
    hide a_idle_fl_face_unsure with dissolve
    a "not if i have my way."
    yd "what?"
    show a_idle_fl_face_blink with dissolve
    a "nothing."
    hide a_idle_fl_face_blink
    show a_idle_fl_face_unsure
    with dissolve
    a "but i meant what i said."
    yd "okay... i think i need to get back to mai."
    y "she's looking at us. and ty lee's waving to us."
    show a_idle_fl_face_anger
    hide a_idle_fl_face_unsure
    with dissolve
    a "of course. mai. your girlfriend."

    if mai_flower_got == False and not_interested_mai:
        yd "Does it look like that to you?"
        yd "Anyway.."

    yd "what's the problem?"
    hide a_idle_fl_face_anger
    with dissolve
    a "there is none."
    a "let's wave to her, shall we?"
    show a_idle_fl_face_unsure with dissolve
    a "i'll just turn around and-"
    scene black with sshake
    "azula turns and stumbles, falling backwards on your lap."
    "the bottom of her outfit seems to come down a little during the fall."
    yd "oomph."
    a_beach "oh no, i tripped!"
    "she wiggles into your cock, seemingly trying to balance herself, but lightly pulling down your shorts in the process..."
    stop music
    play music "audio/Unwritten Return.mp3"
    show azbr azbr02 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "what the fuck?!"
    ya "azula! they're right over-"
    a "haha. how unlike me... i'm not usually this clumsy."
    t_ "are you okay?!"
    show azbr azbr03 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "oh, yes. I think i'll need to sit here for a moment, though."
    yc "ungh."
    show azbr azbr06 with Dissolve(0.35)
    a "what's wrong, zuko?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yc "your... your butt is..."
    show azbr azbr07 with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "is what?"
    yc "it's... ah... my... um..."
    with ushake
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yc "...."
    yd "my cock is between your asscheeks, azula."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "no it's not."
    a "what a silly idea."
    show azbr azbr100 with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "azula smoothly straddles and cups your cock with her cheeks."
    "she's surprisingly light, and yet presses down firmly, burying your cock deeply in her crevice."
    "her soft cheeks surround and squeeze you as she grinds her ass down onto you, keeping her pressure constant."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "now you should wave at the girls."
    a "so they don't think anything suspicious."
    yc "hi! uh... hi... girls... hgh...!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "it's such a nice day..."
    a "i could sit here for hours..."
    show azbr azbr101 with Dissolve(0.35)
    a "wouldn't that be nice?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "just some sibling time?"
    show azbr_blink with Dissolve(0.35)
    a "hmm... i wonder what game we could play...?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_ "are you sure you guys are okay?"
    m_ "should we come over?"
    hide azbr_blink
    show azbr azbr100
    with Dissolve(0.35)
    a "no, we're fine, mai."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "it looks like you're having fun, though!"
    a "i'm sure we'll come in a minute."
    show azbr azbr101 with Dissolve(0.35)

    a "or at least zuko will..."
    a "won't you?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yc "I should... i should get up..."
    show azbr_sultry with Dissolve(0.35)
    a "i think that would be very rude, zuzu."
    a "we're spending good quality time together."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    menu:
        "try to get up":
            yc "i really think i should get up..."
            hide azbr_sultry
            show azbr_angry
            with Dissolve(0.35)
            a "you're going to stay right there, zuko."
            a "you're going to cum."
            a "cum from fucking my ass cheeks."
            a "or i'm going to get up and show everyone what you've been doing here..."
            a "...you disgusting pervert."
            yc "this..."
            ya "this was all you!"
            hide azbr_angry
            with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            a "was it?"
            show azbr azbr105 with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump abeachrub2
        "maybe... maybe another minute...":


            yc "i... guess... ah... we can... catch up... a little longer..."
            hide azbr_sultry with Dissolve(0.35)
            a "good boy."
            show azbr azbr105 with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump abeachrub2

label abeachrub2:
    a "you just enjoy yourself, now."

    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "well done, ty lee... very limber!"
    t_l "thank you, your highness!"
    m_ "i can do that too..."
    m_ "if i wanted to have boys drooling all over me..."

    if mai_flower_got:
        t_ "zuko drools over you."
        m_l "shut up."

    a_beach "zuko would drool over a water balloon if it felt like a boob."
    a_beach "he's a {i}boy{/i}."
    m_l "heh, i guess so."
    "your cock stiffens even more as azula laughs and talks with the girls..."
    "...as she brings you closer to orgasm."
    yc "a...azula... i'm..."
    show azbr azbr102
    show azbr_sultry
    with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "what's wrong, brother?"
    yc "I'm... i'm..."
    a "hmm? what's wrong?"
    a "are you going to spurt in my ass?"
    a "am i spending too much time on your tip? is it too sensitive?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "want me to work the whole shaft?"
    a "pick up the pace? go deeper?"
    yc "n-no..."
    a "that's too bad... because..."
    show azbr azbr104
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "ahh... f-fuck..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "you're not going to cum between my sweet, soft little cheeks are you?"
    a "my little cum-catching ass cheeks?"
    a "you're not going to do that, right?"
    a "you're not going to cover your sister's ass cheeks, right?"
    a "not on a public beach?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "oh, fuck!"
    play sound "audio/splurt3.ogg"
    show azbr azbr07
    show az_mai_sperm_9:
        xpos -420 ypos 300
    with flash
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "oh, {i}no{/i}..."
    play sound "audio/splurt3.ogg"
    hide az_mai_sperm_9
    show a_pussrub_holdcock_sperm01:
        xpos -266 ypos 138
    show az_mai_sperm_10:
        xpos -420 ypos 300
    with flash
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "hgh!"
    a "what are you doing, brother?"
    play sound "audio/splurt3.ogg"
    hide azbr_sultry
    hide az_mai_sperm_10
    show az_mai_sperm_11:
        xpos -420 ypos 300
    with flash
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yc "ghgh...."
    show azbr azbr04 with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "mmmm...."
    a "warm..."
    show azbr azbr07 with Dissolve(0.35)
    "she leans back and whispers lightly in your ear..."
    show azbr_sultry with Dissolve(0.35)
    a "how did my ass feel, brother?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "you fucking disgust me. you're filth. a fucking pervert."
    hide azbr_sultry with Dissolve(0.35)
    a "and wasn't it fun?"
    a "i think we might need a dip in the ocean."
    a "we're covered in cum."
    a "but first... let's go talk to mai."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "yeah..."
    yd "wait, what?"
    ya "no!"
    ya "why do you keep doing this to me??"
    show azbr_blink with Dissolve(0.35)
    a "because it's {i}fun{/i}, dear brother."
    hide azbr_blink with Dissolve(0.35)
    a "come on. you know you want to."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene bg_a_beach_02
    with dissolve
    show azula_idle_fl_beach
    show a_idle_fl_face_blink
    with dissolve
    a "mai!"
    yc "(no no no no no...)"
    "you hastily shove your cock back into your shorts and try to cover up the jizz with your hands."
    "azula makes no such effort, though all of the cum is on her backside."
    show mai_fl_flip:
        xpos 200
    with dissolve
    m "yes?"
    a "what are your thoughts on family?"
    m "..."
    m "it's important?"
    m "i'd do anything for mine."
    hide a_idle_fl_face_blink with dissolve
    a "anything?"
    m "mhmm."
    a "hear that, zuko?"
    a "mai really believes that family-"
    "as azula speaks, a bit of cum drips down the back of her leg and into the crook behind her knee."
    show a_idle_fl_face_unsure with dissolve
    a "oh!"
    m "what?"
    hide a_idle_fl_face_unsure with dissolve
    a "nothing."
    a "as i was saying... mai believes family takes care of each other."
    a "we're going to take care of each other, aren't we zuko?"
    m "um... princess azula?"
    show a_idle_fl_face_blink with dissolve
    a "forsake all others when it really comes down to it."
    m "there's.. um... something dripping..."
    hide a_idle_fl_face_blink with dissolve
    a "what?"
    "as all three of you look down, a big white blob of cum drops off her butt and lands in the sand."
    m "what... is that?"
    a "hmm... a bird must have defecated overhead."
    a "just narrowly missed us."
    m "...oh."
    a "well, i'm going to take a dip, i believe zuko is looking to do the same."
    a "why don't we all go for a swim?"
    m "sure."
    yc "(fucking finally...)"

    scene black with dissolve
    "you dive into the surf and do your best to scrub yourself furiously under the water."
    "you get out of the water as mai makes her way towards you."
    scene bg_a_beach_02
    show mai_fl_flip
    with dissolve
    m "hey. we should talk."
    y "yeah, i'm down."
    m "want to go for a walk?"
    y "sure."
    show azula_idle_fl_beach with dissolve
    a "you guys up for a round of volleyball first?"
    a "we forgot to find out when the party is, and those guys might be around."
    yd "that seems pretty crucial."
    m "i'm down."
    y "yeah, why not."
    a "good."
    $ after_beachrub = True
    jump volleyball

label after_second_volly_win:
    hide screen vstats
    $ vollywin2 = True
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    hide volleyball_net with dissolve
    a "yes!"
    jump after_second_volly

label after_second_volly_lose:
    hide screen vstats
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    hide volleyball_net with dissolve
    a "damn it!"
    jump after_second_volly

label after_second_volly:
    show tylee_idle_ff_beach:
        xpos -250
    with dissolve
    t "hey! i talked to those guys again!"
    a "and?"
    t "they said some of the most important teenagers in the fire nation will be there!"
    a "of course. {i}we'll{/i} be there, after all."
    t "they said they'll be partying from dusk till dawn!"
    a "excellent. then that is when we will arrive."
    show mai_fl_flip:
        xpos 100
    with dissolve
    m "well, i think we're going for a walk."
    a "have fun."
    a "I hope zuko has enough stamina."
    a "i think i really took it out of him."
    m "what?"
    show a_idle_fl_face_blink with dissolve
    a "with volleyball, of course."
    hide a_idle_fl_face_blink with dissolve
    m "oh."
    m "well, then let me know when you're ready, zuko."
    $ ember =7
    jump emberday

label beach_stroll:
    show mai_idle_ff_beach with dissolve
    m "hi, zuko."
    y "come on mai, let's wander."
    m "okay."


    scene black
    scene bg_a_beach_02
    show mai_idle_fl_beach
    with dissolve
    m "so..."
    m "where are we?"
    yd "oh god, the amnesia's contagious."
    y "okay, you're a ball juggler on the starship enterprise, and blowjobs are your favorite-"
    show mai_idle_fl_smile
    with dissolve
    m "no, you idiot."
    hide mai_idle_fl_smile
    with dissolve
    m "i mean with us."
    y "i don't really know."
    y "i guess we're dating if you'd like to be."
    m "....."
    m "what's going on with you and azula?"
    yd "what do you mean?"
    m "you guys seem to be... getting along really well."
    m "it's nice to see, but... unexpected."
    yd "so?"
    m "i just want to make sure you're okay."
    m "i like who you are, you don't need to... change or anything."
    y "i'm fine."
    "the two of you walk down the beach, not really sure what to say."
    menu:
        "give her a seashell":
            "you bend down and pick up a conch shell."
            y "here, this is for you."
            hide mai_idle_fl_beach
            show mai_idle_ff_beach
            with dissolve
            m "why would i want that?"
            yc "i... saw it and thought it was pretty."
            yd "don't girls like stuff like this?"
            show mai_idle_ff_angry with dissolve
            m "ugh. maybe stupid girls."
            ya "forget it."
            hide mai_idle_ff_angry
            hide mai_idle_ff_beach
            show mai_idle_fl_beach
            with dissolve
            "you throw away the shell and go back to walking in silence."
            menu:
                "get her an icecream":
                    "you see a man selling icecream, and grab two cones."
                    y "i thought since it's so hot, here-"
                    hide mai_idle_fl_beach
                    show mai_idle_ff_beach
                    with dissolve
                    "as you go to hand mai her icecream, you drop it on her."
                    show mai_idle_ff_surprised with dissolve
                    m "oh!"
                    hide mai_idle_ff_surprised
                    show mai_idle_ff_angry
                    with dissolve
                    m "thanks..."
                    m "...this is really refreshing."
                    yc "......"
                    hide mai_idle_ff_angry
                    show mai_idle_fl_beach
                    hide mai_idle_ff_beach
                    with dissolve
                    "you go back to walking in silence."
        "get her an icecream":


            "you see a man giving away free icecream, and grab two cones."
            y "i thought since it's so hot, here-"
            hide mai_idle_fl_beach
            show mai_idle_ff_beach
            with dissolve
            "as you go to hand mai her icecream, you drop it on her."
            show mai_idle_ff_surprised with dissolve
            m "oh!"
            hide mai_idle_ff_surprised
            show mai_idle_ff_angry
            with dissolve
            m "thanks..."
            m "...this is really refreshing."
            yc "......"
            hide mai_idle_ff_angry
            show mai_idle_fl_beach
            hide mai_idle_ff_beach
            with dissolve
            "you go back to walking in silence."
            menu:
                "give her a seashell":
                    "you bend down and pick up a conch shell."
                    y "here, this is for you."
                    hide mai_idle_fl_beach
                    show mai_idle_ff_beach
                    with dissolve
                    m "why would i want that?"
                    yc "i... saw it and thought it was pretty."
                    yd "don't girls like stuff like this?"
                    show mai_idle_ff_angry with dissolve
                    m "ugh. maybe stupid girls."
                    ya "forget it."
                    hide mai_idle_ff_angry
                    hide mai_idle_ff_beach
                    show mai_idle_fl_beach
                    with dissolve
                    "you throw away the shell and go back to walking in silence."

    yd ".....do you want to do something other than walk?"
    m "like what?"
    y "how about we have a little... fun?"
    m "okay. see if you can find me."
    yd "what? no, i meant-"
    scene black
    scene bg_a_beach_02
    with dissolve
    y "...fuck."
    $ ember = 8
    jump emberday

label hideandseek:
    m "*sigh...*"
    yd "what?"
    m "nothing."
    yd "that's really annoying."
    show mai_idle_ff_beach
    hide mai_idle_fl_beach
    show mai_idle_ff_angry
    with dissolve
    m "great, i'm annoying. anything else wrong with me?"
    ya "it's just frustrating when you make it clear there's a problem but don't tell me what it is."
    ya "then it's my fault if it doesn't get solved, and the whole atmosphere is shitty, and-"
    m "i want to open a shop here, okay?"
    hide mai_idle_ff_angry with dissolve
    yd "...what?"
    m "i'd like to open a shop on ember island, but it's just not possible."
    m "see? not something you can solve."
    m "let's forget it."
    yd "let's go in. i'm sure it's nothing special anyway."
    m "...okay."
    scene black
    scene bg_a_armory
    with dissolve
    yd "what the..."
    show mai_fl_flip:
        xpos 250
    with dissolve
    m "what's-"
    m "..."
    image mai_fl_flip_angry = im.Flip("mai/mai_idle_fl_angry.png", horizontal=True)
    show mai_fl_flip:
        xpos 200
    show mai_fl_flip_angry:
        xpos 200
    with dissolve
    m "what."
    show shadyguy_grin with dissolve
    sg "welcome to-"
    sg "oh, hey buddy! good to see you again!"
    if mai_flower_got:
        sg "did you find your flower?"
    m "why is your shop..."
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "what?"
    yd "...your shop looks familiar."
    show shadyguy_grin
    hide shadyguy_unsure
    with dissolve
    sg "oh, that? you noticed it huh?"
    sg "yeah... like i said, my brother gave it to me."
    sg "he modeled it after this place in the city."
    sg "big armory. you've probably seen it."
    m "i definitely have."
    sg "well, feel free to look around."
    sg "i've been trying to make it work, but everything's half off, i need to get rid of this place."
    hide mai_fl_flip_angry with dissolve
    m "...and it's already exactly like mine..."
    yd "...."
    y "hey, how much for it?"
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "what?"
    y "how much to buy the place? as is?"
    show shadyguy_grin
    hide shadyguy_unsure
    with dissolve
    sg "well..."
    sg "amazing location on ember island..."
    sg "infamous home of the wealthiest members of the fire nation..."
    sg "with only one unexplained death..."
    yd "what?"
    sg "and a recenty boarded up murder-hole..."
    yd "wait, no, what? hold on-"
    sg "and easy-access parking..."
    yd "no, go back to the thing with the murder and the deaths-"
    sg "since i can tell you're a smart shopper, and not easily swindled..."
    sg "it can be yours for the low, low price of..."
    sg "only 1 million coins!"
    sg "what a steal!"
    sg "can't get a shop here for less than 10 billion coins, honestly."
    yd "....."
    m "....."
    yd "that's super unreasonable."
    y "especially since it comes with a murder-hole."
    yd "whatever that is."
    y "...and if it's such a good deal, why are you having trouble selling it?"
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "i'm almost never on the island, and it turns out there's a ton of paperwork and rules..."
    y "...we'll just take a look around."
    show shadyguy_grin
    hide shadyguy_unsure
    with dissolve
    sg "sure. let me know if anything catches your eye."
    hide shadyguy_grin with dissolve
    hide mai_fl_flip
    show mai_idle_ff_beach
    with dissolve
    m "can you believe this?"
    y "yeah... well, he's a shady guy, what did you expect?"
    show mai_idle_ff_smile with dissolve
    m "it's perfect!"
    yd "...what?"
    m "and the murder-hole will be excellent storage for-"
    yd "it's like a million - no, it's literally - a million coins."
    hide mai_idle_ff_smile with dissolve
    m "oh. right."
    y "let's just look around."
    y "maybe i'll buy you something."
    m "...alright."
    y "(maybe i can figure out a way to get this place for her?)"
    hide mai_idle_ff_beach with dissolve
    "look for clues."
    call screen ember_island_shop

label ember_shop1:
    $ ember_shopspot1 = True
    y "\"for hire\"... hmm...."
    show shadyguy_grin with dissolve
    sg "looking to hire some muscle?"
    sg "his, uh, his body is for rent."
    y "I'm getting that."
    sg "so i mean, if you're looking for some wetwork..."
    yd "like, murder?"
    sg "yeah."
    sg "or you need to be peed on."
    yd "are you trying to tell me he's a hooker?"
    sg "no, no, nothing like that..."
    sg "except yes."
    sg "gotta admit, it's a good picture."
    yd "...it's just a drawing of a helmet."
    sg "it's a sexy helmet though, that's the thing."
    sg "mmmm..."
    y "..."
    y "you okay, buddy?"
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "yeah... i uh, i lost a card game to him once."
    yc "oh, no. and he made you..."
    sg "yeah."
    sg "i had to let him post a flyer here."
    yd "....oh."
    y "well, at least it wasn't-"
    sg "and give him a handjob."
    yd "yup, there it is."
    sg "word of advice... don't hit on 19."
    hide shadyguy_unsure with dissolve
    if ember_shopspot1 and ember_shopspot2 and ember_shopspot3 and ember_shopspot4:
        jump after_ember_shop
    else:
        "you return to looking for clues."
        call screen ember_island_shop

label ember_shop2:
    $ ember_shopspot2 = True
    "you read a posting on the wall."
    y "\"2nd hand tank for cheap!\""
    show shadyguy_grin with dissolve
    sg "need a tank?"
    yd "...rarely."
    y "why do you even have one?"
    sg "i won it."
    sg "sucker didn't even know what hit him."
    sg "went 20 rounds in blind man's bluff... took him for everything he had."
    sg "ran out of coin, but had the deed to an old tank he fixed up."
    sg "i didn't want a tank, but when something like that's on the table..."
    sg "hell, when anything's on the table..."
    sg "you go for it, know what i mean?"
    y "i guess."
    sg "let me know if you change your mind on it... i'll give you a good deal."
    hide shadyguy_grin with dissolve

    if ember_shopspot1 and ember_shopspot2 and ember_shopspot3 and ember_shopspot4:
        jump after_ember_shop
    else:
        "you return to looking for clues."
        call screen ember_island_shop

label ember_shop3:
    $ ember_shopspot3 = True
    "you look at the weapons on the wall."
    show shadyguy_grin with dissolve
    sg "ah... i can see you're a man of taste."
    sg "those knives-"
    show mai_fl_flip:
        xpos 200
    with dissolve
    m "are knockoffs."
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "what...? no, they're rare-"
    m "they're knockoffs."
    m "cheap replicas of the shop this is modeled on."
    m "i know. they're misproportioned -- too much weight in the handle."
    m "plus they're dull and uneven length."
    m "so... knockoffs."
    show shadyguy_grin
    hide shadyguy_unsure
    with dissolve
    sg "can't fool you, huh?"
    sg "you know your stuff, little lady."
    m "...."
    sg "well, you're right."
    sg "my brother added these."
    sg "but i can assure you the swords are real and one-of-a-kind."
    sg "and not for sale."
    sg "these are the actual dueling swords of the championship match between-"
    m "fake, too."
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "no, these are definitely-"
    m "fake. i have - i mean, the armory in the city has - the real ones."
    sg "....."
    sg "alright it's true!"
    sg "you're the first to ever notice."
    sg "but i had the real ones once."
    sg "i had just picked them up... my very first purchase as a shopowner."
    sg "i stopped into the pub for a quick drink when i was approached by the devil himself."
    sg "told me he had exact replicas and 10,000 coins and wanted to know if i'd be willing to trade."
    sg "of course i told him no."
    sg "then he offered to play me for them."
    sg "if i won, he'd give me his swords and coins, if he won, i'd give him my swords."
    sg "lost it all in one hand of glent."
    yd "...glent?"
    sg "yeah, you haven't heard of it? it's a collectible card game, sweeping the nations. tons of fun."
    yd "are you sure you're saying it right?"
    sg "of course! glent. what else would it be?"
    y "......"
    sg "anyway, played him and lost."
    sg "and he was gracious enough to give me the replica swords anyway."
    sg "they're worthless enough..."
    m "why didn't you just... refuse to give him the swords?"
    sg "what kind of man goes back on a gentleman's agreement?"
    sg "no. you say you'll do something, you do it."
    sg "integrity is the most valuable currency, and all we have."
    yd "...your name is \"shady guy\"."
    show shadyguy_grin
    hide shadyguy_unsure
    with dissolve
    sg "that's not my name."
    sg "but i like it."
    sg "let's keep it that way."
    sg "anyway... let me know if something else catches your eye."
    hide shadyguy_grin with dissolve
    hide mai_fl_flip with dissolve

    if ember_shopspot1 and ember_shopspot2 and ember_shopspot3 and ember_shopspot4:
        jump after_ember_shop
    else:
        "you return to looking for clues."
        call screen ember_island_shop

label ember_shop4:
    $ ember_shopspot4 = True
    "you look closely at the scrolls."
    show shadyguy_grin with dissolve
    sg "are you a firebender perchance?"
    y "i am."
    m_ "sort of..."
    ya "you watch your mouth, woman!"
    ya "why don't you come over here and-"
    yc "wait no i'm sorry! i take it back!"
    play sound "audio/thud.mp3"
    scene black
    with flash
    yc "......."
    yc "...ugh..."
    scene bg_a_armory
    show shadyguy_grin
    with dissolve
    yc "what happened...?"
    sg "quite an arm on that young lady."
    yc "right."
    yd "what were we talking about?"
    sg "you were looking at these firebending scrolls."
    sg "there's also one waterbending scroll."
    sg "incredibly, unbelievably rare."
    sg "probably the best thing i own, to be honest."
    yd "how in the world did you come by that?"
    sg "a pirate captain, believe it or not."
    sg "won it in a dice game."
    sg "i don't normally go for anything other than cards, but this was a special occasion."
    y "why?"
    sg "i was pissing-in-the-closet, eating-coins-because-they-look-like-food drunk."
    y "oh."
    sg "he was not happy about it, but he turned it over like a man."
    sg "gotta respect that."
    sg "let me know if you'd like to buy it."
    hide shadyguy_grin with dissolve
    if ember_shopspot1 and ember_shopspot2 and ember_shopspot3 and ember_shopspot4:
        jump after_ember_shop
    else:
        "you return to looking for clues."
        call screen ember_island_shop

label after_ember_shop:
    show mai_idle_ff_beach with dissolve
    y "hey... i have an idea."
    m "what?"
    y "i think we should challenge him to a wager."
    y "a game of cards or something."
    m "what are you talking about?"
    y "i think we can get you this shop."
    show mai_idle_ff_surprised with dissolve
    m "what? are you serious?"
    y "yeah. he seems to have a serious gambling problem, but sticks to his word."
    y "i think we can get you this place."
    hide mai_idle_ff_surprised
    show mai_idle_ff_smile
    with dissolve
    m "what do you need?"
    y "dunno. what do we have to gamble with?"
    m "um... we could... let him see me naked?"
    yd "...maybe."
    y "anything else?"
    show mai_idle_ff_angry
    hide mai_idle_ff_smile
    with dissolve
    m "oh, me naked isn't good enough?"
    ya "would you just focus?"
    ya "do you want this place or not?"
    hide mai_idle_ff_angry
    show mai_idle_ff_smile
    with dissolve
    m "i want it."
    m "let's offer him all your money."
    ya "what?"
    m "well, i didn't bring any."
    yd "...."
    yd "fuck."
    yd "fine."
    hide mai_idle_ff_smile
    hide mai_idle_ff_beach
    with dissolve
    show shadyguy_grin
    show mai_fl_flip:
        xpos 250
    with dissolve
    sg "so, what can i do for you two?"
    y "we'd like to make you an offer."
    sg "oh? for what?"
    y "for your shop."
    sg "i'm all ears."
    y "we'll play for it."
    hide shadyguy_grin
    show shadyguy_unsure
    with dissolve
    sg "what?"
    y "you and i will play a game for it. a game of your choosing."
    sg "i don't gamble any more."
    sg "i love it, don't get me wrong."
    sg "love it so much."
    sg "i miss it... the rush... the thrill of laying it all on the line..."
    sg "and leaving with everything... or nothing..."
    sg "but that's behind me."
    sg "besides, what do you even have that i want?"
    yd "i'll give you... [fmoney] coins."
    if fmoney >= 1000000:
        sg "that's.... why don't you just buy it, then?"
        y "because i want the chance to win the shop and keep the money."
    else:
        y "it's everything i have."
        sg "hmm... that's much less than this is worth."
        y "which is why we're gambling for it."
    sg "hmmm.... what else?"
    m "...i'll let you see me naked."
    show shadyguy_grin
    hide shadyguy_unsure
    with dissolve
    sg "what? really?"
    m "yes."
    sg "now {i}that's{/i} tempting."
    sg "anything else?"
    y "no. that's the deal. [fmoney] coins and mai naked, take it or leave it."
    sg "hmmm..."
    sg "alright. one last bet. a game of blind man's bluff. that's my choice."
    sg "i've had good luck with it in the past."
    sg "i'll explain the rules if you're sure you're up for it."
    m "please, zuko?"
    m "it would mean so much."
    m "i'd owe you... anything."
    menu:
        "gamble everything for mai":
            y "...i'm in."
            show mai_fl_flip_smile:
                xpos 250
            with dissolve
            sg "good lad."
            sg "now for the rules."
            jump blind_man_bluff_rules
        "she's not worth it":

            y "i've changed my mind."
            m "oh."
            y "come on, mai. let's go."
            scene black
            scene bg_a_beach_02
            show mai_idle_fl_beach
            with dissolve
            yc "sorry, mai."
            m "it's okay."
            m "maybe it's just not supposed to happen."
            m "i mean, if you had gotten the deed, there's no end to the things i would have done for you..."
            m "seriously. anything."
            yd "...anything?"
            m "anything."
            m "...but that didn't happen."
            m "and i'm a little bummed."
            m "so we'll just walk a bit and head back."
            jump ember_party_start

label blind_man_bluff_rules:
    $ shady_card = 0
    sg "young lady, i'm going to ask you to step aside."
    hide mai_fl_flip_smile with dissolve
    m "...what?"
    sg "this is between him and i."
    yd "go ahead, mai."
    yd "let me concentrate."
    m "...."
    hide mai_fl_flip with dissolve
    sg "good."
    scene black
    scene bg_a_armory
    show shadyguy_bluff_grin
    with dissolve
    sg "first, put your money on the counter here. i'm gonna lock it up."
    "shady takes your money and puts it in a safe behind the counter."
    sg "i'll return it if you win."
    "he pulls out a piece of paper from the safe."
    sg "this is the deed to the property."
    sg "i'm gonna leave it on the counter in plain sight."
    sg "good? good. now, let's get down to it."
    sg "rules are simple."
    sg "this is a game about bluffing as much as it is strategy."
    sg "we each put a card on our forehead, facing out towards the other player."
    sg "so, you can see my card, and i can see your card, but we can't see our own."
    sg "if your card is higher than mine, you win."
    sg "so, you have to guess if yours is higher or lower than mine."
    sg "of course, i'm an expert at this."
    sg "so, every time you bluff, i learn more about how you lie, and you lose a bluff trick."
    sg "so, it might be worth it to be sincere. i might or might not believe you..."
    sg "normally, we'd bet increasing sums per round, but since there's only one thing on the table each..."
    sg "we'll play by \"Jang Hui\" rules."
    yd "\"jang hui\"?"
    sg "a variation of \"fire fountain city\" rules that i prefer."
    yd "..."
    sg "you think i've only been shady in one city?"
    sg "i've been all over, man."
    sg "i've got std's you've never even heard of."
    sg "alright, so, with \"jang hui\" rules, we are each allowed to draw one replacement card per turn."
    sg "so, if i think i've got a low card i might switch it out..."
    sg "and the same goes for you."
    sg "oh, and aces are high. that means an ace is higher than a king."
    yd "can we play a practice round?"
    sg "no, we play for keeps. but we will do best 2 out of 3."
    jump blind_man_bluff

label mai_anal:
    m "......."
    y "what?"
    m "you're amazing."
    y "aw, it's nothing."
    hide mai_idle_fl_beach
    hide mai_idle_fl_smile
    show mai_idle_ff_beach
    with dissolve
    m "no, that was... unbelievable."
    show mai_idle_ff_smile with dissolve
    m "you..."
    m "{i}you."
    m "is... this happiness?"
    yd "you have to ask?"
    yd "you poor thing."
    m "i can't believe you would do that for me."
    m "i owe you."
    m "you must... love me to do those things for me."
    yd "I-"
    m "you don't have to say it."
    m "but i know it."
    m "do you want to..."
    m "maybe..."
    show mai_idle_ff_blush
    show mai_idle_ff_blink
    with dissolve
    m "...have some fun?"
    ys "yeah!"
    y "i think i saw yahtzee in the hut. maybe jenga."
    yd "i saw monopoly, but i mean, unless you really {i}want{/i} a fight-"
    hide mai_idle_ff_blink with dissolve
    m "no, i mean..."
    m "well, let me put it this way..."
    "mai casually, gracefully, undoes her outfit, which falls into the sand."
    stop music fadeout 2
    play music "audio/Unwritten Return.mp3" fadein 2
    show mai_idle_ff_nude
    hide mai_idle_ff_beach
    hide mai_idle_ff_smile
    show mai_idle_ff_smile
    hide mai_idle_ff_blush
    show mai_idle_ff_blush
    show mai_idle_ff_blink
    with dissolve
    m "...fun."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "..."
    ys "woo!"
    m "oh shut up."
    m "and take your clothes off."
    with ushake
    yn "alright. i'm ready."
    hide mai_idle_ff_blink with dissolve
    m "there's something i really... {i}really{/i} want to do."
    ynd "what-"
    show maan maan00 with sshake
    yng "whoa!"
    yng "you're ready, huh?"
    show maan maan08
    m "like you have no idea."
    ynd "watcha doing there?"
    m "...."
    yng "you're not getting cold feet are you?"
    m "i'm preparing."
    m "...."
    play sound "audio/gltch2.mp3"
    show maan maan07
    with pflash
    m "{size=+6}ah!"

    yna "fuck!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yn "your ass? are you sure?"
    m "ahh... yes..."
    m "ah... ah..."
    yn "you okay?"
    m "it's... fine... i just need..."
    m "ah... need to adjust..."
    m "give me a minute to..."
    m "............"
    play sound "audio/gltch2.mp3"
    show maan maan102
    with vshake
    m "{size=+6}yes!"
    ync "ungh!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "yes, zuko!"
    yn "what happened to taking it slow?"
    m "oh, fuck that."
    show maan maan103
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "ohhh..."
    m "yes... yes... yes!... yes!"
    ync "you're... ah... being a little... ah... rough..."
    m "don't be a baby, zuko..."
    m "i know you... ah... wanted this."
    m "you're so... easy to... ah... read."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yn "and i... thought you wanted to go slow..."
    m "slow? with this huge..."
    m "...shut up, zuko."
    m "...."
    m "i need more!"
    show maan maan104
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "ah! what's gotten into you, mai?!"
    m "fuck... ah... \"slow\"..."
    m "i want you... ah... in..."
    m "in my fucking... ah... asshole..."
    m "i don't care what... ungh... i said..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "mai, i can't last much longer..."
    scene maan19
    show maan maan101
    m "yeah, that's it, zuko! that's it!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink

    m "i'm gonna squeeze out every fucking drop when you cum."
    m "every fucking drop is going in my asshole, zuko."
    m "i don't even care what you want... i want an asshole full of cum."
    m "got it?"
    m "i'm not gonna slow down until you fill me up!"
    m "i want it! i want it!"
    menu:
        "stay with the close up":
            show maan maan101
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "i... mmph... feel you in there, zuko."
            m "my... ah... ass is very... ah... sensitive."
            m "you're swelling up... you're... ah... going to cum, aren't you?"
            m "cum zuko! cum for me!"
            m "fill my ass!"
            yna "here it comes!"
            m "yes, baby! cream in me!"
            play sound "audio/splurt3.ogg"
            show maan maan14
            with flash
            m "yes!"
            play sound "audio/splurt2.ogg"
            show maan maan15
            with flash
            m "oh zuko... ohh..."
            play sound "audio/splurt2.ogg"
            with flash
            m "it's... ah... wait..."
            play sound "audio/splurt3.ogg"
            show maan maan16
            with flash
            m "ah... st... stop... ah..."
            play sound "audio/splurt2.ogg"
            with flash
            m "mmmm... ah... so... satisfying... ahhh...."
            play sound "audio/splurt2.ogg"
            with flash
            m "......"
            m "it's... so.... there's so much..."
            yn "fuck..."
            ynd "what got into you?"
            m "well... i think... you did."
            show maan maan18
            show maan_spermdrip_closeup
            with dissolve
            m "i really needed that."
            m "...wow...look at that..."
            m "oh, that's... a lot... of... um..."

            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show maan maan08
            hide maan_spermdrip_closeup
            show maan_spermdrip
            with dissolve
            yn "what? you're suddenly shy?"
            m "No! i just..."
            m "now that we're finished, i..."
            m "and i realize what we..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "....."
            show maan maan00
            hide maan_spermdrip
            show nude_mai_fl_flip:
                xpos 100
            with dissolve
            m "......."
            jump after_mai_anal
        "zoom out":

            show maan maan104
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "i... mmph... feel you in there, zuko."
            m "my... ah... ass is very... ah... sensitive."
            m "you're swelling up... you're... ah... going to cum, aren't you?"
            m "cum zuko! cum for me!"
            m "fill my ass!"
            yna "here it comes!"
            m "yes, baby! cream in me!"
            play sound "audio/splurt3.ogg"
            show maan maan09
            with flash
            m "yes!"
            play sound "audio/splurt2.ogg"
            show maan maan10
            with flash
            m "oh zuko... ohh..."
            play sound "audio/splurt2.ogg"
            with flash
            m "it's... ah... wait..."
            play sound "audio/splurt3.ogg"
            show maan maan11
            with flash
            m "ah... st... stop... ah..."
            play sound "audio/splurt2.ogg"
            with flash
            m "mmmm... ah... so... satisfying... ahhh...."
            play sound "audio/splurt2.ogg"
            with flash
            m "......"
            m "it's... so.... there's so much..."
            yn "fuck..."
            ynd "what got into you?"
            m "well... i think... you did."
            show maan maan08
            show maan_spermdrip
            with dissolve
            m "i really needed that."
            m "...wow...look at that..."
            m "oh, that's... a lot... of... um..."

            show ctcblink
            $ renpy.pause()
            hide ctcblink
            yn "what? you're suddenly shy?"
            m "No! i just..."
            m "now that we're finished, i..."
            m "and i realize what we..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "....."
            show maan maan00
            hide maan_spermdrip
            show nude_mai_fl_flip:
                xpos 100
            with dissolve
            m "......."
            jump after_mai_anal

label after_mai_anal:
    show mai_fl_flip_angry:
        xpos 100
    with dissolve
    m ".....well, don't just sit there."
    scene black
    scene bg_a_beach_01
    show nude_mai_fl_flip:
        xpos 100
    show mai_fl_flip_angry:
        xpos 100
    with dissolve
    ynd "what?"
    m "let's just go."
    yn "back up a second. that was fun."
    yn "we both enjoyed that."
    ynd "right?"
    hide mai_fl_flip_angry
    with dissolve
    m "...yes."
    m "i really enjoyed that."
    m "it... made me happy."
    ynd "you don't look it."
    hide nude_mai_fl_flip
    hide mai_fl_flip_angry
    show mai_idle_fl_nude
    show mai_idle_fl_smile
    with dissolve
    m "i feel... fulfilled. in a way that i never have before."
    m ".....and a little sore."
    yn "great! so what's the problem?"
    hide mai_idle_fl_smile with dissolve
    m "we're not going to have any more sex."
    ync "w...what? why?"
    ynd "a minute ago you were begging me to fill your ass!"
    ynd "what happened to \"i want you in my fucking asshole, i don't care what i said\"?"
    show mai_idle_fl_angry
    show mai_idle_fl_blush
    with dissolve
    m "ugh. you're so... crude, zuko."
    ynd "you said it."
    m "in... in the heat of the moment."

    hide mai_idle_fl_nude
    hide mai_idle_fl_blush
    hide mai_idle_fl_angry
    show mai_idle_ff_nude
    show mai_idle_ff_angry
    show mai_idle_ff_blush
    show mai_idle_ff_blink
    with dissolve

    m "I feel too slutty."
    m "it's not... that can't be me."
    ynd "what? fun? easy going?"
    hide mai_idle_ff_blink with dissolve
    m "i guess you don't know me, zuko."
    ynd "i'm really confused."
    ynd "are you and i... finished?"
    hide mai_idle_ff_angry with dissolve
    m "no, i still want to be with you."
    ynd "without sex. which we've already been having."
    show mai_idle_ff_angry
    hide mai_idle_ff_blush
    show mai_idle_ff_blush
    with dissolve
    m "is that such a problem?"
    menu:
        "i guess not":
            ynd "well, i mean, no, i guess."
            yn "but... it doesn't seem like what you really want."
        "yeah it's a problem!":

            $ mai_aff -=1
            yna "yeah! my dick belongs in and/or on you, girl!"
            yn "but mostly... it doesn't seem like what you really want."

    yn "i thought we were really getting along."
    m "i'm not discussing this anymore."
    m "i'll see you back at the house before the party."
    scene black
    scene bg_a_beach_01
    show blue_20perc_transparent
    with dissolve
    ynd "what in the world is going on with her?"
    yn "....women."
    yn "oh. i should put my clothes back on."
    ynd "there's... some people staring."
    ynd "...hello..."
    yn "...."
    yn "i should go."
    "you hastily throw your clothes back on."
    y "guess i should head to the house, it's starting to get dark."
    $ ember = 9
    stop music fadeout 2
    play music "audio/Blue Ska.mp3" fadein 2
    "you get attacked by violent sandcrabs!"
    yd "....what?"
    ya "ahh!"
    ya "why??!"
    $ crab_battles = True
    show screen crabstats
    show crabshuffle with dissolve
    jump crab_battle_player

label crab_battle_player:


    if crab_standin:
        if crab_standin_health <=0:
            if crab_standin_normal:
                $ normal_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_normal = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump crab_battle_player2
            if crab_standin_strong:
                $ strong_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_strong = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump crab_battle_player2
            if crab_standin_legend:
                $ legend_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_legend = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump crab_battle_player2
            if crab_standin_bessie:
                $ crab_standin = False
                $ crab_standin_bessie = False
                "bessie falls asleep to recover!"
                yc "wait...."
                "it's your turn again."
                $ crabs_caught -=1
                $ bessie_dead = True
                $ crab_standin_bessie = False
                jump crab_battle_player2
            if crab_standin_musky:
                $ crab_standin = False
                $ crab_standin_musky = False
                "ol' musky falls asleep to recover!"
                yc "wait...."
                "it's your turn again."
                $ crabs_caught -=1
                $ musky_dead = True
                $ crab_standin_musky = False
                jump crab_battle_player2
            if crab_standin_stank:
                $ crab_standin = False
                $ crab_standin_stank = False
                "the stank falls asleep to recover!"
                yc "wait...."
                "it's your turn again."
                $ crabs_caught -=1
                $ stank_dead = True
                $ crab_standin_stank = False
                jump crab_battle_player2
        else:


            if hyperboom ==1:
                "hyper-boom snip activates!"
                if crab_standin_normal:
                    $ crab_health -=11
                    show text "{color=#f00}{b}-11 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump crab_battle_crab
                if crab_standin_strong:
                    $ crab_health -=23
                    show text "{color=#f00}{b}-23 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump crab_battle_crab
                if crab_standin_legend:
                    $ crab_health -= 45
                    show text "{color=#f00}{b}-45 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump crab_battle_crab
                if crab_standin_musky:
                    $ crab_health -= 80
                    show text "{color=#f00}{b}-80 enemy crab health" at truecenter with dissolve
                    "ol' musky rains fire-snips from hell on the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump crab_battle_crab

                if crab_standin_stank:
                    $ crab_health -= 100
                    show text "{color=#f00}{b}-100 enemy crab health" at truecenter with dissolve
                    "the stank snick-snack-paddy-wacks the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump crab_battle_crab
            else:
                if crab_player_health <=0:
                    "you lose!"
                    jump crab_battle_lose
                else:
                    jump crab_battle_player2


    if crab_player_health <=0:
        "you lose!"
        jump crab_battle_lose
    else:
        jump crab_battle_player2

label crab_battle_player2:
    menu:
        "crab battle!" if not crab_standin:
            if crabs_caught >=1:
                if normal_crabs >=1:
                    "you send out a normal crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 50
                    $ crab_standin_normal = True
                    jump crab_battle_player

                if strong_crabs >=1:
                    "you send out a strong crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 80
                    $ crab_standin_strong = True
                    jump crab_battle_player

                if legend_crabs >=1:
                    "you send out a legendary crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 200
                    $ crab_standin_legend = True
                    jump crab_battle_player

                if bessie and not bessie_dead:
                    "you send out bessie!"
                    "she takes your place in the battle!"
                    "she has no special attack, but never misses!"
                    $ crab_standin = True
                    $ crab_standin_health = 180
                    $ crab_standin_bessie = True
                    jump crab_battle_player

                if olmusky and not musky_dead:
                    "you send out ol' musky!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 250
                    $ crab_standin_musky = True
                    jump crab_battle_player

                if stank and not stank_dead:
                    "you send out the stank!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 500
                    $ crab_standin_stank = True
                    jump crab_battle_player
            else:

                "you don't have any crabs!"
                y "....normally a good thing, but whatever."
                jump crab_battle_player


        "snip!" if crab_standin and not crab_standin_musky:
            if crab_standin_bessie:
                $ crab_health -=20
                show text "{color=#f00}{b}-20 enemy crab health" at truecenter with dissolve
                "bessie snips the enemy crab!"
                hide text with dissolve
                ya "take that!"
                jump crab_battle_crab
            $ randcrabpunch = renpy.random.randint(1, 2)
            if crab_standin_normal:
                if randcrabpunch ==1:
                    $ crab_health -=7
                    show text "{color=#f00}{b}-7 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump crab_battle_crab
            if crab_standin_strong:
                if randcrabpunch ==1:
                    $ crab_health -=15
                    show text "{color=#f00}{b}-15 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump crab_battle_crab
            if crab_standin_legend:
                if randcrabpunch ==1:
                    $ crab_health -=30
                    show text "{color=#f00}{b}-30 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump crab_battle_crab
            if crab_standin_stank:
                if randcrabpunch ==1:
                    $ crab_health -=80
                    show text "{color=#f00}{b}-80 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump crab_battle_crab



        "hyper-boom snip - powerful, takes an extra turn, always hits" if crab_standin and not crab_standin_bessie and not crab_standin_musky:
            $ hyperboom = 1
            "your crab charges it's attack! it's glowing!"
            jump crab_battle_crab

        "ol' musky super snip" if crab_standin_musky:
            $ hyperboom = 1
            "ol' musky charges it's attack! it's glowing!"
            jump crab_battle_crab

        "punch" if not crab_standin:
            $ randcrabpunch = renpy.random.randint(1, 3)
            if randcrabpunch ==1:
                if crabs_killed ==0:
                    $ crab_health -=10
                    show text "{color=#f00}{b}-10 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==1:
                    $ crab_health -=12
                    show text "{color=#f00}{b}-12 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==2:
                    $ crab_health -=14
                    show text "{color=#f00}{b}-14 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==3:
                    $ crab_health -=16
                    show text "{color=#f00}{b}-16 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==4:
                    $ crab_health -=18
                    show text "{color=#f00}{b}-18 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==5:
                    $ crab_health -=20
                    show text "{color=#f00}{b}-20 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==6:
                    $ crab_health -=22
                    show text "{color=#f00}{b}-22 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==7:
                    $ crab_health -=24
                    show text "{color=#f00}{b}-24 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==8:
                    $ crab_health -=26
                    show text "{color=#f00}{b}-26 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==9:
                    $ crab_health -=28
                    show text "{color=#f00}{b}-28 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==10:
                    $ crab_health -=30
                    show text "{color=#f00}{b}-30 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==11:
                    $ crab_health -=32
                    show text "{color=#f00}{b}-32 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==12:
                    $ crab_health -=34
                    show text "{color=#f00}{b}-34 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==13:
                    $ crab_health -=36
                    show text "{color=#f00}{b}-36 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==14:
                    $ crab_health -=38
                    show text "{color=#f00}{b}-38 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==16:
                    $ crab_health -=40
                    show text "{color=#f00}{b}-40 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==16:
                    $ crab_health -=42
                    show text "{color=#f00}{b}-42 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==17:
                    $ crab_health -=44
                    show text "{color=#f00}{b}-44 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==18:
                    $ crab_health -=46
                    show text "{color=#f00}{b}-46 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==19:
                    $ crab_health -=48
                    show text "{color=#f00}{b}-48 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==20:
                    $ crab_health -=49
                    show text "{color=#f00}{b}-49 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==21:
                    $ crab_health -=50
                    show text "{color=#f00}{b}-50 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed >=22:
                    $ crab_health -=50
                    show text "{color=#f00}{b}-50 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab


            if randcrabpunch ==2:
                if crabs_killed ==0:
                    $ crab_health -=14
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-14 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==1:
                    $ crab_health -=19
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-19 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==2:
                    $ crab_health -=24
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-24 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==3:
                    $ crab_health -=27
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-27 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==4:
                    $ crab_health -=31
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-31 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==5:
                    $ crab_health -=34
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-34 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==6:
                    $ crab_health -=37
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-37 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==7:
                    $ crab_health -=40
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-40 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==8:
                    $ crab_health -=43
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-43 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==9:
                    $ crab_health -=46
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-46 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed ==10:
                    $ crab_health -=49
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-49 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
                if crabs_killed >=11:
                    $ crab_health -=54
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-54 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump crab_battle_crab
            if randcrabpunch ==3:
                "you miss!"
                jump crab_battle_crab
        "defend":

            $ player_crab_def = True
            "you defend!"
            jump crab_battle_crab
        "try to catch":

            if crab_pockets == crabs_caught:
                "you only have [crab_pockets] pockets and they're all full of crabs!"
                "buy more pockets to catch more crabs!"
                jump crab_battle_player
            else:
                $ randcrabcatch = renpy.random.randint(1, 5)
                if randcrabcatch ==1:
                    "you caught the crab!"
                    "he settles happily into your pocket."
                    yc "...what?"

                    if normal_crab:
                        hide crabshuffle with dissolve
                        $ normal_crabs +=1
                    if strong_crab:
                        hide strongcrabshuffle with dissolve
                        $ strong_crabs +=1
                    if legend_crab:
                        hide legendcrabshuffle with dissolve
                        $ legend_crabs +=1
                    $ crab_battle_total +=1
                    $ crabs_caught +=1
                    $ normal_crab = False
                    $ strong_crab = False
                    $ legend_crab = False
                    jump next_crab_battle
                if randcrabcatch ==2:
                    "your attempt to catch failed!"
                    jump crab_battle_crab
                if randcrabcatch ==3:
                    "your attempt to catch failed!"
                    jump crab_battle_crab
                if randcrabcatch ==4:
                    "your attempt to catch failed!"
                    jump crab_battle_crab
                if randcrabcatch ==5:
                    "your attempt to catch failed!"
                    jump crab_battle_crab
        "use potion":

            "you have [crab_potions] potion(s)."
            "potions recover up to 250 health."
            if crab_potions >=1:
                "use a potion now?"
                menu:
                    "use potion":
                        if crab_standin:
                            $ crab_potions -=1
                            if crab_standin_normal:
                                $ crab_standin_health = 50
                            if crab_standin_strong:
                                $ crab_standin_health = 80
                            if crab_standin_legend:
                                $ crab_standin_health = 200
                            if crab_standin_bessie:
                                $ crab_standin_health = 180
                            if crab_standin_musky:
                                $ crab_standin_health = 250
                            "ally crab health recovered!"
                            jump crab_battle_player
                        else:

                            $ crab_potions -=1
                            $ crab_player_health = 100
                            "your health recovered!"
                            jump crab_battle_player
                    "don't use potion":

                        jump crab_battle_player
            else:
                "you don't have any potions left!"
                "buy more to use them!"
                jump crab_battle_player

        "run away" if first_crab_battles:
            $ crabrun = renpy.random.randint(1, 4)
            if crabrun == 1 or crabrun == 2 or crabrun == 3:
                "escape failed! crab flanked you!"
                jump crab_battle_crab
            else:

                "escape successful! you dodged the crab!"
                hide screen crabstats
                $ crab_standin = False
                $ crab_player_health = 100
                $ crab_standin_normal = False
                $ crab_standin_strong = False
                $ crab_standin_legend = False
                $ crab_standin_bessie = False
                if bessie_dead:
                    $ crabs_caught +=1
                    $ bessie_dead = False
                jump emberday


label crab_battle_crab:
    if crab_health <=0:
        hide crabshuffle
        hide strongcrabshuffle
        hide legendcrabshuffle
        with dissolve
        $ crabs_killed +=1
        $ crab_battle_total +=1
        play sound "audio/win2.mp3"
        "you kicked that crab's ass!"
        "you level up!"
        jump next_crab_battle
    else:
        if crab_charge:
            if player_crab_def:
                $ randcrabattack = renpy.random.randint(1, 2)
                if randcrabattack ==1:
                    if crab_standin:
                        if normal_crab:
                            $ crab_standin_health -=7
                            show text "{color=#f00}{b}-7 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if strong_crab:
                            $ crab_standin_health -=15
                            show text "{color=#f00}{b}-15 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if legend_crab:
                            $ crab_standin_health -=30
                            show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                    else:

                        if normal_crab:
                            $ crab_player_health -=7
                            show text "{color=#f00}{b}-7 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if strong_crab:
                            $ crab_player_health -=15
                            show text "{color=#f00}{b}-15 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if legend_crab:
                            $ crab_player_health -=30
                            show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player

                if randcrabattack ==2:
                    "the crab attacks and misses!"
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump crab_battle_player
            else:

                $ randcrabattack = renpy.random.randint(1, 2)
                if randcrabattack ==1:
                    if crab_standin:
                        if normal_crab:
                            $ crab_standin_health -=14
                            show text "{color=#f00}{b}-14 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if strong_crab:
                            $ crab_standin_health -=30
                            show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if legend_crab:
                            $ crab_standin_health -=60
                            show text "{color=#f00}{b}-60 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                    else:
                        if normal_crab:
                            $ crab_player_health -=14
                            show text "{color=#f00}{b}-14 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if strong_crab:
                            $ crab_player_health -=30
                            show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player
                        if legend_crab:
                            $ crab_player_health -=60
                            show text "{color=#f00}{b}-60 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump crab_battle_player

                if randcrabattack ==2:
                    "the crab attacks and misses!"
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump crab_battle_player
        else:

            $ randcrabattack = renpy.random.randint(1, 3)
            if randcrabattack ==1:
                if crab_standin:
                    if normal_crab:
                        $ crab_standin_health -=7
                        show text "{color=#f00}{b}-7 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump crab_battle_player
                    if strong_crab:
                        $ crab_standin_health -=15
                        show text "{color=#f00}{b}-15 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump crab_battle_player
                    if legend_crab:
                        $ crab_standin_health -=30
                        show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump crab_battle_player
                else:

                    if normal_crab:
                        $ crab_player_health -=7
                        show text "{color=#f00}{b}-7 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump crab_battle_player
                    if strong_crab:
                        $ crab_player_health -=15
                        show text "{color=#f00}{b}-15 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump crab_battle_player
                    if legend_crab:
                        $ crab_player_health -=30
                        show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump crab_battle_player


            if randcrabattack ==2:
                "the crab attacks and misses!"
                $ player_crab_def = False
                jump crab_battle_player
            if randcrabattack ==3:
                "the crab's claws glow! it charges its attack!"
                $ crab_charge = True
                $ player_crab_def = False
                jump crab_battle_player

label next_crab_battle:

    if crab_battle_total <=3:
        $ randcrabselect = renpy.random.randint(1, 5)
        if randcrabselect ==1:
            show crabshuffle with dissolve
            $ crab_health = 50
            $ normal_crab = True
            $ strong_crab = False
            $ legend_crab = False
            "you face a normal battling crab."
            jump crab_battle_player
        if randcrabselect ==2:
            show strongcrabshuffle with dissolve
            $ crab_health = 80
            $ normal_crab = False
            $ strong_crab = True
            $ legend_crab = False
            "you face a strong battling crab."
            jump crab_battle_player
        if randcrabselect ==3:
            show crabshuffle with dissolve
            $ crab_health = 50
            $ normal_crab = True
            $ strong_crab = False
            $ legend_crab = False
            "you face a normal battling crab."
            jump crab_battle_player
        if randcrabselect ==4:
            show strongcrabshuffle with dissolve
            $ crab_health = 80
            $ normal_crab = False
            $ strong_crab = True
            $ legend_crab = False
            "you face a strong battling crab."
            jump crab_battle_player
        if randcrabselect ==5:
            show legendcrabshuffle with dissolve
            $ crab_health = 200
            $ normal_crab = False
            $ strong_crab = False
            $ legend_crab = True
            "you face a legendary battling crab."
            jump crab_battle_player
    else:


        menu:
            "fight another!":

                $ randcrabselect = renpy.random.randint(1, 5)
                if randcrabselect ==1:
                    $ crab_health = 50
                    show crabshuffle with dissolve
                    "you face a normal battling crab."
                    $ normal_crab = True
                    $ strong_crab = False
                    $ legend_crab = False
                    jump crab_battle_player
                if randcrabselect ==2:
                    $ crab_health = 80
                    show strongcrabshuffle with dissolve
                    "you face a strong battling crab."
                    $ normal_crab = False
                    $ strong_crab = True
                    $ legend_crab = False
                    jump crab_battle_player
                if randcrabselect ==3:
                    $ crab_health = 50
                    show crabshuffle with dissolve
                    "you face a normal battling crab."
                    $ normal_crab = True
                    $ strong_crab = False
                    $ legend_crab = False
                    jump crab_battle_player
                if randcrabselect ==4:
                    $ crab_health = 80
                    show strongcrabshuffle with dissolve
                    "you face a strong battling crab."
                    $ normal_crab = False
                    $ strong_crab = True
                    $ legend_crab = False
                    jump crab_battle_player
                if randcrabselect ==5:
                    $ crab_health = 200
                    show legendcrabshuffle with dissolve
                    "you face a legendary battling crab."
                    $ normal_crab = False
                    $ strong_crab = False
                    $ legend_crab = True
                    jump crab_battle_player
            "leave this fucking insanity":

                ":("
                hide screen crabstats
                $ crab_player_health = 100
                $ first_crab_battles = True
                stop music fadeout 2
                play music "audio/Bassa Island Game Loop.ogg" fadein 2
                jump after_crab_battle1

label crab_battle_lose:
    $ normal_crab = True
    $ strong_crab = False
    $ legend_crab = False
    $ musky_crab = False
    $ stank_crab = False
    $ crab_standin = False
    $ crab_standin_normal = False
    $ crab_standin_strong = False
    $ crab_standin_legend = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    $ crab_standin_stank = False
    $ hyperboom = False
    hide legendcrabshuffle
    hide strongcrabshuffle
    hide legendcrabshuffle
    hide muskycrabshuffle
    hide stankcrabshuffle
    with dissolve
    hide screen crabstats
    if bessie_dead:
        $ crabs_caught +=1
        $ bessie_dead = False
    if musky_dead:
        $ crabs_caught +=1
        $ musky_dead = False
    if stank_dead:
        $ crabs_caught +=1
        $ musky_dead = False
    $ crab_standin_stank = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False

    "...and die..."
    "...on the inside."
    "you're more or less fine, physically."
    $ crab_player_health = 100
    "get some potions, buy more pockets, and try again!"
    $ first_crab_battles = True
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg" fadein 2
    if crab_convo:
        jump emberday
    else:
        jump after_crab_battle1

label after_crab_battle1:
    $ normal_crab = True
    $ strong_crab = False
    $ legend_crab = False
    $ musky_crab = False
    $ stank_crab = False
    $ crab_standin = False
    $ crab_standin_normal = False
    $ crab_standin_strong = False
    $ crab_standin_legend = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    $ crab_standin_stank = False
    $ hyperboom = False
    hide legendcrabshuffle
    hide strongcrabshuffle
    hide legendcrabshuffle
    hide muskycrabshuffle
    hide stankcrabshuffle
    with dissolve
    hide screen crabstats
    if bessie_dead:
        $ crabs_caught +=1
        $ bessie_dead = False
    if musky_dead:
        $ crabs_caught +=1
        $ musky_dead = False
    if stank_dead:
        $ crabs_caught +=1
        $ musky_dead = False
    $ crab_standin_stank = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    $ crab_player_health = 100

    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg" fadein 2
    if crab_convo:
        jump emberday
    else:
        show fireguard_halberd with dissolve
        g "psst."
        g "hey."
        yd "what's up?"
        g "i see you're battling crabs."
        ya "well it's not by fucking choice-"
        g "you want in?"
        yd "what?"
        g "the tournament."
        y "the..."
        yd "there's a tournament?"
        g "are you kidding? crab battles are huge on ember island."
        g "this is the premier world location."
        g "...if you've got what it takes."
        g "so, are you interested? want to learn more?"
        $ crab_convo = True
        menu:
            "crabble royale - world champ":
                y "yeah, tell me more."
                g "there are three masters on the island."
                g "me, shady, and fishtits."
                yd "fish.... fishtits?"
                g "you don't know her?"
                g "tell you what, shady's got a boat."
                g "beat him and he might let you use it. if you're packing crabs, she'll show."
                g "li and lo are the current champions."
                g "iroh is the grandsnipper and has never been beaten."
                yd "iroh?"
                g "yeah. he's crazy powerful."
                g "anyway, whenever you want to try me, I guard the house on the hill."
                hide fireguard_halberd with dissolve
                yd "interesting."
                $ crab_tournament_invite = True
                jump emberday
            "nah, i'll pass":

                y "no, thanks."
                y "i might battle for fun, but i'm not up for a whole big thing."
                g "your loss...."
                hide fireguard_halberd with dissolve
                jump emberday

label ember_party_start:
    scene black
    scene emberisland_dock:
        ypos 0
    show blue_20perc_transparent
    with dissolve

    y "well, there it is. the little shack of big-titted horrors."
    yd "these vaginas are going to be the death of me."
    scene black
    scene bg_a_island_hutday
    show blue_20perc_transparent
    with dissolve
    show azula_idle_fl_beach
    with dissolve
    a "it's about time."
    a "where have you been? you've upset mai, that's obvious."
    yd "why do you care?"
    a "oh, i don't. i'm just trying to be nice."
    show tylee_idle_ff_beach:
        xpos -250
    with dissolve
    t "are we almost ready?"
    a "we're waiting on mai, now."
    a "you didn't tell them, did you?"
    t "no, they don't know a thing!"
    yd "what?"
    a "we didn't tell the boys at the party who we are."
    yd "...why?"
    a "I guess i was... intrigued."
    a "i'm so used to people worshiping us-"
    t "they should!"
    show a_idle_fl_face_blink with dissolve
    a "yes, i know, and i love it."
    hide a_idle_fl_face_blink with dissolve
    a "...but for once i just wanted to see how people would treat us if they didn't know who we were."
    hide tylee_idle_ff_beach
    hide azula_idle_fl_beach
    with moveoutleft
    show twins_0 with moveinright
    lal "like waves-"
    ya "ah!"
    yd "every fucking time."
    y "need to put a bell on you two."
    yd "i guess i can follow you by the scent of diaper rash-"
    lal "....."
    lal "...like waves washing away the footprints on the sand..."
    y "shut up."
    lal "...ember island gives everyone a clean slate."
    yd "shut up."
    lal "ember island reveals the true you."
    ya "shut up!"
    hide twins_0 with moveoutright
    show azula_idle_fl_beach
    show tylee_idle_ff_beach:
        xpos -250
    with moveinleft
    show mai_fl_flip:
        xpos 100
    with dissolve
    m "i'm ready."
    a "finally. it's almost dusk and i will {i}not{/i} be late."
    a "let's-"
    lal "to the party!"
    ya "shut up! you're not going!"
    lal "aw."
    ya "That's it! you two are sleeping outside!"
    lal "......."
    y "let's go."
    jump embernight

label dusk_party:
    scene black
    scene bg_a_island_partyhouse
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_beach "hmm."
    yc "it... looks familiar."
    a_beach "it should. it's ours."
    yd "what?"
    a_beach "that, dear brother, is our vacation home."
    yd "we have a vacation home?"
    ya "then why are we staying in damn shack?!"
    yd "i'm sleeping in constant fear of saggy boobs..."
    yc "...they haunt my dreams."
    t_ "i like it! it's full of seashell stuff!"
    m_ "it looks like the beach threw up all over it."
    a_beach "hmm. yes. but did you really {i}want{/i} to stay here, brother?"
    yd "i guess not. i feel... full of sadness when i look at it."
    a_beach "i wonder how many of our mementos are still inside?"
    a_beach "shall we find out?"
    play sound "audio/knocking.mp3"
    "azula walks up and knocks on the door."
    "you hang out to the side and listen in on the conversation."
    chan "um... you're a little early."
    chan "no one's here yet."
    a_beach "you said you'd be partying from dusk to dawn."
    a_beach "it's dusk. so we're here."
    chan "but that's just an expression..."
    a_beach "we are the perfect party guests."
    a_beach "we arrive right on time because we are very punctual."
    chan "uh..... well...."
    chan "......."
    chan "alright, you guys seem... pretty cool."
    chan "you're welcome to the party, but since it's your first time..."
    chan "you've gotta do the \"hunt\" to prove you're worthy to get in."
    a_beach "hunt? of course, a hunt. customary."
    a_beach "well, i'll have you know i'm quite proficient in battle."
    chan "it's not a... it's a scavenger hunt. you guys are really new around here."
    m_ "hold on... a scavenger hunt to get into a party? that's not real."
    "another boy comes to the door."
    rj "yeah, that's totally the requirement, man."
    rj "like, we all had to. for sure."
    t_ "fun! what do we have to find?"
    chan "oh, uh...."
    chan "oh yeah! hold on a sec..."
    chan "here."
    "chan hands azula a page with a riddle on it."
    chan "solve this."
    chan "should take a couple hours, right around the time the party's going."
    "he closes the door in your faces."
    show azula_idle_fl_beach
    show tylee_idle_ff_beach:
        xpos -250
    show mai_fl_flip:
        xpos 100
    with dissolve
    m "...that was rude."
    a "clearly that's the way things are done around here."
    a "hmm... it says there are four items, but i only see one riddle."
    a "we should split up, cover more ground."
    yd "solving the riddle might lead to more-"
    m "this is such a waste of time."
    m "i don't even want to go to this party."
    yd "no, you'd rather sit around be a tease."
    m "...i'll go look down by the shop on the beach."
    hide mai_fl_flip with dissolve
    t "i'll look near the dock."
    hide tylee_idle_ff_beach with dissolve
    a "i'll take the shack, i suppose."
    yd "wait, should we read the riddle first?"
    y "solving it might take us to the item and the next riddle."
    y "the items could be in none of those places."
    a "you can if you'd like, but don't waste time, zuko."
    y "wait- what's this symbol?"
    a "oh, that? that's azulon's seal."
    a "you should really try to learn your family history, brother."
    y "why would it be here?"
    a "who knows?"
    a "get to looking."
    hide azula_idle_fl_beach with dissolve
    y "guess it's up to me."
    $ ember = 10
    jump party_riddles

label party_riddles:
    menu:
        "riddle 1":
            if friddle1:
                y "i've already solved this one."
                jump party_riddles
            else:

                y "\"i move with the wind, and i comfort your head; i aim to help you laugh, and i'm far from lead.\""
                y "scribbled next to it is a note: \"fell off the boat while visiting li and lo.\""
                y "hmm..."
                y "where should i go to look?"
                menu:
                    "dock":
                        jump riddle_dock
                    "shack":

                        jump riddle_shack
                    "shop":

                        jump riddle_shop
                    "party":

                        jump riddle_house

        "riddle 2" if friddle1:
            if friddle2:
                y "i already solved this one."
                jump party_riddles
            else:
                y "\"I turn everything around, but don't move.\""
                y "scribbled next to it is a note: \"given to li and lo.\""
                y "hmm..."
                y "where should i go to look?"
                menu:
                    "shack":

                        jump riddle_shack
                    "shop":

                        jump riddle_shop
                    "party":

                        jump riddle_house

        "riddle 3" if friddle2:
            if friddle3:
                y "i already solved this one."
                jump party_riddles
            else:

                y "\"i have rivers without water, forests without trees, and cities without people.\""
                y "scribbled next to it is a note: \"sold to shop.\""
                y "hmmm...."
                y "where should i go to look?"
                menu:
                    "shop":
                        jump riddle_shop
                    "party":

                        jump riddle_house

        "riddle 4" if friddle3:
            y "\"Young I am tall; old I am short. I love to glow. Breath is my foe.\""
            y "scribbled next to it is a note: \"left in vacation home.\""
            y "hmmm...."
            y "only one place to go, really."
            menu:
                "party":
                    y "guess i'll back to the party."
                    jump riddle_house

label riddle_dock:
    scene emberisland_dock
    show blue_20perc_transparent
    show tylee_idle_ff_beach
    with dissolve
    t "hey, prince!"
    t "any luck?"
    y "clue says it's fell out a boat, so i'm guessing it's around the dock here."
    y "what about you?"
    t "there's lots of metal ornaments down there..."
    t "a wind chime, a knife, a feather, an arrow."
    t "we could be here all night guessing."
    t "which do you think it is?"
    jump riddle_dock_menu

label riddle_dock_menu:
    menu:
        "read riddle 1 again":
            y "\"i move with the wind, and i comfort your head; i aim to help you laugh, and i'm far from lead.\""
            jump riddle_dock_menu
        "choose the wind chime":

            "you dive into the icy-cold water and pull up the wind chime."
            ya "brrrr.... fuck!"
            ya "w-w-w-well... i-i-i-is i-i-it r-r-r-right?"
            t "hmm... doesn't seem to be anything special."
            ya "f-f-f-fuck."
            jump riddle_dock_menu
        "choose the knife":

            "you dive into the icy-cold water and pull up the knife."
            ya "brrrr.... fuck!"
            ya "w-w-w-well... i-i-i-is i-i-it r-r-r-right?"
            t "hmm... doesn't seem to be anything special."
            ya "f-f-f-fuck."
            jump riddle_dock_menu
        "choose the feather":

            "you dive into the icy-cold water and pull up the feather."
            ya "brrrr.... fuck!"
            ya "w-w-w-well... i-i-i-is i-i-it r-r-r-right?"
            play sound "audio/win2.mp3"
            show emberisland_feather with dissolve
            t "this is interesting..."
            ya "w-w-what?"
            t "there's a little symbol on the back..."
            ys "azulon's seal! alright!"
            y "right next to it, it says... \"rest\"."
            yd "huh. wonder what that's for?"
            y "oh, and there's a metal tag with another riddle on it!"
            $ friddle1 = True
            t "great!"
            t "well, i'll leave you to it then."
            t "i'll see you back at the party house!"
            hide tylee_idle_ff_beach
            hide emberisland_feather
            with dissolve
            jump party_riddles
        "choose the arrow":

            "you dive into the icy-cold water and pull up the knife."
            ya "brrrr.... fuck!"
            ya "w-w-w-well... i-i-i-is i-i-it r-r-r-right?"
            t "hmm... doesn't seem to be anything special."
            ya "f-f-f-fuck."
            jump riddle_dock_menu

label riddle_shack:
    scene bg_a_island_hutday
    show blue_20perc_transparent
    show azula_idle_ff_beach
    with dissolve
    if friddle1:
        a "what is it, brother?"
        y "found another clue."
        a "oh?"
        y "yeah, says it was given to li and lo, so the thing's here."
        a "well, there are so many utterly {i}useless{/i} things here."
        a "it could take all night."
        a "look around."
        jump riddle_shack_menu
    else:

        y "any luck?"
        a "why are you here?"
        yd "i'm looking, too."
        a "any clues?"
        y "uh... it says \"fell out of boat while visiting li and lo\"."
        a "...maybe you should look by the dock."
        a "leave. i'm looking here for the other items."
        yd "but you don't even know what you're looking for."
        a "go!"
        jump party_riddles

label riddle_shack_menu:

    menu:
        "read riddle 2":
            y "\"I turn everything around, but don't move.\""
            jump riddle_shack_menu
        "look at clock":

            "you climb over a bunch of shit and take the clock."
            "azula grabs it from your hands."
            yd "well... is it right?"
            a "hmm... doesn't seem to be anything special."
            yd "fuck."
            jump riddle_shack_menu
        "look at mirror":

            "you climb over a bunch of shit and take the mirror."
            "azula grabs it from your hands."
            yd "well... is it right?"
            play sound "audio/win2.mp3"
            show emberisland_mirror with dissolve
            a "this is interesting..."
            y "what?"
            a "azulon's symbol."
            y "sweet! and right next to it, it says... \"twin\"."
            yd "huh. wonder what that's for?"
            y "oh, and there's a little tag with another riddle on it!"
            $ friddle2 = True
            a "well, i'll leave you to it then."
            a "i'll see you back at the party house."
            a "don't take too long."
            hide azula_idle_ff_beach
            hide emberisland_mirror
            with dissolve
            jump party_riddles
        "look at winebottle":

            "you climb over a bunch of shit and take the winebottle."
            "azula grabs it from your hands."
            yd "well... is it right?"
            a "hmm... doesn't seem to be anything special."
            yd "fuck."
            jump riddle_shack_menu
        "look at hat":

            "you climb over a bunch of shit and take the hat."
            "azula grabs it from your hands."
            yd "well... is it right?"
            a "hmm... doesn't seem to be anything special."
            yd "fuck."
            jump riddle_shack_menu

label riddle_shop:
    scene bg_a_armory
    show blue_20perc_transparent
    show mai_idle_ff_beach
    with dissolve

    if friddle1:
        if friddle2:
            m "what is it, zuko?"
            y "found another clue."
            m "oh?"
            y "yeah, says it was sold to this shop, so the thing's here."
            m "well, there's a bunch of crap here."
            m "it could take all night."
            m "or forever."
            m "look around."
            jump riddle_shop_menu
        else:
            y "any luck?"
            m "why are you here?"
            yd "i'm looking, too."
            m "any clues?"
            y "uh... it says \"given to li and lo\"."
            m "...does this look like li and lo's shack?"
            m "leave. i'm looking here for the other items."
            yd "but you don't even know what you're looking for."
            m "go!"
            jump party_riddles
    else:



        y "any luck?"
        m "why are you here?"
        yd "i'm looking, too."
        m "any clues?"
        y "uh... it says \"fell out of boat while visiting li and lo\"."
        m "...does this look like it's outside li and lo's?"
        m "leave. i'm looking here for the other items."
        yd "but you don't even know what you're looking for."
        m "go!"
        jump party_riddles

label riddle_shop_menu:
    menu:
        "read riddle 3":
            y "\"i have rivers without water, forests without trees, and cities without people.\""
            jump riddle_shop_menu
        "look at portrait":

            "you stumble over some old weapons and take the painting."
            "mai grabs it from your hands."
            yd "well... is it right?"
            m "hmm... doesn't seem to be anything special."
            yd "fuck."
            jump riddle_shop_menu
        "look at quiver of arrows":

            "you stumble over some old weapons and take the quiver of arrows."
            "mai grabs it from your hands."
            yd "well... is it right?"
            m "hmm... doesn't seem to be anything special."
            yd "fuck."
            jump riddle_shop_menu
        "look at winebottle":

            "you stumble over some old weapons and take the winebottle."
            "mai grabs it from your hands."
            yd "well... is it right?"
            m "hmm... doesn't seem to be anything special."
            yd "fuck."
            jump riddle_shop_menu
        "look at map":

            "you stumble over some old weapons and take the map."
            "mai grabs it from your hands."
            yd "well... is it right?"
            play sound "audio/win2.mp3"
            show emberisland_map with dissolve
            m "this is interesting..."
            y "what?"
            m "a symbol..."
            y "azulon's! and right next to it, it says... \"where\"."
            yd "weird."
            y "oh, and there's a little tag with another riddle on it!"
            $ friddle3 = True
            m "well, i'll leave you to it."
            m "i'll see you back at the party house, if we have to do that."
            hide mai_idle_ff_beach
            hide emberisland_map
            with dissolve
            jump party_riddles

label riddle_house:
    scene black
    scene bg_a_island_partyhouse
    with dissolve

    if friddle3:
        a_beach "did you find them all?"
        y "yeah, except for one. it says it's here."
        a_beach "excellent, we will let them know."
        play sound "audio/knocking.mp3"
        "azula knocks on the door, and chan answers."
        chan "oh, hey guys. welcome back!"
        chan "come on in."
        a_beach "we completed your hunt except for-"
        chan "what?"
        chan "ohhh... right. yeah, you guys were just here too early, thought we'd have some fun with you."
        chan "you guys are cool though, come on in."
        yd "then why did you have all these riddles ready?"
        chan "came with the house, man."
        chan "some old rich family lived here. heard it was the firelord's, but i don't believe it."
        chan "anyway, that riddle paper thing was here, supposed to open a treasure or something when you get all the things."
        chan "dunno where the treasure is though. probably just nonsense, man."
        chan "come on."
        "you enter the party."
        jump actual_party
    else:

        y "i don't even know why i'm here."
        y "my clue says \"fell out of boat while visiting li and lo\"."
        y "this is definitely not outside li and lo's."
        jump party_riddles

label actual_party:
    show mai_idle_fl_beach with dissolve
    y "so... you're looking at that ruon-jian guy."
    yd "you like him, don't you?"
    show mai_idle_fl_angry with dissolve
    m "ugh, i have no opinon of him."
    y "but you're gonna tease him, right?"
    m "ugh."
    hide mai_idle_fl_beach
    hide mai_idle_fl_angry
    with dissolve
    show azula_idle_fl_beach
    with dissolve
    y "i have no idea what i'm supposed to do here..."
    yd "...and i lost mai. shoot."
    a "......."
    a "...so?"
    show tylee_idle_ff_beach:
        xpos -250
    with dissolve
    t "i'm glad you guys are here!"
    t "those boys won't leave me alone!"
    t "i guess they all just like me too much."
    a " come on, ty lee. you can't be {i}this{/i} ignorant."
    t "what are you talking about?"
    show a_idle_fl_face_blink with dissolve
    a "those boys only like you because you make it so easy for them."
    hide a_idle_fl_face_blink with dissolve
    a "you're not a challenge... you're a tease."
    y "you wanna know who's a tease...?"
    yd "speaking of, where did mai go...?"
    a "i don't know."
    a "and ty lee... it's not as though they actually care who you are."
    show ty_idle_ff_annoyed:
        xpos -250
    show ty_idle_ff_blink:
        xpos -250
    with dissolve
    t "....."
    t "*sob!*"
    show a_idle_fl_face_unsure with dissolve
    a "okay, okay, calm down."
    hide ty_idle_ff_annoyed
    hide ty_idle_ff_blink
    with dissolve
    a "i didn't mean what i said."
    a "look, maybe i just said it because i'm a little... {size=-4}jealous."
    show ty_idle_ff_surprised:
        xpos -250
    with dissolve
    t "what?!"
    t "you're jealous of me?"
    t "but you're the most beautiful, smartest, perfect girl in the world."
    a "well, you're right about all-"
    yd "yeah, i'm bored."
    y "i'm gonna look for mai. and drink."
    jump party_party

label party_party:
    scene black
    scene bg_a_island_partyhouse
    with dissolve
    "either go find mai or do some side stuff first!"
    menu:
        "get crunk!" if not drunk_knives:
            yd "aw, what the hell."
            y "let's drink!"
            "you down several shots in a row, and start gathering a crowd."
            $ double_vision_on("bg_a_island_partyhouse")
            yd "gettin'... gettin' it dizzy good on what?"
            chan "this guy's crazy!"
            chan "hey, it's the avatar!"
            yd "s'wha...?"
            $ double_vision_off()
            scene bg_a_island_avatarposter
            $ double_vision_on("bg_a_island_avatarposter")
            rj "booooo!!!!"
            ya "where's it he? i'm... i'll... poop!"
            chan "here... take it!"
            yd "take.. whosit?"
            $ change_cursor("mustache")
            yd "what... what do i do with it?"
            chan "you gotta pin it on him!"
            chan "ready? go!"
            $ double_vision_off()
            call screen pin_mustache

        "solve final riddle" if not friddle4:
            jump final_riddle_party

            label final_riddle_party:
                y "\"Young I am tall; old I am short. I love to glow. Breath is my foe.\""
                y "it's supposed to be in here somewhere."
                y "there's so much stuff, though..."
                menu:

                    "ty lee" if not tylee_riddle:
                        "you sneak up behind ty lee as she's talking with azula."
                        t "okay, look, if you want a boy to like you..."
                        t "just look at him and smile a lot and laugh at everything he says. even if it's not funny-"
                        "you grab ty lee."
                        show tylee_idle_ff_beach
                        show ty_idle_ff_surprised
                        with dissolve
                        t "oh!"
                        hide ty_idle_ff_surprised with dissolve
                        t "hello!"
                        t "what... um..."
                        y "i was trying to figure out the final riddle."
                        y "i thought you might be it."
                        t "i don't... um... think so."
                        show blackveil
                        hide tylee_idle_ff_beach
                        show tylee_idle_ff_beach
                        with dissolve
                        "you suddenly feel the eyes of 20 guys on you."
                        "the room gets darker."
                        "violence is near."
                        "you let ty lee go."
                        hide blackveil with dissolve
                        "the room returns to normal."
                        t "heehee."
                        yc "you... have some fans."
                        t "yup!"
                        $ tylee_riddle = True
                        y "i'm going to keep looking."
                        t "okay!"
                        hide tylee_idle_ff_beach with dissolve
                        jump final_riddle_party

                    "sword" if not una_party:
                        "you reach for an antique sword and bump into someone."
                        show umg1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
                        with dissolve
                        st "hey!"
                        y "sorry about that."
                        show um1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
                        hide umg1
                        with dissolve
                        st "no worries."
                        yd "hey... you look familiar."
                        st "well, i've lived here most of my life."
                        yd "...what's with all the blue?"
                        st "what? i'm not wearing blue."
                        yd "of... of course you are. what's with the skins and stuff?"
                        st "i'm not wearing any..."
                        show umg1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
                        hide um1
                        with dissolve
                        st "are you okay?"
                        yd "it just seems very water tribe."
                        st ".....i'm wearing a red dress. my father is an admiral."
                        st "i don't know anything {i}about{/i} the water nation."
                        yd "tribe. water tribe."
                        st "i don't care!"
                        st "you're starting to annoy me."
                        hide umg1 with dissolve
                        yd "what was that about?"
                        yd "she seemed familiar... am i going crazy?"
                        "the sword is nothing special."
                        $ una_party = True
                        jump final_riddle_party

                    "candle (locked)" if not tylee_riddle or not una_party:
                        "test"

                    "candle" if tylee_riddle and una_party:
                        "you pick up a gold candle."
                        play sound "audio/win2.mp3"
                        show emberisland_candle with dissolve
                        yd "azulon's symbol. cool."
                        y "and it says... \"flames\"."
                        yd "i wonder if there really is a treasure."
                        y "i'll look into it after this party."
                        $ friddle4 = True
                        jump party_party
        "look for mai (continue quest)":

            y "i wonder where she went-"
            a "{size=+10}hahahahahahaha!"
            "the whole room gets silent for a moment and looks at azula."
            "it picks back up again."
            y "what is ty lee teaching her?"
            menu:
                "look by the food":
                    y "not here..."
                    menu:
                        "look in the bedroom":
                            jump party_bj
                "look in the bedroom":

                    jump party_bj






image devil_aang = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_island_avatarposter.jpg",
    (355, 60), "emberisland/devilmarks.png",
    )

image devil_aang1 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_island_avatarposter.jpg",
    (355, 60), "emberisland/devilmarks.png",
    (355, 60), "emberisland/knife_half.png",
    )

image devil_aang2 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_island_avatarposter.jpg",
    (355, 60), "emberisland/devilmarks.png",
    (355, 60), "emberisland/knife_half.png",
    (240, 200), "emberisland/knife_half.png",
    )

image devil_aang3 = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_island_avatarposter.jpg",
    (355, 60), "emberisland/devilmarks.png",
    (355, 60), "emberisland/knife_half.png",
    (240, 200), "emberisland/knife_half.png",
    (420, 280), "emberisland/knife_half.png",
    )

label mustache_pin:
    $ change_cursor()
    show devil_aang
    with sshake
    chan "hahaha! nice!"
    rj "wooo!"
    rj "knives!"
    yd "wha...?"
    chan "here! go for it, man!"
    $ change_cursor("knife")
    call screen pin_knife

label knife_pin:
    $ change_cursor()
    show devil_aang1
    with sshake
    chan "nicely done!"
    rj "another!"
    $ change_cursor("knife")
    call screen pin_knife1

label knife_pin1:
    $ change_cursor()
    show devil_aang2
    with sshake
    chan "ouch!"
    rj "another!"
    chan "alright, last one!"
    $ change_cursor("knife")
    chan "stab that little fuck!"
    call screen pin_knife2

label knife_pin2:
    $ change_cursor()
    show devil_aang3
    with sshake
    chan "fuck yeah!"
    chan "okay, that's enough, man."
    chan "go walk it off..."
    "you wander for a little bit until you start to sober up."
    yc "whoo. okay. alright."
    $ drunk_knives = True
    jump party_party


label party_bj:
    scene bg_a_island_partyroom
    with dissolve
    ya "ah, shit. not here either."
    yd "i'll just-"
    show azula_idle_ff_beach
    with dissolve
    a "oh, zuzu."
    a "i couldn't help but notice you were having some trouble with mai."
    a "poor brother."
    y "what are you even doing here?"
    a "i'm taking a tour of the house."
    yd "by yourself?"
    a "of course, it's the best way to discover secrets."
    a "so."
    a "are you enjoying yourself here, zuko?"
    yc "i don't even know."
    y "i mean, it's a great place. if you like sand."
    show a_idle_ff_face_smile with dissolve
    a "...ha...hahahahahahahahahahahahahahahahaha."
    yd "(what? just go with it.)"
    y "yeah, it's like \"welcome to sandy land!\""
    show a_idle_ff_face_blink with dissolve
    a "hahahahahahahahahahahahahahahahahahahahahahahahahahahaha!!!"
    yd "...what is wrong with you?"
    hide a_idle_ff_face_smile
    hide a_idle_ff_face_blink
    with dissolve
    a "your arms look... so strong."
    yd "...i mean... i guess?"
    show a_idle_ff_face_unsure with dissolve
    a "....have i done something to you, zuko?"
    y "what do you mean?"
    a "i just see no reason for you to be so mean to me."
    yc "oh, i'm..."
    a "i try to help you with mai, and you get mad at me."
    a "i try to help you with your memories.... by myself.... and you get mad at me."
    a "i think i deserve an apology."
    menu:
        "apologize":
            yc "I'm sorry, azula."
            hide a_idle_ff_face_unsure with dissolve
            a "i knew you'd cower."
            a "but it's good that you not forget that you are indebted to me brother."
            a "in fact, i believe you still haven't completed your training with me, have you?"
            y "oh yeah, you lied to me and made me pick up your luggage."
            a "that was a necessary evil to get you to come with us."
        "i never apologize":


            y "i never apologize."
            hide a_idle_ff_face_unsure with dissolve
            a "interesting. i didn't expect you to be so... strong."
            a "but it's good that you not forget that you are indebted to me brother."
            a "in fact, i believe you still haven't completed your training with me, have you?"
            y "oh yeah, you lied to me and made me pick up your luggage."
            a "that was a necessary evil to get you to come with us."

    y "can you answer me something honestly?"
    a "maybe."
    y "why have you been... helping me... the way you have?"
    show a_idle_ff_face_blink with dissolve
    a "i'm very results oriented, zuko."
    a "failure is unacceptable, and i've known you for a long time."
    a "i know how to make you work best."
    hide a_idle_ff_face_blink with dissolve
    a "i'm rewarding you simply with the goal of encouraging you to fight well and recover your memories."
    a "how else can i expect you to fulfill your duties as prince?"
    y "okay... but what was all that stuff before about \"depending on me\"?"
    y "and that weird conversation we had on the beach, before..."
    show a_idle_ff_face_blink with dissolve
    a "before i rubbed you off and you came all over my ass?"
    y "....you said it, not me."
    hide a_idle_ff_face_blink
    show a_idle_ff_face_unsure
    with dissolve
    a "i was trying to connect, zuko."
    a "i'm just starting to see the value of us... getting along better."
    hide a_idle_ff_face_unsure with dissolve
    a "you are single-handedly halting the earth kingdom, and i am supporting you in recovering your memory..."
    a "...and in other ways."
    a "i think you're going to find you depend on {i}me{/i}, brother. not the other way around."
    yd "......"
    y "maybe."
    y "hey... have you seen mai?"
    show a_idle_ff_face_anger with dissolve
    a "\"mai\" this and \"mai\" that."
    a "am i not having a perfectly nice conversation with you right now?"
    a "what do you want with her anyway? she's boring."
    hide a_idle_ff_face_anger with dissolve
    yd "....."
    a "poor zuko."
    a "poor, poor, zuko."
    yd "what?"
    a "can't even get his rocks off."
    y "yeah, she's-"
    yd "wait, how do you even know about that?"
    a "i wonder... who... could {i}help{/i} him with that?"
    a "hmmmm....."
    a "what do you say, brother?"
    a "i'm in a fun mood."
    a "and you seem {i}so{/i} lonely."
    yd "i mean, there's a party going on right there..."
    yd "hell, the door is open..."
    a "well, i was thinking-"
    scene bg_k_home_01
    show kwhbe at Position (xpos = 0.9, xanchor=0.5, ypos=0.6, yanchor=0.5)
    with flash
    k "hey, aang!"
    y "oh hi, kat-"
    scene black
    scene bg_a_island_partyroom
    show azula_idle_ff_beach
    with flash
    a "...who?"
    y "what?"
    a "you said something about a cat."
    y "i could have sworn..."
    y "...katara...?"
    a "..."
    a "well i don't know, now do i?"
    a "so, what do you think?"
    y "of what?"
    a "of my... proposal."
    y "i didn't hear it."
    a "really? what happened?"
    y "i... had a flashback of some kind, i think."
    a "interesting. i made a suggestion, and you regained some memory."
    a "i think we should explore that don't you?"
    yd "i... suppose."
    show a_idle_ff_face_unsure with dissolve
    a "i'm not good at... asking."
    a "so i'm going to give you an order."
    a "one i believe is necessary for both of us."
    a "do you understand?"
    hide a_idle_ff_face_unsure with dissolve
    yd "uh..."
    show a_idle_ff_face_blink with dissolve
    a "i'm going to put your cock in my mouth."
    yd "........"
    yd "here?!"
    yd "i'm wandering around looking for my girlfriend!"
    a "yes, here."
    menu:
        "that's... kind of crazy":
            y "seriously?"
            y "i mean, we've been fooling around..."
            y "but that seems a little too far, even for us..."
        "awesome!":

            y "sweet!"
            y "i mean, that's a... big step with whatever we're doing."

    a "well, mai doesn't seem interested in taking care of you."
    yd "that can't be the only reason..."
    a "..."


    if mai_flower_got:
        show a_idle_ff_face_anger with dissolve
        a "i saw you! i saw you getting a blowjob from mai!"
        y "oh... um..."
        hide a_idle_ff_face_anger with dissolve
        a "how about a little friendly competition?"
        hide a_idle_ff_face_blink with dissolve
        a "but first..."
    else:
        a "let's just say... I'm feeling generous tonight."

    stop music
    play music "audio/Unwritten Return.mp3"
    "azula unties her top and shuffles out of her skirt, to reveal no panties beneath."
    hide azula_idle_ff_beach
    show afnbe
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "........"
    show alnb
    hide afnbe
    with dissolve
    a "well?"
    y "that... looks... it's good."
    a "thank you."
    a "now was that so hard?"



    yg "no, but... this is."
    a "sit back..."
    a "we're going to have to be quick."
    show ablj1a_1 with dissolve
    a "now give me your stupid cock..."
    show ablj2a_1 with dissolve
    y "this is insane... we're in the middle of a fucking party!"
    show ablj4a_1 with dissolve
    a "..."
    show ablj_tuga_1 with dissolve
    y "ngh..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "that's it, brother..."
    a "just enjoy."
    a "..."
    a "okay."
    show ablj7a_1 with dissolve
    a "..."
    show ablj8a_1 with dissolve
    "azula wraps her lips fully around your member."
    y "fuck."
    show ablj9a_1 with dissolve
    "she drops down further, taking it as deeply as she can."
    a "*mghm* *ngh*"
    "she holds it down before coming up sputtering."
    scene black
    show ablj10a_1
    with dissolve
    a "*cough* *cough*"
    show ablj6a_1 with dissolve
    a "mmmm.... were you inside someone today, brother?"

    if ember_deed:
        y "um... yeah."
        y "...mai's ass."
        show ablj6a_2 with dissolve
        a "well... i'm just going to have to make sure it's only my juices on you."
    else:
        y "Nope, you're the first."

    show ablj7a_1 with dissolve
    a "*sluuurp*"
    y "ngh..."
    show ablj8a_1 with dissolve
    show abj_1a_1
    a "*mmg* *hhngh*"
    y "oh fuck!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "*ngh* *mmmgh*"
    "you hear footsteps walk by and pause just outside the door."
    ya "(fuck! fuck! fuck! i can't be caught with my sister!)"
    a "*slurp* *gulp*"
    "azula either doesn't hear or doesn't care, and shows no sigh of slowing down."
    a "*mmggh*"

    show ablj12a_1 with dissolve
    a "mmmm....."
    show ablj13a_1 with vshake
    a "{size=+5}*hhhgghgh!!!!*"
    y "{size=+3}there we go!"
    a "!!!!!"
    a "*ggaghag*"
    "the footsteps continue on down the hall."
    y "good little sister."
    a "*mmmmmmmm*"
    y "your big brother's cock is in your throat."
    a "*mmmmmmm*"
    y "you really like it, don't you, azula?"
    a "*umph!* *ngh!* *hmmph!*"
    "azula begins moaning into your shaft..."
    show abj_2a_1
    with dissolve
    a "*nmgh!*"
    yc "holy shit!"
    y "this is unreal!"
    y "i can't believe you're blowing me here... you really are a whore!"
    a "*mmnn!*"
    a "*mmmnnn!!!*"
    y "...what?"
    a "{size=+5} *aaaaahgghghhnn!!!!!*"

    scene black
    show ablj33a_1
    with dissolve
    a "*gaggh* *hack* *cough*"
    show ablj34a_1 with dissolve
    a "i am not a whore."
    a "this is just for you."
    a "and you need to be quiet."
    yc "...right."
    a "so... did you ask mai how my ass tasted when you fucked her today?"
    yd "......."

    if ember_deed == False:
        yd "I already told you, that didn't happen!"

    scene black
    show ablj13a_1
    with sshake
    "you grab her bangs and pull her all the way down onto your cock again."
    a "*nnghg!!*"
    show abj_2a_1 with dissolve
    a "*umph!* *ngh!*"
    a "*ggagghh!* *kaghk!*"
    yc "oh... oh fuck..."
    show abj_3a_1 with Dissolve(0.2)
    y "i'm gonna...."
    hide abj_2a_1
    a "!!!"
    a "*nghh!* *nggh!* *aahngh!*"
    ya "oh fuck!"
    a "*??!?!!?*"
    menu:
        "cum in her throat":
            scene black
            show ablj13a_1
            with sshake
            a "!!!!!!"
            hide abj_3a
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            with flash
            a "!!!!!!"
            yc "you have to swallow! we can't make a mess!"
            play sound "audio/splurt2.ogg"
            show ablj14a_1
            with flash
            yc "you have to swallow!"
            a "*mmgnh!*"
            play sound "audio/splurt3.ogg"
            show ablj15a_1
            with flash
            ya "swallow, swallow!"
            play sound "audio/splurt1.ogg"
            show ablj16a_1
            with flash
            a "*hnghh!*"
            play sound "audio/splurt1.ogg"
            show ablj17a_1
            with flash
            a "*mmgh!*"
            y "ahh..."
            a "..."
            scene black
            show ablj35a_1
            with dissolve
            a "..."
            show ablj37a_1 with dissolve
            a "that was fun."
            a "now tell me..."
            show ablj38a_1 with dissolve
            a "was it... better than mai's blowjob?"
            if mai_flower_got:
                menu:
                    "yes":
                        y "definitely."
                        y "mindblowing."
                        a "well."
                        a "let's get back out there."
                        a "we're guests, after all."
                    "no":

                        y "close, but no."
                        y "mai's was better."
                        y "but i'm sure you'll get another chance."
                        a "......."
                        a "well."
                        a "let's get back out there."
                        a "we're guests, after all."
            else:
                y "I wouldn't know. She hasn't given me one yet."
                a "She hasn't even given you a blowjob yet?! Poor zuzu..."

            jump after_party_blowjob
        "cum on her face":

            show ablj21a_1 with sshake
            "azula pulls her head off your cock."
            hide abj_3a
            ya "what?!"
            show ablj22a_1 with dissolve
            a "do it!"
            ya "ngh!"
            show ablj23a_1
            play sound "audio/splurt3.ogg"
            with flash
            a "yes!!! ah!!!"
            a "oh...."
            play sound "audio/splurt2.ogg"
            with flash
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            show ablj24a_1
            with flash
            a "on my face, zuko! cum on your little sister's face!"
            play sound "audio/splurt1.ogg"
            show ablj25a_1
            with flash
            y "ahh..."
            a "..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show ablj36a_1 with dissolve
            a "that was fun."
            a "now tell me..."
            show ablj25a_1 with dissolve
            a "was it... better than mai's blowjob?"
            a "that was fun."
            show ablj25a_1 with dissolve
            a "now tell me..."
            a "was it... better than mai's blowjob?"
            if mai_flower_got:
                menu:
                    "yes":
                        y "definitely."
                        y "mindblowing."
                        a "well."
                        a "let's get back out there."
                        a "we're guests, after all."
                    "no":

                        y "close, but no."
                        y "mai's was better."
                        y "but i'm sure you'll get another chance."
                        a "......."
                        a "well."
                        a "let's get back out there."
                        a "we're guests, after all."
            else:
                y "I wouldn't know. She hasn't given me one yet."
                a "She hasn't even given you a blowjob yet?! Poor zuzu..."

            jump after_party_blowjob

label after_party_blowjob:
    scene black
    scene bg_a_island_partyhouse
    show azula_idle_fl_beach
    show a_idle_fl_face_sperm
    with dissolve
    a "well, it appears we didn't miss much."
    a "tell me..."
    hide a_idle_fl_face_sperm
    hide azula_idle_fl_beach
    show azula_idle_ff_beach
    show a_idle_ff_face_sperm
    with dissolve
    a "is there anything on my face?"
    menu:
        "yeah":
            yg "yeah, jizz."
            a "thank you."
            a "i'll clean it off."
            $ party_face_jizz = True
        "nope":

            yg "nope, not a thing."
            yg "get back out there, girl."
            a "great."

    a "why don't you go find mai?"
    a "and this will... be our little secret."
    a "oh, and i wonder what's making mai so frigid?"
    a "i certainly hope it's not someone close to the two of you."
    ya "oh, you bitch."
    a "that's me. but keep in mind... i'll suck your cock anytime you like, big brother."

    hide azula_idle_ff_beach
    hide a_idle_ff_face_sperm
    with dissolve

    "you wander the party, and eventually find mai in a corner talking to a guy."
    show mai_fl_flip:
        xpos 100
    with dissolve

    if mai_flower_got or not_interested_mai == False:
        ya "hey! stop talking to my girlfriend!"
    else:
        ya "Hey! Stop talking to her!"

    m "what?"
    rj "relax. it's just a party."
    show mai_fl_flip_angry:
        xpos 100
    with dissolve
    m "zuko! what is wrong with you?"
    ya "what's wrong with me?!"
    show mai_fl_flip_blush:
        xpos 100
    with dissolve
    m "your temper's out of control. you're so impatient and hotheaded and... horny!"
    ya "well at least i feel something, you big blob!"
    ya "you can't just shut me off like that!"

    if not_interested_mai and mai_flower_got == False:
        m "Maybe if you had shown a little more interest in me before.."
        if ember_deed:
            ya " I got you the deed to that shop didn't I?!"

    m "you know what, zuko?"
    show tylee_idle_ff_beach:
        xpos -250
    with dissolve
    t "guys!"
    t "everybody... can we just.. calm down?"
    y "yeah, i'll pipe down when she pipes the fuck up."
    m "i don't even know what that means!"
    if party_face_jizz:
        show azula_idle_fl_beach
        with dissolve
    else:
        show azula_idle_fl_beach
        show a_idle_fl_face_sperm
        with dissolve

    a "let's calm down."
    ya "......."
    m "........."
    t "........."
    a "...and destroy this party."
    yd "oh, yeah. i'm in."
    m "me, too."
    a "oh, chaaaaaaaann?"
    chan "yeah?"
    a "we've got some bad news."
    ya "party's over."
    play sound "audio/whoosh.wav"
    show flamespiral with dissolve
    "the party goes down in flames."
    "the four of you leave casually, wearing sunglasses, as explosions go off and people scatter."
    $ ember = 11
    stop music 
    play music "audio/Bassa Island Game Loop.ogg"
    jump embernight

label after_party_sleep:
    scene black
    scene bg_a_island_hutnight
    show tylee_idle_ff_beach:
        xpos -250
    show mai_fl_flip:
        xpos 100
    show mai_fl_flip_angry:
        xpos 100
    show azula_idle_fl_beach
    with Dissolve(1.0)
    yc "man, i'm beat."
    t "same."
    m "....night."
    a "see you all bright and early."
    yd "ugh."
    scene bg_a_farm_singlegirl
    show blackveil
    with dissolve
    yc "finally. bed."
    yc "even with the fleas."
    "you expect to fall asleep easily, but you toss and turn."
    yc "shit."
    y "i might... wander a bit."
    menu:
        "visit ty lee's room":
            show azst azst03
            hide blackveil
            show blackveil
            with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "cute."
            y "let's go visit the other two."
            menu:
                "visit mai & azula":
                    show amsl amsl27 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "aw, yeah."
                    a "mmmhhmph..."
                    show amsl amsl26 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "go back to bed, zuko."
                    y "but-"
                    show amsl amsl27 with dissolve
                    a "bed."
                    y "oh, fine."
                    jump second_night_dream
        "visit mai & azula":

            show amsl amsl27 with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "aw, yeah."
            a "mmmhhmph..."
            show amsl amsl26 with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            a "go back to bed, zuko."
            y "but-"
            show amsl amsl27 with dissolve
            a "bed."
            y "oh, fine."
            y "(might still visit ty lee...)"
            menu:
                "visit ty lee":
                    show azst azst03
                    hide blackveil
                    show blackveil
                    with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "cute."
                    y "alright, i'll go to bed."
                    jump second_night_dream

label second_night_dream:
    scene black
    scene bg_a_farm_singlegirl
    show blackveil
    with dissolve
    "this time you fall asleep almost before you land on the hay."
    stop music
    play music "audio/Kai_Engel_-_01_-_Take_a_Look_Around_You.mp3"
    scene black with Dissolve(1.0)
    "this time, you fall asleep quickly and deeply. before your head even reaches the bed."
    stop music
    play music "audio/Fire2.mp3"
    show azft_fireshadows with Dissolve(1.0)
    "{b}you return."
    "{b}have you remembered?"
    y "what is going on? who are you?"
    "the voices ignore you and repeat their question."
    "{b}have you remembered?"
    y "i remembered a girl."
    y "but... not much else."
    with sshake
    "{b}learn!"
    hide azft_fireshadows with dissolve
    ya "where are you going?"
    "a soft, familiar voice whispers in your ear..."
    s "you must piece through your scattered memories, destroy those that don't belong, and find the true ones that are buried deeply."
    s "drag yourself from moment to moment to get there."
    s "here we go."
    $ glow = 1
    $ false_memory2 = False
    scene green2 with dissolve
    jump second_map

label after_second_dream:
    show kb3 with flash
    k "remember me?"
    hide k_bj5
    show 1kmv2 with flash
    ync "i remember pieces..."
    k "we fought together."
    hide kb3
    ync "we... we did?"
    k "we defeated--"
    scene white with dissolve
    show text "Ember Island\n\nthird day"
    $ renpy.pause (1.5, hard=True)
    scene white with dissolve
    $ ember_day = 3
    play music "audio/Bassa Island Game Loop.ogg"
    scene bg_a_farm_singlegirl with Dissolve(1.0)
    yna "okay, that's getting old."
    ync "i'm waking up more tired than when i fell asleep."
    "your head is spinning with more bits of memories."
    scene bg_a_island_hutday with dissolve
    yd "am i the first person awake?"
    show azula_idle_ff_beach with dissolve
    a "please. you?"
    a "go wake the others."
    yd "..."
    a "...please."
    menu:
        "wake ty lee":
            show azst azst03 with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "oh, that's the good shit."
            "{i}zzzt! zzzt! zzzt!"
            "the toy continues to vibrate and move in her pussy, clearly keeping her asleep."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "fun."
            show azst_eyesopen with dissolve
            t "oh! hello, prince."
            y "good morning."
            y "time to get up."
            t "okay!"
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "......"
            y "alright, i'm going."
            scene black
            scene bg_a_island_hutday
            show tylee_idle_ff_beach:
                xpos -250
            show azula_idle_fl_beach
            with dissolve
            menu:
                "wake mai":
                    show amsl amsl28
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "mai."
                    y "....mai."
                    yd "mai, wake up."
                    yd "...."
                    ya "mai!! get the fuck up!"
                    ya "aaaaahhhhhhhhh!"
                    yd "....damn."
                    y "she really is a heavy sleeper."
                    yd "uh..."
                    scene black
                    scene bg_a_island_hutday
                    show tylee_idle_ff_beach:
                        xpos -250
                    show azula_idle_fl_beach
                    with dissolve
                    y "yeah, not possible."
                    yd "she might be dead."
                    yd "she's not waking up for-"
                    hide tylee_idle_ff_beach
                    hide azula_idle_fl_beach
                    with moveoutright
                    show azms azms01_1
                    show azms_yawn
                    with dissolve
                    "mai wanders out half-asleep."
                    hide azms_yawn with dissolve
                    m "what's going..."
                    m "hold on..."
                    show azms azms04_1 with dissolve
                    m "*yaaawnn*"
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "...god damn it."
                    y "you tease."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    show azms azms01_1 with dissolve
                    m "zuko?"
                    m "what's going on?"
                    y "we're just, uh... getting ready for the day."
                    m "alright, let me get changed..."
                    scene black
                    scene bg_a_island_hutday
                    with dissolve
                    show tylee_idle_ff_beach:
                        xpos -250
                    show azula_idle_fl_beach
                    with moveinright
                    jump ember_third_day_beach
        "wake mai":

            show amsl amsl28
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "mai."
            y "....mai."
            yd "mai, wake up."
            yd "...."
            ya "mai!! get the fuck up!"
            ya "aaaaahhhhhhhhh!"
            yd "....damn."
            y "she really is a heavy sleeper."
            yd "uh..."
            scene black
            scene bg_a_island_hutday
            show azula_idle_fl_beach
            with dissolve
            y "yeah, not possible."
            yd "she might be dead."
            yd "she's not waking up for-"
            hide azula_idle_fl_beach
            with moveoutright
            show azms azms01_1
            show azms_yawn
            with dissolve
            "mai wanders out half-asleep."
            hide azms_yawn with dissolve
            m "what's going..."
            m "hold on..."
            show azms azms04_1 with dissolve
            m "*yaaawnn*"
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "...god damn it."
            y "you tease."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show azms azms01_1 with dissolve
            m "zuko?"
            m "what's going on?"
            y "we're just, uh... getting ready for the day."
            m "alright, let me get changed..."
            scene black
            scene bg_a_island_hutday
            with dissolve
            show azula_idle_fl_beach
            with moveinright
            y "....."
            a "get ty lee."
            menu:
                "wake ty lee":
                    show azst azst03 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "oh, that's the good shit."
                    "{i}zzzt! zzzt! zzzt!"
                    "the toy continues to vibrate and move in her pussy, clearly keeping her asleep."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "fun."
                    show azst_eyesopen with dissolve
                    t "oh! hello, prince."
                    y "good morning."
                    y "time to get up."
                    t "okay!"
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "......"
                    y "alright, i'm going."
                    scene black
                    scene bg_a_island_hutday
                    with dissolve
                    show tylee_idle_ff_beach:
                        xpos -250
                    show azula_idle_fl_beach
                    with moveinright
                    jump ember_third_day_beach

label ember_third_day_beach:
    a "well, ty lee and i are going to explore the island."
    a "we'll meet on the beach later."
    a "mai can just meet us there."
    a "do whatever you'd like, zuko."
    a "today is just a free day for you."
    a "...as if you ever actually fulfill any responsibilities..."
    scene black
    scene bg_a_island_hutday
    with dissolve
    yd "guess i'll-"
    show azms azms01_1
    with dissolve
    m "where is everyone?"
    y "they went to the..."
    yd "...why aren't you dressed?"
    m "i don't feel like it."
    m "i'm done with the beach."
    m "too much sun."
    yd "......"
    y "well, you do have kind of a sexy pale thing going on."
    show azms_yawn with dissolve
    m "*yaawn...*"
    hide azms_yawn with dissolve
    m "don't you think about anything besides sex?"
    yd "......"
    yd "complete this sentence: \"i like....\""
    m "......."
    y "didn't think so."
    m "......"
    m "get out."

    if mai_flower_got or ember_deed:
        ys "admit it, you miss this dick."
        m "no... i don't."
    else:
        ys "admit it, you want this dick."
        m "no... i don't."

    yg "right, that's why you're here with me, only wearing a shirt."
    yg "teasing me with that luscious-"
    show azms azms03_1 with Dissolve(0.7)
    m ".........."
    m "{size=+5}get out!"
    ys "are you that tempted?"
    m "{size=+5}get out! get out! get out!"
    ys "alright, i'm going, i'm going."
    scene black
    scene bg_island_day
    with dissolve
    ys "today's gonna be a good day."
    jump emberday


label abeachrub3:
    stop music
    play music "audio/Unwritten Return.mp3"
    show azbr azbr02 with dissolve

    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "oh, fuck yes."
    a "now, remember..."
    show azbr azbr06 with Dissolve(0.35)
    a "act natural."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "ready?"
    ys "definitely."
    a "say please."
    menu:
        "please...":
            yc "please..."
            a "you're so weak, zuko."
        "get to it!":

            ya "get to it!"
            a "......"
            a "mmmmm....."

    show azbr azbr100 with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "azula smoothly straddles and cups your cock with her cheeks."
    "she's surprisingly light, and yet presses down firmly, burying your cock deeply in her crevice."
    "her soft cheeks surround and squeeze you as she grinds her ass down onto you, keeping her pressure constant."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "now you should wave to ty lee."
    a "so she doesn't think anything suspicious."
    "you smile and wave at ty lee, who smiles and waves back."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "so, you wanted something to do..."
    a "how's my ass? fun?"
    show azbr azbr101 with Dissolve(0.35)
    a "i know i'm having fun."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "we really should spend more time together."
    show azbr_blink with Dissolve(0.35)
    a "isn't this nice?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "bonding like this?"
    hide azbr_blink
    show azbr azbr100
    with Dissolve(0.35)
    a "I can't imagine what father would say."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "he'd be proud of you, i'm sure."
    show azbr azbr101 with Dissolve(0.35)
    a "he's happy to have you home, you know."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "ty lee suddenly gets out of the water and starts walking towards you."
    yc "oh, shit! we should... we should stop..."
    show azbr_sultry with Dissolve(0.35)
    a "nonsense, zuzu."
    a "i can handle ty lee."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    menu:
        "try to get up":
            yc "i really think we should stop..."
            hide azbr_sultry
            show azbr_angry
            with Dissolve(0.35)
            a "you're going to stay right there, zuko."
            a "you're going to cum."
            a "cum from fucking my ass cheeks."
            hide azbr_angry
            with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show azbr azbr105 with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump abeachrub4
        "maybe... maybe another minute...":


            yc "i... guess... ah... you can... deal with her..."
            hide azbr_sultry with Dissolve(0.35)
            a "you're such a good big brother."
            show azbr azbr105 with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump abeachrub4

label abeachrub4:
    a "you just enjoy yourself, now."

    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show azbr azbr02_1 with dissolve
    t "hey, guys!"


    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "hello, ty lee. are you having fun?"
    t "i really am!"
    t "what are you guys up to?"
    show azbr azbr03_1 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "hngh..."
    a "oh, just catching up."
    t "that's great!"
    show azbr azbr03_2 with dissolve
    t "i hope mai's okay..."
    a "i am sure..."
    show azbr azbr04_2 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "*mmmmm*"
    a "...that she is fine."
    show azbr azbr105_1
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "(shit!)"
    show azbr azbr105_2
    t "are... are you okay?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "why, yes. what makes you ask?"
    t "well, you're... rocking... on zuko..."
    a "i have a bit of a... well, a wedgie."
    show azbr azbr105_3
    a "i don't mean to be crude, but it feels like there's something shoved in my ass cheeks."
    show azbr azbr102_1
    show azbr_sultry
    with Dissolve(0.35)
    a "you don't mind, do you, brother?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink

    yc "uuungh....."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "it looks like he doesn't mind."
    a "if that's the case, sorry about this zuko, i'm gonna wiggle extra hard to try to get it out."
    show azbr azbr104_1
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "ahh... f-fuck..."
    show azbr azbr104_2
    t "what's wrong, zuko?"
    hide azbr_sultry with dissolve
    a "yes, what {i}is{/i} the matter, zuzu?"
    yc "i, uh... i think i'm about to cum..."
    yc "...down with something."
    yd "and i think it's going to be... messy..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show azbr_sultry with dissolve
    a "you're certainly not going to make a mess right now, are you?"
    a "not with me on your lap?"
    a "i hope i'm not the cause."
    a "i promise i'm almost done... I think i'm about to get it out."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "oh, fuck!"
    play sound "audio/splurt3.ogg"
    show azbr azbr07_2
    hide azbr_sultry
    show az_mai_sperm_9:
        xpos -420 ypos 300
    with flash
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t "prince, are you okay!"
    a "oh, {i}no{/i}..."
    ya "y-yes, i..."
    play sound "audio/splurt3.ogg"
    hide az_mai_sperm_9
    show a_pussrub_holdcock_sperm01:
        xpos -266 ypos 138
    show az_mai_sperm_10:
        xpos -420 ypos 300
    with flash
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ya "hgh!"
    t "i'll go get a bucket!"
    hide a_pussrub_holdcock_sperm01
    hide az_mai_sperm_10
    show azbr azbr07
    show a_pussrub_holdcock_sperm01:
        xpos -266 ypos 138
    show az_mai_sperm_10:
        xpos -420 ypos 300
    with dissolve
    a "what are you doing, brother?"
    play sound "audio/splurt3.ogg"
    hide azbr_sultry
    hide az_mai_sperm_10
    show az_mai_sperm_11:
        xpos -420 ypos 300
    with flash
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yc "ghgh...."
    a "you shouldn't be cumming on me in front of ty lee."
    show azbr azbr04 with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "mmmm...."
    a "warm..."
    show azbr azbr07
    with Dissolve(0.35)
    a "but it's nice, isn't it brother?"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "you can rely on me... to take care of you."
    show azbr_sultry with Dissolve(0.35)
    a "but now... i think you might need a dip in the ocean."
    yd "don't you?"
    a "i'll just wipe it off in my swimsuit."
    hide azbr_sultry with dissolve
    a "i'll rinse it out later."
    a "i don't think i'll need it for a while."
    a "we {i}should{/i} get up before ty lee comes back, though."
    yd "good plan."
    y "......."
    yd "......."
    yd "you're not moving..."
    show azbr_sultry with dissolve
    a "well, it's nice."
    hide azbr_sultry with dissolve
    a "oh, all right."
    a "oh! it looks like mai is coming over!"
    a "go rinse off. the girls and i will be over by the chairs."
    a "you should come say hello."
    $ ember = 13
    scene black with dissolve
    "you jump into the ocean and rinse yourself off."
    jump ember_beach_day3

label mai_azula_training_caught:
    scene black
    scene bg_a_island_partyhouse
    show azula_idle_fl_beach
    show mai_fl_flip
    with dissolve
    a "...doing really well, i'm proud of you, mai."
    yd "(i wonder what for?)"
    yd "(this is an odd place for a conversation.)"
    show mai_fl_flip_angry with dissolve
    m "it's... difficult. i want to be with him."
    m "i care about him."
    m "even if he acts like a child."
    show a_idle_fl_face_blink with dissolve
    a "trust me, mai. zuko will love and respect you more if you-"

    hide a_idle_fl_face_blink
    hide azula_idle_fl_beach
    show azula_idle_ff_beach
    with dissolve
    a "zuko."
    a "are you eavesdropping?"
    a "go on, mai. we'll talk later."
    m "......"
    hide mai_fl_flip_angry
    hide mai_fl_flip
    with dissolve

    yd "what was that about?"
    a "mai was... wondering about you."
    yd "how so?"
    a "don't worry about it."
    a "did you want something?"
    y "yeah, you still haven't trained me yet."
    show a_idle_ff_face_blink with dissolve
    a "hmmm...."
    a "i think it's time to try to teach you... lightning."
    ys "fuck yeah!"
    a "......"
    hide a_idle_ff_face_blink with dissolve
    a "lightning is a pure expression of firebending, without aggression."
    a "it is not fueled by emotion or rage... like other firebending."
    a "some people call it the cold-blooded fire."
    a "i like that, personally."
    a "but it's much simpler than that."
    a "you simply separate positive and negative energy, and bring them back together."
    yd "....that doesn't sound simple at all."
    show a_idle_ff_face_blink with dissolve
    a "well, i fully expect you to be incapable of it, zuko."
    yd "and there isn't any training between where we are now and lightning?"
    a "you want to be strong? here you go."
    yd "okay."
    ya "................."
    ya "aahhh!!!"
    play sound "audio/whoosh.wav"
    show flamespiral with dissolve
    hide flamespiral with dissolve
    "you get knocked off your feet by the resulting explosion."
    a "see, i knew you'd fail."
    a "you're too emotional."
    "you brace yourself and try again."
    ya "aahhh!!!"
    play sound "audio/whoosh.wav"
    show flamespiral with dissolve
    hide flamespiral with dissolve
    "once again, you get knocked off your feet by the resulting explosion."
    ya "why does it keep blowing up in my face?"
    a "you're. too. emotional."
    a "it's alright, you won't get it zuko."
    a "give up and let's go back. i actually never intended-"
    scene black with dissolve
    "you breathe deeply."
    "azula speaks, but you manage to tune her out and focus on the air around you."
    "you feel... a pulse. with different wavelengths. you seek them out, and with a large, circular motion of your arms, separate them."
    show azula_idle_ff_beach
    hide a_idle_ff_face_blink
    show a_idle_ff_face_unsure
    with dissolve
    "you keep your eyes closed as you move your arms, exterting your will in keeping these powers separate."
    "as your arm extends, you release both of these energies, and you guide them forward as they crash together."
    play sound "audio/firewall.mp3"
    hide a_idle_ff_face_unsure
    hide azula_idle_ff_beach
    show bg_a_island_partyhouse
    show azula_idle_ff_beach
    show a_idle_ff_face_surprise
    with flash
    with flash
    with flash
    a "you.... how can..."
    show a_idle_ff_face_anger
    hide a_idle_ff_face_surprise
    with dissolve
    a "you're not nearly strong enough for... how did you get so strong?"
    a "you're almost... no..."
    a "....."
    a "that's it! no more training."
    yd "what?"
    a "no more."
    yd "but i still have more to learn."
    hide a_idle_ff_face_anger with dissolve
    a "i'm sorry zuko, but you won't get it from me."
    yd "why not?"
    a "i don't think i have the time any more. besides, you're perfectly capable of handling yourself now."
    a "you don't really need any more training, do you?"
    yd "i guess."
    a "excellent."
    a "come on, let's go back to the beach together."
    $ ember_azula_found = True
    if ember_tylee_found and ember_azula_found:
        $ ember = 12
    hide azula_idle_ff_beach with dissolve
    $ firebending = 8
    jump emberday

label spin_the_bottle:
    scene black
    show azft azft08
    show bottle_1
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t "you guys ready?"
    yd "wait, what exactly are we doing here?"
    m "i don't... really know either."
    a "you just... you just spin it, right?"
    t "usually you kiss or something."
    a "really?"
    a "and people have fun with this?"
    t "lots!"
    m "...fine. zuko, why don't you spin it first."
    jump bottle_spin

label bottle_spin:
    menu:
        "random spin":

            $ randbottle = renpy.random.randint(1, 3)
            if randbottle ==1:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 60
                $ renpy.pause (5.0, hard=True)
                jump mai_bottle_kiss

            if randbottle ==2:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 130
                $ renpy.pause (5.0, hard=True)
                jump ty_bottle_kiss

            if randbottle ==3:
                hide bottle_1

                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 200
                $ renpy.pause (5.0, hard=True)

                jump azula_bottle_kiss
        "mai":

            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 60
            $ renpy.pause (5.0, hard=True)
            jump mai_bottle_kiss
        "ty lee":

            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 130
            $ renpy.pause (5.0, hard=True)
            jump ty_bottle_kiss
        "azula":

            hide bottle_1

            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 200
            $ renpy.pause (5.0, hard=True)
            jump azula_bottle_kiss

label mai_bottle_kiss:
    m "...i guess that's me."

    show azft azft08_1
    show blackveil
    show mai_idle_ff_beach:
        xpos -365
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    m "this doesn't mean i forgive you."
    y "well, this doesn't mean i forgive {i}you."
    m "......"
    m "okay."
    show mai_idle_ff_blink:
        xpos -365
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    play sound "audio/kiss.mp3"
    show mai_idle_ff_blush:
        xpos -365
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with pflash
    m "....."
    m "mmmm....."
    hide mai_idle_ff_blink with dissolve
    m "that was nice."
    m "not that i wanted to do it."
    scene black
    show azft azft08
    show bottle_1
    with dissolve
    t "that was fun."
    m "who's next?"
    jump second_kiss

label ty_bottle_kiss:
    t "oh! i guess that's me."

    show azft azft08_1
    show blackveil
    show tylee_idle_ff_beach:
        xpos -365
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    t "so now we... kiss."
    t "i have to admit i've been like, super curious, zuko."
    t "um... sorry mai."
    m "......"
    t "okay."
    show ty_idle_ff_blink:
        xpos -365
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    play sound "audio/kiss.mp3"
    show ty_idle_ff_blush:
        xpos -365
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with pflash
    t "....."
    t "mmmm....."
    hide ty_idle_ff_blink with dissolve
    t "that was nice."
    t "you're a good kisser, zuko!"
    scene black
    show azft azft08
    show bottle_1
    with dissolve
    t "that was fun."
    m "who's next?"
    jump second_kiss

label azula_bottle_kiss:
    a "me?"
    t "ew!"
    t "you can't do that!"
    m "...that is really gross."
    a "and yet those are the rules."
    a "and where would we be without rules?"
    a "zuko and i must kiss to continue."
    show azft azft08_2
    show blackveil
    show azula_idle_ff_beach:
        xpos -360
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    a "put your lips on mine, brother."
    a "kiss me."
    t "I can't watch!"
    t "um... that's your brother..."
    a "here we go."
    show a_idle_ff_face_blink:
        xpos -360
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    play sound "audio/kiss.mp3"
    show a_idle_ff_face_blush:
        xpos -360
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with pflash
    a "*mmm*"
    m "...what was that?"
    t "i think she enjoyed that!"
    a "of course not, you heathens."
    hide a_idle_ff_face_blink with dissolve
    a "{size=-4}you are always welcome, zuzu..."
    scene black
    show azft azft08
    show bottle_1
    with dissolve
    m "who's next?"
    jump second_kiss

label second_kiss:
    a "i believe it is my turn."
    t "um... i don't think it-"
    a "it is my turn."
    t "...okay!"
    a "here it goes!"
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 60
    $ renpy.pause (5.0, hard=True)
    m "....."
    m "oh."
    m "um. okay..."
    a "very well."
    scene black
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -200
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_unsure:
        xpos -200
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 100
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve

    a "...ready?"
    ys "get to it, ladies!"
    m "you're sick, zuko..."
    a "we can't... we can't kiss."
    t "do it!"
    y "this is all you. ty lee and i are just watching."
    ys "have fun with it."
    m "....."
    scene black
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -250
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_unsure:
        xpos -250
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 150
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve

    a "......."
    m "close your eyes, okay? i don't want to look into..."
    a "agreed."

    scene black
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -290
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_unsure:
        xpos -290
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_blink:
        xpos -290
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 190
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show mai_fl_flip_blink:
        xpos 190
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    m "............"
    a "............"
    t "kiss! kiss! kiss!"
    m "............"
    scene black
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -320
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_unsure:
        xpos -320
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_blink:
        xpos -320
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 210
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show mai_fl_flip_blink:
        xpos 210
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    a "you smell... nice..."
    m "you're... soft."
    t "your boobs are pressing! just kiss already!"
    a "....there's really nothing left but to..."
    m "........"
    scene black
    play sound "audio/kiss.mp3"
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -330
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_unsure:
        xpos -330
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_blink:
        xpos -330
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 220
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show mai_fl_flip_blink:
        xpos 220
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    scene pink
    "azula and mai lock lips briefly, but it melds into gently passionate sucking and teasing."
    t "nice!"
    t "alright, alright, sit down!"
    scene black
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -330
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_unsure:
        xpos -330
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show a_idle_fl_face_blink:
        xpos -330
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 220
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    show mai_fl_flip_blink:
        xpos 220
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    a "*sigh...*"
    m "....that was nice."
    scene black
    show azft azft10
    show blackveil
    show azula_idle_fl_beach:
        xpos -160
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5

    show mai_fl_flip:
        xpos 100
        parallel:
            ease 0 zoom 1.08
        parallel:
            yalign 0.0
            linear 0 yalign 0.5
    with dissolve
    t "alright, you two! sit down!"
    scene black
    show azft azft08
    with dissolve
    jump tylee_bottle_turn

label tylee_bottle_turn:
    t "my turn!"
    t "and we're upping the stakes!"
    m "what do you mean?"
    t "who it lands on... takes off their shirt!"
    m "....."
    yg "i'm in."
    a "...as am i."
    m "alright."
    t "great!"
    t "here we go!"
    a "wait!"
    yc "aw..."
    a "zuko, remember that box i had you get?"
    yd "the one that was heavy as shit?"
    a "yes. go get it."
    yd "...why?"
    a "just do it."
    yd "...alright."
    $ ember = 14
    jump emberday

label truth_or_dare:
    scene black
    show azft azft08
    with dissolve
    yd "here."
    with vshake
    "you drop the box into the sand."
    yd "so what did i just bring?"
    a "open it up."
    "you open the box up... and it's full of bottles of alcohol."
    yd "...damn."
    "mai reaches in without hesitation and grabs a bottle."
    t "woohoo!"
    yd "didn't peg you for a party animal, mai."
    m "who drinks for fun?"
    y "...well, if that's what works for you."
    yd "so what did i miss?"
    m "i had an idea."
    yd "is it better than the shirt idea?"
    m "it's a dare...."
    t "what?"
    m "you sure you want to know?"
    a "go ahead."
    m "zuko spins the bottle... and whoever it lands on..."
    m "has to..."
    m "put the bottle in their ass."
    t "....."
    y "i like how you think."
    a "that seems...."
    t "I'm in!"
    a "very well, i am as well."
    m "do it, zuko."
    menu:
        "random spin":

            $ randbottle = renpy.random.randint(1, 3)
            if randbottle ==1:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 60
                $ renpy.pause (5.0, hard=True)
                jump mai_bottle_butt

            if randbottle ==2:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 130
                $ renpy.pause (5.0, hard=True)
                jump ty_bottle_butt

            if randbottle ==3:
                hide bottle_1

                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 200
                $ renpy.pause (5.0, hard=True)

                jump azula_bottle_butt
        "mai":

            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 60
            $ renpy.pause (5.0, hard=True)
            jump mai_bottle_butt
        "ty lee":

            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 130
            $ renpy.pause (5.0, hard=True)
            jump ty_bottle_butt
        "azula":

            hide bottle_1

            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 200
            $ renpy.pause (5.0, hard=True)
            jump azula_bottle_butt

label azula_bottle_butt:
    $ azula_butt_bottle = True
    a "...me?"
    a "oh... goodness..."

    scene black
    show azbb azbb00
    show azbb_azula_getsit
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_b "....well...."
    show azbb azbb01
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_b "here we go..."
    show azbb azbb02 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_be "ahh...."
    show azbb azbb03 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_ube "ooohhhh...."
    a_ub "this bottle isn't really..."
    show azbb azbb05 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_ae "ahhhh.... made for this....."
    t "your pussy is beautiful, though!"
    show azbb azbb100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_ube "oohhhhh.... my ass....."
    t "hot!"
    t "you go, azula!"
    m "wow... i'm glad i'm not doing that..."
    a_ab "this was..."
    a_ae "ah!"
    a_ab "your idea..."
    m "faster!"
    show azbb azbb100_1
    a_ae "nnnghhh....."
    a_b "oh!"
    m "it got nice?"
    a_b "it really did."
    a_be "mmmm... ah, that's nice..."
    a_be "smooth...."
    show azbb azbb101
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a_ube "ohhh......"
    t "easy, your highness!"
    a_b "this is great!"
    a_b "mmmm...."
    a_be "alright.... i think i'm done...."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    jump shirt_bottle

label mai_bottle_butt:
    $ mai_butt_bottle = True
    m "...me?"
    m "....that's what i get...."
    scene black
    show azbb azbb00
    show azbb_mai_getsit
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "....well...."
    show azbb azbb01
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "here we go..."
    show azbb azbb02 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "ahh...."
    show azbb azbb03 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "ooohhhh...."
    m_l "this bottle isn't really..."
    show azbb azbb05 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "ahhhh.... made for this....."
    t "your pussy is beautiful though!"
    show azbb azbb100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "oohhhhh.... my ass....."
    t "hot!"
    t "you go, mai!"
    a "wow... i am glad i'm not doing that, mai."
    m_l "this was..."
    m_l "ah!"
    m_l "not the best idea..."
    a "faster!"
    show azbb azbb100_1
    m_l "nnnghhh....."
    m_l "oh!"
    a "it got nice?"
    m_l "it really did."
    m_l "mmmm... ah, that's nice..."
    m_l "smooth...."
    show azbb azbb101
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m_l "ohhh......"
    t "easy!"
    m_l "this is great!"
    m_l "mmmm...."
    m_l "alright.... i think i'm done...."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    jump shirt_bottle

label ty_bottle_butt:
    $ tylee_butt_bottle = True
    t "...me?"
    t "oh... boy..."
    scene black
    show azbb azbb00
    show azbb_tylee_getsit
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "....well...."
    show azbb azbb01
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "here we go..."
    show azbb azbb02 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "ahh...."
    show azbb azbb03 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "ooohhhh...."
    t_l "this bottle isn't really..."
    show azbb azbb05 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "ahhhh.... made for this....."
    a "your pussy is beautiful though, ty lee."
    t_l "t-thank you, your highness!"
    show azbb azbb100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "oohhhhh.... my ass....."
    m "hot!"
    yg "you go, ty lee!"
    m "wow... i am glad i'm not doing that."
    t_l "this was..."
    t_l "ah!"
    t_l "your idea..."
    m "faster!"
    show azbb azbb100_1
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "nnnghhh....."
    t_l "oh!"
    m "it got nice?"
    t_l "it really did."
    t_l "mmmm... ah, that's nice..."
    t_l "smooth...."
    show azbb azbb101
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    t_l "ohhh......"
    m "easy, ty lee!"
    t_l "this is great!"
    t_l "mmmm...."
    t_l "alright.... i think i'm done...."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    jump shirt_bottle


label shirt_bottle:
    scene black
    show azft azft08
    show bottle_1:
        xpos 350 ypos 440
    with dissolve
    a "well, that was fun."
    yd "mostly crazy."
    m "i'll say."
    t "certainly... filling."
    y "yeah, i-"
    ya "{size=+6}nature calls."
    scene black with dissolve
    "you return four minutes later."
    y "thank goodness for the ocean."
    show azft azft08_4
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 200
    $ renpy.pause (5.0, hard=True)

    yd "what did i miss?"
    a "we got bored so we went ahead."
    m "I lost my shirt."
    y "nice!"
    yd "we still drinking?"
    t "yes!"
    t "and it's mai's turn to spin!"
    t "do it!"
    m "here i go."
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 300
    $ renpy.pause (5.0, hard=True)
    t "take it off, zuko!"
    ys "alright."
    m "wooo!!"
    a "are you already drunk? that was fast."
    m "what? no. i'm just starting to have fun."
    ys "i'm kind of surprised you even know what \"fun\" means."
    m "oh shut up and take off your shit. shirt. you know what i mean."
    with ushake
    yns "there!"
    t "hot stuff!"
    a "very... nice..."
    m "mmmmmmm...."
    a "alright, zuko. spin it!"
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 140
    $ renpy.pause (5.0, hard=True)
    m "tits out, ty lee!"
    yns "you heard her!"
    t "......"
    show azft azft08_3
    with dissolve
    t "here they are!"
    yns "nice!"
    a "i feel like i'm missing out...."
    ys "i've got you covered..."
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 200
    $ renpy.pause (1.0, hard=True)
    "you gently turn the bottle until it points at azula."

    yns "uh oh......"
    a "....."
    a "well, it really is only {i}fair{/i}."
    t "there you go!"
    show azft azft08_5
    with dissolve
    yns "haha! awesome!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "alright... let's do some \"truth or dare\"."
    a "i'll spin."
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 140
    $ renpy.pause (5.0, hard=True)
    a "ty lee -- truth or dare?"
    t "hmmm... truth!"
    a "alright. have you ever... swallowed cum?"
    t "yeah, but it wasn't on purpose."
    m "what? how's that work?"
    t "a bunch of guys jizzed in my milkshake."
    t "drank all of it without noticing."
    t "they told me about it later... they were so cute!"
    ynd "fair enough."
    a "spin it, ty lee."
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 140
    $ renpy.pause (5.0, hard=True)
    t "um... me again..."
    t "i don't think i can ask myself something... i'm gonna spin it again."
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 200
    $ renpy.pause (5.0, hard=True)
    t "azula... truth or dare?"
    if azula_butt_bottle:
        a "truth!"
        t "did you ever see firelord ozai's... dick?"
        a "ty lee!"
        t "i'm sorry!"
        a "......"
        a "once."
        a "surprisingly small."
        a "not like zuko here."
        m "........"
        jump truthdare

    if not azula_butt_bottle:
        a "dare."
        t "i dare you to put the bottle in your butt!"
        a "........."
        a "oh, fine..."
        scene black
        show azbb azbb00
        show azula_getsit_othersnude
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_b "....well...."
        show azbb azbb01
        with dissolve
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_b "here we go..."
        show azbb azbb02 with dissolve
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_be "ahh...."
        show azbb azbb03 with dissolve
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_ube "ooohhhh...."
        show azbb azbb05 with dissolve
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_ae "my butt... ahhhh.... isn't made for this....."
        show azbb azbb100
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_ube "oohhhhh.... my ass....."
        a_ae "nnnghhh....."
        a_b "oh!"
        m "it got nice?"
        m "faster!"
        show azbb azbb100_1
        a_b "it really did."
        a_be "mmmm... ah, that's nice..."
        a_be "smooth...."
        show azbb azbb101
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a_b "okay, i think... that's enough..."
        scene black
        scene azft azft08_5
        with dissolve
        jump truthdare

label truthdare:
    a "i'll spin it."
    hide bottle_1
    show bottle_1:
        xpos 350 ypos 440
        subpixel True
        rotate 0
        linear 1.0 rotate 360
        rotate 0
        linear 2.0 rotate 360
        rotate 0
        linear 1.0 rotate 60
    $ renpy.pause (5.0, hard=True)
    a "mai! truth or dare?"
    m "...dare."
    a "i dare you... to take off your pants!"
    a "let's see that pretty pussy!"
    m "...."
    ynd "do it, do it, do it, do it, do it-"
    scene black
    show azft azft08_6
    show bottle_1:
        xpos 350 ypos 440
    with dissolve
    t "sweet pussy!"
    m "I'll spin..."
    scene black with dissolve
    "the four of you play truth or dare well into the night."
    show azft azft02 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "can we... get a fire going?"
    yn "i got this."
    play sound "audio/whoosh.wav"
    show azft_fireshadows_nude
    t "wow!"
    t "that was impressive, prince!"
    a "not really..."
    m "well, i'm impressed."
    a "......"
    a "you know what's impressive?"
    a "his cock."
    t "azula!"
    m "......"
    a "it's true..."
    a "mai knows, don't you, mai?"
    m "......"
    a "come on, we're all friends here."
    m "we've... done some things."
    t "oooo, like what?"
    a "zuko?"

    menu:
        "tell them":
            if mai_flower_got and ember_deed:
                yn "well, i've put my cock in two out of three holes."
                m "........."
                t "nice!"
                a "well {i}done{/i}, mai."
                $ mai_aff -=1
            elif mai_flower_got or ember_deed:
                yn "well, i've put my cock in one out of three holes."
                m "........."
                t "one down, two to go!"
                a "well {i}done{/i}, mai."
                $ mai_aff -=1
            else:
                yn "well, actually i still have a lot of holes to fill."
                m "........."
                t "aaawh...."
                a "well {i}done{/i}, mai."
                $ mai_aff -=1
        "let mai tell them":


            if mai_flower_got and ember_deed:
                m "he's.... been in two out of three holes."
                t "nice!"
                a "well {i}done{/i}, mai."
            elif mai_flower_got or ember_deed:
                m "he's.... been in one out of three holes."
                t "one down, two to go!"
                a "well {i}done{/i}, mai."
            else:
                m "he... still has a lot of holes to fill."
                t "aaawh...."
                a " well {i}done{/i}, mai."


    t "alright, prince, your turn..."
    t "truth or dare?"
    menu:
        "truth":
            t "of the three of us..."
            t "with no consequences whatsoever..."
            t "who... would you most want to ejaculate on?"
            menu:
                "mai":

                    ynd "hmmm.... mai, probably."
                    t "then... i dare you to cum on mai."
                    yn "...are you serious?"
                    t "yeah. we agreed to let you do it to whoever you picked."
                    t "do it."
                    t "jack off on her."
                    yn ".....and you're all okay with this?"
                    m "...i agreed."
                    a "as did i."
                    a "i want to see it."
                    m "...go for it."
                    t "and i'm always up for stuff."

                    show blackveil
                    show mai_idle_ff_nude:
                        xpos -365
                        parallel:
                            ease 0 zoom 1.08
                        parallel:
                            yalign 0.0
                            linear 0 yalign 0.5

                    with dissolve

                    show azsl_masturbate_2
                    m "wow... that's nice..."
                    t "come on, zuko. cum on her."
                    a "cover mai."
                    "you find your balls churning after very little time."
                    yna "fuck!"
                    play sound "audio/splurt3.ogg"
                    show mai_idle_ff_surprised:
                        xpos -365
                        parallel:
                            ease 0 zoom 1.08
                        parallel:
                            yalign 0.0
                            linear 0 yalign 0.5
                    show c_fuck_spermoutside_03:
                        xpos -130 ypos -20
                    with flash
                    m "oh!"
                    play sound "audio/splurt3.ogg"
                    show c_fuck_spermoutside_02:
                        xpos -80 ypos 20
                    with flash
                    a "cover her."
                    yna "nghh!"
                    play sound "audio/splurt3.ogg"
                    show c_fuck_spermoutside_01:
                        xpos -100 ypos 80
                    with flash
                    t "she's a whore!"
                    play sound "audio/splurt3.ogg"
                    show boobjob__sperm01:
                        xpos -222 ypos -68
                    hide azsl_masturbate_2
                    with flash

                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    m "well... i..."
                    m "think... i need a dip in the ocean..."
                    m "i, uh, i'll go do that."
                    m "but... good load..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    jump after_fire_mast
                "ty lee":

                    ynd "hmmm.... you, probably."
                    t "then... i dare you to cum on me."
                    yn "...are you serious?"
                    t "yeah. we agreed to let you do it to whoever you picked."
                    t "do it."
                    t "jack off on me."
                    yn ".....and you're all okay with this?"
                    m "...i agreed."
                    a "as did i."
                    a "i want to see it."
                    m "...go for it."
                    t "and i'm always up for stuff."

                    show blackveil
                    show ty_idle_ff_nude:
                        xpos -365
                        parallel:
                            ease 0 zoom 1.08
                        parallel:
                            yalign 0.0
                            linear 0 yalign 0.5

                    with dissolve

                    show azsl_masturbate_2
                    t "wow... that's nice..."
                    m "come on, zuko. cum on her."
                    a "cover ty lee."
                    "you find your balls churning after very little time."
                    yna "fuck!"
                    play sound "audio/splurt3.ogg"
                    show ty_idle_ff_surprised:
                        xpos -365
                        parallel:
                            ease 0 zoom 1.08
                        parallel:
                            yalign 0.0
                            linear 0 yalign 0.5
                    show c_fuck_spermoutside_03:
                        xpos -130 ypos -20
                    with flash
                    t "oh!"
                    play sound "audio/splurt3.ogg"
                    show c_fuck_spermoutside_02:
                        xpos -80 ypos 20
                    with flash
                    m "cover her."
                    yna "nghh!"
                    play sound "audio/splurt3.ogg"
                    show c_fuck_spermoutside_01:
                        xpos -100 ypos 80
                    with flash
                    a "she's a whore!"
                    play sound "audio/splurt3.ogg"
                    show boobjob__sperm01:
                        xpos -222 ypos -68
                    hide azsl_masturbate_2
                    with flash

                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    t "well... i..."
                    t "think... i need a dip in the ocean..."
                    t "i, uh, i'll go do that."
                    t "but... good load, zuko!"
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    jump after_fire_mast
                "azula":

                    ynd "hmmm.... azula, probably."
                    t "then... i dare you to cum on azula."
                    yn "...are you serious?"
                    t "yeah. we agreed to let you do it to whoever you picked."
                    t "do it."
                    t "jack off on her."
                    yn ".....and you're all okay with this?"
                    m "...i agreed."
                    a "as did i."
                    a "i want it."
                    m "...go for it."
                    t "and i'm always up for stuff."

                    show blackveil
                    show a_idle_ff_nude:
                        xpos -365
                        parallel:
                            ease 0 zoom 1.08
                        parallel:
                            yalign 0.0
                            linear 0 yalign 0.5

                    with dissolve

                    show azsl_masturbate_2
                    a "wow... that's nice..."
                    m "come on, zuko. cum on her."
                    t "cover our princess."
                    "you find your balls churning after very little time."
                    yna "fuck!"
                    play sound "audio/splurt3.ogg"
                    show a_idle_ff_face_blink:
                        xpos -365
                        parallel:
                            ease 0 zoom 1.08
                        parallel:
                            yalign 0.0
                            linear 0 yalign 0.5
                    show c_fuck_spermoutside_03:
                        xpos -130 ypos -20
                    with flash
                    a "oh!"
                    play sound "audio/splurt3.ogg"
                    show c_fuck_spermoutside_02:
                        xpos -80 ypos 20
                    with flash
                    m "cover her."
                    yna "nghh!"
                    play sound "audio/splurt3.ogg"
                    show c_fuck_spermoutside_01:
                        xpos -100 ypos 80
                    with flash
                    t "she's a whore!"
                    play sound "audio/splurt3.ogg"
                    show boobjob__sperm01:
                        xpos -222 ypos -68
                    hide azsl_masturbate_2
                    with flash

                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    hide a_idle_ff_face_blink with dissolve
                    a "well... i..."
                    a "think... i need a dip in the ocean..."
                    a "i, uh, i'll go do that."
                    a "but... good load..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    jump after_fire_mast
        "dare":

            t "i dare you... to take out your cock..."
            t "and masturbate."
            yn "...are you serious?"
            t "yeah."
            t "we all agreed we want to see it."
            yn "well, then...."
            show azsl_masturbate_2
            t "wow... that's nice..."
            m "come on, zuko. cum on us."
            a "cover us."
            "you find your balls churning after very little time."
            yna "fuck!"
            show c_fuck_spermoutside_03:
                xpos -440 ypos 70
            with flash
            m "oh!"
            show c_fuck_spermoutside_02:
                xpos -84 ypos -130
            t "ah!"
            yna "nghh!"
            show c_fuck_spermoutside_01:
                xpos 220 ypos -80
            a "we're whores!"
            show boobjob__sperm01:
                xpos -580 ypos -170
            hide azsl_masturbate_2
            with flash
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            t "well... i..."
            t "think... we need a dip in the ocean..."
            t "we, uh, we'll go do that."
            t "but... good load..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump after_fire_mast


label after_fire_mast:
    scene black with dissolve
    "you all decide to call it a night."
    jump embernight

label secret_mai_azula_talk:
    a "....i was saying."
    a "if you want his love, and his respect..."
    a "no matter what, you must refuse to do anything sexual."
    ya "(what? that bitch!)"
    yd "(...why would she be encouraging that?)"
    m "i don't know... we just seem to be fighting more than ever..."
    hide a_idle_fl_face_blink with dissolve
    a "of course you're fighting. that's healthy."
    a "you're establishing yourself as strong and independent."
    a "don't let him walk over you and he'll have no choice but to cave to you."
    hide mai_fl_flip_angry with dissolve
    m "but... i don't want him to \"cave\"... just... love... and treat me well."
    show a_idle_fl_face_blink with dissolve
    a "which he won't do without respect, believe me."
    hide a_idle_fl_face_blink with dissolve
    m "i guess..."
    a "keep it up. don't give in for anything, understand."
    m "but i want-"
    a "you want zuko."
    m "right."
    a "so what are you going to do?"
    m "...be celibate."
    a "very good."
    m "i'm... going to go inside. i really have to think about all this."
    hide mai_fl_flip with dissolve
    $ ember = 15
    menu:
        "reveal yourself":
            ya "azula! what the hell?!"
            show a_idle_fl_face_blink with dissolve
            a "oh, you heard that."
            ya "what are you doing?"
            a "giving mai some friendly advice."
            ya "that's not friendly! that's... unfriendy!"
            hide a_idle_fl_face_blink with dissolve
            a "you have such a way with words, brother."
            yd "why are you telling her to distance herself from me?"

            if not_interested_mai and mai_flower_got == False:
                ya "Are you cockblocking me?"
            else:
                y "i like her."

            show a_idle_fl_face_blink with dissolve
            a "she wants your respect, and that's the best way to get it."
            yd "then why aren't you \"cutting yourself off\" from me?"
            hide a_idle_fl_face_blink with dissolve
            a "because i don't want your respect, brother."
            a "i am more powerful than you."
            show a_idle_fl_face_unsure with dissolve
            a "and... i'm having feelings that i don't understand."
            a "weak ones. and... i am trying to sort it out."
            a "and i don't care what you think. i'm doing what i want."
            hide a_idle_fl_face_unsure with dissolve
            a "now, i suggest you go to bed. we're leaving in the morning."
            a "...and i'm sorry to hear that your girlfriend won't have sex with you."
            show a_idle_fl_face_blink with dissolve
            a "if only you had another option...."
            hide a_idle_fl_face_blink with dissolve
            a "goodnight, brother."
            hide azula_idle_fl_beach with dissolve
            jump ember_shack_night3
        "stay hidden and leave":

            ya "(that bitch!)"
            yd "(why is she doing this?)"
            ya "(I'll have to talk to her later about it... and keep a close eye on her.)"
            jump ember_shack_night3



label sleepy_azula_anal:
    stop music
    play music "audio/Unwritten Return.mp3"
    scene black
    scene bg_a_2beds
    show amsl amsl23
    with dissolve
    show amsl amsl22 with dissolve
    "you walk in and azula immediately opens her eyes."
    "almost like she's been waiting for you."
    a "welcome. brother."
    "the way she says it is definitive. like the tolling of a bell."
    "a sense of understanding is heavy in the room. neither of you speak. there's no need."
    show amsl amsl00 with dissolve
    "azula moves slowly, fluidly, cat-like."
    "naked and delicate in the small, shared room, she crouches over mai."
    show amsl amsl12 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    menu:
        "undress":
            "you take off your clothes with ease and purpose, as if pulled by gravity."
        "go back to your room":

            y "no... i don't think i want this."
            show amsl amsl24 with dissolve
            a_b "you can't be serious."
            a_ub "pull out your cock, i need it."
            yd "no. i can't do this to mai."
            a_be "she doesn't {i}matter{/i}."
            a_ub "come here."
            y "no. good night, azula."
            a_ab "you can't-"
            scene black
            scene bg_a_island_hutnight
            with dissolve
            "you leave the room before she can finish yelling at you."
            yd "she... might not let me live that down."
            $ azula_angry = True
            scene black
            show bg_a_farm_singlegirl
            show blackveil
            with dissolve
            "you make your way to your room and undress."
            yn "good trip."
            scene black with dissolve
            jump third_night_memory

    "The sight and scent of her, waiting, patiently, is intoxicating."
    "she smells clean; ever so lightly of lilacs and vanilla."
    "your heart races as she presents her ass to you. there is no hurry. you both know why you came."
    show amsl amsl03 with dissolve
    "you approach her and rest your member lightly against her anus."
    show amsl amsl104
    "azula presses back into you... with mild hesitation."
    "you begin to press forward, and she stops all movement."
    "understanding, you wait for her to adjust."
    "after a moment, she moves again."
    show amsl amsl105
    pause 0.2
    with pflash
    a "*mmmh*"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "and in that moment you're inside of her."
    "azula, your sister."
    "bitter. vengeful. calculating. desperate."
    "you can feel her trying to adjust to the unfamiliar presence of your cock."
    "her anus squeezes you in quick, rapid succession as if trying to force you out, but only serving to make you harder."
    show amsl amsl106
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "ahhh..."
    "small, involuntary noises escape her throat as she pushes to welcome you deeper into her."

    "unable to take it any more, you move violently, thrusting your full mass inside of her."
    show amsl amsl11 with vshake
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "*ahh....*"
    "she holds herself there, but you can tell from the increasing quivering that she is struggling to keep her composure."
    show amsl amsl07 with dissolve
    "azula pulls herself off of your cock enough to gain reprieve from your size."
    show amsl amsl05 with dissolve
    "she slides again until she has almost completely pulled herself off..."
    show amsl amsl100
    "and slides back down, her determination overcoming her discomfort, and growing more confident with every stroke."
    "she begins to pick up speed, pulling out as she fucks you with her ass... making sure to fully stimulate the tip of your cock."
    a "ohhh...."
    "her moans become more frequent, pushing out of her as you enter her..."
    "almost as if each thrust of your cock knocks breath out of her."
    a "yes.... yes.... oh, zuzu... yes....."
    show amsl amsl101
    "her thrusts grow more desperate, her voice becomes more animal, and she skewers herself wildly on your cock."
    a "yes! yes! ngh! fuck! yes!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "fuck me, zuko! fuck me like the fucking whore i am!"
    ync "but mai...."
    a "fuck her! and {i}fuck. me."
    ync "wait, shhh...."
    show amsl amsl102
    a "if you don't give me what i fucking need, i'll wake her myself!"
    menu:
        "give her what she wants... some violence!":
            yna "you want it? take it!"
            play sound "audio/fleshslap.mp3"
            show amsl amsl101_1
            with flash
            a "{i}aahhh{/i}..."
            "you slap azula so hard her face turns back down as you beginning slamming her ass, all caution abandoned."
            "she matches your thrusts with violent eagerness."
            a "that's it, brother! show me who's really in charge!"
            yna "i'm gonna make you {i}hurt{/i}, you sick, manipulative bitch!"
        "go straight to giving it to her hard!":

            yna "you want it? take it!"
            show amsl amsl101_1
            with flash
            a "{i}aahhh{/i}..."
            "you beginning slamming her ass, all caution abandoned."
            "she matches your thrusts with violent eagerness."
            a "that's it, brother! show me who's really in charge!"
            yna "you're going to fucking {i}cry{/i}, azula."

    show ctcblink
    $ renpy.pause()
    hide ctcblink

    a "yes! own me! own my ass! show me!"
    a "prove my ass belongs to-"
    show amsl amsl101_2
    a "unghh! fuck!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "i'm a fuckpig!"
    a "fuck me! fuck my little ass! my poor little ass!"
    a "it's been waiting for big brother to come fill it!"
    ynd "(she seems really into degradation...)"
    menu:
        "spit on her back":
            play sound "audio/spit.mp3"
            show amsl amsl101_3
            with flash
            a "oh!"
            show amsl amsl11_1 with vpunch
            a "ah!"
            a "f...fuck..."
            a "...fuck!"
            a "don't... don't just leave it... oh, fuck it's deep..."
            show amsl amsl11_2 with dissolve
            a "what are... you... doing, broth... ah... brother...?"
            yna "put your head down!"
            show amsl amsl11_1 with dissolve
            a "w... why am i... ah..."
            yn "beg for it, whore."
            a "*mmmm....*"
            a "please, zuko... zuzu... don't make me suffer..."
            a "treat me right.... make me cry from your cock...."
            a "mo... move it... p... please... have mercy..."
            ynd "mercy?"
            yn "coming from you, i know exactly what kind of mercy to give, sis."

            yna "you're going to follow my orders, understand?"
            ynd "now..."
            yna "up!"
            show amsl amsl101_4 with dissolve
            a "unh..."
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "ah!"
            a "ow.... *mmmmmm*....."
            yna "up!"
            show amsl amsl101_4 with dissolve
            yn "who are you?"
            a "a... i'm... az... azula..."
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "unngh...."
            yna "now... {i}what{/i} are you?"
            a "y...your whore..."
            yna "up!"
            show amsl amsl101_4 with dissolve
            yn "what are you?"
            a "i'm a-"
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "ahh...."
            a "b... bitch..."
            yna "up!"
            show amsl amsl101_4 with dissolve
            yn "and?"
            a "a-"
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "s... stupid... cocksleeve..."
            a "who should be beaten."
            show amsl amsl101_4 with dissolve
            a "with precision."
            a "in a steel, soundproof room."
            a "i deserve to have my hair pulled and wear-"
            ynd "uh."
            show amsl amsl18_1 with dissolve
            a "what?"
            yn "shut up."
            show amsl amsl103 with dissolve
        "bury it and hold there":

            show amsl amsl11 with vpunch
            a "ah!"
            a "f...fuck..."
            a "...fuck!"
            a "don't... don't just leave it... oh, fuck it's deep..."
            show amsl amsl11_3 with dissolve
            a "what are... you... doing, broth... ah... brother...?"
            yna "put your head down!"
            show amsl amsl11 with dissolve
            a "w... why am i... ah..."
            yn "beg for it, whore."
            a "*mmmm....*"
            a "please, zuko... zuzu... don't make me suffer..."
            a "treat me right.... make me cry from your cock...."
            a "mo... move it... p... please... have mercy..."
            ynd "mercy?"
            yn "coming from you, i know exactly what kind of mercy to give, sis."
            yna "you're going to follow my orders, understand?"
            ynd "now..."
            yna "up!"
            show amsl amsl101_6 with dissolve
            a "unh..."
            yna "down!"
            show amsl amsl11 with vpunch
            a "ah!"
            a "ow.... *mmmmmm*....."
            yna "up!"
            show amsl amsl101_6 with dissolve
            yn "who are you?"
            a "a... i'm... az... azula..."
            yna "down!"
            show amsl amsl11 with vpunch
            yna "now... {i}what{/i} are you?"
            a "y...your whore..."
            yna "up!"
            show amsl amsl101_6 with dissolve
            yn "what are you?"
            a "i'm a-"
            yna "down!"
            show amsl amsl11 with vpunch
            a "ahh.... b... bitch..."
            yna "up!"
            show amsl amsl101_6 with dissolve
            yn "and?"
            a "a-"
            yna "down!"
            show amsl amsl11 with vpunch
            a "s... stupid... cocksleeve..."
            a "who should be beaten."
            a "with precision."
            a "in a steel, soundproof room."
            a "i deserve to have my hair pulled and wear-"
            ynd "uh."
            show amsl amsl18 with dissolve
            a "what?"
            yn "shut up."
            show amsl amsl103

    show amsl amsl11 with vpunch
    a "nngh...."
    a "...fuck."
    yn "...."
    yna "get to it!"
    show amsl amsl04 with dissolve
    a "....yes, brother...."

    show amsl amsl101_1
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yn "do you like getting your asshole fucked ruthlessly over your friend?"
    a "yes!"
    a "pound my ass over your sleeping girlfriend!"
    a "mai... that frigid bitch... can suck it..."
    a "{i}i{/i} know what you need, brother..."
    yn "oh, fuck, azula... your ass is unreal..."
    a "yes, that's it... enjoy it, zuzu."
    a "it's all yours."
    a "i'm going to..."
    a "i'm going to make you cum."
    a "...oh my god."
    a "......."
    a "...i can't believe it."
    a "i can't believe it!"
    a "you're going to cum in me!"
    a "oh my god!"
    show amsl amsl101_2
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "do it!"
    a "*ah!*"
    a "cum for me!"
    a "cum!"
    a "i don't... *ah!*... i don't think i can do much more..."
    yna "you want my cum, azula?"
    a "yes! *ngh!* please!"
    yna "you want it, sis?"
    a "*ah!* give it to *unh!* me!"
    yna "fuck.. fuck.. fuck!"
    yna "here it cums!"
    yna "i'm fucking cumming! take my load, sis!"
    a "yes! pound *ah!* my fucking asshole, brother!"
    a "{size=+5}cum for me!"
    menu:
        "cum inside":
            $ azula_in_ass = True
            show amsl amsl10 with vpunch
            a "fuck!"
            play sound "audio/splurt3.ogg"
            show amsl_sperminass_1
            with flash
            a "yes!"
            play sound "audio/splurt2.ogg"
            show amsl_sperminass_2
            with flash
            a "big brother!"
            play sound "audio/splurt3.ogg"
            show amsl_sperminass_2
            with flash
            a "{size=+6}cum in me, zuko!"
        "cum outside":


            $ azula_on_ass = True
            show amsl amsl12 with vpunch
            a "fuck!"
            play sound "audio/splurt3.ogg"
            show amsl_spermonbutt_1
            with flash
            a "yes!"
            play sound "audio/splurt2.ogg"
            show amsl_spermonbutt_2
            with flash
            a "big brother!"
            play sound "audio/splurt3.ogg"
            show amsl_spermonbutt_3
            with flash
            a "{size=+6}cum on me, zuko!"


    show az_mai_eyesopen with vshake
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "what..."
    m "what's going on...?"
    play sound "audio/splurt3.ogg"
    with flash
    yna "ngh!"
    ync "......"
    a "........."
    ync "you're, uh, you're having a dream."
    play sound "audio/splurt3.ogg"
    with flash
    a "yes, a dream, mai."
    m "zuko...?"
    if azula_in_ass:
        m "are... you cumming in azula right now?"
    m "....are you two having sex?"
    yn "ssshhhhh.... sh."
    yn "that's just crazy."
    play sound "audio/splurt3.ogg"
    with flash
    a "it's all a dream, mai."
    a "i fell over is all."
    a "go to sleep."
    m "oh... okay..."
    hide az_mai_eyesopen with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "......"
    a "well, that was close."
    a "...you came a lot."
    ync "yeah... her waking up in the middle just..."
    ync "it was the fear."
    ynd "adrenaline, maybe?"
    yn "either way, i just had a fucking great orgasm."
    a "well... i feel like you've earned some rest."
    a "i know i have..."
    yng "have you?"
    if azula_in_ass:
        show az_azula_turnhead4 with dissolve
    else:
        show az_azula_turnhead1 with dissolve
    a "don't confuse who's really in charge here, brother."

    if azula_in_ass:
        show amsl amsl12
        show amsl_spermonbutt_0
        hide az_azula_turnhead4
        hide amsl_sperminass_2
        hide amsl_sperminass_1
        hide amsl_sperminass_3
        with dissolve
    if azula_on_ass:
        hide az_azula_turnhead1 with dissolve
    a "i think it's time for you to leave."
    ynd "...what? you're kicking me out?"
    a "you did your job."
    ynd "i feel used."
    a "oh, you were."
    a "...and so was i, unless you've already forgotten..."
    a "we used each other."
    a "in this cold, dark world."
    a "family, brother."
    a "get some rest."

    "azula, cum dripping out and down her ass, crawls away from you on all fours."
    "it's a pleasure to watch."
    show amsl amsl22
    hide amsl_spermonbutt_0
    hide amsl_spermonbutt_1
    hide amsl_spermonbutt_2
    hide amsl_spermonbutt_3
    with dissolve
    a "goodnight... brother."
    show amsl amsl23 with dissolve
    a "I'm exhausted."
    a "i'll see you in the morning."
    menu:
        "return to your room":
            scene black
            show bg_a_farm_singlegirl
            show blackveil
            with dissolve
            "you make your way to your room, completely wiped."
            yn "good trip."
            scene black with dissolve
            jump third_night_memory

label third_night_memory:
    stop music
    play music "audio/Kai_Engel_-_01_-_Take_a_Look_Around_You.mp3"
    scene black with Dissolve(1.0)
    "you fall asleep immediately, as if you were being pulled into dreams."
    show azft_fireshadows with Dissolve(1.0)
    "{b}this is your last chance."
    "{b}we can only reach you here, on the island."
    ync "what are you?"
    "{b}we are familiar to you because we were not always spirits."
    "{b}this island is... you may think of it as a safe harbor for us."
    "{b}good luck, avatar."
    ync "avatar...?"
    scene black with dissolve
    "you fall for a long time."
    "when your body slows, you are once again greeted by a gentle, familiar voice."
    s "two of these doors are false memories."
    s "find your way."
    $ glow = 1
    jump third_map


label fourth_ember_day:
    $ az_mai_choice = True
    scene white with dissolve
    show text "Ember Island\n\nfourth day"
    $ renpy.pause (1.5, hard=True)
    scene white with dissolve
    $ ember_day = 4
    play music "audio/Bassa Island Game Loop.ogg"
    scene bg_a_farm_singlegirl with Dissolve(1.0)

    ync "....that can't be right."
    ync "i can't.... i can't be the avatar."
    ync "i'm zuko."
    yn "i'm zuko."
    yn "that... that's just crazy."
    yn "just dreams."
    ync "I'll... i'll just go see if anyone's awake."
    scene bg_a_island_hutday with dissolve
    yd "i guess they're all still asleep."
    show azms azms05_1 with dissolve
    m "i'm not."
    yd "you're... naked."

    if azula_angry:
        m "well, we've all seen each other naked by now."
        m "i mean, you've been {i}inside{/i} me, zuko."
        y "...right."
        y "so-"
        show azms azms07_1 with dissolve
        m "*yaaawn*"
        yd "...okay, i'll wait."
        show azms azms05_1 with dissolve
        y "as i was saying-"
        show azms_yawn with dissolve
        m "*yaaawn*"
        ya "would you stop it!"
        m "'m 'ired...."
        yd "what?"
        hide azms_yawn with dissolve
        m "i'm tired."
        m "i had trouble sleeping last night."
        y "you did?"
        m "yeah. i had the weirdest dream."
        y "really? what?"
        m "well, it was you and-"
        show azula_idle_fl_beach:
            xpos -30
        show a_idle_fl_face_anger:
            xpos -30
        with dissolve

        a "......."
        yc "oh, uh... good morning..."
        m "azu-?"
        hide azula_idle_fl_beach
        hide a_idle_fl_face_anger
        show azula_idle_ff_beach:
            xpos -200
            parallel:
                ease 0 zoom 1.15
            parallel:
                yalign 0.0
                linear 0 yalign 0.5
        show a_idle_ff_face_anger:
            xpos -200
            parallel:
                ease 0 zoom 1.15
            parallel:
                yalign 0.0
                linear 0 yalign 0.5
        with dissolve

        a "no one disobeys me like that."
        a "you humiliated me..."
        a "that was your last chance, zuzu... and... and if you don't recognize how good..."
        a "you are going to regret your... decision, {i}brother{/i}."
        a "mai! pack everything."
        a "just... agh!"
        hide azula_idle_ff_beach
        hide a_idle_ff_face_anger
        with dissolve
        m "...what was that about?"
        y "azula's... been trying to fuck me."
        show azms azms06_1 with Dissolve(1.0)
        m ".....{size=+5}what!?!"
        m "that bitch!"

        m "you haven't... done anything with her, right?"
        yc "uh... she may have... organized some... recreation time."
        m "what?"
        yc "...a little."
        yc "but i didn't want to!"
        show azms azms08_1 with dissolve
        m "i'm gonna... she's gonna..."
        m "ty lee!"
        m "wake up!"
        show ty_idle_fl_nude:
            xpos 10
        with Dissolve(1.0)
        t "hhghm... wha'?"
        m "i'm going out. now. grab my clothes and meet me outside. now."
        t "huh? okay?"
        hide ty_idle_fl_nude with dissolve
        yd "hey, don't-"
        m "i need to go punch a tree."
        y "are you mad at me?"
        show azms_normalface with dissolve
        m "no... i just need some fresh air."
        scene black
        scene bg_a_island_hutday
        with dissolve
        y "well, if they're gone i might as well go too."
        jump emberday
    else:


        m "my clothes had something sticky all over them."
        yc "oh, uh..."
        m "but i'm not shy."
        m "we've all seen each other naked by now."

        if mai_flower_got or ember_deed:
            m "i mean, you've been {i}inside{/i} me, zuko."
            y "...right."

        y "so-"
        show azms azms07_1 with dissolve
        m "*yaaawn*"
        yd "...okay, i'll wait."
        show azms azms05_1 with dissolve
        y "as i was-"
        show azms_yawn with dissolve
        m "*yaaawn*"
        ya "would you stop it!"
        m "'m 'ired...."
        yd "what?"
        hide azms_yawn with dissolve
        m "i'm tired."
        m "i had trouble sleeping last night."
        y "you did?"
        m "yeah. i had the weirdest dream."
        y "really? what?"
        m "well, it was you and-"
        show azula_idle_fl_beach:
            xpos -30





        with dissolve

        a "good morning, all."
        a "how did you sleep, mai?"
        m "a little restlessly."
        a "well, i slept {i}very{/i} well."
        a "i had a great night."
        m "you mean around the fire? or--"
        hide azula_idle_fl_beach
        show azula_idle_ff_beach:
            xpos -200
            parallel:
                ease 0 zoom 1.15
            parallel:
                yalign 0.0
                linear 0 yalign 0.5
        show a_idle_ff_face_blush:
            xpos -200
            parallel:
                ease 0 zoom 1.15
            parallel:
                yalign 0.0
                linear 0 yalign 0.5
        with dissolve

        a "zuko, that was... amazing..."
        a "you should... hurt me more."
        yc "what are you doing, don't--"
        a "my ass is still sore."
        a "bye, you two."
        hide azula_idle_ff_beach
        hide a_idle_ff_face_blush
        with dissolve
        m ".........."
        yc "mai, i can--"
        show azms azms06_1 with Dissolve(1.0)
        m "it wasn't a dream!"
        m "what the fuck, zuko?! your sister?!"
        m "how could you?!"
        ya "you cut me off from sex!"
        m "{size=+6}so you fucked your sister?!"
        yc "it was just circumstance and-"
        show azms azms08_1 with dissolve
        m "i can't even look at you!"
        m "ty lee!"
        m "wake up!"
        show ty_idle_fl_nude:
            xpos 10
        with Dissolve(1.0)
        t "hhghm... wha'?"
        m "i'm going out. now. grab my clothes and meet me outside. now."
        t "huh? okay?"
        hide ty_idle_fl_nude with dissolve
        yd "hey, don't-"
        m "don't talk to me!"
        ya "calm down!"
        m "you want me to calm down??"
        show azms_normalface with dissolve
        m "....."
        y "see? now maybe we can-"
        show azms_fist with hpunch
        y "ow. great, now i'm unconcious."
        scene black with dissolve
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        scene bg_a_island_hutday
        with dissolve
        yc "....ow."
        yd "where did they go?"
        yd "....."
        yc "fuck."
        yd "there doesn't seem to be anyone here."
        yd "i should see if i can find someone...."
        jump emberday


label ember_azula_talk_day4:
    $ ember = 16
    scene bg_a_beach_01 with dissolve
    show azula_idle_fl_beach with dissolve
    a "alright, what's the problem?"
    yd "what's the..."
    ya "mai won't talk to me!"
    yd "and i have no idea what you and i are doing."
    a "having fun."
    show a_idle_fl_face_blink with dissolve
    a "and i'm having a lot of it."
    hide a_idle_fl_face_blink with dissolve
    a "i loved that, last night."
    a "i've never felt so satisfied."
    a "so.... used."
    a "it was enlightening."
    yd "\"enlightening\"?"
    a "yes, and in fact, i'd like you to romance me."
    y "you..."
    yd "what?"
    a "i would like some romance."
    yd "........"
    yd "i have no idea how to do that with you."
    a "well, figure it out."
    a "i would like some to go alongside our... violent... sexplay."
    a "if you can't, then i might have to cut you off, just like mai did...."
    yd "i thought you liked being called a whore?"
    show a_idle_fl_face_blink with dissolve
    a "during... last night, yes."
    a "don't confuse sextalk with realtalk, zuko."
    hide a_idle_fl_face_blink with dissolve
    a "i know what i want, and i'm not afraid to take it from you."
    yd "that's obvious."
    show a_idle_fl_face_unsure with dissolve
    a "but while i enjoy... what we do... i'm still a person."
    hide a_idle_fl_face_unsure with dissolve
    a "...but i can be a whore for you."
    a "like you've never seen."
    a "now i think we need to get to the dock."
    a "our ship back to the city should be arriving any minute now."
    y "alright."
    jump emberday


label find_ember_treasure:
    y "\"where twin flames rest\", and li and lo used to sleep here..."
    y "so the treasure must be somewhere in this room."
    "you search all over the room."
    ya "nothing!"
    ya "it would have been worth sleeping on this lumpy, creaky bed of hay if i'd found-"
    yd "wait."
    "you move the hay and find a trap door."
    y "hot damn."
    "opening it, you find a small puzzlebox."
    y "hmm.. interesting. i'll solve it some other time."
    play sound "audio/win2.mp3"
    "you found a puzzlebox!"
    $ ember_treasure_found = True
    jump emberday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
