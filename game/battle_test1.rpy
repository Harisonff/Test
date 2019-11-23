init:
    $ fight_azula = False
    $ fight_naga = False

    image bg_fight_azula = "images/battle/bg_fight_azula.jpg"
    image bg_fight_naga = "images/battle/bg_fight_naga.jpg"

image firewall:
    "battle/walloffire01.png"
    0.3
    "battle/walloffire02.png"
    0.3
    repeat

image white = Solid("#ffffff")

image ally1_bounce:
    "t_battle"
    xalign 0.15 yalign 0.1
    linear 0.3 xalign 0.25
    linear 0.3 xalign 0.15

image ally1_hurt:
    "t_battle"
    xalign 0.15 yalign 0.2
    linear 0.3 xalign 0.25
    linear 0.3 xalign 0.15

image player_bounce:
    "y_battle"
    xalign 0.3 yalign 0.35
    linear 0.3 xalign 0.4
    linear 0.3 xalign 0.3

image player_hurt:
    "y_battle"
    xalign 0.3 yalign 0.35
    linear 0.2 xalign 0.4
    linear 0.2 xalign 0.3

image ally2_bounce:
    "b_battle"
    xalign 0.15 yalign 0.67
    linear 0.3 xalign 0.25
    linear 0.3 xalign 0.15

image ally2_hurt:
    "b_battle"
    xalign 0.15 yalign 0.67
    linear 0.5 xalign 0.25
    linear 0.5 xalign 0.15

image top_enemy_hurt:
    "top_enemy"
    xalign 0.9 yalign 0.2
    linear 0.5 xalign 0.0
    linear 0.5 xalign 0.2

image top_enemy_bounce:
    "top_enemy"
    xalign 0.81 yalign 0.1
    linear 0.5 xalign 0.71
    linear 0.5 xalign 0.81

image mid_enemy_hurt:
    "mid_enemy"
    xalign 0.7 yalign 0.4
    linear 0.5 xalign 0.6
    linear 0.5 xalign 0.7

image mid_enemy_bounce:
    "mid_enemy"
    xalign 0.7 yalign 0.4
    linear 0.5 xalign 0.6
    linear 0.5 xalign 0.7

image bot_enemy_hurt:
    "bot_enemy"
    xalign 0.7 yalign 0.7
    linear 0.5 xalign 0.5
    linear 0.5 xalign 0.7

image bot_enemy_bounce:
    "bot_enemy"
    xalign 0.81 yalign 0.67
    linear 0.5 xalign 0.7
    linear 0.5 xalign 0.81

image battly_menu = "images/battle/Book2_hp_battle_allies.png"

image ally1_choose:
    "battle/ally1_select.png"
    0.1
    "battle/ally1_select_2.png"
    0.1
    "battle/ally1_select_3.png"
    0.1
    "battle/ally1_select_2.png"
    0.1
    repeat

image ally2_choose:
    "battle/ally2_select.png"
    0.1
    "battle/ally2_select_2.png"
    0.1
    "battle/ally2_select_3.png"
    0.1
    "battle/ally2_select_2.png"
    0.1
    repeat


image player_choose:
    "battle/player_select.png"
    0.1
    "battle/player_select_2.png"
    0.1
    "battle/player_select_3.png"
    0.1
    "battle/player_select_2.png"
    0.1
    repeat

image enemy1_choose:
    "battle/enemy1_hover.png"
    0.1
    "battle/enemy1_hover_2.png"
    0.1
    "battle/enemy1_hover_3.png"
    0.1
    "battle/enemy1_hover_2.png"
    0.1
    repeat

image enemy2_choose:
    "battle/enemy2_hover.png"
    0.1
    "battle/enemy2_hover_2.png"
    0.1
    "battle/enemy2_hover_3.png"
    0.1
    "battle/enemy2_hover_2.png"
    0.1
    repeat

image enemy3_choose:
    "battle/enemy3_hover.png"
    0.1
    "battle/enemy3_hover_2.png"
    0.1
    "battle/enemy3_hover_3.png"
    0.1
    "battle/enemy3_hover_2.png"
    0.1
    repeat

image top_enemy = "[randenemy1]"

image mid_enemy = "[randenemy2]"

image bot_enemy = "[randenemy3]"

image top_enemy_attack = ConditionSwitch(
    "top_enemy_attack1 == 'tank'", "battle/enemy_tank_attack.png",
    "top_enemy_attack1 == 'cavalry'", "battle/enemy_cavalry_attack.png",
    "top_enemy_attack1 == 'infantry'", "battle/enemy_infantry_attack.png",
    "top_enemy_attack1 == 'swamp'", "battle/infantry_swamp_2.png",
    )

image mid_enemy_attack = ConditionSwitch(
    "mid_enemy_attack1 == 'tank'", "battle/enemy_tank_attack.png",
    "mid_enemy_attack1 == 'cavalry'", "battle/enemy_cavalry_attack.png",
    "mid_enemy_attack1 == 'infantry'", "battle/enemy_infantry_attack.png",
    "mid_enemy_attack1 == 'swamp'", "battle/infantry_swamp_2.png",
    "mid_enemy_attack1 == 'azula'", "azu_attack",   
    "mid_enemy_attack1 == 'naga'", "naga_attack",   
    )

image bot_enemy_attack = ConditionSwitch(
    "bot_enemy_attack1 == 'tank'", "battle/enemy_tank_attack.png",
    "bot_enemy_attack1 == 'cavalry'", "battle/enemy_cavalry_attack.png",
    "bot_enemy_attack1 == 'infantry'", "battle/enemy_infantry_attack.png",
    "bot_enemy_attack1 == 'swamp'", "battle/infantry_swamp_2.png",
    )

image spirit_attack:
    "battle/swampmonster_attack_1.png"
    0.2
    "battle/swampmonster_attack_2.png"
    0.2
    "battle/swampmonster_attack_3.png"
    0.2
    repeat

image spirit_idle:
    "battle/swampmonster_idle_1.png"
    0.2
    "battle/swampmonster_idle_2.png"
    0.2
    "battle/swampmonster_idle_3.png"
    0.2
    "battle/swampmonster_idle_2.png"
    0.2
    repeat

image azu_attack:
    "battle/azfights/fa06.png"
    0.2
    "battle/azfights/fa06.png"
    0.2
    "battle/azfights/fa06.png"
    0.2
    repeat

image azu_idle:
    "battle/azfights/fa01.png"
    0.2
    "battle/azfights/fa02.png"
    0.2
    "battle/azfights/fa03.png"
    0.2
    "battle/azfights/fa02.png"
    0.2
    repeat

image naga_attack:
    "battle/nagafights/na05.png"
    0.2
    "battle/nagafights/na06.png"
    0.2

    repeat

image naga_idle:
    "battle/nagafights/na01.png"
    0.2
    "battle/nagafights/na02.png"
    0.2
    "battle/nagafights/na03.png"
    0.2
    "battle/nagafights/na02.png"
    0.2
    repeat

image t_battle = ConditionSwitch(
        "top_ally == 'tank'", "battle/fire_tank.png",
        "top_ally == 'infantry'", "battle/fire_infantry.png",
        "top_ally == 'cavalry'", "battle/fire_cavalry.png",
        "top_ally == 'none'", "transparent.png")

image t_battle_attack = ConditionSwitch(
        "top_ally == 'tank'", "battle/fire_tank_attack.png",
        "top_ally == 'infantry'", "battle/fire_infantry_attack.png",
        "top_ally == 'cavalry'", "battle/fire_cavalry_attack.png",
        "top_ally == 'none'", "transparent.png")

image y_battle = ConditionSwitch(
    "player_fight == 'normal'", "battle/aang/a_battle_small.png",
    "player_fight == 'swamp'", "battle/aang/mc_swampbattle_idle.png",
    )

image y_battle_attack = ConditionSwitch(
    "player_fight == 'normal'", "battle/aang/a_battle_small_attack.png",
    "player_fight == 'swamp'", "battle/aang/mc_swampbattle_attack.png",
    )

image b_battle = ConditionSwitch(
        "bot_ally == 'tank'", "battle/fire_tank.png",
        "bot_ally == 'infantry'", "battle/fire_infantry.png",
        "bot_ally == 'cavalry'", "battle/fire_cavalry.png",
        "bot_ally == 'azula'", "battle/azula_fights_idle.png",
        "bot_ally == 'none'", "transparent.png")

image b_battle_attack = ConditionSwitch(
        "bot_ally == 'tank'", "battle/fire_tank_attack.png",
        "bot_ally == 'infantry'", "battle/fire_infantry_attack.png",
        "bot_ally == 'cavalry'", "battle/fire_cavalry_attack.png",
        "bot_ally == 'azula'", "battle/azula_fights_attack.png",
        "bot_ally == 'none'", "transparent.png")

label fighttest:
    stop music
    play music "audio/Industrial Cinematic.mp3"



    $ player_alive = True















    $ blocking1 = False
    $ blocking2 = False
    $ blocking3 = False




    $ ally1_top = False
    $ ally1_mid = False
    $ ally1_bot = False
    $ player_top = False
    $ player_mid = False
    $ player_bot = False
    $ ally2_top = False
    $ ally2_mid = False
    $ ally2_bot = False
    $ player_hp = 1000
    $ ally1_hp = 0
    $ ally2_hp = 0
    if ally1_alive:
        $ ally1_hp = 500
        if f1equip == "health":
            $ ally1_hp = 800

    if ally2_alive:
        $ ally2_hp = 500
        if f2equip == "health":
            $ ally2_hp = 800



    hide screen day

label fighty1:

    if fight_azula:
        jump fight_azula_now
    if fight_naga:
        jump fight_naga_now

    if tentaclefight1:
        jump fighty2
    if tentaclefight2:
        jump fighty2

    if top_enemy_alive:
        if randenemy1 == "battle/enemy_tank.png":
            $ top_enemy_attack1 = "tank"
        elif randenemy1 == "battle/enemy_cavalry.png":
            $ top_enemy_attack1 = "cavalry"
        elif randenemy1 == "battle/enemy_infantry.png":
            $ top_enemy_attack1 = "infantry"
    else:

        jump fighty2

label fighty2:

    if tentaclefight1:
        scene bg_a_swamp_5
        $ ally1_hp = 0
        $ ally2_hp = 0
        $ mid_enemy_hp = 500
        $ mid_enemy_hp_max = 500
        $ randenemy2 = "spirit_idle"
        $ mid_enemy_alive = True
        $ mid_enemy = "spirit_idle"
        $ mid_enemy_attack = "spirit_attack"
        $ player_fight = "swamp"
        show mid_enemy at Position(xalign=0.8, yalign=0.4)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        show screen hp_bar_fire
        with Dissolve(0.5)
        jump fight_buttonstest_tent1

    if tentaclefight2:
        $ ally1_alive = False
        $ ally1_hp = 0
        $ ally2_hp = 1000
        $ ally2_hp_max = 1000
        $ ally2_alive = True
        $ top_enemy_hp = 1500
        $ top_enemy_hp_max = 1500
        $ top_enemy_alive = True
        $ randenemy1 = "battle/infantry_swamp_1.png"
        $ top_enemy_attack1 = "swamp"

        $ mid_enemy_hp = 1500
        $ mid_enemy_hp_max = 1500
        $ mid_enemy_alive = True
        $ randenemy2 = "battle/infantry_swamp_1.png"
        $ mid_enemy_attack1 = "swamp"

        $ bot_enemy_hp = 1500
        $ bot_enemy_hp_max = 1500
        $ bot_enemy_alive = True
        $ randenemy3 = "battle/infantry_swamp_1.png"
        $ bot_enemy_attack1 = "swamp"
        show top_enemy at Position(xalign=1.0, yalign=0)
        show mid_enemy at Position(xalign=1.0, yalign=0.4)
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        en1 "look here, boys."
        en1 "we got a straggler."
        y "no..."
        en2 "survived the last skirmish, eh?"
        y "i'm uh... just a little lost..."
        en1 "yeah. you are."
        en1 "kill him, boys."
        y "*sigh* i'm too tired to fight these guys."
        y "fuck."

        $ bot_ally = "azula"
        $ top_ally = "none"
        show b_battle at Position(xalign=0, yalign=0.77)
        with dissolve
        aa "i. am. fucking. pissed!"
        y "oh, hey."
        y "where... are your pants?"
        aa "you shut your fucking mouth before i put my fist in it and tear your world a-{b}fucking{/b}-sunder."
        y "whoa."
        aa "i don't know where my pants are."
        aa "i lost them getting anally raped by a tentacle spirit."
        aa "i have weird spirit cum dripping out of my asshole -"
        aa "and i. am. fucking. pissed!"
        ae "*deep breath*"
        a_ "let's go, earth boys!"
        a_ "azula is ready to melt some fucking faces."
        ae "watch and copy me, peasant!"
        aa "*screams*"
        play sound "audio/firewall.mp3"
        show firewall with Dissolve(1.0):
            xpos -100
            linear 1.8 xpos 800
        show flamespiral with dissolve
        hide flamespiral with dissolve
        aa "got it?"
        y "i... i think so."
        aa "then do it. keep them pinned."
        a_ "I'm going to beat the shit out of them."
        scene bg_a_swamp_5
        show top_enemy at Position(xalign=1.0, yalign=0)
        show mid_enemy at Position(xalign=1.0, yalign=0.4)
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        show b_battle at Position(xalign=0, yalign=0.77)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        show screen hp_bar_fire
        with Dissolve(0.5)
        jump fight_buttonstest_tent2

    if mid_enemy_alive:
        if randenemy2 == "battle/enemy_tank.png":
            $ mid_enemy_attack1 = "tank"
        elif randenemy2 == "battle/enemy_cavalry.png":
            $ mid_enemy_attack1 = "cavalry"
        elif randenemy2 == "battle/enemy_infantry.png":
            $ mid_enemy_attack1 = "infantry"
    else:
        jump fighty3

