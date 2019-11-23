label emberday:
    $ yn = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_neutral.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    scene black
    scene bg_island_day
    with dissolve
    if ember_day ==1:
        call screen emberisland_map_day1
    if ember_day ==2:
        call screen emberisland_map_day2
    if ember_day ==3:
        if nude_sunbathing and blind_game and crabble_royal:
            if bottle_spin:
                call screen emberisland_map_day3
            else:

                scene bg_a_beach_01
                show tylee_idle_ff_beach:
                    xpos -250
                with dissolve
                t "hey guys! look what i found!"
                t " a bottle with a message!"
                show azula_idle_fl_beach
                a "let me see that."
                a "hmmm...."
                a "\"help! my name is sokka and i desperately--"
                a "well that's trash."
                "she throws away the message."
                a "but now we have a bottle."
                a "and you know what we can do with a bottle?"
                show mai_fl_flip:
                    xpos 100
                with dissolve
                m "spin it."
                a "exactly."
                $ bottle_spin = True
                jump spin_the_bottle

        "Explore the island and play each minigame at least once."
        call screen emberisland_map_day3
    if ember_day ==4:
        call screen emberisland_map_day4


label embernight:
    scene bg_island_night
    with dissolve
    if ember_day ==1:
        call screen emberisland_map_night1
    if ember_day ==2:
        call screen emberisland_map_night2
    if ember_day ==3:
        call screen emberisland_map_night3
    if ember_day ==4:
        "test"




label ember_beach_day1:
    if ember == 0:
        jump ember_beach
    if ember ==1:
        scene black
        scene bg_a_beach_01
        with dissolve
        if twins_encounter ==1:

            y "man, the less time i spend with those two the happier i'm gonna be."
            show twins_1
            with dissolve
            lal "hello, prince."
            ya "ah!"
            yd "didn't i just... how did you get here so fast?"
            lal "we know know the island well."
            lal "we know lots of things."
            lal "things you should learn."
            yd "now you're creeping me out."
            lal "self discovery, boy."
            ya "you keep saying that and it's getting annoying."
            ya "i don't even know what that means."
            lal "not yet, perhaps. who are you?"
            yd "uh... i'm zuko. prince of the fire nation?"
            lal "are you?"
            yd "who else would i be?"
            lal "who indeed......."
            $ twins_encounter = 3
            yd "....."
            yd "are... you just done talking?"
            yd "..........."
            yd "did you die?"
            yc "oh fuck, for real, are you dead?"
            lal "of course we're not dead! but you shouldn't be with us. go enjoy yourself."
            yc "can you... put your tits away?"
            lal "we're going swimming!"
            yc "yeah, i'm out of here."
            hide twins_1 with dissolve
            jump emberday

        if twins_encounter ==3:
            stop music fadeout 2
            play music "audio/Bassa Island Game Loop.ogg"
            jump volleyball
        else:

            y "hmm... nothing much here."
            y "i'll come back in a bit, maybe."
            jump emberday

    if ember ==2:
        scene bg_a_beach_01 with dissolve
        jump beach_mai_flower_menu

        label beach_mai_flower_menu:
            menu:
                "search by the chairs" if not secluded_flower:
                    scene bg_a_beach_chairs with dissolve
                    yd "not seeing any flowers..."
                    jump beach_mai_flower_menu

                "search closer to the shore" if not secluded_flower:
                    scene bg_a_beach_02 with dissolve
                    yd "no flowers."
                    show shadyguy_grin with dissolve
                    sg "hey buddy!"
                    yd "who are you?"
                    hide shadyguy_grin
                    show shadyguy_unsure
                    with dissolve
                    sg "ouch. that hurts."
                    sg "i'm just a guy. i'm around."
                    yd "wait, i know you... don't you hang out in the alleys in the city?"
                    hide shadyguy_unsure
                    show shadyguy_grin
                    with dissolve
                    sg "there you go!"
                    sg "knew you'd remember!"
                    y "what are you doing out here?"
                    yd "also, it's like a billion degrees out, why are you wearing a coat...?"
                    sg "for the ladies."
                    yd "...i don't want to know more, do i?"
                    sg "heh, you really don't."
                    sg "and i've got this shop my brother gave me... it's not working for me though."
                    sg "can't keep going back and forth between the city and the island."
                    sg "it's costing me a fortune in taxes, so i'm trying to get rid of it."
                    y "huh."
                    sg "if you know anyone who's looking, let me know, eh?"
                    sg "anyway, don't mean to bore you."
                    sg "what are you doing out here?"
                    yd "looking for flowers, but can't seem to find any."
                    sg "hmm... i think there's some down over there where it's a little more secluded."
                    y "hey, thanks!"
                    sg "no problem."
                    angry_girls "there's the flasher!"
                    angry_girls "get him!"
                    sg "i've... got to go."
                    sg "see ya!"
                    hide shadyguy_grin with dissolve
                    yd "guess i'll check out over there..."
                    $ secluded_flower = True
                    jump beach_mai_flower_menu

                "search where it's a little secluded" if secluded_flower:
                    scene bg_a_beach_00
                    show bg_k_mountain_flower:
                        xpos 0.5 ypos 0.5
                    with dissolve
                    y "oh, nice!"
                    y "it's really small, but it's pretty."
                    play sound "audio/win2.mp3"
                    hide bg_k_mountain_flower with dissolve
                    "you got the flower!"
                    y "i hope she likes it."
                    $ mai_flower_got = True
                    $ ember = 3
                    jump emberday

                "back to island" if not secluded_flower:
                    jump mai_flower_hunt

    if ember ==3:
        jump volleyball
    else:

        y "hmm.... nothing here right now."
        jump emberday

label ember_party_day1:
    menu:
        "house path":
            show fireguard_halberd with dissolve
            g "this is a private residence."
            g "unless you have an invitation, please return the way you came."
            hide fireguard_halberd with dissolve
            jump ember_party_day1
        "forest path":


            scene black
            scene bg_emberisland_wood
            with dissolve
            if ember == 2:
                "you wade into the forest."
                ya "god damn foliage!"
                ya "who put this here?"
                yd "...i think i just got a bug bite on my ass."
                ya "and how are there no flowers?!"
                ya "useless ass jungle!"
                ya "be a parking lot or leave!"
                jump ember_party_day1
            else:
                "you wade into the forest."
                ya "god damn foliage!"
                ya "who put this here?"
                yd "...i think i just got a bug bite on my ass."
                ya "useless ass jungle!"
                ya "be a parking lot or leave!"
                jump ember_party_day1
        "back to island":

            jump emberday

label ember_shop_day1:
    scene bg_emberisland_ghosthouse with dissolve
    if billy_mays:
        gobm "{size=+8}{i}{b}\"for only the low, low price of-\"{/i}"
        ya "leave me alone, billy!"
        jump emberday
    else:
        y "doesn't look like anything."
        yd "except maybe haunted."
        y "i might come here another time."
        ya "but not because i'm afraid of ghosts."
        yc "i totally don't hear billy mays screaming his name at me in the dark."
        yc ".........."
        yd "who am i talking to?"
        y "shh, zuko. it's okay."
        gobm "{size=+8}{i}{b}\"billy mays here with a great new-\"{/i}"
        ya "shut up, billy!"
        yd "...i might be crazy."
        $ billy_mays = True
        jump emberday

label ember_water_day1:
    y "hmm... i'm gonna need a boat to go out there."
    jump emberday

