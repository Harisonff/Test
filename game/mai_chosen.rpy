screen zember_daymap:

    imagemap:
        ground "emberisland/bg_island_day.jpg"
        hover "emberisland/emberisland_shine.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("zember_party1")
        hotspot (413, 220, 119, 119) clicked Jump("zember_shop1")
        hotspot (355, 348, 142, 114) clicked Jump("zember_beach1")

        hotspot (617, 446, 166, 149) clicked Jump("zember_water1")
        hotspot (795, 275, 125, 125) clicked Jump("zember_shack1")

screen zember_nightmap:

    imagemap:
        ground "emberisland/bg_island_night.jpg"
        hover "emberisland/emberisland_shine_night.png"

        add "emberisland_cloud"


        hotspot (228, 241, 113, 126) clicked Jump("zember_party2")
        hotspot (413, 220, 119, 119) clicked Jump("zember_shop2")
        hotspot (355, 348, 142, 114) clicked Jump("zember_beach2")

        hotspot (617, 446, 166, 149) clicked Jump("zember_water2")
        hotspot (795, 275, 125, 125) clicked Jump("zember_shack2")
label mai_chosen:
    $ maikup_spread = False
    $ maikup_pussylick = False
    $ maikup_anallick = False
    jump zemday

label zemday:
    if not zem_day:
        stop music fadeout 2
        play music "audio/Bassa Island Game Loop.ogg"
        $ zem_day = True
    scene black
    scene bg_island_day
    with dissolve
    call screen zember_daymap

label zemnight:
    if zem_day:
        stop music fadeout 2
        play music "audio/Doctor_Turtle_-_04_-_Im_What_Youd_Be_Without_Her_Long_Version.mp3"
        $ zem_day = False
    scene black
    scene bg_island_night
    with dissolve
    call screen zember_nightmap

label zember_party1:
    if mai_quest_start and not mai_married:
        y "today's the big day. i should see if i can find mai."
        jump zemday

    if not zem_doot:
        stop music
        play music "audio/DOOT DOOT REMIX  Thank mr skeltal.ogg"
        show bg_a_island_partyhouse with dissolve
        y "heh."
        show ml with dissolve
        m "didn't we burn this house down?"
        y "yeah. that's what i was \"heh\"-ing."
        m "i wonder if it's haunted?"
        y "maybe. i-"
        yd "....."
        ya "what the damn hell is that music?"
        m "i don't hear any music."
        yd "it's super.... dooty."
        m "what?"
        yd "Like.... spoo-"
        y "nevermind. this joint is haunted. let's go before we get conscripted."
        m "conscripted?"
        yd "you know, into the skeleton ar-"
        y "forget it."
        y "hey, does that shop sell milk?"
        m "yes.... why?"
        y "calcium. i mean.... no reason."
        $ zem_doot = True
        stop music fadeout 2
        play music "audio/Bassa Island Game Loop.ogg"
        jump zemday
    if zem_doot:
        y "nope, i'm not going there."
        y "i like my skeleton where it is."
        jump zemday

label zember_shop1:
    scene black
    scene bg_a_armory
    with dissolve
    if mai_quest_start and not mai_married:
        y "mai?"
        m "get out of here! you're not supposed to see me!"
        m "....."
        m "and i love you."
        y "i guess i'll wait for her at the beach."
        jump zemday

    scene black
    scene bg_a_armory
    with dissolve
    if zem_sexy:
        yd "huh, mai's not here."
        y "oh, she left a note...."
        m_ "come down to the beach, zuko!"
        m_ "i'll be waiting...."
        y "neat."
        jump zemday

    show ml with dissolve

    if not zem_mai_quest:
        m "you know, i bet i could really make this shop my own."
        m "shady seems long gone from here."
        hide ml
        show mf
        with dissolve
        m "tell you what, if you can grab a few things for me, i'll get this place in working order."
        m "and then we'll have some fun."
        yd "alright, what do you need?"
        m "sea shells for tourists, crabs for the battlers, a vase for decoration, and some fish."
        yd "why the fish?"
        m "so we can eat, zuko."
        y "oh. right."
        y "okay, i'm on it!"
        $ zem_mai_quest = True
        jump zemday
    else:
        if zem_shells and zem_crabs and zem_vase and zem_fish:
            y "i got everything."
            hide ml
            show mls
            with dissolve
            m "you're great, zuko."
            m "it's gonna take me the rest of the day to finish up the shop, though."
            m "meet me here later."
            $ zem_sexy = True
            jump zemnight
        else:

            if zem_boat_start and not zem_boat:
                if need_driftwood and not driftwood_got:
                    m "i need some driftwood if you want me to fix that boat."
                    y "can do."
                    jump zemday

                if need_driftwood and driftwood_got:
                    $ zem_boat = True
                    y "hey, i found this driftwood. will it work?"
                    m "it should. give me a minute."
                    hide ml with dissolve
                    show mf with dissolve
                    m "okay, here's your boat."
                    play sound "audio/win2.mp3"
                    "you got a boat!"
                    m "use it to get us some crabs!"
                    jump zemday
                else:

                    m "any luck finding those items?"
                    menu:
                        "what items, again?":
                            m "i need sea shells, crabs, a vase, and some fish."
                            menu:
                                "i need a boat":
                                    y "any chance you've got a boat back there?"
                                    m "yes, but-"
                                    y "sweet!"
                                    m "but it's missing a plank."
                                    yc "aw."
                                    m "just bring me some driftwood, and i'll put it together for you."
                                    y "get some driftwood. will do!"
                                    $ need_driftwood = True
                                    jump zemday
                                "exit":

                                    jump zemday
                        "i need a boat":

                            y "any chance you've got a boat back there?"
                            m "yes, but-"
                            y "sweet!"
                            m "but it's missing a plank."
                            yc "aw."
                            m "just bring me some driftwood, and i'll put it together for you."
                            y "get some driftwood. will do!"
                            $ need_driftwood = True
                            jump zemday
                        "exit":

                            jump zemday
            else:

                m "hey, zuko! i'm a little busy setting up."
                m "i still need sea shells, crabs, a vase, and some fish."
                m "come back when you've got them!"
                yd "oh, fine."
                jump zemday

