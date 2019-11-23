label DAceCheck:
    $ renpy.block_rollback()
    if HoldAce == True:
        $ HoldAce = False
    if DAce == True:
        if DHand == 10:
            $ DHand =21
            d "{color=#ffffff}Dealer Blackjack!"
            jump lose
        else:
            $ AceVal = int(DHand + 11)
            if AceVal < 21:

                $ DTest = int(DHand + 11)
                if DTest == 21:
                    d "{color=#ffffff}Dealer Blackjack!"
                    jump lose
                    $ DAce = False
                elif DTest > 21:
                    d "{color=#ffffff}Dealer Bust!"
                    jump win
                    $ DAce = False
                elif DTest >= 11 and DTest > 21:
                    "{color=#ffffff}Now I add 1."
                    $ DHand +=1
                    $ DAce = False
                elif DTest <= 10 and DTest < 21:
                    $ DHand +=11
                    $ DAce = False

    if DAce2 == True:
        if DHand == 10:
            d "{color=#ffffff}Dealer Blackjack!"
            jump lose
        else:
            $ AceVal = int(DHand + 11)
            if AceVal < 21:

                $ DTest = int(DHand + 11)
                if DTest == 21:
                    d "{color=#ffffff}Dealer Blackjack!"
                    jump lose
                    $ DAce2 = False
                elif DTest > 21:
                    d "{color=#ffffff}Dealer Bust!"
                    jump win
                    $ DAce2 = False
                elif DTest >= 11 and DTest > 21:
                    "{color=#ffffff}Now I add 1."
                    $ DHand +=1
                    $ DAce2 = False
                elif DTest <= 10 and DTest < 21:
                    $ DHand +=11
                    $ DAce2 = False

    if DAce3 == True:
        if DHand == 10:
            d "{color=#ffffff}Dealer Blackjack!"
            jump lose
        else:
            $ AceVal = int(DHand + 11)
            if AceVal < 21:

                $ DTest = int(DHand + 11)
                if DTest == 21:
                    d "{color=#ffffff}Dealer Blackjack!"
                    jump lose
                    $ DAce3 = False
                elif DTest > 21:
                    d "{color=#ffffff}Dealer Bust!"
                    jump win
                    $ DAce3 = False
                elif DTest >= 11 and DTest > 21:
                    "{color=#ffffff}Now I add 1."
                    $ DHand +=1
                    $ DAce3 = False
                elif DTest <= 10 and DTest < 21:
                    $ DHand +=11
                    $ DAce3 = False

    if DAce4 == True:
        if DHand == 10:
            d "{color=#ffffff}Dealer Blackjack!"
            jump lose
        else:
            $ AceVal = int(DHand + 11)
            if AceVal < 21:

                $ DTest = int(DHand + 11)
                if DTest == 21:
                    d "{color=#ffffff}Dealer Blackjack!"
                    jump lose
                    $ DAce4 = False
                elif DTest > 21:
                    d "{color=#ffffff}Dealer Bust!"
                    jump win
                    $ DAce4 = False
                elif DTest >= 11 and DTest > 21:
                    "{color=#ffffff}Now I add 1."
                    $ DHand +=1
                    $ DAce4 = False
                elif DTest <= 10 and DTest < 21:
                    $ DHand +=11
                    $ DAce4 = False

    if DAce5 == True:
        if DHand == 10:
            d "{color=#ffffff}Dealer Blackjack!"
            jump lose
        else:
            $ AceVal = int(DHand + 11)
            if AceVal < 21:

                $ DTest = int(DHand + 11)
                if DTest == 21:
                    d "{color=#ffffff}Dealer Blackjack!"
                    jump lose
                    $ DAce5 = False
                elif DTest > 21:
                    d "{color=#ffffff}Dealer Bust!"
                    jump win
                    $ DAce5 = False
                elif DTest >= 11 and DTest > 21:
                    "{color=#ffffff}Now I add 1."
                    $ DHand +=1
                    $ DAce5 = False
                elif DTest <= 10 and DTest < 21:
                    $ DHand +=11
                    $ DAce5 = False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
