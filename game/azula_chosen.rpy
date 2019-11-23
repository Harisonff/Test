label zffight_day20:
    if azula_chosen_end:
        jump zuko_ds_battle

    if not flynn_bradsley:
        $ flynn_bradsley = True
        g1 "you're right, that's {i}not{/i} normal."
        g2 "i told you!"
        g1 "can you... put it away, now?"
        g1 "super weird for a shift."
        g2 "what? we're buds."
        g1 "yeah, but... how did you even get burns there?"
        g2 "the new firebending brothel."
        g1 "the what?"
        g2 "they have super warm-"
        g1 "i get it, i get it."
        g1 "look, just... stop whipping it out."
        g2 "come on, we should get in some sword practice."
        g1 "finally, yes, i'll get our blades-"
        g2 "that's not what i meant."
        g1 "oh, god dammit!"
        g1 "no! stop showing me your fucking co-"
        y "hey, can one of you guys unlock the gate for-"
        yd "huh."
        yd "that's... not normal."
        g2 "right!?"
        g1 "put it away!"
        g2 "who's gonna mess with us with our dicks out?"
        yd "not me."
        g1 "especially not with that weird thing."
        g1 "it's blinking at me."
        g2 "aw, don't be mean to it."
        g2 "i'm gonna name it!"
        g1 "don't name it."
        g2 "i'm gonna."
        g1 "don't-"
        g2 "how about..."
        g1 "I'm begging you, here."
        g2 "i'm gonna name him... flynn bradsley."
        g1 "............."
        g1 "....why??"
        g2 "it invokes valor and bravery."
        g1 "why would you even want that? just get rid of it!"
        g2 "i'm not getting rid of flynn bradsley!"
        g2 "you're heartless!"
        g1 "it's literally blinking at me!"
        g2 "are you sure we shouldn't keep it?"
        g1 "what? it's yours!"
        g2 "it's ours!"
        g1 "i don't want it!"
        g2 "shhh.... don't let him hear you say that, you'll hurt his feelings."
        g1 "you're fucking mental."
        g2 "apologize. apologize to flynn bradsley."
        g1 "I'm not apologizing to your dick!"
        g2 "it's not my dick! it's what's growing {i}on{/i} my dick."
        g1 "still not apologizing."
        g2 "aw."
        yd "i'm... gonna just go, now."
        g1 "...take me with you."
        g2 "flynn says bye!"
        jump zaday
    else:

        g1 "look, i'm just saying if you don't feed it properly, it's gonna get sick and-"
        g2 "are you saying that flynn bradsley is malnourished?"
        g1 "no, no, i'm not blaming anyone, i just worry about it-"
        g2 "he's not an \"it\", he's a \"he\"."
        g1 "right, whatever, i just haven't had a pet before and i'm... a little anxious."
        g2 "well, i haven't had a pet that grew out of my dick before, but i had a koala-seal, and i... did not do a good job."
        g2 "what fucking environment can that live in?"
        g2 "...but i know what i'm doing here. i think."
        g1 "is it... sorry, is {i}he{/i}... getting lots of veggies?"
        yd "....okay, i'm not doing this."
        g2 "he likes bananas."
        g2 "and being choked."
        y "yup, nope, i'm out."
        jump zaday


label zfpalace_day20:
    if azula_chosen_end:
        y "i should leave the city."
        jump zaday

    if not az_happy_scene:
        $ az_happy_scene = True
        scene bg_a_smallpalaceroom
        show a_blink
        with dissolve
        a "hey, you."
        y "hey."
        a "i'm...."
        show au
        hide a_blink
        with dissolve
        "azula looks around uncertainly."
        "confirming the two of you are in private, she sighs."
        show aue
        hide au
        with dissolve
        a "i'm having a very stressful day."
        yd "what's wrong?"
        a "......"
        show au
        hide aue
        with dissolve
        a "....i feel so relaxed with you, brother."
        a "this is the relationship we were meant to have...."
        y "is that so?"
        show ae
        hide au
        with dissolve
        a "i'm finally firelord. i can hardly believe it."
        a "so we know i'm the stronger one.... you've accepted that..."
        a "but.... even though I know you're loyal to me...."
        show au
        hide ae
        with dissolve
        a "it's hard for me to be vulnerable with you."
        y "try."
        show aue
        hide au
        with dissolve
        a "i....."
        a "......"
        show au
        hide aue
        with dissolve
        a "i let a peasant off easy!"
        a "i let him off with a warning!"
        a "what's wrong with me?"
        ys "....are you serious? {i}that's{/i} what's bothering you?"
        a "well... yes."
        y "there's nothing wrong with you, babe."
        a "what? of course there is. i've never-"
        y "you're happy. that's all. you're not so obsessed with making people miserable."
        hide au with dissolve
        show alu with dissolve
        a "and this is normal?"
        y "yes!"
        a "oh."
        y "and you might find that people come to love you for being nice."
        a "they don't love me?"
        yc "i mean... they'll love you {i}more{/i}."
        a "....okay."
        show ala
        hide alu
        with dissolve
        a "but you can't tell anyone about this!"
        ys "don't worry, i won't share that you're a big softie."
        show al_blink
        hide ala
        with dissolve
        a "well, i feel better."
        y "good!"
        a "but i still need some.... stress relief."
        y "can i help?"
        hide al_blink with dissolve
        show a_blink
        with dissolve
        a "oh, yes."
        a "we're going to...."
        $ rand_azsex = renpy.random.randint(1, 6)
        if rand_azsex ==1:
            a "jack you off."
            a "i want to grip that big cock of yours."
        if rand_azsex ==2:
            a "i'm going to take a shower.... and you're going to watch."
        if rand_azsex ==3:
            a "you're going to lick me."
        if rand_azsex ==4:
            a "i'm going to suck your cock."
        if rand_azsex ==5:
            a "you're going to fuck my ass."
        if rand_azsex ==6:
            a "we're going to have sex, brother."

        menu:
            "accept":
                if rand_azsex ==1:
                    jump za_handjob
                if rand_azsex ==2:
                    jump za_shower
                if rand_azsex ==3:
                    jump zazula_piss
                if rand_azsex ==4:
                    jump za_blowjob
                if rand_azsex ==5:
                    jump za_anal
                if rand_azsex ==6:
                    jump za_sex
            "argue":


                y "no, we're going to do what i want."
                a "you can't-"
                y "quiet!"
                a "mmmmm....."
                menu:
                    "handjob":
                        y "jack me off!"
                        jump za_handjob
                    "shower":

                        y "i can't think of anything. why don't you just go relax? have a hot shower or something?"
                        a "hmmm.... honestly a hot shower sounds nice...."
                        jump za_shower
                    "lick/piss":

                        jump zazula_piss
                    "blowjob":
                        y "come suck my cock."
                        a "of course, brother."
                        jump za_blowjob
                    "anal":
                        jump za_anal
                    "sex":
                        jump za_sex
    else:



        scene bg_a_smallpalaceroom
        show a_blink
        with dissolve
        a "hello, zuzu."
        if rei_gone and not rei_resolved:
            $ rei_resolved = True
            ya "did you get rid of Rei?"
            a "who?"
            ya "the one-eyed captain?"
            ya "and i don't mean my dick!"
            ya "although that's a great fucking name!"
            ya "dibs!"
            a "ohh... yes, i got rid of her."
            ya "what did you do with her?"
            a "relax. she's been assigned to clean up the earthbender issue."
            yd "really? where?"
            a "i really don't remember. she's a captain, don't forget -- she's under the command of another general."
            yd "......"
            a "what?"
            yd "i'm just.... surprised she's alive. that doesn't really seem like you."
            a "well, of course i had to get rid of her. she'd been scheming to destroy us."
            a "but there's no sense wasting potential like that."
            ys "....."
            a "what now?"
            ys "that was.... sensible."
            ys "are you getting softer?"
            hide a_blink with dissolve
            show ala with dissolve
            a "absolutely not!"
            ys "sure...."
            show ale
            hide ala
            with dissolve
            a "well......."
            hide ale with dissolve
            show a_blink with dissolve
            a "now that that's out of the way, i need some relief."
            a "we're going to...."
            $ rand_azsex = renpy.random.randint(1, 6)
            if rand_azsex ==1:
                a "jack you off."
                a "i want to grip that big cock of yours."
            if rand_azsex ==2:
                a "i'm going to take a shower.... and you're going to watch."
            if rand_azsex ==3:
                a "you're going to lick me."
            if rand_azsex ==4:
                a "i'm going to suck your cock."
            if rand_azsex ==5:
                a "you're going to fuck my ass."
            if rand_azsex ==6:
                a "we're going to have sex, brother."

            menu:
                "accept":
                    if rand_azsex ==1:
                        jump za_handjob
                    if rand_azsex ==2:
                        jump za_shower
                    if rand_azsex ==3:
                        jump zazula_piss
                    if rand_azsex ==4:
                        jump za_blowjob
                    if rand_azsex ==5:
                        jump za_anal
                    if rand_azsex ==6:
                        jump za_sex
                "argue":


                    y "no, we're going to do what i want."
                    a "you can't-"
                    y "quiet!"
                    a "mmmmm....."
                    menu:
                        "handjob":
                            y "jack me off!"
                            jump za_handjob
                        "shower":

                            y "i can't think of anything. why don't you just go relax? have a hot shower or something?"
                            a "hmmm.... honestly a hot shower sounds nice...."
                            jump za_shower
                        "lick/piss":

                            jump zazula_piss
                        "blowjob":
                            y "come suck my cock."
                            a "of course, brother."
                            jump za_blowjob
                        "anal":
                            jump za_anal
                        "sex":
                            jump za_sex
        else:

            $ az_news = renpy.random.randint(1, 2)
            if az_news ==1:
                a "running a nation continues to be difficult."
                a "you'd know that if you were in charge."
                yd "wow. fucking rude."
                a "aw, don't make that face. you know you're my second in command."
                a "besides, i treat you well, don't i?"
                a "i hope you know how much i need you."
                a "for example, right now i want your cum."
                a "come to me, give me what i need. i promise to drain you dry."
                a "we're going to...."
                $ rand_azsex = renpy.random.randint(1, 6)
                if rand_azsex ==1:
                    a "jack you off."
                    a "i want to grip that big cock of yours."
                if rand_azsex ==2:
                    a "i'm going to take a shower.... and you're going to watch."
                if rand_azsex ==3:
                    a "you're going to lick me."
                if rand_azsex ==4:
                    a "i'm going to suck your cock."
                if rand_azsex ==5:
                    a "you're going to fuck my ass."
                if rand_azsex ==6:
                    a "we're going to have sex, brother."

                menu:
                    "accept":
                        if rand_azsex ==1:
                            jump za_handjob
                        if rand_azsex ==2:
                            jump za_shower
                        if rand_azsex ==3:
                            jump zazula_piss
                        if rand_azsex ==4:
                            jump za_blowjob
                        if rand_azsex ==5:
                            jump za_anal
                        if rand_azsex ==6:
                            jump za_sex
                    "argue":


                        y "no, we're going to do what i want."
                        a "you can't-"
                        y "quiet!"
                        a "mmmmm....."
                        menu:
                            "handjob":
                                y "jack me off!"
                                jump za_handjob
                            "shower":

                                y "i can't think of anything. why don't you just go relax? have a hot shower or something?"
                                a "hmmm.... honestly a hot shower sounds nice...."
                                jump za_shower
                            "lick/piss":

                                jump zazula_piss
                            "blowjob":
                                y "come suck my cock."
                                a "of course, brother."
                                jump za_blowjob
                            "anal":
                                jump za_anal
                            "sex":
                                show aa
                                hide a_blink
                                with dissolve
                                a "you really think you can put your thick, smelly cock in firelord azula?"
                                y "yeah."
                                show a_blink
                                hide aa
                                with dissolve
                                a "mmmm.... then let me have it, brother."
                                jump za_sex

            if az_news ==2:
                show ad
                hide a_blink
                with dissolve
                a "those peasants are dreadful."
                yd "what happened?"
                a "they were complaining about being hungry or some nonsense."
                yc "what.... did you do?"
                a "i simply have no patience for that...."
                a "so i gave them some of our extra food."
                show ae
                hide ad
                with dissolve
                a "hopefully they won't bother us anymore."
                yd "....."
                ys "you were nice!"
                a "oh, shut up."
                show a_blink
                hide ae
                with dissolve
                a "now.... i want your cum."
                a "come to me, give me what i need..... i promise to empty your balls."
                $ rand_azsex = renpy.random.randint(1, 6)
                if rand_azsex ==1:
                    a "jack you off."
                    a "i want to grip that big cock of yours."
                if rand_azsex ==2:
                    a "i'm going to take a shower.... and you're going to watch."
                if rand_azsex ==3:
                    a "you're going to lick me."
                if rand_azsex ==4:
                    a "i'm going to suck your cock."
                if rand_azsex ==5:
                    a "you're going to fuck my ass."
                if rand_azsex ==6:
                    a "we're going to have sex, brother."

                menu:
                    "accept":
                        if rand_azsex ==1:
                            jump za_handjob
                        if rand_azsex ==2:
                            jump za_shower
                        if rand_azsex ==3:
                            jump zazula_piss
                        if rand_azsex ==4:
                            jump za_blowjob
                        if rand_azsex ==5:
                            jump za_anal
                        if rand_azsex ==6:
                            jump za_sex
                    "argue":


                        y "no, we're going to do what i want."
                        a "you can't-"
                        y "quiet!"
                        a "mmmmm....."
                        menu:
                            "handjob":
                                y "jack me off!"
                                jump za_handjob
                            "shower":

                                y "i can't think of anything. why don't you just go relax? have a hot shower or something?"
                                a "hmmm.... honestly a hot shower sounds nice...."
                                jump za_shower
                            "lick/piss":

                                jump zazula_piss
                            "blowjob":
                                y "come suck my cock."
                                a "of course, brother."
                                jump za_blowjob
                            "anal":
                                jump za_anal
                            "sex":
                                show aa
                                hide a_blink
                                with dissolve
                                a "you really think you can put your thick, smelly cock in firelord azula?"
                                y "yeah."
                                show a_blink
                                hide aa
                                with dissolve
                                a "mmmm.... then let me have it, brother."
                                jump za_sex

