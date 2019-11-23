label fightspirit1:
    stop music
    play music "audio/Prelude and Action.mp3"

    $ d_flag_01 = False
    $ d_flag_02 = False

    $ av_hp = 1000
    $ moose_hp = 1000

    $ blocking = False
    $ moose_blocking = False
    $ charge = False








    hide screen day

    scene bg_k_battleground
    hide as_battle_small_01
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")

    ds "hello again, [povname]..."
    ds "remember me?"
    yna "... no?"
    ds "maybe from a dream...?"



    yna "oh, you're {i}that{/i} asshole."
    ds "you're not getting away this time, avatar."
    yna "I'm gonna shove my fist up your ass."
    ds "hahaha..."
    ds "you've got spirit, [povname]. but you won't beat me."
    yna "bring it, bitch!"
    if povname == "jack":

        show screen hp_bar10
        with Dissolve(0.5)
    else:

        show screen hp_bar1
        with Dissolve(0.5)








label fight_mainspirit1:
    if av_hp <= 300 and not d_flag_01:
        $ d_flag_01 = True
        y "{size=-4}{i}(i can't beat this guy!)"

    if moose_hp <= 300 and not d_flag_02:
        $ d_flag_02 = True

    call screen fight_buttonsspirit1






label mooses_turnspirit1:
    play sound "audio/hiss.wav"
    if charge:
        $ charge = False


        if blocking:
            $ blocking = False
            show as_battle_small_02 at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(.2)
            hide a_battle_small_01
            show a_battle_small_01_hurt at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
            with hpunch
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide a_battle_small_01_hurt
            show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            $ av_hp -= 300
            if av_hp < 50:
                jump avatar_lostspirit1

            jump fight_mainspirit1
        else:


            show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            show as_battle_small_02 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)

            hide a_battle_small_01
            show a_battle_small_01_hurt at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
            with hpunch
            hide a_battle_small_01_hurt
            show a_battle_small_01_hurt at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide a_battle_small_01_hurt
            show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            $ av_hp -= 300
            if av_hp < 50:
                jump avatar_lostspirit1

            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            jump fight_mainspirit1
    else:


        $ moose_blocking = False

        $ moose_decides = renpy.random.randint(1, 2)

        if moose_decides == 1:
            if blocking:
                $ blocking = False
                jump moose_attack_guardspirit1
            else:
                jump moose_attackspirit1

        elif moose_decides == 2:
            $ charge = True
            hide as_battle_small_01 with dissolve
            ds "you can't fight what you can't see!"

            jump fight_mainspirit1




label moose_attackspirit1:
    play sound "audio/hiss.wav"
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    hide as_battle_small_01
    show as_battle_small_02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01
    show a_battle_small_01_hurt at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=240, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide as_battle_small_02
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)



    $ av_hp -= 300
    if av_hp < 50:
        jump avatar_lostspirit1
    jump fight_mainspirit1



label moose_attack_guardspirit1:
    play sound "audio/hiss.wav"
    hide as_battle_small_01
    show as_battle_small_02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    hide as_battle_small_02
    show a_battle_small_01 at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
    with hpunch
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)

    $ av_hp -= 300
    if av_hp < 50:
        jump avatar_lostspirit1
    jump fight_mainspirit1



