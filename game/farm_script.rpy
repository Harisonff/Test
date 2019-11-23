init:
    $ girl1 = False
    $ girl2 = False
    $ girl3 = False
    $ girl4 = False
    $ girl5 = False
    $ girl6 = False
    $ girl7 = False
    $ girl8 = False
    $ girl9 = False
    $ girl10 = False
    $ girl11 = False
    $ girl12 = False
    $ girl13 = False
    $ girl14 = False
    $ girl15 = False
    $ girl16 = False
    $ girl17 = False
    $ girl18 = False
    $ girl19 = False
    $ girl20 = False
    $ girl21 = False
    $ girl22 = False
    $ girl23 = False
    $ girl24 = False
    $ girl25 = False
    $ girl26 = False
    $ girl27 = False
    $ girl28 = False
    $ girl29 = False
    $ girl30 = False
    $ girl31 = False
    $ girl32 = False
    $ girl33 = False
    $ girl34 = False
    $ girl35 = False
    $ girl36 = False
    $ girl37 = False
    $ girl38 = False
    $ girl39 = False
    $ girl40 = False
    $ girl41 = False
    $ girl42 = False
    $ girl43 = False
    $ girl44 = False
    $ girl45 = False
    $ girl46 = False
    $ girl47 = False
    $ girl48 = False
    $ girl49 = False
    $ girl50 = False
    $ girl51 = False
    $ girl52 = False
    $ girl53 = False
    $ girl54 = False
    $ girl55 = False
    $ girl56 = False
    $ girl57 = False
    $ girl58 = False
    $ girl59 = False
    $ girl60 = False
    $ girl61 = False
    $ girl62 = False
    $ girl63 = False
    $ girl64 = False
    $ girl65 = False
    $ girl66 = False
    $ girl67 = False
    $ girl68 = False
    $ girl69 = False
    $ girl70 = False
    $ girl71 = False
    $ girl72 = False
    $ girl73 = False
    $ girl74 = False
    $ girl75 = False
    $ girl76 = False
    $ girl77 = False
    $ girl78 = False
    $ girl79 = False
    $ girl80 = False
    $ girl81 = False
    $ girl82 = False
    $ girl83 = False
    $ girl84 = False
    $ girl85 = False
    $ girl86 = False
    $ girl87 = False
    $ girl88 = False
    $ girl89 = False
    $ girl90 = False
    $ girl91 = False
    $ girl92 = False
    $ girl93 = False
    $ girl94 = False
    $ girl95 = False
    $ girl96 = False
    $ girl97 = False
    $ girl98 = False
    $ girl99 = False
    $ milked = 0
    $ milked_today_used = False
    $ milked_today_pregnant = False
    $ zuko = 0
    $ cow = Character("cow", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)


image farm_hall = LiveComposite(
    (1000, 720),
    (0, 0), "fbackgrounds/bg_a_farm_mainhall.jpg",
    (0, 0), "farm/farmgirls_all.png",
    )

label farm_script:
    if mai_thefts3:
        show farm_hall with dissolve
        y "okay, gotta talk to one of the cows."
        menu:
            "fresh cow":
                show fc1 with dissolve
                y "do you know anything about any thefts?"
                cow "moo."
                y "come one, answer the-"
                cow "moo."
                y "stop being difficult-"
                cow "moo. moo. moo."
                y "fine."
                menu:
                    "pregnant cow":
                        show pctit1 with dissolve
                        y "do you know anything about any thefts?"
                        cow "moo."
                        y "come one, answer the-"
                        cow "moo."
                        y "stop being difficult-"
                        cow "moo. moo. moo."
                        y "fine."
                        menu:
                            "used cow":
                                show uc1 with dissolve
                                y "do you know anything about any thefts?"
                                cow "yes! finally!"
                                cow "there's a whole conspiracy!"
                                y "...there is?"
                                cow "yes! there's a guard in on it, and no one will listen to me."
                                y "i'm listening."
                                cow "some of the cows are stockpiling weapons, provided by a guard."
                                y "which guard?"
                                cow "the one on duty now."
                                y "thank you."
                                cow "can you... milk me a little?"
                                y "another time."
                                jump guard_caught
                    "used cow":

                        show uc1 with dissolve
                        y "do you know anything about any thefts?"
                        cow "yes! finally!"
                        cow "there's a whole conspiracy!"
                        y "...there is?"
                        cow "yes! there's a guard in on it, and no one will listen to me."
                        y "i'm listening."
                        cow "some of the cows are stockpiling weapons, provided by a guard."
                        y "which guard?"
                        cow "the one on duty now."
                        y "thank you."
                        cow "can you... milk me a little?"
                        y "another time."
                        jump guard_caught
            "pregnant cow":


                show pctit1 with dissolve
                y "do you know anything about any thefts?"
                cow "moo."
                y "come one, answer the-"
                cow "moo."
                y "stop being difficult-"
                cow "moo. moo. moo."
                y "fine."
                menu:
                    "fresh cow":
                        show fc1 with dissolve
                        y "do you know anything about any thefts?"
                        cow "moo."
                        y "come one, answer the-"
                        cow "moo."
                        y "stop being difficult-"
                        cow "moo. moo. moo."
                        y "fine."
                        menu:
                            "used cow":
                                show uc1 with dissolve
                                y "do you know anything about any thefts?"
                                cow "yes! finally!"
                                cow "there's a whole conspiracy!"
                                y "...there is?"
                                cow "yes! there's a guard in on it, and no one will listen to me."
                                y "i'm listening."
                                cow "some of the cows are stockpiling weapons, provided by a guard."
                                y "which guard?"
                                cow "the one on duty now."
                                y "thank you."
                                cow "can you... milk me a little?"
                                y "another time."
                                jump guard_caught
                    "used cow":

                        show uc1 with dissolve
                        y "do you know anything about any thefts?"
                        cow "yes! finally!"
                        cow "there's a whole conspiracy!"
                        y "...there is?"
                        cow "yes! there's a guard in on it, and no one will listen to me."
                        y "i'm listening."
                        cow "some of the cows are stockpiling weapons, provided by a guard."
                        y "which guard?"
                        cow "the one on duty now."
                        y "thank you."
                        cow "can you... milk me a little?"
                        y "another time."
                        jump guard_caught
            "used cow":

                show uc1 with dissolve
                y "do you know anything about any thefts?"
                cow "yes! finally!"
                cow "there's a whole conspiracy!"
                y "...there is?"
                cow "yes! there's a guard in on it, and no one will listen to me."
                y "i'm listening."
                cow "some of the cows are stockpiling weapons, provided by a guard."
                y "which guard?"
                cow "the one on duty now."
                y "thank you."
                cow "can you... milk me a little?"
                y "another time."
                jump guard_caught
    else:

        jump farm_script2