label az_chose_sex_menu:


    menu:
        "handjob":
            y "how about a handy?"
            jump za_handjob
        "shower":
            y "i can't think of anything. why don't you just go relax? have a hot shower or something?"
            a "hmmm.... honestly a hot shower sounds nice...."
            jump za_shower
        "lick/piss":
            jump zazula_piss
        "blowjob":
            y "wanna suck my dick?"
            a "of course, brother."
            jump za_blowjob
        "anal":
            jump za_anal
        "sex":
            jump za_sex
        "back":
            jump az_chose_sex_menu
        "exit":










            jump zaday

label za_handjob:
    a "very well."
    a "i'll send mai on an errand for today..."
    a "so i can make you make a mess in her shop."
    a "how's that sound?"
    yc "um-"
    a "it's decided."
    scene black with dissolve
    "you enter the armory with azula, and find it empty."
    "azula pushes you into a chair."
    scene bg_a_armory
    show ahj7_1
    with dissolve
    a "ah, yes... this magnificent cock. truly fit for a queen."
    a "i... i almost can't stand to wait."
    scene black with dissolve
    "azula pulls down your pants and settles between your legs."
    scene bg_a_armory
    show azhj azhj13
    with dissolve
    a "let's make you cum."
    show azhj azhj01 with dissolve
    a "now, pull it out!"
    show azhj azhj03 with dissolve
    a "my, my."
    a "i never get tired of seeing your cock, brother."
    a "what do you think... should i give you a little tug?"
    show azhj azhj04 with dissolve
    a "well, that didn't take much encouragement."
    a "have you been hoping i'd feel up your cock again?"
    show azhj azhj05 with Dissolve(0.35)
    a "i can't believe you're such a pervert, zuko."
    a "i didn't expect it."
    show azhj azhj08 with Dissolve(0.35)
    a "i almost can't get my hand around it."
    a "is this what you want, you sicko?"
    a "for me to grip your big, handsome cock?"
    show azhj azhj09 with Dissolve(0.35)
    a "i can't believe you."
    show azhj azhj101 with Dissolve(0.35)
    yc "ungh..."
    show azhj azhj105_1 with Dissolve(0.35)
    a "mmm..."
    a "what's wrong, brother?"
    show azhj azhj100 with Dissolve(0.35)
    ya "fuck!"
    a "aw, you're cute when you watch your little sister tug on your cock."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yc "ngh..."
    yc "you're jacking me off... in mai's shop... i still can't believe this is happening..."
    show azhj_blink with Dissolve(0.35)
    a "hm."
    a "you can't?"
    a "why not?"
    y "well, because, you're my sister."
    show azhj_blush
    hide azhj_blink
    with dissolve
    a "...do you think i'm beautiful?"
    menu:
        "yes":
            y "i think you're gorgeous."
            show azhj_blink with dissolve
            a "oh."
            a "i've always... been fascinated with you, zuzu."
            a "I know i can be difficult."
            show azhj_lusty with dissolve
            a "but the truth is, these years you've been away..."
            a "i swore that, well..."
            a "if you came back..."
            show azhj_eyesoncock
            hide azhj_blink
            hide azhj_lusty
            with dissolve
            a "i'd do something about it."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
        "mostly scary":


            yd "more terrifying than anything."
            show azhj_eyesoncock
            a "that's what everyone thinks, i know it."
            a "they're all afraid of me..."
            show azhj_angry
            hide azhj_eyesoncock
            with Dissolve(0.35)
            a "...and they should be!"
            hide azhj_angry
            show azhj_eyesoncock
            with Dissolve(0.35)
            a "but i do wish..."
            a "........."


    a "...they're all too scared to get close to me."
    hide azhj_eyesoncock
    with Dissolve(0.35)
    a "you're scared too, i know it."
    hide azhj_blush
    show azhj_angry
    show azhj_blush
    with Dissolve(0.35)
    a "and if i have to rule with fear, then i will."
    a "i don't have to be gentle."
    show azhj azhj21
    hide azhj_angry
    hide azhj_blush
    with Dissolve(0.35)
    a "here."
    play sound "audio/fleshslap.mp3"
    show azhj azhj17 with vshake
    a "see?"
    a "did you like that?"
    a "here-"
    show azhj azhj105_2
    a "ah... ah... mm..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "do... ah... you like... this?"
    a "slapping... ah... your cock on my... ah... face?"
    a "your little... ah... sister's face?"
    show azhj azhj17 with Dissolve(0.35)
    a "want me to rub it on my face, brother?"
    show azhj azhj105_3
    a "mmmm...."
    a "how is it?"
    yc "ngh... your face is really soft..."
    a "i know."
    yc "ah..."
    a "your cock is so hot on my face."
    a "see, i can be gentle, too."
    yc "hngh..."
    a "oh no brother, what's wrong? you're not going to make a mess, are you?"
    show azhj azhj103 with dissolve
    "azula leans in close to you. you can feel her breath in your ear as her lips lightly brush against you."
    "her tongue flickers in for a moment as she speaks."
    show azhj azhj105
    a "cum for me, brother. make a fucking mess. i want it all over my hands, understand?"
    a "i want to see what you can do. i want to smell my brother's cum on my hands."
    a "do it."
    a "give me that fucking sperm, brother!"
    "azula gives your earlobe one long suck, her soft, succulent lips slowly tugging at your ear as her tongue briefly runs against you."
    show azhj azhj106
    "Her lips pull off with a small \"pop\" and she begins jacking your cock ferociously, forcing the cum out almost against your wishes."
    a "you gonna cum, brother?"
    a "am i making you cum?"
    a "are you gonna make a big, sticky mess that mai has to clean up?"
    show azhj azhj107 with Dissolve(0.3)
    a "is she gonna have to clean up all the cum?"
    a "cum for me. cum for me."
    show azhj_angry with Dissolve(0.3)
    a "cumformecumformecumforme-"
    yc "hgh-"
    show azhj azhj05
    show azhj_surprised
    hide azhj_angry
    show azhj_sperm_1
    play sound "audio/splurt3.ogg"
    with flash
    a "oh!"
    hide azhj_surprised
    hide azhj_sperm_1
    show azhj_lusty
    show azhj_eyesoncock
    show azhj_sperm_2
    play sound "audio/splurt2.ogg"
    with flash
    a "ahh...."
    a "yes..."
    hide azhj_lusty
    hide azhj_eyesoncock
    hide azhj_sperm_2
    show azhj_blush
    show azhj_sperm_3
    play sound "audio/splurt1.ogg"
    with flash
    a "get it all out, zuko..."
    yc "ungh..."
    show azhj_blink
    show azhj_sperm_1 at Position (xpos = 0.32, xanchor=0.5, ypos=0.53, yanchor=0.5)
    show azhj_sperm_2 at Position (xpos = 0.38, xanchor=0.5, ypos=0.45, yanchor=0.5)
    play sound "audio/splurt2.ogg"
    with flash
    a "mmmm...."
    hide azhj_blink with Dissolve(0.25)
    a "feel better?"
    y "fuck. yes."
    a "did i get it all out?"
    yc "unghh..."
    show azhj_lusty
    show azhj_blink
    hide azhj_sperm_1
    hide azhj_sperm_2
    show azhj_sperm_1 at Position (xpos = 0.32, xanchor=0.5, ypos=0.53, yanchor=0.5)
    show azhj_sperm_2 at Position (xpos = 0.38, xanchor=0.5, ypos=0.45, yanchor=0.5)
    with Dissolve(0.25)
    a "good."
    a "now..."
    hide azhj_lusty
    hide azhj_blush
    show azhj_blush at Position (xpos = 0.54, xanchor=0.5, ypos=0.48, yanchor=0.5)
    hide azhj_blink
    show azhj azhj17

    hide azhj_sperm_1
    hide azhj_sperm_2
    show azhj_sperm_1 at Position (xpos = 0.36, xanchor=0.5, ypos=0.498, yanchor=0.5)
    show azhj_sperm_2 at Position (xpos = 0.43, xanchor=0.5, ypos=0.435, yanchor=0.5)

    with Dissolve(0.25)
    a "that was fun."
    a "now, put your clothes on."
    a "i need to clean my hands."
    show azhj azhj15
    hide azhj_sperm_3
    show azhj_sperm_3 at Position (xpos = 0.57, xanchor=0.5, ypos=1.02, yanchor=0.5)
    with Dissolve(0.25)
    y "and your face."
    a "oh, is there something on my face, zuzu?"
    y "yeah, my cum."
    a "on my face."
    y "...yes."
    a "then why ever would i wash it off?"
    scene black
    scene bg_a_armory
    show afnj
    with dissolve
    a "go ahead, zuko. i'll meet you in the palace later."
    if zuko_end:
        jump zcity_night1
    else:
        jump zanight

label za_shower:
    show azsh azsh112
    show azsh_water
    with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yg "damn...."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show azsh azsh110 with dissolve
    a "*mmmmm...*"
    a "*ah*...*ah*..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    yg "that's it, sis..."
    a "*mmm*...*ah*...*yes*...."
    show azsh azsh111
    a "zuzu... are you spying again?"
    yc "ah! uh. i..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show azsh azsh112 with dissolve
    a "such a pest."
    a "come on in, brother."
    show azsh azsh113 with dissolve
    a "it's not like i've never seen you naked."
    show azsh azsh112 with dissolve
    a "take a seat."
    show azsh azsh110 with dissolve
    a "sit down, you pervert."
    show azsh azsh100
    show azsh_doubt
    with dissolve
    a "poor zuko..."
    a "you don't know women's bodies at all, do you?"
    hide azsh_doubt with dissolve
    a "*mmmmm...*"
    y "you seem to be really enjoying that..."
    show azsh azsh102
    show azsh_lusty
    with dissolve
    a "nonsense, i'm just making sure i'm perfectly clean."
    show azsh_doubt with dissolve
    a "well... let me teach you a bit about our bodies."
    hide azsh_lusty
    show azsh_neutral with dissolve
    a "these are breasts, obviously."
    hide azsh_doubt
    y "why are you... showing me?"
    show azsh_doubt with dissolve
    a "you're clearly struggling. why wouldn't i try to help you?"
    hide azsh_neutral
    a "I'm your sister, after all."
    yd "i guess..."
    hide azsh_doubt with dissolve
    show azsh azsh101 with dissolve
    a "and this is a vagina..."
    show azsh_eyesopen
    show azsh_lusty
    with dissolve
    a "want a closer look?"
    a "just between siblings?"
    menu:
        "show me!":
            show azsh azsh11 with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            a "why don't you take out your cock?"
            yd "what?"
            a "well... it seems only fair that i get to look at you... while you look at me."
            yd "....."
            show az_mastufbate_1flip at Position (xpos = 0.65, xanchor=0.5, ypos=.5, yanchor=0.5)
            with dissolve
            a "oh... zuzu... that's... large."
            yd "really?"
            a "would you... rub it a bit?"
            a "here, we'll do it... together...."
            show azsh azsh101 with dissolve
            a "like this...."
            show azsh_mastufbate_1flip at Position (xpos = 0.65, xanchor=0.5, ypos=.5, yanchor=0.5)
            hide az_mastufbate_1flip
            a "yes..."
            a "just like that...."
            a "oh! oh, brother!"
            hide azsh_eyesopen
            hide azsh_lusty
            a "brother i'm going to... to cum..."
            show azsh_lusty
            show azsh azsh11
            hide azsh_mastufbate_1flip
            with vshake
            a "ahhh!!"
            a "mmmmmmmmm......"
            show azsh_doubt
            hide azsh_lusty
            with dissolve
            a "why did you stop?"
            a "keep going."
            y "...."
            show azsh_mastufbate_1flip at Position (xpos = 0.65, xanchor=0.5, ypos=.5, yanchor=0.5)
            hide azsh_doubt
            show azsh_eyesopen
            with dissolve
            a "just like that, zuko..."
            y "i'm... i'm..."
            show azsh_lusty with dissolve
            a "yes, brother! let me see it!"
            play sound "audio/splurt3.ogg"
            show a_mindbreak_spermoutside_1 at Position (xpos = 0.5, xanchor=0.5, ypos=.47, yanchor=0.5)
            with flash
            ya "ughh..."
            play sound "audio/splurt2.ogg"
            show a_mindbreak_spermoutside_2 at Position (xpos = 0.5, xanchor=0.5, ypos=.47, yanchor=0.5)
            with flash
            a "oh!"
            play sound "audio/splurt1.ogg"
            hide azsh_mastufbate_1flip
            show a_mindbreak_spermoutside_3 at Position (xpos = 0.5, xanchor=0.5, ypos=.47, yanchor=0.5)
            with flash
            yc "....."
            yc "sorry..."
            a "don't be."
            hide azsh_lusty
            hide azsh_eyesopen
            with dissolve
            "it's exactly what i wanted."
            a "but now i need to rinse off again..."
            menu:
                "lick her clit":

                    show azsh_lick with dissolve
                    y "*slurp*"
                    show azsh_surprised with dissolve
                    a "oh!"
                    hide azsh_eyesopen
                    hide azsh_surprised with dissolve
                    a "mmmmm...."
                    show azsh_lusty with dissolve
                    a "don't stop..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "how..."
                    a "how are you so good at this...?"
                    y "*sluurp*"
                    hide azsh_neutral
                    hide azsh_doubt
                    hide azsh_lusty
                    with dissolve
                    a "mmm... hgn..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    show azsh_eyesopen with dissolve
                    a "alright, i think that's enough, don't you?"
                    y "'oh."
                    a "i know, it's delicious. but it's not up to you."
                    hide azsh_lick with dissolve
                    show azsh_lusty with dissolve
                    a "well, you... certainly surprised me."
                    show azsh azsh10 with dissolve
                    a "i hope i won't... catch you in here again."
                    hide azsh_eyesopen
                    hide azsh_lusty with dissolve
                    a "now get out... i really do need to shower."
                    if zuko_end:
                        jump zcity_night1
                    else:
                        jump zanight
                "leave":

                    scene black
                    if zuko_end:
                        jump zcity_night1
                    else:
                        jump zanight
        "nah":

            y "nah, i'm good."
            hide azsh_doubt
            show azsh azsh06
            a "get out."

            scene black

            if zuko_end:
                jump zcity_night1
            else:
                jump zanight

