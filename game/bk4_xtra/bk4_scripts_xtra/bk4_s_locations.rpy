screen b4_screen_repcity1:

    imagemap:

        ground "bk4/world_maps/republic_city.jpg"
        hover "bk4/world_maps/republic_city_hover.png"
        idle "bk4/world_maps/republic_city_idle.png"

        add "airtemple_cloud1"



        hotspot (298, 104, 230, 176) action [ Jump("bk4_police")]
        hotspot (543, 113, 295, 174) action [ Jump("bk4_alleys")]

        hotspot (746, 361, 253, 174) action [ Jump("b4_airtemple_map1")]

        hotspot (42, 295, 370, 114) action [ Jump("bk4_park")]
        hotspot (47, 513, 266, 127) action [ Jump("bk4_statue")]

    if bk4_calendar >=2:
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[bk4_money]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[bk4_calendar]"

    if probending_available ==2 and probending_time <7:
        add "misc/star1.png":
            xalign 0.75 yalign 0.0
    if probending_available ==2 and probending_time >=7:
        imagebutton idle "misc/star2.png" hover "bk4_xtra/remove/star3.png" xalign 0.75 yalign 0.0 action Jump("bk4_probending") focus_mask True



screen b4_screen_airtemple1:

    imagemap:

        if b4_daytime:
            ground "bk4/world_maps/airtemple_day.jpg"
        else:
            ground "bk4/world_maps/airtemple_night.jpg"

        hover "bk4/world_maps/airtemple_island_hover.png"
        idle "bk4/world_maps/airtemple_island_idle.png"

        add "airtemple_cloud1"




        hotspot (0, 390, 286, 158) action [ Jump("bk4_your_room")]
        if korra_jail:
            hotspot (71, 187, 444, 175) action [ Jump("bk4_korra_room")]

        hotspot (738, 64, 260, 110) action [ Jump("bk4_tower")]

        hotspot (752, 448, 247, 111) action [ Jump("bk4_train")]
        if b4_daytime:
            hotspot (505, 589, 386, 113) action [ Jump("bk4_docks")]
        if not b4_daytime:
            hotspot (505, 589, 386, 113) action [ Jump("bk4_docks_night")]
        hotspot (310, 87, 325, 82) action [ Jump("bk4_meditation")]

    if bk4_calendar >=2:
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[bk4_money]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[bk4_calendar]"

    if probending_available ==2 and probending_time <7:
        add "misc/star1.png":
            xalign 0.75 yalign 0.0
    if probending_available ==2 and probending_time >=7:
        imagebutton idle "misc/star2.png" hover "bk4_xtra/remove/star3.png" xalign 0.75 yalign 0.0 action Jump("bk4_probending") focus_mask True


label b4_airtemple_map1:
    scene black

    if b4_daytime:
        if not b4_music_day_on:
            $ b4_music_day_on = True
            $ b4_music_night_on = False
            stop music fadeout 1
            play music "audio/bounce_town.mp3"

        scene villagemap_day_base
        scene expression "bk4/world_maps/airtemple_day.jpg"
        if bk4_calendar >=2:
            show screen bk4_money_date
        with dissolve
    else:
        if not b4_music_night_on:
            $ b4_music_night_on = True
            $ b4_music_day_on = False
            stop music fadeout 1
            play music "audio/Noir Beats.mp3"

        scene expression "bk4/world_maps/airtemple_night.jpg"
        if bk4_calendar >=2:
            show screen bk4_money_date
        with dissolve
    call screen b4_screen_airtemple1

label b4_repcity_map1:
    if not b4_music_day_on:
        $ b4_music_day_on = True
        stop music fadeout 1
        play music "audio/bounce_town.mp3"
    scene black
    scene expression "bk4/world_maps/republic_city.jpg"
    if bk4_calendar >=2:
        show screen bk4_money_date
    with dissolve
    if not republic_city_first:
        $ republic_city_first = True
        with dissolve
        tn "ahh... republic city."
        tn "smells like industry, hobos, and selfish go-getters."
        tn "smells like home."
    if probending_available ==1:
        $ probending_available = 2
        show expression "bk4_xtra/remove/blackveil.png" with dissolve
        show expression "misc/star2.png":
            xalign 0.75 yalign 0.0
        with dissolve
        "at the top right of your screen is a star."
        "when it appears, you can click on it to help team avatar fight a probending match."
        $ probending_time = 5
        hide screen bk4_money_date
        show screen bk4_money_date2
        "click it now."
        hide screen bk4_money_date2
        call screen bk4_money_date2
        jump bk4_probending

    call screen b4_screen_repcity1

label bk4_your_room:
    if airbending ==1 and not pema_hj2:
        jump pema_handjob2
    scene black
    scene expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    if not b4_daytime:
        show expression "bk4_xtra/remove/blackveil.png"
    if not korra_jail:
        show bfac bfac01
        with dissolve
        pn "dear?"
        pn "you really should get off this island and go get korra out of police headquarters."
        tn "right, that's what i'm doing."
        tn "just... checking... that you knew that."
        pn "what?"
        tn "i'm gonna go."
        jump b4_airtemple_map1
    if b4_pema_dinner == 8:
        show bfac bfac02
        with dissolve
        pn "shouldn't you be waiting for korra in her room?"
        jump b4_airtemple_map1
    if b4_pema_dinner ==7:
        show bfac bfac02
        show bfae jinora03:
            xpos -600
        with dissolve
        tn "korra's gone."
        pn "well that wasn't very smart."
        pn "she doesn't know anything about the city..."
        jino "is she gonna be okay?"
        tn "dunno."
        tn "i can't leave this fucking island for some reason."
        pn "go wait in her room, dear."
        pn "i'm sure she'll come back eventually."
        jino "i'll go watch for her!"
        hide bfae with moveoutleft
        tn "korra is stressing me out."
        pn "that's alright dear, i'm sure you'll put her in her place soon enough."
        tn "i like you."
        pn "well, that's nice to hear..."
        tn "i mean-"
        pn "I know. the feeling is mutual, my love."
        $ b4_pema_dinner = 8
        jump b4_airtemple_map1

    if b4_pema_dinner ==6:
        show bfac bfac02
        show bfae jinora03:
            xpos -600
        with dissolve
        jino "did you find her?"
        tn "not yet..."
        jump b4_airtemple_map1
    if b4_pema_dinner ==5:
        show bfac bfac02
        show bfae jinora03:
            xpos -600
        with dissolve
        jino "please go see korra!"
        jump b4_airtemple_map1
    if b4_pema_dinner ==4:
        show bfac bfac02
        with dissolve
        pn "well, i hear them all running around in there."
        pn "i guess we should get to eating-"
        show bfae jinora03:
            xpos -600
        with moveinleft
        jino "i think something's wrong with korra!"
        tn "oh?"
        jino "i went and got her for dinner because you forgot to ask her..."
        tn "*cough*"
        jino "...but she won't answer!"
        jino "i think something's wrong!"
        tn "alright, alright, i'll go talk to her."
        $ b4_pema_dinner = 5
        jump b4_airtemple_map1
    if b4_pema_dinner ==3:
        show bfac bfac02
        with dissolve
        pn "you need to tell one more kid that dinner is ready."
        jump b4_airtemple_map1
    if b4_pema_dinner ==2:
        show bfac bfac02
        with dissolve
        pn "please go let the other two know that dinner is ready."
        jump b4_airtemple_map1
    if b4_pema_dinner ==1:
        show bfac bfac02
        with dissolve
        pn "please go tell the kids that dinner is ready!"
        jump b4_airtemple_map1
    if b4_pema_dinner ==0:
        show bfac bfac01
        with dissolve
        pn "hey sweetie, did-"
        pn "......"
        hide bfac with Dissolve(1)
        show bfac bfac02 with Dissolve(1)
        pn "okay, what's wrong?"
        tn "what?"
        pn "i know your face... something's bothering you."
        tn "man, i don't even know my face."
        show bfac bfac06 with dissolve
        tn "....nevermind."
        tn "it's korra."
        pn "mmm... let me guess... being a little bitch?"
        tn "that's... well, yeah."
        show bfac bfac02 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "of course she is."
        show bfac bfac03 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "she's been an entitled little bitch since the day she was born."
        pn "someone should...."
        show bfac bfac02 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "well, nevermind."
        tn "no... i want to hear this."
        pn "i'm sure she'll get put in her place eventually."
        pn "...there's something else, isn't there?"
        tn "oh... right."
        tn "i owe lin 100 coins for getting korra out of jail."
        tn "where's my money, bitch?"
        pn "well, i like that tone..."
        show bfac bfac06 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "...but why do you need to pay lin that much?"
        tn "the... jail... thing?"
        tn "i just-"
        show bfac bfac03 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "ugh! i could just slap her!"
        tn "why?"
        pn "because she knows we don't have that!"
        tn "wait, we... don't?"
        tn "i thought i was loaded..."
        tn "i mean, isn't this my island?"
        show bfac bfac02 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "sorry dear, i don't mean to diminish your achievements."
        pn "but it sounds like i need to remind you that we have a lot of things handed down from aang, your father..."
        pn "...but we're a little cash-light."
        tn "so... i have a nice house and no money?"
        tn "damn this economy!"
        tn "...i guess i'll have to figure something out."
        pn "you also have me, you know."
        tn "oh, speaking of you..."
        tn "there was some mention of 'ball milk' and 'your face'?"
        show bfac bfac06 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "hmm?"
        show bfac bfac02 at Move((0.01, 0.0), (0.0, 0.0), 0.1)
        pn "oh! right! yes!"
        pn "i was hoping you'd give me a little of your time..."
        tn "...what are you doing right now?"
        pn "unfortunately, it's getting late and I've almost finished preparing dinner."
        pn "would you mind getting all the kids?"
        pn "let them know they need to come eat?"
        tn "and then...?"
        pn "and then i'm all yours to fuck filthy, darling."
        tn "loving. this."
        pn "go! scootch! get the kids!"
        pn "and don't worry about korra for now."
        pn "she can just skip dinner."
        tn "alright, alright..."
        scene black with dissolve
        $ b4_pema_dinner = 1
        $ b4_daytime = False
        jump b4_airtemple_map1
    else:

        jump bk4_your_room1

label bk4_korra_room:
    if not korra_jail:
        tn "i need to get off this island and go get korra out of police headquarters."
        jump b4_airtemple_map1
    if b4_pema_dinner <=4:
        play sound "audio/knocking.mp3"
        "you knock on her door."
        "there's no response."
        tn "okay then, i guess just pout."
        "there's still no response... but it's somehow more aggressive."
        jump b4_airtemple_map1
    else:
        if b4_pema_dinner ==5:
            $ b4_pema_dinner = 6
            tn "korra?"
            tn "......"
            tn "..........."
            tn "korra, i'm not playing around, get out here."
            tn "...................."
            tn "when did I become the fucking responsible one?"
            tx "i just want to fuck shit!"
            tn "alright, i tried it your way..."
            scene black
            scene expression "bk4/backgrounds/korra_room_night.jpg":
                ypos 0
            tx "ha!" with hpunch
            "you kick down her door, only to realize it wasn't locked."
            tn "....woops."
            tn "wait...."
            ta "damn it!"
            ta "this chick is gonna be difficult, i can fucking tell."
            ta "i'm coming for you, korra!"
            jump b4_airtemple_map1
        else:
            jump bk4_korra_room1

label bk4_tower:
    scene black
    scene expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0
    if not b4_daytime:
        show expression "bk4/backgrounds/tower_night .jpg":
            ypos 0
    with dissolve
    if not korra_jail or b4_meelo_dinner <2:
        if b4_meelo_dinner ==0:
            tn "Wow, I'm high up!"
            show bfae meelo_01 with moveinbottom
            play sound "audio/burp.mp3"
            mee "**burp!!*" with hpunch
            tn "ah! fuck! why!?"
            mee "...."
            tn "...."
            mee "...."
            tn "are you just gonna-"
            play sound "audio/burp.mp3"
            mee "**burp!!*" with hpunch
            $ b4_meelo_dinner = 1
            if b4_pema_dinner >=1 and b4_pema_dinner <4:
                tn "that reminds me... go eat."
                mee "'kay 'kay!"
                hide bfae with dissolve
                tn "...that kid is weird."
                $ b4_meelo_dinner =2
                $ b4_pema_dinner +=1
                jump b4_airtemple_map1
            else:
                tn "....okay, i'm leaving."
                jump b4_airtemple_map1
        if b4_meelo_dinner ==1:
            show bfae meelo_01 with dissolve
            play sound "audio/burp.mp3"
            mee "**burp!!*" with hpunch
            if b4_pema_dinner >=1 and b4_pema_dinner <4:
                tn "that reminds me... go eat."
                mee "'kay 'kay!"
                hide bfae with dissolve
                tn "...that kid is weird."
                $ b4_meelo_dinner =2
                $ b4_pema_dinner +=1
                jump b4_airtemple_map1
            else:
                tn "....okay, i'm leaving."
                jump b4_airtemple_map1
    else:
        jump bk4_tower1