label ember_shack_day1:
    scene black
    show emberisland_dock:
        ypos 0
    with dissolve

    if ember ==0:
        menu:
            "shack":

                if masturbate_in_closet:
                    scene bg_a_island_hutday
                    with dissolve
                    y "not much going on here right now."
                    menu:
                        "outside":
                            jump ember_shack_day1
                        "check out island":
                            jump emberday
                else:

                    y "not much going on here right now."
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
                                "island":

                                    y "guess i'll check out the island."
                                    jump emberday
                        "back to the island":

                            jump emberday
            "dock":

                scene emberisland_dock with dissolve
                yd "......where did our boat go?"
                yd "are we really just abandoned here?"
                ya "because i will eat people if i have to."
                yd "...balls."
                jump ember_shack_day1
            "back to the island":

                jump emberday

    if ember ==1:
        menu:
            "shack":
                if twins_encounter ==0:
                    $ twins_encounter = 1
                    scene bg_a_island_hutday
                    show twins_0
                    with Dissolve(0.8)
                    lal "hello, prince zuko."
                    yd "ugh, you two."
                    yd "you're so old."
                    lal "yes, prince."
                    lal "how are you enjoying your stay?"
                    yd "it's fine i guess."
                    yd "do you two have cats? are you hiding cats here?"
                    lal "ember island is a magical place, prince."
                    yd "...for hiding animals?"
                    lal "it is a place of self-discovery."
                    yd "you're no fun."
                    lal "correct, prince."
                    yd "bah. i'll be back later."
                    jump emberday

                if twins_encounter ==1:
                    scene bg_a_island_hutday
                    show twins_0
                    with Dissolve(0.8)
                    lal "there is much for you to discover, prince."
                    menu:
                        "outside":
                            jump ember_shack_day1

                if twins_encounter ==3:
                    scene bg_a_island_hutday
                    show twins_0
                    with Dissolve(0.8)
                    yd "huh, i wonder where those two got to..."
                    jump ember_shack_day1
            "dock":

                scene emberisland_dock with dissolve
                yd "......where did our boat go?"
                yd "are we really just abandoned here?"
                ya "because i will eat people if i have to."
                yd "...balls."
                jump ember_shack_day1
            "back to island":

                jump emberday

    if ember ==2:
        menu:
            "shack":
                scene bg_a_island_hutday
                with dissolve
                yd "hmm... nothing in this room..."
                jump inside_flower_menu

                label inside_flower_menu:
                    scene black
                    scene bg_a_island_hutday
                    with dissolve
                    menu:
                        "check azula & mai's room":
                            scene bg_a_2beds with dissolve
                            yd "nothing here."
                            jump inside_flower_menu
                        "check ty lee's room":

                            scene bg_a_island_1bed with dissolve
                            yd "doesn't seem to be a flower here."
                            jump inside_flower_menu
                        "outside":

                            jump ember_shack_day1
            "dock":

                scene emberisland_dock with dissolve
                yd "bummer. no flower here."
                jump ember_shack_day1
            "back to island":

                jump emberday
    else:

        y "hmm.... nothing here right now."
        jump emberday






label ember_beach_night1:
    if ember == 5:
        jump ember_first_night
    else:
        scene black
        scene bg_a_beach_01
        show blackveil
        with dissolve
        y "there's nothing here right now...."
        jump embernight

label ember_party_night1:
    menu:
        "house path":
            show fireguard_halberd with dissolve
            g "this is a private residence."
            g "unless you have an invitation, please return the way you came."
            hide fireguard_halberd with dissolve
            jump ember_party_night1
        "forest path":


            scene black
            scene bg_emberisland_wood_night
            with dissolve


            "you wade into the forest."
            yc "why am i here at night?"
            yc "this is the worst thing."
            yc "......"
            ya "fuck you, malaria!"
            jump ember_party_night1
        "back to island":

            jump embernight

label ember_shop_night1:
    scene black
    scene bg_emberisland_ghosthouse_night
    with dissolve
    yd "okay, there's definitely someone in there."
    y "...this feels like the beginning of a story that starts with \"i was curious\" and ends with \"my butthole hasn't been the same since.\""
    yd "i'm... gonna leave."
    jump embernight

label ember_water_night1:
    y "hmm... i'm gonna need a boat to go out there."
    jump embernight

label ember_shack_night1:
    scene black
    show emberisland_dock:
        ypos 0
    show blackveil
    with dissolve
    if ember ==6:
        y "it's really gotten late, it's so dark i can barely see where i'm walking."
        yd "this trip's starting to be more trouble than it's worth."
        menu:
            "shack":
                y "well... it's not like i'm going to sleep out here."
                y "better go in."
                jump after_first_fire
            "dock":

                scene black
                scene emberisland_dock
                show blackveil
                with dissolve
                if ember_wish:
                    y "there doesn't seem to be anything here right now."
                    jump ember_shack_night1
                else:
                    y "there seems to be a boat here."
                    y "interesting."
                    y "should i get in it?"
                    menu:
                        "get in boat":
                            $ ember_boat = True
                            jump embernight_boat1
                        "back":

                            jump ember_shack_night1
            "back to island":

                jump embernight
    else:


        menu:
            "shack":
                scene bg_a_island_hutnight
                with dissolve
                y "......"
                y "there doesn't seem to be anyone here right now."
                jump ember_shack_night1
            "dock":

                scene black
                scene emberisland_dock
                show blackveil
                with dissolve
                if ember_wish:
                    y "there doesn't seem to be anything here right now."
                    jump ember_shack_night1
                else:
                    y "there seems to be a boat here."
                    y "interesting."
                    y "should i get in it?"
                    menu:
                        "get in boat":
                            $ ember_boat = True
                            jump embernight_boat1
                        "back":

                            jump ember_shack_night1
            "back to island":

                jump embernight

label embernight_boat1:
    scene black
    scene bg_island_night
    with dissolve
    call screen emberisland_map_night_boat1

label ember_party_night_boat1:
    y "can't go here."
    y "i'm on a boat, motherfucker. don't you ever forget."
    jump embernight_boat1

label ember_shop_night_boat1:
    y "can't go here."
    y "i'm on a boat, motherfucker. don't you ever forget."
    jump embernight_boat1

label ember_beach_night_boat1:
    y "can't go here."
    y "i'm on a boat, motherfucker. don't you ever forget."
    jump embernight_boat1

label ember_shack_night_boat1:
    y "can't go here."
    y "i'm on a boat, motherfucker. don't you ever forget."
    jump embernight_boat1

label ember_water_night_boat1:

    scene bg_emberisland_sea_night
    show emberisland_boat:
        ypos 0
        linear 2.0 ypos 30
        ypos 30
        linear 2.0 ypos 0
        repeat
    ya "Where are you mermaids!?"
    ya "I just wanna see you nude!"
    ya "From the middle up!"
    "you hear a voice from the ocean beneath you."
    mv "speak, human."
    mv "what is your wish?"
    menu:
        "money":
            yd "i wanna know what the hell rappers are talking about."
            y "money, please."
            mv "money it is."
            $ fmoney +=500
            "you get 500 coins!"
            mv "goodbye..."
            $ ember_wish = True
            jump end_emberboat1
        "fish tits":

            y "sweet, sweet, fish titties."
            mv "...."
            mv "very well..."

            hide emberisland_boat
            show fishtits with dissolve:
                ypos 0
                linear 2.0 ypos 30
                ypos 30
                linear 2.0 ypos 0
                repeat

            mer "hello!"
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            mer "bye!"
            scene black with dissolve
            $ ember_wish = True
            jump end_emberboat1

            label end_emberboat1:
                "you take the boat back to shore."
                scene black
                scene emberisland_dock
                show blackveil
                with dissolve
                yd "that was weird."
                $ ember_boat = False
                jump embernight






label ember_party_day2:
    hide shadyguy_grin
    menu:
        "house path":
            if crab_tournament_invite:
                if shady_crab_start and not fishtits_crab_start and not lal_crab_start:
                    show fireguard_halberd with dissolve
                    g "go fight shady."
                    hide fireguard_halberd with dissolve
                    jump ember_party_day2

                if fishtits_crab_start or lal_crab_start:
                    show fireguard_halberd with dissolve
                    g "this is a private residence."
                    g "unless you have an invitation, please return the way you came."
                    hide fireguard_halberd with dissolve
                    jump ember_party_day2
                else:


                    show fireguard_halberd with dissolve
                    g "hey! you wanna battle crabs?"
                    menu:
                        "snip snap, bitch":
                            $ guard_crab = 1
                            $ remaining_enemy_crabs = 3
                            stop music fadeout 2
                            play music "audio/Blue Ska.mp3" fadein 2
                            jump guard_crab_battle
                        "no":

                            y "not right now."
                            g "okay, well i'm around."
                            hide fireguard_halberd with dissolve
                            jump ember_party_day2
            else:

                show fireguard_halberd with dissolve
                g "this is a private residence."
                g "unless you have an invitation, please return the way you came."
                hide fireguard_halberd with dissolve
                jump ember_party_day2
        "forest path":

            scene black
            scene bg_emberisland_wood
            with dissolve
            if ember ==8:
                ya "mai, if you're in here, i'm going to be so angry."
                ya "i'm not helping you get out of quicksand."
                ya "you put yourself in this situation!"
                yd "....mai?"
                ya "great, she's not even in here..."
                jump ember_party_day2
            else:

                "you wade into the forest."
                ya "god damn foliage!"
                ya "who put this here?"
                yd "...i think i just got a bug bite on my ass."
                ya "useless ass jungle!"
                ya "be a parking lot or leave!"
                jump ember_party_day2
        "back to island":

            jump emberday

