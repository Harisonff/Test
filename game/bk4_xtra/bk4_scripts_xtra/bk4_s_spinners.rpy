
init:
    image doorspinner sad:
        "bk4_xtra/spinners/door_sad.png"
        xanchor 0.5 xzoom 1.0
        linear 0.3 xzoom -1.0


    image doorspinner smile:
        "bk4_xtra/spinners/door_smile.png"
        xanchor 0.5 xzoom 1.0
        linear 0.3 xzoom -1.0


    image doorspinner symbol:
        "bk4_xtra/spinners/door_symbol.png"
        xanchor 0.5 xzoom 1.0
        linear 0.3 xzoom -1.0


screen bk4_spinner_stats:
    frame:
        xminimum 150
        has vbox
        text "spinner level: [spinner_level]"
        text "to next level: [spinner_level_remaining]"


label first_spinner:

    $ door_1 = 'active'
    $ door_2 = 'active'
    $ door_3 = 'active'

    $ door_state = 'sad'

    $ spin_turns = 0



label startspin:

    if spinner_level ==8:
        if spin_points_total <75:
            $ spin_points_total = 75

    show expression "bk4_xtra/spinners/bg.jpg"
    if not b4_daytime:
        show expression "bk4_xtra/remove/blackveil.png"
    if not first_spinners:
        $ first_spinners = True
        show bfab bfab24
        with dissolve
        kn "so... what am i looking at here?"

        tn "my question exactly..."
        show bfae jinora02:
            xpos -600
        with dissolve
        jino "the spinners train reflex, and teach you how to move fluidly and unpredictably."
        jino "they teach you how to be like the wind!"
        kn "oh... kay..."
        jino "try to line up the spinners, so they're all the same."
        jino "the more you line up, the better your training results will be."
        jino "i'll blast them with some air, and get them spinning, and you can try it out!"
        tn "wait... you can airbend?"
        jino "well, yeah!"
        tn "i thought i was the only airbender?"
        jino "the only airbending {i}master{/i}."
        jino "you've been teaching me how to airbend for years."
        jino "why don't you show korra how it's done?"
        jino "remember you can only go through them {b}while they're spinning{/b}."
        jino "when they have an image facing forward, it won't work."
        tn "uh... alright..."
        hide bfae
        hide bfab
        with fade
        hide expression "bk4_xtra/spinners/bg.jpg"

    if spin_turns != 3:
        show screen stop_screen 
        show screen bk4_spinner_stats

    show expression "bk4_xtra/spinners/bg.jpg"



    if spin_turns <= 0:
        if door_state == 'sad':
            show doorspinner smile as door1:
                xpos 300 ypos 30
        elif door_state == 'smile':
            show doorspinner symbol as door1:
                xpos 300 ypos 30
        elif door_state == 'symbol':
            show doorspinner sad as door1:
                xpos 300 ypos 30
    else:

        if door_1 == 'sad':
            show expression "bk4_xtra/spinners/door_sad.png" as door1:
                xpos 300 ypos 30 xanchor 0.5
        elif door_1 == 'smile':
            show expression "bk4_xtra/spinners/door_smile.png" as door1:
                xpos 300 ypos 30 xanchor 0.5
        elif door_1 == 'symbol':
            show expression "bk4_xtra/spinners/door_symbol.png" as door1:
                xpos 300 ypos 30 xanchor 0.5




    if spin_turns <= 1:

        if door_state == 'sad':
            show doorspinner smile as door2:
                xpos 500 ypos 30
        elif door_state == 'smile':
            show doorspinner symbol as door2:
                xpos 500 ypos 30
        elif door_state == 'symbol':
            show doorspinner sad as door2:
                xpos 500 ypos 30
    else:

        if door_2 == 'sad':
            show expression "bk4_xtra/spinners/door_sad.png" as door2:
                xpos 500 ypos 30 xanchor 0.5
        elif door_2 == 'smile':
            show expression "bk4_xtra/spinners/door_smile.png" as door2:
                xpos 500 ypos 30 xanchor 0.5
        elif door_2 == 'symbol':
            show expression "bk4_xtra/spinners/door_symbol.png" as door2:
                xpos 500 ypos 30 xanchor 0.5



    if spin_turns <= 2:

        if door_state == 'sad':
            show doorspinner smile as door3:
                xpos 700 ypos 30
        elif door_state == 'smile':
            show doorspinner symbol as door3:
                xpos 700 ypos 30
        elif door_state == 'symbol':
            show doorspinner sad as door3:
                xpos 700 ypos 30
    else:


        if door_3 == 'sad':
            show expression "bk4_xtra/spinners/door_sad.png" as door3:
                xpos 700 ypos 30 xanchor 0.5
        elif door_3 == 'smile':
            show expression "bk4_xtra/spinners/door_smile.png" as door3:
                xpos 700 ypos 30 xanchor 0.5
        elif door_3 == 'symbol':
            show expression "bk4_xtra/spinners/door_symbol.png" as door3:
                xpos 700 ypos 30 xanchor 0.5


    if spin_turns == 3:
        jump endspin


    if door_state == 'sad':
        $ door_state = 'smile'
    elif door_state == 'smile':
        $ door_state = 'symbol'
    elif door_state == 'symbol':
        $ door_state = 'sad'

    $ renpy.pause(0.3, hard=True)



    jump startspin