label bk4_train:
    scene black
    scene expression "bk4/backgrounds/training_day_1.jpg":
        ypos 0
    if not b4_daytime:
        show expression "bk4/backgrounds/training_night.jpg":
            ypos 0

    if not korra_jail:
        show bfae jinora02
        with dissolve
        tn "i guess this is where we'll be training..."
        jino "umm... don't you have to go get korra?"
        tn "*grumble* ....everyone always telling me what to do.... *mumble*"
        jump b4_airtemple_map1
    if b4_jinora_dinner <2:
        show bfae jinora02
        with dissolve
        jino "it's gonna be fun training with korra!"
        tn "oh, i have some ideas."
        if b4_pema_dinner >=1 and b4_pema_dinner <4:
            tn "and pema wanted me to tell you to go eat."
            jino "okay!"
            hide bfae with dissolve
            tn "that was easy."
            $ b4_jinora_dinner = 2
            $ b4_pema_dinner +=1
            jump b4_airtemple_map1
        else:
            jump b4_airtemple_map1
    else:
        jump bk4_train1

label bk4_meditation:
    scene black
    scene expression "bk4/backgrounds/meditation_temple.jpg":
        ypos 0
    if not b4_daytime:
        show expression "bk4/backgrounds/meditation_temple_night.jpg":
            ypos 0
    with dissolve
    if not korra_jail or b4_ikki_dinner <2:
        if b4_ikki_dinner ==0:
            tn "well, it's a nice vie-"
            show bfae ikki01 with moveinright
            ikki "hi!" with hpunch
            tn "ah!" with hpunch
            ikki "you're old!"
            tn "....okay, i guess that's how we say 'hello' in crazy town."
            ikki "why are you so old?"
            tn "....i wish i knew."
            tn "what's your name?"
            ikki "b-b-but i'm... ikki..."
            tn "icky? your name is icky?"
            tn "....your mother is not very nice, is she?"
            ikki "no! it's ee-kee!"
            tn "that's a weird sound you're making."
            $ b4_ikki_dinner = 1
            if b4_pema_dinner >=1 and b4_pema_dinner <4:
                tn "oh, right, pema wanted me to tell you to go eat."
                ikki "food!"
                hide bfae with dissolve
                tn "that was easy."
                $ b4_ikki_dinner = 2
                $ b4_pema_dinner +=1
                jump b4_airtemple_map1
            else:
                tn "sorry icky, gotta go do a thing."
                tn "see you later!"
                jump b4_airtemple_map1

        if b4_ikki_dinner ==1:
            show bfae ikki01
            with dissolve
            if b4_pema_dinner >=1 and b4_pema_dinner <4:
                tn "pema wanted me to tell you to go eat."
                ikki "food!"
                hide bfae with dissolve
                tn "that was easy."
                $ b4_ikki_dinner = 2
                $ b4_pema_dinner +=1
                jump b4_airtemple_map1
            else:
                tn "okay, so... you're still here."
                ikki "uh-huh!"
                tn "well... bye."
                jump b4_airtemple_map1
    else:


        jump bk4_meditation1

label bk4_docks:
    if b4_dock_travel:
        jump b4_repcity_map1
    else:
        tn "....where the fuck is the boat!?"
        tn "i guess i'm not leaving the island right now...."
        jump b4_airtemple_map1

label bk4_docks_night:
    tn "the docks are closed at night."
    if b4_pema_dinner ==6:
        tn "fuck."
        tn "how did she even..."
        ta "oh, fucking... damn waterbenders!"
        ta "i can't go after her!?"
        ta "i just have to wait here?"
        tn "...fine."
        tn "but she's gonna get a talking-to when she comes back."
        $ b4_pema_dinner = 7
    jump b4_airtemple_map1

label bk4_police:
    if not korra_jail:
        stop music
        play music "audio/Unanswered Questions.mp3"
        jump korra_arrested
    else:
        jump bk4_police1

label bk4_alleys:
    scene black
    scene expression "bk4/backgrounds/alleys_1.jpg":
        ypos 0
    show bfah bfah01
    with dissolve
    if not korra_jail:
        tn "oh, an alley."
        tn "boy."
        tn "exciting."
        sg "hey, don't knock it."
        sg "it's a {i}good{/i} alley."
        tn "...how can you tell?"
        sg "because i'm in it."
        tn "......"
        tn "so...."
        sg "wanna buy a hat?"
        tn "no, i don't want to buy a hat."
        sg "are you sure?"
        tn "....."
        sg "......"
        tn "...let's talk later."
        sg "you got it, my man."
        jump b4_repcity_map1
    else:
        jump bk4_alleys1

label bk4_park:
    scene black
    scene expression "bk4/backgrounds/park_day_1.jpg":
        ypos 0
    with dissolve
    if not korra_jail:
        tn "well, this is a friendly spot."
        jump b4_repcity_map1
    else:
        jump bk4_park1

label bk4_statue:
    if not korra_jail:
        tn "that's... like... all the way over there."
        tn "i should really go get korra out of police headquarters."
        jump b4_repcity_map1
    else:
        jump bk4_statue1