label ember_shop_day2:
    scene bg_emberisland_ghosthouse with dissolve
    if ember ==8:
        show mai_idle_ff_beach with dissolve
        y "found you!"
        m "...oh, what?"
        yd "we were..... weren't we playing hide and seek?"
        m "no? i mean, maybe, but i just saw this building and...."
        yd "what about it?"
        m "it pretty clearly used to be a thriving business."
        yd "...it did?"
        jump hideandseek

    if ember >=9:
        y "seems pretty dilapidated."
        menu:
            "battle shady guy" if shady_crab_start and not fishtits_crab_start and not lal_crab_start:
                stop music fadeout 2
                play music "audio/Blue Ska.mp3" fadein 2
                jump shady_crab_battle

            "crab supplies" if crab_battles:
                show shadyguy_grin
                with dissolve
                sg "whatcha need?"
                yd "need to show crabs i'm no bitch."
                sg "i gotchu."
                menu:
                    "pockets - 100":
                        if fmoney >=100:
                            "buy an additional pocket for 100 coins?"
                            menu:
                                "buy":
                                    if shady_pockets >=1:
                                        $ crab_pockets +=1
                                        "you bought a pocket!"
                                        $ shady_pockets -=1
                                        jump ember_shop_day2
                                    if shady_pockets ==0:
                                        sg "sorry man, you bought all my pockets."
                                        sg "i used the rest on myself."
                                        jump ember_shop_day2
                                "don't buy":

                                    jump ember_shop_day2
                        else:
                            "not enough money."
                            jump ember_shop_day2
                    "potions - 100":

                        if fmoney >=100:
                            "buy a potion for 100 coins?"
                            menu:
                                "buy":
                                    if crab_potions <=2:
                                        $ crab_potions +=1
                                        "you bought a potion!"
                                        jump ember_shop_day2
                                    else:
                                        "you can't carry more than three crab potions!"
                                        jump ember_shop_day2
                                "don't buy":

                                    jump ember_shop_day2
                        else:
                            "not enough money."
                            jump ember_shop_day2
                    "back":
                        jump ember_shop_day2
            "back to island":


                jump emberday
    else:

        menu:
            "battle shady guy" if shady_crab_start and not fishtits_crab_start and not lal_crab_start:
                stop music fadeout 2
                play music "audio/Blue Ska.mp3" fadein 2
                jump shady_crab_battle

            "crab supplies" if crab_battles:
                show screen fshop
                show shadyguy_grin
                with dissolve
                sg "whatcha need?"
                yd "need to show crabs i'm no bitch."
                sg "i gotchu."
                menu:
                    "pockets - 100":
                        if fmoney >=100:
                            "buy an additional pocket for 100 coins?"
                            menu:
                                "buy":
                                    if shady_pockets >=1:
                                        $ crab_pockets +=1
                                        $ shady_pockets -=1
                                        "you bought a pocket!"
                                        jump ember_shop_day2
                                    if shady_pockets ==0:
                                        sg "sorry man, you bought all my pockets."
                                        sg "i used the rest on myself."
                                        jump ember_shop_day2
                                "don't buy":

                                    jump ember_shop_day2
                        else:
                            "not enough money."
                            jump ember_shop_day2
                    "potions - 100":

                        if fmoney >=100:
                            "buy a potion for 100 coins?"
                            menu:
                                "buy":
                                    if crab_potions <=2:
                                        $ crab_potions +=1
                                        "you bought a potion!"
                                        jump ember_shop_day2
                                    else:
                                        "you can't carry more than three crab potions!"
                                        jump ember_shop_day2
                                "don't buy":

                                    jump ember_shop_day2
                        else:
                            "not enough money."
                            jump ember_shop_day2
                    "back":
                        jump ember_shop_day2
            "back to island":


                hide screen fshop
                jump emberday

label ember_beach_day2:
    scene black
    scene bg_a_beach_01
    with dissolve
    if ember ==6:
        jump ember_second_day
    if ember ==7:
        jump beach_stroll
    if ember ==8:
        show azula_idle_ff_beach with dissolve
        y "have you seen mai?"
        a "maybe."
        yd "oh, come on. can't you just be helpful?"
        show a_idle_ff_face_unsure with dissolve
        a "i'm very helpful, zuko."
        a "maybe you should stop being mean."
        y "sorry. so, have you seen her?"
        hide a_idle_ff_face_unsure with dissolve
        a "maybe."
        ya "you're a jerk."
        a "yeah, yeah."
        a "no, i haven't seen her. maybe you bored her and she went home?"
        hide azula_idle_ff_beach with dissolve
        jump emberday
    if ember >=9:
        menu:
            "walk around beach":
                if not tylee_pre_party_meet:
                    scene black
                    scene bg_a_beach_02
                    show blue_20perc_transparent
                    show tylee_idle_ff_beach
                    with dissolve
                    y "oh. hey, ty lee."
                    t "hey, prince!"
                    t "...you look down. what's wrong?"
                    y "mai is..."
                    t "being mai?"
                    y "i guess. she's being oddly emotional."
                    t "she's a handful, that's for sure!"
                    y "is she... insecure?"
                    t "mai? i dont' know. maybe."
                    t "it's hard to tell with her... even for me! and i've known her forever!"
                    y "yeah, she's kind of closed off."
                    y "we're having a fight. any advice?"
                    t "you should talk to her."
                    y "i did that, it's why we're fighting."
                    t "oh... then i don't know. sorry."
                    t "hey! the party! we should head to the house and get ready!"
                    t "i'll see you there!"
                    $ tylee_pre_party_meet = True
                    jump ember_beach_day2
                else:
                    y "there's no one here..."
                    jump ember_beach_day2
            "crab battle free-for-all":

                show screen crabstats
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
                    "you face a legenday battling crab."
                    $ normal_crab = False
                    $ strong_crab = False
                    $ legend_crab = True
                    jump crab_battle_player
            "back to island":

                jump emberday

label ember_water_day2:
    if fishtits_crab_start:
        scene bg_emberisland_sea
        show emberisland_boat:
            ypos 0
            linear 2.0 ypos 30
            ypos 30
            linear 2.0 ypos 0
            repeat
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        y "hey! fishtits!"
        hide emberisland_boat
        show fishtits with dissolve:
            ypos 0
            linear 2.0 ypos 30
            ypos 30
            linear 2.0 ypos 0
            repeat

        mer "hello!"
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        mer "i can tell you're packing crabs."
        y "i am indeed, nipple-lady of the sea."
        ya "i'm gonna be the crab battle champ!"
        ya "best there ever was!"
        ya "my crabs are impossible to remove!"
        mer ".....i'm sorry to hear that."
        mer "but let's do it!"
        mer "i have to warn you though... i have access to all the crabs out there...."
        mer "this won't be easy."
        stop music fadeout 2
        play music "audio/Blue Ska.mp3" fadein 2
        jump fish_crab_battle
    else:

        y "hmm... i'm gonna need a boat to go out there."
        jump emberday