label za_blowjob:
    a "i'll strip for you."
    hide a_blink with dissolve
    show alnbe with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show alnb with dissolve
    a "how do i look?"
    hide alnbe
    y "great. get down on your knees."
    a "very well."
    a "follow me."
    hide alnb with dissolve
    scene bg_a_azula_room with dissolve
    show ablj1a with dissolve
    a "well? whip it out, brother."
    show ablj2a with dissolve
    a "haha... oh, my. you're ready, aren't you?"
    hide ablj1a
    show ablj4a with dissolve
    a "..."
    hide ablj2a
    hide ablj3a
    show ablj_tuga with dissolve
    y "ngh..."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "that's it, sis..."
    a "..."
    y "you have the best dick-sucking lips in the fire nation."
    y "put them to use."
    show ablj3a with dissolve
    hide ablj_tuga
    hide ablj4a
    a "..."
    show ablj6a with dissolve
    hide ablj3a
    a "okay."
    show ablj7a with dissolve
    hide ablj6a
    a "..."
    show ablj8a with dissolve
    hide ablj7a
    "azula wraps her lips fully around your member."
    y "fuck."
    show ablj9a with dissolve
    hide ablj8a
    "she drops down further, taking it as deeply as she can."
    a "*mghm* *ngh*"
    "she holds it down before coming up sputtering."
    show ablj10a with dissolve
    hide ablj9a
    a "*cough* *cough*"
    show ablj6a with dissolve
    hide ablj10a
    a "how was... that...?"
    y "get. down. there!"
    a "yes, brother! order me!"
    show ablj7a with dissolve
    hide ablj11a
    hide ablj10a
    y "ngh..."
    show ablj8a with dissolve
    hide ablj7a
    show abj_1a
    a "*mmg* *hhngh*"
    y "oh fuck!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "*ngh* *mmmgh*"
    y "deeper..."
    a "*mngh*"
    y "i said \"deeper\"..."
    a "*mmggh*"
    show ablj12a with dissolve
    a "???"
    hide abj_1a
    show ablj13a with vshake
    a "{size=+5}*hhhgghgh!!!!*"
    hide ablj12a
    y "{size=+3}there we go!"
    a "!!!!!"
    a "*ggaghag*"
    y "are you gagging? are you gagging on cock?"
    a "*mmmmmmmm*"
    y "what's that? you like having your throat filled?"
    a "*mmm-hmmmm!!*"
    y "i know you want me to empty my balls in your throat, but i'm just not there yet."
    a "*umph!* *ngh!* *hmmph!*"
    "azula begins moaning into your shaft..."
    show abj_2a with dissolve
    a "*nmgh!*"
    hide ablj8a
    y "i knew you had it in you!"
    y "look how deep you can go!"
    a "*mmnn!*"
    y "what's that?"
    a "*mmmnnn!!!*"
    y "i can't understand a word you're saying... you should really speak up."
    a "{size=+5} *aaaaahgghghhnn!!!!!*"
    y "you're welcome!"

    show ablj33a with dissolve
    a "*gaggh* *hack* *cough*"
    hide abj_2a
    hide ablj13a
    show ablj34a with dissolve
    a "i almost came!"
    hide ablj33a
    a "fuck my mouth again!"
    ya "*rrrrr*"
    show ablj13a with sshake
    "you grab her bangs and pull her all the way down onto your cock again."
    a "*nnghg!!*"
    hide ablj10a
    hide ablj34a
    show abj_2a with dissolve
    a "*umph!* *ngh!*"
    y "look at the prize jewel of the fire nation - azula the whore!"
    y "little dominating sister-princess turned cumslut."
    a "*ggagghh!* *kaghk!*"
    y "that's it, bitch, work that big shaft with your throat."
    y "drain my sack."
    y "suck out all my cum!"
    show ablj34a with dissolve
    a "hey, zuko...."
    hide ablj13a
    yd "what?"
    a "do you... enjoy your time with me?"
    menu:
        "yes":
            yd "definitely."
            a "...that makes me happy, brother."
            a "i was thinking-"
        "no":

            yd "not really."
            a "oh... well, i think-"

    show ablj13a with sshake
    a "!!!!"
    show abj_3a with Dissolve(0.2)
    y "come on! come on!"
    hide abj_2a
    y "work that cock, azula!"
    a "!!!"
    a "*nghh!* *nggh!* *aahngh!*"
    ya "oh fuck!"
    a "*??!?!!?*"
    menu:
        "cum in her throat":
            hide ablj13a
            show ablj13a with sshake
            a "!!!!!!"
            hide abj_3a
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            with flash
            a "!!!!!!"
            ya "swallow it, sis!"
            play sound "audio/splurt2.ogg"
            show ablj14a
            with flash
            y "take it down!"
            hide ablj13a
            a "*mmgnh!*"
            play sound "audio/splurt3.ogg"
            show ablj15a
            with flash
            y "down the hatch!"
            hide ablj14a
            play sound "audio/splurt1.ogg"
            show ablj16a
            with flash
            y "{size=+4}oh no you don't!"
            hide ablj15a
            a "*hnghh!*"
            play sound "audio/splurt1.ogg"
            show ablj17a
            with flash
            a "*mmgh!*"
            hide ablj16a
            y "ahh..."
            a "..."
            show ablj35a with dissolve
            a "..."
            show ablj37a with dissolve
            a "that was fun."
            hide ablj35a
            hide ablj17a
            y "yeah, it was."
            show ablj38a with dissolve
            a "don't be afraid to come back."
            a "and... it wouldn't hurt to be nice to me some."
            hide ablj37a
            hide ablj17a
            hide abj_2a
            hide ablj10a
            hide ablj8a
            hide ablj12a
            hide ablj3a
            hide ablj6a
            hide ablj38a with dissolve
            if zuko_end:
                jump zcity_night1
            else:
                jump zanight
        "cum on her face":

            hide ablj13a
            show ablj21a with sshake
            "you shove azula back off your cock."
            a "!!!!!!"
            hide abj_3a
            ya "stroke it!"
            show ablj22a with dissolve
            a "wha-"
            hide ablj21a
            ya "ngh!"
            show ablj23a
            play sound "audio/splurt3.ogg"
            with flash
            a "!!!!!!"
            a "you're-"
            hide ablj22a
            ya "take it, sis!"
            play sound "audio/splurt2.ogg"
            with flash
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            show ablj24a
            with flash
            y "all over your face, azula!"
            hide ablj23a
            play sound "audio/splurt1.ogg"
            show ablj25a
            with flash
            hide ablj24a
            y "ahh..."
            a "...."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            show ablj36a with dissolve
            a "that was fun, but.... i told you to cum in my mouth."
            a "i have an appointment."
            hide ablj25a
            y "so, go like that."
            show ablj25a with dissolve
            a "maybe i will."
            a "don't be afraid to come back."
            a "and... it wouldn't hurt to be nice to me some."
            hide ablj36a
            hide abj_2a
            hide ablj10a
            hide ablj8a
            hide ablj12a
            hide ablj3a
            hide ablj6a
            hide ablj25a with dissolve
            if zuko_end:
                jump zcity_night1
            else:
                jump zanight

label za_anal:
    y "bend over."
    a "finally."
    hide a_blink with dissolve
    show ash1 with dissolve
    a "i've been hoping all day that you'd shove your fat cock up my asshole."
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "damn."
    a "what do you think?"
    y "it's a great ass."
    show ash2 with dissolve
    ab "what, this?"
    hide ash1
    show ash_1 with dissolve
    hide ash2
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    show ash3 with dissolve
    hide ash_1
    show ash13 with dissolve
    ab "oh, no... what's that...?"
    y "......"
    show ash14 with dissolve
    abe "ah..."
    ab "easy... ah... when going into my... ah..."
    hide ash13
    show ash15 with dissolve
    asbe "oh!!"
    y "what?"
    hide ash14
    asbe "my... ngh... fuck... oh..."
    show ash13 with dissolve
    y "what's my name?"
    hide ash15
    abe "zuko?"
    show ash_an1
    aae "ah!"
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    aae "*ngh!* *ungh!* *ah!*"
    aae "yes, brother! fuck that ass!"
    aab "come on, fuck me!"
    aab "fuck me!"
    aabe "quit being so gentle! pound me like a bitch!"
    y "fine! you want it rough?"
    aab "yes!"
    y "*grr*"
    show ash_an2
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    aabe "yes! yes!"
    hide ash_an1
    abe "ugh! ngh! ah... ah... ha..."
    abe "ohhh... ah...."
    y "you're not getting off that easy!"
    aub "wha-"
    show ash_an3
    asb "ah! ah! ah!"
    hide ash_an2
    asbe "wait! wait!"
    aabe "my ass! ow! wait! no!"
    aabe "*ngh!* *mmgh!*"
    y "you asked for it, bitch!"
    aabe "*ah!* *ungh!*"
    menu:
        "cum outside":
            hide ash13
            show ash23 with flash
            aub "wh-"
            hide ash_an3
            play sound "audio/splurt2.ogg"
            show ash20 with flash
            asb "oh!"
            hide ash23
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show ash21 with flash
            asbe "mmm..."
            hide ash20
            y "not done yet!"
            play sound "audio/splurt2.ogg"
            show ash22 with flash
            abe "ahh...."
            hide ash21
            y "fuck..."
            abe "i'm soaked..."
            abe "i can feel it dripping down my legs..."
            ab "that was great."
            ab "maybe we'll do it again sometime."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            hide ash13
            hide ash22 with dissolve
            if zuko_end:
                jump zcity_night1
            else:
                jump zanight
        "cum inside":

            show ash14 with dissolve
            aub "wh-"
            hide ash_an3
            play sound "audio/splurt2.ogg"
            show ash17 with flash
            asb "ah!"
            hide ash14
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show ash18 with flash
            asbe "ngh..."
            hide ash17
            y "not done yet!"
            play sound "audio/splurt2.ogg"
            show ash19 with flash
            abe "ahh...."
            hide ash18
            y "fuck..."
            abe "i'm so full..."
            ab "that was great."
            ab "maybe we'll do it again sometime."
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            hide ash13
            hide ash19 with dissolve
            if zuko_end:
                jump zcity_night1
            else:
                jump zanight

