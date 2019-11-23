label PlayerPlay:
    $ renpy.block_rollback()
    hide screen pturn
    call CheckDeck from _call_CheckDeck_10
    play sound "Hit.ogg"
    call PlayersCard3 from _call_PlayersCard3
    play sound "card.ogg"
    show card3:
        xalign 0.4 yalign 0.6
    $ renpy.pause(1.0)
    call AceCheck from _call_AceCheck_2
    jump PCheck

label P4Card:
    $ renpy.block_rollback()
    play sound "Hit.ogg"
    hide screen pturn
    call CheckDeck from _call_CheckDeck_11
    call PlayersCard4 from _call_PlayersCard4
    play sound "card.ogg"
    show card4:
        xalign 0.5 yalign 0.6
    jump PCheck

label P5Card:
    $ renpy.block_rollback()
    $ NoMoreCards = True
    d "Last Card"
    play sound "Hit.ogg"
    hide screen pturn
    call CheckDeck from _call_CheckDeck_12
    call PlayersCard5 from _call_PlayersCard5
    play sound "card.ogg"
    show card5:
        xalign 0.6 yalign 0.6
    call AceCheck from _call_AceCheck_3
    jump PCheck

label PCheck:
    $ renpy.block_rollback()
    call AceCheck from _call_AceCheck_4
    if NoMoreCards == False:
        if PHand == 21:
            d "{color=#ffffff}Blackjack!"
            $ TimesPlayed += 1
            jump win
        elif PHand > 21:
            d "{color=#ffffff}Bust!"
            $ TimesPlayed += 1
            jump lose
        else:
            call screen pturn
    else:
        if PHand == 21:
            d "{color=#ffffff}Blackjack!"
            $ TimesPlayed += 1
            jump win
        elif PHand > 21:
            d "{color=#ffffff}Bust!"
            $ TimesPlayed += 1
            jump lose
        else:
            $ NoMoreCards = False
            jump DealersPlay
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