label farm_script2:
    show farm_hall with dissolve
    $ farm_visited = True
    "you have [total_girls] girls total."




    menu:
        "ask guard questions about the farm":
            jump g_questions
        "visit fresh cows - [fresh_girls]":
            if fresh_girls >=1:
                show fc1 with dissolve
                hide farm_hall
                jump farm_fresh
            else:
                "you don't have any..."
                jump farm_script
        "visit used cows - [used_girls]":
            if used_girls >=1:
                show uc1 with dissolve
                hide farm_hall
                jump farm_used
            else:
                "you don't have any..."
                jump farm_script
        "visit pregnant cows - [pregnant_girls]":
            if pregnant_girls >=1:
                show pctit1 with dissolve
                hide farm_hall
                jump farm_preg
            else:
                "you don't have any..."
                jump farm_script
        "milk used and pregnant girls together via lever":
            if milked_today_used and milked_today_pregnant:
                y "i've already milked them today."
                y "i should give them the chance to refill."
                jump farm_script
            if milked_today_used:
                y "i've already milked the used girls... i should visit the pregnant ones for the rest."
                jump farm_script
            if milked_today_pregnant:
                y "i've already milked the pregnant girls... i should visit the used ones for the rest."
                jump farm_script
            else:
                "instead of visiting them individually, you pull the large lever labeled \"milk cows\"."
                "you hear a loud united gasp as the milk is forcefully pumped out of their tits."
                $ milked_today_used = True
                $ milked_today_pregnant = True
                $ milked += pregnant_girls
                $ milked += used_girls
                "you currently have [milked] milkings."
                jump farm_script
        "exit":
            if fdaytime:
                if thief > zuko:
                    jump city
                else:
                    jump zcity1
            else:
                if thief > zuko:
                    jump city_night
                else:
                    jump zcity_night1














label farm_fresh:
    if fresh_girls >=1:
        menu:
            "fresh cows"
            "taunt":

                y "you're going to help the fire nation grow powerful, earth slut."
                cow "i... i am?"
                y "yes... your new role is to be fucked until you're pregnant..."
                y "fucked while you're pregnant..."
                y "and fucked pregnant again."
                cow "no...."
                y "oh yes. and it's going to be fun."
                y "your purpose is to breed powerful firebenders."
                y "and i will provide the semen... forcefully."
                cow "this can't be real..."
                y "i assure you it is."
                y "you are a cow."
                y "with one purpose."
                y "and i will not be gentle."
                cow "no.... *sob*"
                $ morality -=1
                "you got -1 morality."
                jump farm_fresh
            "comfort":

                y "how are you?"
                cow "what are you... going to do to me?"
                cow "are you going to hurt me?"
                y "nah, don't worry. i'll take good care of you."
                y "you're safe here."
                cow "i am?"
                y "yeah, of course."
                y "i can't promise what's going to happen to you-"
                cow "huh?"
                y "but you're in good hands."
                cow "..."
                jump farm_fresh
            "fuck":


                menu:
                    "use breast milk as lube":
                        show fc2 with dissolve
                        y "you see this breast milk?"
                        hide fc1
                        cow "yes..."
                        y "this is your future."
                        y "you are here to make this."
                        y "you seem to need a little lubrication... so this seemed appropriate."
                        cow "lu...lubrication?"
                        y "oh, didn't i tell you?"
                        y "i'm going to fuck you pregnant."
                        cow "no! please! i don't want to get pregnant!"
                        y "that's not up to you."
                        cow "please! i'm still so young..."
                        y "and in..."
                        show fc3 with dissolve
                        hide rc_rub
                        cow "ah!!!"
                        y "we..."
                        cow "no! stop!"
                        show fc4
                        with ushake
                        y "go!"
                        hide fc3
                        hide fc2
                        cow "ah!!"
                        y "mmm...you are young. you have the tightest pussy."
                        y "i'm just going to wreck it, i'll be with you in a minute."
                        show fc_fuck
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        cow "wait! I-"
                        y "what did i just say? shut up until i'm done."
                        y "and then we're going to milk you."
                        cow "please! you're too big! it hurts so much!"
                        y "ahh... yeah... there we go..."
                        cow "ow! ow! stop! stop! i don't want this!"
                        y "and. here. it..."
                        hide fc_fuck
                        with vshake
                        y "cums!"
                        play sound "audio/splurt3.ogg"
                        with flash
                        cow "ah!!"
                        play sound "audio/splurt2.ogg"
                        with flash
                        cow "no!"
                        play sound "audio/splurt1.ogg"
                        with flash
                        cow "*sob*"
                        play sound "audio/splurt3.ogg"
                        with flash
                        y "good cow."
                        y "we'll start milking you soon."
                        cow "*sob*"
                        $ morality -=1
                        "you got -1 morality."
                        hide fc4
                        jump fresh_girl_select
                    "rub your cock against her labia":

                        show fc2 with dissolve
                        "you pull out your cock and begin to rub it against her lips."
                        hide fc1
                        show fc_rub
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        cow "no! please! i don't want to get pregnant!"
                        y "that's not up to you."
                        cow "please! i'm still so young..."
                        y "and very wet. it seems you really enjoy grinding against cock."
                        cow "no! no!"
                        y "and in..."
                        show fc3 with dissolve
                        hide rc_rub
                        cow "ah!!!"
                        y "we..."
                        cow "no! stop!"
                        show fc4
                        with ushake
                        y "go!"
                        hide fc3
                        hide fc2
                        cow "ah!!"
                        y "mmm...you are young. you have the tightest pussy."
                        y "i'm just going to wreck it, i'll be with you in a minute."
                        show fc_fuck
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        cow "wait! I-"
                        y "what did i just say? shut up until i'm done."
                        y "and then we're going to milk you."
                        cow "please! you're too big! it hurts so much!"
                        y "ahh... yeah... there we go..."
                        cow "ow! ow! stop! stop! i don't want this!"
                        y "and. here. it..."
                        hide fc_fuck
                        with vshake
                        y "cums!"
                        play sound "audio/splurt3.ogg"
                        with flash
                        cow "ah!!"
                        play sound "audio/splurt2.ogg"
                        with flash
                        cow "no!"
                        play sound "audio/splurt1.ogg"
                        with flash
                        cow "*sob*"
                        play sound "audio/splurt3.ogg"
                        with flash
                        y "good cow."
                        y "we'll start milking you soon."
                        cow "*sob*"
                        $ morality -=1
                        "you got -1 morality."
                        hide fc4
                        jump fresh_girl_select
            "set free":

                $ morality +=1
                $ total_girls -=1
                $ fresh_girls -=1
                "you set her free!"
                "you got +1 morality."
                jump farm_script
            "back":

                hide fc1
                hide bg_a_farm_singlegirl
                jump farm_script
    else:

        "you don't have any..."
        jump farm_script