label fighty3:
    if bot_enemy_alive:
        if randenemy3 == "battle/enemy_tank.png":
            $ bot_enemy_attack1 = "tank"
        elif randenemy3 == "battle/enemy_cavalry.png":
            $ bot_enemy_attack1 = "cavalry"
        elif randenemy3 == "battle/enemy_infantry.png":
            $ bot_enemy_attack1 = "infantry"























    scene battle_background

    hide as_battle_small_01


    if top_enemy_alive:
        show top_enemy at Position(xalign=1.0, yalign=0)


    if mid_enemy_alive:
        show mid_enemy at Position(xalign=1.0, yalign=0.4)


    if bot_enemy_alive:
        show bot_enemy at Position(xalign=1.0, yalign=0.77)


    if ally1_alive:
        show t_battle at Position(xalign=0, yalign=0)


    show y_battle at Position(xalign=0.2, yalign=0.4)


    if ally2_alive:
        show b_battle at Position(xalign=0, yalign=0.77)





    if training_battle:
        show battly_menu with dissolve
        a "now this is what your fights will look like."
        show ctcblink
        $ renpy.pause()
        hide ctcblink
        a "this captured earth kingdom soldier will be your opponent."
        a "since you have no experience, little firebending, no allies, and no armor..."
        a "i'll start you out against lone, weak individuals like one."
        a "opponents are strong against some types and weak against others."
        a "Tanks are strong against cavalry, cavalry are strong against infantry, and infantry are strong against tanks."
        a "you personally have no special bonuses or weaknesses against any units."
        a "the fight order is: top ally, top enemy, you, middle enemy, bottom ally, bottom enemy."
        a "you can select your enemy directly, or you can choose \"attack\", and select your opponent by clicking their image or one of the numbers beside the attack button."
        a "selecting \"defend\" will automatically place your ally in defensive mode and the next turn commences."
        a "choosing \"item\" allows you to give the ally troop of your choice a potion to heal them."
        a "clicking \"item\" a second time before choosing your ally returns you to your options."
        a "the more you win, the harder the fights will become."
        a "sometimes there will be a specific arrangement of enemies you will have to fight."
        a "to win fights, you will need allies and armor, both of which can be purchased in the armory."
        a "you will also need to train your firebending in order to do more damage."
        a "any questions?"
        jump fight_questions

        label fight_questions:
            menu:
                "what are the strengths and weaknesses?":
                    a "Tanks are strong against cavalry, cavalry are strong against infantry, and infantry are strong against tanks."
                    a "you have no special bonuses or weaknesses."
                    jump fight_questions
                "what is the fight order?":
                    a "the fight order is: top ally, top enemy, you, middle enemy, bottom ally, bottom enemy."
                    jump fight_questions
                "how do i attack?":
                    a "when you choose \"attack\", you may select your opponent by clicking their image or one of the numbers beside the button."
                    jump fight_questions
                "how do i defend?":
                    a "selecting \"defend\" will automatically place your ally in defensive mode and the next turn commences."
                    jump fight_questions
                "how do i use an item?":
                    a "choosing \"item\" allows you to give the ally troop of your choice a potion to heal them."
                    a "clicking \"item\" before doing so returns you to your options."
                    jump fight_questions
                "how do i get stronger?":
                    a "to win fights, you will need allies and armor, both of which can be purchased in the armory."
                    a "you will also need to train your firebending in order to do more damage."
                    jump fight_questions
                "no more questions":
                    a "good, now fight!"
                    y "what?!"
                    y "i'm not ready for that!"
                    a "pick. him or me."
                    y "fuck."
                    hide battly_menu
                    $ training_battle = False
                    $ training_battle1 = True
                    $ top_enemy_hp = 0
                    $ top_enemy_hp_max = 500
                    $ mid_enemy_hp = 250
                    $ mid_enemy_hp_max = 500
                    $ bot_enemy_hp = 0
                    $ bot_enemy_hp_max = 500
                    jump fighttest



    show screen hp_bar_fire
    with Dissolve(0.5)








label fight_maintest:







    jump fight_buttonstest






label top_enemy_turn:
    hide screen_attack_options1
    hide fight_buttonstest
    if tentaclefight2:
        if top_enemy_alive:
            play sound "audio/earth.wav"
            $ randatt1 = renpy.random.choice(['player', 'ally2'])
            jump expression randatt1
        else:
            jump fight_buttonstest_tent2

    if top_enemy_alive:
        play sound "audio/earth.wav"

        if ally1_alive and player_alive and ally2_alive:
            $ randatt1 = renpy.random.choice(['ally1', 'player', 'ally2'])
            jump expression randatt1

        elif ally1_alive and player_alive:
            $ randatt1 = renpy.random.choice(['ally1', 'player'])
            jump expression randatt1

        elif ally1_alive and ally2_alive:
            $ randatt1 = renpy.random.choice(['ally1', 'ally2'])
            jump expression randatt1

        elif player_alive and ally2_alive:
            $ randatt1 = renpy.random.choice(['player', 'ally2'])
            jump expression randatt1

        elif ally1_alive:
            $ randatt1 = renpy.random.choice(['ally1'])
            jump expression randatt1

        elif player_alive:
            $ randatt1 = renpy.random.choice(['player'])
            jump expression randatt1

        elif ally2_alive:
            $ randatt1 = renpy.random.choice(['ally2'])
            jump expression randatt1
    else:

        jump fight_buttonstest1

label ally1:

    if blocking1:
        $ blocking1 = False
        jump moose_attack_guardtest1
    else:
        jump moose_attacktest_ally1

label player:

    if blocking2:
        $ blocking2 = False
        jump moose_attack_guardtest2
    else:
        jump moose_attacktest_player

label ally2:

    if blocking3:
        $ blocking3 = False
        jump moose_attack_guardtest3
    else:
        jump moose_attacktest_ally2

label mid_enemy_turn:
    if tentaclefight1:
        play sound "audio/whoosh.wav"
        $ randatt2 = renpy.random.choice(['player1'])
        jump expression randatt2
    if tentaclefight2:
        if mid_enemy_alive:
            play sound "audio/earth.wav"
            $ randatt2 = renpy.random.choice(['player1', 'ally21'])
            jump expression randatt2
        else:
            jump fight_buttonstest_tent3

    if mid_enemy_alive:
        play sound "audio/earth.wav"
        if ally1_alive and player_alive and ally2_alive:
            $ randatt2 = renpy.random.choice(['ally11', 'player1', 'ally21'])
            jump expression randatt2

        elif ally1_alive and player_alive:
            $ randatt2 = renpy.random.choice(['ally11', 'player1'])
            jump expression randatt2

        elif ally1_alive and ally2_alive:
            $ randatt2 = renpy.random.choice(['ally11', 'ally21'])
            jump expression randatt2

        elif player_alive and ally2_alive:
            $ randatt2 = renpy.random.choice(['player1', 'ally21'])
            jump expression randatt2

        elif ally1_alive:
            $ randatt2 = renpy.random.choice(['ally11'])
            jump expression randatt2

        elif player_alive:
            $ randatt2 = renpy.random.choice(['player1'])
            jump expression randatt2

        elif ally2_alive:
            $ randatt2 = renpy.random.choice(['ally21'])
            jump expression randatt2
    else:

        jump fight_buttonstest2

label ally11:
    if blocking1:
        $ blocking1 = False
        jump moose_attack_guardtest11
    else:
        jump moose_attacktest_ally11

label player1:
    if blocking2:
        $ blocking2 = False
        jump moose_attack_guardtest21
    else:
        jump moose_attacktest_player1

label ally21:
    if blocking3:
        $ blocking3 = False
        jump moose_attack_guardtest31
    else:
        jump moose_attacktest_ally21

label bot_enemy_turn:
    if tentaclefight2:
        if bot_enemy_alive:
            play sound "audio/earth.wav"
            $ randatt2 = renpy.random.choice(['player11', 'ally211'])
            jump expression randatt2
        else:
            jump top_enemy_turn

    if bot_enemy_alive:
        play sound "audio/earth.wav"

        if ally1_alive and player_alive and ally2_alive:
            $ randatt2 = renpy.random.choice(['ally111', 'player11', 'ally211'])
            jump expression randatt2

        elif ally1_alive and player_alive:
            $ randatt2 = renpy.random.choice(['ally111', 'player11'])
            jump expression randatt2

        elif ally1_alive and ally2_alive:
            $ randatt2 = renpy.random.choice(['ally111', 'ally211'])
            jump expression randatt2

        elif player_alive and ally2_alive:
            $ randatt2 = renpy.random.choice(['player11', 'ally211'])
            jump expression randatt2

        elif ally1_alive:
            $ randatt2 = renpy.random.choice(['ally111'])
            jump expression randatt2

        elif player_alive:
            $ randatt2 = renpy.random.choice(['player11'])
            jump expression randatt2

        elif ally2_alive:
            $ randatt2 = renpy.random.choice(['ally211'])
            jump expression randatt2
    else:

        jump fight_buttonstest

label ally111:
    if blocking1:
        $ blocking1 = False
        jump moose_attack_guardtest111
    else:
        jump moose_attacktest_ally111

label player11:
    if blocking2:
        $ blocking2 = False
        jump moose_attack_guardtest211
    else:
        jump moose_attacktest_player11

label ally211:
    if blocking3:
        $ blocking3 = False
        jump moose_attack_guardtest311
    else:
        jump moose_attacktest_ally211