label zember_beach1:
    if mai_quest_start and not mai_married:
        y "today's the big day!"
        jump mai_marry_begin

    if zem_sexy:
        scene black
        scene bg_a_beach_01
        with dissolve
        show mai_idle_ff_beach
        show mai_idle_ff_smile
        show mai_idle_ff_blush
        with dissolve
        if mai_conv >=1:
            m "hello, my love."
            m "i was missing you."
            m "would you like to walk around? or have some fun?"
        if mai_conv ==0:
            $ mai_conv = 1
            m "hello, my love."
            m "did you sleep well?"
            y "i did, yeah."
            y "did you know that you snore a little?"
            show mai_idle_ff_angry with dissolve
            m "i do not!"
            ys "it's very cute, actually."
            hide mai_idle_ff_angry
            show mai_idle_ff_blush
            with dissolve
            m ".....shut up."
            y "so, we've got the island to ourselves."
            y "what do you want to do?"
            m "whatever you'd like."
            m "we could go for a walk and chat...."
            m "....or we could have some fun."

        menu:
            "walk the beach":
                if mai_walk ==2:
                    if start_mai_marriage:
                        y "let's walk around some."
                        m "that sounds nice."
                        scene black
                        scene bk2_beach01:
                            xpos -1000
                            linear 80 xpos 0
                            repeat
                        show mai_idle_fl_beach:
                            ypos 7
                            linear 1 ypos 0
                            linear 1 ypos 7
                            repeat
                        show mai_idle_fl_smile:
                            ypos 7
                            linear 1 ypos 0
                            linear 1 ypos 7
                            repeat
                        with dissolve
                        menu:
                            "propose":

                                if mai_dock and mai_knife and mai_ring:
                                    "there is no turning back from this option."
                                    "continue?"
                                    menu:
                                        "continue":
                                            $ mai_quest_start = True
                                        "not yet":
                                            "you walk around with mai, laughing and talking."
                                            "day passes quicker than you thought possible, and evening arrives."
                                            jump zemnight


                                    y "hey, mai... would you like to walk over to the dock with me?"
                                    m "sure, i'm up for a walk."
                                    scene black with dissolve
                                    "you and mai walk up to the dock."
                                    scene emberisland_dock
                                    show background_fade_purpleish
                                    with dissolve
                                    show mai_idle_fl_beach
                                    show mai_idle_fl_smile
                                    with dissolve
                                    y "mai...."
                                    m "what's up?"
                                    menu:
                                        "you're neat":
                                            y "you are one neato burrito."
                                            m "...okay..."
                                        "i love you":

                                            y "you are my everything."
                                            m "oh, zuko..."
                                        "my erection has lasted longer than 4 hours":

                                            y "i need to see a doctor."
                                            m "what?"
                                            y "because i have a boner.... in my heart."
                                            m "...."

                                    y "my life without you would be..."

                                    menu:
                                        "still nice, but not as nice":
                                            y "...well, my dick would certainly be drier. maybe."
                                            m "would it?"
                                        "probably less gloomy":

                                            y "...probably more cheerful, but co-dependent relationships are where it's at."
                                            m "......"
                                        "worthless":

                                            y "...nothing without you."
                                            m "i feel exactly the same way!"

                                    y "you're the reason i..."

                                    menu:
                                        "smile":
                                            y "...wake up in the morning, willing to face the day."
                                            m "i couldn't bear to be without you."
                                        "drink":

                                            y "get drunk. i mean, you just let me be me. it's great."
                                            m "...i'm glad you feel you can be yourself with me."
                                        "am getting kind of fat":

                                            y "...am pudging out. i don't want to be with anyone else."
                                            m "well... we can both get fat."
                                            ya "no."
                                            ya "just me."

                                    y "will you..."

                                    menu:
                                        "be my boo":
                                            y "be my highest-ranking shawty?"
                                        "keep it tight":

                                            y "be my trophy wife?"
                                        "marry me":

                                            y "be mine forever?"

                                    m "yes! of course!"
                                    m "but... i want you to know that i'm just happy being with you."
                                    m "i don't need more than that."
                                    y "and that's why i want to give you everything."
                                    m "then yes.... i love you! of course i'll marry you!"
                                    show shadyguy_grin:
                                        xpos -300
                                    with dissolve
                                    sg "hey, i've got the-"
                                    ya "ah!"
                                    m "what are you doing here?"
                                    sg "what?"
                                    sg "oh, right, you guys probably don't know."
                                    sg "we're set up for tomorrow."
                                    y "....why?"
                                    sg "because love! why wait?"
                                    sg "risk! love! dare! give! take!"
                                    sg "i'll see you two tomorrow."
                                    hide shadyguy_grin with dissolve
                                    y "well..."
                                    m "i guess..."
                                    y "we're getting married tomorrow?"
                                    m "....i can't wait."
                                    ys "me neither."
                                    m "let's.... sleep separately tonight."
                                    yd "why?"
                                    m "to make tomorrow more special."
                                    y "....fine."
                                    scene black with dissolve
                                    "you sleep in a different room from mai, anxious and hopeful for what the morning will bring."
                                    jump zemday

                                if not mai_dock:
                                    "you don't have permission to use the dock to propose."
                                if not mai_knife:
                                    "you don't have a ceremonial wedding dagger."
                                if not mai_ring:
                                    "you don't have a ring."

                                "you walk around with mai, laughing and talking."
                                "day passes quicker than you thought possible, and evening arrives."
                                jump zemnight
                            "just keep walking":

                                "you walk around with mai, laughing and talking."
                                "day passes quicker than you thought possible, and evening arrives."
                                jump zemnight
                    else:

                        menu:
                            "propose":
                                y "(i have no idea what she wants...)"
                                "you walk around with mai, laughing and talking."
                                "day passes quicker than you thought possible, and evening arrives."
                                jump zemnight
                            "just keep walking":

                                "you walk around with mai, laughing and talking."
                                "day passes quicker than you thought possible, and evening arrives."
                                jump zemnight

                if mai_walk ==1:
                    $ mai_walk = 2
                    y "let's stroll a bit."
                    m "okay, handsome."
                    scene black
                    scene bk2_beach01:
                        xpos -1000
                        linear 80 xpos 0
                        repeat
                    show mai_idle_fl_beach:
                        ypos 7
                        linear 1 ypos 0
                        linear 1 ypos 7
                        repeat
                    show mai_idle_fl_smile:
                        ypos 7
                        linear 1 ypos 0
                        linear 1 ypos 7
                        repeat
                    with dissolve
                    m "so. what would you like to talk about?"
                    y "don't know, just thought we could see what-"
                    scene black
                    scene bk2_beach01
                    show wedding_crowd
                    show mai_idle_fl_beach
                    with dissolve
                    y "i wonder what's going on over there?"
                    m "i think... it's a wedding?"
                    y "huh. odd that it's on a beach."
                    m "i think a beach is a perfect place to get married."
                    y "really?"
                    m "yeah. provided there are umbrellas to stop all the sun."
                    y "interesting."
                    m "i guess."
                    m "there's too many people here -- i'm not big on crowds."
                    m "plus, it's getting late. let's head back."
                    jump zemnight

                if mai_walk ==0:
                    $ mai_walk = 1
                    y "let's go for a walk."
                    ys "I'd like to just.... talk."
                    m "i'd love that."
                    scene black
                    scene bk2_beach01:
                        xpos -1000
                        linear 80 xpos 0
                        repeat
                    show mai_idle_fl_beach:
                        ypos 7
                        linear 1 ypos 0
                        linear 1 ypos 7
                        repeat
                    show mai_idle_fl_smile:
                        ypos 7
                        linear 1 ypos 0
                        linear 1 ypos 7
                        repeat
                    with dissolve
                    y "so. tell me honestly, are you happy?"
                    m "of cour-"
                    hide mai_idle_fl_smile with dissolve
                    m "...."
                    m "i don't know."
                    m "don't get me wrong, i'd rather be here with you than anywhere without you..."
                    m "but giving up everything i know... and you giving up everything you know..."
                    m "is terrifying."
                    y "i know the feeling."
                    scene black
                    scene bk2_beach01
                    show mai_idle_fl_beach
                    with dissolve
                    m "i know."
                    m "i wasn't going to say anything..."
                    m "maybe i would have. i don't know."
                    hide mai_idle_fl_beach with dissolve
                    show mai_idle_ff_beach with dissolve
                    m "i feel... so uncertain."
                    m "like i'm in the wind."
                    m "rootless."
                    y "hmm..."
                    y "well, what would make you feel more secure?"
                    m "i don't think anything. just time, maybe."
                    m "as long as i have you, that's all i need."
                    m "i just want you forever."
                    m "i think everything else will just fall in line then."
                    yd "what do you mean?"
                    m "well, we've only just gotten together."
                    m "our relationship is kind of... uncertain."
                    m "i don't know what could change that."
                    y "hmm...."
                    m "don't worry about it, i'm sure i'll get over it."
                    m "it's getting late.... let's just walk back."
                    jump zemnight
            "blowjob/handjob":


                yd "how about a blowjob?"
                m "mmm... happily."
                jump zem_blowjob
            "anal":

                jump zem_anal

    if zem_mai_quest:
        menu:
            "beach spot 1":
                scene bg_a_beach_01 with dissolve
                yd "crap, no shells here."
                jump zember_beach1
            "beach spot 2":

                if zem_shells:
                    y "i already found sea shells."
                    jump zember_beach1
                else:
                    scene bg_a_beach_02 with dissolve
                    play sound "audio/win2.mp3"
                    y "found some sea shells!"
                    $ zem_shells = True
                    jump zember_beach1
            "beach spot 3":

                scene bg_a_beach_00 with dissolve
                if need_driftwood and not driftwood_got:
                    play sound "audio/win2.mp3"
                    "you found some driftwood!"
                    $ driftwood_got = True
                    y "i should get this driftwood to mai."
                    jump zemday
                else:
                    yd "doesn't seem to be anything i need here...."
                    jump zember_beach1
            "beach spot 4":


                scene bg_a_beach_chairs with dissolve
                if zem_rod:
                    yd "doesn't seem to be anything i need here...."
                    jump zember_beach1
                else:
                    if zem_rod_start:
                        play sound "audio/win2.mp3"
                        "you found a fishing rod!"
                        yd "who would just leave this here?"
                        yd "...."
                        y "i'm not gonna complain about it though."
                        "you stole a bombass fishing pole, you thieving slut!"
                        $ zem_rod = True
                        jump zemday
                    else:

                        yd "doesn't seem to be anything i need here...."
                        jump zember_beach1
            "back":

                jump zemday
    else:

        y "i'll check out the beach a little later."
        jump zemday


