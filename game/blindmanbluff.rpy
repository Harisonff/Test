image shadyguy_bluff_grin = LiveComposite(
    (1000, 720),
    (-270, 50), "shadyguy/shadyguy_grin.png",
    (475, 100), ConditionSwitch(
        "shady_card == 0", "transparent.png",
        "shady_card == 2", "d/2s.png",
        "shady_card == 3", "d/3s.png",
        "shady_card == 4", "d/4s.png",
        "shady_card == 5", "d/5s.png",
        "shady_card == 6", "d/6s.png",
        "shady_card == 7", "d/7s.png",
        "shady_card == 8", "d/8s.png",
        "shady_card == 9", "d/9s.png",
        "shady_card == 10", "d/10s.png",
        "shady_card == 11", "d/Js.png",
        "shady_card == 12", "d/Qs.png",
        "shady_card == 13", "d/Ks.png",
        "shady_card == 14", "d/As.png",
        "True", "transparent.png"
        ),
    )

image shadyguy_bluff_unsure = LiveComposite(
    (1000, 720),
    (-270, 50), "shadyguy/shadyguy_unsure.png",
    (475, 100), ConditionSwitch(
        "shady_card == 0", "transparent.png",
        "shady_card == 2", "d/2s.png",
        "shady_card == 3", "d/3s.png",
        "shady_card == 4", "d/4s.png",
        "shady_card == 5", "d/5s.png",
        "shady_card == 6", "d/6s.png",
        "shady_card == 7", "d/7s.png",
        "shady_card == 8", "d/8s.png",
        "shady_card == 9", "d/9s.png",
        "shady_card == 10", "d/10s.png",
        "shady_card == 11", "d/Js.png",
        "shady_card == 12", "d/Qs.png",
        "shady_card == 13", "d/Ks.png",
        "shady_card == 14", "d/As.png",
        "True", "transparent.png"
        ),
    )

image shadyguy_bluff_unsure2 = LiveComposite(
    (1000, 720),
    (-200, 50), im.Flip("shadyguy/shadyguy_unsure.png", horizontal=True),
    (-50, 100), ConditionSwitch(
        "shady_bro_card == 0", "transparent.png",
        "shady_bro_card == 2", "d/2h.png",
        "shady_bro_card == 3", "d/3h.png",
        "shady_bro_card == 4", "d/4h.png",
        "shady_bro_card == 5", "d/5h.png",
        "shady_bro_card == 6", "d/6h.png",
        "shady_bro_card == 7", "d/7h.png",
        "shady_bro_card == 8", "d/8h.png",
        "shady_bro_card == 9", "d/9h.png",
        "shady_bro_card == 10", "d/10h.png",
        "shady_bro_card == 11", "d/Jh.png",
        "shady_bro_card == 12", "d/Qh.png",
        "shady_bro_card == 13", "d/Kh.png",
        "shady_bro_card == 14", "d/Ah.png",
        "True", "transparent.png"
        ),
    )

