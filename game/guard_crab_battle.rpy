label guard_crab_battle:
    fs1 "let's do it!"
    show screen tourney_crabstats

    if guard_crab ==1:
        show strongcrabshuffle with dissolve
        $ crab_health = 80
        $ normal_crab = False
        $ strong_crab = True
        $ legend_crab = False
        "you face a strong battling crab."
        jump guard_crab_battle_player
    if guard_crab ==2:
        show crabshuffle with dissolve
        $ crab_health = 50
        $ normal_crab = True
        $ strong_crab = False
        $ legend_crab = False
        "you face a normal battling crab."
        jump guard_crab_battle_player
    if guard_crab ==3:
        show crabshuffle with dissolve
        $ crab_health = 50
        $ normal_crab = True
        $ strong_crab = False
        $ legend_crab = False
        "you face a normal battling crab."
        jump guard_crab_battle_player
    if guard_crab ==4:
        show bessiecrabshuffle with dissolve
        $ crab_health = 160
        $ normal_crab = False
        $ strong_crab = True
        $ legend_crab = False
        fs1 "time for bessie, i think."
        fs1 "get on out there girl!"
        fs1 "she doesn't have a special attack, but she never misses!"
        "you face bessie."
        $ bessie_crab = True

        jump guard_crab_battle_player

label guard_crab_battle_player:


    if crab_standin:
        if crab_standin_health <=0:
            if crab_standin_normal:
                $ normal_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_normal = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump guard_crab_battle_player2
            if crab_standin_strong:
                $ strong_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_strong = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump guard_crab_battle_player2
            if crab_standin_legend:
                $ legend_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_legend = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump guard_crab_battle_player2
        else:


            if hyperboom ==1:
                "hyper-boom snip activates!"
                if crab_standin_normal:
                    $ crab_health -=11
                    show text "{color=#f00}{b}-11 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump guard_crab_battle_crab
                if crab_standin_strong:
                    $ crab_health -=23
                    show text "{color=#f00}{b}-23 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump guard_crab_battle_crab
                if crab_standin_legend:
                    $ crab_health -= 45
                    show text "{color=#f00}{b}-45 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump guard_crab_battle_crab

    if crab_player_health <=0:
        "you lose!"
        jump guard_crab_battle_lose
    else:
        jump guard_crab_battle_player2

