init:
    $ bk3_loveroute = False
    default temp_list = []


screen love_basingse_map:

    imagemap:

        ground "ebackgrounds/basingse_city_1.jpg"
        hover "ebackgrounds/basingse_imagemap/basingse_icons.png"
        idle "ebackgrounds/basingse_imagemap/basingse_locations.png"

        hotspot (31, 45, 278, 223) clicked Jump("love_bk3_jasmine")
        hotspot (754, 33, 217, 220) clicked Jump("love_bk3_palace")
        hotspot (411, 37, 214, 213) clicked Jump("love_bk3_fountain")
        hotspot (772, 318, 213, 217) clicked Jump("love_bk3_market")
        hotspot (99, 472, 167, 166) clicked Jump("love_bk3_home")
        hotspot (403, 331, 216, 211) clicked Jump("love_bk3_arena")


    add "emberisland_cloud1"

    if earthbending < 30:
        if we_poor:
            add "calender_and_money.png"
            hbox:
                xalign 0.6
                yalign 0.02
                text "[emoney]"
            hbox:
                xalign 0.45
                yalign 0.02
                text "[ecalendar]"

        if bk3_village_access:
            imagebutton idle "bk3/icons/bk3_village_off.png" hover "bk3/icons/bk3_village_on.png" xpos 0.25 ypos 0 action Jump("love_bk3_village")




        if bk3_stats:
            imagebutton idle "stats_button.png" hover "stats_button_dark.png" xpos 0.7 ypos 0 action [ Jump("stat_screen_earth_day")]

        if bk3_day and laogai_travel:
            imagebutton idle "bk3/icons/bk3_maze_off.png" hover "bk3/icons/bk3_maze_on.png" xpos 0.18 ypos 0 action Jump("love_bk3_maze_start1")


screen love_basingse_night_map:

    imagemap:

        ground "ebackgrounds/basingse_city_night.jpg"
        hover "ebackgrounds/basingse_imagemap/basingse_icons.png"
        idle "ebackgrounds/basingse_imagemap/basingse_locations.png"

        hotspot (31, 45, 278, 223) clicked Jump("love_bk3_jasmine_night")
        hotspot (754, 33, 217, 220) clicked Jump("love_bk3_palace_night")
        hotspot (411, 37, 214, 213) clicked Jump("love_bk3_fountain_night")
        hotspot (772, 318, 213, 217) clicked Jump("love_bk3_market_night")
        hotspot (99, 472, 167, 166) clicked Jump("love_bk3_home_night")
        hotspot (403, 331, 216, 211) clicked Jump("love_bk3_arena_night")


    if we_poor:
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[emoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ecalendar]"

    if bk3_village_access and suki_tylee !=4:
        if (party_plan_explained and not party_complete) or love_suki_hypno ==11:
            add "transparent.png"
        else:
            imagebutton idle "bk3/icons/bk3_village_off.png" hover "bk3/icons/bk3_village_on.png" xpos 0.25 ypos 0 action Jump("love_bk3_village_night")




    if bk3_stats:
        imagebutton idle "stats_button.png" hover "stats_button_dark.png" xpos 0.7 ypos 0 action [ Jump("stat_screen_earth_day")]




label love_basingse_day1:
    stop music fadeout 1
    play music "audio/jangles.mp3"

    if not bk3_day:
        jump love_basingse_night1
    else:

        scene black
        scene basingse_city_1
        show screen earth_money_date
        with dissolve

        call screen love_basingse_map

label love_basingse_night1:
    if suki_tylee ==4 and not find_suki_self:
        $ find_suki_self = True
        y "i need to find suki!"
        jump love_basingse_night1
    if bk3_day:
        jump love_basingse_day1
    else:
        hide screen earth_money_date
        scene black
        scene basingse_city_night
        with dissolve
        call screen love_basingse_night_map

label love_bk3_jasmine:


    if earthbending >= 30:

        scene jasmin_dragon_inside

        if 'jasmine' in temp_list:
            show expression "ebackgrounds/basingse_city_1.jpg"
            y "I've already been there."
            call screen love_basingse_map
        $ temp_list.append('jasmine')


        show toii toii03
        iroh "*Sluuurrp*"
        y "IROHH!!!"
        show toii toii06
        iroh "What?! what is it!?"
        y "Have you seen Katara somewhere around?"
        iroh "The sassy watertribe girl with that nice round..."
        y "Yes! Have you?! There's all sorts of shit going on with Azula and I'm super worried."
        iroh "Sorry, I haven't seen her."
        iroh "My nephew is gone too."
        y "Then why are you just sitting here?"
        show toii toii04
        iroh "Azula has captured him and I don't know where she's keeping him."
        show toii toii02
        iroh "I'm waiting for the right opportunity and some information to free him."
        iroh "don't worry about Katara."
        iroh "She's a strong, smart girl."
        iroh "I'm sure she's okay."
        iroh "If i see her, I'll make sure to send her your way."
        iroh "Maybe we can help each other later."
        iroh "I'm certain we'll meet again."
        y "Okay, thanks for everything!"
        y "You're my favorite uncle."
        show toii toii07
        iroh "But I'm not your-"
        y "Sorry! Gotta go!"

        scene black with Dissolve(1.5)
        call screen love_basingse_map 


    if love_toph_sex and iroh_market < 2:
        y "there's a note on the door..."
        "\"gone to the market, anyone is welcome to join me.\"\n-iroh"
        y "huh."
        y "i'll go look in the market for him, then."
        $ iroh_market = 1
        jump love_basingse_day1

    if love_jin_freed and not love_jin_brothel:
        if jin_brothel_talk:
            stop music
            play music "audio/Ripples.mp3"
            scene jasmin_dragon_inside
            show tojn tojn20
            with dissolve
            jin "hello!"
            jin "any chance you have a room to rent?"
            menu:
                "i do":
                    if love_suki_hypno <13:
                        y "(i should deal with suki's side effects first, since she's been out longer.)"
                        y "i don't have anything for you yet, jin."
                        y "but i should soon."
                        y "be patient, okay?"
                        jin "all right..."
                        jump love_basingse_day1
                    else:
                        y "come live at the brothel."
                        jin "really?!"
                        jin "can i... i mean... do i have to work there?"
                        y "let's talk about that later."
                        y "first, let's get you set up."
                        if brothel_building <2:
                            y "oh, wait."
                            y "shit."
                            jin "what?"
                            y "I don't think there's room for you yet."
                            jin "oh..."
                            jin "that's alright."
                            jin "let me know if that changes."
                            jump love_basingse_day1
                        else:
                            jin "great!"
                            jin "i'll head on over!"
                            $ love_jin_brothel = True
                            jump love_basingse_day1
                "not right now":
                    y "nothing at the moment."
                    jin "oh... okay."
                    jin "let me know if that changes."
                    jump love_basingse_day1
        else:
            $ jin_brothel_talk = True
            stop music
            play music "audio/Ripples.mp3"
            scene jasmin_dragon_inside
            show tojn tojn20
            with dissolve
            jin "hello!"
            y "oh hey, it's you."
            show tojn tojn23 with dissolve
            jin "have we met?"
            y "we... had sex in the tunnels."
            jin "that was you?"
            show tojn tojn20 with dissolve
            jin "great!"
            y "How can... how do you not remember me?"
            jin "honestly, i was... basically out of my mind with lust."
            jin "i barely remember the last week..."
            show tojn tojn24 with dissolve
            jin "...other than the agony of constant orgasm denial."
            jin "......"
            show tojn tojn20 with dissolve
            jin "but that's over with!"
            show tojn tojn24 with dissolve
            jin "of course, now i don't know what to do with myself...."
            y "well, you seem to have found a place to stay, at least."
            jin "i guess?"
            jin "the old guy is super creepy."
            show toii toii06:
                xpos -675
            with moveinleft
            iroh "......"
            hide toii with moveoutleft
            y "right..."
            y "i see what you mean."
            show tojn tojn20 with dissolve
            jin "oh, well."
            jin "i'll... figure something out."
            jin "maybe i'll give some blowjobs."
            jin "try to make some rent money so i can stay somewhere else."
            y "...seriously?"
            jin "yeah, i'm still...."
            show tojn tojn24 with dissolve
            jin "i'm still... super horny all the time."
            jin "i just... i want so much sex."
            jin "I think... ajala broke me."
            show tojn tojn20 with dissolve
            jin "but i really don't mind... i think."
            y "......"
            y "can i help?"
            jin "maybe....."
            jin "any chance you have a room to rent?"
            menu:
                "i do":
                    if love_suki_hypno <13:
                        y "(i should deal with suki's side effects first, since she's been out longer.)"
                        y "i don't have anything for you yet, jin."
                        y "but i should soon."
                        y "be patient, okay?"
                        jin "all right..."
                        jump love_basingse_day1
                    else:

                        y "come live at the brothel."
                        jin "really?!"
                        jin "can i... i mean... do i have to work there?"
                        y "let's talk about that later."
                        y "first, let's get you set up."
                        if brothel_building <2:
                            y "oh, wait."
                            y "shit."
                            jin "what?"
                            y "I don't think there's room for you yet."
                            jin "oh..."
                            jin "that's alright."
                            jin "let me know if that changes."
                            jump love_basingse_day1
                        else:
                            jin "great!"
                            jin "i'll head on over!"
                            $ love_jin_brothel = True
                            jump love_basingse_day1
                "not right now":
                    y "nothing at the moment."
                    jin "oh... okay."
                    jin "let me know if that changes."
                    jump love_basingse_day1

    if toph_chat == 11 and not footjob_book and not iroh_book_talk:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii01
        with dissolve
        "you sneak into the jasmine dragon."
        y "hey... do you happen to have any books?"
        iroh "i..."
        show toii toii02 with dissolve
        iroh "...don't?"
        y "....."
        y "you hesitated."
        show toii toii06 with dissolve
        iroh "i mean..."
        y "....."
        y "...you have smut."
        iroh "wellll..."
        iroh "........"
        show toii toii03 with dissolve
        iroh "i have smut."
        y "can i have some?"
        iroh "you...."
        show toii toii07 with dissolve
        iroh "...want my smut novel?"
        y "i guess?"
        y "i don't have a lot of options here."
        iroh "well... "
        show toii toii01 with dissolve
        iroh "...how close of friends are we gonna be?"
        y "the... best?"
        iroh "........."
        show toii toii05 with dissolve
        iroh "okay, then!"
        y "great, hand it over."
        show toii toii07 with dissolve
        iroh "what?"
        show toii toii02 with dissolve
        iroh "oh, it's not here."
        show toii toii03 with dissolve
        y "...."
        y "then where is it?!"
        show toii toii02 with dissolve
        iroh "i may have...."
        show toii toii03 with dissolve
        iroh "left it in the village."
        y "you're killing me, man."
        y "why is it in the village?"
        show toii toii06 with dissolve
        iroh "well..."
        show toii toii01 with dissolve
        iroh "...remember that night i went over there, and got shooed off..."
        show toii toii06 with dissolve
        iroh "rather forcefully..."
        show toii toii05 with dissolve
        iroh "by that beautiful, ample-bosomed june?"
        y "yes."
        show toii toii01 with dissolve
        iroh "oh! it was the night of your house fire!"
        iroh "remember that?"
        y "....."
        y "i vaguely remember my house burning down, yes."
        show toii toii02 with dissolve
        iroh "well... i might have had..."
        show toii toii03 with dissolve
        iroh "...a request."
        y "so, you brought the smutty novel with you because it had a sex act you wanted done on you?"
        y "and you lost it when you were forced to leave."
        show toii toii02 with dissolve
        iroh "........"
        show toii toii03 with dissolve
        iroh "....yes."
        y "....."
        y "you're a pain in my ass, man."
        show toii toii05 with dissolve
        iroh "enjoy!"
        $ iroh_book_talk = True
        jump love_basingse_day1


    if juneshadytalk and not irohshadytalk:
        $ irohshadytalk = True
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        iroh "hello, stra-"
        ya "did you burn my house down, asshole?"
        iroh "i..."
        show toii toii07 with dissolve
        iroh "what?"
        ya "did. you. burn. my. house. down."
        show toii toii02 with dissolve
        iroh "hmmm..."
        show toii toii03
        show toii_blink
        with dissolve
        iroh "*slurp*"
        ya "answer me, man!"
        show toii toii02 with dissolve
        iroh "ahh..."
        hide toii_blink with dissolve
        iroh "you seem very worked up."
        show toii toii05 with dissolve
        iroh "you should drink some tea!"
        ya "I will shit in your tea, old man!"
        show toii toii06 with dissolve
        iroh "well that's very aggressive...."
        ya "i'm not in a joking mood."
        ya "i'm in a \"murder a would-be murderer\" mood."
        show toii toii07 with dissolve
        iroh "...that's a very specific mood."
        ya "i know what i'm about!"
        iroh "well, i don't."
        show toii toii05 with dissolve
        iroh "sit and chat with me over a cup of-"
        ya "i'm not going to drink tea!"
        show toii toii03 with dissolve
        iroh "your loss."
        ya "okay, i'm just gonna beat your head in."
        show toii toii05 with dissolve
        iroh "whoa, whoa, whoa, stranger..."
        show toii toii04 with dissolve
        iroh "just try it."
        y "...."
        show toii toii05 with dissolve
        iroh "so, how can i help you?"
        y "ugh... for the last time, did you burn down my house last night?"
        show toii toii07 with dissolve
        iroh "why would i burn down a house?"
        y "i don't know! why would you?"
        y "you were seen in the village last night."
        show toii toii06 with dissolve
        iroh "oh, that was..."
        iroh "...unrelated."
        y "the brothel, right?"
        show toii toii05 with dissolve
        iroh "what can i say? i love beautiful women."
        show toii toii01 with dissolve
        iroh "and there's a beautiful woman there now."
        iroh "she used to be at the tavern, but now-"
        ya "i don't care."
        ya "so you didn't burn my house down?"
        show toii toii05 with dissolve
        iroh "heavens, no!"
        ya "then why didn't you say so?"
        show toii toii01 with dissolve
        iroh "calm down."
        show toii toii05 with dissolve
        iroh "have a cup of tea."
        y "....."
        y "...i might."
        y "i'm very stressed right now."
        y "and... i have no leads."
        show toii toii01 with dissolve
        iroh "hmmm..."
        iroh "i can't help you, i'm afraid."
        y "....figures."
        show toii toii05 with dissolve
        iroh "have a nice day!"
        y "....somehow, i doubt it."
        jump love_basingse_day1

    if iroh_battle_count >=6:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        iroh "hello, stranger."
        iroh "relax for a bit, have a cup of tea."
        show toii toii03
        show toii_blink
        with dissolve
        "you sit and sip tea in silence for a bit."
        "it's very relaxing."
        jump love_basingse_day1

    if iroh_battle_convo and iroh_battle_count <=5:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        menu:
            "challenge iroh's crabs":
                y "up for a fun pocket crab battle?"
                iroh "i'm here to drink tea and kick ass."
                iroh "and i'm all out of tea."
                $ iroh_fun_battle = True
                jump bk3_arena_start_shit
            "relax":

                iroh "good decision."
                iroh "i have never found a problem that a good cup of tea can't solve."
                show toii toii03
                show toii_blink
                with dissolve
                "you sit and sip tea in silence for a bit."
                "it's very relaxing."
                jump love_basingse_day1
            "exit":

                jump love_basingse_day1


    if first_arena_match and not iroh_battle_convo:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        y "iroh, have you played pocket crabs?"
        iroh "hmmm... i don't think so."
        y "do you have any crabs?"
        iroh "....that's awfully personal."
        y "i meant for battling, you syphilis-ridden cockhound."
        iroh "oh."
        iroh "well, i do...."
        iroh "i just don't know how it all works."
        y "let's play and you'll pick it up."
        iroh "sure."
        $ iroh_battle_convo = True
        $ iroh_fun_battle = True
        jump bk3_arena_start_shit


    if katara_found and not first_arena_match:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        iroh "hello, stranger."
        iroh "relax for a bit, have a cup of tea."
        show toii toii03
        show toii_blink
        with dissolve
        "you sit and sip tea in silence for a bit."
        "it's very relaxing."
        jump love_basingse_day1



label love_bk3_jasmine_night:
    if suki_tylee ==4:
        stop music
        play music "audio/Ripples.mp3"
        scene black
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        $ suki_tylee = 5
        jump dl_capture

    if jasmine_raid:
        y "these guards are already taken care of."
        jump love_basingse_night1

    if party_plan_explained and not party_complete:
        y "i need to meet katara and toph at the palace."
        jump love_basingse_night1
    if love_suki_hypno == 11 and not jasmine_raid:
        $ jasmine_raid = True
        stop music
        play music "audio/Ripples.mp3"
        scene black
        scene jasmin_dragon_inside
        show toeg toeg01
        show guardb_body_1:
            xpos -500
        with dissolve
        dl1 "hey, while we're stuck here..."
        dl2 "what?"
        dl1 "well... i'm embarrassed to ask."
        dl2 "no, i don't have a pony fetish, stop asking."
        dl2 "and please stop sending me those disturbing party invites."
        dl1 "oh, not that."
        dl1 "i was just wondering... do you like the tea here?"
        dl2 "what? no."
        dl2 "who likes tea?"
        dl1 "a lot of people like tea."
        dl2 "eh."
        dl2 "it's just hot leaf juice."
        play sound "audio/door_slam.mp3"
        with sshake
        dl1 "did... you feel that?"
        dl2 "yeah, sounded like a door slam and angry footsteps-"
        show toii toii04:
            xzoom -1
        with moveinleft
        hide toeg
        hide guardb_body_1
        hide toii
        with moveoutright
        play sound "audio/thud.mp3"
        iroh "aaaghghhhh!!!!!" with hpunch
        dl "aaahhh!!!!"
        iroh "how dare you!"
        play sound "audio/thud.mp3"
        with hpunch
        dl "i'm sorry!"
        iroh "you {i}will{/i} be!"
        play sound "audio/thud.mp3"
        with hpunch
        "you hear horrific screaming that slowly dies down into a kind of hideous gurgling."
        show tosi tosi10:
            xzoom -1
        with dissolve
        suki "hey, you got ahead of me."
        suki "where are...."
        suki "..........."
        suki "is that old man..."
        suki "....waterboarding them with tea?"
        y "yeah."
        y "Looks like he's taking care of them for us."
        suki "agreed."
        y "we should probably scooch on out of here."
        y "he is maaaaad."
        suki "i'm right behind you."
        suki "...and what a cute behind it is."
        y "i'm... not sure what to do with that."
        suki "i have some ideas."
        y "I don't like that. stop that."
        hide tosi with dissolve
        y "did she just wink at me?"
        jump love_basingse_night1



label love_bk3_fountain:


    if earthbending == 30:
        scene bk3_bg_fountain
        if 'fountain' in temp_list:
            show expression "ebackgrounds/basingse_city_1.jpg"
            y "I've already been there."

            call screen love_basingse_map
        $ temp_list.append('fountain')

        if love_jet_freed:

            show expression "maze/jet_stand.png"
            "Jet" "Hey look, it's my savior! Offer still stands, my man."
            y "Let's keep it that way."
            hide expression "maze/jet_stand.png" with dissolve
            show tosb tosb00:
                xpos 300
                linear 1.0 xpos 0
            sb "Thanks again for saving Jet!"
            sb "He's grown tired of BasingSe, too many bad memories, so we'll move somewhere else."
            sb "Maybe a small village..."
            y "I know a pretty cool one nearby, but more importantly..."
            y "Did you see Katara?"
            sb "Not a glimpse, why?"
            y "It's probably nothing, but you should really go to the village."
            y "Soon. Like today soon. Promise?"
            sb "If you think that's for the best."
            y "I do. Okay, gotta go."
        else:
            y "Shit. Nothing here."

        scene black with Dissolve(1.5)
        call screen love_basingse_map

    if earthbending == 31:
        show expression "ebackgrounds/basingse_city_1.jpg"
        show expression "ebackgrounds/basingse_city_night.jpg" with Dissolve(2.0)
        y "Shit... it's already getting dark."
        jump b3love_theend
        call screen love_basingse_map

    scene black
    scene bk3_bg_fountain
    with dissolve
    hide screen earth_money_date


    if love_jet_freed and not love_smellerbee_sex:
        $ love_smellerbee_sex = True
        jump smellerbee_fuck

    if jin_quick_talk ==4:
        y "i hope jin shows up..."
        y "....."
        y "if she's standing me up, i'm gonna be sad."
        y "..........."
        y "maybe she-"
        show tojn tojn23:
            xpos 75
        with dissolve
        jin "hello...?"
        y "jin! over here!"
        show tojn tojn20:
            xpos 75
        with dissolve
        jin "there you are!"
        y "what took you so long?"
        jin "i went to the wrong fountain."
        y "....there's only one."
        jin "really?"
        jin "then where did i go?"
        y "....."
        y "fuck if i know."
        y "come on, walk with me."
        jin "thanks!"
        hide tojn
        show tojn tojn20:
            xpos 0
            xpos 75
            linear 25 xpos -700
            xpos 0
            xzoom -1
            xpos -75
            linear 25 xpos 700
            xzoom 1
            xpos 0
            xpos 75
            linear 25 xpos -700
            xpos 0
            xzoom -1
            xpos -75
            linear 25 xpos 700
            xzoom 1
            repeat
        jin "this is nice..."
        jin "thanks for inviting me..."
        jin "even if it was out of pity."
        y "it wasn't out of pity!"
        jin "it's okay, really."
        y "no, it's not!"
        y "you're beautiful and fun to be around."
        jin "thanks, but-"
        y "(i have to get her to relax...)"
        y "how many people do you think have peed in that fountain?"
        jin "i dunno... all of them?"
        y "...have you?"
        jin "i don't want to answer that."
        y "{i}that's{/i} a yes!"
        jin "it is not a yes!"
        y "you can't fool me."
        jin "...okay, maybe once. once!"
        y "hahaha!"
        y "even i haven't wizzed in there yet!"
        jin "there's always tomorrow."
        show black
        with dissolve
        "you and jin walk around the fountain, laughing and taking it easy."
        "she seems to relax and have a good time by the end of it."
        hide tojn
        show tojn tojn20
        hide black
        with dissolve
        jin "thanks, aang."
        jin "this was a lot of fun!"
        jin "will i see you later?"
        y "count on it."
        jin "Okay!"
        jin "bye!"
        hide tojn with dissolve
        y "....that was a fun."
        y "i should get her a present."
        $ jin_quick_talk = 5
        jump love_basingse_day1

    if love_toph_sex and not cabbage_quest:
        jump cabbages
    if meangirls_escapedmaze ==3 and not mg_reward:
        jump meangirls_reward
    if room30.sp_content >=2 and not smellerbee_gone:
        if not love_smellerbee_sex:
            jump smellerbee_blowjob
    if not smellerbee_gone and mg_reward and love_smellerbee_sex:
        $ randfount = 0
        $ randfount = renpy.random.randint(1,3)
        if randfount ==1:
            jump smellerbee_blowjob
        if randfount ==2:
            jump meangirls_reward
        if randfount ==3:
            jump smellerbee_fuck
    if smellerbee_gone and mg_reward and love_smellerbee_sex:
        $ randfount = 0
        $ randfount = renpy.random.randint(1,2)
        if randfount ==1:
            jump smellerbee_fuck
        if randfount ==2:
            jump meangirls_reward

    if not smellerbee_gone and not mg_reward and love_smellerbee_sex:
        $ randfount = 0
        $ randfount = renpy.random.randint(1,2)
        if randfount ==1:
            jump smellerbee_fuck
        if randfount ==2:
            jump smellerbee_blowjob

    if smellerbee_gone and not mg_reward and love_smellerbee_sex:
        "4"
        jump smellerbee_fuck

    if not smellerbee_gone and mg_reward:
        $ randfount = 1
        $ randfount = renpy.random.randint(1,2)
        if randfount ==1:
            jump smellerbee_blowjob
        if randfount ==2:
            jump meangirls_reward
    if smellerbee_gone and mg_reward:
        jump meangirls_reward
    if fountain_pee2:
        show toeg toeg01 with dissolve
        dl "the fountain is currently-"
        dl "hey! you're that avatar!"
        y "yes i am, and you're welcome."
        dl "get out of my city or i'll throw you out."
        y "oh, yeah?"
        y "you and what army?"
        show guardb_body_1:
            xpos -500
        with dissolve
        dl "your lack of compliance has been noted."
        y "oh. i forgot that you literally have an army."
        y "....um...."
        y "....look over there!"
        "you scurry off."
        "but not like you're scared or anything."
        jump love_basingse_day1

    if fountain_pee:
        show toeg toeg01 with dissolve
        dl "didn't i tell you to fuck off?"
        dl "do i need to choke a bitch?"
        y "...no?"
        dl "if you're not gone in three seconds, that's going to happen."
        y "fine, i'll go. but not because i'm scared of you."
        dl "three."
        y "what?"
        dl "two."
        y "oh, doing a countdown. yeah, real original."
        dl "one."
        y "oh, shit."
        y "bye!"
        $ fountain_pee2 = True
        jump love_basingse_day1
    else:

        show toeg toeg01 with dissolve
        dl "the fountain is currently closed."
        y "why?"
        dl "for your protection."
        y "somebody peed in it, didn't they?"
        dl ".....i'm not at liberty to say."
        y "yeah, they peed."
        dl ".......leave the premises, civilian."
        dl "or you will be removed."
        y "well, i can see {i}urine{/i} a bad mood, so i'll just go."
        dl "ugh. i hate my job."
        y "i also hate your job."
        dl "....you should go. now."
        y "....i'm gonna go."
        dl "good decision."
        hide toeg toeg01 with dissolve
        $ fountain_pee = True
        jump love_basingse_day1


label love_bk3_fountain_night:
    if suki_tylee ==4:
        scene black
        scene bk3_bg_fountain
        show blackveil
        with dissolve
        y "suki?!"
        y "...."
        y "shit, she's not here!"
        jump love_basingse_night1
    if fountain_raid:
        y "these guards are already taken care of."
        jump love_basingse_night1
    if party_plan_explained and not party_complete:
        y "i need to meet katara and toph at the palace."
        jump love_basingse_night1
    if love_suki_hypno ==11 and not fountain_raid:
        $ fountain_raid = True
        show toeg toeg01
        show guardb_body_1:
            xpos -500
        with dissolve
        dl1 "i feel like this fountain has been out of service for a long time."
        dl2 "so?"
        dl1 "well, no one even comes here."
        dl1 "and even if they did, who cares?"
        dl1 "so why are we guarding it?"
        dl2 "well, because the grand secretariat asked if anyone wanted fountain duty."
        dl2 "and you said \"as long as i'm not with that fat ass\" and pointed at me-"
        dl2 "-which hurt, b.t. dubs-"
        dl2 "and then i said \"fuck you, josh\", and then the secretariat threw up his hands and yelled at us."
        dl2 "and now we're here."
        dl1 "......."
        dl2 "......."
        dl1 "what?"
        dl1 "i meant, why does it even matter that we're here?"
        dl2 "oh."
        dl2 "probably to catch hookers or something."
        dl1 "....go on."
        dl2 "i heard there are hookers in this area."
        dl1 "....go on."
        dl2 "that's it. that's all i heard."
        dl2 "it probably wasn't true though."
        dl1 "it might be worth... checking out."
        dl1 "for curfew reasons."
        dl2 "....."
        dl1 "you stay here, i'll look into it."

        hide toeg with dissolve
        dl2 "hey, wait...."
        hide guardb_body_1 with dissolve
        dl2 "damn it josh, get back here!"
        dl1 "no!"
        y "....."
        show tosi tosi10:
            xzoom -1
        with dissolve
        suki "well that was... odd."
        y "this didn't really feel like a raid."
        y "does this count?"
        suki "well, they left..."
        suki "so maybe?"
        suki "either way, no point staying here."
        y "right, let's go."
        suki "aw, you're not even going to offer your body to me for money?"
        y "oh? and how much do you have on you?"
        suki "i have... no money."
        y "and you expect me to just give it up?"
        y "girl, I do not work on credit."
        suki "and ain't that a shame."
        suki "come on."
        jump love_basingse_night1

    scene black

    jump love_basingse_night1


label love_bk3_market_night:
    if suki_tylee ==4:
        scene black
        scene market_general
        show blackveil
        with dissolve
        y "suki?!"
        y "...."
        y "shit, she's not here!"
        jump love_basingse_night1
    if party_plan_explained and not party_complete:
        y "i need to meet katara and toph at the palace."
        jump love_basingse_night1

    if market_raid:
        y "these guards are already taken care of."
        jump love_basingse_night1

    if jasmine_raid and fountain_raid and palace_raid and home_raid and arena_raid:
        scene black
        scene expression "bk3/toph/party/bg_citystreet1.jpg":
            xpos -1000
        show tosi tosi10
        with dissolve
        suki "alright, we're here."
        y "and...?"
        suki "this is the only part of the city we haven't hit yet."
        suki "if they send out the sluts, they'll come here first."
        suki "...if they're smart, anyway."
        y "right, well, how long-"
        dl "that's them!"
        hide tosi with moveoutleft
        show toti toti02:
            xpos -250
        show toeg toeg01
        show guardb_body_1:
            xzoom -1
        with moveinright
        dl1 "those are the two that are being mean!"
        dl2 "...dude."
        dl1 "what?"
        dl2 "get your {i}shit{/i} together."
        show toti toti04 with dissolve
        ty "no, being mean isn't cool."
        show tosi tosi10:
            xpos 50 ypos 420
        suki "there you are, you slut!"
        hide tosi
        show toti toti03 with dissolve
        ty "hey!"
        show toti toti02 with dissolve
        ty "what did i just say about being mean?"
        show tosi tosi10:
            xpos 50 ypos 420
        suki "where's your master?"
        suki "the queen slut?"
        hide tosi
        ty "she's too busy for you..."
        ty "so she sent me."
        show toti toti01 with dissolve
        ty "i hope i'm a challenge!"
        y "{size=-3}psst, suki... sidebar?"
        show tosi tosi10:
            xpos 50 ypos 420
        suki "{size=-3}what's up, aang?"
        hide tosi
        y "{size=-3}i'm seeing people up on the rooftops."
        y "{size=-3}it's not just the three of them."
        y "{size=-3}and this chick can turn off bending, somehow...."
        show tosi tosi10:
            xpos 50 ypos 420
        suki "{size=-3}....fine, you're right."
        suki "{size=-3}the one i want isn't here anyway."
        suki "{size=-3}do some airbending and make a tornado or something so we can escape."
        hide tosi
        y "{size=-3}um, i can't airbend."
        show tosi tosi10:
            xpos 50 ypos 420
        suki "{size=-3}what? why?"
        hide tosi
        y "{size=-3}because it's... dumb?"
        y "{size=-3}...maybe?"
        show tosi tosi10:
            xpos 50 ypos 420
        suki "{size=-3}....."
        suki "{size=-3}whatever, just do something."
        hide tosi
        y "{size=-3}I can make a fog with water."
        y "{size=-3}hold on."
        play sound "audio/whoosh.wav"
        scene black with dissolve
        "you bend the water in the air around you into vapor, causing visuals to become unclear."
        "you and suki escape in the confusion."
        jump love_bk3_village_background
    else:

        show tosi tosi10:
            xzoom -1
        with dissolve
        suki "let's save this one for last."
        menu:
            "okay":
                y "sure thing."
                suki "thanks."
                suki "now, let's take care of the rest."
                jump love_basingse_night1
            "why?":

                y "why?"
                suki "this is close to the palace and thus, the fire nation sluts..."
                suki "...but it's far enough away that we can escape if they send out soldiers instead."
                y "makes sense."
                suki "now, let's take care of the rest."
                jump love_basingse_night1

    scene black
    scene market_general
    show blue_30perc_transparent
    with dissolve
    menu:
        "scams":
            jump bk3_games
        "exit":

            jump love_basingse_night1


label love_bk3_market:


    scene black
    scene market_general
    with dissolve


    if earthbending >= 30:
        if 'market' in temp_list:
            y "She's already gone."
            call screen love_basingse_map
        $ temp_list.append('market')
        show azss azss01
        ss "Hey look who's there!"
        ss "The guy who likes to buy overpriced crap."
        y "Say what?"
        ss "Don't worry about it."
        ss "We won't be able to do any business anymore."
        ss "Shady is packing up and trying his luck elsewhere."
        y "Whatever. Have you seen Ka... a watertribe girl today?"
        y "She has these loopy hairthings in front of her face and..."
        ss "Nope, sorry."
        ss "Look ,I've had fun doing business with you so I'll give you something nice."
        ss "Which won't cost me anything."
        y "That's important to you isn't it?"
        ss "very much so."
        y "I really don't have time for this..."
        show azss azss100
        $ renpy.pause()
        show azss azss101
        y "Hmmmm..."
        menu:
            "Can I have some more please?":
                ss "Why not?"
                show azss azss102
                $ renpy.pause()
                y "this is very nice but I really gotta go."
            "I can't stay.":
                y "they're lovely, but I need to go now."
        show azss azss01
        ss "Bye."
        scene black with Dissolve(1.5)
        call screen love_basingse_map


    if iroh_market ==1:
        show az_iroh_body:
            ypos 60 xzoom -1
        with dissolve
        y "iroh?"
        show irpr_surprise:
            ypos 60 xzoom -1
        with dissolve
        iroh "uh, hello!"

        iroh "i am not this iroh person, though... i am mushi."
        y "what? no, you're iroh."
        iroh "no, i cannot be iroh."
        iroh "for you see, that is a fire nation name, and i am clearly from the {i}earth kingdom{/i}."
        y "ohhhhh, right."
        y "gotcha."
        y "so what are you doing here?"
        y "and why are you dressed like that?"
        hide irpr_surprise with dissolve
        iroh "i am being charitable of course!"
        iroh "and am dressed in an unassuming fashion!"
        iroh "i am providing tea to those who cannot make it to my tea shop."
        iroh "no one should miss out on tea."
        iroh "it is good for the soul."
        show az_iroh_sippingtea2:
            ypos 60 xzoom -1
        with dissolve
        iroh "*slurp*"
        hide az_iroh_sippingtea2
        with dissolve
        iroh "ahh..."
        iroh "...and some people need the help that only good tea can provide."
        y "they do?"
        show irpr_surprise:
            ypos 60 xzoom -1
        with dissolve
        iroh "of course!"
        hide irpr_surprise with dissolve
        iroh "let's see..."
        iroh "there was a crying boy, and some kids with a ball, and one criminal that was not very good at what he was doing."
        iroh "i think i might have accidentally convinced him to become a masseuse."
        y "i hope not a \"happy ending\" masseuse."
        iroh "ahh... well... we are in a poor part of town, so..."
        y "ew."
        show irpr_angry:
            ypos 60 xzoom -1
        with dissolve
        iroh "i... you... don't judge him!"
        hide irpr_angry with dissolve
        iroh "why are you here?"
        y "i saw your note and thought i'd come visit."
        iroh "why were you looking for me?"
        y "I wasn't, i just..."
        y "...i don't know."
        y "i... feel stuck sometimes."
        show irpr_blink:
            ypos 60 xzoom -1
        with dissolve
        iroh "ahh..."
        iroh "...."
        show az_iroh_sippingtea2:
            ypos 60 xzoom -1
        iroh "..........."
        iroh "...................."
        hide az_iroh_sippingtea2 with dissolve
        iroh "..............................."
        "iroh begins to sing a sad, gentle melody."
        iroh "*Leaves from the vine / Falling so slow..."
        iroh "*Like fragile tiny shells / Drifting in the foam..."
        iroh "*Little soldier boy / Come marching home..."
        iroh "*Brave soldier boy / Comes marching home..."
        y "...."
        iroh "*sniff*"
        y "iroh... er, mushi?"
        y "are you okay?"
        iroh "...."
        iroh ".........."
        iroh "...it is my son's birthday today."
        y "you have a son?"
        iroh "...i had one, yes."
        y "oh."
        iroh "i wish... i could have helped lu ten."
        iroh "i... have tried to help others..."
        iroh "....."
        hide irpr_blink with dissolve
        iroh "i have tried to be a good man... a better man..."
        iroh "but... it never goes away."
        iroh "i have learned things... things i never wanted to."
        show irpr_angry:
            ypos 60 xzoom -1
        with dissolve
        iroh "things no man should learn."
        hide irpr_angry with dissolve
        iroh "and i try to... impart them, even as i, too, learn."
        show irpr_blink:
            ypos 60 xzoom -1
        with dissolve
        iroh "i wish my nephew would listen... could find himself..."
        iroh "but one of those things i have learned is the fragility of the human life, and how easy it is to not be there for the people that need you."
        iroh "i will never not be there again."
        iroh "unless it is the only option."
        y "........."
        iroh "*sigh...*"
        iroh "poor zuko..."
        y "........"
        hide irpr_blink with dissolve
        iroh "i have just talked your ear off, haven't i?"
        iroh "is there anything i can help you with?"
        y "I don't think so."
        y "sometimes... it's good to just get out for a bit."
        y "get away from decisions and complications."
        iroh "ahh..."
        iroh "i certainly understand being pulled in different directions, and not knowing your destination, or who you are."
        iroh "i will give you the same advice i gave a young girl recently..."

        y "don't be afraid to take it up the pooper?"
        show irpr_surprise:
            ypos 60 xzoom -1
        with dissolve
        iroh "...that is not bad advice, but not the advice i was going to give."
        y "oh, sorry. go ahead."
        hide irpr_surprise with dissolve
        iroh "just that... it's okay to let others help you."
        iroh "and don't be afraid to follow your gut."
        iroh "you will make wrong decisions, but that is a normal part of life."
        iroh "follow your heart, and commit to friendships, and you will find more good than bad."
        y "......"
        iroh "alright..."
        iroh "i think... i should go."
        iroh "thank you for the good conversation."
        y "thank you."
        hide az_iroh_body with dissolve
        $ iroh_market = 2
        jump love_bk3_market

    if toph_chat == 11 and not iroh_book_talk and not market_book_talk:
        show azss azss01 with dissolve
        y "hey, do you guys sell books?"
        ss "nope."
        y "well, damn it."
        $ market_book_talk = True
        hide azss azss01 with dissolve

    if begin_scams:
        menu:
            "cabbage vendor" if cabbage_quest:
                jump cabbage_vendor
            "shop":


                jump love_bk3_market_shop
            "scams":


                jump bk3_games
            "exit":


                jump love_basingse_day1


label love_bk3_home:

    scene black
    scene basingse_home_1
    hide screen earth_money_date
    with dissolve

    if earthbending >= 30:
        if 'home' in temp_list:
            y "Joodee has left. Good."
            call screen love_basingse_map
        $ temp_list.append('home')
        show toji toji13
        jd "Ah!"
        y "What are you doing here?! It's not safe!"
        jd "I'm sorry!! I just remembered I had hidden some money in this house."
        y "uhhh... you did?"
        jd "Yeah, and I figured it might get stolen in all this commotion so I wanted to go get it."
        jd "but it's all gone already!!!"
        y "Oh wow... that's a real shame."
        y "But I'm sure whoever stole it, needed it for important stuff."
        y "you know... like health and mana potions.... ahem anyway..."
        y "Have you seen Katara?!"
        jd "I'm sorry! I haven't."
        y "Shit shit shit... Get your lovely round ass back to safety."
        y "Just in case something happens to anyone of us I want you to know-"
        show toji toji14
        jd "All will be fine. I'm certain of it."
        jd "but thanks for the wonderful time."
        y "Absolutely."
        hide toji with Dissolve(1.5)
        y "Okay, where to go now...."
        scene black with Dissolve(1.5)
        call screen love_basingse_map


    if jd_free:
        y "there's nothing here."
        jump love_basingse_day1
    if love_jd_hypno ==10 and not jd_free:
        y "i have to figure out a way to rescue joo dee."
        y "i need to find some help."
        jump love_basingse_day1
    if love_jd_hypno ==9:
        y "still no joo dee..."
        y "...and still no guard."
        y "i'll just have to wait for an opportunity to present itself."
        ya "fuck."
        jump love_basingse_day1
    if love_jd_hypno ==8:
        show toeg toeg01 with dissolve
        menu:
            "distract":
                $ love_jd_hypno = 9
                y "(alright... how should i distract this guy?)"
                menu:
                    "yell loudly":
                        y "{size=+10}distraction!"
                        dl "....."
                        dl "...what?"
                        y "{size=+10}distraction!"
                        dl "yeah, no, i get that."
                        dl "i'm just... confused why you're yelling it."
                        y "{size=+10}distraction!"
                        dl "............."
                        dl "........................."
                        dl "is this a \"timmy's trapped in the well\" situation?"
                        dl "can you not use words?"
                        y "{size=+10}distraction!"
                        dl "what is it, boy?"
                        dl "is there trouble?"
                        y "{size=+10}distraction!"
                        dl "where?"
                        y "{size=+10}distraction!"
                        dl "in the old mine?"
                        y "{size=+10}distraction!"
                        dl "I'll head there right now!"
                        hide toeg with dissolve
                        y "............"
                        y "that shouldn't have worked."
                        y "i don't know how the world works any more."
                    "workplace issue":

                        y "hey."
                        dl "...what do you want?"
                        y "frank ate all your peach yogurt."
                        dl "he {i}{size=+6}what?!"
                        dl "{size=+6}that son of a bi-"
                        dl "wait, i don't know a frank."
                        dl "do you mean jimmy?"
                        y "....yes?"
                        dl "{size=+6}that son of a bitch!"
                        dl "you don't mess with another man's peach yogurt, you fuck!"
                        hide toeg with dissolve
                        y "......"
                        y "marvelous."

                scene black
                scene basingse_home_2
                with dissolve
                y "alright, let's see if there's any clues...."
                jump basingse_home_clue_screen
            "leave":

                jump love_basingse_day1

    if love_jd_hypno ==7:
        show toeg toeg01 with dissolve
        dl "leave. now."
        y "....where's joo dee?"
        dl "she has been removed from the premises."
        y "why?"
        dl "we're done talking."
        dl "go."
        y "...fine."
        y "(i hope joo dee's okay.)"
        y "(i wonder where she is?)"
        y "(maybe she left some clues in the house...)"
        y "(I should see if i can distract the guard.)"
        $ love_jd_hypno = 8
        jump love_basingse_day1

    if love_jd_hypno == 6:
        y "joo dee?"
        y "...."
        y "hello?"
        y "maybe she's inside."
        scene black
        scene basingse_home_2
        with dissolve
        y "hmm... not here either."
        y "I wonder where she is?"
        scene black
        scene basingse_home_1
        with dissolve
        show toeg toeg01 with dissolve
        dl "leave. now."
        y "...i was."
        y "where's joo dee?"
        dl "she has been removed from the premises."
        y "why?"
        dl "we're done talking."
        dl "go."
        y "...fine."
        y "(i hope joo dee's okay.)"
        y "(i wonder where she is?)"
        y "(maybe she left some clues in the house...)"
        y "(I should see if i can distract the guard.)"
        $ love_jd_hypno = 8
        jump love_basingse_day1
    if helping_june_convo and love_jd_hypno <6:
        show toji toji01 with dissolve
        menu:
            "chat":
                if love_jd_hypno ==5:
                    jd "i will meet you at your house, avatar."
                    jump love_basingse_day1
                if love_jd_hypno ==4:
                    y "hello, joo dee."
                    jd "have you come to discuss another anti-hypnosis session?"
                    y "yup."
                    jd "great!"
                    jd "i'll meet you at your place."
                    $ love_jd_hypno = 5
                    jump love_basingse_day1
                if love_jd_hypno ==3:
                    jd "i will meet you at your house, avatar."
                    jump love_basingse_day1
                if love_jd_hypno ==2:
                    jd "avatar!"
                    y "you up for another session, joo dee?"
                    jd "of course."
                    jd "I will meet you there."
                    $ love_jd_hypno = 3
                    jump love_basingse_day1
                if love_jd_hypno ==1:
                    jd "i will meet you at your house, avatar."
                    jd "and... i promise not to burn it down again."
                    jump love_basingse_day1
                if love_jd_hypno ==0:
                    jd "hello, avatar!"
                    jd "have you come to help me undo my brainwashing?"
                    if love_june_hypno >=11:
                        $ love_jd_hypno = 1
                        y "i have."
                        y "if you come to my house..."
                        y "...without burning it down..."
                        y "we'll start."
                        show toji_smile with dissolve
                        jd "okay, i will!"
                        jd "th-thank you, avatar!"
                        jd "so unexpected!"
                        y "and joo dee?"
                        jd "yes?"
                        ya "i'm serious about not burning it down."
                        jd "un-understood."
                        jump love_basingse_day1
                    else:
                        y "not yet."
                        y "i still have to help someone."
                        jd "i understand, avatar."
                        jd "goodbye for now, then."
                        jump love_basingse_day1
            "exit":

                jump love_basingse_day1

    if love_suki_hypno >=13 and not jd_apologize:
        show toji toji01 with dissolve
        jd "hel-"
        show toji_surprise with dissolve
        jd "aahh!!!"
        hide toji
        hide toji_surprise
        with dissolve
        "joo dee runs into the house."
        menu:
            "follow her":
                $ jd_apologize = True
                scene black
                show basingse_home_2
                with Dissolve(1)
                y "joo dee?"
                show toji toji01
                show toji_surprise
                with dissolve
                jd "avatar!"
                jd "i am so sorry!"
                jd "please... forgive me for everything!"
                y "Joo dee, calm down!"
                y "i forgive you."
                jd "....."
                jd "really?"
                y "yes!"
                y "in fact... i'm sorry, too."
                y "you only did what you were forced to do."
                y "you've been brainwashed, and have no control over your actions."
                y "i'm actually here to help with that."
                hide toji_surprise with dissolve
                jd "you are?"
                y "yeah."
                if love_june_hypno >=11:
                    $ love_jd_hypno = 1
                    y "if you come to my house..."
                    y "...without burning it down..."
                    y "we'll start."
                    show toji_smile with dissolve
                    jd "okay, i will!"
                    jd "th-thank you, avatar!"
                    jd "so unexpected!"
                    y "and joo dee?"
                    jd "yes?"
                    ya "i'm serious about not burning it down."
                    jd "un-understood."
                    $ helping_june_convo = True
                    jump love_basingse_day1
                else:

                    y "oh, wait..."
                    y "i actually have to help someone else first."
                    y "I'll come back later and let you know."
                    $ helping_june_convo = True
                    jump love_basingse_day1
            "leave":

                jump love_basingse_day1
        "next time you see jd, she apologizes profusely."
        "you shrug it off and apologize yourself."
        "you offer to undo the brainwashing."
        "begin the anti-hypnosis process."

    if joodee_revenge:
        y "hmmm... joo dee is suspiciously absent."
        y "maybe i should have done more than just fuck her tits."
        y "like... lock her up somewhere."
        y "....i'm an idiot."
        jump love_basingse_day1
    if lovehousefire ==5 and not suki_joodee:
        y "nobody here right now."
        y "i wonder where joo dee is?"
        y "she's probably inside."
        y "if i need her, i can just yell."
        jump love_basingse_day1

    if suki_joodee and not joodee_revenge:
        ya "jooooooo deeeeeee!"
        scene black with dissolve
        play sound "audio/thud.mp3"
        scene basingse_home_2 with vshake
        "you kick in the front door."
        ya "jooooooo deeeeee!"
        ya "i'm hooooome!"
        show toji toji01 with dissolve
        jd "hel-"
        show toji toji02
        show toji_surprise
        with dissolve
        jd "avatar!"
        jd "you... you're supposed to be... i mean..."
        show toji_smile
        hide toji_surprise
        with dissolve
        jd "h-how can i help you?"
        ya "someone burned my house down, joo dee."
        hide toji_smile
        show toji_blush
        with dissolve
        jd "u-umm...."
        ya "they burned it down with me {i}inside{/i}."
        ya "and i am understandably upset."
        jd "i c-can imagine you-"
        ya "do you know anything about it, {i}joo dee{/i}?"
        show toji_smile
        hide toji_blush
        show toji_blush
        with dissolve
        jd "m-maybe, um, a burglar was trying to-"
        ya "i think {i}you{/i} did it, joo dee."
        show toji_surprise
        hide toji_smile
        hide toji_blush
        show toji_blush
        with dissolve
        jd "umm. that's not... i mean... i wouldn't..."
        ya "in fact, i {i}know{/i} you did."
        ya "someone saw you running away from my house."
        "you step closer to joo dee, who is suddenly trembling from head to foot."
        jd "i... um..."
        ya "it must have been after you {i}locked me in a burning house{/i}."
        ya "is that familiar?"
        ya "does that sound {i}familiar{/i}, joo dee?"
        jd "n-no... i..."
        ya "why did you try to {i}murder me{/i}?"
        ya "what have i {i}ever{/i} done to a stupid slut like you?"
        jd "i..."
        ya "what? huh?"
        ya "is there any reason why i shouldn't light you on fire right now, joo dee?"
        ya "i am the avatar!"
        jd "i d-didn't-"
        ya "one more lie and this whole place goes up!"
        jd "I... i h-had orders."
        jd "it wasn't pers-"
        ya "it wasn't personal?!"
        ya "apologize! right now!"
        show toji_smile
        hide toji_surprise
        hide toji_blush
        show toji_blush
        with dissolve
        jd "i-i'm sorry, sir."
        jd "m-maybe we can schedule a-"
        ya "{size=+10}what!?!"
        show toji_surprise
        hide toji_smile
        hide toji_blush
        show toji_blush
        with dissolve
        jd "i-"
        ya "{size=+7}is that it!?!"
        "you lunge towards joo dee, snarling."
        hide toji_blush
        hide toji_surprise
        hide toji
        with dissolve
        show tojt tojt01
        show tojt_unhappy
        with dissolve
        "....stopping immediately in front of her."
        jd "i-i'm sorry! i'm sorry!"
        jd "i was just following orders!"
        ya "do you always just do what you're told?"
        ya "what if i said \"take your fucking shirt off\"?"
        ya "would you-"
        show tojt tojt40
        with dissolve
        y "wha-"
        show tojt tojt41 with dissolve
        show ctc
        pause
        hide ctc
        y "....."
        y "seriously?"
        show tojt_blush with dissolve
        jd "i was... instructed to welcome you to the city and do whatever you asked..."
        show tojt_blink with dissolve
        jd "and once you got kicked from the city, my orders never changed..."
        y "so you just... always follow orders?"
        hide tojt_blink with dissolve
        jd "i... yes! i have to!"
        jd "i'm... i'm sorry about your house!"
        jd "it won't happen again!"
        ya "you bet your fat tits it won't!"
        show tojt_surprise
        hide tojt_unhappy
        hide tojt_blush
        show tojt_blush
        with dissolve
        jd "w-what?"

        menu:
            "order her to lay on the floor":
                ya "lay on the floor!"

                play sound "audio/thud.mp3"
                scene basingse_home_4
                show toob toob00 with vshake
                stop music
                play music "audio/Unwritten Return.mp3"
                jd "ah!"
                "as joo dee attempts to lay down, you fully rip open her robe and forcibly shove her onto her back."
            "shove her to the floor":

                ya "get on the floor!"
                play sound "audio/thud.mp3"
                scene basingse_home_4
                show toob toob00 with vshake
                stop music
                play music "audio/Unwritten Return.mp3"
                jd "ah!"
                "you forcibly shove joo dee to the floor, fully ripping open her robe as you do."


        show ctc
        pause
        hide ctc
        jd "w-what are you doing?"
        ya "you were ordered to do what i tell you?"
        jd "well... y-yes..."
        ya "and that order didn't end?"
        jd "...n-no..."
        ya "then here's your new order..."
        ya "take my cock between your plump, juicy tits!"
        jump joodee_boobjob
    else:

        show toji toji01 with dissolve
        jd "hello, avatar!"
        jd "can i help you?"
        y "not at the moment."
        jd "please let me know if that changes!"
        jump love_basingse_day1

label love_bk3_home_night:
    if suki_tylee ==4:
        scene black
        scene basingse_home_1
        show blackveil
        with dissolve
        y "suki?!"
        y "...."
        y "shit, she's not here!"
        jump love_basingse_night1
    if party_plan_explained and not party_complete:
        y "i need to meet katara and toph at the palace."
        jump love_basingse_night1
    if home_raid:
        y "these guards are already taken care of."
        jump love_basingse_night1
    else:
        scene black
        scene basingse_home_1
        show toeg toeg01
        show guardb_body_1:
            xpos -500
        with dissolve
        dl1 "where's that joodee chick?"
        dl2 "oh damn, you don't know?"
        dl1 "no, what's up?"
        dl2 "girl, feng is pissed."
        dl1 "don't... call me \"girl\"."
        dl1 "also, why is he pissed?"
        show tosi tosi10:
            xpos 50 ypos 500
        with dissolve
        suki "{size=-3}pssst!"
        suki "{size=-3}aang, down here!"
        y "{size=-3}what?"
        suki "{size=-3}let's take these guys down."
        suki "{size=-3}you take one and i'll take the other."
        suki "{size=-3}you want left or right?"
        hide tosi
        menu:
            "left":
                y "{size=-3}left."
                show tosi tosi10:
                    xpos 50 ypos 500
                suki "{size=-3}okay... get ready..."
                dl2 "well-"
                suki "{size=+3}go!"
                play sound "audio/thud.mp3"
                hide tosi
                hide toeg with moveoutbottom
                dl1 "aaah!"
                dl2 "what the fuck?"
                y "oh, shit!"
                hide tosi
                show tosi tosi11
                with dissolve
                suki "it's go-time, bitch!"
                y "take this!"
                play sound "audio/thud.mp3"
                hide guardb_body_1 with moveoutbottom
                suki "that's right!"
                show tosi tosi10 with dissolve
                suki "nice teamwork."
            "right":

                y "{size=-3}right."
                show tosi tosi10:
                    xpos 50 ypos 500
                suki "{size=-3}okay... get ready..."
                dl2 "well-"
                suki "{size=+3}go!"
                play sound "audio/thud.mp3"
                hide tosi
                hide guardb_body_1 with moveoutbottom
                dl2 "aaaahhh!!!"
                dl1 "what the fuck?"
                y "oh, shit!"
                hide tosi
                show tosi tosi11:
                    xzoom -1
                with dissolve
                suki "it's go-time, bitch!"
                y "take this!"
                play sound "audio/thud.mp3"
                hide toeg with moveoutbottom
                suki "that's right!"
                show tosi tosi10 with dissolve
                suki "nice teamwork."

        y "thanks."
        suki "i think you and i could work together..."
        suki "....intimately."
        y "oh? i didn't realize this was an interview."
        suki "i guess it depends on what you're willing to do to earn your pay."
        y "enough to keep you enthralled, not enough to make you satisfied."
        suki "oh, you bitch."
        suki "come on, let's get the others... before this interview turns into a casting couch."
        $ home_raid = True
        jump love_basingse_night1

    scene black
    scene basingse_home_1

    jump love_basingse_night1


label love_bk3_arena:


    if earthbending >= 30:
        scene bg_a watchtower_floor
        if 'arena' in temp_list:
            y "Oh wow, Shady's already gone!"
            call screen love_basingse_map
        $ temp_list.append('arena')

        show shadyguy_grin with dissolve
        sg "you're back!"
        y "Dude, no time, have you seen..."
        sg "Your watertribe girl?"
        sg "yeah, I've seen her. "
        sg "feisty little thing. "
        sg "I think I saw her near the fountain."
        $ earthbending = 31

        y "That's great! I owe you man."
        sg "before you go... I feel it's time for smart folk to leave this place... like, really soon."
        y "What are you saying?"
        sg "The entrepeneurial climate is starting to become all fucky so I'm going to move my place of operations."
        sg "Just letting you know. Because... well, you've made me a wealthy man with all that shit you kept buying."
        sg "And I really appreciate that."

        sg "The spirits only know why you didn't just buy all that wood etc from my competition at half the price..."
        sg "but hey, I got you some other nice unique stuff too which you can't buy anywhere else!"
        y "Name one thing..."
        sg "Besides my charming smile and a deep friendship which crosses time?"
        y "What?"
        sg "Shouldn't you be off finding that girl of yours?"
        y "Shit. you're right."
        y "Thanks shady! See ya in the fire nation!"
        sg "I'm going to miss the crabfights... they made me so much money it's almost sickening. Almost."
        sg "Huh...? I didn't tell him where i was going... did I?"
        scene black with Dissolve(1.5)
        call screen love_basingse_map


    if lovehousefire ==5:
        if shadygone:
            show azss azss01
            with dissolve
            ss "mr. shady is still not back, sir."
            y "damn it."
            jump love_basingse_day1
        else:
            hide screen earth_money_date
            scene black
            scene bg_a watchtower_floor
            with dissolve
            ya "shady!"
            ya "get out here, you fuck!"
            show azss azss01
            with dissolve
            ss "may i help you?"
            ya "get shady out here now!"
            ya "that fucker knows what he did."
            ss "i'm sorry, sir, but mr. shady is not here right now."
            ya "bullshit!"
            ya "shady! i'm coming for you! you hear me!?"
            ss "sir-"
            ya "my house burnt down and shady knew about it."
            ya "for all i know, he {i}did{/i} it."
            ya "so, i need to talk with him, or he's gonna find {i}himself{/i} on fire."
            ss "{i}sir{/i}."
            ss "he is {i}not{/i} here."
            ss "he left town yesterday."
            y "he... did?"
            ss "{i}yes{/i}."
            ss "he mentioned that someone might come yelling for him, and to tell them, and i quote..."
            ss "\"sorry brother, but it wasn't me. i did do my best to warn you. hopefully you can find it in your cock to forgive me.\""
            ya "that was his best? he couldn't just say \"someone's gonna burn your house down with you inside it\"?"
            ss "I'm sorry sir, i'm just quoting him."
            y "ugh."
            ss "if it helps... i helped him pack up his cart yesterday during the day."
            y "he... did?"
            ss "yes, sir."
            y "...then it wasn't him?"
            ss "i can vouch that he left town yesterday."
            y "oh."
            y "...he probably left because he knew i'd be pissed."
            ss "perhaps, sir."
            y "then... i need a new lead."
            y "you wouldn't happen to have any thoughts on this, would you?"
            ss "well..."
            ss "there must be someone who's up at night in the village."
            y "hmm... there's an idea."
            y "who's up late at night?"
            y "i'll think on it."
            ss "very good, sir."
            $ shadygone = True
            jump love_basingse_day1

    if brothel_quest ==5:
        y "I should see toph and make sure shady kept his word."
        jump love_basingse_day1

    if brothel_quest ==4:
        if shop_building <2:
            y "i should upgrade the shop in the village."
            jump love_basingse_day1
        else:
            stop music
            play music "audio/Hero Down.mp3"
            scene black
            scene bg_a watchtower_floor
            show shadyguy_grin
            with dissolve
            sg "you're back!"
            sg "you get that shop taken care of?"
            y "yeah, and it wasn't free."
            sg "i know... sorry about that."
            y "i've just spent a lot money on your stupid-"
            sg "aw, don't be like that."
            sg "look, i got you a present!"
            play sound "audio/win2.mp3"
            $ bk3_wood +=5
            $ bk3_steel +=5
            "shady hands you {b}5 wood and 5 steel{/b}."
            y "....this doesn't come close to making up for it."
            sg "i know, and i feel bad about that."
            y "i don't believe you."
            sg "well, i do."
            sg "and to make it up to you..."
            sg "i'm looking into a rare item for you."
            y "what item?"
            sg "oh, no, no."
            sg "you want me to tell you? and ruin the fun?"
            sg "you're just going to have to wait and see."
            sg "but i have my fingers in a few creampies, and-"
            y "...wait, what? do you mean \"pies\"?"
            sg "no, i mean creampies."
            y "that's... not an expression."
            sg "are you sure?"
            y "i'm pretty sure it's \"fingers in a few pies\"."
            y "creampies are completely unrelated."
            sg "not in my circles."
            y "......."
            sg "anyway, if my information is correct, you're gonna need what i'm hunting down."
            sg "you're making some powerful people angry."
            y "that is true."
            show shadyguy_unsure with dissolve
            sg "be careful who you anger."
            sg "the secretariat is not someone to be trifled with."
            sg "he makes people... disappear."
            sg "...or just kills them outright."
            sg "watch your back."
            y "i..."
            y "...thanks. i'll be careful."
            y "do you have any information that i could use?"
            sg "...."
            sg "i........"
            sg "sorry, man."
            sg "I can't pick sides like that."
            sg "some things are just going to happen."
            y "wait, what's going to happen?"
            sg "....."
            sg "I can't say any more."
            sg "you've made a bad enemy."
            sg "...and where there's smoke, there's fire."
            y "that's not very helpful."
            y "it also doesn't make sense."
            sg "well, if i can help without compromising myself, i will."
            y "that's a little selfish, isn't it?"
            show shadyguy_grin
            hide shadyguy_unsure
            with dissolve
            sg "well, i'm a selfish guy."
            sg "but back to business!"
            sg "you need me to fuck someone, right?"
            ya "what? no!"
            sg "really? then what was it you needed?"
            y "i need you to convince toph, in the village, that a brothel is a good idea."
            sg "what? that's it?"
            sg "that's easy."
            sg "i'd have done that for free."
            ya "........"
            ya "(....breathe....)"
            sg "but tell you what, i'll send over my girl."
            sg "she'll do a better job than i would."
            sg "she has some... experience in that field."
            sg "so, where's this chick of yours?"
            y "house in the center of the village."
            y "she's short and blind."
            sg "i'll get my girl on it."
            sg "adios, compadre!"
            hide shadyguy_grin with dissolve
            $ brothel_quest = 5
            jump love_basingse_day1

    if brothel_quest == 3:
        if emoney >=100:
            stop music
            play music "audio/Hero Down.mp3"
            scene black
            scene bg_a watchtower_floor
            show shadyguy_grin
            with dissolve
            sg "hey, brother!"
            sg "got my money?"
            menu:
                "yes":
                    y "right here."
                    sg "nice!"
                    play sound "audio/money.mp3"
                    $ emoney -=100
                    "you give shady 100 coins."
                    sg "ah... that's a pleasant weight."
                    y "so, are we good?"
                    sg "one last thing."
                    y "oh, come on, man!"
                    sg "look, you came to me."
                    sg "you paid for my time, but not for the service."
                    y "what?!"
                    sg "don't worry, you're not going to pay me any more."
                    sg "though i can't promise it won't cost you anything."
                    sg "i need a favor."
                    y "seriously?"
                    sg "a favor for a favor."
                    sg "i don't deal in debts - partial or whole - you do what i ask or we don't have a deal."
                    y "....why are you smiling?"
                    sg "what, i can't be a fun guy?"
                    sg "i'm a jovial sort -- i just have a business to run."
                    y "*sigh...*"
                    y "so what else do i have to do?"
                    sg "that's the right attitude!"
                    y "....."
                    sg "i need you to upgrade the shop in the village."
                    y "...why?"
                    sg "I've invested... heavily... in arena crab battles."
                    sg "i want to make sure the shops are well stocked and pretty."
                    sg "i'm trying to start a craze, here."
                    sg "so... go upgrade the shop, and we'll take care of your lady."
                    y "and this is the last thing i have to do?"
                    sg "the last thing. i promise."
                    y "alright, i'll go upgrade the shop."
                    sg "okay!"
                    sg "bye, friend!"
                    $ brothel_quest = 4
                    jump love_basingse_day1
                "no":

                    y "not yet."
                    sg "that's fine, man."
                    sg "it's your thing."
                    jump love_basingse_day1
        else:
            y "I should get 100 coins to pay shady, and come back."
            jump love_basingse_day1

    if brothel_quest ==2:
        stop music
        play music "audio/Hero Down.mp3"
        scene black
        scene bg_a watchtower_floor
        show shadyguy_grin
        with dissolve
        sg "avatar! my main man!"
        sg "i'm taking bets that you get your ass kicked next time we fight."
        sg "want in?"
        y "....."
        y "....you want me to bet that i'm going to get my ass kicked at crab battles?"
        sg "yeah! you in?"
        y "i'm... gonna pass."
        sg "your loss."
        y "i need something else, though."
        sg "what's up, brother?"
        y "i need your help convincing this chick in the village that brothels are a good idea."
        sg "......."
        sg "that's a weird request."
        y "it's actually really-"
        sg "I'm in!"
        y "whoa. that easy?"
        sg "sure!"
        sg "just give me 100 coins, and i'll send one of my girls over."
        y "...."
        y "i was hoping you'd do this... pro bono."
        sg "I am a very professional boner."
        y "...you misheard me on purpose."
        sg "maybe."
        y "i was hoping you might do this for free."
        sg "nope!"
        sg "I'm a salesman, and i'm selling my services to you."
        sg "for the low, low price of 100 coins."
        y "....fine."
        sg "good deal!"
        sg "let me know when you have it!"
        $ brothel_quest = 3
        jump love_basingse_day1

    if cheat_unlock and crab1:
        stop music
        play music "audio/Hero Down.mp3"
        scene black
        scene bg_a watchtower_floor
        show shadyguy_grin
        with dissolve

        if not first_arena_match:
            sg "welcome to the crabble royale, brother!"
            sg "you ready to get in on this nonsense!?"
            y "i.... have no idea what the fuck is happening."
            sg "sure, sure, i'll give you the run down."
            sg "you have crabs and i have crabs."
            y "....that's not good."
            sg "no, i mean... we have battling crabs."
            sg "Each crab type has different abilities and strengths, with rare and epic crabs being the most powerful."
            sg "you can level up your crabs in battles, but you can level up yourself by fighting crabs."
            sg "of course, you'll only level up your crab-battling abilities... you won't be a better earthbender or anything."
            y "i... think i get it."
            sg "i knew you would."
            if crab1 and crabs_current ==0:
                sg "whoa, that's a shit crab."
                sg "go talk to the shop girl. for real."
                jump basingse_day1
            $ first_arena_match = True
            jump bk3_arena_start_shit
        else:






            if crab1 and crabs_current ==0:
                sg "whoa, that's a shit crab."
                sg "go talk to the shop girl. for real."
                jump love_basingse_day1

            sg "snip snap, bitch."
            hide shadyguy_grin with dissolve
            jump bk3_arena_start_shit


    if cheat_unlock and quest5:
        "\"no arena matches today - everyone's hungover from the celebration of the king's birthday.\""
        y "....still?"

        y "well, fair enough I guess."
        jump love_basingse_day1

    if cheat_unlock and not crab1:
        "\"no arena matches today - everyone's hungover from the celebration of the king's birthday.\""
        y "aw.... well, fair enough I guess."
        jump love_basingse_day1
    else:
        "\"no arena matches today - closed in celebration of the king's birthday.\""
        y "aw, man."
        jump love_basingse_day1






label love_bk3_arena_night:
    if suki_tylee ==4:
        scene black
        scene bg_a watchtower_floor
        show blackveil
        with dissolve
        y "suki?!"
        y "...."
        y "shit, she's not here!"
        jump love_basingse_night1
    if party_plan_explained and not party_complete:
        y "i need to meet katara and toph at the palace."
        jump love_basingse_night1

    if arena_raid:
        y "these guards are already taken care of."
        jump love_basingse_night1
    if not arena_raid:
        stop music
        play music "audio/Hero Down.mp3"
        scene black
        scene bg_a watchtower_floor
        show toeg toeg01
        show guardb_body_1:
            xpos -500
        with dissolve
        dl1 "how are your crabs?"
        dl2 "mild."
        dl1 "...what?"
        dl2 "they've got no spirit!"
        dl2 "they just sit around!"
        dl1 "it's like they {i}also{/i} think the battle formulas are awkward."
        dl2 "...what do you mean \"also\"?"
        play sound "audio/thud.mp3"
        show tosi tosi11:
            xzoom -1
        with moveinleft
        hide guardb_body_1
        with moveoutright
        dl1 "aaaaaaaaaaaahhhhhhhhhhhh!!!"
        dl2 "what the hell?!"
        ya "take this, you critical dick!"
        play sound "audio/thud.mp3"
        hide toeg with moveoutbottom
        dl2 "ooof...."
        y "suki, can you warn me next time?"
        suki "maybe."
        suki "by the way, i've never played here."
        y "so?"
        suki "so... i have no crabs..."
        suki "and i'm ready to have my cherry popped."
        y "......."
        y "holy shit."
        y "did you really just say-"
        suki "come on, we're not done yet."
        hide tosi with dissolve
        y "did anyone else hear that?"
        y "no? just me?"
        y "...why is no one ever around when i get hit on?"
        $ arena_raid = True
        jump love_basingse_night1

    "arena is currently closed."
    jump love_basingse_night1

label love_bk3_palace:


    if earthbending >= 30:
        show expression "ebackgrounds/basingse_city_1.jpg"
        if 'palace' in temp_list:

            y "I've already been there."
            call screen love_basingse_map
        $ temp_list.append('palace')
        show expression "ebackgrounds/basingse_city_1.jpg"
        show expression "maze/love_ajala_surprise.png"
        ct "What are you doing here!? You need to go before anyone else sees you!" with hpunch
        y "Ajala, have you seen Katara? She's a watertribe girl with hairloop thingies in front of her face."
        ct "No I haven't. But you should really get out of here while you can."
        y "Fuck...."
        y "For what it's worth, I really enjoyed our time in the maze."
        y "And if I never get to see you again.. I want you to know...."
        menu:
            "I'm certain you could beat Rei":
                y "I mean in an arm wrestle competition."
                hide expression "maze/love_ajala_surprise.png"
                show expression "maze/love_ajala_armpump.png"
                with Dissolve(1.5)
                ct "Hah! I've never lost one of those to anyone!!"
                ct "Rei will be no exception! Whoever that is."
            "Your muscular body makes me hard":
                hide expression "maze/love_ajala_surprise.png"
                show expression "maze/love_ajala_delight.png"
                with Dissolve(1.5)
                y " Like.. ridiculously hard."
                ct "Thanks, I really like hearing that."
        y "Bye, Ajala."
        scene black with Dissolve(1.5)

        call screen love_basingse_map



    if suki_ty_palace ==3 and suki_tylee <4:
        y "suki and ty lee should be waiting here."
        y "should i go meet them?"
        menu:
            "get this party started":
                $ suki_tylee = 4
                y "all right... here we go."
                jump suki_ty_dai_battle
            "later":

                y "i'll come back in a bit."
                jump love_basingse_day1

    if party_plan_explained and not party_complete:
        y "okay, katara wants me to wait here until nightfall."
        y "should i?"
        menu:
            "wait":
                $ bk3_day = False
                jump love_basingse_night1
            "later":

                y "I'll do it later."
                jump love_basingse_day1

    show toeg toeg01
    show guardb_body_1:
        xpos -500
    with dissolve
    y "um... i don't think i should go there."
    dl "hey, is that the avatar?"
    y "....yeah, i should go."
    jump love_basingse_day1

label love_bk3_palace_night:
    if suki_tylee ==4:
        scene black
        scene expression "bk3/toph/party/bg_alley_epalace.jpg"
        show blackveil
        with dissolve
        y "suki?!"
        y "...."
        y "shit, she's not here!"
        jump love_basingse_night1
    if party_plan_explained and not party_complete:
        jump party_crash

    if palace_raid:
        y "these guards are already taken care of."
        jump love_basingse_night1

    if not palace_raid:
        $ palace_raid = True
        scene black
        scene expression "bk3/toph/party/bg_alley_epalace.jpg"
        show toeg toeg01
        show guardb_body_1:
            xpos -500
        with dissolve
        dl1 "can you believe the avatar and his gang tried to get in here?"
        dl2 "of course. carlos makes the best paella."
        dl1 "what?"
        dl2 "did they not come for the hors d'oeuvres?"
        dl1 "no, you twit."
        dl2 "oh."
        dl2 "then... why?"
        dl1 "dunno."
        dl1 "but it was serious enough that we have to guard this entrance instead of sitting in our outpost."
        dl2 "pfft, it's fine."
        dl2 "it's not like the watchhouse is comfortable, anyway."
        dl2 "who even picked out those chairs?"
        dl1 "i did."
        dl2 "....oh."
        dl1 "....."
        dl2 "....."
        dl2 "*cough*"
        dl1 "so.... the, uh, grand secretariat seems on edge lately."
        dl2 "yeah, even more than usual."
        dl1 "between the avatar and the fire nation princess..."
        dl2 "yeah, i'd be stressed, too."
        dl1 "what do you think about... those girls?"
        dl2 "they're hot."
        dl2 "honestly, they flash me a tit, i'll change sides in a heartbeat."
        dl1 "...really?"
        dl2 "maybe."
        dl1 "huh."
        show tosi tosi10:
            xpos 50 ypos 500
        with dissolve
        suki "{size=-3}aang!"
        suki "{size=-3}how do you want to do this?"
        menu:
            "distract them":
                y "{size=-3}i'm gonna light their little outpost on fire."
                suki "{size=-3}....."
                suki "{size=-3}Not what i had in mind, but sure, let's cause some chaos."
                show black with dissolve
                "you move around the corner and bend a fire in their nearby outpost."
                play music "audio/fire2.mp3"
                hide black with dissolve
                dl2 "the one with the braid is a hot little..."
                dl2 "the outpost!"
                dl1 "my chairs!"
                dl2 "oh no... we should... go..."
                dl1 "come on, you ass!"
                hide toeg
                hide guardb_body_1
                with dissolve
                hide tosi
                show tosi tosi10
                with dissolve
            "hit them with a rock":

                y "{size=-3}I'm gonna wack 'em with a rock."
                suki "{size=-3}....."
                suki "{size=-3}you do you, boo."

                show big_rock with moveinright
                play sound "audio/thud.mp3"
                hide toeg
                hide guardb_body_1
                hide big_rock
                with moveoutleft
                dl "aaahhhh!!"
                dl "whyyy?!?"
                hide tosi
                show tosi tosi10
                with dissolve

        suki "um... interesting approach."
        y "thanks."
        suki "you know what would have been a more interesting distraction, though?"
        y "what?"
        suki "you eating my pussy."
        y "i... you..."
        suki "well, moment passed!"
        suki "still more to do!"
        hide tosi with dissolve
        y "i don't know what's happening, but i am {i}very{/i} interested."
        jump love_basingse_night1


    show toeg toeg01
    show guardb_body_1:
        xpos -500
    with dissolve

    jump love_basingse_night1



label love_bk3_market_shop:
    scene market_general
    if crab1 and shady_explain:
        show azss azss01 with dissolve
        ss "what can i do for ya?"
        jump love_bk3_market_menu
    if crab1 and not shady_explain:
        show azss azss01 with dissolve
        ss "what can i do for ya?"
        y "where's shady?"
        ss "he's over at the arena."
        ss "i've taken over his shop here."
        ss "so, what'll it be?"
        $ shady_explain = True
        jump love_bk3_market_menu
    if bk3_shady_met:
        show shadyguy_grin with dissolve
        sg "hey, buddy!"
        sg "what can i get ya?"
        jump love_bk3_market_menu
    else:
        jump love_bk3_market_menu



label love_bk3_market_menu:
    if katara_lonely ==4 and not katara_present_ask1:
        $ katara_present_ask1 = True
        y "do you have any nice gifts?"
        ss "no, sorry."
        y "shit."

    menu:
        "why do you sell this stuff?":
            if shady_explain:
                ss "i just do what shady tells me."
                jump love_bk3_market_menu
            else:
                sg "real estate, man."
                sg "shit's blowing up."
                jump love_bk3_market_menu

        "wood (5) - 25" if not house_wood:
            if emoney >=25:
                $ house_wood = True
                $ bk3_wood +=5
                $ emoney -=25
                play sound "audio/win2.mp3"
                "you got 5 wood!"
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "wood (5) - 25 (currently sold out)(locked)" if house_wood and not village_dev_explain2:
            "test"

        "wood (5) - 25 (have [bk3_wood])" if house_wood and village_dev_explain2:
            if emoney >=25:
                $ bk3_wood +=5
                $ emoney -=25
                play sound "audio/win2.mp3"
                "you got 5 wood!"
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "steel (5) - 25" if not house_steel:
            if emoney >=25:
                $ house_steel = True
                $ bk3_steel +=5
                $ emoney -=25
                play sound "audio/win2.mp3"
                "you got 5 steel!"
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "steel (5) - 25 (currently sold out)(locked)" if house_steel and not village_dev_explain2:
            "test"

        "steel (5) - 35 (have [bk3_steel])" if house_steel and village_dev_explain2:
            if emoney >=35:
                $ bk3_steel +=5
                $ emoney -=35
                play sound "audio/win2.mp3"
                "you got 5 steel!"
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "madam outfit - 150" if love_june_hypno >=2 and not june_madam_outfit:
            if emoney >=150:
                $ june_madam_outfit = True
                $ emoney -=150
                play sound "audio/win2.mp3"
                "you got the madam outfit!"
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "obsidian - 250" if jd_free_hospital and not jd_obsidian:
            if emoney >=250:
                $ jd_obsidian = True
                $ emoney -=250
                play sound "audio/win2.mp3"
                $ obsidian +=1
                "you recieved 1 obsidian!"
                y "crazy that this was here."
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "french maid outfit - 150" if jd_free_hospital and not jd_maid_outfit:
            if emoney >=150:
                $ jd_maid_outfit = True
                $ emoney -=150
                play sound "audio/win2.mp3"
                "you got the french maid outfit!"
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "gift for jin - 75" if jin_quick_talk ==5 or jin_quick_talk ==7 or jin_quick_talk ==9:
            if emoney >=75:

                if jin_quick_talk ==5 and jin_present ==1:
                    ss "sorry, i don't have any right now."
                    ss "you'll have to wait until my supplier steals... er... aquires more."
                    jump love_bk3_market_menu
                elif jin_quick_talk ==7 and jin_present ==2:
                    ss "i thought i had more of this."
                    ss "come back another time."
                    jump love_bk3_market_menu
                elif jin_quick_talk ==9 and jin_present ==3:
                    ss "i'm afraid my supplier got caught..."
                    ss "so yeah..."
                    ss "no more gifts right now."
                    ss "sorry."
                    jump love_bk3_market_menu

                $ emoney -=75
                play sound "audio/win2.mp3"
                "you got a present!"
                if jin_present ==2:
                    $ jin_present = 3
                if jin_present ==1:
                    $ jin_present =2
                if jin_present ==0:
                    $ jin_present = 1
                jump love_bk3_market_menu
            else:
                "not enough money...."
                jump love_bk3_market_menu

        "please kill my savebug" if shady_explain:
            y "hey, what is this thing?"
            y "why is this option here?"
            ss "i've heard there's a bug that keeps some people from being able to save."
            y "well that's not good."
            ss "this fix will most likely work, but it could mess things up..."
            ss "i can't be sure."
            ss "if you don't already have a problem saving, you're probably fine."
            ss "you can come back later and choose this option if you ever have save issues."
            menu:
                "do it! apply the fix":
                    $ time = None
                    $ renpy.game.log.log=[]
                    ss "okay, stand back."
                    y "did it work?"
                    ss "only way to tell is to try and save your game."
                "maybe later":

                    y "i'll try an older save game."
                    ss "your call."
                    ss "come back if you have a problem."
            jump love_bk3_market
        "back":

            jump love_bk3_market

label love_bk3_village:


    if bk3_day:
        jump love_bk3_village_day
    else:
        jump love_bk3_village_night

label love_bk3_village_day:
    stop music fadeout 1
    play music "audio/Bumba Crossing.mp3"
    $ bk3_day = True
    jump love_bk3_village_background

label love_bk3_village_night:
    stop music fadeout 1
    play music "audio/Blue_Dot_Sessions_-_06_-_Night_Light.mp3"
    $ bk3_day = False
    jump love_bk3_village_background



label love_bk3_next:
    scene black with dissolve
    if earthbending ==29:
        if love_naga_battle and not love_nagina_free:
            hide screen earth_money_date
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            scene black with Dissolve(1.5)
            scene bg_dream with Dissolve(1.5)
            show tonb tonb101 with Dissolve(1.5):
                parallel:
                    xpos -1000
                    linear 1.0 xpos 0
                parallel:
                    ypos 0
                    linear 1 ypos 15
                    linear 1 ypos 0
                    repeat
            y "oh goddamnit..."
            y "please, no more..."
            nag "{i}i am pleasssed that you sssurvived."
            y "yeah, me too..."
            nag "{i}the barriersss are up."
            nag "{i}you are sssafe... for now."
            nag "{i}so i will leave your mind..."
            nag "{i}goodbye...."
            nag "{i}for now."
            hide tonb tonb101 with dissolve
            $ love_nagina_free = True
            y "......"
            y "she is fucking ominous."

        if not love_naga_battle:

            if love_naga_claw != True:
                $ love_naga_claw = True
                jump naga_clawjob

            hide screen earth_money_date
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            scene black with Dissolve(1.5)
            scene bg_dream with Dissolve(1.5)
            show toxe toxe00:
                ypos 40 xpos 330
                parallel:
                    linear 2.0 ypos 60
                    linear 2.0 ypos 40
                    repeat
                parallel:
                    linear 6.0 xpos 500
                    linear 6.0 xpos 330
                    repeat

            "{i}it isss time..."
            y "for what?"
            "{i}for our fight... with the other naga..."
            y "uh, right now?"
            "{i}only if you wisssh..."
            "{i}i will wait here... in your dreamsss..."
            menu:
                "battle of the snakes":
                    $ love_naga_battle = True
                    jump love_nagas_battle
                "not yet":

                    "{i}very well..."

    if earthbending ==26:
        $ earthbending = 27
        hide screen earth_money_date
        stop music
        play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
        show expression "bk3/naga/bj/bg_dream.jpg"

        show toxe toxe00:
            ypos 40 xpos 330
            parallel:
                linear 2.0 ypos 60
                linear 2.0 ypos 40
                repeat
            parallel:
                linear 6.0 xpos 500
                linear 6.0 xpos 330
                repeat
        with Dissolve(1.5)
        "{i}i do not want to disssappear...."
        y "ugh... you again..."
        "{i}yesss..."
        y "so... what are you talking about now?"
        "{i}i do not want to disssappear...."
        y "right."
        y "why would you disappear?"
        "{i}the mental assssaults... and naga will come..."
        y "why should i care, again?"
        "{i}i am keeping you sssane!"
        y "you are?"
        "{i}yesss..."
        "{i}you are under assssault..."
        "{i}if i let down my guard you will not sssurvive intact..."
        y "why should i trust you?"
        "{i}hissss...."
        "{i}ssssee for yourssself..."
        hide toxe with Dissolve(1.5)
        "you feel a sudden emptiness in your mind."
        "as if a part of you that you hadn't noticed was suddenly removed."
        y "there doesn't seem to be anything diff-"

        show hypno_light:
            xalign 1.0 yalign 0.0
            linear 1.0 xalign 0.0
            ease 1.0 truecenter
            pause 1.0
            alignaround (.5, .5)
            linear 2.0 clockwise circles 3 yalign 0.0
            linear 2.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
            ease 1.0 truecenter
            linear 1.0 xalign 1.0
            repeat
        "{size=+5}{i}{b}{color=#f00}die!" with sshake
        "{size=+10}{i}{b}{color=#f00}die die die die-die-die-die-die-die!" with sshake
        y "aahh!!!!"
        y "I get it! i get it!"
        show toxe toxe00:
            ypos 40 xpos 330
            parallel:
                linear 2.0 ypos 60
                linear 2.0 ypos 40
                repeat
            parallel:
                linear 6.0 xpos 500
                linear 6.0 xpos 330
                repeat
        hide hypno_light
        with Dissolve(1)

        "you regain a sense of wholeness as she returns to your mind and pushes out the deranged spirit."
        y "what. the. fuck."
        "{i}that isss what i have been fighting..."
        "{i}i cannot fight them for much longer..."
        "{i}i do not have the full powers of my progenetor..."
        y "your what?"
        "{i}i am not the dreamssstealer... i am a ssshadow of her..."
        "{i}born of your mind..."
        "{i}i have my own identity...."
        "{i}and i do not wisssh to die..."
        y "that... makes me super uncomfortable."
        "{i}protecting your mind will kill me eventually..."
        y "and i'll go insane?"
        "{i}yesss..."
        y "well, i don't want that."
        "{i}i have a sssuggessstion..."
        y "....okay, i'm listening."
        "{i}let me reunite with the true naga..."
        y "that sounds like a terrible idea."
        y "why would i want that?"
        "{i}i will have the power to place permanent barriersss in your mind..."
        "{i}and... i will be friendly..."
        y "you will be friendly? really? that's what you offer?"

        "{i}i have protected you... with nothing in exchange..."
        y "except for your own life."
        "{i}*hisssss....*"
        "{i}what have i ever done to make you dissstrussst me...."
        "{i}you sssnake racissst..."
        y "that's... not a real thing."
        y "and you've tried to kill me in the past!"
        "{i}you underssstand nothing..."
        y "then explain it to me."
        "{i}sssoon...."
        y "ugh."
        "{i}i have helped you... and i will help you..."
        "{i}i am not the original naga... i am my own..."
        "{i}you have given me life... in a way..."
        "{i}and i will repay you..."
        "{i}i tell no liesss..."
        "{i}trussst me..."
        y "let's say i believe you."
        y "how would you even reunite with her?"
        "{i}let her enter your mind... and i will consssume her..."
        y "what!? that's insane! no way."
        y "why would i ever agree to that?"
        "{i}i have more power than her here..."
        "{i}she will lose...."
        y "yeah, a fight in my fucking {i}mind{/i}!"
        y "how much damage would that cause?"
        "{i}none..."
        "{i}though the fight will be... dangerousss..."
        y "explain."
        "{i}our fight would challenge your perceptionsss..."
        "{i}if you sssurvive our fight... with your awarenessss intact... there will be no damage..."
        y "i don't like the sound of that... especially since you may not win, and then she's in my head."
        "{i}i will win..."
        "{i}i was born here..."
        y "that's... weird."
        "{i}i am... in a sssenssse... your mind-child..."
        y "that is very, very weird."
        "{i}but i am naga, too... and i am older than you can fathom..."
        "{i}trussst..."
        "{i}better than the one you fight now...."
        y ".............."
        y "*sigh* that's probably true."
        y "but first, tell me..."
        y "who was the other statue in the tunnels? who is the other snake lady?"
        "{i}....."
        y "tell me or i let you die."
        "{i}you would not dare...."
        y "look into my fucking brain and say that again."
        "{i}..........."
        y "now, tell me."
        "{i}ssshe...."
        "{i}isss my sssissster...."
        y "who?"
        "{i}.........."
        y "i would guess the painted lady, but she doesn't look like a snake."
        "{i}..........."
        y "unless she's in disguise?"
        "{i}.........."
        y "or she's a misdirect?"
        "{i}.........."
        y "I can kill you, you know."
        "{i}sssome thingsss are worth risssking death..."
        y "........"
        y "....oh, fine."
        y "let me consider it."
        "{i}do not wait long...."
        "{i}i may not sssurvive much longer..."
        scene black with Dissolve(1)

    if love_jd_hypno >= 15:
        if bk3_rescue_idiots >=1:
            pass
        else:
            $ bk3_rescue_idiots = 1
    if suki_ty_hospital ==2:
        $ suki_ty_hospital = 3
    if jin_quick_talk ==1:
        $ jin_quick_talk = 2
    if jin_quick_talk ==3:
        $ jin_quick_talk = 4
    if jin_quick_talk ==6:
        $ jin_quick_talk =7
    if jin_quick_talk ==8:
        $ jin_quick_talk =9
    if june_light ==1:
        $ june_light = 2
    if june_light ==3:
        $ june_light = 4
    if toph_back_disappear ==1:
        $ toph_back_disappear = 2
    $ bk3_room38_guardsex = True
    $ maze_music_on = False
    $ june_available = True
    $ suki_visited_today = False
    $ suki_hypno_today = False
    $ june_hypno_today = False
    $ jd_hypno_today = False
    $ tophs_home_access = True
    $ skye_today = False
    $ june_convo_today = False
    $ suki_hypno_today = False
    $ earth_training = False
    $ bk3_day = True
    $ ecalendar += 1
    $ toph_massaged = False
    $ toph_angry -= 1

    $ bk3_fire_remaining = bk3_moves
    $ bk3_water_remaining = bk3_moves


    $ bk3_player_life_start = bk3_hp
    $ bk3_player_life = bk3_player_life_start

    if love_begin_snake_dream and toph_chat >=24:
        if not love_naga_claw:
            $ love_naga_claw = True
            jump naga_clawjob

    if toph_chat ==15 and not madness_spirit:
        $ madness_spirit = True
        show hypno_light:
            xalign 1.0 yalign 0.0
            linear 1.0 xalign 0.0
            ease 1.0 truecenter
            pause 1.0
            alignaround (.5, .5)
            linear 2.0 clockwise circles 3 yalign 0.0
            linear 2.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
            ease 1.0 truecenter
            linear 1.0 xalign 1.0
            repeat
        "{size=+5}{i}{b}{color=#f00}it is come again!" with sshake
        "{size=+10}{i}{b}{color=#f00}the madness time is come again!" with sshake
        hide hypno_light with dissolve

    if toph_chat ==12 and not toph_last_night:
        $ toph_last_night = True
        jump toph_comfort2

    if toph_chat ==9 and lovehousefire ==0:
        jump love_house_fire

    if bk3_store_built:
        if shop_building ==1:
            $ randcoin = renpy.random.randint(3, 8)
            $ emoney += randcoin
            "you got [randcoin] coins from having a shop!"
        if shop_building ==2:
            $ randcoin = renpy.random.randint(8, 15)
            $ emoney += randcoin
            "you got [randcoin] coins from having a shop!"
        if shop_building ==3:
            $ randcoin = renpy.random.randint(15, 24)
            $ emoney += randcoin
            "you got [randcoin] coins from having a shop!"

    if katara_lonely ==1:
        jump katara_lonely1

    jump love_bk3_village


label love_b_earth_journal_menu_day:

    jump love_basingse_day1

label love_b_earth_journal_menu_night:

    jump love_basingse_night1

label love_v_earth_journal_menu:

    menu:
        "page 1":
            show screen earth_journal
            show ctc
            pause
            hide ctc
            hide screen earth_journal
            jump love_bk3_village_background

        "page 2" if quest3:
            show screen earth_journal2
            show ctc
            pause
            hide ctc
            hide screen earth_journal2
            jump love_bk3_village_background
        "exit":

            jump love_bk3_village_background



label love_bk3_maze_start1:
    stop music fadeout 2
    scene black with dissolve
    "you travel to the tunnels beneath lake laogai...."
    jump love_bk3_maze_start






label love_visit_ajala:
    hide screen earth_money_date

    scene dark_tunnel
    show tomc tomc01
    with dissolve


    jump love_ajala_tunnel_menu

label love_ajala_tunnel_menu:

    jump love_bk3_maze_start


label bk3_love_start:
    $ bk3_armor = 'level_15'
    $ bk3_loveroute = True
    y "yeah, i'm nobody's pet."
    lf "you misunderstand, you'll have power over women."
    y "i do just fine with the ladies."
    show tolf tolf02 with dissolve
    lf "...."
    lf "i see."
    lf "well, avatar, i'm sorry that it has come to this."
    lf "but i cannot allow you to leave..."
    lf "...unaltered."
    y "what?"
    lf "there are plenty of mind control rooms available... for the stubborn."
    y "are you trying to threaten me? seriously?"
    y "i will wreck your shit."
    y "how well can you even earthbend?"
    lf "you might be unfortunate enough to find out..."
    lf "but i don't think that will be necessary."
    y "oh? and why is that?"
    lf "ajala."
    y "who?"
    show tomc tomc01:
        xzoom -1.0
    with Dissolve(1.0)
    ct "my lord."
    show tolf tolf01 with dissolve
    lf "thank you for arriving so swiftly, ajala."
    y "oh, that is fine by me."
    y "damn girl, look at those quads!"
    y "i bet you could boxjump a train."
    show tolf tolf02 with dissolve
    y "you do zumba?"
    y "can i watch?"
    y "what's your sign, girl?"
    y "you a taurus?"
    y "because if you're not horny, I'm calling bull."
    ct "......."
    ct "you called, my lord?"
    y "don't ignore me!"
    ct "shall i kill him, my lord?"
    y "oh, okay, an aries."
    y "got it."
    lf "incapacitate the avatar, and..."
    lf "...keep him here."
    show tomc tomc02 with dissolve
    $ renpy.pause(0.15,hard=True)
    show tomc tomc03 with dissolve
    $ renpy.pause(0.15,hard=True)
    show tomc tomc04 with dissolve
    ct "yes, sir."
    y "now hold on-"
    show tolf tolf01
    show tolf_blink
    with dissolve
    lf "ah... what could have been, avatar."
    lf "well, goodbye."
    y "don't leave me with the juggernaut, dude!"
    hide tolf_blink with dissolve
    lf "well, how about..."
    lf "go fuck a duck."
    hide tolf with dissolve
    y "what? why?"
    y "...."
    y "well, see, now that's just rude."
    y "...so what's up with you?"
    y "wanna benchpress me? do squats on my face?"
    y "tiny dick over there is so afraid of me he ran away."
    y "got any thoughts on that?"
    show tomc_angry:
        xzoom -1.0
    with dissolve
    ct "that is the grand secretariat that you are insulting."
    y "that's a horse."
    y "and he started it!"
    y "that guy told me to find a water fowl and-"
    y "no, you know what? i'm not gonna let that guy take my cool."
    y "i'm zen, it's all good."
    y "so what's up, what's happening here."
    hide tomc_angry
    show tomc_blink:
        xzoom -1.0
    with dissolve
    ct "i'm going to enjoy beating you senseless."
    y "oh, okay, just a whole lot of rudeness around here."
    y "i'm the avatar, bitch, just try."
    y "hyyyyaaaaaahhhh!"
    "you try to earthbend, but nothing happens."
    hide tomc_blink with dissolve
    ct "....."
    y "um."
    y "okay."
    y "so if i apologized-"
    hide tomc
    show bk3_ajalagirl
    with dissolve
    y "wait, wait, wait."
    y "let's sit down, talk about alternative methods of solving disagree-"
    show bk3_ajalagirl_flipped
    hide bk3_ajalagirl
    play sound "audio/thud.mp3"
    with flash
    ya "ow! shit! fuck!"
    ya "my nose!"
    ya "you hit me in the nose!"
    ya "smell is 90 percent of taste!"
    ya "what if food tastes different now?"
    ya "you bitch!"
    hide bk3_ajalagirl_flipped
    show bk3_ajalagirl
    play sound "audio/thud.mp3"
    with flash
    "ajala encases you in a rock cocoon."
    ya "ah! god! damn! it!"
    ya "stop hitting me!"
    y "......"
    y "i'm so screwed."
    play sound "audio/earthquake.mp3"
    with sshake
    t "aang!"
    y "...toph?"
    t "i'm coming!"
    ym "heh."
    ct "who?"

    show toph_body_cloth:
        xpos -50 ypos 100
        xzoom -1.0
    hide bk3_ajalagirl
    show bk3_ajalagirl:
        xpos 275

    with sshake
    "toph suddenly bursts through a wall."
    t "what's going on here?"
    y "toph!"
    y "i mean... I'm fine, how are you, i'm not in a rock burrito."
    y "what's up?"
    ct "another pipsqueak?"
    t "what did you call me?"
    show body_rock:
        xpos -50 ypos 100
        xzoom -1.0
    with vshake
    t "how's this for \"pipsqueak\"?"
    show tomc_angry:
        xpos -22
    play sound "audio/thud.mp3"
    with flash
    ct "ow! fuck!"

    play sound "audio/thud.mp3"

    show tomc_blink:
        xpos -22
    $ bk3_armor = 'level_10'
    with flash

    ct "hgn."
    hide tomc_angry
    show tomc_surpise:
        xpos -22
    hide tomc_blink
    show tomc_blink:
        xpos -22
    with dissolve
    ct "ugh..."
    hide tomc_blink with dissolve
    ct "this... this isn't the last you'll see of me, avatar."
    y "can you be fully naked next time?"
    ct "i'll get stronger... and your bodyguard won't be around when-"
    y "she's not my bodyguard."
    t "more like a nanny."
    ya "you're not my nanny!"
    ya "nobody is my nanny!"
    ya "i am a perfectly independent individual!"
    ct "riiight. got it."
    t "right."
    y "...."
    hide tomc_surpise
    show tomc_angry:
        xpos -22
    with dissolve
    ct "we'll meet again, avatar!"
    y "go fuck a duck."
    hide tomc_angry
    hide bk3_ajalagirl
    with dissolve
    with sshake
    "ajala sinks beneath the floor in a swirl of earth, which immediately hardens after her."
    t "huh."
    hide body_rock with dissolve
    t "well..."
    hide toph_body_cloth with dissolve
    show toi toi02 with dissolve
    t "that was interesting."
    y "you're not my nanny."
    show toi toi07 with dissolve
    t "pfft. that's what i {i}let{/i} you think."
    y "shut up and let me out already."
    show toi toi09 with dissolve
    t "what?"
    t "oh, are you still in that rock?"
    y "...yes..."
    t "you really are a baby."
    y "....."
    y "...you're a baby..."
    show toi toi04 with dissolve
    t "do you hear that?"
    y "....."
    t "i think i hear a baby crying."
    t "weird that there's a baby in these tunnels."
    y "....."
    t "but it must be a baby because i haven't heard a \"thank you\"."
    t "so it must not be able to speak yet."
    y "....thank you...."
    show toi toi07 with dissolve
    t "there you go!"
    show toi toi06 with dissolve
    t "but seriously..."
    t "we have got to step up your training."

    t "what even happened down here?"
    y "there was this-"
    show toi toi06
    show toi_blink
    with dissolve
    t "hold on."
    t ".........."
    y "what?"
    hide toi_blink with dissolve
    t "we've got to go."
    t "now."
    y "we do?"
    t "there's.... a lot of footsteps coming our way."
    t "we don't want to be here when they arrive."
    y "get me out of this damn cocoon!"
    t "ugh, here!"
    hide toi
    show toph_body_cloth:
        ypos 100
    with sshake
    "with a quick and calculated step and thrust, toph turns the hard rock around you to sand."
    "you promptly fall on your face."
    "being face-down in the dirt, your \"ow\" comes out slightly muffled."
    yc "nhw."
    t "come on!"
    play sound "audio/earthquake.mp3"
    show black
    "toph grabs the back of your shirt and the two of you ride a wave of earth back to the shore."

    y "wh-aaahhh-!!!"
    play sound "audio/thud.mp3"
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_3
    show toi toi04
    show toi_blink
    with sshake
    y "ngh!"
    y "ow."
    show toi toi09
    hide toi_blink
    with dissolve
    t "are you okay!?"
    y "ungh... my head..."
    show toi toi04 with dissolve
    t "you're fine."
    y "wow, okay, just a rudeness shitstorm today."
    y "how did you even find me?"
    show toi_blink with dissolve
    t "after i caught up with the girl, i sent her to the village."
    t "i figured feng was involved with the tunnels and you'd follow him."
    t "and i came to make sure you were okay."
    hide toi_blink with dissolve
    t "who was that girl in the tunnels?"
    t "and where was feng?"
    t "what the heck is going on?"
    y "feng's got a whole prison down there designed for brainwashing."
    y "bit of a perverted priest vibe, honestly."
    y "very uncomfortable."
    show toi toi09 with dissolve
    t "back up, he's brainwashing people?"
    y "yeah, he's behind a ton of kidnappings, and he's hypnotizing them."
    show toi toi05 with dissolve
    t "....i'm gonna kick that guy's butt!"
    y "slow your roll. don't do anything yet."
    y "i want to think on this a little."
    t "what's to think about?"
    t "let's get down their and deck some dudes!"
    y "this isn't yugioh, toph!"
    y "you can't just kuriboh their blue eyes white dragon!"
    show toi toi09 with dissolve
    y "if anything, they're the kuribohs because there's a billion of them."
    y "and that play probably wouldn't work in an actual duel anyway."
    t "......"
    y "...stop talking about yugioh, toph!"
    y "we have a real problem here!"
    y "look, i think this requires some... finesse."
    show toi toi10 with dissolve
    t "you have finesse?"
    y "would you just..."
    y "don't sass me."
    y "can you just trust me, toph."
    y "do you trust me?"
    show toi toi09 with dissolve
    t "well... yeah, but..."
    y "then let me go down in the tunnels by myself."
    y "i have an idea."
    t "you do?"
    y "yeah, i think if i can grab some of their hypnosis equipment, I can undo some of the damage."
    y "and rescue some girls while i'm at it."
    y "it's the right plan."
    y "and i could use the training anyway."
    t "you're... probably right."
    t "but... alone?"
    t "i could come with you."
    y "no, i don't want to put you in danger."
    y "and the village needs you to look after it."
    y "besides, i'm the avatar -- i can handle myself."
    show toi toi01 with dissolve
    t "i still want to beat him up!"
    show toi toi09 with dissolve
    t "but you're smart, aang."
    t "and tough, when you want to be."
    t "and... i trust you."
    y "thanks, toph."
    y "now let's get out of here, and we'll talk about it later."
    show toi toi02 with dissolve
    t "lead the way."
    $ bk3_day = False
    show blackveil with dissolve
    "you can now travel to the tunnels!"
    $ laogai_travel = True
    show bk3_maze_off:
        xpos 0.18
    with dissolve
    show bk3_maze_on:
        xpos 0.18
    with dissolve
    "click this button on the top of your screen (when it appears) to return to lake laogai!"
    hide bk3_maze_on with dissolve
    hide bk3_maze_off
    hide blackveil
    with dissolve

    jump love_bk3_village_background

label party_crash:
    hide screen earth_money_date
    y "alright, they should be around here somewhere..."
    mv "hello, stranger."
    show tomm tomm01 with Dissolve(1.5)
    y "i'm sorry ladies, i'm waiting for-"
    y "...Katara?"
    y "Toph?"
    y "Wow... you... look beautiful."
    k3 "Tha-"
    show tomm tomm02
    t "Don't talk to the commoner, Katara."
    t "First rule of society."
    y "So... what's going on here?"
    y "there's a party here, right?"
    y "....Hey wait. Did you just call me a commoner?"
    show tomm tomm03
    k3 "There is a party!"
    k3 "For the king's pet bear!"
    y "We're going to ignore that commoner comment, huh?"
    y "Okay, just so I'm clear on that."
    k3 "Toph and i will sneak in with the crowd, tell the king what he needs to hear, and all will be solved!"
    y "That sounds great, and you certainly look the part, but are you sure you can blend in?"
    t "Aang, have you forgetten I'm part of the social elite?"
    y "I think I saw you pull off a part of your toenail yesterday... with your teeth..."
    y "...your {i}teeth{/i}."
    t "Pfffft... when I don't act like the elite it's because I {i}choose{/i} not to."
    t "Not because I can't."
    show tomm tomm01 with dissolve
    t "Trust me, I can guide Katara and me inside without any problems."
    t "Just mentioning my family name will do the trick."
    y "Eh... you sure I shouldn't ask Shady to make up some fake invitation or something?"
    t "Please.... that won't be necessary."
    y "Okay, I guess. But what about me?"
    show tomm tomm03 with dissolve
    t "We'll let you in through the servant entrance once we're in."
    t "A busboy outfit is your best bet to go unnoticed."
    t "....and it's fitting for your class."
    y "...."
    y "....bottle the hurt, avatar...."
    y "keep it together..."

    show expression "bk3/toph/party/bg_alley_epalace.jpg"
    show expression "#000"
    hide expression "#000" with Dissolve(3.0)
    hide tomm
    y "Okay, I have no idea how long this will take so I better get comfortable."
    show tomm tomm04:
        xpos 300
        linear 3.0 xpos 0
    y "Toph?"
    y "Weren't you supposed to open this door from the inside and let me in?"
    t "The guard wouldn't let us in..."
    y "Did you act like a high class member of the social elite?"
    t "I did."
    y "Did you mention your family name?"
    t "I did!"
    y "Awh, shit. Well, too bad. It was a good plan."
    y "Hey, where's Katara?"
    t "When we left, Sokka went running past us carrying a bunch of panties screaming he's innocent."
    t "Some guards and girls were chasing after him."
    t "So katara went to check it out."
    y "Sometimes it feels like Sokka is taking the best route of 'em all."
    t "What?"
    y "Forget it."
    t "I'm going home. Wash this muck off of my face."
    y "(wow she looks really disappointed.)"
    y "Fuck no, you ain't."
    t "The plan has been a bust."
    t "What else is there to do?"
    y "It'd be a waste of all that time you put into gearing up."
    y "And let's be honest... you were looking forward to a party, right?"
    t "....maybe a little."
    y "Then let's have some fun somewhere else!"
    t "How? Where?"
    y "we'll do what we always do... figure it out as we go."
    y "I'm kinda hungry, so let's try and get something to eat first."
    y "I'm sure they've got all sorts of good stuff in a city as big as this."

    show expression "#000" with Dissolve(2.0)
    hide expression "bk3/toph/party/bg_alley_epalace.jpg"
    show text "{color=#ffffff}At first toph hesitantly follows along, but soon enough she's the driving force at trying out as many strange new foods as you can find."
    $ renpy.pause()
    hide text
    hide expression "#000"
    show expression "bk3/toph/party/bg_citystreet1.jpg":
        xpos -1000
        linear 14 xpos 0
    hide tomm
    show tomm tomm11:
        linear 1.0 ypos 20
        linear 1.0 ypos 0
        repeat
    t "Hahahaha!"
    t "I don't think I've eaten this much in a long time!"
    t "It's a good thing I'm not wearing anything with buttons or they would've popped!"
    y "I still can't believe you managed to eat all of that and not barf."
    y "I stopped trying to keep up with you half an hour ago and still feel like I shouldn't make any sudden movements."
    t "You're lacking a healthy appetite, twinkletoes!"
    t "Don't worry, when we're done with your training we'll have fixed that!"
    t "Too bad Katara wasn't with us. Oh well... we'll make up for it sometime later."
    y "Having fun is all about making the most of where and when you are."
    y "But I'm ready to topple over so let's head home."
    "Toph hits you playfully in the shoulder with a short jab." with hpunch
    t "Aaawhh, you big baby! Fine, we'll slowly make our way back to the village."


    show tomm_mgirl_1 with Dissolve(2.0):
        xpos -500
        linear 2.0 xpos 0

    "girl 1" "Oh my god! Look at that, you guys!"
    hide tomm
    show expression "bk3/toph/party/bg_citystreet1.jpg":
        xpos 0
    show tomm tomm12

    show tomm_mgirl_2 behind tomm_mgirl_1:
        xpos -500
        linear 1.0 xpos -400
    "girl 2" "Mmmmmm...."

    show tomm_mgirl_3 behind tomm_mgirl_2:
        linear 1.3 xpos -140


    "girl 3" "Hihihi."
    "girl 1" "It's a little girl on a pretend date with her big brother! How cute!"
    y "The fuck...."
    y "they look like girls but it feels more like a pack of hyena's... going in for the kill."
    "girl 1" "Great makeup!"
    "girl 2" "{size=-5}....for a clown.{/size}"
    y "Do you know them, Toph?"
    show tomm tomm04
    t "No."
    t "Let's... Let's just keep walking..."
    y "But... "

    show tomm_mgirl_1:
        linear 8 xpos 600
    show tomm_mgirl_2:
        linear 8 xpos 600
    show tomm_mgirl_3:
        linear 8 xpos 800
    hide tomm
    show tomm tomm04:

        ypos 0
        linear 1.0 ypos 20
        linear 1.0 ypos 0
        repeat


    t "They're not worth it."
    "girl 1" "Hurry home! It's almost bedtime!"
    "girl 2" "Maybe he'll read you a bedtime story."
    "girl 3" "Or bring you a nice glass of milk!"
    hide tomm_mgirl_1
    hide tomm_mgirl_2
    hide tomm_mgirl_3

    menu:
        "Keep walking":
            y "I could still go back and do horrible things to them."
            t "So could I but... it's useless."
            t "I'm never going to get big and people like that are never going to stop making fun of it."
            t "It's probably why I couldn't get me and Katara in the party..."
            t "...because they see me as a kid playing pranks."
            y "That's bullshit! Who are you? And what did you do to the real Toph?"
            show tomm_mgirl_1 behind tomm:
                xpos 500
                linear 1.0 xpos 0
                linear 12.0 xpos 600
            "girl 1" "Just checking, but he isn't a pedo right?"
            "girl 1" "Blink twice if you need help. HAHAHA!!"

            y "....."
            y "Fuck this passive shit. I gave them a chance to live."
            y "Stay here, Toph... and watch out for blood splatters."
            hide tomm
            hide tomm_mgirl_1
            show tomm_mgirls clothed
            with Dissolve(1.5)
            y "Hey girls. I wanna give you a tip which will save your lives."
            "girl 1" "Hohoho! You gonna threaten us? My dad is head of the city guard."
            "girl 2" "If you so much as lift a finger against us you'll be thrown in jail."
            y "Yeah, I already thought you'd have some sort of leverage like that...."
            y "But no, this is truly some life saving advice."
            y "Ice breaks when subjected to an impact of high enough velocity."
            "girl 1" "What the fuck are you going on about weirdo?"
            y "{i}you{/i} especially should be paying close attention, mickey mouse."
            play sound "audio/whoosh.wav"
            show tomm_mgirls icedup with Dissolve(2.0)
            y "Ice Ice baby."
            y "I left a small opening so you can still hear me."
            y "Wanna breathe and not die? Smash your head on the streets as hard as you can."
            y "Since mickey mouse is the ringleader, I made hers extra hard so she'll have to work a bit harder at it."
            "The girls drop to their knees and start banging their heads on the street."
            hide tomm_mgirls with Dissolve(1.5)
            show tomm tomm04
            t "Ow wow... that's dark stuff, twinkletoes."
            y "I wasn't really going to let them die. Just scar them... er... I mean, scare them."
            show tomm tomm06
            t "...Nah!! Just kidding! It was awesome!"
            t "Look, they already managed to bash the ice open! They'll be fine... relatively."
            t "I kinda wanted to do something like that but I was afraid you'd think of me as bloodthirsty."
            y "You've been training me... I {i}know{/i} you're bloodthirsty."
            y "uh... I see some guards approaching. let's run!"
        "Fuck this shit, time to draw blood":


            y "Enough's enough. They're going down."
            t "Aang, don't... they're just dumb girls."
            y "And I'm a dumb guy, perfect match."
            y "Oh, girls!!"
            hide tomm
            show tomm_mgirls clothed with Dissolve(1.5)
            "girl 1" "Did you get tired of that short stuff?"
            "girl 2" "Wanna hang out with us?"
            y "Fuck no. I just have a question."
            y "Aren't you cold walking around like that?"
            "girl 1" "What are you talking about?"


            show expression "bk3/toph/party/shreds1.png":
                xpos 250 ypos 300
                linear 1.0 xpos -600
            show expression "bk3/toph/party/shreds2.png":
                xpos 250 ypos 300
                linear 1.0 xpos 950
            show tomm_mgirls nude
            with hpunch

            $ renpy.pause ()
            y "I'm talking about you standing there with your tits and pussies all out in the open."
            y "Only a master at waterbending could do this without... casualties..."
            y "Water can cut through steel beams, so fabric isn't much of a problem."
            y "Have a safe trip home girls! Mwahahaha!"
            menu:
                "be creepy":
                    y "Maybe I'll visit you girls one of these nights...."
                    y "...and do... stuff..."
                    y "...using rope and duct tape."
                    y "It would be a unique experience you won't... ever... be able to forget."
                "just give a warning":
                    y "Next time we meet I'm going to be less pleasant."

            show ctc
            pause
            hide ctc
            hide expression "bk3/toph/party/shreds1.png"
            hide expression "bk3/toph/party/shreds2.png"
            "The trio quickly hides behind a cart with cabbages."
            hide tomm_mgirls with Dissolve(1.5)
            "girl 1" "WE.. WE'RE NOT AFRAID OF YOU!"
            "girl 2" "WE'LL MAKE YOU PAY FOR THIS!!"
            y "Oh really?"
            y "HEY EVERYONE! COME TAKE A LOOK!"
            y "THERE'S A COUPLE OF NAKED GIRLS HIDING HERE! WHAT A BUNCH OF PERVERTS!"
            show tomm tomm04 with Dissolve(1.5)
            t "That..."
            y "...was excessive?"
            show tomm tomm06
            t "...WAS AWESOME!!"
            y "Hey, look at that! you can smile again! mission accomplished!"
            y "uh... I see some guards approaching, though. We better make a run for it."

    scene black
    hide expression "bk3/toph/party/bg_citystreet.jpg"
    with dissolve
    "when you finally reach the village, toph is still in high spirits."
    scene toph_home_outside
    show tomm tomm06
    with dissolve
    t "I almost can't stop smiling! Tonight was awesome!"
    y "Well, I don't know about you but I'm dead tired. Goodnight."
    show tomm tomm04
    t "Hey... wait a minute, Aang."
    show tomm fidget
    "Toph starts pacing up and down."
    y "Something the matter?"
    hide tomm
    show tomm tomm08 with Dissolve(1.5):
        xpos -350
    show ctc
    pause
    hide ctc
    t "You got some dirt on your face."
    "you make some halfhearted attempts at wiping your face with your sleeve."
    t "Just lower your face you big oaf!"
    show tomm tomm09
    pause(0.5)
    hide tomm
    show expression "bk3/toph/party/toph_front_kiss.png"
    with Dissolve(2.0)

    "{i}*smoooch*"
    show ctc
    pause
    hide ctc
    hide expression "bk3/toph/party/toph_front_kiss.png"

    show tomm tomm08:
        xpos -350
    y "Di...did you kiss it away? That's unusual."
    show tomm tomm10
    t "Sisters don't kiss their brothers on a pretend date!"
    t "So this proves I'm not a little kid!"
    t "That's all."
    y "I'm not really following your logic, but..."
    y "...You aren't still thinking about what those three trollops were saying are you?"
    t "NO!! ...YES!! ...MAYBE! I DUNNO!"
    y "Okay, okay, stop yelling."
    y "I don't think you really understand what was going on there."
    t "Seems pretty clear to me. They made fun of my undeveloped body."
    y "Nonono. They were giving you shit because they were jealous."
    t "That makes zero sense!"
    y "You really think those three were hanging out with each other because they had boyfriends?"
    y "Oh no. They're just three brats jealous of couples."
    y "They saw you walking around with a guy, figured you were easy prey, and decided to take a few cheap shots."
    show tomm tomm08
    t "You... you really think so?"
    y "I have no doubt about it. But hey, I got a kiss out of it so I'm not complaining!"
    show tomm tomm10
    t "......"
    t "Prepare yourself for tomorrow's training, Aang!"
    t "Don't think this means I'll go easy on you!"
    hide tomm
    "Before you can answer toph enters her home and slams the door close behind her."

    menu:
        "knock on the door":
            t "I'm not home! Go away!"
            y "......."
            y "...every damn time..."
        "leave":
            y "......."
            y "...every damn time..."
            pass
    scene black with dissolve
    $ party_complete = True
    "you head home for the night."
    jump love_bk3_next

label love_june_handjob:
    stop music
    play music "audio/Unwritten Return.mp3"
    hide toju_blink
    hide toju
    with dissolve
    ju "let me undress..."
    ju "i know how you boys like a good show."
    ju "....."
    show toju toju19 with Dissolve(1.5)
    ju "...there."
    show ctc
    pause
    hide ctc
    ju "I can see you're already..."
    show expression "bk3/june/idles/smile.png" with dissolve
    ju "...eager."
    hide expression "bk3/june/idles/smile.png"
    with dissolve
    ju "let's get this taken care of."
    menu:
        "move your hands...":
            y "come on, no need to be shy."
            show toju_blink with dissolve
            ju "....very well."
            show toju toju20 with dissolve
            show ctc
            pause
            hide ctc
            hide toju_blink with dissolve
            ju "so? like what you see?"
            menu:
                "beautiful":
                    $ june_sympathy += 1
                    y "You have a gorgeous body."
                    show toju_blink with dissolve
                    ju "i'm aware."
                    hide toju_blink with dissolve
                    ju "but thank you, all the same."
                    ju "hold on, while i kneel."
                "ugly":

                    y "no, you have fat cow tits and should be ashamed of your body."
                    show expression "bk3/june/idles/angry.png"
                    show toju toju19
                    with dissolve
                    ju "you're such an ass."
                    ju "i'm doing you a fucking favor here."
                    y "we're doing each other a favor."
                    y "and you asked my opinion."
                    hide expression "bk3/june/idles/angry.png"
                    show toju_blink
                    with dissolve
                    ju "whatever."
                    y "get on your knees."
                    ju "fine."
        "kneel!":

            y "get down on the floor."
            y "i want you looking up at me."
            show toju_blink with dissolve
            ju "very well..."








    scene black
    scene hospital_tilted
    with dissolve
    $ totj_hairlock = 'on'

    show totj totj08
    with dissolve
    ju "there."
    ju "is that a nice view?"
    show ctc
    pause
    hide ctc
    menu:
        "great view":
            $ june_sympathy += 1
            y "it's a new personal favorite."
            ju "...you can be sweet when you try, avatar."
        "meh":

            y "I've had better."
            ju "ugh, you're such an asshole."

    y "thanks."
    ju "......"
    ju "well?"
    y "well what?"
    ju "ugh..."
    show totj totj01
    ju "are you gonna take it out or not?"
    y "in a second, but first..."
    menu:
        "\"i like this arrangement\"":
            y "i think this is a good start to our partnership, june."
            show totj totj08
            ju "oh?"
            y "yeah. i think you and will work well together."
            show totj totj01
            ju "maybe..."
        "\"you're a slut\"":

            y "i like that you know your place."
            show totj totj08
            ju "....?"
            y "I'm gonna blow my load on your face, june."
            show totj totj01
            ju "ugh.... you don't have to be so fucking vulgar."

    show ctc
    pause
    hide ctc
    ju "now come on, i'm willing to... repay you..."
    ju "but i haven't got all day."
    y "you have a pretty face, june."
    ju "thank... you?"
    y "and that half-face haircut is pretty sexy, too."
    ju "okay...."
    menu:
        "brush lock of hair aside":
            $ totj_hairlock = 'off'
        "leave it like this":
            $ totj_hairlock = 'on'

    show totj totj02
    if totj_hairlock == 'off':
        y "but i want to see your face..."
        y "...when i make a mess of it."
    else:
        y "so stay just like that..."
        y "so i can make a mess of it."
    ju "......"
    ju "are you..."
    ju "....just take it out, already."

    menu:
        "have her do it":
            y "i think that's part of your role here."
            if june_forced:
                ju "ugh... fine."
            else:
                ju "....fine."
            show totj totj08
            "June leans forward and delicately undoes your belt."
            y "there you go..."
            show totj totj02
            "you feel her fingers slide inside the waist of your pants as she undoes them and pulls them down."
        "help her out":

            y "alright, let's get this party started then."
            "you undo your pants, and drop trou."
            y "there you go."

    play sound "audio/slap.mp3"
    show totj totj03
    with vshake
    ju "oh!"
    "your cock falls out and gives june's face a hearty slap."
    show ctc
    pause
    hide ctc
    if june_forced:
        y "come on, pay your rent."
        ju "fine... come here..."
    else:
        ju "alright, come here..."
    show totj totj04
    with dissolve
    "june's soft fingers and palm curl around the base of your shaft."
    ju "but i do {i}not{/i} want you to make a mess on me, got it?"
    menu:
        "got it":
            y "understood."
            ju "good."
        "we'll see":

            y "let's wait and find out."
            ju "do you want this or not?"
            y "alright, alright..."
            ju "good."

    ju ".....ugh."
    ju "i guess i'll make you feel good."
    show totj totj05
    show ctc
    pause
    hide ctc
    y "uunghhh...."

    "she squeezes and pulls upwards, loosening her warm grip slightly on the way down..."
    "...just to squeeze hard again as she tugs up towards the head."
    "her fingers tenderly roam the length of your cock, sliding all the way up and back again..."
    "tightening and loosening her grip with careful pulsing, june watches your face relax in ecstasy."
    ju "mmm... there you go."
    show ctc
    pause
    hide ctc
    ju "this is... nice."
    y "unnh... fuck..."
    ju "you have a nice cock here."
    ju "{i}really{/i} nice."
    ju "maybe...."
    ju "....nevermind."
    y "what... ah... are you... uh... thinking... about?"
    ju "nothing. just enjoy."
    ju "...and hurry up about it."
    y "you could be more enthusiastic about this, you know."
    y "it might take me some time to-"

    show totj totj13
    y "herk."
    show ctc
    pause
    hide ctc
    ju "how's that, huh?"
    ju "still gonna take you a while?"
    y "f-fuck..."
    ju "come on, baby... cum for me..."
    ju "I can feel you warming in my hand..."
    ju "your nerves are on fire, aren't they?"
    ju "you just want to cum in my hand, don't you?"
    show ctc
    pause
    hide ctc
    ju "let me know when you're close and i'll get out of the way."
    y "yeah... ah... that's not happening."

    show totj totj04 with Dissolve(2.0)
    ju "....."
    ju "what?"
    y "you think i'm going to cum on the floor after this work?"
    y "no, no, no."
    show totj totj07 with Dissolve(2.0)
    ju "...um..."
    y "you're doing this for a big load of splooge."
    y "so... you're going to take a big load of splooge."
    ju "i didn't agree to-"
    ya "grab my cock!"
    ya "do your job!"
    show totj totj09 with Dissolve(2.0)
    ju "......."
    show ctc
    pause
    hide ctc
    ju "I... guess that's... fair..."
    y "(phrasing this as a \"job\" seemed to encourage her...)"
    y "(she seemed willing enough to begin with, but maybe a different option could be to hire her?)"
    y "(she is a bounty hunter after all... maybe brothel clients could be considered bounties?)"
    y "(I still don't know if i even want her to work the brothel...)"
    y "(I'll have to weigh my options later.)"
    ju "come on... come on..."
    y "hmm?"
    ju "get out of there..."
    "June seems fully absorbed in her stroking as her palm twists and fingers curl around the head..."
    "her eyes don't leave your cock as she varies her pace and length of stroke."
    ju "that's it... that's it, baby..."
    ju "let it go... let it all go..."
    show ctc
    pause
    hide ctc
    menu:
        "Keep it nice and slow":
            y "fuck! don't stop!"
            "june digs in deeper, pulling and squeezing and milking you with all she has."
            pass
        "pump it like a supersoaker!":
            y "fuck! faster!"
            show totj totj10
            "June speeds up her pace, pulling and squeezing and milking you with all she has."
    show ctc
    pause
    hide ctc
    "she vigorously works your member as your legs begin to tremble in bliss and urgency."
    ju "I can feel it..."
    ju "the pleasure's building, isn't it?"
    "her voice is soft and seductive, whispering as she works for your cum."
    ju "you're close, aren't you?"
    "you indeed feel the rising pressure surging up from your loins as you clench your muscles trying to hold it back."
    "feeling your approaching climax, june thumbs the underside of the head every time she strokes down, forcing you to the point of no return."
    ya "oh! fuck!"
    show expression "bk3/june/tug/openmouth.png"
    ju "cum in my mouth!"
    ju "I-i don't want it on me!"
    ju "cum! cum in my mouth!"
    show ctc
    pause
    hide ctc
    menu:
        "cum in her mouth":
            hide expression "bk3/june/tug/openmouth.png"
            show totj totj12 with Dissolve(2.0)
            "you grab june's pretty face and force your cock into her mouth...."
            "making sure that her lips fully engulf the head...."
            "but still close enough to the entrance that she'll taste the cum."
            ju "{size=+5}mmmgnh!! mmgh!!"
            show ctc
            pause
            hide ctc
            y "ungh!"
            play sound "audio/splurt2.ogg"
            with flash
            ju "hgmgh! ghm!"
            "the vibration of her moans and mild protests only serve to propel your spunk harder into her throat."
            y "take it, whore!"
            play sound "audio/splurt2.ogg"
            with flash
            y "ahhh...."
            show totj totj08
            "you pull your cock from her mouth, and to her credit, she keeps a tight seal around the head -- making sure not to spill a drop."
            ju "......"
            y "is your mouth full?"
            ju "...mmgn-hmm..."
            y "what was that?"
            ju "...'eth..."
            y "show me."
            show expression "bk3/june/tug/sperminmouth.png" with dissolve
            ju "aahhh....."
            "june opens her mouth, semen tumbling and dripping down her tongue and chin, sticking to her tits and stomach."
            show ctc
            pause
            hide ctc
            ju "doeth thith maketh uth even?"
            menu:
                "definitely":
                    y "i'm certainly satisfied right now."
                    ju "...."
                "at the moment":
                    y "i'm satisfied... for now."
                    ju "...."
            ju "...i nee' oo clean thith themen off."
            ju "'an i go 'ow?"
            menu:
                "in a second":
                    y "not yet, i want a good look."
                    ju "......."
                    ju "...fucking enjoy, then."
                    show ctc
                    pause
                    hide ctc
                "go ahead":

                    pass
        "cum on face":

            y "you know where it's going to go, don't you?"
            ju "yes, i know where it's going to go..."
            ya "stay there!"

            show totj totj11
            ju "right in my mou-"

            y "hngh!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/tug/spermout1.png"
            with flash
            ju "hey!?!"
            y "fuck yeah!"
            play sound "audio/splurt3.ogg"
            hide expression "bk3/june/tug/spermout1.png"
            show expression "bk3/june/tug/spermout2.png"
            with flash
            ju "what the fuck..."
            ju "you just-"
            y "take this, whore!"
            play sound "audio/splurt2.ogg"
            hide expression "bk3/june/tug/spermout2.png"
            show expression "bk3/june/tug/spermout3.png"
            with flash
            show ctc
            pause
            hide ctc
            ju "you... came on my face."
            y "what did you expect?"
            ju "......."
            ju "that was... quite a healthy load."
            hide expression "bk3/june/tug/openmouth.png"
            show totj totj08
            with dissolve
            ju "i hope this makes us even..."
            ju "...and satisfies you for letting me stay here."
            menu:
                "definitely":
                    y "i'm certainly satisfied right now."
                    ju "good."
                "at the moment":
                    y "i'm satisfied... for now."
                    ju "...."
            ju "...i need to go clean this sperm off my face."
            ju "again."
            ju "I wish you'd stop doing that."
            ju "can i go now?"
            menu:
                "in a second":
                    y "not yet, i want a good look."
                    ju "......."
                    ju "...fucking enjoy, then."
                    show ctc
                    pause
                    hide ctc
                "go ahead":

                    pass

    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label love_june_handjob2:
    stop music
    play music "audio/Unwritten Return.mp3"
    hide toju_blink
    hide toju
    with dissolve
    ju "let me undress..."
    ju "i know how you boys like a good show."
    ju "....."
    show toju toju19 with Dissolve(1.5)
    ju "...there."
    show ctc
    pause
    hide ctc
    ju "I can see you're already..."
    show expression "bk3/june/idles/smile.png" with dissolve
    ju "...eager."
    hide expression "bk3/june/idles/smile.png"
    with dissolve
    ju "let's get... this... taken care of."








    scene black
    scene hospital_tilted
    with dissolve
    $ totj_hairlock = 'on'

    show totj totj08
    with dissolve
    ju "there."
    ju "is that a nice view?"
    show ctc
    pause
    hide ctc
    y "sure."
    ju "......"
    ju "well?"
    y "well what?"
    ju "ugh..."
    show totj totj01
    ju "are you gonna take it out or not?"
    y "in a second, but first..."
    show ctc
    pause
    hide ctc
    menu:
        "brush lock of hair aside":
            $ totj_hairlock = 'off'
        "leave it like this":
            $ totj_hairlock = 'on'

    show totj totj02
    if totj_hairlock == 'off':
        y "i want to see your face..."
        y "...when i make a mess of it."
    else:
        y "stay just like that..."
        y "so i can make a mess of you."
    ju "......"
    ju "are you..."
    ju "....just take it out, already."

    menu:
        "have her do it":
            y "i think that's part of your role here."
            ju "....fine."
            show totj totj08
            "June leans forward and delicately undoes your belt."
            y "there you go..."
            show totj totj02
            "you feel her fingers slide inside the waist of your pants as she undoes them and pulls them down."
        "help her out":

            y "alright, let's get this party started then."
            "you undo your pants, and drop trou."
            y "there you go."

    play sound "audio/slap.mp3"
    show totj totj03
    with vshake
    ju "oh!"
    "your cock falls out and gives june's face a hearty slap."
    show ctc
    pause
    hide ctc
    ju "alright, come here..."
    show totj totj04
    with dissolve
    "june's soft fingers and palm curl around the base of your shaft."
    ju "but i do {i}not{/i} want you to make a mess on me, got it?"
    y "let's wait and find out."
    ju ".....ugh."
    ju "i guess i'll make you feel good."
    show totj totj05
    show ctc
    pause
    hide ctc
    y "uunghhh...."

    "she squeezes and pulls upwards, loosening her warm grip slightly on the way down..."
    "...just to squeeze hard again as she tugs up towards the head."
    "her fingers tenderly roam the length of your cock, sliding all the way up and back again..."
    "tightening and loosening her grip with careful pulsing, june watches your face relax in ecstasy."
    ju "mmm... there you go."
    show ctc
    pause
    hide ctc
    ju "this is... nice."
    y "unnh... fuck..."
    ju "you have a nice cock here."
    ju "{i}really{/i} nice."
    ju "maybe...."
    ju "....nevermind."
    y "what... ah... are you... uh... thinking... about?"
    ju "nothing. just enjoy."
    ju "...and hurry up about it."
    y "you could be more enthusiastic about this, you know."
    y "it might take me some time to-"

    show totj totj13
    y "herk."
    show ctc
    pause
    hide ctc
    ju "how's that, huh?"
    ju "still gonna take you a while?"
    y "f-fuck..."
    ju "come on, baby... cum for me..."
    ju "I can feel you warming in my hand..."
    ju "your nerves are on fire, aren't they?"
    ju "you just want to cum in my hand, don't you?"
    show ctc
    pause
    hide ctc
    ju "let me know when you're close and i'll get out of the way."
    y "yeah... ah... that's not happening."

    show totj totj04 with Dissolve(2.0)
    ju "....."
    ju "what?"
    y "you think i'm going to cum on the floor after this work?"
    y "no, no, no."
    show totj totj07 with Dissolve(2.0)
    ju "...um..."
    y "you're doing this for a big load of splooge."
    y "so... you're going to take a big load of splooge."
    ju "i didn't agree to-"
    ya "get to work! grab my cock!"
    show totj totj09 with Dissolve(2.0)
    ju "......."
    ju "I... guess that's... fair..."
    show ctc
    pause
    hide ctc
    ju "come on... come on..."
    y "hmm?"
    ju "get out of there..."
    "June seems fully absorbed in her stroking as her palm twists and fingers curl around the head..."
    "her eyes don't leave your cock as she varies her pace and length of stroke."
    ju "that's it... that's it, baby..."
    ju "let it go... let it all go..."
    show ctc
    pause
    hide ctc
    menu:
        "Keep it nice and slow":
            y "fuck! don't stop!"
            "june digs in deeper, pulling and squeezing and milking you with all she has."
            pass
        "pump it like a supersoaker!":
            y "fuck! faster!"
            show totj totj10
            "June speeds up her pace, pulling and squeezing and milking you with all she has."
    show ctc
    pause
    hide ctc
    "she vigorously works your member as your legs begin to tremble in bliss and urgency."
    ju "I can feel it..."
    ju "the pleasure's building, isn't it?"
    "her voice is soft and seductive, whispering as she works for your cum."
    ju "you're close, aren't you?"
    "you indeed feel the rising pressure surging up from your loins as you clench your muscles trying to hold it back."
    "feeling your approaching climax, june thumbs the underside of the head every time she strokes down, forcing you to the point of no return."
    ya "oh! fuck!"
    show expression "bk3/june/tug/openmouth.png"
    ju "cum in my mouth!"
    ju "I-i don't want it on me!"
    ju "cum! cum in my mouth!"
    show ctc
    pause
    hide ctc
    menu:
        "cum in her mouth":
            hide expression "bk3/june/tug/openmouth.png"
            show totj totj12 with Dissolve(2.0)
            "you grab june's pretty face and force your cock into her mouth...."
            "making sure that her lips fully engulf the head...."
            "but still close enough to the entrance that she'll taste the cum."
            ju "{size=+5}mmmgnh!! mmgh!!"
            show ctc
            pause
            hide ctc
            y "ungh!"
            play sound "audio/splurt2.ogg"
            with flash
            ju "hgmgh! ghm!"
            "the vibration of her moans and mild protests only serve to propel your spunk harder into her throat."
            y "take it, whore!"
            play sound "audio/splurt2.ogg"
            with flash
            y "ahhh...."
            show totj totj08
            "you pull your cock from her mouth, and to her credit, she keeps a tight seal around the head -- making sure not to spill a drop."
            ju "......"
            y "is your mouth full?"
            ju "...mmgn-hmm..."
            y "what was that?"
            ju "...'eth..."
            y "show me."
            show expression "bk3/june/tug/sperminmouth.png" with dissolve
            ju "aahhh....."
            "june opens her mouth, semen tumbling and dripping down her tongue and chin, sticking to her tits and stomach."
            show ctc
            pause
            hide ctc
            ju "thatisthfied?"
            y "i'm certainly satisfied right now."
            ju "good."
            ju "...i nee' oo clean thith themen off."
            ju "'an i go 'ow?"
            menu:
                "in a second":
                    y "not yet, i want a good look."
                    ju "......."
                    ju "...fucking enjoy, then."
                    show ctc
                    pause
                    hide ctc
                "go ahead":

                    pass
        "cum on face":

            y "you know where it's going to go, don't you?"
            ju "yes, i know where it's going to go..."
            ya "stay there!"

            show totj totj11
            ju "right in my mou-"

            y "hngh!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/tug/spermout1.png"
            with flash
            ju "hey!?!"
            y "fuck yeah!"
            play sound "audio/splurt3.ogg"
            hide expression "bk3/june/tug/spermout1.png"
            show expression "bk3/june/tug/spermout2.png"
            with flash
            ju "what the fuck..."
            ju "you just-"
            y "take this, whore!"
            play sound "audio/splurt2.ogg"
            hide expression "bk3/june/tug/spermout2.png"
            show expression "bk3/june/tug/spermout3.png"
            with flash
            show ctc
            pause
            hide ctc
            ju "you... came on my face."
            y "what did you expect?"
            ju "......."
            ju "that was... quite a healthy load."
            hide expression "bk3/june/tug/openmouth.png"
            show totj totj08
            with dissolve
            ju "i hope you're statisfied."
            y "i'm certainly satisfied right now."
            ju "good."
            ju "...i need to go clean this sperm off my face."
            ju "again."
            ju "I wish you'd stop doing that."
            ju "can i go now?"
            menu:
                "in a second":
                    y "not yet, i want a good look."
                    ju "......."
                    ju "...fucking enjoy, then."
                    show ctc
                    pause
                    hide ctc
                "go ahead":

                    pass

    scene black with dissolve
    jump love_bk3_village_background

label toph_walk:
    $ toph_chat = 9
    scene black with dissolve
    "you and toph wander out of the village..."
    show expression "bk3/toph/walk/background.jpg"
    show totw totw01
    with Dissolve(2)
    t "It's... nice that it's cool out tonight."
    y "yeah."
    y "it's pretty perfect for a stroll."
    t "i'm... glad we're doing this."
    y "me too."
    t "come on, let's keep walking."
    hide totw
    hide expression "bk3/toph/walk/background.jpg"
    show expression "bk3/toph/walk/background.jpg":
        xpos -1000
        linear 40 xpos 0
        repeat


    show totw totw01:
        ypos 0
        linear 2 ypos 20
        linear 2 ypos 0
        repeat
    with Dissolve(2.0)
    y "hey, what if i-"
    y "Ouch!!" with hpunch
    y "my fucking foot!"
    y "what's with all these stupid rocks!"
    show totw totw04
    t "Hahaha!"
    t "I'll have to start calling you \"broken toes\" instead of \"twinkle toes\"!"
    y "It's because it's so damn dark!"
    y "I can hardly see where we're walking."
    show totw totw01
    t "Really? I didn't notice."
    y "...right."
    y "Time to firebend myself a light."
    show totw totw03 with hpunch
    t "No way! I didn't bring you out here to cheat, Aang."
    y "So... this is more training to see in the dark?"
    show totw totw01
    t "umm... not necessarily."
    t "But that doesn't mean I want you to ruin the mood with some crackling fire."
    t "Besides you need to learn to sense the rocks around you."
    t "To feel your surroundings."
    y "Feel my surroundings?"
    "You casually lay your hand on Toph's lower back."
    y "Like this?"
    show totw totw00 with Dissolve(1.5)
    "Toph starts walking a little closer to you making it easier to hold her."
    t "No... but keep doing it anyway."
    $ renpy.pause()
    "*crack*" with hpunch
    y "fuuuucckk!"
    y "damn these rocks!"
    t "Let's take a short break."
    hide expression "bk3/toph/walk/background.jpg"
    hide expression "bk3/toph/walk/stars.png"
    hide totw
    show expression "bk3/toph/walk/background.jpg"
    show totw totw01
    show expression "bk3/toph/walk/stars.png"
    with Dissolve(1.5)

    "You and toph stand still and listen to the sounds around you. "
    "A small, soft breeze and the sound of crickets can be heard."
    "Just when you want to say something to toph, you hear a soft moaning."
    "Toph leans towards you and starts whispering."

    hide totw
    show totw totw01:
        xzoom 1.4 yzoom 1.4
        xpos -350 ypos -50
    with dissolve
    t "hey..."
    t "...Do you hear that!?"
    t "There's someone over the hill enjoying... an activity."
    "The sopping sound and increasing volume of the moaning leaves no doubt about what sort of activity is going on."
    t "I'm not entirely sure who she is, but she's by herself and I think..."
    y "We should go and take a peek. "
    t "What?"
    show totw totw03 with hpunch
    t "No!!"
    y "Oh, come on. It'll be fun!"
    show totw totw01
    t "You want fun? Fine."
    y "What?"
    t "Let's combine training with fun."
    t "Can you see that big funny shaped rock over there?"
    y "No."
    t "Last one to reach it has to do whatever the other says!"
    t "And you can't firebend light!"
    hide totw with dissolve
    "before you can agree, Toph runs off in the dark."
    y "This is definitely a ploy to keep me from peeking at that mystery girl doing nasty things...."
    y "Aw shit..."
    show expression "bk3/toph/walk/background.jpg":
        xpos 0
        linear 2 xpos 1000
        repeat
    show totw totw100:
        xpos -300
        linear 4.0 xpos 300
    pause(5.0)
    show totw totw100:
        xpos 300
        easein 2.0 xpos 600
        easein 2.0 xpos 300
        repeat



    y "Hey, you had a headstart!"
    t "Then you'll just have to try harder!"
    "Barely avoiding the rocks, you start running with all you have."
    scene black
    with Dissolve(2.0)
    "After a final wild dash, you reach the funny shaped rock a few seconds before Toph does."



    show expression "bk3/toph/walk/background.jpg"
    show expression "bk3/toph/walk/rockformation.png"
    y "*pant...* I... *pant...* beat you!"
    show totw totw02:
        xpos 300
        linear 1.0 xpos 0

    t "Well done!"
    t "And you didn't trip over a single rock!"
    y "Was that your actual aim?"
    t "I did notice you learn a lot faster when there's urgency and some sort of a reward."
    y "hey... did you create this rock formation?"
    t "No."
    y "Really?"
    y "because either I have a one track mind...."
    y "....or this is made to represent someone's repressed desire for something."
    t "these are perfectly normal rocks."
    y "Okay, whatever you say."
    t "Well... I guess you get to tell me what to do now..."
    t "At least try and keep it within limits."
    y "Hehehe, the possibilities are endless!"
    t "Really? I have a suspicion about the nature of what you'll ask."
    y "Maybe I can surprise you!"
    menu:
        "I'd like to see you naked":
            y "how about... stripping?"
            show totw totw09 with Dissolve(1.5)
            t "Yeah, that's sort of what I was expecting."
            t "But... right here?"
            t "Out in the open?"
            y "You're looking extra cute with the moonlight reflecting off of you right now."
            y "And I want to burn that image into my mind... so I can keep it with me forever."
            t "Oh..."
            t "well... you do make it hard to refuse..."
            y "There's no one around."
            y "...with the exception of that one girl."
            y "and she seemed occupied."
            t "...okay."
            "With just a sliver of hesitation Toph takes off her clothes."
            show totw totw06 with Dissolve(2)
            show ctc
            pause
            hide ctc
            t "Could you say something?"
            t "It feels kinda weird to just stand here being watched in silence."
            y "You look beautiful."
            t "...really?"
            y "May I go limp forever if I'm not telling the truth."
            t "Most people would say something like, \"may I drop dead\"..."
            y "I'd prefer that over going limp."
            $ totw_clothes_sitondick = False
        "Tell me about the kinkiest sexual fantasy you ever had":




            y "what's your naughtiest fantasy?"
            t "Really?"
            t "You don't want me to... you know... touch your dick or something?"
            y "There's time enough for that sometime later."
            y "...though i like where your head's at."
            y "Right know I'd like to get to know you better."
            t "I'm not sure about this...."
            y "Oh, come on."
            y "This is pretty tame stuff I'm asking."
            t "Ooooo.... there's nothing tame about what I'm thinking."
            y "Trust me. There's nothing you can phase me with."
            t "Fine... I'll tell you."
            t "Just don't judge me."
            t "It's kinda wild..."
            t "I've fantasized about... doing something sexy... with you."
            y "Yeah?"
            t "and then Katara unsuspectingly walks in just when I'm about to cum and then I spray all over her... face."
            show totw totw09
            t "I can't believe I'm telling you this!!!"
            y "I've heard stranger fantasies."
            y "Does it have to be katara or can it be someone else?"
            t "Definitely Katara."
            y "Wow, you must really like her."
            t "That's not entirely the reason."
            y "Well.. I can't guaranteed Katara will come around, but I can help with doing something sexy."
            $ totw_clothes_sitondick = True
        "I wanna smell and lick your armpit":

            y "i want to smell and lick your armpit."
            show totw totw09
            t "My what?"
            y "Your armpit."
            t "Why?!?"
            y "Are you going back on your word?"
            t "No... it's just..."
            t "It's just..."
            t "...it's really not what I expected you'd ask for."
            t "Well, I guess it could be worse."
            show totw totw10 with Dissolve(1.5)
            t "Like... like this?"
            y "Show me a little more."
            t "Look... we've been running, I'm sweating..."
            t "I really don't think this will be a good experience for you."
            y "It may be sweat, but it's {i}your{/i} sweat."
            y "And that makes all the difference in the world."
            t "Well, if you put it like that."
            show totw totw11 with Dissolve(1.5)
            show expression "bk3/toph/walk/breath.png":
                alpha 0.1
                xpos 650 ypos 380 xzoom 1 yzoom 1
                linear 6.0 xpos 400 alpha 0.0 xzoom 1 yzoom 1
                repeat
            t "Are you sure you don't want me to get naked instead?"
            y "Nah, this is perfect."
            hide expression "bk3/toph/walk/breath.png"
            show expression "bk3/toph/walk/armpit_sniff.png":
                xpos -70
                linear 1.0 xpos 0
            y "*Sniff* *Sniff*"
            t "This is so embarrassing."

            show expression "bk3/toph/walk/pink.png"
            hide expression "bk3/toph/walk/pink.png" with Dissolve(1.5)
            hide expression "bk3/toph/walk/armpit_sniff.png"
            show totw_lick:
                ypos 0 xpos 0
                linear 1.0 ypos -30 xpos -20
                repeat
            show expression "bk3/toph/walk/armpit_enjoy.png"
            t "This... "
            t "This feels... kinda nice."
            t "I mean it's definitely weird, but still nice."
            hide totw_lick with Dissolve(1.5)
            hide expression "bk3/toph/walk/armpit_enjoy.png"
            show totw totw09 with Dissolve(1.5)
            t "I feel dirty and clean at the same time!"
            $ totw_clothes_sitondick = True

    t "let's sit down for a moment."

    hide expression "bk3/toph/walk/rockformation.png"
    hide totw
    show expression "bk3/toph/walk/moonstars2.png"

    show totw totw12 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "Heh...."
    t "What?"
    y "It's like you're sitting on... nevermind."
    y "I'm kinda surprised this rock doesn't have \"sokka was here\" written on it."
    t "That's a thing?"
    y "I've seen it pop up here and there."
    t "ahum..."
    t "You said that these rocks look like a dick?"
    y "Well, not out loud, put I've been hinting at it pretty hard."
    t "I've never really seen... well, never felt one."
    y "...."
    t "Not even yours...."
    t "Perhaps... we could... change that."
    menu:
        "i'd like that":
            pass
        "are you sure?":
            pass
    y "i..."
    play sound "audio/thud.mp3"
    show totw totw13
    show expression "bk3/toph/walk/jumplines.png"
    $ renpy.pause(0.3)
    hide expression "bk3/toph/walk/jumplines.png"

    show expression "bk3/toph/walk/shopgirl.png" with hpunch



    girl "{size=30}Hey guys!{/size}"
    y "Aaaah!!"
    if totw_clothes_sitondick == True:
        "A startled Toph is standing next to you."
        t "What the hell! Don't scare us like that!"
    else:
        "A startled Toph is standing behind you."
        y "You nearly gave me a heart attack!"
    y "Oh, hey! you're the girl from the shop."
    girl "Sorry! I really didn't mean to sneak up on you guys."
    girl "I was just over there... doing something..."
    y "(so she was the mystery girl...)"
    girl "I heard people talking so I came to take a look at who it was."
    girl "I didn't expect it would be you."
    girl "I see you discovered my sculpture!"
    girl "I call it \"big rock two smaller rocks\"."
    y "Makes sense."
    girl "It's my favorite one, but I have more."
    girl "Would you like to see them?"
    y "Maybe later."
    girl "I'm thinking about making some smaller ones and selling them in the shop."
    y "Ehm, okay?"
    girl "You see, I've found a surefire way to sell them!"
    menu:
        "I'd love to hear about money making scemes":
            y "tell me about it."
            girl "I had this certain product and it was selling like crazy."
            girl "The problem was I was keeping it on the highest shelves... which I need to stand on a chair to reach."
            girl "So I started putting them on the lower shelf for easy access... but then..."
            y "....?"
            girl "Nobody wanted it anymore!"
            girl "Instead, they started buying something else at the same quantities as the first product!"
            y "Really?"
            girl "Yeah! I had moved it from the lowest shelf to the highest."
            girl "To make a long story short, after some experimenting, i made a discovery..."
            girl "whatever I put on the highest shelf is a guaranteed hit!"
            girl "Could it be magic?!?"
            y "....That must be it."
        "Tell me all about it... another time":
            y "maybe some other time."
            girl "Okay!"
    if totw_clothes_sitondick == False:
        girl "I see you are less dressed than usual, Toph."
        girl "Did you perhaps also discover the joys of nudism?"
        girl "Starting at night is a smart move."
        girl "Less people around makes it easier to get into the groove of things."
        t "I... this... this isn't that."
    girl "Am... am I ruining a good mood you guys had going?"
    girl "I'm so sorry! I didn't notice!"
    girl "I'll leave you alone! Sorry for the intrusion!"
    girl "See you later!"
    hide expression "bk3/toph/walk/shopgirl.png" with Dissolve(1.5)


    show expression "bk3/toph/walk/rockdick_big.png":
        xpos -200
    hide totw
    show totw totw09:
        xzoom 0.8 yzoom 0.8
        ypos 150 xpos 150
    with dissolve
    t "She scared the living daylights out of me."
    y "Yeah, I noticed."
    y "Ahum, I bet no one would disturb us at your place."
    y "It has a big sturdy door with a lock."
    t "Sorry, Aang... but that little jumpscare has me totally out of it. "
    t "But we'll absolutely pick up were we left some other time."
    t "ummm...."
    play sound "audio/kiss.mp3"
    with pflash
    "Toph gives you a quick kiss."
    scene black with dissolve
    "the walk back is mostly quiet between the two of you, but it's comfortable."
    "you just enjoy each other's company in the soft moonlight."
    "You walk toph back home and go to sleep."
    show ctc
    pause
    hide ctc
    jump love_bk3_next

label love_house_fire:
    play music "audio/roaring_fire.mp3"
    $ bk3_day = False
    y "*...cough...*"
    y "........"
    y "*cough...* *cough...*"
    y "........"
    y "*cough!* *cough!* *cough!*"
    y "what... *cough!*"
    scene black
    scene inside_shack
    show blackveil
    with dissolve
    show expression "#d3d3d3":
        alpha 0.0
        linear 6 alpha 0.6

    y "what the...."
    y "is that smoke?"
    y "what-"
    ya "oh, fuck!"
    ya "fire!"
    ya "there's a fucking fire!"

    ya "shit!"
    ya "shit, shit, shit!"
    menu:
        "try to find the source":
            y "uh... looks like the walls and the roof are on fire."
            y "so."
            y "that's a thing."
            ya "time to get the fuck out of here!"
        "open the door":

            pass

    "the door is bolted from the outside."
    y "oh."
    y "Oh, no."
    y "that's not good."
    menu:
        "yell for help":
            ya "help!"
            ya "someone!"
            ya "anyone!"
            ya "i keep my porn in here!"
        "kick down door":

            with vshake
            ya "would..."
            with vshake
            ya "you..."
            with vshake
            ya "fucking..."
            with vshake
            ya "open!"
    t "aang!"
    t "i'm here to help!"
    y "toph?"
    k3 "me too!"
    ya "well, get me the fuck out!"
    k3 "it's chained and too hot to touch!"
    ya "chained!?!"
    t "stand back!"
    play sound "audio/thud.mp3"
    with sshake
    "with a massive thud, the door rips off its hinges and slams to the back of your house, forced by a sudden push of earth."
    y "thank... uh... good... ness..."
    t "aang!"
    yc "no... toast... thanks..."
    t "what?"
    play sound "audio/thud.mp3"
    scene black with fade
    show ctc
    pause
    hide ctc
    k3 "aang? aang!!"
    k3 "wake up!"
    $ lovehousefire = 1
    jump love_bk3_village_background

label love_house_fire_cont:
    hide screen earth_money_date
    if lovehousefire ==2:



        hide toki
        hide toki_angry
        hide toi
        hide tocs_fire2
        with dissolve
        stop music
        play music "audio/Unity.mp3"
        "click on the fire when it appears to put it out."

    if lovehousefire ==3:
        scene black
        scene lake_laogai_2
        with dissolve
        stop music
        play music "audio/Unity.mp3"
        "click on the water to put it in the basin."
    jump lovehousefiregame

label lovehousefiregame:


    if housefire_wins ==0:
        call screen housefire_1
    if housefire_wins ==1:
        call screen housefire_2
    if housefire_wins ==2:
        call screen housefire_3
    if housefire_wins ==3:
        call screen housefire_4
    if housefire_wins ==4:
        call screen housefire_5

label housefirescores:
    $ housefire_wins +=1
    play sound "audio/air.wav"
    if housefire_wins >=5:
        play sound "audio/whoosh.wav"
        jump housefirewin

    if housefire_wins ==1:
        ya "one down!"
    if housefire_wins ==2:
        ya "that was close!"
    if housefire_wins ==3:
        ya "how many more are there?"
    if housefire_wins ==4:
        ya "last one!"
    jump lovehousefiregame

label housefirewin:
    if lovehousefire ==3:
        scene black with dissolve
        "digging deep into your newfound earthbending skills, you force the large basin back to the village."
    if lovehousefire ==2:
        scene black with dissolve
        "just as the fire is raging too high to maintain, toph appears."
    jump love_bk3_village_background


label joodee_boobjob:
    $ joodee_revenge = True
    jd "w-wait... we can maybe-"
    ya "you want to make it up to me, don't you?"
    jd "i... i..."
    ya "and your job requires you to {i}obey orders{/i} doesn't it?"
    jd "y-yes... i must... obey orders..."
    y "then do your job, and lie there!"
    y "hmmmm...."


    y "You've got some great undies, but that bra has to go."
    jd "What!? Why?"
    "you reach down..."
    show toob toob01 with vshake
    "...and rip off her bra."
    jd "ayee!"
    show ctc
    pause
    hide ctc
    y "Isn't that better?"
    jd "no!"
    y "stop complaining!"
    y "if you didn't want this to happen, you shouldn't have tried to kill me in my sleep!"
    jd "I-i'm sorry!"
    ya "{i}sir{/i}."
    jd "i-i'm sorry, sir!"
    y "now, are you going to do your job or not?"
    jd "i'm not sure this is part of my job..."
    y "Sure it is!"
    y "But you know... just as a side thought..."
    y "I think you could easily get a new job if Long Feng fires you."
    jd "What?! No!!"
    jd "I have a mortgage!"
    jd "Being fired is a death sentence in this job market!"
    "you pull out your cock while she's complaining."
    y "Oh, wow... my dick feels a bit cold."
    jd "Maybe if you put your clothes back on..."

    show toob toob02 with Dissolve(1.5)
    "you straddle her chest, slipping between her plump tits."
    "her plush mounds almost completely engulf your cock."
    y "OOoooh.... this is nice and warm!"
    y "So comfy and soft...."
    y "Makes me want to slide up and down."
    show toob toob03
    y "Like this! See?"
    show ctc
    pause
    hide ctc
    jd "Th-thank you for the demonstration, sir..."
    jd "but... if you could just stop..."
    y "I can almost reach your mouth with the tip of my dick."
    y "I think I should go a bit faster."
    jd "That... that's really not necessary..."
    jd "In fact, I'd prefer it if you wouldn't."
    show ctc
    pause
    hide ctc
    y "Here I go!"

    show toob toob04
    jd "Ah!"
    show ctc
    pause
    hide ctc
    y "Oh yeah, this is the stuff."
    jd "This is -ah!-"
    jd "slightly -ah!-"
    jd "uncomfortable -ah!-"
    ya "good!"
    ya "you tried to murder me, joo dee!"
    ya "you think your... ungh... swollen... hng... doughy tits... can make up for trying to fucking kill me?"
    ya "use them to milk out my cum and maybe i won't be so angry any more!"
    ya "you don't want me to be angry any more, do you?"
    jd "i... i don't know!"
    show ctc
    pause
    hide ctc
    y "well, lucky for you, i'm a kind dom."
    y "so, here, hold your boobs tight and it won't be as uncomfortable."
    show toob toob05
    show ctc
    pause
    hide ctc
    y "much better right?"
    jd "Y...yeah, but..."
    y "Fuck yeah! You've got some great fucking tits."
    ya "especially for a criminal."
    jd "I'm... i'm not a criminal!"
    ya "what!?"
    jd "i-i mean... i'm a criminal! i'm sorry!"
    jd "please-!"
    show ctc
    pause
    hide ctc
    y "I've been dying to fuck these...."
    y "Hold tight. I'm going to put some weight behind this!"
    jd "Please don't!"
    ya "I'm going to bang your tits off!"
    jd "Nonononono!"


    show toob toob100
    jd "Aaah!!"
    show ctc
    pause
    hide ctc
    y "Fuck! this is great stuff!"
    jd "my breasts aren't made for this!"
    y "yes they fucking are!"
    y "We're going to have a lot of fun together, JD!"
    jd "ungh... hmph... ah... unh..."
    ya "beg for my forgiveness!"
    ya "you want this to end?"
    jd "ungh... ah... yes...!"
    ya "then beg!"
    ya "convince me you're sorry!"
    ya "or it won't end here!"
    jd "i-i'm so sorry!"
    jd "take... take out all your anger on me!"
    jd "on my big, fluid tits!"
    jd "forgive me, avatar! forgive me!"
    jd "fuck my big sinful tits and forgive me!"

    ya "oh, i'm feeling forgiving now!"
    ya "I'll go ahead and end this!"
    jd "Yes! Please end this!"

    menu:
        "piss in her mouth!":
            hide toob
            show toob toob101
            with Dissolve(1.5)
            y "nnghh...."
            y "open your mouth, girl!"
            jd "what are-"
            ya "take this, you bitch!"
            show toob_piss:
                xpos 353 ypos 291
            y "ahhhh...."
            jd "*Gurgle gurgle*"
            hide toob_piss
            show expression "bk3/joodee/boobjob/piss4.png"
            with Dissolve(2.0)
            "you fill up joo dee's mouth with piss until it overflows and runs down her cheeks into her hair."
            y "Aaah. All done."
            show toob toob102 with Dissolve(2.0)
            show ctc
            pause
            hide ctc
            y "I'll let myself out."
            y "you think about what you did."
            y "i'll see you soon, sugar tits."
            jd "gurg..."
            show ctc
            pause
            hide ctc
        "Cum on her face and boobs!!":

            hide toob
            show toob toob101
            with Dissolve(1.5)
            y "open your mouth, girl!"
            jd "what are-"
            ya "take this, you bitch!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/joodee/boobjob/sperm1.png"

            y "hngh!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/joodee/boobjob/sperm2.png"
            jd "unghhh... you're..."
            y "fuck!"
            play sound "audio/splurt1.ogg"
            show expression "bk3/joodee/boobjob/sperm3.png"
            show ctc
            pause
            hide ctc
            y "Aaaah... that was sublime."
            show toob toob102 with Dissolve(2.0)
            y "I'll let myself out."
            y "you think about what you did."
            y "i'll see you soon, sugar tits."

            jd "s...sorry..."
            jd "gurg..."
            show ctc
            pause
            hide ctc
        "Cum on her twat":

            hide toob
            show toob toob06
            "In one fluid motion you flip JooDee's legs up."
            y "let's get rid of those panties."
            jd "nonono! don't!"

            show toob toob07
            "you pull her panties off and spread her legs with no real resistance."
            y "(she must really have to follow orders...)"
            jd "Wha...."
            show toob toob08

            y "just hold still girl."
            jd "what are-"
            ya "take this, you bitch!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/joodee/boobjob/spermtwat1.png"

            jd "unghhh... you're..."
            y "fuck!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/joodee/boobjob/spermtwat2.png"
            jd "no...."
            y "hngh!"

            play sound "audio/splurt1.ogg"
            show expression "bk3/joodee/boobjob/spermtwat3.png"
            show ctc
            pause
            hide ctc
            y "ahh... that was satisfying."
            y "I'll let myself out."
            y "you think about what you did."
            y "i'll see you soon, sugar tits."
            jd "hurg...."
            jd "I'm... covered in..."
            jd "uhhn...."
            show ctc
            pause
            hide ctc

    scene black with dissolve
    "you leave joo dee in a puddle, and head back to the village."
    $ bk3_day = False
    jump love_bk3_village_background

label toph_comfort:
    $ laogai_travel = True
    $ toph_comfort_talk = True
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_night
    show toi toi02
    with dissolve
    t "welcome home!"
    show toi toi07 with dissolve
    t "how was your day, honey?"
    y "well... that's pleasant."
    show toi toi04 with dissolve
    t "....I thought it was funny."
    t "i'm not some housewife."
    y "......"
    t "anyway, how'd your day go? for real?"
    y "it... went."
    y "but i spoke with suki, and she pointed out that you could help me clear the rubble and rebuild my house."
    show toi toi06 with dissolve
    t "did she?"
    y "yeah."
    y "do you think you could do that?"
    show toi toi09 with dissolve
    t "i..."
    t "...i don't think that's a good idea."
    y "what? why?"
    show toi toi06 with dissolve
    t "it's just not!"
    y "....."
    t "i don't want to talk about it any more!"
    y "....."
    y "come on, you've got to give me a reason."
    show toi_blink with dissolve
    t "well... you..."
    t "you... need to be stronger, obviously!"
    hide toi_blink with dissolve
    t "our next training will be focused on getting you strong enough to do it yourself."
    t "I want you..."
    show toi toi09 with dissolve
    t "...."
    t "i want you... to be self-reliant."
    y "....is that all?"
    show toi toi06
    show toi_blink
    with dissolve
    t "obviously."
    t "it's for training reasons that you'll be staying here for now."
    y "......"
    y "It's not that you enjoy my company?"
    hide toi_blink
    show toi toi09
    with dissolve
    t "what?"
    t "no..."
    t "......"
    show toi toi04
    show toi_blink
    with dissolve
    t "okay... maybe a little..."
    y "uh-huh."
    hide toi_blink with dissolve
    t "we'll pick up your training tomorrow."
    t "let's get some rest."
    y "don't have to tell me twice..."
    scene black with dissolve
    "you lay on your bed and fall asleep before your head hits the pillow."
    show ctc
    pause
    hide ctc
    t "no! don't!"
    t "i'll fight you!"
    t "let me out!"
    y "whuzza... who now...?"
    play sound "audio/earthquake.mp3"
    with sshake
    y "whoa!"
    y "what the hell!?"
    t "i'll take you all down!"
    play sound "audio/earthquake.mp3"
    with sshake
    y "oh, shit!"
    y "is she earthbending in her sleep?!"
    y "toph, wake up!"
    y "you're gonna bring the house down on us!"
    t "get back! stay back!"
    play sound "audio/earthquake.mp3"
    with sshake
    menu:
        "yell":
            y "damn it, toph!"
            y "I didn't go out in the fire, i'm not going out here!"
            t "i'll kill you!"
            y "(...that didn't work.)"
            y "(time for calming.)"
            y "hey... it's okay..."
            y "toph, it's all okay."
            y "You're dreaming."
        "speak calmly":

            y "hey... it's okay..."
            y "toph, it's all okay."
            y "You're dreaming."

    t "I... i don't want to!"
    t "I don't want to go!"
    y "toph..."
    y "you're safe. you're safe with me."
    y "I've got you."
    y "...fuck, i wish i could see."
    y "...."
    y "toph?"
    scene bg_toph_missionary
    show blackveil
    show tost tost00
    with Dissolve(2)
    t "...aang?"
    show ctc
    pause
    hide ctc
    y "hey, everything's all right."
    y "what's going on?"
    y "are you okay?"
    t "I... i don't know..."
    t "i've been..."
    show tost tost05
    t "I've been having all these terrible nightmares..."
    show ctc
    pause
    hide ctc
    y "it's okay, it happens to me too, sometimes."
    y "It's not real."
    t "I know, i'm not a kid!"
    t "they just... they seem... *sniff...*"
    t "they're... they're..."
    y "shhhh... it's okay, hey, it's alright."
    t "aang... could..."
    t "could you just hold me?"
    y "yeah, of course, come here."

    show tost tost01
    show expression "bk3/toph/comfort/playerbody.png"
    with Dissolve(1.5)
    "toph grips you tightly, throwing her whole body into you."
    y "(she must really be upset.)"
    y "(even more than she's letting on.)"
    show expression "bk3/toph/comfort/playerbody.png":
        alpha 1.0
        linear 4.0 alpha 0.4
    y "want to tell me what's really bothering you?"
    "toph just squeezes you tighter in response."
    show ctc
    pause
    hide ctc
    y "come on, i've only been here two nights and so far we're two for two with night terrors."
    t "I just..."

    t "i'm so afraid."
    y "you?"
    y "you're the bravest person i know..."
    t "i'm not... afraid of fights or anything like that."
    t "it's... it's a cage."
    t "I'm so afraid of a cage."
    y "oh..."
    t "i don't want to be sent back to my prison of a life!"
    t "the fragile beifong princess... with no life..."
    t "please don't make me go!"
    y "I'm... not sending you anywhere."
    y "I promise."
    y "besides, you'd kick my ass if i even tried. which i wouldn't."
    t "......"
    "You hold each other for a little while longer."
    t "..........."
    t "i don't... i don't know why i bother..."
    y "hmm?"
    t "with y..."
    t "......."
    t "...i'm never going to be loved..."
    y "what? are you crazy?"
    y "you're amazing."
    t "no, i'm not."
    t "I don't know what boys like... and i'm not pretty or busty like katara..."
    t "who would ever love a small, skinny, little blind girl?"
    y "toph...."
    y "i...."
    t "no, don't... i don't want to hear it."
    t "not from you, aang. not right now."
    t "don't say it if you don't mean it."
    y "i-"
    t "stop. just..."
    t "...just hold me a little.."
    y "well... that's... um... going to be a problem."
    t "what do you mea-"

    show tost tost02
    t "oh!"
    t "is that...?"
    y "that... is an erection."
    t "My sadness makes you... hard?"
    y "no, your... um... super sexy naked body does that."

    show tost tost03
    t "oh..."
    t "...really?"
    y "in fact, i have one around you... frequently."
    t "...you do?"
    y "yeah."
    y "i love spending time with you, which gets me to half-mast by itself..."
    y "...and i find you so sexy that i have to walk around with my hands in front of my pants."
    t "it is... sort of... pressing into me."
    t "It's... very... um... determined."
    t "and... large."
    t "it feels... bigger than i was expecting."
    show tost tost02
    t "oh!"
    y "sorry, that kind of talk... gets me going..."
    show tost tost03
    t "...."
    t "hahaha...."
    y "i really..."
    y "well, i really like you."
    y "you know?"
    y "i'm here, aren't i?"
    t "you are."
    t "You're here with me."
    t "....."
    t "you really like me?"
    y "I really do."
    y "and... you?"
    t "i really, really, really like you, too."
    y "that's... nice to hear."
    t "...."
    show tost tost01
    t "oh, aang...."
    "you and toph stay in this position for a little while longer."
    "her perky nipples press into your bare chest, as she rests directly on top of your painfully full erection."
    "you can feel the giving softness between her legs with the head of your cock."
    y "hey..."
    t "yeah...?"
    y "i don't want to ruin this moment, but..."
    menu:
        "wanna sleep together?":
            y "any chance you want to share this bed with me tonight?"
            y "get all snuggly and whatnot?"
        "let's each go to bed":
            y "we should probably get some rest..."
            y "...unless you want to lose the pants."

    show tost tost03
    t "I like that idea, but..."
    t "i think i'm okay, now."
    show tost tost04
    hide expression "bk3/toph/comfort/playerbody.png"
    with Dissolve(1.5)
    t "thanks, aang..."
    t "you're... you're someone i could..."
    t "....."
    t "well, you make me happy."
    y "........."
    y "hahahaha!"
    t "...what?"
    y "You're just so damn cute with your messy hair."
    show ctc
    pause
    hide ctc
    t "oh, be quiet."
    t "i'll see you in the morning?"
    y "I'm not going anywhere."
    t "okay."
    t "goodnight."
    y "goodnight."
    hide tost with dissolve
    y "......"
    show tost tost04 with dissolve
    t "...hey..."
    y "yeah?"
    t "thanks... for being here."
    t "I..."
    t "you make me feel... safe."
    t "thank you."
    y "you're welcome."
    t "okay."
    t "goodnight for real."
    hide tost with dissolve
    scene black with dissolve
    "you stay awake for a long time, eventually hearing toph fall asleep."
    "you close your eyes..."
    "you sleep well."
    jump love_bk3_next


label toph_comfort2:
    scene black with dissolve
    t "....."
    t "....aang?"
    y "*ssnnooorreee....*"
    t "....."
    t "aang?"
    y "wuzz... i'm ready... fart..."
    t "......."
    scene bg_toph_missionary
    show blackveil
    show tost tost00
    with Dissolve(2)
    t "are you awake, aang?"
    y "*yaaaawwn....*"
    y "i am now, i guess."
    y "what's up?"
    y "another nightmare?"
    show tost tost05
    t "*sniff* no..."
    t "I was just thinking..."
    t "and..."
    t "....are we friends?"
    y "are we.... of course we're friends."
    y "actually i think we're a little more than that."
    show tost tost01
    show expression "bk3/toph/comfort/playerbody.png"
    with vshake
    y "oomph!"
    "toph slams into you with a full-bodied hug."
    show expression "bk3/toph/comfort/playerbody.png":
        alpha 1.0
        linear 4.0 alpha 0.4
    y "Okay, what is it?"
    y "something's up."
    t "i just... do you ever want more?"
    menu:
        "sometimes":
            y "it's crossed my mind..."
            y "...a few times."
            y "i... like you."
            y "a lot."
            y "i think we get along really well."
            y "we compliment each other."
            y "and you're beautiful and fun..."
            y "...and honestly fucking scary sometimes."
        "never":

            y "i'm pretty happy with how things are."
            y "my life's great... mostly."

    t "oh..."
    t "....."
    t "when you go... back to your place..."
    t "do you think you'll stay over sometimes?"
    y "sure, i can do that."

    show tost tost02
    t "really!?"

    show tost tost03
    t "that would be amazing!"

    y "i'd love to stay over, if you'll let me."
    t "i totally will!"
    y "i'm not leaving because i don't like you."
    y "You know i like you, right?"

    show tost tost04
    hide expression "bk3/toph/comfort/playerbody.png"
    with Dissolve(1.5)
    "toph gently lets you go..."
    "...and steps back."
    t "i do know that...."
    t "....now."
    t "i get... insecure sometimes."
    y "we all do."
    t "sorry to wake you."
    t "I'll... see you in the morning."
    t "......"
    play sound "audio/kiss.mp3"
    with pflash
    "toph gently presses her lips to yours."
    "it's light and tentative, like others she's given, but... it's slower."
    "a little longer."
    "a little more... wanting."
    "it's barely more than a peck, but it feels... a little different somehow."
    "she pulls back."
    t "goodnight..."
    t "...babe."
    hide tost with dissolve
    y "....."
    y "oh."
    y "wow."
    y "...that's new."
    scene black with dissolve
    "you fall asleep with a little bit lighter heart."
    jump love_bk3_next

label suki_dl_hypno:
    show tosi tosi03:
    show toeg toeg01:
        xzoom -1
    with dissolve
    suki "are you seriously trying to intimidate me?"
    dl "it doesn't have to be intimidation."
    dl "it could be... appreciation."
    dl "...for protection."
    suki "screw your \"protection\"."
    suki "get out of my tavern."
    dl "you really want it to play out like this?"
    dl "it will be much worse for you."
    suki "i'm not showing you my {i}tits{/i}, you asshole."
    suki "threaten all you like."
    suki "i don't care if long feng has a vendetta."
    suki "you can all go-"
    dl "{i}the earth king has invited you to lake laogai."
    show tosi tosi01
    show tosi_hypno_eyes
    with Dissolve(1)
    suki "........."
    suki "i am honored to accept his invitation."
    dl "very good."
    dl "now..."
    dl "open your shirt."
    show tosi tosi04
    with Dissolve(1)
    show ctc
    pause
    hide ctc
    dl "good."
    dl "that's a good girl."
    suki "...."
    dl "say it."
    suki "I'm a... good girl..."
    dl "yes, you are..."
    dl "you're so happy to please long feng."
    suki "i'm... happy to please... long feng..."
    dl "but first, you're going to please me... with a nice view."
    dl "remove your underwear, girl."
    menu:
        "wait":
            $ suki_dl_tits = True

            show tosi tosi05
            with dissolve
            show ctc
            pause
            hide ctc
            dl "nice."
            dl "now..."
        "interrupt":

            pass

    y "all right, that's enough!"
    dl "wh-"
    hide toeg
    show guardb_body_1:
        xzoom -1
    with dissolve
    if love_june_hypno ==0:
        dl "what? who are you?"
        y "I'm the avatar."
        dl "...."
        dl "oh."
        y "yeah, \"oh\"."

    if love_june_hypno >=1:
        dl "what? who-"
        dl "oh, fuck."
        dl "not you again."
        y "yeah, me again."
        dl "well... can you leave?"
        y "no."

    y "now get out of here before i use mother nature to peg you in the ass."
    dl "...."
    dl "you haven't seen the last of me, avatar."
    y "yeah, yeah."
    y "scram."
    hide guardb_body_1 with dissolve
    y "dick."
    y "suki, you okay?"
    suki "......"
    y "come on, wake up already."
    suki "......"
    y "um."
    y "wait here."
    y "i'll... go get katara."
    jump love_bk3_village_background

label jin_anti_hypno1:
    $ bk3_day = False
    scene black
    scene hypno_room2
    with dissolve
    show tojn tojn20 with dissolve
    jin "um... aang?"
    y "hey, welcome."
    y "come on in."
    jin "i already did."
    y "...right."
    show tojn tojn23 with dissolve
    jin "so... what are we doing?"
    y "well, i'm setting up a bunch of heavy, probably seizure-inducing equipment, giving myself a hernia, and you're sitting in a big fucking chair."
    y "...it's not comfortable."
    jin "okay..."
    scene black
    scene hypno_room1
    show tohy jin01
    with fade
    jin "alright, i'm in."
    y "what?"
    y "oh, no, you need to be naked."
    jin "....."
    jin "well, you sure know how to show a girl a good time."
    scene black
    scene hypno_room2
    show tojn tojn20
    with fade
    jin "here goes nothing..."
    hide tojn with dissolve
    show tojn tojn22
    with dissolve
    show ctc
    pause
    hide ctc
    y "very nice."
    y "now get in the damn chair."
    jin "ooh, you're grumpy."
    jin "heehe..."
    scene black with dissolve
    scene hypno_room1
    show expression "bk3/hypno/jin/body2.png"
    with dissolve
    jin "i'm in."
    show ctc
    pause
    hide ctc
    y "and i'm set up over here."
    show hypno_rail with Dissolve(2.0)
    y "A lamp will move along this rail, please follow it with your eyes while listening to my voice."
    y "Okay, here we go."

    show expression "bk3/hypno/jin/sclera.png"
    show tohy_jin_eyewest
    show tohy_jin_eyeeast
    show expression "bk3/hypno/jin/eyes_mask.png"
    show hypno_ball:
        alpha 1.0
        xpos 800 ypos 300
        linear 2.0 xpos -100 ypos 260
        alpha 0.0
        pause 2.0
        repeat
    show tohy_jin_blink

    y "come on...."
    show hypno_ball:
        alpha 1.0
        xpos 800 ypos 300
        linear 1.0 xpos -100 ypos 260
        alpha 0.0
        pause 1.0
        repeat
    "as you wait, the lamp speeds up to incredible speeds."
    y "I hope this works..."

    y "Focus on the light and listen to my voice."

    y "you are strong."
    y "you are determined."
    y "you are your own."

    jin "i am strong... determined... my own..."

    hide tohy_jin_eyewest
    hide tohy_jin_eyeeast

    hide expression "bk3/hypno/jin/sclera.png"
    hide expression "bk3/hypno/jin/eyes_mask.png"
    show tohy jin04
    hide hypno_ball
    hide hypno_glowspot
    hide hypno_rail
    with Dissolve(2.0)


    y "I can put these away."




    y "alright, i don't see any need for a slow breakdown here."
    y "I think we can just bust this thing in one go."
    y "you ready?"
    jin "My name is jin."
    y "....right."
    y "well done."
    y "you're clearly ready."
    y "here we go."

    show black with dissolve
    "you use the equipment following ajala's instructions."
    hide black with dissolve
    y "you no longer have any compulsions over you."
    y "you will no longer answer to any hypnotic phrase."
    y "Your mind is now guarded against hypnosis."
    jin "i am... my own..."
    y "great."
    y "when i snap my fingers, you will wake up."
    y "3... 2... 1..."
    play sound "audio/fingersnap.mp3"
    hide tohy jin04
    show expression "bk3/hypno/jin/body2.png"
    with dissolve
    jin "wha... what just happened?"
    y "how do you feel?"
    jin "I feel..."
    jin "i... feel..."
    y "yes?"
    jin "....."
    jin "...hungry."
    y "hungry?"
    jin "yeah."
    jin "starving."
    y "that's... a new one."
    y "you sure you don't want a nice hot piping bowl of weiners?"
    jin "are you offering?"
    y "well-"
    jin "shame on you!"
    jin "I'm not that easy."
    y "*sigh...*"
    y "I don't know if this wasn't actually a really dumb idea..."
    jin "come on, let's get some grub?"
    jin "it's the least you can do for making me sit in this cold ass chair naked."
    y "that's... but it was because... fine."
    jin "yay!"
    scene black with dissolve
    scene hypno_room1
    show tojn tojn20
    with dissolve
    jin "i'll meet you at the tavern."
    y "sure."
    hide tojn with dissolve
    y "at least she won't have sex with strangers, so that's a comfort."
    y "...even if i don't get any."
    y "......."
    y "damn it."
    y "alright, i'll go meet her at the tavern."
    $ jin_anti_hypno_start = 3
    jump love_bk3_village_background

label jd_anti_hypno1:
    $ bk3_day = False
    scene black
    scene hypno_room2
    with dissolve
    if love_jd_hypno ==15:
        hide toji
        show toji toji14
    else:
        show toji toji01
    with dissolve
    if love_jd_hypno ==1:
        jd "avatar?"
        y "oh, you recognized my house."
        y "i wonder how?"
        jd "i am... still very sorry about that..."
        y "no, i'm sorry."
        y "i'm clearly still very salty about it."
        y "well, let's get started."
        jd "yes, so... what exactly are we doing?"
        y "you're getting into a chair, and i'm undoing a bunch of hypnosis."
        jd "by... going through hypnosis?"
        y "yeah..."
        y "i think of it as a \"hair of the dog\" kind of a thing."
        jd "i suppose..."
    if love_jd_hypno ==3:
        jd "i'm here again, avatar."
        y "great."
        y "just as before, please sit in the chair."
        jd "okay..."
    if love_jd_hypno ==5:
        jd "i'll go ahead and sit, then."
        y "does that really need a response?"
    if love_jd_hypno ==15:
        y "go ahead and sit down, please."
    scene black
    scene hypno_room1
    with Dissolve(1)
    if love_jd_hypno ==15:
        y "i need you to undress for this, joo dee."
        jd "you... you do?"
        y "yes."
        jd "well... if... if it's important..."
        hide toji with dissolve
        show jd_nude with dissolve
        y "okay, now get up in the machine."
        jd "alright..."
        hide jd_nude with dissolve
        show tohy joodee03
        show expression "bk3/hypno/joodee/eyes_norm.png"
        with Dissolve(2)
    else:
        show tohy joodee01 with Dissolve(2.0)
    if love_jd_hypno ==1:
        jd "i'm seated, avatar..."
        jd "Is this... correct?"
        show ctc
        pause
        hide ctc
        y "haven't you done this a bunch already?"
        jd "i don't... remember."
    if love_jd_hypno ==3:
        jd "i'm seated."
        y "good."
    if love_jd_hypno ==5:
        jd "i'm in."
        y "great."
    if love_jd_hypno ==15:
        jd "i'm seated..."
        jd "will this be similar to other times?"
        y "at first."
    y "Make yourself comfortable while I set up the equipment."

    show hypno_rail with Dissolve(2.0)
    if love_jd_hypno ==1:
        y "A lamp will move along this rail, please follow it with your eyes while listening to my voice."

    y "Okay, here we go."

    show expression "bk3/hypno/joodee/sclera.png"
    show tohy_joodee_eyewest
    show tohy_joodee_eyeeast
    show expression "bk3/hypno/joodee/eyes_mask.png"
    show hypno_ball:
        alpha 1.0
        xpos 800 ypos 300
        linear 2.0 xpos -100 ypos 260
        alpha 0.0
        pause 2.0
        repeat

    if love_jd_hypno ==15:
        y "come on...."
        show hypno_ball:
            alpha 1.0
            xpos 800 ypos 300
            linear 1.0 xpos -100 ypos 260
            alpha 0.0
            pause 1.0
            repeat
        "as you wait, the lamp speeds up to incredible speeds."
        y "I hope this works..."

    y "Focus on the light and listen to my voice."
    show ctc
    pause
    hide ctc
    if love_jd_hypno ==15:
        y "you are strong."
        y "you are determined."
        y "you are your own."
    else:
        y "you are safe."
        y "you are accepting."
        y "you are willing."
    hide tohy_joodee_eyewest
    hide tohy_joodee_eyeeast

    hide expression "bk3/hypno/joodee/sclera.png"
    hide expression "bk3/hypno/joodee/eyes_mask.png"
    if love_jd_hypno ==15:
        hide expression "bk3/hypno/joodee/eyes_norm.png"
    else:
        show tohy joodee02
    with Dissolve(2.0)

    y "Okay, I won't need these anymore."

    hide hypno_ball
    hide hypno_glowspot
    hide hypno_rail with Dissolve(2.0)

    if love_jd_hypno ==1:
        y "this might be a good time for a personal question..."
        y "if i was a dick."

        menu:
            "don't invade her privacy":
                pass
            "How often do you masturbate?":
                jd "Almost never."
                y "really? that sucks."
                y "you're missing out."
                y "....or i have a problem."
            "What is your biggest sexual fantasy":
                jd "To be strangled while getting my pussy pounded as if it's a piece of meat."
                y "Wow.. that's pretty hardcore, Joo dee."
                y "I didn't expect that of you."
                y "and i approve."

    y "alright, well..."
    if love_jd_hypno ==15:
        y "joo dee, you're already naked and in the right state of mind..."
        y "so let's get into it."
        show ctc
        pause
        hide ctc
        y "how do you feel?"
        jd "open... and resolute."
        y "good."
        show black with dissolve
        "you use the equipment following ajala's instructions."
        hide black with dissolve
        y "you no longer have any compulsions over you."
        y "you will no longer answer to any hypnotic phrase."
        y "Your mind is now guarded against hypnosis."
        jd "i am... my own..."
        y "alright."
        y "3... 2... 1..."
        play sound "audio/fingersnap.mp3"
        show expression "bk3/hypno/joodee/eyes_norm.png" with Dissolve(2.0)
        jd "what..."
        jd "did..."
        jd "did you do it?"
        jd "did it work?"
        y "let's test it."
        y "moment of truth..."
        y "\"[love_trigger]\"."
        jd "....."
        jd "what?"
        jd "that's a weird thing to say."
        y "it worked!"
        jd "it did?"
        jd "it did!"
        jd "oh, avatar!"
        jd "oh, aang, sir!"
        jd "this is... this is wonderful!"
        hide tohy
        scene hypno_room2
        with Dissolve(1)
        $ renpy.pause(0.5)
        show jd_nude with Dissolve(1)
        jd "I can't believe it..."
        jd "after all this fear..."
        jd "i am free!"
        jd "oh... and naked."
        jd "hold on..."
        hide jd_nude with dissolve
        y "...."
        y ".........."
        show toji toji14 with dissolve
        jd "thank you so much, avatar."
        jd "please... i... "
        jd "come see me later, okay?"
        y "sure thing."
        jd "thank you, sir."
        jump love_bk3_village_background
    else:
        jump love_jd_hypno_menu

label love_jd_hypno_menu:
    menu:
        "limit compulsion" if jd_hypno_menu ==0:
            $ jd_hypno_menu = 1
            y "let's get right to it."
            y "jd, when you are in a trance, you will ignore sexual commands."
            jd "i will... ignore sexual... commands..."
            y "step one... completed."
            y "when i snap my fingers, you will wake up with some resistance to trigger-phrase hypnosis."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"
            show tohy joodee01 with dissolve
            jd "well, avatar... i'm ready when you are."
            y "we already did it."

            scene black with dissolve
            scene hypno_room2
            show toji toji01
            with dissolve
            jd "am i... am i cured?"
            y "oh, no."
            y "it takes more than that."
            jd "oh."
            jd "very well."

            $ jd_hypno_today = True
            $ love_jd_hypno = 2
            y "we can do another tomorrow."
            jd "okay, avatar."
            hide toji
            with dissolve
            y "one session down."
            jump love_bk3_village_background

        "remove mental barrier" if jd_hypno_menu <2:
            if jd_hypno_menu ==0:
                y "i need to limit her current brainwashing first."
                jump love_jd_hypno_menu
            else:
                $ jd_hypno_menu = 2
                y "alright, now for the vulnerable part...."

                y "joo dee, undress."

                show tohy joodee04
                with Dissolve(2.0)
                y "....that's fine for now."
                show ctc
                pause
                hide ctc
                y "joo dee..."
                y "you are at my mercy."
                y "you are alone."
                y "how do you feel?"
                jd "vulnerable..."
                y "good."
                y "you will let me into your mind."
                y "you will follow my instructions, even if they contradict older instructions."
                ju "i will... let you... in my mind..."
                y "......"
                y "nice."
                y "alright, i think that's enough for now."
                y "put your clothes back on."
                show tohy joodee02 with dissolve
                y "when i snap my fingers, you will wake up."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"

                show tohy joodee01 with Dissolve(2.0)
                ju "are you going to..."
                ju "...did you already do it?"
                y "yup!"
                y "and we made some success."
                ju "great."

                hide tohy
                scene hypno_room2
                with Dissolve(1)
                $ renpy.pause(0.5)
                show toji toji01 with Dissolve(1)
                jd "i suppose i still need to come back?"
                y "yeah, at least once."
                y "probably more in the future though."
                jd "very well."
                $ love_jd_hypno = 4
                $ jd_hypno_today = True
                jump love_bk3_village_background

        "remove compulsion" if jd_hypno_menu <3:
            if jd_hypno_menu ==0:
                y "i need to limit her current brainwashing first."
                jump love_jd_hypno_menu
            if jd_hypno_menu ==1:
                y "i need to remove her mental barrier before i can do this."
                jump love_jd_hypno_menu
            else:
                $ jd_hypno_menu = 3
                y "alright joo dee, we need to get you into the right state of mind."
                y "remove your clothes."

                show tohy joodee04
                with Dissolve(2.0)
                show ctc
                pause
                hide ctc
                y "all the way, this time."
                jd "......."
                show tohy joodee03
                with Dissolve(2.0)
                show ctc
                pause
                hide ctc
                y "how do you feel?"
                jd "open..."
                y "good."
                y "now, let's change that trigger phrase."
                y "your new hypnosis-inducing phrase will be..."
                y "\"[love_trigger]\"."

                jd "I will... only answer... to..."
                jd "\"[love_trigger]\"."
                y "great!"
                y "put your clothes back on."
                show tohy joodee02 with Dissolve(1)
                y "alright."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"
                show tohy joodee01 with Dissolve(2.0)
                jd "when will...."
                jd "wait, did you already do it?"
                y "i did."
                y "and your trigger phrase has been changed."
                jd "that's wonderful!"


                hide tohy
                scene hypno_room2
                with Dissolve(1)
                $ renpy.pause(0.5)
                show toji toji01 with Dissolve(1)
                jd "am i safe now?"
                jd "is my mind my own?"
                y "uh... mostly?"
                y "we'll have to keep working on freeing you, but for the time being you're mostly safe."
                y "no one will take advantage of you."
                jd "i appreciate your help, avatar!"
                y "you're welcome."
                jd "come visit me sometime."
                $ love_jd_hypno = 6
                $ jd_hypno_today = True
                jump love_bk3_village_background

label june_anti_hypno1:
    $ bk3_day = False
    $ tohy_junedress_on = True
    scene black
    scene hypno_room2
    with dissolve
    show toju toju10
    with dissolve
    if love_june_hypno ==6:
        ju "avatar?"
        y "ah, good, you're here."
        ju "so... you're going to remove this... brainwashing thing, right?"
        y "we're definitely gonna try."
        show toju_blink with dissolve
        ju "*sigh...*"
        ju "you're not filling me with confidence."
        hide toju_blink
        show toju toju12
        with dissolve
        ju "let's get this over with."
    if love_june_hypno ==8:
        ju "i'm here again."
        y "great!"
        y "settle in."
    if love_june_hypno ==10:
        ju "will this be the last session?"
        y "i don't think so..."
        y "but it should do a lot."
    scene black with dissolve
    scene hypno_room1
    with dissolve

    show tohy june01 with Dissolve(2.0)
    if love_june_hypno ==6:
        ju "i just sit here?"
        show ctc
        pause
        hide ctc
        y "yup."
    if love_june_hypno ==8:
        ju "do you want me to sit here again?"
        show ctc
        pause
        hide ctc
        y "yup, same place as last time."
    if love_june_hypno ==10:
        ju "well, i'm seated."
        ju "let's get this started."
    y "Make yourself comfortable while I set up the equipment."
    if love_june_hypno ==6:
        y "......."
        y "i think this goes here?"
        ju "......."
    if love_june_hypno ==8:
        y "i just have to put this thing in place again...."
    if love_june_hypno ==10:
        y "putting it in place...."
    show hypno_rail with Dissolve(2.0)
    if love_june_hypno ==6:
        y "okay, yeah, that fits."
    if love_june_hypno ==8:
        y "aaaand there we go."
    if love_june_hypno ==10:
        y "aaaand there we go."
    y "alright, a lamp will move along this rail."
    y "please follow it with your eyes while listening to my voice."


    show expression "bk3/hypno/june/sclera.png"
    show tohy_june_eyeeast
    show expression "bk3/hypno/june/eyes_mask.png"
    show hypno_ball:
        alpha 1.0
        xpos 800 ypos 300
        linear 2.0 xpos -100 ypos 260
        alpha 0.0
        pause 2.0
        repeat

    show tohy_june_blink

    show ctc
    pause
    hide ctc
    y "you are safe."
    y "you are accepting."
    y "you are willing."

    hide tohy_june_eyeeast

    hide expression "bk3/hypno/june/sclera.png"
    hide expression "bk3/hypno/june/eyes_mask.png"
    show tohy june02
    with Dissolve(2.0)



    y "Okay, I won't need these anymore."

    hide hypno_ball
    hide hypno_rail with Dissolve(2.0)
    if love_june_hypno ==6:
        y "oooh, this might be a good time to ask a personal question, but..."
        y "maybe i shouldn't..."

        menu:
            "don't invade her privacy":
                $ june_sympathy +=1
                pass
            "how often do you masturbate?":
                ju "A few times a week."
                y "that's... really normal."
                y "i don't know what i was expecting."
            "What's your biggest sexual fantasy?":
                ju "To be in charge."
                y "....huh."
                y "i don't know what i was expecting."

    y "alright, well..."
    jump love_june_hypno_menu

label love_june_hypno_menu:
    menu:
        "limit compulsion" if june_hypno_menu ==0:
            $ june_hypno_menu = 1
            y "june, you will ignore commands given to you while you're in a trance."
            ju "....."
            ju "must... follow... orders..."
            y "right, okay."
            y "then...."
            y "when you are in a trance, you will ignore sexual commands."
            ju "i will... ignore sexual... commands..."
            y "progress!"
            ju "......"
            y "alright, i think that's enough for now."
            y "when i snap my fingers, you will wake up with some resistance to trigger-phrase hypnosis."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"
            show tohy june01 with dissolve
            ju "so... i guess i'm ready to begin when you are."
            y "we already did it."
            ju "oh?"
            ju "and?"
            scene black with dissolve
            scene hypno_room2
            show toju toju09
            with dissolve
            ju "did it work?"
            y "it's a... piecemeal process."
            ju "so that's a \"no\", then?"
            y "i was able to limit your brainwashing to non-sexual requests."
            y "that way soldiers can't make you strip again."
            y "but it'll take more sessions."
            show toju_blink with dissolve
            ju "....at least it's something."

            $ june_hypno_today = True
            $ love_june_hypno = 7
            y "we can do another tomorrow."
            ju "very well."
            hide toju
            hide toju_blink
            with dissolve
            y "one session down."
            jump love_bk3_village_background

        "remove mental barrier" if june_hypno_menu <2:
            if june_hypno_menu ==0:
                y "i need to limit her current brainwashing first."
                jump love_june_hypno_menu
            else:
                $ june_hypno_menu = 2
                y "alright, now for the risky part...."
                y "....where i make her vulnerable to suggestion."
                y "june."
                y "stand up."

                hide tohy
                hide expression "ebackgrounds/hypno_room1.jpg"
                show expression "ebackgrounds/hypno_room2.jpg"
                with Dissolve(2.0)

                show toju toju01
                show toju_hypno_eyes
                with dissolve
                y "june..."
                y "remove your clothes."

                show toju toju20 with Dissolve(1)
                show ctc
                pause
                hide ctc

                y "all right, get back in the chair."

                hide toju toju20
                hide toju_hypno_eyes
                with Dissolve(1)

                hide expression "ebackgrounds/hypno_room2.jpg"

                show expression "ebackgrounds/hypno_room1.jpg"
                show tohy june03
                with Dissolve(2.0)
                y "....nice."
                show ctc
                pause
                hide ctc
                y "let's try this again..."
                y "you are at my mercy."
                y "you are alone."
                y "how do you feel?"
                ju "vul... vulnerable..."
                y "june."
                y "you will let me into your mind."
                y "you will follow my instructions, even if they contradict older instructions."
                ju "i will... let you... in my mind..."
                y "......"
                y "fuck yeah!"
                y "alright, i think that's enough for now."
                y "when i snap my fingers, you will wake up."
                y "3... 2... 1..."
                y "wait."
                y "um."
                y "i don't want june pissed when she regains consciousness."
                y "june, put your clothes back on."
                show tohy june02 with Dissolve(1)
                y "alright."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"

                show tohy june01 with Dissolve(2.0)
                ju "are you going to..."
                ju "...did you already do it?"
                y "yup!"
                y "and we made some success."
                ju "great."

                hide tohy
                scene hypno_room2
                with Dissolve(1)
                $ renpy.pause(0.5)
                show toju toju10 with Dissolve(1)
                ju "so...?"
                ju "am i free?"
                y "not quite yet."
                y "I still have to actually stop you from being triggered, but i should have access to your mind now."
                ju "fine."
                ju "good."
                y "....you could be a little happier about it."
                ju "....."
                show toju toju12 with dissolve
                ju "ohhhh thaaank you great ruler!"
                ju "what would this poor weak woman do without you?"
                y "...jokes on you, i like that."
                y "also, that's uncalled for."
                show toju toju10
                show toju_blink
                with dissolve
                ju "you're probably right."
                ju "i'll go then."
                hide toju
                hide toju_blink
                with dissolve
                y "wow."
                y "she is stiff."
                $ love_june_hypno = 9
                $ june_hypno_today = True
                jump love_bk3_village_background

        "remove compulsion" if june_hypno_menu <3:
            if june_hypno_menu ==0:
                y "i need to limit her current brainwashing first."
                jump love_june_hypno_menu
            if june_hypno_menu ==1:
                y "i need to remove her mental barrier before i can do this."
                jump love_june_hypno_menu
            else:
                $ june_hypno_menu = 3
                y "alright june, we need to get you into the right state of mind."
                y "stand up."

                hide tohy
                hide expression "ebackgrounds/hypno_room1.jpg"
                show expression "ebackgrounds/hypno_room2.jpg"
                with Dissolve(2.0)

                show toju toju01
                show toju_hypno_eyes
                with dissolve
                y "june..."
                y "remove your clothes."

                show toju toju20 with Dissolve(1)
                show ctc
                pause
                hide ctc

                y "all right, get back in the chair."

                hide toju toju20
                hide toju_hypno_eyes
                with Dissolve(1)

                hide expression "ebackgrounds/hypno_room2.jpg"

                show expression "ebackgrounds/hypno_room1.jpg"
                show tohy june03
                with Dissolve(2.0)
                y "....nice."
                show ctc
                pause
                hide ctc

                y "how do you feel?"
                ju "open..."
                y "good."
                y "now, let's change that trigger phrase."
                y "your new hypnosis-inducing phrase will be..."
                y "\"[love_trigger]\"."

                ju "I will... only answer... to..."
                ju "\"[love_trigger]\"."
                y "great!"
                y "Oh, and..."
                y "be nicer to the avatar."
                y "he's trying his best."
                ju "i will... be nicer... to the avatar."
                y "yeah."
                y "......"
                y "(that probably... isn't immoral.)"
                y "(right?)"
                y "......"
                y "anyway, i think this is progress."
                y "put your clothes back on."
                show tohy june02 with Dissolve(1)
                y "alright."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"
                show tohy june01 with Dissolve(2.0)
                ju "this chair is uncomforta...."
                ju "wait, did you already do it?"
                y "i did."
                y "and your trigger phrase has been changed."
                ju "great."
                ju "thank you."


                hide tohy
                scene hypno_room2
                with Dissolve(1)
                $ renpy.pause(0.5)
                show toju toju10 with Dissolve(1)
                ju "so what's next?"
                y "we'll have to keep working on freeing you, but for the time being you're mostly safe."
                ju "that's... nice."
                ju "i appreciate your help, avatar."
                y "you're welcome!"
                show toju_blink
                with dissolve
                ju "I have something... you might be able to help with."
                y "oh?"
                ju "yeah, but... it's not ready yet."
                ju "i'll come find you when it's time."
                hide toju_blink with dissolve
                ju "...if you'd agree to help me."
                y "sure."
                ju "great."
                ju "see you around... avatar."

                hide toju
                hide toju_blink
                with dissolve
                y "she got a little nicer."
                y "that's great."
                y "....i'm still a better person than long feng, right?"
                y "right?"
                y "....."
                y "i'm sure it's fine."
                $ love_june_hypno = 11
                $ june_hypno_today = True
                jump love_bk3_village_background

label suki_anti_hypno1:
    $ bk3_day = False
    show tosi tosi01
    with dissolve
    suki "okay, let's do this."
    if love_suki_hypno ==3:
        suki "do you know what you're doing?"
        menu:
            "of course":
                y "sure i do."
                y "I know all about undoing earth kingdom underground brainwashing."
                y "it's a standard skill."
                suki "i feel like you're being insincere."
                y "no, i totally know what i'm doing, don't worry."
                suki "if you say so..."
                y "I do."
            "um... no":

                y "not... really."
                suki "....oh."
                show tosi_blink with dissolve
                suki "well..."
                hide tosi_blink with dissolve
                suki "we don't really have another option, do we?"
                suki "i guess just try your best."
                y "yeah, of course."

        y "now take off your clothes."
        show tosi tosi03 with dissolve
        suki "what?!"
        y "kidding!"
        y "i'm kidding."
        y "but i'm gonna need you to sit in that chair."
        show tosi tosi01 with dissolve
        suki "okay..."
    if love_suki_hypno ==5:
        y "you seem eager."
        show tosi tosi03 with dissolve
        suki "i want to sleep again."
        suki "i want to not be afraid of everyone that comes into the tavern."
        suki "so let's do this."
        y "take a deep breath."
        y "we're not doing anything while you're this worked up."
        suki "........"
        show tosi_blink with dissolve
        suki "*deep breath in*"
        suki "....."
        show tosi tosi01 with dissolve
        suki "*deep breath out*"
        y "there you go."
        y "we'll beat this thing."
        hide tosi_blink with dissolve
        y "You ready?"
        suki "i'm ready."
        y "great."
        y "get in the chair."

    if love_suki_hypno ==9:
        suki "do you think you can... get my mental block down?"
        y "i honestly don't know."
        y "but we should try."
        suki "agreed."
        suki "i'll get in the chair."

    if love_suki_hypno ==12:
        y "i'll try to remove your compulsion completely, but..."
        suki "no guarantees?"
        y "unfortunately."
        suki "i trust you."

    scene black with Dissolve(1)
    $ renpy.pause(0.5)
    scene hypno_room1
    show tohy suki01
    with Dissolve(2)
    y "alright, get comfortable while I set up the equipment."
    show hypno_rail with Dissolve(2.0)
    suki "Umm..."
    suki "i'm a little nervous."
    if love_suki_hypno ==3:
        y "don't worry, i'm just trying to make you yourself again."
        suki "i trust you, aang."
        suki "thank you."
        y "don't thank me yet."
        y "okay, i think this lamp is going to move along the rail."
        y "follow it with your eyes while listening to my voice."
        suki "i'm ready."
        y "Okay, here we go."
    if love_suki_hypno ==5:
        y "still?"
        suki "it's not like this is a normal thing."
        y "it's alright, i'll take care of you."
        y "like before, this lamp is going to move along the rail."
        y "follow it with your eyes while listening to my voice."
        suki "do it."
        y "Okay, here we go."
    if love_suki_hypno ==9:
        y "about what?"
        suki "that it won't work..."
        suki "and i'll be... broken and... wrong..."
        suki "forever."
        y "I won't let it happen."
        y "now, look here."
    if love_suki_hypno ==12:
        suki "if you can't remove it, i'm stuck like this."
        suki "but what if you do remove it... and it does more damage?"
        y "i don't know, and that's the truth."
        y "but i don't think you have anything to fear from removing an artificial hold on your brain."
        suki "i guess... you're right."
        y "good."
        y "now look here."

    show expression "bk3/hypno/suki/sclera.png"
    show tohy_suki_eyewest
    show tohy_suki_eyeeast
    show expression "bk3/hypno/suki/eyes_mask.png"
    show hypno_ball:
        alpha 1.0
        xpos 800 ypos 300
        linear 2.0 xpos -100 ypos 260
        alpha 0.0
        pause 2.0
        repeat
    show tohy_suki_blink
    show ctc
    pause
    hide ctc
    y "Focus on the light and listen to my voice."
    y "you are safe."
    y "You are relaxed."
    y "you are accepting."
    y "you are willing."

    hide tohy_suki_eyewest
    hide tohy_suki_eyeeast

    hide expression "bk3/hypno/suki/sclera.png"
    hide expression "bk3/hypno/suki/eyes_mask.png"
    show tohy suki02
    with Dissolve(2.0)


    y "Okay, I'll just put these aside...."

    hide hypno_ball
    hide hypno_glowspot
    hide hypno_rail with Dissolve(2.0)


    y "suki, can you hear me?"
    suki "...yes..."
    if love_suki_hypno ==3:
        y "alright, so..."
        y "um..."
        menu:
            "stop being brainwashed!":
                y "stop being brainwashed!"
                suki "...."
                y "are you still compelled to answer to a trigger phrase?"
                suki "yes..."
                y "damn it."
            "pants off!":
                y "lose the clothes!"
                suki "n... no..."
                y "it was worth a try."
                y "now... stop being brainwashed!"
                suki "......"
                y "it didn't work, did it?"
                suki "no...."
                y "damn it."

        y "well... maybe I can change what she's willing to do while hypnotized."
        y "at least a bit."
        y "then i'll work on removing it entirely."
        y "can't have her going around jacking off any of those damn dai lee."
        jump love_suki_hypno_menu

    if love_suki_hypno ==5:
        y "alright, let's see if i can make her more willing to accept future change."
        jump love_suki_hypno_menu
    if love_suki_hypno ==9:
        y "hopefully we can break your mental barrier today..."
        y "somehow."
    if love_suki_hypno ==12:
        y "let's see if we can actually beat your compulsion today."

label love_suki_hypno_menu:
    menu:
        "limit compulsion" if suki_hypno_menu ==0:
            $ suki_hypno_menu = 1
            y "suki, when you are in a trance, you will ignore commands."
            suki "....."
            y "will you ignore commands?"
            suki "must... follow... orders..."
            y "damn."
            y "hmm...."
            y "okay...."
            y "when you are in a trance, you will ignore sexual commands."
            suki "i will... ignore sexual... commands..."
            y "yes!"
            y "woo!"
            suki "......"
            y "alright, i think that's progress enough for this one."
            y "don't want to overdo it."
            y "when i snap my fingers, you will wake up with some resistance to trigger-phrase hypnosis."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"
            show tohy suki01 with Dissolve(2.0)
            suki "wh..."
            suki "....are we gonna start or what?"
            y "we already did it."
            suki "we did?"
            suki "great!"
            hide tohy with Dissolve(1)
            $ renpy.pause(0.5)
            show tosi tosi01 with Dissolve(1)
            suki "so, did it work?"
            y "well... kinda."
            show tosi tosi03 with dissolve
            suki "i don't like the sound of that."
            y "i wasn't able to remove your compulsion entirely yet, but i was able to limit it to non-sexual favors."

            show tosi tosi01
            show tosi_blink
            with dissolve
            suki "....."
            suki "better than nothing, i guess."
            y "don't worry, we'll do more sessions."
            y "we'll fix you eventually."
            suki "...right."
            $ suki_hypno_today = True
            $ love_suki_hypno = 4
            y "we can do another tomorrow."
            suki "fine. sure."
            hide tosi
            hide tosi_blink
            with dissolve
            y "she seems bummed."
            y "i hope another session will help."
            jump love_bk3_village_background

        "remove mental barrier" if suki_hypno_menu <2:
            if suki_hypno_menu ==0:
                y "i need to limit her current brainwashing first."
                jump love_suki_hypno_menu
            else:
                $ suki_hypno_menu = 2
                y "suki, let go of your hesitancy."
                y "release your defenses."
                suki "....."
                y "accept that you will be changed."
                y "do you understand?"
                suki "no...."
                y "*sigh.*"
                y "you must let me give you new instructions for when you hear your brainwash trigger phrase."
                suki "no...."
                y "....damn it."
                y "...."
                y "alright, fine."
                y "i have to think about this."
                y "when i snap my fingers, you will wake up."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"
                show tohy suki01 with Dissolve(2.0)
                suki "wh..."
                suki "....did we already..."
                y "yes, we already had your session."
                hide tohy with Dissolve(1)
                $ renpy.pause(0.5)
                show tosi tosi01 with Dissolve(1)
                suki "and...?"
                y "didn't work."
                y "I can't get you vulnerable enough to accept contradictory instructions to your brainwashing."
                suki "oh."
                show tosi_blink
                with dissolve
                suki "....."
                suki "well, we'll just keep trying, i guess."
                y "i'll figure it out, i promise."
                suki "...right."
                $ suki_hypno_today = True
                $ love_suki_hypno = 6
                y "we can do another tomorrow."
                suki "fine. sure."
                hide tosi
                hide tosi_blink
                with dissolve
                y "i hope i can figure this out."
                jump love_bk3_village_background
        "remove mental barrier" if suki_hypno_menu ==2:
            $ suki_hypno_menu = 3
            y "suki, you're completely calm."
            y "you are at peace."
            y "you want to do as instructed."
            suki "i want to... do as... instructed..."
            y "very good."
            y "now..."
            y "you will let me take control of your mind."
            y "you will let me undo your compulsion."
            suki "n... no..."
            y "damn it!"
            y "what can i do to make you vulnerable!"
            y "hmm....."
            y "that dai lee agent did say something about approaching this a little... differently."
            menu:
                "berate her":
                    ya "listen up, you slut!"
                    suki "....."
                    ya "you're gonna do what you're fucking told!"
                    ya "now let me in!"
                    suki "n... no..."
                    y "...fuck."
                    y "......"
                    y "maybe...."
                "take her clothes off":

                    pass
            y "suki."
            y "stand up."
            hide tohy_suki_blink
            hide tohy
            hide expression "ebackgrounds/hypno_room1.jpg"
            show expression "ebackgrounds/hypno_room2.jpg"
            with Dissolve(2.0)

            show tosi tosi01
            show tosi_hypno_eyes
            with Dissolve(1)

            y "take your clothes off."
            y "(this is an actual hypnotic experience, not from a trigger phrase, so it should work...)"
            suki "......."
            suki "............"
            show tosi tosi04 with Dissolve(2.0)
            y "i know i'm supposed to be the good guy here, but..."
            y "hell yeah!"
            show ctc
            pause
            hide ctc
            y "alright, sit back in the chair, suki."
            hide tosi tosi01
            hide tosi_hypno_eyes
            hide expression "ebackgrounds/hypno_room2.jpg"
            show expression "ebackgrounds/hypno_room1.jpg"
            show tohy suki04
            with Dissolve(2.0)
            y "damn, that's a view."
            show ctc
            pause
            hide ctc
            y "let's try this again..."
            y "you are in your underwear."
            y "you are at my mercy."
            y "you are alone."
            y "how do you feel?"
            suki "vul... vulnerable..."
            y "(i hope this works...)"
            y "suki."
            y "you will let me into your mind."
            y "you will follow my instructions, even if they contradict older instructions."
            suki "i will... let you... in my mind..."
            y "......"
            y "fuck yeah!"
            y "alright, i think that's enough for now."
            y "when i snap my fingers, you will wake up."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"
            show tohy suki05
            with Dissolve(1)
            suki "what..."
            y "welcome back!"
            suki "why..."
            suki "...am i in my underwear?"
            y "oh. um."
            y "i sort of... had to."
            y "to get you vulnerable."
            suki "....."
            suki "did it work?"
            y "yeah, actually."
            suki "great!"

            hide tohy
            scene hypno_room2
            with Dissolve(1)
            $ renpy.pause(0.5)
            show tosi tosi01 with Dissolve(1)
            suki "so...?"
            suki "am i free?"
            y "not yet."
            y "I still have to actually get you out from being triggered, but i think i'll have access now."
            suki "well... if you ever need to..."
            suki "...actually get me naked..."
            suki "you have my permission."
            y "seriously?"
            suki "whatever it takes."
            y "i will keep that in mind."
            suki "um... one other thing."
            y "oh? what's up?"
            show tosi_blink with dissolve
            suki "I have this... urge to share my plans with you."
            y "you do?"
            suki "yeah."
            suki "i think you could help me."
            hide tosi_blink with dissolve
            suki "want to meet at the tavern later and talk about it?"
            y "sure."
            suki "great."
            suki "see you later, aang!"
            hide tosi with dissolve
            y "sounds like a side effect of the treatment."
            y "she's opening up to me."
            y "guess i'll meet her later."
            $ love_suki_hypno = 10
            jump love_bk3_village_background

        "remove compulsion" if suki_hypno_menu <4:
            if suki_hypno_menu ==0:
                y "i need to limit her current brainwashing first."
                jump love_suki_hypno_menu
            if suki_hypno_menu ==1:
                y "i need to remove her mental barrier before i can do this."
                jump love_suki_hypno_menu
            if suki_hypno_menu ==2:
                y "i need to remove her mental barrier before i can do this."
                jump love_suki_hypno_menu
            else:
                $ suki_hypno_menu = 4
                y "alright suki, I think we need to get you into the right state of mind."
                y "stand up."
                hide tohy_suki_blink
                hide tohy
                hide expression "ebackgrounds/hypno_room1.jpg"
                show expression "ebackgrounds/hypno_room2.jpg"
                with Dissolve(2.0)

                show tosi tosi01
                show tosi_hypno_eyes
                with Dissolve(1)

                y "take your clothes off."
                suki "............"
                show tosi tosi04 with Dissolve(2.0)
                y "i'm not gonna get tired of that view any time soon."
                show ctc
                pause
                hide ctc
                y "alright, sit back in the chair, suki."
                hide tosi tosi01
                hide tosi_hypno_eyes
                hide expression "ebackgrounds/hypno_room2.jpg"
                show expression "ebackgrounds/hypno_room1.jpg"
                show tohy suki04
                with Dissolve(2.0)
                y "damn, that's a sight."
                show ctc
                pause
                hide ctc
                y "how do you feel?"
                suki "vul... vulnerable..."
                y "good."
                y "now..."
                y "let go of all your compulsions."
                y "you don't answer to anyone."
                y "You will follow your own heart."

                suki "follow... my... heart..."
                y "that's right."
                suki "must... must answer... to long feng...."
                y "damn."
                y "......."
                y "hmmm...."
                menu:
                    "\"get naked!\"":
                        pass
                    "try again, forcefully":

                        y "suki!"
                        y "let go of all your compulsions!"
                        suki "must... must answer... to long feng...."
                        y "damn it!"
                        y "hmm...."

                y "suki...."
                y "stand up."

                hide tohy_suki_blink
                hide tohy
                hide expression "ebackgrounds/hypno_room1.jpg"
                show expression "ebackgrounds/hypno_room2.jpg"
                with Dissolve(2.0)

                show tosi tosi04
                show tosi_hypno_eyes
                with Dissolve(1)

                y "take your underwear off."
                suki "............"
                show tosi tosi05 with Dissolve(2.0)
                y "oh. hell. yes."
                show ctc
                pause
                hide ctc
                y "go ahead and sit back in the chair."
                hide tosi tosi01
                hide tosi_hypno_eyes
                hide expression "ebackgrounds/hypno_room2.jpg"
                show expression "ebackgrounds/hypno_room1.jpg"
                show tohy suki03
                with Dissolve(2.0)
                y "fuck, you're sexy."
                show ctc
                pause
                hide ctc
                suki "I'm... sexy..."
                y "that's... not what i intended."
                y "...."
                y "but sure, positive body image and all that."
                y "probably good for you?"
                y "not like i know what i'm doing here."
                y "how do you feel?"
                suki "op... open..."
                y "good."
                y "now, give in to me... and let go of your compulsions."
                suki "i must... let go... no... must..."
                suki "answer... long... feng... no... let... no..."
                y "this isn't going well, is it?"
                suki "must... no... must... no..."
                y "okay, before your brain melts, stop trying that."
                suki "............."
                y "how about I change the trigger phrase?"
                y "that at least makes your trance unlikely to induce."
                suki "............."

                y "when you hear your old phrase... um..."
                y "fuck, what was the phrase?"
                jump spam_menu

                label spam_menu:
                    menu:
                        "the earth king has invited you to lake laogai":
                            y "right."
                            y "instead of \"the earth king has invited you to lake laogai\"..."
                        "NYMPHO PEE PEE TEENS HAVE MORTGAGED IT ALL TO UPDATE THEIR PAYPAL ACCOUNT SETTINGS":

                            "why would it be this? and why would you click on it?"
                            "this is clearly spam."
                            "rethink your life choices and try again."
                            jump spam_menu

                y "your new hypnosis-inducing phrase will be..."
                menu:
                    "my meatballs are drenched in sauce":
                        y "\"my meatballs are drenched in sauce.\""
                        $ love_trigger = "my meatballs are drenched in sauce"
                    "man why you even got to do a thing":

                        y "\"man why you even gotta do a thing.\""
                        $ love_trigger = "man why you even gotta do a thing"

                suki "I will... only answer... to..."
                suki "{i}[love_trigger]."
                y "great!"
                y "well, i think this is progress."
                y "when i snap my fingers, you will wake up."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"
                show tohy suki06
                with Dissolve(1)
                suki "what..."
                y "welcome back!"
                suki "did we do it?"
                y "sort of!"
                suki "hey, aang...?"
                y "yeah?"
                suki "why am i naked?"
                y "uh... it was necessary."
                suki "you didn't make me... do anything weird, right?"
                y "like what?"
                suki "Like... take your cock in my ass?"
                y "hrgh."
                suki "what?"
                y "i went from flaccid to rock hard very quickly and it took me by surprise."
                suki "well that just sounds like a good time."

                hide tohy
                scene hypno_room2
                with Dissolve(1)
                $ renpy.pause(0.5)
                show tosi tosi06 with Dissolve(1)
                suki "so...?"
                suki "am i good to go?"
                show ctc
                pause
                hide ctc
                y "um. sort of."
                suki "alright, let me put clothes on and we'll talk."
                show tosi tosi05
                show tosi_blink
                with dissolve
                suki "go ahead, i'm just dressing."
                y "well..."
                show tosi tosi04
                hide tosi_blink
                with dissolve
                suki "uh huh..."
                suki "stupid titwraps..."
                y "i was able to change the trigger phrase, so there's no real risk to you any more."
                show tosi tosi01 with dissolve
                suki "that's great!"
                y "yeah, but it's still embedded in there."
                y "if someone said it by accident..."
                suki "right."
                y "but we're good for the moment i think."
                suki "that's great."
                suki "thanks, aang."
                suki "come by the tavern sometime and keep me company."
                suki "see ya!"
                hide tosi with dissolve
                $ love_suki_hypno = 13
                jump love_bk3_village_background

        "remove compulsion" if suki_hypno_menu ==4:
            $ suki_hypno_menu = 5
            "test"
        "remove compulsion" if suki_hypno_menu ==5:
            $ suki_hypno_menu = 6
            "test"

label suki_night_raid:
    $ suki_hypno_today = True
    hide screen earth_money_date
    scene black with dissolve
    "you follow suki... sneaking into the city."
    scene basingse_city_night
    with dissolve
    y "what now?"
    show tosi tosi10 with dissolve
    suki "now, we-"
    y "whoa!"
    y "when did you get changed?"
    suki "while you were banging one out in the bathroom."
    y "....."
    y "you heard that, huh?"
    suki "uh, yeah."
    suki "guess who i am: \"unh... uh... occupied! i'm... uh... having a difficult... uh... poop!\""
    y "i don't sound like that."
    suki "you sound exactly like that."
    suki "now, focus!"
    y "on what?"
    suki "you know there's a curfew in the city at night, right?"
    y "lame."
    suki "yeah, but that means that dai lee agents are spread out maintaining the curfew."
    suki "we're going to take down the dai lee agents posted at each location."
    y "all of them?"
    suki "all of them."
    y "okay...."
    suki "we'll need to sneak into each location and watch them before we strike."
    suki "just to make sure we hit them at the right moment."
    y "this is not the interior design challenge you promised."
    show tosi tosi11 with dissolve
    suki "just shut up and let's do this."
    y "wait-"
    hide tosi with dissolve
    y "...."
    y "no, that's fine, i didn't have any questions or concerns."
    y "let's just attack earthbending soldiers, that'll be problem-free."
    y "...."
    y "wait up!"
    $ love_suki_hypno = 11
    $ bk3_day = False
    jump love_basingse_night1

label love_suki_mast:
    hide screen earth_money_date
    if not suki_mast:
        suki "also, sorry, but i'm really busy at the moment."
        y "there's... no one here."
        suki "can't talk! lots to do!"
        suki "grab yourself a drink!"
        hide tosi with dissolve
        y "guess i'll stand in the corner or something."
        show tosi tosi03 with moveinright
        hide tosi with moveoutleft
        "You watch suki run back and forth carrying drinks."
        show tosi tosi03:
            xzoom -1
        with moveinleft
        hide tosi with moveoutright
        "she seems to be working hard."
        show tosi tosi02 with dissolve
        suki "*pant pant*"
        y "tired?"
        suki "yeah...."
        suki "can i... sit there?"
        "you look down at a bench next to you."
        scene black
        scene expression "bk3/suki/pussyrub/background.jpg"
        with Dissolve(1)
        y "....why didn't i sit there?"
    if suki_mast:
        scene black
        scene expression "bk3/suki/pussyrub/background.jpg"
        with Dissolve(1)
    stop music
    play music "audio/Unwritten Return.mp3"
    show tosr tosr01 with vshake
    suki "Pffff."
    suki "it's good to get off of my feet for a moment!"
    show ctc
    pause
    hide ctc
    suki "It feels like I've done nothing but walk today!"
    y "Yeah, but it beats being locked up in a woodblock, right?"

    show tosr tosr02
    suki "You got that right!"
    show ctc
    pause
    hide ctc
    if not suki_mast:
        suki "but still... you're going to think I'm crazy..."
        y "I doubt it."
        y "but go on."
        suki "There was something strangely, ehm, exciting about the whole situation."
        y "which?"
        suki "the... woodblock incident."
        y "oh?"
        suki "yeah..."
        suki "I still hate everyone's guts who put me in there..."
        suki "...but when you walked in while I was naked and couldn't move..."
        show tosr tosr03
        suki "part of me was feeling very excited."
        suki "And I don't just mean because I was looking forward to be freed."
        show tosr tosr02
        suki "I feel I can tell you, since you got me out of there..."
        suki "...and we've been really working together..."
        suki "...but it's still hard to admit."
        suki "Even to myself."
        y "Was it exhilarating when you asked me to get the key?"

        show tosr tosr03
        suki "Like you wouldn't believe!"
        show tosr tosr10
        suki "You don't... think less of me for that, do you?"
        y "Fuck no, I don't."
        y "I could hammer nails with how hard my dick was during that."

        show tosr tosr02
        suki "You didn't think it was gross?"
        y "Absolutely not."
        suki "I... eh... I do have one regret..."
        y "seriously?"
        suki "I kind wish the key was put somewhere else..."
        suki "Somewhere a bit lower."
        y ".........."
        suki "If you want you can... go look for the key again."
        suki "I mean... it's not there, but that doesn't mean you can't feel around for it."
        suki "if you {i}feel{/i} me."

    if suki_mast:
        suki "speaking of..."
        suki "i'm having a really stressful day..."
        y "....."
    y "Here? Now?"
    show tosr tosr10
    suki "You don't want to?"

    show tosr tosr04 with hpunch
    suki "ooh!"

    hide tosr
    show tosr tosr05
    show tosr_pussyrub1

    suki "Hmmm...."
    show ctc
    pause
    hide ctc
    y "i can feel a pair of tasty little lips down here."
    suki "mmmm...."
    y "I wonder what happens if i rub them?"
    suki "aahh..."
    suki "I've been looking forward to this so much."
    y "oh?"
    suki "I... i've been thinking about this..."
    suki "a lot."
    y "I can tell, I already feel you moistening right through your pants."
    suki "w...wait..."
    suki "I can't... walk around the rest of the night with soggy pants."
    suki "J-just a moment."
    hide tosr_pussyrub1 with dissolve
    "With a fluid motion Suki slips down her pants."

    show tosr tosr06
    suki "There, that should solve that problem."
    show ctc
    pause
    hide ctc
    y "Someone could come over here any moment."
    y "we're... really visible."
    suki "Unless that's a problem for you, I really don't care who sees us."
    y "That's all I needed to hear."
    menu:
        "stick your fingers in her mouth first":
            y "why don't you wet my fingers? "
            y "I doubt it's needed for lubrication by now, but I just like doing it."
            show tosr tosr07
            show expression "bk3/suki/pussyrub/hand_mouth.png"
            "Suki greedily sucks on your fingers."
            show ctc
            pause
            hide ctc
            y "Everytime i feel like my dick can't get any harder, reality proves me a liar."
            y "Time for some pussy play."
            hide expression "bk3/suki/pussyrub/hand_mouth.png"
        "go straight for the pussy":
            pass


    show tosr tosr11 with Dissolve(1.5)
    show tosr tosr12 with Dissolve(1.5)
    suki "*mmmmm....*"
    show ctc
    pause
    hide ctc
    suki "You're... you're really... really..."
    suki "{i}good{/i} at this."
    show ctc
    pause
    hide ctc
    suki "h-how.... ohh..."
    y "I've had some practice."
    show tosr_pussyrub1

    show tosr tosr07
    "You let your fingers glide over her wet pussy..."
    "...easily slipping your fingers deep within."
    "Making sure you stimulate her clit, you keep going up and down, in and out, at a steady and unrelenting pace."
    suki "I would never have... have believed something like this could ever feel so damn good."
    suki "I've done it for myself, but it... ahhh... just isn't the same."
    suki "Not even close."
    suki "You can help me search for that \"key\" whenever you want, Aang."
    hide tosr_pussyrub1
    show expression "bk3/suki/pussyrub/hand_drip.png"
    with Dissolve(1.5)
    y "whoa, I believe you."
    y "It's like an honest-to-god waterfall down there!"
    menu:
        "make her taste it":
            hide expression "bk3/suki/pussyrub/hand_drip.png"
            show expression "bk3/suki/pussyrub/hand_mouth.png"
            suki "*mmmmm...*"
            suki "i 'aste 'ood."
            y "i'll have to try it myself later."
            suki "*mmmm....*"
            hide expression "bk3/suki/pussyrub/hand_mouth.png"
        "Make her cum!":
            hide expression "bk3/suki/pussyrub/hand_drip.png"
    y "Enough with all this foreplay, I'm going to make you cum so hard you'll be launching yourself."
    show tosr tosr07
    show tosr_pussyrub2
    suki "Ohh... oh... fuck..."
    "You start rubbing Suki's clit with renewed vigor, using every bit of stamina left in your fingers."
    show ctc
    pause
    hide ctc
    hide tosr_pussyrub2
    show tosr tosr13
    suki "Aaah! AAhhh!!"

    show expression "bk3/suki/pussyrub/pjuice_1.png" with hpunch

    suki "Ah!"

    show expression "bk3/suki/pussyrub/pjuice_2.png" with hpunch
    suki "AAahh!!"

    show expression "bk3/suki/pussyrub/pjuice_3.png" with hpunch

    suki "AAAAAAAAAAAahh!!" with hpunch

    show tosr tosr11 with dissolve

    show ctc
    pause
    hide ctc

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.0)


    show tosr tosr07

    suki "OOoooh spirits..."
    suki "I... I came so hard..."
    show tosr tosr07
    suki "Ah... I just... I just need a moment.."
    y "Certainly."
    y "Just make sure you don't slip when you stand up."
    y "The floor is kind of wet."
    y "you think you can still work after this?"
    suki "f...fuck the customers..."
    suki "i'm taking a \"me\" day."
    y "...fair enough."
    if not suki_mast_admit:
        $ suki_mast_admit = True
        y "suki, i have to ask...."
        y "what brought this on?"
        suki "what do you mean?"
        y "well... this."
        suki "oh, you mean you fingerbanging me?"
        suki "i don't know, honestly."
        suki "i've always liked you, you know."
        suki "I just... didn't do anything about it because of katara."
        suki "I know she likes you."
        suki "but for some reason... i just feel more open and free."
        suki "less limited by concerns."
        y ".....oh."
        y "that's probably... fine..."
        suki "yeah...."
        suki "now, i've just got to rest for a minute..."
        y "alright."
    y "I'll see you later."
    suki "anhh...."
    show ctc
    pause
    hide ctc
    $ suki_mast = True
    scene black with dissolve
    "tired, you head home for the night."
    jump love_bk3_village_background

label lake_cock_talk:
    scene black with Dissolve(1)
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_1
    with Dissolve(1)
    y "nice..."
    y "I could really jump in that water."
    y "toph, are you finished getting changed?"
    t "yes..."
    t "um..."
    show toi toi21
    with dissolve
    show ctc
    pause
    hide ctc
    y "...oh, come on."
    y "what are you doing?"
    t "It's... revealing."
    t "maybe i shouldn't have-"
    y "toph, you're sexy."
    y "now quit fucking around, let's go for a swim."
    t "...."
    show toi toi20
    with dissolve
    t "you're right!"
    t "i've got nothing to be ashamed of!"
    y "wow!"
    y "you got that right!"
    t "i mean... not {i}nothing{/i}..."
    t "I have {i}something{/i} to be ashamed of."
    t "i just shouldn't be ashamed of it!"
    y "......."
    show toi_blush
    with dissolve
    t "oh, shut up."
    t "and... i'm not going in the deep end."
    y "It's a lake, not a pool."
    t "you know what i mean."
    t "Let's get in."
    k3 "can i join?"
    hide toi
    hide toi_blush
    show toi toi20:
        xzoom -1
    show toi_swim_surprise
    show toi_blush:
        xzoom -1
    with dissolve
    $ katara_top_nude = False
    $ katara_bottom_nude = False
    show toki toki10
    show toki_swim_smile
    with dissolve
    t "katara?"
    show toki toki11 with dissolve
    k3 "hey guys!"
    hide toi_swim_surprise
    y "how do you always know when we're out here?"
    show toki toki10
    k3 "i don't... i'm just out here all the time."
    k3 "it's not like i'm particularly busy at the hospital."
    k3 "there's like... five important people in the town."
    k3 "and then a bunch of faceless shapes."
    y "that's a little... cynical for a healer."
    k3 "eh."
    k3 "alright, enough talk."
    k3 "i'm here to get wet."
    t "yeah, let's get in the water."
    k3 "not what i meant, but... great!"
    k3 "i'll just take my clothes off and we'll jump in."
    show toi toi22:
        xzoom -1
    with dissolve
    t "wait-"
    $ katara_top_nude = True
    $ katara_bottom_nude = True
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    $ toph_bikini = True
    show ctc
    pause
    hide ctc
    t "umm..."
    k3 "what?"
    k3 "i'm not going to swim in my clothes and get them all ruined."
    k3 "join me, aang."
    t "aang, you're not really going to-"
    y "sure!"
    "you drop your swimsuit to the sand."
    show toi_blush:
        xzoom -1
    with dissolve
    t "okay! i'm going in the water now!"
    hide toi
    hide toi_blush
    hide toi_blink
    with dissolve
    show toki toki12 with dissolve
    k3 "after you, sir!"
    y "thank you, miss!"

    scene black with dissolve
    show expression "ebackgrounds/lake_laogai_2.jpg"
    show toi toi210:
        ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png"
    with dissolve

    t "are you guys done being... weird, yet?"

    show toki toki10:
        ypos -70
    show expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve

    k3 "what's weird?"
    t "you know what i mean!"

    play sound "audio/giggling.mp3"
    show toi toi250
    show toi_wave
    show toki toki11
    show toki_swim_smile:
        ypos -70
    k3 "hey!"
    show toki toki110
    show toki_wave
    k3 "well... take this!"
    play sound "audio/water_splashing.mp3"
    t "haha!"
    y "that's it, i'm taking charge of this water fight!"
    k3 "don't you dare!"
    t "bring it, twinkletoes!"
    y "hey katara, remember when you taught me the \"octopus\" back in your village?"
    k3 "sure! the fighting stance which... give you tentacle arms..."
    y "hehehe..."
    k3 "let's... save that for another time, aang..."
    t "what are you two babbling about?"
    y "i was thinking about throwing you into the lake."
    t "don't even think about it, aang!"
    play sound "audio/giggling.mp3"
    hide toki_wave
    hide toi_wave
    show toi toi210
    show toki toki10
    show toi_swim_smile:
        ypos -100
    hide black
    show black
    with dissolve
    "the three of you spend the afternoon playing and laughing in the water."
    hide black
    with dissolve
    t "hahaha!"
    show toki_swim_surprised:
        ypos -70
    with dissolve
    k3 "i didn't think i'd ever say this, but i'm tired of moving water around!"
    y "yeah, same."
    y "aahh... the sun is nice."
    hide toki_swim_surprised with dissolve
    k3 "i agree!"
    hide toi_swim_smile with dissolve
    t "hey... guys...?"
    y "yeah?"
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "are you both... really so okay with being naked?"
    y "yeah, why not?"
    t "i mean... i know the water is covering some, but isn't it... embarrassing to be that exposed?"
    show toki_swim_surprised:
        ypos -70
    with dissolve
    k3 "I'm not embarrassed."
    show toki_swim_blink:
        ypos -70
    with dissolve
    k3 "i like my body."
    hide toki_swim_blink with dissolve
    k3 "how about you, aang?"
    y "same."
    hide toki_swim_surprised with dissolve
    k3 "see?"
    k3 "join us."
    t "I don't know..."
    y "who's the wimp now?"
    hide toi_swim_blush
    show toi_swim_angry:
        ypos -100
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "I'm not a wimp!"
    t "........."
    t "...fine!"
    hide black
    show black
    with dissolve
    $ toph_bikini = False
    hide black
    show toi_swim_blush:
        ypos -100
    show toi_swim_blink:
        ypos -100
    with dissolve
    t "see?"
    show ctc
    pause
    hide ctc
    y "Nice!"
    k3 "hot stuff!"
    hide toi_swim_angry
    with dissolve
    t "come on, guys... stop it..."
    y "aw, it's flattering to have someone appreciate your nudity."
    k3 "oh, yeah?"
    k3 "then how about i take a look?"
    y "what do you-"

    show expression "bk3/toph/swim_idles/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    show expression "bk3/katara/swim_idle/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat

    y "hey!"
    y "you're lowering the water!"
    show ctc
    pause
    hide ctc
    hide toi_swim_blink with dissolve
    t "katara..."
    show toki_swim_smile:
        ypos -70
    with dissolve
    k3 "you said you didn't mind, aang."
    y "....you've got me there."
    k3 "besides i wanted to take a look at your big, handsome cock."
    show toi_swim_surprise:
        ypos -100
    hide toi_swim_blush
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "katara!"
    k3 "what?"
    k3 "he's got an amazing cock!"
    k3 "don't tell me you haven't gotten a handful of it yourself."
    hide toi_swim_surprise
    with dissolve
    t "um."
    k3 "see? look at that tasty cock."
    k3 "that'd be so nice to suck on."
    show toi_swim_surprise:
        ypos -100
    hide toi_swim_blush
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "ka-katara!"
    k3 "I bet you could use a blowjob, couldn't you?"
    y "well, yeah..."
    t "aang!"
    k3 "mmm... i'd love to take care of that..."
    k3 "but apparently you have a girl that i {i}hope{/i} is taking care of that."
    k3 "for both your sakes."
    hide toi_swim_surprise with dissolve
    t "umm...."
    k3 "it'd be a shame to put that big dick to waste."
    k3 "well, let me know if it doesn't work out between you and that girl, aang..."
    t "....."
    k3 "i'll put you... at ease."
    show toi_swim_angry:
        ypos -100
    hide toi_swim_blush
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "katara!"
    t "that's going too far for a joke!"
    k3 "what joke?"
    y "i'm not worried, katara."
    y "i'm sure she wants to suck me..."
    y "...as badly as i want to slobber on her pussy."
    hide toi_swim_angry
    show toi_swim_surprise:
        ypos -100
    hide toi_swim_blush
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "......"
    t "i......."
    t "you......."
    show toki_swim_blink:
        ypos -70
    with dissolve
    k3 "ahhh... this really is such a nice day."
    k3 "i think we should head back now."
    scene black with dissolve
    $ katara_top_nude = False
    $ katara_bottom_nude = False
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    $ toph_bikini = False
    scene lake_laogai_1
    show toki toki10
    show toi toi210
    show toi_swim_surprise
    with dissolve
    k3 "toph...?"
    t "..........."
    k3 "you should really get dressed, dear."
    t "............"
    y "she seems to still be in shock."
    k3 "maybe i should leave you two alone to.... talk."
    t "....eep...."
    y "go on ahead."
    k3 "good luck."
    hide toki with dissolve
    hide toi
    hide toi_swim_surprise
    with dissolve
    show toi toi210:
        xzoom -1
    show toi_swim_surprise:
        xzoom -1
    with dissolve
    y "toph? you still there?"
    hide toi_swim_surprise
    show expression "bk3/toph/idles/idle_fl_regret.png"
    with dissolve
    t "um..."
    y "there you are."
    y "you okay?"
    y "want to talk?"
    t "i... no."
    t "no, i... i don't want to talk."
    t "can we... maybe... just go for a swim?"
    y "...you know we just did, right?"
    y "how out of it are you?"
    t "we just played in the shallow end."
    t "will you... take me out into the water?"
    t "just the two of us?"
    show toi_blink
    with dissolve

    t "i'm still not a very good swimmer."
    t "I'll... need your help."
    y "uh, sure. of course."
    scene black with dissolve
    "you step into the water and toph follows you."
    "as you work your way into deeper water, she gently takes your hand at first..."
    "...but her grip tightens with fear and determination as you reach a point where she can no longer stand."
    scene bg_swim
    show tols tols05_1:
        xpos 200
        parallel:
            linear 6.0 xpos 300
            linear 6.0 xpos 200
            repeat
        parallel:
            linear 3.0 ypos 20
            linear 3.0 ypos 0
            repeat
    with Dissolve(2.0)
    t "i can... do this..."
    "toph squeezes your hands almost painfully tightly as she lifts her legs up and begins to kick."
    y "ow.... are you okay?"
    t "just... let me get used to it again..."
    show tols tols05_2 with dissolve
    t "don't let go!"
    y "I won't."
    "toph struggles for a few minutes, while she gets used to being in water again."
    show tols tols04_1 with Dissolve(1)
    "she eventually gets the hang of it and you can feel her grip loosening."
    "...she doesn't fully let go, though."
    t "i don't think i'll ever get used to this..."
    y "I can imagine it must be particularly terrifying since you can't see."
    y "floating in a big empty space, unable to tell where the shore is, unable to touch the ground..."
    show tols tols05_1
    t "aang! shut up!"
    y "oh, right. sorry."
    t ".........."
    t "It's...."
    show tols tols04_1 with dissolve
    t "....okay."
    t "i know you meant well."
    t "it is... not my favorite."
    t "but..."
    show tols tols04_2 with dissolve
    t "i have you."
    "you and toph float in silence for a minute, enjoying the water and each other's company."
    t "....."
    show tols tols04_3 with dissolve
    t "I do... want an adult relationship, you know."
    y "hm?"
    t "never mind..."
    t "can we just... swim and relax?"
    show tols tols04_2
    t "i'd like to not worry about anything for a bit."
    y "are you able to swim and relax?"
    y "i feel like they're mutually exclusive for you."
    show tols tols05_1
    t "hey! this is hard!"
    y "wanna go faster?"
    t "this is fast enough...."
    y "i think we can go faster."
    t "don't you da-"
    show tols tols05_1:
        xzoom 1.0
        linear 7.0 xpos 900
        xzoom -1.0
        linear 7.0 xpos -500
        repeat
    t "nonono!!"
    t "wait!"
    t "......."
    show tols tols02_1
    t "weee!!"
    y "no, you're not having fun at all..."
    t "i'm definitely not!"
    t "and don't stop!"
    y "hahaha...."
    show ctc
    pause
    hide ctc
    show tols tols03_1
    t "okay, okay..."
    t "can we go sit where it's shallow?"
    t "i like being in the water, but... it's still nerve-wracking being this far out."
    y "sure, hang on tight."
    scene black
    scene bg_swim_1
    with fade
    "you gently pull toph back to where she can stand."
    show tols tols15 with dissolve
    "she plops right down into the water, kneeling and leaning back."
    show ctc
    pause
    hide ctc
    t "oof!"
    t "that was fun, but i'm glad i can feel the ground again."
    t "i'll never get used to being in all that water."
    "you drop your butt in the sand and lean back on your arms."
    y "you're doing well, all things considered."
    y "It can't be easy."
    y "hey, i just realized, we're kind of training each other."
    y "adds a new level to our relationship, eh?"
    t "....."
    y "i was just kid-"
    t "aang...?"
    t "do we... even have a relationship?"
    y "what? of course we do."
    t "it's just you haven't... we haven't really... labeled us."
    menu:
        "labels don't matter":
            y "i like you and you like me."
            y "we want to be with each other."
            y "if that's not a relationship, i don't know what is."
            t "...you're right."
            t "i'm being ridiculous; we are in a relationship."
        "let's change that":

            y "well..."
            y "will you be my girlfriend?"
            t "r-really?"
            y "yeah."
            t "i'd... really like that."

    y "then it's settled."
    t "wow..."
    t "that's..."
    t "a big deal."
    y "yeah, so don't fuck it up!"
    t "...."
    y "joking, again."
    t "aang, i...."
    t "....i want to be in an adult relationship with you, i just...."
    t "like you said to katara, i... i don't know what... what i'm..."
    show tols tols16
    t "....."
    t "i hope you'll be patient with me."
    t "i hope... you like me for me."
    t "for who i am, and not just... my body or training or... something."
    show tols tols15
    menu:
        "those things are important":
            $ toph_angry = 1
            y "those things are important."
            y "i don't know if we'd be what we are without them."
            show tols tols17 with dissolve
            t "fine."
            t "i'm going to go."
            y "i just meant that it's everything together that-"
            t "it's fine."
            hide tols with dissolve
            y "wait, toph-"
            $ toph_top_nude = False
            $ toph_bottom_nude = False
            scene black
            scene lake_laogai_1
            show toi toi202:
                xzoom -1 xpos 720
            show toi_swim_angry:
                xpos 720
            with fade
            t "i'll see you later, aang."
            y "don't leave angry, i just meant-"
            hide toi
            hide toi_swim_angry
            with moveoutright
            y "*sigh...*"
            y "damn it."
            $ bk3_day = False
            jump love_bk3_village_background
        "those things don't matter":

            y "none of that matters, toph."
            y "I just like you."
            y "you don't have to do anything that makes you uncomfortable."
            t "...thanks, aang."
            t "that... means a lot."
            t "okay, i'm gonna dry off."
            t "....you can watch, if you want."
            scene black
            scene lake_laogai_1
            show tols tols20:
                ypos 0
            with fade

            show ctc
            pause
            hide ctc
            y "what a tight, pretty pussy."
            t "I can still hear you, aang!"
            menu:
                "just calling it like i see it":
                    y "just calling it like i see it."
                    t "you're incorrigable."
                    y "would you like me better if i were?"
                    t "....no...."
                    y "in that case... you have a nice ass, too."
                "oh, sorry, did i say that out loud?":

                    y "it wasn't an accident!"
                    y "i wanted you to hear that."
                    t "why?!"
                    y "because you're sexy and i like teasing you with the truth."
                    t "you're incorrigable."

            $ toph_top_nude = False
            $ toph_bottom_nude = False
            hide tols
            show toi toi200
            with fade
            t "i'm dry, let's go."
            y "sounds good."
            scene black with dissolve
            "particularly tired after the day's excursion, you head home and promptly fall asleep."
            jump love_bk3_next

label june_hunt:
    $ love_june_hypno = 12
    scene black with Dissolve(1)
    hide screen earth_money_date
    stop music
    play music "audio/Smooth Lovin.mp3"
    scene black
    scene inside_brothel_1
    show toju toju01
    with dissolve
    y "the brothel?"
    y "why didn't you just ask me to come here normally?"
    ju "i don't have much time, okay?"
    ju "and it has to be here!"
    y "why?"
    y "also... why aren't you wearing your brothel dress?"
    y "and where is the earthbending training you promised?"
    ju "there... isn't going to be any earthbending."
    y "you lied to toph?"
    ju "yes."
    y "...."
    y "that's actually fine with me."
    ju "as for the rest...."
    ju "i... have to admit something to you."
    y "okay..."
    ju "don't be mad, okay?"
    y "sure."
    ju "i sort of... was hired to hunt you."
    ya "you bitch!"
    ju "you said you wouldn't be mad!"
    ya "i was lying!"
    ya "you bitch!"
    ya "is this where it's going down?"
    ya "is this a trap?"
    ya "i will fucking murder-"
    show toju_blink with dissolve
    ju "No, no, no! listen!"
    ju "i was hired to hunt you, but since you rescued me..."
    ju "and you've been helping me with this brainwashing..."
    ju "i've suddenly been feeling very guilty and... don't want to hurt you."
    y "......"
    y "(i am so glad i told her to be nice to me.)"
    hide toju_blink with dissolve
    ju "I owe you a debt, and i've changed my mind about the hunt."
    ju "unfortunately, the fire nation prince already paid me, and is now demanding your head or mine."
    y "okay...."
    ju "so, i need you to kill me."
    y "....."
    ju "....."
    y "what?!?"
    ju "not really!"
    ju "just... put on a bit of a show."
    ju "and then... prove i'm dead."
    ju "somehow."
    y "alright, when is this going down?"
    ju "Um..."
    ju "now."
    y "what?!"
    ju "they knew i was here, and i sort of... supplied a tip that i'd be catching you here... now-ish."
    y "and you didn't think to give me a heads up?"
    ju "it happened really fast, i didn't have much time."
    y "okay, so we're going to pretend fight, and then..."
    ju "and then you have to convince them i'm dead."
    y "how?"
    ju "i don't know, think of something!"
    ju "i'll go with it."
    "at that moment you hear some light footsteps and see some faces in the window..."
    bk3_fg1 "oh, it hasn't started yet!"
    bk3_fg1 "front row seats!"
    bk3_fg2 "hey, so... what happens if someone catches us?"
    bk3_fg1 "we're... cosplayers?"
    bk3_fg2 "that seems risky."
    bk3_fg1 "just... pay attention!"
    bk3_fg1 "if all goes well, she'll kill him and we can get out of here."
    bk3_fg2 "what if... you know... she doesn't?"
    bk3_fg1 "if the avatar wins?"
    bk3_fg2 "yeah."
    bk3_fg1 "if she's still alive, we're supposed to bring her back with us."
    bk3_fg1 "yeah."
    bk3_fg2 "....."
    bk3_fg2 "fuck, i hope she wins."
    bk3_fg1 "she scares me too, man."
    y "um... june?"
    ju "yeah?"
    y "I... see the guards."
    y "they're at the window."
    show toju_blink with dissolve
    ju "ahem..."
    show toju toju03
    hide toju_blink
    with dissolve
    ju "{size=+5}ah! avatar!"
    ju "{size=+5}at last! i have found you!"
    ju "{size=+5}there is no more escape. for you. here. today. no."
    y "...wow."
    y "{size=-3}did you act in college?"
    ju "{size=-3}a little bit."
    y "{size=-3}it shows."
    ju "{size=-3}thanks."
    ju "{size=+4}time to do the fighting! that is now!"
    y "...."
    y "okay..."
    ju "hyaahh!!"
    scene black with dissolve
    "after a convincing fake battle, june falls to the floor with a death cry."

























    show expression "ebackgrounds/inside_brothel_2.jpg"
    show expression "ebackgrounds/inside_brothel_1.jpg":
        ypos -250

    ju "Aaaah!"
    play sound "audio/thud.mp3"
    show totz totz05 with hpunch

    y "{size=+5}Oh, shit!"
    y "{size=+5}I killed her!"
    y "(that should do it...)"

    bk3_fg2 "Do you think she's really dead?"
    bk3_fg1 "Don't know... she could be just unconscious."
    bk3_fg1 "we should probably... you know... check."
    bk3_fg2 "and if she wakes up and sees me leaning over her?"
    bk3_fg2 "she'll kick my ass."
    bk3_fg1 "come on, you sissy. go check it out."
    bk3_fg2 "why don't you do it, then."
    bk3_fg1 "......."
    bk3_fg1 "....maybe we could ask the avatar to do it?"
    bk3_fg2 "he's the one that took her down!"
    bk3_fg1 "yeah, but... he seems like a pretty good guy."
    bk3_fg2 "....i admire your outlook on life."
    bk3_fg2 "alright, let's do this."
    g1 "hey! avatar!"
    y "(oh, damn it.)"
    y "(did it not work?)"
    y "yes...?"
    g1 "so... i know you just, you know, beat her up, but..."
    g1 "can you check if she's still alive?"
    g1 "we sort of... have to take her with us, if she is."
    y "and if she's not?"
    g1 "we have to reschedule her."
    g2 "....resuscitate her."
    g1 "right."
    g1 "can you... do that for us?"
    y "...why would i?"
    y "aren't we enemies?"
    g1 "i like to think of us as enemies with benefits."
    y "that's... not a thing."
    g2 "is that what you and i are, todd?"
    g1 "yes, now shut it, i'm talking to the avatar."
    g2 "aww..."
    g1 "avatar, if you don't check her out, we have to."
    g1 "and, i have to warn you..."
    g1 "if we do it, and she wakes up..."
    g1 "she'll probably kill us."
    g1 "is that what you want?"
    g1 "our deaths on your conscience?"
    y "i could take it or leave that, honestly."
    g2 "don't be mean."
    y "alright, alright, i'll do it."
    g1 "cool."
    g2 "how are you gonna do it?"
    y "um..."
    g2 "you could hit her in the stomach?"
    g2 "she won't be able to avoid making any noise if you do that."
    g1 "dude."
    g1 "that's rough."
    g1 "but a good idea."
    g1 "avatar, do that."
    y "okay, well, i don't work for you, so try that again."
    g1 "um... please?"
    y "(hitting her in the stomach will definitely make her gasp or something...)"
    y "(what can i do?)"
    y "(hmmm....)"
    y "well, tell you what..."
    y "instead...."
    y "i'll take her clothes off."
    "you might have imagined it, but you could swear you saw june's eye twitch."
    g1 "....what?"
    y "well, if she's faking, that'll certainly get her up."
    y "I mean, seriously... have you met her?"
    g2 "...."
    g2 "makes sense."
    y "and if she's actually unconscious...."
    y "we have to remove her restrictive clothing... so she can... breathe?"
    g2 ".........."
    g2 "this guy knows his stuff."
    g1 "you just want to see her naked."
    g2 "and you don't?"
    g1 "...."
    g1 "i agree that this is the correct medical course of action."
    y "alright, here it goes..."
    y "...."
    hide expression "ebackgrounds/inside_brothel_1.jpg"
    show totz totz01
    with Dissolve(1.5)
    y "there!"
    show ctc
    pause
    hide ctc
    y "see? no response."
    y "so... you guys can leave."
    g1 "she could be faking."
    g2 "maybe we should actually take a look ourselv-"
    y "No!"
    y "I... um..."
    y "i've got an idea."
    y "if she's faking, or just unconscious, this should wake her up."
    y "Okay, here we go."
    y "......."
    y "{size=-6}sorry about this, june... try not to move..."
    y "......."
    show totz totz00
    show totz_hit
    play sound "audio/slap.mp3"
    $ renpy.pause (0.9)
    hide totz_hit
    show totz totz01
    ju "{size=-6}oh...!"

    show ctc
    pause
    hide ctc
    g1 "....that didn't work."
    y "i'll try it again."
    g1 "um-"
    show totz totz00
    show totz_hit:
        xpos 200 xzoom -1
    play sound "audio/slap.mp3"
    $ renpy.pause (1)
    hide totz_hit
    show totz totz01
    ju "{size=-6}ugh..."
    g1 "....still didn't work."
    g2 "isn't there something more... medical... we could do?"
    g1 "we are really unqualified for everything we do."
    g2 "but we do it with love."
    g1 "...we really don't."
    y "shut it, you two."
    g1 "well, if she's not faking, then we need to resuscitate her."
    g1 "can you help?"
    g1 "if you don't, we're gonna have to do it."
    g1 "and, again, that will probably end in our death... if she wakes up."
    g2 "maybe we should check her-"
    y "stop offering!"
    y "I'll do it!"
    y "(sorry, june... but i'm trying to help you here!)"
    $ temp_counter = 1
    while temp_counter != 0:
        show totz totz01

        menu:
            "clear the airways" if temp_counter >= 1:
                y "If I remember correctly, the next step of resuscitation is... mouth to mouth."
                ym "(might as well have fun with it.)"
                "you lean over june and press your lips to hers."
                "not wanting to actually blow into her very-much-alive lungs, you kiss her... with a little tongue."

                show expression "bk3/toph/walk/pink.png" with dissolve
                $ renpy.pause(0.5)
                hide expression "bk3/toph/walk/pink.png" with dissolve

                ju "{size=-6}Hmmmm...{/size=-6}"
                y "{size=-6}shhhhh... you're dead, remember?{/size=-6}"
                show expression "bk3/june/titplay/deadface_annoyed.png" with Dissolve(1.5):
                    xpos 501 ypos 166
                ju "{size=-6}then stop pushing your tongue inside...{/size=-6}"
                y "{size=-6}no."
                ju "{size=-6}ggrrhh...."
                hide expression "bk3/june/titplay/deadface_annoyed.png"
                show expression "bk3/june/titplay/deadface_annoyed_1.png":
                    xpos 501 ypos 166
                g2 "what's happening? i can't see."
                g1 "....i don't think he knows what he's doing."
                g2 "why?"
                g1 "because i think he's tonguing her."
                g2 "he might know more than us about this."
                g1 "everyone knows more than us about this."
                g1 "but still..."

            "heart massage" if temp_counter >= 2:
                g1 "you have to massage the heart or something, right?"
                y "Um.... yes."
                y "(i don't want to just punch her chest...)"
                ym "(oh, i know what to do.)"
                ym "{size=-6}get ready, june."
                ju "{size=-6}for wh-"
                show totz totz02
                show ctc
                pause
                hide ctc
                ju "{size=-6}......"
                ju "{size=-6}....fuck...."
                y "Soooo soooooft..."
                show ctc
                pause
                hide ctc
                g1 "that's... not her heart?"
                g2 "sure it is."
                g2 "the tits are in the way, of course he has to massage them."
                g1 "oh. right."
                show ctc
                $ renpy.pause()
                hide ctc


            "extreme heart massage" if temp_counter >= 3:
                g1 "okay, being gentle is not gonna work."
                g1 "maybe i should-"
                y "look, i've got it, alright?!"
                y "......."
                y "this'll do it!"
                show totz totz00
                show totz_hit
                play sound "audio/slap.mp3"
                $ renpy.pause (0.9)
                hide totz_hit
                play sound "audio/slap.mp3"
                show totz_hit:
                    xpos 200 xzoom -1
                $ renpy.pause (1)
                hide totz_hit
                ju "{size=-6}ughh..."
                show totz_hit
                play sound "audio/slap.mp3"
                $ renpy.pause (1)
                hide totz_hit
                play sound "audio/slap.mp3"
                show totz_hit:
                    xpos 200 xzoom -1
                $ renpy.pause (1)
                hide totz_hit
                show totz totz01
                ju "{size=-6}ahh..."
                g2 "....is it just me or does this not make much sense?"
                g1 "you just don't know anything about medicine."

            "nipple search" if temp_counter >= 4:
                ym "i need to get the blood flowing."
                ym "i'll try to dig out those inverted nipples... that might start something."
                ym "I mean those can't be right... right?"
                show totz totz04
                show ctc
                pause
                hide ctc
                ju "{size=-6}you're just getting off on this, aren't you?"
                ym "{size=-6}maybe a little."
                show ctc
                pause
                hide ctc
                g1 "....i'm kinda jealous now."
                g2 "maybe we can take turns?"
                g1 "don't be weird."
                g1 "this man is a hero."
                ym "Oh look, there they are."
                ym "Stubborn little fellas. They won't stay outside."
                g1 "a hero."

            "done" if temp_counter >= 5:
                y "well, I guess she's dead, guys."
                y "I did all I could do."
                y "No one watching this could say I didn't try."
                g1 "i could say that."
                y "......"
                g2 "......"
                g1 "...but i'd be lying."
                g1 "it's been a pleasure working with you."
                $ temp_counter = -1

        $ temp_counter += 1


    y "you know, it's really too bad..."
    y "she was pretty hot."
    y "but she's dead now."
    y "dead. no doubt. at all."
    g1 "sucks. well, let's get out of here."
    g1 "Yeah... there's nothing more we can do."
    g2 "...except have a quick fap?"
    g2 "I mean... those tits still look pretty nice despite those inverted nipples..."
    g1 "dude, respect the dead."
    g2 "but... he..."
    g1 "no respect at all. disgraceful."
    g1 "you should be more like the avatar."
    y "he's right, get it together."
    g2 "....sorry."
    y "i forgive you."
    g1 "We'll leave now."
    "the two guards make their way out, lightly bickering."
    y "...what a cute couple."
    ju "{size=-6}are they gone...?"
    y "{size=-6}wait a bit to make sure they're gone."
    ym "{size=-6}...and so i can enjoy the view."
    ju "{size=-6}......"
    show ctc
    pause
    hide ctc
    y "...."
    y "........."
    y "...Okay..."
    y "You can get up now."
    y "I'm pretty sure they're gone."
    hide expression "ebackgrounds/inside_brothel_2.jpg"
    hide totz
    show expression "ebackgrounds/inside_brothel_1.jpg":
        xpos 0 ypos 0
    show totz totz40
    with fade
    ju "That went... not exactly as expected, but you got rid of those nuisances, so thanks."
    y "Cool."
    ju "you got a little... into it, though."
    y "yeah..."
    ju "I'm going to... go ice my tits."
    ju "ow...."
    y "sorry."
    y "...sort of."
    scene black with dissolve
    jump love_bk3_village_background

label june_titplay_standing:

    show expression "ebackgrounds/inside_brothel_1.jpg"

    show totz totz40
    y "ahh..."
    y "they're so soft and smackable..."
    show totz totz41 with Dissolve(1.5)
    y "I like titties.... a lot."


    $ temp_boolean = False
    while temp_boolean == False:
        show totz totz41

        menu:
            "massage":
                show totz totz43
                $ renpy.pause()
                y "Soooo soooooft."
                y "It's like digging into big sexy marshmallows."
                show ctc
                pause
                hide ctc
            "hit breasts":


                $ temp_counter = 0
                $ totz_emote = 'shock'

                while temp_counter < 6:
                    show totz totz42
                    show totz_hit
                    play sound "audio/slap.mp3"
                    $ renpy.pause (1.0)
                    hide totz_hit
                    play sound "audio/slap.mp3"
                    show totz_hit:
                        xpos 200 xzoom -1
                    $ renpy.pause (1.0)
                    hide totz_hit
                    $ temp_counter  += 1

                show totz totz41
                y "I don't think I've ever smacked something so tasty looking."
            "nipple search":


                $ totz_emote = 'neutral'
                show totz totz44
                $ renpy.pause()
                y "Am I weird for getting a thrill out of this?"
                show ctc
                pause
                hide ctc
            "done":

                $ totz_emote = 'neutral'
                $ temp_boolean = True

        $ totz_emote = 'neutral'

    show totz totz40 with Dissolve(1.5)
    ju "See you later."

    jump love_bk3_village_background


label toph_ass_massage:
    hide screen earth_money_date
    show toi toi04 with dissolve
    t "hey, aang!"
    y "howdy."
    y "where's suki?"
    t "i think i see her at the back."
    scene black
    show expression "bk3/toph/assmassage/background.jpg"

    show toam toam01
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    with fade
    suki "hey! glad you made it."
    suki "sorry, i'm beat..."
    suki "It was a busy day, i'm only just finally sitting down."
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    show toam toam02 with Dissolve(1.5)
    y "do you need any help?"
    suki "Thanks, but things are going pretty well, just busy."
    suki "How about you?"
    show toam toam03
    "The girls start talking and you slowly move your hand on Tophs back, sliding down."
    show toam toam04
    t "Oohh!!"
    suki "What is it Toph?"
    show toam toam05
    t "Hahaha... nothing nothing at all."
    t "Just... remembered something."
    show toam toam06
    "You start rubbing while the girls resume their conversation."
    show ctc
    pause
    hide ctc
    show toam toam07
    suki "You certain you're alright Toph?"
    show ctc
    pause
    hide ctc
    "you grip and squeeze toph's firm little ass cheeks."
    "they tense and release as you knead them."
    "you can feel the edges of her pussy lips as you pull her small, giving buttocks apart."
    "your thumb occasionally presses against her tight, tiny anus... tensing her up as she squeezes your fingers."
    t "Yeah... ev-everything is... arright."
    show toam toam08
    suki "hey, do you mind waiting here for a moment?"
    suki "I'll be back in a minute or five."
    t "Suuuure... take your time."
    show toam toam15 with Dissolve(1.5)
    hide toam
    show tonf tonf16
    with dissolve
    t "Aang!!"
    t "Don't just start feeling me up when I'm talking to someone!!"
    show tonf tonf17
    t "I should be a lot angrier with you, but we only have five minutes!"
    y "...for what?"

    hide tonf
    show toam toam09
    show expression "bk3/toph/assmassage/fluid_skin.png"
    with Dissolve(1.5)
    t "For you to finish what you started!"
    y "If it's just us..."
    y "I'm going to make it a bit more exciting for me, too."
    t "Fine! But hurry up!"
    hide expression "bk3/toph/assmassage/fluid_skin.png"
    show toam toam10
    with dissolve
    y "Here I go!"
    show toam toam11
    t "Ooh!"
    show ctc
    pause
    hide ctc
    t "i can't believe I'm having a penis rub me down... there... in a public place!"
    t "I can't believe we're doing this!!"
    show toam toam12
    t "Fuuucckk... this feels a lot better than I imagined!"
    show ctc
    pause
    hide ctc
    show toam toam13
    y "I'll go a bit faster so I can finish this before Suki returns."
    t "Go ahead!!"
    show ctc
    pause
    hide ctc
    y "Hnnnngh... i'm getting super close to coming...."
    t "Cum on my ass!!"
    t "Don't leave any evidence Suki can find!"
    show ctc
    pause
    hide ctc
    play sound "audio/splurt2.ogg"
    show toam toam14
    show expression "bk3/toph/assmassage/sperm1.png"
    with flash
    $ renpy.pause()
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/assmassage/sperm2.png"
    with flash
    $ renpy.pause()
    play sound "audio/splurt1.ogg"
    show expression "bk3/toph/assmassage/sperm3.png"
    with flash
    $ renpy.pause()
    show toam toam09
    t "that felt so good!"
    t "my legs are shaking."
    show ctc
    pause
    hide ctc
    y "yeah, i'm honestly kind of stunned that this just happened so quickl-"
    t "suki!"
    t "I think Suki's coming back!"
    t "Quick! Act normal!"
    y "....uhh...."
    t "You're right... don't act normal!"
    t "Act like someone who knows shame!"
    hide expression "bk3/toph/assmassage/sperm1.png"
    hide expression "bk3/toph/assmassage/sperm2.png"
    hide expression "bk3/toph/assmassage/sperm3.png"
    show toam toam02
    show expression "bk3/toph/assmassage/shotcumstain2.png"
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    suki "Here's a little something I wanted to give to you, Toph."
    show expression "bk3/toph/assmassage/small_box.png" with Dissolve(1.5)
    suki "You might..."
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    "Suki glances towards you."
    suki "...need it in the future."
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    "she gives toph a small box while whispering something in her ear."
    hide expression "bk3/toph/assmassage/small_box.png" with Dissolve(1.5)
    show toam toam16
    t "Oh wow, that's really thoughtful, but I don't think I'll need... well, maybe..."
    suki "It's just to give you the option."
    t "Thank you very much."
    show toam toam01
    show tonf tonf17
    t "I'll go home now, Aang."
    t "I have something to think about."
    suki "what's that on your-"
    t "bye!"
    hide tonf
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    hide expression "bk3/toph/assmassage/shotcumstain2.png"
    with dissolve
    y "Sooooo... what exactly did you give her?"
    suki "It's a secret between us girls, Aang."
    suki "Don't worry about it."
    jump love_bk3_village_background

label toph_ass_massage2:
    hide screen earth_money_date

    scene black
    show expression "bk3/toph/assmassage/background.jpg"

    show toam toam01
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    with fade
    suki "oh, hey."
    suki "what are you guys doing here?"
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    show toam toam02 with Dissolve(1.5)
    t "we just thought it'd be fun to-"
    y "to come. here."
    suki "oh. cool."
    suki "i don't know how much free time i have to chat, though..."
    suki "there's a lot to do."
    show toam toam03
    t "oh, don't worry, we're not here to be in your w-"
    show toam toam04
    t "-ay!!"
    suki "What is it Toph?"
    show toam toam05
    t "Hahaha... nothing nothing at all."
    t "Just... remembered something."
    show toam toam06
    "You start rubbing while the girls resume their conversation."
    t "so h-how... are y-you?"
    show ctc
    pause
    hide ctc
    show toam toam07
    t "{size=-6}hungh..."
    suki "You certain you're alright, Toph?"
    show ctc
    pause
    hide ctc
    "you grip and squeeze toph's firm little ass cheeks."
    "they tense and release as you knead them."
    "you can feel the edges of her pussy lips as you pull her small, giving buttocks apart."
    "your thumb occasionally presses against her tight, tiny anus... tensing her up as she squeezes your fingers."
    t "Yeah... ev-everything is... arright."
    show toam toam08
    suki "hey, do you mind waiting here for a moment?"
    suki "I'll be back in a minute or five."
    t "Suuuure... take your time."
    show toam toam15 with Dissolve(1.5)
    hide toam
    show tonf tonf16
    with dissolve
    t "Aang!!"
    t "give me some warning next time!"
    y "why?"
    ym "did you get too wet?"
    show tonf tonf17
    t "just..."
    t "we only have a few minutes!"
    t "so get to it!"

    hide tonf
    show toam toam09
    show expression "bk3/toph/assmassage/fluid_skin.png"
    with Dissolve(1.5)
    t "rub your cock on me!"
    t "i want to feel it in my ass...."
    y "That sounds-"
    t "shut up!"
    t "hurry!"
    hide expression "bk3/toph/assmassage/fluid_skin.png"
    show toam toam10
    with dissolve
    y "you got it!"
    show toam toam11
    t "Ooh!"
    show ctc
    pause
    hide ctc
    t "mmm... yeah... rub me down..."
    t "right here... right in this public... fucking... bar..."
    t "this is crazy, you know that, right?!"
    show toam toam12
    t "Fuuucckk... this feels even better than last time!"
    show ctc
    pause
    hide ctc
    show toam toam13
    y "I'll go a bit faster so I can finish this before Suki returns."
    t "do it!!"
    show ctc
    pause
    hide ctc
    t "yeah... yeah..."
    t "how's my tight ass? gripping your big shaft?"
    t "you like abusing my soon-to-be cummy buttcheeks?"
    t "getting your fucking load out right here in this bar?"
    t "come on, aang... come on baby..."
    y "Hnnnngh... i'm getting super close to coming...."
    t "yeah! fuck it out!"
    t "Cum all over my ass!!"
    t "Don't leave any evidence Suki can find!"
    show ctc
    pause
    hide ctc
    play sound "audio/splurt2.ogg"
    show toam toam14
    show expression "bk3/toph/assmassage/sperm1.png"
    with flash
    $ renpy.pause()
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/assmassage/sperm2.png"
    with flash
    $ renpy.pause()
    play sound "audio/splurt1.ogg"
    show expression "bk3/toph/assmassage/sperm3.png"
    with flash
    $ renpy.pause()
    show toam toam09
    t "that felt so good!"
    t "my legs are shaking."
    t "you got it all over my little... vagina... too?"
    y "i really did."
    show ctc
    pause
    hide ctc
    y "in fact, maybe we can-"
    t "suki!"
    t "I think Suki's coming back!"
    t "i gotta put my pants back on!"
    hide expression "bk3/toph/assmassage/sperm1.png"
    hide expression "bk3/toph/assmassage/sperm2.png"
    hide expression "bk3/toph/assmassage/sperm3.png"
    show toam toam02
    show expression "bk3/toph/assmassage/shotcumstain2.png"
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    suki "oof, it's nice to sit."
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    suki "you guys seem... flushed."
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    show toam toam16
    t "just... just having a... good time."
    suki "okay..."

    show toam toam01
    show tonf tonf17
    t "I think we should go home, Aang."
    suki "wait, what's that on your butt-"
    t "bye!"
    hide tonf
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    hide expression "bk3/toph/assmassage/shotcumstain2.png"
    with dissolve
    y "i'm... gonna go with her."
    suki "did you guys just-"
    y "see ya!"
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next


label smellerbee_blowjob:
    hide screen earth_money_date
    show tosb tosb51 with Dissolve(1)
    sb "Aang! Over here!"
    show tosb tosb00
    sb "What a coincidence meeting you here!"
    if smellerbee_fountain:
        if smellerbee_debt_gone:
            sb "want a little... alley thank you?"
            menu:
                "get some!":
                    jump smellerbee_blowjob2
                "not now":

                    y "not right now."
                    sb "alright!"
                    sb "let me know if you see jet around, okay?"
                    y "sure."
                    jump love_basingse_day1
        else:
            sb "do you have that 300 coins?"
            menu:
                "Give her the money" if emoney >= 300:
                    $ emoney -= 300
                    "You hand Smellerbee the 300 coins."
                    $ smellerbee_debt_gone = True
                    sb "this is amazing!"
                    sb "....."
                    jump smellerbee_blowjob2
                "not yet":

                    y "I don't have it right know, but I promise you I'll get it together soon."
                    sb "okay, well... i need it soon."
                    sb "i'll be here when you have it."
                    jump love_basingse_day1

    y "Yeah, I was wondering if I'd ever got to see you again."
    y "So did you find that Jet guy yet?"
    sb "I thought I saw him yesterday, but lost him in the crowd."
    y "Bummer."
    y "Oh well... that's at least sort of good news right?"
    y "I'm sure you'll find him again soon enough."
    sb "Yeah..."
    y "I feel a \"but\"."
    sb "No, it's just that... I've been spending all time looking and have zero money left."
    sb "I found a job which will get me a lot of money in a short time, though."
    sb "I'm on my way there now."
    y "Soooo.... what kind of job?"
    sb "I'm going to a shoot for... pornlove."
    menu:
        "That's a great idea (approval)":
            y "I love that magazine."
            y "I'll definitely get five copies with you in it."
            sb "Haha... ha... yeah, I'm happy you don't think it's weird."
            y "Promise me you'll sign my copies!"
            sb "Sure thing."
            sb "Well, I don't want to be late, so I guess I'll go now."
            y "Okay, I got some stuff to do too."
            y "see ya!"
            sb "Bye, Aang..."
            $ smellerbee_gone = True
            jump love_basingse_day1
        "uhhhh... for real? (dissuade her)":

            y "Look, it's none of my business, but... are you sure about that?"
            sb "I don't have much choice."
            sb "A normal job leaves me with no time to keep looking for Jet."
            sb "It's just this one time."
            y "How much coin would you need to not have to do this?"
            sb "I'm afraid I built up a debt with some people... so quite a bit... 300 coins."


    menu:
        "Give her the money" if emoney >= 300:
            $ emoney -= 300
            "You hand Smellerbee the 300 coins."
            $ smellerbee_debt_gone = True

        "Say you'll take care of the money" if emoney < 300:
            y "I don't have it right know, but I promise you I'll get it together soon."
            y "So don't do anything you might regret later."
        "Don't give her the money":

            y "I wish I could help you out, but that's quite the sum."
            sb "Don't worry, lots of people do this."
            sb "It won't be my most pleasant experience, but my money problems will be over."
            sb "Well, I don't want to be late, so I guess I'll go now."
            sb "Bye, Aang..."
            $ smellerbee_gone = True
            jump love_basingse_day1

    show tosb tosb53 with hpunch
    sb "seriously?! Just like that? I don't know what to say....."
    show tosb tosb52
    sb "Thanks Aang... but I can't just let you do this."
    y "I'm the avatar, I can do anything. "
    sb "This is quite a lot of money... are you sure? I mean really sure?"
    y "i've never been so sure about anything in my life."
    sb "Thank you... Thank you so much..."
    sb "........"
    jump smellerbee_blowjob2

label smellerbee_blowjob2:
    sb "Come with me for a moment."
    "The girl pulls you into a nearby alley."
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    hide tosb


    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg"

    show tosb tosb01 with Dissolve(1.5)

    if not smellerbee_fountain:
        y "ehm... what're you doing?"
        sb "I want to do something for you Aang, to show my gratitude and I won't take no for an answer."
        y "What do you have in mind?"

    sb "Show me your penis."
    y "okay..."
    show tosb tosb02
    sb "It looks... big..."
    y "Wanna stop?"
    sb "No way."
    show tosb tosb06
    sb "*Sniff* *sniff*"
    show tosb tosb02
    sb "It has a funny smell."
    sb "Not bad, just particular."
    show tosb tosb03
    sb "I'm going to start with a... with a handjob."
    if not smellerbee_fountain:
        sb "That's when you hold it like this..."
        sb "...and start sliding your hand up and down while holding it firmly..."
        sb "...right?"
        y "Eh... yes."
    show tosb tosb04
    sb "Pretty easy."
    sb "Does this feel good?"
    y "Yeah... it's really nice."
    show tosb tosb05
    sb "I'm getting the hang of this."
    $ smellerbee_fountain = True
    menu:
        "cum on her face":
            y "I'm about to cum!"
            sb "O-okay... aim for my mouth so I can keep my clothes clean."
            show expression "bk3/smellerbee/bj/openmouth.png"
            sb "Go ahead."
            play sound "audio/splurt2.ogg"
            show expression "bk3/smellerbee/bj/sperm1.png"
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/smellerbee/bj/sperm2.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/smellerbee/bj/sperm3.png"
            show tosb tosb03
            y "Ah fuck. that was great."
            show ctc
            pause
            hide ctc
            show expression "bk3/smellerbee/bj/sperm4.png"
            hide expression "bk3/smellerbee/bj/sperm3.png"
            hide expression "bk3/smellerbee/bj/sperm2.png"
            hide expression "bk3/smellerbee/bj/sperm1.png"
            hide expression "bk3/smellerbee/bj/openmouth.png"
            play sound "audio/gulp2.mp3"
            sb "*gulp*"
            sb "That was a bit more than I expected."
            y "You didn't have to swallow it, you know."
            sb "I... guess I just wanted to taste it."
            sb "It's not as bad as I heard."
            hide expression "bk3/smellerbee/bj/sperm4.png"
            show tosb tosb00 with Dissolve(1.5)
            if smellerbee_debt_gone == True:
                show tosb tosb50
                sb "If you want to do this again sometimes come and look me up."
                sb "See you later, Aang!"
                hide tosb tosb00
            else:
                sb "If you can bring me that 300 gold we might be able to do this again soon."
                sb "See you later, Aang!"
                hide tosb tosb00
            show ctc
            pause
            hide ctc
            jump love_basingse_day1
        "suppress cumming":
            pass

    show tosb tosb03
    sb "This really doesn't feel like enough."
    sb "Can't I do something more?"
    y "Well, I guess there's one thing which I'd like more..."
    if not smellerbee_fountain:
        y "....and can be done just as fast, right here and now."
        sb "What is it?"
    y "Just doing the same, but with your mouth."
    if not smellerbee_fountain:
        sb "That's a bit..."
        y "But just your hand is plenty fine too."
        sb "No, I really want it to be something you're happy with!"
        sb "...and I'd be doing a lot worse without you, now."
    sb "If my mouth is what it'll take, then that's what I'll do."
    show tosb tosb10
    "Just pushing the tip against her lips feels fantastic."
    y "You can start whenever you feel like it."
    y "Start with the tip."
    y "You can go deeper when you feel comfortable doing so."
    show tosb tosb100
    sb "*sluurp* *gulp*"
    show ctc
    pause
    hide ctc
    y "This is awesome... I'm very happy you're willing to do this for me."
    show tosb tosb101
    if not smellerbee_fountain:
        y "Oh wow, didn't expect you to be able to go this deep so soon."
    else:
        y "you can really... ugh... go deep..."
    sb "*gltch* *mghg* *gag*"
    show ctc
    pause
    hide ctc
    show tosb tosb102
    y "I'm getting very close to cumming...."
    y "Here it comes!"
    sb "go ahead!"
    sb "cum in my mouth when you're ready."
    play sound "audio/splurt2.ogg"
    show tosb tosb16
    with flash
    play sound "audio/splurt3.ogg"
    with flash
    show tosb tosb17
    play sound "audio/splurt1.ogg"
    with flash


    sb "I managed to swallow most of it, but that was a big load!"
    show tosb tosb00 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    if smellerbee_debt_gone == True:
        sb "If you want to do this again sometimes, come and look me up."
        show tosb tosb50
        sb "See you later, Aang!"
        hide tosb tosb00
    else:
        sb "If you can bring me that 300 gold we might be able to do this again soon."
        show tosb tosb50
        sb "See you later, Aang!"
        hide tosb tosb00
    show ctc
    pause
    hide ctc
    jump love_basingse_day1

label basingse_home_clue_screen:
    call screen basingse_home_clue_screen2

label bk3_home_curtain_clue:
    y "This is a curtain, there obviously isn't going to be-"
    y "huh."
    y "would you look at that."
    y "a fucking note."
    show bk3_scroll
    show text "they know i'm... not right. they're coming for me.\ni don't know where they'll take me.\ni'm afraid.\navatar, if you read this... please...\nfind me.\n\njoo dee"
    show ctc
    pause
    hide ctc
    jump jd_clue_menu

    label jd_clue_menu:
        menu:
            "keep reading":
                show ctc
                pause
                hide ctc
                jump jd_clue_menu
            "continue":
                pass
        hide bk3_scroll
        hide text
        ya "...shit."
        ya "shit, shit, shit!!"
        ya "this is my fault."
        ya "i tried to break her hypnosis, and they must have found out."
        y "i just... have no idea where to look."
        y "I guess i'll have to... see if any opportunities present themselves."
        ya "...starting with that guard outside."
        scene black
        scene basingse_home_1
        with dissolve
        y "where are you, guard..."
        y "....."
        y "Is he still not back yet?"
        menu:
            "wait":
                y "i'll talk to that fucking guard if I have to wait all day."
                "........."
                "................."
                "..........................."
                show blackveil with Dissolve(3)
                "...................................."
                ".............................................."
                "........................................................"
                scene black with Dissolve(3)
                "........................................................"
                ".............................................."
                "...................................."
                scene basingse_home_1
                show blackveil
                with Dissolve(3)
                "..........................."
                "................."
                "........."
                hide blackveil with Dissolve(3)
                y "..........."
                ya "what the hell?!"
                ya "i didn't literally mean i'd wait all day."
                ya "where is he?"
                ya "did he abandon his post?"
                ya "is he just fucking done?"
                y "i can't wait here any more."
                y "I'm going home."
                jump love_bk3_next
            "leave":

                jump love_basingse_day1


label bk3_home_cushion_clue1:
    y "nothing here, just a cushion."
    y "...it's a {i}nice{/i} cushion, though."
    if not bk3_cushion1_coins:
        y "oh, hold on..."
        $ emoney +=50
        play sound "audio/money.mp3"
        "you found 50 coins!"
        y "sweet!"
        $ bk3_cushion1_coins = True
    jump basingse_home_clue_screen

label bk3_home_cushion_clue2:
    y "a clue!"
    y "wait, no, that's just the floor."
    if not bk3_cushion2_coins:
        y "oh, hold on..."
        $ emoney +=75
        play sound "audio/money.mp3"
        "you found 25 coins!"
        y "sweet!"
        $ bk3_cushion2_coins = True
    jump basingse_home_clue_screen

label bk3_home_rug_clue:
    y "this is a rug."
    y "it's very exciting."
    y "i'll look underneath, and...."
    y "....ants."
    y "not really what i'm looking for here."
    if not bk3_rug_coins:
        y "wait, what's this?"
        $ emoney +=75
        play sound "audio/money.mp3"
        "you found 75 coins!"
        y "sweet!"
        $ bk3_rug_coins = True
    jump basingse_home_clue_screen

label earth_soldier_follow:
    $ love_jd_hypno = 10
    hide screen earth_money_date
    show toeg toeg01 with dissolve
    dl "oh, hey, it's the big shot avatar."
    y "what the hell are you doing here?"
    dl "what, can't a man enjoy a drink?"
    dl "while looking a pretty girl?"
    dl "and that suki is certainly pretty..."
    dl "it's too bad she left the tunnels before i had a chance to-"
    y "get out. now."
    dl "oh, did i hit a sore spot?"
    dl "i bet you don't want to think about me balls deep in that girl over there, huh?"
    dl "it's too bad you messed her up before i could at least fuck her tits."
    dl "you really ruined her..."
    ya "i'm gonna ruin you."
    dl "...but not as bad as you ruined joo dee."
    dl "she's in a truly awful state now, thanks to you."
    y "what? what do you mean?"
    y "where's joo dee?"
    dl "sorry, state secrets and all that."
    dl "but i will tell you... it's a very sad fate that you've forced on her."
    dl "you're truly heartless."
    ya "tell me or i beat you to shit, right here."
    dl "you might be able to do that... maybe..."
    dl "but if i don't report back to my station soon... unharmed..."
    dl "well... something terrible will happen to her."
    dl "and i know you don't want that."
    ya "...why would something bad happen to her?"
    dl "well... you're known to be protective of your whores..."
    dl "...for some reason..."
    dl "so consider it... leverage."
    y "leverage?"
    dl "is the word to big for you?"
    dl "let me make it simpler."
    dl "the grand secretariat is tired of your forays into the tunnels beneath lake laogai."
    dl "you will stop that immediately..."
    dl "...or joo dee will suffer."
    ya "is that why you came here?"
    ya "to deliver this fucking message, you coward?"
    dl "coward?"
    dl "go ahead and hit me, avatar."
    dl "see what happens to your precious whore, joo dee."
    menu:
        "hit him":
            play sound "audio/thud.mp3"
            with hpunch
            hide toeg with moveoutbottom
            dl "ugh...!"
            "you hit him in the stomach and he crumples to the floor."
            $ dai_lee_hit = True
            dl "...fuck..."
            ya "be careful what you wish for, dick."
            show toeg toeg01 with moveinbottom
            dl "you fucking idiot..."
            dl "i'm gonna see to it that joo dee has a rough fucking night, you hear me?!"
            dl "not the worst night she could have... we'll save that as leverage..."
            dl "but tonight's not gonna be easy for her."
            dl "touch me again, and she'll regret it."
            dl "i'll see to it personally."
            ya "so you know where she is."
            dl "maybe."
            ya "......"
            dl "now get out of my way."
            ya "......"
            hide toeg with dissolve
            "you move aside as the dai lee agent stumbles out of the tavern, holding his stomach."
        "be patient":

            y "....i fucking hate you."
            dl "and isn't that the sweetest music of all?"
            ya "tell me where she is."
            dl "maybe i don't know?"
            ya "you do know."
            dl "that's tough to prove."
            dl "and there's nothing you could about it, even if i did know."
            ya "i could keep you here and follow the messenger to where joo dee is."
            dl "you don't even know where to start."
            dl "what messenger?"
            dl "we have ways of sending messages that don't require messengers."
            ya "maybe i just kill you and forget about joo dee."
            dl "maybe..."
            dl "...but that doesn't seem like your style."
            dl "so you're going to let me go."
            dl "because there's nothing else you can do."
            ya "....let her go."
            ya "let her go and i won't go into the tunnels any more."
            dl "oh, no... she's our leverage."
            dl "but i can promise she won't face a worse fate... if you keep your end of the bargain."
            dl "see you around, avatar."
            dl "try not to ruin any more lives, like you did to poor joo dee."
            dl "byeee...."
            hide toeg with dissolve
    y "....."
    y "that asshole knows where she is."
    y "i'm sorry i put you in this position joo dee... but i swear i'll find you."
    y "...and i'll start by following this fucker."
    scene black with dissolve
    "you hang back as the dai lee agent walks away."
    "keeping him in your sights, you dog his steps and watch where he goes."
    scene black
    scene expression "bk3/toph/party/bg_alley_epalace.jpg"
    show toeg toeg01
    show guardb_body_1:
        xpos -500
    with dissolve
    "he eventually winds his way to the palace, where he meets a large group of guards."
    dl2 "welcome back."
    dl2 "have fun?"
    if dai_lee_hit:
        dl1 "not... really."
    else:
        dl1 "i did, yeah."
    dl1 "the avatar was pissed."
    dl2 "yeah, no shit."
    dl2 "i can't believe he didn't punch you."
    if dai_lee_hit:
        dl1 "...he fucking did."
        dl2 "bummer. i can't imagine that was fun."
        dl1 "it wasn't."
        dl1 "asshole's got an arm like a fucking cannon."
    else:
        dl1 "he knew better."
        dl1 "he didn't want to risk his precious joo dee."
    dl2 "ha! i'm still impressed you were brave enough to volunteer."
    dl1 "pfft. i didn't have to be brave at all."
    dl1 "he's a weak little coward."
    dl1 "no risk at all."
    if dai_lee_hit:
        dl1 "...other than that one cheap shot."
    dl2 "you think he got the message?"
    dl2 "or are you gonna go back?"
    dl1 "no, he got the message."
    dl1 "and he may be a chickenshit, but any man has a breaking point."
    dl1 "i'm not an idiot... i'll stay here where he can't pick us off."
    dl2 "so he's properly enticed?"
    dl1 "yeah... he'll either stay out of the tunnels, which is a win for us..."
    dl1 "or he'll be stupid enough to come after me... and we'll capture him."
    dl2 "you think that's really a possibility?"
    dl1 "sure."
    dl1 "especially since he now knows that i know where that slut is."
    dl1 "i wasn't particularly coy about that."
    dl2 "right... so if he gets frustrated enough, he'll eventually show up..."
    dl1 "and we'll get that fucker."
    dl1 "long feng will be {i}very{/i} happy, either way."
    dl1 "we might even get some holiday handjobs from the girl guards in the tunnels."
    dl2 "really? handjobs?"
    dl2 "what are you, twelve?"
    dl1 "it's a legitimate way to get off!"
    dl2 "is it, though?"
    dl1 "fuck you, jim."
    if dai_lee_hit:
        dl1 "ugh... i think i'm gonna throw up."
        dl1 "or crap."
        dl1 "he practically punched through my colon."
        dl2 "...gross."
        dl2 "do it over there."
    y "(...fuck.)"
    y "(there's too many here.)"
    y "(and they're obviously laying a trap for me.)"
    y "(fuck. fuck fuck fuck.)"
    y "(i need help.)"
    y "(i'm coming for you, joo dee.)"
    y "(hold on, wherever you are.)"
    $ bk3_day = False
    scene black with dissolve
    "tired, you head home for the night."
    jump love_bk3_next

label katara_jd_advice:
    y "katara, i need your help."
    show toki toki02 with dissolve
    k3 "what is it?"
    y "i need a plan."
    k3 "okay...."
    k3 "tell me more."
    show black with dissolve
    "you explain to katara what's going on with joo dee...."
    hide black
    show toki_angry
    with dissolve
    k3 "that... is not good."
    k3 "i don't know her very well, but no one deserves that fate."
    y "what should i do?"
    show toki_blink with dissolve
    k3 "i think..."
    k3 "this is going to have to come down to a fight."
    y "that's fine."
    ya "i've got some pent up aggression."
    hide toki_blink with dissolve
    k3 "you'll have to take them all down at once, and capture the main one."
    y "i don't know if i can do that myself..."
    k3 "you can't, you'll need help."
    y "great, i'll grab toph and-"
    k3 "you... can't."
    y "...what?"
    k3 "toph's not here."
    y "....."
    y "where is she?"
    hide toki_angry
    show toki toki01
    with dissolve
    k3 "i don't know."
    k3 "she told me she was seeing to a personal matter."
    k3 "she seemed really worried, but wouldn't let me go with her."
    y "i hope she's okay."
    k3 "me too."
    y "so what should i do?"
    k3 "i have an idea, but..."
    y "but what?"
    show toki toki02
    show toki_blink
    with dissolve
    k3 "you're not going to like it."
    y "try me."
    hide toki_blink with dissolve
    k3 "the rift between ty lee and suki is becoming a real issue."
    k3 "they're avoiding each other's residences, but when they meet in the street, it's hard to keep them from fighting."
    y "ughh... please don't say what i think you're about to say."
    k3 "you need to get them to work together, and you need their help."
    k3 "it's a win-win."
    y "i really don't want to get involved between them."
    k3 "well, you're going to have to get involved."
    k3 "unless you want this village to end up accidentally burning down one night."
    y "i don't want to go through that again."
    show toki_blink with dissolve
    k3 "me neither."
    y "....aw, shit."
    y "fine, i'll try to get them to work together."
    y "but i'm not happy about it."
    hide toki_blink with dissolve
    k3 "good luck."
    y "thanks, i'm gonna need it."
    jump love_bk3_village_background

label suki_ty_dai_battle:
    hide screen earth_money_date
    show black with dissolve
    "you find suki and ty lee hiding nearby."
    hide black
    show tfa
    show tosi tosi10:
        xzoom -1
    with dissolve
    y "everything okay?"
    suki "we're fine, there's a mission at stake."
    suki "we're just not talking."
    ty "other than you insulting me!"
    y "okay, okay."
    y "get your game faces on, girls."
    y "ty lee, what's the best way to take them out?"
    hide tfa
    show tf
    with dissolve
    ty "we should-"
    suki "aang, do you really trust this slu... ty lee?"
    menu:
        "i trust her":
            y "absolutely."
            y "she's been cast out, and she's willing to help."
            y "i'm going to assume she's trustworthy until proven otherwise."
            ty "aww... thanks, aang!"
            ty "i won't let you down!"
        "for now":

            y "i trust her for this."
            y "but i'll keep an eye on her."
            hide tf
            show tfa
            with dissolve
            ty "that's... really mean."
            ty "i haven't done anything to keep you from trusting me."
            y "other than attacking us?"
            ty "but... but..."
            y "come on, focus."
            ty "....."
            ty "fine."

    ty "okay, the best way is...."
    scene black with dissolve
    "ty lee shares the best angle to attack and the three of you organize an attack strategy."
    "you sneak up on the guards."
    scene black
    scene expression "bk3/toph/party/bg_alley_epalace.jpg"
    show toeg toeg01
    show guardb_body_1:
        xpos -500
    with dissolve
    y "okay, it looks like there's five of them."
    y "everybody ready?"
    ty "let's do this."
    suki "on my mark..."
    suki "get set..."
    suki "{size=+6}go!"
    scene black with dissolve
    "the three of you take the five soldiers by surprise, and gain a valuable few seconds to attack before the dai lee can adjust."
    ty "hi-yah!"
    "ty lee somersaults into a flying kick, hitting the first soldier's helmet so hard it spins, knocking him out."
    play sound "audio/thud.mp3"
    dl "{i}oof."
    "suki follows close behind, dealing a devastating flurry of quick blows to a soldier's gut."
    suki "ah... ha!"
    play sound "audio/thud.mp3"
    dl "{i}fuck!"
    "you pull the feet out from the leader guard during suki's attack, knocking him onto his back and unresponsive."
    y "i'm coming back for you, dick."
    "you turn back to the other dai lee."
    "the remaining two soldiers stand side by side, uncertain, but in an earthbending stance."
    y "you girls take the right one, i've got the left."
    ty "got it!"
    "ty lee slides under the guard of the right one as suki launches herself over his head."
    dl "{i}what the-"
    "you turn your head to the left dai lee agent just in time to see a hardened block of earth barreling towards you."





    menu:
        "do nothing":
            jump dl_slow1
        "do nothing":
            jump dl_slow1
        "do nothing":
            jump dl_slow1
        "spin kick":

            "ducking and spinning, you kick it aside and return to form, shaking your head."
            jump dl_choice1
        "do nothing":
            jump dl_slow1

label dl_slow1:

    $ renpy.block_rollback()
    "it slams you into the chest and sends you reeling, knocking the breath out of you."
    "you roll back on your feet and lift yourself up painfully, rubbing your chest."
    "he gives you a big, vicious smile."
    dl "that all you've got, avatar?"
    "you let loose a small growl."
    y "no even close."
    $ dl_slow_blows +=1
    jump dl_cont1

label dl_choice1:
    $ renpy.block_rollback()
    y "shit, gotta focus."
    y "that was close."
    jump dl_cont1

label dl_cont1:
    $ renpy.block_rollback()




    menu:
        "do nothing":
            jump dl_slow2
        "press him":


            "before he can launch another attack, you send a flurry of icycle-shaped earth spikes his way."
            "you force him to dodge, and he slides to the side, grinning."
            "he turns the spikes into sand, hardens them into little bullets, and forces them towards you once again."
            jump dl_cont2
        "do nothing":
            jump dl_slow2
        "do nothing":
            jump dl_slow2
        "do nothing":
            jump dl_slow2
        "prepare to counter":

            "you and your opponent briefly circle before he launches a flurry of icycle-shaped earth spikes your way."
            "you turn them into sand, harden it into a wall and send it back towards him."
            "he slides to the side, grinning, and breaks the wall into a myriad of little bullets and forces them towards you once again."
            jump dl_cont2

label dl_slow2:

    $ renpy.block_rollback()
    $ dl_slow_blows +=1
    "before you can prepare, he launches a flurry of icycle-shaped earth bullets your way."
    "you manage to dodge most of them, but you recieve a few glancing blows that leave you with a few new cuts."
    y "owww...."
    "the dai lee agent flexes and points at you."
    dl "we're not done yet, shorty."
    jump dl_cont2

label dl_cont2:
    $ renpy.block_rollback()




    menu:
        "do nothing":
            jump dl_slow3
        "do nothing":

            jump dl_slow3
        "do nothing":



            jump dl_slow3
        "do shield":


            "you craft a quick shield, and lift it into the air, blocking the bullets."
            "while you're distracted, he turns the dirt below you into a pit."
            y "shit!"
            jump dl_cont3
        "do launch":


            "you launch yourself into the air as the bullets whiz by."
            "you do a superhero landing, sort of hurting your knees, and he turns the dirt below you into a pit."
            y "shit!"
            jump dl_cont3
        "do nothing":

            jump dl_slow3

label dl_slow3:

    $ renpy.block_rollback()

    "several bullets hit you full on in the stomach, clearly breaking a few ribs."
    "you collapse to the ground, and he turns the dirt below you into a pit."
    jump dl_cont3

label dl_cont3:
    $ renpy.block_rollback()




    menu:
        "sink":

            "in a split second decision, you allow yourself to sink."
            "you travel beneath the ground, waiting until you're underneath him... seeing with your body and not your eyes."
            y "(thanks, toph!)"
            "you launch yourself up from below him, hitting him full-on and sending him flying."
            y "yes!"
            "he rolls in the dirt, clearly in pain."
            "he struggles to stand, falling onto one leg."
            jump dl_choice4
        "do nothing":
            jump dl_slow4
        "do nothing":

            jump dl_slow4
        "do nothing":

            jump dl_slow4
        "do nothing":

            jump dl_slow4
        "do nothing":

            jump dl_slow4
        "harden":


            "you soldify the sinking sandpit around you into a full body shield, and launch yourself toward him."
            "you hit him full-on and send him flying."
            y "yes!"
            "he rolls in the dirt, clearly in pain."
            "he struggles to stand, falling onto one leg."
            jump dl_choice4

label dl_slow4:

    $ renpy.block_rollback()
    $ dl_slow_blows +=1
    "you struggle to breathe as the earth engulfs you."
    "just as you're about to black out, a hand reaches down and pulls you up."
    "you gasp for air and fall onto your hands and knees."
    "you look up just in time to see the soldier launch a single spike of hardened earth your way."
    suki "aang!"
    "suki hits you in the chest and lays you flat as the spike flies overhead."
    "you wait a second and raise your head to see ty lee standing over the soldier's unconscious body."
    jump dl_cont4

label dl_choice4:
    $ renpy.block_rollback()
    y "suck it, dick."
    if dl_slow_blows >=1:
        "you feel a twinge from one of the attacks you took and test to see how serious it is."
        "the soldier launches a single spike of hardened earth your way while you're distracted by your wound."
        suki "aang!"
        "suki hits you in the chest and lays you flat as the spike flies overhead."
        "you wait a second and raise your head to see ty lee standing over the soldier's unconscious body."
        jump dl_cont4
    else:
        "the soldier launches a single spike of hardened earth your way."
        "you force it aside and hit him in the chest with a solid boulder."
        "he breaks it apart, panting, and lifts his leg and arm to send another blow as ty lee hits him with a precise series of hits."
        "she stands over his unconscious body and gives you a sly shrug."
        jump dl_cont4

label dl_cont4:
    $ renpy.block_rollback()
    $ renpy.can_rollback()
    scene black
    scene bg_alley_epalace
    show tf:
        xpos -600
    show tosi tosi10
    with dissolve
    suki "alright, i'll admit it..."
    suki "not bad."
    ty "hee hee."
    suki "that doesn't mean i like y-"
    play sound "audio/thud.mp3"
    show big_rock:
        xpos 600 ypos 250
    with moveinright
    hide tosi
    hide big_rock
    with moveoutleft
    hide tf
    hide tf2
    hide tfa
    show tfa:
        xpos -600
    with dissolve
    suki "{size=+6}ugh!" with vpunch
    y "suki!"
    ty "no!"
    show toeg toeg01 with moveinright
    dl "take... that... bitch..."
    "the leader guard that you'd only pulled the feet out from under appears."
    "before you can process, he pulls out a knife and slams it down towards suki's chest."
    y "no!"
    hide tfa
    hide toeg
    with moveoutright
    "just before the blade makes contact, ty lee kicks the guard, making him fly backwards."
    "a crunching sound as he hits the street tells you he won't be getting up any time soon."
    y "suk... suki!"
    suki "uughh..."
    show tosi tosi10:
        xzoom -1
    with moveinbottom
    y "are you okay?"
    suki "I'm... hurt... I think that rock fractured a rib or two... but i'll live."
    suki "ty lee... she..."
    suki "she stopped the knife..."
    show tfa with dissolve
    ty "are... are you... okay..."
    suki "...thank you."
    ty "no... problem."
    ty "i... i'm not feeling so good."
    hide tfa with moveoutbottom
    y "ty lee?!"
    suki "what the..."
    suki "she's bleeding!"
    suki "that bastard must have somehow stabbed her!"
    ya "we need to get her to katara {i}now{/i}!"
    scene black with dissolve
    "you throw ty lee over your shoulder and sprint back towards the village."
    "you see suki fall behind, clutching her stomach."
    "yelling back at her, you slow down."
    ya "are you okay?!"
    suki "go! i'm fine!"
    suki "get her to katara!"
    ya "got it!"
    "you leave suki behind, returning to a full sprint."
    "......."
    "..................."
    scene inside_hospital
    show toki toki01
    with dissolve
    k3 "welc-"
    show toki toki04
    show toki_angry
    with dissolve
    k3 "ty lee!"
    show toki toki03
    with dissolve
    k3 "get her on the table! now!"
    show black with dissolve
    "after a few scary minutes, ty lee opens her eyes."
    hide black
    show tf:
        xpos -600
    hide toki_angry
    show toki toki02
    with dissolve
    ty "where... what happened...?"
    y "you were stabbed saving our lives."
    ty "i'm... rusty... then..."
    y "no, you're amazing."
    y "get some rest."
    hide tf with dissolve
    k3 "she'll need some time to recover, but the worst has passed."
    y "i still can't believe it."
    k3 "hey...."
    show toki_angry with dissolve
    k3 "where's suki?"
    ya "oh, shit!"
    k3 "and weren't you supposed to bring back a captive guard?"
    ya "shit, shit, shit!!"
    ya "i have to get back to the city!"
    scene black with dissolve
    $ bk3_day = False
    jump love_basingse_night1


label dl_capture:
    ya "suki?!"
    iroh "...well that was loud."
    ya "is she here?"
    show toii toii03 with dissolve
    iroh "who?"
    ya "don't fuck with me right now, old man!"
    show toii toii01 with dissolve
    iroh "....."
    show toii toii06 with dissolve
    iroh "okay, rude..."
    suki "....aang....?"
    ya "suki!"
    show toii toii01 with dissolve
    iroh "oh, her."
    iroh "yes, she's here."
    iroh "and she dragged a body in with her."
    show toii toii06 with dissolve
    iroh "not my usual crowd, but then again we're empty, so..."
    y "she brought a body?"
    show toii toii01 with dissolve
    iroh "a dai lee agent if i'm not mistaken."
    iroh "very risky, but i'm always a sucker for a pretty girl."
    show tosi tosi10:
        xzoom -1
    with dissolve
    suki "aang?"
    y "are you okay?!"
    y "what happened?!"
    suki "I'm fine, just... bruised."
    suki "i think i have a couple broken ribs."
    if dl_slow_blows >=1:
        y "i have some wounds katara's gonna have to tend to as well."
    y "i'm gonna ask again: what happened?"
    suki "well, i realized that we forgot to grab that damn guard."
    suki "so i went back for him."
    suki "i couldn't drag him far, and the lights were on here, so..."
    suki "i decided to risk it."
    suki "the old man is nice, but he keeps looking at my rear when he thinks i'm not looking."
    show toii toii03 with dissolve
    iroh "*cough*"
    suki "what do you want to do, aang?"
    menu:
        "interrogate him here":
            y "we need to get the information out of him as soon as possible."
            y "is he conscious?"
            suki "not yet."
            show toii toii02 with dissolve
            iroh "um."
            y "what?"
            show toii toii01 with dissolve
            iroh "i really don't think you should question him here."
            suki "and why not?"
            iroh "because i'm sure the dai lee will be swarming the city looking for him - and you - any minute now."
            y "that's... fair."
            iroh "and... i don't want to be {i}that{/i} guy, but..."
            iroh "it's my shop and i don't want it corpse-y."
            iroh "or full of angry soldiers."
            suki "okay, that's reasonable too."
            y "we're not gonna make him a corpse."
            y "probably."
            iroh "still..."
            y "alright, we'll take him back to the village."
        "take him back to the village":

            y "the dai lee will be looking for him - and us - any minute now."
            y "we should get him out of here and back to the village."
            show toii toii01 with dissolve
            iroh "good plan."

    show toii toii03 with dissolve
    y "but first..."
    y "iroh?"
    iroh "hmm?"
    y "do you have any rope?"
    show toii toii07 with dissolve
    iroh "why....?"
    scene black with Dissolve(1)
    scene basingse_home_4
    show guard_rope1:
        rotate 90
        ypos -600 xpos -300
    with Dissolve(1.0)
    dl "........"
    dl "...where am i?"
    y "on the floor, you dick."
    dl "i am?"
    y "yeah, and you're coming with us."
    dl "...i am?"
    hide guard_rope1
    show guard_rope1:
        rotate 90
        ypos -600 xpos -300
        linear 15 xpos -1000
    dl "...i guess i am."
    dl "........"
    dl "this is humiliating."
    y "shut up, you."
    dl "*sigh...*"
    stop music
    scene black with Dissolve(1)
    "you drag/carry the dai lee agent back to the village, with suki walking slowly just behind you."
    scene inside_hospital
    show toki toki02
    show toki_smile
    show tosi tosi10:
        xzoom -1
    with dissolve
    k3 "suki!"
    hide toki_smile
    show toki_angry
    with dissolve
    k3 "are you okay?"
    k3 "...and who's this guy with the hat?"
    suki "i'm... fine..."
    y "she's not."
    y "and i'm not."
    y "and this is the guy that knows where joo dee is."
    play sound "audio/thud.mp3"
    with hpunch
    "you drop the soldier onto the floor unceremoniously."
    dl "....ow."
    y "shut it."
    y "katara, heal suki."
    if dl_slow_blows >=1:
        y "i could use some healing, too."
        y "...but it can wait."
        y "her first."
    else:
        y "i got through without much damage, so i'm fine."
        y "but she needs some care."
    y "please."
    hide toki_angry with dissolve
    k3 "i'll take care of it."
    k3 "good thing we have such a large hospital, huh?"
    y "...i guess."
    k3 "come on, suki."
    k3 "ty lee's in one bed, but we have extra space now."
    suki "okay..."
    hide tosi with dissolve
    y "thanks, katara."
    k3 "don't mention it."
    y "i'm going to deal with this asshole."
    dl "hey..."
    k3 "break a leg."
    y "i just might."
    dl "um."
    hide toki with dissolve
    y "alright, you."
    scene black with dissolve
    "you drag the dai lee soldier into a back room."
    scene inside_brothel_2
    show guard_rope1:
        xpos -350
    with dissolve
    with vshake
    dl "oof."
    dl "hello."
    y "tell me about joo dee."
    dl "jokes on you, i've got you right where i want you."
    show guardb_body_1:
        xpos -300 ypos 10
    show guard_rope:
        xpos -350 ypos 10
    hide guard_rope1
    with hpunch
    dl "hhrghh...."
    hide guardb_body_1
    hide guard_rope
    show guard_rope1:
        xpos -350
    with dissolve
    dl "okay, maybe not {i}right{/i} where i want you... but basically."
    y "......."
    y "...you sure?"
    dl "yeah, just....."
    show guardb_body_1:
        xpos -300 ypos 10
    show guard_rope:
        xpos -350 ypos 10
    hide guard_rope1
    with hpunch
    dl "arrrghh...."
    hide guardb_body_1
    hide guard_rope
    show guard_rope1:
        xpos -350
    with dissolve
    dl "ugh."
    dl "okay, you got me."
    y "maybe this will help..."
    play sound "audio/thud.mp3"
    show black
    with hpunch
    "you hit him in the face."
    hide black with dissolve
    dl "ow!"
    dl "hey!"
    dl "why?!"
    y "fuck you."
    y "tell me where joo dee is."
    dl "i... can't."
    y "don't give me that."
    y "where is she?"
    dl "if i tell you, long feng will-"
    play sound "audio/thud.mp3"
    show black
    with hpunch
    "you hit him in the face again."
    hide black with dissolve
    dl "ow! fuck!"
    dl "stop that!"
    y "stop not telling me where joo dee is."
    dl "...fine!"
    dl "she's in the tunnels...."
    y "obviously."
    dl "in the northeast section."
    dl "behind a hidden wall."
    y "........."
    dl "dude, you're never gonna find her."
    y "any chance you have a map?"
    dl "well...."
    dl "no?"
    y "......."
    play sound "audio/thud.mp3"
    show black
    with hpunch
    "you hit him in the face once again."
    hide black with dissolve
    dl "agh!"
    dl "fuck!"
    dl "yes, damn it!"
    dl "there is a map!"
    y "great!"
    y "where?"
    dl "it's not official."
    y "go on..."
    dl "i kept getting lost so i made a map."
    y "okay..."
    dl "and... well... i lost it."
    y "you lost it?"
    dl "i lost it in a game of pocket crabs."
    y "seriously?"
    dl "i was out of money!"
    dl "look, there's this guy... he deals in information."
    dl "...and crabs."
    dl "he has it."
    dl "he's pretty shady though."
    y "....i think i know who you mean."
    dl "well, he's got my map."
    y "great. just great."
    dl "can i go now?"
    y "no you can't fucking go!"
    y "i'm putting you in a closet."
    "you check his pockets."
    dl "what are you doing?"
    y "i'm mad at you."
    play sound "audio/money.mp3"
    $ emoney += 150
    "you found 150 coins."
    y "oh, shit! that's awesome!"
    dl "hey, that's mine..."
    y "not any more."
    y "now it's closet time."
    dl "no! wait! don't-"
    hide guard_rope1 with hpunch
    "you shove the dai lee soldier into a closet."
    "he lets out a muffled yell, but you ignore it."
    scene black
    scene inside_hospital
    with dissolve
    y "katara?"
    show toki toki02
    with dissolve
    k3 "yeah?"
    if dl_slow_blows >=1:
        y "think you can heal me really quickly?"
        k3 "sure."
        show black with dissolve
        "katara heals you with gentle waterbending."
        hide black with dissolve
        k3 "there you go."
        y "thanks."
    y "i need to go get a map from a dude."
    y "...after i get some sleep."
    y "can you keep an eye on the girls?"
    k3 "of course."
    y "you're the best."
    k3 "i know."
    scene black with dissolve
    "you head home for the night."
    $ suki_tylee = 6
    jump love_bk3_next


label suki_lovefuck:




    $ totn_head = 'face'
    $ totn_fuck = 'rub'
    stop music
    play music "audio/Unwritten Return.mp3"
    scene black with dissolve
    scene expression "bk3/june/blowjob/inside_tavern_2.jpg"
    show totn totn03
    with Dissolve(1.5)

    "suki strips and crawls on you, pressing her tits firmly against your chest."
    suki "want me to tease you a bit?"
    suki "or do you want me to be your cock-sleeve right from the start?"


    menu:
        "tease me":
            y "tease me first."
            y "i want to feel you rub against me."
            y "give me an appetizer, girl."
            suki "yes sir...."
            $ totn_fuck = 'rub'
            show totn totn100
            $ totn_head = 'face'
            suki "*mmm...*"
            show ctc
            pause
            hide ctc
            suki "this feels really nice."
            suki "Having your stiff rod slide between my buttcheeks..."
            suki "Can you feel the softness of my pussy lips?"
            y "It's super soft.."
            suki "your precum's getting me going..."
            suki "I'm making your dick all wet from my pussy juice."
            suki "How long do you think you could stand me teasing you like this without cumming?"
            suki "Two minutes?"
            suki "Perhaps five?"
            y "we could... ah... we could test it..."
            suki "we could..."
            $ totn_head = 'back'
            suki "But that's not what you want...."
            show ctc
            pause
            hide ctc
            suki "Playing like this is nice but what you really want..."
            suki "...is to ram my little pussy with your cock, isn't it?"
            suki "*mmh...*"
            suki "imagine how your dick, wet with my love juice, slips inside all the way at the first go."
            suki "Going far deeper than your fingers could..."
            suki "you think we can get it all the way in with one thrust?"
            $ totn_head = 'face'
            suki "*Mmmmm...*"
            show ctc
            pause
            hide ctc
            suki "I can feel it throbbing... eager with anticipation..."
            suki "Enough foreplay."
            suki "Time to put it in."
        "sleeve":

            pass


    show totn totn03
    suki "aiming..."
    show ctc
    pause
    hide ctc
    show totn totn02 with Dissolve(1.5)
    suki "connecting..."
    suki "{size=-5}oh, fuck...."
    show ctc
    pause
    hide ctc
    $ totn_fuck = 'penetrate'
    show totn totn03 with dissolve
    suki "nice and secure..."
    show totn totn03
    suki "Oh... {i}fuck{/i} yes."
    show ctc
    pause
    hide ctc
    suki "this is more like it..."
    suki "You have great finger technique aang, but..."
    suki "...but what I really need right now is a big fat cock greedily kissing my womb."


    show totn totn100
    suki "hunngh...!!!"
    show ctc
    pause
    hide ctc
    y "damn suki..."
    suki "Ah! You're stretching me so wide!"
    suki "I'm going to be feeling this in the morning!"
    y "you have such a delicious fucking ass..."
    y "that pussy is sucking me in..."
    show ctc
    pause
    hide ctc
    suki "Can you take all of me, Aang?"
    suki "Can you take me slamming down on you?"


    menu:
        "Make that ass bounce girl":
            y "give it to me!"
            suki "That's what I wanted to hear!"
            $ totn_head = 'back'
            show totn totn101
            suki "*MMmmmmmmhhh...*"
            show ctc
            pause
            hide ctc
        "Let's take things easy... for now":

            y "nice and easy... this feels amazing..."
            $ totn_head = 'face'
            suki "Aaah... you're no fun."
            suki "but I'm still going to milk you dry."
            $ totn_head = 'back'
            show ctc
            pause
            hide ctc



    suki "I'm going to leave your sack so empty you'll need a week to recover!"
    show ctc
    pause
    hide ctc
    $ totn_head = 'face'
    y "If there's one thing I have absolute confidence in, it's my ability to make the white stuff."
    suki "Let's see you prove that."
    suki "How about it Aang?"
    suki "Are you ready to fill me all up?"
    show ctc
    pause
    hide ctc

    if totn_impreg == False:
        y "ready, willing, and able!"
        suki "I'll leave it up to you Aang."
        suki "Outside or inside, make it spray! "

    y "I think I'll...."

    menu:
        "cum on your ass":
            y "Sit still and spread those asscheeks, Suki!"
            show totn totn09 with Dissolve(1.5)
            suki "Do it!"
            show ctc
            pause
            hide ctc
            suki "Spray your seed all over my ass, Aang!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/suki/lovefuck/spermout_1.png"
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/suki/lovefuck/spermout_2.png"
            $ renpy.pause()
            play sound "audio/splurt2.ogg"
            show expression "bk3/suki/lovefuck/spermout_3.png"
            $ renpy.pause()
            show totn totn10 with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            suki "That's more than I was expecting!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/suki/lovefuck/spermout_4.png"
            suki "Ah! Aang!"
            suki "Are you trying to drown me?"
            suki "it...it's everywhere!"
            suki "You could literally fill up jars!"
            suki "I gotta take a shower quick or I'll be stuck to the floor."
            suki "Let's do this again soon."
            show ctc
            pause
            hide ctc
        "cum inside your cunt":

            y "I'm gonna fill up your cum-sucking cunt!"
            suki "yes! talk dirty! I love it!"
            y "slurp my cum out with your juicy cunt, suki!"
            suki "yes!!!"
            $ totn_impreg = True
            play sound "audio/splurt2.ogg"
            show totn totn03
            with flash
            y "hngh!"
            suki "ffuuuuucck!!!!"
            play sound "audio/splurt3.ogg"
            with flash
            show ctc
            pause
            hide ctc
            show totn totn08 with Dissolve(1.5)
            suki "I could fill a bucket with what's dripping out of me!"
            show ctc
            pause
            hide ctc
            $ totn_head = 'back'
            suki "*mmmm...*"
            play sound "audio/kiss.mp3"
            with pflash
            "suki fiercely kisses your mouth with hers, sucking your bottom lip as she pulls back."
            suki "*mwa!*"
            suki "Thanks for the extra thick filling, Aang."
            show ctc
            pause
            hide ctc

    scene black with dissolve
    "you head home for the night."
    $ love_suki_sex = True
    jump love_bk3_next

label love_ty_footjob:
    stop music
    play music "audio/Unwritten Return.mp3"
    scene black with dissolve
    show expression "bk3/tylee/footjob/bg_bedroom.jpg"
    show totf_upper up2
    show totf totf10
    with dissolve
    ty "hehe!"
    ty "ready?"
    ty "want me to make you cum with my toes?"
    show totf_upper up3
    "you step behind her."
    ty "oh, you're... eager..."
    ty "that's fun..."
    ty "you gonna pull out that big... *giggle*... penis?"

    show totf totf09 with dissolve
    ty "oh, my..."
    ty "you're going to make a lot of cum, aren't you?"
    y "I'm planning on it."
    show totf totf10 with dissolve
    "you step back for a moment."
    y "lift up your legs."
    show totf totf03 with dissolve
    ty "sure!"
    show totf totf04 with dissolve
    ty "can i... start?"
    y "go for it."
    y "use those small agile acrobat feet..."

    show totf totf05 with dissolve
    ty "*giggle*"
    y "what?"
    ty "it's just funny how hot it is."

    show totf totf06
    y "hnngh..."
    show ctc
    pause
    hide ctc
    ty "*giggle*"
    ty "boys are funny!"
    ty "you like me talented little toes on your thick cock?"
    ty "*giggle!*"
    ty "i'm milking you like a cow!"
    y "yeah... you... are..."
    ty "want it faster?"
    y "....."
    y "yes...."
    ty "okay!"
    show totf totf07
    y "oh, fuuuckk..."
    ty "*giggle!*"
    show ctc
    pause
    hide ctc
    ty "oh, no!"
    ty "is it working too well?"
    ty "*giggle!*"
    y "you know exactly... fuck... how well it's working..."
    show ctc
    pause
    hide ctc
    ty "you're getting really stiff..."
    ty "you gonna cum, daddy?"

    menu:
        "cum on ass":
            show totf totf03 with dissolve
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/tylee/footjob/sperm1.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/tylee/footjob/sperm2.png"
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/tylee/footjob/sperm3.png"
            show ctc
            pause
            hide ctc
        "cum on pussy":

            hide totf_upper
            show totf totf08
            with Dissolve(1.5)
            y "oh shit, that's a hot position."
            ty "yeah?"
            ty "does it make you wanna cum?"
            ty "on me?"
            ty "do you want to cum on me?"
            ty "you totally can!"
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/tylee/footjob/sperm4.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/tylee/footjob/sperm5.png"
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/tylee/footjob/sperm6.png"
            $ renpy.pause()
            ty "wow...."
            ty "You can shoot it really far!"
            show ctc
            pause
            hide ctc

            menu:
                "Get her to eat it":
                    y "you know... sperm is a great non-fattening nutrient."
                    ty "it is?"
                    ty "....."
                    show expression "bk3/tylee/footjob/handonpussy.png" with dissolve
                    "She grabs a scoop of your sperm."
                    ty "hmmm...."
                    hide expression "bk3/tylee/footjob/handonpussy.png"
                    show expression "bk3/tylee/footjob/handinmouth.png"
                    with dissolve
                    ty "*mmmgh...*"
                    ty "I'm not crazy about the taste, but as long as it's healthy...."
                    hide expression "bk3/tylee/footjob/handinmouth.png"
                    show totf_scoopsperm
                    ty "it'd be a waste to just wash it off."
                    ty "*mmmgh...*"
                    ty "gotta stay healthy!"
                    ty "*Burp!*"
                    ty "....there's a lot of it though."
                "Leave":
                    pass

    y "Thanks Ty Lee!"
    ty "any time!"


    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label jin_loveblowjob:
    scene dressingroom with dissolve
    "You enter Jin's room."
    y "....is that a suction cup dildo on your wall?"
    show tojn tojn02:
        xzoom -1
    with dissolve
    jin "what?"
    show tojn tojn01 with dissolve
    jin "oh, yeah. it is."
    show ctc
    pause
    hide ctc
    y "...."
    y "you're... mostly naked."
    jin "these are just my lounging around clothes."
    y "so... sexy..."
    jin "hehe!"
    jin "I'd hoped you say that!"
    jin "I have another surprise for you, in that case..."
    hide tojn with dissolve
    show tojn tojn22:
        xzoom -1
    with dissolve
    show ctc
    pause
    hide ctc
    y "...yowza."
    jin "oh, come on..."
    if not jin_love_bj:
        jin "you already saw me naked in the tunnels."
        y "yeah, but that was... a rescue thing..."

        if b3love_jin_mazesex ==1:
            jin "we had sex."
            y "also kind of a rescue thing..."
        if b3love_jin_mazesex ==2:
            jin "you banged me with a dildo."
            y "also kind of a rescue thing..."
        y "this is... you showing yourself freely to me."
        y "it's... hotter."
        y "sexier, in a way."
        jin "you're really making me blush..."
        y "i noticed."

    jin "hey... do you mind if i sit?"
    y "what? of course not."
    y "this is your room."
    jin "cool."
    hide tojn with dissolve
    $ renpy.pause(0.2)
    jump jin_loveblowjob2

label jin_loveblowjob2:
    stop music
    play music "audio/Unwritten Return.mp3"
    show toto toto01 with Dissolve(1)
    y "....nice."
    show ctc
    pause
    hide ctc
    jin "Pffff...."
    jin "i'm just getting comfortable."
    if not jin_love_bj:
        jin "like i said..."
    jin "...you've already seen a lot more of mine than just these tits."
    y "i did."
    y "and trust me... i'm thinking about it right now."
    show toto toto01a
    jin "oh, are you...?"
    y "i'm, uh... straining against my pants, here."
    jin "*mmmm...*"
    show toto toto01 with dissolve
    jin "hey, seriously..."
    jin "I'm super grateful for all the things you've been doing for me."
    if not jin_love_bj:
        jin "I even get to live here for free."
        jin "and... i know we're doing a casual dating thing, but..."
        jin "i'm really having a great time."
        y "me too."
        y "and you're welcome."
        jin "no, that's... not enough."
        jin ".........."
        jin "I just..."
        jin "wish i could give you a blowjob."
        y "......"
        y "...do it."
    if jin_love_bj:
        jin "can i... give you another blowjob?"
        y "...sure."

    show toto toto01b
    jin "seriously?!?" with hpunch
    y "well, yeah."
    y "how could i turn that down?"
    if not jin_love_bj:
        jin "you'd really let me?"
    if jin_love_bj:
        jin "awesome!"
        jin "give it here!"

    if not jin_love_bj:
        show toto toto01
        jin "Thank the spirits..."
        jin "i really really want to taste your cock."
        jin "is that... okay?"
        y "i... well... yes."
        show toto toto01a with dissolve
        jin "pull it out."
        y "....are you teasing me?"
        y "this seems very... um... easy."

        show toto toto01 with dissolve
        jin "were... were you joking?"
        jin "sorry."
        jin "i've been feeling super horny since the tunnels."
        jin "I don't know what that ajala chick did, but i'm just so damn horny all the time."
        jin "i was hoping you could help me..."
        jin "besides, i..."
        jin "...i just want to thank you and show you i appreciate you and..."
        jin "i just really want you to fuck my face."
        jin "please?"
        show toto toto01a with dissolve
        y "...i would be thrilled to provide."
        jin "Great!"
        jin "I've been using a dildo but it's just no substitute for the real thing."
        show toto toto01 with dissolve
        jin "come on! whip it out!"
        jin "Show me what you got!"

    show toto toto02
    jin "oh!"


    if not jin_love_bj:
        if b3love_jin_mazesex == 0:
            jin "Back in the maze you left me... unfilled."
            jin "er... unfulfilled."
            jin "you didn't quite scratch my itch."

        elif b3love_jin_mazesex == 1:
            jin "So this is going to go inside me... again."
            jin "I'm looking forward to it!"

        elif b3love_jin_mazesex ==2:
            jin "this is going to taste so much better than that dildo."

    jin "It's looking really hard."
    jin "I'll start licking the top first."
    jin "That alright with you?"
    y "I have no objections."
    show toto toto03 with Dissolve(1.5)
    "With short little laps she starts licking the top of your penis."
    show ctc
    pause
    hide ctc
    y "That's... very nice."
    jin "If you think that's nice, watch this."

    show toto toto05
    y "You..."
    y "*hnnng...*"
    y "you {i}have{/i} practiced a lot!"
    show ctc
    pause
    hide ctc
    jin "*mmgh...*"
    jin "*slurp* *guuulp* *slllurp*"
    show ctc
    pause
    hide ctc
    y "May I suggest a combo move of licking and sucking?"

    show toto toto04
    jin "shhure!"
    show ctc
    pause
    hide ctc
    jin "*smack* *slurp* *shlap*"
    y "fuuck..."
    show ctc
    pause
    hide ctc
    y "That's really effective."
    menu:
        "Please keep doing what you're doing":
            pass
        "Could you go back to just licking?":
            show toto toto03
        "How about only sucking again?":
            show toto toto05

    show ctc
    pause
    hide ctc
    jin "*Mmmmngh....*"
    show ctc
    pause
    hide ctc

    show toto toto02 with dissolve
    y "....."
    y "Why did you stop?"
    jin "I just wanted to take another look at him."
    jin "Would mind me getting a little rougher?"
    y "As long as it doesn't come off, go right ahead."
    jin "great!"
    show toto toto06
    show ctc
    pause
    hide ctc
    jin "*gag* *gulp* *sluurp*"
    y "i... damn, jin..."
    jin "*gaghh* *shhllllup*"
    y "I... I'm gonna cum...."
    jin "*slluurp* *guulp* shmack* *shlurp*"
    menu:
        "Cum in her mouth":
            show toto toto09 with Dissolve(1.5)
            hide toto
            play sound "audio/splurt2.ogg"
            show toto toto09
            with flash
            $ renpy.pause(0.1)
            play sound "audio/splurt1.ogg"
            with flash
            "jin sucks hard at the tip, pulling out your sperm as it rockets into her throat."
            "she keeps it steady in her mouth as wave after wave of semen spurt into her mouth."
            show toto toto09
            show expression "bk3/jin/love_bj/spermin_1.png"
        "Cum on her face":

            show toto toto07 with Dissolve(1.5)
            hide toto
            show toto toto07
            jin "come on, then."
            y "ngh!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/love_bj/spermout_1.png"
            with flash
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/jin/love_bj/spermout_2.png"
            with flash
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/jin/love_bj/spermout_3.png"
            with flash
            $ renpy.pause()




    show toto toto08
    with dissolve
    jin "Aahh, now that's something a dildo could never give me!"
    jin "come and visit me whenever you feel you need some relief."
    jin "and... thanks, aang."
    jin "you're the best."
    jin "this is... all i've ever wanted."
    jin "and i'm just so happy."
    jin "thanks."
    y "you... i..."
    y "...i need a nap."

    scene black with dissolve
    "you head home for the night."
    $ jin_love_bj = True
    jump love_bk3_next


label meangirls_reward:

    show bk3_bg_fountain
    "You look around but see nothing of interest, when all of a sudden someone taps you on the shoulder."

    show totu totu03 with Dissolve(1.5)
    "red" "Hey it's us!"
    "red" "thanks again for your help in those horrible tunnels."
    if not mg_reward:
        "red" "We talked it over and the three of us... well we'd like to reward you somehow."
        y "Oh, that's cool."
        "red" "Is there anything you'd like?"
        y "uhh... money?"
        "red" "Our parents decided it was best if we didn't have access to funds anymore."
        "red" "They thought us spending it would attract people wanting to rob or abduct us."
        y "I see, well the only other thing I like is watching naked girls, but..."
        "red" "We can do that!"
        "red" "I mean, there's nothing you haven't already seen, so if that's all..."
    "red" "Let... let's go to that alley there."
    menu:
        "lead the way!":
            pass
        "no thanks":

            y "maybe later."
            "red" "oh..."
            jump love_basingse_day1

    hide bk3_bg_fountain
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg"
    hide totu
    show totu totu03

    "red" "Okay, here we are..."
    "The three girls fumble with their clothes and within a few minutes..."

    stop music
    play music "audio/Unwritten Return.mp3"

    show totu totu04 with Dissolve(1.5)
    y "Nice."
    if not mg_reward:
        y "say... aren't you worried about doing this here?"
        "red" "We don't really have anywhere else to do it, and we're guessing you're strong enough to chase anyone away."
        y "True..."
    y "Okay, you just stand there."
    y "I want to make this whole experience slightly better for me."

    $ totu_redgirl = 'neutral'
    $ totu_pinkgirl = 'neutral'
    $ totu_whitegirl = 'neutral'

    hide totu
    show expression "bk3/meangirls/reward/bg_sky.jpg"
    show totu totu01
    with Dissolve(1.5)

    y "I like this... I like this a lot."
    "red" "This is really embarrassing... being stared at from this angle..."
    y "Do you know what would even be more embarrasssing?"
    "red" "...yeah..."
    "red" "Do... do you want me to...?"
    y "absolutely."
    "Hesitantly, she lets her hands slide over her thighs and carefully spreads her lips."
    $ totu_redgirl = 'spread'
    "red" "I... I can't believe I'm doing this..."
    y "Me neither!"
    y "I assumed you were just going to jump up and down and jiggle your titties!"
    y "But this is {i}much{/i} better!"
    y "Hey, pink and yellow."
    y "You're not going to let your friend go through this experience by herself, right?"
    $ totu_pinkgirl = 'spread'
    $ totu_whitegirl = 'spread'

    y "That's nice..."
    y "that's very, very nice."
    y "Why don't you stand around me in a cicle."


    $ totu_redgirl = 'neutral'
    $ totu_pinkgirl = 'neutral'
    $ totu_whitegirl = 'neutral'
    show totu totu02 with Dissolve(1.5)


    y "excellent."
    y "I'd like it a lot if you touch yourself."
    y "I bet you know exactly how it's done, red."
    y "Why don't you show the others how?"
    "red" "I... okay..."
    $ totu_redgirl = 'masturbate'

    "red" "*Hnnnnn...*"
    y "Damn that's hot... "
    y "I'm going to touch myself too."
    "You whip out your erect cock and the girls squeal with surprise as you start stroking it."
    y "Okay, you've seen how it's done, now follow red's lead."
    $ totu_pinkgirl = 'masturbate'
    $ renpy.pause(0.3)
    $ totu_whitegirl = 'masturbate'
    "The two other girls join the first one."
    "They're a bit awkward at first but soon enough any difference between them is gone."
    $ renpy.pause()
    y "Life is good."
    y "Very good."
    "the girls let their hands go up and down, having their fingers follow along the curves of their bodies."
    "Their glistening pussies become wetter with each moment."
    "red" "This... hnnng... this is such a crazy turn-on!"
    "red" "Standing here, stroking ourselves while being watched..."

    y "hold on for a second."

    $ totu_redgirl = 'neutral'
    $ totu_pinkgirl = 'neutral'
    $ totu_whitegirl = 'neutral'


    y "I love seeing you girls enjoy yourselves, but I won't be able to last long as things are."
    y "So before I shoot my load..."
    menu:
        "Piss on me":

            $ totu_redface = 'shock'
            "red" "Piss on you?!?" with hpunch
            y "Yep, that's what I said."
            "red" "Are... are you sure?"
            y "Just empty your bladder all over me."
            $ totu_redface = 'neutral'
            "red" "...okay."
            "red" "Here it comes."
            $ totu_redgirl = 'piss'
            "The salty yellow fluid starts with short uncertain bursts, but within a blink turns into a steady stream."
            y "Red has taken the lead."
            y "What are you waiting for, pink and white?"
            $ totu_whitegirl = 'piss'
            $ totu_pinkgirl = 'piss'
            "Very soon three steady streams are aimed at your face."
            y "*gurgle*"
            $ renpy.pause()
            "red" "Are we doing it right?"
            y "Just the way I imagined it!"
            $ totu_redgirl = 'spread'
            "Red's stream is the first to slow down to a trickle and stop."
            "The other two girls last a few moments longer but are empty soon enough too."
            $ totu_pinkgirl = 'spread'
            $ totu_whitegirl = 'spread'
            y "Well done!"
            $ totu_redgirl = 'neutral'
            $ totu_pinkgirl = 'neutral'
            $ totu_whitegirl = 'neutral'
        "Spread yourself and walk around me":


            y "I want to have a good look at your lady parts from all possible angles."
            "red" "I'm doing the craziest things today!"
            $ totu_redgirl = 'spread'
            $ totu_whitegirl = 'spread'
            $ totu_pinkgirl = 'spread'

            show totu totu02:
                xanchor 0.5 yanchor 0.5 xpos 500 ypos 360
                linear 40.0 rotate 360
            $ renpy.pause()
            y "Fuck yeah."
            y "This is the shit!"
            hide totu
            show totu totu02
            show totu totu01 with Dissolve(1.5)
        "Just keep going as you were":

            $ totu_redgirl = 'masturbate'
            $ renpy.pause(0.5)
            $ totu_whitegirl = 'masturbate'
            $ totu_pinkgirl = 'masturbate'
            y "That's it."
            y "Rub those pretty little twats!"






    y "Okay!"
    y "Line up, spread those pussies, and get ready for some cum."


    show totu totu01 with Dissolve(1.5)

    $ totu_redgirl = 'spread'
    $ totu_pinkgirl = 'spread'
    $ totu_whitegirl = 'spread'


    y "Hnnnnng!"

    show expression "bk3/meangirls/reward/white.png" with Dissolve(0.5)
    play sound "audio/gltch2b.mp3"    
    $ totu_redgirl = 'sperm'
    hide expression "bk3/meangirls/reward/white.png" with Dissolve(1.0)

    $ renpy.pause(0.5)

    show expression "bk3/meangirls/reward/white.png" with Dissolve(0.5)
    play sound "audio/gltch2b.mp3"    
    $ totu_whitegirl = 'sperm'
    hide expression "bk3/meangirls/reward/white.png" with Dissolve(1.0)

    $ renpy.pause(0.5)

    show expression "bk3/meangirls/reward/white.png" with Dissolve(0.5)
    play sound "audio/gltch2b.mp3"    
    $ totu_pinkgirl = 'sperm'
    hide expression "bk3/meangirls/reward/white.png" with Dissolve(1.0)

    $ renpy.pause(0.5)
    y "That's it for today, girls!"


    $ mg_reward = True
    $ bk3_day = False
    jump love_bk3_village_background

label fireguard_hypno:
    hide screen earth_money_date
    scene inside_shack
    show toju toju09
    with dissolve
    ju "...your house?"
    ju "you gonna tuck him in?"
    y "no, just come on."
    scene black with dissolve
    scene hypno_room2
    show toju toju09
    with dissolve
    ju "ahh...."
    ju "you're going to hypnotize him?"
    ju "do you think that will work?"
    y "it's the only thing i can think to try."
    y "this one time only, i'll use this room to hypnotize instead of undo hypnosis."
    y "i'm going to change his memory."
    y "that seems to have happened to all the girls that underwent this... including you."
    y "i think... i think i can manage it."
    ju "there's a lot riding on \"hope\"."
    ya "if it doesn't work... i'll figure it out, okay?"
    ju "sure, sure."
    y "come on, dude..."
    "you lift up the fire nation guard."
    show fireguard_halberd:
        xzoom -1
    with moveinbottom
    fg "unghh..."
    y "I know, i know."
    y "here we go..."
    show black with dissolve
    "you dump him in the chair and set up the hypnosis equipment."
    "after putting him under, you convince him that he almost entered the boarding house, but changed his mind."
    "you put away the equipment."
    hide black with dissolve
    ju "okay... moment of truth."
    y "guard!"
    fg "whosa... whatsit?"
    y "what did you do this afternoon?"
    fg "i... i was going to... go into the boarding house... thought it was a brothel..."
    fg "changed... changed my mind..."
    fg "turned around and went back to the fire nation camp."
    y "who did you see in the village?"
    fg "no one..."
    y "good man."
    ju "hmph."
    show black with dissolve
    "you kick the guard out the door."
    "he wanders off in a haze."
    hide black
    hide fireguard_halberd
    with dissolve
    ju "well..."
    y "well what?"
    ju "that... wasn't bad, avatar."
    y "thanks."
    ju "you're... really actually a good person."
    ju "a really really good one."
    y "i don't know about that..."
    ju "yeah, well, it's true."
    ju "I never thought i'd be attracted to... er..."
    y "me? a nice guy?"
    show toju_blink with dissolve
    ju ".....yes."
    ju "but i am."
    hide toju_blink with dissolve
    ju "so here we are."
    y "yeah."
    ju "you know you saved my ass again today?"
    y "i know."
    ju "...."
    ju "I'm tired."
    ju "I'm going home."
    ju "come over tomorrow."
    ju "i have... something... to give you."
    hide toju with dissolve
    $ bk3_day = False
    jump love_bk3_village_background

label june_lovefuck:
    stop music
    play music "audio/Unwritten Return.mp3"
    scene black with dissolve
    scene expression "bk3/june/lovefuck/bg_bed.jpg"
    with dissolve
    if june_light ==4:
        y "this is your room?"
        y "...it's nice."
        ju "it suffices."
        ju "but before we get any further..."
        ju "i am a fully grown woman, so tell me..."
    if june_light ==5:
        ju "before we get started, remind me..."
    ju "how do you feel about pubic hair?"

    menu:
        "yes pubes":
            y "i like 'em."
            $ june_pubes = 'bush'
        "no pubes":
            y "not a fan."
            $ june_pubes = 'shaven'
    ju "well that's lucky, because..."
    show totp totp00
    show totp_sex totp_stare
    with Dissolve(1.5)
    y "*cough...*"
    show ctc
    pause
    hide ctc
    if june_light ==4:
        y "that's a... good... view..."
    if june_light ==5:
        y "amazing view, just as before."
    ju "i'm glad you approve."
    ju "because..."
    show totp totp01 with Dissolve(1.5)
    ju "i want you inside me."
    show ctc
    pause
    hide ctc
    if june_light ==4:
        y "that's... fuck."
        y "i barely know what to do with my emotions here."
        y "i seem to be very excited."
    if june_light ==5:
        y "you and me both."
    ju "you're cute, you know that?"
    ju "Let me make things clearer."
    show totp totp02 with Dissolve(1.5)
    ju "please... come have your way with me."
    show ctc
    pause
    hide ctc
    y "gulp."
    ju "I want you to pound me with that delicious cock until i scream, aang."
    ju "look at all this sweet pussy... it's yours."
    if june_light ==4:
        y "I didn't think you even knew my name, to be honest."
        y "you've just kept calling me \"avatar\"."
        ju "of course i know your name."
    ju "you're the mighty, throbbing, powerful avatar."
    if june_light ==5:
        ju "now take me."
    show totp totp03 with Dissolve(1.5)
    if june_light ==4:
        ju "now come into me."
    if june_light ==5:
        ju "come into me."
    ju "my squeezing, pulsing, begging pussy is waiting for you."
    ju "come and claim it, baby."
    ju "plant your fucking flag in me and claim your territory."
    ju "mark me yours."
    show ctc
    pause
    hide ctc
    y "......"
    y "beg."
    ju "please, avat... aang."
    ju "don't you want to slip inside?"
    ju "please... let me feel you on my pussy..."
    ju "just... just rub it on my lips a little first... ease me into it..."
    y "...you asked for it."
    play sound "audio/gltch2b.mp3"
    show totp_sex totp_rub with dissolve
    ju "unnnghh...."
    ju "fuuuuck yesss...."
    show ctc
    pause
    hide ctc
    "you slip against june's juicy, soft pussy."
    "the plush lips are so wet and engulfing you risk cumming just from the slickness."
    ju "yes, avatar... aang... yes baby..."
    ju "i feel you... i feel the avatar's cock... pressing against my cunt..."

    if june_pubes == 'bush':
        hide totp_sex totp_rub
        show expression "bk3/june/lovefuck/rubp_1.png"
        with dissolve
        ju "mmmm.... watcha doing there?"
        show ctc
        pause
        hide ctc
        play sound "audio/gltch2b.mp3"
        hide expression "bk3/june/lovefuck/rubp_1.png"
        show expression "bk3/june/lovefuck/fuckp_1.png"
        with dissolve
        ju "*aahhh....*"
        show ctc
        pause
        hide ctc

    if june_pubes == 'shaven':
        hide totp_sex totp_rub
        show expression "bk3/june/lovefuck/rub_1.png"
        with dissolve
        ju "mmmm.... watcha doing there?"
        show ctc
        pause
        hide ctc
        play sound "audio/gltch2b.mp3"
        hide expression "bk3/june/lovefuck/rub_1.png"
        show expression "bk3/june/lovefuck/fuck_1.png"
        with dissolve
        ju "*aahhh....*"
        show ctc
        pause
        hide ctc

    ju "that's it, avatar..."
    ju "what are you waiting for?"
    ju "you want it, don't you?"
    ju "you want me?"
    ju "take me!"
    ju "don't tease me..."
    ju "slide it in... slide it deep, deep inside me..."
    ju "or maybe i should say..."
    show head_eyeonplayer with dissolve
    ju "don't."
    ju "don't you dare."
    ju "you can rub my pussy, but you're not allowed inside me."
    ju "don't you dare put it-"
    play sound "audio/gltch2b.mp3"
    show totp_sex totp_fuck
    show head_shock_2
    hide head_eyeonplayer
    with pflash
    ju "ohhhhh....."
    ju "fuucckkk yesss...."
    show ctc
    pause
    hide ctc
    ju "fill... fill my tight, juicy cocksleeve..."
    hide head_shock_2
    show head_shock_3
    with dissolve
    ju "yess... oh hell yeah..."
    ju "have your way with me... please... own me, baby... that's it..."
    ju "stuff that pussy, baby..."
    ju "oh spirits..."
    show ctc
    pause
    hide ctc
    ju "are you... having... ah... fun with my tight... cock-slurping pussy?"
    ju "because fuck..."
    ju "you're much... much thicker than i... i thought you'd be..."
    ju "i've never... ah... had... such... ah... it's so... fucking... filling me... ah..."
    hide head_shock_3
    with dissolve
    hide totp_sex
    ju "what..."
    show ctc
    pause
    hide ctc
    y "you want it?"
    ju "i want it."
    y "you want it?"
    show head_eyeonplayer
    ju "{size=+6}i want it!"
    ya "you want it?!"
    ju "{size=+6}i want-"
    show totp totp05
    if june_pubes == 'shaven':

        show totp_fuck2_1 with vpunch
    else:
        show totp_fuck2_1p with vpunch

    hide expression "bk3/june/lovefuck/fuck_1.png"
    hide expression "bk3/june/lovefuck/fuckp_1.png"
    ju "{size=+10}oh fat fucking spirits of cock!!!"
    ju "shit!"
    ju "shit! shit! fuck!"
    ju "fuck that's deep!"
    show ctc
    pause
    hide ctc
    ju "avatar!"
    ju "avatar, please! stop! wait! ah!"
    show ctc
    pause
    hide ctc
    if june_pubes == 'shaven':
        hide totp_fuck2_1
        show totp_fuck2_2
    else:
        hide totp_fuck2_1p
        show totp_fuck2_2p
    ju "unghh... ungh.... fuuuck....!!"
    ju "don't speed uuuuppp!!!"
    show ctc
    pause
    hide ctc
    y "\"avatar\" isn't my name, bitch!"
    y "say my name!"
    ju "a-aang!"
    menu:
        "fast":
            $ love_june_fast = True
            if june_pubes == 'shaven':
                hide totp_fuck2_2
                show totp_fuck2_3_1
            else:
                hide totp_fuck2_2p
                show totp_fuck2_3_1p
        "slow":

            $ love_june_fast = False
            if june_pubes == 'shaven':
                hide totp_fuck2_2
                show totp_fuck2_3
            else:
                hide totp_fuck2_2p
                show totp_fuck2_3p

    ju "please, aang! g-gentle! please! ah!"
    ju "you're too bi-big for... ah... this... ah!"
    show ctc
    pause
    hide ctc
    y "Gonna cum!!"
    if love_june_fast:
        if june_pubes == 'shaven':
            hide totp_fuck2_3
            hide totp_fuck2_3_1
            show totp_fuck2_4_1
        else:
            hide totp_fuck2_3p
            hide totp_fuck2_3_1p
            show totp_fuck2_4_1p

    if not love_june_fast:
        if june_pubes == 'shaven':
            hide totp_fuck2_3
            hide totp_fuck2_3_1
            show totp_fuck2_4
        else:
            hide totp_fuck2_3p
            hide totp_fuck2_3_1p
            show totp_fuck2_4p
    ju "yesss...."
    ju "unngh! ungh! ah! ohhngh! fuck!"
    show ctc
    pause
    hide ctc
    ju "fuck it's good! fuck it's so good!"
    ju "give...! oh...! let it... ah... out! fuck! let it out!"
    ju "Please! fuck! fucking fuck! please! fuck!"
    menu:
        "inside":

            $ totp_preg = True
            play sound "audio/splurt2.ogg"
            if june_pubes == 'shaven':
                hide totp_fuck2
                hide totp_fuck2_4_1
                hide totp_fuck2_4
                show expression "bk3/june/lovefuck/fuck_6.png"
            else:
                hide totp_fuckp2
                hide totp_fuck2_4_1p
                hide totp_fuck2_4p
                show expression "bk3/june/lovefuck/fuckp_6.png"
            with flash
            ju "unngh!!"
            ju "fuck... fuck..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/lovefuck/head_shock.png" with vpunch
            ju "oh spirits!"
            ju "there's so fucking mu-"
            play sound "audio/splurt3.ogg"
            hide expression "bk3/june/lovefuck/head_shock.png"
            with flash
            if june_pubes == 'shaven':
                hide expression "bk3/june/lovefuck/fuck_6.png"
            else:
                hide expression "bk3/june/lovefuck/fuckp_6.png"

            show expression "bk3/june/lovefuck/cum_outside.png"
            show totp totp06
            ju "unnngh...."
            show ctc
            pause
            hide ctc
        "outside":

            play sound "audio/splurt2.ogg"
            if june_pubes == 'shaven':
                hide totp_fuck2
                hide totp_fuck2_4_1
                hide totp_fuck2_4
            else:
                hide totp_fuckp2
                hide totp_fuck2_4_1p
                hide totp_fuck2_4p
            show expression "bk3/june/lovefuck/sperm_out_1.png"
            with flash
            $ renpy.pause()
            ju "oh... oh fuck..."
            ju "my... my puss... pussy... ah..."
            play sound "audio/splurt3.ogg"
            show expression "bk3/june/lovefuck/sperm_out_2.png"
            with flash
            $ renpy.pause()
            ju "so... there's so... fucking mu-"
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/lovefuck/sperm_out_3.png"
            with flash
            ju "unnghh...."
            show ctc
            pause
            hide ctc

    show totp totp07 with Dissolve(1.5)
    ju "so... good..."
    ju "and sore..."
    ju "not... not bad, avatar...."
    ju "...fuck."
    ju "need... sleep."
    y "i'll let you rest then."
    ju "thank... you..."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head home for the night."
    $ june_light = 5
    jump love_bk3_next

label toph_shadow_fuck:
    stop music
    play music "audio/Unwritten Return.mp3"
    $ totx_head = 'happy'

    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"

    show totx totx08


    show expression "bk3/toph/shadowfuck/silhouette.png":
        alpha 1.0

    show expression "bk3/toph/shadowfuck/silhouette.png":
        linear 3.0 alpha 0.0
    with fade
    $ renpy.pause(3.0)
    "You barely touch the ground before Toph crawls on your lap."
    t "like this?"
    y "mm-hmm."
    t "You're so warm... It's really nice to hold you like this while we're both naked."
    show ctc
    pause
    hide ctc
    hide expression "bk3/toph/shadowfuck/silhouette.png"


    show expression "bk3/toph/shadowfuck/hands.png"
    show totx totx05 with Dissolve(1.5)
    t "I think... i think i'm ready, aang."
    y "are you sure?"
    t "...i think so..."
    show ctc
    pause
    hide ctc
    t "Katara has filled me in on some of the details..."
    t "I want to do this at my pace, though."
    t "okay?"
    y "of course."
    t "don't do anything unless I say so, okay?"
    y "absolutely."
    y "does that mean you don't want me to make suggestions?"
    $ totx_head = 'worried'
    t "no, you can... you can totally help me..."
    t "just... just don't push it, okay?"
    y "okay."
    show totx totx06 with Dissolve(1.0)
    t "I'm going to hold on to you so you need to... ahumm... aim it...?"
    y "i think now would be the time to put the tip in."
    t "okay..."
    show ctc
    pause
    hide ctc
    t "just... just the tip, okay?"
    t "Slowly."
    t "Veeerry slowly."
    "You do as Toph asks you."
    "It's tight, but not as impossible as you feared."
    play sound "audio/gltch2b.mp3"
    $ totx_head = 'careful'
    show totx totx04
    $ totx_head = 'shock'

    t "Aaaah!" with hpunch
    show ctc
    pause
    hide ctc
    $ totx_head = 'careful'
    t "ooooohh that... that wasn't so bad..."
    t "But we're not there yet..."
    show ctc
    pause
    hide ctc
    play sound "audio/gltch2b.mp3"
    show totx totx03 with Dissolve(1.5)
    t "HNnnnn, a little more.."
    show ctc
    pause
    hide ctc
    play sound "audio/gltch2b.mp3"
    show totx totx02 with Dissolve(1.5)
    t "Not quite there yet...."
    show ctc
    pause
    hide ctc
    play sound "audio/gltch2b.mp3"
    show totx totx01 with Dissolve(1.5)
    t "aaahh!"
    t "Okay... that's as far as it goes."
    t "I'm just going to sit like this for a moment."
    show ctc
    pause
    hide ctc
    "after a long silent moment and a slightly pained expression toph starts to smile."
    $ totx_head = 'happy'
    t "you're all the way in."
    t "Or at least as far as I can get it."
    show ctc
    pause
    hide ctc
    y " You're truly fearless, Toph."
    t "I'm going to move up and down now..."
    t "And remember... you're absolutely forbidden from moving!"
    y "I won't move a finger!"
    t "{size=-4}your fingers aren't the problem..."
    y "what are you muttering?"
    t "...here goes..."
    $ totx_head = 'careful'

    show totx totx100
    t "This is fine... I can take it..."
    $ renpy.pause()
    $ totx_head = 'happy'
    "after a couple of runs, you can feel Toph getting a lot wetter and sliding up and down more easily."
    t "Getting better now..."
    t "a lot better!"
    t "Did you do something?"
    t "You know... with waterbending?"
    y "Nope, this is all you."
    t "aahh...."
    t "*mmmm...*"
    t "oh, aang..."
    t "this is... amazing!"
    t "why haven't we been... ah..."
    show ctc
    pause
    hide ctc
    t "that's it!"
    t "get ready, because I'm ready for more!"
    t "i think my pussy is hungry!"
    t "*giggle!*"
    y "did you just giggle?"
    t "i'm happy!"
    t "here we go!"
    $ totx_head = 'lewd'
    show totx totx101
    y "oh fuck!!"
    show ctc
    $ renpy.pause()
    hide ctc
    y "I'm telling you right now, a few more of those and I'm going to fill you to the brim with my babymaker juice!"
    t "That's okay."
    t "You can cum inside!"
    y "Here it comes!"
    hide expression "bk3/toph/shadowfuck/hands.png"
    hide totx
    show totx totx01

    show totx totx07 with Dissolve(1.5)
    show expression "bk3/toph/shadowfuck/body_5_dick.png" with Dissolve(1.5)
    play sound "audio/splurt2.ogg"
    $ renpy.pause(0.4)
    play sound "audio/splurt1.ogg"
    $ renpy.pause(0.4)
    show expression "bk3/toph/shadowfuck/sperm_inside.png" with Dissolve(1.5)
    play sound "audio/splurt2.ogg"
    $ renpy.pause(0.4)
    t "ohh!!!"
    show ctc
    pause
    hide ctc
    t "it's... wow...!"
    t "my insides are so hot...."
    play sound "audio/splurt3.ogg"
    hide totx
    hide expression "bk3/toph/shadowfuck/body_5_dick.png"
    hide expression "bk3/toph/shadowfuck/sperm_inside.png"
    $ totx_head = 'shock'
    show totx totx01
    show expression "bk3/toph/shadowfuck/hands.png"
    t "Aaah!"
    t "it's... it's still going!"
    t "You weren't kidding about filling me up!"
    show ctc
    pause
    hide ctc
    $ totx_head = 'happy'
    show totx totx02
    $ renpy.pause(0.3)
    show totx totx03
    $ renpy.pause(0.3)
    show totx totx06
    show expression "bk3/toph/shadowfuck/sperm_outside.png"
    with Dissolve(1.5)
    show totx_spermdrip
    $ renpy.pause()
    t "Oh, wow..."
    t "I can feel it literally gush out of me!"

    t "I think I'll go and clean myself up a bit."
    $ toph_back_disappear = 3
    t "get some rest, aang."
    y "that's... no longer going to be difficult..."
    scene black with dissolve
    "you fall fast asleep."
    $ love_toph_sex = True
    jump love_bk3_next

label toph_fuckonback:
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"

    show toty toty07
    with vshake
    "you place toph down on the bedroll."
    t "oof!"
    y "time for round two!"
    show ctc
    pause
    hide ctc
    show toty toty06 with Dissolve(1.5)
    y "i'm not going easy on you this time."
    t "......"
    t "...good."
    t "make me yours, aang."
    show toty toty00 with dissolve
    y "ready?"
    t "i... i think..."
    t "i want you, i just don't know if it will..."
    show toty toty01
    t "ooohh...."
    t "okay... i want you."
    t "i want you {i}hard{/i}, aang."
    y "no turning back from here..."
    t "aang..."
    t "love me... however you need."
    play sound "audio/gltch2b.mp3"
    show toty toty02
    t "*aahhh....*"
    y "and....."
    show toty toty99
    y "here we go..."
    t "oohhh... unngh..."
    show ctc
    pause
    hide ctc
    t "there's... just... so {i}much{/i} of you..."
    t "this is... a really deep position..."
    t "you don't have to be so gentle... i can take it."
    y "you think so?"
    t "i took you before-"
    show toty toty101
    t "{size=+6}ohh!!"
    t "ffffuck!!"
    show ctc
    pause
    hide ctc
    y "it's so cute when you swear."
    t "what... what the... what the fuck!!"
    t "it's... it's hitting something... in me... not supposed to... ah... ah..."
    y "probably your womb."
    y "this is the baby-maker position."
    t "it's... ah... too... too much... "
    t "but... ah... but good... ah..."
    y "alright... ready to get serious?"
    t "{size=+6}serious-?"
    show toty toty102
    t "ahhh!! ahhhh!!! ahhhhhhh!!!"
    show ctc
    pause
    hide ctc
    y "fuck yes!"
    t "too... too much!! too much penis!!"
    y "it's a \"cock\", toph."
    y "say \"cock\"."
    t "c-cock! ah! so... so much cock! too deep! ah!"
    y "you are sooo... damn tight!"
    t "ah! ah! ah! cock! cock!"
    y "time for the jackhammer!"
    t "nooooo....!!"
    show toty toty103
    t "ah! cock! fuck! ungh! ungh!"
    show ctc
    pause
    hide ctc
    t "c-cock! too... much! aang! easy! easy! please!!"
    y "oh shiiiit!"
    show toty toty104
    t "aaaaaaaaaaaahhhhhhhhhhhhhhh!!!!!!!!!!"
    "toph's whole body, including her vocal chords, vibrate with your relentless thrusts into her clutching virgin pussy."
    show ctc
    pause
    hide ctc
    y "here comes the baby batter!"
    t "give... give... semen... want... happy... ahh... ah... cock..."
    menu:
        "come inside":

            show toty toty01_1 with dissolve
            play sound "audio/splurt2.ogg"

            show toty toty04_1
            with vpunch
            t "oh!"
            play sound "audio/splurt3.ogg"
            with flash
            t "ohh... fuck!!"
            play sound "audio/splurt3.ogg"
            show toty toty04 with dissolve
            with flash
            "you shoot several blasts of cum as far into toph as you can manage, filling her womb with splashing sperm."
            show toty toty06
            show expression "bk3/toph/fuckonback/openpussy.png"
            show expression "bk3/toph/fuckonback/dick_outside_sperm.png"
            with dissolve
            "she shivers with satisfaction and exhaustion."

            y "Hmmm..."
        "come outside":

            hide toty
            show toty toty06
            show expression "bk3/toph/fuckonback/openpussy.png"
            t "give me your semen, aang!"
            play sound "audio/splurt2.ogg"

            show expression "bk3/toph/fuckonback/openpussy.png"
            show expression "bk3/toph/fuckonback/spermout_1.png"
            with flash
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/fuckonback/spermout_2.png"
            with flash
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/toph/fuckonback/spermout_3.png"
            with flash
            $ renpy.pause()
            "she shivers with satisfaction and exhaustion."
            pass

    y "you know... at some point i might have you stop taking those contraceptives."
    t "i... might like that..."
    y "sleep well, toph."
    t "hrgh... ah..."
    scene black with dissolve
    "the two of you fall fast asleep."
    jump love_bk3_next

label toph_mean_walk:
    scene black
    hide screen earth_money_date
    with dissolve
    scene basingse_outerwall1
    show toi toi04
    with dissolve
    t "it's nice out here!"
    t "thanks for-"
    show toi toi10
    show toi_blink
    with dissolve
    t "*yaaaawn....*"
    show toi toi09
    hide toi_blink
    with dissolve
    t "uh... what was i saying?"

    show toi toi04 with dissolve
    t "oh, right!"
    t "thanks for exploring with me."
    y "we're exploring?"
    t "yeah, what did you think we were doing?"
    y "i mean... taking a walk?"
    t "what's the point of a walk if you're-"
    show toi toi10
    show toi_blink
    with dissolve
    t "*yyyyaaaaaawwwn...*"
    y "...."
    show toi toi04 with dissolve
    t "what's the point of a walk..."
    show toi toi07
    hide toi_blink
    with dissolve
    t "...if you aren't gonna get in a little trouble?"
    y "you're a rapscallion, you know that, right?"
    show toi_blink with dissolve
    t "of course i am."
    y "hey... why are you so tired?"
    hide toi_blink
    show toi toi09
    with dissolve
    t "oh... um... i've had some weird dreams lately..."
    y "more nightmares?"
    t "not nightmares exactly..."
    t "more like... weird... angry... spirit dreams?"
    y "...go on."
    t "that probably sounds crazy."
    t "they call for blood and stuff."
    t "i keep dreaming that spirits are going insane."
    t "it's really weird."
    y "right... in dreams... not reality."
    t "obviously."
    y "that's not troubling or anything."
    y "i'm definitely not also having those dreams."
    show toi toi04 with dissolve
    t "why would you?"
    t "can we talk about something else now?"
    y "...sure."
    t "awesome."
    t "so, i want to go into the city... but i don't really care where in the city."
    t "you can decide."
    t "where would you like to go?"
    menu:
        "market":
            y "how about the market?"
            show toi toi07 with dissolve
            t "sounds like a good place to get into trouble."
            play sound "audio/earthquake.mp3"
            hide toi
            scene basingse_outerwall
            show toi toi07
            with sshake
            $ renpy.pause(0.5)
            t "path is now open! come on!"

            stop music fadeout 1
            play music "audio/jangles.mp3"
            scene black with dissolve
            scene market_general
            show toi toi04
            with dissolve
            t "alright!"
            t "what can we get up to..."
            "you look around and absorb the activity around you."
            "kids run between the stalls as vendors shout and wave their wares."
            "the scent of freshly made, questionable-quality food fills the air around you."
            y "man, that smells good."
            t "yeah it does."
            show toi toi08 with dissolve
            t "oooh!"
            y "...i don't think i like that look."
            show toi toi07 with dissolve
            t "come on, i have an idea."
            y "...it's not a good idea, is it?"
            t "maybe!"
            hide toi with dissolve
            y "....."
            y "let's do this!"
            show black with dissolve
            "a carriage rolls up... it's obviously the vehicle of a wealthy individual."
            "toph tells you to follow her lead and earthbends an unmoving rock in the road."
            "the carriage slams to a halt and toph hides the rock while lying down near where it was - pretending to have been run over."
            "a man jumps out of the carriage and scurries to her, clearly worried."
            "you threaten to report him to the dai lee if he doesn't pay you for your silence."
            $ emoney =+25
            play sound "audio/money.mp3"
            "you got 25 coins!"
            "it's not much, but the man runs away before you can complain."
            hide black with dissolve
            y "....that's it?"
            y "we could have made that from pretty much any other scam..."
            show toi toi07 with dissolve
            t "that was fun, though."
            t "love to make these rich farts squirm."
            show toeg toeg03:
                xzoom -1
            with dissolve
            dl "hey! you! i saw the whole thing!"
            show toi toi06 with dissolve
            t "oh."
            y "shit."
            dl "you're coming with me!"
            show toi toi07 with dissolve
            t "gonna have to catch us first, slow poke!"
            hide toi with moveoutright
            y "shit!"
            scene black with dissolve
            "you sprint after toph, the dai lee hot on your trail."
            "you manage to sprint your way through alleys and shops, eventually losing the guard."
            scene bg_alley_epalace
            show toi toi02
            with dissolve
            t "oof... haha... that was great!"
            y "it would honestly been less work to just fight that guy."
            show toi toi07 with dissolve
            t "where's the fun in that?"
            t "come on, we can probably go back to the market."
            y "sure, why not, let's go walk all the way back, risk getting arrested, and then probably have to run some more."
            t "yeah!"
            y "you know that i was being sarcastic!"
            scene black with dissolve
            scene market_general
            show toi toi04
            with dissolve
            y "....."
            t "....."
            t "looks like we're in the clear."
            y "yeah..."
            t "that was fun!"
            y "was it?"
            t "i've been needing to blow off some steam."
            y "well, if you're looking for something to blow..."
        "fountain":

            y "how about the fountain?"
            show toi toi07 with dissolve
            t "i hear it's pretty."
            y "i think so."
            play sound "audio/earthquake.mp3"
            scene basingse_outerwall
            hide toi
            show toi toi07
            with sshake
            $ renpy.pause(0.5)
            t "path is now open! come on!"

            stop music fadeout 1
            play music "audio/jangles.mp3"
            scene black with dissolve
            scene bk3_bg_fountain
            show toi toi04
            with dissolve
            y "here we are!"
            show toi toi09 with dissolve
            t "what smells like watersports?"
            y "the fountain."
            show toi toi06 with dissolve
            t "oh."
            y "...there's a dude over there selling a rat on a bun."
            show toi toi04 with dissolve
            t "you know, this city really is pretty."
            y "seriously... a rat. on a bun."
            t "i know there's a lot of problems here..."
            y "who would buy- okay, there's a guy buying one."
            y "why?"
            show toi_blink with dissolve
            y "there's a churro vendor right next to him."
            y "there are so many other options."
            show toi toi06 with dissolve
            y "he could pick literally any other option."
            y "i'm telling you, some people just-"
            show toi toi05
            hide toi_blink
            with dissolve
            t "stop focusing on the rat man!"
            y "that... would be a terrible superhero."
            y "ratman: an orphan with 200 siblings."
            show toi toi06 with dissolve
            t "...."
            t "can you stop talking about rats?"
            y "sure."
            y "....."
            y "it kinda smells good though, doesn't it?"
            t "....."
            y "does it smell good to you?"
            t "....."
            y "should we try-"
            show toi toi05
            show toi_blink
            with dissolve
            t "ugh! you're impossible!"
            y "aw... thanks."
            hide toi_blink with dissolve
            t "you know that wasn't a compliment!"
            y "sorry, sorry, you're right."
            y "we're here at the fountain... let's enjoy ourselves."
            show toi toi04 with dissolve
            t "that's better."
            t "you know, it kinda does smell good."
            show toi toi07 with dissolve
            t "i wonder if we should-"
        "house":

            y "how about that house that we were in for all of two minutes?"
            show toi toi07 with dissolve
            t "sure, i'd like to see it again."
            play sound "audio/earthquake.mp3"
            scene basingse_outerwall
            hide toi
            show toi toi07
            with sshake
            $ renpy.pause(0.5)
            t "path is now open! come on!"

            stop music fadeout 1
            play music "audio/jangles.mp3"
            scene black with dissolve
            scene basingse_home_1
            show toi toi04
            with dissolve
            t "yup, that's it all right."
            show toi toi04 with dissolve
            t "you know, i feel like we haven't really taken advantage of this place."
            y "it's shown up a few times."
            y "it's had it's uses."
            show toi toi09 with dissolve
            t "like when?"
            y "well someone was kidnapped here, and...."
            y "...."
            y "huh."
            t "what?"
            y "nothing, i'm just realizing this is a totally wasted space."
            t "maybe... it doesn't have to be."
            y "what do you mean?"
            show toi toi04 with dissolve
            t "just that... i mean... we're gonna stop long feng and take back the city."
            t "right?"
            y "right..."
            t "...and the fire nation could break through any day, but..."
            t "...if there's a bit of peace..."
            show toi_blush with dissolve
            t "...maybe you and i could make it... kind of our own."
            y "a nice house just for us?"
            show toi toi05 with dissolve
            t "or whatever. i'm not attached to it. i don't care."
            show toi toi06
            show toi_blink
            with dissolve
            t "...."
            y "i like that idea, toph."
            show toi toi04
            hide toi_blink
            with dissolve
            t "you... do?"
            y "having you all to myself in this nice house?"
            y "i'm thinking of taking that tight littly body for a spin right now."
            show toi toi07 with dissolve
            t "*giggle*"
            y "oh, shit. i love it when you giggle."
            t "shut up! i didn't giggle!"
            t "well, maybe i-"

    if meangirls_escapedmaze >=2:
        show toi toi09
        show totu totu03:
            xpos -300
        with Dissolve(1.5)
        t "what the..."
        if meangirls_escapedmaze ==2:
            "red" "oh, hey... avatar..."
            "red" "how... how are you...?"
            t "hmm?"
            "red" "um... t-thanks for freeing us."
            y "what's going on with you?"
        else:
            "red" "oh, hey!"
            "red" "how are you, avatar?"
            y "I'm fine..."
            "red" "it's so cool that we know you now."
            "red" "you should totally come to parties with us."
            y "thanks, but I think i'll pass."
            "red" "aww..."

        "red" "you're just... so intimidating..."
        y "Okay..."
        "red" "you...."
        hide totu
        show tomm_mgirls clothed:
            xpos -150
        with dissolve
        "red" "...you're so cool!"
        y "....."
        y "come again?"
        "red" "we're totally afraid of you! and super impressed!"
        "white" "we are!"
        y "...."
        hide tomm_mgirls
        show totu totu03:
            xpos -300
        with dissolve
        "pink" "you got us out of those scary tunnels..."
        y "actually, you have toph to thank for that."
        "red" "who?"
        show toi toi06
        show toi_blink
        with dissolve
        y "the girl next to you."
        y "if not for her, i wouldn't have rescued you."
        "white" "oh, wow..."
        "red" "toph, was it?"
        t "...yes..."
        "red" "i am so, so sorry for how we treated you."
        show toi toi09
        hide toi_blink
        with dissolve
        t "huh...?"
        "pink" "yeah, it was really wrong of us."
        "white" "i hope you can forgive us."
        t "i... yeah... sure..."
        hide totu
        show tomm_mgirls clothed:
            xpos -150
        with dissolve
        "red" "and since you're friends with this guy, you must be the coolest chick around!"
        y "she is."
        show toi_blush with dissolve
        t "oh... um..."
        "red" "he turned us down, but you're totally welcome at our parties if you ever want to come."
        t "i... think i'll pass, too."
        t "thanks though..."
        "red" "oh... well, okay."
        "red" "yeah, i'm sure you guys are way too cool for our lame parties..."
        "red" "if you ever change your mind, though..."
        "red" "well, see you around!"
        "white" "bye, sexy!"
        "white" "and bye, avatar!"
        show toi toi10
        with dissolve
        t "wait, did she just-"
        hide tomm_mgirls with dissolve
        show toi toi09 with dissolve
        t "that... was so weird."
        show toi toi07 with dissolve
        t "and awesome!"
        t "they thought i was cool!"
        show toi toi04 with dissolve
        t "i mean, i don't really care, but it's still nice to be recognized for the badass i am."
        y "right."
        t "you know..."
        t "i'm impressed with you, too."
        y "i am amazing."
        t "no, shut up."
        t "seriously... you saved them, and gave me the credit."
        show toi toi07 with dissolve
        t "and they were so afraid of you!"
        t "now {i}that's{/i} power!"
        show toi toi04 with dissolve
        t "i don't get to see the hero side of you very often."
        t "it's... kinda awesome."
        t "and you seem totally capable of helping with..."
        show toi toi06
        with dissolve
        t "...nevermind."
        y "what?"
        t "no, nevermind."
        y "toph, i want to help."
        y "what's wrong?"
        y "is it about your family?"
        t "i don't want to talk about-"

    dl "it's the avatar!"
    show toi toi05
    hide toi_blush
    with dissolve
    t "ugh, damn!"
    t "the guards again."
    t "let's split up - we're more likely to lose them that way."
    y "you sure?"
    show toi toi04 with dissolve
    t "yeah."
    t "we'll meet back here after we lose them."
    y "if you're sure..."
    show toi toi07 with dissolve
    t "let's go!"
    t "come on, you coppers!"
    hide toi with moveoutright
    "toph backs up and sprints off as guards appear."
    show toeg toeg01:
        xzoom -1
    with moveinleft
    dl "i'll take this one!"
    hide toeg with moveoutright
    show toeg toeg03:
        xzoom -1
    with moveinleft
    dl "you!"
    y "well... hi?"
    dl "you're not getting away."
    y "oh look, a poor person!"
    dl "where?!"
    hide toeg with moveoutleft
    dl "I'll beat them within an inch of their life!"
    y "that was too easy."
    y "i should get out of here before he realizes he's an idiot."
    show black with dissolve
    "you run off in the opposite direction from toph as the guard realizes he's supposed to be chasing you."
    "sprinting through the streets, you eventually lose him by hiding behind some ale casks."
    "you carefully make your way back to the meeting point."
    hide black with dissolve
    y "....toph?"
    y "hello?"
    y "...."
    y "i guess i'll wait."
    show black with dissolve
    "you hide in an inconspicous location for over an hour."
    "toph eventually reappears just as it's getting dark."
    hide black
    show toi toi09
    show blackveil
    with dissolve
    y "hey..."
    y "everything okay?"
    t "no. hmm? i mean... yes."
    t "i... think?"
    t "i need to think about somethi-"
    dl "there they are again!"
    y "damn it! these assholes are relentless!"
    y "come on toph, let's get out of the city."
    t "we should... what?"
    y "oh, for-"
    "you grab her arm and pull her towards the city wall as the guards approach."
    scene black with dissolve
    "the two of you wind your way through the various stands, buildings, and people, with the guards in tight pursuit."
    y "toph, open the wall!"
    "realizing she's wrapped up in whatever has her distracted, you open up a path yourself, breaking through the wall and exiting into the field outside."
    y "finally!" with hpunch
    scene expression "bk3/toph/walk/background.jpg"
    show totw totw01
    with Dissolve(1)
    y "toph? you with me?"
    t "yeah... sorry."
    t "i was... distracted."
    y "i noticed."
    y "come on, let's keep walking."
    y "we're on the wrong side of the city, we're gonna have to circle around it to get back to the village."
    hide totw
    hide expression "bk3/toph/walk/background.jpg"
    show expression "bk3/toph/walk/background.jpg":
        xpos -1000
        linear 40 xpos 0
        repeat


    show totw totw01:
        ypos 0
        linear 2 ypos 20
        linear 2 ypos 0
        repeat
    with Dissolve(1.0)
    "you begin walking, choosing a comfortable pace."
    "toph seems thoughtful beside you."
    y "want to talk about it?"
    t "not... right now."
    y "what happened?"
    t "what do you mean?"
    y "obviously something happened after we split up."
    y "you were gone a long time."
    t "oh, i just... had a talk with someone."
    t "i'll tell you about it later."
    y "you know... only you could turn an easy walk into a exhausting adventure."
    show totw totw04
    t "hahah!"
    t "it's not my fault!"
    y "i'm in the city all the time and never have a problem..."
    t "you just don't know how to live!"
    y "hey, i like living! what i don't like are prison cells..."
    t "don't be a baby."
    show totw totw01
    t "but... "
    t "sorry it was such a disaster."
    y "ah, it wasn't a disaster."
    y "i like your company..."
    show totw totw00 with Dissolve(1.5)
    "the two of you walk in a comfortable silence for a while."
    y "damn, this city is huge."
    y "how long have we been walking?"
    t "why, are you in a hurry?"
    y "...no, i like spending time with you."
    y "even if it is time spent walking."
    t "hey..."
    t "do...."
    t "do you ever think i'm too-"
    dl "i found them!" with hpunch
    y "oh, fuck me!"
    show totw totw01 with dissolve
    t "come on, aang!"
    t "we'll beat them!"
    scene black
    scene expression "bk3/toph/walk/background.jpg"
    with dissolve
    "toph sprints off."
    y "aarghgh!"
    y "i hate running!"
    y "get a vehicle or stand still!"
    y "hold on, i'm right behind you..."
    show expression "bk3/toph/walk/background.jpg":
        xpos 0
        linear 2 xpos 1000
        repeat
    show totw totw100:
        xpos -300
        linear 4.0 xpos 300
    pause(5.0)
    show totw totw100:
        xpos 300
        easein 2.0 xpos 600
        easein 2.0 xpos 300
        repeat

    t "good to see you again, slow poke!"
    y "i. am. so. tired. of. running!"
    t "quit whining!"
    t "you took a break!"
    y "for like two minutes!"
    t "it's refreshing!"
    t "doesn't this feel good?"
    t "i've been needing to get some exercise in!"
    t "i hate being cooped up!"
    y "you're insane!"
    y "this isn't fun!"
    y "this is torture!"
    t "less complaining, more running!"
    y "hhrrrghh!"
    scene black with Dissolve(1)
    "you and toph run all the way back to the village, finally losing the guards completely in the process."
    scene toph_home_outside
    show tonf tonf15
    show blackveil
    with Dissolve(1)
    t "that was great!"
    y "...you and i have very different definitions of that."
    t "i'm gonna go to bed... want to come in?"
    y "i... am... going... to... collapse..."
    y "die... here... on... stoop..."
    t "so... is that a yes or a no?"
    y "...i'm going back to my place for the night."
    y "I am definitely mad at you for this..."
    t "aw, it was good for you."
    t "sleep well, aang!"
    hide tonf with dissolve
    "toph heads inside as you stumble to your house."
    scene black with dissolve
    scene inside_shack
    if jd_house and jd_house_addressed:
        show toji toji14
    with dissolve
    if jd_house and jd_house_addressed:
        jd "welcome-"
        show jd_idle_surprise
        with dissolve
        jd "avatar...?"
        jd "are you okay?!"
    y "hello bed!"
    y "i missed-"
    play sound "audio/thud.mp3"
    scene black
    "you pass out before you hit the bed."
    jump love_bk3_next

label jd_full_nelson:
    hide screen earth_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    $ totl_penetrate = 'vag'

    if jd_break_hypno ==4:
        y "so what's this all about?"
        jd "i..."
        jd "i'm just so grateful."

        jd "You've done so much for me and all I can do in return is clean your home."
        y "Don't worry about it."
        y "It was pretty much a pigsty and it's nice to have someone to welcome me."
        jd "Still, I want to... service you in more, other ways."
        y "Other ways? I dunno... "
        jd "Please, if only just once."
        jd "I can keep it a secret if that's your concern."

        menu:
            "Decline for now":
                y "Let's keep that for another time okay?"
                jd "okay..."
                jump love_bk3_village_background
            "Agree":
                y "Well, it's not like I haven't been dipping into whatever is female around here anyway..."
                jd "Great! let me get ready."

    jd "will you... wait here for a moment, sir?"
    y "okay..."
    hide toji with dissolve
    y "what are you doing over there?"
    jd "removing my clothes, sir."
    y "neat."
    y "oh, leave on the hat!"
    jd "...of course, sir."
    if jd_break_hypno ==4:
        jd "There is something that I've always wanted to-"
        y "no strangle-sex."
        jd "Aaaawh!"
        jd "how did you know?"
        jd "and why not?"
        y "Imagine what happens if someone walks in while I'm holding my hands around your throat while fucking you?"
        y "...."
        y "that is a p.r. nightmare that i just don't want."
        jd "Then... could you do a standing full nellson?"
        y "....."
        y "I don't know."
        y "but I guess we'll find out!"


    show totl totl08:
        xpos -10 ypos 20 rotate 20
        linear 2.0 xpos -60 ypos -150 rotate 0
    y "Up you go!"
    hide totl
    show totl totl08
    with Dissolve(1.5)
    jd "oh!"
    y "Hnng... looking good so far!"
    y "Let's do some easy rubbing to prepare you down there."

    show totl totl102
    $ renpy.pause()
    jd "Ah!"
    if jd_break_hypno ==4:
        jd "It's a bit scarier than I thought it would be."
        jd "Hanging in the air only supported by your arms..."
        y "You've got nothing to worry about."
        jd "O-okay, I trust you."


    show totl totl11
    y "I think you're ready for some parting of the lips."


    show totl totl07 with Dissolve(1.5)
    y "Ready to have me inside you?"
    jd "Yes!"

    show totl totl01
    show totl_faceshock
    with vpunch
    jd "Hnnnggg!"
    y "You okay?"
    jd "*ah...!*"
    jd "...yeeaasssh..."
    hide totl_faceshock with dissolve
    jd "I mean... I'm... I'm super okay!"
    y "I'm going to move now."

    show totl totl100
    $ renpy.pause()
    if jd_break_hypno ==4:
        y "You're a lot tighter than I expected!"
        y "Hell, I'm not sure I could get in if it wasn't for the help of gravity!"
        jd "That makes me really happy!"
    y "You're certain this isn't too much for you, right?"
    jd "Ah! Ahbsoluteleeeh!!"
    if jd_break_hypno ==4:
        y "I wasn't sure about this position..."
        y "It seems like something I could only do with Toph..."
        y "but here we are, totally doing it!"
        jd "haha, we... we sure are..."
    y "I'm gonna slam it in! Ready?"
    jd "uhhm..."
    y "Here it comes!"
    show totl totl101
    jd "Hiii!!"
    show ctc
    $ renpy.pause()
    hide ctc
    jd "yes!"
    jd "you... ahnn..."
    jd "you must get so... ah... frustrated and pent... ah... pent up..."
    jd "i hate... *mmmngh...* i hate to see that..."
    jd "use my pussy whenever you feel stressed... sir!"
    y "....."
    jd "let out... ohhh... all your frustrations on me!"
    jd "let me fuck them out of you!"
    jd "slam... ahhn... in and out of cunt until you can... unh... finally relax..."

    show totl totl03
    show totl totl07 with Dissolve(1.5)
    y "Gotta take a little breather."
    y "Oh man... pussy is the best thing ever."
    y "Since we're doing this, would you like to switch it up and do some anal too?"
    y "Maybe give your pussy a little rest?"
    show expression "bk3/joodee/nelson/face_uncertain.png"
    jd "What... what would you prefer?"

    menu:
        "vaginal":
            $ totl_penetrate = 'vag'
            y "your juicy pussy."
            show totl totl01
            jd "Thank the spirits..."
            hide expression "bk3/joodee/nelson/face_uncertain.png"
            y "What?"
            jd "Nothing, I'm just happy my pussy is wonderful enough for you to revisit it!"
        "anal":

            y "your juicy ass."
            $ totl_penetrate = 'ass'
            jd "....."
            y "You... don't want to?"
            jd "Nono... anal is... fine, wonderful."
            jd "Let's do that."
            hide expression "bk3/joodee/nelson/face_uncertain.png"

            show totl totl12
            with vpunch

    if totl_penetrate == 'ass':
        jd "Ahh!!!"
        $ renpy.pause()
        y "You okay, Joodee?"
        jd "I'm fine. I'm fine..."
        jd "Ju-just go ahead."
        show totl totl101
        y "Oh yeahh!"
        y "Visiting misses brown in browntown!"
        y "And here I was thinking your twat was tight!"
        jd "Are you enjoying my little backway?"
        y "Am I?!"
    else:
        show totl totl101
        y "Aaaaand it's back in your tight cunt."
        y "Fuck! I love it in here... it's hot, wet, tight and sucking me in harder than a vacuum!"
        $ renpy.pause()
        jd "Aaah!"

    jd "sir...!"
    y "yes?"
    jd "think... ah... of me as your at-home sex doll."
    y "um..."
    jd "i'll be discreet, of course!"
    jd "you saved my life, and so i'm yours... whatever you... hnnn... need..."
    jd "sex dolls can't reveal secrets, after all!"
    y "......."
    show ctc
    pause
    hide ctc
    y "well..."
    y "toph might get grumpy if she finds out one of the services you provide me is endless fucking."
    jd "think.. ah... of it as... unnh... masturbating..."
    jd "just... using my body to do it..."
    jd "instead of cum... cumming... into... *mmm*... tissues or a toilet..."
    jd "...i'm your designated... ah... cum receptacle."
    jd "just when... whenever you need it..."
    y "....i can't argue with that logic!"
    y "fuck, but I'm reaching my limit here."
    y "Outside or inside!?"
    jd "Where... ah!... do you want it... unh!?"


    menu:
        "inside":
            hide totl
            show totl totl04
            y "Fillin you up... right... {size=+6}NOW!"
            play sound "audio/gltch2b.mp3"  
            with flash
            $ renpy.pause(1.0)
            play sound "audio/gltch2b.mp3" 
            with flash
            $ renpy.pause(1.0)
            play sound "audio/gltch2b.mp3"  
            with flash
            $ renpy.pause(1.0)


            if totl_penetrate == 'vag':
                show totl totl06
                show totl_vagspermdrip
                with Dissolve(1.5)
            else:

                show totl totl06
                show totl_asspermdrip
                with Dissolve(1.5)
        "outside":

            hide totl
            show totl totl03
            show totl totl07 with Dissolve(1.5)
            jd "yes, sir!"
            jd "give me your semen!"

            show expression "bk3/joodee/nelson/sperm_onbody_1.png" with vpunch
            play sound "audio/gltch2b.mp3" 
            $ renpy.pause()
            show expression "bk3/joodee/nelson/sperm_onbody_2.png" with vpunch
            play sound "audio/gltch2b.mp3"
            $ renpy.pause()
            show expression "bk3/joodee/nelson/sperm_onbody_3.png" with vpunch
            play sound "audio/gltch2b.mp3"
            $ renpy.pause()

    $ renpy.pause()
    y "That was more than worth it!"
    jd "thank you, sir..."
    jd "let me know... any time..."
    y "oh, i will, joo dee."
    y "i will."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head to your room and fall fast asleep."
    $ jd_break_hypno = 5
    jump love_bk3_next

label cabbages:

    scene black

    show expression "ebackgrounds/fountain/bg_fountain_day.jpg"

    show toxa toxa05:
        xzoom -0.2 yzoom 0.2
        xpos -400 ypos 0

    show expression "bk3/cabbages/fountain_cover.png"
    show bk3_fountain_water:
        xpos 369 ypos 211

    cbg "Cabbages for Sale!!"
    cbg "Buy your cabbages here!!"


    show toxa toxa05:
        xzoom -0.5 yzoom 0.5
        xpos -400 ypos 110
        linear 19.0 xpos 1500 ypos 110
    $ renpy.pause(13.0, hard=True)


    cbg "They're green, they're round, and the size of big boobies!"


    hide expression "bk3/cabbages/fountain_cover.png"
    hide toxa

    show toxa toxa05:
        xzoom 1.0 yzoom 1.0
        xpos 1000 ypos 100
        linear 9.0 xpos 300 ypos 100
    $ renpy.pause(9.0, hard=True)

    show toxa toxa06:
        ypos 100 xpos 300



    show expression "bk3/cabbages/idle_normal.png"
    cbg "Hello, could I perhaps interest you in some fresh cabbages?!"
    y "No."

    show expression "bk3/earth_guards/guard_body_1.png":
        xpos -300 xzoom -1.0
        linear 2.0 xpos 0
    dl "Hey, you."
    dl "Do you have a permit for selling those cabbages?"
    cbg "Yes, all my permits are in order!"
    dl "....you need another \"special\" one."
    dl "Give me 30 gold."
    cbg "But that's all I have..."
    dl "Tough shit."
    dl "Pay up or I'll declare these cabbages unfit for consumption and destroy them."
    dl "Maybe I saw a worm in your cabbages, maybe I didn't... depending on your cooperation."

    menu:
        "Offer to pay for the cabbage guy" if emoney >= 30:
            y "I'll pay if that'll make the both of you leave."
            dl "Wow, look at that... a bleeding heart do-gooder."
            dl "You make me sick, but thanks for the money anyway."
            play sound "audio/money.mp3"
            $ emoney -= 30
            "you spent 30 coins."
            dl "See you next time, pussy."
            hide expression "bk3/earth_guards/guard_body_1.png" with Dissolve(1.5)
            cbg "I'm so sorry mister, but thank you for your help."
            cbg "please have this cabbage for free."
            y "great...."
            play sound "audio/win2.mp3"
            $ bk3_cabbages = 1
            "You got one cabbage!"
            y "ah! it's hot!"
            y "why is it hot?!"
            y "who sells hot cabbages?!"








            show expression "bk3/earth_guards/guard_body_1.png":
                xpos -300 xzoom -1.0
                linear 2.0 xpos 0
            with dissolve
            dl "...."
            y "oh, what now-"
            show expression "bk3/earth_guards/guard_body_1.png":
                linear 0.5 xpos 300
                linear 0.5 xpos 0

            $ renpy.pause(0.6)

            show toxa toxa06:
                linear 0.8 rotate 180 xpos -200

            show toxa toxa06 with vpunch

            hide expression "bk3/cabbages/idle_normal.png"
            show expression "bk3/cabbages/idle_shock.png"
            cbg "{size=+6}MY CABBAGES!!"
            ya "hey!"
            dl "fuck you! and fuck cabbages!"
            y "rrggh...."
        "Give the guard a piece of your mind":

            y "Why don't you go pester someone where I can't see you?"
            dl "Who are you?"
            dl "Some sort of filthy cabbage lover?"
            dl "I bet you like to pretend they're tits and kiss them when you're all alone in your one-room apartment."
            dl "And then you try to stick your dick between them and it doesn't feel good at all."
            dl "And then Hank knocks on your door asking whether you can take over his shift but you've already done that twice!"
            dl "And he never wants to take over your shift!"
            dl "\"Sorry, I'm busy!\""
            dl "\"Sorry, I got a date with my girlfriend!\""
            dl "Well, fuck you Hank! Fuck you and fuck cabbages!"

            show expression "bk3/earth_guards/guard_body_1.png":
                linear 0.5 xpos 300
                linear 0.5 xpos 0

            $ renpy.pause(0.6)

            show toxa toxa06:
                linear 0.8 rotate 180 xpos -200

            show toxa toxa06 with vpunch

            hide expression "bk3/cabbages/idle_normal.png"
            show expression "bk3/cabbages/idle_shock.png"
            cbg "{size=+6}MY CABBAGES!!"
            dl "Oops, looks like I accidentally knocked over the cart."
            dl "They're all squashed and filthy now."
            dl "Guess you should've payed up when you had the chance."

            y "You motherfucker..."

    show expression "bk3/earth_guards/guard_body_1.png":
        linear 20.0 ypos 400
    dl "Why..."
    dl "why are you guys... getting taller?"
    dl "Oh shit! It's me! I'm sinking into the ground!"
    dl "Help! Help me!"

    y "Don't worry."
    y "There's a sewer tunnel beneath you."
    show expression "bk3/earth_guards/guard_body_1.png":
        linear 1.0 ypos 700
    dl "*Aarghurgle gurgle!*"
    cbg "but... my cabbages..."

    y "I'll... just leave now..."
    cbg "wait."
    y "hmm?"
    hide expression "bk3/cabbages/idle_shock.png"
    show expression "bk3/cabbages/idle_normal.png"
    with dissolve
    cbg "i know things just went... bad..."
    cbg "but i've set up a stall in the market if you'd like to meet me there later."
    y "....sure, why not."
    cbg "great! i'll see you there!"
    $ cabbage_quest = True
    jump love_basingse_day1

label cabbage_vendor:







    show toxa toxa06:
        ypos 100 xpos 300
    show expression "bk3/cabbages/idle_normal.png"
    with dissolve
    cbg "Hello! could I perhaps interest you in some fresh cabbages?"
    if cabbage_tylee:
        jump cabbage_menu
    $ cabbage_tylee = True
    y "i'll take a look."
    menu:
        "cabbage - 100":
            if emoney >=100:
                $ emoney -=100
                play sound "audio/money.mp3"
                $ bk3_cabbages +=1
                "you got a cabbage."
            else:
                y "I don't have enough..."
        "back":
            pass

    y "holy shit this is a lot of money to spend on a cabbage."
    y "why? why so much?"
    cbg "i need to make up the loss of my cart exploding."
    y "it looks fine now..."
    cbg "only because i had to take out yet {i}another{/i} loan to get it fixed."
    y "are these the cabbages that fell on the ground?"
    cbg "...cabbages come out of the ground, you know."
    y "{i}that's{/i} a yes."
    cbg "look, i'm just a small business owner trying to-"
    show tf:
        xpos -550
    with moveinleft
    ty "hello, mister cabbage seller!"
    cbg "oh! hello, young miss!"
    cbg "it's good to see you again!"
    cbg "how are you? and would you like a cabbage?"
    ty "you're funny!"
    ty "avatar? what are you doing here?"
    y "um... ditto."
    ty "we're friends."
    y "...why?"
    ty "he's funny!"
    cbg "thank you."
    cbg "...cabbage?"
    y "no!"
    ty "i heard about your poor cart, mister cabbage seller."
    ty "avatar... i hope you'll help him recover his losses."
    y "....."
    y "how...?"
    ty "by buying cabbages, of course!"
    y "why would i do that?"
    ty "hmm..."
    ty "what if i thanked you?"
    y "okay... what are you thinking?"
    ty "well... you put cabbages in your mouth, so..."
    ty "what if i put you in my mouth?"
    ty "would that be fair?"
    cbg "...i'd take you up on that offer..."
    y "no one's talking to you, cabbage man!"
    if bk3_cabbages >=1:
        ty "oh! i see you already have a cabbage!"
        ty "do you want me to go ahead and thank you here?"
        menu:
            "yes please":
                $ cabbage_cart_blow = True
                y "that sounds good to me!"
                ty "okay!"
                ty "um..."
                y "what?"
                ty "...you don't want it, do you?"
                y "the cabbage?"
                y "not really, no."
                y "they're gross."
                cbg "hey..."
                y "they were on the ground!"
                ty "can i have it, then?"
                ty "I really like them!"
                y "sure, go for it."
                ty "thanks!"
                $ bk3_cabbages -=1
                $ ty_cabbages +=1
                "you gave ty lee a cabbage."
                cbg "can i stay?"
                menu:
                    "sure, enjoy the view":
                        y "sure, no harm in a little audience."
                        y "you can watch this girl suck my cock, i don't really care."
                        cbg "i'll stand over here to the side... *ahem*..."
                        y "fine, just don't say a word, or i'll light your cart on fire."
                        cbg "......"
                        y "well said."
                        scene black
                        scene bg_alley_fountain
                        with fade
                        $ cabbage_watch = True
                        jump ty_cabbage_bj
                    "no, you weirdo":

                        y "no, go away."
                        cbg "aww...."
                        cbg "fine, i'll go."
                        cbg "...don't touch the cabbages."
                        y "not even if {i}you{/i} paid {i}me{/i}."
                        hide expression "bk3/cabbages/idle_normal.png"
                        scene black
                        scene bg_alley_fountain
                        with fade
                        jump ty_cabbage_bj
            "not {i}right{/i} here...":

                y "can i raincheck?"
                ty "sure!"
                pass

    ty "if you buy some cabbages, come visit me in my room, and i'll thank you!"
    ty "bye, cabbager!"
    cbg "goodbye, dear."
    jump love_basingse_day1

label cabbage_menu:
    menu:
        "cabbage - 100":
            if emoney >=100:
                $ emoney -=100
                play sound "audio/money.mp3"
                $ bk3_cabbages +=1
                "you got a cabbage."
                "you have [bk3_cabbages] cabbages."
                jump cabbage_menu
            else:
                y "I don't have enough..."
                jump cabbage_menu
        "exit":

            jump love_bk3_market

label ty_cabbage_bj:
    $ love_ty_bj = True
    hide screen earth_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    $ temp_boolean = False
    if not cabbage_cart_blow:
        scene black
        scene expression "bk3/tylee/footjob/bg_bedroom.jpg"
        with dissolve

    show toth toth19 with dissolve
    ty "Ready whenever you are!"

    show toth toth12 with dissolve
    ty "Hello mister dick!"
    ty "How do you do?"
    y "uh... dicks can't talk..."
    show toth toth20 with dissolve
    ty "I know that! "
    ty "It's just funny to pretend!"
    y "In that case, he likes to be kissed!"

    show toth toth13 with Dissolve(1.5)
    ty "I Have to know him a lot better before I can do that!"
    y "In that case... we should start with a firm handshake."
    y "a firm... long... handshake."

    show toth toth14
    ty "Teehee! It's a pleasure to meet you!"
    y "Likewise! *you say with a low-pitched voice.*"
    ty "Let's shake on it!"
    y "Yes, please!"

    show toth toth15
    ty "How's life going for you, mr. dick?"
    y "Right now life's hard."
    y "veeery hard."
    ty "I'm sorry to hear that!"
    y "Nonono... for dicks, a hard life isn't that bad."
    y "If taken care of the right way, it makes us cry white tears of joy!"
    ty "That's strange! How can I help?!"
    y "A small kiss on the tip helps."
    ty "I guess one little kiss is fine."


    show toth toth01 with Dissolve(.2)
    ty "*smooch!*"
    show toth toth13 with Dissolve(.2)
    y "Maybe a slightly deeper kiss?"

    show toth toth10 with Dissolve(.2)
    ty "*Smoooooch!*"
    show toth toth13

    y "Maybe a sliightly deeper kiss?"
    show toth toth09 with Dissolve(.2)
    ty "*Smoooooooooooch!*"
    show toth toth13 with Dissolve(.2)

    y "Maybe a sliiiiiightly deeper kiss?"
    show toth toth08 with Dissolve(.2)
    "*Smooooooooooooooooooch!*"
    show toth toth13 with Dissolve(.2)


    show toth toth13 with Dissolve(1.5)
    ty "I've changed my mind, mr. dick!"
    ty "After kissing you, I decided... I'm going to eat you!"
    ty "Swallow you whole because you taste so nice!"
    ty "And if I don't succeed the first time, I'll try again and again and again!!"
    y "YES!"
    y "Uh... I mean... ooooh no... please don't eat me!"
    ty "My mind is made up!"
    ty "Please don't struggle, but you can cry if you need to."


    show toth toth100 with dissolve
    ty "Hmmmmm!"

    show ctc
    pause
    hide ctc
    ty "*sluurp* *glurp* *gah*"
    y "He's really putting up a fight, isn't he?!"
    ty "*glp* *shlup*"
    show toth toth13 with Dissolve(1.5)
    ty "He is!"
    ty "What should I do?"
    menu:
        "Just keep trying to swallow him!!":
            $ temp_boolean = True
            show toth toth10
            ty "'ere i go!"
            show toth toth101
            ty "*gagh!* *mmg!*"
        "Shake him until he cries!":


            show toth toth16
            ty "Take this! You naughty dick!"
            ty "I need to shake some sense into you!"
    show ctc
    pause
    hide ctc
    y "fuck!"
    y "Hnnnggg..."
    y "gonna cum... eh, cry... soon!"

    menu:
        "in mouth":
            if temp_boolean == False:
                y "Quick! open your mouth!"
                show toth toth16
                show expression "bk3/tylee/loveblow/openmouth.png":
                    xpos 0 ypos 0
            else:
                hide toth
                show toth toth07

            play sound "audio/gltch2b.mp3" 
            if temp_boolean == False:
                show expression "bk3/tylee/loveblow/spermout_5.png"
                with flash
            $ renpy.pause()

            play sound "audio/gltch2b.mp3" 
            if temp_boolean == False:
                show expression "bk3/tylee/loveblow/spermout_6.png"
                with flash
            $ renpy.pause()

            play sound "audio/gltch2b.mp3" 
            if temp_boolean == False:
                show expression "bk3/tylee/loveblow/spermout_7.png"
                with flash

            $ renpy.pause()
            show toth toth12
            if temp_boolean == False:
                hide expression "bk3/tylee/loveblow/openmouth.png"
                hide expression "bk3/tylee/loveblow/spermout_5.png"
                hide expression "bk3/tylee/loveblow/spermout_6.png"
                hide expression "bk3/tylee/loveblow/spermout_7.png"

            show expression "bk3/tylee/loveblow/sperm_inmouth.png"
            with Dissolve(1.5)
            ty "Hmmm! Delicous tears of joy!"
        "on face":


            hide toth
            if temp_boolean == False:
                show toth toth17
            else:
                show toth toth12

            $ renpy.pause(1.0)
            show expression "bk3/tylee/loveblow/spermout_1.png"
            show toth_blink_temp
            play sound "audio/gltch2b.mp3"    
            with flash
            $ renpy.pause()

            play sound "audio/gltch2b.mp3" 
            show expression "bk3/tylee/loveblow/spermout_2.png"
            show toth_blink_temp
            with flash
            $ renpy.pause()
            show toth toth18

            ty "Are you done crying?"
            play sound "audio/gltch2b.mp3" 
            show expression "bk3/tylee/loveblow/spermout_3.png"
            show toth_blink_temp
            with flash
            ty "You must be really happy!"
            y "*pant* he is."

    show ctc
    pause
    hide ctc
    y "That was divine... Thanks."
    ty "you... really shoot a lot of semen.."
    ty "did you know that?"
    y "I did know that."
    ty "it's so thick... i don't mind though."
    ty "come back again, okay?"
    y "sure thing."
    show toth toth19 with Dissolve(1.5)
    y "Cya later, Ty!"
    show toth toth21 with Dissolve(1.5)
    ty "Bye!"
    scene black with dissolve
    "fully drained, you stumble back to your house and fall asleep."
    $ cabbage_cart_blow = False
    jump love_bk3_next

label haiku_quest:
    hide screen earth_money_date
    scene black
    scene basingse_home_2
    show sokka_idle:
        xzoom -1
    with fade
    y "here it is, home sweet-"
    y "what the hell?"
    show tosi tosi01 with dissolve
    suki "sokka?!"
    suki "what are you doing here?"
    sok "oh... heyyy..."
    y "i... what."
    sok "yeah, i... figured out how to leave those damn tunnels."
    sok "i'll go back in a bit though."
    sok "got a sweet pad down there."
    y "what are you doing here?"
    sok "not... anything... weird, if that's what you're asking."
    y "...it's panties, isn't it?"
    sok "i'm looking for panties."
    y "figures."
    suki "hey, sokka?"
    sok "yeah?"
    suki "i don't mean to be mean, but... i've been doing double shifts, surrounded by people all the time..."
    suki "i need some alone time."
    suki "could you please just go somewhere else today?"
    sok "well things haven't been a cakewalk for me, either."
    sok "trying to avoid being captured by a bunch of crazy amazon-like women with scary masks is tense."
    sok "i could use some relaxation, too."
    sok "so... you get out."
    suki "no, you get out."
    sok "no, you!"
    show tosi tosi03 with dissolve
    suki "No, you!"
    y "hey, guys?"
    suki "what?"
    y "i feel like we're devolving a bit here."
    y "how about we settle this over a little friendly competition?"
    suki "...."
    sok "i'm listening..."
    y "if suki wins, sokka has to leave."
    sok "hey..."
    y "but if sokka wins, suki has to give him a pair of her panties."
    sok "...and i'm in."
    suki "well, i'm not!"
    y "okay, to make it fair... suki can decide what kind of competition."
    sok "aw..."
    suki "okay, fine."
    suki "I agree."
    sok "...fine."
    y "great."
    y "suki, what are you thinking?"
    suki "I'm thinking that sokka is an idiot, so..."
    show tosi tosi01 with dissolve
    suki "...how about a haiku battle?"
    y "a what?"
    sok "yeah, a what?"
    suki "a haiku battle."
    suki "a haiku is a type of poem..."
    suki "5 syllables / 7 syllables / 5 syllables."
    sok "a... poem, really? that doesn't seem all that fun. just... kinda boring."
    y "okay, one point to sokka."
    sok "what?"
    suki "five, seven, then five / syllables mark a haiku / remarkable oaf."
    y "and one point to suki."
    sok "....."
    sok "pucker up your lips, and kiss my sweaty butthole, you're going down bitch."
    suki "it's you going down / how many dicks have you sucked / you reek of semen."
    y "oh... shit."
    y "this is getting real."
    sok "speaking of semen, how is that raggedy cunt? flapping in the breeze?"
    suki "classy as always / such a loud, angry display / is it loneliness?"
    y "okay, maybe we should move on from personal insults to something-"
    sok "you're just like a dog, barking loudly and biting, you just need a bone."
    suki "you're not one to talk / stealing panties from houses / aang has fucked me good."
    y "oh. shit. uh..."
    sok "....."
    sok "...did you have some fucks? because i don't give even one. he fucks everything."
    y "okay, hold on, when did this become about me?"
    suki "he's a better man / you do not even compete / you got stinky feet."
    y "okay, i'm calling it. this is over."
    suki "who wins?"
    sok "yeah, who wins?"
    y "oh shit, i'm the judge?"
    y "yeah, that makes sense."
    y "uh..."
    menu:
        "sokka":
            y "sokka was better."
            sok "yes!"
            sok "suck it, suki!"
            suki "are you serious?"
            suki "his last line had an extra syllable!"
            suki "how were you too stupid to miss that?"
            suki "...i'm not giving sokka any panties."
            sok "what? come on."
            suki "no, because you messed up!"
            suki "i'm leaving."
            y "wait, suki."
            suki "what?"
            y "i'm sure there's a hotel in the city somewhere."
            y "find a nice one and stay there... i'll pick up the tab."
            show tosi tosi01 with dissolve
            suki "you sure?"
            y "yeah."
            suki "thanks, aang!"
            hide tosi with dissolve
            y "bullet dodged."
            sok "....i did fuck up a line though, i'd hoped you guys missed it."
            y "eh."
            sok "well, you gave me more time to look for panties at least."
            sok "here, have this."
            $ bk3_cabbages +=1
            play sound "audio/win2.mp3"
            "you got a cabbage!"
            y "oh, fun."
            y "get me some fiber."
            sok "yeah you will."
            y "have fun."
            sok "will do!"
        "suki":

            y "suki is the winner."
            show tosi tosi01 with dissolve
            suki "yes!"
            suki "suck it, sokka!"
            sok "aw..."
            suki "you thought we didn't catch that extra syllable you threw in that last line!"
            suki "how were you too stupid to miss that?"
            sok "....fine, i'll go."
            sok "but i'm not happy about it."
            hide sokka_idle with dissolve
            y "well done, suki."
            suki "thanks!"
            suki "i'm definitely going to enjoy some peace and quiet today."
            suki "here, for the help."
            $ emoney +=100
            play sound "audio/money.mp3"
            "you got 100 coins!"
            y "nice, thanks."
            suki "see you later!"
    $ haiku_battle = True
    $ bk3_day = False
    jump love_bk3_village_background

label katara_lonely1:
    $ katara_lonely = 2
    hide screen earth_money_date
    ".........."
    k3 "excuse me?" with vpunch
    "you wake up to the sound of raised voices...."
    jd "i said you'll have to leave, he's sleeping."
    k3 "then maybe i'll just join him-"
    jd "i'm sorry, but the master needs his rest."
    k3 "the... master?"
    k3 "does he make you call him that?"
    k3 "it's current year, tell him to get with the times."
    jd "...did you just say \"current year\"?"
    y "ughh.... too much talking."
    k3 "aang?"
    jd "see, you woke him!"
    jd "now, go!"
    y "unbunch your panties, both of you!"
    scene black
    scene inside_shack
    show toji toji11
    show toki toki02:
        xzoom -1
    show toki_angry:
        xzoom -1
    with eye_open
    y "okay, what is this yelling about?"
    hide toki_angry with dissolve
    k3 "heya, aang."
    jd "good morning, sir."
    jd "i tried to make her leave-"
    show toki_angry:
        xzoom -1
    k3 "this big-boobed prostitute tried to keep me out."

    menu:
        "katara is always welcome here":
            y "katara is always welcome here, joo dee."
            show toji toji12 with dissolve
            jd "i just thought that you needed some sleep-"
            y "and i appreciate that, but now you know better."
            show toji toji13 with dissolve
            jd "i...."
            show toji toji14 with dissolve
            jd "....yes, sir."
        "joo dee is right, you should have knocked":
            y "as much as i enjoy your company, you can't just burst into a dude's house."
            y "i might be banging this hooker, here."
            show toji toji13 with dissolve
            jd "i..."
            y "ah, i'm just teasing."
            show toji toji14 with dissolve
            jd "oh. right."
            y "you know i fuck you for free."
            show toji toji15 with dissolve
            jd "yes.... sir."
            y "but seriously katara, you started this by calling her a prostitute."
            k3 "...i might have been slightly too confrontational..."
            k3 "but from now on, she better not stop me from seeing you!"
            y "consider it a done deal."

    hide toki_angry with dissolve
    k3 "right, well, now that that's settled..."
    k3 "want to go to the lake with me?"
    y "really?"
    y "but... it's so early."
    k3 "yeah, it'll be refreshing."
    y "...alright, fine."
    show toki toki04
    show toki_smile:
        xzoom -1
    with dissolve
    k3 "yay!"
    show toki toki01 with dissolve
    k3 "come on!"
    y "after you."
    scene black with dissolve
    "you follow katara down to the lake."
    $ katara_top_nude = False
    $ katara_bottom_nude = False
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_1
    with dissolve
    k3 "isn't it great out here, aang?"
    show toki toki10 with dissolve
    y "i guess... it's early, though."
    k3 "that makes it feel special to me..."
    y "so why are we here?"
    k3 "to... swim?"
    k3 "why else?"
    y "...okay, sure."
    k3 "what?"
    y "it's not like you normally pull me out of bed to go swimming, you know."
    y "is there something you want to talk about?"
    k3 "nah, come on, let's just have some fun!"

    scene black with dissolve
    scene lake_laogai_2
    show toki toki11:
        ypos -70
    show expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve
    k3 "ooo, cold!"
    y "y-y-yeah...."
    y "fffffffuck."
    show toki toki10 with dissolve
    k3 "okay, it just takes a moment to get used to."
    y "m-maybe for you...."
    k3 "it's true, i'm never more comfortable than in the water."
    y "hey, you're wearing clothes."
    k3 "yes...?"
    y "i'm just surprised."
    y "you usually swim naked."
    show toki_swim_blink:
        ypos -70
    with dissolve
    k3 "there's nothing wrong with a little modesty."
    y "there isn't?"
    hide toki_swim_blink
    show toki_swim_oneeye:
        ypos -70
    with dissolve
    k3 "heehee."
    y "i can't believe you're supporting modesty."
    y "what happened to kinky katara?"
    hide toki_swim_oneeye
    with dissolve
    k3 "oh, she's still here..."
    k3 "i just want to keep your imagination intact."
    y "i don't need imagination, i need boobs."
    show toki_swim_smile:
        ypos -70
    with dissolve
    k3 "well in that case, you might just have to woo my clothes off."
    k3 "i'm not a piece of meat, you know."
    k3 "i happen to be a real live girl, believe it or not."
    y "oh, i believe it..."
    y "I've been inside of you."
    show toki_swim_surprised:
        ypos -70
    hide toki_swim_smile
    with dissolve
    k3 "i've got to say, you're terrible at wooing."
    y "no i'm not, i'm just not trying."
    hide toki_swim_surprised
    show toki_swim_angry:
        ypos -70
    with dissolve
    k3 "...."
    k3 "well, why not?"
    y "because it's silly?"
    y "when have i needed to woo you?"
    k3 "well, i remember a time when you had to!"
    k3 "or at the very least spend time with me!"
    k3 "you're more frustrating this time around..."
    y "what do you mean \"this time\"?"
    show toki_swim_blink:
        ypos -70
    with dissolve
    k3 "nothing. never mind."
    y "damn it, katara!"
    y "what do you know?!"
    y "what's happening with these spirits?"
    y "what am i supposed to do?"
    k3 "i... i can't..."
    y "what is it?!"
    hide toki_swim_blink with dissolve
    k3 "I can't tell you!"
    k3 "stop asking!"
    k3 "there's a damn reason!"
    k3 "so stop it!"
    hide toki_swim_angry
    show toki_swim_blink:
        ypos -70
    with dissolve
    k3 "*sigh...*"
    k3 "this is my fault..."
    y "are you gonna tell me anything or not?"
    show toki_swim_surprised:
        ypos -70
    hide toki_swim_blink
    with dissolve
    k3 "are you just going to keep asking me questions that i can't answer?"
    k3 "or are you going to have a nice time with me?"
    y "questions that you can't answer or {i}won't{/i} answer?"
    show toki_swim_angry:
        ypos -70
    hide toki_swim_surprised
    with dissolve
    k3 "stop it, aang!"
    k3 "if you don't want to spend time with me, just say so!"
    y "i'm... sorry."
    y "it's just hard not to push when i know... when i {i}think{/i}... that you have some answers for me."
    hide toki_swim_angry
    with dissolve
    k3 "i don't have answers, aang. i really don't."
    y "i'm sorry."
    k3 "me too."
    show toki_swim_blink:
        ypos -70
    with dissolve
    k3 "*sigh...*"
    k3 "well, i guess this isn't the happy afternoon i was hoping for..."
    hide toki_swim_blink with dissolve
    k3 "well, we both have things to do."
    k3 "let's get back to shore."

    scene black
    scene lake_laogai_1
    show toki toki10
    with fade
    k3 "alright, well..."
    k3 "I'll see you later, aang."
    y "wait, katara..."
    k3 "no hard feelings, aang."
    k3 "really."
    k3 "it's fine."
    k3 "oh, by the way, i found this for you."
    play sound "audio/win2.mp3"
    "you got 1 obsidian!"
    $ obsidian +=1
    y "oh."
    k3 "see you later, handsome."
    hide toki with dissolve
    y "....."
    y "i feel like an ass."
    y "she really tries to make my life better."
    y "....i'm a dick."
    $ bk3_day = False
    jump love_bk3_village_background

label katara_stick_melon:
    scene black
    scene bg_bk3_tophome_day
    show toi toi04
    with dissolve
    y "toph, do you have any idea where i can get a gift for katara?"
    show toi toi09 with dissolve
    t "no, but... why?"
    y "she seems really down."
    t "maybe... you can pick her a flower or something?"
    t "isn't that a thing girls like?"
    y "...aren't you a girl?"
    show toi toi07 with dissolve
    t "no, i'm a badass."
    y "right, i always forget."
    y "where should i look?"
    show toi toi04 with dissolve
    t "how about outside?"
    y "...you're kind of a smart ass, you know that?"
    t "yeah, but am i wrong?"
    y "no..."
    t "then i'll see ya."
    y "mm."
    $ katara_lonely = 5
    scene black with dissolve
    scene bg_training_0
    show stick:
        xalign .4 yalign .4
    with dissolve
    show ctc
    pause
    hide ctc
    y "......"
    y "damn, there's nothing here."
    y "well, i guess there's a stick here."
    y "I could give her that."
    menu:
        "pick up stick":
            y "stick it is!"
            play sound "audio/win2.mp3"
            hide stick with dissolve
            "you got a stick!"
            y "....."
            y "........."
            y "I can't give her a stick!"
            y "i've got to figure something else out."
        "figure out something else":

            y "i should keep looking."

    y "I'll ask toph for any other ideas."
    scene black with dissolve
    "you head back to toph's house."
    scene bg_bk3_tophome_day
    show toi toi04
    with dissolve
    t "any luck?"
    y "no, just a stick."
    t "then maybe give her that?"
    y "i'm not giving her a stick."
    t "she sounds high maintenance."
    y "i'm not looking for commentary, toph!"
    y "do you have any other ideas?"
    t "i mean... outside is pretty much my only idea."
    t "what about that hill where we trained last time?"
    y "that's... not a bad idea."
    y "i'll head there now."
    t "okay... why are you telling me?"
    y "stop. the... sass. you."
    show toi toi07 with dissolve
    t "kay."
    scene black with dissolve
    "you head out to the training hill."
    scene expression "ebackgrounds/cliff.jpg"
    show melon_head:
        xalign .6 ypos .5
        rotate 40
    with dissolve
    show ctc
    pause
    hide ctc
    y "great, an old melon."
    y "....."
    y "well, i'm officially out of ideas."
    y "she's gonna get this."
    play sound "audio/win2.mp3"
    hide melon_head with dissolve
    "you got a melon head!"
    $ katara_lonely = 6
    jump love_bk3_village_background

label katara_sea_trip:
    scene black with dissolve
    scene basingse_city_1
    show expression "bk3/train/train_station_1.png"
    show toki toki01
    show toki_smile
    with dissolve
    k3 "i can't believe we're actually gonna do this!"
    y "you're very excited about this."
    k3 "well yeah!"
    k3 "i've been stuck in that..."
    show toki_blink
    with dissolve
    k3 "no, i'm not going to complain."
    hide toki_blink with dissolve
    k3 "I'm just happy we're going somewhere."
    y "so, where are you thinking?"
    y "do you have a place in mind?"
    k3 "well... i miss the water."
    y "the water?"
    y "we were just at the lake."
    k3 "yeah, but... there's nothing like seeing the ocean."
    k3 "It's so much... bigger."
    k3 "more powerful."
    k3 "and... more romantic."
    y "i get that."
    y "okay, let's go."
    hide toki_smile with dissolve
    k3 "wait."
    k3 "i... i really appreciate this."
    k3 "but i don't want to take you away from your responsibilities."
    y "would you quit worrying about me?"
    y "none of that matters."
    y "{i}you{/i} matter."
    y "and i want to treat you, if i can."
    k3 "oh.... that's...."
    show toki_smile with dissolve
    k3 "okay."
    k3 "let's do it."
    k3 "let's see the sea."
    y "right on."
    k3 "okay, it looks like tickets are 50 coins each..."
    k3 "we still need to get those, right?"
    menu:
        "oh, right... (100 coins)":
            if emoney >=100:
                y "alright, let's get those tickets."
                play sound "audio/money.mp3"
                $ emoney -=100
                show black
                hide toki_smile
                hide toki
                with dissolve
                "you purchase two tickets to the coast."
                $ katara_lonely = 9
            else:
                $ katara_lonely = 10
                y "um... i don't have that much."
                hide toki_smile with dissolve
                k3 "really? oh... uh..."
                y "why don't we just sneak on?"
                k3 "are you sure?"
                k3 "maybe we shouldn't-"
                y "come on, i'm the avatar."
                y "what kind of trouble could we get in?"
                k3 "you know, that's the sort of thing that preceeds someone getting beaten up or put in jail."
                y "we'll be fine."
                y "neither of those will happen."
                k3 "....."
                k3 "i think i can hear my future self complaining about this moment."
                y "come on."
                k3 "....."
                show toki_smile with dissolve
                k3 "ah, what the heck."
                k3 "onward to adventure!"
                y "that's the spirit!"
        "i already have them (lie)":

            $ katara_lonely = 10
            y "i already bought them."
            hide toki_smile with dissolve
            k3 "you did?"
            k3 "when?"
            y "before."
            k3 "before what?"
            k3 "we only just decided to do this..."
            y "look, do you want to go or not?"
            show toki_smile with dissolve
            k3 "i want to go!"
            y "come on then."
            k3 "okay!"

    hide screen earth_money_date
    show black
    hide toki_smile
    hide toki
    with dissolve

    hide black
    show totr totr06
    show toki toki01:
        xpos -200 ypos 100
    with Dissolve(1.5)
    k3 "thanks for this, aang."
    k3 "that you would do this for me..."
    y "you're really worked up about this."
    y "it's just a little trip."
    k3 "it's not, though!"
    y "what d'you mean?"
    k3 "well..."
    k3 "...."
    k3 "...when is this train gonna start?"
    y "they're probably waiting for a few stragglers."
    y "so what did you mean?"
    k3 "it's just-"
    "{b}{i}ding!" with hpunch
    "{b}{i}ladies and gentlemen, the train is now leaving."
    y "well there that is."
    "{b}{i}please have your tickets ready for inspection."
    show expression "bk3/train/train_station_1.png":
        linear 10 xpos 2000
    hide totr
    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    hide toki
    show toki toki01:
        xpos -200 ypos 90
        linear 1 ypos 100
        ypos 100
        linear 1 ypos 90
        repeat
    with sshake


    "{b}{i}thank you for visiting ba sing se."
    show toki toki_smile
    k3 "it's started!"

    jump love_train_hj

label katara_train_cont:
    show screen earth_money_date
    hide totr
    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    show toki toki_smile:
        xpos -200 ypos 90
        linear 1 ypos 100
        ypos 100
        linear 1 ypos 90
        repeat
    with fade
    k3 "well, that was fun."
    k3 "though my hand is sticky..."
    y "i wonder how long this trip is?"
    show toki toki01 with dissolve
    k3 "it shouldn't be long... i think the coast is pretty close by."
    y "ah, that's good."
    y "oh, hey, you were saying?"
    k3 "hmm?"
    y "you were talking about how this trip matters to you."
    k3 "okay, well..."
    show toeg toeg02 with dissolve
    dl "tickets, sir?"
    if katara_lonely ==9:
        y "right here, my good man."
        dl "ah, excellent."
        dl "most people invent these crazy stories."
        dl "and then i have to talk to them."
        dl "and arrest them."
        dl "it's nice when i don't have to do that."
        y "okay..."
        dl "seriously, the stories that people come up with..."
        y "i get it."
        dl "alright, i'll go."
        y "......"
        dl "......"
        y "you... aren't going."
        dl "i'm not?"
        y "no, you're just... standing there."
        dl "oh, my bad."
        dl "here i go."
        y "...."
        dl "...."
        y "you-"
        hide toeg
        show toki toki_angry_blink
        with flash
        k3 "*cough* *cough*"
        "he disappears in a flash."
        k3 "what the heck..."
        y "*cough* *cough*"
        y "where did he get the smoke?"

        y "alright, you were saying?"
        show toki toki01
        k3 "what?"
        y "about the trip?"
        k3 "oh, right."

        k3 "you don't understand, i grew up surrounded by water."
        k3 "it's my element."
        k3 "and my home."
        k3 "and... i barely see it any more."
        y "i'm sorry."
        show toki toki_blink
        k3 "it's okay, it's not your fault."
        y "it kind of is though, right?"
        y "since you're following me around?"
        show toki toki01
        k3 "i'm not \"following you around\", aang."
        k3 "we're trying to save the world."
        k3 "that requires sacrifice from all of us..."
        k3 "you most of all."
        k3 "and i know that."
        k3 "but i can still miss things."
        y "you're right, i didn't mean to be dismissive."
        k3 "it's okay."
        show toki toki_blink
        y "......"
        k3 "......"
        show toki toki01
        k3 "hey..."
        y "yeah?"
        k3 "since you bought the tickets..."
        k3 "I figure i owe you one."
        y "owe me one what?"
        k3 "whatever."
        k3 "one favor."
        k3 "how's that sound?"
        y "great!"
        y "but you know i'm gonna use it for tits, right?"
        show toki toki_smile
        k3 "hahaha!"
        k3 "I guessed."
        scene black
        with Dissolve(1)
        "the two of you chat for a little while."
        k3 "aang!"
        y "hmm?"
        k3 "look!"
        scene bk2_beach01:
            xpos -1000
            linear 10 xpos 0
            repeat
        show expression "bk3/train/train_station_1.png":
            xpos -2000
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        show toki toki_smile:
            xpos -200 ypos 90
            linear 1 ypos 100
            ypos 100
            linear 1 ypos 90
            repeat
        with Dissolve(1)
        k3 "the sea!"
        show ctc
        pause
        hide ctc
        y "it's beachy, for sure."
    else:

        show toki toki01
        y "uh...."
        menu:
            "they're right here":
                y "here you go."
                dl "...."
                dl "you... didn't do anything."
                y "what?"
                dl "you said \"here you go\" and then stayed still."
                dl "do you have tickets, or not?"
                y "sorry, my bad, here they are."
                dl "...."
                dl "you did it again."
                dl "...you don't have any tickets, do you?"
                y "i totally do, they were right here a minute ago..."
                y "maybe they fell onto the floor."
                y "i'll look."
                y "come back in a bit."
                dl "you... are not looking, and i can see the whole floor clearly."
                dl "there are no tickets there."
                y "you got me..."
                y "i'm a magician."
                y "i already put them in your pocket."
                dl "i don't have any pockets."
                y "......"
                y "ta-da?"
                dl "that's it, you're under arrest, come on."
            "i'm five years old, have you seen my mom":

                y "hewo, i'm wost!"
                y "have you seen my mommy?"
                k3 "....."
                dl "......"
                y "......."
                dl "ma'am, is this your idiot?"
                y "hey!"
                dl "what?"
                y "I'm not an idiot!"
                dl "gotcha."
                y "....what?"
                dl "you cheats always fall for the insults."
                dl "sometimes i try racism, sometimes sexism."
                dl "you can't help but correct me, and bam, you give yourselves away."
                y "oh."
                dl "but that \"i'm wost\" thing is the worst line that i've ever heard."
                dl "and i've been doing this for years."
                dl "did you really think that would work?"
                y "i'd hoped."
                dl "come on, get up, you're under arrest."
            "they combusted":

                y "you'll never believe this..."
                dl "uh huh."
                y "they exploded."
                dl "sure."
                y "they did!"
                y "they just caught fire and disappeared."
                dl "that's funny, i don't see any ashes, or smell smoke."
                y "they... were fancy?"
                dl "were they?"
                dl "there should still be some remains."
                y "i... snorted them?"
                dl "you snorted them."
                y "yes?"
                dl "you... snorted your tickets."
                y "i... have a problem?"
                dl "i'll say."
                dl "get up, you're under arrest."
                y "for snorting tickets?"
                dl "for not having tickets, and then giving me a headache."
            "a hobo barreled through here, ate the tickets, jacked me off against my will, exploded into bats, and flew away":

                dl "You too, huh?"
                dl "that keeps happening."
                y "really? that specific event?"
                dl "oh yeah, all the time."
                dl "we get a lot of vampires around here."
                y "......"
                dl "......."
                y "really?"
                dl "no! not really!"
                dl "pay for your tickets, asshole!"
                dl "i'm kicking you off."
                y "while we're moving?"
                dl "standard policy."
                y "that is a terrible policy."
                dl "fine, if you wanna be difficult about it, i'll just arrest you."
                y "i... also don't like that?"
                dl "tough titties."


        k3 "sir?"
        dl "hm?"
        k3 "this is the avatar."
        dl "he's the what now?"
        y "the avatar."
        dl "uh..."
        k3 "do you think the avatar would really do something so stupid as to not have a ticket?"
        y "um..."
        dl "well he-"
        k3 "sir."
        dl "i guess i could be mistaken."
        dl "I'll... go."
        k3 "i hope you've learned a lesson."
        hide toeg with dissolve
        y "yeah, don't be a dick to people that didn't buy tickets."
        show toeg toeg02 with dissolve
        dl "i knew it!"
        dl "alright, you, let's go."
        y "dude, i am the avatar."
        y "you cannot take me."
        dl "hmmm."
        dl "well, i might not be able to fight you..."
        y "that's an understatement."
        dl "but i can prevent you from taking the train back to the city."
        y "oh... uh..."
        dl "tell you what..."
        dl "pay for the tickets... and an additional pain-in-my-ass fee... and i'll let this slide."
        menu:
            "pay (150)":
                y "alright, fine."
                if emoney >=150:
                    play sound "audio/money.mp3"
                    $ emoney -=150
                    dl "very well, sir."
                    dl "have a nice trip."
                    hide toeg with dissolve
                    y "dick."

                    y "so what were you saying?"
                    k3 "about what?"
                    y "about why this trip's important to you."
                    k3 "oh, right."
                    k3 "i've got a bit of a headache..."
                    k3 "can we talk about it in a bit?"
                    y "oh. sure."
                    scene black with Dissolve(1)
                    "you and katara sit quietly for a little bit."
                    k3 "aang!"
                    y "hmm?"
                    k3 "look!"
                    scene bk2_beach01:
                        xpos -1000
                        linear 10 xpos 0
                        repeat
                    show expression "bk3/train/train_station_1.png":
                        xpos -2000
                    show totr totr101:
                        ypos -10
                        linear 1 ypos 0
                        ypos 0
                        linear 1 ypos -10
                        repeat
                    show toki toki_smile:
                        xpos -200 ypos 90
                        linear 1 ypos 100
                        ypos 100
                        linear 1 ypos 90
                        repeat
                    with Dissolve(1)
                    k3 "the sea!"
                    y "nice!"
                    k3 "so what were we talking about?"
                    y "the trip."
                    k3 "ah, it wasn't important."
                else:
                    y "I... don't have that much money."
                    dl "well..."
                    dl "you're the avatar, kind of an ambassador, i get that..."
                    dl "but i can't lose face around these other passengers."
                    dl "they can't think they'll get away without paying."
                    dl "so, if you spend the rest of the trip picking up gum from under the seats, we'll call it even."
                    y "aw shit."
                    k3 "aang..."
                    y "fine, let's do it."
                    scene black with dissolve
                    "you spend the trip picking up old gum."
                    play sound "audio/win2.mp3"
                    "you acquired a big ball of yucky gum!"
                    "...and immediately throw it in the trash."
                    y "....ugh."

                    "you find your way back to your cabin."
                    scene bk2_beach01:
                        xpos -1000
                        linear 10 xpos 0
                        repeat
                    show expression "bk3/train/train_station_1.png":
                        xpos -2000
                    show totr totr101:
                        ypos -10
                        linear 1 ypos 0
                        ypos 0
                        linear 1 ypos -10
                        repeat
                    show toki toki_smile:
                        xpos -200 ypos 90
                        linear 1 ypos 100
                        ypos 100
                        linear 1 ypos 90
                        repeat
                    with Dissolve(1)
                    k3 "welcome back!"
                    k3 "how was your ride?"
                    y "i don't want to talk about it."
                    y "how come you got to stay here?"
                    k3 "after talking to you, he felt bad for me."
                    y "...that dick."
                    k3 "isn't the view pretty?"
                    y "it's beachy, for sure."
            "be stubborn":

                y "no."
                k3 "aang..."
                y "this guy's a dick."
                dl "alright, you're walking back."
                y "fine."
                show toki toki_angry
                k3 "aang!"
                y "okay, alright, i'll pay or whatever."
                dl "too late, dick."
                y "what does that mean?"
                dl "you're the avatar, kind of an ambassador, i get that..."
                dl "but i can't lose face around these other passengers."
                dl "they can't think they'll get away without paying."
                dl "so, if you spend the rest of the trip picking up gum from under the seats, we'll call it even."
                y "aw shit."
                k3 "aang..."
                y "fine, let's do it."
                scene black with dissolve
                "you spend the trip picking up old gum."
                play sound "audio/win2.mp3"
                "you acquired a big ball of yucky gum!"
                "...and immediately throw it in the trash."
                y "....ugh."

                "you find your way back to your cabin."
                scene bk2_beach01:
                    xpos -1000
                    linear 10 xpos 0
                    repeat
                show expression "bk3/train/train_station_1.png":
                    xpos -2000
                show totr totr101:
                    ypos -10
                    linear 1 ypos 0
                    ypos 0
                    linear 1 ypos -10
                    repeat
                show toki toki_smile:
                    xpos -200 ypos 90
                    linear 1 ypos 100
                    ypos 100
                    linear 1 ypos 90
                    repeat
                with Dissolve(1)
                k3 "welcome back!"
                k3 "how was your ride?"
                y "i don't want to talk about it."
                y "how come you got to stay here?"
                k3 "after talking to you, he felt bad for me."
                y "...that dick."
                k3 "isn't the view pretty?"
                y "it's beachy, for sure."

    "{b}{i}*ding!*" with hpunch
    "{b}{i}we are now arriving."
    "{b}{i}*kshh*"
    "{b}{i}i hope you have a better experience than i did the last time i was here."
    "{b}{i}fuck you, bianca! you whore!"
    "{b}{i}enjoy your stay."
    y "...?"
    "{b}{i}what do you mean i can't say that?"
    "{b}{i}look, i drive this fucking thing, i can say what i want."
    "{b}{i}don't do that, you always make this about-"
    "{b}{i}*crackle*"
    "{b}{i}*pop*"
    "{b}{i}*crackle*"
    "{b}{i}...fine."
    "{b}{i}dear, sweet, baby passengers-"
    "{b}{i}-no, shut up, you wanted me to apologize, i'm doing it-"
    "{b}{i}-my outburst was unwarranted."
    "{b}{i}bianca, who serves the drinks, is a nice person."
    "{b}{i}*crackle*"
    "{b}{i}and a whore!"
    "{b}{i}no! it's my microphone! stop it! you can't-"
    "{b}{i}ladies and gentlemen, the driver is-"
    "{b}{i}-i love you, bianca! come back! i'm sorry for-"
    "{b}{i}*crackle*"
    "{b}{i}*sshh*"
    "{b}{i}*pop*"
    "{b}{i}*crackle*"
    y "...."
    y "is that it?"
    y "...."
    y "i like him."

    show expression "bk3/train/train_station_1.png":
        linear 10 xpos 0
    $ renpy.pause(8.2, hard=True)

    hide totr
    scene expression "fbackgrounds/bk2_beach01.jpg":
        xpos 0
    show expression "bk3/train/train_station_1.png":
        xpos 0
    show totr totr06
    hide toki
    show toki toki_smile:
        xpos -200 ypos 100
    with vshake
    "the train comes to a gentle halt."
    k3 "we're here!"
    "{b}{i}*ding!*" with hpunch
    "{b}{i}ladies and gentlemen, we have arrived."
    "{b}{i}i apologize to everyone for my outburst."
    "{b}{i}*kshh*"
    "{b}{i}except bianca."
    "{b}{i}*kshh*"
    "{b}{i}you know what you did."
    "{b}{i}*kshh*"
    "{b}{i}enjoy your stay."
    y "...."
    "{b}{i}not you, bianca."
    y "okay, let's go before they lock the doors and we have to listen to more of that."
    hide toki with dissolve
    show toki toki_smile with dissolve
    k3 "alright!"
    k3 "come on!"
    hide toki with moveoutright
    y "right behind you."
    hide screen earth_money_date
    scene black
    with Dissolve(1)
    play sound "audio/seagull.mp3"
    scene bk2_beach00
    show toki toki_blink
    with dissolve
    k3 "mmmm... breathe in that sea air."
    y "i am."
    y "real fishy."
    y "not my fav."
    k3 "you could be more romantic, aang."
    y "sorry."
    y "i meant to say... yay! fish!"
    show toki toki01 with dissolve
    k3 "....."
    y "....sorry."
    show toki_smile with dissolve
    k3 "i'm just teasing!"
    k3 "come on, walk with me."
    show black with dissolve
    hide black
    show expression "fbackgrounds/bk2_beach01.jpg":
        xpos -1000
        linear 80 xpos 0
        repeat
    hide toki
    hide toki_smile
    show toki toki01:
        ypos 7
        linear 1 ypos 0
        linear 1 ypos 7
        repeat
    with Dissolve(1)
    k3 "this is nice."
    y "yeah."
    show toki toki_blink with dissolve
    k3 "......."
    k3 "hey..."
    y "yeah?"
    k3 "do you... still like me?"
    y "what? of course i do."
    k3 "oh. i'm glad."
    k3 "so..."
    show toki toki01 with dissolve
    k3 "things seem to be going well with toph."
    y "they are."
    y "mostly thanks to you, i think."
    k3 "just trying to help."
    y "you're... really understanding."
    k3 "I have to be."
    k3 "you have a big responsibility."
    k3 "and you need someone in your corner."
    y "and that's you?"
    k3 "that's me."
    k3 "because... i love you."
    y "ah. oh."
    k3 "don't make more of that than you need to right now."
    k3 "you've got toph to focus on."
    k3 "but you should know it."
    show toki toki_blink with dissolve
    k3 "it's not temporary, it's not a phase... i love you."
    k3 "the end."
    y "i... see."
    y "that makes me a lucky guy."
    y "and..."
    menu:
        "i feel the same":
            y "you should know that i-"
            show toki toki01 with dissolve
            k3 "stop."
            k3 "i wasn't looking to complicate things."
            k3 "i just wanted to make sure you knew."
            y "i... okay."
            y "thank you for telling me."
            k3 "you're welcome."
        "thank you for telling me":

            y "thank you for telling me, katara."
            y "that's... an unbelievable gift."
            k3 "for both of us."
            show toki toki01 with dissolve
            k3 "I feel the way I do because you deserve it."
            k3 "i'm not looking to complicate things."
            k3 "just to make sure you know."
            y "I... okay."
            y "thank you."
            k3 "you're welcome."

    show expression "fbackgrounds/bk2_beach01.jpg":
        xpos 0
    hide toki
    show toki toki01
    show katara_lookleft
    with dissolve
    k3 "hey... what's that?"
    y "looks like a little hut."
    k3 "let's check it out."
    scene black with dissolve
    scene bg_maiend_beach1
    show toki toki02
    with dissolve
    k3 "cozy."
    k3 "hey, there's a pack of cards here."
    y "really?"
    k3 "yeah, wanna play something?"
    y "i dunno..."
    y "what do you know?"
    show katara_lookleft with dissolve
    k3 "I'm not really a card person..."
    hide katara_lookleft with dissolve
    k3 "how about a quick game of \"go fish\"?"
    k3 "it's not like we have anything else to do."
    scene black
    scene bg_maiend_beach2
    with fade
    "katara sits in front of you."
    k3_n "ready?"
    y "alright, yeah."
    k3_h "let's just play an easy round, okay?"
    k3_h "doesn't matter who wins?"
    y "sure."
    k3_n "cool."
    $ go_fish_talk = True
    jump go_fish_begin

label after_gf:
    y "i think i've had about all the fun i can take."
    k3_h "aw... okay."
    scene black with dissolve
    scene bg_maiend_beach1
    show blackveil
    show toki toki01
    with dissolve
    k3 "so what now?"
    y "it's getting pretty late..."
    k3 "we can start walking back."
    scene black with dissolve
    scene bk2_beach01
    show blackveil
    show toki toki01
    with dissolve
    k3 "it's so pretty out here..."
    k3 "there's always this sense of... adventure at the beach at night."
    hide toki with dissolve
    y "katara...?"
    "katara walks out towards the water."
    show bg_emberisland_sea_night
    show toki toki01
    with fade
    k3 "isn't it... enticing?"
    y "you're scaring me, katara..."
    k3 "just look."
    hide toki with dissolve
    y "i'm looking."
    show ctc
    pause
    hide ctc
    y "...what am i looking at?"
    k3 "doesn't it pull at you?"
    y "I kinda feel what you mean..."
    k3 "oh, alright... come on."
    scene black
    scene bg_a_beach_00_night
    show toki toki02
    with fade
    y "i thought you were gonna walk out into the ocean and... who knows what."
    k3 "i am a waterbender, you know."
    k3 "water's not scary."
    y "agree to disagree."
    if katara_lonely ==9:
        show toki toki01 with dissolve
        k3 "you know... you still haven't called in that favor."
        y "i haven't, have i?"


        k3 "do you think i'm pretty?"
        y "I do..."
        k3 "yeah?"
        k3 "you like my tight... willing... body?"
        y "yes..."
        k3 "you're such a pervert, aang..."
        k3 "but i guess i don't have a choice."
        k3 "i owe you... something..."

    elif gf_first_win:
        show toki toki01 with dissolve
        k3 "you know... you did win our little game of go fish..."
        y "i remember..."
        k3 "i think that earns you something, don't you?"
        y "...i do think that."
        k3 "do you think i'm pretty?"
        y "I do..."
        k3 "yeah?"
        k3 "you like my tight... willing... body?"
        y "yes..."
        k3 "you're such a pervert, aang..."
        k3 "but i guess i don't have a choice."
        k3 "i owe you... something..."
    else:

        show toki toki01 with dissolve
        k3 "i was thinking..."
        y "yeah?"
        k3 "you've been so wonderful... taking me all the way out here..."
        k3 "i think... that earns you something."
        k3 "don't you?"
        y "...i do think that."
        k3 "do you think i'm pretty?"
        y "I do..."
        k3 "yeah?"
        k3 "you like my tight... willing... body?"
        y "yes..."
        k3 "you're such a pervert, aang."
        k3 "but i guess i don't have a choice."
        k3 "i owe you... something..."

    y "you. naked. now."
    show toki toki04
    show toki_surprised
    with dissolve
    k3 "...right now?"
    y "yeah."
    k3 "here on this... public beach?"
    k3 "Fully nude?"
    y "yes..."
    hide toki_surprised
    show toki_blink
    with dissolve
    k3 "you want... my tits out?"
    y "yes, damn it."
    show toki toki01 with dissolve
    k3 "how about my pussy?"
    k3 "my little... tasty... pussy?"
    k3 "can that stay in my panties?"
    y "no."
    k3 "well, i guess that makes sense..."
    k3 "...since i'm not wearing any anyway..."
    ya "take your clothes off!"
    ya "here, in public, right now, on this beach."
    ya "i want to see your tits!"
    k3 "....."
    scene black with dissolve
    "without another word, katara softly slips out of her dress."
    scene bk2_night00
    show totk totk03
    with Dissolve(1)
    stop music
    play music "audio/Unwritten Return.mp3"
    "she looks up at you with shining eyes... her young, perky breasts fully displayed in the cool night air."
    show ctc
    pause
    hide ctc
    k3 "aren't i good girl, master?"
    k3 "have you gotten a good eye-full?"
    y "not yet, slut."
    show totk totk04 with dissolve
    "you see a shiver a pleasure run through katara." with vshake
    y "(damn, she's... really into this right now.)"
    show totk totk03 with dissolve
    k3 "master?"
    y "you're going to put two fingers in that cute little pussy."
    k3 "right... here?"
    k3 "can't we go somewhere more... private, master?"
    y "do as you are told, slut."
    y "right here on the fucking beach."
    k3 "okay..."
    show totk totk01 with Dissolve(1)
    "katara begins rubbing her pussy lips."
    "she lets out a little gasp as she slips her fingers inside."
    k3 "ahh..."
    k3 "mmmm..."
    show ctc
    pause
    hide ctc
    k3 "ohhh... yes..."
    y "look at you, fingering yourself in public, completely fucking nude."
    k3 "ahh..."
    menu:
        "spit on her tits":
            $ temp_boolean2 = True
            play sound "audio/spit.mp3"
            show expression "bk3/joodee/titplay/spithead.png":
                xpos 100 ypos 180
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 30 ypos -305
            with flash
            "you spit... but miss and hit katara's chin instead."
            "luckily, most of it slides off of her face and onto her tit."
            show totk totk02
            hide expression "bk3/joodee/titplay/spitmouth.png"
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 80 ypos -264
            with dissolve
            "katara slowly looks up at you with surprise, spit dripping its way down around her well-rounded breast."
            "you notice, grinning, that she doesn't even slow down finger-fucking her pussy."

            k3 "you... spit on me."
            y "is that a problem?"

            "katara blinks once, carefully, smiling mischeviously."
            k3 "no."
            show totk totk01
            hide expression "bk3/joodee/titplay/spitmouth.png"
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 30 ypos -305
            with dissolve
            y "want me to spit on you again?"
            k3 "...maybe..."
        "call her beautiful":

            $ temp_boolean2 = False
            y "you're so beautiful, katara."
            show totk totk02
            "katara looks at you warmly, her fingers still working vigorously in and out of her cunt."
            play sound "audio/kiss.mp3"
            with pflash
            "she gives you a warm, wet kiss and pulls back gently."
            k3 "don't ruin the game, love..."
            y "right."
            y "*ahem*"
            y "you want me to spit on you?"
            k3 "...maybe..."

    y "too bad."
    y "stop."
    k3 "w-what..."
    y "i said stop!" with hpunch
    show totk totk00
    if temp_boolean2:
        hide expression "bk3/joodee/titplay/spitmouth.png"
        show expression "bk3/joodee/titplay/spitmouth.png":
            rotate 40
            xpos 80 ypos -264
    with dissolve
    k3 "i... why?"
    y "i can hear your sopping wet pussy... there's no way your little fingers are cutting it."
    y "i mean, look at it."
    scene black
    scene bg_dream
    show background_fade_purpleish
    show blackveil
    hide totk
    show totk totk17
    with fade
    y "you're dripping down your legs."
    k3 "I... i know..."
    show ctc
    pause
    hide ctc
    y "it looks to me..."
    show totk totk14 with Dissolve(1.5)
    "you stand behind katara and slide your hand down over belly as she lifts her arms."
    k3 "oh!"
    y "...like you could use a little help."
    show ctc
    pause
    hide ctc

    k3 "don't... don't tease me, aang..."
    k3 "i'm... i'm aching here..."
    y "what do you want?"
    k3 "i-in... put them in... please..."
    k3 "be... be inside me..."
    y "oh? was i right? do you need help?"
    k3 "...yes! yes, you were right!"
    k3 "please... i need help... i need your help..."
    k3 "will you please-"
    show totk totk11 with Dissolve(1)
    k3 "ohhh... {i}fuck{/i}!"
    show ctc
    pause
    hide ctc
    "you slide two fingers in and out of katara's already very moist pussy."
    k3 "ohh... oh yes... ohh... aang..."
    k3 "spirits, that's... goooood..."
    show ctc
    pause
    hide ctc
    k3 "you got... how did you get so good..."
    k3 "did you practice on a lot of bitches while you were gone?"
    y "...gone?"
    k3 "you... ah... you know what i... ah... mean..."
    menu:
        "A few, but only because I had to!":
            y "If I had the option back then in your village... "
            k3 "...then what?"
            y "I would've fucked you silly every single day without ever moving on."
            y "Your home would permanently reek of semen."
            y "And you'd be known as the girl with the softest, prettiest skin."
            k3 "you're making me... ah... regret you leaving even... mmm... even more..."
        "Yeah, it was great!":

            "The amount of pussy I got...."
            scene black
            scene bk2_night00
            show totk totk00
            with Dissolve(1.5)
            "....you can feel Katara freeze up slightly."
            y "...was unavoidable, but I'm glad it at least helps me to be a better lover for you."
            k3 "That is... true I guess..."
            k3 "Any of them pretty?"
            show totk totk03
            y "Compared to you? Fuck no."
            scene bg_dream
            show background_fade_purpleish
            show blackveil
            show totk totk11
            with Dissolve(1)

    y "you have the sweetest pussy in the world, katara."
    k3 "i'm... unnh... so happy you... ahh... think so..."
    k3 "it's all yours... you're so so so... good with it..."
    k3 "it belongs to you... oh spirits... you really... ah... own this pussy..."
    y "so speaking of skills i gained..."
    y "Let me show you a new trick."
    k3 "what-"
    show totk totk15 with vpunch
    k3 "oh, {i}fuck{/i}!!!"
    "you start finger-fucking her at a furious pace, her whole body bucking against your hand in pleasure."
    k3 "AAAaaaah!!!!"
    k3 "oh, fuck!"
    k3 "oh fuck, aang!"
    k3 "i'm... i'm..."
    y "cum, katara!"
    y "you slut, you little brown slut, i wanna feel you squirt!"
    k3 "ungh... ah... ah...!!!"
    y "who owns you!?"
    k3 "you do!"
    y "who owns you!?"
    k3 "{size=+5}{i}you!!!"

    show expression "bk3/suki/pussyrub/pjuice_1.png" with vshake
    k3 "Aaah!!!"

    show expression "bk3/suki/pussyrub/pjuice_2.png" with vshake
    k3 "AAahh!!"

    show totk totk16
    show expression "bk3/suki/pussyrub/pjuice_3.png" with vshake
    k3 "AAAAAAAAAAAahh!!"
    show ctc
    pause
    hide ctc

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.5)

    k3 "fuck... fuck... fuck..."
    k3 "Okay, I'm not... i'm not complaining, but what.."
    show totk totk17 with dissolve
    "you gently pull your arm away, and katara leans back against you."
    k3 "shit... fuck, my legs are shaking..."
    k3 "what about you?"

    show totk totk06 with Dissolve(1.5)
    "You drop your pants and stick your erect dick in between her legs."
    k3 "oh..."
    k3 "aang... umm..."
    k3 "i love your cock, you know that, but..."
    k3 "it's... it's not safe today..."
    k3 "but... but you can rub against me..."
    k3 "Just... just rub a bit..."
    k3 "i want... i want to feel your cock on my clit..."
    show totk totk05

    show ctc
    pause
    hide ctc
    k3 "oh, spirits..."
    k3 "i should have known you wouldn't be able to keep it in your pants."
    y "are you disappointed?"
    k3 "are you kidding?"
    k3 "you should have started with this."
    k3 "I'm surprised you didn't..."
    k3 "you know how much i love your cock, aang."
    show ctc
    pause
    hide ctc
    "katara's still soaking pussy immediately lubricates your cock..."
    "her wet juices coat your cock as fuck against her warm, plush lips with a velvet smoothness."
    k3 "ahhh..."
    k3 "it's too bad we can't have sex..."
    y "are you sure we can't?"
    k3 "i'm sure... today isn't a safe day..."
    k3 "you can go ahead and cum between my thighs, though."
    y "you're so slick though, it's hard not to accidentally-"
    show totk totk06 with dissolve
    show totk totk07 with vpunch
    k3 "ah!"
    k3 "a-aang!"
    k3 "y-you're inside me!"
    show ctc
    pause
    hide ctc

    y "fuck you're tight... and wet..."
    show totk totk08 with Dissolve(1.5)
    k3 "unnh..."
    k3 "what... ah... are you... {i}fuck...{/i} doing...?"
    show ctc
    pause
    hide ctc
    y "i'm using your body... is that a problem?"
    k3 "my pussy is... unh... yours to use whenever, aang..."
    k3 "you know that..."
    k3 "I just want to remind you... mmmgh... it's not... ah... safe..."
    y "who gives a shit?"
    menu:
        "rub her tits while you fuck her":
            $ temp_boolean = True
            y "Lift your arms."
            show totk totk09 with dissolve
            k3 "why...?"
            show totk totk10 with dissolve
            "You start kneading her tits tenderly as you slide your shaft in and out of katara."
            k3 "ohhhh.... fuck, you know me..."
            show ctc
            pause
            hide ctc
        "keep going like this":
            $ renpy.pause()
            pass

    k3 "we... we shouldn't be doing this..."
    k3 "what are we doing..."
    y "i'm enjoying your body."
    if temp_boolean:
        y "...and your big, warm tits."
    y "and you don't seem to be stopping me."
    k3 "i... i can't... i'm... oh... i'm powerless with you..."
    k3 "whatever... whatever you want... whatever you need..."
    k3 "take it..."
    show totk totk08 with Dissolve(1)
    y "Okay, then."
    y "you asked for it."
    show totk totk100
    show ctc
    pause
    hide ctc
    "you start pumping your hard cock into Katara's tight pussy at a higher speed."
    k3 "HHNNnnngg!"

    "old man" "what the..."
    "you look up to see a man walking by, taken aback at the blatant display."
    y "oh, shit."
    k3 "ah! ah! ah!"
    "old man" "youths nowadays!"
    "old man" "no respect for public decency!"
    y "dude, you're... ungh... getting a free show here!"
    y "this isn't indecency, this is a public service!"
    k3 "ohhhh...."
    "old man" "unbelievable!"
    "the man walks away grumbling, but glances back, clearly enjoying the view..."

    k3 "well that... was... unnff... nerve wracking..."
    dap1 "hello again!"
    "the woman from the train has appeared from the other direction."
    k3 "lot of... ah... people!"
    k3 "oh... oh no!"
    y "where did... unh... you come from?"
    dap1 "we all took the same train, you know."
    k3 "we're.. ungh... ah... a little... mmm... busy..."
    dap1 "oh, don't mind me."
    dap1 "i'm going to jill off nearby."
    dap1 "have fun, you two!"
    "the lady disappears in a hurry."
    y "fuck! what is with all these people?"
    k3 "we are... ahh... on a... fuck!... public beach..."
    y "right... right..."
    k3 "ohhhh....!"
    k3 "i'm... i'm getting close again, my love..."
    y "damn, I'm about to cum, too."
    y "Where do you want it Katara? In or outside!?"
    k3 "Whatever... unf! you like!"
    k3 "i'd love to be full of your baby batter, but..."
    k3 "...if you don't want kids, you shouldn't shoot it in me..."
    k3 "unghh.... fuck, i love this cock!"
    y "oh shit you got even tighter!"
    k3 "it feels so good!!"
    y "fuck, i'm gonna cum!"
    menu:
        "Inside it is!":
            $ katara_cum_inside = True
            y "Here... it... comes !"
            show totk totk12
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            k3 "Mmmm...."
            y "Once for fun."
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Twice for making sure."
            k3 "fuck..."
            k3 "i can feel you drowning my womb..."
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "And thrice just because I find it impossible to pull out of you before emptying my sack."

            hide totk
            show totk totk06
            show expression "bk3/katara/rub/sperm_flowout.png"
            with Dissolve(1.5)
            y "....aaand I'm empty."
            k3 "Mmmmmm... I hope you are!"
            k3 "How can your balls contain this much?!"
            y "Spermbending?"
            show ctc
            pause
            hide ctc
        "cum outside":

            hide totk
            show totk totk19
            with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm1.png"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm2.png"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm3.png"
            $ renpy.pause()
            "You barely manage to pull out and cum all over Katara's ass."
            y "You're just too pretty and sexy, Katara!"
            k3 "You're pretty handsome too."
            show ctc
            pause
            hide ctc

    k3 "that felt amazing."
    hide expression "bk3/katara/rub/sperm_flowout.png"
    hide expression "bk3/katara/rub/body_butt_sperm1.png"
    hide expression "bk3/katara/rub/body_butt_sperm2.png"
    hide expression "bk3/katara/rub/body_butt_sperm3.png"
    play sound "audio/kiss.mp3"
    show pink
    show totk totk03
    show ctc
    pause
    hide ctc
    scene black
    scene bk2_night00
    show totk totk03
    with Dissolve(2)
    if katara_cum_inside:
        k3 "it was dangerous finishing in me, aang..."
        k3 "i'm happy you did, though..."
        k3 "i love how i feel when you're filling me with your... spunk."
        k3 "...do you want to see my belly swell up with your kid?"
        k3 "is that why you came in me?"
        y "maybe."
        k3 "i'm always yours, you know."
        k3 "whatever you'd like to do with me."
        k3 "one thing to keep in mind, though..."
        k3 "we will have to work on toph if i'm going to have your offspring swelling up my belly."
        k3 "we'll worry about that later though, if it happens."
    else:
        k3 "we have to do this again."
        k3 "soon."
        y "we will."
        k3 "i can't be without your cock anymore, aang... i just can't."
        y "i understand, we'll figure it out."
        k3 "we will have to work on toph, but..."
        k3 "we'll worry about that later."

    k3 "oh..."
    k3 "you poor thing, you're a mess."
    y "what? my dick?"
    k3 "yes."
    k3 "come here..."
    hide totk with Dissolve(1)
    scene black
    scene bk2_night00
    show expression "bk3/toph/anal/bodykat0.png"
    show expression "bk3/toph/anal/dick_hold.png"
    with Dissolve(1)
    k3 "every woman should clean her man's cock after sex."
    y "....i couldn't agree more."
    hide expression "bk3/toph/anal/dick_hold.png"
    show expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*shluuurp!*"
    show expression "bk3/toph/anal/dick_hold.png"
    hide expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*ah!*"
    k3 "i taste pretty good...."
    k3 "and so do you."
    k3 "your semen is a gift... especially if your girl makes you cum."
    y "you did do that..."
    k3 "exactly!"
    k3 "the mess is my fault, after all."
    k3 "besides, you have places to go, and things to do!"
    k3 "i can't let you go out there with a cum-and-pussy-juice covered cock..."
    k3 "i have my pride."
    hide expression "bk3/toph/anal/dick_hold.png"
    show expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*mmhh...*"
    "katara gives your cock a final, long, deep suck."
    show expression "bk3/toph/anal/dick_hold.png"
    hide expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*mwah!*"

    scene black with dissolve
    "katara redresses as you pack your cock away."
    scene bg_a_beach_00_night
    show blackveil
    show toki toki01
    with dissolve
    stop music
    play music "audio/Deliberate Thought.mp3"
    k3 "i guess we need to see about the train back, right?"
    y "yeah... luckily the station isn't too far away from here."
    k3 "i think... there are some people over there that saw us..."
    y "yeah, i sort of forgot we were in public once we got going there."
    k3 "me, too!"
    k3 "you're the best, aang."
    y "ditto."
    y "come on."
    scene black with dissolve
    "you head back to the train station."
    "as you approach the ticket desk, a lady hands you two tickets."
    "strange woman" "thanks for the show, this is on me."
    play sound "audio/win2.mp3"
    "you got two tickets!"
    y "uh, thanks?"
    dap1 "no, thank you!"
    dap1 "i haven't squirted like that in ages..."
    "you glance over at katara, who is blushing deeply."
    "it's adorable."
    dap1 "keep him, young lady."
    k3 "y-yes, ma'am."
    "the lady walks off, happily whistling to herself."
    "you find your way to your seats as the train takes off."
    scene basingse_city_1
    show purple_layer
    show blackveil
    show blue_50perc_transparent
    hide totr
    show expression "bk3/train/train_station_1.png":
        xpos -2000

    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    show toki toki01:
        xpos -200 ypos 90
        linear 1 ypos 100
        ypos 100
        linear 1 ypos 90
        repeat

    with fade
    y "hahaha!"
    y "i can't believe that lady..."
    k3 "spirits, that was embarrassing..."
    y "what are you talking about?"
    y "that woman obviously had a good time!"
    y "plus, we got tickets out of it."
    y "it couldn't have gone any better."
    k3 "i guess..."
    y "besides, i don't know about you, but i had a good time."
    show toki toki_smile with dissolve
    k3 "you did, huh?"
    k3 "...me too."
    show toki toki01 with dissolve
    k3 "thanks for... taking care of me tonight."
    y "my pleasure."
    show expression "bk3/train/train_station_1.png":

        linear 10 xpos 0
    $ renpy.pause(8.2, hard=True)

    hide totr
    hide toki
    show expression "bk3/train/train_station_1.png":
        xpos 0
    show totr totr06
    show toki toki01:
        xpos -200 ypos 90
    with vshake
    "with a light jolt, the train comes to a halt."
    "{b}{i}*ding!*"
    "{b}{i}great, we're back, hooray."
    "{b}{i}bianca and i made up, not that anyone cares."
    "{b}{i}all of you get off my train."
    y "...good for them."
    scene black with dissolve
    "you walk katara back to the hospital."
    scene inside_hospital
    show toki toki01
    with dissolve
    k3 "thanks again, aang."
    k3 "I had a great night."
    k3 "come see me again some time and maybe we'll have another quick... date."
    scene black with dissolve
    "with a deep kiss - with tongue - she sends you out, to head back home."
    "you sleep soundly."
    $ katara_lonely = 12
    jump love_bk3_next

label katara_rub_sex:
    $ temp_boolean = False
    scene black with dissolve
    "without another word, katara softly slips out of her dress."
    scene floor_tokt
    show totk totk03
    with Dissolve(1)
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    show ctc
    pause
    hide ctc
    k3 "aren't i good girl, master?"
    k3 "have you gotten a good eye-full?"
    y "not yet, slut."
    show totk totk04 with dissolve
    "you see a shiver a pleasure run through katara." with vshake
    show totk totk03 with dissolve
    k3 "master?"
    y "you're going to put two fingers in that cute little pussy."
    k3 "right here?"
    y "do as you are told, slut."
    show totk totk01 with Dissolve(1)
    "katara begins rubbing her fingers against her pussy."
    "she lets out a little gasp as she slips her fingers inside."
    k3 "ahh..."
    k3 "mmmm..."
    show ctc
    pause
    hide ctc
    k3 "ohhh... yes..."
    menu:
        "spit on her tits":
            $ temp_boolean2 = True
            play sound "audio/spit.mp3"
            show expression "bk3/joodee/titplay/spithead.png":
                xpos 100 ypos 180
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 30 ypos -305
            with flash
            "you spit... but miss and hit katara's chin instead."
            "luckily, most of it slides off of her face and onto her tit."
            show totk totk02
            hide expression "bk3/joodee/titplay/spitmouth.png"
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 80 ypos -264
            with dissolve
            "katara slowly looks up at you with surprise, spit dripping its way down around her well-rounded breast."
            "you notice, grinning, that she doesn't even slow down finger-fucking her pussy."

            k3 "you... spit on me."
            y "is that a problem?"

            "katara blinks once, carefully, smiling mischeviously."
            k3 "no."
            show totk totk01
            hide expression "bk3/joodee/titplay/spitmouth.png"
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 30 ypos -305
            with dissolve
            y "want me to spit on you again?"
            k3 "...maybe..."
        "call her beautiful":

            y "you're so beautiful, katara."
            show totk totk02
            "katara looks at you warmly, her fingers still working vigorously in and out of her cunt."
            play sound "audio/kiss.mp3"
            with pflash
            "she gives you a warm, wet kiss and pulls back gently."
            k3 "don't ruin the game, love..."
            y "right."
            y "*ahem*"
            y "you want me to spit on you?"
            k3 "...maybe..."

    y "too bad."
    y "stop."
    k3 "w-what..."
    y "i said stop!" with hpunch
    show totk totk00
    if temp_boolean2:
        hide expression "bk3/joodee/titplay/spitmouth.png"
        show expression "bk3/joodee/titplay/spitmouth.png":
            rotate 40
            xpos 80 ypos -264
    with dissolve
    k3 "i... why?"
    y "i can hear your sopping wet pussy... there's no way your little fingers are cutting it."
    y "i mean, look at it."
    scene black
    scene expression "ebackgrounds/ceiling_1.jpg"
    hide totk
    show totk totk17
    with fade
    y "you're dripping down your legs."
    k3 "I... i know..."
    show ctc
    pause
    hide ctc
    y "it looks to me..."
    show totk totk14 with Dissolve(1.5)
    "you stand behind katara and slide your hand down over belly as she lifts her arms."
    k3 "oh!"
    y "...like you could use a little help."
    show ctc
    pause
    hide ctc

    k3 "don't... don't tease me, aang..."
    k3 "i'm... i'm aching here..."
    y "what do you want?"
    k3 "i-in... put them in... please..."
    k3 "be... be inside me..."
    y "oh? was i right? do you need help?"
    k3 "...yes! yes, you were right!"
    k3 "please... i need help... i need your help..."
    k3 "will you please-"
    show totk totk11 with Dissolve(1)
    k3 "ohhh... {i}fuck{/i}!"
    show ctc
    pause
    hide ctc
    "you slide two fingers in and out of katara's already very moist pussy."
    k3 "ohh... oh yes... ohh... aang..."
    k3 "spirits, that's... goooood..."
    show ctc
    pause
    hide ctc
    k3 "you got... how did you get so good..."
    k3 "did you practice on a lot of bitches while you were gone?"
    y "...gone?"
    k3 "you... ah... you know what i... ah... mean..."
    menu:
        "A few, but only because I had to!":
            y "If I had the option back then in your village... "
            k3 "...then what?"
            y "I would've fucked you silly every single day without ever moving on."
            y "Your home would permanently reek of semen."
            y "And you'd be known as the girl with the softest, prettiest skin."
            k3 "you're making me... ah... regret you leaving even... mmm... even more..."
        "Yeah, it was great!":

            "The amount of pussy I got...."
            scene black
            scene floor_tokt
            show totk totk00
            with Dissolve(1.5)
            "....you can feel Katara freeze up slightly."
            y "...was unavoidable, but I'm glad it at least helps me to be a better lover for you."
            k3 "That is... true I guess..."
            k3 "Any of them pretty?"
            show totk totk03
            y "Compared to you? Fuck no."
            scene expression "ebackgrounds/ceiling_1.jpg"
            show totk totk11
            with Dissolve(1)

    y "you have the sweetest pussy in the world, katara."
    k3 "i'm... unnh... so happy you... ahh... think so..."
    k3 "it's all yours... you're so so so... good with it..."
    k3 "it belongs to you... oh spirits... you really... ah... own this pussy..."
    y "so speaking of skills i gained..."
    y "Let me show you a new trick."
    k3 "what-"
    show totk totk15 with vpunch
    k3 "oh, {i}fuck{/i}!!!"
    "you start finger-fucking her at a furious pace, her whole body bucking against your hand in pleasure."
    k3 "AAAaaaah!!!!"
    k3 "oh, fuck!"
    k3 "oh fuck, aang!"
    k3 "i'm... i'm..."
    y "cum, katara!"
    y "you slut, you little brown slut, i wanna feel you squirt!"
    k3 "ungh... ah... ah...!!!"
    y "who owns you!?"
    k3 "you do!"
    y "who owns you!?"
    k3 "{size=+5}{i}you!!!"

    show expression "bk3/suki/pussyrub/pjuice_1.png" with vshake
    k3 "Aaah!!!"

    show expression "bk3/suki/pussyrub/pjuice_2.png" with vshake
    k3 "AAahh!!"

    show totk totk16
    show expression "bk3/suki/pussyrub/pjuice_3.png" with vshake
    k3 "AAAAAAAAAAAahh!!"
    show ctc
    pause
    hide ctc

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.5)

    k3 "fuck... fuck... fuck..."
    k3 "Okay, I'm not... i'm not complaining, but what.."
    show totk totk17 with dissolve
    "you gently pull your arm away, and katara leans back against you."
    k3 "shit... fuck, my legs are shaking..."
    k3 "what about you?"

    show totk totk06 with Dissolve(1.5)
    "You drop your pants and stick your erect dick in between her legs."
    k3 "oh..."
    k3 "aang... umm..."
    k3 "i love your cock, you know that, but..."
    k3 "it's... it's not safe today..."
    k3 "but... but you can rub against me..."
    k3 "Just... just rub a bit..."
    k3 "i want... i want to feel your cock on my clit..."
    show totk totk05

    show ctc
    pause
    hide ctc
    k3 "oh, spirits..."
    k3 "i should have known you wouldn't be able to keep it in your pants."
    y "are you disappointed?"
    k3 "are you kidding?"
    k3 "you should have started with this."
    k3 "I'm surprised you didn't..."
    k3 "you know how much i love your cock, aang."
    show ctc
    pause
    hide ctc
    "katara's still soaking pussy immediately lubricates your cock..."
    "her wet juices coat your cock as fuck against her warm, plush lips with a velvet smoothness."
    k3 "ahhh..."
    k3 "it's too bad we can't have sex..."
    y "are you sure we can't?"
    k3 "i'm sure... today isn't a safe day..."
    k3 "you can go ahead and cum between my thighs, though."
    y "you're so slick though, it's hard not to accidentally-"
    show totk totk06 with dissolve
    show totk totk07 with vpunch
    k3 "ah!"
    k3 "a-aang!"
    k3 "y-you're inside me!"
    show ctc
    pause
    hide ctc

    y "fuck you're tight... and wet..."
    show totk totk08 with Dissolve(1.5)
    k3 "unnh..."
    k3 "what... ah... are you... {i}fuck...{/i} doing...?"
    show ctc
    pause
    hide ctc
    y "i'm using your body... is that a problem?"
    k3 "my pussy is... unh... yours to use whenever, aang..."
    k3 "you know that..."
    k3 "I just want to remind you... mmmgh... it's not... ah... safe..."
    y "who gives a shit?"
    menu:
        "rub her tits while you fuck her":
            $ temp_boolean = True
            y "Lift your arms."
            show totk totk09 with dissolve
            k3 "why...?"
            show totk totk10 with dissolve
            "You start kneading her tits tenderly as you slide your shaft in and out of katara."
            k3 "ohhhh.... fuck, you know me..."
            show ctc
            pause
            hide ctc
        "keep going like this":
            $ renpy.pause()
            pass

    k3 "we... we shouldn't be doing this..."
    k3 "what are we doing..."
    y "i'm enjoying your body."
    if temp_boolean:
        y "...and your big, warm tits."
    y "and you don't seem to be stopping me."
    k3 "i... i can't... i'm... oh... i'm powerless with you..."
    k3 "whatever... whatever you want... whatever you need..."
    k3 "take it..."
    show totk totk08 with Dissolve(1)
    y "Okay, then."
    y "you asked for it."
    show totk totk100
    show ctc
    pause
    hide ctc
    "you start pumping your hard cock into Katara's tight pussy at a higher speed."
    k3 "HHNNnnngg!"
    k3 "i'm... i'm getting close again, my love..."
    y "damn, I'm about to cum, too."
    y "Where do you want it Katara? In or outside!?"
    k3 "Whatever... unf! you like!"
    k3 "i'd love to be full of your baby batter, but..."
    k3 "...if you don't want kids, you shouldn't shoot it in me..."
    k3 "unghh.... fuck, i love this cock!"
    y "oh shit you got even tighter!"
    k3 "it feels so good!!"
    y "fuck, i'm gonna cum!"
    menu:
        "Inside it is!":
            $ temp_boolean2 = True
            $ katara_cum_inside = True
            y "Here... it... comes !"
            show totk totk12
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            k3 "Mmmm...."
            y "Once for fun."
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Twice for making sure."
            k3 "fuck..."
            k3 "i can feel you drowning my womb..."
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "And thrice just because I find it impossible to pull out of you before emptying my sack."

            hide totk
            show totk totk06
            show expression "bk3/katara/rub/sperm_flowout.png"
            with Dissolve(1.5)
            y "....aaand I'm empty."
            k3 "Mmmmmm... I hope you are!"
            k3 "How can your balls contain this much?!"
            y "Spermbending?"
            show ctc
            pause
            hide ctc
        "cum outside":

            $ temp_boolean2 = False
            hide totk
            show totk totk19
            with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm1.png"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm2.png"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm3.png"
            $ renpy.pause()
            "You barely manage to pull out and cum all over Katara's ass."
            y "You're just too pretty and sexy, Katara!"
            k3 "You're pretty handsome too."
            show ctc
            pause
            hide ctc

    k3 "that felt amazing."
    hide expression "bk3/katara/rub/sperm_flowout.png"
    hide expression "bk3/katara/rub/body_butt_sperm1.png"
    hide expression "bk3/katara/rub/body_butt_sperm2.png"
    hide expression "bk3/katara/rub/body_butt_sperm3.png"
    play sound "audio/kiss.mp3"
    show pink
    show totk totk03
    show ctc
    pause
    hide ctc
    scene black
    scene floor_tokt
    show totk totk03
    with Dissolve(2)
    if temp_boolean2:
        k3 "it was dangerous finishing in me, aang..."
        k3 "i'm happy you did, though..."
        k3 "i love how i feel when you're filling me with your... spunk."
        k3 "...do you want to see my belly swell up with your kid?"
        k3 "is that why you came in me?"
        y "maybe."
        k3 "i'm always yours, you know."
        k3 "whatever you'd like to do with me."
        k3 "one thing to keep in mind, though..."
        k3 "we will have to work on toph if i'm going to have your offspring swelling up my belly."
        k3 "we'll worry about that later though, if it happens."
    else:
        k3 "we have to do this again."
        k3 "soon."
        y "we will."
        k3 "i can't be without your cock anymore, aang... i just can't."
        y "i understand, we'll figure it out."
        k3 "we will have to work on toph, but..."
        k3 "we'll worry about that later."

    k3 "oh..."
    k3 "you poor thing, you're a mess."
    y "what? my dick?"
    k3 "yes."
    k3 "come here..."
    hide totk with Dissolve(1)
    scene black
    scene floor_tokt
    show expression "bk3/toph/anal/bodykat0.png"
    show expression "bk3/toph/anal/dick_hold.png"
    with Dissolve(1)
    k3 "every woman should clean her man's cock after sex."
    y "....i couldn't agree more."
    hide expression "bk3/toph/anal/dick_hold.png"
    show expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*shluuurp!*"
    show expression "bk3/toph/anal/dick_hold.png"
    hide expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*ah!*"
    k3 "i taste pretty good...."
    k3 "and so do you."
    k3 "your semen is a gift... especially if your girl makes you cum."
    y "you did do that..."
    k3 "exactly!"
    k3 "the mess is my fault, after all."
    k3 "besides, you have places to go, and things to do!"
    k3 "i can't let you go out there with a cum-and-pussy-juice covered cock..."
    k3 "i have my pride."
    hide expression "bk3/toph/anal/dick_hold.png"
    show expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*mmhh...*"
    "katara gives your cock a final, long, deep suck."
    show expression "bk3/toph/anal/dick_hold.png"
    hide expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*mwah!*"

    scene black with dissolve
    "katara redresses as you pack your cock away."
    scene inside_hospital
    show toki toki01
    with dissolve
    k3 "that was lovely."
    k3 "thank you aang."
    y "you are very welcome."
    k3 "see you later!"
    scene black with dissolve
    "you're so wiped, you head home and sleep."
    jump love_bk3_next

label love_jin_date2:
    scene black with dissolve
    "jin takes your arm and walks you out of the village."
    y "where are we going?"
    jin "i found a cozy little spot!"
    jin "it's got a cool statue or something."
    y "uh, alright."
    "the two of you walk out in the fields, bantering good-naturedly."
    show expression "bk3/toph/walk/background.jpg"
    show expression "bk3/toph/walk/rockformation.png"
    show tojn tojn20
    with dissolve
    y "oh."
    y "this... i did not expect."
    jin "weird, right?"
    y "uh, yeah."
    y "maybe we should go, though."
    show tojn tojn23 with dissolve
    jin "why?"
    jin "is something wrong?"
    y "not exactly..."
    y "it's just... last time i was here there was-"
    show expression "bk3/toph/walk/shopgirl.png":
        xzoom -1
    with moveinleft
    girl "hey guys!"
    y "...someone trying to sell me something."
    show tojn tojn20 with dissolve
    jin "hello!"
    y "don't encourage it."
    girl "it?"
    girl "you mean me?"
    girl "that's so mean!"
    jin "yeah, don't be mean, aang."
    y "sorry..."
    y "i was just thinking about the 95 percent profits she's taking from the store."
    y "i mean, sure, I should have set boundaries, but still!"
    jin "aw, you made her sad."
    jin "hey... do you need a kiss?"
    y "i mean, i wouldn't say no..."
    jin "i wasn't talking to {i}you{/i}."
    hide tojn
    show tojn tojn20:
        xpos 0
        linear 1 xpos -350
    girl "oh...!"
    girl "um... i don't know..."
    jin "shhh..."
    jin "close your eyes..."
    hide tojn
    show tojn tojn20:
        xpos -350
        linear 1 xpos -400
    play sound "audio/kiss.mp3"
    show pink with dissolve
    "jin leans in and kisses the girl."
    "the girl's body is a bit stiff at first, but soon responds to jin's gentle tongue-work."
    "jin lifts her lips from the girl's and moves back a few steps."
    hide pink
    hide tojn
    show tojn tojn20:
        xpos -400
        linear 2 xpos 0
    with dissolve
    girl "oh... wow."
    jin "this was fun."
    girl "I'll... you... wow."
    jin "well that was... tasty."
    jin "what do you think, aang?"
    y "i also thought it was tasty."
    girl "um... i'm gonna... that was hot."
    girl "...."
    girl ".........."
    hide expression "bk3/toph/walk/shopgirl.png"
    with moveoutleft
    y "I think you scared her."
    jin "she liked it."
    y "i'm not disagreeing, i'm just saying she ran away."
    jin "she'll figure it out."
    y "damn, jin."
    y "what's gotten into you?"
    jin "I'm... i don't know."
    jin "feeling... liberated."
    jin "empowered."
    y "huh."
    jin "damn, that was so hot..."
    jin "I'm really..."
    jin "hey, are we done here?"
    y "what? this was your idea."
    jin "and i'm done."
    y "i mean... okay."
    jin "let's head back."
    y "sure."
    scene black with dissolve
    "the two of you return to the village."

    stop music
    play music "audio/Smooth Lovin.mp3"
    scene black
    scene inside_brothel_1
    show tojn tojn20
    with dissolve
    jin "thanks for walking me all the way back."
    y "my pleasure."
    jin "wanna see my room?"
    y "i mean..."
    hide tojn with dissolve
    "jin opens her dress, letting it fall to her feet and looking up at you with wide eyes and a cheeky little smile."
    show tojn tojn22
    with dissolve
    jin "you were saying?"
    y "i... i want to see your room."
    "she lets out a mischevious little giggle and tugs on your arm."
    jump love_jin_sex_anal

label love_jin_sex_anal:
    scene black with dissolve
    scene expression "bk3/tylee/footjob/bg_bedroom.jpg":
        xzoom -1
    show totg totg12
    with dissolve
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    "jin settles on the bed, leaning back and presenting her breasts in full display."
    "a look of promise and begging sexuality radiates from her face."
    show ctc
    pause
    hide ctc

    if not love_jin_sex:
        y "...hey."
        "your voice sounds a little rough to you."
        "you clear your throat and try again."
        y "the room looks good."
        "it still comes out hoarse."
        jin "you made this place, right?"
        y "yeah."
        y "with a bit of help."
        jin "i like what you've done with it."
        y "thanks."
        jin "I was actually referring to that thing in your pants."
        y "...oh."
        jin "but making this place a boarding house was a stand-up thing to do."
        jin "...just like this little guy right here."
        y "...please don't call it little."
        y "i'm wildly insecure."
        jin "he doesn't seem bothered."
        y "he basically only ever has one opinion."
        y "so... is there any, uh, coffee? maybe?"
        "you wince at your stupid comment."
        jin "that's not what i need right now."
        y "oh? what do you need?"
        "you have to make a conscious effort not to clear your throat again."
        jin "Mmm... what do you think?"
        y "i think... you're gorgeous, and... have recently undergone some kinda trauma."
        y "(damn you, conscience!)"
        jin "really?"
        jin "because I think that i'm thinking clearly for the first time in ages."
        jin "and i want you."

    jin "so..."
    jin "are you going to fuck me or what?"
    if not love_jin_sex:
        y "what about that \"take it slow\" stuff?"
        "jin shrugs and lowers her head slightly, giving you a lightly submissive glance to go along with her ever-present mischevious grin."
        y "You little minx... you were already planning to give it up, weren't you?"
        jin "i wanted you, and... i wanted to make you want me too."
        jin "and kissing that girl... i thought might entice you."
        y "of course i want you."
        y "look at you."
        jin "now that's what i wanted to hear."
    jin "take off your pants."
    "you drop your clothes and stand at attention."
    show totg totg13 with Dissolve(1.5)
    jin "oh, mmmm..."
    jin "you know how to make a girl feel special."
    show ctc
    pause
    hide ctc
    if not love_jin_sex:
        y "lay back."
        jin "no..."
        y "what?"
        jin "that's not what i want."
    show totg totg09 with Dissolve(1.5)
    jin "I want it hard."
    jin "and deep."
    jin "i want you to fucking wreck me."
    jin "take me from behind."
    show ctc
    pause
    hide ctc
    jin "can you do that?"
    y "i think i can manage."
    show totg totg10 with Dissolve(1.5)
    jin "come on then."
    show ctc
    pause
    hide ctc
    jin "what are you waiting for?"


    show totg totg06 with Dissolve(1.5)
    y "you talk too much."
    y "do you need it?"
    jin "....yes, okay?!"
    jin "I need it bad!"
    jin "I'm in... i'm in fucking {i}heat{/i} here!"
    jin "fucking give it to my pussy!"
    jin "give-"
    $ totg_sex = 'pussy'
    show totg totg07a
    jin "{size=+5}ah!" with hpunch
    show ctc
    pause
    hide ctc
    show totg totg07 with dissolve
    jin "{i}fuuuuck{/i} yes!"
    y "you convinced me."

    y "You're practically drooling down here, so don't mind me foregoing any pleasantries."
    jin "are you joking?"
    jin "fuck me!"
    y "Here I go!"
    show totg totg102
    jin "uuuhhh.... fuck..."
    show ctc
    pause
    hide ctc
    jin "it's... ahh... bigger than i remember..."
    jin "mmmmmmhh...."
    jin "you know exactly at what angle to go in."
    jin "Soooo gooooood..."
    jin "you stiff dick is fucking stuffing me!"
    jin "Mmmmh..."
    y "That's good, because I'm going to give you plenty of this."
    show ctc
    pause
    hide ctc

    show totg totg06 with Dissolve(1.5)
    jin "Awh, don't stop yet!"
    jin "come on!"
    y "Don't worry. I'll put it in again."
    y "But before I do...."
    jin "I want it! i want it!"
    jin "fuck me, aang! fuck me!"
    jin "come on! what are you waiting for?"

    menu:
        y "(where should i fuck her...)"
        "tight pussy!":
            $ totg_sex = 'pussy'
            show totg totg07 with Dissolve(1.5)
            jin "unngh..."
            y "I thought about fucking your ass..."
            y "but decided to concentrate on this tight cunt of yours."
            jin "mmmm... good call..."
            jin "you can stuff my butt later."
        "little asshole":

            $ totg_sex = 'anal'
            show totg totg07a with Dissolve(1.5)
            jin "Ah!!"
            jin "fuck!!!"
            show ctc
            pause
            hide ctc
            show totg totg07 with Dissolve(1.5)
            jin "....fuck yes!"
            jin "Pound my tight little asshole!"
            jin "Plunge it in deep!"
            show totg totg102
            jin "ungh... uh... fuck... unhh... shit... ungh..."
            jin "Just don't... ahnh... stick it back in my pussy after putting it in my ass."
            y "this ass is all i need right now."
            y "Your pussy is safe... for now."



    jin "You... you can get rough if you want."
    y "Things can get pretty wild when I get rough..."
    jin "Good, I like that."
    y "In that case.... one rough ride coming up!"
    show totg totg05a with hpunch
    show totg totg101
    jin "{size=+6}AAAaaahh!"
    show ctc
    pause
    hide ctc
    jin "fuck! yes! more!"
    y "more?"
    jin "more!!"
    show totg totg103

    jin "{size=+6}YESSS!! SMASSHH ITT!!!"
    show ctc
    pause
    hide ctc
    if totg_sex == 'anal':
        jin "{size=+6}SMASH MY ASS TILL IT BREAKS!!! DOO ITTTT!!"
    else:
        jin "{size=+6}BREAK MY CUNT!! SLAM YOUR HARD COCK IN THERE!!"
    show ctc
    pause
    hide ctc
    y "take this, slut!"
    show totg totg104
    jin "{size=+6}AAAaaahh!"
    jin "{size=+6}fuckfuckfuckfuckfuck!!!"
    show ctc
    pause
    hide ctc
    y "HNNNGGG!!!"

    menu:
        "unload inside":
            if totg_sex == 'anal':
                y "i'm gonna fill your slut asshole with cum!"
                jin "yes! yes, i'm a slut! i'm your slut!"
                jin "use me! use my ass! give it all to me!"
            else:
                y "i'm gonna fill your slut pussy with cum!"
                jin "yes! yes, i'm a slut! i'm your slut!"
                jin "use me! use my pussy! give it all to me!"
            hide totg
            show totg totg05

            play sound "audio/gltch2b.mp3" 
            show totg totg05a with hpunch
            jin "ungh!"
            play sound "audio/gltch2b.mp3" 
            with hpunch
            $ renpy.pause(0.7)
            show totg totg05 with dissolve
            play sound "audio/gltch2b.mp3" 
            with hpunch
            jin "damn..."
            $ renpy.pause(0.7)

            if totg_sex == 'anal':
                show totg totg08
                show expression "bk3/jin/analove/sperm_insideass.png"
                with Dissolve(1.5)
            else:
                show totg totg08
                show expression "bk3/jin/analove/sperm_insidepuss.png"
                with Dissolve(1.5)

            jin "there's so much..."
            if totg_sex == 'anal':
                jin "It's flowing out of my ass, even though it's facing up!"
            else:
                jin "it's dripping out of my pussy, even though it's facing up!"
        "outside":
            hide totg
            show totg totg11
            with Dissolve(1.5)
            y "Take this!"
            jin "what are you-"
            show expression "bk3/jin/analove/spermout1.png"
            play sound "audio/gltch2b.mp3"
            show totg totg11a
            with flash
            jin "oh!"
            show ctc
            pause
            hide ctc

            show expression "bk3/jin/analove/spermout2.png"
            play sound "audio/gltch2b.mp3" 
            show totg totg11
            with flash
            jin "ahhh... yeah... cover me..."
            show ctc
            pause
            hide ctc

            show expression "bk3/jin/analove/spermout3.png"
            play sound "audio/gltch2b.mp3" 
            with flash
            show ctc
            pause
            hide ctc
            jin "mmmmmgh... you came so much!"

    jin "And it's so thick!"
    y "Good girls deserve good sperm."
    y "and lots of it."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    scene expression "bk3/tylee/footjob/bg_bedroom.jpg":
        xzoom -1
    show tojn tojn22
    with dissolve
    jin "well that was... satisfying."
    jin "i hope you had fun...."
    jin "I know i did."
    jin "i'll just get dressed..."
    hide tojn with dissolve
    show tojn tojn20 with dissolve
    if totg_sex == 'anal':
        jin "my little butt is still pulsing."
    else:
        jin "my little pussy is still pulsing."
    y "nice."
    jin "heehee... i agree."
    jin "i'll see you later, handsome."
    jin "thanks for the date."
    scene black with dissolve
    "feeling fully drained, you head back to your place and sleep soundly."
    $ love_jin_sex = True
    jump love_bk3_next

label toph_suki_katara_tav:
    hide screen earth_money_date
    scene black
    show expression "bk3/toph/assmassage/background.jpg"
    show toki toki01:
        xzoom -1 xpos 300 ypos -100
    show expression "bk3/toph/assmassage/ass_table_back2.png"

    show toam toam02
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    with fade
    suki "hey! you guys made it!"
    y "for sure."
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    t "of course we did."

    y "so what's up?"
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    suki "\"what's up?\""
    suki "i'm bored is what's up."
    suki "you guys wanna get balls deep some drinks?"
    y "almost usually."
    t "i can try..."
    k3 "i'm not really a drinker."
    suki "four drinks it is!"
    k3 "oh... kay..."
    scene black with dissolve
    "suki pours each of you a drink."
    t "*cough* *cough*"
    t "ugh! that was awful..."
    y "mmm... malty."
    suki "ah..."
    suki "katara, you didn't drink yours."
    k3 "and i'm not going to, sorry."
    y "no need to apologize."
    k3 "i have more fun without alcohol..."
    suki "more for me!"
    y "haha, you've got a fan, katara."
    k3 "thanks guys..."
    t "well i'm not gonna wimp out!"
    y "it's not wimping out."
    t "spoken like a wimp!"
    t "suki! give me another!"

    "the four of you hang out, laughing and drinking deep into the night..."
    scene inside_tavern_night
    show totd totd03:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat
        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat

    show totd totd05:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat
        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat
    with Dissolve(1.5)
    t "is... is a thing abou the stuffs in... *hick*..."
    t "...bitches."
    y "...where did your shirt go?"
    show ctc
    pause
    hide ctc
    t "dunno..."
    t "bet katara took it."
    $ toph_drunk = 'angry'
    t "katana!"
    y "...katara."
    t "righ'."
    t "katana! gimme shirt back!"
    y "you have had way too much."
    t "dun... dun tell me what to do!"
    $ toph_drunk = 'sad'
    t "errybody always... tellin me..."
    t "i'm an *hick* an adult!"
    y "i know... i know... now put that down..."
    show totd totd06
    t "*gulp* *gulp* *gulp*"
    y "...yeah, that'll end well."
    show totd totd05
    t "*sniff*"
    $ toph_drunk = 'smile'
    t "i like your dick!"
    y "and i like not cleaning up puke."
    y "where is katara?"
    show toki toki02:
        xzoom -1
    with moveinleft
    k3 "uh, aang? can you come here for a minute?"
    y "there you are!"
    y "this was a terrible idea."
    y "can you get this bottle away from her?"
    y "maybe just like... waterbend out the wine or whatever?"
    k3 "we've got another problem..."
    y "what?"
    k3 "um, suki is..."
    y "is what?"
    k3 "well... take a look."

    "You hear cheering and turn your head to look at the commotion."
    hide totd
    hide toki
    show black
    with Dissolve(1)
    hide black
    show totd_crowd
    show totd totd25:
        parallel:
            xpos 0
            linear 3.0 xpos 100
            linear 3.0 xpos -100
            linear 3.0 xpos 0
            repeat
        parallel:
            ypos 0
            linear 0.5 ypos 10
            linear 0.5 ypos 0

            repeat
    with Dissolve(1)
    "A highly intoxicated Suki is shaking her tits while walking up and down."
    "A small crowd has formed around her."
    y "...oh, shit."
    show ctc
    pause
    hide ctc
    y "those... those tits are amazing."
    y "so... hypnotic..."

    show totd totd26
    suki "Oh *hick* hey Aang!"
    suki "Do you you come here too?"
    show ctc
    pause
    hide ctc
    y "we... started this night together."
    y "seriously, how did this all happen?"
    suki "jus.. *hick* jus enjoy the show!"
    suki "you wanna fuck 'em? huh? wanna fuck me?"
    suki "you fuck me good."
    show totd totd25
    y "you are super hot, but you should probably put those away."
    suki "no!"
    y "dang, this is a mess."
    y "toph, are you-"
    "You turn your attention back to Toph."
    $ toph_drunk = 'smile'
    hide totd_crowd
    hide totd
    with Dissolve(1.5)


    show totd totd100:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat
        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat


    t "hey... hey, tha's preedy good."
    t "but sheck this out..."
    t "hold bottle, aang..."
    y "uh, hold on-"
    hide totd
    show totd totd101:
        linear 3 xpos 5
        easeout 3.3 xpos -5
        repeat
    with Dissolve(1.5)
    "toph just drops the bottle on the floor and gets up on the table."
    t "Lalalala... *hick*... lalaalaa."
    t "Imma superstar!!"
    t "lalallaaa..."
    menu:
        "Watch Toph":
            y "You're the most sexy of 'em all Toph!"
            y "Now come down from there before you break something."
            t "you're gonna hava cash me first!"
            y "cash?"
            y "oh, \"catch\"."
            y "don't... don't do that."
            y "...when did i turn into the mom here?"

            t "I'm tired.. I'm just gonna close my eyes for a second."
            y "wait, you'll fall-"
            hide totd
            show totd totd00 with hpunch
        "Watch Suki":



            hide totd with dissolve
            show totd_crowd
            show totd totd25:
                parallel:
                    xpos 0
                    linear 3.0 xpos 100
                    linear 3.0 xpos -100
                    linear 3.0 xpos 0
                    repeat
                parallel:
                    ypos 0
                    linear 0.5 ypos 10
                    linear 0.5 ypos 0
                    repeat
            y "hey... so..."
            y "not that i don't appreciate what you're doing here - because i do - but..."
            y "maybe you should put your clothes back on?"
            suki "no!"
            y "*sigh...*"
            y "okay..."
            y "it's not that i don't love the undoubtedly impending rise in customers, but..."
            y "....there's no one to serve drinks."
            y "so it's kinda counter-productive."
            suki "haha!"
            y "........"
            show ctc
            pause
            hide ctc
            y "young lady, put your clothes on!"
            suki "{i}you{/i} put {i}your{/i} clothes on!"
            y "my clothes {i}are{/i} on!"
            suki "lame."
            y "okay, look-"
            show totd
            show totd_crowd
            with hpunch
            play sound "audio/thud.mp3"
            "Suddenly you hear a crash behind you."
            hide totd
            hide totd_crowd
            show totd totd00

            y "Oh shit... Are you okay, Toph?"

    t "hrghh... agh..."
    y "...ouch."
    y "Oh man.. she's wasted."
    y "hey, katara?"
    show toki toki02 with moveinright
    k3 "this is so much fun!"
    k3 "i'm so glad i came!"
    y "...you're fucked up."
    y "i like that."
    y "i'm gonna take toph back to her house and put her to bed."
    y "can you make sure suki's okay?"
    k3 "sure."
    y "thanks."
    y "alright you midget, come on."
    t "eeegrgh...."
    scene black with dissolve
    "you throw toph over your shoulder and carry her back to her house."
    scene bg_bk3_tophome_night
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    show toi toi200
    show toi_blink
    show toi_blush
    with dissolve
    y "okay, here we are..."
    t "toi... toilet..."
    t "dun feel... so good..."
    y "alright, come on."
    scene black
    scene toilet
    with fade
    y "alright, i'll leave you in here."
    y "come out when you're ready."
    scene black with dissolve
    "you wait outside the bathroom."
    "toph eventually stumbles out."
    y "that sounded rough."
    t "ugh... i'm never drinking again."
    y "sounds like a good plan."
    y "how do you feel?"
    t "sucky... but a bit better."
    y "good."
    y "let's get you into your bed, and i'll head out."
    t "okay."
    scene bg_night_tophhome
    show totc totc14a
    with dissolve
    y "there you go, nice and comfy."
    t "hey... thanks for... for taking care of me."
    y "of course."
    t "and not... taking advantage or anything."
    y "what am i, a psychopath?"
    y "get some rest, kid."
    t "will you stay?"
    y "i could, i guess..."
    t "please."
    t "i'd like to have you around."
    y "aw, that's sweet."
    t "...to clean up if i have to toss up again."
    y "that's... less sweet."
    y "aw, man... you threw up {i}in{/i} the toilet right?"
    y "not, like, beside it or something, right?"
    t "I don't remember..."
    t "but you can just waterbend it into the toilet, right?"
    y "i... don't want to try."
    y "but you do sound a lot better."
    y "you're coherent at least."
    t "i feel a lot better now that i've thrown up."
    y "alright, sure, i'll stay."
    show expression "bk3/toph/nightmare/face_amused.png"
    with dissolve
    t "thanks, you!"
    t "I'll scoot over."
    scene black with Dissolve(1)
    "toph moves over and lets you in."
    scene bg_night_tophhome
    show totc totc15
    with Dissolve(1)
    t "mmm... you're cool."
    y "i've always thought so."
    t "no, i mean, i'm really hot."
    y "a little conceited, but yeah, hot."
    show expression "bk3/toph/nightmare/face_angryzoom.png"
    with dissolve
    t "no, i..."
    hide expression "bk3/toph/nightmare/face_angryzoom.png"
    show expression "bk3/toph/nightmare/face_lewdzoom.png"
    with dissolve
    t "i meant that i feel really warm, and you feel really cool against me."
    t "i'm gonna sleep now, okay?"
    y "i wish you would."
    show expression "bk3/toph/nightmare/blink_zoom.png"
    with dissolve
    t "oh, shut up."
    t "...and good night."
    scene black with dissolve
    "you sleep soundly next to toph, secure in the fact that she's already emptied her stomach..."
    "...so you won't have to wake up in a gross puddle."
    y "the things i do out of the goodness of my heart..."
    scene bg_day_tophhome with Dissolve(1)
    y "*yaaawn...*"
    y "toph?"
    $ totx_head = 'happy'
    t "good morning!"
    show totx totx08
    show expression "bk3/toph/shadowfuck/silhouette.png":
        alpha 0.1
    with dissolve
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    "toph plops into your lap, straddling you as you sit up and blink into consciousness." with hpunch
    show ctc
    pause
    hide ctc
    y "*yaaawn...*"
    y "you're in a good mood."
    y "did you... do your hair?"
    hide expression "bk3/toph/shadowfuck/silhouette.png"
    show expression "bk3/toph/shadowfuck/hands.png"
    show totx totx05 with Dissolve(1.5)

    t "yeah, i woke up a little bit ago and started getting ready for the day."
    t "i figured i'd let you sleep."
    show ctc
    pause
    hide ctc
    y "i appreciate that."

    t "you were so wonderful last night..."
    $ totx_head = 'worried'
    t "i thought i'd wake up feeling much worse."
    y "me too, honestly."
    y "i hope suki and katara got home okay."
    t "well, we can go out and see, or..."
    y "...or what?"
    t "or..."
    show totx totx06 with Dissolve(1.0)
    t "...you can take care of the cute girl on your lap?"
    show ctc
    pause
    hide ctc
    y "I can do that."
    $ totx_head = 'careful'
    show totx totx04
    $ totx_head = 'shock'

    t "oh!" with hpunch
    show ctc
    pause
    hide ctc
    y "that what you had in mind?"
    $ totx_head = 'careful'
    t "y-yes..."
    t "ohhh..."
    show totx totx01 with Dissolve(1.5)
    t "hnnnhahhh...."
    show ctc
    pause
    hide ctc
    t "there's so much of you."
    y "i'm impressed you can take it all."
    $ totx_head = 'happy'
    t "Me too."
    t "it's... tight... but amazing."
    $ totx_head = 'careful'

    show totx totx100
    t "mmmmn...."
    show ctc
    pause
    hide ctc
    $ totx_head = 'happy'
    t "...this feels so good!"
    y "what a way to wake up."
    t "heehee...."
    t "good morning, aang!"
    y "good morning, toph!"
    show ctc
    pause
    hide ctc
    t "let's pick things up!"
    $ totx_head = 'lewd'
    show totx totx101
    show ctc
    pause
    hide ctc
    y "oh, daaamn...."
    show ctc
    pause
    hide ctc
    y "I can't hold out any more!"
    y "Here it comes!"
    t "go ahead, aang..."
    t "let it all out in me..."
    t "i want to feel you soak my insides."
    hide expression "bk3/toph/shadowfuck/hands.png"
    hide totx
    show totx totx01

    show totx totx07 with Dissolve(1.5)
    show expression "bk3/toph/shadowfuck/body_5_dick.png" with Dissolve(1.5)
    play sound "audio/splurt2.ogg"
    $ renpy.pause(0.4)
    play sound "audio/splurt1.ogg"
    $ renpy.pause(0.4)
    show expression "bk3/toph/shadowfuck/sperm_inside.png" with Dissolve(1.5)
    play sound "audio/splurt2.ogg"
    $ renpy.pause(0.4)
    t "ahh...!"
    show ctc
    pause
    hide ctc
    t "ohhhgh.... yes...."
    t "fill me up...."
    play sound "audio/splurt3.ogg"
    hide totx
    hide expression "bk3/toph/shadowfuck/body_5_dick.png"
    hide expression "bk3/toph/shadowfuck/sperm_inside.png"
    $ totx_head = 'shock'
    show totx totx01
    show expression "bk3/toph/shadowfuck/hands.png"
    with Dissolve(1)
    t "it's... it's still going!"

    y "fuck!"
    $ totx_head = 'lewd'
    t "yes, sexy! keep... keep pumping... ahhh..."
    t "keep going!"

    t "ahhhh...!"

    t "empty it all... it all in me!"
    show ctc
    pause
    hide ctc
    y "I'm... fuck, i think i'm done..."
    y "I came so hard..."
    $ totx_head = 'worried'
    show totx totx02
    $ renpy.pause(0.3)
    show totx totx03
    $ renpy.pause(0.3)
    show totx totx06
    show expression "bk3/toph/shadowfuck/sperm_outside.png"
    with Dissolve(1.5)
    show totx_spermdrip
    $ renpy.pause()
    t "spirits... that's a lot."
    t "was... i sexy?"
    y "hella."
    $ totx_head = 'happy'
    t "yes!"
    t "i'm so happy...."
    $ totx_head = 'worried'
    t "....."
    t "....wow."
    y "what?"
    $ totx_head = 'lewd'
    t "I can feel it literally gush out of me..."

    t "I think I'll go and clean myself up a bit."
    y "alright, i'll leave you to it, then."
    $ totx_head = 'happy'
    t "okay!"
    $ totx_head = 'worried'
    t "...will you come by again later?"
    y "i'd love to."
    $ totx_head = 'happy'
    t "yay!"
    t "see ya, handsome."
    scene black with dissolve
    jump love_bk3_next

label earthbending_date:
    hide screen earth_money_date
    t "where do you wanna go?"
    menu:
        "outside":
            $ toph_date_walk = "outside"
            y "how about a walk outside?"
            t "sure! okay!"

            scene black with dissolve
            "the two of you head out, walking and chatting..."
            show expression "ebackgrounds/bg_forest_large.jpg":
                xpos -1000
                linear 80 xpos 0
                repeat
            show tonf tonf15:
                zoom 0.88
                xpos 80 ypos 120
                linear 1 ypos 113
                linear 1 ypos 120
                repeat
            with Dissolve(1.5)
        "city":

            $ toph_date_walk = "city"
            y "how about somewhere in the city?"
            t "sure! okay!"
            scene black with dissolve
            "the two of you head out, walking and chatting..."
            scene jasmin_dragon_inside
            show tonf tonf15:
                zoom 0.88
                xpos 80 ypos 120
            with Dissolve(1.5)

    y "...and the heavyset girl said that I had a receding hair line and that I was a couple pounds overweight and I was like 'Go fuck yourself!'"
    y "......"
    y "................."
    if toph_date_walk == "outside":
        y "...where the fuck are we?"
        t "a forest."
    else:
        y "...where are we?"
        t "we're in the tea shop."
    y "okay... why?"
    t "you were talking a lot and we just kinda... wandered this way."
    if toph_date_walk == "outside":
        t "i knew there was one nearby."
    y "huh."
    y "alright, that's on me."
    y "i guess i got wrapped up, didn't i?"
    t "a little bit, but i thought it was funny."
    if toph_date_walk == "outside":
        t "what's that?"
        hide expression "ebackgrounds/bg_forest_large.jpg"
        hide tonf
        show expression "ebackgrounds/bg_forest_large.jpg":
            xpos -500
        show tonf tonf15:
            zoom 0.88
            xpos 80 ypos 120
        with Dissolve(1)
        y "Looks like... some kind of arch."
        t "it's pretty."
        t "do you think that's natural?"
        t "or someone made it?"
        y "I don't know."
        y "...but i know there's no one i'd rather see it with."

    if toph_date_walk == "city":
        t "I like these little places."
        t "i never got to go out much before we started traveling together."
        t "i know that a tea shop probably isn't exciting for you, but..."
        t "i like being out."
        t "and i like being out with you."
        y "you're right that it's not exciting."
        t "oh..."
        y "but you make it exciting."

    show tonf tonf17 with dissolve
    t "aang, you..."
    t "....."
    t "do you lo... like me, aang? really?"
    t "even though i'm little, and... and bad with feelings, and... difficult?"
    t "i'm sorry, you know."
    t "i just... i hate being vulnerable, and... blah."
    t "does this..."
    t "...does this sound as stupid to you as it does to me?"
    y "no, it's important to talk about these things."
    y "and i like you about as much as a person can."
    t "........"
    t "aang..."
    y "hm?"
    show tonf tonf51 with Dissolve(2)
    t "touch..."
    t "touch me."
    stop music
    play music "audio/Unwritten Return.mp3"
    show ctc
    pause
    hide ctc



    hide tonf
    show tonf tonf52:
        ypos 2
    with Dissolve(2)
    show ctc
    pause
    hide ctc
    t "...aang?"
    show tonf tonf52:
        ypos 2
        linear 3 ypos -252
    "your eyes drink her in, from her pretty, blushing face down to her small breasts and pink, stiffening nipples."
    $ renpy.pause(3,hard=True)
    if toph_date_walk == "city":
        show toii toii01:
            xzoom -1
        with moveinleft
        iroh "welcome to the jas-"
        show toii toii06:
            xzoom -1
        with dissolve
        iroh "oh, hey, look, a wall."
        hide toii


        show toii toii06:
            xpos -600
        with dissolve
        hide toii
        with moveoutleft
        iroh "when will these people leave me alone..."

    show tonf tonf53 with Dissolve(2)
    y "......"
    t "do it..."
    show tonf tonf54
    show ctc
    pause
    hide ctc
    t "you like them, don't you?"
    t "you like me?"
    t "my body?"
    show ctc
    pause
    hide ctc
    y "completely."
    y "especially..."
    show tonf tonf55
    y "these perky little nipples."
    show ctc
    pause
    hide ctc
    t "ohhh..."
    t "you make me... so warm..."
    show tonf tonf56
    y "fuck these are firm."
    y "you have perfect little tits, toph."
    t "yes... keep... ah..."
    show ctc
    pause
    hide ctc
    show tonf tonf57
    t "oh, aaang...!"
    t "ease... easy... they're so sensitive..."
    show tonf_lewd with Dissolve(1.5)
    t "ohhhh...."
    show ctc
    pause
    hide ctc
    y "you like that, huh?"
    t "unnhh..."
    show tonf tonf58
    t "ohh... you... ahhhh...."
    show ctc
    pause
    hide ctc
    t "aang..."
    y "yum..."
    hide tonf_lewd with dissolve
    t "a-aang...?"
    y "yeth?"
    t "take me."
    show tonf tonf56 with dissolve
    t "hm?"
    t "i... i want you."
    t "i want you to take me."
    show tonf tonf54 with dissolve
    y "boob..."
    t "i want to have sex with you."
    t "right here."
    show tonf tonf52 with dissolve
    y "wait... right here?"
    t "unless you'd rather do it at my house?"
    menu:
        "right here is fine":
            y "no, i can't wait."
            t "me neither, take me!"
            if toph_date_walk == "city":
                iroh "i... uh... there's a cot in the back..."
                scene black with dissolve
                "toph pulls you eagerly to the back of the shop and through a door."
                scene inside_tavern_1
                with dissolve
                show tonf tonf51 with dissolve
                t "okay... hold on, let me get undressed."
                hide tonf with dissolve
                y "alright, there's a cot in this other corner..."
                scene black with dissolve
                scene bg_day_tophhome
                with dissolve
                y "looks like there's a window so we can get some light..."
                y "nice."
                t "okay, i'm... i'm naked."
            else:

                t "there's a field over there."
                t "come with me..."
                scene black with dissolve
                "toph pulls you eagerly out of the woods and into the nearby field."

                t "okay... hold on, let me get undressed."
                "toph undresses and lays on the ground."
                scene bg_training_0 with dissolve
        "let's go to the house":


            y "let's go back to your house, first."
            t "okay..."
            t "but hurry!"
            t "i'm so... so ready."
            scene black with dissolve
            "toph pulls you eagerly back to the village."
            "you barely get through the door, when she starts pulling her clothes off."
            scene bg_bk3_tophome_day
            show tonf tonf51
            with dissolve
            t "okay... hold on, let me get undressed."
            hide tonf with dissolve
            y "alright, there's a good spot over here..."
            scene bg_bk3_tophome_0 with dissolve
            t "okay, i'm... i'm naked."


    show toty toty07 with Dissolve(1)
    show ctc
    pause
    hide ctc
    y "are you ready?"
    show toty toty06 with Dissolve(1)
    t "i'm... i'm always ready for you."
    y "...."
    t "...what?"
    y "I was just thinking how amazing you are."
    t "come on, don't be embarrassing."
    y "your pussy's in the air, and {i}that{/i} makes you uncomfortable?"
    t "i... i don't..."
    y "alright, alright."
    show toty toty00 with dissolve
    "You pull out your cock and line it up with toph's small, eager pussy."
    show toty toty01 with dissolve
    t "oh...?"
    y "are you okay?"
    t "i... think so."
    t "go ahead."
    show toty toty02_1
    t "ah!!"
    t "wait!"
    y "I'm not even-"
    t "out! pull it out!"
    show toty toty00 with dissolve
    t "ohh..."
    y "are you okay?"
    y "what was that?"
    t "it... it's really sore."
    t "try... try again?"
    y "okay..."
    show toty toty01 with dissolve
    y "you sure?"
    t "y-yeah."
    show toty toty02_1
    t "ungh!"
    y "toph?"
    show expression "bk3/toph/fuckonback/blink.png":
        xpos 368 ypos 244
    t "fffu... ugh... hngh..."
    y "do you need me to pull out?"
    t "n-no... ah... ah..."
    t "ow... owww...."
    y "okay, i'm pulling out."
    hide expression "bk3/toph/fuckonback/blink.png"
    show toty toty01
    with dissolve
    t "s-sorry..."
    t "it feels sore... maybe chafed."
    show toty toty06 with dissolve
    y "we did just have sex recently..."
    t "you must have rubbed me too raw inside."
    t "don't forget, i'm... i'm new at this, you know?"
    show toty toty07 with dissolve
    t "*sniff...*"
    t "i'm so sorry, aang..."
    t "i want... i want to have sex with you!"
    t "and i want you to have sex... i want to be what you need!"
    y "hey, don't cry, it's okay."
    t "....there is another, um... option."
    y "what? your mouth?"
    t "no, another {i}another{/i} option."
    y "what?"
    t "we could... we could try anal, maybe?"
    menu:
        "we can wait":
            y "we don't have to do that, toph."
            y "it's okay, really."
            t "no!"
            t "i... i want to!"
        "that sounds great":

            y "if you're ready, i'd love to do that."
            t "o-okay!"
            t "let's... let's do anal!"

    y "turn over, then."
    hide toty with Dissolve(1)
    jump love_toph_anal1

label love_toph_anal1:
    $ tota_assfuck_seeface = False
    $ tota_assfuck_xray = False

    show tota tota00 with Dissolve(1.5)
    t "o-okay."
    if not love_toph_anal1:
        y "(hot damn! I think i'm about to actually fuck her in the ass...)"
        t "this... this isn't something I'd ever really considered doing before."
    $ tota_assfuck_seeface = True
    t "just be gentle, okay?"
    t "i want to... to make you happy but... i'm small."
    if not love_toph_anal1:
        y "are you sure you want this?"
        t "i can handle a little pain, just... go slow."
    show tota tota01 with dissolve
    if not love_toph_anal1:
        t "Like... reaaaaally slow."
    t "i put a finger in there the other day and it's... it's really tight."
    show tota tota02 with dissolve
    t "try not to... to tear or hurt me, okay?"
    y "i'll be careful."
    y "try and relax... being tense will make it more difficult."
    t "that's easy for you to say..."
    if not love_toph_anal1:
        y "want a safeword?"

        t "What's that?"
        y "Just a word you use when the other should stop whatever he or she is doing."
        t "Why can't they just say \"STOP!\"?"
        y "Because sometimes people say \"stop\" when what they really want is the other to keep doing it."
        t "Well, that's weird and I don't need one."
        t "buuuut... let's just go with... \"bananas\"."
        t "is that okay?"
        y "it's your word."
        t "But when I tell you to stop you need to stop too!"
        y "Understood."
    y "here it goes."
    $ tota_assfuck_seeface = False
    if not love_toph_anal1:
        y "(i'm about to put my dick in toph's ass!)"

    show tota tota10b
    with Dissolve(1.5)

    t "uunnghh..."
    "toph takes several deep breaths."
    t "O-okay... okay..."
    t "This isn't so bad."
    t "Just... just a penis going into my anus..."
    t "nothing to be alarmed about."
    t "it's just like normal... but entirely different..."
    t "....and against what nature intended."
    y "Alright, I'll put in the head now."
    $ tota_assfuck_seeface = True
    t "it's... it's not in?"
    y "no, this is just the tip."
    $ tota_assfuck_seeface = False
    t "oh..."
    y "...Ready?"

    t "s-sure thing..."
    $ tota_assfuck_seeface = True
    t "wait, don't we... uh... don't we need lubricant or something?"
    y "i mean... i don't have any with me."
    y "i could spit on it?"
    y "how about that?"
    t "i think that's a... a good idea."
    $ tota_assfuck_seeface = False
    t "this is... already kind of difficult..."

    show tota tota01 with dissolve
    y "okay."
    play sound "audio/spit.mp3"
    show expression "bk3/joodee/titplay/spithead.png":
        xpos 325 ypos 225
        alpha 1.0
        linear 4.0 alpha 0
    with ushake
    t "oh!"
    t "that was... wet."
    y "well, yeah."
    y "okay, that should do it."
    show tota tota10
    with Dissolve(1.5)
    t "hngh..."
    y "just sliding back in..."
    t "o-okay..."
    y "it's going in now... ready?"
    t "........"

    show tota tota03 with hpunch

    if not love_toph_anal1:
        t "{size=+20}Heeeeeee!! Take it out!"
        t "{size=+20}STOP!!! bananas!!!bananas!!!"

        show tota tota02
        $ tota_assfuck_seeface = True
        with Dissolve(1.5)
        y "It's out! It's out!"
        y "Are you okay?!"

        t "i'm... i'm okay..."
        t "just... ha... just surprised more than anything..."
        t "Let's... let's try it again."
        y "You sure?"
        y "I could lick you a bit first to help you relax..."
        show expression "bk3/toph/ass_fuck/face_angry.png"
        t "{size=+20}NEVER!!!{/size}" with hpunch
        t "I can do this!"
        t "and there's no way I'm letting you put your tongue there!!"
        t "This is embarrassing enough as it is!"
        y "embarrassing? this was your idea..."
        hide expression "bk3/toph/ass_fuck/face_angry.png" with Dissolve(1.5)
        t "i know... and i want to, i just..."
        t "...i'm not used to being this vulnerable."
        t "please don't make me more so."
        y "i understand."
        y "no tongue, i promise."
        t "okay..."
        t "Then... let's try this again."
        t "Slowly."
    else:
        t "{size=+20}ahhh!! fuck!!"
    $ tota_assfuck_seeface = False

    show tota tota11 with Dissolve(1.5)
    t "unnghh.... ohhh.... oh...."

    y "The head is in."
    $ tota_assfuck_seeface = True
    t "....I noticed...."
    show ctc
    pause
    hide ctc
    show tota tota12 with Dissolve(1.5)
    t "Ohh... ohh... it's..."
    t "ow..."
    show ctc
    pause
    hide ctc
    t "it's painful, i'm sorry..."
    y "just a bit more."
    show tota tota13 with Dissolve(1.5)
    t "ahhh...!! ah...."
    show ctc
    pause
    hide ctc
    show tota tota14 with Dissolve(1.5)
    t "ohhh...!!!"
    if not love_toph_anal1:
        y "That's it."
        y "This is as far as it'll ever go."
        t "don't.. don't move..."
        t "Just stay like like this for a minute..."
        t "{size=+5}don't move."
        "You stay in the current position, softly kissing Toph's earlobes."
        show ctc
        pause
        hide ctc
        y "Do you feel better?"
        t "...yeah."


    y "I'll just do some short strokes now, okay?"
    t "Oh... okay..."
    show tota tota102 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    t "oohh... ahh..."
    t "oww... uh..."
    y "you okay?"
    t "Ah... that's... that's okay..."
    t "Short strokes are... are okay..."

    t "Just keep doin' it like this for a bit... please..."
    "you pop in and out of the tight hole..."
    "the constant pressure of her little entrance squeezing around your cock feels incredible."
    show ctc
    pause
    hide ctc
    "After several minutes of slowly prodding Toph's ass, never going deeper than the tip, you feel her relax."
    t "Okay... this is a lot better..."

    t "I think it's okay for you to go deeper now."
    y "Just yell when I need to stop."
    if not love_toph_anal1:
        y "Just... you know, not hard enough for other people to come and see what's going on."
        t "Did I really yell that hard before?"
        y "Let's just say I'm happy no one is here right know."
    y "here we go."
    show tota tota100

    with Dissolve(1.5)
    t "ohhhhhh...... {i}fuuuuck{/i}, aang!"
    y "it's so cute when you swear."
    t "well... fuck!"
    t "Hnnnff... I... I could do this..."
    y "you are doing this..."
    t "i mean... i could... get used to this..."
    t "this... this isn't so bad..."
    t "just keep going slowly..."
    $ tota_assfuck_seeface = True
    t "It's still weird, but not impossible to... enjoy."
    show ctc
    pause
    hide ctc

    menu:
        "turn xray on":
            $ tota_assfuck_xray = True
        "leave xray off":
            pass
    show ctc
    pause
    hide ctc
    $ tota_assfuck_seeface = False
    y "Think you're ready for me putting my weight behind it?"
    t "I... can take it!"
    t "I want to... i want to make this good for you!"
    y "it's already good for me, toph."
    t "no, i can... i can do it!"
    t "g-go ahead!"
    y "Here it comes!"
    $ tota_assfuck_seeface = True
    show tota tota101
    t "AAhh!!"
    y "Should I stop?"
    t "HNG... NO! Keep going!!"
    t "does it... does it feel good?"
    y "fuck yes..."
    t "g-good! ohhh...."
    show ctc
    pause
    hide ctc
    t "you're... all the way in my stomach..."
    t "unngh... ahh..."
    t "there's so much... of you... ahh..."
    y "i need... i need more!"
    show tota tota103
    t "ahhh!! ahhh!!"
    t "ohh... ahh!"
    t "wait!"
    y "oh, shit, should i-"
    t "keep... don't... stop...!!"
    t "i just... ah... i need to... you're just so..."
    t "you're just so... {size=+5}big{/size} inside me!"
    show ctc
    pause
    hide ctc
    t "i can't... ohh... ow..."
    y "do you need me to stop?"
    t "no, keep... keep going... oww..."
    t "you can... you can go faster... if you... ah... if you need to..."
    y "fuck yes!"
    show tota tota104
    t "ahhh!!"
    show ctc
    pause
    hide ctc
    y "fuck! this ass is so fucking... tight!!"
    t "ungh... unghh... ohh..."
    y "why haven't i been slamming this ass for ages?!"
    t "fu... fuck! ah!"
    if not love_toph_anal1:
        t "a-aang... ohhh..."
        y "yes?"
        t "ohh... oh... i can't wait any... oh, it hurts so..."
        t "oh... oh, i..."
    t "i... i love..."
    show tota tota105
    t "i... love you! i love you!"
    if not love_toph_anal1:
        t "there, i said it!"
    t "you have my ass... you have all of me!"
    if not love_toph_anal1:
        t "do you love me? please! i... ahh! i need to hear it!"

        menu:
            "i love you, too!":
                $ toph_say_love = True
                y "I love you, toph!"
                y "I love you with all my fucked up heart!"
                t "i love you, aang!"
                t "ohhh!!!"
                show tota tota106
                t "fuck my ass, my love!"
                t "fuck it hard!"
                t "give me everything!"
                show tota tota107
            "i'm... i'm not ready":

                $ toph_say_love = False
                show tota tota103
                y "I'm not ready to say it back, toph..."
                y "I'm so sorry."
                t "i... i understand..."
                t "you aren't ready..."
                t "but i still love you..."
                t "just... ohh... just finish, aang..."
                $ tota_assfuck_seeface = False
                t "unnghh..."
    else:
        show tota tota107

    $ tota_assfuck_seeface = False
    y "I'm close to exploding!"
    y "Any preferences about where I'll make a mess?!!"
    t "Hnno!!"

    menu:
        "come outside":
            hide tota
            if toph_say_love:
                show tota tota01a
            else:
                show tota tota01b
            with Dissolve(1.5)
            y "Here it comes!!"

            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/spermout1.png"
            with flash
            $ renpy.pause ()
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/spermout2.png"
            with flash
            $ renpy.pause ()
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/spermout3.png"
            with flash
            y "All over your pretty white butt."
        "come inside":

            hide tota
            show tota tota14
            $ toph_assfuck_xray = False
            show expression "bk3/toph/ass_fuck/inanus.png"
            with Dissolve(1.5)

            $ renpy.pause(0.5)

            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/sperm1.png" with hpunch

            y "Hhnnn~"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/sperm2.png" with hpunch

            y "HNNNGGG!!"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/sperm3.png" with hpunch

            hide expression "bk3/toph/ass_fuck/inanus.png"
            hide expression "bk3/toph/ass_fuck/sperm1.png"
            hide expression "bk3/toph/ass_fuck/sperm2.png"
            hide expression "bk3/toph/ass_fuck/sperm3.png"

            hide tota
            show tota tota01a
            show expression "bk3/toph/ass_fuck/sperm4.png"
            with Dissolve(2.0)

    $ tota_assfuck_seeface = True
    show tota tota01
    show expression "bk3/toph/ass_fuck/face_lewd.png"
    if not love_toph_anal1:
        t "That wasn't nearly as bad as I had imagined it."
        t "Next time... I won't take it lying down though.... literally."
        y "I'm Looking forward to it."
    else:
        t "oahh.... that was fun...."
    if not love_toph_anal1:
        if not toph_say_love:
            y "hey, i'm sorry i couldn't... i can't... say it back, yet."
            show tota tota01b
            hide expression "bk3/toph/ass_fuck/face_lewd.png"
            with dissolve
            t "i... it's fine."
            t "it's my fault for saying it too soon."
            show tota tota01
            show expression "bk3/toph/ass_fuck/face_lewd.png"
            with dissolve

    t "Now give me a kiss you big oaf."
    t "I need a bath."
    if not love_toph_anal1:
        y "i think we both do."
        t "great, you can come with me, and help me warm up the water with your firebending."
        y "i see what i am to you..."
        y "i'm an easy butler and an easier lay, is that right?"
        t "you got it!"

    show pink with dissolve
    play sound "audio/kiss.mp3"
    $ renpy.pause(0.5)
    "toph leans back towards you and plants a surprisingly soft and gentle kiss on your lips."
    "she holds it there for a moment and falls back onto her stomach."
    hide pink with dissolve
    t "ahh..."
    t "come on, let's go."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    $ bk3_day = False

    if love_toph_anal1:
        "you head home and fall fast asleep."
        jump love_bk3_next

    scene bg_bk3_tophome_night
    show tocl_tub
    show tocl tocl11
    with Dissolve(1)
    t "you ready?"
    show tocl tocl10
    y "oh, we're really taking a bath?"
    show tocl tocl11
    t "well, yeah."
    show tocl tocl10
    t "you need one."
    show tocl tocl11
    y "{i}you{/i} need one."
    show tocl tocl09
    show tocl_smile
    with dissolve
    t "you tease me too much and you won't get a peek at the goods you enjoy so much..."
    y "don't make me come over there."
    t "oh yeah?"
    t "and do what?"
    y "you'll find out."
    show tocl tocl08 with dissolve
    t "bring it on, twinkle toes."
    y "aarrghgh!"
    play sound "audio/thud.mp3"
    hide tocl_smile
    show black
    "you tackle toph, who falls into the water giggling."
    "you teasingly wrestle before you fall to kissing and eventually washing one another."
    "once finished, you step out and dry off."
    hide black
    show tocl tocl06
    with dissolve
    t "well, i wasn't quite expecting that..."
    show tocl tocl05 with dissolve
    y "you should have, i'm very aggressive."
    show tocl tocl06
    with dissolve
    t "i'll say... my poor pussy is still sore..."
    show tocl tocl05
    with dissolve
    t "and now my butt, too."
    y "sorry... i might have gotten carried away."
    show tocl tocl08
    show tocl_smile
    with dissolve
    t "i'm only messing around, i feel fine, really!"
    t "come on, i'm ready for bed."
    t "how about you?"
    y "yeah, i'm beat."
    t "okay, come on."
    scene black with dissolve
    scene bg_night_tophhome
    show totc totc15
    with Dissolve(1.5)
    t "thanks for a great day, aang."
    y "it was nice, wasn't it?"
    show expression "bk3/toph/nightmare/face_lewdzoom.png"
    with dissolve
    t "and now i get to sleep next to you."
    t "this might be my favorite day ever."
    y "i know my favorite part."
    with vshake
    t "toph gives you a light smack on the arm."
    t "....me too."
    "you snuggle up together in bed, and fall fast asleep."
    scene black with dissolve
    $ love_toph_anal1 = True
    jump love_bk3_next

label love_toph_anal2:
    scene bg_bk3_tophome_2
    show tota tota19
    with eye_open
    $ renpy.pause(1,hard=True)
    stop music
    play music "audio/Unwritten Return.mp3"
    if not love_toph_anal2:
        y "*yaaawnn...*"
        y "...toph?"
        show ctc
        pause
        hide ctc
        t "good morning, sleepyhead."
        y "what's going on?"
    else:
        t "sit."
        y "okay..."
    show tota tota29 with Dissolve(1.5)
    t "i was thinking..."
    show ctc
    pause
    hide ctc
    if not love_toph_anal2:
        t "you were so gentle with me the other day..."
        y "i was?"
        t "you took my anal virginity so carefully, i'm worried you didn't get to enjoy it."
        y "no... i definitely enjoyed it."
        t "it's okay, aang."
        t "we both enjoyed it, but..."
        show tota tota20 with dissolve
        t "...it was more about helping me through my first time."
        t "and i really appreciate it."
        t "but i wanted to repay your kindness - for fucking my ass so well - and i'm a quick learner, so..."
        t "...i thought \"how about a little morning anal?\""
        t "\"i'm sure he'd love to dump a load in my tiny... cute... little butt.\""
        y "...it {i}is{/i} a cute butt."
    else:
        t "...do you want to dump a load in my cute little butt?"
        y "hell yeah i do."

    t "here..."
    show expression "bk3/toph/ass_fuck/zbottle.png" with dissolve
    show expression "bk3/toph/ass_fuck/zbottle_fluid.png":
        alpha 1.0
        linear 4.0 alpha 0.0
    $ renpy.pause(.5, hard=True)
    y "Lubricant?"
    t "yeah, and plenty of it!"
    t "i'm gonna fuck you {i}hard{/i}."
    t "and i think this will help both of us."
    hide expression "bk3/toph/ass_fuck/zbottle.png"
    hide expression "bk3/toph/ass_fuck/zbottle_fluid.png"
    show tota tota21 with Dissolve(1.5)
    t "go ahead... aim him somewhere... interesting."
    show ctc
    pause
    hide ctc
    show tota tota22
    show expression "bk3/toph/ass_fuck/zput_itin.png"
    with Dissolve(1.5)
    y "Here?"
    t "That's a fine place."
    hide expression "bk3/toph/ass_fuck/zput_itin.png" with Dissolve(1.5)
    t "now, i want you to sit back..."
    t "...while i make you cum with my tight, teen ass."
    show tota tota26 with Dissolve(1.5)
    y "oh, fuck..."
    t "*mmmm...*"
    t "How does.. this feel?"
    y "*swallows*"
    show ctc
    pause
    hide ctc
    show tota tota27 with Dissolve(1.5)
    t "and... further..."
    y "oh, shit..."
    show ctc
    pause
    hide ctc
    show tota tota22 with Dissolve(1.5)
    t "Warmup is done!"
    show tota tota110
    t "ahh!"
    show ctc
    pause
    hide ctc
    t "ahhhn... yeah...!!"
    show ctc
    pause
    hide ctc
    if not love_toph_anal2:
        y "Wow... this is... so different from the other day."
        t "like i said, I'm a quick learner."
        t "...and I don't give up."
        t "Buuut...."
        y "butt?"
    t "What I really want..."
    t "...is for you to experience how it feels..."
    t "...when I put my full weight on your big dick in this position."
    if not love_toph_anal2:
        t "we can get {i}much{/i} deeper this way, i think..."
    show ctc
    pause
    hide ctc
    show tota tota22 with Dissolve(1.5)
    if not love_toph_anal2:
        t "You know, you can shout \"bananas\" if you want to."
        y "bana...?"
        y "oh, you mean the safeword?"
        y "Why, will that make you stop?"
        "toph smiles the biggest damn grin you've ever seen."
        t "oh, no. That's {i}my{/i} safeword."
        t "We've never agreed on a safeword for {i}you{/i}."
    t "i'm gonna make you cum... and there's nothing you can do about it."

    show tota tota111
    $ renpy.pause(1.0)
    t "ugh!"
    t "fuck!"
    show ctc
    pause
    hide ctc
    y "sh-shit!"
    t "i'm taking it... *fuck!*... all the way to... *ugh!*... balls!"
    y "hell yeah you are!"
    t "you gonna... ugh... cum!?"
    y "soon...!!"
    y "I never thought such a small, slender frame could generate this much of a downwards... hnnng... force!"
    t "And this is me still playing nice!"
    show ctc
    pause
    hide ctc
    y "what's you playing mean?"
    show tota tota22 with dissolve
    t "i thought you'd never ask!"
    show tota tota112
    t "ungh! ahhh! mmm!"
    y "what the fuck, toph!?"
    show ctc
    pause
    hide ctc
    t "watch my... *ugh!*... bouncing little titties while i... *mmgh!*"
    t "while i squeeze out your... *ah!*... cum with my tight... *mmh!*... teen butt!"
    t "stuff my butt with your fucking cum!"
    show tota tota113
    t "Ah... I... I can feel something happening!"
    t "you're getting... bigger?!"
    t "are you... *ah!*... gonna shoot that big... *mmgh!*... fucking load in my ass!?"
    show ctc
    pause
    hide ctc
    t "i'm going to milk your fucking cock!"
    t "give me your cum, love!"

    menu:
        "cum inside":
            hide tota
            show tota tota24 with vpunch
            play sound "audio/gltch2b.mp3" 
            $ renpy.pause(1.0)
            show tota tota24 with vpunch
            play sound "audio/gltch2b.mp3"
            $ renpy.pause(1.0)

            show tota tota25 with Dissolve(1.5)
        "cum outside":


            hide tota
            show tota tota24
            show tota tota20 with Dissolve(1.5)
            t "cover me!"
            show expression "bk3/toph/ass_fuck/zbody_1_blink.png":
                xpos 0 ypos 0

            show expression "bk3/toph/ass_fuck/zsperm_1.png"
            play sound "audio/gltch2b.mp3" 
            with flash
            $ renpy.pause()
            show expression "bk3/toph/ass_fuck/zsperm_2.png"
            play sound "audio/gltch2b.mp3" 
            with flash
            $ renpy.pause()
            show expression "bk3/toph/ass_fuck/zsperm_3.png"
            play sound "audio/gltch2b.mp3" 
            with flash
            $ renpy.pause()
            hide expression "bk3/toph/ass_fuck/zbody_1_blink.png"
            show ctc
            pause
            hide ctc

    y "that... that was... what the shit..."
    t "i was hoping you'd say that."
    y "how did... you..."
    t "aang, i... you make me so happy."
    t "i will make you happy too... for as long as you'll have me."
    t "i love you... and i'm not taking that back."
    t "now... i need to wipe this off..."
    t "i'll see you later!"
    t "bye!"
    show ctc
    pause
    hide ctc
    show tota tota18
    hide expression "bk3/toph/ass_fuck/zsperm_3.png"
    hide expression "bk3/toph/ass_fuck/zsperm_2.png"
    hide expression "bk3/toph/ass_fuck/zsperm_1.png"
    with dissolve
    y "i should go as well..."
    y "whew."
    if not love_toph_anal2:
        y "good start to the day."
    else:
        scene black with dissolve
        "you head home for the night."
        jump love_bk3_next
    scene black with dissolve
    $ love_toph_anal2 = True
    jump love_bk3_next

label ty_rescue_suki:
    $ bk3_day = False
    "you and ty lee race to the forest outside the city, keeping an eye out for any sign of suki."
    scene black
    scene bg_emberisland_wood_night
    show tfa
    with dissolve
    y "suki?!"
    ty "shh!"
    y "what?"
    y "oh, right, trap."
    ty "behind you!"
    hide tfa with moveoutright
    show fireguard_halberd:
        xzoom -1
    show toeg toeg01
    show tosi tosi10:
        zoom 0.87 xpos -180 ypos 130
    show guard_rope:
        zoom .95 xpos -280 ypos 75
    with moveinleft
    y "aw, crap."
    y "fire nation and dai lee?!"
    y "damn it, azula..."
    y "why do you have to be so conniving?"
    dl "we meet again, avatar..."
    fg "hey buddy!"
    y "fuck you, earth bro."
    y "and hello fire bro!"
    y "we're gonna beat you off!"
    fg "you're gonna what?"
    y "ty lee! go!"
    play sound "audio/whoosh.wav"
    show tfa with moveinright
    hide fireguard_halberd
    hide tfa
    with moveoutleft
    fg "waa!"
    play sound "audio/thud.mp3"
    ty "i got this one!"
    y "suki, duck!"
    suki "where?"
    suki "oh, right!"
    hide guard_rope
    hide tosi
    with dissolve
    dl "get some!"
    show black with dissolve
    "you engage the dai lee agent."
    "the blows are fast and relentless, but he proves to be no match for you."
    play sound "audio/thud.mp3"
    hide black
    with flash
    hide toeg with moveoutbottom
    dl "uhghh...."
    y "okay, that guy's dealt with..."
    y "ty lee!"
    ty "help!"
    show fireguard_halberd:
        xpos -250
    with dissolve
    fg "uh... hey?"
    y "what did you do?"
    fg "i whacked her."
    y "you what?"
    fg "i whacked her in the head."
    y "why?!"
    fg "she was attacking me!"
    y "you kidnapped her friend!"
    fg "yeah, under {i}orders{/i}."
    y "okay, that's it."
    y "i'm gonna whip your ass."
    fg "you mean \"whoop\" my ass?"
    y "no."
    "using the water in the forest and vines, you animate nature."
    show a_swampcl_whip2 with dissolve
    fg "...?"
    fg "what..."
    show a_swampcl_whip1
    hide a_swampcl_whip2
    with dissolve
    fg "what are you gonna do with that?"
    show vine_whip
    hide a_swampcl_whip1
    fg "ow... ow... ow!"
    fg "hey! ow! stop it!"
    fg "ow!"
    fg "I'm going! i'm going!"
    fg "you pervert."
    hide vine_whip
    hide fireguard_halberd
    show a_swampcl_whip1
    with dissolve
    y "that's right!"
    y "wait, no, i mean-"
    ty "heyyy... thanks..."
    show tfa
    hide a_swampcl_whip1
    with dissolve
    ty "you... you saved my life..."
    y "maybe?"
    y "i bet you could have managed."
    ty "normally, but he caught me off-guard somehow."
    y "no worries."
    y "let's grab suki and get out of here."
    show black with dissolve
    "you cut suki's ropes..."
    hide black
    show tosi tosi10:
        xzoom -1
    with dissolve
    suki "well... that sucked."
    y "understatement."
    suki "let's get out of these stupid woods."
    ty "i couldn't agree more!"
    scene black with dissolve
    "the three of you head to the tavern."
    scene inside_tavern_night
    show tosi tosi10:
        xzoom -1
    show tf
    with dissolve
    ty "you sure you'll be okay?"
    suki "yeah, i just need to get some rest."
    y "you should go see katara if you don't feel well."
    suki "i will if i need to, don't worry."
    suki "and... thanks for saving me, both of you."
    y "my pleasure."
    ty "happy to!"
    suki "i'm gonna go lie down... i'll check you later."
    hide tosi with dissolve
    y "well that was something."
    ty "will you walk me back to my place?"
    y "sure, are you okay?"
    ty "yeah! i just like your company!"
    y "i like your company, too."
    scene black with dissolve
    "you walk ty lee back to the boarding house."
    scene inside_brothel_1
    show tf
    with dissolve
    ty "thanks for the walk!"
    y "any time."
    ty "want to hang out in my room?"
    y "sure, why not?"
    scene black with dissolve
    "you follow ty lee into her room."
    jump tylee_lovefuck

label tylee_lovefuck:
    show expression "ebackgrounds/bed_inside.jpg"
    $ toxd_transparent = 'false'
    $ toxd_dildo= False
    ty "i need to get stuffed. now."
    "you watch as ty lee drops her clothes to the floor."
    show toxd_head eyesfront with Dissolve(1.5)
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    ty "sit down, i'm going to give you a penis massage."
    y "a... penis massage?"
    ty "yeah!"
    show toxd toxd00a with Dissolve(1.5)
    hide toxd_head
    show toxd_head eyesfront
    if love_ty_sex_quest <5:
        ty "i'm so glad we're all alive and safe!"
    ty "i have to thank mr. dick!"
    y "...i have no problem with that."
    ty "I have a nice warm place for him to take a rest and massage him at the same time!"
    ty "And I'm sure he'll be super happy and cry again."
    show toxd toxd00b with Dissolve(1.5)
    "With practiced ease you quickly slide out of your clothes and position yourself beneath Ty Lee."
    show toxd_head eyesdown
    y "Well... he has been playing outside a lot, so I guess he could use some inside relaxing."
    show toxd_head eyesfront
    ty "Then it's decided!"

    show toxd_head eyesdown
    show toxd toxd00c
    ty "I'll just grab him and gently guide him to where he'll need to be."
    show toxd_head lewd
    with Dissolve(1.5)
    ty "MMMMhhh, he's so stiff. "
    ty "I'll really have to massage him hard so he can become soft again."


    show toxd toxd01 with Dissolve(1.5)
    show toxd_head eyesfront
    ty "Are you ready?"
    y "Super ready."
    hide toxd_head
    show toxd toxd02
    with Dissolve(1.5)


    ty "Hmmm, I'll just slowly put him in deeper."
    show toxd toxd03 with Dissolve(1.5)
    ty "He feels really warm all by itself."
    show toxd toxd04 with Dissolve(1.5)
    ty "but it also feels like he's shivering? That's odd!"
    y "Yeah, when he's really looking forward to something he starts pulsating."
    y "Perfectly normal, please go on."
    show toxd toxd05a with Dissolve(1.5)
    ty "Ah!! I don't think he can go deeper. We've hit the ceiling!"
    show toxd_head eyesfront:
        ypos 12
    ty " I think it's tip is about..."
    show expression "bk3/tylee/lovedildo/body_1_armpoint.png":
        ypos 0 xpos 1000
        linear 0.8 xpos 900
        linear 1.2 ypos 100 xpos 800
    show toxd_head eyesdown
    ty "here.."
    hide expression "bk3/tylee/lovedildo/body_1_armpoint.png"
    show toxd toxd01
    hide toxd_head
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "Time for the massage."
    hide toxd_head
    show toxd toxd100
    $ renpy.pause()
    ty "Hmm I really like massaging you."
    ty "It makes my head feel all fluffy and light."


    menu:
        "x-ray on ":
            $ toxd_transparent = 'dick'
        "keep going like this":

            pass
    $ renpy.pause()
    show toxd toxd01
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "Mmmh... I'm gonna massage you really hard now!"
    ty "So you better be prepared!"

    y "I'm ready!"
    hide toxd_head
    show toxd toxd101
    hide toxd_head

    y "Wohoo! "
    $ renpy.pause()
    y "Oh, shit!"
    y "gonna cum!!!"
    ty "not in me!"
    menu:
        "inside":
            hide toxd
            show toxd toxd05a
            if toxd_transparent == 'dick':
                show expression "bk3/tylee/lovedildo/womb.png":
                    alpha 0.0
                    linear 1.5 alpha 0.5

            y "Gonna fill you up!"
            show toxd toxd05b
            ty "No! wait!"
            ty "don't-"
            if toxd_transparent == 'dick':
                show expression "bk3/tylee/lovedildo/womb_sperm.png":
                    alpha 0.0
                    linear 4.0 alpha 1.0
            show toxd toxd05a
            play sound "audio/gltch2b.mp3"
            $ renpy.pause(2.0)
            play sound "audio/gltch2b.mp3"
            $ renpy.pause(2.0)
            play sound "audio/gltch2b.mp3"
            ty "unghh... ahh..."

            ty "u-uh spirits... you... you came in me!"


            if toxd_transparent == 'dick':
                hide expression "bk3/tylee/lovedildo/womb.png"
                hide expression "bk3/tylee/lovedildo/womb_sperm.png"

            show toxd toxd00b
            show toxd_spermgush
            show toxd_head eyeshalf
            with Dissolve(1.5)
            ty "you actually... finished in-inside me!"
            y "was i not supposed to?"
            ty "umm... it... it should be fine..."
        "outside":

            show toxd_head eyeshalf
            hide toxd
            show toxd toxd05a
            $ toxd_transparent = 'false'
            show toxd toxd00d with Dissolve(1.5)
            y "hnnnngg!"
            play sound "audio/gltch2b.mp3"              
            show expression "bk3/tylee/lovedildo/spermout_1.png"
            $ renpy.pause()

            play sound "audio/gltch2b.mp3"              
            show expression "bk3/tylee/lovedildo/spermout_2.png"
            $ renpy.pause()

            play sound "audio/gltch2b.mp3"              
            show expression "bk3/tylee/lovedildo/spermout_3.png"
            $ renpy.pause()
            ty "Ooh! All over my boobies!"
            hide toxd_head
            hide expression "bk3/tylee/lovedildo/spermout_1.png"
            hide expression "bk3/tylee/lovedildo/spermout_2.png"
            hide expression "bk3/tylee/lovedildo/spermout_3.png"
            show toxd toxd08 with hpunch
            "Tylee slides off your dick and falls backwards, exhausted from the effort."
            $ renpy.pause()
            ty "Ah, that felt so nice."
            ty "I feel drenched..."
            y "you are."


    y "We'll do this again soon."
    ty "that sounds... fun."
    scene black with dissolve
    "you head home for the night."
    $ love_ty_sex_quest = 5
    jump love_bk3_next

label tylee_lovedildo:

    show expression "ebackgrounds/bed_inside.jpg"
    with dissolve

    $ toxd_transparent = 'false'
    $ toxd_dildo= True

    show toxd_head eyesfront with Dissolve(1.5):
        xzoom -1

    ty "Say, Suki told me about this thing she lost in the tunnels."
    ty "She said I could have it if she ever finds it again."
    ty "As a thanks for saving her life."
    ty "Have you found something like a small statue in the tunnels?"
    y "I might... could you describe it?"

    ty "It's green, looks like avatar Kyoshi and is the size of a fairly impressive banana."
    ty "It's for.... fun."
    y "could... could it be this?"
    show toxd_head eyesdown
    show expression "bk3/tylee/lovedildo/solodildo.png" with Dissolve(1.5)
    ty "Ah, yes!"
    ty "That's it!"
    show toxd_head eyesfront
    ty "Thanks for finding it!"
    ty "Would you like me to give you a demonstration of how it's used?"
    ty "As a thanks?"
    y "Well, as long as it doesn't cost me cabbages."
    ty "Of course not!"
    hide toxd_head

    show toxd toxd00b
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "You're supposed to kiss it, but with your \"other lips\"."
    hide expression "bk3/tylee/lovedildo/solodildo.png"
    show toxd toxd00c
    show toxd_head lewd
    with Dissolve(1.5)
    ty "I need to... put it in here... AHH!!" with hpunch

    show toxd toxd01 with Dissolve(1.5)
    show toxd_head eyesfront
    ty "Ehehe... just a second."
    hide toxd_head
    show toxd toxd02 with Dissolve(1.5)
    ty "Mmmh, I'm pushing down now."

    show toxd toxd03 with Dissolve(1.5)
    ty "fuuurther..."
    show toxd toxd04 with Dissolve(1.5)
    ty "I'm eating it all up!!"

    show toxd toxd05a with Dissolve(1.5)

    ty "Ahh!"
    ty "I'm kissing it, but like really deep!"

    show toxd_head eyesfront:
        ypos 12
    show expression "bk3/tylee/lovedildo/body_1_armpoint.png":
        ypos 0 xpos 1000
        linear 0.8 xpos 900
        linear 1.2 ypos 100 xpos 800
    ty "It reaches about... "
    ty "here."
    ty "Do you like the show so far?"
    hide expression "bk3/tylee/lovedildo/body_1_armpoint.png"

    show toxd toxd05a
    y "There's literally no way I can't like this!"
    show toxd toxd01
    hide toxd_head
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "Good!"
    ty "And that was just the warm up!"
    ty "Now watch closely as I make it disappear and appear again! "
    ty "Like a magician!"

    hide toxd_head
    show toxd toxd100

    $ renpy.pause()


    ty "Ah!... Aah!!..."
    ty "do you... like this?"
    y "Best damn magic show ever."
    y "All magicians should be pretty girls and this should be their first trick!"

    menu:
        "do some x-ray trickery ":
            $ toxd_transparent = 'dildo'
        "keep going like this":

            pass
    $ renpy.pause()
    ty "I have one more trick to show you!"
    ty "I call it... rockin the cradle!"
    show toxd toxd101
    y "Fuck this is hot..."
    y "Would you mind me jacking off to this?"
    ty "Not at all!"
    ty "...*Unff!!*... Go a ...*unff!!*... ahead!!"


    ty "Ah... i'm feeling funny!!"

    y "I'm getting there too, just go with it!"

    show toxd toxd05a with hpunch
    show toxd toxd05a with hpunch

    hide toxd
    show toxd toxd06
    with Dissolve(1.5)
    $ renpy.pause()
    show toxd toxd07 with Dissolve(1.5)
    $ renpy.pause()

    y "I'll take care of the encore."
    play sound "audio/gltch2b.mp3"
    show expression "bk3/tylee/lovedildo/spermout_dildo1.png"
    $ renpy.pause()
    play sound "audio/gltch2b.mp3"
    show expression "bk3/tylee/lovedildo/spermout_dildo2.png"
    $ renpy.pause()
    play sound "audio/gltch2b.mp3"
    show expression "bk3/tylee/lovedildo/spermout_dildo3.png"

    ty "*Pant...* *pant...*"
    ty "that... that was really nice!"
    ty "Suki is a great friend to have!"
    y "Yeah, I like her a lot too."

    jump love_bk3_next


label naga_clawjob:
    stop music
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
    show expression "bk3/naga/bj/bg_dream.jpg"

    show toxe toxe00:
        ypos 40 xpos 330
        parallel:
            linear 2.0 ypos 60
            linear 2.0 ypos 40
            repeat
        parallel:
            linear 6.0 xpos 500
            linear 6.0 xpos 330
            repeat

    "{i} Lisssten to me!{/i}" with hpunch
    y "{size=+5}ah!" with hpunch
    y "what the shit?!"
    y "you can't just pop up in my-"
    y "......"
    y "OH my god!!"
    y "You're so cute!"
    "{i} We have seriousss thingsss to talk about...{/i}"
    y "Coochie, coochie, coo!"

    show toxe toxe01 with Dissolve(1.5)
    "{i} SSSilence!!!{/i}" with hpunch
    y "Aaaawhh, you're even cute when you're angry!"
    y "Okay, but seriously now..."
    y "What the flying fuck are you and what are you doing in my mind?"

    show toxe toxe09 with Dissolve(1.5)
    "{i}I wasss born when you took the eyesss..."
    "{i}freed."
    y "So you're not the dreamstealer?"
    "{i} A part of her... small, weak... but strong here... hiding."
    y "Here where? My mind? My dreams?"
    "{i}HISSSS!!!!{/i}"
    "{i}Your mind is unssstable, illusssionsss, hallucinationsss."
    "{i}You're tainted.{/i}"
    y "Really?"
    y "Except for some restless dreams... which YOU could've done for all i know... I feel fine."
    "{i}I've been protecting you, but I can't do much more..."
    "{i}...not unless you allow me within your mind.{/i}"
    "{i}Invite me in.{/i}"
    y "Invite?"
    y "Wow, you certain you're not a vampire?"
    y "Needing permission to enter?"
    y "Anyway, not gonna happen... why would I trust you?"
    y "Why do you even want to help me?"
    y "So far anything with a lisp has caused me nothing but trouble."
    show toxe toxe01 with hpunch
    "{i}HISSSS!!!! Foool!!!{/i}"
    y "You're not winning me over..."
    show toxe toxe00
    "{i}I can do other things for you....{/i}"



    show expression "bk3/naga/clawjob/playerbody.png"
    show expression "bk3/naga/clawjob/dicksolo.png":
        xpos 360 ypos 0
    with Dissolve(1.5)
    y "what the..."
    "{i}...Sssshhhht...{/i}"

    hide toxe
    hide expression "bk3/naga/clawjob/dicksolo.png"
    show toxe toxe03:
        linear 2.0 ypos 10
        linear 2.0 ypos 0
        repeat
    with Dissolve(1.5)
    "{i}Like this... you like thisss... right?{/i}"
    y "....I don't dislike it."
    y "But I still won't let you burrow into my mind."
    "{i}Prreettyy pleasssse?{/i}"
    y "Nope."
    show toxe toxe04

    show expression "bk3/naga/clawjob/tailcover.png":
        xpos 620 ypos 120
        linear 2.0 yzoom 1.0 ypos 300 rotate 0 xpos 630
        linear 2.0 yzoom 0.9 ypos 120 rotate 20 xpos 620
        repeat

    "{i}Prreeeettyy pleasssse?{/i}"
    y "No, you little vixen!"

    hide expression "bk3/naga/clawjob/tailcover.png"
    show toxe toxe01
    show expression "bk3/naga/clawjob/dicksolo.png":
        xpos 360 ypos 0
    with Dissolve(1.5)

    "{i}HIsss!!"
    "{i}Ssstop being ssso ssstubborn!!{/i}"
    "{i}Your sssafety is my sssafety!!{/i}"
    show toxe toxe00:
        xpos 300
    with Dissolve(1.5)
    "{i}SSsorryy, I'm a bit on edge... Let me... continue.{/i}"
    menu:
        "use your tail":
            hide toxe
            show toxe toxe04
            show expression "bk3/naga/clawjob/tailcover.png":
                xpos 620 ypos 120
                linear 2.0 yzoom 1.0 ypos 300 rotate 0 xpos 630
                linear 2.0 yzoom 0.9 ypos 120 rotate 20 xpos 620
                repeat
        "use your little clawhands":
            hide toxe
            hide expression "bk3/naga/clawjob/dicksolo.png"
            show toxe toxe03:
                linear 2.0 ypos 10
                linear 2.0 ypos 0
                repeat
    y "Damn, that's nice."
    y "I'm about to \"pop the cork\"!"

    scene black
    show expression "bk3/naga/bj/bg_dream.jpg"
    show expression "bk3/naga/clawjob/playerbody.png"
    show toxe toxe05
    with Dissolve(1.5)
    "{i}Would you like me to drink your champagne? {/i}"

    menu:
        "No, gonna go for a facial!":
            play sound "audio/gltch2b.mp3"
            show expression "bk3/naga/clawjob/spermout_1.png" with hpunch
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show expression "bk3/naga/clawjob/spermout_2.png" with hpunch
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show expression "bk3/naga/clawjob/spermout_3.png" with hpunch
            $ renpy.pause()


            scene black
            show expression "bk3/naga/bj/bg_dream.jpg"


            show toxe toxe08:
                xpos 300
                linear 3.0 ypos 20
                linear 3.0 ypos 40
                repeat
            with Dissolve(1.5)
            "{i}That'sss... thick ssstuff...{/i}"
        "Swallow it all!":

            show toxe toxe06
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            $ renpy.pause()
            show toxe toxe06
            play sound "audio/gltch2b.mp3"
            $ renpy.pause()

            scene black
            show expression "bk3/naga/bj/bg_dream.jpg"

            show toxe toxe07:
                xpos 300
                linear 3.0 ypos 20
                linear 3.0 ypos 40
                repeat
            with Dissolve(1.5)
            "{i}Burrp! That'sss... more than I expected.{/i}"
    "{i}I'll leave you alone now..."
    "{i}Do I have your permisssion?{/i}"

    y "Hmmm what? Sure."
    "{i}Thankssss!{/i}"
    hide toxe with Dissolve(1.5)
    y "...wait, I gave you permission to leave! Nothing else!"

    "{i}NO! That totally counted as an invite into your mind!!!{/i}" with hpunch
    y "Nuh-uh!"
    "{i}Yeah-eh!{/i}"
    "{i}Don't worry... It'll be better for both of usss.{/i}"
    "{i}I'm leaving for real now."
    "{i}And I have your permisssion!{/i}"
    y "You're leaving with my permission to leave! That's it!"
    "{i}Lalalalal! "
    "{i}I can't hear you!! {/i}"
    jump love_bk3_next


label love_train_hj:

    y "it's nice to get away for a bit."
    k3 "yeah, it..."
    show toki toki01
    k3 "what's that?"
    y "what?"
    k3 "you're sitting on something."
    y "i am?"
    "you reach under your seat and find a magazine..."
    if smellerbee_gone:
        play sound "audio/win2.mp3"
        "it's a pornlove!"
        y "who just leaves a pornlove around?"
        y "don't they know how valuable these are?"
        k3 "well...?"
        y "well, what?"
        show toki toki_smile
        k3 "aren't you going to open it?"
        y "...you want to see what's in it?"
        k3 "yeah! come on, let's take a look!"
        y "alright..."

        scene black
        scene smeller_dp1
        with Dissolve(1)
        show ctc
        pause
        hide ctc
        k3_n "oh, that's hot."
        show ctc
        pause
        hide ctc
        y "i guess she really did it."
        k3_h "is that... smellerbee?"
        y "you remember her?"
        k3_n "of course i do."
        k3_n "she... looks good."
        y "i'll say."
        k3_h "oh! looks like somebody else agrees, too...."
        k3_h "i can see you growing down there."
        y "well, i mean... you can't blame me..."
        k3_n "i don't..."
        k3_h "want me to jack you off?"
        y "...."
        y "...are you serious?"
        k3_h "yeah!"
        k3_h "come on, it'll be fun!"
        y "we're on a train... we could get caught."
        k3_h "i don't care."
        scene black
        scene basingse_city_1
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        with Dissolve(1)
        y "i don't know..."
        show tokh arm_hj
        with Dissolve(1)
        "ignoring you, katara pulls out your cock and lightly wraps her hand around it."
        y "um."
        "she wraps her fingers around your shaft and squeezes you as she pulls."
        k3_n "mmm... that magazine really did make you hard, didn't it?"
        y "w-well yeah... damn..."
        k3_h "come on, look at the pages again..."
        scene black
        scene smeller_dp1
        with Dissolve(1)
        show ctc
        pause
        hide ctc
        k3_n "flip the page!"
        k3_h "i wanna see if she actually did it!"
        scene black
        scene smeller_dp2
        with Dissolve(1)
        k3_h "oooo, sexy!"
        show ctc
        pause
        hide ctc
        k3_h "look at that tight, tiny butt and pussy."
        k3_h "that looks like untapped territory to me..."
        k3_n "you think she's a virgin?"
        k3_p "you think she's gonna get stuffed harder than she can take?"
        k3_p "so full of cock she can't think?"
        "katara's stroking becomes more insistent."
        y "unnngh...."
        y "you're... uhh... getting turned on, aren't you?"
        k3_h "hmmm..."
        k3_h "i wonder what happens next..."
        "you look back down at her hand, now truly pumping your cock."
        scene black
        scene basingse_city_1
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        show tokh arm_hj2
        with Dissolve(1)
        y "oh shit, katara..."
        k3_h "shhh..."
        k3_h "don't you want to see the last page?"
        k3_p "don't you want to know what happens to poor, little, smellerbee?"
        show tokh arm_hj3
        "katara speeds up even more, working your cock to ecstasy."
        y "I... i do..."
        k3_n "relax, take a look..."
        k3_h "you're in good hands...."
        y "unnhh..."
        scene black
        scene smeller_dp2
        with Dissolve(1)
        show ctc
        pause
        hide ctc
        k3_n "flip the page, aang!"
        k3_h "I wanna see her get stuffed!"
        y "o-okay..."
        scene black
        scene smeller_dp3
        with Dissolve(1)
        y "damn!" with vpunch
        show ctc
        pause
        hide ctc
        k3_p "oh, she wasn't ready for that, was she?"
        show ctc
        pause
        hide ctc
        k3_h "not only did she take her first cock... she took two at once!"
        k3_p "her poor ass... and pussy..."
        k3_p "...getting filled with sperm..."
        y "unghh..."
        k3_h "oh dear, are you about to cum?"
        y "fffuuuuuu...."
        k3_p "huh? you gonna cum?"
        k3_p "you gonna cum all over my little hands?"
        k3_u "right here on the train?"
        k3_u "we won't be able to hide it, you know..."
        k3_n "what will people say?"
        y "uhh... katara... unh..."
        k3_p "do it. cum on her."
        k3_p "cum on that slut."
        k3_p "and on me..."
        k3_p "cum on my hand..."
        k3_p "let me see you shoot that big load."
        y "I'm... gonna..."
        k3_h "shoot that big, sticky, thick load on-"
        play sound "audio/splurt2.ogg"
        show expression "bk3/toph/missionary/spermout1.png":
            zoom 2 xpos -300 ypos -300
        with flash
        k3_h "oh!"
        play sound "audio/splurt3.ogg"
        hide expression "bk3/toph/missionary/spermout1.png"
        show expression "bk3/toph/missionary/spermout2.png":
            zoom 2 xpos -300 ypos -300
        with flash
        show ctc
        pause
        hide ctc
        k3_h "mmmm.... good for you, aang..."
        k3_h "cum all over that tiny slut."
        k3_h "you also came all over my hand..."
        scene black
        scene basingse_city_1
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        show expression "bk3/katara/handjob/kat_arm_6.png":
            xpos 400 ypos 320
        show expression "azula/handjob/az_sperm_3.png":
            xzoom -1 rotate 20 xpos 100 ypos -165
        with Dissolve(1)
        show ctc
        pause
        hide ctc
        "the door to your cabin opens and a woman steps inside."
        dap1 "hello, is this-"
        dap1 "oh!"
        k3_h "hello."
        y "uh..."
        k3_h "we're a little busy."
        dap1 "i... i see that..."
        dap1 "i'll... just... go..."
        dap1 "......."
        dap1 "that's a big dick."
        dap1 "bye!"
        "the woman leaves in a hurry, but gives one last look before closing the door."
        k3_h "hahahaha!"
    else:

        "...but the pages are stuck together."
        k3 "is that a pornlove?"
        y "yeah, but... ew... the pages are stuck together..."
        y "man, what a waste."
        k3 "that is a waste, isn't it?"
        k3 "i mean... how will you get off without a magazine?"
        y "......."
        y "i don't {i}need{/i} a magazine, it just helps."
        show toki toki_smile
        k3 "what if... i helped you instead?"
        y "...we're on a train, katara."
        y "we'd get caught."
        k3 "maybe not."
        hide toki with dissolve
        "katara slips onto the seat next to you."
        y "what are you..."
        k3_h "want me to jack you off?"
        y "...."
        y "...are you serious?"
        k3_h "yeah!"
        k3_h "come on, it'll be fun!"
        y "we're on a train... we could get caught."
        k3_h "i don't care."
        y "i don't know..."
        show tokh arm_hj
        with Dissolve(1)
        "ignoring you, katara pulls out your cock and lightly wraps her hand around it."
        y "um."
        "she grips her fingers around your shaft and squeezes you as she pulls."
        k3_n "mmm... you got hard quickly."
        y "w-well yeah... damn..."
        show tokh arm_hj2
        "katara's stroking becomes more insistent."
        y "unnngh...."
        k3_h "you're getting turned on, aren't you?"
        k3_n "hmmm..."
        "you look back down at her hand, now truly pumping your cock."
        hide totr
        hide tokh
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        show expression "maze/sp_prisonbitch.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        show expression "maze/sp_prisonbitch_clothes.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        show tokh arm_hj2
        with Dissolve(1.5)

        dap2 "hello, is this-"
        dap2 "oh!"
        y "um... occupied..."
        dap2 "i... i see that..."
        dap2 "i'll just... go..."
        dap2 ".........."
        k3_p "you like his cock, don't you?"
        dap2 "um..."
        k3_n "don't be shy."
        dap2 "it... it is handsome..."
        y "why... fuck... why are you wearing those rags?"
        dap2 "i escaped a... a real maze of a place."
        dap2 "i haven't had a chance to change."
        k3_n "would you like to see something fun?"
        show tokh arm_hj3
        "katara speeds up even more, working your cock to ecstasy."
        y "oh... oh shit..."
        show ctc
        pause
        hide ctc
        "the woman stares at your cock as katara rapidly hand-fucks it."
        k3_n "you're among friends here... you can take off your clothes."
        dap2 "i don't know if-"
        k3_p "do it."
        dap2 "...o-okay..."
        hide expression "maze/sp_prisonbitch_clothes.png" with dissolve
        y "oh... shit... that... worked..."
        dap2 "i've been... been following orders for so long..."
        k3_n "you can relax, you're in good hands...."
        y "are you... talking to... her or me, katara?"
        k3_n "yes."
        y "unnhh..."
        k3_h "oh dear, are you about to cum?"
        y "fffuuuuuu...."
        k3_p "huh? you gonna cum?"
        k3_p "you gonna cum all over my little hands?"
        k3_u "right here on the train?"
        k3_u "we won't be able to hide it, you know..."
        k3_n "what will people say?"
        y "uhh... katara... unh..."
        k3_p "do it. cum on her."
        dap2 "wait..."
        k3_p "cum on that slut."
        k3_p "let me see you shoot that big load."
        y "I'm... gonna..."
        dap2 "hold on, i don't-"
        k3_h "shoot that big, sticky, thick load on-"

        play sound "audio/splurt2.ogg"
        hide totr
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        hide expression "maze/sp_prisonbitch.png"
        show expression "maze/sp_prisonbitch.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        show expression "maze/sp_prisonbitch_sperm1.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        hide tokh
        show tokh arm_hj3
        with flash
        dap2 "oh!"
        play sound "audio/splurt3.ogg"
        hide totr
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        hide expression "maze/sp_prisonbitch.png"
        show expression "maze/sp_prisonbitch.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        hide expression "maze/sp_prisonbitch_sperm1.png"
        show expression "maze/sp_prisonbitch_sperm2.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        hide tokh
        show tokh arm_hj3
        with flash

        dap2 "you... you're... you're cumming all over m-"
        k3_h "drench that bitch!"
        play sound "audio/splurt2.ogg"
        hide totr
        show totr totr101:
            ypos -10
            linear 1 ypos 0
            ypos 0
            linear 1 ypos -10
            repeat
        hide expression "maze/sp_prisonbitch.png"
        show expression "maze/sp_prisonbitch.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        hide expression "maze/sp_prisonbitch_sperm2.png"
        show expression "maze/sp_prisonbitch_sperm3.png":
            xpos 300 ypos 0
            linear 1 ypos 10
            ypos 10
            linear 1 ypos 0
            repeat
        hide tokh
        show expression "bk3/katara/handjob/kat_arm_6.png":
            xpos 400 ypos 320
        show expression "azula/handjob/az_sperm_3.png":
            xzoom -1 rotate 20 xpos 100 ypos -165
        with flash
        show ctc
        pause
        hide ctc
        dap2 "......."
        k3_h "mmmm.... good for you, aang..."
        k3_h "you came all over that slut."
        k3_h "you also came all over my hand..."
        dap2 "i... i think i should... i should go..."
        hide expression "maze/sp_prisonbitch_sperm3.png"
        hide expression "maze/sp_prisonbitch.png"
        with moveoutright
        "the woman leaves in a hurry, but gives one last look before closing the door."
        k3_h "hahahaha!"

    jump katara_train_cont


label suki_barblow:
    hide screen earth_money_date

    "You take your position behind the bar."
    if suki_bar_blow ==6:
        y "damn it..."
        y "there's so many people in here."
        y "how many stupid drinks i'm i gonna have to-"
    if suki_bar_blow ==7:
        "you feel a hand rest against your cock, over your pants."
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    scene black

    show expression "bk3/suki/barblow/floor.jpg"
    show expression "bk3/suki/barblow/floor_body.png"
    show expression "bk3/suki/barblow/floor_torso.png":
        xpos 360 ypos 10
    show expression "bk3/suki/barblow/floor_head.png":
        xpos 360 ypos 25
    show expression "bk3/suki/barblow/desk.png":
        xpos 0 ypos 0
    if suki_bar_blow ==7:
        y "oh!" with hpunch
        y "easy, girl..."
    if suki_bar_blow ==6:
        y "Wha... the fuck?!" with hpunch
        y "Suki?"
    suki "...hehehe..."
    if suki_bar_blow ==6:
        y "What are you doing?"

    show expression "bk3/suki/barblow/floor_torso.png":
        xpos 360 ypos 10
        linear 4.0 ypos 60
    show expression "bk3/suki/barblow/floor_head.png":
        xpos 360 ypos 25
        linear 4.0 ypos 90
    show expression "bk3/suki/barblow/desk.png":
        xpos 0 ypos 0
        linear 2.0 alpha 1.0
        linear 2.0 alpha 0.8
    if suki_bar_blow ==6:
        suki "I just thought we might have a conversation."
    show ctc
    pause
    hide ctc
    if suki_bar_blow ==6:
        y "uh-huh..."
        suki "and that... i don't know... maybe you'd be more receptive if we did it like this."
        y "uh...."
        suki "Just go with it!"
    if suki_bar_blow ==7:
        y "you haven't forgotten that we're surrounded by people, right?"
    if suki_bar_blow ==6:
        y "There's people in here..."
    suki "well, you're the bartender."
    suki "take their orders."
    if suki_bar_blow ==6:
        y "but you're... i don't... what if..."
    "Suki pulls down your pants while a customer approaches the bar."
    show expression "bk3/suki/barblow/flash.png"
    show expression "bk3/suki/barblow/floor_dick.png"
    $ renpy.pause(0.2)
    hide expression "bk3/suki/barblow/flash.png" with dissolve
    if suki_bar_blow ==6:
        y "oh shit."
    suki "don't mess up any orders, aang..."
    show ctc
    pause
    hide ctc

    scene black
    hide text
    show expression "ebackgrounds/bar.jpg"
    show toxc toxc01
    show expression "bk3/suki/barblow/top.png":
        alpha 0.8
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    "you feel warm breath panting against your cock as the customer stops at the bar."

    suki "Hmmmm... it looks delicious!!!"
    y "{size=-5}shut up, suki..."
    show toxc toxc02
    if suki_bar_blow ==6:
        suki "ooo, that is a tasty looking cock..."
    suki "I'm going to have some fun with this."
    bk3c "Sorry, did you say something?"
    y "...no."
    y "What can I get you?"
    if suki_bar_blow ==6:
        bk3c "Give me a filthy Larry."
        y "(a fuckin' what?)"
    if suki_bar_blow ==7:
        bk3c "tequila."
        y "you got it."
    show toxc toxc03
    show expression "bk3/suki/barblow/arm_holddick.png"
    with Dissolve(1.5)
    "Suki takes your dick in her mouth and start making circular motions with her tongue."

    y "hnnnnh..."
    show ctc
    pause
    hide ctc
    if suki_bar_blow ==6:
        y "(i have no idea what that drink is... and suki is hell of... distracting...)"
    bk3c "come on man, i don't have all night."
    if suki_bar_blow ==6:
        y "(i'll just throw something together.)"

        call screen e_bar_screen1

        play sound "audio/bubbles.ogg"
        "you send [drink3] to the [tumbler]."
        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        "you send [drink4] to the [tumbler]."

        y "Here's your dirty harry."
    if suki_bar_blow ==7:
        y "here you go."

    show toxc_servedrink
    play sound "audio/thud.mp3"    
    cus "That's... not what I ordered."
    y "Ah sorry, this one is on the house."
    bk3c "Thanks!"
    hide toxc_servedrink
    show toxc toxc04
    hide expression "bk3/suki/barblow/arm_holddick.png"
    with Dissolve(1.5)
    y "ungh! shit!"
    bk3c "hey, don't beat yourself up man, it happens."
    y "go sit down!"
    bk3c "...i like when you take charge."
    "the customer walks back to their table."
    y "Suki, that feels reeeally nice, but..."
    y "I don't think I'll be able to get anyone's order right with my dick in your mouth."
    y "Especially when you do that thing with your tongue."
    show toxc toxc08 with Dissolve(1.5)
    "With a small plopping sound Suki pulls her lips from your cock."

    suki "suck it up."
    y "really?"
    suki "well, if i'm sucking it up, you should too."
    suki "it's not like i get their drinks right anyway."
    y "......."
    y "I'd be a lot more upset with that work ethic if you didn't say that right after taking my cock out of your mouth."
    suki "It's the magic of a good blowjob!"
    bk3c "hey, that-"
    y "ah!"
    y "i mean... hello-"
    show toxc toxc05 with dissolve
    y "ah!"
    suki "mmmmghhh...."
    bk3c "....."
    y "....hello, sir."
    bk3c "...right."
    bk3c "well, that dirty harry actually tasted pretty damn good, Can I have another one?"
    y "You finished it already?!"
    bk3c "I was thirsty!"
    y "i-"
    show toxc toxc06 with dissolve
    suki "*gahgh*"
    y "-oof."
    bk3c "what?"
    y "i was saying..."
    show toxc toxc106
    suki "*sluuurp!*"
    show ctc
    pause
    hide ctc
    y "oh sweet baby roku."
    bk3c "....what?"
    y "i was... i was gonna say..."
    y "that i like that in my customers..."
    bk3c "like what?"
    y "you... being thirsty... fuck..."
    bk3c "did... you just call me a thirsty fuck?"
    y "no... the... the fuck was unrelated..."
    if suki_bar_blow ==6:
        bk3c "....are you dying?"
        y "are you?"
        bk3c "fucking maybe!"
        bk3c "is this purgatory?!"
        bk3c "....are you even listening?"
        y "who are you?"
        bk3c "........."
        bk3c "can you just make me another dirty harry?"
    if suki_bar_blow ==7:
        bk3c "just get me another tequila."

    y "sure."
    if suki_bar_blow ==6:
        y "(....i have no idea how i made it.)"
        y "(okay, this is too much thinking.)"
        y "(i'm gonna pull a bill murray here...)"
        y "(everyone gets tequila.)"

    play sound "audio/thud.mp3"
    show toxc_servedrink

    y "Here you go!"
    bk3c "Thanks!"
    hide toxc_servedrink

    "they walk back to their table."
    y "this is... getting stressful."
    show toxc toxc08 with dissolve
    suki "yeah? you sure you're not having fun?"
    y "...maybe a little."
    suki "hey, so..."
    show toxc toxc04 with dissolve
    y "ah..."
    suki "*mmmmmm....*"
    suki "*slluuurp*"
    if suki_bar_blow ==6:
        show toxc toxc08 with dissolve
        suki "I wanted to ask you something."
        y "yeah?"
        suki "if you say yes..."
        suki "i'll suck you off."
        show toxc toxc04 with dissolve
        suki "hhmmmm...."
        "suki hums, vibrating the bit that's in her mouth."
        y "ahhh..."
        y "and if i say no?"
        show toxc toxc08 with dissolve
        suki "then we'll call it even and i'll go back to bartending."
        suki "but... i'm really, really hoping you'll say yes."
        y "....."
        y "alright, what is it?"
        suki "well..."
        suki "you know how i'm trying to save up to bribe the palace guards into releasing my friends?"
        y "yes..."

        suki "can i...."
        suki "....can i keep all my tips from now on?"
        suki "instead of splitting them with you?"
        y "oh, i don't know about-"
        suki "wait! before you answer."


    show toxc toxc05 with Dissolve(1.5)
    show toxc toxc100
    show ctc
    $ renpy.pause()
    hide ctc
    suki "*schluurrrpp...* *schlurp...* *schurp...* *sccchlluuuurp...*"
    y "uuuuhhhhh...."
    show ctc
    pause
    hide ctc
    "the wet warmth radiating from her mouth engulfs and soaks you as she sucks and gulps at your cock."
    show ctc
    pause
    hide ctc
    if suki_bar_blow ==6:
        y "this... this isn't fair..."

        bk3c "hey! so that wasn't a dirty-"
        y "dude!"
        y "please!"
        y "come on!"
        bk3c "...what?"
        y "i... nevermind. sorry."
        bk3c "you sure you're okay?"
        y "i am maybe in the middle of a panic attack."
        bk3c "...?"
        y "also... i'm worried that you have a drinking problem."
        bk3c "yeah, and you're welcome."
        bk3c "so..."
        bk3c "...that was just tequila."
        bk3c "not a dirty larry or a dirty harry."
        bk3c "it was just a lot of tequila."
        bk3c "with no mixer."
        bk3c "who does that?"
        y "yeah, i know, that's... fuck!... all i have."
        bk3c "...what about all those other bottles?"
        suki "*shhlllllllluuuuuuuurp* *gag* *smack*"
        y "they're... unnnnghh..."
        y "...decoration."
        bk3c "decoration?"
        bk3c "....."
        bk3c "...all of them?"
        y "yes! now what do you want?!"
        bk3c "i mean... i guess a shot of-"
        play sound "audio/thud.mp3"
        show toxc_servedrink

        y "here!"
        y "go away!"
        bk3c "...you're lucky these drinks are free."
        hide toxc_servedrink
        "the customer walks away."
        y "have... have i not been charging him?"
        y "damn it, suki! i can't do both!"

        suki "*sluurp*"
        show toxc toxc08 with dissolve
        suki "ah!"
        suki "that was just a little sample."
        suki "so, what do you think?"
        y "i think that this is not fair at all."
        y "you can't ask a favor from me when my cock is in your mouth."
        suki "but i can."
        y "that's a lot of money..."
        show toxc toxc08_2 with dissolve

        suki "pleeease?"
        show ctc
        pause
        hide ctc
        suki "I'll make you cum."
        suki "so hard."
        show toxc toxc08_1 with dissolve
        suki "i promise."
        suki "you know you want to cum on my face..."
        suki "or..."
        show toxc toxc04 with dissolve
        suki "...in my mouth."
        y "uh...."
        show toxc toxc08 with dissolve
        suki "all you have to do is let me keep my tips."
        y "i... don't think that's a great idea."
        y "maybe i should go..."
        show toxc toxc08_1

        with dissolve
        suki "wait!"
        suki "how about... how about a compromise?"
        y "....i'm listening."
        show toxc toxc04
        with dissolve
        suki "*sluuurp...*"
        suki "*uummm...*"
        suki "...every... every day you let me keep my tips, i'll suck you off."
        suki "...okay?"
        y "well..."
        show toxc toxc102
        show ctc
        pause
        hide ctc
        suki "*slluuurp* *slurp* gag*"
        suki "*suuuck...*"
        suki "*mmmmm....*"
        show toxc toxc08_1 with dissolve
        suki "please!"
        suki "it's a good deal!"
        suki "i promise to make you shoot a huge, huge load!"
        suki "in my mouth, face, tits, wherever you want!"
        y "i don't want to take advantage of you..."
        suki "you're not! i'll enjoy it!"
        show toxc toxc04 with dissolve
        suki "*scchhlluup!*"
        y "well, that does seem like a good deal..."
        y "and it's money that you make anyway."
        y "i'm just letting you keep it."
        y "and only on days you suck me off..."
        y "...okay, i agree."
        show toxc toxc08 with dissolve
        suki "starting today, okay?"
        suki "if i suck semen out of this cock, right now, i'll keep the tips for today, okay?"
        menu:
            "you can keep today's tips":
                y "(that's like... 11 coins.)"
                y "(and she needs it more than me, anyway.)"
                y "(i'll help her out.)"
                y "sure, you can keep today's tips."
            "i need a gesture of good faith":
                y "what if it's a bad blowjob?"
                suki "it won't be!"
                y "i can't agree to that without a demonstration."
                suki "o-okay."
                suki "but next time?"
                y "next time."

        suki "awesome."
        suki "let's do this."
    suki "i'm gonna make you blow so hard."
    show toxc toxc04 with dissolve
    suki "come on, let's get this face fucked."
    show toxc toxc06 with Dissolve(1.5)
    show toxc toxc107
    show ctc
    pause
    hide ctc
    suki "*suck!* *slurp!*"
    y "damn!"
    y "this... is... nuts..."
    suki "*gasp!*"
    bk3c "hey, it's me again, can i-"
    y "damn you!"
    suki "*schluurrrpp* *schluurrrpp*"
    bk3c "What's that sound I keep hearing?"
    y "Pro... pro...aaahh...bably a cat."
    show toxc toxc06 with Dissolve(1.5)
    suki "Meww!! Meeewww!!"
    y "No! Bad kitty! Bad Kitty!!"
    show toxc toxc107
    suki "*slllurp!*"
    bk3c "Another Dirty Harry please."
    y "one tequila, coming up."
    play sound "audio/thud.mp3"
    show toxc_servedrink
    y "here."
    bk3c "cheers!"
    hide toxc_servedrink
    "he wanders off."
    show toxc toxc08 with Dissolve(1)
    suki "mmm..."
    y "you're not... gonna stop now, are you?"
    suki "relax, i'm not going anywhere..."
    suki "...although pretty soon {i}you'll{/i} be {i}coming{/i}."
    show toxc toxc03 with dissolve
    suki "get it?"
    show toxc toxc04 with dissolve
    y "that's a terrible joke."
    suki "who's telling jokes?"
    show toxc toxc101
    y "hnnngg!" with hpunch
    show ctc
    pause
    hide ctc
    suki "*gulp!* *sllllllllurp!*"
    y "damn girl!"
    suki "*slurp* *slurp* gagh* *mmgh*"
    show ctc
    pause
    hide ctc
    y "that's..."
    y "oh, what the hell!"
    y "this stupid customer keeps coming back!"
    show toxc toxc100 with Dissolve(1)
    suki "don't... *slurp...* mess... *gulp...* up..."
    suki "i... *ahhh...* need... *mmmmm...* these... *shhlurp...* customers..."
    show ctc
    pause
    hide ctc
    y "you're not making this easy."
    suki "*mmmmm....*"
    suki "focus on the job, baby..."
    y "i am."
    suki "i meant that job."
    y "oh."
    show ctc
    pause
    hide ctc
    suki "i'll just be here... taking my time..."
    suki "...enjoying slobbering on your cock... "
    suki "...while you focus..."
    show toxc toxc103
    y "fuck!"
    show ctc
    pause
    hide ctc
    bk3c "hey! i-"
    play sound "audio/thud.mp3"
    show toxc_servedrink
    y "here!"
    y "go away!"
    y "something important is happening!"
    bk3c "....."
    bk3c "okay!"
    hide toxc_servedrink
    show ctc
    pause
    hide ctc
    y "that guy...."
    y "how is he still conscious?"
    show toxc toxc08_1 with Dissolve(1)
    suki "I watered down all the bottles."
    show toxc toxc100 with Dissolve(1)
    show ctc
    pause
    hide ctc
    y "...i'd give you a promotion if you weren't my only employee."
    y "also, why are you slowing down?"
    show toxc toxc08 with Dissolve(1)
    suki "i can feel you swelling... you're getting close aren't you?"
    y "i... well... yeah..."
    suki "i'm not going to let you cum yet."
    y "...say again?"
    suki "i'm not finished enjoying feeling you throbbing in my mouth."
    show toxc toxc06 with Dissolve(1)
    suki "squeezing you with my throat muscles... pressing my tongue into you..."
    y "Unnnghh...."
    show toxc toxc100 with Dissolve(1)
    suki "*sluuurp*"
    suki "you're not gonna cum from these slurps, are you?"
    suki "*slurp!* *slurp!* *slurp!*"
    suki "just from these slurps here?"
    y "uuuhhhh...."
    y "I'm gonna cu-"
    y "oh, that stupid... that customer is coming up here again!"
    suki "take his order when you drench my throat."
    suki "let it all go, down my throat, while you work."
    show toxc toxc104
    suki "*gag!*"
    show ctc
    pause
    hide ctc
    y "fuck!"
    bk3c "what?"
    y "no-nothing..."
    y "what do... ah... what... fuck..."
    bk3c "dude, your face is really red."
    bk3c "you're shaking!"
    suki "*slurp!!* *sluuurp!!* *gulp!!*"
    y "ah! fuck!"
    bk3c "shit!"
    bk3c "dude, are you gonna die?"
    y "what... god {i}damn{/i} it! what do you want!? fuck!"
    bk3c "i mean... a guess another shot of tequila."
    bk3c "but it's not my favorite."
    bk3c "i guess i was just thinking that..."
    "the customer starts rambling..."
    "you feel your balls begin to churn, drenched as they are with suki's spit."
    show ctc
    pause
    hide ctc
    y "(oh, shit, suki!)"
    show toxc toxc105
    "feeling you tense up, suki goes all out, fucking your cock with her face and wet, pouty lips."
    suki "*slurp!!* *slurp!!* *slurp!!*"
    show ctc
    pause
    hide ctc


    menu:
        "unload on her face!":
            show toxc toxc08_1 with Dissolve(1)
            suki "cover me!"


            bk3c "where's my drink?"
            show expression "bk3/suki/barblow/glass_hand.png" with hpunch
            y "fuck... ing... ah... here!"

            "leaning on the counter, you take one step back just before you blow."

            hide toxc
            show toxc toxc00
            hide expression "bk3/suki/barblow/top.png"
            show expression "bk3/suki/barblow/top.png":
                alpha 0.8
            show toxc_playbody
            with dissolve

            suki "that's it... come on...."

            show expression "bk3/suki/barblow/blink.png":
                xpos 531 ypos 187
            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/spermout_1.png"
            with flash
            suki "....mmmm!"
            show ctc
            pause  
            hide ctc
            y "fuck!"

            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/spermout_2.png"
            with flash
            suki "yes, sexy...."
            show ctc
            pause  
            hide ctc
            bk3c "...what's happening now?"
            suki "hmmm... yes... that's it..."
            show ctc
            pause  
            hide ctc
            bk3c "hey! let go of my drink!"
            suki "that... was a lot of-"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/spermout_3.png"
            hide expression "bk3/suki/barblow/blink.png"
            with flash
            show ctc
            pause  
            hide ctc
            suki "....whoa."
            suki "this... is a lot of semen."
            show ctc
            pause
            hide ctc
            suki "i don't... even know how i'm gonna get out of here..."
            hide expression "bk3/suki/barblow/glass_hand.png" with dissolve
            "you let go of the drink."

            bk3c "thanks man."
            bk3c "but i think you should get checked for epilepsy."

            show ctc
            pause
            hide ctc
            y "fuck... that... guy..."
            show expression "bk3/suki/barblow/arm_bitefinger.png"
            suki "that was a huge load..."
            y "you earned it."
            suki "i did, didn't i?"
            suki "Maybe I could use it to make a special girls only {i}cock{/i}tail."
            y "what did i say about your jokes?"
            suki "like i said before... who's joking?"
            show ctc
            pause
            hide ctc
        "dump it down her throat!":


            bk3c "where's my drink?"
            y "fuck... ing... ah... here!"
            show expression "bk3/suki/barblow/glass_hand.png" with hpunch
            bk3c "that wasn't so hard, right?"
            hide expression "bk3/suki/barblow/glass_hand.png"
            hide toxc
            show toxc toxc09
            show expression "bk3/suki/barblow/floor_torso.png":
                xpos 360 ypos 80

            show expression "bk3/suki/barblow/floor_headsuck.png":
                xpos 360 ypos 90

            show expression "bk3/suki/barblow/desk.png":
                xpos 0 ypos 0 alpha 0.8
            with Dissolve(1.5)

            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/floor_headsuck.png":
                linear 0.3 ypos 30
                linear 1.0 ypos 90
            show expression "bk3/suki/barblow/floor_torso.png":
                xpos 360 ypos 80
                linear 0.3 ypos 60
                linear 1.0 ypos 80

            show ctc
            pause  
            hide ctc
            suki "mmmm!!"
            bk3c "what do i owe you?"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/floor_headsuck.png":
                linear 0.3 ypos 30
                linear 1.0 ypos 90
            show expression "bk3/suki/barblow/floor_torso.png":
                xpos 360 ypos 80
                linear 0.3 ypos 60
                linear 1.0 ypos 80
            y "I think... hgnh... 25 coins should cover it."
            show ctc
            pause  
            hide ctc
            play sound "audio/gulp2.mp3"
            suki "*gulp!!* *gulp!!* *gulp!!*"
            hide expression "bk3/suki/barblow/floor_torso.png"
            hide expression "bk3/suki/barblow/floor_headsuck.png"
            hide expression "bk3/suki/barblow/desk.png"
            show expression "bk3/suki/barblow/glass_hand.png"
            show toxc toxc07a
            show expression "bk3/suki/barblow/hands_pinch.png":
                xpos 10
            with Dissolve(1.5)
            bk3c "that seems fair."
            "Suki grabs your ass with a vice-like grip and shoves you farther down her throat as you feel the third wave approching."
            show ctc
            pause
            hide ctc
            bk3c "hey! let go of my drink!"
            play sound "audio/gltch2b.mp3"
            show toxc toxc07a with vshake
            show ctc
            pause
            hide ctc
            suki "......"
            suki ".............."
            play sound "audio/gulp2.mp3"
            suki "{size=+10}*gulp!!!*" with hpunch

            hide toxc
            hide expression "bk3/suki/barblow/top.png"
            show toxc toxc02
            show expression "bk3/suki/barblow/top.png":
                alpha 0.8

            hide expression "bk3/suki/barblow/hands_pinch.png"

            show expression "bk3/suki/barblow/spermin_1.png"
            with Dissolve(1.5)
            suki "gah!"
            suki "....wow."
            suki "that... was a lot of semen."
            show ctc
            pause
            hide ctc
            suki "i don't... even know how i'm gonna get out of here..."
            hide expression "bk3/suki/barblow/glass_hand.png" with dissolve
            "you let go of the drink."

            bk3c "thanks man."
            bk3c "but i think you should get checked for epilepsy."

            show ctc
            pause
            hide ctc
            y "fuck... that... guy..."
            suki "that was a huge load..."
            y "you earned it."
            suki "i did, didn't i?"
            suki "Maybe I could use it to make a special girls only {i}cock{/i}tail."
            y "what did i say about your jokes?"
            show toxc toxc02_3
            suki "like i said before... who's joking?"
            show ctc
            pause
            hide ctc
    if suki_bar_blow ==6:
        suki "so... we have a deal?"
        y "yeah, we have a deal...."
    hide expression "bk3/suki/barblow/arm_bitefinger.png"
    if suki_bar_blow ==6:
        suki "great!"
    suki "come by whenever you need a little work release, and i'll keep my tips!"
    suki "it's a win-win."
    suki "i'm gonna try to sneak to the back..."
    suki "i didn't think there'd be this much cum..."
    y "ahhh... that was fun."
    show ctc
    pause
    hide ctc
    if suki_bar_blow ==7:
        $ bk3_day = False
        jump love_bk3_village_background
    else:
        scene black with dissolve
        "totally exhausted, you head home and crash."
        $ suki_bar_blow = 7
        jump love_bk3_next

label katara_toph_scissor:
    stop music
    play music "audio/Unwritten Return.mp3"
    scene black
    scene bed_inside
    show tote tote01
    with Dissolve(1.5)
    if earthbending ==25:
        t "hahahaha!!!"
        t "i can't believe he did that!"
        k3 "i know, sokka is such an idiot."
        t "no wonder he doesn't let that boomerang out of his sight!"
        t "oh, man..."
        t "you know guys..."
        t "i'm having a lot of fun."
        t "i didn't think i'd be this comfortable... all naked together..."
        t "but... it seems... easy, you know?"
        y "i told you it would be."
        t "yeah, i know..."
        k3 "oh! look at that!"
    k3 "i think aang's getting excited."
    t "he's {i}been{/i} excited."
    t "his heartrate's been going a zillion beats a minute."
    y "that seems... high."
    k3 "well..."

    show tote tote02 with dissolve
    k3 "why don't i take care of that for you?"
    show ctc
    pause
    hide ctc
    t "uhh..."
    k3 "come on!"
    k3 "toph's obviously not jumping to the challenge."
    k3 "plus i'm the oldest, so you should start with me."
    if earthbending ==25:
        t "st-start?!"
    t "if anyone's gonna take care of his penis, it's gonna be me!"

    show tote tote03 with dissolve
    t "come on, sexy!"
    t "i'll give you a {i}real{/i} tight experience."
    show ctc
    pause
    hide ctc
    k3 "hmmgh...."
    k3 "actually..."
    show tote tote02 with dissolve
    k3 "how about a little competition?"
    show ctc
    pause
    hide ctc
    t "compe... tition?"
    k3 "to see who has the best pussy!"
    t "i don't know..."
    k3 "here's the twist -- no penetration allowed!"
    t "what? how would that work?"
    k3 "aang, lay on the bed."
    show tote tote04 with Dissolve(1.5)
    k3 "perfect, now follow my lead, toph..."

    show tote tote11 with Dissolve(1.5)
    t "like this?"
    k3 "right."
    y "oh... damn..."
    "katara and toph's pussy lips press into your cock, slightly enveloping it."
    "their vaginas are so small that their lips don't even come close to touching."
    "but you can feel a hot wetness on each side that makes it impossible to tell."

    k3 "what do you think, aang?"
    y "i think... that this isn't just about me."
    y "you girls should enjoy yourselves, and each other, as much as with me."
    if earthbending ==25:
        t "oh... um..."

    y "in fact, I think you should kiss each other."
    if earthbending ==25:
        t "Ki-kissing a girl is...."
        t "....I never really considered it."
        y "Katara, if you'd see Toph in trouble would you help her out?"
        k3 "Of course!"
        t "are... you sure?"
        k3 "are you kidding?!"
        k3 "i'd love to!"
        k3 "you're my friend and I care for you."
        k3 "plus you're so sexy."
        k3 "i love that tiny little body."
        y "how about you, Toph?"
        y "you find katara sexy, right?"
        t "i... i do..."
        t "We might not agree on... well a lot of things... but I care about Katara."
        t "and... she is pretty. i think."
        t "...and soft."
        t "if i was going to kiss a girl... the only one would be katara."

        y "katara?"
        y "want to help her out?"

    show tote tote06 with Dissolve(1.5)
    "katara takes toph's hand and they pull toward each other, their pussies pressing harder into your shaft."
    k3 "mmmm...."
    t "ohhh..."
    "toph moans into katara's mouth."
    "they're clearly both enjoying it."
    "you stay silent for a minute while they each explore the feeling of the other girl's lips on theirs."
    show ctc
    pause
    hide ctc
    y "you know.... I said a little kiss, but..."
    y "...a long one is fine too."

    show tote tote07 with Dissolve(1.5)
    "tentatively, they flick their tongues out and wrap them around each other's."
    "the kiss increases in energy, the two girls beginning to really delve into the other's mouth."
    "they press their lips and tongues into one another as you watch them taste each other's saliva."
    y "Wow, you guys are taking to this a lot better than I expected."
    y "....don't forget about me."

    show tote tote11 with Dissolve(1.5)
    t "haha... aw, is someone feeling left out?"
    y "...a little."
    k3 "we haven't forgotten you, handsome."
    t "i kinda did."
    t "your lips are so soft, Katara!"
    k3 "yours too!"
    if earthbending ==25:
        k3 "We really should've done this earlier."
    t "i can't believe how sexy it is kissing you with this big dick between us..."
    t "i'm so horny!"
    k3 "i know... i'm soaking his balls..."
    t "i thought that was me?"
    t "can i put him in me?"
    k3 "that's not the game!"
    k3 "what do you think aang... are you ready to judge our pussies?"
    y "this is already my favorite sport."

    k3 "alright toph, move your pussy up and down, like this."
    show tote tote100
    show ctc
    pause
    hide ctc
    k3 "just like that!"
    k3 "mmmmm...."
    "The two girls slide their wet pussies over your shaft, which throbs with every pressing grind."
    show ctc
    pause
    hide ctc
    k3 "Having two pretty girls using their lips on each other..."
    k3 "and their other lips on your dick..."
    k3 "...must be pretty nice, Aang."
    y "Nice? "
    y "I don't think it can get any better than this."
    if earthbending ==25:
        y "You two girls are totally in sync, but you each have your own unique beauty..."
        y "it's like I'm looking at the perfect being split into two."

        t "\"The perfect being split in two...\""
        t "...you really know what to say, twinkletoes."
        y "Just stating the obvious."
        t "i think you're just trying to get out of judging the better pussy."
        t "it's okay, i know it's mine."
        k3 "nuh-uh!"
    show ctc
    pause
    hide ctc
    y "You two can get a bit rougher if you want."
    y "that'll help."
    k3 "oh? is that right?"

    show tote tote103
    k3 "like this?"
    show ctc
    pause
    hide ctc
    y "uhhhh..."
    t "i think he liked that."
    k3 "how about a little more?"
    show ctc
    pause
    hide ctc
    t "oh fuck... that feels good..."
    t "come on... yeah... ah... ah..."

    show tote tote101
    k3 "yes... ungh...."
    show ctc
    pause
    hide ctc
    y "oh shit..."
    k3 "you gonna cum, aang?"
    k3 "from my pussy?"
    t "no, he's gonna cum from mine!"
    t "isn't that right, aang?"
    t "isn't my pussy so wet and hot?"
    k3 "not more than mine!"
    y "Hnnng... i'm gonna..."

    hide tote
    show tote tote11
    with Dissolve(1)
    t "you gonna cum, twinkletoes?"
    t "cover these hot young bodies in sperm?"
    show tote tote13 with dissolve
    k3 "will you soak us, aang?"
    k3 "tits and tummies sticky with your cum?"
    y "don't stop!"
    k3 "you heard him!"
    show tote tote104 with Dissolve(1)
    show ctc
    pause
    hide ctc
    y "fuck!"
    y "Okay now i'm really gonna cum!"
    t "cum from my hot pussy!"
    k3 "no, mine!"
    play sound "audio/gltch2b.mp3" 
    show expression "bk3/katara/scissor/spermshot.png"
    $ renpy.pause(0.3)
    hide expression "bk3/katara/scissor/spermshot.png" with Dissolve(1.0)
    play sound "audio/gltch2b.mp3" 
    show expression "bk3/katara/scissor/spermshot.png"
    $ renpy.pause(0.3)
    show tote tote11
    show expression "bk3/katara/scissor/sperm1.png"
    with Dissolve (1.5)
    hide expression "bk3/katara/scissor/spermshot.png" with Dissolve(1.0)

    show ctc
    pause
    hide ctc


    y "aaaah...."
    k3 "so?"
    y "...what?"
    t "who's was better?"
    y "....yes."
    t "that's not-"
    y "yes."
    k3 "hahaha... oh, aang..."
    k3 "this was a lot of fun, toph."
    k3 "thank you."
    t "i think we're all welcome."
    k3 "i think aang's about to fall asleep."
    t "let's join him."
    k3 "mm-hmm."
    show ctc
    pause
    hide ctc
    scene black with Dissolve(1)
    "the three of you fall asleep together."



    if earthbending < 26:
        $ earthbending = 26

    jump love_bk3_next

label love_nagas_battle:
    y "let's do it."
    y "but... why now?"
    cn "{i}weak..."
    cn "{i}too weak to ssstay much longer..."
    cn "{i}your hallucinationsss fight me..."
    cn "{i}not ssstrong enough..."
    cn "{i}mussst defeat the dreamssstealer sssoon, or i will not win..."
    y "i'm fuzzy on the details of this \"merging\" situation."
    y "what will happen to you?"
    y "and what will happen to my mind?"
    cn "{i}i will be ssstrong enough to put up barriersss in your mind..."
    y "and i can trust you on that?"
    cn "{i}hissss..."
    cn "{i}yesss... i have been nothing but honessst with you..."
    cn "{i}i am from the dreamssstealer... but i am not the dreamssstealer..."
    cn "{i}i wasss born here... in your mind..."
    y "right, right, you've said that before."
    y "tell me about this merge you want to do."
    cn "{i}i.... am not clear...."
    y "wait, what? tell me you're joking."
    cn "{i}i do not know what will happen..."
    y "i don't like this plan."
    cn "{i}i have called her."
    y "you {i}what{/i}!?"
    y "i didn't give you permission for that!"
    cn "{i}here ssshe comesss..."
    cn "{i}ssstay ssstrong...."
    y "i don't like th-"
    play sound "audio/hiss.wav"
    show flyby at right
    with moveinright
    hide flyby with moveoutleft
    with sshake
    $ renpy.pause(1.0, hard=True)
    play sound "audio/hiss.wav"
    ds "*hss!*"
    ds "i have come, avatar!"
    with sshake
    ds "foolissh child!"
    ds "thosse eyess were curssed..."
    ds "and i have let me into your mind!"
    with sshake
    play sound "audio/hiss.wav"
    show flyby2 at left
    with moveinleft
    hide flyby2 with moveoutright
    $ renpy.pause(1.0, hard=True)
    ds "goodbye, little one... your work is finisshed..."
    cn "{i}no."
    ds "thiss is the en- what?"
    cn "{i}thisss isss my mind!"
    y "um... pretty sure it's mine-"
    with sshake
    ds "you sstay out of thiss!"
    ds "i am naga, the dreamsstealer!"
    ds "powerful and older than the ssky!"
    ds "you cannot sstop me, you imitation!"
    play sound "audio/hiss.wav"
    show flyby at right
    with moveinright
    hide flyby with moveoutleft
    with sshake
    $ renpy.pause(1.0, hard=True)
    y "ow...."
    cn "{i}i am no imitation...."
    cn "{i}and i am ssstronger than you, here..."
    ds "we sshall ssee!"
    with sshake

    show tonc_floats:
        around (.5, .5) alignaround (.5, .5) xalign .7 yalign .5
        rotate 0
        linear 10 rotate 360
        repeat
    with flash
    y "what..."
    y "why is that happening..."
    show flyby:
        parallel:
            rotate -90
            xpos -200
        parallel:
            ypos -1000
            linear 5 ypos 920
        repeat
    with flash
    y "why is any of this happening...?"
    y "ow... my head...!!"
    y "who... are you weirdos?"
    ds "sstop! you cannot win!"
    cn "{i}thisss man is mine!"
    cn "{i}hisss mind belongsss to me!"
    ds "no! you are a cheap imitation! i am real!"
    cn "{i}i am real!!"
    with flash
    ds "noo...!!"
    cn "{i}hssss!!"
    y "my fucking head..."
    hide tonc_floats
    hide toxe
    hide flyby
    with flash
    with flash
    with flash
    show ctc
    pause
    hide ctc
    y "......"
    y "where did they go?"
    show tonb tonb101 with Dissolve(1.5):
        parallel:
            xpos -1000
            linear 1.0 xpos 0
        parallel:
            ypos 0
            linear 1 ypos 15
            linear 1 ypos 0
            repeat

    show ctc
    pause
    hide ctc

    "{i}i am here, avatar...."
    "{i}and i am... not amusssed..."
    y "oh. that's... not good."
    "{i}but i will keep my bargain."
    y "uh, wait..."
    y "which one are you?"
    "{i}i am both."
    "{i}call me..."
    nag "{i}nagina."
    y "you want me to call you vagina?"
    nag "{i}no... nagina."
    y "fine."
    y "so what's the deal?"
    nag "{i}i will... put up barriersss... against my better judgement..."
    nag "{i}I will keep my word..."
    nag "{i}but i will take down the current barriersss before I can build permanent onesss..."
    nag "{i}this will not be pleasssant..."
    nag "{i}you may die..."
    y "wait... die!? straight up just die!?"
    nag "{i}the russsh of violent hallucinationsss may sssend you into the darknessss..."
    nag "{i}and never return."
    y "that's not good."
    nag "{i}here..."
    y "ohhhh shhiiiiiiiit-"
    with flash
    with flash
    $ double_vision_on("tonb tonb101_1")
    y "what... what... no..."
    nag "{i}ssstay! ssstay awake!"
    y "where the fuck am i?"
    y "i... can't..."
    nag "{i}no! you mussst-"
    scene black with Dissolve(1)
    $ double_vision_off()
    show ctc
    pause
    hide ctc
    "you drift...."
    "for a time."
    "the deeper darkness calls to you."
    jump kat_toph_bj

label kat_toph_bj:
    "You feel weightless, floating in a vast, cold nothingness."
    "It would be so easy to just let your sense of self sink into the black void, but something is tugging at you."
    show expression "ebackgrounds/bed_inside.jpg"
    show tote tote23
    show expression "bk3/katara/scissor/black.png":
        alpha 1.0
        linear 5.0 alpha 0.8

    t "I... I think I feel something..."
    t "A slightly increased pulse... it's slipping away again..."
    show expression "bk3/katara/scissor/black.png":
        alpha 0.8
        linear 2.0 alpha 1.0
    t "Should I take over?"
    show expression "bk3/katara/scissor/black.png":
        alpha 1.0
        linear 5.0 alpha 0.5
    show tote tote24
    k3 "Keep sucking that dick Toph... i think..."
    y "Whhaaa...ss... goin...on...?"
    "your voice sounds heavy and tired."
    show tote tote24a
    k3 "He's waking up!!"
    k3 "Aang!!"
    k3 "How are you feeling?!"
    show expression "bk3/katara/scissor/black.png":
        alpha 0.5
        linear 1.0 alpha 1.0
        linear 2.0 alpha 0.0
    y "...like shit..."
    y "As if someone replaced my brain with a cabbage..."
    hide expression "bk3/katara/scissor/black.png"
    show tote tote19 with Dissolve(1.5)
    t "so normal."
    y "screw... you..."
    t "He's fine!"
    t "I knew he'd come out of it."
    t "i wasn't worried for a single minute!"
    t "Aang's as tough as this fella is hard!"
    show tote tote21

    play sound "audio/kiss.mp3"
    show tobb_heart:
        xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
        xzoom 1 yzoom 1 alpha 1.0
        linear 1.0 xzoom 4 yzoom 4 alpha 0.0
    $ renpy.pause(1.3)
    hide tobb_heart
    show tote tote19 with Dissolve(1.5)
    k3 "I'll have some of that too!"
    show tote tote22

    play sound "audio/kiss.mp3"
    show tobb_heart:
        xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
        xzoom 1 yzoom 1 alpha 0.5
        linear 1.0 xzoom 4 yzoom 4 alpha 0.5
    $ renpy.pause(1.3)
    hide tobb_heart
    show tote tote19 with Dissolve(1.5)
    t "I feel like kissing some more..."
    k3 "Who's gonna stop us?"
    show tote tote20 with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show tobb_heart:
        xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
        xzoom 1 yzoom 1 alpha 1.0
        linear 1.0 xzoom 4 yzoom 4 alpha 0.0
    $ renpy.pause(1.3)
    hide tobb_heart
    show tote tote19 with Dissolve(1.5)
    y "I feel woozy."
    k3 "Don't get up just yet, you lost a lot of stamina."
    k3 "Maybe you should keep going Toph, Just to be sure."
    menu:
        "Yeah keep going":
            show tote tote24
        "That's not necessary":
            pass
    $ renpy.pause()
    y "Okay so, I like what I'm seeing, but I have no memory of starting all of this."
    y "What's going on?"
    k3 "I don't really know, I just found you on the floor, unconscious."
    k3 "It looks like a spirit almost sucked you dry of your lifeforce."
    show tote tote19 with dissolve
    t "I suggested to just give you a blowjob, to keep your blood flowing, and enticing your spirit to stay put!"
    k3 "That's right!"
    k3 "It was Toph's idea and she wasn't bawling her eyes out at all while you were lying there on the brink of death."
    t "Yeah, I... hey!!"
    show tote tote24 with dissolve
    t "*grumble...*"
    k3 "We've been taking turns, keeping you warm with our bodies and giving you continuous blowjobs."
    k3 "We figured your mind wouldn't leave before you got the chance to cum."
    y "Sooo... why didn't I cum?"
    k3 "My waterbending kept your sperm from escaping your balls. "
    k3 "It was easy!"
    y "That's not terrifying at all..."
    y "Thanks. "
    y "I owe you both big time."
    k3 "We'll continue for a few more minutes."
    k3 "Just to be certain."
    y "sounds good to me..."
    show tote tote19 with dissolve
    t "Can you take this one Katara?"
    t "I'd like to talk to Aang and that's kinda hard with a dick in my mouth."
    k3 "Of course!"
    show tote tote23 with Dissolve(1.5)
    $ renpy.pause()
    t "I... it was really devastating to see you lying there and not knowing what would happen."
    t "Not knowing whether you'd live or die..."
    y "Sorry, I didn't want to make you worry."
    t "I know... but it made me think and reconsider a lot of things..."
    t "You're not perfect, Aang."
    t "But neither am I, and I'm not willing to let whatever it is we have to be destroyed by something like jealousy."
    t "Me and Katara did a lot of talking."
    t "With one of us sucking your dick and the other listening, we've really come to understand each other better."
    t "I'm still not happy with your crazy sexdrive including anyone other than me."
    t "But... I'd rather share you than not have you at all."
    show tote tote27 with Dissolve(1.5)
    t "*Sniff...* I thought you were going to die and I'd never see you again..."
    y "Please don't cry Toph, if you cry I'll cry and things will get super awkward."
    y "I'm still alive!"
    y "and even if I did die I'd come back for you!"
    y "I'm the avatar, baby!"
    y "I reincarnate at the drop of a hat."
    y "and when I do, I'll come back and capture your heart all over again!"
    t "*Sniff...* but what if you'd reincarnate as a girl?"
    y "Well, I guess you'd have to learn how to munch carpet!"
    show tote tote23
    t "Hah..ahhahahah!! You dumbass!"
    t "You better shave or you can wait a long time for that to happen!"
    show tote tote19 with Dissolve(1.5)
    k3 "Ready for some unloading?"
    y "Fuck yeah!"
    y "I have two balls filled to the brim, and I'm going to dedicate one to each of my saviors."
    t "You go first, Katara."
    show tote tote25 with Dissolve(1.5)
    k3 "Aaaah!!"
    play sound "audio/gltch2b.mp3"
    $ renpy.pause(0.5)
    play sound "audio/gltch2b.mp3" 
    show expression "bk3/katara/scissor/bj_sperm_katside.png"
    k3 "oh!!"
    show tote tote26
    hide expression "bk3/katara/scissor/bj_sperm_katside.png"
    show expression "bk3/katara/scissor/bj_sperm_katside.png":
        xpos 75
    with Dissolve(1.5)
    t "My turn!"
    show expression "bk3/katara/scissor/bj_sperm_topside.png"
    play sound "audio/gltch2b.mp3" 
    $ renpy.pause(0.5)
    play sound "audio/gltch2b.mp3" 
    t "ahhhh....!!!"
    hide expression "bk3/katara/scissor/bj_sperm_katside.png"
    hide expression "bk3/katara/scissor/bj_sperm_topside.png"
    show tote tote19
    show expression "bk3/katara/scissor/bj_sperm_katfront.png"
    show expression "bk3/katara/scissor/bj_sperm_topfront.png"
    with Dissolve(1.5)
    k3 "how do we look?"
    t "sticky?"
    t "my face feels very... warm."
    t "and... soaking wet."
    k3 "isn't it nice?"
    t "i love the smell..."
    y "I'm taking a mental snapshot of this moment and will consider it as my most precious memory."
    k3 "Well, we've bothered you long enough. "
    k3 "you don't want to push yourself too hard."
    t "you did a good job cumming on our faces, twinkletoes."
    k3 "you did! now get some well deserved rest!"
    y "I will..."
    scene black with dissolve
    "you fall back asleep..."
    "...and dream deeply."
    jump love_bk3_next

label smellerbee_fuck:
    $ temp_boolean = False
    show tosb tosb51
    sb "aang, quick!! Follow me into this alley!"
    hide tosb with dissolve
    "smellerbee races around the corner before you can process what happened."
    "a little delayed, you follow in behind her."
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg"
    show toxg toxg10:
        ypos -300
        linear 6.0 ypos 0
    with Dissolve(1.5)
    y "uuhh... your pants are missing..."
    sb "i met jet! he told me you saved him!!!"
    y "I can't see them anywhere."
    y "Did you throw them in a garbage bin?"
    sb "I was so happy Jet is okay... "
    y "Do you need money for a new pair?"
    sb "I just can't help myself."
    y "Maybe some tight fitting jeans with rips in it?"
    sb "I thought I would never see him again..."
    y "oh, yeah, about Jet...."
    menu:
        "He was also very... happy. Very.":
            sb "Did he try to give you a blowjob?"
            y "uhh... would that bother you?"
            sb "Well, yeah a bit but that's just how he is."
            sb "He usually pretends to like girls, but..."
            sb "Let's just say there's a reason why I dress like a boy and keep it at that."
            sb "But I have needs too, so how about...."
        "He offered to suck me off":
            sb "Yeah he... does that."
            sb "But that just means I can do something like that for you too!"
            sb "But I already gave you a blowjob so how about...."


    show toxg toxg09 with Dissolve(1.5)
    sb "...I take this off, you bend me over and take me like a little bitch in heat?"
    show ctc
    pause
    hide ctc
    hide toxg
    show expression im.Flip("bk3/smellerbee/bj/bg_alley_fountain.jpg",horizontal=True)
    show expression "bk3/smellerbee/fuck/shadow.png"
    with Dissolve(1.5)

    show toxg toxg00b with Dissolve(1.5)

    sb "Come on! I want a dick in my little pussy for once!"
    show ctc
    pause
    hide ctc
    show toxg toxg00
    y "...I can do that."
    show ctc
    pause
    hide ctc
    show toxg toxg00a
    sb "Ah!!"
    sb "Oh, sorry. I'm reasonably new to anything not going up my ass."
    show toxg toxg01
    y "We can take our time."
    show toxg toxg04 with Dissolve(1.5)
    sb "Mmmmmmmhhh!!"
    show ctc
    pause
    hide ctc
    show toxg toxg01 with Dissolve(1.5)
    sb "Give it to me Aang!"
    sb "I'm ready!"

    hide toxg
    show toxg toxg100:
        xpos 20 ypos 0
    sb "That's it!"
    show ctc
    $ renpy.pause()
    hide ctc
    sb "Aaah... you're stretching my pussy in every direction under the sun!"
    sb "I LOVE IT!"
    y "Hngh... glad to be of service."
    sb "My pussy has needed servicing for a loooong time now."
    show ctc
    pause
    hide ctc
    y "Just... just asking, but would you mind if I cum inside you?"
    sb "That's no problem."
    sb "Make a nice creampie or cum all over me."
    sb "It's all fine."
    show ctc
    pause
    hide ctc
    sb "Can... Can you slam it?"
    sb "Like really hard?"
    sb "my cunt is so new it's practically under warranty."
    sb "so treat me like it!"
    sb "slam me hard!"
    sb "Don't let my small stature fool you! I can take it. I need it!"
    y "Honestly, I was going to do that anyway."
    y "Starting...."
    hide toxg
    show toxg toxg101
    y "now!!!" with flash
    sb "{size=+6}HGHHGHNNNGNG!!"
    show ctc
    pause
    hide ctc
    sb "{size=+6}YESSS!!"
    sb "{size=+6}FUCK IT! fUCK IT HARD!!!"

    menu:
        "cum inside":
            $ temp_boolean = True
            show toxg toxg07
            play sound "audio/gltch2b.mp3"
            show toxg toxg07 with hpunch
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show toxg toxg07 with hpunch
            $ renpy.pause()
            hide toxg
            show toxg toxg08
            show toxg_spermdrip
            with Dissolve(1.5)
            $ renpy.pause()
            sb "That... was a BIG load you fired off in me!"
            sb "...fuck, i'm sticky!"
            y "um..."
            sb "it's great!"
            show ctc
            pause
            hide ctc
        "cum outside":

            hide toxg
            show toxg toxg08
            with dissolve
            y "Cumming... now!"
            play sound "audio/gltch2b.mp3"
            show toxg_spermshot
            show expression "bk3/smellerbee/fuck/spermout1.png"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show toxg_spermshot
            show expression "bk3/smellerbee/fuck/spermout2.png"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show toxg_spermshot
            show expression "bk3/smellerbee/fuck/spermout3.png"
            $ renpy.pause()
            sb "...fuck, i'm sticky!"
            y "um..."
            sb "it's great!"
            show ctc
            pause
            hide ctc

    scene black
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg" with Dissolve(1.5)
    if temp_boolean == True:
        show toxg toxg11:
            ypos -100
            linear 6.0 ypos 0
        with Dissolve(1.5)

        sb "I think I gained a pound or two from that!"
    else:
        show toxg toxg12 with Dissolve(1.5)
        sb "Good thing I took all of my clothes off this time!"
    sb "See you later, Aang."
    y "count on it."
    $ bk3_day = False
    jump love_bk3_village_background

label bk3_love_final:
    hide screen earth_money_date
    scene black
    with dissolve
    scene bg_alley_epalace
    show toi toi06
    with dissolve
    y "well, here we are."
    y "the back way in."
    t "i'm done waiting."
    t "let's go."
    hide toi toi06 with dissolve



    show tosi tosi01:
        xpos 200
        linear 1.0 xpos 0

    suki "Hey Aang. I've been looking for you."
    y "Hey Suki. Well here I am. What's up?"
    suki "There's something I need to tell you about those birth-control pills I've been handing out."

    menu:
        "Fear grips your heart":
            y "Oh no... you're not going to tell me you switched them with high blood pressure ones by acccident, are you?!"
            y "I'm... I'm not ready to be a dad.."
            suki "relax, they work fine. I just wanna say I have a fresh batch."
            $ katara_cum_inside = False
            $ toxh_preg = False
            $ totk_preg = False
            $ toxk_preg = False
            $ totf_preg = False
            y "Good... good. Man I thought I was getting a heart attack."
        "you're curious but not worried.":
            y "Yeah, what about them?"
            suki "I've accidentally swapped them with high blood-pressure ones."
            y "You...you mean..."
            suki "I mean there's a chance you've knocked up whomever was counting on those to work."
            suki "Well, if you came inside them of course."
            y "....I think I need one of those high blood pressure pills right now."
            suki "really?"
            y "actually, that's... kinda exciting."




    suki "Gotta go!"
    show tosi tosi01:
        xpos 0
        linear 1.5 xpos -1000



    scene black with dissolve
    "nodding in agreement, you and toph slip your way into the throneroom."
    "the dai lee watch you carefully, and maybe even a little fearfully."
    show king_sitting
    show toi toi04
    with Dissolve(1)
    ek "hello!"
    ek "who are you?"
    y "we're your friends, your earthiness."
    ek "are you sure? you did sort of... burst in."
    y "i'm the avatar."
    y "and this is... toph."
    t "hello, your highness."
    ek "hello, small person."
    show toi toi06 with dissolve
    t "....."
    t "aang... can we get to it?"
    y "your earthiness, there is a matter of grave-"
    ek "wait, did you say you're the avatar?"
    y "i did."
    show king_angry with dissolve
    ek "then you are an enemy of the state!"
    show toi toi09 with dissolve
    y "i mean... i'm definitely not a benefit to the state..."
    y "but i'm not an enemy."
    show king_blink with dissolve
    ek "yes, you are!"
    ek "long feng has made that clear!"
    y "long feng was a traitor, my dude."
    hide king_blink
    hide king_angry
    with dissolve
    ek "oh."
    ek "well, then that's fine."
    y "...."
    ek "um... do you know what happened to him?"
    y "i believe he is imprisoned in the very labyrinth he designed."
    ek "that seems poetic."
    ek "so what can i do for you?"
    y "well, the earth kingdom has secretly been at war for one hundred years."
    ek "really now."
    ek "neat."
    ek "what does that have to do with me?"
    y "...well, we figured out how to stop them."
    y "the day of black sun..."
    scene black with dissolve
    "you spend some time discussing with the earth king the vague details you remember about plans to stop the fire nation."
    show king_sitting
    show toi toi09
    with dissolve
    ek "well, this {i}is{/i} serious!"
    ek "i'll see to it right away!"
    y "thank you, your majestic-ness."
    ek "no, thank you."
    ek "for opening my eyes."
    ek "and exposing the traitor long feng."
    ek "for this...."
    ek "i shall grant you one boon."
    y "a boob?"
    ek "a {i}boon{/i}."
    ek "...though it could be a boob if you'd like."
    ek "i like boobs."
    ek "but i like pretty much everything."
    y "hmmmm...."
    ek "may i make a suggestion?"
    y "sure."
    ek "this beautiful young lady here seems to be infatuated with you."
    y "the feeling is mutual."
    ek "perhaps this would be a good time to... solidify that."
    y "that... is a great idea."
    show toi toi09 with dissolve
    t "what...?"
    ek "then what boon would you have me grant?"
    menu:
        "a wedding":
            $ dressfuck_place = 'palace'
            y "I would ask your highness to grant us..."
            y "...a wedding."
            show toi toi10
            t "a {size=+10}what?!" with hpunch
            y "i love this girl, with all my heart."
            y "i wish to have her by mine, always."
            y "and i wish to be hers."
            t "I... i..."
            ek "very well, if this young lady agrees."
            t "i... you... i... agree..."
            ek "then we must have a ceremony!"
            t "i can't... you... but i..."
            ek "but of course the lady must prepare!"
            ek "and we must have an audience!"
            ek "what is a wedding without a crowd?"
            ek "i'll bring out every single person in this palace!"
            ek "and i'll have my staff assemble all your friends."
            y "thank you, your grace."
            t "bu... bu... bu..."
            ek "avatar, perhaps you could stay and discuss the war in more detail while this \"toph\" goes home to get ready."
            y "it would be a privilege."
            ek "you are correct."
            y "(man, i don't actually know any details...)"
            y "(i really should have paid more attention in history class.)"
            t "i... i need katara."
            hide toi with moveoutleft
            t "katara!!"
            ek "cute. she's a good catch."
            y "thanks, buddy."
            ek "oh, i like that!"
            ek "{size=+6}did you guys hear that?!"
            ek "{size=+6}he called me his buddy!"
            ek "we are buddies now."
            ek "this is decided."
            hide black
            show black
            with dissolve
            "you stay and discuss what you can remember about the day of black sun with the earth king."
            "...but really you end up talking about fuzzy animals and big hats."
            hide black with dissolve
            ek "that was certainly enlightening."
            y "yes, your highness."
            ek "well, we've assembled all of your friends, and pretty much everyone of class in ba sing se."
            ek "so this should be quite the ceremony!"
            show toeg toeg01 with moveinright
            dl "*whisper* "
            ek "mm-hmm... i see..."
            hide toeg with moveoutright
            ek "it has come to my attention that your lady and her friend are here."
            ek "a \"katara\"."
            ek "you may come forward, girl."
            show toki toki01:
                xzoom -1
            with moveinleft
            k3 "thank you, your grace."
            k3 "she is ready if you are."
            if totf_preg:
                k3 "and... i've helped her prepare a surprise for you."
                y "for me?"
            ek "excellent!"
            ek "let's do this thing properly then!"
            ek "stand back, buddy!"
            scene black with dissolve
            show toxk_background toxk_palace:
                xpos 0 ypos 0
            show toki toki01:
                xzoom -1
            with dissolve
            ek "let us begin."
            "a hush falls over the audience."
            k3 "{size=+6}ladies and gentlemen!"
            k3 "i present...."
            show toki toki03
            show toki_smile:
                xzoom -1
            with dissolve
            k3 "miss toph beifong!"
            hide toki
            hide toki_smile
            with moveoutleft
        "a house":

            $ dressfuck_place = 'home'
            y "I would ask your highness to grant us..."
            y "...a house."
            show toi toi10
            t "a {size=+10}what?!" with hpunch
            y "i love this girl, with all my heart."
            y "i wish to grow beside her."
            y "and a little home in the city would be perfect for that."
            t "I... i..."
            ek "very well, if this young lady agrees."
            t "i... you... i..."
            t "yes! of course!"
            ek "very well!"
            ek "you may have the house that was given to you when you first arrived."
            ek "it is yours."
            ek "i wish you much happiness."
            y "thank you, your highness."
            t "that... that house is... is..."
            y "ours."
            y "come."
            t "bu..."
            scene black with dissolve
            "you lightly take toph's stunned hand and direct her through the city and to the house."
            scene basingse_home_1
            show toi toi04
            with dissolve
            y "there it is."
            show toi toi10
            t "that's... ours?"
            t "I can't believe it..."
            y "come on, let's go inside."
            y "i'm feeling... a need."
            show toi toi08
            t "oh?"
            t "it wouldn't be a need to be... inside me, would it?"
            y "it might be."
            show toi toi07
            t "oh, i hope so."
            y "come on!"
            scene black with dissolve
            "you grab her hand and she giggles as you pull her eagerly inside."
            scene basingse_home_2
            show toi toi07
            with dissolve
            t "it's the same as it's always been, but..."
            t "it feels so... different."
            y "...ours."
            show toi toi09 with dissolve
            t "hmm?"
            y "it feels like ours."
            show toi toi04 with dissolve
            t "well said, my love."
            t "I... i can't keep it in anymore!"
            t "i have to tell katara!"
            t "i'll be back in a bit!"
            t "she's gonna be so excited!"
            hide toi with moveoutleft
            y "hahaha... damn she's cute."
            scene black with dissolve
            "you sit for a while, taking in the room."
            "you feel peaceful... and grateful."
            k3 "knock knock!"
            scene black with dissolve
            show toxk_background toxk_home:
                xpos 0 ypos 0
            with dissolve
            show toki toki01:
                xzoom -1
            with moveinleft
            k3 "i hope i'm not interrupting."
            y "no, i'm just having some happy thoughts."
            k3 "well, they're about to get better."
            y "oh? how?"
            k3 "well a certain cute chick came up to me all excited, and asked me to do something for her..."
            k3 "and i think you'll enjoy it."
            k3 "so, without further ado..."
            k3 "i present...."
            show toki toki03
            show toki_smile:
                xzoom -1
            with dissolve
            k3 "miss toph beifong!"
            hide toki
            hide toki_smile
            with moveoutleft

    $ toxk_dress = True
    $ toxk_sex = 'pussy'

    if totf_preg:
        $ toxk_preg = True
    else:
        $ toxk_preg = False


    show toxk toxk10:
        xpos 0 ypos 0
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc

    if dressfuck_place == 'palace':
        "the crowd cheers and toph blushes!"

    if dressfuck_place == 'home':
        "you let out a long, low whistle."
        "she blushes!"

    t "stop..."
    if toxk_preg:
        y "wait..."
        y "i... what..."
        y "your tummy..."
        y "how..."
        t "we had sex."
        t "a lot of it."
        y "no, i mean... you... already..."
        t "how am i already showing?"
        y "yes!"
        y "i just saw you!"
        t "katara."
        t "she gave me a pregnancy speed-up potion."
        t "she thought... she thought you'd like it."
        show toxk toxk12
        t "do you not like it?"
        t "I can't... undo it..."
        t "It's your seed growing inside me."
        t "i'm growing your sperm into a baby... that i'll birth for you."
        t "because... i love you."
        t "is that... okay?"
        y "...of course that's okay!"
        y "that's wonderful!"
        show toxk toxk10
        t "i'm so happy you said that!"
    else:

        y "you deserve that and then some, with how good you look."
        t "oh, aang...."

    y "Hey... you seem taller."

    show toxk toxk12
    t "That... that's probably because of the way I had my hair done."
    t "Katara did it for me."
    y "You look..."
    t "...yes?"

    show toxk toxk10:
        linear 3.0 ypos -260

    if dressfuck_place == 'palace':
        show toxk_background toxk_palace:
            linear 3.0 ypos -230
    else:

        show toxk_background toxk_home:
            linear 3.0 ypos -230
    y "...You look stunning."
    t "...thanks."
    y "Do you have some special underwear to go with it?"
    t "I figured..."
    stop music
    play music "audio/Unwritten Return.mp3"
    show toxk toxk11 with Dissolve(1.5)
    "Toph slowly raises her dress... totally giving away her elevated footwear but doesn't realize it."
    t "well... i figured you'd like it better this way."
    y "You know me so well!"
    y "did you... struggle into your first pair of high heels for me?"
    t "i... wanted to be tall..."
    y "you're so damn cute."
    t "hehehe... so whatcha wanna do now?"
    if dressfuck_place == 'palace':
        ek "a-hem!"
        show toxk toxk10:
            linear 3.0 ypos 0
        show toxk_background toxk_palace:
            linear 3.0 ypos 0
        ek "i believe vows are in order."
        ek "do you promise to forever love each other?"
        ek "through all the fetishes and loud chewing?"
        y "that's... oddly specific, but yes. i do."
        t "i do, too."
        ek "then, using my power as king, i now declare you married!"
        ek "you may consummate!"
        y "yeah, let's-"
        y "wait, what?"
        ek "you must consummate."
        y "here?"
        ek "of course!"
        ek "it is part of the ceremony."
        t "didn't you know that, aang?"
        y "I... guess i didn't."
        t "why did you think i was so shocked?"
        t "but i accept, and i want everyone to see you fill me!"
        t "to prove to everyone that i am your wife!"
        show toxk toxk11 with Dissolve(1.5)
        t "look at me..."
        show toxk toxk11:
            linear 3.0 ypos -260

        show toxk_background toxk_palace:
            linear 3.0 ypos -230
        t "take me."
    else:

        t "I want you to take me."
        t "i want you to fill me."








    y "*gulp....*"



    hide toxk

    if dressfuck_place == 'palace':
        show expression "ebackgrounds/palace_crowd.jpg"
    else:
        show expression "ebackgrounds/basingse_home_zoom.jpg"

    show toxk toxk06
    with fade
    if dressfuck_place == 'palace':
        "toph lays on her back in the center of the throne room."
    if dressfuck_place == 'home':
        "toph lays on her back on the floor."
    y "Sounds like a plan to me."
    if dressfuck_place == 'palace':
        y "...but there are a lot of people here."
        t "i don't see anyone else."
        y "yeah, but you can't see anything."
        t "hahaha!"
        t "well..."

    if dressfuck_place == 'home':
        t "i... i love how intimate this is."
    t "i see you."
    t "I've never seen anyone how i see you."
    if dressfuck_place == 'home':
        y "you've never seen anyone period."
        t "haha..."
        t "well..."
        t "i see {i}you{/i}."
    t "before this goes further... thank you."
    t "for what you are to me."
    y "thank you, toph."
    t "now..."
    if dressfuck_place == 'palace':

        t "don't forget why you're doing this."
        t "you're marking me, in front of everyone."
        t "you're claiming me as owned, by you."
        t "you must prove that i am taken, filled, and permanently marked as yours."
    if dressfuck_place == 'home':
        t "stop fucking around..."
        t "and start fucking into. me."
    y "...i can do that."
    y "Why don't we get that dress out of our way."
    show expression "bk3/toph/dressfuck/head_0_cynic.png"
    t "But sir... I'm a high class lady!"
    t "the only child of the wealthy Beifong family!"
    t "I couldn't do something so indecent as exposing myself and show my... my... "
    t "it's too crude to say!"
    y "...what?"
    y "you already did... just a moment ago."
    hide expression "bk3/toph/dressfuck/head_0_cynic.png"
    show expression "bk3/toph/dressfuck/head_0_angry.png"
    t "Just play along, Aang!"
    t "It's called roleplay."
    y "But you {i}are{/i} a high class lady and the only child of the wealthy Beifong family..."
    t "You want to do this or not?"
    y "Ahum! Don't worry about that, my precious little gem."
    y " Your family must accept me!"
    y "your family will watch as i penetrate you and take you as my love, and my fuckmate for life!"
    y "and if society denies our love then let it burn!!"
    hide expression "bk3/toph/dressfuck/head_0_angry.png"
    t "That's the spirit!"
    y "What?! Where!?"
    t "It's just an expression. Keep doing what you're doing!"
    y "Ah, right of course."
    y "My love for you burns more passionately than the fire of a blacksmith."
    y "I must have you! Allow me to sheath my sword into your forge of love!"

    hide toxk_background

    $ toxk_dress = True



    show toxk toxk00
    t "Is this more to your liking, noble sir?"

    menu:
        "YES! This will do nicely":
            pass
        "No, take it off entirely.":

            $ toxk_dress = False




    show toxk toxk07 with Dissolve(1.5)
    y "It certainly is!"

    show toxk toxk08 with Dissolve(2.0)

    y "Now before I ravish you, let me kiss those lips of yours."

    play sound "audio/kiss.mp3"
    show toxk toxk08 with pflash
    show toxk toxk07 with Dissolve(1.5)
    y "As sweet as strawberries."


    show toxk toxk01 with Dissolve(2.0)
    y "And now... I shall tend to your other lips..."



    show toxk toxk100
    $ renpy.pause()
    y "Hnn, you're as tight as ever, Toph!"
    y "Just pushing it in makes me afraid I'll break you."
    t "Pffff, as if you could!"
    t "I can clamp down so hard on you, it'd break off."
    y "uh, that's not really helping me in the \"staying hard\" department Toph.. "
    t "Oh... I mean... I'm a frail girl!"
    t "Please don't crush my pussy with your monster cock!"
    if dressfuck_place == 'palace':
        ek "i must say, i'm very much enjoying the drama here."
        ek "are there snacks?"
        ek "for those of us who are a little peckish?"
    y "...."
    y "so! You're challenging me me to crush your pussy!"
    t "I don't think you can, go ahead and try!"
    y "Does that go for your ass too?"

    if dressfuck_place == 'home':
        t "we're going to live together."
        t "so, whenever you need to rut, you can have it."
    else:
        t "well, it belongs to you now doesn't it?"
        t "whenever you need to rut, you can have it."

    t "or my pussy, if you'd prefer."
    t "i want you... however you want to have me."
    if dressfuck_place == 'palace':
        t "i'll finally be a proper married woman!"
        t "happily being fucked... without a say..."
        t "don't you know anything about marriage?"
    menu:
        "pick anal":
            $ toxk_sex = 'anal'
        "keep pounding pussy":
            $ toxk_sex = 'pussy'
    $ renpy.pause()
    y "I'm going to slam my cock into you so hard you'll be seeing stars!"
    t "Promises, promises."
    y "....better prepare yourself!"
    y "Riiiight now...."
    show toxk toxk101
    $ renpy.pause()
    t "Hnnff!! Is... is that all you got!"

    menu:
        "inside":
            hide toxk

            show expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)

            show toxk toxk15
            with Dissolve(1.5)
            play sound "audio/gltch2b.mp3" 
            show toxk toxk15 with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3" 
            show toxk toxk15 with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"   
            show toxk toxk15 with flash
            $ renpy.pause()
            show toxk toxk16



            if toxk_sex == 'anal':
                show expression "bk3/toph/dressfuck/spermdrip_top_ass.png"
                with Dissolve(1.5)
            else:
                show expression "bk3/toph/dressfuck/top_spermdrip.png"
                with Dissolve(1.5)

            if toxk_sex == 'pussy':
                t "Did you just give me a creampie?"
                y "Sure did!"
            else:

                t "Filling my ass with your cream... you're a real pervert!"
                t "I love it!"


            y "Now gimme some sugar as a reward."

            if toxk_sex == 'anal':
                hide expression "bk3/toph/dressfuck/spermdrip_top_ass.png"
            else:
                hide expression "bk3/toph/dressfuck/top_spermdrip.png"




            show expression "bk3/toph/dressfuck/side_creampie.png"
        "outside":

            hide toxk


            show expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)



            show toxk toxk15
            with Dissolve(1.5)
            $ renpy.pause()
            y "Show me that pretty face of yours Toph!!"
            show toxk toxk16 with Dissolve(1.5)
            play sound "audio/gltch2b.mp3" 
            show expression "bk3/toph/dressfuck/spermout1.png" with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3" 
            show expression "bk3/toph/dressfuck/spermout2.png" with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3" 
            show expression "bk3/toph/dressfuck/spermout3.png" with flash
            t "mmmm.... warm...."
            $ renpy.pause()
            y "Fuck yeah."
            y "Now gimme some sugar."
            hide expression "bk3/toph/dressfuck/spermout1.png"
            hide expression "bk3/toph/dressfuck/spermout2.png"
            hide expression "bk3/toph/dressfuck/spermout3.png"
            show expression "bk3/toph/dressfuck/spermout4.png"


    hide expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)


    show toxk toxk13
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show toxk toxk13 with pflash
    $ renpy.pause()
    show toxk toxk00 with Dissolve(1.5)
    y "I... really love you Toph."
    t "I love you too."
    if dressfuck_place == 'home':
        scene black with Dissolve(1)
        "you fall asleep in each other's arms."
    else:
        ek "good show!"
        k3 "well done!"
        y "i think they're applauding you."
        t "well {i}i{/i} think they're applauding {i}you{/i}."
        t "you... you rock my whole stupid world."
        ek "alright, can we clean this up now?"
        ek "bring out the royal jizz cleaner!"
        y "...that is a terrible job."
        scene black with Dissolve(1)
        "you put toph up on her feet and together the two of you walk back to the village; completely, happily content."
        "you sleep together in a loving, fulfilling embrace."

    jump love_bk3_next

label katara_pregfuck:
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/inside_hospital.jpg"
    $ temp_boolean = False
    if katara_cum_inside or totk_preg:
        $ toxh_preg = True
    else:
        $ toxh_preg = False



    show toxh toxh09
    k3 "Hey sexy!"
    if toxh_preg == True:
        y "Uuuuh... is that belly signifying what I think it does?"
        k3 "Surprised? With the amount of sperm you release?"
        k3 "It saturates the room so much that simply smelling it could get a girl pregnant!"
        y "Yeah, but usually this kinda thing takes time.."
        k3 "Ba sing Se is a big city with ingredients from all over the world."
        k3 "I figured it was best to move things along faster with the help of some special potions."
        y "But you know I can't stay...."
        k3 "Another reason why I wanted to speed things up."
        k3 "And you will come back for me..."
        k3 "Right?"
        y "It's not like I can buy a ticket and ride the time train whenever I want, but...."
        y "I'll do whatever I can."

    k3 "...do you have to go soon?"
    y "i'm not sure."
    y "i'm starting to get that feeling, though."
    k3 "did you have a good night with toph?"
    y "i had an amazing night."
    y "thanks for your help with that."
    k3 "you're so welcome!"
    k3 "i'm glad you came to visit me... even though you're starting to feel pressed for time."
    y "I love you and I love Toph, but it all started with you."
    k3 "We're sperm sisters! "
    y "Sperm sisters?"
    k3 "it's like eskimo brothers."
    y "so... you wanted to see me?"
    show toxh toxh10 with Dissolve(1.5)
    k3 "I was hoping for a little... something."
    y "have i told you you're pretty, lately?"
    k3 "it's always nice to hear."
    k3 "Have you ever played \"doctor\"?"
    k3 "because...."
    hide toxh with Dissolve(1.5)

    $ toxh_upperbody = 'up_default'
    hide expression "ebackgrounds/inside_hospital.jpg"
    show expression "ebackgrounds/inside_hospital_2.jpg"
    show expression "bk3/katara/pregfuck/braid_solo.png":
        xpos 0 ypos 0
    hide toxh
    show toxh toxh06
    with Dissolve(1.5)
    k3 "I feel like I need a thorough examination."
    show toxh toxh07
    k3 "Down there..."
    y "I can already see you are very, very hot. Feverish even."
    if toxh_preg == True:
        y "But... uuuuh... you sure that's safe with the baby and all?"
        k3 "Don't worry, it's perfectly safe."
        k3 "So safe we could even do this standing up!"
        y "For real?"
        k3 "For real."

        menu:
            "Nah, just stay like you are.":
                y "I kinda like this position better anyway."
                pass
            "Okay let's do it!":
                y "I mean if you're really certain it's safe."
                k3 "I am"
                jump bk3_katara_pregrub

    y "Let's take a closer look."
    show toxh toxh11 with Dissolve(1.5)
    y "Hmmm... everything looks perfectly fine so far..."
    show expression "bk3/katara/pregfuck/point.png" with Dissolve(1.5)
    k3 "You should especially inspect this part."


    menu:
        "spread pussy":
            hide expression "bk3/katara/pregfuck/point.png"
            show toxh toxh12
            with Dissolve(1.5)
        "kiss pussy":
            hide expression "bk3/katara/pregfuck/point.png" with dissolve

            play sound "audio/kiss.mp3"            
            "you tenderly put your lips on Katara's clit and softly kiss it." with pinkflash
    y "This seems like the perfect place to take your temperature."
    y "But let's lick it first."
    show toxh_tongue:
        xpos 630 ypos 400
        easein 1.2 ypos 370
        repeat
    $ renpy.pause (1.0)
    show expression "bk3/katara/pregfuck/spit.png":
        xpos 615 ypos 300 alpha 0.6
        linear 0.6 ypos 150 xpos 600 alpha 0.0
        linear 0.6 ypos 150 xpos 600 alpha 0.0
        repeat
    show expression "bk3/katara/pregfuck/front_blink.png":
        ypos 0
    k3 "Hmmmm... I like how thorough you are."

    hide toxh_tongue
    hide expression "bk3/katara/pregfuck/spit.png"
    y "That should do it."
    show toxh toxh11 with Dissolve(1.5)
    y " Time to take your temperature."
    hide expression "bk3/katara/pregfuck/front_blink.png"

    show toxh toxh00 with Dissolve(1.5)
    k3 "What an impressive thermometer!"
    y "I've already warmed it up for you."
    k3 "I'm not sure it'll fit, doctor!"

    show toxh toxh01
    y "Well, it might sting a little at first, but I'm certain it'll turn out all right."
    k3 "Then please dive right in."



    show toxh toxh100
    $ toxh_upperbody = 'up_blink'
    k3 "OH!" with hpunch

    $ toxh_upperbody = 'up_lewd'
    k3 "That's reaaally nice..."
    k3 "But shouldn't it be left inside for several minutes?"
    y "Its... ahhh... a special one."
    y "It works best when inserted repeatedly."
    y "It's my special thermometer for a very special patient."

    $ toxh_upperbody = 'up_blink'
    k3 "FUUUuuuuuckkk!! "

    $ toxh_upperbody = 'down'
    k3 "I'm goin to lie down for a moment."
    k3 "It's like your dick is handmade for my pussy."
    k3 "I can't understand how I managed to go without it for so long."


    $ toxh_upperbody = 'up_lewd'
    k3 "But you can't be satisfied with this slow pace."
    k3 "Don't hold back! Treat it as if it's the last pussy you'll ever have!"
    y "Don't say scary things like that!!"
    k3 "AAwwh, don't be scared."
    k3 "My little honeypot will always be there for you."
    show toxh toxh01
    y "In that case... make sure you hold your head or you'll end up with whiplash."
    k3 "That seems unlikely."
    y "Dont underestimate me, woman!!!"
    $ toxh_upperbody = 'up_blink'
    k3 "Do it! DO IT NOW!!"
    show toxh toxh101
    k3 "AH!!! THAT'S IT!"
    $ renpy.pause()
    "You keep slamming in your dick while Katara is making all sorts of appreciative sounds"
    y "HHHNNGG... Can't keep this up much longer!"
    y "Vitamin... shot... coming... your way now!"
    menu:
        "cum inside":
            $ temp_boolean = False
            hide toxh
            show toxh toxh05
            play sound "audio/gltch2b.mp3"            
            $ renpy.pause(1.0)
            play sound "audio/gltch2b.mp3"            
            $ renpy.pause(1.0)
            play sound "audio/gltch2b.mp3"            
            $ renpy.pause(1.0)
            show toxh toxh00
            show expression "bk3/katara/pregfuck/spermin1.png"
            with Dissolve(1.5)
            k3 "mmmm..."
        "cum outside":

            $ temp_boolean = True
            hide toxh
            show toxh toxh00
            play sound "audio/gltch2b.mp3" 
            show toxh_spermshot
            show expression "bk3/katara/pregfuck/spermout1.png"
            $ renpy.pause()

            play sound "audio/gltch2b.mp3"
            show toxh_spermshot
            show expression "bk3/katara/pregfuck/spermout2.png"
            $ renpy.pause()

            play sound "audio/gltch2b.mp3"
            show toxh_spermshot
            show expression "bk3/katara/pregfuck/spermout3.png"
            $ toxh_upperbody = 'up_lewd'
            $ renpy.pause()

    scene black
    show expression "ebackgrounds/inside_hospital_2.jpg"
    show expression "bk3/katara/pregfuck/braid_solo.png":
        xpos 0 ypos 0
    show toxh toxh08
    if temp_boolean == True:
        show expression "bk3/katara/pregfuck/spermout4.png"
    else:
        show expression "bk3/katara/pregfuck/spermin2.png"
    k3 "How about a kiss?"
    y "That seems an impropriate thing to do considering you're my patient."
    y "....eh, screw medical ethics!"
    show expression "bk3/katara/pregfuck/shadowkiss.png" with pinkflash

    play sound "audio/kiss.mp3"

    "you let your lips linger on Katara's for a moment and then slowly pull away."
    show expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    hide expression "bk3/katara/pregfuck/shadowkiss.png"
    with Dissolve(1.5)
    y "I... have to go now."
    k3 "Please come back soon!"
    y "Don't worry. I will, but be warned."
    y "When I do... I'm gonna fuck you so hard you'll need a real doctor afterwards!"
    k3 "...that's... disturbing."
    y "Sorry, thought it would sound cool and all."
    y "fuck... can i just sleep here?"
    y "i'm worn out."
    y "I need a nap."
    k3 "of course you can sleep here, love."
    y "oh."
    y "good..."
    y "*yaawn*"
    scene black with Dissolve(1)
    "you fall asleep quickly and deeply."
    stop music
    play music "audio/Kai_Engel_-_01_-_Take_a_Look_Around_You.mp3"
    ".........."
    "........................."
    "mmmmggaggmmm!"
    "mmagamgmgammagmmag!!"
    "mfmmmmaghgghmmmahgghg!!!!"
    y "whosa... wha?"
    suki "aang! wake! up!"
    scene inside_hospital
    show tosi tosi03
    with dissolve
    suki "I've been yelling for like fifteen minutes!"
    y "that noise was you?"
    suki "how asleep were you?!"
    suki "nevermind!"
    suki "shit's hitting the fan!"
    y "what do you mean...?"
    suki "ba sing se has fallen!"
    y "what do you mean \"it's fallen\"?"
    suki "I mean azula and her cronies have taken over the palace and the city!"
    suki "it's chaos out there!"
    y "is everyone in the village okay?"
    suki "everyone except katara!"
    suki "she's gone!"
    ya "{size=+5}what?!? {/size}" with hpunch
    ya "where is she?"
    suki "she's. in. the. city. you. melon."
    y "why?"
    suki "I don't know!"
    suki "supplies, maybe?"
    y "well, I have to go get her!"
    suki "no shit!"
    suki "get out there!"
    y "is toph okay?"
    suki "yes!"
    suki "now go!"
    y "fuck!"

    scene black with dissolve
    play music "audio/Industrial Cinematic.mp3"
    call screen love_basingse_map 


label b3love_theend:
    scene
    show expression "bk3/toph/party/bg_citystreet1.jpg":
        xpos -1000
    with Dissolve(1)
    y "katara!"
    y "are you here!"
    play sound "audio/earth.wav"
    y "fuuuuck!" with sshake
    y "katara!"
    show toeg toeg01:
        xzoom -1
    show toki toki03
    show toki_angry
    with moveinright
    k3 "take this!"
    with flash
    dl "ah!" with hpunch
    dl "yeah, take this!"
    with flash
    k3 "ugh!" with hpunch
    k3 "taaake...."
    k3 "this!" with hpunch
    dl "ahh!" with hpunch
    show toki toki02
    hide toeg
    with dissolve
    k3 "*pant...* *pant...*"
    y "katara, you're okay!"

    k3 "\"okay\" is relative, here..."
    k3 "the city is falling."
    k3 "we... we have to stop it..."
    y "it's not falling, katara... it's {i}fallen{/i}."
    y "you have to get out of here."
    k3 "what about you?"
    y "i... i think i should-"
    play sound "audio/thunder2.mp3"
    with flash
    y "fuck!"
    k3 "what now?!"
    play sound "audio/thunder2.mp3"
    show pgfull
    with flash
    s "{b}it is time."
    y "oh, {i}bullshit{/i}!"
    y "i'm getting katara out of here first!"
    k3 "i'll be fine, aang!"
    k3 "it's okay!"
    k3 "go!"
    k3 "i know how to get back safely, i just... didn't want to believe the city would fall..."
    k3 "goodbye, aang!"
    k3 "i... i hope i see you in my future!"
    y "what do you mean?!"
    y "you never explained how you know so much!"
    k3 "i... i shouldn't tell you!"
    k3 "but... you came back!"
    y "what?!"
    k3 "you came back!"
    k3 "you told me what would happen! and how i could help!"
    k3 "i hope i did you justice!"
    y "you were amazing!"
    k3 "don't leave me forever, okay?!"
    y "I promise!"
    s "{b}we must leave."
    y "fuck you, spirit!"
    y "go away for now!"
    y "i'm saying goodbye!"
    s "{b}very well."
    s "{b}i will return."
    play sound "audio/thunder2.mp3"
    hide pgfull
    with flash
    y "ah!"
    y "..."
    y "damn that bitch."
    hide toki_angry with dissolve
    k3 "it's okay, aang."
    k3 "i understand."
    y "toph won't."
    k3 "I'll help her."
    k3 "she's strong."
    k3 "she might take it even better than i did."
    y "help her, please."
    k3 "I will, i promise."
    k3 "goodbye, aang."
    y "goodbye, katara."
    hide toki with moveoutleft
    y "alright, spirit..."
    y "......"
    y "great, now that i'm ready, you're not around."
    y "this is bullshit."
    y "where the fuck did you-"
    jump tylee_rub

label tylee_rub:
    $ toxj_arms = 'down'
    $ toxj_face = 'normal'
    $ toxj_bikini = 'on'
    stop music
    play music "audio/Unwritten Return.mp3"
    play sound "audio/thud.mp3"
    show toxj_ty01
    y "ow!" with sshake
    y "ty lee...?"
    y "fuck, that was like running into a wall."
    y "how did i not knock you over?"
    ty "strong thighs."
    y "....nice."

    ty "What are you doing here?"
    y "I'm actually... leaving."
    ty "For how long?"
    y "Oh, you'll see me soon again."
    y "In fact, I promise I'll help you out in your tavern."
    ty "But I don't have a tavern."
    y "Yet."
    ty "Oh, okay!"
    y "What are you wearing?"
    ty "It's a spanking new swimsuit! How do you like it?"
    y "It's nice."
    hide toxj_ty01
    show toxj_ty03
    ty "You can't just say it like that!"
    y "I... I can't?"
    ty "No, you have to look up and down and say stuff like \"That looks hot\"!"
    y "No prob."
    hide toxj_ty03
    show toxj_ty02:
        xpos 0 ypos 0
        easeout 5.0 ypos -360
        easeout 5.0 ypos 0
    with Dissolve(1.5)
    $ renpy.pause()
    y "Okay, I got me an eyeful of that."
    ty "And?"
    y "It nicely accents your voluptuous figure and it looks super hot!"
    ty "that's a lot better!"

    hide toxj_ty02
    show toxj_ty01
    with Dissolve(1.5)
    ty "Well, if you're going... Can we do something before you go?"
    y "It has to be quick, but sure I can spare a few minutes."
    ty " I want to waterboard you."
    y "Say what?"
    ty "I want you to lie down so I can squat over your face and rub my pussy all over."
    ty "That's what they call waterboarding right?"
    y "That's... news to me. "
    y "I guess when you're a gusher it can be though."
    menu:
        "Sure let's do this!":
            $ toxj_rub = 'face'
            y "That sounds.. great!"
        "suggest alternative":

            $ toxj_rub = 'dick'
            y "How about my dick instead?"
            ty "I already played lot's with mr. penis I want something new."
            y "Sorry Tylee, but mr. dick misses miss pussy."
            ty "....okay fine."

    hide toxj_ty01
    show toxj_ty05

    with Dissolve(1.5)
    ty "I'll take this off and..."
    y "Eeehh, we might better do this in that alley over there."
    ty "Oh! Good idea!"
    hide toxj_ty05
    show expression "ebackgrounds/nightsky.jpg"
    hide expression "bk3/toph/party/bg_citystreet1.jpg"

    show toxj toxj00
    if toxj_rub == 'face':
        show expression "bk3/tylee/tyrub/face1.png"
    with Dissolve(1.5)

    ty "You have the best seat in the house!"


    "you can already see her moistening in anticipation."
    "she lowers her body and..."
    show toxj toxj03 with Dissolve(1.5)
    if toxj_rub == 'dick':
        "presses her pussy lips again your penis."

        y "A dick carressed by the lower lips of a pretty girl... it doesn't get more comfortable."
        y "Mr. dick is ready to get a full body wash!"
        y "A happy end is unavoidable!"
    else:
        "presses her pussy lips against your face."
        ty "Please give miss pussy a nice fat kiss."
        play sound "audio/kiss.mp3"         
        show expression "bk3/tylee/tyrub/face1.png":
            alpha 0.5
        with pinkflash
        show toxj_tongue:
            xpos 420 ypos 320
            easein 1.2 ypos 260
            repeat

        "You give a long kiss and start sliding your tongue between Tylee's labia."

        $ toxj_face = 'lewd'
        ty "Oooh, I like it when you do that!"
        ty "Let's... let's just keep doing that... for a while longer"
        $ renpy.pause()
        ty "Oooohh, yeah. Make sure to hit all nooks and crannies... *mmm...*"
        ty "Ah... this... is nice but I still have to waterboard you so hold on for a minute."

        hide toxj_tongue
        show toxj toxj03
        show expression "bk3/tylee/tyrub/face1.png":
            linear 7.0 alpha 0.0





    $ toxj_face = 'normal'
    ty "Okay, I'll start rubbing now!"
    show toxj toxj100
    "toxj100"
    ty "Oh! This feels so naughty! I'm a naughty girl!"
    ty "Look at me, rubbing my pussy all over you!"
    $ toxj_face = 'lewd'
    ty "mmmmmm... I really like the rubbing against my clit."
    $ renpy.pause()
    $ toxj_arms = 'up'
    $ renpy.pause()
    ty "I'm getting reeaally hot... Gotta take off the top too!"
    $ toxj_bikini = 'off'
    ty "That's better!"
    ty "Gotta go faster! Hold on!"

    show toxj toxj101
    if toxj_rub == 'dick':
        "The super quick rubbing makes you feel like your dick has caught fire."
        "Luckily your dick is drenched in Tylee's juices."
    else:

        "You gasp for air during the small moments you can as Tylee is ferociously goes back and forward."
        "Your face is drenched in Tylee's juices."
    $ toxj_face = 'normal'
    ty "I'm.... I'm about to squirt!"
    ty "Get ready for a flood!"
    $ toxj_arms = 'down'
    if toxj_rub == 'dick':
        y "Right behind you!"
    else:
        y "*mumble*"

    $ toxj_face = 'lewd'
    play sound "audio/gltch2b.mp3" 
    show toxj toxj02 with flash
    show expression "bk3/suki/pussyrub/pjuice_1.png"
    ty "Ahh!!"
    play sound "audio/gltch2b.mp3" 
    show toxj toxj03 with flash
    show expression "bk3/suki/pussyrub/pjuice_2.png"
    ty "Aaaaah!!"
    play sound "audio/gltch2b.mp3" 
    show toxj toxj04 with flash
    show expression "bk3/suki/pussyrub/pjuice_3.png"
    ty "Aaaaah!!"

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.5)

    hide toxj
    show toxj toxj00
    with Dissolve(1.5)

    $ toxj_face = 'normal'
    ty "That was fun!"

    mv "TYLEE!!" with hpunch

    hide toxj
    hide expression "ebackgrounds/nightsky.jpg"
    show expression "bk3/toph/party/bg_citystreet1.jpg":
        xpos -1000

    show toxj_ty03:
        xzoom -1.0
    ty "Aaaah! Who's that!"
    show toxj_az02:
        xpos 400
        linear 0.5 xpos 0
    a "what are you doing?!"
    hide toxj_ty03
    show toxj_ty04:
        xzoom -1.0
    ty "uh, oh, hi... Azula..."
    a "You're butt naked! In the streets!" with hpunch
    ty "Uh... I'm wearing a smile?"
    "You slowly crawl away in the commotion."
    "Azula, completely flustered with Tylee's undressed state, hasn't even noticed you. "
    hide toxj_az02
    show toxj_az01:
    with Dissolve(1.5)
    a "I can't believe you... you were... I haven't even... Well, whatever!!"
    a "we got work to do!"
    show toxj_mai01:
        xpos 300
        linear 2.0 xpos 100
    m "Hey Ty!"
    ty "Hey Mai!"
    hide toxj_az01
    show toxj_az01:
        xpos 0
        linear 1.0 xpos -200
    a "Enough!"
    a "put some pants on Ty Lee. We leave now!"
    ty "Okay!"
    $ toxj_bikini = 'on'
    hide toxj_ty04
    show toxj_ty02:
        xzoom -1.0
    ty "What are we going to do?"
    a "Topple a king."
    a "Do you still have that \"fangirl\" outfit? "
    ty "Fangirl? OH the kyoshi warrior outfit! Haha, good one, azula!"
    ty "But I'm afraid I lost it...."
    a "I should have expected this to happen... and I did. I have another one for you."
    a "now let's go."
    hide toxj_az01 with Dissolve(1.5)
    show toxj_mai01:
        xpos 0
    m "Hope you had fun while being away, Azula has been extra touchy lately so we better not make her wait."
    ty "I'll be with you guys in a minute."
    hide toxj_mai01 with Dissolve(1.5)
    hide toxj_ty02
    show toxj_ty01
    with Dissolve(1.5)
    ty "Pssst... Are you still there, Aang?"
    y "Yep."
    ty "I had a lot of fun, but it looks like I gotta go too!"
    y "Don't worry about it. We'll have even more fun in your future!"
    ty "Really?"
    y "I guarantee it! See you later Ty!"
    ty "Bye Bye!!"
    hide toxj_ty01 with Dissolve(1.5)
    y "I feel a little strange and sad her future is my past."

    show pgfull with dissolve
    s "{b}it is time."
    y "alright."
    y "i'm ready."
    "the spirit pulls you out of aang's body."
    scene black with dissolve
    scene black
    scene worldmap_01
    show pgfull
    with dissolve
    y "so what happens now?"
    s "{b}you will learn airbending."
    y "i will?"
    y "how?"
    s "{b}you will find out... now."
    jump b4_s_main


    "test"

    "test"

    "test"


    "test"

    "test"

"test"


label bk3_katara_pregrub:




    $ totk_preg = True


    scene black
    show expression "bk3/katara/rub/floor_tokt.jpg"
    show totk totk03
    with Dissolve(1.5)

    k3 "Ready when you are."
    y "I was ready the first day I saw you."

    show expression "ebackgrounds/ceiling_1.jpg"
    hide totk
    show totk totk17 with Dissolve(1.5)

    show ctcblink
    $ renpy.pause()
    hide ctcblink

    y "Wow, you're dripping wet already!"

    show totk totk14 with Dissolve(1.5)
    "You stand behind Katara and slide your hand down over her big belly as she lifts her arms."

    show totk totk11 with Dissolve(1.5)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "Just making absolutely certain you're ready to receive me in my full glory."
    "you keeping sliding your two fingers in and out of Katara's pussy."
    "katara" "Hnnn... "
    y "That's my girl."

    show totk totk06 with Dissolve(1.5)
    "You drop your pants and stick your dick in between her legs."
    k3 "That didn't take you long. You couldn't hold back any longer?"
    show totk totk05
    y "Don't underestimate my willpower woman!"
    y "I'm going to rub up against your lips until you go crazy!"

    k3 "You're such a tease."
    k3 "Do you want me to beg for it?"
    k3 "Beg for you to stop rubbing your throbbing cock up against my clit?"
    k3 "Beg to put it in my wet tight-"

    show totk totk06
    y "...."

    k3 "Why did you stop?"

    show totk totk07 with vpunch
    k3 "Ah!"

    show totk totk08 with Dissolve(1.5)
    y "I changed my mind!"
    y "My willpower remains as strong as ever!"
    k3 "I'm loving that hard and thick willpower of yours."
    y "Hnnnnng! I could do this forever."

    k3 "I don't need forever. But... Ah!! ..how does the rest of our lives sound like to you?"
    y "....Pretty good... "
    y " Never ever change Katara."
    k3 "I won't! And if you ever get impotent I can bloodbend your dick all hard again!"
    y "Hah! With such a plump booty in arms reach? No way that'll ever happen."
    y "...please don't bloodbend my dick.."
    y "Or I'll spank you!"

    menu:
        "slap her ass.":

            show totk totk06
            show totk totk19 with Dissolve(1.5)

            $ temp_int = 0

            show expression "bk3/katara/rub/ass_blush.png":
                alpha 0.1 xpos 400 ypos 200

            while temp_int < 7:


                play sound "audio/slap.mp3"  


                show totk totk19
                show expression "bk3/katara/rub/ass_blush.png":
                    alpha 1.0
                show expression "bk3/katara/rub/ass_slaphand_1.png":
                    xpos 440 ypos -40
                show expression "bk3/katara/rub/head_surprise3.png":
                    xpos -420 ypos -20
                show text "AH!":
                    xpos 100 ypos 240
                with hpunch

                hide expression "bk3/katara/rub/head_surprise3.png"
                hide text
                show expression "bk3/katara/rub/head_standard.png":
                    xpos -420 ypos -20

                hide expression "bk3/katara/rub/ass_slaphand_1.png"
                show expression "bk3/katara/rub/ass_slaphand_0.png" at Move((700, -250), (900, 0), 0.15 )


                show expression "bk3/katara/rub/ass_blush.png":

                    alpha 1.0
                    xpos 400 ypos 200
                    linear 3.0 alpha 0.1
                $ renpy.pause()
                $ temp_int += 1

                hide expression "bk3/katara/rub/ass_slaphand_0.png"

                hide expression "bk3/katara/rub/head_standard.png"

            hide expression "bk3/katara/rub/ass_blush.png"
            hide expression "bk3/katara/rub/ass_slaphand.png"

            show expression "bk3/katara/rub/head_standard.png":
                xpos -420 ypos -20


            k3 "I'm not convinced yet."
            k3 "Maybe if you slap me some more..."
            y "...."
            hide expression "bk3/katara/rub/head_standard.png"

            show totk totk07
            k3 "Ah!" with vpunch
            y "Back inside it goes!!"
        "keep going like this":



            $ renpy.pause()
            pass

    y "Ready or not. I'm gonna split that pussy open with enough force to lift you from the ground!"
    k3 "DO IT!!"
    show totk totk100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "you start thrusting your cock into Katara just hard enough for her to make small shreeks."
    k3 "Hiii!"
    y "Where do you want it Katara? In or outside!?"
    k3 "Wherever.. unf! you prefer! It's not like you can get me more pregnant!"
    y "Is that a challenge!?!"
    y "gonna cum!"

    menu:
        "Inside!":

            y "Here... it... comes !"
            show totk totk12
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Going once!"
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Going twice!"
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "SOOOOLLLLDDDD!!!!"

            hide totk
            show totk totk06
            show expression "bk3/katara/rub/sperm_flowout.png"
            with Dissolve(1.5)
            y "....annndd I'm empty"
            y "I feel completely drained."
            y "You're just too pretty and sexy Katara!"
        "cum outside":


            $ temp_boolean = True
            hide totk
            show totk totk19
            with Dissolve(1.5)
            "You pull out of Katara and.."
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm1.png" with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm2.png" with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"    
            show expression "bk3/katara/rub/body_butt_sperm3.png" with flash
            $ renpy.pause()
            "..paint her ass white."
            y "You're just too pretty and sexy Katara!"



    k3 "Mmmm, that was fantastic. My legs are feeling wobbly."
    y "Why don't you lie down for a minute?"

    scene black

    show expression "ebackgrounds/inside_hospital_2.jpg"
    show expression "bk3/katara/pregfuck/braid_solo.png":
        xpos 0 ypos 0
    show toxh toxh08
    show expression "bk3/katara/pregfuck/spermin2.png"
    show expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    with Dissolve(1.5)

    k3 "How about a kiss for your sexy watertribe girl?"
    y "I can do better than that!"



    show expression "bk3/katara/pregfuck/zhadkiss_katface.png"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    hide expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png" with pinkflash

    "You softly kiss katara on her lips."

    hide expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png":
        xpos 300 ypos 50
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png" with pinkflash

    "On her belly."



    hide expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png":
        xpos 450 ypos 170
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png" with pinkflash


    "And finally between her legs."

    hide expression "bk3/katara/pregfuck/zhadkiss_katface.png"
    hide expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    show expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    with Dissolve(1.5)

    y "I... have to go now."
    k3 "Please come back soon!"
    y "Don't worry. I will, but be warned."
    y "When I do... I'm gonna fuck you so hard you'll need a doctor afterwards!"
    k3 "...that's... disturbing."
    y "Sorry, thought it would sound cool and all."
    y "fuck... can i just sleep here?"
    y "i'm worn out."
    y "I need a nap."
    k3 "of course you can sleep here, love."
    y "oh."
    y "good..."
    y "*yaawn*"
    scene black with Dissolve(1)
    "you fall asleep quickly and deeply."
    stop music
    play music "audio/Kai_Engel_-_01_-_Take_a_Look_Around_You.mp3"
    ".........."
    "........................."
    "mmmmggaggmmm!"
    "mmagamgmgammagmmag!!"
    "mfmmmmaghgghmmmahgghg!!!!"
    y "whosa... wha?"
    suki "aang! wake! up!"
    scene inside_hospital
    show tosi tosi03
    with dissolve
    suki "I've been yelling for like fifteen minutes!"
    y "that noise was you?"
    suki "how asleep were you?!"
    suki "nevermind!"
    suki "shit's hitting the fan!"
    y "what do you mean...?"
    suki "ba sing se has fallen!"
    y "what do you mean \"it's fallen\"?"
    suki "I mean azula and her cronies have taken over the palace and the city!"
    suki "it's chaos out there!"
    y "is everyone in the village okay?"
    suki "everyone except katara!"
    suki "she's gone!"
    ya "{size=+5}what?!? {/size}" with hpunch
    ya "where is she?"
    suki "she's. in. the. city. you. melon."
    y "why?"
    suki "I don't know!"
    suki "supplies, maybe?"
    y "well, I have to go get her!"
    suki "no shit!"
    suki "get out there!"
    y "is toph okay?"
    suki "yes!"
    suki "now go!"
    y "fuck!"

    scene black with dissolve
    play music "audio/Industrial Cinematic.mp3"
    call screen love_basingse_map 
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
