label fish_crab_battle:
    $ fish_crab = 1
    $ remaining_enemy_crabs = 0
    show screen tourney_crabstats

    if fish_crab ==1:
        show stankcrabshuffle with dissolve
        $ crab_health = 500
        $ normal_crab = False
        $ strong_crab = False
        $ legend_crab = False
        mer "this is the best crab i've found!"
        "you face the stank!"
        $ stank_crab = True
        jump fish_crab_battle_player

label fish_crab_battle_player:


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
                jump fish_crab_battle_player2
            if crab_standin_strong:
                $ strong_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_strong = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump fish_crab_battle_player2
            if crab_standin_legend:
                $ legend_crabs -=1
                $ crabs_caught -=1
                $ crab_standin = False
                $ crab_standin_legend = False
                "your crab scuttles off!"
                yc "wait...."
                "he disappears, and it's your turn again."
                jump fish_crab_battle_player2
            if crab_standin_bessie:
                $ crab_standin = False
                $ crab_standin_bessie = False
                "bessie falls asleep to recover!"
                yc "wait...."
                "it's your turn again."
                $ crabs_caught -=1
                $ bessie_dead = True
                $ crab_standin_bessie = False
                jump fish_crab_battle_player2
            if crab_standin_musky:
                $ crab_standin = False
                $ crab_standin_musky = False
                "ol' musky falls asleep to recover!"
                yc "wait...."
                "it's your turn again."
                $ crabs_caught -=1
                $ musky_dead = True
                $ crab_standin_musky = False
                jump fish_crab_battle_player2
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
                    jump fish_crab_battle_crab
                if crab_standin_strong:
                    $ crab_health -=23
                    show text "{color=#f00}{b}-23 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump fish_crab_battle_crab
                if crab_standin_legend:
                    $ crab_health -= 45
                    show text "{color=#f00}{b}-45 enemy crab health" at truecenter with dissolve
                    "your crab hyper-boom snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump fish_crab_battle_crab
                if crab_standin_musky:
                    $ crab_health -= 80
                    show text "{color=#f00}{b}-80 enemy crab health" at truecenter with dissolve
                    "ol' musky rains fire-snips from hell on the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    $ hyperboom = 0
                    jump fish_crab_battle_crab
            else:
                if crab_player_health <=0:
                    "you lose!"
                    jump fish_crab_battle_lose
                else:
                    jump fish_crab_battle_player2


    if crab_player_health <=0:
        "you lose!"
        jump fish_crab_battle_lose
    else:
        jump fish_crab_battle_player2