label bk4_your_room1:



    if korra_spank_bj ==4:
        show bfac bfac02
        with dissolve
        pn "hi, dear."
        pn "is everything all right?"
        tn "did korra come by?"
        tn "tell you anything?"
        show bfac bfac06 with dissolve
        pn "korra?"
        pn "no... why?"
        tn "oh, no reason."
        tn "excuse me, but i need to go speak with her."
        show bfac bfac02 with dissolve
        pn "put her in her place, dear."
        $ korra_spank_bj = 5
        jump b4_airtemple_map1
    if korra_spank_bj ==5:
        with dissolve
        tn "i need to go find korra."
        jump b4_airtemple_map1

    if study_unlock:
        menu:
            "bedroom":
                pass
            "study":

                scene black
                scene expression "bk4/backgrounds/study0.jpg":
                    ypos 0
                with fade
                if lin_rub_equal >=3 and meelo_stall ==0:
                    $ meelo_stall = 1
                    show bfae meelo_01 with dissolve
                    mee "i need my rock!"
                    tn "...what are you doing here?"
                    mee "i need-"
                    tn "no, i heard you, but why are you asking that in here?"
                    mee "'cause i need it."
                    tn "...right."
                    tn "why do you need this rock?"
                    mee "because it makes me happy!"
                    tn "and you need me to get it for you?"
                    mee "yes!"
                    tn "...."
                    tn "fine..."
                    mee "yay!"
                    jump b4_airtemple_map1
                if meelo_stall ==1:
                    show bfae meelo_01 with dissolve
                    mee "i need my rock!"
                    tn "i know, i'm working on it."
                    jump b4_airtemple_map1
                if meelo_stall ==2:
                    show bfae meelo_01 with dissolve

                    "you give meelo a rock."
                    mee "yay my rock!"
                    mee "now i can get back to sorting coins!"
                    hide bfae with dissolve
                    tn "glad that's over."
                    $ meelo_stall = 3
                    jump bk4_your_room1

                if asami_bj and not shady_sleep_call:
                    $ shady_sleep_call = True
                    "*ring!*"
                    tn "what the..."
                    "*ring!* *ring!* *ring!*"
                    b4_tp "who is this?"
                    b4_tp "how did you get this number?"
                    sg "it's shady."
                    sg "and... it's shady."
                    b4_tp "right. what do you want?"
                    sg "i have a special item for you."
                    b4_tp "what kind of special?"
                    sg "the kind of special that knocks someone out for a bit and paralyzes their limbs."
                    sg "maybe long enough to transport them from one place to another."
                    b4_tp "you think i'd be interested in that?"
                    b4_tp "me? tenzin? the upstanding council member?"
                    sg "no, of course not..."
                    sg "...and if you sent someone to get it, it absolutely wouldn't be here."
                    b4_tp "send someone?"
                    b4_tp "why wouldn't i go myself?"
                    sg "...do you really want to be seen buying this?"
                    b4_tp "fair point."
                    b4_tp "how much is it?"
                    sg "60 coins."
                    b4_tp "60?!"
                    b4_tp "nope, that's too much."
                    sg "look, it's that or nothing."
                    b4_tp "we'll see."
                    b4_tp "i'll send a girl over to pick it up."
                    sg "good."
                    $ korra_spank_bj = 1

                jump study_menu
            "exit":
                jump b4_airtemple_map1

                label study_menu:
                    menu:
                        "call asami" if lin_rub_equal >=3:
                            if sato_weapon:
                                if not asami_bj:
                                    $ asami_bj = True
                                    jump asami_blowjob1
                                menu:
                                    "tits":
                                        jump asami_tits2
                                    "blowjob":
                                        if asami_bj:
                                            jump asami_blowjob2
                                        else:
                                            tn "i don't think that's gonna fly yet."
                                            jump study_menu
                                    "!!!!!!" if korra_spank_bj >=6 and asami_bj and k_a_titsuck ==0:
                                        jump korra_asami_titsuck1
                                    "girls titsuck" if k_a_titsuck >=2:
                                        b4_tp "asami!"
                                        b4_tp "go suck korra's tits."
                                        asa "...."
                                        asa "only because i have to."
                                        b4_tp "you don't need to lie to me."
                                        asa "shut up."
                                        jump korra_asami_titsuck1
                                    "back":
                                        jump study_menu
                            else:
                                b4_tp "*ring...*"
                                b4_tp "*ring...* *ring...*"
                                b4_tp "no response."
                                jump study_menu
                        "call zhu li":

                            if lin_rub_quest ==0 or lin_rub_quest >=3:
                                b4_tp "*ring...*"
                                b4_tp "*ring...* *ring...*"
                                b4_tp "no response."
                                jump study_menu

                            if lin_rub_quest ==1:
                                zh "varrick global industries."
                                b4_tp "zhu li, i need you to do a thing."
                                zh "almost, sir."
                                b4_tp "what?"
                                zh "close, but that's not the phrase."
                                b4_tp "phrase? for what?"
                                zh "...who is this?"
                                b4_tp "it's tenzin."
                                b4_tp "er... the tenzin cosplayer."
                                zh "right, right."
                                zh "what do you want?"
                                b4_tp "I need a favor."
                                zh "and why should i care?"
                                b4_tp "because then i'll owe {i}you{/i} a favor."
                                zh "you already do."
                                b4_tp "then i'll owe you multiple favors."
                                b4_tp "look, i have pull with the real tenzin, so help me out, would you?"
                                zh "...very well."
                                zh "but i expect these \"favors\" to be paid in full, without question, when the time comes."
                                b4_tp "fine, you got it, whatever."
                                zh "then what do you need?"
                                b4_tp "I need to meet with you."
                                zh "*sigh*"
                                zh "i will meet you on the city streets."
                                b4_tp "excellent, see you there."
                                zh "yes."
                                "*click*"
                                b4_tp "....."
                                b4_tp "that's fine, that's not rude."
                                b4_tp "goodbye, have a nice day, please eat a handful of weiners."
                                $ lin_rub_quest = 2
                                $ b4_zhuli_exists = True
                                jump study_menu
                            if lin_rub_quest ==2:
                                tn "i should meet zhu li on the city streets."
                                jump study_menu
                        "exit":
                            jump b4_airtemple_map1

    if meet_kyoshi >=1:
        if not study_unlock:

            if korra_pema_upset ==0:
                show bfac bfac03
                show bfab bfab06:
                    xzoom -1
                with dissolve
                pn "that's not the way we do things, korra!"
                show bfab bfab24 with dissolve
                kn "well then the way you do things is dumb."
                pn "i swear to beyonce, I will slap you."
                kn "why you so mad, bro?"
                pn "you can't be purposefully inciteful and then shrug and say \"oh, why are you mad?\""
                pn "that's a total cunt move, and you know good and well that there are things that make you pissed off."
                pn "it's just different things for you and me, so you feel superior that the things that make me mad don't make you mad."
                pn "you fucking cunt."
                show bfab bfab06 with dissolve
                kn "yeah, well, i don't remember asking for your opinion."
                kn "and, besides... maybe i'm just not as sensitive as you."
                pn "oh yeah?"
                pn "well next time you get excited about a game or something, i'm gonna insult it a lot."
                pn "and see how controlled you are then."
                kn "ugh, why are you still talking?"
                pn "okay, it's fucking go time-"
                tn "hey... maybe it's not."
                show bfab bfab24 with dissolve
                kn "tenzin? what are you doing here?"
                tn "i live here."
                tn "what are {i}you{/i} doing here?"
                kn "i was asking for money, because you guys are fucking loaded."
                pn "we are {i}not{/i}!"
                kn "...yeah, that's why you have a private island."
                tn "korra."
                kn "yeah?"
                tn "get the fuck out."
                kn "...."
                kn "fine."
                kn "...."
                show bfab bfab06 with dissolve
                kn "bitch."
                pn "you-"
                hide bfab with dissolve
                pn "aarggh!!!"
                tn "that was all... a thing."
                tn "what's going on?"
                pn "you heard her, she wants money."
                tn "for what?"
                pn "i don't know!"
                pn "ask her."
                pn "for all i care, she can sell both her kidneys to get it!"
                pn "i'll help cut them out!"
                pn "ugh, i need a nap."
                pn "this stress is not good for the baby."
                hide bfac with dissolve
                tn "...i'm gonna have to have a talk with korra."
                $ korra_pema_upset = 1
                jump b4_airtemple_map1

            if korra_pema_upset ==2:
                show bfac bfac02
                with dissolve
                pn "hey, are you okay?"
                pn "i didn't mean to upset you with that argument with korra."
                tn "me? yeah, i'm fine."
                tn "how are you?"
                pn "i'm-"
                show bfab bfab05:
                    xzoom -1
                with dissolve
                kn "hey, pema."
                show bfac bfac03 with dissolve
                pn "what do you want?"
                kn "I want to apologize."
                pn "....."
                kn "i'm really sorry for... asking for money..."
                tn "that's not the problem, korra."
                tn "do better."
                kn "..."
                kn "I'm sorry for..."
                kn "...treating you so badly."
                pn "....."
                kn "you didn't deserve my attitude."
                kn "and... i'm sorry."
                pn "....."
                pn "that's very mature of you, korra."
                pn "but i am still very upset with you."
                pn "i'd like you to leave now."
                kn "...okay."
                hide bfab with dissolve
                show bfac bfac02 with dissolve
                pn "did you do this?"
                tn "...maybe."
                pn "you're amazing."
                pn "i'm... so grateful i have you."
                tn "likewise."
                pn "now, i need to lie down again."
                pn "but later..."
                pn "well, we'll do something later, okay?"
                tn "sounds good."
                $ b4_daytime = False
                $ korra_pema_upset = 3
                jump b4_airtemple_map1

            if korra_pema_upset ==3 and b4_daytime:

                show bfac bfac02
                with dissolve
                pn "tenzin... i need you."
                tn "...."
                tn "i don't think i'm ready for commitment."
                pn "no, i mean... i {i}need{/i} you."
                tn "oh."
                tn "oh!"
                tn "really?"
                tn "now?"
                pn "look, i know you're busy, and don't like sex very much..."
                tn "......"
                tn "...sure..."
                pn "but i'll give you a present... if you fuck me like a rag doll."
                tn "....."
                tn "just to be clear..."
                tn "you want me to fuck you, and in exchange... you'll give me a present?"
                pn "you've just been so sexual lately, and i'm so... {i}fucking{/i}... wet."
                pn "all the time."
                pn "i need you to stuff my cunt, love."
                pn "please?"
                menu:
                    "what kind of present?":
                        tn "tell me more about this gift."
                        pn "it's a surprise!"
                    "yup, no questions needed":

                        tn "i will do that for you."
                        tn "because i'm a giver."

                pn "just one thing..."
                tn "hm?"
                pn "i want to make sweaty, filthy, love..."
                pn "...in the park?"
                tn "was that really a question?"
                pn "i know you aren't really interested in being adventurous, but i just thought i'd-"
                tn "let's do it."
                pn "really?!"
                tn "i can't let you go unfulfilled... and unfilled."
                tn "you want to get fucked in the park?"
                tn "we're gonna fuck in the park."
                pn "oh, lovely!"
                pn "i'll get the kids and while they play, you and i can slip off somewhere..."
                scene black with dissolve
                "within record time you and pema round up the kids and head off to the park."
                jump pema_vag2

    if pema_bj ==3:
        $ b4_jinora_exists = True
        $ pema_bj =4
        show bfac bfac02 with dissolve
        pn "thank you for getting korra off the island."
        pn "did you speak with jinora?"
        tn "i did, yes."
        pn "i want you to know that, however you decided to handle it, i support you absolutely."
        pn "i'm just... so {i}proud{/i} to be your wife."
        pn "and i want to show you how grateful i am."
        tn "oh?"
        pn "you did such a good job today..."
        pn "I think you deserve a treat."
        tn "...i agree."
        jump pema_blowjob1

    if air_scroll ==1 and not amon_mask:
        jump rescue_korra1

    if bk4_swim_mission ==3 and b4_daytime:
        show bfac bfac02
        show bfae group03
        with dissolve
        pn "is korra ready?"
        show bfab bfab03:
            xzoom -1
        with dissolve
        kn "here!"
        pn "oh, that's great!"
        pn "come on, let's go to the park."
        scene black with Dissolve(1.5)
        jump bk4_swim_time

    if bk4_calendar ==2:
        if pema_hj ==0:
            $ pema_hj = 1
            with dissolve
            jump pema_handjob1
        if pema_hj ==1:
            if airbending ==1:
                jump pema_handjob2
            else:
                show bfaj bfaj19
                with dissolve
                pn "have you finished with korra?"
                tn "not yet..."
                jump b4_airtemple_map1
    if pema_hj ==2:
        if missing_meelo ==2:
            show bfac bfac03
            with dissolve
            pn "did you find meelo?"
            tn "i did... and he is happy, and safe, at the park."
            show bfac bfac06 with dissolve
            pn "the... park?"
            pn "did you bring him home?"
            tn "no..."
            pn "....."
            pn "why...?"
            tn "because he's out making fat stacks on stacks, pema!"
            tn "stacks on stacks on stacks!"
            tn "and i need him out there, making money to hire me, so that we can get by!"
            tn "trust me."
            pn "*sigh...*"
            show bfac bfac02 with dissolve
            pn "well, the park is the safest place in the city."
            pn "i'll ask lin to have police around for him."
            pn "she owes us that at least."
            tn "cool."
            $ missing_meelo = 3
            tn "uh... where's korra?"
            pn "i think i heard her come back."
            tn "alright, thanks."
            jump b4_airtemple_map1



        if lin_equalists ==2 and missing_meelo ==0:
            show bfac bfac03
            pn "tenzin!!" with hpunch
            pn "thank goodness you're home!"
            tn "uh... you're welcome?"
            pn "it's meelo!"
            tn "oh, was he eating glue? or boogers?"
            tn "that kid isn't very sma-"
            pn "no! he's missing!"
            tn "what? really?"
            pn "yes!"
            tn "...how?"
            pn "i... what?"
            tn "how is he missing?"
            tn "we're on an island."
            pn "i don't know!"
            pn "but i can't find him!"
            tn "could he have left the island?"
            pn "maybe!?"
            pn "please! please find him!"
            show bfab bfab24:
                xzoom -1
            with moveinleft
            kn "hey, is everything okay? i heard shout-"
            show bfac bfac03 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
            pn "meelo is missing!"
            show bfab bfab04 with dissolve
            kn "don't worry, i'll find him."
            tn "no, you're staying here."
            kn "tenzin... i can help. really."
            pn "I don't care! both of you go!"
            show bfab bfab03 with dissolve
            kn "awesome!"
            tn "...awesome?"
            show bfab bfab09 with dissolve
            kn "finally a chance for some action!"
            kn "explore the city some... get to help somebody..."
            tn "this is a missing child."
            show bfab bfab24 with dissolve
            kn "meh, he's fine."
            kn "what could happen?"
            show bfab bfab03 with dissolve
            kn "i'm on it."
            tn "...alright, whatever."
            tn "let's split up, then."
            show bfab bfab04 with dissolve
            kn "on it!"
            hide bfab with moveoutleft
            hide bfac with dissolve
            show bfac bfac02 with dissolve
            pn "tenzin... please."
            pn "find our boy."
            tn "i'm on it, sugar britches."
            $ missing_meelo = 1
            jump b4_airtemple_map1

        show bfac bfac02
        with dissolve
        if missing_meelo ==1:
            show bfac bfac02
            with dissolve
            pn "please find our boy."
            jump pema_chat_menu
        else:
            $ randpema = 0
            $ randpema = renpy.random.randint(1,3)
            if randpema ==1:
                pn "hello, my love."

            if randpema ==2:
                pn "it's always lovely to see you, dear."

            if randpema ==3:
                pn "welcome back, handsome."

            if asami_tits >=2 and pema_bj ==0:
                pn "do you have a minute to talk?"
                pn "something's come up."

        jump pema_chat_menu

        label pema_chat_menu:
            menu:
                "sleep" if missing_meelo >=6 and not b4_daytime:
                    jump bk4_next

                "wait until night" if missing_meelo >=6 and b4_daytime:
                    if airbending ==2 and meditation_level ==0:
                        tn "i have something to do, first."
                        jump b4_airtemple_map1

                    $ b4_daytime = False
                    scene black with dissolve
                    jump b4_airtemple_map1
                "talk":

                    if asami_tits >=2:
                        if pema_bj ==1:
                            pn "please get korra off this island for the day..."
                            pn "...and talk to jinora."
                            jump pema_chat_menu

                        if pema_bj ==0:
                            $ pema_bj = 1
                            tn "what's up?"
                            pn "can you... get korra off the island for a bit?"
                            tn "uh, sure."
                            tn "why?"
                            show bfac bfac03 with dissolve
                            pn "she's been really getting on my nerves lately."
                            pn "making a mess, demanding i do her laundry, arguing with me constantly..."
                            tn "okay, but... where should she go?"
                            show bfac bfac06 with dissolve
                            pn "maybe avatar statue island?"
                            pn "and tell her to take jinora with her."
                            pn "she's been stuck here and could use a bit of time off the island as well."
                            show bfac bfac02 with dissolve
                            pn "actually, this might be a good time to have a talk with jinora."
                            tn "about what?"
                            pn "well... becoming a woman."
                            tn "oh... i do not want that conversation."
                            pn "well, you're the one that has to have it with her."
                            tn "why?"
                            pn "she might confuse her love for you as a father... for something else."
                            pn "you need to explain the situation to her."
                            tn "...right. on it."
                            show bfac bfac03 with dissolve
                            pn "but seriously? get korra off this damn island for a day."
                            tn "will do."
                            jump b4_airtemple_map1

                    if k_protein ==1:
                        tn "hey, you make korra protein shakes, right?"
                        show bfac bfac03 with dissolve
                        pn "yes... and she's never grateful."
                        pn "so i don't make them very well."
                        show bfac bfac06 with dissolve
                        pn "why?"
                        tn "i'd like you to make me one."
                        tn "a good one, please."
                        show bfac bfac02 with dissolve
                        pn "mmm... i know where i like to get my protein..."
                        tn "i like that energy, but i'm serious right now."
                        tn "but i like that."
                        tn "did i already say that?"
                        pn "you did."
                        pn "tell you what, let me make it for you."
                        pn "you've been... fun, lately."
                        pn "I'd like to take care of you."
                        tn "fucking deal."
                        hide bfac with dissolve
                        tn "....."
                        tn "..........."
                        tn "..................."
                        show bfac bfac02 with dissolve
                        pn "here you go!"
                        play sound "audio/win2.mp3"
                        "you got the protein shake!"
                        tn "thanks, babe."
                        pn "my pleasure!"
                        pn "but we still need to discuss a protein shake for {i}me{/i}."
                        tn "we will, you tease."
                        $ k_protein = 2
                        jump b4_airtemple_map1

                    if korra_pb_chat ==2:
                        if bk4_swim_mission ==0:
                            pn "hey, i was thinking..."
                            pn "how about a family swim?"
                            tn "really?"
                            tn "where?"
                            pn "the park!"
                            pn "there's a river there..."
                            pn "it'll be a lot of fun to take the kids... and korra."
                            tn "...alright, yeah."
                            tn "sounds like fun."
                            pn "you'll need to buy us all swimsuits."
                            tn "where do i buy those?"
                            pn "i'm sure you'll find someone that sells them."
                            pn "there's bound to be somewhere in the city."
                            $ bk4_swim_mission = 1
                            scene black with dissolve
                            jump b4_airtemple_map1
                        if bk4_swim_mission ==1:
                            if korra_swimsuit and pema_swimsuit and kids_swimsuit:
                                tn "here, i got all the swimsuits."
                                pn "oh! wonderful!"
                                pn "you're such a good man."
                                pn "i'll take mine and the children's..."
                                pn "would you mind delivering korra's?"
                                tn "sure, not a problem."
                                pn "wonderful."
                                pn "we'll meet back here once you give it to her."
                                $ bk4_swim_mission = 2
                                jump b4_airtemple_map1
                            else:
                                pn "please find us some swimsuits, dear."
                                scene black with dissolve
                                jump b4_airtemple_map1
                        if bk4_swim_mission ==2:
                            pn "please deliver korra's swimsuit to her, dear."
                            pn "and tell her to come to our room."
                            jump b4_airtemple_map1
                        if bk4_swim_mission ==3:
                            if not b4_daytime:
                                pn "did you give korra the swimsuit?"
                                tn "i did."
                                pn "wonderful."
                                pn "well, let's pick this up during the day."
                                jump pema_chat_menu
                            else:
                                show bfac bfac02
                                show bfae group03
                                with dissolve
                                pn "is korra ready?"
                                show bfab bfab03:
                                    xzoom -1
                                with dissolve
                                kn "here!"
                                pn "oh, that's great!"
                                pn "come on, let's go to the park."
                                scene black with Dissolve(1.5)
                                jump bk4_swim_time

                    if lin_hj and not pema_lin_hj_talk:
                        $ pema_lin_hj_talk = True
                        pn "how'd it go with lin?"
                        pn "did you pay her back?"
                        menu:
                            "i jizzed in her mouth":
                                tn "I nutted in her mouth, and she swallowed it."
                                tn "mostly."
                                show bfac bfac06
                                pn "....."
                                show bfac bfac02
                                pn "serves her right!"
                                pn "i bet she loved it, the pent-up cow."
                                pn "well done, love."
                                tn "...you are something special."
                                pn "as are you, dear."
                                jump pema_chat_menu
                            "i did":

                                tn "oh, i definitely paid her back."
                                pn "good!"
                                pn "I hope you unloaded on her face or something."
                                tn "....."
                                tn "something like that, actually, yeah."
                                pn "good job, baby!"
                                tn "you... are a catch."
                                pn "and that's how i feel about you, my love."
                                jump pema_chat_menu


                    if missing_meelo ==1:
                        show bfac bfac02
                        with dissolve
                        pn "you have to find meelo."
                        jump pema_chat_menu

                    $ randpema = renpy.random.randint(1,2)
                    if randpema ==1:
                        tn "how's it going?"
                        pn "wonderful!"
                        pn "well... the kids can be tiresome, but i wouldn't trade our life for anything."
                    if randpema ==2:
                        pn "do you need anything?"
                        tn "not right now."
                    jump pema_chat_menu
                "handjob":

                    tn "so... how about another handjob?"
                    if missing_meelo ==1:
                        show bfac bfac02
                        with dissolve
                        pn "i'm sorry, too stressed... please find our boy."
                        jump pema_chat_menu

                    if not pema_hj_daily:
                        pn "sure, come here."
                        jump pema_handjob3
                    else:
                        pn "i love your enthusiasm, dear, but we already did that today."
                        pn "i don't want to wear you out."
                        jump pema_chat_menu

                "?????(locked)" if pema_bj <5:
                    "test"
                "blowjob" if pema_bj >=5:
                    jump pema_blowjob1

                "fuck" if study_unlock:
                    tn "i have to have you right here, right now."
                    pn "where... where has this fire been all these years?!"
                    show bfac bfac03 at Move((0.01, 0.0), (0.0, 0.0), 0.1,  delay=1.55)
                    pn "fuck me. fuck me now!"
                    pn "take me!" with hpunch
                    jump pema_vag3
                "exit":

                    jump b4_airtemple_map1