label blind_man_bluff:
    $ shady_wins = 0
    $ player_shady_wins = 0
    $ remaining_bluffs = 2
    show screen bluffstats
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff










































    $ config.rollback_enabled = False

    yd "these cards are enormous..."
    sg "just lick 'em and stick 'em to yer head."
    yd "but... why? why would you have these?"
    sg "well, i banged an old lady with poor vision but hands like-"
    yd "i retract the question."
    yd "alright, let me just put mine on..."
    with ushake
    y "there."
    y "now what?"
    sg "now we chat."
    yd "...um...alright."
    sg "alright, so what have i got?"
    y "i... don't think i'm supposed to tell you."
    sg "what? of course you are. how are we supposed to play otherwise?"
    sg "i taught you the rules to this thing."
    sg "now, tell me my card or lose the round."
    menu:
        "tell him":
            $ config.rollback_enabled = False
            y "alright, your card..."
            if shady_card <= 10:
                y "[shady_card]."
            if shady_card ==11:
                y "jack."
            if shady_card ==12:
                y "queen."
            if shady_card ==13:
                y "king."
            if shady_card ==14:
                y "ace."
            if shady_card > bluff_card:
                sg "aw, horseshit."
                sg "alright, well, no point in delaying, let's lay them down."
                menu:
                    "draw another card":
                        $ config.rollback_enabled = False
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
                            if bluff_card == shady_card:
                                $ bluff_card = renpy.random.randint(2,14)
                                if bluff_card == shady_card:
                                    $ bluff_card = renpy.random.randint(2,14)
                                    if bluff_card == shady_card:
                                        $ bluff_card = renpy.random.randint(2,14)
                        y "...i don't trust you."
                        y "i'm gonna draw another card first."
                        sg "heh. smart kid."
                        sg "a little late, but better than never."
                        "you discard your card and draw another."
                        sg "first rule of blind man's bluff, kid -- once the game starts, never trust your opponent."
                        sg "still, you may not have drawn a better card, so I've got the advantage this time."
                        sg "we've both drawn our replacement... let's see what we've got."
                        jump bluff_results1
                    "lay down cards":

                        $ config.rollback_enabled = False
                        $ shady_wins +=1
                        if bluff_card <=10:
                            sg "yes! you only have a [bluff_card]."
                        if bluff_card ==11:
                            sg "yes! you only have a jack."
                        if bluff_card ==12:
                            sg "yes! you only have a queen."
                        if bluff_card ==13:
                            sg "yes! you only have a king."
                        if bluff_card ==14:
                            sg "yes! you only have an ace."
                        sg "so i win."
                        yd "...what? but i-"
                        sg "first rule of blind man's bluff, kid -- once the game starts, never trust your opponent."
                        ya "that's not fair!"
                        sg "ah, but you learned something. personal growth is important to a happy life."
                        yd "......"
                        ya "not getting cheated is important to a happy life!"
                        sg "draw again or forfeit."
                        ya "....."
                        ya "fine."
                        jump blind_man_bluff2

            if bluff_card > shady_card:
                sg "huh. shit."
                yd "what?"
                sg "well, my card's less than yours."
                sg "so i'll just redraw..."
                jump bluff_cheat_draw

                label bluff_cheat_draw:
                    $ shady_card = renpy.random.randint(2,14)

                    if shady_card == bluff_card:
                        jump bluff_cheat_draw
                    else:


                        sg "alright, what's this one?"
                        menu:
                            "tell him":
                                $ config.rollback_enabled = False
                                yd "your card is..."
                                if shady_card <=10:
                                    y "[shady_card]."
                                if shady_card ==11:
                                    y "jack."
                                if shady_card ==12:
                                    y "queen."
                                if shady_card ==13:
                                    y "king."
                                if shady_card ==14:
                                    y "ace."

                                if shady_card > bluff_card:
                                    show shadyguy_bluff_unsure
                                    hide shadyguy_bluff_grin
                                    with dissolve
                                    sg "aw, horseshit."
                                    sg "alright, well, no point in delaying, let's lay them down."
                                    menu:
                                        "draw another card":
                                            $ config.rollback_enabled = False
                                            $ bluff_card = renpy.random.randint(1,13)
                                            if bluff_card == shady_card:
                                                $ bluff_card = renpy.random.randint(1,13)
                                                if bluff_card == shady_card:
                                                    $ bluff_card = renpy.random.randint(1,13)
                                                    if bluff_card == shady_card:
                                                        $ bluff_card = renpy.random.randint(1,13)
                                                        if bluff_card == shady_card:
                                                            $ bluff_card = renpy.random.randint(1,13)
                                            y "...i don't trust you."
                                            y "i'm gonna draw another card first."
                                            sg "heh. smart kid."
                                            sg "a little late, but better than never."
                                            "you discard your card and draw another."
                                            sg "first rule of blind man's bluff, kid -- once the game starts, never trust your opponent."
                                            sg "still, you may not have drawn a better card, so I've got the advantage this time."
                                            sg "we've both drawn our replacement... let's see what we've got."
                                            jump bluff_results1
                                        "lay down cards":

                                            $ config.rollback_enabled = False
                                            $ shady_wins +=1
                                            sg "yes! you only have a [bluff_card]."
                                            sg "so i win."
                                            yd "...what? but i-"
                                            sg "first rule of blind man's bluff, kid -- once the game starts, never trust your opponent."
                                            ya "that's not fair!"
                                            sg "ah, but you learned something. personal growth is important to a happy life."
                                            yd "......"
                                            ya "not getting cheated is important to a happy life!"
                                            sg "draw again or forfeit."
                                            ya "....."
                                            ya "fine."
                                            jump blind_man_bluff2
                                else:

                                    show shadyguy_bluff_unsure
                                    hide shadyguy_bluff_grin
                                    with dissolve
                                    sg "nice! that means-"
                                    sg "uh."
                                    sg "well..."
                                    sg "....."
                                    sg "alright, fine."
                                    sg "we're still in the first round, so i'll be gracious..."
                                    sg "you might want to redraw. that's all i'll say, though."
                                    menu:
                                        "draw another card":
                                            $ config.rollback_enabled = False
                                            $ bluff_card = renpy.random.randint(2,14)
                                            if bluff_card == shady_card:
                                                $ bluff_card = renpy.random.randint(2,14)
                                                if bluff_card == shady_card:
                                                    $ bluff_card = renpy.random.randint(2,14)
                                                    if bluff_card == shady_card:
                                                        $ bluff_card = renpy.random.randint(2,14)
                                                        if bluff_card == shady_card:
                                                            $ bluff_card = renpy.random.randint(2,14)
                                            y "i'm gonna draw another card."
                                            "you discard your card and draw another."
                                            sg "heh."
                                            sg "well, I've got the advantage this time, because i tricked you."
                                            sg "but we've both drawn a replacement... so, let's see what we've got."
                                            jump bluff_results1
                                        "lay down cards":

                                            $ config.rollback_enabled = False
                                            sg "shit."
                                            sg "well, i lose this one."
                                            sg "but you're so damn naive, i still feel bad."
                                            sg "first rule of blind man's bluff, kid -- once the game starts, never trust your opponent."
                                            jump bluff_results1
                            "don't tell him":


                                $ config.rollback_enabled = False
                                yd "uh... no."
                                y "no, i don't think i'll tell you."
                                sg "now you're getting it, kid."
                                sg "first rule of blind man's bluff -- once the game starts, never trust your opponent."
                                if bluff_card <=8:
                                    sg "well, this round's done."
                                    sg "let's lay 'em down."
                                else:
                                    show shadyguy_bluff_unsure
                                    hide shadyguy_bluff_grin
                                    with dissolve
                                    sg "it's the first round still, so i'll be gracious..."
                                    sg "you might want to redraw. that's all i'll say, though."

                                menu:
                                    "draw another card":
                                        $ config.rollback_enabled = False
                                        $ bluff_card = renpy.random.randint(2,14)
                                        if bluff_card == shady_card:
                                            $ bluff_card = renpy.random.randint(2,14)
                                            if bluff_card == shady_card:
                                                $ bluff_card = renpy.random.randint(2,14)
                                                if bluff_card == shady_card:
                                                    $ bluff_card = renpy.random.randint(2,14)
                                                    if bluff_card == shady_card:
                                                        $ bluff_card = renpy.random.randint(2,14)
                                        y "i'm gonna draw another card."
                                        sg "heh."
                                        "you discard your card and draw another."
                                        sg "well, I've got the advantage this time, because i tricked you."
                                        sg "but we've both drawn a replacement... so, let's see what we've got."
                                        jump bluff_results1
                                    "lay down cards":

                                        $ config.rollback_enabled = False
                                        sg "well, I've got the advantage this time, because i tricked you."
                                        sg "but we've both drawn a replacement... so, let's see what we've got."
                                        jump bluff_results1
        "don't tell him":


            $ config.rollback_enabled = False
            yd "uh... no."
            y "no, i don't think i'll tell you."
            sg "heh. you're picking it up quick, kid."
            sg "first rule of blind man's bluff -- once the game starts, never trust your opponent."
            if bluff_card >=9:
                show shadyguy_bluff_unsure
                hide shadyguy_bluff_grin
                with dissolve
                sg "still, i feel bad that you've got-"
                sg "uh, nevermind."
                sg "how am i looking?"
            if bluff_card <=8:
                show shadyguy_bluff_unsure
                hide shadyguy_bluff_grin
                with dissolve
                sg "but damn do i hate beginner's lu-"
                sg "uh, nevermind."
                sg "how am i looking?"

            menu:
                "bluff to have him redraw" if remaining_bluffs >=1:
                    ys "oh, {i}no{/i}..."
                    ys "don't know what i'll do..."
                    sg "...not gonna trick me."
                    sg "i'm redrawing."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == shady_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == shady_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == shady_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == shady_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
                    $ remaining_bluffs -=1

                "bluff to make him stay" if remaining_bluffs >=1:
                    yc "i just hope i'm packing here."
                    sg "heh."
                    sg "well... i think i'll just keep what i've got."
                    $ remaining_bluffs -=1
                "be honest":


                    if shady_card <=5:
                        yd "not great."
                        sg "shit."
                        sg "wait. you could be lying."
                        $ randshady = renpy.random.randint(1, 2)
                        if randshady ==1:
                            sg "well... it was a coin toss, but i think i'll stick with it."
                            sg "i don't trust you."
                        if randshady ==2:
                            sg "...i'll risk a redraw."
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == shady_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == shady_card:
                                    $ shady_card = renpy.random.randint(2,14)
                                    if shady_card == shady_card:
                                        $ shady_card = renpy.random.randint(2,14)
                                        if shady_card == shady_card:
                                            $ shady_card = renpy.random.randint(2,14)
                            sg "alright, i'm ready."
                    elif shady_card >=6 and shady_card <=9:
                        yd "eh. you're okay."
                        $ randshady = renpy.random.randint(1, 2)
                        if randshady ==1:
                            sg "well... it was a coin toss, but i think i'll stick with it."
                            sg "i don't trust you."
                        if randshady ==2:
                            sg "hmm... i think i'll draw another card."
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == shady_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == shady_card:
                                    $ shady_card = renpy.random.randint(2,14)
                                    if shady_card == shady_card:
                                        $ shady_card = renpy.random.randint(2,14)
                                        if shady_card == shady_card:
                                            $ shady_card = renpy.random.randint(2,14)
                            sg "alright, i'm ready."
                    elif shady_card >=10:
                        yd "it's high, man."
                        yd "i'd stick with it."
                        sg "great- oh, you tricky dick."
                        $ randshady = renpy.random.randint(1, 2)
                        if randshady ==1:
                            sg "well... it was a coin toss, but i think i'll stick with it."
                        if randshady ==2:
                            sg "hmm... i think i'll draw another card."
                            sg "i don't trust you."
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == shady_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == shady_card:
                                    $ shady_card = renpy.random.randint(2,14)
                                    if shady_card == shady_card:
                                        $ shady_card = renpy.random.randint(2,14)
                                        if shady_card == shady_card:
                                            $ shady_card = renpy.random.randint(2,14)
                            sg "alright, i'm ready."
            menu:
                "draw another card":
                    $ config.rollback_enabled = False
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
                            if bluff_card == shady_card:
                                $ bluff_card = renpy.random.randint(2,14)
                                if bluff_card == shady_card:
                                    $ bluff_card = renpy.random.randint(2,14)
                    y "i'm gonna draw another card."
                    "you discard your card and draw another."
                    sg "alright, let's see what we've got."
                    jump bluff_results1
                "stay":

                    y "think i'm gonna stay with what i've got."
                    sg "alright, let's see what we've got."
                    jump bluff_results1


