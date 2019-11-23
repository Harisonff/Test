




define quest = {"age":0, "name":""}
define quests_completed = 0

init:
    $ tavern_quest_time = 0
    $ tavern_quests_complete = 0
    $ quest_minutes_remaining = 0
    $ tavern_quest_name = "adventurer in trouble!"
    $ starting_quest_time = 5
    $ current_quest = 0
    $ tavern_quest1 = False
    $ tavern_quest2 = False
    $ tavern_quest3 = False
    $ tavern_quest4 = False
    $ tavern_quest5 = False
    $ tavern_quest6 = False
    $ tavern_quest7 = False
    $ tavern_quest8 = False
    $ tavern_quest9 = False
    $ tavern_quest10 = False
    $ tavern_quest11 = False
    $ tavern_quest12 = False
    $ tavern_quest13 = False
    $ tavern_quest14 = False
    $ tavern_quest15 = False
    $ quest1_hero = 0


label time_test:
    $ time_now = TimeModule.time()
    "Unix time in seconds: [time_now]"
    jump tavern_quest_menu

label start_tavern_quest:
    if tavern_quest_time == 0:
        menu:
            "adventurer in trouble! (5:00)" if not tavern_quest1:
                show blackveil
                show letter_0
                with dissolve
                show text "help! i sort of... may have... picked a fight\ni wasn't ready for and... um...\ni might be hiding in a cave. there's only\none way out and there's three of them out\nthere looking for me! i sent my trusty bird to\n deliver this, i hope someone gets it soon!":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest1 = True
                        $ tavern_quest_name = "adventurer in trouble!"
                        $ tavern_quest_time = TimeModule.time() + 300
                        $ starting_quest_time = 5
                        $ current_quest = 1
                        "two adventurers are interested in this quest!"
                        "Mango" "I, mango, the famous giant earthbender, will destroy them!"
                        "Tango" "I can sneak around them. there might be a back way into the cave."
                        jump tavern_quest1_menu

                        label tavern_quest1_menu:
                            menu:
                                "mango - strength":
                                    $ quest1_hero = 1
                                    "mango" "i will eat their skulls!"
                                    y "...how?"
                                    "mango" "with my fists!"
                                    y "...."
                                    y "i know where you fall on the brains vs. brawns chart."
                                    "mango" "at the top!"
                                    y "....good luck."
                                    "mango set out on this quest!"
                                "tango - stealth":

                                    $ quest1_hero = 2
                                    "tango" "they'll never hear me coming."
                                    y "good luck."
                                    "tango" "thanks. i pride myself on quiet masturbation."
                                    y "what... oh, that's what you meant."
                                    y "just... get out of here."
                                    y "shoo!"
                                    "tango set out on this quest!"
                    "back":

                        hide letter_0
                        hide blackveil
                        hide text
                        with dissolve
                        jump start_tavern_quest
            "mysterious package? (5:00)" if not tavern_quest2:
                show blackveil
                show letter_0
                with dissolve
                show text "found a strange box, not sure what's inside.\ncould use another set of eyes.\npreferably sensible ones.":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest2 = True
                        $ tavern_quest_name = "mysterious package?"
                        $ tavern_quest_time = TimeModule.time() + 300
                        $ current_quest = 2
                        $ starting_quest_time = 5
                        "two adventurers are interested in this quest!"
                        "tina" "i'm good with my hands, let me do this."
                        "inga" "sometimes the right course is the thoughtful one, let me try."
                        jump tavern_quest2_menu

                        label tavern_quest2_menu:
                            menu:
                                "tina - stealth":
                                    $ quest1_hero = 1
                                    "tina" "i've got this."
                                    "tina set out on this quest!"
                                "inga - wisdom":

                                    $ quest1_hero = 2
                                    "inga" "i'll figure out what's going on."
                                    "inga set out on this quest!"
                    "back":
                        jump start_tavern_quest
            "firebender attack! (10:00)" if not tavern_quest3 and tavern_quests_complete >=1:
                show blackveil
                show letter_0
                with dissolve
                show text "firebenders are attacking.\nwe're massively overwhelmed! help!":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest3 = True
                        $ tavern_quest_name = "firebender attack!"
                        $ tavern_quest_time = TimeModule.time() + 600
                        $ current_quest = 3
                        $ starting_quest_time = 10
                        "two adventurers are interested in this quest!"
                        "fria" "i'll pound those assholes with my meaty earth-fists!"
                        "tonka" "hold up, maybe I can undermine them somehow?"
                        jump tavern_quest3_menu

                        label tavern_quest3_menu:
                            menu:
                                "fria - strength":
                                    $ quest1_hero = 1
                                    "fria" "i've got this."
                                    "fria set out on this quest!"
                                "tonka - stealth":

                                    $ quest1_hero = 2
                                    "tonka" "i'm sure there's a way."
                                    "tonka set out on this quest!"
                    "back":
                        jump start_tavern_quest
            "beast on the prowl... (5:00)" if not tavern_quest4 and tavern_quests_complete >=2:
                show blackveil
                show letter_0
                with dissolve
                show text "there's a terrifying beast out here.\nonly appears at night.\nhard to catch.":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest4 = True
                        $ tavern_quest_name = "beast on the prowl..."
                        $ tavern_quest_time = TimeModule.time() + 300
                        $ current_quest = 4
                        $ starting_quest_time = 5
                        "shank" "as a thief, i know my way around prowlers..."
                        "yuni" "i'll punch it. doesn't matter what it is."
                        jump tavern_quest4_menu

                        label tavern_quest4_menu:
                            menu:
                                "shank - stealth":
                                    $ quest1_hero = 1
                                    "shank" "i've got this."
                                    "shank set out on this quest!"
                                "yuni - strength":

                                    $ quest1_hero = 2
                                    "yuni" "i'm sure there's a way."
                                    "yuni set out on this quest!"
                    "back":

                        jump start_tavern_quest
            "quick delivery (5:00)" if not tavern_quest5 and tavern_quests_complete >=4:
                show blackveil
                show letter_0
                with dissolve
                show text "got a package needs deliverin'.\ngotta get there quick.":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest5 = True
                        $ tavern_quest_name = "quick delivery"
                        $ tavern_quest_time = TimeModule.time() + 300
                        $ current_quest = 5
                        $ starting_quest_time = 5
                        "stiffy" "i'm all muscle. i'll do it."
                        "rig" "i'll think this through. maybe i can make a faster version."
                        jump tavern_quest5_menu

                        label tavern_quest5_menu:
                            menu:
                                "stiffy - strength":
                                    $ quest1_hero = 1
                                    "stiffy" "i've got this."
                                    "stiffy set out on this quest!"
                                "rig - wisdom":

                                    $ quest1_hero = 2
                                    "rig" "i'm sure there's a way."
                                    "rig set out on this quest!"
                    "back":
                        jump start_tavern_quest























            "airbenders? (8:00)" if not tavern_quest6 and tavern_quests_complete >=5:
                show blackveil
                show letter_0
                with dissolve
                show text "rumors of airbenders have surfaced.\nif true, trade will be lucrative.":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest6 = True
                        $ tavern_quest_name = "airbenders?"
                        $ tavern_quest_time = TimeModule.time() + 480
                        $ current_quest = 6
                        $ starting_quest_time = 8
                        "sera" "this requires attention and thought."
                        "ryo" "i'll find 'em or bust a nut trying."
                        y "...."
                        jump tavern_quest6_menu

                        label tavern_quest6_menu:
                            menu:
                                "sera - wisdom":
                                    $ quest1_hero = 1
                                    "sera" "i'll be thoughtful."
                                "ryo - strength":

                                    $ quest1_hero = 2
                                    "ryo" "they won't know what hit 'em!"
                    "back":
                        jump start_tavern_quest
















































            "a peck of knowledge (7:00)" if not tavern_quest7 and tavern_quests_complete >=6:
                if tavern_shack <3:
                    "you need to upgrade the tavern to start this quest!"
                    jump start_tavern_quest

                show blackveil
                show letter_0
                with dissolve
                show text "I just, uh, found a giant library. i need\n a hand. since it's in a buttload of sand.\nmind need to be careful though, there are funny noises.":
                    yalign .3
                show ctc
                pause
                hide ctc
                menu:
                    "start this quest":
                        $ tavern_quest7 = True
                        $ tavern_quest_name = "a peck of knowledge"
                        $ tavern_quest_time = TimeModule.time() + 420
                        $ current_quest = 7
                        $ starting_quest_time = 7
                        "yanny" "we're talking about books. Obviously, you need a thinker."
                        "laurel" "if there's danger there, you want someone quick and quiet. me."
                        jump tavern_quest7_menu

                        label tavern_quest7_menu:
                            menu:
                                "yanny - wisdom":
                                    $ quest1_hero = 1
                                    "yanny" "i'll be mindful."
                                "laural - stealth":

                                    $ quest1_hero = 2
                                    "laural" "quick and cautious."
                    "back":

                        jump start_tavern_quest

















            "kill the avatar!" if not tavern_quest15 and tavern_quests_complete >=7 and not bk3_loveroute:
                if tavern_shack <3:
                    "you need to upgrade the tavern to start this quest!"
                    jump tavern_quest_menu
                if june_hypno >=11 and june_thighs:
                    y "kill... the avatar?"
                    y "but that's me!"
                    y "who would start this?"
                    y "June!"
                    show toju toju16 with dissolve
                    ju "yes, master?"
                    y "who put this up?"
                    ju "i don't know..."
                    y "seriously, who would even take this quest, though?"
                    y "I mean, you'd be taking on the avatar! me!"
                    y "i'm awesome!"
                    ju "well... i took it on, once."
                    y "what?"
                    ju "yeah, i... hunted you."
                    y "....."
                    y "you..."
                    y "{i}{size=+5}bitch{/i}."
                    show june_lewd with dissolve
                    ju "ungh...."
                    y "you disgusting, stupid, fuckpig..."
                    with ushake
                    ju "yes... yes... ungh..."
                    ju "don't stop..."
                    y "...."
                    ju "please!"
                    y "june, you useless, filthy, pathetic whore..."
                    ju "ungh... unh... ffu... ah..."
                    y "you deserve to be beaten and drenched in cum."
                    show june_blink with dissolve
                    ju "yes... yes... almost... almost...."
                    y "in fact, i'm going to fuck your mouth right now."
                    y "the only thing you're fucking good for, you slut."
                    hide june_lewd
                    show june_surprise
                    show june_blush
                    hide june_blink
                    with vshake
                    ju "oh!"
                    ju "oh, my...!"
                    show june_blink with vshake
                    ju "{size=+10}fuuuuckk!!!!!"
                    ju "hhngh....."
                    show june_lewd
                    hide june_surprise
                    hide june_blush
                    hide june_blink
                    with dissolve
                    ju "oh, fuck... that was... so... fucking..."
                    ju "good...."
                    $ tavern_quest15 = True
                    y "you... bitch!"
                    y "You think you get to cum and are forgiven?"
                    ju "n...no..."
                    y "you have to earn forgiveness, bitch."
                    y "and i know how you're gonna pay me back!"
                    $ tavern_quest_name = "fuck june's face!"
                    $ current_quest = 15
                    $ starting_quest_time = 0
                else:
                    y "i need to progress farther with june to get this, I think."
                    jump tavern_quest_menu
            "back":
                jump tavern_quest_menu

        play sound "audio/Cowboy Sting.ogg"
        "\"{b}[tavern_quest_name]{/b}\" begins!"
        if current_quest ==15:
            hide blackveil
            hide letter_0
            hide text
            with dissolve
            jump june_bj1
        $ quest_minutes_remaining = ((tavern_quest_time - TimeModule.time())/60)
        python:
            minutes_answer = str(round(quest_minutes_remaining, 2))
        "It will take {b}[starting_quest_time]{/b} real-time minutes."
        "Check back then!"
        hide blackveil
        hide letter_0
        hide text
        with dissolve

    elif TimeModule.time() >= tavern_quest_time:
        "\"{b}[tavern_quest_name]{/b}\" has finished and is waiting for you to check it!"
    else:

        "\"{b}[tavern_quest_name]{/b}\" is your active quest."

    jump tavern_quest_menu