label za_sex:
    $ zaz_sex = True
    yg "let's fuck, beautiful."
    hide a_blink
    hide aln
    if zuko_end:
        show alne
        with dissolve
        a "you know, brother.... i was thinking the same thing."
        show aln
        hide alne
        with dissolve
    else:

        show ae
        with dissolve
        a "you know, brother.... i was thinking the same thing."
        show a_blink
        hide ae
        with dissolve
        a "after all, i can't bear your children without sucking up your sperm, now can i?"
    scene black
    scene bg_a_threesome_03
    with dissolve
    a "lie down for me."
    show azrr azrr01 with dissolve
    yd "like this?"
    show azrr azrr02 with dissolve
    a "perfect."
    a "are you ready, brother?"
    y "like you wouldn't believe."
    "azula presses down on your cock, expecting it to slide in easily."
    "the tip of your cock stops at the entrance to her pussy for a half-second before the pressure from azula forces you suddenly inside her."
    play sound "audio/gltch2.mp3"
    show azrr azrr06
    with pflash

    a "fff...fuck!"
    show ctcblink
    pause
    hide ctcblink
    "azula immediately stops applying weight onto your cock, and you hold there, throbbing in the warmth of her pussy."
    "you can tell she's taken aback at the resistance."

    a "fuck, fuck, fuck...."
    a "it's... it's too tight, i don't think..."
    a "ah...."
    a "fuck!"
    a "no! i'm going to take this fucking cock!"
    show azrr azrr05 with dissolve
    show ctcblink
    pause
    hide ctcblink
    a "ah... ah... ha... oh, fuck, zuko...."
    a "how do... how do you fuck any girls with this..."
    show azrr azrr06 with dissolve
    a "fuck... i need a second..."
    a "......"
    a "okay.... okay...."
    a "here we go...."
    show azrr azrr10 with dissolve

    show ctcblink
    pause
    hide ctcblink
    show azrr azrr09 with Dissolve(0.3)
    a "mmnghh..."
    show ctcblink
    pause
    hide ctcblink
    a "ngh..."
    show azrr azrr08 with Dissolve(0.3)
    a "hhnggh... mgh... ah..."
    show ctcblink
    pause
    hide ctcblink
    a "just that... that little bit was... shit...."
    show azrr azrr04 with dissolve
    yg "you really are tight, little sis."
    a "shut... shut up... zuko..."
    yg "is big brother's dick too big?"
    a "no... you're... ah... i just... i want to fuck.... you.... ah..."
    show azrr azrr03 with vshake
    a "ah!"
    a "fuck!"
    show azrr azrr07 with Dissolve(0.3)
    show ctcblink
    pause
    hide ctcblink
    a "damn it! shit!"
    a "ahhh..... shhh..... don't... don't say a fucking.... ahh...."
    show azrr azrr03 with Dissolve(0.3)
    a "don't... don't move..."
    show azrr azrr106
    show ctcblink
    pause
    hide ctcblink
    a "ah.... ah.... ah...."
    a ".......i think we can do this, zuko."
    a "i just..."
    a "give me... a second..."
    a "okay..."
    a "okay... here we go..."

    show azrr azrr107

    show ctcblink
    pause
    hide ctcblink
    a "ah!"
    a "yes!"
    show azrr azrr100
    a "ohhh...."
    show ctcblink
    pause
    hide ctcblink
    a "*ngh*... *mmph*... *ah*..."
    a "yes... ngh... final... finally...."
    a "how... how is it, brother?"
    a "is it good? is your sister's pussy good?"
    show ctcblink
    pause
    hide ctcblink
    show azrr azrr04 with Dissolve(0.3)
    a "oh, fuck..."
    show azrr azrr08 with Dissolve(0.4)
    a "oh, fuck!"
    show azrr azrr108
    show ctcblink
    pause
    hide ctcblink
    a "zuzu.... oh, zuzu.... keep... just keep fucking me...."
    a "the palace is ours.... the nation is ours...."
    a "no one can stop us...."
    a "just keep... keep fucking me...."
    a "we can do this for whenever... forever..."
    show ctcblink
    pause
    hide ctcblink
    a "tell me you love it... tell me!"
    yg "you feel fucking amazing..."
    a "more... i need more...!"
    show azrr azrr101
    show ctcblink
    pause
    hide ctcblink
    a "yes! yes!"
    a "oh, big brother! oh, zuzu!"
    a "let me ride you! baby sis will always be here to ride your big cock!"

    show azrr azrr109 with dissolve

    a "i can't stop watching it...."
    a "i've wanted this, but i've been so afraid..."
    a "afraid of how good it would feel..."
    a "fuck... fuck... you're so thick..."
    if not zuko_end:
        a "this feels even better than when i burned down that entire pathetic earth kingdom village."
    show azrr azrr103 with dissolve
    if not zuko_end:
        a "i'm never letting you leave... never!"
    if zuko_end:
        a "please... never leave, zuzu..."
    show ctcblink
    pause
    hide ctcblink
    show azrr azrr104 with dissolve
    show ctcblink
    pause
    hide ctcblink
    a "you'll never leave me, right, zuko?"
    a "you'll stay and let me fuck you over and over and over and over again?"
    a "right? won't you?"
    a "i love you, zuko."
    a "i love you so much."
    if not zuko_end:
        a "i want to bear your children."

    a "this feels good, right?"
    a "doesn't this feel perfect?"
    a "tell me you love me."
    show azrr azrr102 with dissolve
    show ctcblink
    pause
    hide ctcblink
    a "tell me, zuko..."
    a "tell me that you love me...!"
    a "i need to hear it...."
    a "tell me!"
    y "i-"
    a "look me in the eyes!"
    a "tell me!"
    show ctcblink
    pause
    hide ctcblink
    menu:
        "tell her":
            y "i love you."
            a "of course..."
            a "of course you love me..."

            show azrr azrr104 with dissolve
            a "how could you not?"
            a "i know you love how this feels... watching me..."
            a "this right here."
            a "feel me squeezing out that cum?"
            a "i know you're desperate to fill me up with sperm, brother."
            if not zuko_end:
                a "fill up your little sister. your filthy slut of a little sister."
                a "azula, your personal family slut."
            if zuko_end:
                a "fill up your little sister!"
        "don't tell her":

            "you remain silent."
            a "No?"
            a "you sure?"
            show azrr azrr104 with dissolve
            a "you sure you don't love me?"
            a "that you don't love this?"
            a "this right here?"
            a "feel me squeezing out that cum?"
            a "i know you're desperate to fill me up with sperm, brother."
            if not zuko_end:
                a "fill up your little sister. your filthy slut of a little sister."
                a "azula, your personal family slut."
            if zuko_end:
                a "fill up your little sister!"

    show azrr azrr101 with dissolve
    if not zuko_end:
        a "fuck yes.... i'm the firelord..."
        a "i have my brother as my fuck slave...."
        yd "hey..."
        a "i can defeat any and every one..."
        a "my life is so good.... so fucking good..."
    if zuko_end:
        a "fuck yes.... i'm fucking the firelord..."
        a "i'm zuzu's...."
        a "my life is so good.... so fucking good..."
    show azrr azrr109 with dissolve
    a "and this cock... this fucking cock..."
    a "yes... yes... i feel you swelling..."
    show azrr azrr103 with dissolve
    a "i feel you in there..."
    a "give me that load.... that big fucking load..."
    a "fill my pure, ready pussy...."
    a "it's okay. you can cum, zuzu."
    a "i need this. we need this."
    a "cum in me. give me your seed."
    a "yes... yes... fuck, you're getting... getting too.. ah... ah..."
    a "cum for me! cum on, brother! cum!"
    if not azula_preg:
        if not zuko_end:
            a "impregnate me!"
        menu:
            "impregnate azula":
                y "ngh!"
                show azrr azrr07
                show azzr_xray
                with Dissolve(1.0)
                play sound "audio/splurt2.ogg"
                show azzr_xray_spermshot
                $ renpy.pause(0.3)
                hide azzr_xray_spermshot
                show azzr_xray_sperm1
                a "yes!"
                show azrr azrr12 with dissolve
                play sound "audio/splurt2.ogg"
                show azzr_xray_spermshot
                $ renpy.pause(0.3)
                hide azzr_xray_spermshot
                hide azzr_xray_sperm1
                show azzr_xray_sperm2
                if not zuko_end:
                    a "give me babies, zuzu!"
                y "fuck!"

                show azrr azrr03 with dissolve
                play sound "audio/splurt1.ogg"
                show azzr_xray_spermshot
                $ renpy.pause(0.3)
                hide azzr_xray_spermshot
                hide azzr_xray_sperm2
                show azzr_xray_sperm3
                a "mmmm..."
                hide azzr_xray_sperm2
                show azrr_fertilize
                pause
                a "wow...."
                a "that... that was a huge load, zuko."
                $ azula_preg = True
            "superheat and kill your sperm":

                "as your begin to ejaculate, you heat your sperm just high enough to kill them."
                y "ngh!"
                show azrr azrr07
                show azzr_xray
                with Dissolve(1.0)
                play sound "audio/splurt2.ogg"
                show azzr_xray_spermshot
                $ renpy.pause(0.3)
                hide azzr_xray_spermshot
                show azzr_xray_sperm1
                a "yes!"
                show azrr azrr12 with dissolve
                play sound "audio/splurt2.ogg"
                show azzr_xray_spermshot
                $ renpy.pause(0.3)
                hide azzr_xray_spermshot
                hide azzr_xray_sperm1
                show azzr_xray_sperm2
                if not zuko_end:
                    a "give me babies, zuzu!"
                y "fuck!"
                show azrr azrr03 with dissolve
                play sound "audio/splurt1.ogg"
                show azzr_xray_spermshot
                $ renpy.pause(0.3)
                hide azzr_xray_spermshot
                hide azzr_xray_sperm2
                show azzr_xray_sperm3
                a "mmmm..."
                hide azzr_xray_sperm2
                pause
                a "wow...."
                a "that... that was a huge load, zuko."
                a "and... very warm..."
    else:

        y "ngh!"
        show azrr azrr07
        show azzr_xray
        with Dissolve(1.0)
        play sound "audio/splurt2.ogg"
        show azzr_xray_spermshot
        $ renpy.pause(0.3)
        hide azzr_xray_spermshot
        show azzr_xray_sperm1
        a "yes!"
        show azrr azrr12 with dissolve
        play sound "audio/splurt2.ogg"
        show azzr_xray_spermshot
        $ renpy.pause(0.3)
        hide azzr_xray_spermshot
        hide azzr_xray_sperm1
        show azzr_xray_sperm2
        if not zuko_end:
            a "give me babies, zuzu!"
        y "fuck!"

        show azrr azrr03 with dissolve
        play sound "audio/splurt1.ogg"
        show azzr_xray_spermshot
        $ renpy.pause(0.3)
        hide azzr_xray_spermshot
        hide azzr_xray_sperm2
        show azzr_xray_sperm3
        a "mmmm..."
        hide azzr_xray_sperm2
        show azrr_fertilize
        pause
        a "wow...."
        a "that... that was a huge load, zuko."

    show azrr azrr12 with dissolve
    a "mmmm...."
    pause
    show azrr azrr14 with dissolve
    if not zuko_end:
        a "hopefully it took."
    show azrr azrr15 with dissolve
    a "don't forget this moment."
    a "we're going to have a lifetime of them."
    show ctcblink
    pause
    hide ctcblink
    show azrr azrr105
    hide azzr_xray
    hide azzr_xray_sperm3
    with dissolve
    a "mmm..."
    a "look at all the cum...."
    if not zuko_end:
        a "i can't wait to bear our children, zuko."
        scene black
        scene bg_a_threesome_03
        show alnb
        with dissolve
        a "that was wonderful."
        a "unfortunately, i have things to take care of."
        a "i'll see you later, handsome!"
        hide alnb with dissolve
        jump zanight

    if zuko_end:
        a "now..."
        a "i'll let you relax...."
        scene black with dissolve
        jump zcity_night1

label za_beachrub:
    a "and let's bring ty lee along."
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
    a "now you should wave to those curious people over there."
    a "so they don't think anything suspicious."
    "you smile and wave at the beach-goers, who smile and wave back."
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
    show azbr azbr101 with Dissolve(0.35)
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
        "maybe... maybe another minute...":

            yc "i... guess... ah... you can... deal with her..."
            hide azbr_sultry with Dissolve(0.35)
            a "you're such a good big brother."
            show azbr azbr105 with Dissolve(0.35)
            show ctcblink
            $ renpy.pause()
            hide ctcblink

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
    t "i hope the weather stays nice..."
    a "i am sure that..."
    show azbr azbr04_2 with dissolve
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    a "*mmmmm*"
    a "...that it will stay fine."
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
    scene black with dissolve
    "you spend the rest of the day at the beach and head home that evening."
    if zuko_end:
        jump zcity_night1
    else:
        jump zanight

label zftower_day20:
    if azula_chosen_end:
        y "i should leave the city."
        jump zaday

    scene black
    scene bg_a watchtower_day
    with dissolve
    if not rei_gone:
        yd "hello?"
        "there's no response. the tower seems empty."
        yd "where the hell is rei-"
        ya "no. azula wouldn't...."
        yc "she would."
        yc "fuck."
        ya "i have to find out for sure if azula got rid of rei."
        $ rei_gone = True
        jump zaday
    else:
        if not rei_resolved:
            yd "i should ask azula if she knows what's happened to rei."
            jump zaday
        else:
            if zaz_sex:
                "you hear a faint whisper, seemingly coming from within the walls of the tower."
                "{i}thisss isss a lie....."
                "{i}there isss more, and i will bring your world crumbling down.... {size=-4}down.... {size=-4}down...."
                "{i}are you ready for thisss to end? ssssimply lissssten...."
                menu:
                    "i am ready":
                        "warning! there is no returning from this quest."
                        menu:
                            "continue":
                                jump zuko_ds_talk
                            "back":
                                y "no, not yet. i'm enjoying myself."
                                jump zaday
                    "not yet":

                        y "no, not yet. I'm enjoying myself."
                        jump zaday
            else:
                "you feel a presence, but it seems to be waiting for something...."
                jump zaday

