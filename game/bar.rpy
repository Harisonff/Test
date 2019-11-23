init python:

    def drink_dragged1(drags, drop):
        
        if not drop:
            return
        
        store.drink1 = drags[0].drag_name
        store.mixer = drop.drag_name
        
        return True

    def drink_dragged2(drags, drop):
        
        if not drop:
            return
        
        store.drink2 = drags[0].drag_name
        store.mixer = drop.drag_name
        
        return True

screen bar_screen1:


    add "fbackgrounds/bg_a_tavern_dark.jpg"
    if bar_unlocked:
        imagebutton idle "bar/book.png" hover "bar/book_hover.png" xpos 478 ypos 500 action Jump("bar_book1") focus_mask True

    if randbar ==1:
        text "{color=#ffffff}wanker" xpos 470 ypos 100
    if randbar ==2:
        text "{color=#ffffff}tickleberry" xpos 460 ypos 100
    if randbar ==3:
        text "{color=#ffffff}slapdapper" xpos 460 ypos 100
    if randbar ==4:
        text "{color=#ffffff}slumpthumper" xpos 450 ypos 100
    if randbar ==5:
        text "{color=#ffffff}hank" xpos 460 ypos 100
    if randbar ==6:
        text "{color=#ffffff}little tart" xpos 460 ypos 100
    if randbar ==7:
        text "{color=#ffffff}old juice" xpos 470 ypos 100
    if randbar ==8:
        text "{color=#ffffff}coinpouch" xpos 460 ypos 100




    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged1
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged1
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged1
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged1
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged1
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged1
            xpos 800 ypos 400


        drag:
            drag_name "Mixer"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

screen bar_screen2:


    add "fbackgrounds/bg_a_tavern_dark.jpg"
    if bar_unlocked:
        imagebutton idle "bar/book.png" hover "bar/book_hover.png" xpos 478 ypos 500 action Jump("bar_book2") focus_mask True

    if randbar ==1:
        text "{color=#ffffff}wanker" xpos 470 ypos 100
    if randbar ==2:
        text "{color=#ffffff}tickleberry" xpos 460 ypos 100
    if randbar ==3:
        text "{color=#ffffff}slapdapper" xpos 460 ypos 100
    if randbar ==4:
        text "{color=#ffffff}slumpthumper" xpos 450 ypos 100
    if randbar ==5:
        text "{color=#ffffff}hank" xpos 460 ypos 100
    if randbar ==6:
        text "{color=#ffffff}little tart" xpos 460 ypos 100
    if randbar ==7:
        text "{color=#ffffff}old juice" xpos 470 ypos 100
    if randbar ==8:
        text "{color=#ffffff}coinpouch" xpos 460 ypos 100



    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged2
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged2
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged2
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged2
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged2
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged2
            xpos 800 ypos 400


        drag:
            drag_name "Mixer"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

label barroom_first:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label barroom_second:

    "What else?"

    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."

    if drink1 == "red" and drink2 == "blue":
        t "well done!"
    else:

        t "uh oh."
        t "let's try that again."
        t "one part red, one part blue."
        t "in that order."
        jump barroom_first


label first_mix:
    t "we've also got an old book of mixes around here somewhere..."
    hide tf with dissolve
    yd "......"
    show tf with dissolve
    t "here it is!"
    t "feel free to look through it when you get an order, but doing so will probably affect your tips."
    t "now i'll leave you to it!"
    hide tf with dissolve
    $ bar_unlocked = True
    jump zftavern_day1

label bar_book1:
    $ used_book = True
    menu:
        "wanker":
            "red, then blue."
            jump bar_book1
        "tickleberry":

            "green, then pink."
            jump bar_book1
        "slapdapper":

            "yellow, then green."
            jump bar_book1
        "slumpthumper":

            "pink, then blue."
            jump bar_book1
        "hank":

            "grey, then red."
            jump bar_book1
        "little tart":

            "blue, then yellow."
            jump bar_book1
        "old juice":

            "grey, then blue."
            jump bar_book1
        "coinpouch":

            "pink, then red."
            jump bar_book1
        "return":

            if not bar_unlocked:
                jump barroom_first
            else:
                if randbar ==1:
                    jump wanker
                if randbar ==2:
                    jump tickleberry

                if randbar ==3:
                    jump slapdapper

                if randbar ==4:
                    jump slumpthumper

                if randbar ==5:
                    jump hank

                if randbar ==6:
                    jump littletart

                if randbar ==7:
                    jump oldjuice

                if randbar ==8:
                    jump coinpouch