label bluff_results1:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    sg "fun, right?"
    menu:
        "no!":
            ya "no!"
            sg "you'll come around."
        "yeah!":
            y "gotta admit... i'm having more fun than i thought."
            sg "good. because i'm coming for you."
            sg "not gonna let you win easy."

    sg "so, let's try this again, eh?"
    sg "i'm pulling out all the stops now."
    jump blind_man_bluff2


label blind_man_bluff2:
    sg "let's draw."
    jump blind_man_bluff2cont

label blind_man_bluff2cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff2cont

    $ config.rollback_enabled = False
    sg "so... tell me what i've got."
    yd "uh... no."
    yd "not happening."
    sg "well, it was worth trying again."
    if bluff_card >=9:
        sg "you might want to stick with those."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you might want to stick with those."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results2
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results2


label bluff_results2:
    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    if player_shady_wins ==0:
        sg "i win again!"
        sg "that's two rounds, boy."
        sg "girl, cough up them titties-"
        ya "no!"
        sg "come again?"
        yd "i'll... uh..."
        ya "i'll up the stakes!"
        sg "...how?"
        yd "mai will... mai will give you 25 percent of her proceeds."
        m_ "zuko!"
        sg "proceeds... wait, she owns the armory?"
        sg "that's very interesting..."
        sg "alright."
        sg "we'll start over."
        sg "go 5 out of 7."
        sg "that's fair, i believe."
        jump blind_man_bluff4

    if player_shady_wins ==1:
        y "tie game."
        sg "best kind."
        sg "let's do this."
        jump blind_man_bluff3

    if player_shady_wins ==2:
        $ bluff_matches_won +=1
        y "yes!"
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        y "i win your shop, man."
        sg "no."
        ya "what?"
        sg "i'm not losing my whole shop on a 2 out of 3 deal."
        sg "we're gonna go 5 out of 7."
        ya "that wasn't the deal!"
        sg "if you want to win the shop, it's the deal!"
        ya "fine. draw, asshole!"
        jump blind_man_bluff4