label moose_attacktest_ally1:
    $ renpy.pause(0.08)
    hide top_enemy
    show top_enemy_attack at Position(xalign=1.0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide top_enemy_attack
    show top_enemy at Position(xalign=1.0, yalign=0)
    hide t_battle
    show t_battle at Position(xalign=0, yalign=0)
    with dissolve

    if top_ally == "tank" and randenemy1 == "battle/enemy_tank.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "tank" and randenemy1 == "battle/enemy_infantry.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "tank" and randenemy1 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "infantry" and randenemy1 == "battle/enemy_tank.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "infantry" and randenemy1 == "battle/enemy_infantry.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "infantry" and randenemy1 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "cavalry" and randenemy1 == "battle/enemy_tank.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "cavalry" and randenemy1 == "battle/enemy_infantry.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif top_ally == "cavalry" and randenemy1 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            hide ally1_hurt with Dissolve(0.2)
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1



label moose_attacktest_player:
    if tentaclefight2:
        $ renpy.pause(0.08)
        hide top_enemy
        show top_enemy_attack at Position(xalign=1.0, yalign=0)
        with dissolve
        $ renpy.pause(0.08)
        hide top_enemy_attack
        show top_enemy at Position(xalign=1.0, yalign=0)
        hide y_battle
        $ renpy.pause(0.08)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        with dissolve
        $ player_hp -=100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            dev "how did you even do this."
            dev "{size=+6}starting over."
            jump fighttest
        jump fight_buttonstest_tent2

    $ renpy.pause(0.08)
    hide top_enemy
    show top_enemy_attack at Position(xalign=1.0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide top_enemy_attack
    show top_enemy at Position(xalign=1.0, yalign=0)
    hide y_battle
    $ renpy.pause(0.08)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    with dissolve

    if farmor == 0:

        $ player_hp -= 175
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 1:

        $ player_hp -= 150
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 2:

        $ player_hp -= 100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 3:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:

            jump fight_buttonstest1

    elif farmor == 4:

        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1



label moose_attacktest_ally2:
    if tentaclefight2:
        $ renpy.pause(0.08)
        hide top_enemy
        show top_enemy_attack at Position(xalign=0.8, yalign=0.4)
        with dissolve
        $ renpy.pause(0.08)
        hide top_enemy_attack
        show top_enemy at Position(xalign=0.8, yalign=0.4)
        hide b_battle
        $ renpy.pause(0.08)
        show b_battle at Position(xalign=0, yalign=0.77)
        with Dissolve(0.2)
        $ ally2_hp -= 50
        if ally2_hp <= 0:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                dev "how did you lose this fight?"
                dev "it was fucking easy!"
                dev "alright, you know what? you get a freebie."
                dev "here we go."
                dev "don't fuck it up again!"
                jump fighttest
            else:
                jump fight_buttonstest_tent2


    $ renpy.pause(0.08)
    hide top_enemy
    show top_enemy_attack at Position(xalign=1.0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide top_enemy_attack
    show top_enemy at Position(xalign=1.0, yalign=0)
    hide b_battle
    $ renpy.pause(0.08)
    show b_battle at Position(xalign=0, yalign=0.77)
    with dissolve

    if bot_ally == "tank" and randenemy1 == "battle/enemy_tank.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "tank" and randenemy1 == "battle/enemy_infantry.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "tank" and randenemy1 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "infantry" and randenemy1 == "battle/enemy_tank.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "infantry" and randenemy1 == "battle/enemy_infantry.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "infantry" and randenemy1 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "cavalry" and randenemy1 == "battle/enemy_tank.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "cavalry" and randenemy1 == "battle/enemy_infantry.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif bot_ally == "cavalry" and randenemy1 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1




label moose_attacktest_ally11:
    $ renpy.pause(0.08)
    hide mid_enemy
    show mid_enemy_attack at Position(xalign=1.0, yalign=0.4)
    with dissolve
    $ renpy.pause(0.08)
    hide mid_enemy_attack
    show mid_enemy at Position(xalign=1.0, yalign=0.4)
    hide t_battle
    $ renpy.pause(0.08)
    show t_battle at Position(xalign=0, yalign=0)
    with Dissolve(0.2)


    if top_ally == "tank" and randenemy2 == "battle/enemy_tank.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "tank" and randenemy2 == "battle/enemy_infantry.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "tank" and randenemy2 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "infantry" and randenemy2 == "battle/enemy_tank.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "infantry" and randenemy2 == "battle/enemy_infantry.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "infantry" and randenemy2 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "cavalry" and randenemy2 == "battle/enemy_tank.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "cavalry" and randenemy2 == "battle/enemy_infantry.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif top_ally == "cavalry" and randenemy2 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2



label moose_attacktest_player1:
    if tentaclefight1:
        $ renpy.pause(0.08)
        $ mid_enemy = "spirit_idle"
        hide spirit_idle
        show spirit_attack at Position(xalign=0.8, yalign=0.4)
        with dissolve
        $ renpy.pause(0.08)
        hide spirit_attack
        show spirit_idle at Position(xalign=0.8, yalign=0.4)
        hide y_battle
        $ renpy.pause(0.08)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        with Dissolve(0.2)
        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                dev "how did you lose this fight?"
                dev "it was fucking easy!"
                dev "alright, you know what? you get a freebie."
                dev "here we go."
                dev "stop fucking it up."
                jump fighttest
            else:
                jump fight_buttonstest_tent1
        else:
            jump fight_buttonstest_tent1

    if tentaclefight2:
        $ renpy.pause(0.08)
        hide mid_enemy
        show mid_enemy_attack at Position(xalign=0.8, yalign=0.4)
        with dissolve
        $ renpy.pause(0.08)
        hide mid_enemy_attack
        show mid_enemy at Position(xalign=0.8, yalign=0.4)
        hide y_battle
        $ renpy.pause(0.08)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        with Dissolve(0.2)
        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                dev "how did you lose this fight?"
                dev "it was fucking easy!"
                dev "alright, you know what? you get a freebie."
                dev "here we go."
                dev "don't fuck it up again!"
                jump fighttest
            else:
                jump fight_buttonstest_tent3
        else:
            jump fight_buttonstest_tent3

    $ renpy.pause(0.08)
    hide mid_enemy
    show mid_enemy_attack at Position(xalign=1.0, yalign=0.4)

    $ renpy.pause(0.08)
    hide mid_enemy_attack
    show mid_enemy at Position(xalign=1.0, yalign=0.4)
    hide y_battle
    $ renpy.pause(0.08)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    with Dissolve(0.2)

    if farmor == 0:

        $ player_hp -= 175
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 1:

        $ player_hp -= 150
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 2:

        $ player_hp -= 100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 3:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 4:

        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2



label moose_attacktest_ally21:
    if tentaclefight2:
        $ renpy.pause(0.08)
        hide mid_enemy
        show mid_enemy_attack at Position(xalign=0.8, yalign=0.4)
        with dissolve
        $ renpy.pause(0.08)
        hide mid_enemy_attack
        show mid_enemy at Position(xalign=0.8, yalign=0.4)
        hide b_battle
        $ renpy.pause(0.08)
        show b_battle at Position(xalign=0, yalign=0.77)
        with Dissolve(0.2)
        $ ally2_hp -= 50
        if ally2_hp <= 0:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                dev "how did you lose this fight?"
                dev "it was fucking easy!"
                dev "alright, you know what? you get a freebie."
                dev "here we go."
                dev "don't fuck it up again!"
                jump fighttest
            else:
                jump fight_buttonstest_tent3
        else:
            jump fight_buttonstest_tent3

    $ renpy.pause(0.08)
    hide mid_enemy
    show mid_enemy_attack at Position(xalign=1.0, yalign=0.4)
    with dissolve
    $ renpy.pause(0.08)
    hide mid_enemy_attack
    show mid_enemy at Position(xalign=1.0, yalign=0.4)
    hide b_battle
    $ renpy.pause(0.08)
    show b_battle at Position(xalign=0, yalign=0.77)
    with Dissolve(0.2)


    if bot_ally == "tank" and randenemy2 == "battle/enemy_tank.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "tank" and randenemy2 == "battle/enemy_infantry.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "tank" and randenemy2 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "infantry" and randenemy2 == "battle/enemy_tank.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "infantry" and randenemy2 == "battle/enemy_infantry.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "infantry" and randenemy2 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "cavalry" and randenemy2 == "battle/enemy_tank.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "cavalry" and randenemy2 == "battle/enemy_infantry.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif bot_ally == "cavalry" and randenemy2 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2




label moose_attacktest_ally111:
    $ renpy.pause(0.08)
    hide bot_enemy
    show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide bot_enemy_attack
    show bot_enemy at Position(xalign=1.0, yalign=0.77)
    hide t_battle
    $ renpy.pause(0.08)
    show t_battle at Position(xalign=0, yalign=0)
    with Dissolve(0.2)

    if top_ally == "tank" and randenemy3 == "battle/enemy_tank.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "tank" and randenemy3 == "battle/enemy_infantry.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "tank" and randenemy3 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "infantry" and randenemy3 == "battle/enemy_tank.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "infantry" and randenemy3 == "battle/enemy_infantry.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "infantry" and randenemy3 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "cavalry" and randenemy3 == "battle/enemy_tank.png":

        $ ally1_hp -= 200
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "cavalry" and randenemy3 == "battle/enemy_infantry.png":

        $ ally1_hp -= 50
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif top_ally == "cavalry" and randenemy3 == "battle/enemy_cavalry.png":

        $ ally1_hp -= 100
        if ally1_hp < 50:
            $ ally1_hp = 0
            hide t_battle with dissolve
            $ ally1_alive = False
            if not ally1_alive:
                if not player_alive:
                    if not ally2_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest



label moose_attacktest_player11:
    if tentaclefight2:
        $ renpy.pause(0.08)
        hide bot_enemy
        show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
        with dissolve
        $ renpy.pause(0.08)
        hide bot_enemy_attack
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        hide y_battle
        $ renpy.pause(0.08)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        with Dissolve(0.2)
        $ player_hp -= 100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        dev "....how?"
                        jump fighttest
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn
        else:
            jump top_enemy_turn



    $ renpy.pause(0.08)
    hide bot_enemy
    show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide bot_enemy_attack
    show bot_enemy at Position(xalign=1.0, yalign=0.77)
    hide y_battle
    $ renpy.pause(0.08)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    with Dissolve(0.2)

    if farmor == 0:

        $ player_hp -= 175
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 1:

        $ player_hp -= 150
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 2:

        $ player_hp -= 100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 3:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 4:

        $ player_hp -= 50
        if player_hp <0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest



label moose_attacktest_ally211:
    if tentaclefight2:
        $ renpy.pause(0.08)
        hide bot_enemy
        show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
        with dissolve
        $ renpy.pause(0.08)
        hide bot_enemy_attack
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        hide b_battle
        $ renpy.pause(0.08)
        show b_battle at Position(xalign=0, yalign=0.77)
        with Dissolve(0.2)
        $ ally2_hp -= 100
        if ally2_hp <= 0:
            $ ally2_hp = 0
            hide b_battle with dissolve
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        dev "....how?"
                        jump fighttest
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn
        else:
            jump top_enemy_turn

    $ renpy.pause(0.08)
    hide bot_enemy
    show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide bot_enemy_attack
    show bot_enemy at Position(xalign=1.0, yalign=0.77)
    hide b_battle
    $ renpy.pause(0.08)
    show b_battle at Position(xalign=0, yalign=0.77)
    with Dissolve(0.2)

    if bot_ally == "tank" and randenemy3 == "battle/enemy_tank.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "tank" and randenemy3 == "battle/enemy_infantry.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "tank" and randenemy3 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "infantry" and randenemy3 == "battle/enemy_tank.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "infantry" and randenemy3 == "battle/enemy_infantry.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "infantry" and randenemy3 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "cavalry" and randenemy3 == "battle/enemy_tank.png":

        $ ally2_hp -= 200
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "cavalry" and randenemy3 == "battle/enemy_infantry.png":

        $ ally2_hp -= 50
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif bot_ally == "cavalry" and randenemy3 == "battle/enemy_cavalry.png":

        $ ally2_hp -= 100
        if ally2_hp < 50:
            $ ally2_hp = 0
            hide b_battle with dissolve
            $ ally2_alive = False
            if not ally2_alive:
                if not ally1_alive:
                    if not player_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest







label moose_attack_guardtest1:
    $ renpy.pause(0.08)
    hide top_enemy
    show top_enemy_attack at Position(xalign=1.0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide top_enemy_attack
    show top_enemy at Position(xalign=1.0, yalign=0)
    hide t_battle
    $ renpy.pause(0.08)
    show t_battle at Position(xalign=0, yalign=0)
    with dissolve

    $ ally1_hp -= 50
    if ally1_hp < 50:
        $ ally1_hp = 0
        hide t_battle with dissolve
        $ ally1_alive = False
        if not ally1_alive:
            if not player_alive:
                if not ally2_alive:
                    jump avatar_losttest
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1
    else:
        jump fight_buttonstest1



























































































































































































label moose_attack_guardtest2:
    $ renpy.pause(0.08)
    hide top_enemy
    show top_enemy_attack at Position(xalign=1.0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide top_enemy_attack
    show top_enemy at Position(xalign=1.0, yalign=0)
    hide y_battle
    $ renpy.pause(0.08)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    with dissolve

    if farmor == 0:

        $ player_hp -= 100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 1:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 2:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 3:

        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1

    elif farmor == 4:

        $ player_hp -= 0
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest1
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1



label moose_attack_guardtest3:
    $ renpy.pause(0.08)
    hide top_enemy
    show top_enemy_attack at Position(xalign=1.0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide top_enemy_attack
    show top_enemy at Position(xalign=1.0, yalign=0)
    hide b_battle
    $ renpy.pause(0.08)
    show b_battle at Position(xalign=0, yalign=0)
    with dissolve

    $ ally2_hp -= 50
    if ally2_hp < 50:
        $ ally2_hp = 0
        hide b_battle with dissolve
        $ ally2_alive = False
        if not ally2_alive:
            if not ally1_alive:
                if not player_alive:
                    jump avatar_losttest
                else:
                    jump fight_buttonstest1
            else:
                jump fight_buttonstest1
        else:
            jump fight_buttonstest1
    else:
        jump fight_buttonstest1


























































































































































































label moose_attack_guardtest11:
    $ renpy.pause(0.08)
    hide mid_enemy
    show mid_enemy_attack at Position(xalign=1.0, yalign=0.4)
    with dissolve
    $ renpy.pause(0.08)
    hide mid_enemy_attack
    show mid_enemy at Position(xalign=1.0, yalign=0.4)
    hide t_battle
    $ renpy.pause(0.08)
    show t_battle at Position(xalign=0, yalign=0)
    with Dissolve(0.2)

    $ ally1_hp -= 50
    if ally1_hp < 50:
        $ ally1_hp = 0
        hide t_battle with dissolve
        $ ally1_alive = False
        if not ally1_alive:
            if not player_alive:
                if not ally2_alive:
                    jump avatar_losttest
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2
    else:
        jump fight_buttonstest2

























































































































































































label moose_attack_guardtest21:
    if tentaclefight1:
        $ renpy.pause(0.08)
        hide mid_enemy
        show spirit_attack at Position(xalign=0.8, yalign=0.4)
        with dissolve
        $ renpy.pause(0.08)
        hide spirit_attack
        show spirit_idle at Position(xalign=0.8, yalign=0.4)
        hide y_battle
        $ renpy.pause(0.08)
        show y_battle at Position(xalign=0.2, yalign=0.4)
        with Dissolve(0.2)
        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            dev "how did you even lose?"
            dev "fine, here do it again."
            dev "don't fuck it up!"
            jump fighttest
        else:
            jump fight_buttonstest_tent1


    $ renpy.pause(0.08)
    hide mid_enemy
    show mid_enemy_attack at Position(xalign=1.0, yalign=0.4)
    with dissolve
    $ renpy.pause(0.08)
    hide mid_enemy_attack
    show mid_enemy at Position(xalign=1.0, yalign=0.4)
    hide y_battle
    $ renpy.pause(0.08)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    with Dissolve(0.2)

    if farmor == 0:

        $ player_hp -= 100
        if player_hp <=0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 1:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 2:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 3:

        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2

    elif farmor == 4:

        $ player_hp -= 0
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest2
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2



label moose_attack_guardtest31:
    $ renpy.pause(0.08)
    hide mid_enemy
    show mid_enemy_attack at Position(xalign=1.0, yalign=0.4)
    with dissolve
    $ renpy.pause(0.08)
    hide mid_enemy_attack
    show mid_enemy at Position(xalign=1.0, yalign=0.4)
    hide b_battle
    $ renpy.pause(0.08)
    show b_battle at Position(xalign=0, yalign=0.77)
    with Dissolve(0.2)

    $ ally2_hp -= 50
    if ally2_hp < 50:
        $ ally2_hp = 0
        hide b_battle with dissolve
        $ ally2_alive = False
        if not ally2_alive:
            if not ally1_alive:
                if not player_alive:
                    jump avatar_losttest
                else:
                    jump fight_buttonstest2
            else:
                jump fight_buttonstest2
        else:
            jump fight_buttonstest2
    else:
        jump fight_buttonstest2


























































































































































































label moose_attack_guardtest111:
    $ renpy.pause(0.08)
    hide bot_enemy
    show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide bot_enemy_attack
    show bot_enemy at Position(xalign=1.0, yalign=0.77)
    hide t_battle
    $ renpy.pause(0.08)
    show t_battle at Position(xalign=0, yalign=0)
    with Dissolve(0.2)

    $ ally1_hp -= 50
    if ally1_hp < 50:
        $ ally1_hp = 0
        hide t_battle with dissolve
        $ ally1_alive = False
        if not ally1_alive:
            if not player_alive:
                if not ally2_alive:
                    jump avatar_losttest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest
    else:
        jump fight_buttonstest


























































































































































































label moose_attack_guardtest211:
    $ renpy.pause(0.08)
    hide bot_enemy
    show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide bot_enemy_attack
    show bot_enemy at Position(xalign=1.0, yalign=0.77)
    hide y_battle
    $ renpy.pause(0.08)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    with Dissolve(0.2)

    if farmor == 0:

        $ player_hp -= 100
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 1:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 2:

        $ player_hp -= 75
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 3:

        $ player_hp -= 50
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest

    elif farmor == 4:

        $ player_hp -= 0
        if player_hp <= 0:
            $ player_hp = 0
            hide y_battle with dissolve
            $ player_alive = False
            if not player_alive:
                if not ally2_alive:
                    if not ally1_alive:
                        jump avatar_losttest
                    else:
                        jump fight_buttonstest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest



label moose_attack_guardtest311:
    $ renpy.pause(0.08)
    hide bot_enemy
    show bot_enemy_attack at Position(xalign=1.0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide bot_enemy_attack
    show bot_enemy at Position(xalign=1.0, yalign=0.77)
    hide b_battle
    $ renpy.pause(0.08)
    show b_battle at Position(xalign=0, yalign=0.77)
    with Dissolve(0.2)

    $ ally2_hp -= 50
    if ally2_hp < 50:
        $ ally2_hp = 0
        hide b_battle with dissolve
        $ ally2_alive = False
        if not ally2_alive:
            if not ally1_alive:
                if not player_alive:
                    jump avatar_losttest
                else:
                    jump fight_buttonstest
            else:
                jump fight_buttonstest
        else:
            jump fight_buttonstest
    else:
        jump fight_buttonstest

























































































































































































label ally1_attacktest:
    play sound "audio/air.wav"
    $ renpy.pause(0.08)
    hide t_battle
    show t_battle_attack at Position(xalign=0, yalign=0)
    with dissolve
    $ renpy.pause(0.08)
    hide fight_buttonstest
    hide t_battle_attack
    show t_battle at Position(xalign=0, yalign=0)

    if ally1_top:
        $ ally1_top = False
        hide top_enemy with Dissolve(0.2)
        show top_enemy at Position(xalign=1.0, yalign=0)
        with Dissolve(0.2)

        if top_ally == "tank" and randenemy1 == "battle/enemy_tank.png":

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "tank" and randenemy1 == "battle/enemy_infantry.png":

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "tank" and randenemy1 == "battle/enemy_cavalry.png":

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "infantry" and randenemy1 == "battle/enemy_tank.png":

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "infantry" and randenemy1 == "battle/enemy_infantry.png":

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "infantry" and randenemy1 == "battle/enemy_cavalry.png":

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "cavalry" and randenemy1 == "battle/enemy_tank.png":

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "cavalry" and randenemy1 == "battle/enemy_infantry.png":

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "cavalry" and randenemy1 == "battle/enemy_cavalry.png":

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

    if ally1_mid:
        hide mid_enemy
        with Dissolve(0.2)
        show mid_enemy at Position(xalign=1.0, yalign=0.4)
        with Dissolve(0.2)
        $ ally1_mid = False
        if top_ally == "tank" and randenemy2 == "battle/enemy_tank.png":

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "tank" and randenemy2 == "battle/enemy_infantry.png":

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "tank" and randenemy2 == "battle/enemy_cavalry.png":

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "infantry" and randenemy2 == "battle/enemy_tank.png":

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "infantry" and randenemy2 == "battle/enemy_infantry.png":

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "infantry" and randenemy2 == "battle/enemy_cavalry.png":

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "cavalry" and randenemy2 == "battle/enemy_tank.png":

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "cavalry" and randenemy2 == "battle/enemy_infantry.png":

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "cavalry" and randenemy2 == "battle/enemy_cavalry.png":

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


    if ally1_bot:
        $ ally1_bot = False
        hide bot_enemy
        with Dissolve(0.2)
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        with Dissolve(0.2)
        if top_ally == "tank" and randenemy3 == "battle/enemy_tank.png":

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


        elif top_ally == "tank" and randenemy3 == "battle/enemy_infantry.png":

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "tank" and randenemy3 == "battle/enemy_cavalry.png":

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "infantry" and randenemy3 == "battle/enemy_tank.png":

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "infantry" and randenemy3 == "battle/enemy_infantry.png":

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "infantry" and randenemy3 == "battle/enemy_cavalry.png":

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "cavalry" and randenemy3 == "battle/enemy_tank.png":

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "cavalry" and randenemy3 == "battle/enemy_infantry.png":

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn

        elif top_ally == "cavalry" and randenemy3 == "battle/enemy_cavalry.png":

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump top_enemy_turn
                    else:
                        jump top_enemy_turn
                else:
                    jump top_enemy_turn
            else:
                jump top_enemy_turn


label player_attacktest:
    if tentaclefight1:
        play sound "audio/air.wav"
        $ renpy.pause(0.08)
        hide y_battle
        show y_battle_attack at Position(xalign=0.2, yalign=0.4)
        with dissolve
        $ renpy.pause(0.08)
        hide fight_buttonstest
        hide y_battle_attack
        show y_battle at Position(xalign=0.2, yalign=0.4)
        $ player_mid = False
        hide spirit_idle
        hide mid_enemy
        with Dissolve(0.2)
        show spirit_idle at Position(xalign=0.8, yalign=0.4)
        with Dissolve(0.2)
        $ mid_enemy_hp -= 150
        if mid_enemy_hp < 50:
            $ mid_enemy_hp = 0
            $ mid_enemy_alive = False
            jump tentaclefight1_won
        else:
            jump mid_enemy_turn

    play sound "audio/air.wav"
    $ renpy.pause(0.08)
    hide y_battle
    show y_battle_attack at Position(xalign=0.2, yalign=0.4)
    with dissolve
    $ renpy.pause(0.08)
    hide fight_buttonstest
    hide y_battle_attack
    show y_battle at Position(xalign=0.2, yalign=0.4)

    if player_top:
        $ player_top = False
        hide top_enemy
        with Dissolve(0.2)
        show top_enemy at Position(xalign=1.0, yalign=0)
        with Dissolve(0.2)
        if firebending <=3:

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=4 and firebending <=6:

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=7 and firebending <=9:

            $ top_enemy_hp -= 150
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=10:

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

    if player_mid:
        $ player_mid = False
        hide mid_enemy
        with Dissolve(0.2)
        show mid_enemy at Position(xalign=1.0, yalign=0.4)
        with Dissolve(0.2)
        if firebending <=3:

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=4 and firebending <=6:

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=7 and firebending <=9:

            $ mid_enemy_hp -= 150
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=10:

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

    if player_bot:
        $ player_bot = False
        hide bot_enemy
        with Dissolve(0.2)
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        with Dissolve(0.2)
        if firebending <=3:

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=4 and firebending <=6:

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=7 and firebending <=9:

            $ bot_enemy_hp -= 150
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn

        elif firebending >=10:

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump mid_enemy_turn
                    else:
                        jump mid_enemy_turn
                else:
                    jump mid_enemy_turn
            else:
                jump mid_enemy_turn


label ally2_attacktest:
    if tentaclefight2:
        play sound "audio/air.wav"
        $ renpy.pause(0.08)
        hide b_battle
        show b_battle_attack at Position(xalign=0, yalign=0.77)
        with dissolve
        $ renpy.pause(0.08)
        hide fight_buttonstest
        hide b_battle_attack
        show b_battle at Position(xalign=0, yalign=0.77)
        if ally2_top:
            $ ally2_top = False
            hide top_enemy
            with Dissolve(0.2)
            show top_enemy at Position(xalign=1.0, yalign=0)
            with Dissolve(0.2)
            $ top_enemy_hp -= 300
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump tentaclefight2_won
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        if ally2_mid:
            $ ally2_mid = False
            hide mid_enemy
            with Dissolve(0.2)
            show mid_enemy at Position(xalign=1.0, yalign=0.4)
            with Dissolve(0.2)
            $ mid_enemy_hp -= 300
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        if ally2_bot:
            $ ally2_bot = False
            hide bot_enemy
            with Dissolve(0.2)
            show bot_enemy at Position(xalign=1.0, yalign=0.77)
            with Dissolve(0.2)
            $ bot_enemy_hp -= 300
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

    play sound "audio/air.wav"
    $ renpy.pause(0.08)
    hide b_battle
    show b_battle_attack at Position(xalign=0, yalign=0.77)
    with dissolve
    $ renpy.pause(0.08)
    hide fight_buttonstest
    hide b_battle_attack
    show b_battle at Position(xalign=0, yalign=0.77)

    if ally2_top:
        $ ally2_top = False
        hide top_enemy
        with Dissolve(0.2)
        show top_enemy at Position(xalign=1.0, yalign=0)
        with Dissolve(0.2)

        if bot_ally == "tank" and randenemy1 == "battle/enemy_tank.png":

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "tank" and randenemy1 == "battle/enemy_infantry.png":

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "tank" and randenemy1 == "battle/enemy_cavalry.png":

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy1 == "battle/enemy_tank.png":

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy1 == "battle/enemy_infantry.png":

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy1 == "battle/enemy_cavalry.png":

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy1 == "battle/enemy_tank.png":

            $ top_enemy_hp -= 50
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy1 == "battle/enemy_infantry.png":

            $ top_enemy_hp -= 200
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy1 == "battle/enemy_cavalry.png":

            $ top_enemy_hp -= 100
            if top_enemy_hp < 50:
                $ top_enemy_hp = 0
                hide top_enemy with dissolve
                $ top_enemy_alive = False
                if not top_enemy_alive:
                    if not mid_enemy_alive:
                        if not bot_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

    if ally2_mid:
        $ ally2_mid = False
        hide mid_enemy
        with Dissolve(0.2)
        show mid_enemy at Position(xalign=1.0, yalign=0.4)
        with Dissolve(0.2)
        if bot_ally == "tank" and randenemy2 == "battle/enemy_tank.png":

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "tank" and randenemy2 == "battle/enemy_infantry.png":

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "tank" and randenemy2 == "battle/enemy_cavalry.png":

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy2 == "battle/enemy_tank.png":

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy2 == "battle/enemy_infantry.png":

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy2 == "battle/enemy_cavalry.png":

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy2 == "battle/enemy_tank.png":

            $ mid_enemy_hp -= 50
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy2 == "battle/enemy_infantry.png":

            $ mid_enemy_hp -= 200
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy2 == "battle/enemy_cavalry.png":

            $ mid_enemy_hp -= 100
            if mid_enemy_hp < 50:
                $ mid_enemy_hp = 0
                hide mid_enemy with dissolve
                $ mid_enemy_alive = False
                if not mid_enemy_alive:
                    if not bot_enemy_alive:
                        if not top_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

    if ally2_bot:
        $ ally2_bot = False
        hide bot_enemy
        with Dissolve(0.2)
        show bot_enemy at Position(xalign=1.0, yalign=0.77)
        with Dissolve(0.2)
        if bot_ally == "tank" and randenemy3 == "battle/enemy_tank.png":

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "tank" and randenemy3 == "battle/enemy_infantry.png":

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "tank" and randenemy3 == "battle/enemy_cavalry.png":

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy3 == "battle/enemy_tank.png":

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy3 == "battle/enemy_infantry.png":

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "infantry" and randenemy3 == "battle/enemy_cavalry.png":

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy3 == "battle/enemy_tank.png":

            $ bot_enemy_hp -= 50
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy3 == "battle/enemy_infantry.png":

            $ bot_enemy_hp -= 200
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn

        elif bot_ally == "cavalry" and randenemy3 == "battle/enemy_cavalry.png":

            $ bot_enemy_hp -= 100
            if bot_enemy_hp < 50:
                $ bot_enemy_hp = 0
                hide bot_enemy with dissolve
                $ bot_enemy_alive = False
                if not bot_enemy_alive:
                    if not top_enemy_alive:
                        if not mid_enemy_alive:
                            jump moose_losttest
                        else:
                            jump bot_enemy_turn
                    else:
                        jump bot_enemy_turn
                else:
                    jump bot_enemy_turn
            else:
                jump bot_enemy_turn



label potiontest:
    show a_battle_small_01_heal at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with dissolve
    $ potions -=1
    $ player_hp += 300
    if player_hp >= 1000:
        $ player_hp = 1000
    hide a_battle_small_01_heal with dissolve
    jump top_enemy_turn






label ally1_att:
    hide screen_attack_options1
    hide fight_buttonstest
    hide screen_attack_options2
    hide fight_buttonstest1
    hide screen_attack_options3
    hide fight_buttonstest2
    $ blocking1 = False
    jump ally1_attacktest

label player_att:
    hide screen_attack_options1
    hide fight_buttonstest
    hide screen_attack_options2
    hide fight_buttonstest1
    hide screen_attack_options3
    hide fight_buttonstest2
    $ blocking2 = False
    jump player_attacktest

label ally2_att:
    hide screen_attack_options1
    hide fight_buttonstest
    hide screen_attack_options2
    hide fight_buttonstest1
    hide screen_attack_options3
    hide fight_buttonstest2
    $ blocking3 = False
    jump ally2_attacktest

label main_potiontest:
    if potions >= 1:
        jump potiontest1
    else:
        show potion_idle
        "no potions!"
        hide potion_idle
        jump fight_buttonstest1

label main_potiontest1:
    if potions >= 1:
        jump potiontest2
    else:
        show potion_idle
        "no potions!"
        hide potion_idle
        jump fight_buttonstest

label main_potiontest2:
    if potions >= 1:
        jump potiontest3
    else:
        show potion_idle
        "no potions!"
        hide potion_idle
        jump fight_buttonstest2






init -1:



    screen hp_bar_fire:
        add "battle/Book2_hp_battle_allies.png"
        text "{color=#000000}[player_hp]/1000{/color}" xpos 280 ypos 645
        if ally1_alive:
            text "{color=#000000}[ally1_hp]/500{/color}" xpos 260 ypos 607
        if ally2_alive:
            text "{color=#000000}[ally2_hp]/500{/color}" xpos 260 ypos 682
        if top_enemy_alive:
            add "battle/Book2_hpbar1.png" xpos 520 ypos 50
            text "{color=#ffffff}[top_enemy_hp]/[top_enemy_hp_max]{/color}" xpos 530 ypos 50
        if mid_enemy_alive:
            add "battle/Book2_hpbar1.png" xpos 490 ypos 200
            text "{color=#ffffff}[mid_enemy_hp]/[mid_enemy_hp_max]{/color}" xpos 500 ypos 200
        if bot_enemy_alive:
            add "battle/Book2_hpbar1.png" xpos 520 ypos 350
            text "{color=#ffffff}[bot_enemy_hp]/[bot_enemy_hp_max]{/color}" xpos 530 ypos 350






screen screen_enemy1_glowball:
    add 'enemy1_choose'
screen screen_enemy2_glowball:
    add 'enemy2_choose'
screen screen_enemy3_glowball:
    add 'enemy3_choose'

screen screen_ally1_glowball:
    add 'ally1_choose'
screen screen_player_glowball:
    add 'player_choose'
screen screen_ally2_glowball:
    add 'ally2_choose'

screen screen_firewall_selected:
    add "battle/androi_sml_atck_butns_on.png"



label fight_buttonstest:
    if ally1_alive:
        if auto_battle:
            jump auto_battle_ally1

        call screen fight_buttonstest
    else:

        jump top_enemy_turn


    screen fight_buttonstest:
        add "battle/androi_ally1_select.png"

        imagemap:

            ground "battle/androi_main_butns_off.png"
            hover "battle/androi_main_butns_on.png"
            idle "battle/androi_main_butns_trnsp.png"

            hotspot (520,580,120,130) action [Jump("screen_attack_options1")]
            hotspot (650,580,120,130) action [SetVariable("blocking1", True), Jump("top_enemy_turn")]
            hotspot (780,580,120,130) action [Jump("main_potiontest1")]





            if top_enemy_alive:
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("ally1_top", True), Jump("ally1_att")]

            if mid_enemy_alive:
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("ally1_mid", True), Jump("ally1_att")]

            if bot_enemy_alive:
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("ally1_bot", True), Jump("ally1_att")]


            if not auto_battle:
                textbutton "auto" xpos 0.9 ypos 0.78:
                    action [SetVariable("auto_battle", True), Jump("auto_battle_ally1")]

            if auto_battle:
                textbutton "auto off" xpos 0.88 ypos 0.78:
                    action [SetVariable("auto_battle", False), Jump("fight_buttonstest")]

label auto_battle_ally1:
    if top_enemy_alive:
        $ ally1_top = True
        jump ally1_att
    if mid_enemy_alive:
        $ ally1_mid = True
        jump ally1_att
    if bot_enemy_alive:
        $ ally1_bot = True
        jump ally1_att



label screen_attack_options1:
    call screen screen_attack_options1



    screen screen_attack_options1:

        add "battle/androi_ally1_select.png"
        add "battle/Book2_hp_battle_allies.png"

        imagemap:

            ground "battle/androi_sml_atck_butns_off.png"
            hover "battle/androi_sml_atck_butns_on.png"
            idle "battle/androi_sml_atck_butns_trnsp.png"





            if top_enemy_alive:
                hotspot (520, 591, 117,  41) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("ally1_top", True), Jump("ally1_att")]
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("ally1_top", True), Jump("ally1_att")]

            if mid_enemy_alive:
                hotspot (520, 634, 119,  34) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("ally1_mid", True), Jump("ally1_att")]
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("ally1_mid", True), Jump("ally1_att")]

            if bot_enemy_alive:
                hotspot (520, 670, 121,  39) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("ally1_bot", True), Jump("ally1_att")]
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("ally1_bot", True), Jump("ally1_att")]






