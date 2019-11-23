






init:
    python:
        import math
        def Trampoline(n):
            return (0.5, 1 - math.sin(math.pi * n), 0.5, 0)

init:
    $ hammer_points = 0
    $ hammer_rounds = 0
    $ hammer_cheat = False
    $ ham_hint = False
    $ emoney = 0
    $ scams =0
    $ earth_dice_round = 0
    $ earth_dice_cheats = 2
    $ earth_dice_round_won = 0
    $ dice_tips = False
    $ cups_toph = False
    $ minigames_won = 0


















label bk3_games:

    if village_dev_explain2 and not hammer_game:
        show azss azss01
        if love_jd_hypno ==10 and suki_tylee <7:
            pass
        else:
            show toi toi04
        with dissolve
        ss "hey, nice to see you come back."
        ss "some people just can't stay away from the risk."
        ss "you wanna try your hand at a new game?"
        $ hammer_game = True
        menu:
            "yes":
                ss "nice... nice."
                ss "just select \"hammer time\" from the game list and we'll get started."
            "no":

                ss "....well the option still exists, so whatever."

    if earthbending >=3 and not dice_game:
        show azss azss01
        if love_jd_hypno ==10 and suki_tylee <7:
            pass
        else:
            show toi toi04
        with dissolve
        ss "hey, you."
        y "that's me."
        ss "don't be sassy."
        ss "i've got another game for you."
        y "oh, another one? sweet!"
        $ dice_game = True
        ss "just select \"x's and o's\" from the game list to get started."


    menu:
        "cups":
            jump dicecups_start

        "Hammer time!" if village_dev_explain2:
            if love_jd_hypno ==10 and suki_tylee <7:
                pass
            else:
                show toi toi04
                with dissolve
            if not hammer_game2:
                show azss azss01 with dissolve
                ss "Time your hammer hits to get more points!"
                ss "The closer to the center the needle is the more points you score!"

                ss "the more points you have, the more money you can make."
                ss "A full match is 3 rounds."
                $ hammer_game2 = True

                ss "Let's begin!"
                hide azss azss01 with dissolve
            if love_jd_hypno ==10 and suki_tylee <7:
                pass
            else:
                t "how do you want me to distract the crowd?"
                menu:
                    "stick your tongue out":
                        show toi toi09 with dissolve
                        t "okay..."
                        show toi toi12:
                            xzoom -1.0
                        with dissolve
                        $ scam_distraction = 1

                    "wear swimsuit" if market_stroll <2:
                        show toi toi09 with dissolve
                        t "i'm not doing that!"
                        t "i'll just stick my tongue out..."
                        show toi toi12:
                            xzoom -1.0
                        with dissolve
                        $ scam_distraction = 1

                    "wear swimsuit" if market_stroll >=2:
                        $ toph_top_nude = False
                        $ toph_bottom_nude = False
                        show toi toi210
                        with dissolve
                        $ scam_distraction = 2

                    "wear bikini" if toph_massage < 4 and not love_toph_bikini:
                        show toi toi09 with dissolve
                        t "i'm not doing that!"
                        t "i'll just stick my tongue out..."
                        show toi toi12:
                            xzoom -1.0
                        with dissolve
                        $ scam_distraction = 1

                    "wear bikini (+1 public)" if toph_massage >=4 or love_toph_bikini:
                        $ toph_public +=1
                        show toi toi09 with dissolve
                        t "okay...."
                        show toi toi21 with dissolve
                        t "........"
                        show toi toi22:
                            xzoom -1.0
                        with dissolve
                        $ scam_distraction = 3


                    "give handjob" if not toph_titjob:
                        show toi toi09 with dissolve
                        t "i'm not doing that!"
                        t "i'll just stick my tongue out..."
                        show toi toi12:
                            xzoom -1.0
                        with dissolve
                        $ scam_distraction = 1

                    "give me a handjob (+2 public)" if toph_titjob:
                        $ toph_public +=2
                        show toi toi09 with dissolve
                        t "okay..."
                        show toi toi111:
                            xzoom -1.0
                        with dissolve
                        t "....."
                        $ scam_distraction = 4


            $ emoney -=5
            jump hamjam

        "x's and o's" if earthbending >=3:
            if love_jd_hypno ==10 and suki_tylee <7:
                pass
            else:
                show toi toi04
                with dissolve
            if not dice_game2:
                show azss azss01 with dissolve
                ss "match your dice to win!"
                ss "there are three rounds per match. the more rounds you win, the better your reward!"
                $ dice_game2 = True

                ss "Let's begin!"
                hide azss azss01 with dissolve
                if love_jd_hypno ==10 and suki_tylee <7:
                    pass
                else:
                    t "hey, I can help you cheat twice per match by letting you re-roll."
                    t "how do you want me to distract the crowd?"
                    menu:
                        "stick your tongue out":
                            show toi toi09 with dissolve
                            t "okay..."
                            show toi toi12:
                                xzoom -1.0
                            with dissolve
                            $ scam_distraction = 1

                        "wear swimsuit" if market_stroll <2:
                            show toi toi09 with dissolve
                            t "i'm not doing that!"
                            t "i'll just stick my tongue out..."
                            show toi toi12:
                                xzoom -1.0
                            with dissolve
                            $ scam_distraction = 1

                        "wear swimsuit" if market_stroll >=2:
                            $ toph_top_nude = False
                            $ toph_bottom_nude = False
                            show toi toi210
                            with dissolve
                            $ scam_distraction = 2

                        "wear bikini" if toph_massage < 4 and not love_toph_bikini:
                            show toi toi09 with dissolve
                            t "i'm not doing that!"
                            t "i'll just stick my tongue out..."
                            show toi toi12:
                                xzoom -1.0
                            with dissolve
                            $ scam_distraction = 1

                        "wear bikini (+1 public)" if toph_massage >=4 or love_toph_bikini:
                            $ toph_public +=1
                            show toi toi09 with dissolve
                            t "okay...."
                            show toi toi21 with dissolve
                            t "........"
                            show toi toi22:
                                xzoom -1.0
                            with dissolve
                            $ scam_distraction = 3

                        "give handjob" if not toph_titjob:
                            show toi toi09 with dissolve
                            t "i'm not doing that!"
                            t "i'll just stick my tongue out..."
                            show toi toi12:
                                xzoom -1.0
                            with dissolve
                            $ scam_distraction = 1

                        "give me a handjob (+2 public)" if toph_titjob:
                            $ toph_public +=2
                            show toi toi09 with dissolve
                            t "um... okay..."
                            t "if... you really think that's best..."
                            show toi toi111:
                                xzoom -1.0
                            with dissolve
                            t "....."
                            $ scam_distraction = 4

            $ emoney -=5
            jump earth_dice
        "back":

            if bk3_loveroute:
                jump love_bk3_market
            else:
                jump bk3_market







label hamjam:
    show screen hamish
    $ hm = 0
    show hammer_toph_wait
    show hammer_bar
    show hammer_line:
        xpos 0.1 ypos 0.1 xanchor 0.5
    if love_jd_hypno ==10 and suki_tylee <7:
        pass
    else:
        if scam_distraction == 1:
            hide toi toi12
            show toi toi12:
                xzoom -1.0
        if scam_distraction ==2:
            hide toi toi210
            show toi toi210
        if scam_distraction ==3:
            hide toi toi22
            show toi toi22:
                xzoom -1.0
        if scam_distraction ==4:
            hide toi toi111
            show toi toi111:
                xzoom -1.0
    jump hammer_begin