label bk4_korra_room1:


    if k_a_titsuck >=2 and airbending >=7 and not korra_fj:
        jump korra_footjob1

    if korra_spank_bj ==5:
        tn "oh, korra..."
        kn "...come in, tenzin."
        hide screen bk4_money_date
        scene expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0
        show bfab bfab27
        with fade
        kn "y-yes?"
        tn "you didn't talk to pema, like i told you to."
        show bfab bfab26 with dissolve
        kn "i... i know."
        tn "why not?"
        kn "...."
        kn "because i..."
        show bfab bfab27
        with dissolve
        kn "because i... i got distracted."
        tn "....is that so?"
        kn "y-yeah."
        kn "it was... it was not on purpose."
        tn "...you realize that i have to punish you again, don't you?"
        kn "yes..."
        kn "and i... i deserve it."
        tn "then bend over my lap again."
        show bfab bfab26 with dissolve
        kn "okay..."
        jump korra_spank3

    if korra_spank_bj ==4:
        scene expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0
        with dissolve
        tn "korra's not here..."
        jump b4_airtemple_map1

    if k_a_titsuck ==1 and not b4_daytime:
        jump korra_asami_titsuck1

    if k_protein ==1:
        tn "i should come back when I have a protein shake for her."
        jump b4_airtemple_map1
    if k_protein ==2:
        if not micro_convince or korra_resist >86:
            tn "(i don't think she'll be fooled by what i'm going to do to this protein shake...)"
            if korra_resist >86:
                tn "(i need to meditate with her some more, and lower her {b}resistance{/b}.)"
            if not micro_convince:
                tn "(i wonder if I can buy her another outfit from shady and make her wear it while meditating?)"
        else:
            if not b4_daytime:
                tn "i should come back during the day with this protein shake."
                jump b4_airtemple_map1
            else:
                jump korra_protein1

    scene black

    if bk4_swim_mission ==4:
        with dissolve
        play music "audio/gltch.mp3"
        "you hear an odd sound coming from korra's room."
        menu:
            "investigate":
                jump korra_rubbing
            "come back later":

                stop music
                $ b4_music_day_on = False
                jump b4_airtemple_map1

    if b4_daytime and not korra_leg and meditation_level >=3:
        jump korra_legwork

    if b4_daytime:
        scene expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
    else:
        scene expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0
        if airbending >=3 and korra_resist <=88:
            if korra_rubbed ==0:
                jump korra_rubbing2
            if korra_rubbed ==1:
                jump amon_mast_scare
            if korra_rubbed ==2:
                jump korra_rubbing3

    if korra_pema_upset ==1:
        show bfab bfab24 with dissolve
        kn "...what?"
        tn "you do {i}not{/i} get to treat pema that way."
        kn "like what? an adult who should be in control of her emotions?"
        tn "and your acting like a petulant, needling, weak-willed child is more noble?"
        kn "hey..."
        tn "she is also fucking pregnant."
        kn "if she wanted to get pregnant, then she should deal with-"
        tn "shut up with your \"should\" bullshit."
        tn "this is how people are."
        tn "civility is just as much about not causing unhappiness as it is about not reacting to it."
        tn "nihilism doesn't {i}work{/i} unless you go through the other side to actual zen, but you're a total poser."
        tn "so shut up, go talk to pema, and apologize."
        kn "pfft. and if i don't?"
        tn "then game over, you stupid, stupid, stupid girl."
        show bfab bfab06 with dissolve
        kn "you can't-"
        tn "apologize."
        $ korra_pema_upset = 2
        jump b4_airtemple_map1
    if korra_pema_upset ==2:
        show bfab bfab24 with dissolve
        kn "what's up?"
        tn "go apologize to pema."
        jump b4_airtemple_map1

    if korra_spank_bj ==2:
        if b4_daytime:
            tn "korra's out getting the special powder."
            tn "i should come back later."
            jump b4_airtemple_map1
        else:
            show bfab bfab24 with dissolve
            kn "uh... hey..."
            kn "here's your weird package."
            play sound "audio/win2.mp3"
            "korra hands you a little envelope."
            tn "great."
            tn "where's my change?"
            show bfab bfab03 with dissolve
            kn "well... about that..."
            kn "there is none."
            kn "i couldn't negotiate him down."
            ta "i was serious about this, korra!"
            ta "you were supposed to negotiate, not spend it all!"
            show bfab bfab05 with dissolve
            kn "but... but i couldn't!"
            kn "i tried!"
            tn "that's no excuse."
            tn "time for the consequences."
            kn "come on! that's not fair!"
            tn "you disobeyed your master's command!"
            tn "and i know just how to punish you."
            tn "come here."
            show bfab bfab24 with dissolve
            kn "...what?"
            tn "do as i say."
            $ korra_spank_bj =3
            $ b4_korra_exists = True
            jump korra_spank1

    if korra_spank_bj ==1:
        if not b4_daytime:
            tn "i should visit korra during the day if she's going to go pick up that powder from shady."
            jump b4_airtemple_map1
        if bk4_money >=60:
            show bfab bfab04
            with dissolve
            kn "hey, tenzin."
            kn "what's up?"
            tn "i need you to pick up something for me in town."

            show bfab bfab24 with dissolve
            if korra_resist >=85:
                kn "uh... i'm not your servant, tenzin."
                kn "get it yourself."
                tn "...."
                "korra's {b}resistance{/b} is too high for this."
                jump b4_airtemple_map1

            kn "uh... why?"
            tn "it's important for your training."
            kn "well, what is it?"
            tn "it's a special muscle stimulant."
            show bfab bfab01 with dissolve
            kn "why didn't you just say so?"
            kn "sure, i'll get it."
            tn "just one thing..."
            tn "he says it's 60 coins."
            tn "but i expect you to haggle with him."
            show bfab bfab24 with dissolve
            kn "...really?"
            tn "yeah."
            tn "if you spend all 60, i'm going to be upset."
            tn "understand?"
            kn "i guess..."
            kn "what does this have to do with training?"
            tn "you have to learn to overcome indirect obstacles."
            tn "and i said so."
            show bfab bfab05 with dissolve
            kn "okay..."
            tn "negotiate it lower or you will be punished."
            kn "...i understand."
            play sound "audio/money.mp3"
            $ bk4_money -=60
            "you give korra 60 coins."
            kn "i'll... go do this, then..."
            hide bfab with dissolve
            tn "i'll come back later."
            $ korra_spank_bj = 2
            $ b4_korra_exists = False
            jump b4_airtemple_map1
        else:

            tn "(i need 60 coins in order to get korra to buy the sleeping powder from shady.)"

    if nude_meditate and pema_bj >=5:
        if korra_boobjob ==0:
            hide black
            show black with dissolve
            "you hear asami and korra having a conversation."
            menu:
                "eavesdrop":
                    jump korra_boobjob0
                "leave":

                    jump b4_airtemple_map1


    if pema_bj ==2 or pema_bj ==3:
        with dissolve
        tn "korra is at the statue."
        jump b4_airtemple_map1
    if pema_bj ==1:
        if b4_daytime:
            show bfab bfab04
            with dissolve
            kn "what's up, tenzin?"
            tn "you need to get off the island until i tell you to come back."
            show bfab bfab24 with dissolve
            kn "what? why?"
            tn "because you're annoying the shit out of pema."
            kn "so?"
            tn "okay, let me put it this way..."
            tn "go to avatar statue island or no more training."
            kn "easy... easy... yeah, sure, no problem."
            tn "and take jinora with you."
            kn "why?"
            tn "...."
            kn "alright, i'm going, i'm going."
            $ pema_bj = 2
            kn "i'll go now."
            $ b4_korra_exists = True
            $ b4_jinora_exists = True
            hide bfab with dissolve
            jump b4_airtemple_map1
        else:
            with dissolve
            tn "(i should come back during the day.)"
            jump b4_airtemple_map1

    if amon_mask and not korra_rescue_talk:
        jump korra_rescued_talk
    if korra_rescue_talk and not korra_rescue_slap:
        tn "korra is waiting for me at meditation."
        jump b4_airtemple_map1

    if air_scroll ==1 and not amon_mask:
        tn "...korra?"
        tn "huh."
        tn "maybe she's at the training grounds?"
        jump b4_airtemple_map1

    if missing_meelo ==6:
        if korra_mad >=1:
            show bfab bfab06
        else:
            if not b4_daytime:
                show bfab bfab04
            pass
        with dissolve
        jump bk4_korra_slave_menu

        label bk4_korra_slave_menu:
            menu:
                "give gift" if korra_mad >=1:
                    if korra_gift >=1:
                        $ korra_gift -=1
                        "you give korra some exercise equipment."
                        $ korra_mad -=1
                        if korra_mad ==0:
                            show bfab bfab04 with dissolve
                            "she becomes happy, instead of unhappy."
                        if korra_mad ==1:
                            "she becomes unhappy, instead of angry."
                        if korra_mad ==2:
                            "she becomes angry, instead of furious."
                        if korra_mad >=3:
                            "she's a little less furious."
                        kn "...thanks."
                        if korra_mad ==0:
                            if b4_daytime:
                                kn "I guess i'll get back to what i was doing..."
                                hide bfab with dissolve
                        jump bk4_korra_slave_menu
                    else:
                        tn "(i have nothing to give her...)"
                        jump bk4_korra_slave_menu
                "chat" if not b4_daytime or korra_mad >=1:
                    if korra_mad >=1:
                        kn "i don't want to talk to you right now."
                        jump bk4_korra_slave_menu
                    else:
                        if bk4_swim_mission ==5:
                            if korra_rubbed >=3:
                                kn "did... did you want something?"
                                jump bk4_korra_slave_menu
                            else:
                                kn "um... you didn't... um... see... what you think you did."
                                jump bk4_korra_slave_menu
                        if bk4_swim_mission ==3:
                            if b4_daytime:
                                tn "meet us in my room."
                                jump bk4_korra_slave_menu
                            else:
                                tn "meet us in my room during the day."
                                jump bk4_korra_slave_menu

                        if bk4_swim_mission ==2:
                            if not b4_daytime:
                                tn "hey, i'm here to give you this swimsuit."
                                play sound "audio/win2.mp3"
                                "korra got a swimsuit!"
                                kn "oh, thanks!"
                                show bfab bfab03 with dissolve
                                kn "this'll be great for showing off my muscles."
                                tn "meet us in my room during the day."
                                kn "okay."
                                $ bk4_swim_mission = 3
                                jump b4_airtemple_map1

                            if b4_daytime:
                                show bfab bfab04
                                with dissolve
                                tn "hey, i'm here to give you this swimsuit."
                                play sound "audio/win2.mp3"
                                "korra got a swimsuit!"
                                kn "oh, thanks!"
                                show bfab bfab03 with dissolve
                                kn "this'll be great for showing off my muscles."
                                tn "meet us in my room."
                                kn "okay."
                                $ bk4_swim_mission = 3
                                jump b4_airtemple_map1

                        if korra_pb_chat ==2:
                            kn "yeah, i'm not doing that other stuff."
                            kn "just regular training and meditation for me, thanks."
                            jump bk4_korra_slave_menu

                        if korra_pb_chat ==1:
                            tn "i was thinking-"
                            kn "so was i, tenzin."
                            show bfab bfab01 with dissolve
                            kn "i didn't like that \"open-minded\" stuff."
                            kn "I'm sure i can learn airbending without it."
                            kn "and i appreciate the probending help, but you get paid for that."
                            tn "...what."
                            show bfab bfab04 with dissolve
                            kn "yeah, so we'll just focus on regular training and meditating."
                            kn "i'm not doing that other stuff."
                            tn "but... i told you that it's necessary."
                            kn "yeah, but..."
                            show bfab bfab24 with dissolve
                            kn "eh."
                            show bfab bfab04 with dissolve
                            kn "anything else?"
                            tn "....."
                            tn "(i'm going to break you, korra.)"
                            show bfab bfab24 with dissolve
                            kn "hmm?"
                            tn "...have it your way."
                            $ korra_pb_chat = 2
                            jump bk4_korra_slave_menu

                        if probending_first and korra_pb_chat ==0 and korra_leg:
                            $ korra_pb_chat = 1
                            show bfab bfab04 with dissolve
                            kn "hey, thanks for helping out at the probending arena."
                            kn "we were really struggling until you jumped in."
                            tn "were you really doing that badly?"
                            show bfab bfab03 with dissolve
                            kn "oh yeah, without you we were guaranteed to get kicked out."
                            tn "and you enjoy doing it?"
                            kn "are you kidding?!"
                            kn "i love it!"
                            tn "and you'd hate to lose the opportunity?"
                            show bfab bfab24 with dissolve
                            kn "well, yeah..."
                            tn "then thank me."
                            kn "um..."
                            kn "okay..."
                            kn "thank you, tenzin."
                            tn "\"thank you, {i}sir{/i}.\""
                            show bfab bfab05 with dissolve
                            kn "....."
                            kn "thank you... sir."
                            tn "if you want my continued help, i expect more obedience from you."
                            kn "i get it, you want me to stay here on the island and die of old age."
                            tn "i mean, do what i tell you, when i tell you."
                            tn "for example, right now, i want you to say..."
                            menu:
                                "i'm a disgusting pig whore":
                                    $ temp_boolean = False
                                "i'm a spoiled, entitled brat":

                                    $ temp_boolean = True

                            show bfab bfab12
                            kn "what!?!" with hpunch
                            kn "i'm not saying that!!"
                            tn "you know, last i checked..."
                            tn "i'm your airbending master."
                            tn "and your probending coach."
                            tn "and you're in trouble with the city."
                            tn "and you live in my house."
                            tn "i suggest you do as i say."
                            show bfab bfab06 with dissolve
                            kn "screw you, tenzin!"
                            tn "i know it's hard to believe, but i'm trying to open your mind."
                            tn "airbending is about... going with the flow."
                            tn "you're uptight and stiff..."
                            tn "you're basically a penis, korra."
                            tn "you're a penis."
                            tn "do you want to be a penis?"
                            tn "hmm?"
                            tn "that tickle your fancy?"
                            show bfab bfab05 with dissolve
                            kn "...."
                            kn "no...."
                            tn "i'm here to teach you."
                            tn "airbenders are... free with their bodies."
                            tn "it's intrinsic to their mental philosophy."



                            tn "is that understood?"
                            show bfab bfab06 with dissolve
                            kn "....yes."
                            tn "now, say it."
                            kn "......."
                            if not temp_boolean:
                                kn "{size=-15}i'm a disgusting pig whore."
                            else:
                                kn "{size=-15}i'm a spoiled, entitled brat."
                            tn "what was that?"
                            kn "......"
                            show bfab bfab25 with dissolve
                            if not temp_boolean:
                                kn "...i'm a disgusting pig whore."
                            else:
                                kn "...i'm a spoiled, entitled brat."
                            tn "good girl."
                            show ctc
                            pause
                            hide ctc
                            show bfab bfab06
                            kn "now get out of my room!" with hpunch
                            play sound "audio/win2.mp3"
                            $ korra_mad += 3
                            $ korra_resist -=1
                            $ korra_moral -=1
                            "korra's {b}resistance{/b} lowered."
                            "korra's {b}morality{/b} lowered."
                            "korra is now {b}furious{/b}."

                            scene black with hpunch
                            "korra slams the door in your face."
                            "chuckling to yourself, you head to bed."
                            jump bk4_next
                        else:

                            show bfab bfab03
                            with dissolve
                            kn "i can't wait to become an airbender!"
                            show bfab bfab04 with dissolve
                            kn "i'm gonna find and kick {b}amon's{/b} ass!"
                            jump b4_airtemple_map1


























                "?????(locked)" if not korra_wash:
                    "test"
                "washroom" if korra_wash:
                    if korra_mad >=1:
                        tn "(she seems to mad for this...)"
                        jump bk4_korra_slave_menu
                    if korra_wash_daily:
                        tn "she's already washed today."
                        jump bk4_korra_slave_menu
                    else:
                        jump korra_washroom
                "?????(locked)" if not korra_leg:
                    "test"
                "legwork" if korra_leg:
                    if korra_mad >=1:
                        tn "(she seems to mad for this...)"
                        jump bk4_korra_slave_menu
                    if korra_leg_daily:
                        tn "she's already exercised today."
                        jump bk4_korra_slave_menu
                    else:
                        if not b4_daytime:
                            tn "your legs are looking a little weak."
                            show bfab bfab05 with dissolve
                            kn "oh, no!"
                            kn "excuse me."
                        else:
                            pass
                        jump korra_legwork2
                "?????(locked)" if korra_rubbed <3:
                    "test"
                "rub" if korra_rubbed >=3:
                    tn "i'm going to be busy the rest of the night, so you'll have to... entertain... yourself."
                    $ korra_rub_order = 3
                    scene black with dissolve
                    "you step outside and wait for a few minutes before entering again."
                    jump korra_rubbing3

                "?????(locked)" if not korra_tits_out:
                    "test"
                "titplay" if korra_tits_out:
                    jump air_train2

                "?????(locked)" if k_protein <3 and b4_daytime:
                    "test"
                "protein shake" if k_protein >=3 and b4_daytime:
                    jump korra_protein2

                "?????(locked)" if korra_boobjob <3:
                    "test"
                "boobjob" if korra_boobjob >=3:
                    jump korra_boobjob2

                "?????(locked)" if korra_spank_bj <6:
                    "test"
                "spank" if korra_spank_bj >=6:
                    menu:
                        "thankful":
                            jump korra_spank3
                        "resistant":

                            jump korra_spank2
                        "back":

                            jump bk4_korra_slave_menu
                "?????(locked)" if not korra_fj:
                    "test"

                "footjob" if korra_fj:
                    jump korra_footjob1

                "stats" if meditation_level >=1:
                    show screen korra_stats
                    show ctc
                    pause
                    hide ctc
                    hide screen korra_stats
                    jump bk4_korra_slave_menu
                "exit":

                    jump b4_airtemple_map1

    if missing_meelo ==5:
        show bfab bfab03
        with dissolve
        kn "I'm so excited!"
        kn "let's start training tomorrow!"
        tn "for disobeying me... repeatedly..."
        show bfab bfab24 with dissolve
        kn "...?"
        tn "your... {i}training...{/i} is not going to be easy."
        kn "...what?"
        kn "but... i'm the avatar."
        tn "that's not going to get you special treatment any more."
        tn "not with me."
        kn "but... i am special."
        tn "...."
        tn "you know what?"
        tn "you are. you are special."
        tn "and you're going to get special treatment."
        show bfab bfab04 with dissolve
        kn "great!"
        tn "i won't need to be gentle with you."
        tn "you're going to get the hard and fast airbending training."
        show bfab bfab24 with dissolve
        kn "oh..."
        tn "that's okay, right?"
        tn "you want to get good fast, don't you?"
        kn "um... yeah..."
        tn "and you can handle it, can't you?"
        tn "you are the {i}avatar{/i}, after all..."
        kn "y-yeah... i... i can..."
        tn "are you sure? are you sure you're up for the challenge?"
        tn "it will be the hardest training you've ever received."
        tn "no more coddling."
        tn "you might want to quit... but if you do, then i will never train you. ever."
        tn "and then you will {i}never{/i} be an airbender."
        tn "and without mastering the four elements, you will never master being the avatar."
        show bfab bfab05 with dissolve
        kn "i can... i can take anything you give me."
        tn "oh, we're definitely going to find out if that's true."
        kn "......"
        tn "goodnight, korra...."
        kn "good... goodnight, tenzin..."
        $ missing_meelo = 6
        jump b4_airtemple_map1


    if b4_pema_dinner ==8:
        with dissolve
        tn "i go out... i rescue her from prison..."
        tn "then i give her a bed..."
        tn "and then she ignores me?"
        tn "i'm gonna-"
        jino "she's here!"
        kn "jinora, shut up!"
        ta "korra! get in here!"
        show bfab bfab06 with dissolve
        kn "what?"
        tn "you are... hey! don't \"what\" me!"
        tn "you should be apologizing!"
        tn "where were you?"
        tn "i told you to-"
        kn "ugh! get out, tenzin!"
        play sound "audio/thud.mp3"
        scene black with sshake
        "korra slams the door in your face, stunning you."
        tn "...."
        tn "we are just... gonna... talk about this in the morning!"
        kn "okay! whatever!"
        $ b4_pema_dinner = 9
        "you head to your room, and find pema asleep."
        tn "great."
        tn "no release either."
        tn "i'm gonna have to start slapping people."
        "you fall asleep."
        "...grumpily."
        jump bk4_next

    if b4_pema_dinner ==7:
        with dissolve
        tn "what should i do?"
        jump b4_airtemple_map1
    if b4_pema_dinner ==6:
        with dissolve
        tn "korra's still not back...."
        jump b4_airtemple_map1






    with dissolve
    if missing_meelo ==1:
        tn "meelo's not here."
        jump b4_airtemple_map1

    if missing_meelo ==3:
        if not b4_daytime:
            tn "i'll check on korra tomorrow."
            hide black
            show black wth dissolve
            "you go to sleep and visit korra again in the morning."
            $ b4_daytime = True
            hide black with dissolve
            jump bk4_korra_room1

        show bfad bfad01
        with dissolve
        tn "ko-"
        tn "...yowza."
        asa "oh, hello."
        asa "you must be tenzin."
        tn "i am."
        tn "who are you?"
        hide bfad with dissolve
        show bfad bfad02 with dissolve
        asa "i'm asami."
        asa "asami sato."
        asa "it's a pleasure to meet you."
        show bfad bfad02 at Move((0.0, 0.0), (0.0, -0.5), 2.0,  bounce = True )
        show expression "bk4/backgrounds/korra_room_day.jpg" at Move((0.0, 0.0), (0.0, -0.5), 2.0,  bounce = True )

        show ctc
        pause
        hide ctc
        tn "yes it is..."
        show bfad bfad08 with dissolve
        asa "um... i'm sorry?"
        tn "I mean..."
        tn "what are you doing here?"
        show bfad bfad02 with dissolve
        asa "well, as the new sponsor of team avatar, I thought i'd come by and see-"
        tn "back up... what is \"team avatar\"?"
        asa "you don't know about pro-bending?"
        tn "is it as dumb as it sounds?"
        asa "what? no! it's thrilling to watch."
        asa "and provides great visibility for future industries."
        tn "oh shit, future industries?"
        tn "wait... you're {i}that{/i} asami?"
        tn "you were a fucking megajillionaire!"
        asa "that's... not a word..."
        asa "and you must be thinking of my father."
        asa "i'm still learning from him."
        tn "(oh, right... she hasn't done all that, yet...)"
        tn "right, so, tell me more about this \"team avatar\" probending nonsense."
        asa "well, since korra join the pro-bending arena, future industries has agreed to sponsor her."
        tn "......."
        tn "................"
        tn "............................."
        ta "{size=+10}she fucking what?!?" with hpunch
        show bfad bfad08 with dissolve
        asa "oh, this is... um... awkward."
        asa "i'll... ah... go."
        asa "please let korra know i wanted to see her."
        tn "....fine."
        show bfad bfad02 with dissolve
        asa "thank you."
        hide bfad with dissolve
        tn "she... is a hottie."
        tn "......."
        tx "damn korra!"
        tx "why do i have to babysit this reckless girl!?"
        tn "now i gotta find korra."
        $ missing_meelo = 4
        jump b4_airtemple_map1

    "korra isn't here right now."
    jump b4_airtemple_map1