label farm_used:
    if used_girls >=1:

        menu:
            "used cows"
            "talk":

                y "hello, cow."
                cow "mooooo...."
                y "who's a good girl?"
                cow "moo?"
                y "that's right, it's you!"
                cow "mooo!"
                jump farm_used
            "milk used cows":

                if milked_today_used:
                    y "i've already milked the used cows today..."
                    jump farm_used
                else:
                    menu:
                        "milk her":
                            $ milked += used_girls
                            $ milked_today_used = True
                            cow "please milk me, my breasts are so swollen."
                            cow "please, i need it!"
                            show uc_milk with dissolve
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            "you milk the cow, squeezing her engorged breasts."
                            "you empty her tit cream into the bucket."
                            show ctcblink
                            $ renpy.pause()
                            hide ctcblink
                            "the girl sighs in relief."
                            cow "thank you, owner."
                            y "what was that?"
                            cow "moo! :)"
                            "you got [used_girls] milkings from the used cows."
                            hide uc_milk
                            jump farm_used
                        "play with her nipples":

                            $ milked += used_girls
                            $ milked_today_used = True
                            show uctit1 with dissolve
                            y "hmm..."
                            cow "(...please...)"
                            show uctit2 with dissolve
                            cow "yes...."
                            hide uctit1
                            show uctit
                            cow "ohhhhh..!!"
                            cow "yes!"
                            cow "yes! yes!"
                            cow "ohhh... it's so good..."
                            cow "that's it! just like that!"
                            y "who's a good cow?"
                            cow "i am!"
                            cow "i'm a good cow! i'm a good cow!"
                            cow "ahh..ah...ah...ohh...mooo..oh.."
                            cow "here it... moooo... oh... ah!! ah!!"
                            cow "mooo! moo!!"
                            show uctit5 with dissolve
                            "she cums all over the floor, and squirts a good bit of milk..."
                            hide uctit
                            "luckily, you were prepared for it, and catch it all in the bucket."
                            y "can't let your tit cream go to waste, now can we?"
                            cow "mooooo!!! :)"
                            "you got [used_girls] milkings from the used cows."
                            hide uctit2
                            hide uctit5 with dissolve
                            jump farm_used
            "fuck":


                show fc1 with dissolve
                cow "this is my place."
                show fc2 with dissolve
                cow "i'm a useless slut."
                hide fc1
                show fc_rub
                cow "my only purpose is to bear your child."
                cow "please enter me."
                show fc3 with dissolve
                cow "ohhh..."
                hide fc_rub
                hide fc2
                cow "yes..."
                cow "more, please... please!"
                show fc4 with ushake
                cow "{size=+4}yes!"
                hide fc3
                show fc_fuck
                cow "mmoooooo...."
                cow "ohhhh...."
                cow "thank you, master."
                cow "unnnghhh...."
                cow "you're so filling..."
                cow "fuck your cow."
                cow "fuck your useless cow."
                cow "give me purpose."
                cow "thank you."
                cow "thank you."
                cow "thank you."
                cow "thank you. thank you. thank you. thank you. thank you. thank you. thank you. thank you. thank you. thank you."
                y "ungh..."
                cow "yes! empty your cock into me!"
                cow "please empty into me!"
                cow "let me drain you!"
                cow "give me your cum!"
                cow "let me bear you a powerful heir!"
                hide fc_fuck
                with vshake
                cow "that's it, master."
                play sound "audio/splurt3.ogg"
                with flash
                y "ngh!"
                cow "empty into me, sir."
                play sound "audio/splurt2.ogg"
                with flash
                cow "i'm so lucky."
                play sound "audio/splurt3.ogg"
                with flash
                cow "thank you, master... give me all of your precious seed."
                play sound "audio/splurt1.ogg"
                with flash
                y "ahhh...."
                cow "don't stop, master, please."
                y "...i'm done..."
                y "...you're going to need to stop squeezing."
                cow "no sir, more cum, sir."
                y "i'm... out."
                cow "please master."
                cow "mmoooo."
                cow "i'll moo for you."
                cow "mmmmmmmooooooooooo!!!!"
                y "that's nice... but i'm tapped out."
                cow "...oh..."
                show fc2 with dissolve
                y "i promise to come fuck you again."
                hide fc4
                cow "...really?"
                show fc1 with dissolve
                hide fc2
                cow "oh thank you, sir!"
                cow "mmoooo!!"
                hide fc1 with dissolve

                jump used_girl_select
            "set free":

                y "you're free."
                cow "but... where will i go?"
                cow "i'm used up."
                cow "i'm only good for dumping cum and milking."
                cow "you have \"broken\" me, sir."
                cow "i'm only good for being ridden."
                y "you can have a better life somewhere else."
                cow "*sob* was i not good enough?"
                cow "mooooo!!!"
                cow "i can be better!!"
                cow "mooooo!!!"
                y "leave, and find a new master."
                cow "you think there's one out there for me?"
                y "i do."
                cow "if you say so, master."
                $ used_girls -=1
                $ total_girls -=1
                jump farm_used
            "back":

                jump farm_script
    else:

        "you don't have any..."
        jump farm_script

