label ReDrawp2:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_283
        jump PlayersCard2


label PlayersCard2:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawp2
            else:
                $ P2 = "As"
                $ Ace2 = True
                $ PAs = True
        else:
            $ P2 = "As"
            $ Ace2 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawp2
            else:
                $ P2s = True
                $ P2 = "2s"
                $ PHand += 2
        else:
            $ P2s = True
            $ P2 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawp2
            else:
                $ P3s = True
                $ P2 = "3s"
                $ PHand += 3
        else:
            $ P3s = True
            $ P2 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawp2
            else:
                $ P4s = True
                $ P2 = "4s"
                $ PHand += 4
        else:
            $ P4s = True
            $ P2 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawp2
            else:
                $ P5s = True
                $ P2 = "5s"
                $ PHand += 5
        else:
            $ P5s = True
            $ P2 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawp2
            else:
                $ P6s = True
                $ P2 = "6s"
                $ PHand += 6
        else:
            $ P6s = True
            $ P2 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawp2
            else:
                $ P7s = True
                $ P2 = "7s"
                $ PHand += 7
        else:
            $ P7s = True
            $ P2 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawp2
            else:
                $ P8s = True
                $ P2 = "8s"
                $ PHand += 8
        else:
            $ P8s = True
            $ P2 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawp2
            else:
                $ P9s = True
                $ P2 = "9s"
                $ PHand += 9
        else:
            $ P9s = True
            $ P2 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawp2
            else:
                $ P10s = True
                $ P2 = "10s"
                $ PHand += 10
        else:
            $ P10s = True
            $ P2 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawp2
            else:
                $ PJs = True
                $ P2 = "Js"
                $ PHand += 10
        else:
            $ PJs = True
            $ P2 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawp2
            else:
                $ PQs = True
                $ P2 = "Qs"
                $ PHand += 10
        else:
            $ PQs = True
            $ P2 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawp2
            else:
                $ PKs = True
                $ P2 = "Ks"
                $ PHand += 10
        else:
            $ PKs = True
            $ P2 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_284
                jump ReDrawp2
            else:
                $ P2 = "Ad"
                $ Ace2 = True
                $ PAd = True
        else:
            $ P2 = "Ad"
            $ Ace2 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawp2
            else:
                $ P2d = True
                $ P2 = "2d"
                $ PHand += 2
        else:
            $ P2d = True
            $ P2 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_285
                jump ReDrawp2
            else:
                $ P3d = True
                $ P2 = "3d"
                $ PHand += 3
        else:
            $ P3d = True
            $ P2 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_286
                jump ReDrawp2
            else:
                $ P4d = True
                $ P2 = "4d"
                $ PHand += 4
        else:
            $ P4d = True
            $ P2 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_287
                jump ReDrawp2
            else:
                $ P5d = True
                $ P2 = "5d"
                $ PHand += 5
        else:
            $ P5d = True
            $ P2 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_288
                jump ReDrawp2
            else:
                $ P6d = True
                $ P2 = "6d"
                $ PHand += 6
        else:
            $ P6d = True
            $ P2 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_289
                jump ReDrawp2
            else:
                $ P7d = True
                $ P2 = "7d"
                $ PHand += 7
        else:
            $ P7d = True
            $ P2 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_290
                jump ReDrawp2
            else:
                $ P8d = True
                $ P2 = "8d"
                $ PHand += 8
        else:
            $ P8d = True
            $ P2 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_291
                jump ReDrawp2
            else:
                $ P9d = True
                $ P2 = "9d"
                $ PHand += 9
        else:
            $ P9d = True
            $ P2 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_292
                jump ReDrawp2
            else:
                $ P10d = True
                $ P2 = "10d"
                $ PHand += 10
        else:
            $ P10d = True
            $ P2 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_293
                jump ReDrawp2
            else:
                $ PJd = True
                $ P2 = "Jd"
                $ PHand += 10
        else:
            $ PJd = True
            $ P2 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_294
                jump ReDrawp2
            else:
                $ PQd = True
                $ P2 = "Qd"
                $ PHand += 10
        else:
            $ PQd = True
            $ P2 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_295
                jump ReDrawp2
            else:
                $ PKd = True
                $ P2 = "Kd"
                $ PHand += 10
        else:
            $ PKd = True
            $ P2 = "Kd"
            $ FHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_296
                jump ReDrawp2
            else:
                $ P2 = "Ac"
                $ Ace2 = True
                $ PAc = True
        else:
            $ P2 = "Ac"
            $ Ace2 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_297
                jump ReDrawp2
            else:
                $ P2c = True
                $ P2 = "2c"
                $ PHand += 2
        else:
            $ P2c = True
            $ P2 = "2c"
            $ FHand += 2
    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_298
                jump ReDrawp2
            else:
                $ P3c = True
                $ P2 = "3c"
                $ PHand += 3
        else:
            $ P3c = True
            $ P2 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_299
                jump ReDrawp2
            else:
                $ P4c = True
                $ P2 = "4c"
                $ PHand += 4
        else:
            $ P4c = True
            $ P2 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_300
                jump ReDrawp2
            else:
                $ P5c = True
                $ P2 = "5c"
                $ PHand += 5
        else:
            $ P5c = True
            $ P2 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_301
                jump ReDrawp2
            else:
                $ P6c = True
                $ P2 = "6c"
                $ PHand += 6
        else:
            $ P6c = True
            $ P2 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_302
                jump ReDrawp2
            else:
                $ P7c = True
                $ P2 = "7c"
                $ PHand += 7
        else:
            $ P7c = True
            $ P2 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_303
                jump ReDrawp2
            else:
                $ P8c = True
                $ P2 = "8c"
                $ PHand += 8
        else:
            $ P8c = True
            $ P2 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_304
                jump ReDrawp2
            else:
                $ P9c = True
                $ P2 = "9c"
                $ PHand += 9
        else:
            $ P9c = True
            $ P2 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_305
                jump ReDrawp2
            else:
                $ P10c = True
                $ P2 = "10c"
                $ PHand += 10
        else:
            $ P10c = True
            $ P2 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_306
                jump ReDrawp2
            else:
                $ PJc = True
                $ P2 = "Jc"
                $ PHand += 10
        else:
            $ PJc = True
            $ P2 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_307
                jump ReDrawp2
            else:
                $ PQc = True
                $ P2 = "Qc"
                $ PHand += 10
        else:
            $ PQc = True
            $ P2 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_308
                jump ReDrawp2
            else:
                $ PKc = True
                $ P2 = "Kc"
                $ PHand += 10
        else:
            $ PKc = True
            $ P2 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_309
                jump ReDrawp2
            else:
                $ P2 = "Ah"
                $ Ace2 = True
                $ PAh = True
        else:
            $ P2 = "Ah"
            $ Ace2 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_310
                jump ReDrawp2
            else:
                $ P2h = True
                $ P2 = "2h"
                $ PHand += 2
        else:
            $ P2h = True
            $ P2 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_311
                jump ReDrawp2
            else:
                $ P3h = True
                $ P2 = "3h"
                $ PHand += 3
        else:
            $ P3h = True
            $ P2 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_312
                jump ReDrawp2
            else:
                $ P4h = True
                $ P2 = "4h"
                $ PHand += 4
        else:
            $ P4h = True
            $ P2 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_313
                jump ReDrawp2
            else:
                $ P5h = True
                $ P2 = "5h"
                $ PHand += 5
        else:
            $ P5h = True
            $ P2 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_314
                jump ReDrawp2
            else:
                $ P6h = True
                $ P2 = "6h"
                $ PHand += 6
        else:
            $ P6h = True
            $ P2 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_315
                jump ReDrawp2
            else:
                $ P7h = True
                $ P2 = "7h"
                $ PHand += 7
        else:
            $ P7h = True
            $ P2 = "7h"
            $ FHand += 7
    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_316
                jump ReDrawp2
            else:
                $ P8h = True
                $ P2 = "8h"
                $ PHand += 8
        else:
            $ P8h = True
            $ P2 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_317
                jump ReDrawp2
            else:
                $ P9h = True
                $ P2 = "9h"
                $ PHand += 9
        else:
            $ P9h = True
            $ P2 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_318
                jump ReDrawp2
            else:
                $ P10h = True
                $ P2 = "10h"
                $ PHand += 10
        else:
            $ P10h = True
            $ P2 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_319
                jump ReDrawp2
            else:
                $ PJh = True
                $ P2 = "Jh"
                $ PHand += 10
        else:
            $ PJh = True
            $ P2 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_320
                jump ReDrawp2
            else:
                $ PQh = True
                $ P2 = "Qh"
                $ PHand += 10
        else:
            $ PQh = True
            $ P2 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_321
                jump ReDrawp2
            else:
                $ PKh = True
                $ P2 = "Kh"
                $ PHand += 10
        else:
            $ PKh = True
            $ P2 = "Kh"
            $ FHand += 10
    else:

        jump endgame

    if freeplay == True:
        if P1 == P2:

            call AceBlock from _call_AceBlock_7
            $ FHand = 0
            jump TryAgainP2
        else:
            $ PHand += FHand
            $ FHand = 0
            $ PCards +=1
            return
    else:
        $ deck -=1
        $ PCards +=1
        return

label TryAgainP2:
    call CardSelect from _call_CardSelect_322
    jump PlayersCard2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