label check_tavern_quest:


    if tavern_quest_time == 0:
        "you have no active quests..."

    elif TimeModule.time() >= tavern_quest_time:
        "\"{b}[tavern_quest_name]{/b}\" has finished!"
        if current_quest == 1:
            if quest1_hero == 1:
                "mango" "i, mango, have returned victorious!"
                "mango" "all smushed, except for man i save."
                "mango" "man so happy, he gave i, mango, hefty reward."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=35
                "35 coins!"
            if quest1_hero ==2:
                "tango" "hey, i'm back!"
                y "and?"
                "tango" "well... erm... we got out of there..."
                "tango" "but, uh, there was no back way in and they definitely saw us trying to escape."
                y "so what happened?"
                "tango" "we ran. a lot. and we're still alive."
                "tango" "though the guy did get hit by a rock."
                "tango" "anyway, he gave me a reward for getting him out of there."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=25
                "25 coins!"
        if current_quest == 2:
            if quest1_hero == 1:
                "tina" "well... good news and bad news."
                "tina" "the good news is that we got the box open..."
                "tina" "the bad news is that it was full of eggs."
                y "eggs?"
                "tina" "yup, old eggs."
                "tina" "they, uh, shot out of it on a kind of spring-loaded contraption."
                "tina" "he... was not happy."
                "tina" "anyway, he still paid."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=25
                "25 coins!"
            if quest1_hero ==2:
                "inga" "i'm back."
                y "and?"
                "inga" "the package was unmarked, other than his name and address."
                "inga" "but after a little caution, weight measurement, and sniffing...."
                "inga" "i determined it was eggs."
                "inga" "or a box of farts."
                "inga" "either way i advised him not to open it."
                "inga" "he gave me a reward for avoiding a mess."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=35
                "35 coins!"
        if current_quest == 3:
            if quest1_hero == 1:
                "fria" "that sucked."
                y "what happened?"
                "fria" "too many of them."
                "fria" "i was able to help hold them off until we could retreat safely, though."
                "fria" "anyway, they still paid."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=25
                "25 coins!"
                play sound "audio/win2.mp3"
                $ obsidian +=1
                "you got 1 obsidian!"
            if quest1_hero ==2:
                "tonka" "killed it."
                y "oh?"
                "tonka" "too many of them, but..."
                "tonka" "a few carefully placed mines, and..."
                "tonka" "no more firebenders."
                y "hardcore."
                "tonka" "they gave me a reward for helping out."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=35
                "35 coins!"
                play sound "audio/win2.mp3"
                $ obsidian +=1
                "you got 1 obsidian!"
        if current_quest == 4:
            if quest1_hero == 1:
                "shank" "it was a cat."
                y "seriously?"
                "shank" "yeah...."
                "shank" "but a real dick of a cat."
                "shank" "anyway, i put out some traps and we released it out of the town."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=35
                "35 coins!"
            if quest1_hero ==2:
                "yuni" "it was a cat."
                y "really?"
                "yuni" "yeah. um... but that's not all."
                y "okay..."
                "yuni" "i may have punched a person."
                "yuni" "and a mailbox."
                y "...why?"
                "yuni" "i thought they were the prowlers!"
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=25
                "25 coins!"
        if current_quest == 5:
            if quest1_hero == 1:
                "stiffy" "no problem at all."
                y "what was the package?"
                "stiffy" "oh, uh...."
                "stiffy" "bananas."
                "stiffy" "she was building a giant slippery banana-man."
                "stiffy" "never seen so many banana-penises in my life."
                y "I am... full of questions."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=35
                "35 coins!"
            if quest1_hero ==2:
                "rig" "i made a machine to get me there faster."
                y "that's great!"
                "rig" "yeah, but it took me a long time to make it."
                y "oh."
                "rig" "so, the bananas spoiled."
                y "bananas?"
                "rig" "yup. she was building a giant slippery banana-man."
                y "...why?"
                "rig" "dunno. dick-taking practice?"
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=25
                "you got 25 coins!"
        if current_quest == 6:
            if quest1_hero == 1:
                "sera" "not really airbenders."
                y "was anyone actually there?"
                "sera" "yeah, a mad scientist and bunch of peeps flying around all crazy."
                "sera" "our contact was actually happier about that."
                "sera" "he packed up more expensive items and gave me a reward."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=35
                "35 coins!"
            if quest1_hero ==2:
                "ryo" "i don't think they were airbenders."
                y "you... don't think? are you not sure?"
                "ryo" "well, i've never seen an airbender."
                y "i... guess that's fair."
                "ryo" "anyway, i wasn't sure, so i told the contact \"maybe\"."
                "ryo" "he was not happy when you got there."
                "ryo" "he said he would have packed more expensive merchandise for them."
                "ryo" "anyway, here."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=25
                "you got 25 coins!"
        if current_quest == 7:
            if quest1_hero == 1:
                "yanny" "uh."
                y "what happened?"
                "yanny" "owl attack."
                y "and?"
                "yanny" "not a hoot."
                y "...that was a terrible pun."
                "yanny" "well, we got out of there, but the contact was not happy."
                y "i really thought it was yanny at first, but obviously laurel was the correct choice."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"
                $ emoney +=25
                "25 coins!"
                play sound "audio/win2.mp3"
                $ obsidian +=1
                "you got 1 obsidian!"
            if quest1_hero ==2:
                "laurel" "killed it."
                y "what happened?"
                "laurel" "owl attack."
                "laurel" "it was a hoot."
                y "......"
                y "amazing."
                y "hardcore."
                "laurel" "they gave me a reward for getting them out with some books."
                y "i really thought it was yanny at first, but obviously laurel is the correct choice."
                "you take your cut of the reward..."
                play sound "audio/money.mp3"

                $ emoney +=35
                "35 coins!"
                play sound "audio/win2.mp3"
                $ obsidian +=1
                "you got 1 obsidian!"
        if current_quest == 8:
            "test"
        if current_quest == 9:
            "test"
        if current_quest == 10:
            play sound "audio/win2.mp3"
            $ obsidian +=1
            "test"
        if current_quest == 11:
            "test"
        if current_quest == 12:
            "test"
        if current_quest == 13:
            "test"
        if current_quest == 14:
            "test"
        if current_quest == 15:
            "you just gotta fuck june's face!"
        $ tavern_quests_complete +=1
        $ tavern_quest_time = 0
    else:

        $ quest_minutes_remaining = ((tavern_quest_time - TimeModule.time())/60)
        python:
            minutes_answer = str(round(quest_minutes_remaining, 2))

        "\"{b}[tavern_quest_name]{/b}\" has {b}[minutes_answer]{/b} minute(s) remaining."


    jump tavern_quest_menu


label tavern_quest_menu:




    menu:
        "start quest":



            jump start_tavern_quest
        "check quest":

            jump check_tavern_quest
        "tutorial":

            show blackveil with dissolve
            "people in need sometimes post quests on the local notice board, located in your tavern."
            "adventurers come from all over to take on these quests, often fighting over the few available ones."
            "as the tavern owner, you have the final say over who gets which quests, and you receive some of the reward."
            "There is sometimes an adventurer better suited for the quest, but there are no wrong options... follow your gut!"
            "these quests happen in real time, so the quest timer will continue even if the game isn't running."
            "the last few quests will require you to completely upgrade the tavern."
            "good luck - adventure awaits!"
            hide blackveil with dissolve
            jump tavern_quest_menu
        "back":

            if bk3_loveroute:
                jump love_inside_tavern_shack
            else:
                jump inside_tavern_shack
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