label zem_blowjob:
    m "take off your pants, my love."
    y "really?"
    with vshake
    yn "{size=+6}done!"
    m "that was fast..."
    m "now... sit."
    stop music fadeout 2
    play music "audio/Unwritten Return.mp3" fadein 2
    scene black
    show mabj mabj22
    with dissolve
    m "mmmm...."
    show mabj mabj23 with dissolve
    m_l "i hope no one sees..."
    scene black with dissolve
    "mai lays down in the sand in front of you..."
    show mabj mabj01 with Dissolve(0.8)
    m "{size=-4}(wow... i'm always amazed...)"
    show mabj_eyesup with dissolve
    m "zuko..."
    m "i'm..."
    hide mabj_eyesup with dissolve
    m "...happy i'm here with you."
    m "this almost doesn't seem real, does it?"
    show mabj_eyesup with dissolve
    m "we're finally together..."
    m ".........."
    hide mabj_eyesup
    show mabj mabj02
    with dissolve
    m "i want to do this for you forever."
    show mabj mabj100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show mabj_smile
    hide mabj_unsure
    with dissolve
    m "oh, zuko..."
    m "are you ready?"
    show mabj_unsure
    hide mabj_smile
    with dissolve
    yn "that... is a dumb question."
    show mabj mabj05
    hide mabj_smile
    hide mabj_unsure
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
    ync "i want to fuck your mouth every day from now on...."
    m "o'ay..."
    show mabj mabj102
    m "how's it 'eel, prince?"
    yn "unbelieveable!"
    m "'ood..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "hgh..."
    yn "you're so good at this!"
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
    m "you like when i jack your cock?"
    m "am i milking you right?"
    show mabj_angry
    hide mabj_unsure
    with dissolve
    m "i'm going to get this cum out."
    m "you're mine, zuko."
    m "no one else's."
    show mabj_unsure
    hide mabj_angry
    with dissolve
    m "right?"
    ync "hhgngh..."
    m "this feels great, right? and you're mine, right?"
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
            m "i loved it, too."
            if zuko_end:
                jump zcity_night1
            else:
                jump zemnight
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
            m "i loved it, too."
            if zuko_end:
                jump zcity_night1
            else:
                jump zemnight

label zem_anal:
    y "want it in the ass?"
    m "oh, fuck yes."
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
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "..."
    ys "woo!"
    m "oh be quiet, love."
    m "and take your clothes off."
    with ushake
    yn "alright. i'm ready."
    hide mai_idle_ff_blink with dissolve
    m "this is something i really... {i}really{/i} want to do."
    ynd "what-"
    show maan maan00 with sshake
    yng "whoa!"
    yng "you're ready, huh?"
    show maan maan08
    m "like you have no idea."
    ynd "watcha doing there?"
    m "...."
    yng "you're not getting cold feet are you, beautiful?"
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
    m "i need more!"
    show maan maan104
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    ync "ah! what's gotten into you, mai?!"
    m "fuck... ah... \"slow\"..."
    m "i want you... ah... in..."
    m "in my fucking... ah... asshole..."
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
            yn "that's a pretty view."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "amazing."
            show maan maan00
            hide maan_spermdrip
            show nude_mai_fl_flip:
                xpos 100
            with dissolve
            if zuko_end:
                jump zcity_night1
            else:
                jump zemnight
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
            yn "that's a pretty view."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "amazing."
            show maan maan00
            hide maan_spermdrip
            show nude_mai_fl_flip:
                xpos 100
            with dissolve
            if zuko_end:
                jump zcity_night1
            else:
                jump zemnight