label guard_crab_battle_player2:
    menu:
        "crab battle!" if not crab_standin:
            if crabs_caught >=1:
                if normal_crabs >=1:
                    "you send out a normal crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 50
                    $ crab_standin_normal = True
                    jump guard_crab_battle_player

                if strong_crabs >=1:
                    "you send out a strong crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 80
                    $ crab_standin_strong = True
                    jump guard_crab_battle_player

                if legend_crabs >=1:
                    "you send out a legendary crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 200
                    $ crab_standin_legend = True
                    jump guard_crab_battle_player

                if bessie:
                    "you send out bessie!"
                    "she takes your place in the battle!"
                    "she has no special attack, but never misses!"
                    $ crab_standin = True
                    $ crab_standin_health = 180
                    $ crab_standin_bessie = True
                    jump guard_crab_battle_player
            else:
                "you don't have any crabs!"
                y "....normally a good thing, but whatever."
                jump guard_crab_battle_player


        "snip!" if crab_standin and not olmusky:
            if crab_standin_bessie:
                if randcrabpunch ==1:
                    $ crab_health -=20
                    show text "{color=#f00}{b}-20 enemy crab health" at truecenter with dissolve
                    "bessie snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
            $ randcrabpunch = renpy.random.randint(1, 2)
            if crab_standin_normal:
                if randcrabpunch ==1:
                    $ crab_health -=7
                    show text "{color=#f00}{b}-7 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump guard_crab_battle_crab
            if crab_standin_strong:
                if randcrabpunch ==1:
                    $ crab_health -=15
                    show text "{color=#f00}{b}-15 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump guard_crab_battle_crab
            if crab_standin_legend:
                if randcrabpunch ==1:
                    $ crab_health -=30
                    show text "{color=#f00}{b}-30 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump guard_crab_battle_crab


        "hyper-boom snip - powerful, takes an extra turn, always hits" if crab_standin and not bessie:
            $ hyperboom = 1
            "your crab charges it's attack! it's glowing!"
            jump guard_crab_battle_crab

        "punch" if not crab_standin:
            $ randcrabpunch = renpy.random.randint(1, 3)
            if randcrabpunch ==1:
                if crabs_killed ==0:
                    $ crab_health -=10
                    show text "{color=#f00}{b}-10 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==1:
                    $ crab_health -=12
                    show text "{color=#f00}{b}-12 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==2:
                    $ crab_health -=14
                    show text "{color=#f00}{b}-14 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==3:
                    $ crab_health -=16
                    show text "{color=#f00}{b}-16 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==4:
                    $ crab_health -=18
                    show text "{color=#f00}{b}-18 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==5:
                    $ crab_health -=20
                    show text "{color=#f00}{b}-20 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==6:
                    $ crab_health -=22
                    show text "{color=#f00}{b}-22 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==7:
                    $ crab_health -=24
                    show text "{color=#f00}{b}-24 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==8:
                    $ crab_health -=26
                    show text "{color=#f00}{b}-26 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==9:
                    $ crab_health -=28
                    show text "{color=#f00}{b}-28 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==10:
                    $ crab_health -=30
                    show text "{color=#f00}{b}-30 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==11:
                    $ crab_health -=32
                    show text "{color=#f00}{b}-32 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==12:
                    $ crab_health -=34
                    show text "{color=#f00}{b}-34 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==13:
                    $ crab_health -=36
                    show text "{color=#f00}{b}-36 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==14:
                    $ crab_health -=38
                    show text "{color=#f00}{b}-38 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==16:
                    $ crab_health -=40
                    show text "{color=#f00}{b}-40 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==16:
                    $ crab_health -=42
                    show text "{color=#f00}{b}-42 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==17:
                    $ crab_health -=44
                    show text "{color=#f00}{b}-44 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==18:
                    $ crab_health -=46
                    show text "{color=#f00}{b}-46 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==19:
                    $ crab_health -=48
                    show text "{color=#f00}{b}-48 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==20:
                    $ crab_health -=49
                    show text "{color=#f00}{b}-49 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==21:
                    $ crab_health -=50
                    show text "{color=#f00}{b}-50 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed >=22:
                    $ crab_health -=50
                    show text "{color=#f00}{b}-50 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab

            if randcrabpunch ==2:
                if crabs_killed ==0:
                    $ crab_health -=14
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-14 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==1:
                    $ crab_health -=19
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-19 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==2:
                    $ crab_health -=24
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-24 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==3:
                    $ crab_health -=27
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-27 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==4:
                    $ crab_health -=31
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-31 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==5:
                    $ crab_health -=34
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-34 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==6:
                    $ crab_health -=37
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-37 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==7:
                    $ crab_health -=40
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-40 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==8:
                    $ crab_health -=43
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-43 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==9:
                    $ crab_health -=46
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-46 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed ==10:
                    $ crab_health -=49
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-49 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
                if crabs_killed >=11:
                    $ crab_health -=54
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-54 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump guard_crab_battle_crab
            if randcrabpunch ==3:
                "you miss!"
                jump guard_crab_battle_crab
        "defend":

            $ player_crab_def = True
            "you defend!"
            jump guard_crab_battle_crab
        "try to catch":

            "you can't catch someone else's crabs!"
            yd "...if only that was true."
            jump shady_crab_battle_player
        "use potion":

            "you have [crab_potions] potion(s)."
            "potions recover up to 250 health."
            if crab_potions >=1:
                "use a potion now?"
                menu:
                    "use potion":
                        if crab_standin:
                            $ crab_potions -=1
                            if crab_standin_normal:
                                $ crab_standin_health = 50
                            if crab_standin_strong:
                                $ crab_standin_health = 80
                            if crab_standin_legend:
                                $ crab_standin_health = 200
                            if crab_standin_bessie:
                                $ crab_standin_health = 180
                            "ally crab health recovered!"
                            jump guard_crab_battle_player
                        else:

                            $ crab_potions -=1
                            $ crab_player_health = 100
                            "your health recovered!"
                            jump guard_crab_battle_player
                    "don't use potion":

                        jump guard_crab_battle_player
            else:
                "you don't have any potions left!"
                "buy more to use them!"
                jump guard_crab_battle_player

        "run away" if first_crab_battles:
            "you can't run from a trainer battle!"
            jump guard_crab_battle_player


