label ReDrawp4:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect
        jump PlayersCard4


label PlayersCard4:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawp4
            else:
                $ P4 = "As"
                $ Ace4 = True
                $ PAs = True
        else:
            $ P4 = "As"
            $ Ace4 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawp4
            else:
                $ P2s = True
                $ P4 = "2s"
                $ PHand += 2
        else:
            $ P2s = True
            $ P4 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawp4
            else:
                $ P3s = True
                $ P4 = "3s"
                $ PHand += 3
        else:
            $ P3s = True
            $ P4 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawp4
            else:
                $ P4s = True
                $ P4 = "4s"
                $ PHand += 4
        else:
            $ P4s = True
            $ P4 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawp4
            else:
                $ P5s = True
                $ P4 = "5s"
                $ PHand += 5
        else:
            $ P5s = True
            $ P4 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawp4
            else:
                $ P6s = True
                $ P4 = "6s"
                $ PHand += 6
        else:
            $ P6s = True
            $ P4 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawp4
            else:
                $ P7s = True
                $ P4 = "7s"
                $ PHand += 7
        else:
            $ P7s = True
            $ P4 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawp4
            else:
                $ P8s = True
                $ P4 = "8s"
                $ PHand += 8
        else:
            $ P8s = True
            $ P4 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawp4
            else:
                $ P9s = True
                $ P4 = "9s"
                $ PHand += 9
        else:
            $ P9s = True
            $ P4 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawp4
            else:
                $ P10s = True
                $ P4 = "10s"
                $ PHand += 10
        else:
            $ P10s = True
            $ P4 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawp4
            else:
                $ PJs = True
                $ P4 = "Js"
                $ PHand += 10
        else:
            $ PJs = True
            $ P4 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawp4
            else:
                $ PQs = True
                $ P4 = "Qs"
                $ PHand += 10
        else:
            $ PQs = True
            $ P4 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawp4
            else:
                $ PKs = True
                $ P4 = "Ks"
                $ PHand += 10
        else:
            $ PKs = True
            $ P4 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_1
                jump ReDrawp4
            else:
                $ P4 = "Ad"
                $ Ace4 = True
                $ PAd = True
        else:
            $ P4 = "Ad"
            $ Ace4 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawp4
            else:
                $ P2d = True
                $ P4 = "2d"
                $ PHand += 2
        else:
            $ P2d = True
            $ P4 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_2
                jump ReDrawp4
            else:
                $ P3d = True
                $ P4 = "3d"
                $ PHand += 3
        else:
            $ P3d = True
            $ P4 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_3
                jump ReDrawp4
            else:
                $ P4d = True
                $ P4 = "4d"
                $ PHand += 4
        else:
            $ P4d = True
            $ P4 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_4
                jump ReDrawp4
            else:
                $ P5d = True
                $ P4 = "5d"
                $ PHand += 5
        else:
            $ P5d = True
            $ P4 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_5
                jump ReDrawp4
            else:
                $ P6d = True
                $ P4 = "6d"
                $ PHand += 6
        else:
            $ P6d = True
            $ P4 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_6
                jump ReDrawp4
            else:
                $ P7d = True
                $ P4 = "7d"
                $ PHand += 7
        else:
            $ P7d = True
            $ P4 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_7
                jump ReDrawp4
            else:
                $ P8d = True
                $ P4 = "8d"
                $ PHand += 8
        else:
            $ P8d = True
            $ P4 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_8
                jump ReDrawp4
            else:
                $ P9d = True
                $ P4 = "9d"
                $ PHand += 9
        else:
            $ P9d = True
            $ P4 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_9
                jump ReDrawp4
            else:
                $ P10d = True
                $ P4 = "10d"
                $ PHand += 10
        else:
            $ P10d = True
            $ P4 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_10
                jump ReDrawp4
            else:
                $ PJd = True
                $ P4 = "Jd"
                $ PHand += 10
        else:
            $ PJd = True
            $ P4 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_11
                jump ReDrawp4
            else:
                $ PQd = True
                $ P4 = "Qd"
                $ PHand += 10
        else:
            $ PQd = True
            $ P4 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_12
                jump ReDrawp4
            else:
                $ PKd = True
                $ P4 = "Kd"
                $ PHand += 10
        else:
            $ PKd = True
            $ P4 = "Kd"
            $ FHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_13
                jump ReDrawp4
            else:
                $ P4 = "Ac"
                $ Ace4 = True
                $ PAc = True
        else:
            $ P4 = "Ac"
            $ Ace4 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_14
                jump ReDrawp4
            else:
                $ P2c = True
                $ P4 = "2c"
                $ PHand += 2
        else:
            $ P2c = True
            $ P4 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_15
                jump ReDrawp4
            else:
                $ P3c = True
                $ P4 = "3c"
                $ PHand += 3
        else:
            $ P3c = True
            $ P4 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_16
                jump ReDrawp4
            else:
                $ P4c = True
                $ P4 = "4c"
                $ PHand += 4
        else:
            $ P4c = True
            $ P4 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_17
                jump ReDrawp4
            else:
                $ P5c = True
                $ P4 = "5c"
                $ PHand += 5
        else:
            $ P5c = True
            $ P4 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_18
                jump ReDrawp4
            else:
                $ P6c = True
                $ P4 = "6c"
                $ PHand += 6
        else:
            $ P6c = True
            $ P4 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_19
                jump ReDrawp4
            else:
                $ P7c = True
                $ P4 = "7c"
                $ PHand += 7
        else:
            $ P7c = True
            $ P4 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_20
                jump ReDrawp4
            else:
                $ P8c = True
                $ P4 = "8c"
                $ PHand += 8
        else:
            $ P8c = True
            $ P4 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_21
                jump ReDrawp4
            else:
                $ P9c = True
                $ P4 = "9c"
                $ PHand += 9
        else:
            $ P9c = True
            $ P4 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_22
                jump ReDrawp4
            else:
                $ P10c = True
                $ P4 = "10c"
                $ PHand += 10
        else:
            $ P10c = True
            $ P4 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_23
                jump ReDrawp4
            else:
                $ PJc = True
                $ P4 = "Jc"
                $ PHand += 10
        else:
            $ PJc = True
            $ P4 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_24
                jump ReDrawp4
            else:
                $ PQc = True
                $ P4 = "Qc"
                $ PHand += 10
        else:
            $ PQc = True
            $ P4 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_25
                jump ReDrawp4
            else:
                $ PKc = True
                $ P4 = "Kc"
                $ PHand += 10
        else:
            $ PKc = True
            $ P4 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_26
                jump ReDrawp4
            else:
                $ P4 = "Ah"
                $ Ace4 = True
                $ PAh = True
        else:
            $ P4 = "Ah"
            $ Ace4 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_27
                jump ReDrawp4
            else:
                $ P2h = True
                $ P4 = "2h"
                $ PHand += 2
        else:
            $ P2h = True
            $ P4 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_28
                jump ReDrawp4
            else:
                $ P3h = True
                $ P4 = "3h"
                $ PHand += 3
        else:
            $ P3h = True
            $ P4 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_29
                jump ReDrawp4
            else:
                $ P4h = True
                $ P4 = "4h"
                $ PHand += 4
        else:
            $ P4h = True
            $ P4 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_30
                jump ReDrawp4
            else:
                $ P5h = True
                $ P4 = "5h"
                $ PHand += 5
        else:
            $ P5h = True
            $ P4 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_31
                jump ReDrawp4
            else:
                $ P6h = True
                $ P4 = "6h"
                $ PHand += 6
        else:
            $ P6h = True
            $ P4 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_32
                jump ReDrawp4
            else:
                $ P7h = True
                $ P4 = "7h"
                $ PHand += 7
        else:
            $ P7h = True
            $ P4 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_33
                jump ReDrawp4
            else:
                $ P8h = True
                $ P4 = "8h"
                $ PHand += 8
        else:
            $ P8h = True
            $ P4 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_34
                jump ReDrawp4
            else:
                $ P9h = True
                $ P4 = "9h"
                $ PHand += 9
        else:
            $ P9h = True
            $ P4 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_35
                jump ReDrawp4
            else:
                $ P10h = True
                $ P4 = "10h"
                $ PHand += 10
        else:
            $ P10h = True
            $ P4 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_36
                jump ReDrawp4
            else:
                $ PJh = True
                $ P4 = "Jh"
                $ PHand += 10
        else:
            $ PJh = True
            $ P4 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_37
                jump ReDrawp4
            else:
                $ PQh = True
                $ P4 = "Qh"
                $ PHand += 10
        else:
            $ PQh = True
            $ P4 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_38
                jump ReDrawp4
            else:
                $ PKh = True
                $ P4 = "Kh"
                $ PHand += 10
        else:
            $ PKh = True
            $ P4 = "Kh"
            $ FHand += 10
    else:

        jump endgame

    if freeplay == True:
        if P4 == P1 or P4 == P2 or P4 == P3:

            call AceBlock from _call_AceBlock
            $ FHand = 0
            jump TryAgainP4
        else:
            $ PHand += FHand
            $ FHand = 0
            $ PCards +=1
            return
    else:
        $ deck -=1
        $ PCards +=1
        return

label TryAgainP4:
    call CardSelect from _call_CardSelect_39
    jump PlayersCard4
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
