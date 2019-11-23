
label CardSelect:
    $ renpy.block_rollback()

    $ CardSelector = renpy.random.randint(1,13)

    $ SuitSelector = renpy.random.randint(1,4)

    if CardSelector == 1:
        $ P1Card = 1
    elif CardSelector == 2:
        $ P1Card = 2
    elif CardSelector == 3:
        $ P1Card = 3
    elif CardSelector == 4:
        $ P1Card = 4
    elif CardSelector == 5:
        $ P1Card = 5
    elif CardSelector == 6:
        $ P1Card = 6
    elif CardSelector == 7:
        $ P1Card = 7
    elif CardSelector == 8:
        $ P1Card = 8
    elif CardSelector == 9:
        $ P1Card = 9
    elif CardSelector == 10:
        $ P1Card = 10
    elif CardSelector == 11:
        $ P1Card = 11
    elif CardSelector == 12:
        $ P1Card = 12
    elif CardSelector == 13:
        $ P1Card = 13

    if SuitSelector == 1:

        pass
    elif SuitSelector == 2:

        $ CardSelector += 13
    elif SuitSelector == 3:

        $ CardSelector += 26
    elif SuitSelector == 4:

        $ CardSelector += 39


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