label blind_man_bluff3:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "let's draw."
    jump blind_man_bluff3cont

label blind_man_bluff3cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff3cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "tough luck."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you might want to stick with those."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results3
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results3

label bluff_results3:
    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    if player_shady_wins ==1:
        sg "i win again!"
        sg "that's two rounds, boy."
        sg "girl, cough up them titties-"
        ya "no!"
        sg "come again?"
        yd "i'll... uh..."
        ya "i'll up the stakes!"
        sg "...how?"
        yd "mai will... mai will give you 25 percent of her proceeds."
        m_ "zuko!"
        sg "proceeds... wait, she owns the armory?"
        sg "that's very interesting..."
        sg "alright."
        sg "we'll start over."
        sg "go 5 out of 7."
        sg "that's fair, i believe."
        jump blind_man_bluff4

    if player_shady_wins ==2:
        $ bluff_matches_won +=1
        y "yes!"
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        y "i win your shop, man."
        sg "no."
        ya "what?"
        sg "i'm not losing my whole shop on a 2 out of 3 deal."
        sg "we're gonna go 5 out of 7."
        ya "that wasn't the deal!"
        sg "if you want to win the shop, it's the deal!"
        ya "fine. draw, asshole!"
        jump blind_man_bluff4

label blind_man_bluff4:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    $ player_shady_wins = 0
    $ shady_wins = 0
    $ remaining_bluffs = 5
    sg "let's draw."
    jump blind_man_bluff4cont

