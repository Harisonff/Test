image white = "#FFFFFF"
image blackjack = "bjtable.png"
image hit = "hit.png"
image stand = "stand.png"


define op = Character(None, what_text_align=0, window_left_padding = 200, window_right_margin=200, window_xalign=0.5, window_yalign=0.5, window_background= None)
define e = Character(None, what_text_align=0, what_color = "#FFFFFF", window_left_padding = 200, window_right_margin=200, window_xalign=0.5, window_yalign=0.5, window_background = None)
define lady = Character('Ty lee', color="#ffec04", window_left_padding = 150)
define lady2 = Character('ty lee', color="#ffec04", window_left_padding = 194, window_right_padding = 150)
define guy = Character('you', color="#123456", window_left_padding = 194, window_right_padding = 150)
define r0 = Character(None, what_text_align=0, what_color = "#FFFFFF", window_left_padding = 25, window_right_margin=0, window_xalign=0.5, window_yalign=0.5, window_background= None)
define r1 = Character(None, what_text_align=0, what_color = "#FFFFFF", window_left_padding = 150, window_right_margin=0, window_xalign=0.2, window_yalign=0.3, window_background= None)
define r2 = Character(None, what_text_align=0, what_color = "#FFFFFF", window_left_padding = 100, window_right_margin=0, window_xalign=1.0, window_yalign=0.7, window_background= None)
define r2a = Character(None, what_text_align=0, what_color = "#FFFFFF", window_left_padding = 300, window_right_margin=0, window_xalign=0.5, window_yalign=0.8, window_background= None)
define r3 = Character(None, what_text_align=0, what_color = "#FFFFFF", window_left_padding = 175, window_right_margin=0, window_xalign=0.5, window_yalign=0.5, window_background= None)
define d = Character(None, what_text_align=0.0, window_left_padding = 620, window_right_margin=-300, window_xalign=0.9, window_yalign=0.75, what_size = 36, window_background = None)


init python:

    config.side_image_only_not_showing = True

init:
    $ FileWins = "Story Mode"
    $ c = Character(None, kind=nvl)
    $ persistent.firstgame = True
    $ persistent.unlockedmessage = False
    $ persistent.win1 = False
    $ freeplay = False
    $ test_game = False
    $ LadyFace = "normal"
    $ GuyFace = "normal"
    $ LadyFull = "normal"
    $ LastHand = False
    $ TimesPlayed = 0
    $ DisplayPts = False
    $ D2 = "blank"
    $ D3 = "blank"
    $ D4 = "blank"
    $ D5 = "blank"
    $ P2 = "blank"
    $ P3 = "blank"
    $ P4 = "blank"
    $ P5 = "blank"
    $ bj_told = False


label bjstart:

    scene blackjack

    if bj_told:
        $ config.rollback_enabled = False
        show screen bjtable
        $ TimesPlayed = 1
        jump BlackJack
    else:

        show hit:
            xalign 0.4 yalign 0.5
        with dissolve
        show stand:
            xalign 0.55 yalign 0.5
        with dissolve
        t "the goal of blackjack is to get as close to 21 as possible without going over."
        t "face cards - jack, queen, king - are all 10 points."
        t "the ace can either be 1 point or 11 points - it's up to you."
        t "if you go over 21, you \"bust\" and the dealer wins the round."
        t "The left button is “Hit”, which means you want another card."
        t "The right button is “Stand”, which means you end your turn."
        $ bj_told = True
        hide hit with dissolve
        hide stand with dissolve
        t "I'll be the dealer!"
        y "oh, wait, yeah i've played this..."
        y "player wins if there's a tie."
        t "um... i thought..."
        y "nope, player definitely wins."
        t "oh... okay!"
        t "first to three points wins!"
        t "Let's have some fun!"
        $ config.rollback_enabled = False
        show screen bjtable
        $ TimesPlayed = 1
        jump BlackJack

label BlackJack:
    $ renpy.block_rollback()
    call CheckDeck from _call_CheckDeck_9

    d "{color=#ffffff}Begin Hand [TimesPlayed]{nw}"
    call BlackJack_Coding from _call_BlackJack_Coding
    $ renpy.pause(1.0)
    scene blackjack
    jump BlackJack

