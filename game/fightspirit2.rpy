label fightspirit2:
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
    show k_battle_small_01 at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")



    ds "you can run all you want, avatar, but there's no escape from me."
    yna "shut {size=+4}up!"
    yna "This time I'm kicking your {size=+4}ass!"
    ds "oh, i'm sure!"
    ds "you couldn't even touch me last time."
    ds "Leave now, and I'll let you live a little longer."
    k_p "*growl*"
    ds "my, my, aren't we feisty."
    ds "do you even know who this man is, dear?"
    yna "I'm done talking!"







    show screen hp_bar1
    with Dissolve(0.5)








label fight_mainspirit2:
    if av_hp <= 300 and not d_flag_01:
        $ d_flag_01 = True
        y "{size=+4}{i}I'm not done with you yet!"

    if moose_hp <= 300 and not d_flag_02:
        $ d_flag_02 = True
        $ potions +=1

    call screen fight_buttonsspirit2






label mooses_turnspirit2:
    play sound "audio/hiss.wav"
    if charge:
        $ charge = False


        if blocking:
            $ blocking = False
            show as_battle_small_02 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(.2)
            hide a_battle_small_01
            show a_battle_small_01_hurt at Position(xpos=240, ypos=430, xanchor="center", yanchor="center")
            hide k_battle_small_01
            show k_battle_small_01_hurt at Position(xpos=290, ypos=280, xanchor="center", yanchor="center")
            with hpunch
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            hide a_battle_small_01_hurt
            show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
            with Dissolve(0.02)
            hide k_battle_small_01_hurt
            show k_battle_small_01 at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
            with Dissolve(.02)
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)

            $ av_hp -= 150
            if av_hp < 50:
                jump avatar_lostspirit2

            jump fight_mainspirit2
        else:


            show as_battle_small_02 at Position(xpos=280, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(.2)
            hide a_battle_small_01
            show a_battle_small_01_hurt at Position(xpos=240, ypos=430, xanchor="center", yanchor="center")
            hide k_battle_small_01
            show k_battle_small_01_hurt at Position(xpos=290, ypos=280, xanchor="center", yanchor="center")
            with hpunch
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.02)
            hide a_battle_small_01_hurt
            show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
            with Dissolve(0.02)
            hide k_battle_small_01_hurt
            show k_battle_small_01 at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
            with Dissolve(.02)
            hide as_battle_small_02
            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            with Dissolve(0.2)
            $ av_hp -= 300
            if av_hp < 50:
                jump avatar_lostspirit2

            show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
            jump fight_mainspirit2
    else:


        $ moose_blocking = False

        $ moose_decides = renpy.random.randint(1, 2)

        if moose_decides == 1:
            if blocking:
                $ blocking = False
                jump moose_attack_guardspirit2
            else:
                jump moose_attackspirit2

        elif moose_decides == 2:
            $ charge = True
            hide as_battle_small_01 with dissolve
            ds "you can't fight what you can't see!"
            jump fight_mainspirit2