label blind_man_bluff4cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff4cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "nice cards."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "looking a little low there, friend..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results4
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results4

label bluff_results4:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    sg "bring it on, punk."
    jump blind_man_bluff5

label blind_man_bluff5:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "let's draw."
    jump blind_man_bluff5cont

label blind_man_bluff5cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff5cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're really not very good at this."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "looking a little low there, friend..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results5
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results5

label bluff_results5:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    ya "let's go!"
    jump blind_man_bluff6

label blind_man_bluff6:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff6cont

label blind_man_bluff6cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff6cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're really not very good at this."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "hmm... tough one this time..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results6
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results6

label bluff_results6:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    ya "come on!"
    show mai_fl_flip with dissolve
    m "hold on."
    m "zuko, can i talk to you for a moment?"
    menu:
        "talk to mai":
            y "sure."
            hide shadyguy_bluff_grin
            hide shadyguy_bluff_unsure
            with dissolve
            hide mai_fl_flip
            show mai_idle_ff_beach:
                xpos -250
            with dissolve
            m "i think i can help."
            yd "how?"
            m "i've been watching him, and he seems to frown when he's lying."
            m "you can still draw bad cards even knowing the difference, but-"
            yd "that's all you have?"
            show mai_idle_ff_angry:
                xpos -250
            with dissolve

            m "yeah. and i don't want to have to be naked."
            m "and you shouldn't want that either."
            m "so win."
            hide mai_idle_ff_angry
            hide mai_idle_ff_beach
            show mai_fl_flip


            show shadyguy_bluff_grin
            with dissolve
            sg "you ready to play?"
            m "i'll let you get back to it."
            hide mai_fl_flip with dissolve
            y "yeah. come on."
        "keep playing":

            ya "i'm busy, mai!"
            ya "come on, shady!"
            show mai_fl_flip_angry with dissolve
            m "fine!"
            hide mai_fl_flip_angry
            hide mai_fl_flip
            with dissolve


    jump blind_man_bluff7

label blind_man_bluff7:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff7cont

label blind_man_bluff7cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff7cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're really not very good at this."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "hmm... i'm gonna have a tough time..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results7
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results7

label bluff_results7:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0
    sg "you're doing very well for your first time."
    y "hey, thanks."
    ya "wait, stop being nice!"
    sg "i'm always nice."
    jump blind_man_bluff8

label blind_man_bluff8:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff8cont

label blind_man_bluff8cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff8cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "oh, you're intimidating."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "looking a little low, kid."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results8
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results8

label bluff_results8:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if player_shady_wins ==5:
        jump player_wins_bluff2

    if shady_wins ==5:
        jump shady_wins_bluff2

    jump blind_man_bluff9