label hammer_begin:
    show screen hamish 
    if love_jd_hypno ==10 and suki_tylee <7:
        pass
    else:
        if scam_distraction == 1:
            hide toi toi12
            show toi toi12:
                xzoom -1.0
        if scam_distraction ==2:
            hide toi toi210
            show toi toi210
        if scam_distraction ==3:
            hide toi toi22
            show toi toi22:
                xzoom -1.0
        if scam_distraction ==4:
            hide toi toi111
            show toi toi111:
                xzoom -1.0
    $ hm = 1
    $ hm_xpos = 0.1
    show hammer_line at Move((0.1,1.0,0.1,1.0),(0.15,1.0,0.15,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 2
    $ hm_xpos = 0.15
    show hammer_line at Move((0.15,1.0,0.15,1.0),(0.20,1.0,0.20,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 3
    $ hm_xpos = 0.20
    show hammer_line at Move((0.20,1.0,0.20,1.0),(0.25,1.0,0.25,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 4
    $ hm_xpos = 0.25
    show hammer_line at Move((0.25,1.0,0.25,1.0),(0.30,1.0,0.30,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 5
    $ hm_xpos = 0.30
    show hammer_line at Move((0.30,1.0,0.30,1.0),(0.35,1.0,0.35,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 6
    $ hm_xpos = 0.35
    show hammer_line at Move((0.35,1.0,0.35,1.0),(0.4,1.0,0.4,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 7
    $ hm_xpos = 0.4
    show hammer_line at Move((0.40,1.0,0.40,1.0),(0.45,1.0,0.45,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 8
    $ hm_xpos = 0.45
    show hammer_line at Move((0.45,1.0,0.45,1.0),(0.5,1.0,0.5,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 9
    $ hm_xpos = 0.5
    show hammer_line at Move((0.50,1.0,0.50,1.0),(0.55,1.0,0.55,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 10
    $ hm_xpos = 0.55
    show hammer_line at Move((0.55,1.0,0.55,1.0),(0.6,1.0,0.6,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 11
    $ hm_xpos = 0.6
    show hammer_line at Move((0.60,1.0,0.60,1.0),(0.65,1.0,0.65,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 12
    $ hm_xpos = 0.65
    show hammer_line at Move((0.65,1.0,0.65,1.0),(0.7,1.0,0.7,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 13
    $ hm_xpos = 0.7
    show hammer_line at Move((0.70,1.0,0.70,1.0),(0.75,1.0,0.75,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 14
    $ hm_xpos = 0.75
    show hammer_line at Move((0.75,1.0,0.75,1.0),(0.8,1.0,0.8,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 15
    $ hm_xpos = 0.8
    show hammer_line at Move((0.80,1.0,0.80,1.0),(0.85,1.0,0.85,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 16
    $ hm_xpos = 0.85
    show hammer_line at Move((0.85,1.0,0.85,1.0),(0.9,1.0,0.9,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 17
    $ hm_xpos = 0.9
    show hammer_line at Move((0.90,1.0,0.90,1.0),(0.91,1.0,0.91,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 18
    $ hm_xpos = 0.91
    show hammer_line at Move((0.91,1.0,0.91,1.0),(0.9,1.0,0.9,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 19
    $ hm_xpos = 0.9
    show hammer_line at Move((0.85,1.0,0.85,1.0),(0.85,1.0,0.85,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 20
    $ hm_xpos = 0.85
    show hammer_line at Move((0.8,1.0,0.8,1.0),(0.8,1.0,0.8,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 21
    $ hm_xpos = 0.8
    show hammer_line at Move((0.75,1.0,0.75,1.0),(0.7,1.0,0.7,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 22
    $ hm_xpos = 0.7
    show hammer_line at Move((0.7,1.0,0.7,1.0),(0.65,1.0,0.65,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 23
    $ hm_xpos = 0.65
    show hammer_line at Move((0.65,1.0,0.65,1.0),(0.6,1.0,0.6,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 24
    $ hm_xpos = 0.6
    show hammer_line at Move((0.6,1.0,0.6,1.0),(0.55,1.0,0.55,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 25
    $ hm_xpos = 0.55
    show hammer_line at Move((0.55,1.0,0.55,1.0),(0.5,1.0,0.5,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 26
    $ hm_xpos = 0.5
    show hammer_line at Move((0.5,1.0,0.5,1.0),(0.45,1.0,0.45,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 27
    $ hm_xpos = 0.45
    show hammer_line at Move((0.45,1.0,0.45,1.0),(0.4,1.0,0.4,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 28
    $ hm_xpos = 0.4
    show hammer_line at Move((0.4,1.0,0.4,1.0),(0.35,1.0,0.35,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 29
    $ hm_xpos = 0.35
    show hammer_line at Move((0.35,1.0,0.35,1.0),(0.3,1.0,0.3,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 30
    $ hm_xpos = 0.3
    show hammer_line at Move((0.3,1.0,0.3,1.0),(0.25,1.0,0.25,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 31
    $ hm_xpos = 0.25
    show hammer_line at Move((0.25,1.0,0.25,1.0),(0.2,1.0,0.2,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm = 32
    $ hm_xpos = 0.2
    show hammer_line at Move((0.15,1.0,0.15,1.0),(0.1,1.0,0.1,1.0),0.001)
    $ renpy.pause(0.001)
    $ hm_xpos = 0.1
    jump hammer_begin


label hamish_clicked:

    hide hammer_toph_wait

    show hammer_toph_hit:
        xpos (hm_xpos- 0.1)


    show hammer_bar with vpunch
    if love_jd_hypno ==10 and suki_tylee <7:
        pass
    else:
        if scam_distraction == 1:
            hide toi toi12
            show toi toi12:
                xzoom -1.0
        if scam_distraction ==2:
            hide toi toi210
            show toi toi210
        if scam_distraction ==3:
            hide toi toi22
            show toi toi22:
                xzoom -1.0
        if scam_distraction ==4:
            hide toi toi111
            show toi toi111:
                xzoom -1.0
    hide screen hamish

    if hm ==8 or hm ==25:
        "3 points!"
        $ hammer_points +=3
        hide hammer_toph_hit
        show hammer_toph_wait
        jump hammer_end

    if not ham_hint:
        $ ham_hint = True
        if love_jd_hypno ==10 and suki_tylee <7:
            pass
        else:
            "Toph can aid you by distracting the public. That way you can move the needle a little to the left or right, but only once per match."

    if hammer_cheat or not bk3_day:

        if hm ==1:
            $ hammer_points +=1
            "1 point!"
        if hm ==2:
            $ hammer_points +=1
            "1 point!"
        if hm ==3:
            $ hammer_points +=1
            "1 point!"
        if hm ==4:
            $ hammer_points +=2
            "2 points!"
        if hm ==5:
            $ hammer_points +=2
            "2 points!"
        if hm ==6:
            $ hammer_points +=2
            "2 points!"
        if hm ==7:
            $ hammer_points +=2
            "2 points!"
        if hm ==8:
            $ hammer_points +=3
            "3 points!"
        if hm ==9:
            $ hammer_points +=2
            "2 points!"
        if hm ==10:
            $ hammer_points +=2
            "2 points!"
        if hm ==11:
            $ hammer_points +=2
            "2 points!"
        if hm ==12:
            $ hammer_points +=2
            "2 points!"
        if hm ==13:
            $ hammer_points +=1
            "1 point!"
        if hm ==14:
            $ hammer_points +=1
            "1 point!"
        if hm ==15:
            $ hammer_points +=1
            "1 point!"
        if hm ==16:
            $ hammer_points +=1
            "1 point!"
        if hm ==17:
            $ hammer_points +=1
            "1 point!"
        if hm ==18:
            $ hammer_points +=1
            "1 point!"
        if hm ==19:
            $ hammer_points +=1
            "1 point!"
        if hm ==20:
            $ hammer_points +=1
            "1 point!"
        if hm ==21:
            $ hammer_points +=2
            "2 points!"
        if hm ==22:
            $ hammer_points +=2
            "2 points!"
        if hm ==23:
            $ hammer_points +=2
            "2 points!"
        if hm ==24:
            $ hammer_points +=2
            "2 points!"
        if hm ==25:
            $ hammer_points +=3
            "3 points!"
        if hm ==26:
            $ hammer_points +=2
            "2 points!"
        if hm ==27:
            $ hammer_points +=2
            "2 points!"
        if hm ==28:
            $ hammer_points +=2
            "2 points!"
        if hm ==29:
            $ hammer_points +=2
            "2 points!"
        if hm ==30:
            $ hammer_points +=1
            "1 point!"
        if hm ==31:
            $ hammer_points +=1
            "1 point!"
        if hm ==32:
            $ hammer_points +=1
            "1 point!"

        hide hammer_toph_hit
        show hammer_toph_wait


        jump hammer_end

    if love_jd_hypno ==10 and suki_tylee <7:
        hide hammer_toph_hit
        show hammer_toph_wait

        if hm ==1:
            $ hammer_points +=1
            "1 point!"
        if hm ==2:
            $ hammer_points +=1
            "1 point!"
        if hm ==3:
            $ hammer_points +=1
            "1 point!"
        if hm ==4:
            $ hammer_points +=2
            "2 points!"
        if hm ==5:
            $ hammer_points +=2
            "2 points!"
        if hm ==6:
            $ hammer_points +=2
            "2 points!"
        if hm ==7:
            $ hammer_points +=2
            "2 points!"
        if hm ==8:
            $ hammer_points +=3
            "3 points!"
        if hm ==9:
            $ hammer_points +=2
            "2 points!"
        if hm ==10:
            $ hammer_points +=2
            "2 points!"
        if hm ==11:
            $ hammer_points +=2
            "2 points!"
        if hm ==12:
            $ hammer_points +=2
            "2 points!"
        if hm ==13:
            $ hammer_points +=1
            "1 point!"
        if hm ==14:
            $ hammer_points +=1
            "1 point!"
        if hm ==15:
            $ hammer_points +=1
            "1 point!"
        if hm ==16:
            $ hammer_points +=1
            "1 point!"
        if hm ==17:
            $ hammer_points +=1
            "1 point!"
        if hm ==18:
            $ hammer_points +=1
            "1 point!"
        if hm ==19:
            $ hammer_points +=1
            "1 point!"
        if hm ==20:
            $ hammer_points +=1
            "1 point!"
        if hm ==21:
            $ hammer_points +=2
            "2 points!"
        if hm ==22:
            $ hammer_points +=2
            "2 points!"
        if hm ==23:
            $ hammer_points +=2
            "2 points!"
        if hm ==24:
            $ hammer_points +=2
            "2 points!"
        if hm ==25:
            $ hammer_points +=3
            "3 points!"
        if hm ==26:
            $ hammer_points +=2
            "2 points!"
        if hm ==27:
            $ hammer_points +=2
            "2 points!"
        if hm ==28:
            $ hammer_points +=2
            "2 points!"
        if hm ==29:
            $ hammer_points +=2
            "2 points!"
        if hm ==30:
            $ hammer_points +=1
            "1 point!"
        if hm ==31:
            $ hammer_points +=1
            "1 point!"
        if hm ==32:
            $ hammer_points +=1
            "1 point!"
    else:

        menu:

            "move the needle left" if not hammer_cheat and bk3_day:
                if not bk3_day:
                    "toph is at home! you can't cheat at night..."
                    jump hammer_end

                "while Toph is distracting the crowd you move the needle a bit."
                hide hammer_toph_hit

                $ hammer_cheat = True
                if hm ==1:
                    "it can't go any more to the left!"
                    $ hammer_cheat = False
                    hide slutty_toph_1

                    jump hamish_clicked
                if hm ==2:
                    show hammer_line at Move((0.2,1.0,0.2,1.0),(0.15,1.0,0.15,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==3:
                    show hammer_line at Move((0.25,1.0,0.25,1.0),(0.2,1.0,0.2,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==4:
                    show hammer_line at Move((0.3,1.0,0.3,1.0),(0.25,1.0,0.25,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==5:
                    show hammer_line at Move((0.35,1.0,0.35,1.0),(0.3,1.0,0.3,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==6:
                    show hammer_line at Move((0.4,1.0,0.4,1.0),(0.35,1.0,0.35,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==7:
                    show hammer_line at Move((0.45,1.0,0.45,1.0),(0.4,1.0,0.4,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==8:
                    show hammer_line at Move((0.5,1.0,0.5,1.0),(0.45,1.0,0.45,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==9:
                    show hammer_line at Move((0.55,1.0,0.55,1.0),(0.5,1.0,0.5,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=3
                    "3 points!"
                if hm ==10:
                    show hammer_line at Move((0.6,1.0,0.6,1.0),(0.55,1.0,0.55,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==11:
                    show hammer_line at Move((0.65,1.0,0.65,1.0),(0.6,1.0,0.6,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==12:
                    show hammer_line at Move((0.7,1.0,0.7,1.0),(0.65,1.0,0.65,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==13:
                    show hammer_line at Move((0.75,1.0,0.75,1.0),(0.7,1.0,0.7,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==14:
                    show hammer_line at Move((0.8,1.0,0.8,1.0),(0.75,1.0,0.75,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==15:
                    show hammer_line at Move((0.85,1.0,0.85,1.0),(0.8,1.0,0.8,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==16:
                    show hammer_line at Move((0.9,1.0,0.9,1.0),(0.85,1.0,0.85,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==17:
                    show hammer_line at Move((0.91,1.0,0.91,1.0),(0.9,1.0,0.9,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==18:
                    show hammer_line at Move((0.9,1.0,0.9,1.0),(0.85,1.0,0.85,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==19:
                    show hammer_line at Move((0.85,1.0,0.85,1.0),(0.8,1.0,0.8,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==20:
                    show hammer_line at Move((0.8,1.0,0.8,1.0),(0.75,1.0,0.75,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==21:
                    show hammer_line at Move((0.7,1.0,0.7,1.0),(0.65,1.0,0.65,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==22:
                    show hammer_line at Move((0.65,1.0,0.65,1.0),(0.6,1.0,0.6,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==23:
                    show hammer_line at Move((0.6,1.0,0.6,1.0),(0.55,1.0,0.55,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==24:
                    show hammer_line at Move((0.55,1.0,0.6,1.0),(0.5,1.0,0.5,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=3
                    "3 points!"
                if hm ==25:
                    show hammer_line at Move((0.5,1.0,0.5,1.0),(0.45,1.0,0.45,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==26:
                    show hammer_line at Move((0.45,1.0,0.45,1.0),(0.4,1.0,0.4,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==27:
                    show hammer_line at Move((0.4,1.0,0.4,1.0),(0.35,1.0,0.35,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==28:
                    show hammer_line at Move((0.4,1.0,0.4,1.0),(0.35,1.0,0.35,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==29:
                    show hammer_line at Move((0.35,1.0,0.35,1.0),(0.3,1.0,0.3,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==30:
                    show hammer_line at Move((0.3,1.0,0.3,1.0),(0.25,1.0,0.25,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==31:
                    show hammer_line at Move((0.2,1.0,0.2,1.0),(0.15,1.0,0.15,1.0),0.05)
                    $ renpy.pause(0.05)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==32:
                    "it can't go any more to the left!"
                    $ hammer_cheat = False
                    show hammer_toph_wait
                    jump hamish_clicked

                show hammer_toph_wait

            "move the needle right" if not hammer_cheat and bk3_day:
                if not bk3_day:
                    "toph is at home! you can't cheat at night..."
                    jump hammer_end

                $ hammer_cheat = True
                "while Toph is distracting the crowd you move the needle a bit."
                hide hammer_toph_hit



                if hm ==1:
                    show hammer_line at Move((0.15,1.0,0.15,1.0),(0.2,1.0,0.2,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==2:
                    show hammer_line at Move((0.2,1.0,0.2,1.0),(0.25,1.0,0.25,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==3:
                    show hammer_line at Move((0.25,1.0,0.25,1.0),(0.3,1.0,0.3,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 point!"
                if hm ==4:
                    show hammer_line at Move((0.3,1.0,0.3,1.0),(0.35,1.0,0.35,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==5:
                    show hammer_line at Move((0.35,1.0,0.35,1.0),(0.4,1.0,0.4,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==6:
                    show hammer_line at Move((0.4,1.0,0.4,1.0),(0.45,1.0,0.45,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==7:
                    show hammer_line at Move((0.45,1.0,0.45,1.0),(0.5,1.0,0.5,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=3
                    "3 points!"
                if hm ==8:
                    show hammer_line at Move((0.5,1.0,0.5,1.0),(0.55,1.0,0.55,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==9:
                    show hammer_line at Move((0.55,1.0,0.55,1.0),(0.6,1.0,0.6,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==10:
                    show hammer_line at Move((0.6,1.0,0.6,1.0),(0.65,1.0,0.65,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==11:
                    show hammer_line at Move((0.65,1.0,0.65,1.0),(0.7,1.0,0.7,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==12:
                    show hammer_line at Move((0.7,1.0,0.7,1.0),(0.75,1.0,0.75,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 points!"
                if hm ==13:
                    show hammer_line at Move((0.75,1.0,0.75,1.0),(0.8,1.0,0.8,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==14:
                    show hammer_line at Move((0.8,1.0,0.8,1.0),(0.85,1.0,0.85,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==15:
                    show hammer_line at Move((0.85,1.0,0.85,1.0),(0.9,1.0,0.9,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==16:
                    show hammer_line at Move((0.9,1.0,0.9,1.0),(0.91,1.0,0.91,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==17:
                    $ hammer_cheat = False
                    "you can't go any further right!"
                    jump hamish_clicked
                if hm ==18:
                    show hammer_line at Move((0.85,1.0,0.85,1.0),(0.9,1.0,0.9,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==19:
                    show hammer_line at Move((0.8,1.0,0.8,1.0),(0.85,1.0,0.85,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==20:
                    show hammer_line at Move((0.75,1.0,0.75,1.0),(0.8,1.0,0.8,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "1 point!"
                if hm ==21:
                    show hammer_line at Move((0.7,1.0,0.7,1.0),(0.75,1.0,0.75,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==22:
                    show hammer_line at Move((0.65,1.0,0.65,1.0),(0.7,1.0,0.7,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==23:
                    show hammer_line at Move((0.6,1.0,0.6,1.0),(0.65,1.0,0.65,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==24:
                    show hammer_line at Move((0.55,1.0,0.55,1.0),(0.6,1.0,0.6,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==25:
                    show hammer_line at Move((0.5,1.0,0.5,1.0),(0.55,1.0,0.55,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==26:
                    show hammer_line at Move((0.45,1.0,0.45,1.0),(0.5,1.0,0.5,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=3
                    "3 points!"
                if hm ==27:
                    show hammer_line at Move((0.4,1.0,0.4,1.0),(0.45,1.0,0.45,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==28:
                    show hammer_line at Move((0.35,1.0,0.35,1.0),(0.4,1.0,0.4,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=2
                    "2 points!"
                if hm ==29:
                    show hammer_line at Move((0.3,1.0,0.3,1.0),(0.35,1.0,0.35,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "2 points!"
                if hm ==30:
                    show hammer_line at Move((0.25,1.0,0.25,1.0),(0.3,1.0,0.3,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "2 points!"
                if hm ==31:
                    show hammer_line at Move((0.2,1.0,0.2,1.0),(0.25,1.0,0.25,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                if hm ==32:
                    show hammer_line at Move((0.15,1.0,0.15,1.0),(0.2,1.0,0.2,1.0),0.001)
                    $ renpy.pause(0.001)
                    $ hammer_points +=1
                    "1 point!"
                hide slutty_toph_1
                show hammer_toph_wait

            "i don't need the help!" if bk3_day:
                hide hammer_toph_hit
                show hammer_toph_wait

                if hm ==1:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==2:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==3:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==4:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==5:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==6:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==7:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==8:
                    $ hammer_points +=3
                    "3 points!"
                if hm ==9:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==10:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==11:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==12:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==13:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==14:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==15:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==16:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==17:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==18:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==19:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==20:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==21:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==22:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==23:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==24:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==25:
                    $ hammer_points +=3
                    "3 points!"
                if hm ==26:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==27:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==28:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==29:
                    $ hammer_points +=2
                    "2 points!"
                if hm ==30:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==31:
                    $ hammer_points +=1
                    "1 point!"
                if hm ==32:
                    $ hammer_points +=1
                    "1 point!"



label hammer_end:
    $ hammer_rounds +=1
    if hammer_rounds >=3:
        hide hammer_toph_wait
        hide hammer_bar
        hide hammer_line
        $ scams +=1
        hide toi toi12
        hide toi toi210
        hide toi toi22
        hide toi toi111
        if hammer_points >=9:
            if scam_distraction ==4:
                show toi toi83 with vshake
            "whoa, you got [hammer_points] total! that's amazing!"
            "you get 25 coins!"
            $ hammer_points = 0
            $ hammer_rounds = 0
            $ hammer_cheat = False
            $ emoney +=25

            jump bk3_games

        if hammer_points ==8:
            if scam_distraction ==4:
                show toi toi83 with vshake
            "great! you got [hammer_points] total!"
            "you get 20 coins!"
            $ hammer_points = 0
            $ hammer_rounds = 0
            $ hammer_cheat = False
            $ emoney +=20
            jump bk3_games
        if hammer_points >=6 and hammer_points <=7:
            if scam_distraction ==4:
                show toi toi83 with vshake
            "not bad! you got [hammer_points] total!"
            "you get 15 coins!"
            $ hammer_points = 0
            $ hammer_rounds = 0
            $ hammer_cheat = False
            $ emoney +=15
            jump bk3_games
        else:
            if scam_distraction ==4:
                show toi toi83 with vshake
            "you got [hammer_points] total. not your best."
            "you get 10 coins!"
            $ hammer_points = 0
            $ hammer_rounds = 0
            $ hammer_cheat = False
            $ emoney +=10
            jump bk3_games
    else:


        jump hammer_begin

screen hamish:
    button:
        text "{color=#ffffff}hit!" size 30
        background "#000"
        xpos .45
        ypos .45
        xysize (100, 100)
        action [Hide("hamish"),Jump("hamish_clicked")]




image earth_dice1 = ConditionSwitch(
    "rand_earth_dice1_img == '1'", "misc/x2_2.png",
    "rand_earth_dice1_img == '2'", "misc/o2_2.png",
    "rand_earth_dice1_img == '3'", "misc/x3_2.png",
    "rand_earth_dice1_img == '4'", "misc/o3_2.png",)

image earth_dice2 = ConditionSwitch(
    "rand_earth_dice2_img == '1'", "misc/x2_3.png",
    "rand_earth_dice2_img == '2'", "misc/o2_3.png",
    "rand_earth_dice2_img == '3'", "misc/x3_3.png",
    "rand_earth_dice2_img == '4'", "misc/o3_3.png",)

label earth_dice:
    scene black
    scene cup_background
    if love_jd_hypno ==10 and suki_tylee <7:
        pass
    else:
        if scam_distraction ==1:
            show toi toi12:
                xzoom -1.0
        if scam_distraction ==2:
            show toi toi210
        if scam_distraction ==3:
            show toi toi22
        if scam_distraction ==4:
            show toi toi111:
                xzoom -1.0
    $ rand_earth_dice1 = 1
    $ rand_earth_dice2 = 2
    $ rand_earth_dice1_stop = 1
    $ rand_earth_dice2_stop = 1

    if rand_earth_dice1 ==1:
        $ rand_earth_dice1_img = "1"
    if rand_earth_dice1 ==2:
        $ rand_earth_dice1_img = "2"
    if rand_earth_dice1 ==3:
        $ rand_earth_dice1_img = "3"
    if rand_earth_dice1 ==4:
        $ rand_earth_dice1_img = "4"

    if rand_earth_dice2 ==1:
        $ rand_earth_dice2_img = "1"
    if rand_earth_dice2 ==2:
        $ rand_earth_dice2_img = "2"
    if rand_earth_dice2 ==3:
        $ rand_earth_dice2_img = "3"
    if rand_earth_dice2 ==4:
        $ rand_earth_dice2_img = "4"

    image edice_ani:
        "misc/edice1.png"
        0.2
        "misc/edice2.png"
        0.2
        repeat

    show edice_ani:
        ypos 150
        xpos 500
        linear 2.0 xpos -50 ypos -60
    pause 2.0


    hide edice_ani





    show earth_dice1:
        xalign 0.35 yalign 0.2
    show earth_dice2:
        xalign 0.55 yalign 0.1
    with dissolve

    jump earth_dice_cont

label earth_dice_cont:

    if rand_earth_dice1_stop ==2 and rand_earth_dice2_stop ==2:
        jump earth_dice_check

    if rand_earth_dice1_stop ==1:
        $ rand_earth_dice1 = 2
        $ rand_earth_dice1_img = "2"
        $ rand_earth_dice1_stop = renpy.random.randint(1,2)

    if rand_earth_dice2_stop ==1:
        $ rand_earth_dice2 = 3
        $ rand_earth_dice2_img = "3"
        $ rand_earth_dice2_stop = renpy.random.randint(1,2)

    $ renpy.pause(0.25)

    if rand_earth_dice1_stop ==2 and rand_earth_dice2_stop ==2:
        jump earth_dice_check

    if rand_earth_dice1_stop ==1:
        $ rand_earth_dice1 = 3
        $ rand_earth_dice1_img = "3"
        $ rand_earth_dice1_stop = renpy.random.randint(1,2)

    if rand_earth_dice2_stop ==1:
        $ rand_earth_dice2 = 4
        $ rand_earth_dice2_img = "4"
        $ rand_earth_dice2_stop = renpy.random.randint(1,2)

    $ renpy.pause(0.25)

    if rand_earth_dice1_stop ==2 and rand_earth_dice2_stop ==2:
        jump earth_dice_check

    if rand_earth_dice1_stop ==1:
        $ rand_earth_dice1 = 4
        $ rand_earth_dice1_img = "4"
        $ rand_earth_dice1_stop = renpy.random.randint(1,2)

    if rand_earth_dice2_stop ==1:
        $ rand_earth_dice2 = 1
        $ rand_earth_dice2_img = "1"
        $ rand_earth_dice2_stop = renpy.random.randint(1,2)

    $ renpy.pause(0.25)

    if rand_earth_dice1_stop ==2 and rand_earth_dice2_stop ==2:
        jump earth_dice_check

    if rand_earth_dice1_stop ==1:
        $ rand_earth_dice1 = 1
        $ rand_earth_dice1_img = "1"
        $ rand_earth_dice1_stop = renpy.random.randint(1,2)

    if rand_earth_dice2_stop ==1:
        $ rand_earth_dice2 = 2
        $ rand_earth_dice2_img = "2"
        $ rand_earth_dice2_stop = renpy.random.randint(1,2)

    $ renpy.pause(0.25)
    jump earth_dice_cont

label earth_dice_check:

    if rand_earth_dice1 == rand_earth_dice2:
        "you win the round!"
        $ earth_dice_round_won +=1
        jump earth_dice_round_check
    else:

        if earth_dice_cheats >0:
            if love_jd_hypno ==10 and suki_tylee <7:
                pass
            else:

                show text "you have [earth_dice_cheats] cheat-rolls remaining.":
                    xpos 460 ypos 480



                call screen bk3_screen_dicescam

                label rerollleftdice:
                    "While Toph is distracting the crowd, you do some cheating!"

                    $ earth_dice_cheats -=1
                    $ rand_earth_dice1 = 0
                    $ rand_earth_dice1 = renpy.random.randint(1,4)
                    if rand_earth_dice1 ==1:
                        $ rand_earth_dice1_img = "1"
                    if rand_earth_dice1 ==2:
                        $ rand_earth_dice1_img = "2"
                    if rand_earth_dice1 ==3:
                        $ rand_earth_dice1_img = "3"
                    if rand_earth_dice1 ==4:
                        $ rand_earth_dice1_img = "4"
                    jump earth_dice_check

                label rerollrightdice:
                    "While Toph is distracting the crowd, you do some cheating!"
                    $ earth_dice_cheats -=1
                    $ rand_earth_dice2 = 0
                    $ rand_earth_dice2 = renpy.random.randint(1,4)
                    if rand_earth_dice2 ==1:
                        $ rand_earth_dice2_img = "1"
                    if rand_earth_dice2 ==2:
                        $ rand_earth_dice2_img = "2"
                    if rand_earth_dice2 ==3:
                        $ rand_earth_dice2_img = "3"
                    if rand_earth_dice2 ==4:
                        $ rand_earth_dice2_img = "4"
                    jump earth_dice_check
        else:
            "you lose the round."
            jump earth_dice_round_check

label earth_dice_round_check:
    $ earth_dice_round +=1
    if earth_dice_round >=3:
        $ scams +=1
        if earth_dice_round_won ==3:
            if scam_distraction ==4:
                show toi toi83 with vshake
            "you win the match! you get 25 coins!"
            $ emoney +=25
        if earth_dice_round_won ==2:
            if scam_distraction ==4:
                show toi toi83 with vshake
            $ emoney +=20
            "you won twice! you get 20 coins!"
        if earth_dice_round_won ==1:
            if scam_distraction ==4:
                show toi toi83 with vshake
            $ emoney +=15
            "you only won once, but you get 15 coins!"
        if earth_dice_round_won ==0:
            if scam_distraction ==4:
                show toi toi83 with vshake
            "you lost."

        $ earth_dice_round = 0
        $ earth_dice_cheats = 2
        $ earth_dice_round_won = 0
        scene black
        scene market_general
        with dissolve
        jump bk3_games
    else:

        jump earth_dice




label dicecups_start:









    if not solo_dicecups:
        show azss azss01

        show toi toi04
        with dissolve
        ss "hey! what do you two think you're doing here?"
        y "just looking around."
        ss "hmmm...."
        ss "well, you look like a gambling man."
        y "i've been known to dabble."
        ss "right, well, we're playing {b}cups{/i}."
        ss "the buy-in is 5 coins."
        ss "if you win, you get 15 coins, plus your 5 back."
        ss "if you lose, we keep your 5 coins."
        ss "so, you in?"
        y "i don't know...."
        ss "well, tell you what -- i'm a forgiving lass."
        ss "first go is on me."
        y "....alright, sure."
        ss "good...."
        ss "the rules to {b}cups{/b} are simple."
        ss "you've gotta keep your eye on the cup that's hiding the stone."
        ss "There are 3 rounds in a match."
        ss "You have to win all 3 rounds to win money."
        ss "Each round is slightly faster than the one before it."
        $ solo_dicecups = True
        ss "so, are you ready?"

        t "hold on, we need to talk."
        ss "....fine, but be quick."
        hide azss azss01 with dissolve
        y "what's up?"
        show toi toi50 with dissolve
        t "i'm gonna distract the crowd here while you play."
        y "yeah, you mentioned that..."
        y "how?"
        t "i don't know, i'll stick my tongue out at them or something."
        t "but i can also help you cheat once."
        t "any more than that and we risk having to mess with the guards."
        t "any questions?"
        y "well, yeah-"
        t "tough. you'll just have to figure it out."
        y "....you're a sassy little thing."
        show toi toi02 with dissolve
        t "hey, lady! we're ready!"
        show azss azss01 with dissolve
        ss "about time."
        ss "let's do it!"
    else:
        if not cups_toph:
            show azss azss01

            show toi toi04
            with dissolve
            ss "hey, it's you again."
            ss "alright, you know the rules already so let's begin!"

            t "hold on, we need to talk."
            ss "....fine, but be quick."
            hide azss azss01 with dissolve
            y "what's up?"
            show toi toi50
            with dissolve
            t "i'm gonna distract the crowd here while you play."
            y "yeah, you mentioned that..."
            y "how?"
            t "i don't know, i'll stick my tongue out at them or something."
            t "but i can also help you cheat once."
            t "any more than that and we risk having to mess with the guards."
            t "any questions?"
            y "well, yeah-"
            t "tough. you'll just have to figure it out."
            y "....you're a sassy little thing."
            show toi toi02 with dissolve
            t "hey, lady! we're ready!"
            show azss azss01 with dissolve
            ss "about time."
            ss "let's do it!"
        else:
            $ emoney -=5

    if scams >=2:
        hide toi toi02
        hide azss azss01
        if love_jd_hypno ==10 and suki_tylee <7:
            pass
        else:
            show toi toi02
            with dissolve
            t "how do you want me to distract the crowd?"
            menu:
                "stick your tongue out":
                    show toi toi09 with dissolve
                    t "okay..."
                    $ scam_distraction = 1

                "wear swimsuit" if market_stroll <2:
                    show toi toi09 with dissolve
                    t "i'm not doing that!"
                    t "i'll just stick my tongue out..."
                    show toi toi12
                    with dissolve
                    $ scam_distraction = 1

                "wear swimsuit" if market_stroll >=2:
                    $ toph_top_nude = False
                    $ toph_bottom_nude = False
                    show toi toi200
                    with dissolve
                    $ scam_distraction = 2

                "wear bikini" if toph_massage < 4 and not love_toph_bikini:
                    show toi toi09 with dissolve
                    t "i'm not doing that!"
                    t "i'll just stick my tongue out..."
                    show toi toi12
                    with dissolve
                    $ scam_distraction = 1

                "wear bikini (+1 public)" if toph_massage >=4 or love_toph_bikini:
                    $ toph_public +=1
                    show toi toi09 with dissolve
                    t "okay...."
                    show toi toi21 with dissolve
                    t "........"
                    show toi toi22
                    with dissolve
                    $ scam_distraction = 3

                "give handjob" if not toph_titjob:
                    show toi toi09 with dissolve
                    t "i'm not doing that!"
                    t "i'll just stick my tongue out..."
                    show toi toi12:
                        xzoom -1.0
                    with dissolve
                    $ scam_distraction = 1

                "give me a handjob (+2 public)" if toph_titjob:
                    $ toph_public +=2
                    show toi toi09 with dissolve
                    t "um... okay..."
                    t "if... you really think that's best..."
                    show toi toi111:
                        xzoom -1.0
                    with dissolve
                    t "....."
                    $ scam_distraction = 4


label dicecups_start2:

    $ dicecup_round = 1
    $ dicecup_cheat = False
    $ times_cups_shuffled = 0
    $ rand_ball = 2
    $ dc1 = 1
    $ dc2 = 2
    $ dc3 = 3






    jump dicecup_match

label dicecup_match:
    scene market_cupgame
    if cheat_unlock:
        if love_jd_hypno ==10 and suki_tylee <7:
            pass
        else:
            hide toi toi09
            if scam_distraction ==1:
                hide toi toi12
                show toi toi12
            if scam_distraction ==2:
                hide toi toi210
                show toi toi210
            if scam_distraction ==3:
                hide toi toi22
                show toi toi22
            if scam_distraction ==4:
                hide toi toi111
                show toi toi111
    $ rand_ball = renpy.random.randint(1,3)
    if rand_ball ==1:
        show red_ball at Position(xpos=0.3, xanchor=0.3, ypos=0.5, yanchor=0.5)
    if rand_ball ==2:
        show red_ball at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    if rand_ball ==3:
        show red_ball at Position(xpos=0.7, xanchor=0.7, ypos=0.5, yanchor=0.5)

    show dicecup1 at Position(xpos=0.3, xanchor=0.3, ypos=0.3, yanchor=0.3)
    show dicecup2 at Position(xpos=0.5, xanchor=0.5, ypos=0.3, yanchor=0.3)
    show dicecup3 at Position(xpos=0.7, xanchor=0.7, ypos=0.3, yanchor=0.3)
    with dissolve
    $ renpy.pause(0.5, hard=True)

    show dicecup1 at Move((0.3,0.3,0.3,0.3),(0.3,0.5,0.3,0.5),0.5)
    show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.5)
    show dicecup3 at Move((0.7,0.3,0.7,0.3),(0.7,0.5,0.7,0.5),0.5)
    $ renpy.pause(1.0)
    hide red_ball
    $ dc1 = 1
    $ dc2 = 2
    $ dc3 = 3

    jump dicecup1_shuffle

label dicecup1_shuffle:
    if dc1 == 1:
        $ dc1 = renpy.random.randint(2,5)
        if dc1 == 2:
            if dicecup_round ==1:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.35)
                jump dicecup2_shuffle
            if dicecup_round ==2:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.3)
                jump dicecup2_shuffle
            if dicecup_round ==3:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.25)
                jump dicecup2_shuffle

        if dc1 == 3:
            if dc2 == 4 or dc2 == 5 or dc3 ==4 or dc3 ==5:
                $ dc1 = 1
                jump dicecup1_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.35)
                    jump dicecup2_shuffle
                if dicecup_round ==2:
                    show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.3)
                    jump dicecup2_shuffle
                if dicecup_round ==3:
                    show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.25)
                    jump dicecup2_shuffle

        if dc1 == 4:
            if dicecup_round ==1:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.35)
                jump dicecup2_shuffle
            if dicecup_round ==2:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.3)
                jump dicecup2_shuffle
            if dicecup_round ==3:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.25)
                jump dicecup2_shuffle

        if dc1 == 5:
            if dicecup_round ==1:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.35)
                jump dicecup2_shuffle
            if dicecup_round ==2:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.3)
                jump dicecup2_shuffle
            if dicecup_round ==3:
                show dicecup1 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.25)
                jump dicecup2_shuffle

    if dc1 == 2:
        if dc2 == 4 and dc3 ==7:
            jump dicecup2_shuffle
        if dc2 ==7 and dc3 ==4:
            jump dicecup2_shuffle
        if dc2 ==5 and dc3 ==6:
            jump dicecup2_shuffle
        if dc2 ==6 and dc3 ==5:
            jump dicecup2_shuffle

        $ dc1 = renpy.random.randint(1,3)
        if dc1 == 1:
            if dc2 == 6 or dc2 == 7 or dc3 ==6 or dc3 ==7:
                $ dc1 =2
                jump dicecup1_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.35)
                    jump dicecup2_shuffle
                if dicecup_round ==2:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.3)
                    jump dicecup2_shuffle
                if dicecup_round==3:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.25)
                    jump dicecup2_shuffle
        if dc1 == 2:
            if dc2 == 6 or dc2 == 7 or dc3 ==6 or dc3 ==7:
                $ dc1 =2
                jump dicecup1_shuffle
            else:
                $ dc1 = 1
                if dicecup_round ==1:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.35)
                    jump dicecup2_shuffle
                if dicecup_round ==2:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.3)
                    jump dicecup2_shuffle
                if dicecup_round ==3:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.25)
                    jump dicecup2_shuffle
        if dc1 == 3:
            if dc2 == 4 or dc2 == 5 or dc3 ==4 or dc3 ==5:
                $ dc1 =2
                jump dicecup1_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.35)
                    jump dicecup2_shuffle
                if dicecup_round ==2:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.3)
                    jump dicecup2_shuffle
                if dicecup_round ==3:
                    show dicecup1 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.25)
                    jump dicecup2_shuffle

    if dc1 == 3:
        $ dc1 = renpy.random.randint(1,5)
        if dc1 == 1:
            if dc2 == 6 or dc2 ==7 or dc3 ==6 or dc3 ==7:
                $ dc1 = 3
                jump dicecup1_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.35)
                    jump dicecup2_shuffle
                if dicecup_round ==2:
                    show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.3)
                    jump dicecup2_shuffle
                if dicecup_round ==3:
                    show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.25)
                    jump dicecup2_shuffle
        if dc1 == 2:
            if dicecup_round ==1:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.35)
                jump dicecup2_shuffle
            if dicecup_round ==2:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.3)
                jump dicecup2_shuffle
            if dicecup_round==3:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.25)
                jump dicecup2_shuffle
        if dc1 == 3:
            $ dc1 = 2
            if dicecup_round ==1:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.35)
                jump dicecup2_shuffle
            if dicecup_round ==2:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.3)
                jump dicecup2_shuffle
            if dicecup_round ==3:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.25)
                jump dicecup2_shuffle
        if dc1 == 4:
            $ dc1 = 6
            if dicecup_round ==1:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.35)
                jump dicecup2_shuffle
            if dicecup_round ==2:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.3)
                jump dicecup2_shuffle
            if dicecup_round ==3:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.25)
                jump dicecup2_shuffle
        if dc1 == 5:
            $ dc1 = 7
            if dicecup_round ==1:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.35)
                jump dicecup2_shuffle
            if dicecup_round==2:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.3)
                jump dicecup2_shuffle
            if dicecup_round==3:
                show dicecup1 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.25)
                jump dicecup2_shuffle

    if dc1 == 4:
        $ dc1 = 3
        if dicecup_round ==1:
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            jump dicecup2_shuffle
        if dicecup_round ==2:
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.3)
            jump dicecup2_shuffle
        if dicecup_round ==3:
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.25)
            jump dicecup2_shuffle

    if dc1 == 5:
        $ dc1 = 3
        if dicecup_round ==1:
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            jump dicecup2_shuffle
        if dicecup_round ==2:
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.3)
            jump dicecup2_shuffle
        if dicecup_round ==3:
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.25)
            jump dicecup2_shuffle

    if dc1 ==6:
        $ dc1 = 1
        if dicecup_round ==1:
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)
            jump dicecup2_shuffle
        if dicecup_round ==2:
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.3)
            jump dicecup2_shuffle
        if dicecup_round ==3:
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.25)
            jump dicecup2_shuffle

    if dc1 ==7:
        $ dc1 = 1
        if dicecup_round ==1:
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)
            jump dicecup2_shuffle
        if dicecup_round ==2:
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.3)
            jump dicecup2_shuffle
        if dicecup_round ==3:
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.25)
            jump dicecup2_shuffle

label dicecup2_shuffle:
    if dc2 == 1:
        $ dc2 = renpy.random.randint(2,5)
        if dc2 == 2:
            if dc1 ==2:
                $ dc2 = 1
                jump dicecup2_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.35)
                    jump dicecup3_shuffle
                if dicecup_round ==2:
                    show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.3)
                    jump dicecup3_shuffle
                if dicecup_round ==3:
                    show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.25)
                    jump dicecup3_shuffle

        if dc2 == 3:
            if dc1 ==3:
                $ dc2 = 1
                jump dicecup2_shuffle
            else:
                if dc3 ==4 or dc3 ==5:
                    $ dc2 = 1
                    jump dicecup2_shuffle
                else:
                    if dicecup_round ==1:
                        show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.35)
                        jump dicecup3_shuffle
                    if dicecup_round ==2:
                        show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.3)
                        jump dicecup3_shuffle
                    if dicecup_round ==3:
                        show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.25)
                        jump dicecup3_shuffle
        if dc2 == 4:
            if dicecup_round ==1:
                show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.25)
                jump dicecup3_shuffle

        if dc2 == 5:
            if dicecup_round ==1:
                show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.25)
                jump dicecup3_shuffle

    if dc2 == 2:
        if dc1 ==1 and dc3 ==4:
            jump dicecup3_shuffle
        if dc1 ==3 and dc3 ==6:
            jump dicecup3_shuffle
        if dc1 ==1 and dc3 ==5:
            jump dicecup3_shuffle
        if dc1 ==3 and dc3 ==7:
            jump dicecup3_shuffle

        $ dc2 = renpy.random.randint(1,3)
        if dc2 == 1:
            if dc1 ==1:
                $ dc2 = 2
                jump dicecup2_shuffle
            else:
                if dc3 == 6 or dc3 ==7:
                    $ dc2 = 2
                    jump dicecup2_shuffle
                else:
                    if dicecup_round ==1:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.35)
                        jump dicecup3_shuffle
                    if dicecup_round ==2:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.3)
                        jump dicecup3_shuffle
                    if dicecup_round ==3:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.25)
                        jump dicecup3_shuffle
        if dc2 == 2:

            if dc1 ==1:
                $ dc2 = 2
                jump dicecup2_shuffle
            else:
                if dc3 == 6 or dc3 ==7:
                    $ dc2 = 2
                    jump dicecup2_shuffle
                else:
                    $ dc2 = 1
                    if dicecup_round ==1:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.35)
                        jump dicecup3_shuffle
                    if dicecup_round ==2:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.3)
                        jump dicecup3_shuffle
                    if dicecup_round ==3:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.25)
                        jump dicecup3_shuffle
        if dc2 == 3:

            if dc1 ==3:
                $ dc2 = 2
                jump dicecup2_shuffle
            else:
                if dc3 ==4 or dc3 ==5:
                    $ dc2 = 2
                    jump dicecup2_shuffle
                else:
                    if dicecup_round ==1:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.35)
                        jump dicecup3_shuffle
                    if dicecup_round ==2:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.3)
                        jump dicecup3_shuffle
                    if dicecup_round ==3:
                        show dicecup2 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.25)
                        jump dicecup3_shuffle

    if dc2 == 3:
        $ dc2 = renpy.random.randint(1,5)
        if dc2 == 1:

            if dc1 ==1:
                $ dc2 = 3
                jump dicecup2_shuffle
            else:
                if dc3 ==6 or dc3 ==7:
                    $ dc2 = 3
                    jump dicecup2_shuffle
                else:
                    if dicecup_round ==1:
                        show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.35)
                        jump dicecup3_shuffle
                    if dicecup_round ==2:
                        show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.3)
                        jump dicecup3_shuffle
                    if dicecup_round ==3:
                        show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.25)
                        jump dicecup3_shuffle

        if dc2 == 2:
            if dc1 == 2:
                $ dc2 = 3
                jump dicecup2_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.35)
                    jump dicecup3_shuffle
                if dicecup_round ==2:
                    show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.3)
                    jump dicecup3_shuffle
                if dicecup_round ==3:
                    show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.25)
                    jump dicecup3_shuffle

        if dc2 == 3:

            if dc1 == 2:
                $ dc2 = 3
                jump dicecup2_shuffle
            else:
                $ dc2 = 2
                if dicecup_round ==1:
                    show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.35)
                    jump dicecup3_shuffle
                if dicecup_round ==2:
                    show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.3)
                    jump dicecup3_shuffle
                if dicecup_round ==3:
                    show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.25)
                    jump dicecup3_shuffle

        if dc2 == 4:
            $ dc2 = 6
            if dicecup_round ==1:
                show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.25)
                jump dicecup3_shuffle

        if dc2 == 5:
            $ dc2 = 7
            if dicecup_round ==1:
                show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.25)
                jump dicecup3_shuffle

    if dc2 == 4:
        if dc1 ==3:
            jump dicecup3_shuffle
        else:
            $ dc2 = 3
            if dicecup_round ==1:
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.25)
                jump dicecup3_shuffle

    if dc2 == 5:
        if dc1 ==3:
            jump dicecup3_shuffle
        else:
            $ dc2 = 3
            if dicecup_round ==1:
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.25)
                jump dicecup3_shuffle

    if dc2 ==6:
        if dc1 ==1:
            jump dicecup3_shuffle
        else:
            $ dc2 = 1
            if dicecup_round ==1:
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.25)
                jump dicecup3_shuffle

    if dc2 ==7:
        if dc1 ==1:
            jump dicecup3_shuffle
        else:
            $ dc2 = 1
            if dicecup_round ==1:
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)
                jump dicecup3_shuffle
            if dicecup_round ==2:
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.3)
                jump dicecup3_shuffle
            if dicecup_round ==3:
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.25)
                jump dicecup3_shuffle

label dicecup3_shuffle:
    if dc3 == 1:
        $ dc3 = renpy.random.randint(2,5)
        if dc3 == 2:
            if dc1 ==2 or dc2 ==2:
                $ dc3 = 1
                jump dicecup3_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.5,0.5,0.5),0.25)
                    jump after_dicecup_shuffle
        if dc3 == 3:
            if dc1 ==3 or dc2 ==3:
                $ dc3 = 1
                jump dicecup3_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.7,0.5,0.7,0.5),0.35)
                    jump after_dicecup_shuffle
        if dc3 == 4:
            if dicecup_round ==1:
                show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.3,0.5,0.3),0.25)
                jump after_dicecup_shuffle

        if dc3 == 5:
            if dicecup_round ==1:
                show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.3,0.5,0.3,0.5),(0.5,0.7,0.5,0.7),0.25)
                jump after_dicecup_shuffle

    if dc3 == 2:
        if dc1 ==1 and dc2 ==3:
            jump after_dicecup_shuffle
        if dc1 ==3 and dc2 ==1:
            jump after_dicecup_shuffle

        $ dc3 = renpy.random.randint(1,3)
        if dc3 == 1:
            if dc1 ==1 or dc2 ==1:
                $ dc3 =2
                jump dicecup3_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.25)
                    jump after_dicecup_shuffle

        if dc3 == 2:

            if dc1 ==1 or dc2 ==1:
                $ dc3 =2
                jump dicecup3_shuffle
            else:
                $ dc3 = 1
                if dicecup_round ==1:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.3,0.5,0.3,0.5),0.25)
                    jump after_dicecup_shuffle
        if dc3 == 3:
            if dc1 ==3 or dc2 ==3:
                $ dc3 =2
                jump dicecup3_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.5,0.5,0.5,0.5),(0.7,0.5,0.7,0.5),0.25)
                    jump after_dicecup_shuffle

    if dc3 == 3:
        $ dc3 = renpy.random.randint(1,5)
        if dc3 == 1:
            if dc1 ==1 or dc2 ==1:
                $ dc3 =3
                jump dicecup3_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.3,0.5,0.3,0.5),0.25)
                    jump after_dicecup_shuffle

        if dc3 == 2:
            if dc1 ==2 or dc2 ==2:
                $ dc3 =3
                jump dicecup3_shuffle
            else:
                if dicecup_round ==1:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.25)
                    jump after_dicecup_shuffle

        if dc3 == 3:

            if dc1 ==2 or dc2 ==2:
                $ dc3 =3
                jump dicecup3_shuffle
            else:
                $ dc3 = 2
                if dicecup_round ==1:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.35)
                    jump after_dicecup_shuffle
                if dicecup_round ==2:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.3)
                    jump after_dicecup_shuffle
                if dicecup_round ==3:
                    show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.5,0.5,0.5),0.25)
                    jump after_dicecup_shuffle

        if dc3 == 4:
            $ dc3 = 6
            if dicecup_round ==1:
                show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.3,0.5,0.3),0.25)
                jump after_dicecup_shuffle

        if dc3 == 5:
            $ dc3 = 7
            if dicecup_round ==1:
                show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.7,0.5,0.7,0.5),(0.5,0.7,0.5,0.7),0.25)
                jump after_dicecup_shuffle

    if dc3 == 4:
        if dc1 ==1 and dc2 ==3:
            jump after_dicecup_shuffle
        if dc1 ==3 and dc2 ==1:
            jump after_dicecup_shuffle
        else:

            $ dc3 = 3
            if dicecup_round ==1:
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.25)
                jump after_dicecup_shuffle

    if dc3 == 5:
        if dc1 ==1 and dc2 ==3:
            jump after_dicecup_shuffle
        if dc1 ==3 and dc2 ==1:
            jump after_dicecup_shuffle
        else:

            $ dc3 = 3
            if dicecup_round ==1:
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.25)
                jump after_dicecup_shuffle

    if dc3 ==6:
        if dc1 ==1 and dc2 ==3:
            jump after_dicecup_shuffle
        if dc1 ==3 and dc2 ==1:
            jump after_dicecup_shuffle
        else:
            $ dc3 = 1
            if dicecup_round ==1:
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.25)
                jump after_dicecup_shuffle

    if dc3 ==7:
        if dc1 ==1 and dc2 ==3:
            jump after_dicecup_shuffle
        if dc1 ==3 and dc2 ==1:
            jump after_dicecup_shuffle
        else:
            $ dc3 = 1
            if dicecup_round ==1:
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)
                jump after_dicecup_shuffle
            if dicecup_round ==2:
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.3)
                jump after_dicecup_shuffle
            if dicecup_round ==3:
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.25)
                jump after_dicecup_shuffle

label after_dicecup_shuffle:
    $ config.rollback_enabled = False
    if dicecup_round ==1:
        $ renpy.pause(0.35, hard=True)
    if dicecup_round ==2:
        $ renpy.pause(0.3, hard=True)
    if dicecup_round ==3:
        $ renpy.pause(0.25, hard=True)

    $ times_cups_shuffled +=1
    if times_cups_shuffled >= 8:
        $ times_cups_shuffled = 0
        jump dicecup_wrapup1
    else:

        jump dicecup1_shuffle

label dicecup_wrapup1:
    if dc1 ==4:
        if dc2 ==1 or dc3 ==1:
            if dc2 ==2 or dc3 ==2:
                $ dc1 = 3
                show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc1 = 2
                show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc1 = 1
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup2

    if dc1 ==5:
        if dc2 ==1 or dc3 ==1:
            if dc2 ==2 or dc3 ==2:
                $ dc1 = 3
                show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc1 = 2
                show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc1 = 1
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup2

    if dc1 ==6:
        if dc2 ==1 or dc3 ==1:
            if dc2 ==2 or dc3 ==2:
                $ dc1 = 3
                show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc1 = 2
                show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc1 = 1
            show dicecup1 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup2

    if dc1 ==7:
        if dc2 ==1 or dc3 ==1:
            if dc2 ==2 or dc3 ==2:
                $ dc1 = 3
                show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc1 = 2
                show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc1 = 1
            show dicecup1 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup2
    else:

        jump dicecup_wrapup2

label dicecup_wrapup2:
    if dc2 ==4:
        if dc1 ==1 or dc3 ==1:
            if dc1 ==2 or dc3 ==2:
                $ dc2 = 3
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc2 = 2
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc2 = 1
            show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup3

    if dc2 ==5:
        if dc1 ==1 or dc3 ==1:
            if dc1 ==2 or dc3 ==2:
                $ dc2 = 3
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc2 = 2
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc2 = 1
            show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup3

    if dc2 ==6:
        if dc1 ==1 or dc3 ==1:
            if dc1 ==2 or dc3 ==2:
                $ dc2 = 3
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc2 = 2
                show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc2 = 1
            show dicecup2 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup3

    if dc2 ==7:
        if dc1 ==1 or dc3 ==1:
            if dc1 ==2 or dc3 ==2:
                $ dc2 = 3
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc2 = 2
                show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc2 = 1
            show dicecup2 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_wrapup3

label dicecup_wrapup3:
    if dc3 ==4:
        if dc1 ==1 or dc2 ==1:
            if dc1 ==2 or dc2 ==2:
                $ dc3 = 3
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc3 = 2
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc3 = 1
            show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_guess

    if dc3 ==5:
        if dc1 ==1 or dc2 ==1:
            if dc1 ==2 or dc2 ==2:
                $ dc3 = 3
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc3 = 2
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc3 = 1
            show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_guess

    if dc3 ==6:
        if dc1 ==1 or dc2 ==1:
            if dc1 ==2 or dc2 ==2:
                $ dc3 = 3
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc3 = 2
                show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc3 = 1
            show dicecup3 at Move((0.5,0.3,0.5,0.3),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_guess

    if dc3 ==7:
        if dc1 ==1 or dc2 ==1:
            if dc1 ==2 or dc2 ==2:
                $ dc3 = 3
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.7,0.5,0.7,0.5),0.35)
            else:
                $ dc3 = 2
                show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.5,0.5,0.5,0.5),0.35)
        else:
            $ dc3 = 1
            show dicecup3 at Move((0.5,0.7,0.5,0.7),(0.3,0.5,0.3,0.5),0.35)

        jump dicecup_guess

label dicecup_guess:
    $ dicecup_round +=1
    show text "which cup is the ball under?":
        xpos 500 ypos 260
    jump dicecup_guess_menu

label dicecup_guess_menu:





    call screen bk3_screen_cupscam


    label usetophtocheat:
        if not cheat_unlock:
            "toph isn't with you!"
            jump dicecup_guess_menu
        if love_jd_hypno ==10 and suki_tylee <7:
            "toph isn't with you!"
        else:

            "you only get to use this option once per match. use it now?"
            menu:
                "cheat" if not dicecup_cheat:
                    $ dicecup_cheat = True
                    if rand_ball ==1:
                        if dc1 ==1:
                            "toph" "the ball is under the left one!"
                        if dc1 ==2:
                            "toph" "the ball is under the middle one!"
                        if dc1 ==3:
                            "toph" "the ball is under the right one!"
                    if rand_ball ==2:
                        if dc2 ==1:
                            "toph" "the ball is under the left one!"
                        if dc2 ==2:
                            "toph" "the ball is under the middle one!"
                        if dc2 ==3:
                            "toph" "the ball is under the right one!"
                    if rand_ball ==3:
                        if dc3 ==1:
                            "toph" "the ball is under the left one!"
                        if dc3 ==2:
                            "toph" "the ball is under the middle one!"
                        if dc3 ==3:
                            "toph" "the ball is under the right one!"

                    if dicecup_round >=4:
                        jump dicecups_win
                    else:
                        "you win the round!"
                        if dicecup_round ==2:
                            "two rounds to go!"
                            jump dicecup_match
                        if dicecup_round ==3:
                            "one more round to go!"
                            jump dicecup_match
                "back":

                    jump dicecup_guess_menu

    label bk3_cupleft:
        if rand_ball ==1:
            if dc1 ==1:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match

        if rand_ball ==2:
            if dc2 ==1:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match

        if rand_ball ==3:
            if dc3 ==1:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match



    label bk3_cupmiddle:
        if rand_ball ==1:
            if dc1 ==2:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match

        if rand_ball ==2:
            if dc2 ==2:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match

        if rand_ball ==3:
            if dc3 ==2:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match



    label bk3_cupright:
        if rand_ball ==1:
            if dc1 ==3:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match

        if rand_ball ==2:
            if dc2 ==3:
                if dicecup_round >=4:
                    jump dicecups_win
                else:
                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match

        if rand_ball ==3:
            if dc3 ==3:
                if dicecup_round >=4:
                    jump dicecups_win
                else:

                    "you win the round!"
                    if dicecup_round ==2:
                        "two rounds to go!"
                        jump dicecup_match
                    if dicecup_round ==3:
                        "one more round to go!"
                        jump dicecup_match






    if not dicecup_cheat and cheat_unlock:
        $ dicecup_cheat = True
        "as you reach for the wrong cup, toph quickly moves the stone to be under the one you chose."
        "you win the round!"
        "since you haven't cheated yet in this match, no one suspects anything."
        if dicecup_round ==2:
            "two rounds to go!"
            jump dicecup_match
        if dicecup_round ==3:
            "one more round to go!"
            jump dicecup_match
    else:

        if scam_distraction ==4:
            show toi toi83 with vshake
        show azss azss01 with dissolve
        ss "no. you suck."
        y "hey...."
        scene black
        scene market_general
        with dissolve
        $ config.rollback_enabled = True
        if not solo_dicecups:
            show azss azss01 with dissolve
            ss "better luck next time."
            y "yeah, well, maybe {i}you{/i} should suck."
            ss "what?"
            y "you know. on my dangly bits."
            ss "....okay, now i'm pissed."
            ss "disappear."

            hide azss azss01 with dissolve
            jump basingse_day1
        else:

            if katara_found:
                $ cups_toph = True
                show azss azss01 with dissolve
                ss "you up for playing again?"
                menu:
                    "play again":
                        jump dicecups_start
                    "stop calling here":







                        ss ":("
                        jump bk3_market
            else:

                show azss azss01 with dissolve
                ss "later, suckers."
                hide azss azss01 with dissolve
                y "we... didn't even pay her..."
                show toi toi06 with dissolve
                t "oh, nicely done, aang."
                t "well, let's go find katara."
                y "any idea where we should look first?"
                show toi toi09 with dissolve
                t "hm..."
                y "hell, she could be lost somewhere in the market and it'd take us all day to find her."
                t "that's a good point."
                show toi toi04 with dissolve
                t "let's split up, we'll cover more ground that way."
                t "i'll stay here and search for her."
                t "you go look elsewhere."
                y "by myself? but... it's a big city..."
                t "stop whining, i'm covering the whole market."
                show toi toi06 with dissolve
                t "now get to it!"
                hide toi toi06 with dissolve
                $ cups_toph = True
                jump basingse_day1


label dicecups_win:
    $ config.rollback_enabled = True
    $ scams +=1
    if scam_distraction ==4:
        show toi toi83 with vshake
    "you win the match!"
    scene black
    scene market_general
    show azss azss01
    with dissolve
    ss "well, i'm a bitch of my word... here's your money."
    play sound "audio/win2.mp3"
    if not cheat_unlock:
        $ emoney +=15
        "you won 15 coins!"
        $ solo_dicecups = True
        ss "i think that's enough for the moment."
        ss "come back when i'm less pissed."
        jump basingse_day1
    else:
        if katara_found:
            $ minigames_won +=1
            $ emoney +=20
            $ cups_toph = True
            "you won 20 coins!"
            ss "you up for playing again?"
            menu:
                "play again":
                    jump dicecups_start
                "stop calling here":






                    ss ":("
                    jump bk3_market
        else:
            $ minigames_won +=1
            $ emoney +=15
            "you won 15 coins!"
            ss "rrgghh...."
            hide azss azss01 with dissolve
            show toi toi04 with dissolve
            t "nicely done, aang."
            t "let's go find katara."
            y "any idea where we should look first?"
            show toi toi09 with dissolve
            t "hm..."
            y "hell, she could be lost somewhere in the market and it'd take us all day to find her."
            t "that's a good point."
            show toi toi04 with dissolve
            t "let's split up, we'll cover more ground that way."
            t "i'll stay here and search for her."
            t "you go look elsewhere."
            y "by myself? but... it's a big city..."
            t "stop whining, i'm covering the whole market."
            show toi toi06 with dissolve
            t "now get to it!"
            hide toi toi06 with dissolve
            $ cups_toph = True
            jump basingse_day1








screen bk3_screen_cupscam:

    imagemap:

        ground "misc/minipixel.png"
        hover "misc/cups_hover.png"
        idle "misc/cups_idle.png"


        hotspot (255, 270, 130, 185) clicked Jump("bk3_cupleft")

        hotspot (436, 270, 130, 185) clicked Jump("bk3_cupmiddle")

        hotspot (618, 270, 130, 185) clicked Jump("bk3_cupright")

        if cheat_unlock == True and dicecup_cheat==False:
            add "misc/cups_cheat.png"
        if cheat_unlock == True and dicecup_cheat==False:
            hotspot (380, 495, 244, 96) clicked Jump("usetophtocheat")



screen bk3_screen_dicescam:

    imagemap:

        ground "misc/minipixel.png"
        hover "misc/dice_hover.png"
        idle "misc/dice_idle.png"

        if earth_dice_cheats >0:
            hotspot (280, 133, 167, 265) clicked Jump("rerollleftdice")
        if earth_dice_cheats >0:
            hotspot (451, 102, 165, 257) clicked Jump("rerollrightdice")

        hotspot (300, 514, 330, 51) clicked Jump("earth_dice_round_check")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
