label ReDrawp3:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_323
        jump PlayersCard3


label PlayersCard3:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawp3
            else:
                $ P3 = "As"
                $ Ace3 = True
                $ PAs = True
        else:
            $ P3 = "As"
            $ Ace3 = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawp3
            else:
                $ P2s = True
                $ P3 = "2s"
                $ PHand += 2
        else:
            $ P2s = True
            $ P3 = "2s"
            $ FHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawp3
            else:
                $ P3s = True
                $ P3 = "3s"
                $ PHand += 3
        else:
            $ P3s = True
            $ P3 = "3s"
            $ FHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawp3
            else:
                $ P4s = True
                $ P3 = "4s"
                $ PHand += 4
        else:
            $ P4s = True
            $ P3 = "4s"
            $ FHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawp3
            else:
                $ P5s = True
                $ P3 = "5s"
                $ PHand += 5
        else:
            $ P5s = True
            $ P3 = "5s"
            $ FHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawp3
            else:
                $ P6s = True
                $ P3 = "6s"
                $ PHand += 6
        else:
            $ P6s = True
            $ P3 = "6s"
            $ FHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawp3
            else:
                $ P7s = True
                $ P3 = "7s"
                $ PHand += 7
        else:
            $ P7s = True
            $ P3 = "7s"
            $ FHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawp3
            else:
                $ P8s = True
                $ P3 = "8s"
                $ PHand += 8
        else:
            $ P8s = True
            $ P3 = "8s"
            $ FHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawp3
            else:
                $ P9s = True
                $ P3 = "9s"
                $ PHand += 9
        else:
            $ P9s = True
            $ P3 = "9s"
            $ FHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawp3
            else:
                $ P10s = True
                $ P3 = "10s"
                $ PHand += 10
        else:
            $ P10s = True
            $ P3 = "10s"
            $ FHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawp3
            else:
                $ PJs = True
                $ P3 = "Js"
                $ PHand += 10
        else:
            $ PJs = True
            $ P3 = "Js"
            $ FHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawp3
            else:
                $ PQs = True
                $ P3 = "Qs"
                $ PHand += 10
        else:
            $ PQs = True
            $ P3 = "Qs"
            $ FHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawp3
            else:
                $ PKs = True
                $ P3 = "Ks"
                $ PHand += 10
        else:
            $ PKs = True
            $ P3 = "Ks"
            $ FHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_324
                jump ReDrawp3
            else:
                $ P3 = "Ad"
                $ Ace3 = True
                $ PAd = True
        else:
            $ P3 = "Ad"
            $ Ace3 = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawp3
            else:
                $ P2d = True
                $ P3 = "2d"
                $ PHand += 2
        else:
            $ P2d = True
            $ P3 = "2d"
            $ FHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_325
                jump ReDrawp3
            else:
                $ P3d = True
                $ P3 = "3d"
                $ PHand += 3
        else:
            $ P3d = True
            $ P3 = "3d"
            $ FHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_326
                jump ReDrawp3
            else:
                $ P4d = True
                $ P3 = "4d"
                $ PHand += 4
        else:
            $ P4d = True
            $ P3 = "4d"
            $ FHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_327
                jump ReDrawp3
            else:
                $ P5d = True
                $ P3 = "5d"
                $ PHand += 5
        else:
            $ P5d = True
            $ P3 = "5d"
            $ FHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_328
                jump ReDrawp3
            else:
                $ P6d = True
                $ P3 = "6d"
                $ PHand += 6
        else:
            $ P6d = True
            $ P3 = "6d"
            $ FHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_329
                jump ReDrawp3
            else:
                $ P7d = True
                $ P3 = "7d"
                $ PHand += 7
        else:
            $ P7d = True
            $ P3 = "7d"
            $ FHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_330
                jump ReDrawp3
            else:
                $ P8d = True
                $ P3 = "8d"
                $ PHand += 8
        else:
            $ P8d = True
            $ P3 = "8d"
            $ FHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_331
                jump ReDrawp3
            else:
                $ P9d = True
                $ P3 = "9d"
                $ PHand += 9
        else:
            $ P9d = True
            $ P3 = "9d"
            $ FHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_332
                jump ReDrawp3
            else:
                $ P10d = True
                $ P3 = "10d"
                $ PHand += 10
        else:
            $ P10d = True
            $ P3 = "10d"
            $ FHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_333
                jump ReDrawp3
            else:
                $ PJd = True
                $ P3 = "Jd"
                $ PHand += 10
        else:
            $ PJd = True
            $ P3 = "Jd"
            $ FHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_334
                jump ReDrawp3
            else:
                $ PQd = True
                $ P3 = "Qd"
                $ PHand += 10
        else:
            $ PQd = True
            $ P3 = "Qd"
            $ FHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_335
                jump ReDrawp3
            else:
                $ PKd = True
                $ P3 = "Kd"
                $ PHand += 10
        else:
            $ PKd = True
            $ P3 = "Kd"
            $ FHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_336
                jump ReDrawp3
            else:
                $ P3 = "Ac"
                $ Ace3 = True
                $ PAc = True
        else:
            $ P3 = "Ac"
            $ Ace3 = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_337
                jump ReDrawp3
            else:
                $ P2c = True
                $ P3 = "2c"
                $ PHand += 2
        else:
            $ P2c = True
            $ P3 = "2c"
            $ FHand += 2

    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_338
                jump ReDrawp3
            else:
                $ P3c = True
                $ P3 = "3c"
                $ PHand += 3
        else:
            $ P3c = True
            $ P3 = "3c"
            $ FHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_339
                jump ReDrawp3
            else:
                $ P4c = True
                $ P3 = "4c"
                $ PHand += 4
        else:
            $ P4c = True
            $ P3 = "4c"
            $ FHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_340
                jump ReDrawp3
            else:
                $ P5c = True
                $ P3 = "5c"
                $ PHand += 5
        else:
            $ P5c = True
            $ P3 = "5c"
            $ FHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_341
                jump ReDrawp3
            else:
                $ P6c = True
                $ P3 = "6c"
                $ PHand += 6
        else:
            $ P6c = True
            $ P3 = "6c"
            $ FHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_342
                jump ReDrawp3
            else:
                $ P7c = True
                $ P3 = "7c"
                $ PHand += 7
        else:
            $ P7c = True
            $ P3 = "7c"
            $ FHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_343
                jump ReDrawp3
            else:
                $ P8c = True
                $ P3 = "8c"
                $ PHand += 8
        else:
            $ P8c = True
            $ P3 = "8c"
            $ FHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_344
                jump ReDrawp3
            else:
                $ P9c = True
                $ P3 = "9c"
                $ PHand += 9
        else:
            $ P9c = True
            $ P3 = "9c"
            $ FHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_345
                jump ReDrawp3
            else:
                $ P10c = True
                $ P3 = "10c"
                $ PHand += 10
        else:
            $ P10c = True
            $ P3 = "10c"
            $ FHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_346
                jump ReDrawp3
            else:
                $ PJc = True
                $ P3 = "Jc"
                $ PHand += 10
        else:
            $ PJc = True
            $ P3 = "Jc"
            $ FHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_347
                jump ReDrawp3
            else:
                $ PQc = True
                $ P3 = "Qc"
                $ PHand += 10
        else:
            $ PQc = True
            $ P3 = "Qc"
            $ FHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_348
                jump ReDrawp3
            else:
                $ PKc = True
                $ P3 = "Kc"
                $ PHand += 10
        else:
            $ PKc = True
            $ P3 = "Kc"
            $ FHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_349
                jump ReDrawp3
            else:
                $ P3 = "Ah"
                $ Ace3 = True
                $ PAh = True
        else:
            $ P3 = "Ah"
            $ Ace3 = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_350
                jump ReDrawp3
            else:
                $ P2h = True
                $ P3 = "2h"
                $ PHand += 2
        else:
            $ P2h = True
            $ P3 = "2h"
            $ FHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_351
                jump ReDrawp3
            else:
                $ P3h = True
                $ P3 = "3h"
                $ PHand += 3
        else:
            $ P3h = True
            $ P3 = "3h"
            $ FHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_352
                jump ReDrawp3
            else:
                $ P4h = True
                $ P3 = "4h"
                $ PHand += 4
        else:
            $ P4h = True
            $ P3 = "4h"
            $ FHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_353
                jump ReDrawp3
            else:
                $ P5h = True
                $ P3 = "5h"
                $ PHand += 5
        else:
            $ P5h = True
            $ P3 = "5h"
            $ FHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_354
                jump ReDrawp3
            else:
                $ P6h = True
                $ P3 = "6h"
                $ PHand += 6
        else:
            $ P6h = True
            $ P3 = "6h"
            $ FHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_355
                jump ReDrawp3
            else:
                $ P7h = True
                $ P3 = "7h"
                $ PHand += 7
        else:
            $ P7h = True
            $ P3 = "7h"
            $ FHand += 7

    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_356
                jump ReDrawp3
            else:
                $ P8h = True
                $ P3 = "8h"
                $ PHand += 8
        else:
            $ P8h = True
            $ P3 = "8h"
            $ FHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_357
                jump ReDrawp3
            else:
                $ P9h = True
                $ P3 = "9h"
                $ PHand += 9
        else:
            $ P9h = True
            $ P3 = "9h"
            $ FHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_358
                jump ReDrawp3
            else:
                $ P10h = True
                $ P3 = "10h"
                $ PHand += 10
        else:
            $ P10h = True
            $ P3 = "10h"
            $ FHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_359
                jump ReDrawp3
            else:
                $ PJh = True
                $ P3 = "Jh"
                $ PHand += 10
        else:
            $ PJh = True
            $ P3 = "Jh"
            $ FHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_360
                jump ReDrawp3
            else:
                $ PQh = True
                $ P3 = "Qh"
                $ PHand += 10
        else:
            $ PQh = True
            $ P3 = "Qh"
            $ FHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_361
                jump ReDrawp3
            else:
                $ PKh = True
                $ P3 = "Kh"
                $ PHand += 10
        else:
            $ PKh = True
            $ P3 = "Kh"
            $ FHand += 10
    else:

        jump endgame

    if freeplay == True:
        if D2 == P3 or P3 == P1 or P3 == P2:

            call AceBlock from _call_AceBlock_8
            $ FHand = 0
            jump TryAgainP3
        else:
            call AceCheck from _call_AceCheck_1
            $ PHand += FHand
            $ FHand = 0
            $ PCards +=1
            return
    else:
        $ deck -=1
        $ PCards +=1
        return

label TryAgainP3:
    call CardSelect from _call_CardSelect_362
    jump PlayersCard3

label AceBlock:
    if HoldAce == False:
        if Ace == True or Ace2 == True or Ace3 == True or Ace4 == True or Ace5 == True or DAce == True or DAce2 == True or DAce3 == True or DAce4 == True or DAce5 == True:

            $ HoldAce = True
        else:
            $ Ace = False
            $ Ace2 = False
            $ Ace3 = False
            $ Ace4 = False
            $ Ace5 = False
            $ DAce2 = False
            $ DAce = False
            $ DAce3 = False
            $ DAce4 = False
            $ DAce5 = False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