label guard_crab_battle_crab:
    if crab_health <=0:
        hide crabshuffle
        hide strongcrabshuffle
        hide legendcrabshuffle
        hide bessiecrabshuffle
        with dissolve

        play sound "audio/win2.mp3"
        "you kicked that crab's ass!"

        if guard_crab == 1:
            $ guard_crab = 2
            $ remaining_enemy_crabs = 2
            fs1 "don't get too excited, i've got more!"
            jump guard_crab_battle_next

        if guard_crab == 2:
            $ guard_crab = 3
            $ remaining_enemy_crabs = 1
            fs1 "don't get too excited, i've got more!"
            jump guard_crab_battle_next

        if guard_crab == 3:
            $ guard_crab = 4
            $ remaining_enemy_crabs = 0
            fs1 "it's time to bring out bessie!"
            jump guard_crab_battle_next
        if guard_crab ==4:
            $ bessie = True
            "you win!"
            jump guard_crab_win
    else:

        if crab_charge:
            if player_crab_def:
                if bessie_crab:
                    if crab_standin:
                        $ crab_standin_health -=20
                        show text "{color=#f00}{b}-20 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump guard_crab_battle_player
                    else:
                        $ crab_player_health -=20
                        show text "{color=#f00}{b}-20 player health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump guard_crab_battle_player

                $ randcrabattack = renpy.random.randint(1, 2)
                if randcrabattack ==1:
                    if crab_standin:
                        if normal_crab:
                            $ crab_standin_health -=7
                            show text "{color=#f00}{b}-7 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if strong_crab:
                            $ crab_standin_health -=15
                            show text "{color=#f00}{b}-15 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if legend_crab:
                            $ crab_standin_health -=30
                            show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                    else:

                        if normal_crab:
                            $ crab_player_health -=7
                            show text "{color=#f00}{b}-7 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if strong_crab:
                            $ crab_player_health -=15
                            show text "{color=#f00}{b}-15 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if legend_crab:
                            $ crab_player_health -=30
                            show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player

                if randcrabattack ==2:
                    "the crab attacks and misses!"
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump guard_crab_battle_player
            else:

                $ randcrabattack = renpy.random.randint(1, 2)
                if randcrabattack ==1:
                    if crab_standin:
                        if normal_crab:
                            $ crab_standin_health -=14
                            show text "{color=#f00}{b}-14 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if strong_crab:
                            $ crab_standin_health -=30
                            show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if legend_crab:
                            $ crab_standin_health -=60
                            show text "{color=#f00}{b}-60 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                    else:
                        if normal_crab:
                            $ crab_player_health -=14
                            show text "{color=#f00}{b}-14 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if strong_crab:
                            $ crab_player_health -=30
                            show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player
                        if legend_crab:
                            $ crab_player_health -=60
                            show text "{color=#f00}{b}-60 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump guard_crab_battle_player

                if randcrabattack ==2:
                    "the crab attacks and misses!"
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump guard_crab_battle_player
        else:

            if bessie_crab:
                if crab_standin:
                    $ crab_standin_health -=20
                    show text "{color=#f00}{b}-20 ally crab health" at truecenter with dissolve
                    "the crab snips you!"
                    hide text with dissolve
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump guard_crab_battle_player
                else:
                    $ crab_player_health -=20
                    show text "{color=#f00}{b}-20 player health" at truecenter with dissolve
                    "the crab snips you!"
                    hide text with dissolve
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump guard_crab_battle_player

            $ randcrabattack = renpy.random.randint(1, 3)
            if randcrabattack ==1:
                if crab_standin:
                    if normal_crab:
                        $ crab_standin_health -=7
                        show text "{color=#f00}{b}-7 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump guard_crab_battle_player
                    if strong_crab:
                        $ crab_standin_health -=15
                        show text "{color=#f00}{b}-15 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump guard_crab_battle_player
                    if legend_crab:
                        $ crab_standin_health -=30
                        show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump guard_crab_battle_player
                else:

                    if normal_crab:
                        $ crab_player_health -=7
                        show text "{color=#f00}{b}-7 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump guard_crab_battle_player
                    if strong_crab:
                        $ crab_player_health -=15
                        show text "{color=#f00}{b}-15 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump guard_crab_battle_player
                    if legend_crab:
                        $ crab_player_health -=30
                        show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump guard_crab_battle_player


            if randcrabattack ==2:
                "the crab attacks and misses!"
                $ player_crab_def = False
                jump guard_crab_battle_player
            if randcrabattack ==3:
                "the crab's claws glow! it charges its attack!"
                $ crab_charge = True
                $ player_crab_def = False
                jump guard_crab_battle_player