label bar_book2:
    $ used_book = True
    menu:
        "wanker":
            "red, then blue."
            jump bar_book2
        "tickleberry":

            "green, then pink."
            jump bar_book2
        "slapdapper":

            "yellow, then green."
            jump bar_book2
        "slumpthumper":

            "pink, then blue."
            jump bar_book2
        "hank":

            "grey, then red."
            jump bar_book2
        "little tart":

            "blue, then yellow."
            jump bar_book2
        "old juice":

            "grey, then blue."
            jump bar_book2
        "coinpouch":

            "pink, then red."
            jump bar_book2
        "return":

            if not bar_unlocked:
                jump barroom_second
            else:
                if randbar ==1:
                    jump wanker2
                if randbar ==2:
                    jump tickleberry2

                if randbar ==3:
                    jump slapdapper2

                if randbar ==4:
                    jump slumpthumper2

                if randbar ==5:
                    jump hank2

                if randbar ==6:
                    jump littletart2

                if randbar ==7:
                    jump oldjuice2

                if randbar ==8:
                    jump coinpouch2



label barroom:
    $ used_book = False
    if drinks_served ==3:
        $ bar_count += 1
        if bar_count >=4:
            if zbartender:
                $ zbartender = True
            else:
                show tf with dissolve
                t "congrats! i'm making you a fulltime bartender!"
                t "you're gonna make a lot of money!"
                t "don't forget, you'll make more money if you don't have to look at recipes."
                t "and have fun!"
                hide tf with dissolve
                $ zbartender = True

        if not fdaytime:
            show tf with dissolve
            t "nicely done!"
            t "time for the next shift."
            if bar_shifts ==0:
                jump zcity_night1
            else:
                $ bar_shifts +=1
                jump zcity_night1
        else:

            show tf with dissolve
            t "nicely done!"
            t "time for the next shift."
            $ drinks_served = 0
            if bar_shifts ==0:
                jump zcity_night1
            else:
                $ bar_shifts +=1
                jump zcity_night1
    else:
        $ drinks_served +=1
        $ randbar = renpy.random.randint(1, 8)
        if randbar ==1:
            "customer" "hi there, can you make me a 'wanker'?"
            jump wanker

        if randbar ==2:
            "customer" "hi there, can you make me a 'tickleberry'?"
            jump tickleberry

        if randbar ==3:
            "customer" "hi there, can you make me a 'slapdapper'?"
            jump slapdapper

        if randbar ==4:
            "customer" "hi there, can you make me a 'slumpthumper'?"
            jump slumpthumper

        if randbar ==5:
            "customer" "hi there, can you make me a 'hank'?"
            jump hank

        if randbar ==6:
            "customer" "hi there, can you make me a 'little tart'?"
            jump littletart

        if randbar ==7:
            "customer" "hi there, can you make me a 'old juice'?"
            jump oldjuice

        if randbar ==8:
            "customer" "hi there, can you make me a 'coinpouch'?"
            jump coinpouch

label wanker:

    call screen bar_screen1

    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label wanker2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "red" and drink2 == "blue":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label tickleberry:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label tickleberry2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "green" and drink2 == "pink":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label slapdapper:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label slapdapper2:


    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "yellow" and drink2 == "green":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label slumpthumper:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label slumpthumper2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "pink" and drink2 == "blue":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label hank:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label hank2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "grey" and drink2 == "red":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label littletart:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label littletart2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "blue" and drink2 == "yellow":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label oldjuice:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label oldjuice2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "grey" and drink2 == "blue":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom

label coinpouch:

    call screen bar_screen1
    play sound "audio/bubbles.ogg"
    "Okay, we'll send [drink1] to the [mixer]."

label coinpouch2:



    call screen bar_screen2
    play sound "audio/bubbles.ogg"
    "Okay, let's check what we've made."
    if drink1 == "pink" and drink2 == "red":
        if zbartender:
            if used_book:
                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 30 coins!"
                $ fmoney +=30
                jump barroom
            else:

                "customer" "cheers!"
                play sound "audio/money.mp3"
                "you got 45 coins!"
                $ fmoney +=45
                jump barroom
        else:

            if used_book:
                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    jump barroom
                else:

                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 5 coins!"
                    $ fmoney +=5
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    t "plus, you had to look up instructions."
                    hide tf with dissolve
                    $ bar_training_talk = True
                    jump barroom
            else:

                if bar_training_talk:
                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    jump barroom
                else:


                    "customer" "cheers!"
                    play sound "audio/money.mp3"
                    "you got 8 coins!"
                    $ fmoney +=8
                    y "...that's it?"
                    show tf with dissolve
                    t "don't forget that you're still in training."
                    t "work a few shifts and you'll start making real money."
                    $ bar_training_talk = True
                    jump barroom
    else:


        "customer" "this isn't what I ordered."
        "customer" "i'm not paying for this."
        "customer" "...but i'm still going to drink it."
        "you make no money."
        jump barroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