label blind_man_bluff9:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff9cont

label blind_man_bluff9cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff9cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're looking low, friend."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "looking great, kid."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            if shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            if shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results9
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results9

label bluff_results9:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if player_shady_wins ==5:
        jump player_wins_bluff2

    if shady_wins ==5:
        jump shady_wins_bluff2

    jump blind_man_bluff10

label blind_man_bluff10:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff10cont

label blind_man_bluff10cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff10cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're looking low, friend."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "looking great, kid."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results10
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results10

label bluff_results10:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if player_shady_wins ==5:
        jump player_wins_bluff2

    if shady_wins ==5:
        jump shady_wins_bluff2

    jump blind_man_bluff11

label blind_man_bluff11:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff11cont

label blind_man_bluff11cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff11cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're looking low, friend."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "looking great, kid."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results11
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results11

label bluff_results11:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if player_shady_wins ==5:
        jump player_wins_bluff2

    if shady_wins ==5:
        jump shady_wins_bluff2

    jump blind_man_bluff12

label blind_man_bluff12:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff12cont

label blind_man_bluff12cont:
    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff12cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "looking great, kid."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "you're looking low, friend."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results12
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results12

label bluff_results12:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if player_shady_wins ==5:
        jump player_wins_bluff2

    if shady_wins ==5:
        jump shady_wins_bluff2

    jump blind_man_bluff13

label blind_man_bluff13:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "draw."
    jump blind_man_bluff13_cont

label blind_man_bluff13_cont:

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff13_cont

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're really not very good at this."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "looking a little low there, friend..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results14
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results14

label bluff_results14:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if player_shady_wins ==5:
        jump player_wins_bluff2

    if shady_wins ==5:
        jump shady_wins_bluff2

label player_wins_bluff2:
    y "yes! i win!"
    $ bluff_matches_won +=1
    jump bluff2_win

label shady_wins_bluff2:
    sg "yes! i win!"
    jump bluff2_win

label bluff2_win:
    if bluff_matches_won ==0:
        hide shadyguy_bluff_unsure
        show shadyguy_bluff_grin
        with dissolve
        sg "well, that's game."
        ya "wait!"
        sg "oh, come on."
        sg "i've won two full matches in a row."
        ya "one last, all-or-nothing match."
        y "winner of this is winner of all time."
        sg "why would i agree to that?"
        ya "i'll give you..."
        sg "you have nothing i want."
        ya "i'll give you full access to the farm!"
        sg "the... what?"
        y "the farm. where you can breed girls to your heart's content."
        sg "really? now that's interesting..."
        y "so?"
        sg "hmmm...."
        sg "let's do it."
        jump blind_man_bluff15

    if bluff_matches_won ==1:
        hide shadyguy_bluff_unsure
        show shadyguy_bluff_grin
        with dissolve
        sg "well, it looks like we might need a tie-breaker."
        sg "winner takes all."
        jump blind_man_bluff15

    if bluff_matches_won >=2:
        y "i won the whole thing!"
        jump player_win_bluff

label blind_man_bluff15:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    $ remaining_bluffs = 2
    $ shady_wins = 0
    $ player_shady_wins = 0

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff15

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're really not very good at this."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "looking a little low there, friend..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results15
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results15

label bluff_results15:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    jump blind_man_bluff16

label blind_man_bluff16:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff16

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "good card."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "oh, that's a high... nevermind."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results16
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results16

label bluff_results16:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if shady_wins ==2:
        jump shady_win_bluff

    if player_shady_wins ==2:
        jump player_win_bluff

    jump blind_man_bluff17

label blind_man_bluff17:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff17

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "good card."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "oh, that's a high... nevermind."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results17
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results17

label bluff_results17:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if shady_wins ==2:
        jump shady_win_bluff

    if player_shady_wins ==2:
        jump player_win_bluff