label potiontest2:
    $ ally1_heal = False
    $ player_heal = False
    $ ally2_heal = False
    call screen potion_screen1

    screen potion_screen1:

        imagemap:

            ground "battle/androi_sml_itm_butns_off.png"
            hover "battle/androi_sml_itm_butns_on.png"
            idle "battle/androi_sml_itm_butns_trnsp.png"

            hotspot (780,580,110,130) action [Jump("fight_buttonstest")]






            if ally1_alive:
                hotspot (892, 591, 107,  44) hovered [Show('screen_ally1_glowball')] unhovered [Hide('screen_ally1_glowball')] action [Hide('screen_ally1_glowball'), SetVariable("ally1_heal", True),  Jump("potion_give1")]
                hotspot (  1,   1, 500, 189) hovered [Show('screen_ally1_glowball')] unhovered [Hide('screen_ally1_glowball')] action [Hide('screen_ally1_glowball'), SetVariable("ally1_heal", True),  Jump("potion_give1")]

            if player_alive:
                hotspot (898, 638, 101,  36) hovered [Show('screen_player_glowball')] unhovered [Hide('screen_player_glowball')] action [Hide('screen_player_glowball'), SetVariable("player_heal", True), Jump("potion_give1")]
                hotspot (  1, 190, 500, 189) hovered [Show('screen_player_glowball')] unhovered [Hide('screen_player_glowball')] action [Hide('screen_player_glowball'), SetVariable("player_heal", True), Jump("potion_give1")]

            if ally2_alive:
                hotspot (890, 681, 109,  35) hovered [Show('screen_ally2_glowball')] unhovered [Hide('screen_ally2_glowball')] action [Hide('screen_ally2_glowball'), SetVariable("ally2_heal", True),  Jump("potion_give1")]
                hotspot (  1, 382, 500, 189) hovered [Show('screen_ally2_glowball')] unhovered [Hide('screen_ally2_glowball')] action [Hide('screen_ally2_glowball'), SetVariable("ally2_heal", True),  Jump("potion_give1")]