label bk4_tower1:
    if pema_bj ==2:
        tn "i should visit the statue."
        jump b4_airtemple_map1
    if pema_bj ==3:
        tn "i should talk to pema."
        jump b4_airtemple_map1
    if airbending >=6:
        if asami_tits ==0:
            jump asami_tits1
        if asami_tits >=2:
            menu:
                "call asami" if lin_rub_equal <3:
                    jump asami_tits2
                "exit":

                    jump b4_airtemple_map1

    if b4_pema_dinner ==5 or b4_pema_dinner ==7 or b4_pema_dinner ==8:
        tn "it's just a tower."
        jump b4_airtemple_map1
    if b4_pema_dinner ==6:
        tn "doesn't look like korra's here..."
        jump b4_airtemple_map1



    if missing_meelo ==1:
        tn "meelo's not here."
        jump b4_airtemple_map1

    tn "nothing here right now."
    jump b4_airtemple_map1

label bk4_train1:
    if b4_pema_dinner ==5 or b4_pema_dinner ==7 or b4_pema_dinner ==8:
        tn "nothing going on here right now."
        jump b4_airtemple_map1
    if b4_pema_dinner ==6:
        tn "...shit."
        tn "i was hoping she'd be here."
        tx "where are you, korra!?"
        jump b4_airtemple_map1



    scene black
    if b4_daytime:
        scene expression "bk4/backgrounds/training_day_1.jpg":
            ypos 0

        if air_scroll ==1 and not amon_mask:
            tn "hello? korra?"
            tn "where is she?"
            jump b4_airtemple_map1
        if missing_meelo >=6:
            jump bk4_train2
        if missing_meelo >=2 and missing_meelo <=5:
            with dissolve
            tn "korra's not here..."
            jump b4_airtemple_map1
        if missing_meelo ==1:
            with dissolve
            tn "meelo's not here."
            jump b4_airtemple_map1
        if airbending ==1:
            show bfab bfab04
            with dissolve
            kn "uh... hey."
            kn "I'm... not... getting in trouble?"
            kn "is that cool?"
            tn "where's jinora?"
            kn "dunno."
            ta "she's supposed to be watching you!"
            ta "nobody listens to me!"
            ta "this whole place is full of assholes!"
            show bfab bfab24 with dissolve
            kn "uh... you should go meditate."
            tn "that seems boring."
            kn "uh... well, yeah."
            tn "then i win this conversation."
            kn "...what?"
            tn "i win!"
            kn "......."
            jump b4_airtemple_map1
        if airbending ==0:
            show bfab bfab01
            with dissolve
            kn "took you long enough."
            tn "...you're talking to me as if you're not in trouble."
            kn "pfft, come on."
            kn "don't be so uptight."
            show bfab bfab02 with dissolve
            kn "now let's get into some airbending!"
            kn "i'm ready to kick some windy butt!"
            tn "apologize. now."
            show bfab bfab24 with dissolve
            kn "what?"
            kn "why?"
            tn "because you disobeyed my direct orders and left the island!"
            kn "and...?"
            tn "and if you disobey me again, there will be consequences."
            kn "okay, i'm sorry. whatever."
            kn "can we get into it now?"
            show bfab bfab09 at Move((0.0, 0.0), (-0.3, 0.0), 0.9)
            kn "because i'm ready!"
            kn "i'm the best bender in the world, and once i can airbend, i'll be unstoppable!"
            kn "i'm in peak condition!"
            kn "i'm in my prime, tenzin!"
            kn "let's crack some skulls!"
            tn "that... was a terrible fucking apology."
            show bfab bfab24 with dissolve
            kn "yeah, yeah, i'm sorry."
            show bfab bfab10 at Move((-0.3, 0.0), (0.0, 0.0), 1.4) with Dissolve(3.0)
            kn "now..."
            kn "show me what you got!"
            tn "...what?"
            show bfab bfab09 with dissolve
            kn "come on!"
            kn "i demand you begin training me!"
            kn "i can take it!"
            kn "give me your worst!"
            tn "uh..."
            tn "...i'm teaching you?"
            show bfab bfab24 with dissolve
            kn "well... yeah..."
            tn "i thought you were supposed to teach me?"
            tn "what the fuck do i know about airbending?"
            kn "you're... kinda the only airbender in the world."
            tn "I am? that sucks."
            kn "........"
            tn "i mean... that is a thing that i knew."
            kn "so...."
            tn "so...."
            show bfae jinora02:
                xpos -600
            with dissolve
            jino "hey!"
            jino "how's it going?"
            jino "have you started her on the spinners, yet?"
            tn "the... spinners?"
            jino "yeah."
            jino "come on!"
            show black
            hide bfae
            hide bfab
            with dissolve
            "you and korra follow jinora as she sets up the equipment."
            jump first_spinner


    if not b4_daytime:
        scene expression "bk4/backgrounds/training_night.jpg":
            ypos 0
        with dissolve
        if airbending >=2:
            jump bk4_training_menu

        tn "korra's not here."
        jump b4_airtemple_map1