label farm_preg:
    menu:
        "pregnant cows"
        "taunt":

            y "how is it being pregnant by a firebender, earth slut?"
            cow "..."
            y "that's right... you're going to make the fire nation very powerful..."
            y "by having your pussy recklessly abused."
            cow "no...."
            y "oh yes. and your pregnancy is going to be fast..."
            y "so i can pump you full over and over and over again."
            cow "how can you do this...?"
            y "you'll soon break... and come to love it."
            y "you are a cow."
            y "with one purpose."
            cow "...*sob*..."
            y "now, \"moo\" for me."
            cow "{size=-5}moo...."
            y "again, louder."
            cow "moo."
            y "louder!"
            cow "..."
            cow "{size=+5}mmmmmmoooooooooo!!!"
            y "good girl."
            cow "*sob*"
            $ morality -=1
            "you got -1 morality."
            jump farm_preg
        "comfort":

            y "how are you?"
            cow "are you... here to... hurt me?"
            y "hurt you?"
            y "i'm here to take care of you."
            y "make sure you're safe and warm."
            cow "you are?"
            y "absolutely."
            y "i will fill you up again and again..."
            cow "..."
            y "but i'll take care of you."
            cow "..."
            jump farm_preg
        "milk pregnant cows":

            if milked_today_pregnant:
                y "i've already milked the pregnant cows today..."
                jump farm_script
            else:
                $ milked += pregnant_girls
                $ milked_today_pregnant = True
                "you approach one of the cows. and firmly grip her swollen breasts."
                menu:
                    "play with her nipples":
                        show pctit with dissolve
                        "you suddenly pinch her nipples and she gasps and tries to struggle away uselessly."
                        "pulling and twisting on her swollen pink areolas, milk leaks out onto your hand."
                        cow "ohhh...."
                        "her initial resistance turns into soft moans as you fondle and pinch her nipples."
                        cow "ah....ah....ah...i'm..."
                        menu:
                            "let her cum":
                                "your steady handling of her swollen nipples has her rocking in her harness."
                                "her moans reverberate through the other stalls where the other cows are desperate to get off."
                                cow "ah!...ah!...yes!...yes, owner!...yes!!"
                                show pctit5 with dissolve
                                "she slams her head back and screams as her full body shakes with orgasm."
                                hide pctit
                                "her breasts squirt a torrent of creamy milk as you quickly grab a bucket."
                                "you got an extra-large milking from her!"
                                $ milked +=1
                                "you let her go and she sags in her restraints."
                                "she lets out a tiny whisper."
                                cow "...thank...you..."
                                "you let her go and milk the rest of the cows."
                                $ milked += pregnant_girls
                                $ milked_today_pregnant = True
                                hide pctit5
                                jump farm_script
                            "don't let her cum":

                                hide pctit with dissolve
                                "you drop her engorged tits and she looks up at you with desperation."
                                "she lets out the smallest whisper."
                                cow "please..."
                                show uc_milk with dissolve
                                "you ignore her pleas and begin milking her as she tries to rock in her harness."
                                show ctcblink
                                $ renpy.pause()
                                hide ctcblink
                                "unable to masturbate, she begs you harder as tears roll lightly down her face."
                                cow "please! i... just need to cum so badly..."
                                cow "you don't understand! these restraints... i can't..."
                                cow "please, owner! i need it, please!"
                                y "be a good girl... and maybe next time."
                                "she drops her head and remains quiet as you milk her."
                                "you milk the rest of the girls."
                                hide uc_milk
                                hide pctit1
                                $ milked += pregnant_girls
                                $ milked_today_pregnant = True
                                jump farm_script
                    "milk her":


                        $ milked += pregnant_girls
                        $ milked_today_pregnant = True
                        y "are you ready to be milked?"
                        cow "...."
                        cow "{size=-5}yes."
                        y "i didn't hear that."
                        cow "yes... please...."
                        y "well, if you don't need it-"
                        cow "please milk me!"
                        cow "please, i need it!"
                        y "let's empty those udders."
                        show uc_milk with dissolve
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        "you milk the cow, squeezing her engorged breasts."
                        "you empty her tit cream into the bucket."
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        "the girl sighs in relief."
                        cow "thank you..."
                        y "what?"
                        cow "....mooo."
                        ya "you can do better than that."
                        cow "..."
                        cow "mmmmmmooooooo!!"
                        y "good girl."
                        "you got [pregnant_girls] milkings from the used cows."
                        hide uc_milk
                        jump farm_script
        "fuck":

            show pc1 with dissolve
            y "what a good cow."
            y "spread those legs."
            y "let's see if we can hump you until your udders leak."
            cow "......"
            show pc3 with dissolve
            cow "ah!"
            cow "wait, that was too quick-"
            hide pc1
            cow "stop!"
            show pc4 with ushake
            hide pc3
            cow "ow!!"
            cow "why are you doing this? i'm already pregnant!"
            show pc_fuck1
            y "because it's so much fun, cow!"
            y "who knows? maybe now this soldier will be twice as powerful!"
            y "maybe emptying load after load of cum in you, leaving you sticky and full, will help."
            cow "i... *umph*... don't... *ngh*... want... *ugh*... this...!"
            y "but i do, and since you're my cum holster, i'm gonna drain my balls in you."
            y "and then leave you here."
            cow "*ungh* - *umph*"
            y "ngh!"
            cow "i hate-"
            hide pc_fuck1
            play sound "audio/splurt3.ogg"
            with flash
            cow "!!!!"
            play sound "audio/splurt1.ogg"
            with flash
            cow "you assho-"
            play sound "audio/splurt3.ogg"
            with flash
            y "ngh!"
            play sound "audio/splurt3.ogg"
            with flash
            cow "..."
            y "yeah, that hit the spot."
            show pc2 with dissolve
            hide pc4
            y "see you around, cow."
            cow "...."
            show pc1 with dissolve
            hide pc2
            y "what was that?"
            cow "...."
            cow "moo."
            y "haha, good enough."
            $ morality -=1
            "you got -1 morality."
            show farm_hall with dissolve
            hide pc1
            hide pctit1
            jump farm_script
        "set free":

            $ morality +=1
            $ total_girls -=1
            $ pregnant_girls -=1
            "you set her free!"
            "you got +1 morality."
            if girl1:
                $ girl1_points = 0
                $ girl1 = False
            if girl2:
                $ girl2_points = 0
                $ girl2 = False
            if girl3:
                $ girl3_points = 0
                $ girl3 = False
            if girl4:
                $ girl4_points = 0
                $ girl4 = False
            if girl5:
                $ girl5_points = 0
                $ girl5 = False
            if girl6:
                $ girl6_points = 0
                $ girl6 = False
            if girl7:
                $ girl7_points = 0
                $ girl7 = False
            if girl8:
                $ girl8_points = 0
                $ girl8 = False
            if girl9:
                $ girl9_points = 0
                $ girl9 = False
            if girl10:
                $ girl10_points = 0
                $ girl10 = False
            if girl11:
                $ girl11_points = 0
                $ girl11 = False
            if girl12:
                $ girl12_points = 0
                $ girl12 = False
            if girl13:
                $ girl13_points = 0
                $ girl13 = False
            if girl14:
                $ girl14_points = 0
                $ girl14 = False
            if girl15:
                $ girl15_points = 0
                $ girl15 = False
            if girl16:
                $ girl16_points = 0
                $ girl16 = False
            if girl17:
                $ girl17_points = 0
                $ girl17 = False
            if girl18:
                $ girl18_points = 0
                $ girl18 = False
            if girl19:
                $ girl19_points = 0
                $ girl19 = False
            if girl20:
                $ girl20_points = 0
                $ girl20 = False
            if girl21:
                $ girl21_points = 0
                $ girl21 = False
            if girl22:
                $ girl22_points = 0
                $ girl22 = False
            if girl23:
                $ girl23_points = 0
                $ girl23 = False
            if girl24:
                $ girl24_points = 0
                $ girl24 = False
            if girl25:
                $ girl25_points = 0
                $ girl25 = False
            if girl26:
                $ girl26_points = 0
                $ girl26 = False
            if girl27:
                $ girl27_points = 0
                $ girl27 = False
            if girl28:
                $ girl28_points = 0
                $ girl28 = False
            if girl29:
                $ girl29_points = 0
                $ girl29 = False
            if girl30:
                $ girl30_points = 0
                $ girl30 = False
            if girl31:
                $ girl31_points = 0
                $ girl31 = False
            if girl32:
                $ girl32_points = 0
                $ girl32 = False
            if girl33:
                $ girl33_points = 0
                $ girl33 = False
            if girl34:
                $ girl34_points = 0
                $ girl34 = False
            if girl35:
                $ girl35_points = 0
                $ girl35 = False
            if girl36:
                $ girl36_points = 0
                $ girl36 = False
            if girl37:
                $ girl37_points = 0
                $ girl37 = False
            if girl38:
                $ girl38_points = 0
                $ girl38 = False
            if girl39:
                $ girl39_points = 0
                $ girl39 = False
            if girl40:
                $ girl40_points = 0
                $ girl40 = False
            if girl41:
                $ girl41_points = 0
                $ girl41 = False
            if girl42:
                $ girl42_points = 0
                $ girl42 = False
            if girl43:
                $ girl43_points = 0
                $ girl43 = False
            if girl44:
                $ girl44_points = 0
                $ girl44 = False
            if girl45:
                $ girl45_points = 0
                $ girl45 = False
            if girl46:
                $ girl46_points = 0
                $ girl46 = False
            if girl47:
                $ girl47_points = 0
                $ girl47 = False
            if girl48:
                $ girl48_points = 0
                $ girl48 = False
            if girl49:
                $ girl49_points = 0
                $ girl49 = False
            if girl50:
                $ girl50_points = 0
                $ girl50 = False
            if girl51:
                $ girl51_points = 0
                $ girl51 = False
            if girl52:
                $ girl52_points = 0
                $ girl52 = False
            if girl53:
                $ girl53_points = 0
                $ girl53 = False
            if girl54:
                $ girl54_points = 0
                $ girl54 = False
            if girl55:
                $ girl55_points = 0
                $ girl55 = False
            if girl56:
                $ girl56_points = 0
                $ girl56 = False
            if girl57:
                $ girl57_points = 0
                $ girl57 = False
            if girl58:
                $ girl58_points = 0
                $ girl58 = False
            if girl59:
                $ girl59_points = 0
                $ girl59 = False
            if girl60:
                $ girl60_points = 0
                $ girl60 = False
            if girl61:
                $ girl61_points = 0
                $ girl61 = False
            if girl62:
                $ girl62_points = 0
                $ girl62 = False
            if girl63:
                $ girl63_points = 0
                $ girl63 = False
            if girl64:
                $ girl64_points = 0
                $ girl64 = False
            if girl65:
                $ girl65_points = 0
                $ girl65 = False
            if girl66:
                $ girl66_points = 0
                $ girl66 = False
            if girl67:
                $ girl67_points = 0
                $ girl67 = False
            if girl68:
                $ girl68_points = 0
                $ girl68 = False
            if girl69:
                $ girl69_points = 0
                $ girl69 = False
            if girl70:
                $ girl70_points = 0
                $ girl70 = False
            if girl71:
                $ girl71_points = 0
                $ girl71 = False
            if girl72:
                $ girl72_points = 0
                $ girl72 = False
            if girl73:
                $ girl73_points = 0
                $ girl73 = False
            if girl74:
                $ girl74_points = 0
                $ girl74 = False
            if girl75:
                $ girl75_points = 0
                $ girl75 = False
            if girl76:
                $ girl76_points = 0
                $ girl76 = False
            if girl77:
                $ girl77_points = 0
                $ girl77 = False
            if girl78:
                $ girl78_points = 0
                $ girl78 = False
            if girl79:
                $ girl79_points = 0
                $ girl79 = False
            if girl80:
                $ girl80_points = 0
                $ girl80 = False
            if girl81:
                $ girl81_points = 0
                $ girl81 = False
            if girl82:
                $ girl82_points = 0
                $ girl82 = False
            if girl83:
                $ girl83_points = 0
                $ girl83 = False
            if girl84:
                $ girl84_points = 0
                $ girl84 = False
            if girl85:
                $ girl85_points = 0
                $ girl85 = False
            if girl86:
                $ girl86_points = 0
                $ girl86 = False
            if girl87:
                $ girl87_points = 0
                $ girl87 = False
            if girl88:
                $ girl88_points = 0
                $ girl88 = False
            if girl89:
                $ girl89_points = 0
                $ girl89 = False
            if girl90:
                $ girl90_points = 0
                $ girl90 = False
            if girl91:
                $ girl91_points = 0
                $ girl91 = False
            if girl92:
                $ girl92_points = 0
                $ girl92 = False
            if girl93:
                $ girl93_points = 0
                $ girl93 = False
            if girl94:
                $ girl94_points = 0
                $ girl94 = False
            if girl95:
                $ girl95_points = 0
                $ girl95 = False
            if girl96:
                $ girl96_points = 0
                $ girl96 = False
            if girl97:
                $ girl97_points = 0
                $ girl97 = False
            if girl98:
                $ girl98_points = 0
                $ girl98 = False
            if girl99:
                $ girl99_points = 0
                $ girl99 = False
            jump farm_script
        "back":


            jump farm_script