label zaday:
    if guards_assigned:
        scene black
        scene bg_a_city_day
        with dissolve
        call screen zfday20
    else:
        scene black
        scene bg_a_city_day
        with dissolve
        y "alright, where should i-"
        g1 "hey, buddy."
        yd "oh, right. my babysitters."
        g2 "dank! where?"
        g1 "he means {i}us{/i}, you choad."
        g2 "are you sure? i have a thing for babysitters."

        y "everyone has a thing for babysitters."

        g1 "and don't say \"dank\". it's unprofessional."
        g2 "i'm like, 90 percent sure \"choad\" is less professional."
        g2 "maybe 85."
        g2 "but no, i mean, when i was a kid i had one that was super sexy...."
        g2 "it kind of messed me up."
        g2 "attraction-wise."
        g1 "you don't mean you're into young-"
        g2 "he was so sexy."
        yd "wait, hold on-"
        g2 "he had legs for miles-"
        g1 "damn it tom, shut up!"
        g1 "the prince doesn't want to hear about that."
        y "i might."
        yd "wait... am i still the prince?"
        y "i should figure that out."
        g1 "look mate, we're just gonna hang out behind you."
        g1 "you won't even notice us."
        g2 "that's right, we'll just watch you walk."
        g1 "right, we'll-"
        g1 "fucking damn it, tom!"
        g1 "can you not flirt with the prince?"
        y "ah, he's fine. i'm secure. it's flattering."
        g2 "see?"
        g1 "i hate you both."
        yd "...."
        ys "i like you."
        g1 "fuck you."
        g1 "sir."
        ys "heh. we're gonna get along just fine."
        $ guards_assigned = True
        jump zaday


label zanight:
    scene black
    scene bg_a_city_night
    with dissolve
    call screen zfnight20

label zffight_night20:
    if azula_chosen_end:
        jump zuko_ds_battle

    if not flynn_bradsley:
        $ flynn_bradsley = True
        g1 "you're right, that's {i}not{/i} normal."
        g2 "i told you!"
        g1 "can you... put it away, now?"
        g1 "super weird for a shift."
        g2 "what? we're buds."
        g1 "yeah, but... how did you even get burns there?"
        g2 "the new firebending brothel."
        g1 "the what?"
        g2 "they have super warm-"
        g1 "i get it, i get it."
        g1 "look, just... stop whipping it out."
        g2 "come on, we should get in some sword practice."
        g1 "finally, yes, i'll get our blades-"
        g2 "that's not what i meant."
        g1 "oh, god dammit!"
        g1 "no! stop showing me your fucking co-"
        y "yo guys, what's-"
        yd "huh."
        yd "that's... not normal."
        g2 "right!?"
        g1 "put it away!"
        g2 "who's gonna mess with us with our dicks out?"
        yd "not me."
        g1 "especially not with that weird thing."
        g1 "it's blinking at me."
        g2 "aw, don't be mean to it."
        g2 "i'm gonna name it!"
        g1 "don't name it."
        g2 "i'm gonna."
        g1 "don't-"
        g2 "how about..."
        g1 "I'm begging you, here."
        g2 "i'm gonna name him... flynn bradsley."
        g1 "............."
        g1 "....why??"
        g2 "it invokes valor and bravery."
        g1 "why would you even want that? just get rid of it!"
        g2 "i'm not getting rid of flynn bradsley!"
        g2 "you're heartless!"
        g1 "it's literally blinking at me!"
        g2 "are you sure we shouldn't keep it?"
        g1 "what? it's yours!"
        g2 "it's ours!"
        g1 "i don't want it!"
        g2 "shhh.... don't let him hear you say that, you'll hurt his feelings."
        g1 "you're fucking mental."
        g2 "apologize. apologize to flynn bradsley."
        g1 "I'm not apologizing to your dick!"
        g2 "aw."
        yd "i'm... gonna just go, now."
        g1 "...take me with you."
        g2 "flynn says bye!"
        jump zanight
    else:

        g1 "look, i'm just saying if you don't feed it properly, it's gonna get sick and-"
        g2 "are you saying that flynn bradsley is malnourished?"
        g1 "no, no, i'm not blaming anyone, i just worry about it-"
        g2 "he's not an \"it\", he's a \"he\"."
        g1 "right, whatever, i just haven't had a pet before and i'm... a little anxious."
        g2 "well, i haven't had a pet that grew out of my dick before, but i had a koala-seal, and i... did not do a good job."
        g2 "what fucking environment can that live it?"
        g2 "...but i know what i'm doing here. i think."
        g1 "is it... sorry, is {i}he{/i}... getting lots of veggies?"
        yd "....okay, i'm not doing this."
        g2 "he likes bananas."
        g2 "and being choked."
        y "yup, nope, i'm out."
        jump zanight

label zfpalace_night20:
    if azula_chosen_end:
        y "i should leave the city."
        jump zanight

    $ rand_azula_sleep = renpy.random.randint(1, 5)
    if rand_azula_sleep ==1:
        show azsl azsl01 with dissolve
    if rand_azula_sleep ==2:
        show azsl azsl02 with dissolve
    if rand_azula_sleep ==3:
        show azsl azsl03 with dissolve
    if rand_azula_sleep ==4:
        show azsl azsl04 with dissolve
    if rand_azula_sleep ==5:
        show azsl azsl05 with dissolve

    menu:
        "lay down":
            show ctc
            pause
            hide ctc
            show azsl_eyeshalfopen with dissolve
            a "*sleepily* hey, brother...."
            a "don't be shy, this is your bed now, too."
            menu:
                "cuddle":
                    "you undress and lay next to her."
                    show azsl_eyesopen
                    hide azsl_eyeshalfopen
                    with dissolve
                    "azula runs her fingers down your chest, watching your face with a hungry intensity."
                    "her fingers continue to run down your naked body, until she reaches your cock...."
                    with ushake
                    "....which she grasps and squeezes, causing you to gasp."
                    show azsl_eyeshalfopen
                    hide azsl_eyesopen
                    with dissolve
                    a "mmmm.... i love your cock."
                    a "will you......"
                    y "what?"
                    a "....will you just hold me?"
                    ys "of course."
                    hide azsl_eyeshalfopen with dissolve
                    if rand_azula_sleep ==1:
                        show azsl azsl11 with dissolve
                    if rand_azula_sleep ==2:
                        show azsl azsl12 with dissolve
                    if rand_azula_sleep ==3:
                        show azsl azsl14 with dissolve
                    if rand_azula_sleep ==4:
                        show azsl azsl13 with dissolve
                    if rand_azula_sleep ==5:
                        show azsl azsl15 with dissolve

                    "azula rolls over, and you put your arms around her."
                    a "*mmmm....*"
                    "she moans and presses backwards against you as you settle your member between her cheeks."
                    "you can feel the vibration from her moan against your chest as you grip and press your fingers into her soft, accepting breasts."
                    "you sleep soundly."
                    scene black
                    jump zaday
                "do you believe in love?":

                    y "do you believe in life after love?"
                    a "....what?"
                    y "i meant... do you think love is real, or is it just pheromones, or-"
                    a "....i don't know."
                    show azsl_eyesopen
                    hide azsl_eyeshalfopen
                    with dissolve
                    a "but i want to be with you."
                    a "and you make me feel safe. and i want to see you happy."
                    show azsl_eyeshalfopen
                    hide azsl_eyesopen
                    with dissolve
                    a "and i don't care what that's called."
                    hide azsl_eyeshalfopen with dissolve
                    a "now, can we sleep?"
                    if rand_azula_sleep ==1:
                        show azsl azsl11 with dissolve
                    if rand_azula_sleep ==2:
                        show azsl azsl12 with dissolve
                    if rand_azula_sleep ==3:
                        show azsl azsl14 with dissolve
                    if rand_azula_sleep ==4:
                        show azsl azsl13 with dissolve
                    if rand_azula_sleep ==5:
                        show azsl azsl15 with dissolve

                    "azula rolls over, and pushes backwards against you."
                    "you sleep soundly."
                    scene black
                    jump zaday
        "masturbate":



            show azsl_masturbate_1 with Dissolve(0.3)
            menu:
                "be quiet":
                    y "careful...."
                    show azsl azsl06 with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    y "god damn, those are some perfect tits."
                    show azsl_masturbate_1 with Dissolve(0.3)
                    y "that's it, sis."
                    y "if you want to be slathered in cum, stay right there."
                    menu:
                        "cum on tits":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            show azsl azsl11
                            with dissolve
                            a "*mmghn...*"
                            ys "ahh... i needed that."
                            scene black with dissolve
                            "you sleep next to azula."
                            show azsl azsl01
                            show azsl_spermtits_3
                            with dissolve
                            a "hhmmmm....."
                            show azsl_eyeshalfopen with dissolve
                            a "good morning, broth-"
                            a "......"
                            a "what the..."
                            show azsl_eyesopen
                            hide azsl_eyeshalfopen
                            with dissolve
                            a "did you ejaculate on me during the night, zuzu?"
                            y "...maybe."
                            a "...."
                            a "................"
                            a "well did you have fun at least?"
                            y "oh yeah."
                            show azsl_eyeshalfopen
                            hide azsl_eyes_open
                            with dissolve
                            a "very well. at least wake me next time."
                            a "now i need a shower. you've left me sticky."
                            a "get out."
                            scene black
                            jump zaday
                        "cum on pussy":


                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3
                            show azsl azsl11
                            with dissolve
                            a "*mmghn...*"
                            ys "ahh... i needed that."
                            scene black with dissolve
                            "you sleep next to azula."
                            show azsl azsl01
                            show azsl_spermvag_3
                            with dissolve
                            a "hhmmmm....."
                            show azsl_eyeshalfopen with dissolve
                            a "good morning, broth-"
                            a "......"
                            a "what the..."
                            show azsl_eyesopen
                            hide azsl_eyeshalfopen
                            with dissolve
                            a "did you ejaculate on me during the night, zuzu?"
                            y "...maybe."
                            a "...."
                            a "................"
                            a "well did you have fun at least?"
                            y "oh yeah."
                            show azsl_eyeshalfopen
                            hide azsl_eyes_open
                            with dissolve
                            a "very well. at least wake me next time."
                            a "now i need a shower. you've left me sticky."
                            a "get out."
                            scene black
                            jump zaday
                        "cum on both":

                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            ya "(not done yet!)"

                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            show azsl azsl11
                            with dissolve
                            a "*mmghn...*"
                            ys "ahh... i needed that."
                            scene black with dissolve
                            "you sleep next to azula."
                            show azsl azsl01
                            show azsl_spermtits_3
                            show azsl_spermvag_3
                            with dissolve
                            a "hhmmmm....."
                            show azsl_eyeshalfopen with dissolve
                            a "good morning, broth-"
                            a "......"
                            a "what the..."
                            show azsl_eyesopen
                            hide azsl_eyeshalfopen
                            with dissolve
                            a "did you ejaculate on me during the night, zuzu?"
                            y "...maybe."
                            a "...."
                            a "................"
                            a "well did you have fun at least?"
                            y "oh yeah."
                            show azsl_eyeshalfopen
                            hide azsl_eyes_open
                            with dissolve
                            a "very well. at least wake me next time."
                            a "now i need a shower. you've left me sticky."
                            a "get out."
                            scene black
                            jump zaday
                "make noise":



                    y "*pant* *pant*"
                    y "that's it..."
                    y "i'm gonna..."
                    show azsl_eyeshalfopen with dissolve
                    y "take th-"
                    y "oh. sorry."
                    show azsl_eyesopen with dissolve
                    a "sigh... go ahead."
                    hide azsl_eyesopen
                    with dissolve
                    a "here."
                    show azsl azsl06 with dissolve
                    a "does this help?"
                    y "fffuuuu...."
                    a "yes, i know."
                    a "go ahead, so i can get some rest."
                    y "well, since you asked..."
                    a "....."
                    y "ngh...."
                    menu:
                        "cum on tits":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            y "there..."
                            a "mmmm... warm."
                            a "all done?"
                            a "good."
                            a "now maybe i can get some sleep."
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            hide azsl_eyesopen
                            hide azsl_eyeshalfopen
                            show azsl azsl11
                            with dissolve
                            a "get into the bed, idiot."
                            a "and get that blanket."
                            scene black with dissolve
                            "you manage to fall asleep."
                            jump zaday
                        "cum on pussy":


                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            y "there..."
                            a "mmmm... warm."
                            a "all done?"
                            a "good."
                            a "now maybe i can get some sleep."
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3
                            hide azsl_eyesopen
                            hide azsl_eyeshalfopen
                            show azsl azsl11
                            with dissolve
                            a "get into the bed, idiot."
                            a "and get that blanket."
                            scene black with dissolve
                            "you manage to fall asleep."
                            jump zaday
                        "cum on both":

                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            ya "not done yet!"
                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            y "there..."
                            y "there..."
                            a "mmmm... warm."
                            a "all done?"
                            a "good."
                            a "now maybe i can get some sleep."
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3
                            hide azsl_eyesopen
                            hide azsl_eyeshalfopen
                            show azsl azsl11
                            with dissolve
                            a "get into the bed, idiot."
                            a "and get that blanket."
                            scene black with dissolve
                            "you manage to fall asleep."
                            jump zaday

        "fuck her tits" if azula_night_titfuck:
            show azsf azsf01 with dissolve
            y "time to take her up on her offer."
            show azsf azsf02 with dissolve
            "you straddle azula's chest and lay your cock on her tits."
            y "yeah, that's nice."
            y "time to bury my cock in your fat tits, sister."
            show azsf azsf03 with Dissolve(0.35)
            yc "oh, fuck..."
            show azsf azsf06 with Dissolve(0.35)
            a "*hsfas...*"
            "azula stretches out a little in her sleep."
            yd "...."
            yg "well, let's get to work."
            show azsf azsf100
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            yc "nghh..."
            y "that's it...."
            ys "sshhh... just stay asleep..."
            yg "now, that's some good squish."
            menu:
                "grab her boobs":
                    show azsf azsf12 with dissolve
                    yg "let's pick things up a little..."
                    show azsf azsf101
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "*mmmffshgh.....*"
                    ys "yeah... that's it..."
                    yg "come on, azula... make me cum..."
                    show azsf_sidehead with dissolve
                    show azsf azsf102
                    ya "make me cum... make me cum..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "fuck... fuck... fuck..."
                    show azsf azsf103
                    ya "faster... faster..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "you're gonna make me..."
                    ya "hhngh..."
                    show azsf azsf104
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "come on! come on!"
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    show azsf azsf105
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "ahhh!!"
                    ya "i'm cumming, sis!"
                    ya "take it!"
                    hide azsf_sidehead
                    with dissolve
                    a "*hghngh...?...*"
                    ya "ngh!"
                    play sound "audio/splurt2.ogg"
                    show azsf azsf15
                    show azsf_sperm1
                    with flash
                    a "*nnghnm...*"
                    play sound "audio/splurt2.ogg"
                    hide azsf_sperm1
                    show azsf_sperm2
                    with flash
                    yc "nngh..."
                    yc "fuck, i think..."
                    ya "ungh!"
                    play sound "audio/splurt2.ogg"
                    hide azsf_sperm2
                    show azsf_sperm3
                    with flash
                    y "damn."
                    show azsf azsf00
                    show azsf_sperm1:
                        xpos -200 ypos 100
                    with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    yg "that's a good look for you, sis."
                    show azsf_eyesopen
                    show azsf_mouthopen
                    hide azsf_sperm3
                    show azsf_sperm3
                    with dissolve
                    a "mmmm.... thank you, love."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    menu:
                        "cover her with a blanket":
                            hide azsf_eyeopen
                            show azsf_cover
                            with dissolve
                            a "thank... you..."
                            "you lay next to azula and sleep soundly."
                            jump zaday
                        "no blanket":

                            "you lay next to azula and sleep soundly."
                            jump zaday
                "stay like this":

                    yg "let's pick things up a little..."
                    show azsf azsf106
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    a "*mmmffshgh.....*"
                    ys "yeah... that's it..."
                    yg "come on, azula... make me cum..."
                    show azsf_sidehead with dissolve
                    show azsf azsf107
                    ya "make me cum... make me cum..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "fuck... fuck... fuck..."
                    show azsf azsf108
                    ya "faster... faster..."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "you're gonna make me..."
                    ya "hhngh..."
                    show azsf azsf109
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "come on! come on!"
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    show azsf azsf110
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    ya "ahhh!!"
                    ya "i'm cumming, sis!"
                    ya "take it!"
                    hide azsf_sidehead
                    with dissolve
                    a "*hghngh...?...*"
                    ya "ngh!"
                    play sound "audio/splurt2.ogg"
                    show azsf azsf09
                    show azsf_sperm1
                    with flash
                    a "*nnghnm...*"
                    play sound "audio/splurt2.ogg"
                    hide azsf_sperm1
                    show azsf_sperm2
                    with flash
                    yc "nngh..."
                    yc "fuck, i think..."
                    ya "ungh!"
                    play sound "audio/splurt2.ogg"
                    hide azsf_sperm2
                    show azsf_sperm3
                    with flash
                    y "damn."
                    show azsf azsf00
                    show azsf_sperm1:
                        xpos -200 ypos 100
                    with dissolve
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    yg "that's a good look for you, sis."
                    show azsf_eyesopen
                    show azsf_mouthopen
                    hide azsf_sperm3
                    show azsf_sperm3
                    with dissolve
                    a "mmmm.... thank you, love."
                    show ctcblink
                    $ renpy.pause()
                    hide ctcblink
                    menu:
                        "cover her with a blanket":
                            hide azsf_eyeopen
                            show azsf_cover
                            with dissolve
                            a "thank... you..."
                            "you lay next to azula and sleep soundly."
                            jump zaday
                        "no blanket":

                            "you lay next to azula and sleep soundly."
                            jump zaday



