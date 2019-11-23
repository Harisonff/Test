label AceCheck:

    $ renpy.block_rollback()
    if HoldAce == True:
        $ HoldAce = False
    if Ace == True:
        if PHand == 10:
            $ PHand = 21
            d "{color=#ffffff}Blackjack!"
            $ TimesPlayed += 1
            jump win
        else:
            $ AceVal = int(PHand + 11)
            if AceVal > 21:
                menu:
                    d "{color=#ffffff}Your ace is low."
                    "Continue":
                        $ PHand +=1
                        $ Ace = False
            else:
                menu:
                    d "{color=#ffffff}High or Low Ace?"
                    "Low":
                        $ PHand +=1
                        $ Ace = False
                    "High":
                        $ PHand +=11
                        $ Ace = False
    if Ace2 == True:
        if PHand == 10:
            d "{color=#ffffff}Blackjack!"
            $ TimesPlayed += 1
            jump win
        else:
            $ AceVal = int(PHand + 11)
            if AceVal > 21:
                menu:
                    d "{color=#ffffff}Your ace is low."
                    "Continue":
                        $ PHand +=1
                        $ Ace2 = False
            else:
                menu:
                    d "{color=#ffffff}High or Low Ace?"
                    "Low":
                        $ PHand +=1
                        $ Ace2 = False
                    "High":
                        $ PHand +=11
                        $ Ace2 = False

    if Ace3 == True:
        $ AceVal = int(PHand + 11)
        if AceVal == 21:
            d "{color=#ffffff}BlackJack"
            $ TimesPlayed += 1
            jump win
        elif AceVal > 21:
            menu:
                d "{color=#ffffff}Your ace is low."
                "Continue":
                    $ PHand +=1
                    $ Ace3 = False
        else:
            menu:
                d "{color=#ffffff}High or Low Ace?"
                "Low":
                    $ PHand +=1
                    $ Ace3 = False
                "High":
                    $ PHand +=11
                    $ Ace3 = False

    if Ace4 == True:
        $ AceVal = int(PHand + 11)
        if AceVal == 21:
            d "{color=#ffffff}BlackJack"
            $ TimesPlayed += 1
            jump win
        elif AceVal > 21:
            menu:
                d "{color=#ffffff}Your ace is low."
                "Continue":
                    $ PHand +=1
                    $ Ace4 = False
        else:
            menu:
                d "{color=#ffffff}High or Low Ace?"
                "Low":
                    $ PHand +=1
                    $ Ace4 = False
                "High":
                    $ PHand +=11
                    $ Ace4 = False

    if Ace5 == True:
        $ AceVal = int(PHand + 11)
        if AceVal == 21:
            d "{color=#ffffff}BlackJack"
            $ TimesPlayed += 1
            jump win
        elif AceVal > 21:
            menu:
                d "{color=#ffffff}Your ace is low."
                "Continue":
                    $ PHand +=1
                    $ Ace5 = False
        else:
            menu:
                d "{color=#ffffff}High or Low Ace?"
                "Low":
                    $ PHand +=1
                    $ Ace5 = False
                "High":
                    $ PHand +=11
                    $ Ace5 = False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