label g_questions:
    menu:
        g "what?"
        "how do i capture girls?":

            g "i don't know."
            g "use war prisoners or buy them from someone."
            jump g_questions
        "how do i impregnate them?":

            g "..."
            g "the usual way."
            jump g_questions
        "what if i don't impregnate them?":

            g "they will be happy with you."
            g "...but azula won't be."
            g "you won't get paid, and azula might have to take care of it."
            y "...does she have a dick or something?"
            g "man, who knows."
            y "..."
            jump g_questions
        "how long will they stay pregnant?":

            g "20 days."
            g "after that they will need to be impregnated again."
            jump g_questions
        "how often does azula come by?":

            g "every 7 days."
            jump g_questions
        "which girls do i milk?":

            g "you milk the used ones and the pregnant ones."
            g "we make sure that they produce early and for a long time."
            jump g_questions
        "how do i milk them?":

            g "use the equipment, moron."
            g "there's instructions on them."
            jump g_questions
        "what happens if there's a birth?":

            g "azula will pay you extra."
            jump g_questions
        "how much do I get paid?":

            g "5 coins per milking, 10 coins per birth."
            jump g_questions
        "which ones can i fuck?":

            g "i don't care."
            g "fuck the fresh ones, fuck the used ones, fuck the pregnant ones."
            jump g_questions
        "how many girls can the farm hold?":

            g "the farm can hold 99 girls."
            jump g_questions
        "back":

            jump farm_script


