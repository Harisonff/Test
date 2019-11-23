init python:

    def drink_dragged3(drags, drop):
        
        if not drop:
            return
        
        store.drink3 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

    def drink_dragged4(drags, drop):
        
        if not drop:
            return
        
        store.drink4 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

    def drink_dragged5(drags, drop):
        
        if not drop:
            return
        
        store.drink5 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

    def drink_dragged6(drags, drop):
        
        if not drop:
            return
        
        store.drink6 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

    def drink_dragged7(drags, drop):
        
        if not drop:
            return
        
        store.drink7 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

    def drink_dragged8(drags, drop):
        
        if not drop:
            return
        
        store.drink8 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

    def drink_dragged9(drags, drop):
        
        if not drop:
            return
        
        store.drink9 = drags[0].drag_name
        store.tumbler = drop.drag_name
        
        return True

screen e_bar_screen1:


    if suki_bar_blow ==6:
        add "ebackgrounds/bar.jpg"
        add "toxc toxc03"
        add "bk3/suki/barblow/top.png":
            alpha 0.8
        add "bk3/suki/barblow/arm_holddick.png"
    elif bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    elif not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"





















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged3
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged3
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged3
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged3
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged3
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged3
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

screen e_bar_screen2:


    if suki_bar_blow ==6:
        add "ebackgrounds/bar.jpg"
        add "toxc toxc03"
        add "bk3/suki/barblow/top.png":
            alpha 0.8
        add "bk3/suki/barblow/arm_holddick.png"
    elif bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    elif not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"




















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged4
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged4
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged4
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged4
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged4
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged4
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160


screen e_bar_screen3:


    if bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    if not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"




















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged5
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged5
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged5
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged5
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged5
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged5
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

screen e_bar_screen4:


    if bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    if not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"




















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged6
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged6
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged6
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged6
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged6
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged6
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

screen e_bar_screen5:


    if bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    if not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"




















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged7
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged7
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged7
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged7
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged7
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged7
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

screen e_bar_screen6:


    if bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    if not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"




















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged8
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged8
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged8
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged8
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged8
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged8
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

screen e_bar_screen7:


    if bk3_day:
        add "ebackgrounds/inside_tavern_day.jpg"
    if not bk3_day:
        add "ebackgrounds/inside_tavern_night.jpg"




















    draggroup:


        drag:
            drag_name "yellow"
            child "bar/drink1.png"
            droppable False
            dragged drink_dragged9
            xpos 50 ypos 10
        drag:
            drag_name "red"
            child "bar/drink2.png"
            droppable False
            dragged drink_dragged9
            xpos 50 ypos 200
        drag:
            drag_name "grey"
            child "bar/drink3.png"
            droppable False
            dragged drink_dragged9
            xpos 50 ypos 400
        drag:
            drag_name "blue"
            child "bar/drink4.png"
            droppable False
            dragged drink_dragged9
            xpos 800 ypos 10
        drag:
            drag_name "green"
            child "bar/drink5.png"
            droppable False
            dragged drink_dragged9
            xpos 800 ypos 200
        drag:
            drag_name "pink"
            child "bar/drink6.png"
            droppable False
            dragged drink_dragged9
            xpos 800 ypos 400


        drag:
            drag_name "tumbler"
            child "bar/mixer.png"
            draggable False
            xpos 420 ypos 160

label bk3_love_bartend:
    y "alright, time to make some drinks."
    jump earth_tavern