label fish_crab_battle_player2:
    menu:
        "crab battle!" if not crab_standin:
            if crabs_caught >=1:
                if normal_crabs >=1:
                    "you send out a normal crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 50
                    $ crab_standin_normal = True
                    jump fish_crab_battle_player

                if strong_crabs >=1:
                    "you send out a strong crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 80
                    $ crab_standin_strong = True
                    jump fish_crab_battle_player

                if legend_crabs >=1:
                    "you send out a legendary crab!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 200
                    $ crab_standin_legend = True
                    jump fish_crab_battle_player

                if bessie and not bessie_dead:
                    "you send out bessie!"
                    "she takes your place in the battle!"
                    "she has no special attack, but never misses!"
                    $ crab_standin = True
                    $ crab_standin_health = 180
                    $ crab_standin_bessie = True
                    jump fish_crab_battle_player

                if olmusky and not musky_dead:
                    "you send out ol' musky!"
                    "it takes your place in the battle!"
                    $ crab_standin = True
                    $ crab_standin_health = 250
                    $ crab_standin_musky = True
                    jump fish_crab_battle_player
            else:
                "you don't have any crabs!"
                y "....normally a good thing, but whatever."
                jump fish_crab_battle_player


        "snip!" if crab_standin and not crab_standin_musky:
            if crab_standin_bessie:
                $ crab_health -=20
                show text "{color=#f00}{b}-20 enemy crab health" at truecenter with dissolve
                "bessie snips the enemy crab!"
                hide text with dissolve
                ya "take that!"
                jump fish_crab_battle_crab
            $ randcrabpunch = renpy.random.randint(1, 2)
            if crab_standin_normal:
                if randcrabpunch ==1:
                    $ crab_health -=7
                    show text "{color=#f00}{b}-7 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump fish_crab_battle_crab
            if crab_standin_strong:
                if randcrabpunch ==1:
                    $ crab_health -=15
                    show text "{color=#f00}{b}-15 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump fish_crab_battle_crab
            if crab_standin_legend:
                if randcrabpunch ==1:
                    $ crab_health -=30
                    show text "{color=#f00}{b}-30 enemy crab health" at truecenter with dissolve
                    "your crab snips the enemy crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if randcrabpunch ==2:
                    "your crab misses!"
                    jump fish_crab_battle_crab


        "hyper-boom snip - powerful, takes an extra turn, always hits" if crab_standin and not crab_standin_bessie and not crab_standin_musky:
            $ hyperboom = 1
            "your crab charges it's attack! it's glowing!"
            jump fish_crab_battle_crab

        "ol' musky super snip" if crab_standin_musky:
            $ hyperboom = 1
            "ol' musky charges it's attack! it's glowing!"
            jump fish_crab_battle_crab

        "punch" if not crab_standin:
            $ randcrabpunch = renpy.random.randint(1, 3)
            if randcrabpunch ==1:
                if crabs_killed ==0:
                    $ crab_health -=10
                    show text "{color=#f00}{b}-10 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==1:
                    $ crab_health -=12
                    show text "{color=#f00}{b}-12 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==2:
                    $ crab_health -=14
                    show text "{color=#f00}{b}-14 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==3:
                    $ crab_health -=16
                    show text "{color=#f00}{b}-16 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==4:
                    $ crab_health -=18
                    show text "{color=#f00}{b}-18 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==5:
                    $ crab_health -=20
                    show text "{color=#f00}{b}-20 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==6:
                    $ crab_health -=22
                    show text "{color=#f00}{b}-22 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==7:
                    $ crab_health -=24
                    show text "{color=#f00}{b}-24 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==8:
                    $ crab_health -=26
                    show text "{color=#f00}{b}-26 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==9:
                    $ crab_health -=28
                    show text "{color=#f00}{b}-28 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==10:
                    $ crab_health -=30
                    show text "{color=#f00}{b}-30 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==11:
                    $ crab_health -=32
                    show text "{color=#f00}{b}-32 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==12:
                    $ crab_health -=34
                    show text "{color=#f00}{b}-34 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==13:
                    $ crab_health -=36
                    show text "{color=#f00}{b}-36 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==14:
                    $ crab_health -=38
                    show text "{color=#f00}{b}-38 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==16:
                    $ crab_health -=40
                    show text "{color=#f00}{b}-40 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==16:
                    $ crab_health -=42
                    show text "{color=#f00}{b}-42 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==17:
                    $ crab_health -=44
                    show text "{color=#f00}{b}-44 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==18:
                    $ crab_health -=46
                    show text "{color=#f00}{b}-46 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==19:
                    $ crab_health -=48
                    show text "{color=#f00}{b}-48 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==20:
                    $ crab_health -=49
                    show text "{color=#f00}{b}-49 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==21:
                    $ crab_health -=50
                    show text "{color=#f00}{b}-50 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed >=22:
                    $ crab_health -=50
                    show text "{color=#f00}{b}-50 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab

            if randcrabpunch ==2:
                if crabs_killed ==0:
                    $ crab_health -=14
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-14 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==1:
                    $ crab_health -=19
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-19 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==2:
                    $ crab_health -=24
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-24 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==3:
                    $ crab_health -=27
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-27 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==4:
                    $ crab_health -=31
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-31 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==5:
                    $ crab_health -=34
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-34 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==6:
                    $ crab_health -=37
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-37 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==7:
                    $ crab_health -=40
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-40 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==8:
                    $ crab_health -=43
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-43 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==9:
                    $ crab_health -=46
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-46 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed ==10:
                    $ crab_health -=49
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-49 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
                if crabs_killed >=11:
                    $ crab_health -=54
                    show text "{color=#ffffff}{b}critical hit!":
                        xpos 450 ypos 300
                    show text "{color=#f00}{b}-54 crab health" at truecenter with dissolve
                    "you punch the crab!"
                    hide text with dissolve
                    ya "take that!"
                    jump fish_crab_battle_crab
            if randcrabpunch ==3:
                "you miss!"
                jump fish_crab_battle_crab
        "defend":

            $ player_crab_def = True
            "you defend!"
            jump fish_crab_battle_crab
        "try to catch":

            "you can't catch someone else's crabs!"
            yd "...if only that was true."
            jump fish_crab_battle_player
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
                            if crab_standin_musky:
                                $ crab_standin_health = 250
                            "ally crab health recovered!"
                            jump fish_crab_battle_player
                        else:

                            $ crab_potions -=1
                            $ crab_player_health = 100
                            "your health recovered!"
                            jump fish_crab_battle_player
                    "don't use potion":

                        jump fish_crab_battle_player
            else:
                "you don't have any potions left!"
                "buy more to use them!"
                jump fish_crab_battle_player

        "run away" if first_crab_battles:
            "you can't run from a trainer battle!"
            jump fish_crab_battle_player