label zember_water1:
    if mai_quest_start and not mai_married:
        y "today's the big day. i should see if i can find mai."
        jump zemday
    scene black
    scene bg_emberisland_sea
    with dissolve
    if zem_sexy:
        y "doesn't seem like there's anything here."
        jump zemday

    if zem_boat:
        if zem_crabs:
            y "i've already caught crabs."
            yd "...."
            jump zemday
        else:
            play sound "audio/win2.mp3"
            "you got crabs!"
            yd "hmm."
            $ zem_crabs = True
            jump zemday
    else:

        yd "this would be a good spot to look for crabs."
        y "i should see if mai has a boat in the shop."
        $ zem_boat_start = True
        jump zemday

label zember_shack1:
    if mai_quest_start and not mai_married:
        y "today's the big day. i should see if i can find mai."
        jump zemday
    if zem_sexy:
        if start_mai_marriage and not mai_dock:
            scene black
            scene emberisland_dock
            with dissolve
            yd "hello?"
            show expression "emberisland/twins_0.png" with dissolve
            lal "hello, dearie."
            yc "hey, i was hoping-"
            lal "you want to use our dock to propose."
            yd "....how did you know that?"
            lal "because we know that mai girl."
            lal "and you had better treat her right."
            y "or what?"
            hide expression "emberisland/twins_0.png"
            show expression "emberisland/twins_1.png"
            with vshake
            ya "ah!"
            lal "or we keep stripping!"
            ya "i get it, i get it!"
            lal "well, you have our permission."
            lal "now get lost... we've got swimming to do!"
            yc "with pleasure...."
            $ mai_dock = True
            jump zemday
        else:

            yd "not much here."
            jump zemday

    menu:
        "shack":
            scene black
            scene bg_a_island_hutday
            with dissolve
            if not zem_vase:
                play sound "audio/win2.mp3"
                "you found a vase!"
                y "sweet!"
                $ zem_vase = True
                jump zember_shack1
            else:
                y "i've already got the vase."
                jump zember_shack1
        "dock":

            scene black
            scene emberisland_dock
            with dissolve
            if zem_rod_start:
                if zem_rod:
                    if zem_fish:
                        y "I've already caught fish."
                        jump zemday
                    else:

                        play sound "audio/win2.mp3"
                        "you caught some fish!"
                        y "suck it, nature."
                        $ zem_fish = True
                        jump zemday
                else:

                    y "this looks like a good spot to fish."
                    yd "i'm gonna need to find a fishing rod though."
                    jump zember_shack1
            else:

                y "this looks like a good spot to fish."
                yd "i'm gonna need a fishing rod though."
                $ zem_rod_start = True
                jump zember_shack1
        "back":

            jump zemday

label zember_party2:
    y "no reason to go there."
    jump zemnight

label zember_shop2:
    scene black
    scene bg_a_armory
    with dissolve
    show mls with dissolve
    if not zem_first_night:
        m "hey."
        m "so, i set us up a room in the back."
        yd "we're.... gonna sleep here?"
        m "well, yeah. do you really want to stay in the shack?"
        m "things.... happened there."
        m "and if azula ever comes looking...."
        y "it'll be the first place she looks. right, that's fair."
        m "anyway, i was thinking...."
        m "we should really break this place in."
        ys "yeah?"
        m "yeah."
        m "but.... maybe we'll start tomorrow."
        m "i'm really tired."
        m "unless you're adamant."
        $ zem_first_night = True
        menu:
            "sleep with mai":
                y "nah, let's get some rest."
                m "oh, i'm glad you said that."
                m "come lay with me."
                scene black with dissolve
                "you follow mai into the back, and watch her lay down."
                show amsl amsl00 with dissolve
                show ctcblink
                $ renpy.pause()
                hide ctcblink
                "she falls asleep immediately."
                y "you're so damn cute."
                "she mumbles in her sleep."
                m "*mmghn....*"
                y "i guess we'll talk later...."
                "you lay next to her and she immediately burrows into you, seemingly desperate for your warmth."
                yd "...why {i}don't{/i} we have blankets?"
                y "not that i'm complaining."
                "mai sleeps soundly in your arms, her breasts pressed against you."
                "her little sleepy noises make you smile as her chest rises and falls."
                "you lightly stroke her bare butt and she makes a soft little moan."
                "you fall asleep without even noticing."
                jump zemday
            "demand sex":


                y "i think we need to go ahead and have some fun."
                m "....."
                m "okay, love. if that's what you want."
                menu:
                    "boob massage":
                        jump zem_boob
                    "sex":

                        jump zem_sex
    else:

        if mai_walk ==2:
            if not start_mai_marriage:
                $ start_mai_marriage = True
                show mai_idle_fl_smile with dissolve
                m "hey, guess what i found!"
                yd "what?"
                m "well... it's broken right now, but... look!"
                show knife_half at truecenter
                with dissolve
                yd "what is that?"
                m "really? you've never seen one of these?"
                m "it's a ceremonial wedding dagger."
                yd "a.... what?"
                m "*sigh...*"
                hide knife_half with dissolve
                y "not everyone is as into knives as you are."
                m "i suppose."
                m "but it's an ancient artifact. it's interesting."
                y "if you say so. what's it's purpose?"
                m "well, you propose marriage with it."
                yd ".....what? how?"
                y "that sounds super violent."
                yd "i thought you gave someone a ring..."
                m "well... it's kind of both."
                m "my understanding is that the knife is to symbolize cutting all past attachments..."
                m "that's why it's for proposals. it's someone relinquishing their past and saying that they want to start anew with you."
                m "rings are given at the actual ceremony, symbolizing unity with the other person."
                m "so... the knife cuts attachments, and the ring makes them whole."
                y "hmmm...."
                m "i can't believe you don't know any of this."
                m "it's incredibly common."
                m "anyway, do you have something on your mind?"
            else:
                m "hello, love."
                m "something on your mind?"

        menu:
            "borrow the broken ceremonial dagger" if start_mai_marriage and not mai_knife:
                y "hey, that knife is really cool -- can i borrow it for a bit?"
                m "sure, but bring it back, okay?"
                y "will do."
                "you got the broken ceremonial wedding dagger!"
                scene black
                scene bg_emberisland_ghosthouse_night
                with dissolve
                "you step outside."
                yd "now how the fuck do i fix this thing?"
                sg "this seems like a job for..."
                yd "who...."
                yc "oh, no."
                show shadyguy_grin with dissolve
                sg "shady!"
                y "what are doing here, man?"
                sg "what are any of us doing here?"
                y "...."
                sg "i planted some drugs behind the shop."
                y "figures."
                y "look, can you fix this dagger?"
                sg "hmm..."
                sg "............."
                sg "yeah, shouldn't be a problem."
                sg "a wedding dagger, eh?"
                y "yeah..."
                sg "tell you what, i'll throw in a ring for free if you let me officiate."
                yd "what?"
                sg "you need someone to officiate your wedding."
                yc "i haven't even decided-"
                sg "oh, come on. you're made for each other. or something."
                sg "look, it's a small island, i'll hear about your proposal.... when you do it."
                sg "let me officiate and i'll take care of the ring and dagger. deal?"
                y "......"
                y "deal."
                sg "great!"
                y "why do you even want to?"
                sg "are you kidding? it's a lifelong dream of mine."
                y "that's a terrible dream."
                sg "what can i say... i'm a sucker for love."
                sg "anyway, i fixed the dagger while you were talking."
                show knife_whole at truecenter
                with dissolve
                "you got the ceremonial wedding dagger!"
                hide knife_whole with dissolve
                yd "h...how?"
                sg "oh, and here's a ring."
                "you got a ring!"
                sg "catch you later!"
                hide shadyguy_grin with dissolve
                y "......"
                y "i might love that bastard."
                $ mai_knife = True
                $ mai_ring = True
                jump zemnight
            "sleep":

                $ randmai = renpy.random.randint(1, 2)
                if randmai ==1:
                    scene black
                    show amsl amsl00
                    with dissolve
                    "she falls asleep immediately."
                    y "you're so damn cute."
                    "she mumbles in her sleep."
                    m "*mmghn....*"
                    y "i guess we'll talk later...."
                    "you lay next to her and she immediately burrows into you, seemingly desperate for your warmth."
                    yd "...why {i}don't{/i} we have blankets?"
                    y "not that i'm complaining."
                    "mai sleeps soundly in your arms, her breasts pressed against you."
                    "her little sleepy noises make you smile as her chest rises and falls."
                    "you lightly stroke her bare butt and she makes a soft little moan."
                    "you fall asleep without even noticing."
                    jump zemday

                if randmai ==2:
                    scene black
                    show amsl amsl28
                    with dissolve
                    y "you're so damn cute."
                    "she mumbles in her sleep."
                    m "*mmghn....*"
                    y "i guess we'll talk later...."
                    "you lay next to her and she immediately burrows into you, seemingly desperate for your warmth."
                    yd "...why {i}don't{/i} we have blankets?"
                    y "not that i'm complaining."
                    "mai sleeps soundly in your arms, her breasts pressed against you."
                    "her little sleepy noises make you smile as her chest rises and falls."
                    "you lightly stroke her bare butt and she makes a soft little moan."
                    "you fall asleep without even noticing."
                    jump zemday
            "boob massage":

                jump zem_boob
            "sex":

                jump zem_sex