label earth_tavern1:
    if not earth_tavern_start:
        $ earth_tavern_start = True
        y "huh. that wasn't so bad."
        y "i can totally handle this."

    if bk3_love_bartending >=1 and bk3_love_bartending <4:
        $ bk3_love_bartending +=1
    if bk3_love_bartending ==4:
        if bk3_bar_level ==1:
            if bk3_bar_wins == 1:
                $ bk3_bar_payout = 3
            if bk3_bar_wins ==3:
                $ bk3_bar_payout = 7
            if bk3_bar_wins == 4:
                $ bk3_bar_payout = 10
            if bk3_bar_wins == 5:
                $ bk3_bar_payout = 12
            if bk3_bar_wins ==6:
                $ bk3_bar_payout = 15

            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

        elif bk3_bar_level ==2:

            if bk3_bar_wins == 3:
                $ bk3_bar_payout = 7
            if bk3_bar_wins ==6:
                $ bk3_bar_payout = 15
            if bk3_bar_wins ==7:
                $ bk3_bar_payout = 17
            if bk3_bar_wins ==10:
                $ bk3_bar_payout = 23
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

        elif bk3_bar_level ==3:

            if bk3_bar_wins == 4:
                $ bk3_bar_payout = 15
            if bk3_bar_wins ==8:
                $ bk3_bar_payout = 20
            if bk3_bar_wins ==10:
                $ bk3_bar_payout = 23
            if bk3_bar_wins ==14:
                $ bk3_bar_payout = 30
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

        y "neat."
        show tosi tosi03
        show tosi_blink
        with moveinright
        suki "damn..."
        y "welcome back!"
        y "i'll have you know i only barely didn't know what i was doing."
        y "...what's wrong?"
        hide tosi_blink
        show tosi tosi01
        with dissolve
        suki "i followed some leads and found the other kyoshi warriors..."
        y "that seems like good news."
        suki "yes, but... they're harder to get to than i was hoping."
        y "are they in the tunnels?"
        y "do you need a hand?"
        suki "they're not in the tunnels."
        suki "it's worse."
        y "worse?"
        suki "they're in a secret dungeon within in the palace."
        suki "there's just no way to get in there."
        y "are you sure?"
        y "there's gotta be a way."
        suki "maybe..."
        suki "i'll keep looking into it."
        suki "thanks, aang."
        suki "come by later if you have some time."
        suki "i might need your help again."
        $ suki_bar_blow = 3
        $ bk3_love_bartending = 5
        $ bk3_day = False

        if bk3_loveroute == True:
            jump love_bk3_village_background
        else:
            jump bk3_village_background



    if bk3_love_bartending >=7 and bk3_love_bartending <10:
        $ bk3_love_bartending +=1
    if bk3_love_bartending ==10:
        if bk3_bar_level ==1:

            if bk3_bar_wins == 1:
                $ bk3_bar_payout = 3
            if bk3_bar_wins ==3:
                $ bk3_bar_payout = 7
            if bk3_bar_wins == 4:
                $ bk3_bar_payout = 10
            if bk3_bar_wins == 5:
                $ bk3_bar_payout = 12
            if bk3_bar_wins ==6:
                $ bk3_bar_payout = 15
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

        elif bk3_bar_level ==2:

            if bk3_bar_wins == 3:
                $ bk3_bar_payout = 7
            if bk3_bar_wins ==6:
                $ bk3_bar_payout = 15
            if bk3_bar_wins ==7:
                $ bk3_bar_payout = 17
            if bk3_bar_wins ==10:
                $ bk3_bar_payout = 23
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

        elif bk3_bar_level ==3:

            if bk3_bar_wins == 4:
                $ bk3_bar_payout = 15
            if bk3_bar_wins ==8:
                $ bk3_bar_payout = 20
            if bk3_bar_wins ==10:
                $ bk3_bar_payout = 23
            if bk3_bar_wins ==14:
                $ bk3_bar_payout = 30
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

        y "boom daddy."
        show tosi tosi01
        show tosi_blink
        with moveinright
        suki "hmmmmm....."
        y "how'd it go?"
        hide tosi_blink with dissolve
        suki "I made progress, but..."
        suki "...it's not exactly what i wanted."
        y "what do you mean?"
        show tosi_blink with dissolve
        suki "the only way to get them out is by bribing certain guards."
        suki "it'll take me a while to make the money together."
        hide tosi_blink with dissolve
        suki "thanks for helping me out."
        suki "come by later, maybe i'll come up with an idea or something."
        hide tosi with dissolve
        $ bk3_day = False
        $ bk3_love_bartending = 11

        if bk3_loveroute == True:
            jump love_bk3_village_background
        else:
            jump bk3_village_background

    if bk3_bar_level ==1:
        if bk3_bar_memory <3:
            jump earth_tavern
        else:

            if bk3_bar_wins == 1:
                $ bk3_bar_payout = 3
            if bk3_bar_wins ==3:
                $ bk3_bar_payout = 7
            if bk3_bar_wins == 4:
                $ bk3_bar_payout = 10
            if bk3_bar_wins == 5:
                $ bk3_bar_payout = 12
            if bk3_bar_wins ==6:
                $ bk3_bar_payout = 15
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

            if bk3_loveroute == True:
                jump bk3_love_tavern_menu
            else:
                jump inside_tavern_shack

    if bk3_bar_level ==2:
        if bk3_bar_memory <5:
            jump earth_tavern
        else:

            if bk3_bar_wins == 3:
                $ bk3_bar_payout = 7
            if bk3_bar_wins ==6:
                $ bk3_bar_payout = 15
            if bk3_bar_wins ==7:
                $ bk3_bar_payout = 17
            if bk3_bar_wins ==10:
                $ bk3_bar_payout = 23
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

            if bk3_loveroute == True:
                jump bk3_love_tavern_menu
            else:
                jump inside_tavern_shack

    if bk3_bar_level ==3:
        if bk3_bar_memory <7:
            jump earth_tavern
        else:

            if bk3_bar_wins == 4:
                $ bk3_bar_payout = 15
            if bk3_bar_wins ==8:
                $ bk3_bar_payout = 20
            if bk3_bar_wins ==10:
                $ bk3_bar_payout = 23
            if bk3_bar_wins ==14:
                $ bk3_bar_payout = 30
            play sound "audio/money.mp3"
            $ emoney += bk3_bar_payout
            "you got [bk3_bar_payout] coins!"

            if bk3_loveroute == True:
                jump bk3_love_tavern_menu
            else:
                jump inside_tavern_shack