label potion_give1:
    if ally1_heal:
        $ potions -=1
        $ ally1_hp += 300
        if f1equip == "health":
            if ally1_hp >= 800:
                $ ally1_hp = 800
            jump top_enemy_turn
        else:
            if ally1_hp >= 500:
                $ ally1_hp = 500
            jump top_enemy_turn

    if player_heal:
        $ potions -=1
        $ player_hp += 400
        if player_hp >= 1000:
            $ player_hp = 1000
        jump top_enemy_turn


    if ally2_heal:
        $ potions -=1
        $ ally2_hp += 300
        if f2equip == "health":
            if ally2_hp >= 800:
                $ ally2_hp = 800
            jump top_enemy_turn
        else:
            if ally2_hp >= 500:
                $ ally2_hp = 500
            jump top_enemy_turn






label fight_buttonstest1:
    if player_alive:
        if auto_battle:
            if firewall_acquired:
                jump firewall_them_all
            else:
                jump auto_battle_player

        call screen fight_buttonstest1
    else:

        jump mid_enemy_turn


    screen fight_buttonstest1:
        add "battle/androi_player_select.png"
        imagemap:

            ground "battle/androi_main_butns_off.png"
            hover "battle/androi_main_butns_on.png"
            idle "battle/androi_main_butns_trnsp.png"

            hotspot (520,580,120,130) action [Jump("screen_attack_options2")]
            hotspot (650,580,120,130) action [SetVariable("blocking2", True), Jump("mid_enemy_turn")]
            hotspot (780,580,120,130) action [Jump("main_potiontest")]





            if top_enemy_alive:
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("player_top", True), Jump("player_att")]

            if mid_enemy_alive:
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("player_mid", True), Jump("player_att")]

            if bot_enemy_alive:
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("player_bot", True), Jump("player_att")]






            if firewall_acquired == True:
                add "battle/androi_firewall.png"
                hotspot (405, 600, 115, 115) hovered [Show('screen_firewall_selected')] unhovered [Hide('screen_firewall_selected')] action [Hide('screen_firewall_selected'),SetVariable("player_bot", True), Jump("firewall_them_all")]

            if not auto_battle:
                textbutton "auto" xpos 0.9 ypos 0.78:
                    action [SetVariable("auto_battle", True), Jump("auto_battle_player")]

            if auto_battle:
                textbutton "auto off" xpos 0.88 ypos 0.78:
                    action [SetVariable("auto_battle", False), Jump("fight_buttonstest1")]


label auto_battle_player:
    if top_enemy_alive:
        $ player_top = True
        jump player_att
    if mid_enemy_alive:
        $ player_mid = True
        jump player_att
    if bot_enemy_alive:
        $ player_bot = True
        jump player_att



label fight_buttonstest_tent1:
    if player_alive:
        call screen fight_buttonstest_tent1
    else:

        jump mid_enemy_turn


    screen fight_buttonstest_tent1:
        add "battle/androi_player_select.png"
        imagemap:

            ground "battle/androi_main_butns_off.png"
            hover "battle/androi_main_butns_on.png"
            idle "battle/androi_main_butns_trnsp.png"

            hotspot (520,580,120,130) action [Jump("screen_attack_options2")]





            if top_enemy_alive:
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("player_top", True), Jump("player_att")]

            if mid_enemy_alive:
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("player_mid", True), Jump("player_att")]

            if bot_enemy_alive:
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("player_bot", True), Jump("player_att")]






            if firewall_acquired == True:
                add "battle/androi_firewall.png"
                hotspot (405, 600, 115, 115) hovered [Show('screen_firewall_selected')] unhovered [Hide('screen_firewall_selected')] action [Hide('screen_firewall_selected'),SetVariable("player_bot", True), Jump("firewall_them_all")]



label fight_buttonstest_tent2:
    if player_alive:
        call screen fight_buttonstest_tent2
    else:

        jump mid_enemy_turn


    screen fight_buttonstest_tent2:
        add "battle/androi_player_select.png"
        imagemap:

            ground "battle/androi_main_butns_off.png"
            hover "battle/androi_main_butns_on.png"
            idle "battle/androi_main_butns_trnsp.png"





















            if firewall_acquired == True:
                add "battle/androi_firewall.png"
                hotspot (405, 600, 115, 115) hovered [Show('screen_firewall_selected')] unhovered [Hide('screen_firewall_selected')] action [Hide('screen_firewall_selected'),SetVariable("player_bot", True), Jump("firewall_them_all")]






label screen_attack_options2:
    call screen screen_attack_options2 

    screen screen_attack_options2:

        add "battle/androi_player_select.png"
        add "battle/Book2_hp_battle_allies.png"

        imagemap:

            ground "battle/androi_sml_atck_butns_off.png"
            hover "battle/androi_sml_atck_butns_on.png"
            idle "battle/androi_sml_atck_butns_trnsp.png"

            if top_enemy_alive:
                hotspot (520, 591, 117,  41) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("player_top", True), Jump("player_att")]
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'), SetVariable("player_top", True), Jump("player_att")]

            if mid_enemy_alive:
                hotspot (520, 634, 119,  34) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("player_mid", True), Jump("player_att")]
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'), SetVariable("player_mid", True), Jump("player_att")]

            if bot_enemy_alive:
                hotspot (520, 670, 121,  39) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("player_bot", True), Jump("player_att")]
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'), SetVariable("player_bot", True), Jump("player_att")]





            if firewall_acquired == True:
                add "battle/androi_firewall.png"
                hotspot (405, 600, 115, 115) action [SetVariable("player_bot", True), Jump("firewall_them_all")]










label potiontest1:
    $ ally1_heal = False
    $ player_heal = False
    $ ally2_heal = False
    call screen potion_screen

    screen potion_screen:
        add "battle/Book2_hp_battle_allies.png"


        imagemap:

            ground "battle/androi_sml_itm_butns_off.png"
            hover "battle/androi_sml_itm_butns_on.png"
            idle "battle/androi_sml_itm_butns_trnsp.png"


            hotspot (780,580,110,130) action [Jump("fight_buttonstest1")]


            if ally1_alive:
                hotspot (892,591, 107,  44) hovered [Show('screen_ally1_glowball')] unhovered [Hide('screen_ally1_glowball')] action [Hide('screen_ally1_glowball'), SetVariable("ally1_heal", True),  Jump("potion_give")]
                hotspot (  1,  1, 500, 189) hovered [Show('screen_ally1_glowball')] unhovered [Hide('screen_ally1_glowball')] action [Hide('screen_ally1_glowball'), SetVariable("ally1_heal", True),  Jump("potion_give")]

            if player_alive:
                hotspot (898, 638, 101,  36) hovered [Show('screen_player_glowball')] unhovered [Hide('screen_player_glowball')] action [Hide('screen_player_glowball'), SetVariable("player_heal", True), Jump("potion_give")]
                hotspot (  1, 190, 500, 189) hovered [Show('screen_player_glowball')] unhovered [Hide('screen_player_glowball')] action [Hide('screen_player_glowball'), SetVariable("player_heal", True), Jump("potion_give")]

            if ally2_alive:
                hotspot (890, 681, 109,  35) hovered [Show('screen_ally2_glowball')] unhovered [Hide('screen_ally2_glowball')] action [Hide('screen_ally2_glowball'), SetVariable("ally2_heal", True),  Jump("potion_give")]
                hotspot (  1, 382, 500, 189) hovered [Show('screen_ally2_glowball')] unhovered [Hide('screen_ally2_glowball')] action [Hide('screen_ally2_glowball'), SetVariable("ally2_heal", True),  Jump("potion_give")]


label potion_give:
    if ally1_heal:
        $ potions -=1
        $ ally1_hp += 300
        if f1equip == "health":
            if ally1_hp >= 800:
                $ ally1_hp = 800
            jump mid_enemy_turn
        else:
            if ally1_hp >= 500:
                $ ally1_hp = 500
            jump mid_enemy_turn

    if player_heal:
        $ potions -=1
        $ player_hp += 400
        if player_hp >= 1000:
            $ player_hp = 1000
        jump mid_enemy_turn


    if ally2_heal:
        $ potions -=1
        $ ally2_hp += 300
        if f2equip == "health":
            if ally2_hp >= 800:
                $ ally2_hp = 800
            jump mid_enemy_turn
        else:
            if ally2_hp >= 500:
                $ ally2_hp = 500
            jump mid_enemy_turn





label fight_buttonstest2:
    if ally2_alive:
        if auto_battle:
            jump auto_battle_ally2
        call screen fight_buttonstest2
    else:

        jump bot_enemy_turn


    screen fight_buttonstest2:
        add "battle/androi_ally2_select.png"
        imagemap:

            ground "battle/androi_main_butns_off.png"
            hover "battle/androi_main_butns_on.png"
            idle "battle/androi_main_butns_trnsp.png"

            hotspot (520,580,120,130) action [Jump("screen_attack_options3")]
            hotspot (650,580,120,130) action [SetVariable("blocking3", True), Jump("bot_enemy_turn")]
            hotspot (780,580,120,130) action [Jump("main_potiontest2")]




            if top_enemy_alive:
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'),SetVariable("ally2_top", True), Jump("ally2_att")]

            if mid_enemy_alive:
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'),SetVariable("ally2_mid", True), Jump("ally2_att")]

            if bot_enemy_alive:
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'),SetVariable("ally2_bot", True), Jump("ally2_att")]

            if not auto_battle:
                textbutton "auto" xpos 0.9 ypos 0.78:
                    action [SetVariable("auto_battle", True), Jump("auto_battle_ally2")]

            if auto_battle:
                textbutton "auto off" xpos 0.88 ypos 0.78:
                    action [SetVariable("auto_battle", False), Jump("fight_buttonstest2")]


label auto_battle_ally2:
    if top_enemy_alive:
        $ ally2_top = True
        jump ally2_att
    if mid_enemy_alive:
        $ ally2_mid = True
        jump ally2_att
    if bot_enemy_alive:
        $ ally2_bot = True
        jump ally2_att




label screen_attack_options3:
    call screen screen_attack_options3

    screen screen_attack_options3:

        add "battle/androi_ally2_select.png"
        add "battle/Book2_hp_battle_allies.png"

        imagemap:

            ground "battle/androi_sml_atck_butns_off.png"
            hover "battle/androi_sml_atck_butns_on.png"
            idle "battle/androi_sml_atck_butns_trnsp.png"

            if top_enemy_alive:
                hotspot (520, 591, 117,  41) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'),SetVariable("ally2_top", True), Jump("ally2_att")]
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'),SetVariable("ally2_top", True), Jump("ally2_att")]

            if mid_enemy_alive:
                hotspot (520,634,119,34) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'),SetVariable("ally2_mid", True), Jump("ally2_att")]
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'),SetVariable("ally2_mid", True), Jump("ally2_att")]

            if bot_enemy_alive:
                hotspot (520, 670, 121,  39) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'),SetVariable("ally2_bot", True), Jump("ally2_att")]
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'),SetVariable("ally2_bot", True), Jump("ally2_att")]






