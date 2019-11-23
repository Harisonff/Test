label stat_screen_fire_day:
    call screen stat_screen_fire_day

label stat_screen_fire_night:
    call screen stat_screen_fire_night

screen stat_screen_fire_day:
    add "letters/letter0.jpg"

    text "{color=#000000}battle rank:{/color}" xpos 250 ypos 200
    if fbattles <=5:
        text "{color=#000000}a baby turtle (1/3){/color}" xpos 450 ypos 200
    if fbattles ==6:
        text "{color=#000000}not very good, to be honest (1/3){/color}" xpos 450 ypos 200
    if fbattles ==7:
        text "{color=#000000}trying his best, bless him (1/3){/color}" xpos 450 ypos 200
    if fbattles >=8 and fbattles <=14:
        text "{color=#000000}captain (2/3){/color}" xpos 450 ypos 200
    if fbattles >=15:
        text "{color=#ffffff}general (3/3){/color}" xpos 450 ypos 200

    text "az. sluttiness:" xpos 250 ypos 250
    text "[aslut]/11" xpos 450 ypos 250

    text "az. public:" xpos 250 ypos 300
    if apublic <=7:
        text "prude (1/3)" xpos 450 ypos 300
    if apublic >=8 and apublic <=14:
        text "on display (2/3)" xpos 450 ypos 300
    if apublic >=15:
        text "sexhibitionist (3/3)" xpos 450 ypos 300

    text "morality:" xpos 250 ypos 350
    if morality >=0:
        text "[morality] (good)" xpos 450 ypos 350
    if morality <0:
        text "[morality] (evil)" xpos 450 ypos 350

    text "firebending:" xpos 250 ypos 400
    text "[firebending]/10" xpos 450 ypos 400

    if not amindbreak:
        text "???" xpos 250 ypos 450
    if amindbreak:
        text "{color=#0000ff}m{color=#faebd7}i{color=#b22222}n{color=#228b22}d{color=#ff00ff}b{color=#dda0dd}r{color=#ff69b4}o{color=#a9a9a9}k{color=#b0c4de}e{color=#008080}n" xpos 250 ypos 450

    textbutton "Return" action Jump("city") xpos 450 ypos 600

screen stat_screen_fire_night:
    add "letters/letter0.jpg"

    text "{color=#000000}battle rank:{/color}" xpos 250 ypos 200
    if fbattles <=5:
        text "{color=#000000}a baby turtle (1/3){/color}" xpos 450 ypos 200
    if fbattles ==6:
        text "{color=#000000}not very good, to be honest (1/3){/color}" xpos 450 ypos 200
    if fbattles ==7:
        text "{color=#000000}trying his best, bless him (1/3){/color}" xpos 450 ypos 200
    if fbattles >=8 and fbattles <=14:
        text "{color=#000000}captain (2/3){/color}" xpos 450 ypos 200
    if fbattles >=15:
        text "{color=#ffffff}general (3/3){/color}" xpos 450 ypos 200

    text "az. sluttiness:" xpos 250 ypos 250
    text "[aslut]/11" xpos 450 ypos 250

    text "az. public:" xpos 250 ypos 300
    if apublic <=7:
        text "prude (1/3)" xpos 450 ypos 300
    if apublic >=8 and apublic <=14:
        text "on display (2/3)" xpos 450 ypos 300
    if apublic >=15:
        text "sexhibitionist (3/3)" xpos 450 ypos 300

    text "morality:" xpos 250 ypos 350
    if morality >=0:
        text "[morality] (good)" xpos 450 ypos 350
    if morality <0:
        text "[morality] (evil)" xpos 450 ypos 350

    text "firebending:" xpos 250 ypos 400
    text "[firebending]/10" xpos 450 ypos 400

    if not amindbreak:
        text "???" xpos 250 ypos 450
    if amindbreak:
        text "{color=#0000ff}m{color=#faebd7}i{color=#b22222}n{color=#228b22}d{color=#ff00ff}b{color=#dda0dd}r{color=#ff69b4}o{color=#a9a9a9}k{color=#b0c4de}e{color=#008080}n" xpos 250 ypos 450

    textbutton "Return" action Jump("city_night") xpos 450 ypos 600



screen stats_fire_end:
    add "letters/letter0.jpg"

    text "{color=#000000}high morality ending scene:{/color}" xpos 250 ypos 200
    if morality >=1:
        text "{color=#000000}achieved!{/color}" xpos 650 ypos 200
    if morality <=0:
        text "{color=#000000}locked{/color}" xpos 650 ypos 200
        text "{color=#8b0000}do good deeds!{/color}" xpos 300 ypos 250

    text "{color=#000000}low morality ending scene:{/color}" xpos 250 ypos 300
    if morality <=-1:
        text "{color=#000000}achieved!{/color}" xpos 650 ypos 300
    if morality >=0:
        text "{color=#000000}locked{/color}" xpos 650 ypos 300
        text "{color=#8b0000}do bad deeds!{/color}" xpos 300 ypos 350

    text "cows escaped ending scene:" xpos 250 ypos 400
    if girls_guns:
        text "achieved!" xpos 650 ypos 400
    if not girls_guns:
        text "locked" xpos 650 ypos 400
        text "{color=#8b0000}let the cows keep the weapons!" xpos 300 ypos 450


    text "public ending scene:" xpos 250 ypos 500
    if apublic >=15:
        text "achieved!" xpos 650 ypos 500
    if apublic <15:
        text "locked" xpos 650 ypos 500
        text "{color=#8b0000}pass 15 judgements in the throne room!" xpos 300 ypos 550

    textbutton "Next" action Jump("worldmap3") xpos 450 ypos 600
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