label zftower_night20:
    if azula_chosen_end:
        y "i should leave the city."
        jump zanight

    scene black
    scene bg_a watchtower_night
    with dissolve
    if not rei_gone:
        yd "hello?"
        "there's no response. the tower seems empty."
        yd "where the hell is rei-"
        ya "no. azula wouldn't...."
        yc "she would."
        yc "fuck."
        ya "i have to find out for sure if azula got rid of rei."
        $ rei_gone = True
        jump zanight
    else:
        if not rei_resolved:
            yd "i should ask azula if she knows what's happened to rei."
            jump zanight
        else:
            if zaz_sex:
                "you hear a faint whisper, seemingly coming from within the walls of the tower."
                "{i}thisss isss a lie....."
                "{i}there isss more, and i will bring your world crumbling down.... {size=-4}down.... {size=-4}down...."
                "{i}are you ready for thisss to end? ssssimply lissssten...."
                menu:
                    "i am ready":
                        "warning! there is no returning from this quest."
                        menu:
                            "continue":
                                jump zuko_ds_talk
                            "back":
                                y "no, not yet. i'm enjoying myself."
                                jump zanight
                    "not yet":
                        y "no, not yet. I'm enjoying myself."
                        jump zanight
            else:
                "you feel a presence, but it seems to be waiting for something...."
                jump zanight

label zuko_ds_talk:
    y "alright, what is it?"
    "{i}leave the sssss-city."
    "{i}your path issss sssssecured."
    yd "why would i do that?"
    "{i}i will tell you everything there."
    g1 "um..."
    yd "just tell me here."
    g2 "{size=-4}psst.... is he talking to himself?"
    g1 "{size=-4}azula asked us to tell her if he acts strangely."
    g2 "{size=-4}i'm on it."
    "one of your guards hurries off, but you barely notice."
    "{i}it issss not sssssafe here...."
    y "you're already here, though."
    "you argue with the voice - kind of petulantly - for a bit."
    "{i}leave the sssss-city."
    yd "yeah, you've been saying th-"
    "the presence seems to disappear."
    yd "....huh."
    $ azula_chosen_end = True
    scene bg_a_city_night with dissolve
    show au with dissolve
    a "zuzu? are you... okay?"
    yd "what are you doing here?"
    a "one of your guards came and got me."
    a "he mentioned you were talking to the air?"
    a "i'm.... worried about you."
    y "not the air. a voice in the air. a spirit or something."
    a "oh...kay."
    a "your mind's had some.... issues before. i don't want to see that happen again."
    yd "what? i'm not crazy."
    a "would more freedom help you?"
    yd "(hmm.... the spirit did say to leave the city...)"
    y "sure, more freedom would be great."
    y "i'd like to take a long walk outside the city."
    a "is that what the.... voice.... told you to do?"
    y "well-"
    hide au
    show a_blink
    with dissolve
    a "okay."
    yd "really? that easily?"
    a "yes. but i'm coming with you."
    yc "oh... i don't think that's a good idea."
    show ae
    hide a_blink
    with dissolve
    a "you can go with me or stay here."
    a "that's final."
    yd "fine, let's go."
    show a_blink
    hide ae
    with dissolve
    a "wait. i want to do something first."
    a "will you wait here for me?"
    menu:
        "yes, i'll wait":
            show ae
            hide a_blink
            with dissolve
            a "oh, wonderful."
            hide ae with dissolve
            "you wait outside the tower."
            yd "i wonder what's taking her so long?"
            g1 "dunno."
            yd "oh, shit. you're still here."
            g1 "okay. seriously. i have fucking feelings."
            g1 "am i just invisible?"
            "you ignore him."
            "you watch the few people still out after curfew -- particularly any pretty girls."
            "you hear someone crying nearby. it sounds like its muffled by a helmet, but there's no one around you."
            "a girl runs by and you watch closely as she hurries on."
            scene black
            "hands suddenly cover your eyes and you panic for a moment, but a familar feminine voice soothes you."
            mv "guess who."
            menu:
                "azula?":
                    yd "azula?"
                    mv "good guess!"
                "tom?":

                    yd "is that you, tom?"
                    mv "what? no! do i sound like a boy?"

            scene bg_a_city_night
            show b2az b2az01
            with Dissolve(1.0)
            a "hi."
            y "hi."
            ys "you look beautiful."
            a "thank you, brother."

            if azula_preg:
                yd "....and pregnant."
                a "well... that's what happens when you fuck...."
                show b2az_idleblink with dissolve
                a "and jizz in my insides."
                hide b2az_idleblink with dissolve
                yd "but... where were you hiding it?"
                a "i've been wearing particularly flattering clothing."
                y "i've also seen you naked."
                a "i may have recently drunk some of that quick-pregnancy potion we gave the cows."
                y "ah. that explains everything. neatly."

            a "well.... shall we walk?"
            y "with you on my arm?"
            y "it would be a pleasure."
            hide b2az b2az01 with dissolve
            "you walk together to the gates of the city."
            show b2az b2az01 with dissolve
        "no, i won't wait":

            y "nah, i'm pretty eager to go."
            show au
            hide a_blink
            with dissolve
            a "oh."
            a "well, at least wait for me at the city gates."
            y "oh, fine."
            hide au with dissolve
            "you wander down to the gates of the city."
            g1 "so. sports, huh?"
            yd "what?"
            g1 "i'm no good at small talk."
            y "then don't try."
            g1 "....."
            g1 "weather, eh?"
            yd "....."
            g1 "did you see-"
            show b2az b2az01
            with Dissolve(1.0)
            a "hi, brother."
            g1 "oh, thank god."
            y "oh, thank god."
            g1 "...."
            y "...."
            g1 "i'll just be quiet."

            y "hi, sis."
            ys "you look beautiful."
            a "thank you, zuzu."

            if azula_preg:
                yd "....and pregnant."
                a "well... that's what happens when you fuck...."
                show b2az_idleblink with dissolve
                a "and jizz in my insides."
                hide b2az_idleblink with dissolve
                yd "but... where were you hiding it?"
                a "i've been wearing particularly flattering clothing."
                y "i've also seen you naked."
                a "i may have recently drunk some of that quick-pregnancy potion we gave the cows."
                y "ah. that explains everything. neatly."

            a "well.... shall we walk?"
            y "with you on my arm?"
            y "it would be a pleasure."

    "azula clings tightly to your arm."
    y "you're very pretty with your hair down, you know."
    y "you should do that more often."
    a "i'm.... glad you think so, zuko."
    a "i thought I'd make this a nice moonlight stroll."
    a "but i think we can do without the commentary, don't you?"
    yd "what?"
    g1 "she means us, you jerk."
    y "oh."
    a "guards, leave us."
    g1 "....but it might be dangerous outside the city, my queen."
    show b2az_idleblink with dissolve
    a "Hahaha!"
    a "Yes.... for anyone zuzu and i might encounter!"
    hide b2az_idleblink with dissolve
    a "now Hush! And follow my commands. I won't tell you twice."
    g1 "....yes, your highness."
    scene black with dissolve
    "the guards leave you and azula alone as you stroll out past the gates."
    show expression "fbackgrounds/bk2_night01.jpg":
        xpos -1000
        linear 80 xpos 0
        repeat
    show expression "bk2end/badend/idlestroll_moon.png"
    show b2az b2az01:
        ypos 7
        linear 1 ypos 0
        linear 1 ypos 7
        repeat
    with Dissolve(1.0)
    show ctc
    pause
    hide ctc
    y "Wow, the Azula from before would've incinerated that guard for not immediately following her command!"
    show b2az b2az02
    with dissolve
    "azula stretches her arms behind her head."
    a "Well, I was a bit more on edge back then. I feel a lot more relaxed nowadays."
    a "The war is going great."
    a "The other girls know their limits when it comes to you and the weather has been great lately!"
    show ctc
    pause
    hide ctc
    a "it's so nice out here."
    a "i never seem to leave the palace anymore."
    a "it's hard work maintaining total control of a city."
    yd "what do you mean?"
    show az_idle_body_shock with dissolve
    a "I'm not sure if this is what other people call happiness, but I'm going to do everything in my control to make it be like this forever."
    hide az_idle_body_shock with dissolve
    a "Dear zuzu, our father won't live forever and when he croaks we can do whatever we want."
    a "By that time you'll be more accustomed to your life and I can allow you your full freedom again."
    y "sweet!"
    a "But if you stick it in another girl, She and her family will be killed...."
    yd "...."
    a "just a fair warning."
    show b2az b2az01 with dissolve
    "you walk in silence for a few minutes, just enjoying each other's company outside of the city."
    "you notice azula gently holding her stomach."
    y "you've been really wanting to get yourself pregnant.... why?"
    a "to Keep our bloodline pure."
    y "Are you sure it's not just another way of binding me to you?"
    a "....couldn't hurt. I need you and We'll need a successor so it all works out."
    a "besides, i think being bred by you is.... well, the idea makes me awfully wet."
    a "in fact...."
    scene black

    show expression "fbackgrounds/bk2_night01.jpg"
    show expression "bk2end/badend/idlestroll_moon.png"

    show b2az b2az01
    with Dissolve(2.0)
    a "i'm horny right now."
    a "what would you say to a blowjob?"
    yd "out here?"
    a "sure. there's no one around."
    a "let me suck you off. i'd love to have that taste in my mouth as we walk around."
    ys "well, i've never been one to turn down head from my sexy princess sister."
    a "queen. your sexy queen sister."
    y "right."
    hide b2az b2az01 with dissolve
    scene black
    scene bk2_night01
    show b2az b2az04
    with dissolve
    "azula kneels in front of you, almost in reverence."
    a "well?"
    show b2az_blink_ani
    a "get it out."
    show b2az_openmouth with dissolve
    show ctc
    pause
    hide ctc
    a "......"
    y "are you waiting for my cock?"
    a "uh-huh..."
    show b2az_solodick with dissolve
    "you pull out your cock put keep it just out of her reach."
    hide b2az_solodick
    show b2az_handson
    with ushake
    "she leans forward but you stop her."
    hide b2az_openmouth with dissolve
    a "hmm? what is it?"
    menu:
        "tell her you love her":
            y "i love you, azula."
            y "i think we may both be monsters...."
            y "but god help me, i love you."
            show b2az_blush with dissolve
            a "oh...."
            a "i...."
            a "...i love you too."
            a "now stop fucking around and work my mouth."
            hide b2az_solodick
            show b2az_openmouth
            show b2az_solodick
            hide b2az_handson
            with dissolve
        "nothing":

            y "nevermind, it's nothing."
            a "then stop fucking around and work my mouth."
            hide b2az_solodick
            show b2az_openmouth
            show b2az_solodick
            hide b2az_handson
            with dissolve

    ys "you want it?"
    a "ple-"

    hide b2az_solodick
    hide b2az_openmouth
    show b2az_bj_ani
    a "mmm!"
    show ctc
    pause
    hide ctc
    y "oh, sis... it's so perfect... "
    y "your mouth is so warm...."

    hide b2az_bj_ani
    show b2az_bj_ani2
    show b2az_blink with dissolve
    show ctc
    pause
    hide ctc
    a "*slurp* *gulp*"
    y "yes... yes..."
    hide b2az_bj_ani2
    show b2az_bj_ani3
    hide b2az_blink with dissolve
    show ctc
    pause
    hide ctc
    y "fuck... fuck..."
    a "hngh! mmngh! *sluurp*"
    hide b2az_bj_ani3
    show b2az_bj_ani4
    show b2az_blink with dissolve
    show ctc
    pause
    hide ctc
    "azula slurps and gags obediently as you slam your cock against the back of her throat."
    "her soft lips surround and suck at your shaft as you hump her unresisting face."
    a "*gltch* *gulp*"
    y "angh! i'm gonna cum!"
    hide b2az_blink with dissolve
    a "*slurp* mgh! *slurp* *gulp*"

    menu:
        "in her mouth":
            play sound "audio/splurt2.ogg"
            hide b2az_bj_ani4
            show az_knee_d4
            show b2az_blink
            with flash
            a "mgh!"
            a "*gulp* *gulp*"
            play sound "audio/splurt3.ogg"
            with flash
            hide b2az_blink with dissolve
            a "*gulp* *gulp* *gulp*"
            hide az_knee_d4
            show b2az_openmouth
            with dissolve
            if azula_preg:
                a "feed my baby!"
            play sound "audio/splurt2.ogg"
            hide b2az_blink
            show c_fuck_spermoutside_01 at Position (xpos = 0.42, xanchor=0.5, ypos=0.3, yanchor=0.5)
            with flash
            a "yes!"
            show ctc
            pause
            hide ctc
            hide b2az_openmouth with dissolve
            a "i wanted to taste it all..."
            a "...but at least my face is warm."
        "on her face":


            hide b2az_bj_ani4
            hide b2az_solodick
            show b2az_openmouth
            with dissolve
            a "give me your cum, brother!"
            if azula_preg:
                a "feed my baby!"
            play sound "audio/splurt2.ogg"
            hide b2az_blink_ani
            show c_fuck_spermoutside_01 at Position (xpos = 0.42, xanchor=0.5, ypos=0.21, yanchor=0.5)
            with flash
            a "fuck yes!"
            play sound "audio/splurt3.ogg"
            hide c_fuck_spermoutside_01

            show c_fuck_spermoutside_02 at Position (xpos = 0.42, xanchor=0.5, ypos=0.2, yanchor=0.5)
            show c_fuck_spermoutside_01 at Position (xpos = 0.42, xanchor=0.5, ypos=0.5, yanchor=0.5)
            with flash
            a "ohh....."
            show ctc
            pause
            hide ctc
            hide b2az_openmouth with dissolve
            a "i wanted to taste it..."
            a "...but at least my face is warm."

    show ctc
    pause
    hide ctc
    $ ds_battle_music = True
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
    play sound "audio/thud.mp3"
    hide c_fuck_spermoutside_02
    hide c_fuck_spermoutside_01
    hide b2az_blink_ani
    show b2az b2az03
    with sshake
    "suddenly azula is knocked out!"
    ya "what the hell!?"
    show b2az_nagashadow with Dissolve(2.0)
    ds "forget about me?"
    show ctc
    pause
    hide ctc
    jump zuko_ds_battle


