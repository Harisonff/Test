label fightuna2:
    stop music
    play music "audio/Prelude and Action.mp3"

    $ d_flag_01 = False
    $ d_flag_02 = False

    $ moose_hp = 1000

    $ blocking = False
    $ moose_blocking = False
    $ charge = False









    show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with dissolve
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")

    yna "Another one!?"
    play sound "audio/tiger.mp3"
    "mooselion" "aaahhrrhh!"
    yna "{size=-4}(...shit.){/size}"
    show screen hp_bar9
    with Dissolve(0.5)








label fight_mainuna2:
    if av_hp <= 300 and not d_flag_01:
        $ d_flag_01 = True
        yna "{size=+4}{i}I'm gonna eat your babies, you son of a bitch!"

    if moose_hp <= 300 and not d_flag_02:
        $ d_flag_02 = True
        yna "{size=-4}(He is getting weaker!){/size}"

    call screen fight_buttonsuna2





label mooses_turnuna2:
    play sound "audio/tiger.mp3"
    if charge:
        $ charge = False


        if blocking:
            $ blocking = False
            hide m_battle_stance02
            show m_battle_stance03 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide a_battle_small_01
            show a_battle_small_01_hurt at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
            with hpunch
            hide a_battle_small_01_hurt
            show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide m_battle_stance03
            show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            $ av_hp -= 50
            if av_hp < 50:
                jump avatar_lostuna2

            jump fight_mainuna2
        else:


            show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide m_battle_stance01
            show m_battle_stance02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide m_battle_stance02
            show m_battle_stance03 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide a_battle_small_01
            show a_battle_small_01_hurt at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
            with hpunch
            hide a_battle_small_01_hurt
            show a_battle_small_01_hurt at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide m_battle_stance03
            show m_battle_stance02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide a_battle_small_01_hurt
            show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide m_battle_stance02
            show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            $ av_hp -= 300
            if av_hp < 50:
                jump avatar_lostuna2
            hide m_battle_stance03
            show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            jump fight_mainuna2
    else:


        $ moose_blocking = False

        $ moose_decides = renpy.random.randint(1, 2)

        if moose_decides == 1:
            if blocking:
                $ blocking = False
                jump moose_attack_guarduna2
            else:
                jump moose_attackuna2

        elif moose_decides == 2:
            $ charge = True
            hide m_battle_stance01
            show m_battle_stance02 at Position(xpos=700, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(.02)





            jump fight_mainuna2




label moose_attackuna2:
    play sound "audio/tiger.mp3"
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    hide m_battle_stance01
    show m_battle_stance02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide m_battle_stance02
    show m_battle_stance03 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
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
    hide m_battle_stance03
    show m_battle_stance02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide m_battle_stance02
    show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)


    $ av_hp -= 100
    if av_hp < 50:
        jump avatar_lostuna2
    jump fight_mainuna2



label moose_attack_guarduna2:
    play sound "audio/tiger.mp3"
    hide m_battle_stance01
    show m_battle_stance02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    hide m_battle_stance02
    show m_battle_stance03 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    show a_battle_small_01 at Position(xpos=260, ypos=350, xanchor="center", yanchor="center")
    with hpunch
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    hide m_battle_stance03
    show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)

    jump fight_mainuna2