label zem_boob:
    y "i was thinking of playing with your tits."
    m "okay."
    m "let me just close up...."
    hide mls with dissolve
    pause 0.5
    show mf with dissolve
    m "there."
    hide mf with dissolve
    show mabo mabo01 with dissolve
    m "....."
    show mabo mabo02
    show mabo_blush
    with dissolve
    m "here."
    show mabo_blink with dissolve
    m "...."
    show mabo mabo03 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "go ahead, love."
    show mabo mabo04
    hide mabo_blink
    hide mabo_blush
    show mabo_surprise
    show mabo_blush
    show mabo_eyesdown
    with dissolve
    m "oh!"
    hide mabo_surprise
    hide mabo_blush
    hide mabo_eyesdown
    show mabo_smile
    show mabo_blush
    show mabo_eyesdown
    show mabo mabo100
    m "mmmmm....."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    hide mabo_eyesdown
    m "having... ah... fun?"
    y "you have the softest tits..."
    hide mabo_smile
    show mabo mabo101
    with Dissolve(0.2)
    m "ohhh... easy..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show mabo_blink with Dissolve(0.2)
    m "ahh..."
    show mabo mabo102
    y "yeah... perfect fucking pillows..."
    m "mmmm...."
    show mabo mabo106
    m "easy, zuko...."
    m "be... be gentle..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    hide mabo_blink
    m "zuko... ah... ah.... you're making me wet..."
    show mabo mabo19
    show mabo_surprise
    show mabo_eyesdownleft
    hide mabo_blush
    show mabo_blush
    with Dissolve(0.35)
    m "ahhh... oh, zuko..."
    show mabo mabo104
    show mabo_surprise
    show mabo_blink
    hide mabo_blush
    show mabo_blush
    with Dissolve(0.35)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "ahh... it feels so nice..."
    hide mabo_blink with Dissolve(0.3)
    m "i'm... oh, i'm wet...."
    hide mabo_surprise
    show mabo_blink
    with Dissolve(0.3)
    m "i'm dripping..."
    y "you're dripping here, too."
    show mabo mabo105
    show mabo_smile
    hide mabo_blush
    show mabo_blush
    with Dissolve(0.3)
    m "nnnghhh.... fuck, zuko...."
    m "mmmmmm...."
    hide mabo_eyesdownleft
    show mabo_eyesdownleft with Dissolve(0.3)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "yes, zuko... baby... suck my tits..."
    m "my breasts are yours..."
    m "oh fuck, i'm fucking wet...."
    m "keep sucking...."
    m "i think... ah... i think i'm going to... ah... cum... zu..."
    m "i'm gonna cum, zuko... i'm gonna cum from you sucking my tits..."
    hide mabo_smile
    show mabo_blink
    hide mabo_eyesdownleft
    with vshake
    m "{size=+4}zuko!!"
    show ctc
    pause
    hide ctc

    show mabo_smile
    show mabo_blush
    show mabo_blink
    with Dissolve(0.3)
    m "thank you..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "okay..."
    m "easy...."
    hide mabo_blink
    show mabo mabo03
    with Dissolve(0.3)
    m "will i see you later?"
    y "of course."
    show mabo mabo01 with Dissolve(0.3)
    play sound "audio/kiss.mp3"
    hide mabo_blush
    show mabo_surprise
    show mabo_blush
    with pflash
    m "mmm!"
    hide mabo_surprise
    show mabo_smile
    hide mabo_blush
    show mabo_blush
    m "that was nice...."
    scene black with dissolve
    if zuko_end:
        jump zcity_night1
    else:
        jump zemday