label moose_attackspirit2:
    play sound "audio/hiss.wav"
    show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
    show k_battle_small_01 at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    hide as_battle_small_01
    show as_battle_small_02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01
    show a_battle_small_01_hurt at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide k_battle_small_01
    show k_battle_small_01_hurt at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=240, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide k_battle_small_01_hurt
    show k_battle_small_01_hurt at Position(xpos=290, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=240, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide k_battle_small_01_hurt
    show k_battle_small_01_hurt at Position(xpos=290, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=240, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide k_battle_small_01_hurt
    show k_battle_small_01_hurt at Position(xpos=290, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01_hurt at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide k_battle_small_01_hurt
    show k_battle_small_01_hurt at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(.02)

    hide as_battle_small_02
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide a_battle_small_01_hurt
    show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(.02)
    hide k_battle_small_01_hurt
    show k_battle_small_01 at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(.02)


    $ av_hp -= 150
    if av_hp < 50:
        jump avatar_lostspirit2
    jump fight_mainspirit2



label moose_attack_guardspirit2:
    play sound "audio/hiss.wav"
    hide as_battle_small_01
    show as_battle_small_02 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    show a_battle_small_01 at Position(xpos=240, ypos=430, xanchor="center", yanchor="center")
    show k_battle_small_01 at Position(xpos=290, ypos=280, xanchor="center", yanchor="center")
    with hpunch
    show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    show k_battle_small_01 at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    with Dissolve(0.02)
    hide as_battle_small_02
    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with Dissolve(0.02)

    $ av_hp -= 0
    if av_hp < 50:
        jump avatar_lostspirit2
    jump fight_mainspirit2



label avatar_attackspirit2:
    play sound "audio/knife.wav"
    if charge:
        show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
        show k_battle_small_01 at Position(xpos=305, ypos=280, xanchor="center", yanchor="center")
        hide a_battle_small_01
        show a_battle_small_02 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
        with Dissolve(.03)
        hide k_battle_small_01
        show k_battle_small_02 at Position(xpos=305, ypos=280, xanchor="center", yanchor="center")
        with Dissolve(.03)
        hide a_battle_small_02
        show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
        with Dissolve(.03)
        hide k_battle_small_02
        show k_battle_small_01 at Position(xpos=305, ypos=280, xanchor="center", yanchor="center")
        with Dissolve(.03)
        ds "foolish avatar... you can't hurt me!"


        jump mooses_turnspirit2
    else:

        show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
        show k_battle_small_01 at Position(xpos=305, ypos=280, xanchor="center", yanchor="center")
        hide a_battle_small_01
        show a_battle_small_02 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide k_battle_small_01
        show k_battle_small_02 at Position(xpos=305, ypos=280, xanchor="center", yanchor="center")
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
        show a_battle_small_01 at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
        with Dissolve(.02)
        hide k_battle_small_02
        show k_battle_small_01 at Position(xpos=305, ypos=280, xanchor="center", yanchor="center")
        with Dissolve(.02)




        if charge:
            $ moose_hp -= 200
        else:
            $ moose_hp -= 150
        if moose_hp < 50:
            jump moose_lostspirit2
        jump mooses_turnspirit2




label potionspirit2:
    show a_battle_small_01_heal at Position(xpos=250, ypos=430, xanchor="center", yanchor="center")
    with dissolve
    show k_battle_small_01_heal at Position(xpos=300, ypos=280, xanchor="center", yanchor="center")
    with dissolve
    hide a_battle_small_01_heal with dissolve
    hide k_battle_small_01_heal with dissolve
    $ renpy.play('audio/water.wav')
    $ potions -=1
    $ av_hp += 300
    if av_hp >= 1000:
        $ av_hp = 1000
    hide a_battle_small_01_heal
    jump mooses_turnspirit2






label main_attackspirit2:
    $ blocking = False
    if moose_blocking:
        $ moose_blocking = False
        pause 1
        jump moose_defendsspirit2
    else:
        jump avatar_attackspirit2

label main_blockspirit2:
    $ blocking = True

    jump mooses_turnspirit2

label main_potionspirit2:
    if potions >= 1:
        jump potionspirit2
    else:
        yna "Crap! I'm out of healing potions!"
        jump fight_mainspirit2








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






















screen fight_buttonsspirit2:
    imagemap:

        ground "battle/userinterface/androi_bk1_btle_butns_off.png"
        hover "battle/userinterface/androi_bk1_btle_butns_on.png"
        idle "battle/userinterface/androi_bk1_btle_butns_trnsp.png"


        hotspot (690, 570, 67, 147) action [Jump("main_attackspirit2")]
        hotspot (760, 570, 67, 147) action [Jump("main_blockspirit2")]
        hotspot (830, 570, 67, 147) action [Jump("main_potionspirit2")]





label moose_lostspirit2:

    show as_battle_small_01 at Position(xpos=680, ypos=350, xanchor="center", yanchor="center")
    with flash
    hide screen hp_bar1
    hide screen hp_bar10
    ds "wait!"
    ds "don't kill me! I'll tell you everything!"
    k_p "aang..."
    ya "and in return?"
    ds "I'll leave and never come back."
    k_a "aang!"
    menu:
        "listen":
            y "go ahead."
            k_a "aang, no!"
            ds "i can see you're not only powerful, but wise as well."
            ds "the ritual is the source of the avatar's strength."
            ds "...but his ultimate downfall as well."
            y "that tattooed chick did say something about my predecessor dying..."
            ds "the first avatar united with Raava, an ancient spirit."
            ds "That spirit was the embodiement of all things that are good."
            ds "Primarily... *ptoo* love, ugh."
            ds "that union is the reason for the avatar's strength."
            ya "Get to the point before I turn you into a belt!"
            ds "Sex..."
            y "Okay, you've got my attention again."
            ds "Sex is the ultimate act of love..."
            ds "A short lived union of mind and flesh."
            ym "What about hate-fucking? That's a thing."
            ds "A broken, corrupted form, but in essence the same."
            ds "Gaining power, staying sane and more importantly..."
            ds "maintaining the balance in the world..."
            ds "without appeasing the ''good'' that your merge has made you the champion of, chaos reigns."
            ym "Fucking makes the world a better place? I'm ready to do my part!"
            ds "But as you age, fucking becomes your only desire and destroys your mind and body..."
            ds "Your human self can't keep up forever. "
            ds "With each incarnation the taint grows stronger."
            ym "Well, I {i}AM{/i} pretty perverted I guess..."
            k_a "You musn't believe this spirit Aang!"
            k_a "Whatever it says it's either a lie or a twisted half-truth!"
            ds "Lies? We all lie... Sometimes to ourselves. in little and big ways..."
            ds "Don't we Katara?"
            k_p "I... I have no idea what you're talking about..."
            ya "Enough with this shit already!"
            ya "Tell me something useful right now or I'll tie you into a fucking knot!"
            ds "Then let me tell you about the final part of the ritual."
            ds "And about the painted lady, your spirit guide..."
            y "what final part? what about the painted lady?"
            hide as_battle_small_01
            hide as_battle_small_01_hurt
            hide as_battle_small_02
            show background_fade_purpleish
            show pgfull with dissolve
            s "that's enough!"
            ya "Damnit! We were finally getting somewhere!"
            s "No, you're done listening."
            ya "you're not my real mom!"
            k_p "where... did that snake-like spirit go?"
            y "what?"
            ya "look what you did! It escaped!"
            s "avatar, you must focus on your mission!"
            y "which is?"
            s "you must keep training."
            y "for what?"
            s "you will find out soon enough."
            ya "that is a bullshit answer and you know it!"
            hide background_fade_purpleish
            hide pgfull with dissolve
            ya "Arrghh! I hate when you do that!"
            k_a "Why did you listen to that snake?"
            k_p "and... who was that shrouded woman?"
            y "Some ghost chick that bothers me from time to time."
            y "Seriously, I'm like a magnet for this sort of shit."
        "don't listen":

            yna "i'm not an idiot."
            yna "yippeekiyay mother fucker."
            ds "wait!"
            ds "the ''ritual'' is-"
            hide as_battle_small_01
            hide as_battle_small_01_hurt
            hide as_battle_small_02
            show background_fade_purpleish
            show pgfull with dissolve
            s "that's enough!"
            ya "Damnit! We were finally getting somewhere!"
            s "No, you're done listening."
            ya "you're not my real mom!"
            k_p "where... did that snake like spirit go?"
            y "what?"
            ya "look what you did! It escaped!"
            s "avatar, you must focus on your mission!"
            y "which is?"
            s "you must keep training."
            y "for what?"
            s "you will find out soon enough."
            ya "that is a bullshit answer and you know it!"
            hide background_fade_purpleish
            hide pgfull with dissolve
            ya "Arrghh! I hate when you do that!"
            k_a "Why did you listen to that snake?"
            k_p "and... who was that shrouded woman?"
            y "Some ghost chick that bothers me from time to time."
            y "Seriously, I'm like a magnet for this sort of shit."

    hide as_battle_small_01_hurt
    hide as_battle_small_01 with dissolve
    hide as_battle_small_01_hurt
    hide as_battle_small_02
    show kwp at Position (xpos = 0.9, xanchor=0.5, ypos=0.6, yanchor=0.5)
    with dissolve
    k "...I guess we won."
    k "well aang, you've learned how to fight spirits."
    k "hopefully you'll never need to use it again."
    hide kwp
    show kwe at Position (xpos = 0.9, xanchor=0.5, ypos=0.6, yanchor=0.5)
    with dissolve
    k "get some rest, you did well."
    hide kwe with dissolve
    hide bg_k_battleground
    $ katara_aff +=1
    jump tribe2



label avatar_lostspirit2:
    hide bg_k_battleground
    hide screen hp_bar1
    hide screen hp_bar10
    hide as_battle_small_01
    hide as_battle_small_01_hurt
    hide as_battle_small_02
    hide a_battle_small_01
    hide a_battle_small_01_hurt
    stop music fadeout 2
    scene black
    show pgfull with dissolve
    s "one more try, young avatar..."
    jump fightspirit2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