label shady_win_bluff:
    hide screen bluffstats
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "i win again!"
    ya "shit."
    sg "alright, where's this 'farm'?"
    sg "i haven't heard of it."
    sg "oh, wait, let me get something to write with."
    hide shadyguy_bluff_grin with dissolve
    show mai_fl_flip:
        xpos 100
    with dissolve
    m "it's okay, zuko."
    m "oh, the deed's still on the counter."
    m "it's too bad."
    menu:
        "grab deed and book it!":
            "while shady's in the back, you quickly steal the deed to the shop."
            m "what are you doing?"
            ya "let's go!"
            m "are you seri- okay!"
            scene black
            scene bg_a_beach_02
            show mai_idle_fl_beach
            with dissolve
            y ".........."
            m ".........."
            y "haha...."
            show mai_idle_fl_smile with dissolve
            m "ha..."
            y "hahaha! i can't believe we did that!"
            m "i can't believe i have the deed to the shop..."
            y "you know how all this works, is it legal?"
            m "yeah, the rules of transaction here are stiff, but whoever has the deed owns the property."
            yd "that seems like terrible oversight."
            y "but i'm not complaining."
            m "me neither."
            m "poor shady."
            y "ah, i'm sure he'll be fine."
            $ ember_deed = True
            jump mai_anal
        "lose gracefully":

            "you wait for shady to return."
            show shadyguy_bluff_grin with dissolve
            sg "hey, okay, i got it."
            sg "so where's the farm?"
            ya "it's in the city."
            sg "...that's not helpful."
            ya "so find it yourself."
            ya "come on, mai."
            sg "hey..."
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
            m "...sorry you lost all your money, though."
            yc "yeah... me too."
            $ fmoney = 0
            jump ember_party_start

label player_win_bluff:
    hide screen bluffstats
    $ bluff_matches_won +=1
    show shadyguy_bluff_unsure
    hide shadyguy_bluff_grin
    with dissolve
    sg "ah, balls."
    sg "...."
    sg "well..."
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    sg "to be honest, it's kind of a relief."
    sg "alright, here you go."
    "you got the deed for the shop!"
    ys "woo!"
    sg "oh, and here's your money back."
    y "sweet."
    sg "well, i'll start cleaning up my things."
    sg "alright, get out of here, you two."
    sg "come back later."
    sg "see ya!"
    scene black
    scene bg_a_beach_02
    show mai_idle_fl_beach
    with dissolve
    y ".........."
    m ".........."
    y "haha...."
    show mai_idle_fl_smile with dissolve
    m "ha..."
    y "hahaha! i can't believe that happened!"
    m "i can't believe i have the deed to the shop..."
    y "you know how all this property stuff works, is it legal?"
    m "yeah, the rules of transaction here are stiff, but whoever has the deed owns the property."
    yd "that seems like terrible oversight."
    y "but i'm not complaining."
    m "me neither."
    m "poor shady."
    y "ah, i'm sure he'll be fine."
    $ ember_deed = True
    jump mai_anal


label blind_man_bluff_day3:
    show shadyguy_bluff_grin
    with dissolve
    sg "alright! let's do this."
    sg "2 out of 3 wins it."
    sg "wanna place a bet on this one?"
    menu:
        "bet 25":
            if fmoney >=25:
                y "25 coins?"
                sg "sounds good."
                $ bluff_bet = 25
            else:
                y "25 coins?"
                sg "sounds good, except... i don't think you have that."
                y "woops."
                y "let's just play then."
        "bet 50":

            if fmoney >=50:
                y "50 coins?"
                sg "sounds good."
                $ bluff_bet = 50
            else:
                y "250 coins?"
                sg "sounds good, except... i don't think you have that."
                y "woops."
                y "let's just play then."
        "bet nothing":

            y "nah, let's just play a match."
            $ bluff_bet = 0

    $ shady_wins = 0
    $ player_shady_wins = 0
    $ remaining_bluffs = 2
    show screen bluffstats
    jump blind_man_bluff_day3_1

label blind_man_bluff_day3_1:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve
    $ shady_wins = 0
    $ player_shady_wins = 0

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff_day3_1

    $ config.rollback_enabled = False
    if bluff_card >=9:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "you're really not very good at this."
        sg "just saying."
        sg "how am i looking?"
    if bluff_card <=8:
        sg "looking a little low there, friend..."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results_day3_1
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results_day3_1

label bluff_results_day3_1:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    jump blind_man_bluff_day3_2

label blind_man_bluff_day3_2:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff_day3_2

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "good card."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "oh, that's a high... nevermind."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results_day3_2
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results_day3_2

label bluff_results_day3_2:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if shady_wins ==2:
        jump shady_win_bluff_day3

    if player_shady_wins ==2:
        jump player_win_bluff_day3

    jump blind_man_bluff_day3_3

