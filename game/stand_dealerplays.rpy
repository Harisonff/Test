label DealersPlay:
    $ renpy.block_rollback()
    hide screen pturn
    call CheckDeck from _call_CheckDeck_5
    d "{color=#ffffff}ty lee's Turn"
    call CardSelect from _call_CardSelect_82
    call DealersCard1 from _call_DealersCard1
    play sound "card.ogg"
    show dcard1:
        xalign 0.2 yalign 0.2
    hide dcardb
    $ renpy.pause(1.0)
    call DAceCheck from _call_DAceCheck
    call DCheck from _call_DCheck

label D3Card:
    $ renpy.block_rollback()
    play sound "Hit.ogg"
    show dcard3:
        xalign 0.4 yalign 0.2
    $ renpy.pause(0.5)
    jump DCheck

label D4Card:
    $ renpy.block_rollback()
    play sound "Hit.ogg"
    show dcard4:
        xalign 0.5 yalign 0.2
    $ renpy.pause(0.5)
    jump DCheck

label D5Card:
    $ renpy.block_rollback()
    play sound "Hit.ogg"
    show dcard5:
        xalign 0.6 yalign 0.2
    $ renpy.pause(0.5)
    jump DCheck

label DCheck:
    $ renpy.block_rollback()
    if freeplay == False:
        pass
    if NoMoreCards == False:
        if DHand == 21:
            d "{color=#ffffff}ty lee Blackjack!"
            $ TimesPlayed += 1
            jump lose
        elif DHand > 21:
            d "{color=#ffffff}ty lee Bust!"
            $ TimesPlayed += 1
            jump win
        elif DHand >= 17:
            if PHand >= DHand:

                jump Dto17
            elif PHand < DHand:
                d "{color=#ffffff}ty lee Stands."
                jump results
        elif DHand <= 16:

            jump Dto17
        else:
            jump Dto17
    else:
        if DHand == 21:
            d "{color=#ffffff}ty lee Blackjack!"
            $ TimesPlayed += 1
            jump lose
        elif DHand > 21:
            d "{color=#ffffff}ty lee Bust!"
            $ TimesPlayed += 1
            jump win
        else:
            d "{color=#ffffff}Dealer Stands!"
            jump results
return

label Dto17:
    $ renpy.block_rollback()
    if DCards == 3:
        call CheckDeck from _call_CheckDeck_6
        jump DealersCard3
    elif DCards == 4:
        call CheckDeck from _call_CheckDeck_7
        jump DealersCard4
    elif DCards == 5:
        call CheckDeck from _call_CheckDeck_8
        $ NoMoreCards = True
        jump DealersCard5
    else:
        pass
    jump DCheck
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