label potiontest3:
    $ ally1_heal = False
    $ player_heal = False
    $ ally2_heal = False
    call screen potion_screen2


    screen potion_screen2:
        imagemap:

            ground "battle/androi_sml_itm_butns_off.png"
            hover "battle/androi_sml_itm_butns_on.png"
            idle "battle/androi_sml_itm_butns_trnsp.png"


            hotspot (780,580,110,130) action [Jump("fight_buttonstest2")]

            if ally1_alive:
                hotspot (892,591, 107,  44) hovered [Show('screen_ally1_glowball')] unhovered [Hide('screen_ally1_glowball')] action [Hide('screen_ally1_glowball'), SetVariable("ally1_heal", True),  Jump("potion_give2")]
                hotspot (  1,  1, 500, 189) hovered [Show('screen_ally1_glowball')] unhovered [Hide('screen_ally1_glowball')] action [Hide('screen_ally1_glowball'), SetVariable("ally1_heal", True),  Jump("potion_give2")]

            if player_alive:
                hotspot (898, 638, 101,  36) hovered [Show('screen_player_glowball')] unhovered [Hide('screen_player_glowball')] action [Hide('screen_player_glowball'), SetVariable("player_heal", True), Jump("potion_give2")]
                hotspot (  1, 190, 500, 189) hovered [Show('screen_player_glowball')] unhovered [Hide('screen_player_glowball')] action [Hide('screen_player_glowball'), SetVariable("player_heal", True), Jump("potion_give2")]

            if ally2_alive:
                hotspot (890, 681, 109,  35) hovered [Show('screen_ally2_glowball')] unhovered [Hide('screen_ally2_glowball')] action [Hide('screen_ally2_glowball'), SetVariable("ally2_heal", True),  Jump("potion_give2")]
                hotspot (  1, 382, 500, 189) hovered [Show('screen_ally2_glowball')] unhovered [Hide('screen_ally2_glowball')] action [Hide('screen_ally2_glowball'), SetVariable("ally2_heal", True),  Jump("potion_give2")]





label potion_give2:
    if ally1_heal:
        $ potions -=1
        $ ally1_hp += 300
        if f1equip == "health":
            if ally1_hp >= 800:
                $ ally1_hp = 800
            jump bot_enemy_turn
        else:
            if ally1_hp >= 500:
                $ ally1_hp = 500
            jump bot_enemy_turn

    if player_heal:
        $ potions -=1
        $ player_hp += 400
        if player_hp >= 1000:
            $ player_hp = 1000
        jump bot_enemy_turn


    if ally2_heal:
        $ potions -=1
        $ ally2_hp += 300
        if f2equip == "health":
            if ally2_hp >= 800:
                $ ally2_hp = 800
            jump bot_enemy_turn
        else:
            if ally2_hp >= 500:
                $ ally2_hp = 500
            jump bot_enemy_turn



label fight_buttonstest_tent3:

    if ally2_alive:
        call screen fight_buttonstest_tent3
    else:

        jump bot_enemy_turn


    screen fight_buttonstest_tent3:
        add "battle/androi_ally2_select.png"
        imagemap:

            ground "battle/androi_main_butns_off.png"
            hover "battle/androi_main_butns_on.png"
            idle "battle/androi_main_butns_trnsp.png"

            hotspot (520,580,120,130) action [Jump("screen_attack_options3")]




            if top_enemy_alive:
                hotspot (500,   1, 500, 189) hovered [Show('screen_enemy1_glowball')] unhovered [Hide('screen_enemy1_glowball')] action [Hide('screen_enemy1_glowball'),SetVariable("ally2_top", True), Jump("ally2_att")]

            if mid_enemy_alive:
                hotspot (500, 190, 500, 189) hovered [Show('screen_enemy2_glowball')] unhovered [Hide('screen_enemy2_glowball')] action [Hide('screen_enemy2_glowball'),SetVariable("ally2_mid", True), Jump("ally2_att")]

            if bot_enemy_alive:
                hotspot (500, 382, 500, 189) hovered [Show('screen_enemy3_glowball')] unhovered [Hide('screen_enemy3_glowball')] action [Hide('screen_enemy3_glowball'),SetVariable("ally2_bot", True), Jump("ally2_att")]



label firewall_them_all:

    play sound "audio/firewall.mp3"

    show firewall with Dissolve(1.0):
        xpos -100
        linear 1.8 xpos 800


    show flamespiral with dissolve
    hide flamespiral with dissolve
    "Your special attack damaged all enemies!!"


    if top_enemy_alive:
        $ top_enemy_hp -= 400
    if mid_enemy_alive:
        $ mid_enemy_hp -= 400
    if bot_enemy_alive:
        $ bot_enemy_hp -= 400

    if top_enemy_hp <= 0:
        $ top_enemy_hp <= 0
        $ top_enemy_alive = False
        hide top_enemy with dissolve

    if mid_enemy_hp <= 0:
        $ mid_enemy_hp <= 0
        $ mid_enemy_alive = False
        hide mid_enemy with dissolve

    if bot_enemy_hp <= 0:
        $ bot_enemy_hp <= 0
        $ bot_enemy_alive = False
        hide bot_enemy with dissolve

    if top_enemy_alive == False and mid_enemy_alive == False and bot_enemy_alive == False:
        if tentaclefight2:
            jump tentaclefight2_won
        jump moose_losttest
    elif top_enemy_alive:
        jump mid_enemy_turn
    elif mid_enemy_alive:
        jump mid_enemy_turn
    elif bot_enemy_alive:
        jump bot_enemy_turn







label moose_losttest:
    $ auto_battle = False
    $ fbattles +=1

    if fight_azula:
        jump fight_azula_youwon
    if fight_naga:
        jump fight_naga_youwon

    if training_battle1:
        $ training_battle1 = False
        hide screen hp_bar_fire
        a "congratulations, you beat a weak, lone earthbender. barely."
        a "hopefully you can find some troops that aren't as weak as you are."
        a "get your shit together and then go deal with the straggling forces."
        play sound "audio/win2.mp3"
        "you won your first battle!"
        $ fbattles -=1
        hide battle_background
        hide a_battle_small
        stop music fadeout 3
        play music "audio/Shenyang.ogg" fadein 3
        if thief > zuko:
            jump city
        else:
            jump zcity1

    if fbattles == 3:
        if thief > zuko:
            $ randcoin = renpy.random.randint(30, 50)
            $ fmoney += randcoin
            play sound "audio/money.mp3"
            "you got [randcoin] coins!"

            play sound "audio/win2.mp3"
            stop music fadeout 3
            hide screen hp_bar_fire
            hide hp_bar_fire
            hide battle_background
            hide a_battle_small
            scene bg_a_city_night with dissolve
            show a_blink with dissolve
            a "i'm surprised at you, thief."
            a "i expected you to be dead long before now, but instead... you're winning."
            show au with dissolve
            hide a_blink
            a "i... underestimated you."
            a "which is not easy for me to say."
            a "..."
            show a_blink with dissolve
            hide au
            a "my captains are woefully incompetent, and I need someone who can win skirmishes."
            a "i'm going to give you some harder battles. I expect you to win them."
            a "as a reward for doing so, I will give you zuko's old room in the palace..."
            a "you will no longer have to sleep in the prison."
            y "he doesn't need it?"
            show au with dissolve
            hide a_blink
            a "poor zuzu came by briefly, but left before I could speak to him."
            show a_blink with dissolve
            hide au
            y "well, i'm not gonna complain."
            a "good. for now i have one other task for you."
            a "come with me to the farm."
            hide a_blink with dissolve
            "you follow azula to a large building, surrounded by guards."
            y "what is this place?"
            show a_blink with dissolve
            a "it's a... new program i've come up with."
            a "and you're going to help me make it a success."
            a "come inside and I'll explain further..."
            hide a_blink with dissolve
            show farm_hall with dissolve
            "you walk through the enormous doors and find yourself surrounded by contained girls."
            y "whoa. what... what am i looking at."
            show al_blink with dissolve
            a "this... is the farm."
            a "it serves two purposes."
            a "First, This is where we breed future firebenders for our army."
            a "we impregnate the girls with powerful firebenders."
            a "we will be unstoppable. our empire will expand throughout time."
            a "this is merely the next obvious step."
            a "it's other purpose is to serve as a source of income for us from our elite society members."
            y "...how?"
            show ale with dissolve
            hide al_blink
            a "we milk the girls regularly - it goes for quite a high price."
            y "seriously? why?"
            show ald with dissolve
            hide ale
            a "breast-feeding your own child is so... peasant. So high-ranking ladies purchase it."
            show ale with dissolve
            hide ald
            a "and of course gentlemen have all sorts of uses for it."
            show al_blink with dissolve
            hide ale
            a "but the pregnancy takes too long, and I have no one I trust to manage them."
            a "that's where you come in, thief."
            y "..."
            y "i can't... make the gestation time faster..."
            show ale with dissolve
            hide al_blink
            a "there's a recipe. This old witch, Hermione, was notorious for her potions and scrolls."
            show al_blink with dissolve
            hide ale
            a "one of which hastens pregnancy to 20 days."
            y "20 days?!? that's insane."
            show ald with dissolve
            hide al_blink
            a "i don't need you to question me, thief."
            a "but i need some ingredients to make it happen."
            show ale with dissolve
            hide ald
            a "i have the ejaculate of a virgin girl. one of these cows provided it..."
            show al_blink with dissolve
            hide ale
            a "...against her will..."
            a "...but i also need a dragon scale and some root of quickwort."
            y "..."
            y "where the fuck am i supposed to get those?"
            a "that's your problem, and you had better solve it soon."
            a "there's money to be made and women to fuck, so go get those ingredients."
            a "i'll give you full access to the city in the morning."
            a "i have great plans for you."
            hide al_blink with dissolve
            y "..."
            y "guess i'll see if I can find any rumors."
            play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
            scene bg_a_city_night with dissolve
            hide farm_hall
            jump second_city_access_night
        else:
            $ randcoin = renpy.random.randint(30, 50)
            $ fmoney += randcoin
            play sound "audio/money.mp3"
            "you got [randcoin] coins!"

            play sound "audio/win2.mp3"
            stop music fadeout 3
            hide screen hp_bar_fire
            hide hp_bar_fire
            hide battle_background
            hide a_battle_small
            scene bg_a_city_night with dissolve
            show a_blink with dissolve
            a "i'm surprised at you, brother."
            a "i didn't expect you to do this well."
            show au with dissolve
            hide a_blink
            a "i... underestimated you."
            a "which is not easy for me to say."
            a "..."
            show a_blink with dissolve
            hide au
            a "our captains are woefully incompetent, and I need someone who can win skirmishes."
            a "i'm going to give you some harder battles. I expect you to win them."
            a "now i have one other task for you."
            a "come with me to the farm."
            hide a_blink with dissolve
            "you follow azula to a large building, surrounded by guards."
            y "what is this place?"
            show a_blink with dissolve
            a "it's a... new program i've come up with."
            a "and you're going to help me make it a success."
            a "come inside and I'll explain further..."
            hide a_blink with dissolve
            show farm_hall with dissolve
            "you walk through the enormous doors and find yourself surrounded by contained girls."
            y "whoa. what... what am i looking at."
            show al_blink with dissolve
            a "this... is the farm."
            a "it serves two purposes."
            a "First, This is where we breed future firebenders for our army."
            a "we impregnate the girls with powerful firebenders."
            a "we will be unstoppable. our empire will expand throughout time."
            a "this is merely the next obvious step."
            a "it's other purpose is to serve as a source of income for us from our elite society members."
            y "...how?"
            show ale with dissolve
            hide al_blink
            a "we milk the girls regularly - it goes for quite a high price."
            y "seriously? why?"
            show ald with dissolve
            hide ale
            a "breast-feeding your own child is so... peasant. So high-ranking ladies purchase it."
            show ale with dissolve
            hide ald
            a "and of course gentlemen have all sorts of uses for it."
            show al_blink with dissolve
            hide ale
            a "but the pregnancy takes too long, and I have no one I trust to manage them."
            a "that's where you come in, brother."
            y "..."
            y "i can't... make the gestation time faster..."
            show ale with dissolve
            hide al_blink
            a "there's a recipe. This old witch, Hermione, was notorious for her potions and scrolls."
            show al_blink with dissolve
            hide ale
            a "one of which hastens pregnancy to 20 days."
            y "20 days?!? that's insane."
            a "i need some ingredients to make it happen."
            show ale with dissolve
            hide ald
            a "i have the ejaculate of a virgin girl. one of these cows provided it..."
            show al_blink with dissolve
            hide ale
            a "...against her will..."
            a "...but i also need a dragon scale and some root of quickwort."
            y "..."
            y "where am i supposed to get those?"
            a "that's your problem, and you had better solve it soon."
            a "there's money to be made and women to fuck, so go get those ingredients."
            a "i have great plans for you."
            hide al_blink with dissolve
            y "..."
            ya "she is so... argh."
            yd "and insane. this is insane."
            yd "i can't believe she wants to... breed me?"
            yc "she's got problems."
            y "...."
            y "well, i guess i'll see if I can find any rumors for those ingredients."
            play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
            scene bg_a_city_night with dissolve
            hide farm_hall
            $ farm_initiated = True
            jump zcity_night1
    else:
        if thief > zuko:
            $ randcoin = renpy.random.randint(30, 50)
            $ fmoney += randcoin
            play sound "audio/money.mp3"
            "you got [randcoin] coins!"

            if farm_unlocked:
                $ randcow = renpy.random.randint(1, 2)
                if randcow ==1:
                    if total_girls <=98:
                        play sound "audio/win2.mp3"
                        "you win!"
                        "one of the earth kingdom fighters was a girl!"
                        "you sent her to the farm."
                        $ fresh_girls +=1
                        $ total_girls +=1
                        $ a_aff +=1
                        hide screen hp_bar_fire
                        hide hp_bar_fire
                        hide battle_background
                        hide a_battle_small
                        stop music fadeout 3
                        play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                        scene bg_a_city_night with dissolve
                        if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                            $ ally1_alive = True
                        if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                            $ ally2_alive = True
                        jump second_city_access_night
                    else:















                        play sound "audio/win2.mp3"
                        "you win!"
                        $ a_aff +=1
                        hide screen hp_bar_fire
                        hide hp_bar_fire
                        hide battle_background
                        hide a_battle_small
                        stop music fadeout 3
                        play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                        scene bg_a_city_night with dissolve
                        if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                            $ ally1_alive = True
                        if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                            $ ally2_alive = True
                        jump second_city_access_night















                if randcow ==2:
                    play sound "audio/win2.mp3"
                    "you win!"
                    $ a_aff +=1
                    hide screen hp_bar_fire
                    hide hp_bar_fire
                    hide battle_background
                    hide a_battle_small
                    stop music fadeout 3
                    play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                    scene bg_a_city_night with dissolve
                    if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                        $ ally1_alive = True
                    if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                        $ ally2_alive = True
                    jump second_city_access_night
            else:















                play sound "audio/win2.mp3"
                "you win!"
                $ a_aff +=1
                hide hp_bar_fire
                hide screen hp_bar_fire
                hide battle_background
                hide a_battle_small
                stop music fadeout 3
                play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                scene bg_a_city_night with dissolve
                if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                    $ ally1_alive = True
                if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                    $ ally2_alive = True
                jump second_city_access_night
        else:
















            $ randcoin = renpy.random.randint(30, 50)
            $ fmoney += randcoin
            play sound "audio/money.mp3"
            "you got [randcoin] coins!"

            if farm_unlocked:
                $ randcow = renpy.random.randint(1, 2)
                if randcow ==1:
                    if total_girls <=98:
                        play sound "audio/win2.mp3"
                        "you win!"
                        "one of the earth kingdom fighters was a girl!"
                        "you sent her to the farm."
                        $ fresh_girls +=1
                        $ total_girls +=1
                        $ a_aff +=1
                        hide screen hp_bar_fire
                        hide hp_bar_fire
                        hide battle_background
                        hide a_battle_small
                        stop music fadeout 3
                        play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                        scene bg_a_city_night with dissolve
                        if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                            $ ally1_alive = True
                        if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                            $ ally2_alive = True
                        jump zcity_night1
                    else:















                        play sound "audio/win2.mp3"
                        "you win!"
                        $ a_aff +=1
                        hide screen hp_bar_fire
                        hide hp_bar_fire
                        hide battle_background
                        hide a_battle_small
                        stop music fadeout 3
                        play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                        scene bg_a_city_night with dissolve
                        if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                            $ ally1_alive = True
                        if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                            $ ally2_alive = True
                        jump zcity_night1















                if randcow ==2:
                    play sound "audio/win2.mp3"
                    "you win!"
                    $ a_aff +=1
                    hide screen hp_bar_fire
                    hide hp_bar_fire
                    hide battle_background
                    hide a_battle_small
                    stop music fadeout 3
                    play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                    scene bg_a_city_night with dissolve
                    if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                        $ ally1_alive = True
                    if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                        $ ally2_alive = True
                    jump zcity_night1
            else:















                play sound "audio/win2.mp3"
                "you win!"
                $ a_aff +=1
                hide hp_bar_fire
                hide screen hp_bar_fire
                hide battle_background
                hide a_battle_small
                stop music fadeout 3
                play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
                scene bg_a_city_night with dissolve
                if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
                    $ ally1_alive = True
                if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
                    $ ally2_alive = True
                jump zcity_night1

