label zem_sex:
    if maikup_spread and maikup_pussylick and maikup_anallick:
        $ maikup_spread = False
        $ maikup_pussylick = False
        $ maikup_anallick = False
        jump zem_sex2

    scene black
    scene bg_a_armory_1
    show azmu azmu15
    with Dissolve(0.35)

    menu:
        "spread her lips" if not maikup_spread:
            $ maikup_spread = True

            show azmu_pussyclosed
            with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show azmu azmu00 with dissolve
            m "what are you doing back there, zuko?"
            y "just getting a closer look."
            show azmu_pussyopen
            hide azmu_pussyclosed
            show azmu_blink
            with dissolve
            m "ohhh...."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            menu:
                "lick her pussy":
                    show azmu_pussylicking
                    show azmu_surprised with dissolve
                    m "oh!"
                    m "zuko...."
                    hide azmu_blink
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    menu:
                        "lick a little more":

                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            jump zem_sex
                        "back to options":

                            jump zem_sex
                "back to options":

                    jump zem_sex


        "lick her pussy" if not maikup_pussylick:
            $ maikup_pussylick = True
            show azmu_pussylicking
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show azmu azmu00
            show azmu_surprised
            with dissolve
            m "oh!"
            show ctcblink
            $ renpy.pause()
            hide ctcblink

            m "oh, my!"
            hide azmu_surprised
            show azmu_blink
            with dissolve
            m "*mmmmmm*"
            m "i didn't realize i needed a tongue bath."
            hide azmu_blink with dissolve
            m "was i getting messy back there?"
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            menu:
                "lick a little more":
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    jump zem_sex
                "back to options":

                    jump zem_sex


        "lick her ass" if not maikup_anallick:
            $ maikup_anallick = True
            show azmu_pussylicking:
                ypos -130 xpos -10

            show azmu azmu00
            show azmu_surprised
            hide azmu_pussylicking
            show azmu_pussylicking:
                ypos -130 xpos -10
            with dissolve

            m "oh!"
            m "zuko, i don't know if-"
            show azmu_blink
            hide azmu_surprised
            with dissolve
            m "ohhh..."
            m "mmmmmm....."
            hide azmu_blink with dissolve
            m "you're really being... thorough back there."
            m "....don't stop."
            menu:
                "lick a little more":
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    jump zem_sex
                "back to options":
                    jump zem_sex

label zem_sex2:
    scene black
    scene bg_a_armory_1
    show azmu azmu00
    with dissolve
    m "zuko...."
    m "please.... put your cock inside me."
    show azmu azmu01 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "you rest the tip of your cock against her lips."
    m "yes... that's it, baby..."
    yg "you want it? come get it."
    m "*mmmm*"
    m "that's my naughty prince."
    show azmu azmu08 with Dissolve(0.3)
    show azmu azmu02 with Dissolve(0.3)
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    "mai slides a little into your cock, pushing it just past her pussy lips."
    m "is that what you want?"
    y "fuck. yes."
    play sound "audio/gltch2.mp3"
    show azmu azmu03
    with pflash
    m "{i}ohhhh...."
    "with a slow, determined push, mai presses your cock into her hot, welcoming pussy."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "fuck...."
    m "now you stay right there...."
    m "i'm going to do all the work, baby."
    show azmu azmu100
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "i've waited so long for you..."
    m "is it everything you wanted?"
    m "it's better than i dreamed of... and i've been dreaming of this since we were kids."
    show azmu azmu102
    m "i can't believe your perfect, fat cock is inside me."
    m "zuko, i can't...."
    show azmu azmu100_1
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "fuck..."
    m "i need you."
    m "i'm so happy here with you."


    show azmu azmu102_1
    m "i promise to give you anything you need."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "stay with me and i promise to give you whatever you want, whenever you want it."
    m "because...."


    show azmu azmu101
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "i want it, too."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    m "i'm going to take care of you, baby. my poor baby. you have such needs."
    m "i'm here to make them... easier."
    jump zem_sex_menu

label zem_sex_menu:
    m "how do you want it?"
    menu:
        "fast - smooth":
            show azmu azmu100_2
            m "ah, fuck yes baby..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump zem_sex_menu
        "fast - hard":

            show azmu azmu101_1
            m "ah, fuck yes baby..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump zem_sex_menu
        "slow - smooth":

            show azmu azmu100
            m "ah, fuck yes baby..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump zem_sex_menu
        "slow - hard":

            show azmu azmu101_2
            m "ah, fuck yes baby..."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            jump zem_sex_menu
        "cum":

            show azmu azmu100_3

            show ctcblink
            $ renpy.pause()
            hide ctcblink
            m "yes, baby fuck this cunt!"
            m "cum for me!"
            m "i wanna feel your hot load, zuko!"

            menu:
                "cum inside":
                    $ mai_preg = True
                    show azmu azmu06
                    m "yes, nut in me, my prince!"
                    m "empty that fat cock in my hot little pussy!"
                    ya "ngh!"
                    play sound "audio/splurt2.ogg"
                    show azmu_inpussperm1
                    with flash
                    m "oh!"
                    m "it's warm!"
                    play sound "audio/splurt2.ogg"
                    show azmu_inpussperm2
                    hide azmu_inpussperm1
                    with flash
                    m "*mmmmm* yes, zuko, you're doing so good...."
                    m "...don't stop..."
                    ya "fuck!"
                    play sound "audio/splurt3.ogg"
                    show azmu_inpussperm3
                    hide azmu_inpussperm2
                    with flash
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    show azmu azmu00
                    hide azmu_inpussperm3
                    show azmu_inpussperm4
                    show azrr_fertilize
                    with dissolve

                    m "thank you, zuko."
                    m "and i... i'm so happy with you."
                    m "I love you."
                    scene black with dissolve
                    if zuko_end:
                        jump zcity_night1
                    else:
                        scene black with dissolve
                        "you sleep until morning."
                        jump zemday
                "cum outside":

                    show azmu azmu00
                    show azmu_masturbate
                    with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    m "yes, nut on me, my prince!"
                    m "empty that fat cock on my hot little pussy!"
                    ya "ngh!"
                    play sound "audio/splurt2.ogg"
                    show azmu_buttsperm1
                    show azmu_surprised
                    with flash
                    m "oh!"
                    m "it's warm!"
                    play sound "audio/splurt2.ogg"
                    show azmu_buttsperm2
                    hide azmu_buttsperm1
                    hide azmu_surprised
                    with flash
                    m "*mmmmm* yes, zuko, you're doing so good...."
                    m "...don't stop..."
                    ya "fuck!"
                    play sound "audio/splurt3.ogg"
                    show azmu_buttsperm3
                    hide azmu_buttsperm2
                    hide azmu_masturbate
                    with flash
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    m "thank you, zuko."
                    m "and i... i'm so happy with you."
                    m "I love you."
                    scene black with dissolve
                    if zuko_end:
                        jump zcity_night1
                    else:
                        scene black with dissolve
                        "you sleep until morning."
                        jump zemday