label guard_crab_battle_next:

    if guard_crab ==1:
        show strongcrabshuffle with dissolve
        $ crab_health = 80
        $ normal_crab = False
        $ strong_crab = True
        $ legend_crab = False
        "you face a strong battling crab."
        jump guard_crab_battle_player
    if guard_crab ==2:
        show crabshuffle with dissolve
        $ crab_health = 50
        $ normal_crab = True
        $ strong_crab = False
        $ legend_crab = False
        "you face a normal battling crab."
        jump guard_crab_battle_player
    if guard_crab ==3:
        show crabshuffle with dissolve
        $ crab_health = 50
        $ normal_crab = True
        $ strong_crab = False
        $ legend_crab = False
        "you face a normal battling crab."
        jump guard_crab_battle_player
    if guard_crab ==4:
        show bessiecrabshuffle with dissolve
        $ crab_health = 160
        $ normal_crab = False
        $ strong_crab = False
        $ legend_crab = False
        $ bessie_crab = True
        fs1 "time for bessie, i think."
        fs1 "get on out there girl!"
        fs1 "she doesn't have a special attack, but she never misses!"
        jump guard_crab_battle_player

label guard_crab_battle_lose:
    $ normal_crab = True
    $ strong_crab = False
    $ legend_crab = False
    $ bessie_crab = False
    $ crab_standin = False
    $ crab_standin_normal = False
    $ crab_standin_strong = False
    $ crab_standin_legend = False
    $ hyperboom = False
    hide legendcrabshuffle
    hide strongcrabshuffle
    hide legendcrabshuffle
    hide bessiecrabshuffle
    with dissolve
    hide screen tourney_crabstats
    show fireguard_halberd with dissolve
    g "well played, mate."
    g "come back again when you beef up."
    $ crab_player_health = 100
    g "get some potions, buy more pockets, and try again!"
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg" fadein 2
    jump emberday

label guard_crab_win:
    $ crab_player_health = 100
    $ normal_crab = True
    $ strong_crab = False
    $ legend_crab = False
    $ crab_standin = False
    $ bessie_crab = False
    $ crab_standin_normal = False
    $ crab_standin_strong = False
    $ crab_standin_legend = False

    $ hyperboom = False
    hide screen tourney_crabstats
    show fireguard_halberd with dissolve
    g "well, you won fair and square."
    g "to congratulate you, i'm gonna to give you another pocket."
    $ crab_pockets +=1
    "you got an additional pocket!"
    g "and i'd like you to have bessie."
    $ crabs_caught +=1
    g "she'll never leave, even if you lose."
    g "she doesn't have a special attack, but her regular attack never misses."
    g "your next opponent is shady."
    g "dude has an unreasonable amount of pockets, so watch out for that."
    g "good luck."
    hide fireguard_halberd with dissolve
    $ shady_crab_start = True
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg" fadein 2
    jump emberday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