label ember_shack_day2:
    scene black
    show emberisland_dock:
        ypos 0
    with dissolve
    if ember ==8:
        menu:
            "shack":
                if twin_dance_scare:
                    scene bg_a_island_hutday
                    show twins_0
                    with dissolve
                    lal "hello, prince zuko."
                    lal "what can we do for you?"
                    yd "have you seen mai?"
                    lal "last we saw, she was going to the beach with the girls."
                    yd "hmm. thanks."
                    jump ember_shack_day2
                else:

                    scene bg_a_island_hutday
                    show twins_0
                    with dissolve
                    lal "hello, prince zuko."
                    lal "what can we do for you?"
                    yd "dunno. what can you do?"
                    lal "we can dance for you."
                    yc "........."
                    lal "we can also tell you that the girls are down at the beach."
                    yc ".........."
                    lal "are... you okay prince?"
                    yc "i wish i could control my amnesia."
                    yd "have you seen mai?"
                    lal "last we saw, she was going to the beach with the girls."
                    yd "hmm. thanks."
                    $ twin_dance_scare = True
                    jump ember_shack_day2
            "dock":

                scene black
                scene emberisland_dock
                with dissolve
                yd "nothing here..."
                jump ember_shack_day2
            "back to island":

                jump emberday

    if ember ==9:
        menu:
            "shack":
                jump ember_party_start
            "dock":

                scene black
                scene emberisland_dock
                with dissolve
                yd "nothing here..."
                jump ember_shack_day2
            "back to island":

                jump emberday
    else:



        menu:
            "shack":
                if twin_dance_scare:
                    scene bg_a_island_hutday
                    show twins_0
                    with dissolve
                    lal "hello, prince zuko."
                    lal "the girls are down at the beach."
                    y "thanks."
                    jump ember_shack_day2
                else:

                    scene bg_a_island_hutday
                    show twins_0
                    with dissolve
                    lal "hello, prince zuko."
                    lal "what can we do for you?"
                    yd "dunno. what can you do?"
                    lal "we can dance for you."
                    yc "........."
                    lal "we can also tell you where the girls are."
                    yc ".........."
                    lal "are... you okay prince?"
                    yc "i wish i could control my amnesia."
                    yd "where are the girls?"
                    lal "at the beach."
                    y "thanks."
                    y "i'll... be back later."
                    $ twin_dance_scare = True
                    jump ember_shack_day2
            "dock":

                scene black
                scene emberisland_dock
                with dissolve
                yd "nothing here..."
                jump ember_shack_day2
            "back to island":

                jump emberday







label ember_party_night2:
    menu:
        "house path":
            if ember ==11:
                yd "it's... probably a bad idea to go back there."
                jump embernight
            else:
                jump dusk_party
        "forest path":

            scene black
            scene bg_emberisland_wood_night
            with dissolve
            ya "most useless place on the whole damn island."
            jump ember_party_night2
        "back to island":

            jump embernight


label ember_shop_night2:
    scene black
    scene bg_emberisland_ghosthouse_night
    with dissolve
    y "nothing here right now...."
    menu:
        "back to island":
            jump embernight
label ember_beach_night2:
    scene black
    scene bg_a_beach_01
    show blackveil
    with dissolve
    y "nothing here right now....."
    menu:
        "back to island":
            jump embernight

label ember_water_night2:
    y "hmm... i'm gonna need a boat to go out there."
    jump embernight

label ember_shack_night2:
    scene black
    show emberisland_dock:
        ypos 0
    show blackveil
    with dissolve
    menu:
        "shack":
            if ember ==11:
                jump after_party_sleep
            else:

                scene bg_a_island_hutnight
                with dissolve
                y "......"
                y "there doesn't seem to be anyone here right now."
                jump ember_shack_night2
        "dock":

            scene black
            scene emberisland_dock
            show blackveil
            with dissolve
            if ember_wish2:
                y "there doesn't seem to be anything here right now."
                jump ember_shack_night2
            else:

                y "there seems to be a boat here."
                y "interesting."
                y "should i get in it?"
                menu:
                    "get in boat":
                        scene bg_emberisland_sea_night
                        show emberisland_boat:
                            ypos 0
                            linear 2.0 ypos 30
                            ypos 30
                            linear 2.0 ypos 0
                            repeat
                        "the boat drifts out to sea on it's own."
                        y "neat."
                        yd "Where are the mermaids!?"
                        ya "I just wanna see you nude!"
                        ya "From the middle up!"
                        "you hear a voice from the ocean beneath you."
                        mv "speak, human."
                        mv "what is your wish?"
                        menu:
                            "money":
                                yd "i wanna know what the hell rappers are talking about."
                                y "money, please."
                                mv "money it is."
                                $ fmoney +=500
                                "you get 500 coins!"
                                mv "goodbye..."
                                $ ember_wish2 = True
                                jump end_emberboat2
                            "fish tits":

                                y "sweet, sweet, fish titties."
                                mv "very well..."

                                hide emberisland_boat
                                show fishtits with dissolve:
                                    ypos 0
                                    linear 2.0 ypos 30
                                    ypos 30
                                    linear 2.0 ypos 0
                                    repeat

                                mer "hello!"
                                show ctcblink
                                $ renpy.pause()
                                hide ctcblink
                                mer "bye!"
                                scene black with dissolve
                                $ ember_wish2 = True
                                jump end_emberboat2

                                label end_emberboat2:
                                    "you take the boat back to shore."
                                    scene black
                                    scene emberisland_dock
                                    show blackveil
                                    with dissolve
                                    yd "that was weird."
                                    jump ember_shack_night2
                    "back":

                        jump ember_shack_night2
        "back to island":

            jump embernight