label bk4_train2:
    if airbending >=2:
        with dissolve
        jump bk4_training_menu

        label bk4_training_menu:
            menu:
                "train with korra" if b4_daytime:

                    if korra_spank_bj ==2:
                        tn "she's out buying that special powder from shady."
                        tn "I should visit her in her room later."
                        jump bk4_training_menu
                    if pema_bj ==1:
                        tn "i should talk to korra in her room."
                        jump b4_airtemple_map1
                    if pema_bj ==2 or pema_bj ==3:
                        tn "korra is at the statue."
                        jump b4_airtemple_map1
                    if korra_mad >=1:
                        tn "she's too mad at me to train..."
                        jump bk4_training_menu
                    else:
                        if amon_mask and not korra_rescue_talk:
                            tn "korra's not here..."
                            jump bk4_training_menu
                        if korra_rescue_talk and not korra_rescue_slap:
                            tn "korra is waiting for me at meditation."
                            jump b4_airtemple_map1
                        if airbending ==2 and meditation_level ==0:
                            tn "I should really meet korra and jinora."
                            jump bk4_training_menu
                        else:
                            if bk4_swim_mission ==4:
                                tn "korra's not here..."
                                jump bk4_training_menu
                            else:
                                jump korra_training
                "train with spinners":

                    jump first_spinner
                "exit":

                    jump b4_airtemple_map1
    if airbending ==1:
        $ bk4_training_daily = True
        show bfab bfab02b
        with dissolve
        kn "hey... ready to get starting airbending?"
        tn "....."
        tn "no...."
        show bfab bfab04 with dissolve
        kn "hit me, come on."
        kn "what's the first lesson?"
        tn "(...what the fuck do i do...)"
        menu:
            "eat ass, live fast":
                show bfab bfab24 with dissolve
                kn "i... that can't be the first rule."
                tn "it's the one i live by."
            "never trust a man in a turtleneck sweater and glasses":

                show bfab bfab24 with dissolve
                kn "...why?"
                tn "he's gonna be a dick."
                tn "a self-absorbed, pretentious dick."
                kn "that seems a little bigoted."
                tn "maybe."
            "french girls enjoy being lied to so they can yell at you":

                show bfab bfab24 with dissolve
                kn "....really?"
                tn "i don't know."
                tn "what, do you really think i've dated a french chick?"
                kn "......"
                kn "who hurt you?"


        show bfae jinora02:
            xpos -600
        with dissolve
        jino "hey, can i join?"
        tn "yes! thank the spirits."
        kn "...."
        tn "i... mean... yes?"
        jino "have you started on the spinners yet?"
        tn "oh. right. uh... we were just about to."
        kn "why are the spinners important again?"
        jino "as you learn new airbending forms, you'll need to train your body to use those forms properly."
        jino "just learning new forms won't be enough."
        jino "you'll have to make sure your body is capable of using the form."
        jino "that's where the spinners help."
        kn "okay, so... every time i'm ready to do more intense training, i'll need to level up on the spinners?"
        jino "yup."
        kn "alright, i think i got it."
        kn "wanna go first, tenzin?"
        tn "no?"
        tn "...oh, alright."
        jump first_spinner

    "test"

label bk4_meditation1:
    if korra_fj and not kyoshi_puss_fan:
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, 0.0), 0.0)
        hide screen bk4_money_date
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 1.0)

        $ renpy.pause(0.5)

        show bfaf bfaf01
        with Dissolve(0.5)
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 0.0)
        kn "hey, tenzin..."
        kn "can you meditate with me?"
        kn "i'm having trouble getting the hang of it."
        tn "(...i don't know how to do that...)"
        tn "uh... sure?"
        "you sit down next to korra and close your eyes."
        scene black with Dissolve(1.5)
        jump kyoshi_pussyfan1

    if pema_bj ==1:
        tn "i should talk to korra in her room."
        jump b4_airtemple_map1
    if pema_bj ==2 or pema_bj ==3:
        tn "korra is at the statue."
        jump b4_airtemple_map1
    if b4_pema_dinner ==5 or b4_pema_dinner ==7 or b4_pema_dinner ==8:
        tn "comfy, but... nothing's happening here right now."
        jump b4_airtemple_map1
    if b4_pema_dinner ==6:
        tx "{size=+10}korra!!"
        tx "your ass is grass and i'm gonna mow it!"
        jump b4_airtemple_map1



    if korra_rescue_talk and not korra_rescue_slap:
        jump korra_meditate_slaps
    if amon_mask and not korra_rescue_talk:
        tn "korra's not here..."
        jump b4_airtemple_map1
    if air_scroll ==1 and not amon_mask:
        tn "...korra?"
        tn "huh."
        tn "not here."
        jump b4_airtemple_map1
    if meditation_level >=1 and b4_daytime:
        if korra_mad <=0:
            if bk4_swim_mission ==4:
                tn "korra's not here..."
                jump b4_airtemple_map1
            else:
                jump korra_meditation
        else:
            tn "i think korra's too mad for meditation."
            jump b4_airtemple_map1
    if airbending ==2 and meditation_level ==0:
        show bfab bfab01
        show bfae jinora02:
            xpos -600
        with dissolve
        kn "about time."
        kn "let's knock out some meditation... or whatever."
        kn "totally ready."
        kn "so what are we doing?"
        tn "(hmmm.....)"
        tn "(maybe i can turn this into a fun time for me...)"
        tn "jinora..."
        jino "yes?"
        tn "korra is about to undergo a very... special... type of meditation."
        tn "it's for her advanced airbending training."
        tn "i'd like you to leave us."
        show bfae jinora03 with dissolve
        jino "aww... really?"
        jino "i wanna join!"
        tn "maybe in the future, but for now... you need to leave."
        jino "okay..."
        show bfae jinora02 with dissolve
        jino "do a good job, korra!"
        kn "you know i will!"
        hide bfae with dissolve
        kn "okay... so."
        kn "what first?"
        $ b4_dock_travel = True
        jump korra_meditation
    if missing_meelo ==1:
        tn "meelo's not here."
        jump b4_airtemple_map1

    tn "nothing here right now."
    jump b4_airtemple_map1

