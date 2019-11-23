label ReDrawd5:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_83
        jump DealersCard5


label DealersCard5:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawd5
            else:
                $ D5 = "As"
                $ DAce5 = True
                $ PAs = True
        else:
            $ D5 = "As"
            $ DAce5 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawd5
            else:
                $ P2s = True
                $ D5 = "2s"
                $ DHand += 2
        else:
            $ P2s = True
            $ D5 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawd5
            else:
                $ P3s = True
                $ D5 = "3s"
                $ DHand += 3
        else:
            $ P3s = True
            $ D5 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawd5
            else:
                $ P4s = True
                $ D5 = "4s"
                $ DHand += 4
        else:
            $ P4s = True
            $ D5 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawd5
            else:
                $ P5s = True
                $ D5 = "5s"
                $ DHand += 5
        else:
            $ P5s = True
            $ D5 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawd5
            else:
                $ P6s = True
                $ D5 = "6s"
                $ DHand += 6
        else:
            $ P6s = True
            $ D5 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawd5
            else:
                $ P7s = True
                $ D5 = "7s"
                $ DHand += 7
        else:
            $ P7s = True
            $ D5 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawd5
            else:
                $ P8s = True
                $ D5 = "8s"
                $ DHand += 8
        else:
            $ P8s = True
            $ D5 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawd5
            else:
                $ P9s = True
                $ D5 = "9s"
                $ DHand += 9
        else:
            $ P9s = True
            $ D5 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawd5
            else:
                $ P10s = True
                $ D5 = "10s"
                $ DHand += 10
        else:
            $ P10s = True
            $ D5 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawd5
            else:
                $ PJs = True
                $ D5 = "Js"
                $ DHand += 10
        else:
            $ PJs = True
            $ D5 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawd5
            else:
                $ PQs = True
                $ D5 = "Qs"
                $ DHand += 10
        else:
            $ PQs = True
            $ D5 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawd5
            else:
                $ PKs = True
                $ D5 = "Ks"
                $ DHand += 10
        else:
            $ PKs = True
            $ D5 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_84
                jump ReDrawd5
            else:
                $ D5 = "Ad"
                $ DAce5 = True
                $ PAd = True
        else:
            $ D5 = "Ad"
            $ DAce5 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawd5
            else:
                $ P2d = True
                $ D5 = "2d"
                $ DHand += 2
        else:
            $ P2d = True
            $ D5 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_85
                jump ReDrawd5
            else:
                $ P3d = True
                $ D5 = "3d"
                $ DHand += 3
        else:
            $ P3d = True
            $ D5 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_86
                jump ReDrawd5
            else:
                $ P4d = True
                $ D5 = "4d"
                $ DHand += 4
        else:
            $ P4d = True
            $ D5 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_87
                jump ReDrawd5
            else:
                $ P5d = True
                $ D5 = "5d"
                $ DHand += 5
        else:
            $ P5d = True
            $ D5 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_88
                jump ReDrawd5
            else:
                $ P6d = True
                $ D5 = "6d"
                $ DHand += 6
        else:
            $ P6d = True
            $ D5 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_89
                jump ReDrawd5
            else:
                $ P7d = True
                $ D5 = "7d"
                $ DHand += 7
        else:
            $ P7d = True
            $ D5 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_90
                jump ReDrawd5
            else:
                $ P8d = True
                $ D5 = "8d"
                $ DHand += 8
        else:
            $ P8d = True
            $ D5 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_91
                jump ReDrawd5
            else:
                $ P9d = True
                $ D5 = "9d"
                $ DHand += 9
        else:
            $ P9d = True
            $ D5 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_92
                jump ReDrawd5
            else:
                $ P10d = True
                $ D5 = "10d"
                $ DHand += 10
        else:
            $ P10d = True
            $ D5 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_93
                jump ReDrawd5
            else:
                $ PJd = True
                $ D5 = "Jd"
                $ DHand += 10
        else:
            $ PJd = True
            $ D5 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_94
                jump ReDrawd5
            else:
                $ PQd = True
                $ D5 = "Qd"
                $ DHand += 10
        else:
            $ PQd = True
            $ D5 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_95
                jump ReDrawd5
            else:
                $ PKd = True
                $ D5 = "Kd"
                $ DHand += 10
        else:
            $ PKd = True
            $ D5 = "Kd"
            $ DHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_96
                jump ReDrawd5
            else:
                $ D5 = "Ac"
                $ DAce5 = True
                $ PAc = True
        else:
            $ D5 = "Ac"
            $ DAce5 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_97
                jump ReDrawd5
            else:
                $ P2c = True
                $ D5 = "2c"
                $ DHand += 2
        else:
            $ P2c = True
            $ D5 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_98
                jump ReDrawd5
            else:
                $ P3c = True
                $ D5 = "3c"
                $ DHand += 3
        else:
            $ P3c = True
            $ D5 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_99
                jump ReDrawd5
            else:
                $ P4c = True
                $ D5 = "4c"
                $ DHand += 4
        else:
            $ P4c = True
            $ D5 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_100
                jump ReDrawd5
            else:
                $ P5c = True
                $ D5 = "5c"
                $ DHand += 5
        else:
            $ P5c = True
            $ D5 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_101
                jump ReDrawd5
            else:
                $ P6c = True
                $ D5 = "6c"
                $ DHand += 6
        else:
            $ P6c = True
            $ D5 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_102
                jump ReDrawd5
            else:
                $ P7c = True
                $ D5 = "7c"
                $ DHand += 7
        else:
            $ P7c = True
            $ D5 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_103
                jump ReDrawd5
            else:
                $ P8c = True
                $ D5 = "8c"
                $ DHand += 8
        else:
            $ P8c = True
            $ D5 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_104
                jump ReDrawd5
            else:
                $ P9c = True
                $ D5 = "9c"
                $ DHand += 9
        else:
            $ P9c = True
            $ D5 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_105
                jump ReDrawd5
            else:
                $ P10c = True
                $ D5 = "10c"
                $ DHand += 10
        else:
            $ P10c = True
            $ D5 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_106
                jump ReDrawd5
            else:
                $ PJc = True
                $ D5 = "Jc"
                $ DHand += 10
        else:
            $ PJc = True
            $ D5 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_107
                jump ReDrawd5
            else:
                $ PQc = True
                $ D5 = "Qc"
                $ DHand += 10
        else:
            $ PQc = True
            $ D5 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_108
                jump ReDrawd5
            else:
                $ PKc = True
                $ D5 = "Kc"
                $ DHand += 10
        else:
            $ PKc = True
            $ D5 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_109
                jump ReDrawd5
            else:
                $ D5 = "Ah"
                $ DAce5 = True
                $ PAh = True
        else:
            $ D5 = "Ah"
            $ DAce5 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_110
                jump ReDrawd5
            else:
                $ P2h = True
                $ D5 = "2h"
                $ DHand += 2
        else:
            $ P2h = True
            $ D5 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_111
                jump ReDrawd5
            else:
                $ P3h = True
                $ D5 = "3h"
                $ DHand += 3
        else:
            $ P3h = True
            $ D5 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_112
                jump ReDrawd5
            else:
                $ P4h = True
                $ D5 = "4h"
                $ DHand += 4
        else:
            $ P4h = True
            $ D5 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_113
                jump ReDrawd5
            else:
                $ P5h = True
                $ D5 = "5h"
                $ DHand += 5
        else:
            $ P5h = True
            $ D5 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_114
                jump ReDrawd5
            else:
                $ P6h = True
                $ D5 = "6h"
                $ DHand += 6
        else:
            $ P6h = True
            $ D5 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_115
                jump ReDrawd5
            else:
                $ P7h = True
                $ D5 = "7h"
                $ DHand += 7
        else:
            $ P7h = True
            $ D5 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_116
                jump ReDrawd5
            else:
                $ P8h = True
                $ D5 = "8h"
                $ DHand += 8
        else:
            $ P8h = True
            $ D5 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_117
                jump ReDrawd5
            else:
                $ P9h = True
                $ D5 = "9h"
                $ DHand += 9
        else:
            $ P9h = True
            $ D5 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_118
                jump ReDrawd5
            else:
                $ P10h = True
                $ D5 = "10h"
                $ DHand += 10
        else:
            $ P10h = True
            $ D5 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_119
                jump ReDrawd5
            else:
                $ PJh = True
                $ D5 = "Jh"
                $ DHand += 10
        else:
            $ PJh = True
            $ D5 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_120
                jump ReDrawd5
            else:
                $ PQh = True
                $ D5 = "Qh"
                $ DHand += 10
        else:
            $ PQh = True
            $ D5 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_121
                jump ReDrawd5
            else:
                $ PKh = True
                $ D5 = "Kh"
                $ DHand += 10
        else:
            $ PKh = True
            $ D5 = "Kh"
            $ FHand += 10
    else:

        jump endgame

    if freeplay == True:
        if D5 == D1 or D5 == D2 or D5 == D3 or D5 == D4:

            call AceBlock from _call_AceBlock_2
            $ FHand = 0
            jump TryAgainD5
        else:
            $ DHand += FHand
            $ FHand = 0
            $ DCards +=1
            return
    else:
        $ DCards +=1
        $ deck -= 1
        jump D5Card

label TryAgainD5:
    call CardSelect from _call_CardSelect_122
    jump DealersCard5
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