label ember_party_day3:
    menu:
        "house path":
            if azula_found_start and ember_azula_found:
                if crab_tournament_invite:
                    if shady_crab_start and not fishtits_crab_start and not lal_crab_start:
                        show fireguard_halberd with dissolve
                        g "go fight shady."
                        hide fireguard_halberd with dissolve
                        jump ember_party_day3

                    if fishtits_crab_start or lal_crab_start:
                        scene black
                        scene bg_a_island_partyhouse
                        with dissolve
                        y "there's nothing here..."
                        jump ember_party_day3
                    else:

                        show fireguard_halberd with dissolve
                        g "hey! you wanna battle crabs?"
                        menu:
                            "snip snap, bitch":
                                $ guard_crab = 1
                                $ remaining_enemy_crabs = 3
                                stop music fadeout 2
                                play music "audio/Blue Ska.mp3" fadein 2
                                jump guard_crab_battle
                            "no":

                                y "not right now."
                                g "okay, well i'm around."
                                hide fireguard_halberd with dissolve
                                jump ember_party_day3
                else:
                    scene black
                    scene bg_a_island_partyhouse
                    with dissolve
                    y "there's nothing here..."
                    jump ember_party_day3

            if azula_found_start and not ember_azula_found:
                jump mai_azula_training_caught
            else:

                $ azula_found_start = True
                scene black
                scene bg_a_island_partyhouse
                show azula_idle_fl_beach
                show a_idle_fl_face_unsure
                show a_idle_fl_face_blink
                with dissolve
                y "hey."
                show a_idle_fl_face_surprise
                with dissolve
                hide a_idle_fl_face_surprise
                hide a_idle_fl_face_blink
                hide a_idle_fl_face_unsure
                show a_idle_fl_face_anger
                with dissolve
                a "what is it?"
                yd "...what did i do?"
                show a_idle_fl_face_unsure
                hide a_idle_fl_face_anger
                with dissolve
                a "...nothing. you just surprised me, is all."
                yd "why is it so dark here?"
                hide a_idle_fl_face_unsure
                show a_idle_fl_face_anger
                with dissolve
                a "there's a cloud overhead. when did you become an idiot?"
                yd "...."
                y "what's going on?"
                hide a_idle_fl_face_anger
                show a_idle_fl_face_unsure
                with dissolve
                a "i was just..."
                show a_idle_fl_face_blink with dissolve
                a "looking at the house and remembering."
                hide a_idle_fl_face_blink with dissolve
                a "i'm sure we had good memories here, but... i can't seem to remember any."
                menu:
                    "comfort":
                        y "i'm sorry, a-cakes."
                    "shrug":

                        y "meh. it's really not a big deal."

                y "but we can make new memories."
                hide a_idle_fl_face_unsure
                show a_idle_fl_face_blink
                with dissolve
                a ".....with our own family....."
                yd "what?"
                show a_idle_fl_face_unsure
                hide a_idle_fl_face_blink
                with dissolve
                a "hmm? just mumbling."
                a "why don't you head on back to the beach?"
                a "i'll meet you by the chairs soon."
                y "alright."
                scene bg_island_day
                hide a_idle_fl_face_unsure
                hide azula_idle_fl_beach
                with dissolve
                yd "oh, wait."
                y "okay, i need azula actually train me."
                yd "i should head back and ask her about it."
                menu:
                    "return to azula":
                        jump mai_azula_training_caught
                    "head to the island":

                        jump emberday
        "forest path":

            scene black
            scene bg_emberisland_wood
            with dissolve
            if ember >=11:
                if not ember_tylee_found:
                    yd "okay, i'm going to be careful in here."
                    yd "I'm not going to get bit by bugs-"
                    ya "ow! shit!"
                    yc "i don't know what i'm even in here."
                    yd "there's never anyone in-"
                    show tylee_idle_ff_beach
                    show ty_idle_ff_annoyed
                    with dissolve
                    t "zuko!"
                    y "whoa... every time i say something, the opposite comes true."
                    yd ".............."
                    ya ".....i'm not going to plow azula's ass!"
                    yd "....she's not even here, i don't know why i bothered trying that."
                    yd "how about..."
                    ya "i'm not going to see ty lee's tits!"
                    t "zuko! stop messing around! it's an emergency!"
                    yd "what's up?"
                    t "look!"
                    "ty lee points deeper into the foliage and you see earth kingdom troops moving slowly through the underbrush."
                    yc "oh. fuck."
                    t "i'm going to go get some help. you stay here and keep an eye on them."
                    y "okay, go."
                    hide tylee_idle_ff_beach
                    hide ty_idle_ff_annoyed
                    with dissolve
                    ya "even on vacation these assholes follow me."
                    ya "this is why i can't have nice things."
                    "some time passes, but the earth kingdom troops don't make it far."
                    "they apparently don't like the forest either."
                    en1 "god damn jungle...."
                    en1 "why is this here?!"
                    en1 "fucking... bitch ass trees..."
                    en1 "you! you're the most bitchass tree of all!"
                    en1 "look at you! what are you, birch?"
                    en1 "ha! checkmate! that sounds like bitch!"
                    en1 "take this!"
                    play sound "audio/construction2.mp3"
                    with vshake
                    "he starts swinging his sword into the tree."
                    "it doesn't do much damage."
                    en2 "...we can earthbend, you know. why don't we just do that?"
                    en1 "we're {i}incognito{/i}, you twat."
                    en2 "is that why you're yelling?"
                    en1 "you don't know the first thing about warfare."
                    en2 "well you don't know the first things about fighting trees, apparently."
                    en1 "yeah, well, at least my mother isn't a slut!"
                    en2 "how would you know?"
                    en1 "what?"
                    en2 "how would you know she isn't a slut?"
                    en1 "well... i would know."
                    en2 "did she have lots of male guests over?"
                    en1 "well... yeah."
                    en2 "did she always have cash?"
                    en1 "........yes."
                    en2 "did you and she live on 69 mashbangers lane?"
                    en1 "............"
                    en2 "the one with the red door?"
                    en1 "........you asshole."
                    en2 "sorry, buddy."
                    en1 "you fucked my mom?!"
                    en1 "why?!"
                    en2 "i was young."
                    en1 "we're the same age!"
                    en2 "yeah, she basically kidnapped me."
                    en1 "oh, that's not cool either."
                    en2 "not really, no."
                    en1 "wow. i can't believe we only just discovered each other."
                    yd "i'm going to have to kill these guys."
                    yd "just so they stop talking."
                    show tylee_idle_ff_beach
                    show ty_idle_ff_annoyed
                    with dissolve
                    t "i brought help!"
                    ya "okay, we'll take this. you go warn the island."
                    hide tylee_idle_ff_beach
                    hide ty_idle_ff_annoyed
                    with dissolve
                    en1 "ow! i just got bitten!"
                    en1 "this jungle sucks so much ass!"
                    y "right?"
                    en2 "who's there?"
                    "his startled yell and the continued tree-wacking wake up a very angry python, who drops onto them...."
                    en1 "what the-"
                    en1 "aaaahhhhhhhhhhhh!!!!"
                    "One of the soldiers kicks a treetrunk."
                    show tylee_idle_ff_beach
                    show ty_idle_ff_annoyed
                    with dissolve
                    t "alright, i brought help!"
                    yd "i uh... don't think it'll be necessary any more."
                    t "why-"
                    hide ty_idle_ff_annoyed
                    show ty_idle_ff_surprised
                    with dissolve
                    t "oh."
                    y "yeah."
                    t "well... i guess it worked out."
                    hide ty_idle_ff_surprised
                    t "i'll meet you on the beach, zuko!"
                    $ ember_tylee_found = True
                    if ember_tylee_found and ember_azula_found:
                        $ ember = 12
                    jump emberday
                else:
                    y "nothing here...."
                    jump ember_party_day3
        "back to island":

            jump emberday

label ember_shop_day3:
    scene bg_emberisland_ghosthouse with dissolve
    menu:

        "battle shady guy" if shady_crab_start and not fishtits_crab_start and not lal_crab_start:
            stop music fadeout 2
            play music "audio/Blue Ska.mp3" fadein 2
            jump shady_crab_battle
        "blind man's bluff":

            $ blind_game = True
            jump blind_man_bluff_day3

        "crab supplies" if crab_battles:
            show shadyguy_grin
            with dissolve
            sg "whatcha need?"
            yd "need to show crabs i'm no bitch."
            sg "i gotchu."
            menu:
                "pockets - 100":
                    if fmoney >=100:
                        "buy an additional pocket for 100 coins?"
                        menu:
                            "buy":
                                if shady_pockets >=1:
                                    $ crab_pockets +=1
                                    "you bought a pocket!"
                                    $ shady_pockets -=1
                                    jump ember_shop_day2
                                if shady_pockets ==0:
                                    sg "sorry man, you bought all my pockets."
                                    sg "i used the rest on myself."
                                    jump ember_shop_day2
                            "don't buy":

                                jump ember_shop_day3
                    else:
                        "not enough money."
                        jump ember_shop_day3
                "potions - 100":

                    if fmoney >=100:
                        "buy a potion for 100 coins?"
                        menu:
                            "buy":
                                if crab_potions <=2:
                                    $ crab_potions +=1
                                    "you bought a potion!"
                                    jump ember_shop_day3
                                else:
                                    "you can't carry more than three crab potions!"
                                    jump ember_shop_day3
                            "don't buy":

                                jump ember_shop_day3
                    else:
                        "not enough money."
                        jump ember_shop_day3
                "back":
                    jump ember_shop_day3
        "back to island":


            jump emberday