label fish_crab_battle_crab:
    if crab_health <=0:
        hide crabshuffle
        hide strongcrabshuffle
        hide legendcrabshuffle
        hide bessiecrabshuffle
        hide muskycrabshuffle
        hide stankcrabshuffle
        with dissolve

        play sound "audio/win2.mp3"
        "you kicked that crab's ass!"

        if fish_crab ==1:
            $ stank = True
            "you win!"
            jump fish_crab_win
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
                        jump fish_crab_battle_player
                    else:
                        $ crab_player_health -=20
                        show text "{color=#f00}{b}-20 player health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump fish_crab_battle_player

                if musky_crab:
                    $ randcrabattack = renpy.random.randint(1, 3)
                    if randcrabattack ==1:
                        if crab_standin:
                            $ crab_standin_health -=40
                            show text "{color=#f00}{b}-40 ally crab health" at truecenter with dissolve
                            "ol 'musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        else:
                            $ crab_player_health -=40
                            show text "{color=#f00}{b}-40 player health" at truecenter with dissolve
                            "ol' musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                    if randcrabattack ==2:
                        if crab_standin:
                            $ crab_standin_health -=40
                            show text "{color=#f00}{b}-40 ally crab health" at truecenter with dissolve
                            "ol 'musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        else:
                            $ crab_player_health -=40
                            show text "{color=#f00}{b}-40 player health" at truecenter with dissolve
                            "ol' musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player

                    if randcrabattack ==3:
                        "ol' musky attacks and misses!"
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump fish_crab_battle_player

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
                            jump fish_crab_battle_player
                        if strong_crab:
                            $ crab_standin_health -=15
                            show text "{color=#f00}{b}-15 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if legend_crab:
                            $ crab_standin_health -=30
                            show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if stank_crab:
                            $ crab_standin_health -=60
                            show text "{color=#f00}{b}-60 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                    else:

                        if normal_crab:
                            $ crab_player_health -=7
                            show text "{color=#f00}{b}-7 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if strong_crab:
                            $ crab_player_health -=15
                            show text "{color=#f00}{b}-15 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if legend_crab:
                            $ crab_player_health -=30
                            show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if stank_crab:
                            $ crab_player_health -=60
                            show text "{color=#f00}{b}-60 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player

                if randcrabattack ==2:
                    if stank_crab:
                        "the stank attacks and misses!"
                    else:
                        "the crab attacks and misses!"
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump fish_crab_battle_player
            else:

                if musky_crab:
                    $ randcrabattack = renpy.random.randint(1, 3)
                    if randcrabattack ==1:
                        if crab_standin:
                            $ crab_standin_health -=80
                            show text "{color=#f00}{b}-80 ally crab health" at truecenter with dissolve
                            "ol' musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        else:
                            $ crab_player_health -=80
                            show text "{color=#f00}{b}-80 player health" at truecenter with dissolve
                            "ol' musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                    if randcrabattack ==2:
                        if crab_standin:
                            $ crab_standin_health -=80
                            show text "{color=#f00}{b}-80 ally crab health" at truecenter with dissolve
                            "ol' musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        else:
                            $ crab_player_health -=80
                            show text "{color=#f00}{b}-80 player health" at truecenter with dissolve
                            "ol' musky snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player

                    if randcrabattack ==3:
                        "ol' musky attacks and misses!"
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump fish_crab_battle_player

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
                            jump fish_crab_battle_player
                        if strong_crab:
                            $ crab_standin_health -=30
                            show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if legend_crab:
                            $ crab_standin_health -=60
                            show text "{color=#f00}{b}-60 ally crab health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if stank_crab:
                            $ crab_standin_health -=140
                            show text "{color=#f00}{b}-140 ally crab health" at truecenter with dissolve
                            "the stank wrecks your shit!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                    else:

                        if normal_crab:
                            $ crab_player_health -=14
                            show text "{color=#f00}{b}-14 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if strong_crab:
                            $ crab_player_health -=30
                            show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if legend_crab:
                            $ crab_player_health -=60
                            show text "{color=#f00}{b}-60 player health" at truecenter with dissolve
                            "the crab snips you!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player
                        if stank_crab:
                            $ crab_player_health -=140
                            show text "{color=#f00}{b}-140 player health" at truecenter with dissolve
                            "the stank wrecks your shit!"
                            hide text with dissolve
                            $ player_crab_def = False
                            $ crab_charge = False
                            jump fish_crab_battle_player

                if randcrabattack ==2:
                    if stank_crab:
                        "the stank attacks and misses!"
                    else:
                        "the crab attacks and misses!"
                    $ player_crab_def = False
                    $ crab_charge = False
                    jump fish_crab_battle_player
        else:



            if musky_crab:
                "ol' musky's claws glow! it charges its attack!"
                $ crab_charge = True
                $ player_crab_def = False
                jump fish_crab_battle_player

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
                        jump fish_crab_battle_player
                    if strong_crab:
                        $ crab_standin_health -=15
                        show text "{color=#f00}{b}-15 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump fish_crab_battle_player
                    if legend_crab:
                        $ crab_standin_health -=30
                        show text "{color=#f00}{b}-30 ally crab health" at truecenter with dissolve
                        "the crab snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump fish_crab_battle_player
                    if stank_crab:
                        $ crab_standin_health -=60
                        show text "{color=#f00}{b}-60 ally crab health" at truecenter with dissolve
                        "the stank snips you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        $ crab_charge = False
                        jump fish_crab_battle_player
                else:

                    if normal_crab:
                        $ crab_player_health -=7
                        show text "{color=#f00}{b}-7 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump fish_crab_battle_player
                    if strong_crab:
                        $ crab_player_health -=15
                        show text "{color=#f00}{b}-15 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump fish_crab_battle_player
                    if legend_crab:
                        $ crab_player_health -=30
                        show text "{color=#f00}{b}-30 player health" at truecenter with dissolve
                        "the crab hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump fish_crab_battle_player
                    if stank_crab:
                        $ crab_player_health -=60
                        show text "{color=#f00}{b}-60 player health" at truecenter with dissolve
                        "the stank hurts you!"
                        hide text with dissolve
                        $ player_crab_def = False
                        jump fish_crab_battle_player


            if randcrabattack ==2:
                if stank_crab:
                    "the stank attacks and misses!"
                else:
                    "the crab attacks and misses!"
                $ player_crab_def = False
                jump fish_crab_battle_player
            if randcrabattack ==3:
                if stank_crab:
                    "the stank's claws glow! it charges its attack!"
                else:
                    "the crab's claws glow! it charges its attack!"
                $ crab_charge = True
                $ player_crab_def = False
                jump fish_crab_battle_player

