label ReDrawd3:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_42
        jump DealersCard3


label DealersCard3:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawd3
            else:
                $ D3 = "As"
                $ DAce3 = True
                $ PAs = True
        else:
            $ D3 = "As"
            $ DAce3 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawd3
            else:
                $ P2s = True
                $ D3 = "2s"
                $ DHand += 2
        else:
            $ P2s = True
            $ D3 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawd3
            else:
                $ P3s = True
                $ D3 = "3s"
                $ DHand += 3
        else:
            $ P3s = True
            $ D3 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawd3
            else:
                $ P4s = True
                $ D3 = "4s"
                $ DHand += 4
        else:
            $ P4s = True
            $ D3 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawd3
            else:
                $ P5s = True
                $ D3 = "5s"
                $ DHand += 5
        else:
            $ P5s = True
            $ D3 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawd3
            else:
                $ P6s = True
                $ D3 = "6s"
                $ DHand += 6
        else:
            $ P6s = True
            $ D3 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawd3
            else:
                $ P7s = True
                $ D3 = "7s"
                $ DHand += 7
        else:
            $ P7s = True
            $ D3 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawd3
            else:
                $ P8s = True
                $ D3 = "8s"
                $ DHand += 8
        else:
            $ P8s = True
            $ D3 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawd3
            else:
                $ P9s = True
                $ D3 = "9s"
                $ DHand += 9
        else:
            $ P9s = True
            $ D3 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawd3
            else:
                $ P10s = True
                $ D3 = "10s"
                $ DHand += 10
        else:
            $ P10s = True
            $ D3 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawd3
            else:
                $ PJs = True
                $ D3 = "Js"
                $ DHand += 10
        else:
            $ PJs = True
            $ D3 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawd3
            else:
                $ PQs = True
                $ D3 = "Qs"
                $ DHand += 10
        else:
            $ PQs = True
            $ D3 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawd3
            else:
                $ PKs = True
                $ D3 = "Ks"
                $ DHand += 10
        else:
            $ PKs = True
            $ D3 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_43
                jump ReDrawd3
            else:
                $ D3 = "Ad"
                $ DAce3 = True
                $ PAd = True
        else:
            $ D3 = "Ad"
            $ DAce3 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawd3
            else:
                $ P2d = True
                $ D3 = "2d"
                $ DHand += 2
        else:
            $ P2d = True
            $ D3 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_44
                jump ReDrawd3
            else:
                $ P3d = True
                $ D3 = "3d"
                $ DHand += 3
        else:
            $ P3d = True
            $ D3 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_45
                jump ReDrawd3
            else:
                $ P4d = True
                $ D3 = "4d"
                $ DHand += 4
        else:
            $ P4d = True
            $ D3 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_46
                jump ReDrawd3
            else:
                $ P5d = True
                $ D3 = "5d"
                $ DHand += 5
        else:
            $ P5d = True
            $ D3 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_47
                jump ReDrawd3
            else:
                $ P6d = True
                $ D3 = "6d"
                $ DHand += 6
        else:
            $ P6d = True
            $ D3 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_48
                jump ReDrawd3
            else:
                $ P7d = True
                $ D3 = "7d"
                $ DHand += 7
        else:
            $ P7d = True
            $ D3 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_49
                jump ReDrawd3
            else:
                $ P8d = True
                $ D3 = "8d"
                $ DHand += 8
        else:
            $ P8d = True
            $ D3 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_50
                jump ReDrawd3
            else:
                $ P9d = True
                $ D3 = "9d"
                $ DHand += 9
        else:
            $ P9d = True
            $ D3 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_51
                jump ReDrawd3
            else:
                $ P10d = True
                $ D3 = "10d"
                $ DHand += 10
        else:
            $ P10d = True
            $ D3 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_52
                jump ReDrawd3
            else:
                $ PJd = True
                $ D3 = "Jd"
                $ DHand += 10
        else:
            $ PJd = True
            $ D3 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_53
                jump ReDrawd3
            else:
                $ PQd = True
                $ D3 = "Qd"
                $ DHand += 10
        else:
            $ PQd = True
            $ D3 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_54
                jump ReDrawd3
            else:
                $ PKd = True
                $ D3 = "Kd"
                $ DHand += 10
        else:
            $ PKd = True
            $ D3 = "Kd"
            $ DHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_55
                jump ReDrawd3
            else:
                $ D3 = "Ac"
                $ DAce3 = True
                $ PAc = True
        else:
            $ D3 = "Ac"
            $ DAce3 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_56
                jump ReDrawd3
            else:
                $ P2c = True
                $ D3 = "2c"
                $ DHand += 2
        else:
            $ P2c = True
            $ D3 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_57
                jump ReDrawd3
            else:
                $ P3c = True
                $ D3 = "3c"
                $ DHand += 3
        else:
            $ P3c = True
            $ D3 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_58
                jump ReDrawd3
            else:
                $ P4c = True
                $ D3 = "4c"
                $ DHand += 4
        else:
            $ P4c = True
            $ D3 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_59
                jump ReDrawd3
            else:
                $ P5c = True
                $ D3 = "5c"
                $ DHand += 5
        else:
            $ P5c = True
            $ D3 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_60
                jump ReDrawd3
            else:
                $ P6c = True
                $ D3 = "6c"
                $ DHand += 6
        else:
            $ P6c = True
            $ D3 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_61
                jump ReDrawd3
            else:
                $ P7c = True
                $ D3 = "7c"
                $ DHand += 7
        else:
            $ P7c = True
            $ D3 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_62
                jump ReDrawd3
            else:
                $ P8c = True
                $ D3 = "8c"
                $ DHand += 8
        else:
            $ P8c = True
            $ D3 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_63
                jump ReDrawd3
            else:
                $ P9c = True
                $ D3 = "9c"
                $ DHand += 9
        else:
            $ P9c = True
            $ D3 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_64
                jump ReDrawd3
            else:
                $ P10c = True
                $ D3 = "10c"
                $ DHand += 10
        else:
            $ P10c = True
            $ D3 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_65
                jump ReDrawd3
            else:
                $ PJc = True
                $ D3 = "Jc"
                $ DHand += 10
        else:
            $ PJc = True
            $ D3 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_66
                jump ReDrawd3
            else:
                $ PQc = True
                $ D3 = "Qc"
                $ DHand += 10
        else:
            $ PQc = True
            $ D3 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_67
                jump ReDrawd3
            else:
                $ PKc = True
                $ D3 = "Kc"
                $ DHand += 10
        else:
            $ PKc = True
            $ D3 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_68
                jump ReDrawd3
            else:
                $ D3 = "Ah"
                $ DAce3 = True
                $ PAh = True
        else:
            $ D3 = "Ah"
            $ DAce3 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_69
                jump ReDrawd3
            else:
                $ P2h = True
                $ D3 = "2h"
                $ DHand += 2
        else:
            $ P2h = True
            $ D3 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_70
                jump ReDrawd3
            else:
                $ P3h = True
                $ D3 = "3h"
                $ DHand += 3
        else:
            $ P3h = True
            $ D3 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_71
                jump ReDrawd3
            else:
                $ P4h = True
                $ D3 = "4h"
                $ DHand += 4
        else:
            $ P4h = True
            $ D3 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_72
                jump ReDrawd3
            else:
                $ P5h = True
                $ D3 = "5h"
                $ DHand += 5
        else:
            $ P5h = True
            $ D3 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_73
                jump ReDrawd3
            else:
                $ P6h = True
                $ D3 = "6h"
                $ DHand += 6
        else:
            $ P6h = True
            $ D3 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_74
                jump ReDrawd3
            else:
                $ P7h = True
                $ D3 = "7h"
                $ DHand += 7
        else:
            $ P7h = True
            $ D3 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_75
                jump ReDrawd3
            else:
                $ P8h = True
                $ D3 = "8h"
                $ DHand += 8
        else:
            $ P8h = True
            $ D3 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_76
                jump ReDrawd3
            else:
                $ P9h = True
                $ D3 = "9h"
                $ DHand += 9
        else:
            $ P9h = True
            $ D3 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_77
                jump ReDrawd3
            else:
                $ P10h = True
                $ D3 = "10h"
                $ DHand += 10
        else:
            $ P10h = True
            $ D3 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_78
                jump ReDrawd3
            else:
                $ PJh = True
                $ D3 = "Jh"
                $ DHand += 10
        else:
            $ PJh = True
            $ D3 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_79
                jump ReDrawd3
            else:
                $ PQh = True
                $ D3 = "Qh"
                $ DHand += 10
        else:
            $ PQh = True
            $ D3 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_80
                jump ReDrawd3
            else:
                $ PKh = True
                $ D3 = "Kh"
                $ DHand += 10
        else:
            $ PKh = True
            $ D3 = "Kh"
            $ FHand += 10
    else:

        jump endgame

    if freeplay == True:
        if D3 == D2 or D3 == D1:

            call AceBlock from _call_AceBlock_1
            $ FHand = 0
            jump TryAgainD3
        else:
            $ DHand += FHand
            $ FHand = 0
            $ DCards +=1
            return
    else:
        $ DCards +=1
        $ deck -= 1
        jump D3Card

label TryAgainD3:
    call CardSelect from _call_CardSelect_81
    jump DealersCard3
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