screen stop_screen:

    vbox xalign 0.9 yalign 0.4:
        imagebutton:
            idle "bk4_xtra/spinners/symbol_idle.png"
            hover "bk4_xtra/spinners/symbol_hover.png"
            action Jump("whatup")





label whatup:
    hide screen stop_screen
    hide screen bk4_spinner_stats

    if spin_turns == 0:
        $ door_1 = door_state
    if spin_turns == 1:
        $ door_2 = door_state
    if spin_turns == 2:
        $ door_3 = door_state

    $ spin_turns += 1


    $ renpy.pause(0.2, hard=True)
    scene
    jump startspin

label endspin:
    if door_1 == door_2:
        if door_2 == door_3:
            "3 points!"
            $ spin_points_temp = 3
            $ spin_points_total += 3
            jump spin_conc
        else:
            "2 points!"
            $ spin_points_temp = 2
            $ spin_points_total += 2
            jump spin_conc
    if door_2 == door_3:
        if door_1 == door_2:
            "3 points!"
            $ spin_points_temp = 3
            $ spin_points_total += 3
            jump spin_conc
        else:
            "2 points!"
            $ spin_points_temp = 2
            $ spin_points_total += 2
            jump spin_conc
    if door_1 == door_3:
        if door_1 == door_2:
            "3 points!"
            $ spin_points_temp = 3
            $ spin_points_total += 3
            jump spin_conc
        else:
            "2 points!"
            $ spin_points_temp = 2
            $ spin_points_total += 2
            jump spin_conc
    else:
        "1 point."
        $ spin_points_temp = 1
        $ spin_points_total += 1
        jump spin_conc


label spin_conc:
    if airbending <2:
        show bfae jinora02:
            xpos -600
        show bfab bfab04
        with dissolve
        if spin_points_temp ==3:
            jino "wow! that was incredible!"
        if spin_points_temp ==2:
            jino "not bad."
        if spin_points_temp ==1:
            jino "oof, that was not your best."
    else:
        if airbending <=2:
            if spin_points_temp ==3:
                tn "hey! i did pretty well!"
            if spin_points_temp ==2:
                tn "i didn't do too badly."
            if spin_points_temp ==1:
                tn "oof, that was not my best."

    if spinner_level ==1:
        if spin_points_total >=1:
            $ spinner_level = 2
            $ spinner_level_up = True
            $ spinner_level_remaining = (5-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==2:
        if spin_points_total >=5:
            $ spinner_level = 3
            $ spinner_level_up = True
            $ spinner_level_remaining = (15-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (5-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==3:
        if spin_points_total >=15:
            $ spinner_level = 4
            $ spinner_level_up = True
            $ spinner_level_remaining = (30-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (15-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==4:
        if spin_points_total >=30:
            $ spinner_level = 5
            $ spinner_level_up = True
            $ spinner_level_remaining = (45-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (30-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0

    if spinner_level ==5:
        if spin_points_total >=45:
            $ spinner_level = 6
            $ spinner_level_up = True
            $ spinner_level_remaining = (60-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (45-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0

    if spinner_level ==6:
        if spin_points_total >=60:
            $ spinner_level = 7
            $ spinner_level_up = True
            $ spinner_level_remaining = (75-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (60-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0

    if spinner_level ==7:
        if spin_points_total >=75:
            $ spinner_level = 8
            $ spinner_level_up = True
            $ spinner_level_remaining = (85-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (75-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==8:
        if spin_points_total >=85:
            $ spinner_level = 9
            $ spinner_level_up = True
            $ spinner_level_remaining = (100-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (85-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==9:
        if spin_points_total >=100:
            $ spinner_level = 10
            $ spinner_level_up = True
            $ spinner_level_remaining = (115-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (100-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==10:
        if spin_points_total >=115:
            $ spinner_level = 11
            $ spinner_level_up = True
            $ spinner_level_remaining = (130-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (115-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
    if spinner_level ==11:
        if spin_points_total >=130:
            $ spinner_level = 12
            $ spinner_level_up = True
            $ spinner_level_remaining = 0
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0
        else:
            $ spinner_level_remaining = (130-spin_points_total)
            if spinner_level_remaining <=0:
                $ spinner_level_remaining = 0


    if spinner_level_up:
        $ spinner_level_up = False
        play sound "audio/win2.mp3"
        "{b}you reached spinner level [spinner_level]!{/b}"

    if airbending ==1:
        if spinner_level <3:
            jino "you should keep trying."
            hide bfae jinora02
            hide bfab
        if spinner_level >=3:
            jino "alright!"
            jino "your turn, korra."
            jump after_spinners2


    if first_spinners and not first_spinners_conc:
        $ first_spinners_conc = True
        jino "your turn, korra!"
        kn "oh... uh..."
        kn "okay..."
        show black with Dissolve(1.5)
        "korra steps into the spinners, and..."
        "...get the shit beaten out of her by the quickly rotating panels."
        jump after_spinners

    if airbending >=2:
        menu:
            "continue":
                jump first_spinner
            "exit":
                jump bk4_train

    jump first_spinner
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
