label ReDrawd1:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_123
        jump DealersCard1


label DealersCard1:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawd1
            else:
                $ D1 = "As"
                $ DAce2 = True
                $ PAs = True
        else:
            $ D1 = "As"
            $ DAce2 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawd1
            else:
                $ P2s = True
                $ D1 = "2s"
                $ DHand += 2
        else:
            $ P2s = True
            $ D1 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawd1
            else:
                $ P3s = True
                $ D1 = "3s"
                $ DHand += 3
        else:
            $ P3s = True
            $ D1 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawd1
            else:
                $ P4s = True
                $ D1 = "4s"
                $ DHand += 4
        else:
            $ P4s = True
            $ D1 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawd1
            else:
                $ P5s = True
                $ D1 = "5s"
                $ DHand += 5
        else:
            $ P5s = True
            $ D1 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawd1
            else:
                $ P6s = True
                $ D1 = "6s"
                $ DHand += 6
        else:
            $ P6s = True
            $ D1 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawd1
            else:
                $ P7s = True
                $ D1 = "7s"
                $ DHand += 7
        else:
            $ P7s = True
            $ D1 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawd1
            else:
                $ P8s = True
                $ D1 = "8s"
                $ DHand += 8
        else:
            $ P8s = True
            $ D1 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawd1
            else:
                $ P9s = True
                $ D1 = "9s"
                $ DHand += 9
        else:
            $ P9s = True
            $ D1 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawd1
            else:
                $ P10s = True
                $ D1 = "10s"
                $ DHand += 10
        else:
            $ P10s = True
            $ D1 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawd1
            else:
                $ PJs = True
                $ D1 = "Js"
                $ DHand += 10
        else:
            $ PJs = True
            $ D1 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawd1
            else:
                $ PQs = True
                $ D1 = "Qs"
                $ DHand += 10
        else:
            $ PQs = True
            $ D1 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawd1
            else:
                $ PKs = True
                $ D1 = "Ks"
                $ DHand += 10
        else:
            $ PKs = True
            $ D1 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_124
                jump ReDrawd1
            else:
                $ D1 = "Ad"
                $ DAce2 = True
                $ PAd = True
        else:
            $ D1 = "Ad"
            $ DAce2 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawd1
            else:
                $ P2d = True
                $ D1 = "2d"
                $ DHand += 2
        else:
            $ P2d = True
            $ D1 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_125
                jump ReDrawd1
            else:
                $ P3d = True
                $ D1 = "3d"
                $ DHand += 3
        else:
            $ P3d = True
            $ D1 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_126
                jump ReDrawd1
            else:
                $ P4d = True
                $ D1 = "4d"
                $ DHand += 4
        else:
            $ P4d = True
            $ D1 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_127
                jump ReDrawd1
            else:
                $ P5d = True
                $ D1 = "5d"
                $ DHand += 5
        else:
            $ P5d = True
            $ D1 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_128
                jump ReDrawd1
            else:
                $ P6d = True
                $ D1 = "6d"
                $ DHand += 6
        else:
            $ P6d = True
            $ D1 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_129
                jump ReDrawd1
            else:
                $ P7d = True
                $ D1 = "7d"
                $ DHand += 7
        else:
            $ P7d = True
            $ D1 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_130
                jump ReDrawd1
            else:
                $ P8d = True
                $ D1 = "8d"
                $ DHand += 8
        else:
            $ P8d = True
            $ D1 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_131
                jump ReDrawd1
            else:
                $ P9d = True
                $ D1 = "9d"
                $ DHand += 9
        else:
            $ P9d = True
            $ D1 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_132
                jump ReDrawd1
            else:
                $ P10d = True
                $ D1 = "10d"
                $ DHand += 10
        else:
            $ P10d = True
            $ D1 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_133
                jump ReDrawd1
            else:
                $ PJd = True
                $ D1 = "Jd"
                $ DHand += 10
        else:
            $ PJd = True
            $ D1 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_134
                jump ReDrawd1
            else:
                $ PQd = True
                $ D1 = "Qd"
                $ DHand += 10
        else:
            $ PQd = True
            $ D1 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_135
                jump ReDrawd1
            else:
                $ PKd = True
                $ D1 = "Kd"
                $ DHand += 10
        else:
            $ PKd = True
            $ D1 = "Kd"
            $ DHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_136
                jump ReDrawd1
            else:
                $ D1 = "Ac"
                $ DAce2 = True
                $ PAc = True
        else:
            $ D1 = "Ac"
            $ DAce2 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_137
                jump ReDrawd1
            else:
                $ P2c = True
                $ D1 = "2c"
                $ DHand += 2
        else:
            $ P2c = True
            $ D1 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_138
                jump ReDrawd1
            else:
                $ P3c = True
                $ D1 = "3c"
                $ DHand += 3
        else:
            $ P3c = True
            $ D1 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_139
                jump ReDrawd1
            else:
                $ P4c = True
                $ D1 = "4c"
                $ DHand += 4
        else:
            $ P4c = True
            $ D1 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_140
                jump ReDrawd1
            else:
                $ P5c = True
                $ D1 = "5c"
                $ DHand += 5
        else:
            $ P5c = True
            $ D1 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_141
                jump ReDrawd1
            else:
                $ P6c = True
                $ D1 = "6c"
                $ DHand += 6
        else:
            $ P6c = True
            $ D1 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_142
                jump ReDrawd1
            else:
                $ P7c = True
                $ D1 = "7c"
                $ DHand += 7
        else:
            $ P7c = True
            $ D1 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_143
                jump ReDrawd1
            else:
                $ P8c = True
                $ D1 = "8c"
                $ DHand += 8
        else:
            $ P8c = True
            $ D1 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_144
                jump ReDrawd1
            else:
                $ P9c = True
                $ D1 = "9c"
                $ DHand += 9
        else:
            $ P9c = True
            $ D1 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_145
                jump ReDrawd1
            else:
                $ P10c = True
                $ D1 = "10c"
                $ DHand += 10
        else:
            $ P10c = True
            $ D1 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_146
                jump ReDrawd1
            else:
                $ PJc = True
                $ D1 = "Jc"
                $ DHand += 10
        else:
            $ PJc = True
            $ D1 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_147
                jump ReDrawd1
            else:
                $ PQc = True
                $ D1 = "Qc"
                $ DHand += 10
        else:
            $ PQc = True
            $ D1 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_148
                jump ReDrawd1
            else:
                $ PKc = True
                $ D1 = "Kc"
                $ DHand += 10
        else:
            $ PKc = True
            $ D1 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_149
                jump ReDrawd1
            else:
                $ D1 = "Ah"
                $ DAce2 = True
                $ PAh = True
        else:
            $ D1 = "Ah"
            $ DAce2 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_150
                jump ReDrawd1
            else:
                $ P2h = True
                $ D1 = "2h"
                $ DHand += 2
        else:
            $ P2h = True
            $ D1 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_151
                jump ReDrawd1
            else:
                $ P3h = True
                $ D1 = "3h"
                $ DHand += 3
        else:
            $ P3h = True
            $ D1 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_152
                jump ReDrawd1
            else:
                $ P4h = True
                $ D1 = "4h"
                $ DHand += 4
        else:
            $ P4h = True
            $ D1 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_153
                jump ReDrawd1
            else:
                $ P5h = True
                $ D1 = "5h"
                $ DHand += 5
        else:
            $ P5h = True
            $ D1 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_154
                jump ReDrawd1
            else:
                $ P6h = True
                $ D1 = "6h"
                $ DHand += 6
        else:
            $ P6h = True
            $ D1 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_155
                jump ReDrawd1
            else:
                $ P7h = True
                $ D1 = "7h"
                $ DHand += 7
        else:
            $ P7h = True
            $ D1 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_156
                jump ReDrawd1
            else:
                $ P8h = True
                $ D1 = "8h"
                $ DHand += 8
        else:
            $ P8h = True
            $ D1 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_157
                jump ReDrawd1
            else:
                $ P9h = True
                $ D1 = "9h"
                $ DHand += 9
        else:
            $ P9h = True
            $ D1 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_158
                jump ReDrawd1
            else:
                $ P10h = True
                $ D1 = "10h"
                $ DHand += 10
        else:
            $ P10h = True
            $ D1 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_159
                jump ReDrawd1
            else:
                $ PJh = True
                $ D1 = "Jh"
                $ DHand += 10
        else:
            $ PJh = True
            $ D1 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_160
                jump ReDrawd1
            else:
                $ PQh = True
                $ D1 = "Qh"
                $ DHand += 10
        else:
            $ PQh = True
            $ D1 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_161
                jump ReDrawd1
            else:
                $ PKh = True
                $ D1 = "Kh"
                $ DHand += 10
        else:
            $ PKh = True
            $ D1 = "Kh"
            $ FHand += 10
    else:

        jump endgame
    if freeplay == True:
        if D1 == D2 or D1 == P1 or D1 == P3 or D1 == P4 or D1 == P5:

            call AceBlock from _call_AceBlock_3
            $ FHand = 0
            jump TryAgainD1
        else:
            $ DHand += FHand
            $ FHand = 0
            $ DCards +=1
            return
    else:
        $ DCards +=1
        return

label TryAgainD1:
    call CardSelect from _call_CardSelect_162
    jump DealersCard1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