label fresh_girl_select:

    $ fresh_girl_selector = renpy.random.randint(1,99)


    if fresh_girl_selector == 1:
        if girl1:
            jump fresh_girl_select
        else:
            $ girl1 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 2:
        if girl2:
            jump fresh_girl_select
        else:
            $ girl2 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 3:
        if girl3:
            jump fresh_girl_select
        else:
            $ girl3 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 4:
        if girl4:
            jump fresh_girl_select
        else:
            $ girl4 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 5:
        if girl5:
            jump fresh_girl_select
        else:
            $ girl5 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 6:
        if girl6:
            jump fresh_girl_select
        else:
            $ girl6 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 7:
        if girl7:
            jump fresh_girl_select
        else:
            $ girl7 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 8:
        if girl8:
            jump fresh_girl_select
        else:
            $ girl8 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 9:
        if girl9:
            jump fresh_girl_select
        else:
            $ girl9 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 10:
        if girl10:
            jump fresh_girl_select
        else:
            $ girl10 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 11:
        if girl11:
            jump fresh_girl_select
        else:
            $ girl11 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 12:
        if girl12:
            jump fresh_girl_select
        else:
            $ girl12 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 13:
        if girl13:
            jump fresh_girl_select
        else:
            $ girl13 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 14:
        if girl14:
            jump fresh_girl_select
        else:
            $ girl14 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 15:
        if girl15:
            jump fresh_girl_select
        else:
            $ girl15 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 16:
        if girl16:
            jump fresh_girl_select
        else:
            $ girl16 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 17:
        if girl17:
            jump fresh_girl_select
        else:
            $ girl17 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 18:
        if girl18:
            jump fresh_girl_select
        else:
            $ girl18 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 19:
        if girl19:
            jump fresh_girl_select
        else:
            $ girl19 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 20:
        if girl20:
            jump fresh_girl_select
        else:
            $ girl20 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 21:
        if girl21:
            jump fresh_girl_select
        else:
            $ girl21 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 22:
        if girl22:
            jump fresh_girl_select
        else:
            $ girl22 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 23:
        if girl23:
            jump fresh_girl_select
        else:
            $ girl23 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 24:
        if girl24:
            jump fresh_girl_select
        else:
            $ girl24 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 25:
        if girl25:
            jump fresh_girl_select
        else:
            $ girl25 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 26:
        if girl26:
            jump fresh_girl_select
        else:
            $ girl26 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 27:
        if girl27:
            jump fresh_girl_select
        else:
            $ girl27 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 28:
        if girl28:
            jump fresh_girl_select
        else:
            $ girl28 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 29:
        if girl29:
            jump fresh_girl_select
        else:
            $ girl29 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 30:
        if girl30:
            jump fresh_girl_select
        else:
            $ girl30 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 31:
        if girl31:
            jump fresh_girl_select
        else:
            $ girl31 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 32:
        if girl32:
            jump fresh_girl_select
        else:
            $ girl32 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 33:
        if girl33:
            jump fresh_girl_select
        else:
            $ girl33 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 34:
        if girl34:
            jump fresh_girl_select
        else:
            $ girl34 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 35:
        if girl35:
            jump fresh_girl_select
        else:
            $ girl35 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 36:
        if girl36:
            jump fresh_girl_select
        else:
            $ girl36 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 37:
        if girl37:
            jump fresh_girl_select
        else:
            $ girl37 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 38:
        if girl38:
            jump fresh_girl_select
        else:
            $ girl38 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 39:
        if girl39:
            jump fresh_girl_select
        else:
            $ girl39 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 40:
        if girl40:
            jump fresh_girl_select
        else:
            $ girl40 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 41:
        if girl41:
            jump fresh_girl_select
        else:
            $ girl41 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 42:
        if girl42:
            jump fresh_girl_select
        else:
            $ girl42 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 43:
        if girl43:
            jump fresh_girl_select
        else:
            $ girl43 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 44:
        if girl44:
            jump fresh_girl_select
        else:
            $ girl44 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 45:
        if girl45:
            jump fresh_girl_select
        else:
            $ girl45 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 46:
        if girl46:
            jump fresh_girl_select
        else:
            $ girl46 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 47:
        if girl47:
            jump fresh_girl_select
        else:
            $ girl47 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 48:
        if girl48:
            jump fresh_girl_select
        else:
            $ girl48 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 49:
        if girl49:
            jump fresh_girl_select
        else:
            $ girl49 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 50:
        if girl50:
            jump fresh_girl_select
        else:
            $ girl50 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 51:
        if girl51:
            jump fresh_girl_select
        else:
            $ girl51 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 52:
        if girl52:
            jump fresh_girl_select
        else:
            $ girl52 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 53:
        if girl53:
            jump fresh_girl_select
        else:
            $ girl53 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 54:
        if girl54:
            jump fresh_girl_select
        else:
            $ girl54 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 55:
        if girl55:
            jump fresh_girl_select
        else:
            $ girl55 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 56:
        if girl56:
            jump fresh_girl_select
        else:
            $ girl56 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 57:
        if girl57:
            jump fresh_girl_select
        else:
            $ girl57 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 58:
        if girl58:
            jump fresh_girl_select
        else:
            $ girl58 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 59:
        if girl59:
            jump fresh_girl_select
        else:
            $ girl59 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 60:
        if girl60:
            jump fresh_girl_select
        else:
            $ girl60 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 61:
        if girl61:
            jump fresh_girl_select
        else:
            $ girl61 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 62:
        if girl62:
            jump fresh_girl_select
        else:
            $ girl62 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 63:
        if girl63:
            jump fresh_girl_select
        else:
            $ girl63 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 64:
        if girl64:
            jump fresh_girl_select
        else:
            $ girl64 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 65:
        if girl65:
            jump fresh_girl_select
        else:
            $ girl65 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 66:
        if girl66:
            jump fresh_girl_select
        else:
            $ girl66 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 67:
        if girl67:
            jump fresh_girl_select
        else:
            $ girl67 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 68:
        if girl68:
            jump fresh_girl_select
        else:
            $ girl68 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 9:
        if girl69:
            jump fresh_girl_select
        else:
            $ girl69 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 70:
        if girl70:
            jump fresh_girl_select
        else:
            $ girl70 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 71:
        if girl71:
            jump fresh_girl_select
        else:
            $ girl71 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 72:
        if girl72:
            jump fresh_girl_select
        else:
            $ girl72 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 73:
        if girl73:
            jump fresh_girl_select
        else:
            $ girl73 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 74:
        if girl74:
            jump fresh_girl_select
        else:
            $ girl74 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 75:
        if girl75:
            jump fresh_girl_select
        else:
            $ girl75 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 76:
        if girl76:
            jump fresh_girl_select
        else:
            $ girl76 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 77:
        if girl77:
            jump fresh_girl_select
        else:
            $ girl77 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 78:
        if girl78:
            jump fresh_girl_select
        else:
            $ girl78 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 79:
        if girl79:
            jump fresh_girl_select
        else:
            $ girl79 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 80:
        if girl80:
            jump fresh_girl_select
        else:
            $ girl80 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 81:
        if girl81:
            jump fresh_girl_select
        else:
            $ girl81 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 82:
        if girl82:
            jump fresh_girl_select
        else:
            $ girl82 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 83:
        if girl83:
            jump fresh_girl_select
        else:
            $ girl83 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 84:
        if girl84:
            jump fresh_girl_select
        else:
            $ girl84 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 85:
        if girl85:
            jump fresh_girl_select
        else:
            $ girl85 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 86:
        if girl86:
            jump fresh_girl_select
        else:
            $ girl86 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 87:
        if girl87:
            jump fresh_girl_select
        else:
            $ girl87 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 88:
        if girl88:
            jump fresh_girl_select
        else:
            $ girl88 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 89:
        if girl89:
            jump fresh_girl_select
        else:
            $ girl89 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 90:
        if girl90:
            jump fresh_girl_select
        else:
            $ girl90 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 91:
        if girl91:
            jump fresh_girl_select
        else:
            $ girl91 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 92:
        if girl92:
            jump fresh_girl_select
        else:
            $ girl92 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 93:
        if girl93:
            jump fresh_girl_select
        else:
            $ girl93 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 94:
        if girl94:
            jump fresh_girl_select
        else:
            $ girl94 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 95:
        if girl95:
            jump fresh_girl_select
        else:
            $ girl95 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 96:
        if girl96:
            jump fresh_girl_select
        else:
            $ girl96 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 97:
        if girl97:
            jump fresh_girl_select
        else:
            $ girl97 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 98:
        if girl98:
            jump fresh_girl_select
        else:
            $ girl98 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif fresh_girl_selector == 99:
        if girl99:
            jump fresh_girl_select
        else:
            $ girl99 = True
            $ fresh_girls -=1
            $ pregnant_girls +=1
            jump farm_script