label zember_beach2:


















    "you sense a presence, but it seems to be waiting for something."
    jump zemnight

label zember_water2:
    y "no reason to go there."
    jump zemnight

label zember_shack2:
    y "no reason to go there."
    jump zemnight

label zem_ds_talk:
    y "alright, what is it?"
    "{i}go to the other sssside of the island...."
    "{i}i will tell you everything there."
    "the presence seems to disappear."
    $ mai_chosen_end = True
    $ fight_naga = True
    jump fighttest

label mai_marry_begin:
    scene bk2_beach01:
        xpos -1000
    with dissolve
    "you wait at the entrance to the beach, keeping an eye out for mai."
    y "i hope she-"
    show b2ma b2ma01 with dissolve
    "she approaches and your jaw drops."
    show ctc
    pause
    hide ctc
    yc "i...."
    yc "you...."
    show mai_idle_fl_blink with dissolve
    m "i was hoping you'd say that."
    ys "you're beautiful!"
    if mai_preg:
        y "....and pregnant!"
        hide mai_idle_fl_blink with dissolve
        m "oh, is it starting to show?"
        y "....yes!"
        m "well, that's because you came in me, zuko."
        m "what did you think would happen?"
        m "you filled me up, after all."
    if not mai_preg:
        hide mai_idle_fl_blink with dissolve
    m "well... let's go. i believe we have an event to get to."
    show expression "fbackgrounds/bk2_beach01.jpg":
        xpos -1000
        linear 80 xpos 0
        repeat

    show b2ma_blink_ani:
        ypos 7
        linear 1 ypos 0
        linear 1 ypos 7
        repeat
    y "this seems unreal..."
    m "zuko.... my whole life...."
    m "...has been a series of disappointments."
    m "i was born to a wealthy family, but my home life was difficult."
    m "i was never allowed to just be me."
    m "and my best friends are either demanding or attention-stealing."
    y "i'm sorry about that, mai."
    m "no, but... the point i'm trying to make..."
    m "is that i feel like the center of attention with you."
    m "...like i can just be me. like i don't have expectations to meet."
    m "i feel safe. i feel loved. unconditionally."
    m "i just... i think i really found happiness with you."
    y "i feel the same, mai."
    y "i didn't expect this relationship to blossom the way it has... but i can't imagine my life without it."
    m "....thank you, zuko."
    y "thank {i}you{/i}, mai."
    scene black
    scene bk2_beach01

    show b2ma b2ma01
    with Dissolve(2.0)
    m "oh, it looks like we're here."
    m "ready?"
    y "...as i'll ever be."
    scene black
    hide b2ma b2ma01
    scene bg_maiend_beach1
    show b2sh_lectern
    with dissolve
    show b2ma b2ma01 with dissolve
    "mai steps up next to you delicately."
    m "this is perfect. on the beach and under an umbrella!"
    yd "where's-"
    hide b2sh_lectern
    show b2sh b2sh01
    show b2sh_lectern
    with dissolve
    sg "i'm here, i'm here!"
    sg "don't start without me!"
    yd "we... can't..."
    sg "oh, good."
    sg "is everyone here?"
    y "what are you talking about? there's-"
    "you turn around and notice a few strangers have wandered up to watch the ceremony."
    y "huh."
    y "yeahh... i think we're good to go."
    sg "very well."
    sg "we're gathered here today-"
    sg "oh, hey, anybody wanna buy a watch?"
    hide b2sh_lectern
    show b2sh b2sh03
    show b2sh_lectern
    with dissolve
    sg "anybody? no? alright..."
    sg "...to celebrate the union of-"
    show b2sh_annoyed with dissolve
    sg "you know what, i can't handle this lectern."
    sg "hold on."
    hide b2sh_lectern
    show flying_lectern at speedycard
    with vshake
    "shady kicks the lectern away."
    yd "....."
    yd "um... is it supposed to do that?"
    sg "no."
    ys "i kind of like it."
    m "it's... a little distracting."
    sg "hold on, hold on...."
    hide flying_lectern with moveoutright
    hide b2sh_annoyed
    show b2sh b2sh01
    with dissolve
    sg "better."
    sg "anyway, the union of-"
    show b2sh b2sh02 with dissolve
    sg "you! hey, you! in the back! don't i know you?"
    sg "yeah, you're that pervert that keeps slapping my slave girl's tits."
    sg "you keep that up and i'm gonna shit in your eyes!"
    sg "that's right, you better run!"
    show b2sh b2sh03 with dissolve
    sg "...union between zuko and mai."
    sg "you'll now recite your own vows."
    show b2ma b2ma02 with dissolve
    m "zuko, my love. my one truth."
    m "i vow to always be by your side."
    m "i vow to never intentionally hurt you."
    m "this i swear."
    show b2sh_tears with dissolve
    sg "buh... buh... baaaaahhhhhh!!"
    yd "what?"
    sg "it's so beautiful!!!"
    sg "....sniff...."
    sg "and your vows?"
    y "mai, you are my...."
    menu:
        "bacon":
            y "....bacon. you're perfect."
        "salvation":

            y "....everything. my saving grace."

    y "i vow to always..."
    menu:
        "put you first":
            y "...put your needs above my own."
        "use the shitty generic controller so that you can have the name brand one that actually works and doesn't have buttons that stick or are off-center":

            y "...give you the good controller."

    y "i vow to never..."
    menu:
        "take one of your bagel bites unless you're cool with it or not looking":
            y "...take your snacks."
            y "though you should probably make an extra 1-3 so we can both be happy."
        "let you feel unwanted":

            y "...let you feel unloved."

    y "this i swear."
    sg "hot shit, gang."
    sg "just the hottest."
    sg "now for the ring..."
    show b2ma b2ma03 with dissolve
    sg "put the ring on her {b}hand{/b} whenever you're ready, son."
    call screen mai_ring_select