label ember_beach_day3:

    scene black
    scene bg_a_beach_01
    with dissolve
    if ember ==14:
        if heavy_box_given:
            jump truth_or_dare
        else:
            y "i need to get that box from the shack."
            jump emberday

    if ember >=11 and ember <=13:
        menu:


            "visit the girls" if ember ==11:
                if ember_azula_found and not ember_tylee_found:
                    show asun asun32 with dissolve
                    a "hello, zuko."
                    a "i wonder where ty lee is?"
                    a "probably lost somewhere."
                    a "go find her for me, would you?"
                    yd "......fine."
                    a "good."
                    jump ember_beach_day3

                if ember_tylee_found and not ember_azula_found:
                    show asun asun31 with dissolve
                    t "hey, prince!"
                    t "i'm worried about azula."
                    yd "...."
                    yd "alright, i'll go find her."
                    jump ember_beach_day3
                else:


                    scene bg_a_beach_chairs with dissolve
                    y "hmmm.... we were supposed to meet here."
                    yd "i know mai's back at the shack."
                    y "i hope azula and ty lee are okay..."
                    yd "*sigh...* i should go find them and make sure."
                    jump ember_beach_day3

            "visit the girls" if ember ==13:
                if nude_sunbathing:
                    show asun asun03 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ys "hey."
                    show asun asun03_1 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "hello, zuko."
                    a "oh, right. tan lines."
                    show asun asun04 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "*mmmmm...*"
                    a "that's nice..."
                    show asun asun101_1
                    show asun_azulablink
                    with dissolve
                    a "oh, feel that breeze....."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    hide asun_azulablink with dissolve
                    a "alright, zuko. go on."
                    a "you can come back later."
                    jump ember_beach_day3
                else:


                    show asun asun03 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ys "whoa."
                    ys "nice."
                    show asun asun03_1 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "hello, zuko."
                    ys "so, uh, what's going on here?"
                    t "we were convinced to tan naked!"
                    m "no tan lines."
                    y "well, i kind of like tan lines..."
                    ys "but i have no problem with this."
                    yd "i have to say though, aren't you worried about tan lines on your inner thigh?"
                    m "...what?"
                    yd "with your legs' crossed like that."
                    a "hmm... you're right, zuko."
                    a "thank you."
                    show asun asun04 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    "As Azula spreads her legs unashamedly, Ty lee happily follows suit."
                    "Mai, looking flustered, surprised, and angry for a split second, hurriedly copies the other two girls."
                    "You feel a lot like they're playing \"chicken\"."
                    a "*mmmmm...*"
                    m "i don't know what i was complaining about...."
                    t "right?! this weather is perfect..."
                    show asun asun101_1
                    show asun_azulablink
                    show asun_tyleeblink
                    with dissolve
                    a "oh, feel that breeze....."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    m "it's so hot, i've got sweat rolling down to my cunt..."
                    m "...do you need something, zuko?"
                    yd "uhhh...."
                    t "yeah, he needs some pussy!"
                    t "you two are terrible!"
                    a "....."
                    m "....."
                    m "what is it that you know, ty lee?"
                    t "that the weather is nice."
                    a "hmm."
                    hide asun_azulablink with dissolve
                    a "alright, zuko. go on."
                    a "you can come back later."
                    $ nude_sunbathing = True
                    jump ember_beach_day3

            "visit the girls" if ember ==12:
                if volleybutt_start:
                    if volleybutt >=3:
                        show asun asun29
                        hide asun_azulablink
                        with dissolve
                        a "well {i}done{/i}, brother."
                        a "that got me... worked up."
                        a "ty lee. go for a swim."
                        t "okay!"
                        show asun asun30 with dissolve
                        a "you want another assjob, don't you, zuko?"
                        a "i'm surprised you did all that."
                        a "what's the matter, big brother?"
                        a "can't stay away from your little sister's tight asscheeks?"
                        a "i know, i have a perfect ass."
                        a "come, i'll let you put it right between my cheeks and you can hump it out."
                        jump abeachrub3
                    else:

                        show asun asun28
                        show asun_azulablink
                        with dissolve
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        t "hey, prince!"
                        a "zuko, go win three matches of that ball game, and i'll keep you busy like i did yesterday."
                        a "otherwise, let us tan."
                        jump ember_beach_day3
                else:

                    show asun asun28
                    show asun_azulablink
                    with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    t "hey, prince!"
                    t "having fun?"
                    menu:
                        "yeah":
                            y "i'm enjoying myself."
                            t "that's great!"
                            t "there's plenty of stuff around."
                        "anything to do?":

                            y "i'm looking for stuff to do."
                            t "what do you mean?"
                            t "we're on an island vacation! there's lots to do!"


                    t "by the way, where's mai?"
                    y "i think she decided to stay inside, at least for now."
                    t "I hope she comes out soon..."
                    show asun asun29
                    hide asun_azulablink
                    with dissolve
                    a "i've got something for you to do."
                    yd "what?"
                    a "i enjoy watching that ball game."
                    yd "volleyball?"
                    a "yes. i like watching you - i mean, those boys - play."
                    a "maybe... win three or so rounds and I'll... keep you busy like i did yesterday."
                    $ volleybutt_start = True
                    y "sure, i can do that."
                    a "very well, we're agreed. now get to it."
                    jump ember_beach_day3
            "volleyball":

                jump volleyball
            "crab battling!":

                $ crabble_royal = True
                show screen crabstats
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
                    "you face a legenday battling crab."
                    $ normal_crab = False
                    $ strong_crab = False
                    $ legend_crab = True
                    jump crab_battle_player
            "back to island":

                jump emberday

label ember_water_day3:
    if fishtits_crab_start:
        scene bg_emberisland_sea
        show emberisland_boat:
            ypos 0
            linear 2.0 ypos 30
            ypos 30
            linear 2.0 ypos 0
            repeat
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        y "hey! fishtits!"
        hide emberisland_boat
        show fishtits with dissolve:
            ypos 0
            linear 2.0 ypos 30
            ypos 30
            linear 2.0 ypos 0
            repeat

        mer "hello!"
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        mer "i can tell you're packing crabs."
        y "i am indeed, nipple-lady of the sea."
        ya "i'm gonna be the crab battle champ!"
        ya "best there ever was!"
        ya "my crabs are impossible to remove!"
        mer ".....i'm sorry to hear that."
        mer "but let's do it!"
        mer "i have to warn you though... i have access to all the crabs out there...."
        mer "this won't be easy."
        stop music fadeout 2
        play music "audio/Blue Ska.mp3" fadein 2
        jump fish_crab_battle
    else:

        y "hmm... i'm gonna need a boat to go out there."
        jump emberday

label ember_shack_day3:
    scene black
    show emberisland_dock:
        ypos 0
    with dissolve
    menu:
        "shack":
            if ember ==14:
                if heavy_box_given:
                    y "there's nothing going on here..."
                    jump ember_shack_day3
                else:

                    scene bg_a_island_hutday
                    show twins_0
                    with dissolve
                    lal "can we help you, prince zuko?"
                    yd "yeah, i'm looking for a heavy box. clinks a bit."
                    lal "ah, you are getting up to trouble."
                    lal "very well, it's here."
                    "they hand you the box."
                    ya "fuck! i forgot how heavy this was..."
                    $ heavy_box_given = True
                    jump ember_shack_day3
            else:

                if lal_crab_start and not lal_crab_win:
                    scene black
                    scene bg_a_island_hutday
                    show twins_0
                    with dissolve
                    lal "hello, prince zuko."
                    lal "what can we do for you?"
                    menu:
                        "i want your crabs in my face!":
                            ya "give me your crabs!"
                            lal "what?"
                            y "i'mma pinch you, girl."
                            lal "are you trying to crab battle us?"
                            y "obviously."
                            lal "you have no idea what you're in for, zuko."
                            lal "we're the best around."
                            lal "nothing's ever gonna keep us down."
                            yd "...what?"
                            lal "only iroh, the grandsnipper, has beaten us."
                            yd "grandsnipper?"
                            lal "you heard us! now... whip it out!"
                            lal "and your crabs!"
                            yd "...."
                            ya "let's go!"
                            stop music fadeout 2
                            play music "audio/Blue Ska.mp3" fadein 2
                            jump lal_crab_battle
                        "nothing, nevermind, no std puns here":

                            yd "nevermind."
                            jump ember_shack_day3
                else:

                    y "there's nothing going on here..."
                    jump ember_shack_day3
        "dock":

            scene black
            scene emberisland_dock
            with dissolve
            yd "nothing here..."
            jump ember_shack_day3
        "back to island":

            jump emberday






label ember_party_night3:
    menu:
        "house path":

            scene black
            scene bg_a_island_partyhouse
            with dissolve
            y "there's nothing here..."
            jump ember_party_night3
        "forest path":

            scene black
            scene bg_emberisland_wood_night
            with dissolve
            y "there's nothing here..."
            jump ember_party_night3
        "back to island":

            jump embernight


label ember_shop_night3:
    scene black
    scene bg_emberisland_ghosthouse_night
    with dissolve
    y "nothing here right now...."
    menu:
        "back to island":
            jump embernight

label ember_beach_night3:
    scene black
    scene bg_a_beach_01
    show blackveil
    with dissolve
    if dolphin_sex:
        y "there's nothing here..."
        menu:
            "back to island":
                jump embernight
    else:

        show tylee_idle_ff_beach with dissolve
        t "hey, zuko."
        y "what's up, ty. why are you out here?"
        t "just enjoying a night-time swim."
        t "plus i hear that dolphins love sex, and-"
        yd "stop. stop right there. i want to know zero more information."
        y "where are the girls?"
        t "don't know, but they're not here at the beach."
        y "alright, thanks."
        yd "and... be safe."
        t "eeeeaeehyyeaeey."
        t "that's dolphin for \"pork me daddy\"."
        ya "{size=+4}i wanted zero more information!"
        hide tylee_idle_ff_beach with dissolve
        $ dolphin_sex = True

        menu:
            "back to island":
                jump embernight

label ember_water_night3:
    y "hmm... i'm gonna need a boat to go out there."
    jump embernight