label avatar_attackspirit1:
    play sound "audio/knife.wav"
    if charge:
        show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide a_battle_small_01
        show a_battle_small_02 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.2)
        hide a_battle_small_02
        show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.2)
        ds "foolish avatar... you can't hurt me!"






        if charge:
            $ moose_hp -= 0
        else:
            $ moose_hp -= 0
        if moose_hp < 50:
            jump moose_lostspirit1
        jump mooses_turnspirit1
    else:


        show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide a_battle_small_01
        show a_battle_small_02 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide as_battle_small_01
        hide as_battle_small_02
        show as_battle_small_01_hurt at Position(xpos=700, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(0.02)
        hide as_battle_small_01_hurt
        show as_battle_small_01_hurt at Position(xpos=720, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide as_battle_small_01_hurt
        show as_battle_small_01_hurt at Position(xpos=700, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide as_battle_small_01_hurt
        show as_battle_small_01_hurt at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide as_battle_small_01_hurt
        show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide a_battle_small_02
        show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
        with Dissolve(.02)





        if charge:
            $ moose_hp -= 0
        else:
            $ moose_hp -= 0
        if moose_hp < 50:
            jump moose_lostspirit1
        jump mooses_turnspirit1




label potionspirit1:
    hide a_battle_small_01
    show a_battle_small_01_heal at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with dissolve
    hide a_battle_small_01_heal with dissolve
    $ renpy.play('audio/water.wav')
    $ potions -=1
    $ av_hp += 300
    if av_hp >= 1000:
        $ av_hp = 1000
    hide a_battle_small_01_heal
    jump mooses_turnspirit1






label main_attackspirit1:
    $ blocking = False
    if moose_blocking:
        $ moose_blocking = False
        pause 1
        jump moose_defendsspirit1
    else:
        jump avatar_attackspirit1

label main_blockspirit1:
    $ blocking = True

    jump mooses_turnspirit1

label main_potionspirit1:
    if potions >= 1:
        jump potionspirit1
    else:
        yna "Crap! I'm out of healing potions!"
        jump fight_mainspirit1








init -1:



    screen hp_bar10:
        if av_hp == 1000:
            add "battle/userinterface/hp_bar_02.png"
        if av_hp == 950:
            add "battle/userinterface/hp_bar_02.png" xpos -15 ypos 0
        if av_hp == 900:
            add "battle/userinterface/hp_bar_02.png" xpos -30 ypos 0
        if av_hp == 850:
            add "battle/userinterface/hp_bar_02.png" xpos -45 ypos 0
        if av_hp == 800:
            add "battle/userinterface/hp_bar_02.png" xpos -60 ypos 0
        if av_hp == 750:
            add "battle/userinterface/hp_bar_02.png" xpos -75 ypos 0
        if av_hp == 700:
            add "battle/userinterface/hp_bar_02.png" xpos -90 ypos 0
        if av_hp == 650:
            add "battle/userinterface/hp_bar_02.png" xpos -105 ypos 0
        if av_hp == 600:
            add "battle/userinterface/hp_bar_02.png" xpos -120 ypos 0
        if av_hp == 550:
            add "battle/userinterface/hp_bar_02.png" xpos -135 ypos 0
        if av_hp == 500:
            add "battle/userinterface/hp_bar_02.png" xpos -150 ypos 0
        if av_hp == 450:
            add "battle/userinterface/hp_bar_02.png" xpos -165 ypos 0
        if av_hp == 400:
            add "battle/userinterface/hp_bar_02.png" xpos -180 ypos 0
        if av_hp == 350:
            add "battle/userinterface/hp_bar_02.png" xpos -195 ypos 0
        if av_hp == 300:
            add "battle/userinterface/hp_bar_02.png" xpos -210 ypos 0
        if av_hp == 250:
            add "battle/userinterface/hp_bar_02.png" xpos -225 ypos 0
        if av_hp == 200:
            add "battle/userinterface/hp_bar_02.png" xpos -240 ypos 0
        if av_hp == 150:
            add "battle/userinterface/hp_bar_02.png" xpos -255 ypos 0
        if av_hp == 100:
            add "battle/userinterface/hp_bar_02.png" xpos -270 ypos 0
        if av_hp == 50:
            add "battle/userinterface/hp_bar_02.png" xpos -285 ypos 0
        if av_hp < 50:
            add "battle/userinterface/hp_bar_02.png" xpos -300 ypos 0
        add "battle/userinterface/hp_bar.png"

        add "battle/userinterface/hp_bar_attack_01.png"
        add "battle/userinterface/hp_bar_defend_01.png"
        add "battle/userinterface/hp_bar_item_01.png"

        if moose_hp == 1000:
            add "battle/userinterface/hp_bar_02_enemy.png"
        if moose_hp == 950:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 15 ypos 0
        if moose_hp == 900:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 30 ypos 0
        if moose_hp == 850:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 45 ypos 0
        if moose_hp == 800:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 60 ypos 0
        if moose_hp == 750:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 75 ypos 0
        if moose_hp == 700:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 90 ypos 0
        if moose_hp == 650:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 105 ypos 0
        if moose_hp == 600:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 120 ypos 0
        if moose_hp == 550:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 135 ypos 0
        if moose_hp == 500:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 150 ypos 0
        if moose_hp == 450:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 165 ypos 0
        if moose_hp == 400:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 180 ypos 0
        if moose_hp == 350:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 195 ypos 0
        if moose_hp == 300:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 210 ypos 0
        if moose_hp == 250:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 225 ypos 0
        if moose_hp == 200:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 240 ypos 0
        if moose_hp == 150:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 255 ypos 0
        if moose_hp == 100:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 270 ypos 0
        if moose_hp == 50:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 285 ypos 0
        if moose_hp < 50:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 300 ypos 0


        add "images/battle/userinterface/hp_bar_angryspirit.png"

    screen hp_bar1:
        if av_hp == 1000:
            add "battle/userinterface/hp_bar_02.png"
        if av_hp == 950:
            add "battle/userinterface/hp_bar_02.png" xpos -15 ypos 0
        if av_hp == 900:
            add "battle/userinterface/hp_bar_02.png" xpos -30 ypos 0
        if av_hp == 850:
            add "battle/userinterface/hp_bar_02.png" xpos -45 ypos 0
        if av_hp == 800:
            add "battle/userinterface/hp_bar_02.png" xpos -60 ypos 0
        if av_hp == 750:
            add "battle/userinterface/hp_bar_02.png" xpos -75 ypos 0
        if av_hp == 700:
            add "battle/userinterface/hp_bar_02.png" xpos -90 ypos 0
        if av_hp == 650:
            add "battle/userinterface/hp_bar_02.png" xpos -105 ypos 0
        if av_hp == 600:
            add "battle/userinterface/hp_bar_02.png" xpos -120 ypos 0
        if av_hp == 550:
            add "battle/userinterface/hp_bar_02.png" xpos -135 ypos 0
        if av_hp == 500:
            add "battle/userinterface/hp_bar_02.png" xpos -150 ypos 0
        if av_hp == 450:
            add "battle/userinterface/hp_bar_02.png" xpos -165 ypos 0
        if av_hp == 400:
            add "battle/userinterface/hp_bar_02.png" xpos -180 ypos 0
        if av_hp == 350:
            add "battle/userinterface/hp_bar_02.png" xpos -195 ypos 0
        if av_hp == 300:
            add "battle/userinterface/hp_bar_02.png" xpos -210 ypos 0
        if av_hp == 250:
            add "battle/userinterface/hp_bar_02.png" xpos -225 ypos 0
        if av_hp == 200:
            add "battle/userinterface/hp_bar_02.png" xpos -240 ypos 0
        if av_hp == 150:
            add "battle/userinterface/hp_bar_02.png" xpos -255 ypos 0
        if av_hp == 100:
            add "battle/userinterface/hp_bar_02.png" xpos -270 ypos 0
        if av_hp == 50:
            add "battle/userinterface/hp_bar_02.png" xpos -285 ypos 0
        if av_hp < 50:
            add "battle/userinterface/hp_bar_02.png" xpos -300 ypos 0
        add "battle/userinterface/hp_bar.png"
        add "battle/userinterface/hp_bar_attack_01.png"
        add "battle/userinterface/hp_bar_defend_01.png"
        add "battle/userinterface/hp_bar_item_01.png"

        if moose_hp == 1000:
            add "battle/userinterface/hp_bar_02_enemy.png"
        if moose_hp == 950:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 15 ypos 0
        if moose_hp == 900:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 30 ypos 0
        if moose_hp == 850:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 45 ypos 0
        if moose_hp == 800:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 60 ypos 0
        if moose_hp == 750:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 75 ypos 0
        if moose_hp == 700:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 90 ypos 0
        if moose_hp == 650:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 105 ypos 0
        if moose_hp == 600:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 120 ypos 0
        if moose_hp == 550:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 135 ypos 0
        if moose_hp == 500:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 150 ypos 0
        if moose_hp == 450:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 165 ypos 0
        if moose_hp == 400:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 180 ypos 0
        if moose_hp == 350:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 195 ypos 0
        if moose_hp == 300:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 210 ypos 0
        if moose_hp == 250:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 225 ypos 0
        if moose_hp == 200:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 240 ypos 0
        if moose_hp == 150:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 255 ypos 0
        if moose_hp == 100:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 270 ypos 0
        if moose_hp == 50:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 285 ypos 0
        if moose_hp < 50:
            add "battle/userinterface/hp_bar_02_enemy.png" xpos 300 ypos 0


        add "images/battle/userinterface/hp_bar_angryspirit.png"























screen fight_buttonsspirit1:
    imagemap:

        ground "battle/userinterface/androi_bk1_btle_butns_off.png"
        hover "battle/userinterface/androi_bk1_btle_butns_on.png"
        idle "battle/userinterface/androi_bk1_btle_butns_trnsp.png"


        hotspot (690, 570, 67, 147) action [Jump("main_attackspirit1")]
        hotspot (760, 570, 67, 147) action [Jump("main_blockspirit1")]
        hotspot (830, 570, 67, 147) action [Jump("main_potionspirit1")]





label moose_lostspirit1:

    show as_battle_small_01_hurt at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with flash
    hide as_battle_small_01_hurt
    hide screen hp_bar1
    hide screen hp_bar10

    hide as_battle_small_01 with dissolve
    hide as_battle_small_01_hurt
    hide as_battle_small_02
    jump fightspirit12




label avatar_lostspirit1:
    hide screen hp_bar1
    hide screen hp_bar10
    ds "this is the end for you, avatar."
    yna "..."
    yna "look over there!"
    ds "...what?"
    hide a_battle_small_01
    hide a_battle_small_01_hurt
    with flash
    ds "..."
    ds "tricky."
    ds "you can run..."
    hide bg_k_battleground
    hide as_battle_small_01
    hide as_battle_small_01_hurt
    hide as_battle_small_02

    stop music fadeout 2
    show kday with dissolve
    "you barely escape."
    yna "i've never run that fast in my life."
    yna "that spirit was fucking unbeatable."
    yna "i hope katara knows what she's doing."
    hide kday
    jump train_day
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