label mai_ring_on:
    show b2ma b2ma04 with dissolve
    sg "well done."
    sg "now for the knife."
    yc "what... do i do with it?"
    sg "seriously?"
    show b2ma b2ma01 with dissolve
    m "you cut off my dress, zuko."
    yd "....are you serious?"
    m "of course!"
    m "and then i'll cut off your clothes."
    yd "...why?"
    m "to be naked before one another."
    y "fine...."
    yc "careful.... careful...."

    show b2ma b2ma05 with dissolve
    "mai's clothes split and drop to the floor."
    show ctc
    pause
    hide ctc
    m "now for yours."
    yc "aw man... i liked these pants."
    yc "they're the only ones i own."
    with vshake
    "mai slices off your clothing with quick precision."
    y "remind me to never get on your bad side when there are knives around."
    m "don't worry... i will."
    sg "well, by the power vested in me by two old witches that live in the shack on the dock and seem to run everything..."
    sg "i now pronounce you husband and wife!"
    sg "you may now fuck the bride!"
    y "grea-"
    yd "what."
    m "we consumate our love, zuko."
    m "you really don't know anything."
    yd "uh. here? in public?"
    m "there are only a few stragglers. it's normal."
    yd "......."
    yd "well, a man's gotta do what a man's gotta do...."
    scene black with dissolve
    show bg_maiend_beach2
    show b2ma b2ma07
    with dissolve
    show ctc
    pause
    hide ctc
    m "my pussy is your responsibility now, zuko."
    m "you have to beat it, take care of it.... {i}own{/i} it. starting now."
    show b2ma b2ma08 with dissolve
    show ctc
    pause
    hide ctc
    m "don't be shy, husband."
    y "one thing i'm not is shy."
    show b2ma b2ma09 with dissolve
    m "mmm... that's my big, thick, man."
    m "give me your love."
    show b2ma b2ma11 with dissolve
    m "yes...."
    show b2ma b2ma100
    show ctc
    pause
    hide ctc
    m "yes, zuko... make love to me..."
    m "make me yours, forever and always..."
    m "i'll be-"
    show b2ma b2ma101
    m "oh!"
    m "getting a little rougher, i see...."
    show ctc
    pause
    hide ctc
    m "ngh! ah!"
    m "i'll be your partner, your sex toy, your-"
    show b2ma b2ma102
    show b2ma_blink with dissolve
    show ctc
    pause
    hide ctc
    m "ah... ah... maid... ah... fuck... ah..."
    m "....friend....ah...."
    hide b2ma_blink with dissolve
    show b2ma b2ma104
    show ctc
    pause
    hide ctc
    m "f...fuck...."
    m "yes..."
    m "oh, zuko....."
    m "harder... harder..."
    show b2ma b2ma103
    show ctc
    pause
    hide ctc
    m "yes... yes... fuck me! fuck me, zuko!"
    m "fuck me, husband!"
    ya "i'm cumming, wife!"
    m "cum, husband! cum!"
    m "mark me!"
    m "let them all know i'm taken!"
    show ctc
    pause
    hide ctc
    m "take me!"
    menu:
        "cum inside":
            if not mai_preg:
                play sound "audio/splurt2.ogg"
                show b2ma b2ma17
                with flash
                m "yes!"
                play sound "audio/splurt1.ogg"
                with flash
                ya "take my jizz, wife!"
                m "please!"
                play sound "audio/splurt1.ogg"
                with flash
                m "ohh...."
                show b2ma b2ma09
                show azrr_fertilize
                show b2ma_sperm4
                with flash
                show ctc
                pause
                hide ctc
                m "oh, zuko...."
            else:
                play sound "audio/splurt2.ogg"
                show b2ma b2ma17
                with flash
                m "yes!"
                play sound "audio/splurt1.ogg"
                with flash
                ya "take my jizz, wife!"
                m "please!"
                play sound "audio/splurt1.ogg"
                with flash
                m "ohh...."
                show b2ma b2ma09
                show b2ma_sperm4
                with flash
                show ctc
                pause
                hide ctc
                m "oh, zuko...."
        "cum outside":

            show b2ma b2ma09 with Dissolve(0.2)
            play sound "audio/splurt2.ogg"
            show b2ma_spermshot
            $ renpy.pause(0.3)
            hide b2ma_spermshot
            show b2ma_sperm1
            show ctc
            pause
            hide ctc
            m "mmmm...."
            play sound "audio/splurt3.ogg"
            show b2ma_spermshot
            $ renpy.pause(0.3)
            hide b2ma_spermshot
            show b2ma_sperm2
            show ctc
            pause
            hide ctc
            ya "take my jizz, wife!"
            m "please!"
            hide b2ma_sperm1
            play sound "audio/splurt2.ogg"
            show b2ma_spermshot
            $ renpy.pause(0.3)
            hide b2ma_spermshot
            show b2ma_sperm3
            show ctc
            pause
            hide ctc
            m "ohh...."
            hide b2ma_sperm2
            show ctc
            pause
            hide ctc
    play sound "audio/applause.mp3"
    "there's a very polite burst of applause that takes you by surprise."
    y "i... forgot that there were people there...."
    m "you did very well, hunny."
    m "walking is going to... be difficult."
    scene black with dissolve
    scene bg_maiend_beach1
    show b2ma b2ma05
    with dissolve
    y "well, that was something."
    show b2sh b2sh01
    show b2sh_tears
    with dissolve
    sg "just wonderful. really inspiring."
    ya "would you get out of here?"
    yd "and stop crying."
    hide b2sh_tears
    show b2sh_annoyed
    show b2sh_tears
    with dissolve
    sg "let me feel my feelings!"
    ya "no!"
    m "that's alright, shady. we're going."
    m "thank you for your help."
    hide b2sh_annoyed
    hide b2sh_tears
    with dissolve
    sg "anytime."
    scene black with dissolve
    scene bk2_beach01:
        xpos -1000
    with dissolve
    show expression "fbackgrounds/bk2_beach01.jpg":
        xpos -1000
        linear 80 xpos 0
        repeat

    show b2ma b2ma05:
        ypos 7
        linear 1 ypos 0
        linear 1 ypos 7
        repeat
    with dissolve
    m "well... what would you like to do now?"
    y "whatever you want."
    m "hmm.... whatever i want?"
    y "always."
    m "well... if you think you can go again..."
    $ renpy.pause(1.0)
    play sound "audio/hiss.wav"
    show flyby at right
    with moveinright
    hide flyby with moveoutleft
    with sshake
    play sound "audio/hiss.wav"
    ds "*hss!*"
    scene black
    scene bk2_beach01
    show b2ma b2ma05
    show mai_idle_fl_angry
    with dissolve
    m "what was that!?"
    ya "I'm not sure...."
    ds "avatar!"
    ds "i will wait no longer!"
    ya "stand back, mai!"
    m "i can help..."
    ya "no! this has to be me.... i can't explain why, but i know it..."
    play sound "audio/hiss.wav"
    ds "*hss!*"
    hide b2ma b2ma05
    hide mai_idle_fl_angry
    with sshake
    "mai is knocked unconscious."
    $ fight_naga = True
    jump fighttest



"test"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
