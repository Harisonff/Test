label ReDrawp5:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_163
        jump PlayersCard5


label PlayersCard5:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawp5
            else:
                $ P5 = "As"
                $ Ace5 = True
                $ PAs = True
        else:
            $ P5 = "As"
            $ Ace5 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawp5
            else:
                $ P2s = True
                $ P5 = "2s"
                $ PHand += 2
        else:
            $ P2s = True
            $ P5 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawp5
            else:
                $ P3s = True
                $ P5 = "3s"
                $ PHand += 3
        else:
            $ P3s = True
            $ P5 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawp5
            else:
                $ P5s = True
                $ P5 = "4s"
                $ PHand += 4
        else:
            $ P5s = True
            $ P5 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawp5
            else:
                $ P5s = True
                $ P5 = "5s"
                $ PHand += 5
        else:
            $ P5s = True
            $ P5 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawp5
            else:
                $ P6s = True
                $ P5 = "6s"
                $ PHand += 6
        else:
            $ P6s = True
            $ P5 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawp5
            else:
                $ P7s = True
                $ P5 = "7s"
                $ PHand += 7
        else:
            $ P7s = True
            $ P5 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawp5
            else:
                $ P8s = True
                $ P5 = "8s"
                $ PHand += 8
        else:
            $ P8s = True
            $ P5 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawp5
            else:
                $ P9s = True
                $ P5 = "9s"
                $ PHand += 9
        else:
            $ P9s = True
            $ P5 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawp5
            else:
                $ P10s = True
                $ P5 = "10s"
                $ PHand += 10
        else:
            $ P10s = True
            $ P5 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawp5
            else:
                $ PJs = True
                $ P5 = "Js"
                $ PHand += 10
        else:
            $ PJs = True
            $ P5 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawp5
            else:
                $ PQs = True
                $ P5 = "Qs"
                $ PHand += 10
        else:
            $ PQs = True
            $ P5 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawp5
            else:
                $ PKs = True
                $ P5 = "Ks"
                $ PHand += 10
        else:
            $ PKs = True
            $ P5 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_164
                jump ReDrawp5
            else:
                $ P5 = "Ad"
                $ Ace5 = True
                $ PAd = True
        else:
            $ P5 = "Ad"
            $ Ace5 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawp5
            else:
                $ P2d = True
                $ P5 = "2d"
                $ PHand += 2
        else:
            $ P2d = True
            $ P5 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_165
                jump ReDrawp5
            else:
                $ P3d = True
                $ P5 = "3d"
                $ PHand += 3
        else:
            $ P3d = True
            $ P5 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_166
                jump ReDrawp5
            else:
                $ P5d = True
                $ P5 = "4d"
                $ PHand += 4
        else:
            $ P5d = True
            $ P5 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_167
                jump ReDrawp5
            else:
                $ P5d = True
                $ P5 = "5d"
                $ PHand += 5
        else:
            $ P5d = True
            $ P5 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_168
                jump ReDrawp5
            else:
                $ P6d = True
                $ P5 = "6d"
                $ PHand += 6
        else:
            $ P6d = True
            $ P5 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_169
                jump ReDrawp5
            else:
                $ P7d = True
                $ P5 = "7d"
                $ PHand += 7
        else:
            $ P7d = True
            $ P5 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_170
                jump ReDrawp5
            else:
                $ P8d = True
                $ P5 = "8d"
                $ PHand += 8
        else:
            $ P8d = True
            $ P5 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_171
                jump ReDrawp5
            else:
                $ P9d = True
                $ P5 = "9d"
                $ PHand += 9
        else:
            $ P9d = True
            $ P5 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_172
                jump ReDrawp5
            else:
                $ P10d = True
                $ P5 = "10d"
                $ PHand += 10
        else:
            $ P10d = True
            $ P5 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_173
                jump ReDrawp5
            else:
                $ PJd = True
                $ P5 = "Jd"
                $ PHand += 10
        else:
            $ PJd = True
            $ P5 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_174
                jump ReDrawp5
            else:
                $ PQd = True
                $ P5 = "Qd"
                $ PHand += 10
        else:
            $ PQd = True
            $ P5 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_175
                jump ReDrawp5
            else:
                $ PKd = True
                $ P5 = "Kd"
                $ PHand += 10
        else:
            $ PKd = True
            $ P5 = "Kd"
            $ FHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_176
                jump ReDrawp5
            else:
                $ P5 = "Ac"
                $ Ace5 = True
                $ PAc = True
        else:
            $ P5 = "Ac"
            $ Ace5 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_177
                jump ReDrawp5
            else:
                $ P2c = True
                $ P5 = "2c"
                $ PHand += 2
        else:
            $ P2c = True
            $ P5 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_178
                jump ReDrawp5
            else:
                $ P3c = True
                $ P5 = "3c"
                $ PHand += 3
        else:
            $ P3c = True
            $ P5 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_179
                jump ReDrawp5
            else:
                $ P5c = True
                $ P5 = "4c"
                $ PHand += 4
        else:
            $ P5c = True
            $ P5 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_180
                jump ReDrawp5
            else:
                $ P5c = True
                $ P5 = "5c"
                $ PHand += 5
        else:
            $ P5c = True
            $ P5 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_181
                jump ReDrawp5
            else:
                $ P6c = True
                $ P5 = "6c"
                $ PHand += 6
        else:
            $ P6c = True
            $ P5 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_182
                jump ReDrawp5
            else:
                $ P7c = True
                $ P5 = "7c"
                $ PHand += 7
        else:
            $ P7c = True
            $ P5 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_183
                jump ReDrawp5
            else:
                $ P8c = True
                $ P5 = "8c"
                $ PHand += 8
        else:
            $ P8c = True
            $ P5 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_184
                jump ReDrawp5
            else:
                $ P9c = True
                $ P5 = "9c"
                $ PHand += 9
        else:
            $ P9c = True
            $ P5 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_185
                jump ReDrawp5
            else:
                $ P10c = True
                $ P5 = "10c"
                $ PHand += 10
        else:
            $ P10c = True
            $ P5 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_186
                jump ReDrawp5
            else:
                $ PJc = True
                $ P5 = "Jc"
                $ PHand += 10
        else:
            $ PJc = True
            $ P5 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_187
                jump ReDrawp5
            else:
                $ PQc = True
                $ P5 = "Qc"
                $ PHand += 10
        else:
            $ PQc = True
            $ P5 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_188
                jump ReDrawp5
            else:
                $ PKc = True
                $ P5 = "Kc"
                $ PHand += 10
        else:
            $ PKc = True
            $ P5 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_189
                jump ReDrawp5
            else:
                $ P5 = "Ah"
                $ Ace5 = True
                $ PAh = True
        else:
            $ P5 = "Ah"
            $ Ace5 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_190
                jump ReDrawp5
            else:
                $ P2h = True
                $ P5 = "2h"
                $ PHand += 2
        else:
            $ P2h = True
            $ P5 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_191
                jump ReDrawp5
            else:
                $ P3h = True
                $ P5 = "3h"
                $ PHand += 3
        else:
            $ P3h = True
            $ P5 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_192
                jump ReDrawp5
            else:
                $ P5h = True
                $ P5 = "4h"
                $ PHand += 4
        else:
            $ P5h = True
            $ P5 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_193
                jump ReDrawp5
            else:
                $ P5h = True
                $ P5 = "5h"
                $ PHand += 5
        else:
            $ P5h = True
            $ P5 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_194
                jump ReDrawp5
            else:
                $ P6h = True
                $ P5 = "6h"
                $ PHand += 6
        else:
            $ P6h = True
            $ P5 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_195
                jump ReDrawp5
            else:
                $ P7h = True
                $ P5 = "7h"
                $ PHand += 7
        else:
            $ P7h = True
            $ P5 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_196
                jump ReDrawp5
            else:
                $ P8h = True
                $ P5 = "8h"
                $ PHand += 8
        else:
            $ P8h = True
            $ P5 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_197
                jump ReDrawp5
            else:
                $ P9h = True
                $ P5 = "9h"
                $ PHand += 9
        else:
            $ P9h = True
            $ P5 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_198
                jump ReDrawp5
            else:
                $ P10h = True
                $ P5 = "10h"
                $ PHand += 10
        else:
            $ P10h = True
            $ P5 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_199
                jump ReDrawp5
            else:
                $ PJh = True
                $ P5 = "Jh"
                $ PHand += 10
        else:
            $ PJh = True
            $ P5 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_200
                jump ReDrawp5
            else:
                $ PQh = True
                $ P5 = "Qh"
                $ PHand += 10
        else:
            $ PQh = True
            $ P5 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_201
                jump ReDrawp5
            else:
                $ PKh = True
                $ P5 = "Kh"
                $ PHand += 10
        else:
            $ PKh = True
            $ P5 = "Kh"
            $ FHand += 10
    else:

        jump endgame

    if freeplay == True:
        if P5 == P1 or P5 == P2 or P5 == P3 or P5 == P4:

            call AceBlock from _call_AceBlock_4
            $ FHand = 0
            jump TryAgainP5
        else:
            $ PHand += FHand
            $ FHand = 0
            $ PCards +=1
            return
    else:
        $ deck -=1
        $ PCards +=1
        return

label TryAgainP5:
    call CardSelect from _call_CardSelect_202
    jump PlayersCard5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