label zuko_ds_battle:
    $ fight_naga = True
    jump fighttest


label zftavern_day20:
    scene bg_a_tavern with dissolve
    if not az_ty_resolve:
        $ az_ty_resolve = True
        show tf with dissolve
        t "hey, zuko!"
        g2 "hey, ty lee!"
        g1 "hi, ty lee!"
        g2 "watch it, bro."
        g1 "wait, you're into chicks?"
        g2 "everyone's into ty lee."
        show tf2
        hide tf
        with dissolve
        t "heehee."
        g1 "i have dibs, though."
        g2 "since when?"
        g1 "since.... now. dibs."
        g2 "wait, you can't-"
        g1 "dibs. i called dibs. dibs."
        g2 "it doesn't work like-"
        y "he called dibs, bro."
        g1 "i did. dibs."
        g2 "....man."
        g2 "alright, gotta respect a dib."
        g1 "it's not singular, you ballsack."
        yd "rrriiiight. so, anyway...."
        y "how are you, ty lee?"
        hide tf2
        show tf
        with dissolve
        t "fantastic!"
        t "i saw azula earlier today."
        t "she seems really happy lately, is that your doing?"
        y "i guess."
        y "i'm pretty happy too, truth be told."
        t "that's great!"
        hide tf
        show tfa
        with dissolve
        t "sorry to hear that azula won, though."
        yd "what do you mean?"
        t "well.... you're the older sibling, right? so you should have been firelord?"
        hide tfa
        show tf
        with dissolve
        t "but as long as you're happy, that's good."
        t "i {i}know{/i} azula is."
        t "i've seen her humming. humming!"
        t "she doesn't kill nearly as many peasants anymore, either."
        yd "....that's good...."
        t "yeah! so maybe things didn't turn out exactly.... how i expected...."
        t "but everything has definitely become better around here."
        t "so... good job!"
        yd "thanks. i think."
        t "well, i've gotta go serve some people celebrating our new firelord, but let me know if you need anything!"
        hide tf with dissolve


    menu:
        "serve drinks":
            jump barroom
        "drink with soldiers":

            fs1 "i wonder where that avatar kid is?"
            fs2 "dunno, but he's too chicken shit to take us on."
            fs1 "i hear he can't even firebend."
            fs2 "well, yeah. who's gonna teach him that?"
            yd "...."
            fs1 "oh, hello your highness. hard to see in here."
            fs2 "anyway, what firebender would teach the avatar, huh?"
            fs1 "what about the prince, here? he could show the avatar a thing or two, eh?"
            fs2 "hahaha that'd be the day!"
            yd "right..."
            jump zftavern_day20
        "gamble vs ty lee":

            show tf with dissolve
            $ bet_payout = 0
            y "up for a game of blackjack?"
            t "sure!"
            t "how much do you wanna bet?"
            menu:
                "10":
                    if fmoney >=10:
                        $ bet_payout = 10
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_day20
                "25":

                    if fmoney >=25:
                        $ bet_payout = 25
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_day20
                "50":

                    if fmoney >=50:
                        $ bet_payout = 50
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_day20
                "100":

                    if fmoney >=100:
                        $ bet_payout = 100
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_day20
        "exit":

            jump zaday

label zfalley_day20:
    if lia_freed:
        show bg_a_prison_inside with dissolve
        yd "wow, these alleys are shit."
        yd "the buildings have bars on them.... hobos have hay beds...."
        yd "it's basically prison out here."
        g2 "poverty is a different kind of prison."
        g1 "....that was deeper than i expected."
        g2 "so's your mum lol."
        g1 "aaand back to normal."
        show l2s
        with dissolve
        p "hey!"
        y "sup?"
        g1 "you!"
        p "since you're my savior.... wanna fuck?"
        yg "seriously? that's awesome-"
        g1 "ahem."
        yc "i mean... no...."
        g1 "atta boy."
        p "aw...."
        y "sorry, i'm a kept man now."
        p "as long as you're happy!"
        jump zaday
    else:
        show bg_a_prison_inside with dissolve
        yd "wow, these alleys are shit."
        yd "the buildings have bars on them.... hobos have hay beds...."
        yd "it's basically prison out here."
        g2 "poverty is a different kind of prison."
        g1 "....that was deeper than i expected."
        g2 "so's your mum lol."
        g1 "aaand back to normal."
        jump zaday

label zfprison_day20:
    scene black
    scene bg_a_prison_inside
    with dissolve
    menu:
        "visit lia" if lia_caught:
            show l2s with dissolve
            p "hello again!"
            g1 "hands to yourself, prisoner."
            g2 "more like \"hands to {i}myself{/i}\", eh?"
            g1 "...what?"
            g2 "i'm saying she can touch my-"
            y "you seem chipper, lia."
            p "azula's been feeding me a lot more lately!"
            p "she's even letting me wander outside a bit."
            p "i'm not sure what's gotten into her, but i'm pretty happy."
            y "that's great!"
            p "it really is. i'm basically free, this place is sort of just my home now."
            p "i'm gonna try to put my life of sex behind me."
            yd "....that sounds terrible."
            p "i think i'm going to spend some time working on me, you know?"
            p "becoming a more whole person."
            yd "i mean, do you."
            p "actually, i'm planning to stop that, too."
            yd "stop...."
            ya "stop masturbating!?"
            y "i.... can't handle this."
            g2 "me neither. it's my only outlet."
            y "good luck on your new life."
            p "thanks! you too!"
            jump zaday
        "visit iroh's cell":

            show irpr irpr03 with dissolve
            "you find a note in iroh's cell."
            y "\"dear nephew, i'd hoped for so much more from you, but i understand.\""
            y "\"i hope you find what you seek. we may meet again some day.\""
            y "....i guess he escaped. i hope i see him again eventually."
            jump zaday

label zfarmory_day20:
    if not mai_gone:
        $ mai_gone = True
        scene bg_a_armory with dissolve
        yc "....mai?"
        show mf with dissolve
        m "hello, zuko."
        m "i wondered when you'd come see me."
        yc "hey. i'm sorry."
        show mf2
        hide mf
        with dissolve
        m "why?"
        m "you've chosen azula. it.... hurts...."
        m "but i understand. she's beautiful and powerful.... and family...."
        show mf
        hide mf2
        with dissolve
        m "how could i compete?"
        y "i'm glad you understand-"
        show mfa
        hide mf
        with dissolve
        m "i mean, why wouldn't you abandon me?"
        yc "i-"
        m "break my heart without even having the guts to tell me to my face?"
        yc "i'm sorry."
        m "don't worry about it."
        m "i hope you're happy, zuko. i really do."
        y "mai...."
        show mf2
        hide mfa
        with dissolve
        m "i think.... i'm going to go away for a while."
        m "maybe to ember island.... maybe somewhere.... farther."

        m "i thought we might go together, but.... that was a foolish dream."
        show mf
        hide mf2
        with dissolve
        m "i don't blame you, though."
        y "it would never have worked between us."
        y "i was in a difficult position. i went with what i thought was best."
        m "i know."
        hide mf with dissolve
        show ml with dissolve
        m "i hope azula treats you well. she certainly seems happier than i've ever seen her."
        m "you're good for her. you two work."
        m "i wish you all the best, zuko."
        m "now, i think you should go."
        y "mai-"
        show ml2
        hide ml
        with dissolve
        m "it's too late, zuko. you made your choice. and i respect it."
        m "please respect mine."
        y ".....okay."
        show ml
        hide ml2
        with dissolve
        m "goodbye, zuko."
        jump zaday
    else:

        y "there's a note on the door...."
        y "\"goodbye, zuko. -mai\""
        yc "i guess... she left the city."
        jump zaday