label fish_crab_battle_next:

    if fish_crab ==1:
        show stankcrabshuffle with dissolve
        $ crab_health = 500
        $ normal_crab = False
        $ strong_crab = False
        $ legend_crab = False
        $ bessie_crab = False
        $ musky_crab = False
        mer "time for the stank."
        "you face the stank!"
        $ stank_crab = True
        jump fish_crab_battle_player

label fish_crab_battle_lose:
    $ normal_crab = True
    $ strong_crab = False
    $ legend_crab = False
    $ musky_crab = False
    $ stank_crab = False
    $ crab_standin = False
    $ crab_standin_normal = False
    $ crab_standin_strong = False
    $ crab_standin_legend = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    $ crab_standin_stank = False
    $ hyperboom = False
    hide legendcrabshuffle
    hide strongcrabshuffle
    hide legendcrabshuffle
    hide muskycrabshuffle
    hide stankcrabshuffle
    with dissolve
    if bessie_dead:
        $ crabs_caught +=1
        $ bessie_dead = False
    if musky_dead:
        $ crabs_caught +=1
        $ musky_dead = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    hide screen tourney_crabstats
    mer "well played."
    mer "come back again when you get stronger."
    $ crab_player_health = 100
    mer "get some potions, buy more pockets, and try again!"
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg" fadein 2
    jump emberday

label fish_crab_win:
    $ crab_player_health = 100
    $ normal_crab = True
    $ strong_crab = False
    $ legend_crab = False
    $ musky_crab = False
    $ stank_crab = False
    $ crab_standin = False
    $ crab_standin_normal = False
    $ crab_standin_strong = False
    $ crab_standin_legend = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    $ crab_standin_stank = False
    $ hyperboom = False
    hide legendcrabshuffle
    hide strongcrabshuffle
    hide legendcrabshuffle
    hide muskycrabshuffle
    hide stankcrabshuffle
    with dissolve
    if bessie_dead:
        $ crabs_caught +=1
        $ bessie_dead = False
    if musky_dead:
        $ crabs_caught +=1
        $ musky_dead = False
    $ crab_standin_bessie = False
    $ crab_standin_musky = False
    hide screen tourney_crabstats

    ya "snick snack crab attack, bitch!"

    mer "well, you won fair and square."
    mer "to congratulate you, i'm gonna to give you another pocket."
    $ crab_pockets +=1
    "you got an additional pocket!"
    mer "and i'd like you to have the stank."
    $ crabs_caught +=1
    $ stank = True
    mer "he'll never leave, even if you lose."
    mer "he has an all-over powerful crab."
    mer "your next opponents are li and lo."
    mer "they've been around forever... and play together."
    mer "i'll return your boat to shady when you get back to shore."
    mer "good luck."
    $ fishtits_crab_start = False
    $ lal_crab_start = True
    stop music fadeout 2
    play music "audio/Bassa Island Game Loop.ogg" fadein 2
    jump emberday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