label avatar_losttest:










    if fight_azula:
        jump fight_azula_youlost
    if fight_naga:
        jump fight_naga_youlost

    $ auto_battle = False
    hide screen hp_bar_fire
    hide hp_bar_fire
    y "well, I got my ass kicked, but I think I did enough damage that they need to retreat and regroup."
    y "i should stock up on items or troops before trying that again."
    y "getting some stronger armor or more firebending training wouldn't be a bad idea either."
    hide battle_background
    hide a_battle_small
    stop music fadeout 3
    play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
    scene bg_a_city_night with dissolve
    if top_ally == "tank" or top_ally == "cavalry" or top_ally == "infantry":
        $ ally1_alive = True
    if bot_ally == "tank" or bot_ally == "cavalry" or bot_ally == "infantry":
        $ ally2_alive = True
    if not ally1_alive:
        $ top_ally = "none"
        if not ally2_alive:
            $ bot_ally = "none"
            if thief > zuko:
                jump second_city_access_night
            else:
                jump zcity_night1
        else:
            if thief > zuko:
                jump second_city_access_night
            else:
                jump zcity_night1
    else:
        if not ally2_alive:
            $ bot_ally = "none"
            if thief > zuko:
                jump second_city_access_night
            else:
                jump zcity_night1
        else:
            if thief > zuko:
                jump second_city_access_night
            else:
                jump zcity_night1




label tentaclefight1_won:
    scene bg_a_swamp_2
    show y_battle at Position(xalign=0.2, yalign=0.4)
    show mid_enemy at Position(xalign=0.8, yalign=0.4)
    hide screen hp_bar_fire
    hide hp_bar_fire
    play sound "audio/win2.mp3"
    y "now you're gonna give me some real answers!"
    play sound "audio/hiss.wav"
    ds "hisss!"
    y "why did you take azula?"
    ds "........"
    y "tell me!"
    ds "....so she cannot train you!"
    y "why?"
    ds "because then you will be powerful and nearer..."
    ds "and only one will survive."
    y "between you and i?"
    ds "you?"
    ds "you don't matter at all."
    ds "this battle has waged for eons, avatar."
    y "what battle?"
    ds "where is your spirit guide?"
    y "i don't know."
    ds "find out."
    ds "and don't forget..."
    ds "you must fuck to maintain the balance..."
    ds "and yet it will bring you insanity and endless nothingness."
    ds "and i'm only here to help."
    y "by trying to kill me?"
    ds "this time."
    y "stop being so fucking vague!"
    y "what the fuck is the ritual?"
    ds "you walk a razor's edge with your lust, avatar."
    ds "be careful."
    y "what does that mean?"
    hide spirit_idle with flash
    y "where-"
    y "oh, god damn it."
    $ tentaclefight1 = False
    $ tentaclefight2 = True
    y "i hate this fucking swamp."
    y "i hate everything."
    y "and my head fucking hurts..."
    $ firewall_acquired = True
    jump fighttest


label tentaclefight2_won:
    ae "ah... i feel much better."
    y "well I'm fucking exhausted."
    y "my body feels like soup."
    y "oh shit, i found your pants."
    a_ "well you finally did something right, i suppose."
    hide a_battle_small
    hide y_battle
    hide b_battle
    show a_blink with dissolve
    a "earth cowards beaten..."
    show au with dissolve
    a "...at an unfortunate cost..."
    hide a_blink
    show a_blink with dissolve
    a "let's return."
    hide au
    hide a_blink with dissolve
    hide bg_a_swamp_5
    hide screen hp_bar_fire
    hide hp_bar_fire
    stop music fadeout 3
    play music "audio/Komiku_-_10_-_Something_to_save.mp3" fadein 2
    scene bg_a_city_night with dissolve
    $ tentaclefight2 = False
    $ overthrow_begin = True
    $ player_fight = "normal"
    $ bot_ally = "none"
    $ ally2_alive = False
    jump overthrow

label fight_azula_now:
    scene bg_fight_azula
    show azu_idle at Position(xalign=0.8, yalign=0.4)
    show y_battle at Position(xalign=0.2, yalign=0.4)

    a "Everyone is always deserting me! Mother! father!"
    a "Even you when you went to chase after the avatar!!"
    a "all i wanted was for us to be happy! for you to stay with me!"
    a "we could have stayed that way forever and ever and ever and ever and ever!!!"
    if mai_chosen:
        y "i'm sorry, azula, but i love mai. i knew you wouldn't understand."
        y "this relationship you and i have is twisted, i can't do it any more."
        a "i don't care! i need you!"
    a "and if you won't love me.... then i won't let you love anyone!"


    if zuko_wounded:
        $ player_hp = 500
        yc "aw crap, and she wounded me during that damn hug...."
    hide azu_idle
    hide y_battle


    $ mid_enemy_hp = 500
    $ mid_enemy_hp_max = 500
    $ randenemy2 = "azu_idle"

    $ mid_enemy_alive = True
    $ top_enemy_alive = False
    $ bot_enemy_alive = False
    $ ally1_alive = False
    $ ally2_alive = False
    $ top_ally = "none"
    $ bot_ally = "none"

    $ mid_enemy = "azu_idle"
    $ mid_enemy_attack = 'azu_attack'
    $ mid_enemy_attack1 = 'azula'
    $ player_fight = "normal"
    show mid_enemy at Position(xalign=0.8, yalign=0.4)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    show screen hp_bar_fire
    with Dissolve(0.5)
    jump fight_buttonstest_tent1

label fight_azula_youwon:
    $ auto_battle = False
    stop music fadeout 3
    hide screen hp_bar_fire
    hide hp_bar_fire

    $ fight_azula = False
    a "no! no, it's not fair! it's not fair!!"
    "azula falls unconcious where she lies on the ground. You make sure she's okay."
    y "I don't think I could've won if you were your usual cold and calculating self."
    y "I'm sorry, I really am."
    if mai_chosen:
        yc "i love mai, azula."
        y "i know you don't understand."
        y "but that's the way it is."
        jump mai_chosen_battle
    else:
        jump after_agni_kai

label fight_azula_youlost:
    $ auto_battle = False
    stop music fadeout 3
    hide screen hp_bar_fire
    hide hp_bar_fire
    scene black with dissolve
    show pgfull with dissolve
    s "one more try, avatar...."
    hide pgfull with dissolve
    $ zuko_wounded = False
    if mai_chosen:
        jump fighttest
    else:
        jump zuko_return

label fight_naga_now:
    if azula_chosen:
        scene bg_fight_naga with dissolve
    if zuko_end:
        scene bg_fight_naga with dissolve
    if mai_chosen:
        scene bk2_beach00 with dissolve
    show naga_idle at Position(xalign=0.8, yalign=0.4)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    if zuko_end:
        y "i remember you, snake."
        y "i'm here, what do you want?"
        play sound "audio/hiss.wav"
        ds "hisss..."
        ds "i am an old spirit, human."
        ds "more powerful than you can imagine."
        ds "and sweeter than cherry popping."
        ds "and perhaps the only one to stop you."
        ds "or save you."
        ds "i haven't quite made up my mind."
        ds "except for now."
        y "are you just insane? leave me alone!"
        ds "where is your painted lady! hiss!"
        ds "she is not here!"
        ds "but {i}i{/i} am here! oh, yes!"
        y "did you hurt her?"
        ds "hurt her? me? no...."
        ds "i cannot hurt her...."
        ds "for all my knowledge and strength i cannot..."
        ds "just as she cannot hurt me..."
        ds "but i can hurt you!"
        yc "uh-"
        ds "HIiiissss, I'm gonna tear out your entrails."
        ya "nuhuh!"
        yd "fuck, i need a better battle cry."
        ds "too late!"
        hide naga_idle
        hide y_battle
    else:

        ya "why did you do that?"
        ds "for privacy."
        ya "what do you want?"
        ya "what are you?"
        play sound "audio/hiss.wav"
        ds "hisss..."
        ds "i am an old spirit, human."
        ds "more powerful than you can imagine."
        ds "and sweeter than cherry popping."
        ds "and perhaps the only one to stop you."
        ds "or save you."
        ds "i haven't quite made up my mind."
        ds "except for now."
        ya "are you just insane? leave me alone!"
        ds "where is your painted lady! hiss!"
        ds "she is not here!"
        ds "but {i}i{/i} am here! oh, yes!"
        y "did you hurt her?"
        ds "hurt her? me? no...."
        ds "i cannot hurt her...."
        ds "for all my knowledge and strength i cannot..."
        ds "just as she cannot hurt me..."
        ds "but i can hurt you!"
        yc "uh-"
        ds "HIiiissss, I'm gonna tear out your entrails."
        ya "nuh-uh!"
        yd "fuck, i need a better battle cry."
        ds "too late!"
        hide naga_idle
        hide y_battle



    $ mid_enemy_hp = 500
    $ mid_enemy_hp_max = 500
    $ randenemy2 = "naga_idle"

    $ mid_enemy_alive = True
    $ top_enemy_alive = False
    $ bot_enemy_alive = False
    $ ally1_alive = False
    $ ally2_alive = False
    $ top_ally = "none"
    $ bot_ally = "none"

    $ mid_enemy = "naga_idle"
    $ mid_enemy_attack = 'naga_attack'
    $ mid_enemy_attack1 = 'naga'
    $ player_fight = "normal"
    show mid_enemy at Position(xalign=0.8, yalign=0.4)
    show y_battle at Position(xalign=0.2, yalign=0.4)
    show screen hp_bar_fire
    with Dissolve(0.5)
    jump fight_buttonstest_tent1

