
image bk4_train_day = "bk4/backgrounds/training_day_1.jpg"
image bk4_tower = "bk4/backgrounds/tower_day_1.jpg"
image korra_fight:
    "bk4_xtra/probending/enemies/korra_fight1.png"
    1.5
    "bk4_xtra/probending/enemies/korra_fight2.png"
    1.5
    repeat

image probending_game_over:
    "bk4_xtra/probending/effects/game_over.png" with Dissolve(0.2)
    0.2
    "bk4_xtra/probending/effects/game_over_2.png" with Dissolve(0.2)
    0.2
    "bk4_xtra/probending/effects/game_over_3.png" with Dissolve(0.2)
    0.2
    "bk4_xtra/probending/effects/game_over_4.png" with Dissolve(0.2)

label bk4_probending_start:
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Action.mp3"

    $ bk4_arena_korra_score = 0
    $ bk4_arena_score = 0

    $ bk4_arena_attacks = 0
    $ bk4_arena_circle = "bk4_xtra/probending/enemies/bk4_blue_near.png"
    $ bk4_arena_player_element = "water"
    $ bk4_arena_opp_element = "bk4_xtra/probending/enemies/bk4_fire.png"
    $ bk4_arena_opp_xpos = 350
    $ bk4_arena_opp_ypos = 200
    $ bk4_arena_clicked = False

    $ temp_boolean = False
    $ temp_boolean2 = False
    $ bk4_arena_hits = 0

    scene bk4_train_day
    with Dissolve(1)

    if not probending_first:
        jump bk4_arena_intro
    else:
        menu:
            "instructions":
                jump bk4_arena_instructions
            "get to the fight!":

                jump bk4_arena_fight

label bk4_arena_intro:
    tn "so this is the arena, eh?"
    show bfad bfad02 with dissolve
    asa "hey!"
    asa "tenzin, right?"
    tn "yeah, what are you doing here?"
    asa "sato industries is sponsoring team avatar, remember?"
    tn "oh, right."
    asa "what about you?"
    tn "I'm taking over as coach."
    asa "oh, thank goodness."
    asa "they need it."
    show bfad bfad03 with dissolve
    asa "did you know that they {i}aren't good{/i}?"
    asa "because that would have been nice to know {i}before{/i} we sponsored them."
    tn "i was told very recently about it."
    show bfad bfad02 with dissolve
    asa "ah, well."
    tn "so, where are they?"
    asa "about to go on."
    tn "...how do i talk to them?"
    asa "you're in luck there!"
    asa "probenders are all provided with undetectable, brand new, state of the art, sato industries ear-hearies!"
    tn "...earphones?"
    asa "that's a silly name..."
    asa "but no, we call them ear-hearies."
    asa "here."
    "asami hands you a small ear piece."
    tn "alright, whatever."
    tn "so i can just put this in and talk to them?"
    asa "yes."
    asa "you should review the rules first, though."
    hide bfad
    with fade
    jump bk4_arena_instructions

label bk4_arena_instructions:

    "benders will attack korra with fire, water, or earth."

    show expression bk4_arena_circle:
        xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos

    "This is what their attack will look like... but there's a twist."
    "These are distractions that are used to hide the real attacks."

    show expression bk4_arena_opp_element:
        xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos

    "the real attack is {b}fire{/b}."
    "Don't be fooled by the color of the circle!"
    "The real element is the {b}word{/b} inside."
    "That's what you'll have to counter."
    show screen bk4_arena_elements_2

    "Each of your three counter elements are set to a numeral key:\n1 = Water, 2 = Earth, 3 = Fire."
    "Water beats Earth, Earth beats Fire, Fire beats Water."
    "You'll need to type the countering element's key on your keyboard (1, 2, or 3), and then click the attack with your mouse."
    "Or if you're using a touchscreen, press the images 1, 2 or 3."
    "Remember to counter the {b}word{/b} in the circle, not the color."
    hide screen bk4_arena_elements_2
    show screen bk4_arena_elements
    "Since Korra is being attacked with {b}Fire{/b}, you need to tell her to counter with {b}Earth{/b}."
    "Type the {b}2{/b} key to prepare your {b}Earth{/b} counter, then click on the attack to stop it!"
    jump bk4_arena_tutorial_fight

label bk4_arena_tutorial_fight:
    hide screen bk4_arena_elements
    call screen bk4_arena_elements_3

    if bk4_arena_player_element != "earth":
        "You need to type the {b}2{/i} key on your keyboard to select {b}Earth{/b}, and then click on the {b}Fire{/b} attack to stop it!"
        jump bk4_arena_tutorial_fight
    else:


        "Well done!"
        "Remember, don't be fooled by the color of the circle, pay attention to the {b}word{/b} inside."
        "In the real thing, you'll have to move quickly or they'll hit her!"

    hide bk4_arena_circle
    hide bk4_arena_opp_element

    menu:
        "ready":
            jump bk4_arena_fight
        "uh... what?":

            jump bk4_arena_instructions