label zftraining_day20:
    show al_blink with dissolve
    a "helloooo handsome."
    y "well, you're in a good mood."
    a "of course, i'm the firelord. why wouldn't i be happy?"
    a "but why are you out here?"
    y "just walking around. why are {i}you{/i} out here?"
    show ale
    hide al_blink
    with dissolve
    a "hmm.... i suppose you could call it \"maintenance\"."
    a "perfection comes naturally to me, of course.... but training helps keep one sharp."
    y "want to show me some moves?"
    a "oh, zuko."
    show al_blink
    hide ale
    with dissolve
    a "that won't help anything. i'm sorry, but we both know i'm the stronger of us."
    y "well, then teach me something."
    a "i just don't see the point, brother."
    a "oh, how are the guards working out?"
    menu:
        "they suck":
            y "they're a little lame."
            g2 "i'm.... i'm right here."
            g2 "why would you say that?"
            y "see?"
        "i kinda like them":

            y "we're getting along fine."
            g2 "the three amigos!"
            g2 "the three musketeers!"
            g2 "the three blind mice!"
            g2 "the three... some?"
            y "okay, i like them a little less."

    a "yes, they're imbeciles. i'm sorry."
    g1 "...that's fine, i don't need self-esteem."
    g2 "hey! you made a joke!"
    g1 "i really didn't."
    a "so, guards, how has zuko been doing?"
    y "i'm right here, you know."
    a "you're biased."
    yd "....."
    y "fair."
    g1 "he's doing excellently.... your excellency."
    g2 "nice."
    a "i can't believe i have to converse with you."
    g1 "i know you can't tell but i'm crying in my helmet."
    g2 "let it out, bill. she can't hurt you if you don't let her."
    a "wrong."
    a "but i'll let that slide."
    a "well, i'm happy to see you zuko...."
    a "but, i'd like a little practice time, and, well...."
    a "that cute butt is a little distracting."
    yd "i have a cute butt?"
    a "very cu-"
    g2 "yes."
    a "....."
    g1 "....."
    y "....."
    g2 "....."
    g2 "i stand by it."
    a "i'll see you later, zuzu."

    jump zaday

label zffarm_day20:
    yd "....the doors are locked."
    g1 "sorry, your highness. azula has shut down the farm."
    yd "why?"
    g1 "well... we're winning the war."
    g1 "don't need to breed the cows anymore."
    g2 "plus, i'm pretty sure azula wants your bangers and mash on lockdown."
    yd "...."
    g1 "bro!"
    g2 "what, bro?"
    g1 "that's unprofessional!"
    g2 "...."
    g2 "can you not just be cool?"
    g2 "just once. just one time."
    g2 "just one time can you be cool."
    g1 "will you-"
    g2 "just one time."
    g1 "...."
    g2 "...."
    g1 "...."
    g1 "well-"
    g2 "canyoujustonetimebecool-"
    g1 "agh! shut up!"
    y "it's alright, guys. farm's shut down. I just remembered azula mentioning it, anyway."
    jump zaday

label zfalley_night20:
    show shadyguy_grin with dissolve
    sg "hey, man. tough luck."
    yd "what?"
    sg "your sister made you her bitch."
    sg "totally backwards from what i expected."
    yd "i'm not her bitch."
    sg "sure, sure. as long as everyone's happy, right?"
    yd "...."
    sg "so, are you gonna buy-"
    show shadyguy_unsure
    hide shadyguy_grin
    with dissolve
    sg "are those guards?"
    g1 "yeah, and i'm doing my best to ignore this situation."
    g2 "hey.... do you have any fermented crab?"
    sg "i do-"
    g1 "it's illegal."
    sg "-not. i do not have fermented crab. you should have let me finish."
    g1 "prince, if this guy doesn't get out of here immediately, i'm gonna arrest him."
    sg "....i should go."
    hide shadyguy_unsure with dissolve
    y "aw, man.... bye shady."
    jump zanight

label zfarmory_night20:
    if not mai_gone:
        $ mai_gone = True
        scene bg_a_armory with dissolve
        yc "....mai?"
        show mf with dissolve
        m "hello, zuko."
        m "i wondered when you'd come see me."
        yc "hey. i'm sorry."
        show mf2
        hide mf
        with dissolve
        m "why?"
        m "you've chosen azula. it.... hurts...."
        m "but i understand. she's beautiful and powerful.... and family...."
        show mf
        hide mf2
        with dissolve
        m "how could i compete?"
        y "i'm glad you understand-"
        show mfa
        hide mf
        with dissolve
        m "i mean, why wouldn't you abandon me?"
        yc "i-"
        m "break my heart without even having the guts to tell me to my face?"
        yc "i'm sorry."
        m "don't worry about it."
        m "i hope you're happy, zuko. i really do."
        y "mai...."
        show mf2
        hide mfa
        with dissolve
        m "i think.... i'm going to go away for a while."
        m "maybe to ember island.... maybe somewhere.... farther."

        m "i thought we might go together, but.... that was a foolish dream."
        show mf
        hide mf2
        with dissolve
        m "i don't blame you, though."
        y "it would never have worked between us."
        y "i was in a difficult position. i went with what i thought was best."
        m "i know."
        hide mf with dissolve
        show ml with dissolve
        m "i hope azula treats you well. she certainly seems happier than i've ever seen her."
        m "you're good for her. you two work."
        m "i wish you all the best, zuko."
        m "now, i think you should go."
        y "mai-"
        show ml2
        hide ml
        with dissolve
        m "it's too late, zuko. you made your choice. and i respect it."
        m "please respect mine."
        y ".....okay."
        show ml
        hide ml2
        with dissolve
        m "goodbye, zuko."
        jump zanight
    else:

        y "there's a note on the door...."
        y "\"goodbye, zuko. -mai\""
        yc "i guess... she left the city."
        jump zanight

label zffarm_night20:
    yd "....the doors are locked."
    g1 "sorry, your highness. azula has shut down the farm."
    yd "why?"
    g1 "well... we're winning the war."
    g1 "don't need to breed the cows anymore."
    g2 "plus, i'm pretty sure azula wants your bangers and mash on lockdown."
    yd "...."
    g1 "bro!"
    g2 "what, bro?"
    g1 "that's unprofessional!"
    g2 "...."
    g2 "can you not just be cool?"
    g2 "just once. just one time."
    g2 "just one time can you be cool."
    g1 "will you-"
    g2 "just one time."
    g1 "...."
    g2 "...."
    g1 "...."
    g1 "well-"
    g2 "canyoujustonetimebecool-"
    g1 "agh! shut up!"
    y "it's alright, guys. farm's shut down. I just remembered azula mentioning it, anyway."
    jump zanight

label zfprison_night20:
    scene black
    scene bg_a_prison_inside
    with dissolve
    menu:
        "visit lia" if lia_caught:
            show l2s with dissolve
            p "hello again!"
            g1 "hands to yourself, prisoner."
            g2 "more like \"hands to {i}myself{/i}\", eh?"
            g1 "...what?"
            g2 "i'm saying she can touch my-"
            y "you seem chipper, lia."
            p "azula's been feeding me a lot more lately!"
            p "she's even letting me wander outside a bit."
            p "i'm not sure what's gotten into her, but i'm pretty happy."
            y "that's great!"
            p "it really is. i'm basically free, this place is sort of just my home now."
            p "i'm gonna try to put my life of sex behind me."
            yd "....that sounds terrible."
            p "i think i'm going to spend some time working on me, you know?"
            p "becoming a more whole person."
            yd "i mean, do you."
            p "actually, i'm planning to stop that, too."
            yd "stop...."
            ya "stop masturbating!?"
            y "i.... can't handle this."
            g2 "me neither. it's my only outlet."
            y "good luck on your new life."
            p "thanks! you too!"
            jump zanight
        "visit iroh's cell":

            show irpr irpr03 with dissolve
            "you find a note in iroh's cell."
            y "\"dear nephew, i'd hoped for so much more from you, but i understand.\""
            y "\"i hope you find what you seek. we may meet again some day.\""
            y "....i guess he escaped. i hope i see him again eventually."
            jump zanight

label zftavern_night20:
    scene bg_a_tavern with dissolve
    if not az_ty_resolve:
        $ az_ty_resolve = True
        show tf with dissolve
        t "hey, zuko!"
        g2 "hey, ty lee!"
        g1 "hi, ty lee!"
        g2 "watch it, bro."
        g1 "wait, you're into chicks?"
        g2 "everyone's into ty lee."
        show tf2
        hide tf
        with dissolve
        t "heehee."
        g1 "i have dibs, though."
        g2 "since when?"
        g1 "since.... now. dibs."
        g2 "wait, you can't-"
        g1 "dibs. i called dibs. dibs."
        g2 "it doesn't work like-"
        y "he called dibs, bro."
        g1 "i did. dibs."
        g2 "....man."
        g2 "alright, gotta respect a dib."
        g1 "it's not singular, you ballsack."
        yd "rrriiiight. so, anyway...."
        y "how are you, ty lee?"
        hide tf2
        show tf
        with dissolve
        t "fantastic!"
        t "i saw azula earlier today."
        t "she seems really happy lately, is that your doing?"
        y "i guess."
        y "i'm pretty happy too, truth be told."
        t "that's great!"
        hide tf
        show tfa
        with dissolve
        t "sorry to hear that azula won, though."
        yd "what do you mean?"
        t "well.... you're the older sibling, right? so you should have been firelord?"
        hide tfa
        show tf
        with dissolve
        t "but as long as you're happy, that's good."
        t "i {i}know{/i} azula is."
        t "i've seen her humming. humming!"
        t "she doesn't kill nearly as many peasants anymore, either."
        yd "....that's good...."
        t "yeah! so maybe things didn't turn out exactly.... how i expected...."
        t "but everything has definitely become better around here."
        t "so... good job!"
        yd "thanks. i think."
        t "well, i've gotta go serve some people celebrating our new firelord, but let me know if you need anything!"
        hide tf with dissolve

    if not azula_chosen_drunk:
        $ azula_chosen_drunk = True
        show afl with dissolve
        a "drinks all around!"
        "azula waves a mug of ale as the tavern's patrons cheer."
        ys "you okay, sis?"
        a "me? i'm grreeat! we're drinking!"
        ys "i see that. any particular reason?"
        a "why not? huh? you gonna fight me?"
        a "i'm gonna... i'm...."
        show aub
        hide afl
        with dissolve
        a "i dun feel so good."
        yc "like you need to throw up?"
        a "nn... no. that's not it."
        a "...."
        hide aub with vshake
        "azula throws up."
        yd "....yeah."
        show aub with dissolve
        a "can... can go... can help me home?"
        yd "wow, you're a mess."
        a "i dun like it."
        scene black with dissolve
        show azsl azsl02 with dissolve
        menu:
            "cop a feel":
                show azsl azsl03 with dissolve
                "you pull up azula's top and squeeze her tits."
                a "i like.... like that you like me...."
                a "s'good."
                a "{size=+4}*buurp*"
            "don't squeeze her boob":

                "you decide to be a gentleman and leave her covered."

        a "spin.... spinning...."
        y "i know."
        a "i'm not drunk, you know. i'm fine. i'm fine. so fine. good."
        ys "yeah, i know."
        a "still spinning. think i'm gonna throw up again."
        show azsl_eyeshalfopen with dissolve
        a "stay...? will you stay?"
        y "well, yeah. we share a bed, now."
        hide azsl_eyeshalfopen with dissolve
        a "oh..."
        a "yay."
        "azula promptly falls asleep, refusing to roll over."
        "you sleep next to her, right on the edge of the bed."
        jump zaday

    menu:
        "serve drinks":
            jump barroom
        "drink with soldiers":

            fs1 "i wonder where that avatar kid is?"
            fs2 "dunno, but he's too chicken shit to take us on."
            fs1 "i hear he can't even firebend."
            fs2 "well, yeah. who's gonna teach him that?"
            yd "...."
            fs1 "oh, hello your highness. hard to see in here."
            fs2 "anyway, what firebender would teach the avatar, huh?"
            fs1 "what about the prince, here? he could show the avatar a thing or two, eh?"
            fs2 "hahaha that'd be the day!"
            yd "right..."
            jump zftavern_night20
        "gamble vs ty lee":

            show tf with dissolve
            $ bet_payout = 0
            y "up for a game of blackjack?"
            t "sure!"
            t "how much do you wanna bet?"
            menu:
                "10":
                    if fmoney >=10:
                        $ bet_payout = 10
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_night20
                "25":

                    if fmoney >=25:
                        $ bet_payout = 25
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_night20
                "50":

                    if fmoney >=50:
                        $ bet_payout = 50
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_night20
                "100":

                    if fmoney >=100:
                        $ bet_payout = 100
                        jump bjstart
                    else:
                        t "you don't have enough!"
                        jump zftavern_night20
        "exit":

            jump zanight

label zftraining_night20:
    "the grounds are quiet. there's no one here."

    jump zanight
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