label used_girl_select:

    $ used_girl_selector = renpy.random.randint(1,99)

    if used_girl_selector == 1:
        if girl1:
            jump used_girl_select
        else:
            $ girl1 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 2:
        if girl2:
            jump used_girl_select
        else:
            $ girl2 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 3:
        if girl3:
            jump used_girl_select
        else:
            $ girl3 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 4:
        if girl4:
            jump used_girl_select
        else:
            $ girl4 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 5:
        if girl5:
            jump used_girl_select
        else:
            $ girl5 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 6:
        if girl6:
            jump used_girl_select
        else:
            $ girl6 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 7:
        if girl7:
            jump used_girl_select
        else:
            $ girl7 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 8:
        if girl8:
            jump used_girl_select
        else:
            $ girl8 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 9:
        if girl9:
            jump used_girl_select
        else:
            $ girl9 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 10:
        if girl10:
            jump used_girl_select
        else:
            $ girl10 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 11:
        if girl11:
            jump used_girl_select
        else:
            $ girl11 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 12:
        if girl12:
            jump used_girl_select
        else:
            $ girl12 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 13:
        if girl13:
            jump used_girl_select
        else:
            $ girl13 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 14:
        if girl14:
            jump used_girl_select
        else:
            $ girl14 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 15:
        if girl15:
            jump used_girl_select
        else:
            $ girl15 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 16:
        if girl16:
            jump used_girl_select
        else:
            $ girl16 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 17:
        if girl17:
            jump used_girl_select
        else:
            $ girl17 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 18:
        if girl18:
            jump used_girl_select
        else:
            $ girl18 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 19:
        if girl19:
            jump used_girl_select
        else:
            $ girl19 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 20:
        if girl20:
            jump used_girl_select
        else:
            $ girl20 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 21:
        if girl21:
            jump used_girl_select
        else:
            $ girl21 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 22:
        if girl22:
            jump used_girl_select
        else:
            $ girl22 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 23:
        if girl23:
            jump used_girl_select
        else:
            $ girl23 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 24:
        if girl24:
            jump used_girl_select
        else:
            $ girl24 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 25:
        if girl25:
            jump used_girl_select
        else:
            $ girl25 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 26:
        if girl26:
            jump used_girl_select
        else:
            $ girl26 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 27:
        if girl27:
            jump used_girl_select
        else:
            $ girl27 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 28:
        if girl28:
            jump used_girl_select
        else:
            $ girl28 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 29:
        if girl29:
            jump used_girl_select
        else:
            $ girl29 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 30:
        if girl30:
            jump used_girl_select
        else:
            $ girl30 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 31:
        if girl31:
            jump used_girl_select
        else:
            $ girl31 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 32:
        if girl32:
            jump used_girl_select
        else:
            $ girl32 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 33:
        if girl33:
            jump used_girl_select
        else:
            $ girl33 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 34:
        if girl34:
            jump used_girl_select
        else:
            $ girl34 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 35:
        if girl35:
            jump used_girl_select
        else:
            $ girl35 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 36:
        if girl36:
            jump used_girl_select
        else:
            $ girl36 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 37:
        if girl37:
            jump used_girl_select
        else:
            $ girl37 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 38:
        if girl38:
            jump used_girl_select
        else:
            $ girl38 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 39:
        if girl39:
            jump used_girl_select
        else:
            $ girl39 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 40:
        if girl40:
            jump used_girl_select
        else:
            $ girl40 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 41:
        if girl41:
            jump used_girl_select
        else:
            $ girl41 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 42:
        if girl42:
            jump used_girl_select
        else:
            $ girl42 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 43:
        if girl43:
            jump used_girl_select
        else:
            $ girl43 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 44:
        if girl44:
            jump used_girl_select
        else:
            $ girl44 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 45:
        if girl45:
            jump used_girl_select
        else:
            $ girl45 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 46:
        if girl46:
            jump used_girl_select
        else:
            $ girl46 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 47:
        if girl47:
            jump used_girl_select
        else:
            $ girl47 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 48:
        if girl48:
            jump used_girl_select
        else:
            $ girl48 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 49:
        if girl49:
            jump used_girl_select
        else:
            $ girl49 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 50:
        if girl50:
            jump used_girl_select
        else:
            $ girl50 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 51:
        if girl51:
            jump used_girl_select
        else:
            $ girl51 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 52:
        if girl52:
            jump used_girl_select
        else:
            $ girl52 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 53:
        if girl53:
            jump used_girl_select
        else:
            $ girl53 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 54:
        if girl54:
            jump used_girl_select
        else:
            $ girl54 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 55:
        if girl55:
            jump used_girl_select
        else:
            $ girl55 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 56:
        if girl56:
            jump used_girl_select
        else:
            $ girl56 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 57:
        if girl57:
            jump used_girl_select
        else:
            $ girl57 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 58:
        if girl58:
            jump used_girl_select
        else:
            $ girl58 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 59:
        if girl59:
            jump used_girl_select
        else:
            $ girl59 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 60:
        if girl60:
            jump used_girl_select
        else:
            $ girl60 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 61:
        if girl61:
            jump used_girl_select
        else:
            $ girl61 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 62:
        if girl62:
            jump used_girl_select
        else:
            $ girl62 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 63:
        if girl63:
            jump used_girl_select
        else:
            $ girl63 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 64:
        if girl64:
            jump used_girl_select
        else:
            $ girl64 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 65:
        if girl65:
            jump used_girl_select
        else:
            $ girl65 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 66:
        if girl66:
            jump used_girl_select
        else:
            $ girl66 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 67:
        if girl67:
            jump used_girl_select
        else:
            $ girl67 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 68:
        if girl68:
            jump used_girl_select
        else:
            $ girl68 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 9:
        if girl69:
            jump used_girl_select
        else:
            $ girl69 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 70:
        if girl70:
            jump used_girl_select
        else:
            $ girl70 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 71:
        if girl71:
            jump used_girl_select
        else:
            $ girl71 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 72:
        if girl72:
            jump used_girl_select
        else:
            $ girl72 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 73:
        if girl73:
            jump used_girl_select
        else:
            $ girl73 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 74:
        if girl74:
            jump used_girl_select
        else:
            $ girl74 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 75:
        if girl75:
            jump used_girl_select
        else:
            $ girl75 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 76:
        if girl76:
            jump used_girl_select
        else:
            $ girl76 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 77:
        if girl77:
            jump used_girl_select
        else:
            $ girl77 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 78:
        if girl78:
            jump used_girl_select
        else:
            $ girl78 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 79:
        if girl79:
            jump used_girl_select
        else:
            $ girl79 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 80:
        if girl80:
            jump used_girl_select
        else:
            $ girl80 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 81:
        if girl81:
            jump used_girl_select
        else:
            $ girl81 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 82:
        if girl82:
            jump used_girl_select
        else:
            $ girl82 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 83:
        if girl83:
            jump used_girl_select
        else:
            $ girl83 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 84:
        if girl84:
            jump used_girl_select
        else:
            $ girl84 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 85:
        if girl85:
            jump used_girl_select
        else:
            $ girl85 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 86:
        if girl86:
            jump used_girl_select
        else:
            $ girl86 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 87:
        if girl87:
            jump used_girl_select
        else:
            $ girl87 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 88:
        if girl88:
            jump used_girl_select
        else:
            $ girl88 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 89:
        if girl89:
            jump used_girl_select
        else:
            $ girl89 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 90:
        if girl90:
            jump used_girl_select
        else:
            $ girl90 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 91:
        if girl91:
            jump used_girl_select
        else:
            $ girl91 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 92:
        if girl92:
            jump used_girl_select
        else:
            $ girl92 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 93:
        if girl93:
            jump used_girl_select
        else:
            $ girl93 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 94:
        if girl94:
            jump used_girl_select
        else:
            $ girl94 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 95:
        if girl95:
            jump used_girl_select
        else:
            $ girl95 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 96:
        if girl96:
            jump used_girl_select
        else:
            $ girl96 = True
            jump farm_script
    elif used_girl_selector == 97:
        if girl97:
            jump used_girl_select
        else:
            $ girl97 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 98:
        if girl98:
            jump used_girl_select
        else:
            $ girl98 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script
    elif used_girl_selector == 99:
        if girl99:
            jump used_girl_select
        else:
            $ girl99 = True
            $ used_girls -=1
            $ pregnant_girls +=1
            jump farm_script