label bk4_arena_fight:

    scene bk4_train_day

    if not probending_intro:
        show bfab bfab09
        with fade

        kn "alright guys, let's-"
        tn "korra."
        show bfab bfab24 with dissolve
        kn "who... tenzin?"
        kn "what are you doing?"
        tn "i'm here to help."
        tn "you guys suck, and i'm here to coach you."
        kn "really?"
        tn "yeah, you apparently really need me."
        kn "i guess we can give it a try."
        tn "do exactly as i say, and you'll get through this."

        hide bfab bfab09 with dissolve
        show korra_fight with dissolve
        kn "alright, then."
        kn "come on!"
    else:

        show korra_fight
        with fade
        jump bk4_arena_select2








label bk4_arena_select:



    if bk4_arena_attacks <10:
        $ bk4_arena_attacks +=1
        $ bk4_arena_circle = "none"
        $ bk4_arena_circle = renpy.random.choice(["bk4_xtra/probending/enemies/bk4_blue_near.png","bk4_xtra/probending/enemies/bk4_blue_mid.png","bk4_xtra/probending/enemies/bk4_blue_far.png","bk4_xtra/probending/enemies/bk4_green_near.png","bk4_xtra/probending/enemies/bk4_green_mid.png","bk4_xtra/probending/enemies/bk4_green_far.png","bk4_xtra/probending/enemies/bk4_red_near.png","bk4_xtra/probending/enemies/bk4_red_mid.png","bk4_xtra/probending/enemies/bk4_red_far.png"])
        $ bk4_arena_opp_element = "none"
        $ bk4_arena_opp_element = renpy.random.choice(["bk4_xtra/probending/enemies/bk4_water.png","bk4_xtra/probending/enemies/bk4_earth.png","bk4_xtra/probending/enemies/bk4_fire.png"])
        $ bk4_arena_opp_xpos = 0
        $ bk4_arena_opp_xpos = renpy.random.randint(50,800)
        $ bk4_arena_opp_ypos = 0
        $ bk4_arena_opp_ypos = renpy.random.randint(50,500)
        $ bk4_arena_clicked = False
        $ temp_boolean2 = False
        $ rand_time = 3

        show expression bk4_arena_circle:
            xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos

        show expression bk4_arena_opp_element:
            xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos

        call screen bk4_arena_1

        hide expression bk4_arena_circle
        hide expression bk4_arena_opp_element

        if bk4_arena_clicked:
            if bk4_arena_opp_element == "bk4_xtra/probending/enemies/bk4_water.png":
                if bk4_arena_player_element == "fire":
                    $ bk4_arena_score +=10
                else:
                    $ bk4_arena_korra_score +=20
                    $ bk4_arena_hits +=1
                    $ temp_boolean2 = True

            if bk4_arena_opp_element == "bk4_xtra/probending/enemies/bk4_earth.png":
                if bk4_arena_player_element == "water":
                    $ bk4_arena_score +=10
                else:
                    $ bk4_arena_korra_score +=20
                    $ bk4_arena_hits +=1
                    $ temp_boolean2 = True

            if bk4_arena_opp_element == "bk4_xtra/probending/enemies/bk4_fire.png":
                if bk4_arena_player_element == "earth":
                    $ bk4_arena_score +=10
                else:
                    $ bk4_arena_korra_score +=20
                    $ bk4_arena_hits +=1
                    $ temp_boolean2 = True
        else:


            $ bk4_arena_hits +=1
            $ temp_boolean2 = True


        if bk4_arena_korra_score >=100:
            jump probending_game_over_man
        else:

            if temp_boolean2:
                if bk4_arena_hits ==1:
                    kn "Ouch!"
                    tn "sorry!"

                if bk4_arena_hits ==2:
                    kn "Ouch!"
                    kn "Shit!"

                if bk4_arena_hits ==3:
                    kn "Ouch!"
                    tn "my bad!"

                if bk4_arena_hits ==4:
                    kn "Ouch!"
                    tn "come on, we got this!"

                if bk4_arena_hits ==5:
                    kn "Ouch!"
                    tn "we can do this!"

            jump bk4_arena_select


    if bk4_arena_korra_score >= 100:
        jump probending_game_over_man


    jump bk4_post_fight_check

