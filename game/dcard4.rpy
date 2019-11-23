label ReDrawd4:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_243
        jump DealersCard4


label DealersCard4:
    $ renpy.block_rollback()
    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawd4
            else:
                $ D4 = "As"
                $ DAce4 = True
                $ PAs = True
        else:
            $ D4 = "As"
            $ DAce4 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawd4
            else:
                $ P2s = True
                $ D4 = "2s"
                $ DHand += 2
        else:
            $ P2s = True
            $ D4 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawd4
            else:
                $ P3s = True
                $ D4 = "3s"
                $ DHand += 3
        else:
            $ P3s = True
            $ D4 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawd4
            else:
                $ P4s = True
                $ D4 = "4s"
                $ DHand += 4
        else:
            $ P4s = True
            $ D4 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawd4
            else:
                $ P5s = True
                $ D4 = "5s"
                $ DHand += 5
        else:
            $ P5s = True
            $ D4 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawd4
            else:
                $ P6s = True
                $ D4 = "6s"
                $ DHand += 6
        else:
            $ P6s = True
            $ D4 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawd4
            else:
                $ P7s = True
                $ D4 = "7s"
                $ DHand += 7
        else:
            $ P7s = True
            $ D4 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawd4
            else:
                $ P8s = True
                $ D4 = "8s"
                $ DHand += 8
        else:
            $ P8s = True
            $ D4 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawd4
            else:
                $ P9s = True
                $ D4 = "9s"
                $ DHand += 9
        else:
            $ P9s = True
            $ D4 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawd4
            else:
                $ P10s = True
                $ D4 = "10s"
                $ DHand += 10
        else:
            $ P10s = True
            $ D4 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawd4
            else:
                $ PJs = True
                $ D4 = "Js"
                $ DHand += 10
        else:
            $ PJs = True
            $ D4 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawd4
            else:
                $ PQs = True
                $ D4 = "Qs"
                $ DHand += 10
        else:
            $ PQs = True
            $ D4 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawd4
            else:
                $ PKs = True
                $ D4 = "Ks"
                $ DHand += 10
        else:
            $ PKs = True
            $ D4 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_244
                jump ReDrawd4
            else:
                $ D4 = "Ad"
                $ DAce4 = True
                $ PAd = True
        else:
            $ D4 = "Ad"
            $ DAce4 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawd4
            else:
                $ P2d = True
                $ D4 = "2d"
                $ DHand += 2
        else:
            $ P2d = True
            $ D4 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_245
                jump ReDrawd4
            else:
                $ P3d = True
                $ D4 = "3d"
                $ DHand += 3
        else:
            $ P3d = True
            $ D4 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_246
                jump ReDrawd4
            else:
                $ P4d = True
                $ D4 = "4d"
                $ DHand += 4
        else:
            $ P4d = True
            $ D4 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_247
                jump ReDrawd4
            else:
                $ P5d = True
                $ D4 = "5d"
                $ DHand += 5
        else:
            $ P5d = True
            $ D4 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_248
                jump ReDrawd4
            else:
                $ P6d = True
                $ D4 = "6d"
                $ DHand += 6
        else:
            $ P6d = True
            $ D4 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_249
                jump ReDrawd4
            else:
                $ P7d = True
                $ D4 = "7d"
                $ DHand += 7
        else:
            $ P7d = True
            $ D4 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_250
                jump ReDrawd4
            else:
                $ P8d = True
                $ D4 = "8d"
                $ DHand += 8
        else:
            $ P8d = True
            $ D4 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_251
                jump ReDrawd4
            else:
                $ P9d = True
                $ D4 = "9d"
                $ DHand += 9
        else:
            $ P9d = True
            $ D4 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_252
                jump ReDrawd4
            else:
                $ P10d = True
                $ D4 = "10d"
                $ DHand += 10
        else:
            $ P10d = True
            $ D4 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_253
                jump ReDrawd4
            else:
                $ PJd = True
                $ D4 = "Jd"
                $ DHand += 10
        else:
            $ PJd = True
            $ D4 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_254
                jump ReDrawd4
            else:
                $ PQd = True
                $ D4 = "Qd"
                $ DHand += 10
        else:
            $ PQd = True
            $ D4 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_255
                jump ReDrawd4
            else:
                $ PKd = True
                $ D4 = "Kd"
                $ DHand += 10
        else:
            $ PKd = True
            $ D4 = "Kd"
            $ DHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_256
                jump ReDrawd4
            else:
                $ D4 = "Ac"
                $ DAce4 = True
                $ PAc = True
        else:
            $ D4 = "Ac"
            $ DAce4 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_257
                jump ReDrawd4
            else:
                $ P2c = True
                $ D4 = "2c"
                $ DHand += 2
        else:
            $ P2c = True
            $ D4 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_258
                jump ReDrawd4
            else:
                $ P3c = True
                $ D4 = "3c"
                $ DHand += 3
        else:
            $ P3c = True
            $ D4 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_259
                jump ReDrawd4
            else:
                $ P4c = True
                $ D4 = "4c"
                $ DHand += 4
        else:
            $ P4c = True
            $ D4 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_260
                jump ReDrawd4
            else:
                $ P5c = True
                $ D4 = "5c"
                $ DHand += 5
        else:
            $ P5c = True
            $ D4 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_261
                jump ReDrawd4
            else:
                $ P6c = True
                $ D4 = "6c"
                $ DHand += 6
        else:
            $ P6c = True
            $ D4 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_262
                jump ReDrawd4
            else:
                $ P7c = True
                $ D4 = "7c"
                $ DHand += 7
        else:
            $ P7c = True
            $ D4 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_263
                jump ReDrawd4
            else:
                $ P8c = True
                $ D4 = "8c"
                $ DHand += 8
        else:
            $ P8c = True
            $ D4 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_264
                jump ReDrawd4
            else:
                $ P9c = True
                $ D4 = "9c"
                $ DHand += 9
        else:
            $ P9c = True
            $ D4 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_265
                jump ReDrawd4
            else:
                $ P10c = True
                $ D4 = "10c"
                $ DHand += 10
        else:
            $ P10c = True
            $ D4 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_266
                jump ReDrawd4
            else:
                $ PJc = True
                $ D4 = "Jc"
                $ DHand += 10
        else:
            $ PJc = True
            $ D4 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_267
                jump ReDrawd4
            else:
                $ PQc = True
                $ D4 = "Qc"
                $ DHand += 10
        else:
            $ PQc = True
            $ D4 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_268
                jump ReDrawd4
            else:
                $ PKc = True
                $ D4 = "Kc"
                $ DHand += 10
        else:
            $ PKc = True
            $ D4 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_269
                jump ReDrawd4
            else:
                $ D4 = "Ah"
                $ DAce4 = True
                $ PAh = True
        else:
            $ D4 = "Ah"
            $ DAce4 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_270
                jump ReDrawd4
            else:
                $ P2h = True
                $ D4 = "2h"
                $ DHand += 2
        else:
            $ P2h = True
            $ D4 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_271
                jump ReDrawd4
            else:
                $ P3h = True
                $ D4 = "3h"
                $ DHand += 3
        else:
            $ P3h = True
            $ D4 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_272
                jump ReDrawd4
            else:
                $ P4h = True
                $ D4 = "4h"
                $ DHand += 4
        else:
            $ P4h = True
            $ D4 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_273
                jump ReDrawd4
            else:
                $ P5h = True
                $ D4 = "5h"
                $ DHand += 5
        else:
            $ P5h = True
            $ D4 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_274
                jump ReDrawd4
            else:
                $ P6h = True
                $ D4 = "6h"
                $ DHand += 6
        else:
            $ P6h = True
            $ D4 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_275
                jump ReDrawd4
            else:
                $ P7h = True
                $ D4 = "7h"
                $ DHand += 7
        else:
            $ P7h = True
            $ D4 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_276
                jump ReDrawd4
            else:
                $ P8h = True
                $ D4 = "8h"
                $ DHand += 8
        else:
            $ P8h = True
            $ D4 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_277
                jump ReDrawd4
            else:
                $ P9h = True
                $ D4 = "9h"
                $ DHand += 9
        else:
            $ P9h = True
            $ D4 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_278
                jump ReDrawd4
            else:
                $ P10h = True
                $ D4 = "10h"
                $ DHand += 10
        else:
            $ P10h = True
            $ D4 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_279
                jump ReDrawd4
            else:
                $ PJh = True
                $ D4 = "Jh"
                $ DHand += 10
        else:
            $ PJh = True
            $ D4 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_280
                jump ReDrawd4
            else:
                $ PQh = True
                $ D4 = "Qh"
                $ DHand += 10
        else:
            $ PQh = True
            $ D4 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_281
                jump ReDrawd4
            else:
                $ PKh = True
                $ D4 = "Kh"
                $ DHand += 10
        else:
            $ PKh = True
            $ D4 = "Kh"
            $ FHand += 10
    else:

        jump endgame
    if freeplay == True:

        if D4 == D2 or D4 == D1 or D4 == D3:

            call AceBlock from _call_AceBlock_6
            $ FHand = 0
            jump TryAgainD4
        else:
            $ DHand += FHand
            $ FHand = 0
            $ DCards +=1
            return
    else:
        $ DCards +=1
        $ deck -= 1
        jump D4Card

label TryAgainD4:
    call CardSelect from _call_CardSelect_282
    jump DealersCard4
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