label bk4_police1:



    scene black with dissolve
    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0
    if meet_kyoshi >=1:
        if lin_rub_quest ==0:
            show bfaa bfaa01
            with dissolve
            lin "tenzin. good."
            tn "lin. busty."
            show bfaa bfaa00 with dissolve
            lin "...what?"
            tn "aren't we talking like cavemen?"
            lin "don't be an idiot."
            tn "man, i'm trying."
            lin "shut up."
            show bfaa bfaa03 with dissolve
            lin "i need more updates on equalists."
            lin "despite all expectation, you have actually been more helpful than my police force."
            tn "have you considered hiring me?"
            tn "i could use money."
            tn "it is a useful object."
            lin "have you considered not being an idiot?"
            tn "........"
            tn "....yes."
            lin "look, just get me some damn equalist insight."
            lin "and then... we can look into payment."
            tn "what kind of-"
            show bfaa bfaa07 with dissolve
            lin "this kind."
            show bfaa bfaa08 with dissolve
            tn "...."

            lin "got it?"
            tn "got it."
            show bfaa bfaa03 with dissolve
            lin "good."
            lin "on your way, now."
            $ lin_rub_quest = 1
            tn "(....how do i get that information?)"

    if korra_tits_out:
        if lin_butt_quest ==0:
            show bfaa bfaa01
            with dissolve
            lin "ah, tenzin."
            hide bfaa with dissolve
            show bfaa bfaa03 with dissolve
            lin "i need you again."
            tn "do you want me to just whip it out here or-"
            show bfaa bfaa04 with hpunch
            lin "not like that!"
            lin "i need you to investigate the equalists some more."
            show bfaa bfaa03 with dissolve
            lin "you've proven to be... skilled at doing so."
            lin "i would be a bad police chief if I didn't utilize an asset such as yourself."
            tn "you sure it's not because you want me around?"
            show bfaa bfaa09 with dissolve
            lin "no, it's..."
            lin "it's for the city..."
            tn "...."
            tn "alright, alright."
            tn "what do i need to know?"
            show bfaa bfaa03 with dissolve
            lin "they've got some kind of big supplier."
            lin "i don't know how they're staying so well outfitted."
            lin "these lightning weapons... they're something new."
            lin "i need you to get out into the city streets and see what you can uncover."
            tn "streets?"
            lin "start at the statue, see if there's anything there."
            lin "grab that damn skybison of yours and fly around."
            lin "see what you can see."
            lin "but my gut says, once you grab your skybison, you should check the city."
            tn "i can do that."
            tn "but..."
            lin "but what?"
            tn "...."
            lin "oh."
            lin "right."
            lin "....."
            show bfaa bfaa07 with dissolve
            lin "...please, tenzin."
            lin "help me out."
            tn "i will."
            lin "thank you."
            tn "you and your big tits are welcome."
            show bfaa bfaa08 with dissolve
            lin "...."
            lin "uh..."
            lin "th-thanks."
            lin "....."
            lin "umm...."
            lin "are you just gonna stand there? staring?"
            tn "until i'm ready."
            lin "...."
            lin "i mean..."
            show bfaa bfaa09 with dissolve
            lin "i do... have things to do."
            tn "you're a cutie."
            lin "come... come on, tenzin."
            tn "alright, i'll go."
            tn "see you around, tits!"
            lin "....."
            lin "...bye."
            $ lin_butt_quest = 1
            jump b4_repcity_map1

    if probending_first and not lin_hj2:
        jump lin_handjob2
    if missing_meelo ==4:
        show bfaa bfaa01
        show bfab bfab04:
            xzoom -1
        with dissolve
        kn "come on! help me out, lin!"
        lin "absolutely not!"
        show bfab bfab09 with dissolve
        kn "i'm totally ready!"
        lin "no, you are not."
        tn "what's happening?"
        lin "this... child... has been given-"
        show bfab bfab02b with dissolve
        kn "tenzin!"
        kn "tell this chick that i'm ready!"
        tn "uh, no, and what are we talking about?"
        show bfab bfab03 with dissolve
        kn "i was given the job of hunting amon and the equalists!"
        tn "...."
        tn "lin..."
        lin "wasn't me."
        show bfab bfab04 with dissolve
        kn "the city council gave me the job."
        tn "...i'm on the council."
        tn "i think."
        tn "so... how did you get that job?"
        kn "oh, i just... asked them if there was anything i could do."
        show bfab bfab01 with dissolve
        kn "they seemed thrilled to give me the job."
        ta "I told you to stay on the island and stop getting in trouble!"
        show bfab bfab02 with dissolve
        kn "yeah... but i didn't."
        kn "and now i have a job to do!"
        ta "you disobedient..."
        ta "you are in no way ready for that!"
        show bfab bfab03 with dissolve
        kn "sure i am!"
        show bfab bfab09 with dissolve
        kn "gonna beat up some bad guys!"
        lin "no, you're not."
        lin "and you're not getting extra help from the police."
        lin "we're already working on neutralizing this threat."
        show bfab bfab04 with dissolve
        kn "then help me train, tenzin."
        kn "i'm totally willing to buckle down and learn."
        tn "*sigh...*"
        tn "fine."
        tn "come on, you're coming back to the island."
        kn "totally."
        kn "i'm all about it."
        lin "watch her, tenzin."
        tn "i'm trying!"
        $ missing_meelo = 5
        $ b4_daytime = False
        jump b4_repcity_map1

    if missing_meelo ==1:
        show bfaa bfaa00
        with dissolve
        tn "is meelo here?"
        lin "no."
        tn "shoot."
        jump b4_repcity_map1
    if not lin_equalist_quest:
        jump lin_equalist_start
    if lin_equalist_quest and lin_equalists <=1:
        if lin_equalists ==0:
            show bfaa bfaa00
            with Dissolve(1.5)
            lin "go find that equalist rally, and report back."
            tn "I guess \"hello\" is too difficult for you."
            tn "fine."
            jump b4_repcity_map1
        if lin_equalists ==1:
            show bfaa bfaa00
            with Dissolve(1.5)
            lin "go find that equalist rally, and report back."
            tn "i already did."
            hide bfaa with dissolve
            show bfaa bfaa03 with dissolve
            jump lin_equalist_cont
    if lin_equalists ==2:
        show bfaa bfaa03
        with dissolve
        jump lin_menu

        label lin_menu:
            menu:
                "talk":
                    if lin_rub_quest >=1:
                        if lin_rub_quest ==1 or lin_rub_quest ==2:
                            lin "get me more information on the equalists, tenzin."
                            jump lin_menu
                        if lin_rub_quest ==3:
                            lin "well?"
                            menu:
                                "tell her about the equalist rally":
                                    $ lin_rub_quest = 4
                                    jump lin_rub1
                                "nothing":

                                    tn "i don't have anything yet."
                                    lin "then stop wasting my time."
                                    jump lin_menu
                        if lin_rub_quest ==4:
                            if lin_rub_equal <3:
                                jump lin_rub1
                    if lin_butt_quest ==1:
                        if become_a_star >=5:
                            $ lin_butt_quest = 2
                            lin "well?"
                            lin "anything on the equalists?"
                            tn "i have the location of some weapons."
                            lin "that's excellent!"
                            lin "well done, tenzin!"
                            tn "oh, you know... i'm amazing."
                            lin "bring that address over to my desk so I can take a good look."
                            tn "first... do you have a way to make copies of photos?"
                            lin "of course."
                            lin "in that corner over there."
                            tn "thanks."
                            hide black
                            show black with dissolve
                            "you make extra prints of the compromising photo of mr. sato and amon."
                            hide black with dissolve
                            tn "alright, here's that address..."
                            jump lin_buttjob1
                        else:

                            lin "have you uncovered information regarding the equalists?"
                            tn "not yet."
                            lin "then i suggest you start walking the streets."
                            jump lin_menu

                    if lin_hj2 and not lin_equalist_warning:
                        tn "I have something to report."
                        lin "why didn't you tell me earlier?"
                        tn "you... you were too busy eating my nut!"
                        lin "no excuse."
                        lin "what is it?"
                        tn "...."
                        tn "the equalists are planning some kind of event."
                        lin "hmm... what else?"
                        tn "they have some kind of zappy things... that may or may not involve nipple play."
                        tn "it was a little confusing."
                        lin "that's not very helpful."
                        lin "you heard this at the arena?"
                        tn "yup."
                        lin "hmm... that might be where it'll happen, then."
                        lin "i'll direct some patrols there."
                        tn "cool."
                        lin "and tenzin..."
                        tn "hm?"
                        lin "...thanks."
                        tn "you're wel-"
                        hide bfaa with dissolve
                        show bfaa bfaa01 with dissolve
                        lin "dismissed."
                        tn "...."
                        tn "dick."
                        $ lin_equalist_warning = True
                        jump b4_repcity_map1

                    if lin_hj and not probending_first:
                        jump lin_bending_job

                    if not lin_hj:
                        lin "do you have my money yet?"
                        lin "i'm not giving you that job until you do."
                        menu:
                            "yes - 100 coins":
                                if bk4_money >=100:
                                    tn "here, you big-titted jerk."
                                    play sound "audio/money.mp3"
                                    $ bk4_money -=100
                                    $ lin_hj = True
                                    jump lin_handjob1
                                else:
                                    lin "you're a terrible liar, tenzin."
                                    lin "come back when you have it."
                                    jump b4_repcity_map1
                            "no":

                                tn "uh... do we really own anything?"
                                lin "...come back when you have 100 coins for me."
                                jump b4_repcity_map1
                    else:
                        lin "i'm busy, tenzin."
                        jump lin_menu

                "jerk off" if lin_hj2:
                    jump lin_handjob3

                "buttjob" if lin_buttstuff:
                    jump lin_buttjob2

                "pussy rub" if lin_rub_equal >=3:
                    tn "I was thinking..."
                    jump lin_rub2
                "exit":

                    jump b4_repcity_map1

    "test"

label bk4_alleys1:



    if meelo_stall ==1:
        sg "hey, i found this rock."
        play sound "audio/win2.mp3"
        "you got a rock!"
        sg "looks dumb."
        sg "like a kid's toy."
        tn "it's useful, believe me."
        sg "no."
        tn "...."
        $ meelo_stall = 2
    if meet_kyoshi >=1 and not shady_store_minded:
        sg "hey, watch the store for me."
        tn "what? no."
        sg "come on, i need to get some shit."
        sg "trust me, you'll love it."
        tn "...."
        tn "what stuff?"
        sg "no, no, no, you gotta agree first."
        sg "so whadda ya say?"
        sg "watch the store?"
        menu:
            "mind the store":
                $ shady_store_minded = True
                tn "sure, i can do th-"
                hide bfah with dissolve
                tn "-at."
                tn "...."
                tn "alright, now what?"
                tn "......."
                tn "............"
                tn "i can't believe he left me with all this merchandise."
                menu:
                    "look through it":
                        tn "let's take a peek."
                        "you rummage around his various for-sale items."
                        tn "...this is all crap."
                        menu:
                            "take the rusty shield":
                                hide screen bk4_money_date
                                show black with Dissolve(1)
                                show text "{color=#ffffff}the power of the guardian.\nkindness to aid friends.\na shield to repel all."
                                with dissolve
                                $ shady_power = "shield"
                            "take the rusty sword":

                                hide screen bk4_money_date
                                show black with Dissolve(1)
                                show text "{color=#ffffff}the power of the warrior.\ninvincible courage.\na sword of terrible destruction."
                                with dissolve
                                $ shady_power = "sword"
                            "take the rusty wand":

                                hide screen bk4_money_date
                                show black with Dissolve(1)
                                show text "{color=#ffffff}the power of the mystic.\ninner strength.\na staff of wonder and ruin."
                                with dissolve
                                $ shady_power = "wand"
                    "watch the alley":


                        tn "i don't want him mad at me."
                        hide screen bk4_money_date
                        show black with Dissolve(1)
                        show text "{color=#ffffff}the power of the sage.\nwisdom and patience.\na mind of focus and determination."
                        with dissolve
                        $ shady_power = "mind"

                show ctc
                pause
                hide ctc
                hide text with Dissolve(1)
                play sound "audio/win2.mp3"
                show text "{color=#ffffff}you have gained the power of the [shady_power]."
                with Dissolve(1)
                show ctc
                pause
                hide ctc
                hide text with Dissolve(1)
                hide black
                show screen bk4_money_date
                with Dissolve(1)
                tn "........."
                tn "....what just happened?"
                tn "....."
                tn "..........."
                tn "no, seriously, what just happened?!"
                show bfal bfal04 with dissolve
                e1 "hello, new friend."
                tn "...hi?"
                tn "i'm sort of in the middle of something."
                e1 "oh."
                e1 "does that mean i can't get new batteries for my shocker weapon thing?"
                e1 "and... some nipple cream?"
                tn "...."
                e1 "......"
                tn "i don't know if i have that."
                e1 "where's shady?"
                tn "he's out."
                tn "let me look...."
                tn "oh, here."
                tn "with a note that says \"the usual\"."
                tn "i guess this is for you."
                e1 "thanks buddy."
                hide bfal with dissolve
                play sound "audio/money.mp3"
                $ bk4_money +=15
                "you made 15 coins!"
                tn "neat."
                tn "....."
                tn "now what?"
                tn "and what was that power thing?"
                show black with dissolve
                "you wait impatiently but nothing else happens."
                hide black with dissolve
                tn "I'm boooooooooored."
                show bfah bfah01 with dissolve
                sg "ask and ye shall receive, brother."
                tn "oh, hey."
                tn "so this weird thing happened..."
                sg "tom? yeah, he does that."
                sg "did you give him his usual package?"
                tn "no, not... well, yeah, but i mean... there was thing thing with a [shady_power] power..."
                sg "oh yeah, don't worry about that."
                tn "...what do you mean \"don't worry about that\"?"
                tn "how can i not worry about that."
                sg "if it becomes important, you'll figure it out."
                if shady_power == "mind":
                    sg "i appreciate you not sorting through my trash, though."
                else:
                    sg "you cleaned up some of my trash, though."
                tn "that was {i}trash{/i}?!"
                sg "well, yeah."
                sg "you don't think i'd leave you in charge of actual merchandise unsupervised do you?"
                tn "i mean..."
                sg "tell you what, take this for your trouble."
                hide screen bk4_money_date
                show black
                with Dissolve(1)
                tn "no, no, no..."
                show text "{color=#ffffff}the power of the friend.\nloyal tenacity.\na gift of comfort and ferocity."
                with Dissolve(1)
                show ctc
                pause
                hide ctc
                hide text with Dissolve(1)
                tn "stop it."
                play sound "audio/win2.mp3"
                show text "{color=#ffffff}you have gained the power of shady's friendship."
                with Dissolve(1)
                show ctc
                pause
                hide ctc
                hide text with Dissolve(1)
                hide black
                show screen bk4_money_date
                with Dissolve(1)
                tn "....."
                tn "...why?"
                sg "have a good day!"
                tn "how?"
                jump b4_repcity_map1
            "not now":

                tn "i'm not really feeling it."
                sg "boo."
                jump bk4_alley_menu

    if korra_scroll2 >=1 and not statue_key_talk:
        $ statue_key_talk = True
        sg "hey, i found a key!"
        sg "don't know what it does or where it goes!"
        sg "intriguing, right?"

    if bk4_swim_mission >=5 and not shady_air_scroll:
        sg "man, i've got something for you."
        sg "you're gonna be fucking thrilled."
        tn "what is it?"
        sg "guess."
        tn "is-"
        sg "{size=+10}it's an airbending scroll!" with hpunch
        sg "duuuuuude!"
        sg "am i your favorite person or what?"
        tn "you're definitely up there."
        tn "thanks for finding that."
        sg "you are welcome, my man."
        tn "....."
        tn "so...."
        sg "...what?"
        tn "where is it?"
        sg "in the shop."
        tn "man, you... i have to buy it?"
        sg "well, duh."
        tn "...you misled me."
        sg "but i {i}have{/i} it, and that is a nifty thing."
        $ shady_air_scroll = True
        jump bk4_alley_menu

    if bk4_shady_meet:
        if missing_meelo ==1:
            tn "meelo's not here."
        jump bk4_alley_menu

    if not bk4_shady_meet:
        sg "hey, buddy."
        tn "so what's happening here?"
        sg "i've got all {i}kinds{/i} of good shit for sale."
        tn "....."
        tn "............"
        sg "what?"
        tn "i'm sorry, i just have to ask..."
        tn "are you... shady?"
        sg "excuse me?"
        sg "i, sir, am legitimate!"
        tn "no, i mean your name."
        tn "is your name \"shady\"?"
        sg "oh. yeah."
        sg "why?"
        tn "just... how old are you?"
        tn "are you shady's son? or..."
        sg "*sigh*"
        sg "it's a long story."
        tn "what's the short story?"
        sg "i'm accidentally immortal."
        tn "...what?"
        sg "i... didn't mean to do it, but it happened."
        sg "now i can't die or age."
        sg "i don't want to get into it."
        sg "need a watch? or some exercise equipment?"
        tn "you're... immortal..."
        sg "yeah."
        tn "and you... sell watches? in an alley?"
        sg "man's gotta make a living."
        tn "..."
        tn "just show me your wares."
        sg "sure."
        $ bk4_shady_meet = True
    jump bk4_alley_menu