label ember_shack_night3:
    scene black
    show emberisland_dock:
        ypos 0
    show blackveil
    with dissolve
    menu:
        "shack":
            if ember ==15:
                if azula_too_bad:
                    menu:
                        "go to bed":
                            scene black
                            scene bg_a_farm_singlegirl
                            show blackveil
                            with dissolve
                            "you lay on your pile of fucking hay. congratulations. this is you in your prime."
                            "you're peaking."
                            "on your fucking hay."

                            if mai_flower_got == False and not_interested_mai and ember_deed == False:
                                "you've blown all your chances of having sex with Mai so far."
                            elif ember_deed:
                                "Mai has stopped having sex with you."
                            else:
                                "your girlfriend stopped having sex with you."

                            "and your sister is evil, horny, and fucked up."
                            "no wonder you can't sleep."
                            ya "fuck this."
                            menu:
                                "mai and azula's room":
                                    jump sleepy_azula_anal
                                "ty lee's room":

                                    scene black
                                    show azst azst04
                                    show blackveil
                                    with dissolve
                                    "{i}zzzt! zzzt! zzzt!"
                                    show ctcblink
                                    $ renpy.pause()
                                    hide ctcblink
                                    y "aw, that's adorable."
                                    "the toy continues to vibrate and move in her pussy, clearly keeping her asleep."
                                    show ctcblink
                                    $ renpy.pause()
                                    hide ctcblink
                                    menu:
                                        "mai and azula's room":
                                            jump sleepy_azula_anal
                        "outside":


                            jump ember_shack_night3
                else:

                    scene black
                    scene bg_a_island_hutnight
                    show azula_idle_fl_beach
                    with dissolve
                    yd "hey, where's mai? i want to talk to her."
                    a "no... she's gone to bed, i'm afraid."
                    show a_idle_fl_face_blink with dissolve
                    a "not that it will make a difference... she's not interested in sleeping with you."
                    ya "...you're confusing her and fucking up our relationship! why?"
                    hide a_idle_fl_face_blink with dissolve
                    a "i have my reasons, brother."
                    a "but it's simply too bad that she's in that room right there, with me, and you can't even visit her to get off."
                    show a_idle_fl_face_blink with dissolve
                    a "i wish you had another option, but oh well...."
                    hide a_idle_fl_face_blink with dissolve
                    a "goodnight, brother. sweet dreams...."
                    hide azula_idle_fl_beach with dissolve
                    $ azula_too_bad = True
                    menu:
                        "go to bed":
                            scene black
                            scene bg_a_farm_singlegirl
                            show blackveil
                            with dissolve
                            "you lay on your pile of fucking hay. congratulations. this is you in your prime."
                            "you're peaking."
                            "on your fucking hay."

                            if mai_flower_got == False and not_interested_mai and ember_deed == False:
                                "you've blown all your chances of having sex with Mai so far."
                            elif ember_deed:
                                "Mai has stopped having sex with you."
                            else:
                                "your girlfriend stopped having sex with you."

                            "and your sister is evil, horny, and fucked up."
                            "no wonder you can't sleep."
                            ya "fuck this."
                            menu:
                                "mai and azula's room":
                                    jump sleepy_azula_anal
                                "ty lee's room":

                                    scene black
                                    show azst azst04
                                    show blackveil
                                    with dissolve
                                    "{i}zzzt! zzzt! zzzt!"
                                    show ctcblink
                                    $ renpy.pause()
                                    hide ctcblink
                                    y "aw, that's adorable."
                                    "the toy continues to vibrate and move in her pussy, clearly keeping her asleep."
                                    show ctcblink
                                    $ renpy.pause()
                                    hide ctcblink
                                    menu:
                                        "mai and azula's room":
                                            jump sleepy_azula_anal
                        "outside":


                            jump ember_shack_night3
            else:

                scene bg_a_island_hutnight
                with dissolve
                y "......"
                yd "where is everyone?"
                y "ty lee does her own thing, but i usually know where mai and azula are..."
                y "i should see if i can find them. make sure they're okay."
                jump ember_shack_night3
        "dock":

            if ember >=15:
                scene black
                scene emberisland_dock
                show blackveil
                with dissolve
                y "there's nothing here..."
                jump ember_shack_night3
            else:

                scene black
                scene emberisland_dock
                show blackveil
                show azula_idle_fl_beach
                show mai_fl_flip
                with dissolve
                "you once again catch mai and azula speaking. you decide to be stealthy this time and listen in."
                jump secret_mai_azula_talk
        "back to island":


            jump embernight





label ember_party_day4:
    menu:
        "house path":
            scene black
            scene bg_a_island_partyhouse
            with dissolve
            y "there's nothing here..."
            jump ember_party_day4
        "forest path":

            scene black
            scene bg_emberisland_wood
            with dissolve
            y "nothing here...."
            jump ember_party_day4
        "back to island":

            jump emberday


label ember_shop_day4:
    scene bg_emberisland_ghosthouse with dissolve
    menu:
        "blind man's bluff":
            $ blind_game = True
            jump blind_man_bluff_day3

        "crab supplies" if crab_battles:
            show shadyguy_grin
            with dissolve
            sg "whatcha need?"
            yd "need to show crabs i'm no bitch."
            sg "i gotchu."
            menu:
                "pockets - 100":
                    if fmoney >=100:
                        "buy an additional pocket for 100 coins?"
                        menu:
                            "buy":
                                if shady_pockets >=1:
                                    $ crab_pockets +=1
                                    "you bought a pocket!"
                                    $ shady_pockets -=1
                                    jump ember_shop_day2
                                if shady_pockets ==0:
                                    sg "sorry man, you bought all my pockets."
                                    sg "i used the rest on myself."
                                    jump ember_shop_day2
                            "don't buy":

                                jump ember_shop_day4
                    else:
                        "not enough money."
                        jump ember_shop_day4
                "potions - 100":

                    if fmoney >=100:
                        "buy a potion for 100 coins?"
                        menu:
                            "buy":
                                if crab_potions <=2:
                                    $ crab_potions +=1
                                    "you bought a potion!"
                                    jump ember_shop_day4
                                else:
                                    "you can't carry more than three crab potions!"
                                    jump ember_shop_day4
                            "don't buy":

                                jump ember_shop_day4
                    else:
                        "not enough money."
                        jump ember_shop_day4
                "back":
                    jump ember_shop_day4
        "back to island":


            jump emberday

label ember_beach_day4:
    scene black
    scene bg_a_beach_01
    with dissolve
    menu:
        "walk around beach":

            if azula_angry:
                $ ember = 16
                y "there's no one here..."
                jump ember_beach_day4

            if ember ==16:
                y "there's no one here..."
                jump ember_beach_day4
            else:

                show asun asun30 with dissolve
                a "you look so glum, zuzu."
                ya "why did you do that?"
                a "do what?"
                ya "you... you told mai! she's furious!"
                a "i decided to stop playing that game."
                ya "you started this!"
                a "oh, you and i aren't finished."
                a "but you and mai... well, that's not up to me."
                a "hold on, i'll get up."
                jump ember_azula_talk_day4
        "crab battling!":




            $ crabble_royal = True
            show screen crabstats
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
                "you face a legenday battling crab."
                $ normal_crab = False
                $ strong_crab = False
                $ legend_crab = True
                jump crab_battle_player
        "back to island":

            jump emberday

label ember_water_day4:
    y "hmm... i'm gonna need a boat to go out there."
    jump emberday

