label ReDrawp1:
    $ renpy.block_rollback()
    if deck <= 0:
        jump CheckDeck
    else:
        call CardSelect from _call_CardSelect_363
        jump PlayersCard1


label PlayersCard1:
    $ renpy.block_rollback()

    if CardSelector == 1:
        if freeplay == False:
            if PAs== True:
                jump ReDrawp1
            else:
                $ P1 = "As"
                $ Ace = True
                $ PAs = True
        else:
            $ P1 = "As"
            $ Ace = True
    elif CardSelector == 2:
        if freeplay == False:
            if P2s == True:
                jump ReDrawp1
            else:
                $ P2s = True
                $ P1 = "2s"
                $ PHand += 2
        else:
            $ P2s = True
            $ P1 = "2s"
            $ PHand += 2
    elif CardSelector == 3:
        if freeplay == False:
            if P3s == True:
                jump ReDrawp1
            else:
                $ P3s = True
                $ P1 = "3s"
                $ PHand += 3
        else:
            $ P3s = True
            $ P1 = "3s"
            $ PHand += 3
    elif CardSelector == 4:
        if freeplay == False:
            if P4s == True:
                jump ReDrawp1
            else:
                $ P4s = True
                $ P1 = "4s"
                $ PHand += 4
        else:
            $ P4s = True
            $ P1 = "4s"
            $ PHand += 4
    elif CardSelector == 5:
        if freeplay == False:
            if P5s == True:
                jump ReDrawp1
            else:
                $ P5s = True
                $ P1 = "5s"
                $ PHand += 5
        else:
            $ P5s = True
            $ P1 = "5s"
            $ PHand += 5
    elif CardSelector == 6:
        if freeplay == False:
            if P6s == True:
                jump ReDrawp1
            else:
                $ P6s = True
                $ P1 = "6s"
                $ PHand += 6
        else:
            $ P6s = True
            $ P1 = "6s"
            $ PHand += 6
    elif CardSelector == 7:
        if freeplay == False:
            if P7s == True:
                jump ReDrawp1
            else:
                $ P7s = True
                $ P1 = "7s"
                $ PHand += 7
        else:
            $ P7s = True
            $ P1 = "7s"
            $ PHand += 7
    elif CardSelector == 8:
        if freeplay == False:
            if P8s == True:
                jump ReDrawp1
            else:
                $ P8s = True
                $ P1 = "8s"
                $ PHand += 8
        else:
            $ P8s = True
            $ P1 = "8s"
            $ PHand += 8
    elif CardSelector == 9:
        if freeplay == False:
            if P9s == True:
                jump ReDrawp1
            else:
                $ P9s = True
                $ P1 = "9s"
                $ PHand += 9
        else:
            $ P9s = True
            $ P1 = "9s"
            $ PHand += 9
    elif CardSelector == 10:
        if freeplay == False:
            if P10s == True:
                jump ReDrawp1
            else:
                $ P10s = True
                $ P1 = "10s"
                $ PHand += 10
        else:
            $ P10s = True
            $ P1 = "10s"
            $ PHand += 10
    elif CardSelector == 11:
        if freeplay == False:
            if PJs == True:
                jump ReDrawp1
            else:
                $ PJs = True
                $ P1 = "Js"
                $ PHand += 10
        else:
            $ PJs = True
            $ P1 = "Js"
            $ PHand += 10
    elif CardSelector == 12:
        if freeplay == False:
            if PQs == True:
                jump ReDrawp1
            else:
                $ PQs = True
                $ P1 = "Qs"
                $ PHand += 10
        else:
            $ PQs = True
            $ P1 = "Qs"
            $ PHand += 10
    elif CardSelector == 13:
        if freeplay == False:
            if PKs== True:
                jump ReDrawp1
            else:
                $ PKs = True
                $ P1 = "Ks"
                $ PHand += 10
        else:
            $ PKs = True
            $ P1 = "Ks"
            $ PHand += 10
    elif CardSelector == 14:
        if freeplay == False:
            if PAd == True:
                call CardSelect from _call_CardSelect_364
                jump ReDrawp1
            else:
                $ P1 = "Ad"
                $ Ace = True
                $ PAd = True
        else:
            $ P1 = "Ad"
            $ Ace = True
            $ PAd = True
    elif CardSelector == 15:
        if freeplay == False:
            if P2d == True:
                jump ReDrawp1
            else:
                $ P2d = True
                $ P1 = "2d"
                $ PHand += 2
        else:
            $ P2d = True
            $ P1 = "2d"
            $ PHand += 2
    elif CardSelector == 16:
        if freeplay == False:
            if P3d == True:
                call CardSelect from _call_CardSelect_365
                jump ReDrawp1
            else:
                $ P3d = True
                $ P1 = "3d"
                $ PHand += 3
        else:
            $ P3d = True
            $ P1 = "3d"
            $ PHand += 3
    elif CardSelector == 17:
        if freeplay == False:
            if P4d == True:
                call CardSelect from _call_CardSelect_366
                jump ReDrawp1
            else:
                $ P4d = True
                $ P1 = "4d"
                $ PHand += 4
        else:
            $ P4d = True
            $ P1 = "4d"
            $ PHand += 4
    elif CardSelector == 18:
        if freeplay == False:
            if P5d == True:
                call CardSelect from _call_CardSelect_367
                jump ReDrawp1
            else:
                $ P5d = True
                $ P1 = "5d"
                $ PHand += 5
        else:
            $ P5d = True
            $ P1 = "5d"
            $ PHand += 5
    elif CardSelector == 19:
        if freeplay == False:
            if P6d == True:
                call CardSelect from _call_CardSelect_368
                jump ReDrawp1
            else:
                $ P6d = True
                $ P1 = "6d"
                $ PHand += 6
        else:
            $ P6d = True
            $ P1 = "6d"
            $ PHand += 6
    elif CardSelector == 20:
        if freeplay == False:
            if P7d == True:
                call CardSelect from _call_CardSelect_369
                jump ReDrawp1
            else:
                $ P7d = True
                $ P1 = "7d"
                $ PHand += 7
        else:
            $ P7d = True
            $ P1 = "7d"
            $ PHand += 7
    elif CardSelector == 21:
        if freeplay == False:
            if P8d == True:
                call CardSelect from _call_CardSelect_370
                jump ReDrawp1
            else:
                $ P8d = True
                $ P1 = "8d"
                $ PHand += 8
        else:
            $ P8d = True
            $ P1 = "8d"
            $ PHand += 8
    elif CardSelector == 22:
        if freeplay == False:
            if P9d == True:
                call CardSelect from _call_CardSelect_371
                jump ReDrawp1
            else:
                $ P9d = True
                $ P1 = "9d"
                $ PHand += 9
        else:
            $ P9d = True
            $ P1 = "9d"
            $ PHand += 9
    elif CardSelector == 23:
        if freeplay == False:
            if P10d == True:
                call CardSelect from _call_CardSelect_372
                jump ReDrawp1
            else:
                $ P10d = True
                $ P1 = "10d"
                $ PHand += 10
        else:
            $ P10d = True
            $ P1 = "10d"
            $ PHand += 10
    elif CardSelector == 24:
        if freeplay == False:
            if PJd == True:
                call CardSelect from _call_CardSelect_373
                jump ReDrawp1
            else:
                $ PJd = True
                $ P1 = "Jd"
                $ PHand += 10
        else:
            $ PJd = True
            $ P1 = "Jd"
            $ PHand += 10
    elif CardSelector == 25:
        if freeplay == False:
            if PQd == True:
                call CardSelect from _call_CardSelect_374
                jump ReDrawp1
            else:
                $ PQd = True
                $ P1 = "Qd"
                $ PHand += 10
        else:
            $ PQd = True
            $ P1 = "Qd"
            $ PHand += 10
    elif CardSelector == 26:
        if freeplay == False:
            if PKd== True:
                call CardSelect from _call_CardSelect_375
                jump ReDrawp1
            else:
                $ PKd = True
                $ P1 = "Kd"
                $ PHand += 10
        else:
            $ PKd = True
            $ P1 = "Kd"
            $ PHand += 10

    elif CardSelector == 27:
        if freeplay == False:
            if PAc == True:
                call CardSelect from _call_CardSelect_376
                jump ReDrawp1
            else:
                $ P1 = "Ac"
                $ Ace = True
                $ PAc = True
        else:
            $ P1 = "Ac"
            $ Ace = True
            $ PAc = True
    elif CardSelector == 28:
        if freeplay == False:
            if P2c == True:
                call CardSelect from _call_CardSelect_377
                jump ReDrawp1
            else:
                $ P2c = True
                $ P1 = "2c"
                $ PHand += 2
        else:
            $ P2c = True
            $ P1 = "2c"
            $ PHand += 2

    elif CardSelector == 29:
        if freeplay == False:
            if P3c == True:
                call CardSelect from _call_CardSelect_378
                jump ReDrawp1
            else:
                $ P3c = True
                $ P1 = "3c"
                $ PHand += 3
        else:
            $ P3c = True
            $ P1 = "3c"
            $ PHand += 3
    elif CardSelector == 30:
        if freeplay == False:
            if P4c == True:
                call CardSelect from _call_CardSelect_379
                jump ReDrawp1
            else:
                $ P4c = True
                $ P1 = "4c"
                $ PHand += 4
        else:
            $ P4c = True
            $ P1 = "4c"
            $ PHand += 4
    elif CardSelector == 31:
        if freeplay == False:
            if P5c == True:
                call CardSelect from _call_CardSelect_380
                jump ReDrawp1
            else:
                $ P5c = True
                $ P1 = "5c"
                $ PHand += 5
        else:
            $ P5c = True
            $ P1 = "5c"
            $ PHand += 5
    elif CardSelector == 32:
        if freeplay == False:
            if P6c == True:
                call CardSelect from _call_CardSelect_381
                jump ReDrawp1
            else:
                $ P6c = True
                $ P1 = "6c"
                $ PHand += 6
        else:
            $ P6c = True
            $ P1 = "6c"
            $ PHand += 6
    elif CardSelector == 33:
        if freeplay == False:
            if P7c == True:
                call CardSelect from _call_CardSelect_382
                jump ReDrawp1
            else:
                $ P7c = True
                $ P1 = "7c"
                $ PHand += 7
        else:
            $ P7c = True
            $ P1 = "7c"
            $ PHand += 7
    elif CardSelector == 34:
        if freeplay == False:
            if P8c == True:
                call CardSelect from _call_CardSelect_383
                jump ReDrawp1
            else:
                $ P8c = True
                $ P1 = "8c"
                $ PHand += 8
        else:
            $ P8c = True
            $ P1 = "8c"
            $ PHand += 8
    elif CardSelector == 35:
        if freeplay == False:
            if P9c == True:
                call CardSelect from _call_CardSelect_384
                jump ReDrawp1
            else:
                $ P9c = True
                $ P1 = "9c"
                $ PHand += 9
        else:
            $ P9c = True
            $ P1 = "9c"
            $ PHand += 9
    elif CardSelector == 36:
        if freeplay == False:
            if P10c == True:
                call CardSelect from _call_CardSelect_385
                jump ReDrawp1
            else:
                $ P10c = True
                $ P1 = "10c"
                $ PHand += 10
        else:
            $ P10c = True
            $ P1 = "10c"
            $ PHand += 10
    elif CardSelector == 37:
        if freeplay == False:
            if PJc == True:
                call CardSelect from _call_CardSelect_386
                jump ReDrawp1
            else:
                $ PJc = True
                $ P1 = "Jc"
                $ PHand += 10
        else:
            $ PJc = True
            $ P1 = "Jc"
            $ PHand += 10
    elif CardSelector == 38:
        if freeplay == False:
            if PQc == True:
                call CardSelect from _call_CardSelect_387
                jump ReDrawp1
            else:
                $ PQc = True
                $ P1 = "Qc"
                $ PHand += 10
        else:
            $ PQc = True
            $ P1 = "Qc"
            $ PHand += 10
    elif CardSelector == 39:
        if freeplay == False:
            if PKc== True:
                call CardSelect from _call_CardSelect_388
                jump ReDrawp1
            else:
                $ PKc = True
                $ P1 = "Kc"
                $ PHand += 10
        else:
            $ PKc = True
            $ P1 = "Kc"
            $ PHand += 10

    elif CardSelector == 40:
        if freeplay == False:
            if PAh == True:
                call CardSelect from _call_CardSelect_389
                jump ReDrawp1
            else:
                $ P1 = "Ah"
                $ Ace = True
                $ PAh = True
        else:
            $ P1 = "Ah"
            $ Ace = True
            $ PAh = True
    elif CardSelector == 41:
        if freeplay == False:
            if P2h == True:
                call CardSelect from _call_CardSelect_390
                jump ReDrawp1
            else:
                $ P2h = True
                $ P1 = "2h"
                $ PHand += 2
        else:
            $ P2h = True
            $ P1 = "2h"
            $ PHand += 2
    elif CardSelector == 42:
        if freeplay == False:
            if P3h == True:
                call CardSelect from _call_CardSelect_391
                jump ReDrawp1
            else:
                $ P3h = True
                $ P1 = "3h"
                $ PHand += 3
        else:
            $ P3h = True
            $ P1 = "3h"
            $ PHand += 3
    elif CardSelector == 43:
        if freeplay == False:
            if P4h == True:
                call CardSelect from _call_CardSelect_392
                jump ReDrawp1
            else:
                $ P4h = True
                $ P1 = "4h"
                $ PHand += 4
        else:
            $ P4h = True
            $ P1 = "4h"
            $ PHand += 4
    elif CardSelector == 44:
        if freeplay == False:
            if P5h == True:
                call CardSelect from _call_CardSelect_393
                jump ReDrawp1
            else:
                $ P5h = True
                $ P1 = "5h"
                $ PHand += 5
        else:
            $ P5h = True
            $ P1 = "5h"
            $ PHand += 5
    elif CardSelector == 45:
        if freeplay == False:
            if P6h == True:
                call CardSelect from _call_CardSelect_394
                jump ReDrawp1
            else:
                $ P6h = True
                $ P1 = "6h"
                $ PHand += 6
        else:
            $ P6h = True
            $ P1 = "6h"
            $ PHand += 6
    elif CardSelector == 46:
        if freeplay == False:
            if P7h == True:
                call CardSelect from _call_CardSelect_395
                jump ReDrawp1
            else:
                $ P7h = True
                $ P1 = "7h"
                $ PHand += 7
        else:
            $ P7h = True
            $ P1 = "7h"
            $ PHand += 7

    elif CardSelector == 47:
        if freeplay == False:
            if P8h == True:
                call CardSelect from _call_CardSelect_396
                jump ReDrawp1
            else:
                $ P8h = True
                $ P1 = "8h"
                $ PHand += 8
        else:
            $ P8h = True
            $ P1 = "8h"
            $ PHand += 8
    elif CardSelector == 48:
        if freeplay == False:
            if P9h == True:
                call CardSelect from _call_CardSelect_397
                jump ReDrawp1
            else:
                $ P9h = True
                $ P1 = "9h"
                $ PHand += 9
        else:
            $ P9h = True
            $ P1 = "9h"
            $ PHand += 9
    elif CardSelector == 49:
        if freeplay == False:
            if P10h == True:
                call CardSelect from _call_CardSelect_398
                jump ReDrawp1
            else:
                $ P10h = True
                $ P1 = "10h"
                $ PHand += 10
        else:
            $ P10h = True
            $ P1 = "10h"
            $ PHand += 10
    elif CardSelector == 50:
        if freeplay == False:
            if PJh == True:
                call CardSelect from _call_CardSelect_399
                jump ReDrawp1
            else:
                $ PJh = True
                $ P1 = "Jh"
                $ PHand += 10
        else:
            $ PJh = True
            $ P1 = "Jh"
            $ PHand += 10
    elif CardSelector == 51:
        if freeplay == False:
            if PQh == True:
                call CardSelect from _call_CardSelect_400
                jump ReDrawp1
            else:
                $ PQh = True
                $ P1 = "Qh"
                $ PHand += 10
        else:
            $ PQh = True
            $ P1 = "Qh"
            $ PHand += 10
    elif CardSelector == 52:
        if freeplay == False:
            if PKh== True:
                call CardSelect from _call_CardSelect_401
                jump ReDrawp1
            else:
                $ PKh = True
                $ P1 = "Kh"
                $ PHand += 10
        else:
            $ PKh = True
            $ P1 = "Kh"
            $ PHand += 10
    else:

        jump endgame

    $ PCards +=1
    $ deck -=1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