label blind_man_bluff_day3_3:
    hide shadyguy_bluff_unsure
    show shadyguy_bluff_grin
    with dissolve

    $ bluff_card = renpy.random.randint(2,14)

    $ shady_card = renpy.random.randint(2,14)

    if shady_card == bluff_card:
        jump blind_man_bluff_day3_3

    $ config.rollback_enabled = False
    if bluff_card >=9:
        sg "good card."
        sg "how am i looking?"
    if bluff_card <=8:
        show shadyguy_bluff_unsure
        hide shadyguy_bluff_grin
        with dissolve
        sg "oh, that's a high... nevermind."
        sg "how am i looking?"

    menu:
        "bluff to have him redraw" if remaining_bluffs >=1:
            ys "oh, {i}no{/i}..."
            ys "don't know what i'll do..."
            sg "...not gonna trick me."
            sg "i'm redrawing."
            $ shady_card = renpy.random.randint(2,14)
            if shady_card == bluff_card:
                $ shady_card = renpy.random.randint(2,14)
                if shady_card == bluff_card:
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
            sg "alright, i'm ready."
            $ remaining_bluffs -=1

        "bluff to make him stay" if remaining_bluffs >=1:
            yc "i just hope i'm packing here."
            sg "heh."
            sg "well... i think i'll just keep what i've got."
            $ remaining_bluffs -=1
        "be honest":


            if shady_card <=5:
                yd "not great."
                sg "shit."
                sg "wait. you could be lying."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "...i'll risk a redraw."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=6 and shady_card <=9:
                yd "eh. you're okay."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                    sg "i don't trust you."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
            elif shady_card >=10:
                yd "it's high, man."
                yd "i'd stick with it."
                sg "great- oh, you tricky dick."
                $ randshady = renpy.random.randint(1, 2)
                if randshady ==1:
                    sg "well... it was a coin toss, but i think i'll stick with it."
                if randshady ==2:
                    sg "hmm... i think i'll draw another card."
                    sg "i don't trust you."
                    $ shady_card = renpy.random.randint(2,14)
                    if shady_card == bluff_card:
                        $ shady_card = renpy.random.randint(2,14)
                        if shady_card == bluff_card:
                            $ shady_card = renpy.random.randint(2,14)
                            if shady_card == bluff_card:
                                $ shady_card = renpy.random.randint(2,14)
                                if shady_card == bluff_card:
                                    $ shady_card = renpy.random.randint(2,14)
                    sg "alright, i'm ready."
    menu:
        "draw another card":
            $ config.rollback_enabled = False
            $ bluff_card = renpy.random.randint(2,14)
            if bluff_card == shady_card:
                $ bluff_card = renpy.random.randint(2,14)
                if bluff_card == shady_card:
                    $ bluff_card = renpy.random.randint(2,14)
                    if bluff_card == shady_card:
                        $ bluff_card = renpy.random.randint(2,14)
                        if bluff_card == shady_card:
                            $ bluff_card = renpy.random.randint(2,14)
            y "i'm gonna draw another card."
            "you discard your card and draw another."
            sg "alright, let's see what we've got."
            jump bluff_results_day3_3
        "stay":

            y "think i'm gonna stay with what i've got."
            sg "alright, let's see what we've got."
            jump bluff_results_day3_3

label bluff_results_day3_3:

    y "what do i have?"
    if bluff_card <=10:
        y "[bluff_card]."
    if bluff_card ==11:
        y "a jack."
    if bluff_card ==12:
        y "a queen."
    if bluff_card ==13:
        y "a king."
    if bluff_card ==14:
        y "an ace!"


    if shady_card > bluff_card:
        sg "i win!"
        $ shady_wins +=1

    if bluff_card > shady_card:
        y "i win, dickwhisperer!"
        sg "oh, uncalled for."
        $ player_shady_wins +=1

    $ shady_card = 0

    if shady_wins ==2:
        jump shady_win_bluff_day3

    if player_shady_wins ==2:
        jump player_win_bluff_day3

label shady_win_bluff_day3:
    "you lost [bluff_bet] coins."
    $ fmoney -= bluff_bet
    sg "thanks, mate."
    $ bluff_bet = 0
    hide screen bluffstats
    jump ember_shop_day3

label player_win_bluff_day3:
    "you won [bluff_bet] coins."
    $ fmoney += bluff_bet
    ys "thanks, mate."
    $ bluff_bet = 0
    hide screen bluffstats
    jump ember_shop_day3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