label farm_visit:
    show farm_hall with dissolve
    show a_blink with dissolve
    a "well, let's see where we are."
    a "you've done [milked] milkings."
    $ milk_payout = (milked*5)
    a "at 5 coins each, that's [milk_payout]."
    $ fmoney += milk_payout
    if milk_payout < 100:
        a "you're disappointing me."
    $ milked = 0
    a "how many births did you have?"
    a "[fbirths]?"
    if fbirths >=1:

        $ birth_payout = (fbirths*20)
        a "here's [birth_payout] coins."
        $ fmoney += birth_payout
    $ fbirths = 0
    a "now... how many pregnant cows do we have?"
    a "[pregnant_girls]?"
    if pregnant_girls >=1:
        a "good. i expect them to be... bountiful."
        a "enjoy yourself."
        if thief > zuko:
            jump city
        else:
            jump zcity1
    if pregnant_girls == 0:
        a "none?"
        if total_girls <=98:
            a "lucky for you i brought one."
            "azula brings in a young girl, kicking and screaming."
            "she disappears into the back with the girl for a few minutes."
            a "there, she's pregnant."
            y "...how..."
            "azula simply glares at you and leaves."









            $ total_girls +=1
            $ fresh_girls +=1
            hide a_blink
            jump fresh_girl_select
        else:

            if fresh_girls >=1:
                a "how about i show you how it's done?"
                "azula brings out a fresh girl, kicking and screaming."
                "she disappears into the back with the girl for a few minutes."
                a "there, she's pregnant."
                y "...how..."
                "azula simply glares at you and leaves."










                hide a_blink
                jump fresh_girl_select
            else:
                a "how about i show you how it's done?"
                "azula brings out a used girl, obediently following."
                "she disappears into the back with the girl for a few minutes."
                a "there, she's pregnant."
                y "...how..."
                "azula simply glares at you and leaves."











                hide a_blink
                jump used_girl_select

label farm_visit1:
    show farm_hall with dissolve
    show fireguard_halberd with dissolve
    g "well, let's see where we are."
    g "you've done [milked] milkings."
    $ milk_payout = (milked*5)
    g "at 5 coins each, that's [milk_payout]."
    $ fmoney += milk_payout
    if milk_payout < 100:
        g "you don't seem to be doing very well."
    $ milked = 0
    g "how many births did you have?"
    g "[fbirths]?"
    if fbirths >=1:

        $ birth_payout = (fbirths*20)
        g "here's [birth_payout] coins."
        $ fmoney += birth_payout
    $ fbirths = 0
    g "now... how many pregnant cows do we have?"
    g "[pregnant_girls]?"
    if pregnant_girls >=1:
        g "good. i expect them to be... bountiful."
        g "enjoy yourself."
        hide fireguard_halberd
        jump city
    if pregnant_girls == 0:
        g "none?"
        if total_girls <=98:
            g "lucky for you i brought one."
            "the guard brings in a young girl, kicking and screaming."
            "he disappears into the back with the girl for a few minutes."
            g "there, she's pregnant."
            $ total_girls +=1
            $ fresh_girls +=1
            hide fireguard_halberd
            jump fresh_girl_select
        else:

            if fresh_girls >=1:
                g "how about i show you how it's done?"
                "the guard brings out a fresh girl, kicking and screaming."
                "he disappears into the back with the girl for a few minutes."
                g "there, she's pregnant."

                hide fireguard_halberd
                jump fresh_girl_select
            else:
                g "how about i show you how it's done?"
                "the guard brings out a used girl, obediently following."
                "he disappears into the back with the girl for a few minutes."
                g "there, she's pregnant."
                hide fireguard_halberd
                jump used_girl_select


label guard_caught:
    scene farm_hall with dissolve
    show fireguard_halberd with dissolve
    g "sir."
    y "i know, guard. you've been caught."
    g "....caught?"
    y "stealing weapons for the cows."
    g "no sir, not me."
    y "we'll let mai decide."
    y "or maybe azula."
    g "wait!"
    g "it's..."
    g "i feel so bad for the girls."
    g "i just want to give them a chance to escape and defend themselves."
    g "please, if you don't say anything... we won't steal anything else."
    y "...."
    y "i'll consider it."
    hide fireguard_halberd
    $ mai_thefts3 = False
    $ mai_thefts4 = True
    jump city
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