label BadEnd:
    if thief > zuko:
        if tavern_day:
            if second_tavern_visit:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i win!"
                $ fmoney -= bet_payout
                play sound "audio/money.mp3"
                "you lost [bet_payout] coins."
                $ bet_payout = 0
                hide blackjack
                jump ftavern_day2
            else:

                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i win!"
                t "but...I'll let you out of it this time!"
                hide blackjack
                $ second_tavern_visit = True
                jump ftavern_day2
        else:
            if second_tavern_visit:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i win!"
                $ fmoney -= bet_payout
                play sound "audio/money.mp3"
                "you lost [bet_payout] coins."
                $ bet_payout = 0
                hide blackjack
                jump ftavern_night2
            else:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i win!"
                t "but...I'll let you out of it this time!"
                hide blackjack
                $ second_tavern_visit = True
                jump ftavern_night2
    else:

        if fdaytime:
            scene bg_a_tavern with dissolve
            show tf with dissolve
            $ lwins = 0
            $ gwins = 0
            t "i win!"
            $ fmoney -= bet_payout
            play sound "audio/money.mp3"
            "you lost [bet_payout] coins."
            $ bet_payout = 0
            hide blackjack
            jump zftavern_day1
        else:

            scene bg_a_tavern with dissolve
            show tf with dissolve
            $ lwins = 0
            $ gwins = 0
            t "i win!"
            $ fmoney -= bet_payout
            play sound "audio/money.mp3"
            "you lost [bet_payout] coins."
            $ bet_payout = 0
            hide blackjack
            jump zftavern_night1

label GoodEnd:
    if thief > zuko:

        if tavern_day:
            if bet_payout >=100:
                scene bg_a_tavern with dissolve
                show tfa with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i..."
                t "i only have 75 coins."
                y "that's not what we agreed. how else can you pay?"
                t "...do you wanna see my tits?"
                y "..."
                t "please!"
                t "i don't have any money... and i really need what i have..."
                t "and i have great tits! look!"
                y "well, i-"
                show ty_idle_ff_tittyflash
                hide tfa
                with dissolve
                show ctcblink
                $ renpy.pause()
                hide ctcblink
                y "huh."
                y "yup, those are great."
                t "and... here's 75 coins."
                $ fmoney += 75
                play sound "audio/money.mp3"
                "you got 75 coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                hide ty_idle_ff_tittyflash
                jump ftavern_day2
            else:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "aw..."
                t "well, fair's fair."
                $ fmoney += bet_payout
                play sound "audio/money.mp3"
                "you got [bet_payout] coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                jump ftavern_day2
        else:
            if bet_payout >=100:
                scene bg_a_tavern with dissolve
                show tfa with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i..."
                t "i only have 75 coins."
                y "that's not what we agreed. how else can you pay?"
                t "...do you wanna see my tits?"
                y "..."
                t "please!"
                t "i don't have any money... and i really need what i have..."
                t "and i have great tits! look!"
                y "well, i-"
                show ty_idle_ff_tittyflash
                hide tfa
                with dissolve
                show ctcblink
                $ renpy.pause()
                hide ctcblink
                y "huh."
                y "yup, those are great."
                t "and... here's 75 coins."
                $ fmoney += 75
                play sound "audio/money.mp3"
                "you got 75 coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                hide ty_idle_ff_tittyflash
                jump ftavern_night2
            else:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "aw..."
                t "well, fair's fair."
                $ fmoney += bet_payout
                play sound "audio/money.mp3"
                "you got [bet_payout] coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                jump ftavern_night2
    else:

        if fdaytime:
            if bet_payout >=100:
                scene bg_a_tavern with dissolve
                show tfa with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i..."
                t "i only have 75 coins."
                y "that's not what we agreed. how else can you pay?"
                t "...do you wanna see my tits?"
                y "..."
                t "please!"
                t "i don't have any money... and i really need what i have..."
                t "and i have great tits! look!"
                y "well, i-"
                show ty_idle_ff_tittyflash
                hide tfa
                with dissolve
                show ctcblink
                $ renpy.pause()
                hide ctcblink
                y "huh."
                y "yup, those are great."
                t "and... here's 75 coins."
                $ fmoney += 75
                play sound "audio/money.mp3"
                "you got 75 coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                hide ty_idle_ff_tittyflash
                jump zftavern_day1
            else:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "aw..."
                t "well, fair's fair."
                $ fmoney += bet_payout
                play sound "audio/money.mp3"
                "you got [bet_payout] coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                jump zftavern_day1
        else:
            if bet_payout >=100:
                scene bg_a_tavern with dissolve
                show tfa with dissolve
                $ lwins = 0
                $ gwins = 0
                t "i..."
                t "i only have 75 coins."
                y "that's not what we agreed. how else can you pay?"
                t "...do you wanna see my tits?"
                y "..."
                t "please!"
                t "i don't have any money... and i really need what i have..."
                t "and i have great tits! look!"
                y "well, i-"
                show ty_idle_ff_tittyflash
                hide tfa
                with dissolve
                show ctcblink
                $ renpy.pause()
                hide ctcblink
                y "huh."
                y "yup, those are great."
                t "and... here's 75 coins."
                $ fmoney += 75
                play sound "audio/money.mp3"
                "you got 75 coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                hide ty_idle_ff_tittyflash
                jump zftavern_night1
            else:
                scene bg_a_tavern with dissolve
                show tf with dissolve
                $ lwins = 0
                $ gwins = 0
                t "aw..."
                t "well, fair's fair."
                $ fmoney += bet_payout
                play sound "audio/money.mp3"
                "you got [bet_payout] coins."
                $ bet_payout = 0
                t "i'll get you next time!"
                hide blackjack
                jump zftavern_night1

label end:
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