label ember_shack_day4:
    scene black
    show emberisland_dock:
        ypos 0
    with dissolve
    menu:
        "shack":
            scene bg_a_island_hutday
            with dissolve

            if ember ==16:
                if ember_ship_ready:
                    y "they're all down at the dock..."
                    jump ember_shack_day4
                else:

                    show mai_fl_flip:
                        xpos 100
                    show tylee_idle_ff_beach:
                        xpos -250
                    show azula_idle_fl_beach
                    with dissolve

                    a "good we're all here."
                    t "this was fun!"
                    t "...why is everyone so gloomy?"
                    t "......."
                    t "fine."
                    if masturbate_in_closet:
                        with sshake
                        lal "ah!"
                        lal "who jizzed on our coats?!"
                        "the girls all look at you."
                        yd "what?"
                        a "when... did you even have time for that?"
                        yd "i keep busy."

                    m "...let's just meet on the ship."
                    a "good idea."
                    $ ember_ship_ready = True
                    jump ember_shack_day4

            if ember_treasure_found:
                y "there's nothing here..."
                jump ember_shack_day4

            if ember_treasure_start and not ember_treasure_found:
                if not friddle4:
                    y "there's nothing here..."
                    jump ember_shack_day4

                if friddle4:
                    menu:
                        "azula & mai's room":
                            scene bg_a_2beds with dissolve
                            yd "nothing here."
                            menu:
                                "ty lee's room":
                                    scene bg_a_island_1bed with dissolve
                                    yd "doesn't seem to be anything here."
                                    menu:
                                        "your room":
                                            scene black
                                            scene bg_a_farm_singlegirl
                                            with dissolve
                                            jump find_ember_treasure
                                        "outside":

                                            jump ember_shack_day4
                                "your room":

                                    scene black
                                    scene bg_a_farm_singlegirl
                                    with dissolve
                                    jump find_ember_treasure
                                "outside":

                                    jump ember_shack_day4
                        "ty lee's room":

                            scene bg_a_island_1bed with dissolve
                            yd "doesn't seem to be a flower here."
                            menu:
                                "azula & mai's room":
                                    scene bg_a_2beds with dissolve
                                    yd "nothing here."
                                    menu:
                                        "your room":
                                            scene black
                                            scene bg_a_farm_singlegirl
                                            with dissolve
                                            jump find_ember_treasure
                                        "outside":

                                            jump ember_shack_day4
                                "your room":


                                    scene black
                                    scene bg_a_farm_singlegirl
                                    with dissolve
                                    jump find_ember_treasure
                                "outside":

                                    jump ember_shack_day4
                        "your room":

                            scene black
                            scene bg_a_farm_singlegirl
                            with dissolve
                            jump find_ember_treasure
                        "outside":

                            jump ember_shack_day4
            else:


                scene bg_a_island_hutday
                show twins_0
                with dissolve
                lal "can we help you, prince zuko?"
                yd "any experience trying to get someone to forgive you for fucking your sister?"
                lal "......"
                lal "yes."
                lal "a lot."
                yd "wait. i take it back, don't-"
                lal "the other day-"
                yd "\"the other day\"?"
                yd "i wasn't prepared for you to talk about 20 years ago, i am definitely not prepared for current events."
                lal "....."
                lal "patience and effort. perseverence is the only route to success."
                y "...thanks."
                y "i know i've been a bit of a jerk, but you two are alright."
                lal "well, if you really want to make it up to us, how about we all-"
                y "never. never ever."
                $ ember_treasure_start = True
                if friddle4:
                    lal "very well."
                    lal "oh, by the way, we found a number of azulon's heirlooms in your room."
                    lal "do they have a purpose, or may we keep them?"
                    y "i guess you can keep them. i couldn't figure out the treasure."
                    lal "treasure?"
                    y "yeah, the- alright, hold on."
                    "you go find the items and read their clues."
                    y "the clues are: \"rest\", \"twin\", \"flames\", and \"where\"?"
                    lal "what could that mean?"
                    menu:
                        "twin flames rest where":
                            yd "twin flames rest where?"
                            yd "that doesn't sound right."
                            lal "may we suggest: \"where twin flames rest\"?"
                            yd "huh. that sounds right."
                            yd "wonder what it means?"
                            lal "speaking of rest, how are you enjoying your room?"
                            yd "...enjoying?"
                            yd "i'm sleeping on fucking hay."
                            yd "i'm not \"enjoying\"."
                            lal "that's too bad, that used to be our room when we waited on azulon."
                            lal "lot of good memories there..."
                            lal "well, let us know if there's anything we can do for you."
                            lal "we hope you find your treasure."
                            jump ember_shack_day4
                        "flames twin where rest":


                            yd "flames twin where rest?"
                            yd "that doesn't sound right."
                            lal "may we suggest: \"where twin flames rest\"?"
                            yd "huh. that sounds right."
                            yd "wonder what it means?"
                            lal "speaking of rest, how are you enjoying your room?"
                            yd "...enjoying?"
                            yd "i'm sleeping on fucking hay."
                            yd "i'm not \"enjoying\"."
                            lal "that's too bad, that used to be our room when we waited on azulon."
                            lal "lot of good memories there..."
                            lal "well, let us know if there's anything we can do for you."
                            lal "we hope you find your treasure."
                            jump ember_shack_day4
                        "rest flames where twin":


                            yd "flames twin where rest?"
                            yd "that doesn't sound right."
                            lal "may we suggest: \"where twin flames rest\"?"
                            yd "huh. that sounds right."
                            yd "wonder what it means?"
                            lal "speaking of rest, how are you enjoying your room?"
                            yd "...enjoying?"
                            yd "i'm sleeping on fucking hay."
                            yd "i'm not \"enjoying\"."
                            lal "that's too bad, that used to be our room when we waited on azulon."
                            lal "lot of good memories there..."
                            lal "well, let us know if there's anything we can do for you."
                            lal "we hope you find your treasure."
                            jump ember_shack_day4
                        "where twin flames rest":

                            yd "\"where twin flames rest\"?"
                            yd "that sounds right."
                            yd "wonder what it means?"
                            lal "speaking of rest, how are you enjoying your room?"
                            yd "...enjoying?"
                            yd "i'm sleeping on fucking hay."
                            yd "i'm not \"enjoying\"."
                            lal "that's too bad, that used to be our room when we waited on azulon."
                            lal "lot of good memories there..."
                            lal "well, let us know if there's anything we can do for you."
                            lal "we hope you find your treasure."
                            jump ember_shack_day4
                else:
                    lal "oh, well."
                    jump ember_shack_day4
        "dock":

            if leave_mai_alone:
                if ember_ship_ready:
                    "you're getting ready to leave ember island."
                    "continue?"
                    menu:
                        "leave ember island":
                            $ firebending = 8
                            scene black
                            scene emberisland_dock
                            show mai_fl_flip:
                                xpos 100
                            show tylee_idle_ff_beach:
                                xpos -250
                            show azula_idle_fl_beach
                            with dissolve
                            t "bye bye, ember island!"
                            t "thanks for the fun!"
                            "the ship arrives and you board it."
                            scene black with dissolve
                            "you travel back to the fire nation, your ember island adventures weighing heavily on your mind."
                            if billy_mays:
                                gobm "{size=+8}{i}{b}\"right now, if you buy three-"
                                y "*sigh...* not the time, billy."
                            "eventually, you arrive back in the city."
                            scene bg_a_city_day
                            if azula_angry:
                                show ad with dissolve
                                a "well wasn't that a {i}fun{/i} trip for everyone?"
                                y "azula-"
                                hide ad with dissolve
                                y "*sigh* i'm gonna have to fix this."
                            else:

                                show a_blink
                                with dissolve
                                a "well, that was a fun trip."
                                a "i'll see you back at the palace later, zuko."
                                hide a_blink with dissolve

                            show tf with dissolve
                            t "thanks for a great trip, prince!"
                            t "let's do it again, sometime!"
                            hide tf with dissolve
                            if azula_angry:
                                show mf with dissolve
                                m "thanks for a great trip, zuko."
                                m "stop by some time!"
                                hide mf with dissolve
                            else:

                                show mf with dissolve
                                m "..........."
                                m "if i have to serve you at my shop, i will."
                                m "but our relationship is formal from here on out."
                                y "wait-"
                                hide mf with dissolve
                                yd "*sigh*"
                                yd "back to the city."

                            jump zcity1
                        "go back":

                            jump ember_shack_day4
                else:


                    scene black
                    scene emberisland_dock
                    show mai_idle_fl_beach
                    with dissolve
                    y "she won't talk to me."
                    jump ember_shack_day4
            else:

                if azula_angry:
                    scene black
                    scene emberisland_dock
                    show mai_idle_fl_beach
                    with dissolve
                    y "hey, you okay?"
                    m "yeah, i'm just... trying to make sense of this."
                    y "look, i just want to be with you."
                    y "that's all that matters to me."
                    m "....."
                    m "you really mean that, don't you?"
                    y "yeah."
                    m "don't worry, i.... forgive you."
                    m "but azula is another story."
                    m "just... let me think for a while."
                    $ leave_mai_alone = True
                    jump ember_shack_day4
                else:

                    scene black
                    scene emberisland_dock
                    show mai_idle_fl_beach
                    with dissolve
                    y "hey."
                    m "......."
                    y "talk to me."
                    m "........"
                    y "if you're secretly a dude, don't say anything."
                    m "........."
                    yd "i thought for sure that'd work..."
                    y "look, i don't know what i'm doing here."
                    y "in this situation."
                    y "i'm in chaos, just like you are."
                    m ".........."
                    yd "though, admittedly, of the two of us, i'm the only one fucking his sister."
                    m "........."
                    yd "right, i don't need to remind you."
                    y "i actually like this. it's like therapy."
                    y "i feel like my parents never really-"
                    m "leave me alone, zuko."
                    yd "but-"
                    m "leave me alone."
                    yd "...."
                    yd "fine."
                    $ leave_mai_alone = True
                    jump ember_shack_day4
        "back to island":

            jump emberday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