label earth_tavern:
    $ bk3_bar_payout = 0
    hide screen earth_money_date
    $ renpy.block_rollback()
    if bk3_bar_memory ==0:
        $ bk3_bar_memory = 1
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])

        cus "hi there, can you make me a {b}[randbar1]?"
        $ renpy.block_rollback()
        call screen e_bar_screen1

        play sound "audio/bubbles.ogg"
        "Okay, let's check what we've made."
        if drink3 == randbar1:
            cus "cheers!"
            play sound "audio/win2.mp3"
            $ bk3_bar_wins +=1
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this....but i'm still going to drink it."

        jump earth_tavern1


    if bk3_bar_memory ==1:
        $ bk3_bar_memory = 2
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar2 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])

        cus "hi there, can you make me a {b}[randbar1] & [randbar2]?"
        $ renpy.block_rollback()
        call screen e_bar_screen1

        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        "Okay, let's check what we've made."
        if drink3 == randbar1 and drink4 == randbar2:
            play sound "audio/win2.mp3"
            cus "cheers!"
            $ bk3_bar_wins +=2
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this....but i'm still going to drink it."

        jump earth_tavern1

    if bk3_bar_memory ==2:
        $ bk3_bar_memory = 3
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar2 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar3 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])

        cus "hi there, can you make me a {b}[randbar1] & [randbar2] & [randbar3]?"
        $ renpy.block_rollback()

        call screen e_bar_screen1    
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen3
        play sound "audio/bubbles.ogg"

        "Okay, let's check what we've made."
        if drink3 == randbar1 and drink4 == randbar2 and drink5 == randbar3:
            cus "cheers!"
            play sound "audio/win2.mp3"
            $ bk3_bar_wins +=3
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this....but i'm still going to drink it."

        jump earth_tavern1


    if bk3_bar_memory ==3:
        $ bk3_bar_memory = 4
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar2 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar3 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar4 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])

        cus "hi there, can you make me a {b}[randbar1] & [randbar2] & [randbar3] & [randbar4]?"
        $ renpy.block_rollback()
        call screen e_bar_screen1

        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen3
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen4

        "Okay, let's check what we've made."
        if drink3 == randbar1 and drink4 == randbar2 and drink5 == randbar3 and drink6 == randbar4:
            cus "cheers!"
            play sound "audio/win2.mp3"
            $ bk3_bar_wins +=3
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this...but i'm still going to drink it."

        jump earth_tavern1


    if bk3_bar_memory ==4:
        $ bk3_bar_memory = 5
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar2 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar3 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar4 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar5 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])

        cus "hi there, can you make me a {b}[randbar1] & [randbar2] & [randbar3] & [randbar4] & [randbar5]?"
        $ renpy.block_rollback()
        call screen e_bar_screen1

        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen3
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen4
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen5

        "Okay, let's check what we've made."
        if drink3 == randbar1 and drink4 == randbar2 and drink5 == randbar3 and drink6 == randbar4 and drink7 == randbar5:
            cus "cheers!"
            play sound "audio/win2.mp3"
            $ bk3_bar_wins +=4
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this....but i'm still going to drink it."

        jump earth_tavern1

    if bk3_bar_memory ==5:
        $ bk3_bar_memory = 6
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar2 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar3 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar4 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar5 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar6 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])

        cus "hi there, can you make me a {b}[randbar1] & [randbar2] & [randbar3] & [randbar4] & [randbar5] & [randbar6]?"
        $ renpy.block_rollback()
        call screen e_bar_screen1    
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen3
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen4
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen5
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)




        call screen e_bar_screen6

        "Okay, let's check what we've made."
        if drink3 == randbar1 and drink4 == randbar2 and drink5 == randbar3 and drink6 == randbar4 and drink7 == randbar5 and drink8 == randbar6:
            cus "cheers!"
            play sound "audio/win2.mp3"
            $ bk3_bar_wins +=4
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this....but i'm still going to drink it."

        jump earth_tavern1


    if bk3_bar_memory ==6:
        $ bk3_bar_memory = 7
        $ randbar1 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar2 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar3 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar4 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar5 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar6 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])
        $ randbar7 = renpy.random.choice(["red","blue","green","pink","yellow","grey"])


        cus "hi there, can you make me a {b}[randbar1] & [randbar2] & [randbar3] & [randbar4] & [randbar5] & [randbar6] & [randbar7]?"
        $ renpy.block_rollback()
        call screen e_bar_screen1    
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 220), (400, 180), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen2
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen3
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen4
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen5
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen6
        play sound "audio/bubbles.ogg"
        show expression "bar/mixer.png" at Move((420, 160), (400, 220), .10, bounce=True, delay=.35)
        pause(0.3)


        call screen e_bar_screen7

        "Okay, let's check what we've made."
        if drink3 == randbar1 and drink4 == randbar2 and drink5 == randbar3 and drink6 == randbar4 and drink7 == randbar5 and drink8 == randbar6 and drink9 == randbar7:
            cus "cheers!"
            play sound "audio/win2.mp3"
            $ bk3_bar_wins +=6
        else:
            cus "this isn't what I ordered."
            cus "i'm not paying for this....but i'm still going to drink it."

        jump earth_tavern1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
