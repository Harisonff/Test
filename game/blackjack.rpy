init:
    $ lwins = 0
    $ gwins = 0
    $ split = False
    $ CardSelector = 0
    $ SuitSelector = 0
    $ P1Card = 0
    $ P2Card = 0
    $ PHand = 0
    $ DHand = 0
    $ FHand = 0
    $ PCards = 0
    $ DCards = 0
    $ Ace = False
    $ Ace2 = False
    $ Ace3 = False
    $ Ace4 = False
    $ Ace5 = False
    $ AceVal = 0
    $ DTest = 0
    $ DAce2 = False
    $ DAce = False
    $ DAce3 = False
    $ DAce4 = False
    $ DAce5 = False
    $ deck = 52
    $ HoldAce = False
    $ NoMoreCards = False
    $ Warn4 = False

screen bjtable:
    use quick_menu
    window background None:
        frame xalign 1.0 yalign 0.1 background None:
            has vbox
            text "{color=#ffffff}[lwins] pts."
        frame xalign 0.35 yalign 0.9 background None:
            has vbox
            text "{color=#ffffff}[gwins] pts."
        frame xalign 1.5 yalign 0.0 background None:
            add "ll-face.png"

        frame xalign 0.21 yalign 0.51 background None:
            if thief > zuko:
                add "thief_face1"
            if zuko > thief:
                add "zuko/zuko_sidebox/zuko_sidebox_neutral.png"

            if DisplayPts == True:
                if PHand >=1 or DHand >=1:
                    frame xalign 0.2 yalign 0.06 background None:
                        text "{color=#ffffff}dealer: [DHand]"
                    frame xalign 0.2 yalign 0.45 background None:
                        text "{color=#ffffff}player: [PHand]"
            if freeplay == True:
                frame xalign 0.5 yalign 0.2 background None:
                    text "{color=#ffffff}Hand [TimesPlayed]"
            if test_game == True:
                frame xalign 0.5 yalign 0.0 background None:
                    has vbox
                    text "{color=#ffffff}[TimesPlayed]"
                    text "{color=#ffffff}[deck]"
                    text "{color=#ffffff}[CardSelector] card"
                    text "{color=#ffffff}[SuitSelector] suit"


screen pturn:
    modal True
    zorder 10
    window background None:
        has frame xalign 0.85 yalign 1.0 background None
        hbox:
            if split == True:
                add "split.png"
            if PCards == 3:
                imagebutton:
                    idle "hit.png"
                    hover "hit_hover.png"
                    action Jump("P4Card")
            elif PCards == 4:
                imagebutton:
                    idle "hit.png"
                    hover "hit_hover.png"
                    action Jump("P5Card")
            elif PCards >= 4:
                imagebutton:
                    idle "hit.png"
                    hover "hit_hover.png"
                    action Jump("P5Card")
            else:
                imagebutton:
                    idle "hit.png"
                    hover "hit_hover.png"
                    action Jump("PlayerPlay")
            imagebutton:
                idle "stand.png"
                hover "stand_hover.png"
                action Jump("DealersPlay")

label BlackJack_Coding:
    $ renpy.block_rollback()
    call CheckDeck from _call_CheckDeck

    call CardSelect from _call_CardSelect_40
    call PlayersCard1 from _call_PlayersCard1
    play sound "card.ogg"
    show card1:
        xalign 0.2 yalign 0.6

    call CheckDeck from _call_CheckDeck_1
    $ renpy.pause(1.0)
    $ DCards +=1
    $ deck -= 1
    show dcardb:
        xalign 0.2 yalign 0.2
    play sound "card.ogg"
    $ renpy.pause(1.0)

    call CheckDeck from _call_CheckDeck_2
    call PlayersCard2 from _call_PlayersCard2
    play sound "card.ogg"
    show card2:
        xalign 0.3 yalign 0.6
    $ renpy.pause(1.0)
    $ DisplayPts = True

    call CheckDeck from _call_CheckDeck_3
    call DealersCard2 from _call_DealersCard2
    if P2 == D2:

        call CardSelect from _call_CardSelect_41
        call DealersCard2 from _call_DealersCard2_1
    play sound "card.ogg"
    show dcard2:
        xalign 0.3 yalign 0.2

    call CheckDeck from _call_CheckDeck_4
    call AceCheck from _call_AceCheck
    show screen pturn
return

label CheckDeck:
    $ renpy.block_rollback()
    if lwins >=3 or gwins >=3:
        jump endgame

    elif deck == 0:
        if PCards >=1 or DCards >=1:
            d "No More Cards!"
            jump endgame
        else:
            jump endgame
    elif deck <= 0:
        jump endgame
    else:
        return
return









label results:
    $ renpy.block_rollback()
    $ TimesPlayed += 1
    if DHand > PHand:
        jump lose
    else:
        jump win
return


label win:
    $ renpy.block_rollback()
    $ gwins +=1
    d "{color=#ffffff}Player Wins"
    scene blackjack
    call HandReset from _call_HandReset
    jump BlackJack

label lose:
    $ renpy.block_rollback()
    $ lwins +=1
    d "{color=#ffffff}House Wins."
    scene blackjack
    call HandReset from _call_HandReset_1
    jump BlackJack

label endgame:
    $ renpy.block_rollback()
    $ DisplayPts = False
    hide screen bjtable
    with dissolve
    hide screen pturn
    with dissolve
    scene white with fade
    stop music fadeout 1.5
    call CardReset from _call_CardReset
    if lwins >= gwins:
        jump BadEnd
    else:
        jump GoodEnd
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