label bk4_alley_menu:
    menu:
        "exercise equipment - 15 ([korra_gift] owned)":
            if bk4_money >=15:
                $ bk4_money -=15
                $ korra_gift +=1
                play sound "audio/money.mp3"
                "you got some exercise equipment!"
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "watch - 30" if not shady_watch:
            if bk4_money >=30:
                $ bk4_money -=30
                $ shady_watch = True
                play sound "audio/money.mp3"
                "you got a watch!"
                sg "...really?"
                sg "I didn't think you'd buy that."
                tn "should i not have?"
                sg "no, no, it's... fine."
                tn "....."
                tn "...take it back."
                sg "no."
                tn "no, give me my money back."
                tn "I don't want this."
                sg "no refunds."
                tn "....i'm gonna regret buying this, aren't i?"
                sg "who's to say?"
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "mysterious key - 30" if korra_scroll2 >=1 and not statue_key:
            if bk4_money >=30:
                $ bk4_money -=30
                $ statue_key = True
                play sound "audio/money.mp3"
                "you got a mysterious key!"
                sg "so myserious!"
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "korra swimsuit - 25(locked)" if bk4_swim_mission ==0:
            "test"
        "korra swimsuit - 25" if bk4_swim_mission ==1 and not korra_swimsuit:
            if bk4_money >=25:
                $ bk4_money -=25
                $ korra_swimsuit = True
                play sound "audio/money.mp3"
                "you got korra's swimsuit!"
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "pema swimsuit - 25(locked)" if bk4_swim_mission ==0:
            "test"
        "pema swimsuit - 25" if bk4_swim_mission ==1 and not pema_swimsuit:
            if bk4_money >=25:
                $ bk4_money -=25
                $ pema_swimsuit = True
                play sound "audio/money.mp3"
                "you got pema's swimsuit!"
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "kid swimsuits - 25(locked)" if bk4_swim_mission ==0:
            "test"
        "kid swimsuits - 25" if bk4_swim_mission ==1 and not kids_swimsuit:
            if bk4_money >=25:
                $ bk4_money -=25
                $ kids_swimsuit = True
                play sound "audio/money.mp3"
                "you got the kid swimsuits!"
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "airbending scroll - 40" if air_scroll ==0 and bk4_swim_mission >=5:
            if bk4_money >=40:
                $ bk4_money -=40
                $ air_scroll = 1
                play sound "audio/win2.mp3"
                "you got an airbending scroll!"
                tn "neat."
                tn "i should figure out what to do with this."
                tn "maybe show it to korra?"
                tn "she can't know what i'm doing though..."
                tn "maybe i can have her figure it out and pretend i'm teaching her?"
                tn "...i'll wing it."
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu
        "micro swimsuit - 40" if korra_tits_out and not micro_suit:
            if bk4_money >=40:
                $ bk4_money -=40
                $ micro_suit = True
                play sound "audio/win2.mp3"
                "you got a micro swimsuit."
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu
        "amon outfit - 50" if meet_kyoshi >=1 and not amon_outfit and shady_store_minded:
            if bk4_money >=50:
                $ bk4_money -=50
                $ amon_outfit = True
                play sound "audio/win2.mp3"
                "you got the amon outfit."
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu

        "rope - 30" if meet_kyoshi >=1 and not bk4_rope and shady_store_minded:
            if bk4_money >=30:
                $ bk4_money -=30
                $ bk4_rope = True
                play sound "audio/win2.mp3"
                "you got the rope."
                jump bk4_alley_menu
            else:
                sg "not enough money, mate..."
                jump bk4_alley_menu
        "exit":

            jump b4_repcity_map1

label bk4_park1:



    if missing_meelo >=2:
        show bfae meelo_01
        with dissolve
        jump meelo_menu

        label meelo_menu:
            menu:
                "talk":
                    mee "poops!"
                    tn "...right."
                    jump meelo_menu
                "sort coins":

                    if meelo_stall >=1 and meelo_stall <3:
                        tn "meelo's waiting for me in my study."
                        jump b4_repcity_map1
                    if not bk4_coins_daily:
                        $ temp_int = 0
                        jump three_in_one
                    else:
                        mee "all the coins for today!"
                        mee "come back tomorrow!"
                        jump meelo_menu
                "exit":

                    jump b4_repcity_map1

    if missing_meelo ==1:
        show bfae meelo_02
        with dissolve
        mee "hello!"
        tn "meelo!"
        tn "what the heck are you doing here?"
        mee "um... coins."
        tn "what?"
        mee "coins in the water."
        tn "ah, making a little spare change, huh?"
        tn "i can respect that."
        tn "but you need to get back to your mother."
        mee "kay!"
        tn "how much-"
        play sound "audio/thud.mp3"
        with hpunch
        "meelo slams down a giant bag of coins."
        tn "......"
        tn "what the shit."
        mee "lots of coins come through the water every day!"
        tn "uh... what... uh... can i have some?"
        mee "no!"
        tn "come on little dude."
        mee "hmmm...."
        mee "help me sort it into piles of three and you can keep some, okay?"
        tn "uh... sure."
        $ temp_int = 0
        jump three_in_one

    if not park_equalists:
        show bfal bfal01
        with dissolve
        e1 "alright people!"
        e1 "we are here to protest the unfairness of these benders!"
        e1 "we will no longer be subjucated to their unfair treatment!"
        e1 "join the-"
        show bfal bfal02 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "what are you people doing?"
        e1 "that's not how you protest!"
        e1 "get your... get that out of his mouth!"
        e1 "stop that!"
        e1 "this is a public park!"
        e1 "there are children around!"
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "are. you. quite. finished."
        e1 "....then shut up."
        show bfal bfal03 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "i said shut up!!"
        e1 "yes, you, with the thing!"
        e1 "i see you making that face!"
        e1 "don't make me come over there!"
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "oh, okay, yeah, real mature."
        e1 "everyone can see your butt, you know."
        e1 "it's embarrassing."
        e1 "for you."
        e1 "i'm fine."
        e1 "okay, that's it..."
        e1 "todd! get out here!"
        show bfal04 with dissolve
        e2 "hm?"
        e2 "I was eating a sandw-"
        e1 "go get that guy."
        e2 "which one?"
        e1 "the one mooning me!"
        e2 "where?"
        show bfal bfal03 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "over there! go get him!"

        e2 "on it."
        hide bfal04
        show bfal bfal01
        with dissolve
        e1 "see!"
        e1 "that's what happens when you oppose-"
        show bfal bfal02 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "no! no no no!"
        e1 "that's a lady!"
        e1 "todd, what the hell are you doing!?"
        e1 "leave her alone! those are her real teeth!"
        e1 "stop! just stop!"
        e1 "go sit down."
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "okay, this is harder than i thought it would be."
        crowd "{size=-5}you look like a twat!"
        e1 "{size=+5}I'm ignoring you, sir!"
        e1 "ahem, look..."
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "{size=+10}are you tired of living under the tyranny of benders?"
        crowd "{size=-5}i'm tired of living under the tyranny of your mum!"
        crowd "{size=-5}she keeps waking me up to suck my dick and i'm running out of hiding places!"
        e1 "......."
        show bfal bfal05 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "{size=+10}....then join the equalists!"
        e1 "{size=+10}for too long, the benders of this city have forced the non-benders to live as lower-class citizens!"
        crowd "{size=-5}lower-class citizen? i've gone into severe debt to afford the erection pills and stunt doubles necessary to keep your mum from handling my scoops at all hours!"
        e1 "...can we {i}please{/i} get off my mother?"
        crowd "{size=-5}if she'll get off of me!"
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "...you know what, that's my fault for engaging."
        e1 "ahem."
        show bfal bfal05 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "{size=+10}join amon and together we will tear down the bending establishment!"
        e1 "{size=+10}soon, the benders of this city will fear him and his power!"
        e1 "{size=+10}he can remove their bending!"
        e1 "{size=+10}how's that sound!?"
        crowd "{size=-5}can he remove your mum's bending? my hips are sore!"
        show bfal bfal03 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "that's it!"
        e1 "fuck you!"
        e1 "it's go time!"
        e1 "i'm going to put my whole fist up your ass!"
        crowd "{size=-5}just like your mother!"
        show bfal bfal02 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "{size=+10}ararghghghgh!!!"
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "i hate you."
        tn "......"
        tn "who is this weirdo?"
        tn "man, people and their cosplays, am i right?"
        show bfal04:
            zoom 1.5 xpos -300
        with dissolve
        e2 "you are not wrong, my dude."
        tn "whoa, you are {i}awfully{/i} close to me right now."
        tn "also, aren't you... with him?"
        e2 "oh. uh, yeah, i think so."
        e2 "i'm new here."
        e2 "hi, i'm todd."
        tn "i really don't care, tom."
        e2 "aw..."
        show bfal bfal02 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "todd! get backstage!"
        e2 "oh, sorry, gotta go!"
        hide bfal04 with dissolve
        e1 "fucking..."
        show bfal bfal01 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "alright, now it's time for our chant!"
        e1 "we found an ancient song that's perfect for the downtrodden like us!"
        e1 "it was lost to time, but we equalists have pulled it from the depths of history!"
        e1 "it shall never again be forgotten!"
        e1 "the words of the poet will live on in infamy, and in our hearts!"
        e1 "ready?"
        show bfal bfal03 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "{size=+6}{b}you{/b} crank that soulja, watch me {b}you{/b} crank that soulja-"
        tn "i.... think that's my cue."
        tn "i'm gonna leave before these furries start keyforging."
        show bfal bfal03 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
        e1 "{size=+6}now {b}you{/b} crank that soulja-"
        $ park_equalists = True
        $ lin_equalists += 1
        jump b4_repcity_map1
    else:
        tn "nothing here right now."
        jump b4_repcity_map1

label bk4_statue1:



    if lin_butt_quest >=1:
        menu:
            "Visit statue":
                jump b4_label_sai_arrival
            "Visit city streets":

                jump b4_label_citystreets_arrival
            "exit":




                jump b4_repcity_map1
    else:

        tn "that's... like... all the way over there."
        if missing_meelo ==1:
            tn "meelo won't be there."

        jump b4_repcity_map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