label fight_naga_youwon:
    $ auto_battle = False
    stop music fadeout 3
    hide screen hp_bar_fire
    hide hp_bar_fire

    if zuko_end:
        $ fight_naga = False
        show naga_idle at Position(xalign=0.8, yalign=0.4) with dissolve
        ya "you!"
        ya "now you're gonna give me some real answers!"
        play sound "audio/hiss.wav"
        ds "hisss!"
        ya "why are you attacking me?"
        ds "........"
        ya "tell me!"
        ds "....so she cannot train you!"
        yd "who? azula?"
        y "Why? what does any of that got to do with you?!"
        ds "because then you will be powerful and nearer to..."
        ds "........"
        ds "....and only one will survive."
        yd "between you and i?"
        ds "you?"
        ds "you don't matter at all."
        ds "this battle has waged for eons, avatar."
        yd "what battle?"
        ds "where is your spirit guide?"
        y "i don't know."
        ds "find out."
        ds "and don't forget..."
        ds "you must fuck to maintain the balance..."
        ds "and yet it will bring you insanity and endless nothingness."
        ds "and i'm only here to help."
        yd "by trying to kill me?"
        ds "this time."
        ya "stop being so fucking vague!"
        ya "what the fuck is the ritual?"
        ds "you walk a razor's edge with your lust, avatar."
        ds "be careful."
        yd "what does that mean?"
        ds "the ritual is not-"
        show pgfull with flash
        with sshake
        s "{b}that's enough!"
        hide naga_idle with flash
    else:


        $ fight_naga = False
        "in a final flurry of attack, you tap into unknown reserves and launch a massive wall of fire."
        show firewall with Dissolve(1.0):
            xpos -100
            linear 1.8 xpos 800
        play sound "audio/win2.mp3"
        "your memories come flooding back to you, and you remember clearly who you are."
        "you feel like you've just stepped out of a fog."
        y "what the balls...."
        y "okay, i'm the avatar. i'm just... in another time."
        y "i don't care what it takes, i'm not doing this amnesia shit again."
        show naga_idle at Position(xalign=0.8, yalign=0.4) with dissolve
        ya "you!"
        ya "now you're gonna give me some real answers!"
        play sound "audio/hiss.wav"
        ds "hisss!"
        ya "why are you attacking me?"
        ds "........"
        ya "tell me!"
        ds "....so she cannot train you!"
        yd "who? azula?"
        y "Why? what does any of that got to do with you?!"
        ds "because then you will be powerful and nearer to..."
        ds "........"
        ds "....and only one will survive."
        yd "between you and i?"
        ds "you?"
        ds "you don't matter at all."
        ds "this battle has waged for eons, avatar."
        yd "what battle?"
        ds "where is your spirit guide?"
        y "i don't know."
        ds "find out."
        ds "and don't forget..."
        ds "you must fuck to maintain the balance..."
        ds "and yet it will bring you insanity and endless nothingness."
        ds "and i'm only here to help."
        yd "by trying to kill me?"
        ds "this time."
        ya "stop being so fucking vague!"
        ya "what the fuck is the ritual?"
        ds "you walk a razor's edge with your lust, avatar."
        ds "be careful."
        yd "what does that mean?"
        ds "the ritual is not-"
        show pgfull with flash
        with sshake
        s "{b}that's enough!"
        hide naga_idle with flash

    yd "where-"
    ya "oh, god damn it!"
    ya "i was just about to get some answers!"
    ya "i hate everything."
    yc "and my head fucking hurts..."
    s "well done avatar, I'm happy you have regained your memory. i regret that it took so much."
    ya "you let her attack me?"
    s "i was... occupied."
    s "but this outcome is satisfactory."
    ya "fuck you."
    s "not yet, avatar.... not yet...."
    yd "what?"
    s "it is time to leave this place, avatar."
    if zuko_end:
        $ zuko_goodbye_start = True
        y "i can't leave right now... i have to at least say goodbye."
        s "my energy here is weakening. we must leave soon."
        s "when you've said your goodbyes, visit me in the tower at night."
        s "i'll be waiting...."
        scene black with dissolve
        scene bg_a_city_night with dissolve
        y "i guess... i should say goodbye to azula and mai."
        y "and then i'll go to the tower at night to leave."
        jump zcity_night1

    s "you can leave immediately or wait for the girl to awaken."
    s "my energy here is weakening. we must leave soon either way."
    s "you will be able to come back to this point in the future."
    yd "i will?"
    s "yes, eventually. you will be able to return to this time."
    y "what will happen to my body?"
    s "it will be returned to it's natural inhabitant."
    y "will he know about any of this?"
    s "no."
    y "i see."
    menu:
        "leave now":
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            scene black with dissolve
            "you lift up and into the sky."
            hide afnabce with dissolve
            scene black with dissolve
            show pgfull with dissolve
            s "you have learned much."
            y "yeah, yeah. where to now?"
            s "the earth kingdom."
            $ firebending = 10
            hide pgfull with dissolve
            scene black
            scene worldmap_01
            jump worldmap3

        "wait for mai" if mai_chosen:
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            "you wait patiently for mai to regain consciousness."
            scene black
            scene bk2_beach01
            show b2ma b2ma05
            show mai_idle_fl_angry
            with dissolve
            m "what... happened...?"
            m "i remember a spirit..."
            hide mai_idle_fl_angry with dissolve
            m "zuko! you're okay!"
            yc "...for the moment."
            show mai_idle_fl_angry with dissolve
            m "is something wrong?"
            yc "i don't know how to tell you this, but...."
            y "i'm going to lose my memory."
            m "again?"
            y "yes, but.... this time will be different."
            y "i won't remember us."
            m "what are you talking about?"
            y "i'm sorry."
            y "I promise to come back to you."
            yc "but.... i can't promise when."
            y "hopefully, you'll never notice anything, but if i mess up..."
            m "zuko... i don't understand..."
            y "i don't know how much i understand either."
            y "but know that i love you."
            y "you'll just have to make me fall in love with you all over again."
            y "but... i don't believe you'll find it very difficult."
            m "why...?"
            y "it's time."
            m "what? what does that mean?"
            y "i will come back for you. i promise."
            m "....please. i need you."
            y "i will be back for you, love."
            "the spirit pulls you out of zuko's body."
            "you watch the body you'd inhabited fall to the ground as mai moves quickly to it."
            m "no!"
            scene black with dissolve

        "wait for azula" if azula_chosen:
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            "you pull out a knife and make a shallow cut on your head, causing your face to become bloody."
            s "....why are you doing that?"
            y "you'll see. just stand by to get me out of here."
            scene black
            scene bk2_night01
            show b2az b2az03
            with dissolve
            "you lie down and wait for azula to stir, lightly shaking her as she wakes up."
            "you stand up."
            scene black with dissolve
            "azula tries to get up as well, but falls back on her knees."
            scene bk2_night01
            show b2az b2az04
            show b2az_concern
            show b2az_blink
            with dissolve
            a "ungh...."
            y "azula! Are you alright?"
            a "i think so...wh...what happened?"
            y "Some bandits... now in the profession of being ashes."
            a "Those motherfuc-"
            hide b2az_blink with dissolve
            a "what happened to your head!?"
            y "They got a lucky shot in. I'm feeling very groggy."
            y "My head is pounding twice as hard as back when I lost my memory."
            y "If I do lose my memory again...."
            a "{size=+4}YOU WONT!"
            a "I'll get the best doctors and they'll..."
            show b2az_handson with dissolve
            "you reach out and place your hands on her shoulders, trying to comfort her."
            y "azula, if I do lose my memory again, you can't force your way into my heart by threats."
            hide b2az_concern with dissolve
            a "It worked before."
            y "Just try the gentle approach first, please."
            scene black with dissolve
            "azula succeeds in standing up this time."
            scene bk2_night01
            with dissolve
            show b2az b2az01
            with dissolve
            a "...."
            play sound "audio/kiss.mp3"
            with pflash
            "azula gives you a kiss."
            a "I promise, but you won't lose your memory so all of this is needless talk."
            ys "You aren't crossing your fingers behind your back are you?"
            a "Firescout's honor!"
            y "it's time."
            a "what?"
            y "i think i'm going to lose myself, azula."
            a "no.... no, i can't lose you!"
            y "i will come back for you. i promise."
            a "....please. i need you."
            y "i will be back for you, love."
            "the spirit pulls you out of zuko's body."
            show az_idle_body_shock with dissolve
            "you watch the body you'd inhabited fall to the ground as azula moves quickly to it."
            a "no!"
            scene black with dissolve

    show pgfull with dissolve
    s "you have learned much."
    y "yeah, yeah. where to now?"
    s "the earth kingdom."
    $ firebending = 10
    hide pgfull with dissolve
    scene black
    scene worldmap_01
    jump worldmap3

label fight_naga_youlost:
    $ auto_battle = False
    stop music fadeout 3
    hide screen hp_bar_fire
    hide hp_bar_fire

    if zuko_end:
        $ fight_naga = False
        "in your desperation, you tap into unknown reserves and launch a massive wall of fire."
        show firewall with Dissolve(1.0):
            xpos -100
            linear 1.8 xpos 800
        play sound "audio/win2.mp3"
        hide naga_idle with dissolve
        show naga_idle at Position(xalign=0.8, yalign=0.4) with dissolve
        ya "now you're gonna give me some real answers!"
        play sound "audio/hiss.wav"
        ds "hisss!"
        ya "why are you attacking me?"
        ds "........"
        ya "tell me!"
        ds "....so she cannot train you!"
        yd "who? azula?"
        y "Why? what does any of that got to do with you?!"
        ds "because then you will be powerful and nearer to..."
        ds "........"
        ds "....and only one will survive."
        yd "between you and i?"
        ds "you?"
        ds "you don't matter at all."
        ds "this battle has waged for eons, avatar."
        yd "what battle?"
        ds "where is your spirit guide?"
        y "i don't know."
        ds "find out."
        ds "and don't forget..."
        ds "you must fuck to maintain the balance..."
        ds "and yet it will bring you insanity and endless nothingness."
        ds "and i'm only here to help."
        yd "by trying to kill me?"
        ds "this time."
        ya "stop being so fucking vague!"
        ya "what the fuck is the ritual?"
        ds "you walk a razor's edge with your lust, avatar."
        ds "be careful."
        yd "what does that mean?"
        ds "the ritual is not-"
        show pgfull with flash
        with sshake
        s "{b}that's enough!"
        hide naga_idle with flash
    else:


        $ fight_naga = False
        "in your desperation, you tap into unknown reserves and launch a massive wall of fire."
        show firewall with Dissolve(1.0):
            xpos -100
            linear 1.8 xpos 800
        hide naga_idle with dissolve
        play sound "audio/win2.mp3"
        "your memories come flooding back to you, and you remember clearly who you are."
        "you feel like you've just stepped out of a fog."
        y "what the balls.... okay, i don't care what it takes, i'm not doing this amnesia shit again."
        show naga_idle at Position(xalign=0.8, yalign=0.4) with dissolve
        ya "you!"
        ya "now you're gonna give me some real answers!"
        play sound "audio/hiss.wav"
        ds "hisss!"
        ya "why are you attacking me?"
        ds "........"
        ya "tell me!"
        ds "....so she cannot train you!"
        yd "who? azula?"
        y "Why? what does any of that got to do with you?!"
        ds "because then you will be powerful and nearer to..."
        ds "........"
        ds "....and only one will survive."
        yd "between you and i?"
        ds "you?"
        ds "you don't matter at all."
        ds "this battle has waged for eons, avatar."
        yd "what battle?"
        ds "where is your spirit guide?"
        y "i don't know."
        ds "find out."
        ds "and don't forget..."
        ds "you must fuck to maintain the balance..."
        ds "and yet it will bring you insanity and endless nothingness."
        ds "and i'm only here to help."
        yd "by trying to kill me?"
        ds "this time."
        ya "stop being so fucking vague!"
        ya "what the fuck is the ritual?"
        ds "you walk a razor's edge with your lust, avatar."
        ds "be careful."
        yd "what does that mean?"
        ds "the ritual is not-"
        show pgfull with flash
        with sshake
        s "{b}that's enough!"
        hide naga_idle with flash

    yd "where-"
    ya "oh, god damn it!"
    ya "i was just about to get some answers!"
    ya "i hate everything."
    yc "and my head fucking hurts..."
    s "well done avatar, I'm happy you have regained your memory. i regret that it took so much."
    ya "you let her attack me?"
    s "i was... occupied."
    s "but this outcome is satisfactory."
    ya "fuck you."
    s "not yet, avatar.... not yet...."
    yd "what?"
    s "it is time to leave this place, avatar."
    if zuko_end:
        $ zuko_goodbye_start = True
        y "i can't leave right now... i have to at least say goodbye."
        s "my energy here is weakening. we must leave soon."
        s "when you've said your goodbyes, visit me in the tower at night."
        s "i'll be waiting...."
        scene black with dissolve
        scene bg_a_city_night with dissolve
        y "i guess... i should say goodbye to azula and mai."
        y "and then i'll go to the tower at night to leave."
        jump zcity_night1

    s "you can leave immediately or wait for the girl to awaken."
    s "my energy here is weakening. we must leave soon either way."
    s "you will be able to come back to this point in the future."
    yd "i will?"
    s "yes, eventually. you will be able to return to this time."
    y "what will happen to my body?"
    s "it will be returned to it's natural inhabitant."
    y "will he know about any of this?"
    s "no."
    y "i see."
    menu:
        "leave now":
            scene black with dissolve
            "you lift up and into the sky."
            hide afnabce with dissolve
            scene black with dissolve
            show pgfull with dissolve
            s "you have learned much."
            y "yeah, yeah. where to now?"
            s "the earth kingdom."
            $ firebending = 10
            hide pgfull with dissolve
            scene black
            scene worldmap_01
            jump worldmap3

        "wait for mai" if mai_chosen:
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            "you wait patiently for mai to regain consciousness."
            scene black
            scene bk2_beach01
            show b2ma b2ma05
            show mai_idle_fl_angry
            with dissolve
            m "what... happened...?"
            m "i remember a spirit..."
            hide mai_idle_fl_angry with dissolve
            m "zuko! you're okay!"
            yc "...for the moment."
            show mai_idle_fl_angry with dissolve
            m "is something wrong?"
            yc "i don't know how to tell you this, but...."
            y "i'm going to lose my memory."
            m "again?"
            y "yes, but.... this time will be different."
            y "i won't remember us."
            m "what are you talking about?"
            y "i'm sorry."
            y "I promise to come back to you."
            yc "but.... i can't promise when."
            y "hopefully, you'll never notice anything, but if i mess up..."
            m "zuko... i don't understand..."
            y "i don't know how much i understand either."
            y "but know that i love you."
            y "you'll just have to make me fall in love with you all over again."
            y "but... i don't believe you'll find it very difficult."
            m "why...?"
            y "it's time."
            m "what? what does that mean?"
            y "i will come back for you. i promise."
            m "....please. i need you."
            y "i will be back for you, love."
            "the spirit pulls you out of zuko's body."

            "you watch the body you'd inhabited fall to the ground as mai moves quickly to it."
            m "no!"
            scene black with dissolve
        "wait for azula":

            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            "you pull out a knife and make a shallow cut on your head, causing your face to become bloody."
            s "....why are you doing that?"
            y "you'll see. just stand by to get me out of here."
            scene black
            scene bk2_night01
            show b2az b2az03
            with dissolve
            "you lie down and wait for azula to stir, lightly shaking her as she wakes up."
            "you stand up."
            scene black with dissolve
            "azula tries to get up as well, but falls back on her knees."
            scene bk2_night01
            show b2az b2az04
            show b2az_concern
            show b2az_blink
            with dissolve
            a "ungh...."
            y "azula! Are you alright?"
            a "i think so...wh...what happened?"
            y "Some bandits... now in the profession of being ashes."
            a "Those motherfuc-"
            hide b2az_blink with dissolve
            a "what happened to your head!?"
            y "They got a lucky shot in. I'm feeling very groggy."
            y "My head is pounding twice as hard as back when I lost my memory."
            y "If I do lose my memory again...."
            a "{size=+4}YOU WONT!"
            a "I'll get the best doctors and they'll..."
            show b2az_handson with dissolve
            "you reach out and place your hands on her shoulders, trying to comfort her."
            y "azula, if I do lose my memory again, you can't force your way into my heart by threats."
            hide b2az_concern with dissolve
            a "It worked before."
            y "Just try the gentle approach first, please."
            scene black with dissolve
            "azula succeeds in standing up this time."
            scene bk2_night01
            with dissolve
            show b2az b2az01
            with dissolve
            a "...."
            play sound "audio/kiss.mp3"
            with pflash
            "azula gives you a kiss."
            a "I promise, but you won't lose your memory so all of this is needless talk."
            ys "You aren't crossing your fingers behind your back are you?"
            a "Firescout's honor!"
            y "it's time."
            a "what?"
            y "i think i'm going to lose myself, azula."
            a "no.... no, i can't lose you!"
            y "i will come back for you. i promise."
            a "....please. i need you."
            y "i will be back for you, love."
            "the spirit pulls you out of zuko's body."
            show az_idle_body_shock with dissolve
            "you watch the body you'd inhabited fall to the ground as azula moves quickly to it."

            a "no!"
            scene black with dissolve

    show pgfull with dissolve
    s "you have learned much."
    y "yeah, yeah. where to now?"
    s "the earth kingdom."
    $ firebending = 10
    hide pgfull with dissolve
    scene black
    scene worldmap_01
    jump worldmap3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