label avatar_attackuna2:
    play sound "audio/knife.wav"
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01
    show a_battle_small_02 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide m_battle_stance01
    hide m_battle_stance02
    show m_battle_small_01_hurt at Position(xpos=700, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    hide m_battle_small_01_hurt
    show m_battle_small_01_hurt at Position(xpos=720, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide m_battle_small_01_hurt
    show m_battle_small_01_hurt at Position(xpos=700, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide m_battle_small_01_hurt
    show m_battle_small_01_hurt at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide m_battle_small_01_hurt
    show m_battle_stance01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_02
    show a_battle_small_01 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)




    if charge:
        $ moose_hp -= 200
    else:
        $ moose_hp -= 100
    if moose_hp < 50:
        jump moose_lostuna2
    jump mooses_turnuna2




label potionuna2:
    show a_battle_small_01_heal at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
    with dissolve
    hide a_battle_small_01_heal with dissolve
    $ renpy.play('audio/water.wav')
    $ potions -=1
    $ av_hp += 500
    if av_hp >= 1000:
        $ av_hp = 1000
    jump mooses_turnuna2






label main_attackuna2:
    $ blocking = False
    if moose_blocking:
        $ moose_blocking = False
        pause 1
        jump moose_defendsuna2
    else:
        jump avatar_attackuna2

label main_blockuna2:
    $ blocking = True

    jump mooses_turnuna2

label main_potionuna2:
    if potions >= 1:
        jump potionuna2
    else:
        yna "Crap! I'm out of healing potions!"
        jump fight_mainuna2








init -1:



    screen hp_bar:
        if av_hp == 1000:
            add 'battle/userinterface/hp_bar_02.png'
        if av_hp == 950:
            add 'battle/userinterface/hp_bar_02.png' xpos -15 ypos 0
        if av_hp == 900:
            add 'battle/userinterface/hp_bar_02.png' xpos -30 ypos 0
        if av_hp == 850:
            add 'battle/userinterface/hp_bar_02.png' xpos -45 ypos 0
        if av_hp == 800:
            add 'battle/userinterface/hp_bar_02.png' xpos -60 ypos 0
        if av_hp == 750:
            add 'battle/userinterface/hp_bar_02.png' xpos -75 ypos 0
        if av_hp == 700:
            add 'battle/userinterface/hp_bar_02.png' xpos -90 ypos 0
        if av_hp == 650:
            add 'battle/userinterface/hp_bar_02.png' xpos -105 ypos 0
        if av_hp == 600:
            add 'battle/userinterface/hp_bar_02.png' xpos -120 ypos 0
        if av_hp == 550:
            add 'battle/userinterface/hp_bar_02.png' xpos -135 ypos 0
        if av_hp == 500:
            add 'battle/userinterface/hp_bar_02.png' xpos -150 ypos 0
        if av_hp == 450:
            add 'battle/userinterface/hp_bar_02.png' xpos -165 ypos 0
        if av_hp == 400:
            add 'battle/userinterface/hp_bar_02.png' xpos -180 ypos 0
        if av_hp == 350:
            add 'battle/userinterface/hp_bar_02.png' xpos -195 ypos 0
        if av_hp == 300:
            add 'battle/userinterface/hp_bar_02.png' xpos -210 ypos 0
        if av_hp == 250:
            add 'battle/userinterface/hp_bar_02.png' xpos -225 ypos 0
        if av_hp == 200:
            add 'battle/userinterface/hp_bar_02.png' xpos -240 ypos 0
        if av_hp == 150:
            add 'battle/userinterface/hp_bar_02.png' xpos -255 ypos 0
        if av_hp == 100:
            add 'battle/userinterface/hp_bar_02.png' xpos -270 ypos 0
        if av_hp == 50:
            add 'battle/userinterface/hp_bar_02.png' xpos -285 ypos 0
        if av_hp < 50:
            add 'battle/userinterface/hp_bar_02.png' xpos -300 ypos 0
        add 'battle/userinterface/hp_bar.png'
        add 'battle/userinterface/hp_bar_attack_01.png'
        add 'battle/userinterface/hp_bar_defend_01.png'
        add 'battle/userinterface/hp_bar_item_01.png'

        if moose_hp == 1000:
            add 'battle/userinterface/hp_bar_02_enemy.png'
        if moose_hp == 950:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 15 ypos 0
        if moose_hp == 900:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 30 ypos 0
        if moose_hp == 850:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 45 ypos 0
        if moose_hp == 800:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 60 ypos 0
        if moose_hp == 750:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 75 ypos 0
        if moose_hp == 700:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 90 ypos 0
        if moose_hp == 650:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 105 ypos 0
        if moose_hp == 600:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 120 ypos 0
        if moose_hp == 550:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 135 ypos 0
        if moose_hp == 500:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 150 ypos 0
        if moose_hp == 450:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 165 ypos 0
        if moose_hp == 400:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 180 ypos 0
        if moose_hp == 350:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 195 ypos 0
        if moose_hp == 300:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 210 ypos 0
        if moose_hp == 250:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 225 ypos 0
        if moose_hp == 200:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 240 ypos 0
        if moose_hp == 150:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 255 ypos 0
        if moose_hp == 100:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 270 ypos 0
        if moose_hp == 50:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 285 ypos 0
        if moose_hp < 50:
            add 'battle/userinterface/hp_bar_02_enemy.png' xpos 300 ypos 0


        add 'images/battle/userinterface/hp_bar_mooselion.png'






















screen fight_buttonsuna2:
    imagemap:

        ground "battle/userinterface/androi_bk1_btle_butns_off.png"
        hover "battle/userinterface/androi_bk1_btle_butns_on.png"
        idle "battle/userinterface/androi_bk1_btle_butns_trnsp.png"


        hotspot (690, 570, 67, 147) action [Jump("main_attackuna2")]
        hotspot (760, 570, 67, 147) action [Jump("main_blockuna2")]
        hotspot (830, 570, 67, 147) action [Jump("main_potionuna2")]




label moose_lostuna2:

    show m_battle_small_01_hurt at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with flash
    hide m_battle_small_01_hurt with dissolve
    hide screen hp_bar9
    hide m_battle_stance01
    hide m_battle_small_01_hurt
    hide m_battle_stance02
    hide a_battle_small_01
    hide a_battle_small_01_hurt
    stop music fadeout 2
    y "no kid..."
    hide bg_k_battleground
    $ una_unlock +=1
    $ villagefavors +=1
    scene kday with dissolve
    play music "audio/Bumba Crossing.mp3"
    show um1 at Position(xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
    with dissolve
    ya "una, i'm sorry... I couldn't find the kid."
    st "oh, uh..."
    st "turns out she was just in the bathroom, sorry about that."
    ya "..."
    st "anyway, as a thank you for your help, take this!"
    "you got 100 coins!"
    $ money +=100
    ync "where'd you get this?"
    st "parents donate it for school supplies, but..."
    st "i just use it to buy weed."
    y "nice."
    hide um1 with dissolve
    play sound "audio/win2.mp3"
    "you completed a favor, the village likes you more!"
    jump day_time




label avatar_lostuna2:
    hide bg_k_battleground
    hide screen hp_bar9
    hide m_battle_stance01
    hide m_battle_small_01_hurt
    hide m_battle_stance02
    hide a_battle_small_01
    hide a_battle_small_01_hurt
    stop music fadeout 2
    show kday with dissolve
    yna "okay, i need to stock up on potions before I try that again."
    hide kday
    $ lostkid = False
    jump day_time
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