label bk4_arena_select2:

    if bk4_arena_attacks <10:
        $ bk4_arena_attacks +=1
        $ bk4_arena_circle = "none"
        $ bk4_arena_circle = renpy.random.choice(["bk4_xtra/probending/enemies/bk4_blue_near.png","bk4_xtra/probending/enemies/bk4_blue_mid.png","bk4_xtra/probending/enemies/bk4_blue_far.png","bk4_xtra/probending/enemies/bk4_green_near.png","bk4_xtra/probending/enemies/bk4_green_mid.png","bk4_xtra/probending/enemies/bk4_green_far.png","bk4_xtra/probending/enemies/bk4_red_near.png","bk4_xtra/probending/enemies/bk4_red_mid.png","bk4_xtra/probending/enemies/bk4_red_far.png"])
        $ bk4_arena_opp_element = "none"
        $ bk4_arena_opp_element = renpy.random.choice(["bk4_xtra/probending/enemies/bk4_water.png","bk4_xtra/probending/enemies/bk4_earth.png","bk4_xtra/probending/enemies/bk4_fire.png"])
        $ bk4_arena_opp_xpos = 0
        $ bk4_arena_opp_xpos = renpy.random.randint(50,800)
        $ bk4_arena_opp_ypos = 0
        $ bk4_arena_opp_ypos = renpy.random.randint(50,500)
        $ bk4_arena_clicked = False
        $ temp_boolean2 = False
        $ rand_time = 0
        $ rand_time = renpy.random.randint(1,3)
        if rand_time ==1:
            $ rand_time = 1.5
        if rand_time ==2:
            $ rand_time = 2
        if rand_time ==3:
            $ rand_time = 2.5

        show expression bk4_arena_circle:
            xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos

        show expression bk4_arena_opp_element:
            xpos bk4_arena_opp_xpos ypos bk4_arena_opp_ypos

        call screen bk4_arena_1

        hide expression bk4_arena_circle
        hide expression bk4_arena_opp_element

        if bk4_arena_clicked:
            if bk4_arena_opp_element == "bk4_xtra/probending/enemies/bk4_water.png":
                if bk4_arena_player_element == "fire":
                    $ bk4_arena_score +=10
                else:
                    $ bk4_arena_korra_score +=20
                    $ bk4_arena_hits +=1
                    $ temp_boolean2 = True

            if bk4_arena_opp_element == "bk4_xtra/probending/enemies/bk4_earth.png":
                if bk4_arena_player_element == "water":
                    $ bk4_arena_score +=10
                else:
                    $ bk4_arena_korra_score +=20
                    $ bk4_arena_hits +=1
                    $ temp_boolean2 = True

            if bk4_arena_opp_element == "bk4_xtra/probending/enemies/bk4_fire.png":
                if bk4_arena_player_element == "earth":
                    $ bk4_arena_score +=10
                else:
                    $ bk4_arena_korra_score +=20
                    $ bk4_arena_hits +=1
                    $ temp_boolean2 = True
        else:

            $ bk4_arena_hits +=1
            $ temp_boolean2 = True

        if bk4_arena_korra_score >=100:
            jump probending_game_over_man
        else:

            if temp_boolean2:
                kn "Ouch!"
                tn "sorry!"
            jump bk4_arena_select2


    if bk4_arena_korra_score >= 100:
        jump probending_game_over_man

    jump bk4_post_fight_check

    kn "Suck it!"

    return

label bk4_after_probending:
    if probending_won:
        hide korra_fight
        show bk4_train_day
        show bfab bfab03
        show screen bk4_money_date
        with dissolve
        kn "we did it!"
        kn "tenzin, you're amazing!"
        kn "we really, really need you on the team."
        tn "okay, but don't you forget it."
        kn "i won't!"
    else:

        hide korra_fight
        show bk4_train_day
        show bfab bfab25
        show screen bk4_money_date
        with dissolve
        kn "well, we lost..."
        kn "but at least we did better than usual."
        kn "thanks for the help, tenzin..."
        kn "we really, really need you on the team."
        kn "obviously."

    play sound "audio/money.mp3"
    $ bk4_money += pb_money_got
    "you got [pb_money_got] coins!"
    $ pb_money_got = 0
    $ probending_time = 0
    $ probending_intro = True

    if not probending_first:
        $ probending_first = True
        scene black with dissolve
        "you leave the arena and find yourself in a hallway."
        "you hear footsteps approaching and, on a whim, you duck into a room."
        "they stop near you."
        b4_eq2 "........"
        b4_eq2 "...where am i?"
        b4_eq1 "what?"
        b4_eq2 "these hallways are confusing."
        b4_eq1 "it's... one hallway."
        b4_eq1 "it's literally just one long hallway."
        b4_eq2 "it is?"
        b4_eq1 "...how do you function?"
        b4_eq2 "with aplomb."
        b4_eq1 "how do you know that word and are still lost in a straight hallway?"
        b4_eq2 "i guess i'm just focused on the new plan."
        b4_eq1 "yeah, i can't wait either."
        b4_eq2 "but what about the benders?"
        b4_eq1 "what {i}about{/i} the benders?"
        b4_eq1 "they've been oppressors for as long as they've existed."
        b4_eq2 "yeah... you're right..."
        b4_eq1 "i know i'm right."
        b4_eq1 "look, when the gathering goes down... which it will in a few days..."
        b4_eq1 "we're going to shake the benders to their core."
        b4_eq2 "and we're sure the zappy things will work?"
        b4_eq1 "they work on me..."
        b4_eq1 "........."
        b4_eq1 "i don't use them on my nipples."
        b4_eq2 "......"
        b4_eq1 "........"
        b4_eq2 "..........."
        b4_eq1 "...empanadas?"
        b4_eq2 "empanadas."
        "they walk off."
        tn "i should let lin know about this."

    $ b4_daytime = False

    jump b4_airtemple_map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
