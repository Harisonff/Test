screen bk4_money_date:
    add "calender_and_money.png"

    hbox:
        xalign 0.6
        yalign 0.02
        text "[bk4_money]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[bk4_calendar]"


screen bk4_money_date2:
    add "calender_and_money.png"

    hbox:
        xalign 0.6
        yalign 0.02
        text "[bk4_money]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[bk4_calendar]"

    if probending_available ==2 and probending_time <5:
        add "misc/star1.png":
            xalign 0.75 yalign 0.0
    if probending_available ==2 and probending_time >=5:
        imagebutton idle "misc/star2.png" hover "bk4_xtra/remove/star3.png" xalign 0.75 yalign 0.0 action Jump("bk4_probending") focus_mask True


screen korra_stats:
    frame:
        xminimum 1000 yminimum 720 xalign .5 yalign .5
        has vbox:
            xalign .5 yalign .5
        text "{size=+20}resistance: [korra_resist]"
        text "{size=+20}morality: [korra_moral]"
        if korra_mad ==0:
            text "{size=+20}status: happy"
        if korra_mad ==1:
            text "{size=+20}status: unhappy"
        if korra_mad ==2:
            text "{size=+20}status: angry"
        if korra_mad >=3:
            text "{size=+20}status: furious"

label bk4_next:
    scene black with Dissolve(1)
    $ b4_daytime = True
    $ bk4_calendar += 1
    $ b4_music_day_on = False
    $ pema_hj_daily = False
    $ bk4_coins_daily = False
    $ bk4_training_daily = False
    $ bk4_meditation_daily = False
    $ probending_time +=1
    $ korra_leg_daily = False
    $ korra_wash_daily = False
    if korra_boobjob >=3 and meet_kyoshi ==0:
        $ meet_kyoshi = 1
        jump b4_meet_kyoshi
    if korra_mad >=1:
        $ korra_mad -=1
    if korra_pb_chat >=2 and lin_hj2 and korra_wash ==0:
        jump korra_washroom
    if missing_meelo <6:
        jump bk4_your_room1
    else:
        jump b4_airtemple_map1

label b4_s_main:
    stop music fadeout 2
    scene black with Dissolve(2)
    play music "audio/(Orchestral) Playful Tension by Shadow16nh.mp3"

    show expression "bk4/painted_lady/pfull.png"
    with Dissolve(2.0)
    b4_sp "Okay, time for our last trip."
    menu:
        "slave route":
            $ bk4_route = 'slave'
            pass

    b4_sp "Are you ready?"
    b4_yn "man, have i ever been ready?"
    b4_yn "i miss my computer."
    b4_yn "you know what a computer is?"
    b4_yn "it's a magic box where I can play games and look at sluts."
    b4_sp "but... you do that {i}now{/i}."
    b4_ys "yeah, but i have to work for it."
    b4_sp ".........."
    b4_sp "....let's play a game."
    b4_yn "okay..."
    b4_sp "how many fucks am i holding?"
    b4_yn "....."
    b4_sp "come on, play."
    b4_yn "....i don't want to."
    b4_sp "it'll be fun."
    b4_sp "how many?"
    b4_yn "....none."
    b4_sp "none! that's right!"
    b4_sp "that's how many fucks i can give!"
    b4_yn "this is a terrible game."
    b4_sp "once again, count the fucks!"
    b4_yn "....you've gotten sassier."
    b4_sp "your culture is... influencial."
    b4_yn "alright, well, since I'm not ready, and you don't care...."
    b4_yn "Whose body am I going to possess this time?"
    b4_sp "You'll see."
    b4_ya "No, no, no."
    b4_ya "I want a name and description first."
    b4_sp "Do you like watertribe girls?"
    b4_ys "Yeah, but what has that got to do with..."
    play sound "audio/whoosh.wav"
    show expression "bk4/painted_lady/pfull.png" at Move((0.0, 0.0), (-0.3, 0.2), 0.4, bounce = True)
    pause(0.5)
    show expression "bk4/painted_lady/pfull.png":
        xzoom 1.0 yzoom 1.0
        linear 3.0 xzoom 0.2 yzoom 0.2 xpos 1000
    b4_ya "oof!"
    b4_sp "And off you go!"
    hide expression "bk4/painted_lady/pfull.png"
    with dissolve
    play sound "audio/whoosh.wav"
    show expression "bk4_xtra/remove/worldmap_01.jpg":
        xpos 0.0 ypos 0.0
        zoom 0 rotate 00.0 subpixel True
        ease 10 zoom 10 rotate 150.0
    "The spirit gives you a sudden shove and you fly off to a small village."
    b4_ya "Fuuuuuuccccckkk!!!!!"


    play sound "audio/thud.mp3"
    show expression "bk4/backgrounds/watertribe_village_1.jpg" with vpunch
    $ renpy.pause(0.5)

    show expression "bk4/korra/chibi/white_lotus.png"
    with Dissolve(1.5)
    "So what makes you think your daughter is the one?"

    b4_senna_n "....what?"
    b4_senna_n "Are you... are you talking to me?"
    wl "ugh, attention seekers like you disgust me."
    wl "you bring us all the way out here with false promises of the avatar to-"
    b4_senna_n "....what?"
    b4_senna_n "Sorry, no, just... give me a second to get my bearings."
    b4_senna_n "Some asshole pushed me... and..."
    b4_senna_n "....my chest feels heavy?"
    wl "*ahem* well, that's... are you trying to... seduce us?"
    b4_senna_n "seduce... no, you weirdo! Do i look like a woman to you?"
    wl "i'm... confused."
    b4_senna_n "i feel like I'm... missing something... but I can't put my finger on it."
    b4_senna_n "Wait a minute..."
    b4_senna_n "am I a woma-"
    play sound "audio/thud.mp3"
    show expression "bk4/backgrounds/watertribe_village_1.jpg" with hpunch
    b4_senna_n "...What's that sound?"
    hide expression "bk4/korra/chibi/white_lotus.png" with Dissolve(1.5)

    show expression "bk4/backgrounds/watertribe_village_1.jpg" with hpunch
    $ renpy.pause (.5,hard=True)

    show expression "bk4/backgrounds/watertribe_village_2.jpg":
        ypos 0

    play sound "audio/thud.mp3"
    show expression "bk4/korra/chibi/wallpiece.png" at Move((0.0, 0.0), (0.9, 0.9), 0.5 )
    $ renpy.pause(0.5,hard=True)
    show bfab bfab50 with dissolve
    "I'm the avatar!"
    window hide
    play sound "audio/whoosh.wav"
    show bfab bfab51 at Move((0.0, 0.0), (-0.03, 0.0), 0.3, bounce = True)
    show expression "bk4/korra/chibi/fire.png" at Move((0.4, 0.4), (-0.3, 0.4), 0.8 )
    $ renpy.pause(0.4,hard=True)
    play sound "audio/whoosh.wav"
    show bfab bfab52 at Move((0.0, 0.0), (-0.03, 0.0), 0.3, bounce = True)
    show expression "bk4/korra/chibi/fire.png" at Move((0.35, 0.35), (-0.3, 0.4), 0.8 )

    $ renpy.pause (0.8,hard=True)
    play sound "audio/water2.wav"
    show bfab bfab51 at Move((0.1, 0.0), (0.12, 0.0), 0.3, bounce = True):
        xzoom -1.0
    show expression "bk4/korra/chibi/water.png" at Move((0.5, 0.4), (1.5, 0.4), 0.8 )
    $ renpy.pause(0.4,hard=True)
    play sound "audio/water2.wav"
    show bfab bfab52 at Move((0.1, 0.0), (0.12, 0.0), 0.3, bounce = True):
        xzoom -1.0
    show expression "bk4/korra/chibi/water.png" at Move((0.5, 0.4), (1.5, 0.4), 0.8 )

    $ renpy.pause (0.8,hard=True)
    hide bfab
    play sound "audio/earthquake.mp3"
    show bfab bfab50 at Move((0.0, 0.05), (0.0, 0.0), 0.3, bounce = True)
    show expression "bk4/korra/chibi/earth.png" at Move((0.6, 1.0), (0.6, 0.4), 0.8 )
    $ renpy.pause (0.8,hard=True)

    "You gotta deal with it!"
    hide expression "bk4/korra/chibi/earth.png" with Dissolve(2.0)

    b4_senna_n "Wow, that kid's really...."

    menu:
        "Annoying":
            b4_senna_n "...did she just demolish a wall so she could show off!?"
            b4_senna_n "is this my house?"
            b4_senna_n "did she demolish a wall in my house?"
            b4_senna_n "Am I the only one who thinks that's not okay?"
            wl "....."
            wl "i mean..."
            b4_senna_n "Okay... I guess I'll have to be the adult here."
            b4_senna_n "Go get daddy's belt, dear... it's for your own good."
        "Adorable":
            b4_senna_n "cute!"
            b4_senna_n "Aaaww!"
            b4_senna_n "who's a cutie pie? who's the cutest pie!"
            b4_senna_n "a little pumpkin pie? a little pumpkin?"
            b4_senna_n "who's a pumpkin! you are! yes, you are!"
            wl "i... should we go, or...?"
            b4_senna_n "Come here and give me a hug!"

    show expression "bk4/korra/chibi/white_lotus.png"
    hide bfab
    with Dissolve(1.5)

    wl "Ahum... we're convinced she's the avatar."
    b4_senna_n "....you don't say!"
    b4_senna_n "What tipped you off?"
    b4_senna_n "was it the firebending?"
    b4_senna_n "how about the earthbending?"
    b4_senna_n "did the earthbending tip you off?"
    wl "well, together they-"
    b4_senna_n "Wait, no, shut up."
    b4_senna_n "There's something more important I have to deal with first."
    b4_senna_n "{size=+30}SPIIRIIIITT!!!!{/size}" with hpunch


    show expression "bk4_xtra/remove/blackveil.png" with Dissolve(1)
    show expression "bk4/painted_lady/pfull.png"
    with Dissolve(1.5)
    b4_sp "hey, what are you doing here?"
    b4_sp "this is the wrong time."
    b4_senna_n "oh, is it? is it the wrong time?"
    b4_senna_n "my bad, i didn't mean to go to the wrong-"
    b4_senna_n "{size=+30}just fix it!!" with hpunch
    b4_sp "...Ooops."
    b4_sp "right."
    b4_sp "Sorry, I messed up."
    b4_yds "........"

    b4_senna_n "Get me the fuck out of here."
    b4_sp "Sure, sure."
    scene black with Dissolve(2.0)
    show expression "bk4/painted_lady/pfull.png" with Dissolve(2.0)
    b4_ya "What the fuck were you trying to do?"
    b4_sp "I thought I saw the dreamstealer and had to move quickly."
    b4_sp "she is... different now."
    b4_sp "I don't know what happened, but she is... stronger."
    b4_yn "i... don't know anything about that?"
    b4_yn "(please believe me....)"
    b4_sp "you should be wary of her."
    b4_yn "right."
    b4_sp "in any case... my aim was completely off..."
    b4_ya "I... don't think I believe you."
    b4_sp "Think what you will."
    b4_sp "I am low on energy, so we will have to be more careful with the next try."
    b4_yn "Who was that girl?"
    b4_sp "Avatar korra."
    b4_yn "Oh... so that's why you asked whether I liked watertribe girls."
    b4_ys "Well I do, but..."
    b4_yn "...not when they're that young."
    b4_yn "Also... Korra is a bit of an odd choice to teach me airbending."
    b4_yn "As far as I can remember, she had a really hard time learning it herself."
    b4_yn "right?"
    b4_sp "uhhhh...."
    b4_yn "Well, she was too young here, so I'm guessing you were at least a decade off with your time travel stuff."
    b4_sp "uhhhh...."
    b4_yn "But that wasn't the only mistake you made...."
    b4_sp "........"
    b4_yn "........."
    b4_ya "You bitch!"
    b4_ya "You were trying to put me in Korra's body!!!" with hpunch
    b4_sp "See! that's why I didn't say anything!"
    b4_sp "I knew you'd be touchy about this!"
    b4_ya "I am {i}not{/i} going into a girl's body!"
    b4_ys "I mean... I will..."
    b4_ya "but not the way you want me to!"
    b4_sp "Why not?"
    b4_sp "It's perfect!"
    b4_sp "She already knows water, earth, and fire bending, but knows nothing of airbending!"
    b4_sp "Okay, she needs to be a bit older, but other than-"
    b4_ya " I can't fuck girls without a dick!!"
    b4_sp "ugh, typical... I bet you think penetration is the only qualifier for sex."
    b4_sp "don't be narrow-minded."
    b4_ya "I'm not narrow-mi... i'm not letting you genderbend me!!"
    b4_sp "Don't be an ass!"
    b4_sp "We've arrived at the right time."
    b4_sp "Get into her body willingly and learn airbending!"
    b4_ya "{size=+15}NO!"
    b4_sp "I don't have enough energy for another trip!"
    b4_sp "Do as I say!"
    b4_ya "Make me!"
    b4_sp "You ungrateful piece of... plenty of people would be elated to take over a girl's body!!"
    b4_sp "Think... think of the sick shit you can do with it!"
    b4_yn "...like what?"
    b4_sp "uhhh... you could take pictures of yourself while doing sex stuff and bury them somewhere only you know of."
    b4_sp "Dig them up again in your own time and sell them for an incredible profit!!"
    b4_yn "That's... that's actually not a bad idea."
    b4_yn "Why didn't I think of this before?"
    b4_sp "see?"
    b4_sp "so...?"
    b4_ya "still no!"
    b4_ya "no dick, no deal."
    b4_sp "...Okay I see we'll have to do this the hard way."
    b4_ya "I like doing it the \"hard\" way... which is why I need a dick!"
    b4_ya "{size=+15}so no female hosts!"
    b4_sp "If you resist, there's no telling where you'll end up, so I suggest you hold veeerrry still."
    "You start performing jumping jacks while sticking out your tongue."
    b4_sp "RAAaah!! You're infuriating! Screw this!"
    play sound "audio/air.wav"
    show expression "bk4/painted_lady/pfull.png" at Move((0.0, 0.0), (-0.3, 0.2), 0.4, bounce = True)
    pause(0.5)
    show expression "bk4/painted_lady/pfull.png":
        xzoom 1.0 yzoom 1.0
        linear 3.0 xzoom 0.2 yzoom 0.2 xpos 1200
    b4_sp "This is on you, avatar! Sink or swim!!"
    b4_ya "Fuck-fuck-fuck!!"
    "You fly backwards at an alarming speed."
    b4_ya "Pleasenotagirl\nPleasenotagirl\nPleasenotagirl\nPleasenotagirl..."

    show expression "bk4/world_maps/sea_blue.jpg" with Dissolve(1.5)

    play sound "audio/whoosh.wav"
    show expression "bk4/world_maps/airtemple_solo.png":
        xanchor 0.4 yanchor 0.2 xpos 500 ypos 200 xzoom 0.01 yzoom 0.01

        easeout 7.0 rotate 1100 xzoom 4.0 yzoom 4.0 ypos -600 xpos 0

    $ renpy.pause(2.0, hard = True)
    b4_ya "i'm gonna throw up!!!!{w=2.0} {nw}"
    b4_yc "here it comes!!!{w=2.0} {nw}"
    $ renpy.pause (0.8,hard=True)
    scene

    play sound "audio/thud.mp3"
    show expression "bk4/backgrounds/tenzin_room_day.jpg" at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    $ renpy.pause(1.5,hard=True)
    scene
    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    y4 "{size=+15}bllauugharrhgh" with hpunch
    y4 "haghhh... hghh... aghh... uhgh..."
    y4 "okay..."
    y4 "okay... I'm... i think i'm..."
    y4 "i think i-"
    y4 "{size=+15}bllauugharrhghagaghahhagahhhghbalgjaghlalghagl" with sshake
    y4 "....uuughhhh...."
    y4 "i think... i threw up... on the {i}inside{/i}..."
    y4 "my life... is an existential nightmare... from which there is no escape..."
    y4 "breathe... breathe... i'm okay... i'm okay..."
    y4 "i'm... where am i?"
    show bfae jinora01 as kid1 at Move((-1.0, 0.0), (0.0, 0.0), 0.7)
    b4_cn "hey dad! Can you take me to the zoo?"
    y4 "wha... who's what now?"
    y4 "*burp*"
    y4 "ughhhh...."
    show bfae ikki01 as kid2 at Move((-1.0, 0.0), (0.0, 0.0), 0.7)
    b4_cn "I want candy!!"
    y4 "don't... don't talk..."
    show bfae meelo_01 as kid3 at Move((-1.0, 0.0), (0.0, 0.0), 0.7)
    b4_cn "Raaaaawr!!"
    show bfae jinora01 as kid1 at Move((0.0, 0.0), (-0.3, 0.0), 2.0, bounce=True, repeat=True)
    show bfae ikki01 as kid2 at Move((0.0, 0.0), (-0.3, 0.0), 1.0, bounce=True, repeat=True)
    show bfae meelo_01 as kid3 at Move((0.0, 0.0), (-0.3, 0.0), 0.7, bounce=True, repeat=True)
    b4_cn "candy! zoo! Raaawr!!!"
    y4 "haghh... stop..."
    y4 "gonna... be sick..."
    show bfac bfac01 behind kid1, kid2, kid3 at Move((0.5, 0.0), (0.0, 0.0), 3.0)




    pn "Kids! please calm down."

    b4_cn "{size=+15}CANDY!! ZOOO!!! RAAAWWWR!"
    y4 "who are you people?"

    hide bfac
    show bfac bfac03 behind kid1, kid2, kid3 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    hide kid1
    hide kid2
    hide kid3
    show bfae group01 at Move((0.3, 0.0), (-0.1, 0.0), 2.0)

    pn "{size=+10}I said calm the fuck down!!{/size}" with vpunch
    y4 "....thanks."
    show bfac bfac02
    pn "There, that's better."
    show ctc
    pause
    hide ctc
    y4 "....that is better, actually."
    pn "Now come here and say sorry to your dad."
    y4 "their... their what?"
    show bfae group02 at Move((-0.2, 0.0), (0.0, 0.0), 2.0) with Dissolve(1.5)
    b4_cn "Sorry dad!"
    show bfae group03 at Move((0.0, 0.0), (0.0, 0.0), 2.0)
    with dissolve
    pn "your father likes a calm energy in the house... doesn't he?"
    b4_cn "yes, momma!"

    pn "Why don't you three go and help feed the skybisons?"
    b4_cn "Okay mom!"
    hide bfae
    with Dissolve(1.5)
    pn "they're sweet, but... troublesome sometimes."
    pn "oh, look at you! you've gone all pale!"
    "you glance at yourself in a mirror across the room."
    "you seem a bit older, with blue arrows on your face."
    tn "uh... what."
    show bfac bfac06 with dissolve
    pn "are you alright?"
    tn "...too soon to tell, i think."
    show bfac bfac02
    pn "Well honey, I've got things to do as well so..."
    tn "(...honey?)"
    "You look at the woman in front of you."
    show expression "bk4/backgrounds/tenzin_room_day.jpg" at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    show bfac bfac02 at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    pause(4.0)
    pn "It's been a while since you gave me that look."
    tn "uh, what look?"
    pn "The kind you give me when you want to knock me up."
    tn "That's... a good thing right?"
    pn " I can only have one baby at a time, dear..."
    pn "...but we can test that theory later, hmm?"
    tn "...oh, dang."
    pn "but like i said, i'm busy at the moment, so hold onto that thought."
    tn "uh... will do?"
    "she blows you a kiss as she walks out the door."
    hide bfac with Dissolve(2.0)
    tn "Okaaay."
    tn "apparently i have kids."
    tn "{i}that's{/i} a new one."
    tn "and a wife. that's also new."
    tn "The good news is that I didn't lose my memory this time."
    tn "Let's see, what else?"
    tn "I have a dick, {i}that's{/i} something i'm not going to take for granted..."
    tn "and judging by those kids and the pregnant state of that woman..."
    tn "my dick's in perfect working condition."
    tn "also not taking that for granted."
    tn "But who the hell am I supposed to be?"
    tn "I have blue arrow tattoos, but.... does that mean I'm in the body of the avatar again?"
    tn "am i... old aang?"

    show bfac bfac02 with dissolve

    pn "oh, tenzin! i almost forgot!"
    tn "(i guess my name is tenzin?)"
    pn "korra's been arrested."
    tn "and why should i care about-"
    tn "wait... {i}korra?"
    tn "as in... {i}avatar{/i} korra?"
    tn "(i'm trying to get in korra's pants? that's like... my pants.)"
    tn "(am i... going to... fuck myself?)"
    tn "(she's an earlier incarnation of me, so...)"
    tn "(i mean i masturbate constantly, but this is a new one, even for me.)"
    tn "(aaaaand morally adjusted.)"
    pn "as in... the one you've known since she was a kid, yes."
    tn "i have?"
    show bfac bfac06 with dissolve
    pn "...are you okay, dear?"
    tn "rarely."
    tn "why has she been arrested?"
    tn "she's the avatar!"
    tn "...can she even be arrested?"
    show bfac bfac02
    pn "my love, all i know is that she's been arrested by Lin."
    pn "she's at police headquarters."
    tn "...lin?"
    show bfac bfac06 with dissolve
    pn "what's going on with you?"
    pn "lin beifong."
    pn "chief of police for republic city."
    pn "you know... where we live?"
    show bfac bfac02
    pn "well, we live on air temple island, but, you know..."

    pn "same thing."

    tn "(republic city!?)"
    b4_ts "(that means i'm home!)"
    b4_ts "(sure, if korra's here, then it's a republic city from way before I was born, but it's an improvement!)"
    pn "are you alright?"
    b4_ts "are you kidding?"
    b4_ts "i'm better than alright!"
    b4_ts "i finally feel like i belong!"
    pn "belong...?"
    pn "of course you belong!"
    pn "you're on the ruling council of the city, love!"
    pn "you don't just belong, you are {i}powerful{/i}."
    tn "...that is all happy news."
    pn "i'm glad, honey."
    pn "now go get that slut-in-training out of jail."
    tn "....\"slut-in-training\"?"
    pn "oh, you know my opinion, dear."
    show bfac bfac03 with dissolve
    pn "some new little {i}bitch{/i} comes into town thinking she's hot stuff and everyone fawns all over her."
    pn "she doesn't know the first thing about pleasing a man."
    pn "i bet she doesn't even know how to successfully slobber out a man's cum."
    pn "i could show these {i}fanboys{/i} a thing or two."
    tn "you... could?"
    pn "of course!"
    show bfac bfac02 with Dissolve(1)
    pn "fortunately for me, the only man i've ever been with is a wonderful lover."
    pn "and i am absolutely infatuated with him and his cock..."
    tn "just to be clear... you mean me, right?"
    pn "yes, silly."
    pn "why do you think i've let you breed me? so frequently and repeatedly?"
    pn "i can't imagine anyone fucking me the way you do."
    show bfac bfac02a with dissolve
    pn "sometimes... i can't believe how perfect my life is."
    pn "three wonderful children... and a mildly insatiable man... *sigh...*"
    pn "it really doesn't get any better..."
    tn "...did you just call me \"mildly insatiable\"?"
    tn "what the hell does that mean?"
    show bfac bfac02 with dissolve
    pn "hmm?"
    pn "oh, we both know i have a higher sex drive than you, dear."
    pn "i've tried to ease off, as you've asked."
    pn "but don't worry, that's what masturbation is for!"
    tn "i... asked you to have less sex with me?"
    pn "well, yes."
    pn "but it doesn't matter!"
    pn "i love our relationship, and our life together..."
    tn "that sounds... like i'm an idiot."
    tn "am i an idiot?"
    pn "no dear, just very serious."
    pn "you're a man of responsibilites."
    pn "and i understand."
    pn "now, go get korra!"
    tn "alright..."
    pn "good."
    pn "oh, and then come back and drench my face in your ball milk, okay?"
    tn "i..."
    pn "only if you don't mind."
    pn "good luck, sweetie!"
    hide bfac with dissolve
    tn "....well, there's nothing better than a personal milf."
    tn "i'm definitely going to take her up on that."
    tn "...i wish i'd gotten her name, though."
    tn "that's a recipe for awkward."
    tn "also... what kind of asshole asks for {i}less{/i} sex from his wife?"
    tn "an idiot, that's who."
    tn "things are going to start changing around here."
    tn "but first i guess i need to go get korra out of the police station."
    tn "*sigh...*"
    tn "it's never easy."
    tn "well... let's step out of this room and see where the hell i am."
    tn "....here we go."
    tn "into a bright new adventure."
    stop music fadeout 1.5
    scene black with Dissolve(1.5)
    play music "audio/bounce_town.mp3"
    scene expression "bk4/world_maps/airtemple_day.jpg"
    with Dissolve(1.5)
    tn "air temple island!"
    tn "man... it's different than back home, but... close enough."
    tn "i guess this is my island."
    tn "or... tenzin's anyway."
    tn "which is apparently me."
    tn "i suppose the tattoos on my face mean i'm an airbender, which makes sense..."
    tn "the name is familiar, too."
    tn "i'm sure someone will tell me who the hell i am, eventually."
    tn "alright, time to go find some bitches."
    tn "bit of a weird start, but i'm gonna start finding some sluts or my name isn't... whatever it is."
    tn "tenzin. yeah."
    tn "go me."
    jump b4_airtemple_map1

label korra_arrested:
    $ korra_jail = True
    scene black with dissolve
    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0
    show bfaa bfaa01
    with Dissolve(1.5)
    lin "councilman... tenzin."
    show ctc
    pause
    hide ctc
    tn "well... that sounds ominous."
    tn "....."
    tn "...did the soundtrack just change?"
    tn "............."
    tn "what that thang do, girl?"
    lin "hmph, i suppose i know why you're here."
    lin "your... protege was caught doling out vigilante justice today."
    tn "you mean... normal avatar justice?"
    lin "no."
    hide bfaa with Dissolve(1)
    show bfaa bfaa00 with Dissolve(1)
    lin "I mean reckless, destructive, thoughtless actions brought on by a naive little girl who believes rules don't apply to her."
    tn "that's... probably a little harsh."
    lin "is it?"
    lin "then why does my city have a bunch of busted up shops, and wounded police?"
    tn "probably because you tried to fight the avatar."
    lin "tenzin..."
    lin "*sigh...*"
    lin "i know that aang being your father has given you a certain... respect for the avatar."
    tn "(oh, shit! that's how i know tenzin! he was aang's son!)"
    lin "hey!" with hpunch
    lin "pay attention!"
    tn "what? sorry."
    lin "tenzin..."
    hide bfaa with Dissolve(1)
    show bfaa bfaa03 with Dissolve(1)
    lin "what is korra doing in my city?"
    show ctc
    pause
    hide ctc
    tn "uhh..."
    lin "i thought you were going to go down to the south pole to train her?"
    tn "that's... definitely... a plan..."
    show bfaa bfaa02 with dissolve
    lin "i have my hands full at the moment as it is..."
    lin "i don't need some self-righteous little..."
    show expression "bk4/backgrounds/police_hq_desk.jpg" at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    show bfaa bfaa03 at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    show ctc
    pause(4.0)
    hide ctc
    lin "...little..."
    lin "what the..."

    scene
    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0
    show bfaa bfaa03
    lin "are you..."
    show bfaa bfaa04 with hpunch
    lin "tenzin!"
    lin "are... are you checking me out?"
    tn "what? me?"
    tn "......"
    tn "yes."
    show bfaa bfaa09 with dissolve
    lin "oh."
    lin "i... uh..."
    tn "i don't normally go for older broads, but with you i'd make an exception."
    tn "you are keeping it {i}tight{/i}."
    tn "that chest would make a pirate jealous."
    lin "well... that is... i... ah..."
    lin "...."
    show bfaa bfaa04 with hpunch
    lin "you...!"
    lin "you... made your choice!"
    tn "...what?"
    tn "...was it the pirate line?"
    tn "because i'll admit i could have probably chosen a better-"
    show bfaa bfaa05 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "you chose {i}pema{/i}."
    lin "you're a fucking asshole, and you broke my heart."
    lin "and i want you to get the hell out of my office!"
    tn "...my wife's name is pema?"
    show bfaa bfaa06a at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "oh, for fuck's sake... yes, her name is pema."
    lin "i dodged a bullet when you dumped me."
    tn "someone has a cruuuush."
    tn "you like me, eh? eh?"
    tn "wanna bang it out?"
    show bfaa bfaa06
    lin "i..."
    show bfaa bfaa04 with hpunch
    lin "no, i don't want to 'bang it out'!"
    show bfaa bfaa05 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "I want you to get the fuck out!"
    tn "dang, that wasn't very far under the surface, was it?"
    lin "get-"
    tn "look, as much as i'm enjoying you pointing and yelling at me..."
    tn "i have a package to pick up."
    show bfaa bfaa04 with dissolve
    lin "...what?"
    tn "you know... can bend the four elements? has tits? that package?"
    lin "i... right."
    lin "hey! someone get the avatar in here!"
    hide bfaa with Dissolve(1)
    show bfaa bfaa01 with Dissolve(1)
    tn "I just want to say... before korra gets here..."
    tn "...you are repressed as hell, girl."
    lin "i should make you lick my boots."
    tn "oh, is that what you're into?"
    tn "you like being the one in charge, eh?"
    lin "....i hate you."
    tn "but do you?"
    lin "you are such a-"
    kn "...hello?"
    show bfab bfab00 at Move((-0.6, 0.0), (-0.25, 0.0), 1.0):
        xzoom -1.0

    kn "tenzin...?"
    tn "korra! get over here!"
    hide bfab with Dissolve(1)
    show bfab bfab03:
        xzoom -1
    with Dissolve(1)
    kn "uh... hey..."
    ts "(yes! she's hot!)"
    ts "(look at those tits!)"
    show ctc
    pause
    hide ctc
    ts "(i could fuck those until she breaks!)"
    ts "hell, that's the plan, isn't it..."
    show bfab bfab24 with dissolve
    kn "uh... what?"
    tn "(shit, did i say that last part out loud?)"
    tn "*cough*"
    tn "i mean... what do you have to say for yourself?"
    show bfab bfab03 with dissolve
    kn "it's... uh... always good to see-"
    tn "what the hell were you thinking?"
    show bfab bfab04 with dissolve
    kn "i was thinking i could help people..."
    kn "i mean... that's what i've been training for, right?"
    tn "yes... but you are still {i}in{/i} training."
    tn "so there will be no more of that."
    lin "that's right, no more busting up shops and taking matters into your own-"
    show bfab bfab02a with dissolve
    kn "blah blah blah, i get it..."
    lin "you little-"
    tn "you are not to talk, korra."
    show bfab bfab05 with dissolve
    kn "i'm not some little kid, tenzin!"
    kn "i'm the avatar!"
    tn "not until you have finished training and have proved yourself responsible!"
    show bfab bfab06 with dissolve
    kn "i am responsible!"
    kn "just because you were basically born an old man-"
    ta "you insolent little-"
    lin "well..."
    hide bfaa with Dissolve(1)
    show bfaa bfaa03 with Dissolve(1)

    lin "as much as i'm enjoying this -- and believe me, i am -- i think this conversation can, in fact, happen elsewhere."
    kn "or not at all..."
    lin "well, that's between the two of you now, isn't it?"
    lin "but before you go..."
    lin "{i}someone{/i} has to pay for all the damages to the city."
    lin "korra?"
    show bfab bfab24 with dissolve
    kn "i don't... have any money..."
    kn "I've never... needed it."
    lin "i'm sure you're not spoiled at all..."
    kn "but that leaves you, tenzin."

    tn "it... does?"
    kn "come on, everyone knows you're loaded."
    tn "i am?"
    tn "well, that's cool, but..."
    tn "...can't the city pay for it or something?"
    lin "oh, absolutely."
    tn "great."
    lin "we'll just jail korra, and go through the standard legal channels..."
    tn "you're enjoying this, aren't you?"
    lin "oh... very much."
    tn "fine, what do i owe?"
    lin "i think 100 coins sounds fair, don't you?"
    tn "...i don't know if that's a lot of money or not."
    lin "you two deserve each other."
    lin "get out of my office, and don't come back until you have the 100 coins."
    tn "well, you're terrible."
    tn "...and busty."
    lin "flattery won't get you out of this, tenzin."
    tn "okay... but let me ask this..."
    tn "will it get me some play time with those big-"
    show bfaa bfaa05 with hpunch
    lin "leave."
    tn "fine, i'm going, i'm going..."
    show bfaa bfaa04
    show bfab bfab04
    with dissolve
    kn "...smooth, tenzin."
    tn "oh shut up, you're in trouble."
    show bfab bfab03 with dissolve
    kn "heh."
    tn "and lin, you ruined my mood."
    tn "i was all ready to have a nice day, and you ruined it."
    tn "so thanks for nothing, have a horrible day."
    show bfaa bfaa06a at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "would you just... get... out..."
    tn "okay, but only because i want to."
    lin "as long as you leave, i don't care why."
    tn "well, i'm counting that as a win."
    tn "come on, korra!"
    kn "okay...."
    lin "fucking..."

    scene black with Dissolve(1)
    "korra trails behind you all the way back to air temple island..."
    stop music fadeout 1
    play music "audio/bounce_town.mp3"



    scene black with dissolve
    scene expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0
    show bfab bfab04
    with Dissolve(1.5)
    tn "alright, this can be your room for now."
    tn "since, i guess... i'm going to be training with you?"
    kn "that's the plan, yeah."
    tn "cool."
    tn "always good to have a plan."
    show bfab bfab24 with dissolve
    kn "hey... tenzin..."
    tn "yes?"
    show bfab bfab25 with dissolve
    kn "i'm... sorry."
    menu:
        "forgiven":
            tn "i forgive you..."
            tn "...but you should really keep a low profile."
        "tough titties":
            tn "...you think that's it?"
            tn "a quick apology and you're done?"
            tn "after the shit you just pulled?"
    show bfab bfab06 with dissolve
    kn "hey! I told you I'm sorry!"
    tn "....and?"
    show bfab bfab01 with Dissolve(1)
    show expression "bk4/backgrounds/korra_room_day.jpg" at Move((0.0, 0.0), (0.0, -0.5), 5.0, bounce = True)
    show bfab bfab01 at Move((0.0, 0.0), (0.0, -0.5), 5.0, bounce = True)
    "korra steps back and stretches with her hands behind her head."
    kn "...and nothing."
    $ renpy.pause(3.0)
    hide bfab
    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0
    show bfab bfab01
    tn "hmmm...."
    show bfab bfab24 with dissolve
    kn "look, I just... don't know what my role is, here."
    kn "they're lucky i'm here, but they don't seem to want my help."
    kn "i'm the avatar... but no one's worshipping me."
    kn "i don't understand."
    tn "(shit, this girl is entitled...)"
    show bfab bfab04 with dissolve
    kn "look, i... i want to learn to airbend."
    kn "I need to, if i'm going to save this city."
    tn "(...and a messiah complex.)"
    kn "so please don't send me back to the south pole."
    kn "i... i promise to be good."
    tn "will you do as you're told?"
    show bfab bfab24 with dissolve
    kn "uh... sure?"
    tn "that was unconvincing."
    tn "but... i won't send you back to the south pole."
    show bfab bfab03 with dissolve
    kn "thanks tenz!"
    kn "you're all tens."
    kn "get it?"
    tn "...that was even worse than my pirate pickup line."
    kn "I don't think so..."
    show bfae jinora03:
        xzoom -1 xpos 91 ypos 67
    with moveinleft
    jino "hey dad, i heard korra was-"
    show bfae jinora02
    jino "korra!" with hpunch
    show bfab bfab02b with dissolve
    kn "hey, short stuff."
    jino "is it true you're staying with us?"
    show bfab bfab02c with dissolve
    kn "you betcha, kiddo!"
    jino "that's great!"
    jino "{size=+15}she's staying, guys!!!" with hpunch
    hide bfae
    show bfae group02:
        xzoom -1
    with dissolve
    b4_cn "yay! thanks dad!"
    tn "i... guess."
    show bfab bfab03 with dissolve
    kn "i look forward to serving you guys!"
    kn "and the city!"
    ts "(and me, soon enough...)"
    kn "i'm so happy to be here!"
    b4_cn "us too!"
    b4_cn "see you later, korra!"
    hide bfae with moveoutleft
    tn "great, well, relax for a bit then."
    menu:
        "...but stay put!":
            tn "but you are not allowed to leave the island!"
            tn "not until you've proven yourself to be a good girl."
        "please stay here on the island":

            tn "but please don't leave the island."
            tn "i'd like you to keep out of trouble."

    show bfab bfab24 with dissolve
    kn "wait... what?"
    tn "i'm serious."
    tn "the two of us need to focus on training."
    show bfab bfab06 with dissolve
    kn "you want me... cooped up here?"
    tn "just until i can trust you to do as you're told."
    kn "i'm sick of being caged!"
    kn "i want to get out there and do stuff!"
    ta "i'm not getting you out of jail again!"
    kn "...ugh. fine. i guess."
    tn "good girl."
    kn "just... give me some space, tenzin."
    tn "with pleasure."
    $ b4_dock_travel = False
    jump b4_airtemple_map1

label pema_handjob1:
    stop music
    play music "audio/Unwritten Return.mp3"
    show ctc
    pause
    hide ctc
    "you begin to wake up feeling... comfy."
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos -350

    show bfaj bfaj00
    with Dissolve(2)
    show ctc
    pause
    hide ctc
    tx "*yyaaaawwwnn...*"

    tn "oh, hey..."
    pn "hmmmnh...?"
    show bfaj bfaj01 with dissolve
    pn "good mor-"
    show bfaj bfaj01a with dissolve
    pn "*yaaawnn*"
    show bfaj bfaj02 with dissolve
    pn "good morning, honey."
    show ctc
    pause
    hide ctc
    tn "that's nice to wake up to."
    pn "I'm glad you approve."
    pn "how'd you sleep?"
    tn "a little... pent-up."
    pn "oh, i'm sorry, dear."
    pn "i fell asleep before you got back, didn't i?"
    tn "yeah. uncool."
    pn "well, how about i make it up to you?"
    tn "i would not argue."
    pn "then get-"
    kn "tenzin!" with hpunch
    tn "agh!"
    tn "what! korra!"
    kn "i'm ready to get started!"
    tn "...i'm going to kill her."
    pn "please wait a moment, korra, dear!"
    kn "no!" with hpunch
    tn "....i might actually kill her."
    pn "i'm... sure you can."
    tn "....you hesitated."
    pn "....no?"
    kn "come on!" with hpunch
    tn "ugh. fine. i'm getting up."
    show bfaj bfaj01 with dissolve
    pn "wait."
    tn "hm?"
    pn "you need to start putting that tight, busty virgin in her place."
    tn "i do, don't i?"
    pn "don't let her start getting away with disobedience."
    pn "you wouldn't accept that with me, would you?"
    tn "absolutely not."
    pn "then go show her where she belongs in this pecking order."
    scene expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    show bfaj bfaj19
    with Dissolve(1)
    tn "alright, but i'm gonna come back."
    tn "and then... well, just, and then."
    play sound "audio/kiss.mp3"
    with pflash
    pn "*mwa*"
    kn "tenziiiiin!!!" with hpunch
    tn "ugh..."
    jump b4_airtemple_map1

label pema_handjob2:
    $ b4_music_day_on = False
    $ pema_hj2 = True
    $ pema_hj_daily = True
    $ pema_hj = 2
    scene black with Dissolve(1.5)
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos -350

    show bfaj bfaj13
    with Dissolve(2)

    pn "Hey, honey... i waited for you."
    show ctc
    pause
    hide ctc
    tn "yeah, you did."
    pn "why don't you slip in here with me for a moment?"
    pn "I'm wearing your favorite outfit."

    show bfaj bfaj14
    pn "Nothing."
    show ctc
    pause
    hide ctc
    tn "Huuuu... I can do that."
    "You quickly undress and slide under the sheets next to Pema."


    show bfaj bfaj00 with fade
    "Pema rests her head on you shoulder and closes her eyes."
    pn "mmmmn..."
    tn "...hello?"
    show bfaj bfaj01 with Dissolve(1.5)

    pn "Ooh... I almost fell asleep!"

    show bfaj bfaj01a
    pn "*Yaaaawn*"



    show bfaj bfaj02
    pn "I sometimes get so tired with three kids and this baby in my belly."
    menu:
        "don't stress":
            tn "It's only natural."
            tn "Don't push yourself."
            pn "Sure, but I can't ignore your needs."
        "and a man to please...":
            tn "as long as you're fulfilling your wifely duties."
            pn "of course! I know not to ignore your needs."

    pn "Although I'm too tired for a real nice long fuck... how about..."
    show bfaj bfaj03a
    "Pema reaches under the sheet... Sliding her hand over your belly downwards."
    pn "oh! what's this..."
    "When she reaches your dick, she grabs it firmly, Giving it short little jerks."

    show bfaj bfaj03
    pn "let's give you a nice little handjob to hold you over."
    pause
    tn "mmm... gotta agree that's nice..."
    tn "...but I hope you like messy sheets, because that's what you're going to get."
    pn "I don't mind..."


    show bfaj bfaj11
    pn "but here, let me take these off anyway."
    pn "You can try and reach the ceiling when you cum."
    "Pema is just about to throw the sheets off of you when-"

    show bfaj bfaj04
    b4_cn "{size=+30} MOMMM!!!! {/size} " with hpunch
    b4_cn "{size=+30} MOOOOOOOOOOOOOOMM!!!! {/size} " with hpunch

    hide bfaj
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos 0
    show bfaj bfaj05:
        linear 2.0 ypos 280 xpos 100
    pn "What?!? What is it!? Is someone hurt?!"
    pn "Is someone hurt?!"


    show bfae group04 behind bfaj:
        xpos -900
        linear 0.8 xpos 0

    b4_cn "mooom!!! Ikki is being mean!"
    b4_cn "And Meelo is being gross with boogers!"
    show bfae group04 at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
    b4_cn "NOT TRUE!"
    b4_cn "Jinora is being a stuck up little-"
    pn "{size=+30} STOP IT! {/size}" with hpunch
    pn "Don't scare me like that!"
    pn "You shouldn't shout unless it's for a very good reason! "
    pn "now, you three should... just... go away for now!"
    jino "why?"
    mee "yeah, why?"
    pn "because... i said so!"
    mee "but... can we yell if... what if... if i'm bored?"
    ikki "or... like... i'm hungry?"

    tn "these are the worst damn-"
    show bfaj bfaj05a
    tn "hrk!"
    "pema, her hand having never left your dick, begins jacking you off again."
    pn "Hmmm...."
    pn "well, you know..."
    pn "those are very good questions, meelo and ikki..."

    tn "what... what the..."
    tn "(this chick is... just... fucking... crazy!)"
    pause
    show bfaj bfaj03
    pn "what do you think, dear?"
    pause
    tn "{size=-6}what... what are you doing, pema...?"
    pn "having a conversation?"
    pn "don't you think it's such a nice time for a... conversation?"
    tx "not... not particularly..."

    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos -350
    show bfaj bfaj03:
        linear 2.0 ypos 0 xpos 0
    show bfae group04 behind bfaj:
        ypos 0
        linear 2.0 ypos -350

    pause

    pn "well?"
    pn "i think your children asked you questions."
    tn "what... shit..."
    jino "hey... what are you guys... doing?"
    pn "just scratching an... itch for daddy, dear."
    pn "isn't that right?"
    pn "aren't i just... scratching... that... itch?"
    tx "unnngh...."
    jino "oh..."
    pn "go ahead, honey... do you think being hungry is worth yelling about?"
    tx "this is the most... bonkers... shit..."
    pn "okay, okay..."

    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos 0
    show bfaj bfaj05:
        linear 2.0 ypos 280 xpos 100
    show bfae group04 behind bfaj:
        ypos -350
        linear 2.0 ypos 0

    pn "I love all three of you more than life itself, But for the next ten minutes I need some alone time with daddy."
    pn "go feed the skybisons or something!"
    b4_cn "But they've already been-"
    pn "Just ten minutes!!"
    b4_cn "Okkkaaaay!!!"
    show bfae group04:
        linear 0.8 xpos -900

    $ renpy.pause()



    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos -350
    show bfaj bfaj05:
        linear 2.0 ypos 0 xpos 0


    tn "that... was insane."
    tn "what the hell!?"
    tn "your tits were even out!"
    pn "i thought it'd be fun..."
    tn "you pretty much killed my erection..."
    hide bfae

    show bfaj bfaj11
    with dissolve
    pn "I just bought ourselves ten minutes."
    pn "I can do wonders in that time."


    show bfaj bfaj06 with Dissolve(1.5)
    pn "Oooh, what's this?"
    pn "Didn't you say your erection was ruined?"
    tn "I did... but then I looked at those big fat tits of yours, and it was cured."

    show bfaj bfaj12
    pn "Is that so?"
    pn "Do you like my big tits? Even after all these years?"
    menu:
        "they're ripe for squeezing":
            tn "all the breastmilk in there is doing wonders for filling them out."
            tn "i think pretty soon i made need some alone time with them."
        "they've always been great":

            tn "Time has nothing to do with it... They're big, round and squishy."
            tn "Hanging under a lovely face."
            tn "What's not to like?"

    "Pema starts stroking your cock slowly."

    show bfaj bfaj07
    show expression "bk4/pema/handjob/handface.png"
    pn "You've always been quite the charmer."
    pause
    show bfaj bfaj07a
    pn "Hmmm... looking at that nice hard long cock of yours... makes me wonder why there isn't a blue arrow tattooed on it."
    pause
    tn "uhhh, probably because it'd need to be erect for someone to tattoo it."
    tn "And who's going to stay erect when there's needles being pushed in?"
    show bfaj bfaj07
    pn "I can't wait till we have time again for you to push your big \"needle\" into me."
    tn "...I could push it into you right now."
    tn "also... please don't call it a needle."
    pn "One of these days, when we have enough time and a lock on the bedroom door, we will, honey."
    pn "Till then you'll just have to be happy with this."
    pn "Aren't you happy with this?"
    menu:
        "i suppose as long as you're satisfying me...":
            tn "just keeping doing your job, and get me off."
        "very much so!":

            tn "Hmm, of course I am..."

    pn "Well, I'm pretty sure the kids have no concept of time... or privacy... so I'll speed things up."
    tn "Speaking of the kids... do you think they knew what we were up to?"
    pn "Meelo, absolutely not. Ikki, I doubt it."
    pn "Jinora... I'm not so certain. "
    "Pema suddenly starts speeding up tremendously."
    show bfaj bfaj08a
    b4_tx "ffuuuuuuckkkk..."
    pn "mmmm... i love that look on your face..."
    pn "am i gonna make you cum?"
    pn "are my milf hands gonna make you cum?"
    pause
    pn "you want me to call the kids back in?"
    tx "what... the fuck... is wrong... with you... fuck... that's good..."

    show bfaj bfaj08:
        linear 0.8 ypos 0
        ypos 10
        repeat


    tx "That's very good..."
    b4_tx "Hnn... getting close..."
    hide bfaj
    hide expression "bk4/pema/handjob/handface.png"

    play sound "audio/splurt2.ogg"
    show bfaj bfaj09

    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve

    pn "oh!"
    pause(0.5)
    play sound "audio/splurt1.ogg"
    show bfaj bfaj09
    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve

    pn "Mmm..."
    pause(0.5)
    play sound "audio/gltch.mp3"
    show bfaj bfaj09
    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve
    pn "good job!"
    pn "you always amaze me with how much you shoot..."
    b4_ts "That.... was fantastic!"




    show bfaj bfaj17:
        ypos 720
    with Dissolve(1.5)
    pn "One of these days you're going to create a sperm stalactite on the ceiling."



    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos -200
    show bfaj bfaj17:
        ypos 720
        linear 2.0 ypos 880
    pn "that was just the thing to get my spirits up, today."
    pn "thank you, dear."
    tn "thank... thank {i}you{/i}."
    tn "but hey, i have a question."
    pn "hm?"
    tn "do you have any idea how i should pay lin back?"
    tn "where do i get money?"
    pn "that hardass bint..."
    pn "{i}i{/i} have you now, and she's just jealous."
    show bfaj bfaj18
    pn "maybe you should show lin what she's missing..."
    pn "...but that uptight police bitch would probably be too prissy."
    pn "maybe you should remind her... hm?"
    tn "...are you real?"
    pn "haha... very much so, love."
    pn "but to answer your other question..."
    show bfaj bfaj17
    pn "maybe go into the city and walk around until you find something?"

    pn "i'm sure there has to be some opportunity to make money in the city."
    tn "alright, i will."
    pn "good!"

    pn "Time for me to put some clothes on and deal with whatever the children have been doing."
    pn "....."

    show bfaj bfaj18
    pn "Don't just lie there with a big grin on your face!"
    pn "Move over so I can get out of bed!"
    pn "You're not going to let your pregnant wife crawl all over you are you?"
    tn "Oops, sorry."
    "You stand up to give Pema the room to get out of bed."

    scene black
    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    show bfaj bfaj19
    with Dissolve(1.5)
    tn "Do I need to do something else?"
    pn "Nope, I can take it from here."
    pn "You just go get that money and do whatever you can to teach Korra some humbleness."
    scene black with dissolve
    $ b4_dock_travel = True
    jump b4_airtemple_map1

label pema_handjob3:
    $ b4_music_day_on = False
    $ pema_hj_daily = True
    scene black with Dissolve(1.5)
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos -350

    show bfaj bfaj13
    with Dissolve(2)

    pn "alright, honey... get in here."
    tn "with pleasure."
    pn "I hope i'm presentable."
    show bfaj bfaj14
    pn "hm?"
    show ctc
    pause
    hide ctc
    tn "oh yes, very... presentable."
    "You quickly undress and slide under the sheets next to Pema."


    show bfaj bfaj00 with fade
    "Pema rests her head on you shoulder and closes her eyes."
    pn "mmmmn..."
    tn "...hello?"
    show bfaj bfaj01 with Dissolve(1.5)

    pn "Ooh... sorry!"

    show bfaj bfaj01a
    pn "*Yaaaawn*"



    show bfaj bfaj02
    pn "I sometimes get so tired with three kids and this baby in my belly."
    pn "but we're here to... talk... about you."
    show bfaj bfaj03a
    "Pema reaches under the sheet... Sliding her hand over your belly downwards."
    pn "oh! what's this..."
    "When she reaches your dick, she grabs it firmly, Giving it short little jerks."

    show bfaj bfaj03
    pn "let's get that cock warmed up."
    pause
    tn "mmm... gotta agree that's nice..."
    tn "...but I hope you like messy sheets, because that's what you're going to get."
    pn "I don't mind..."


    show bfaj bfaj11
    pn "but here, let me take these off anyway."

    show bfaj bfaj06 with Dissolve(1.5)
    pn "Oooh, what's this?"
    pn "are you {i}hard{/i}? for your {i}wife{/i}?"
    pn "what's wrong with you?!"
    pn "it's... digusting... i should... make it go away."
    tn "this is... weird foreplay."
    pn "foreplay?"
    pn "this thick... throbbing... cock... is shameful and... needs to go away."
    pn "as your wife, it is my responsibility."

    show bfaj bfaj12
    pn "mmmmm....."
    pn "....."
    pn "hey..."
    tn "hm?"
    pn "Do you... like my tits? Even after all these years?"
    menu:
        "they're ripe for squeezing":
            tn "all the breastmilk in there is doing wonders for filling them out."
            tn "i think pretty soon i made need some alone time with them."
        "they've always been great":

            tn "Time has nothing to do with it... They're big, round and squishy."
            tn "Hanging under a lovely face."
            tn "What's not to like?"

    "Pema starts stroking your cock slowly."

    show bfaj bfaj07
    show expression "bk4/pema/handjob/handface.png"
    pn "You've always been quite the charmer."
    pause
    show bfaj bfaj07a
    pn "Hmmm... looking at that nice hard long cock of yours... makes me jealous it's not inside me."
    pause
    tn "we can change that."
    show bfaj bfaj07
    pn "I can't wait...."
    show ctc
    pause
    hide ctc
    pn "...but for now, let's go ahead and make you cum."


    show bfaj bfaj08a
    "Pema suddenly starts speeding up tremendously."
    pn "mmmm... i love that look on your face..."
    pn "am i gonna make you cum?"
    pn "are my milf hands gonna make you cum?"
    pause
    pn "you want me to call the kids in?"
    tx "what... the fuck... is wrong... with you... fuck... that's good..."
    pause

    b4_tx "Hnn... getting close..."
    hide bfaj
    hide expression "bk4/pema/handjob/handface.png"

    play sound "audio/splurt2.ogg"
    show bfaj bfaj09

    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve

    pn "oh!"
    pause(0.5)
    play sound "audio/splurt1.ogg"
    show bfaj bfaj09
    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve

    pn "Mmm..."
    pause(0.5)
    play sound "audio/gltch.mp3"
    show bfaj bfaj09
    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve
    pn "good job!"
    pn "you always amaze me with how much you shoot..."
    b4_ts "That.... was fantastic!"


    if not b4_daytime:
        hide black
        show black with Dissolve(1.5)
        $ renpy.pause(.2)
        hide black
        show bfaj bfaj01a
        with Dissolve(1.5)
        pn "*yaaaawn*"
        show bfaj bfaj02 with dissolve
        pn "it's late... let's get some rest."
        show bfaj bfaj00 with dissolve
        pn "good... night... love..."
        scene black with Dissolve(1)
        jump bk4_next

    show bfaj bfaj17:
        ypos 720
    with Dissolve(1.5)
    pn "you know... i wouldn't be surprised if that drips on me during the night."



    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos -200
    show bfaj bfaj17:
        ypos 720
        linear 2.0 ypos 880
    pn "that was just the thing to get my spirits up, today."
    pn "thank you, dear."
    tn "thank... thank {i}you{/i}."

    pn "well, i think it's time for me to put some clothes on and deal with whatever the children have been doing."
    pn "....."

    show bfaj bfaj18
    pn "Don't just lie there with a big grin on your face!"
    pn "Move over so I can get out of bed!"
    pn "You're not going to let your pregnant wife crawl all over you are you?"
    tn "Oops, sorry."
    "You stand up to give Pema the room to get out of bed."

    scene black
    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    show bfaj bfaj19
    with Dissolve(1.5)
    pn "now, go do your thing, handsome."
    pn "I'll be here, taking care of the house and kids, if you need me."
    scene black with dissolve
    jump b4_airtemple_map1

label after_spinners:
    hide black
    show bfab bfab25
    with Dissolve(1)
    kn "*pant* *pant*"
    show bfab bfab06 with dissolve
    kn "stupid! planks!"
    kn "agh!"
    tn "calm yourself, korra."
    show bfab bfab25 with dissolve
    kn "sorry..."
    kn "i'm just... not used to not being good at this stuff!"
    show bfab bfab10 with hpunch
    kn "ha! there's a trick, isn't there!"
    kn "you guys are doing something!"
    tn "the trick... is airbending."
    show bfab bfab25 with dissolve
    kn "i know..."
    kn "............"
    show bfab bfab11 with hpunch
    kn "*aahhhh!!!*"
    kn "why can't i do it!?"
    tn "...why are you crying?"
    kn "it's not fair!"
    tn "oh, sweet spirits... stop crying, you baby!"
    tn "are you really this upset over something so trivial?"
    kn "it doesn't make sense!"
    show bfab bfab25 with dissolve
    kn "*sniff...*"
    show bfab bfab05 with dissolve
    kn "can we... take a break?"
    tn "....sure."
    tn "that sounds great, honestly."
    tn "I fucking hate doing work."
    show bfae jinora03
    show bfab bfab24
    with dissolve
    jino "um..."
    tn "what?"
    jino "just... the... swearing..."
    tn "well, now you're an adult. congratulations."
    tn "you did it."
    tn "you can now swear, pay taxes, and be responsible for dental appointments."
    tn "woo."
    jino "oh... uh... 'kay..."
    tn "korra, you're still in trouble."
    show bfab bfab05 with dissolve
    kn "aw man, what? why?"
    tn "jinora, keep an eye on her."
    show bfae jinora02 with dissolve
    jino "yes, sir!"
    kn "boo..."
    tn "i've gotta figure out how to make some money, anyway..."
    show bfab bfab24 with dissolve
    kn "uh... why?"
    tn "you know, because of the shit you caused?"
    show bfae jinora03 with dissolve
    jino "uh-"
    tn "don't you start."
    kn "but... i wasn't trying to-"
    tn "i don't care why!"
    tn "you fucked up the city!"
    tn "and now my bank account!"
    tn "just... go not be troublesome in a corner somewhere, would you?"
    kn "....."
    kn "but i-"
    tn "do as you're told!"
    tn "jinora! watch this ho!"
    jino "this is... kind of a lot... at once..."
    tn "good! that's your final training as an adult!"
    tn "everything is happening at once and you're unprepared for it."
    tn "and it's all horrible!"
    jino "i don't think i like being an adult..."
    tn "once again, welcome to the club."
    jino "...."
    tn "korra, stay."
    kn "....."
    $ airbending = 1
    jump b4_airtemple_map1

label after_spinners2:
    kn "okay... i can... i can totally do this."
    show black with dissolve
    "korra jumps into the spinning panels again."
    "she does a little better this time, but not much."
    hide black
    show bfab bfab25
    with dissolve
    kn "oof... man that's hard..."
    jino "you did better this time though, korra!"
    show bfab bfab04 with dissolve
    kn "thanks, jinora."
    kn "alright, so... now we get to the actual training right?"
    jino "yup!"
    jino "now we progress your actual airbending ability!"

    tn "(shit! i don't know any airbending forms yet!)"
    tn "uh..."
    menu:
        "i have an emergency":
            tn "i have... diarrhea."
            show bfab bfab24 with dissolve
            kn "i'm... sorry?"
        "pushups?":

            tn "do... the... earth-pushes."
            kn "what?"
            tn "...pushups. is what those are called."
            tn "maybe?"
    jino "okay..."
    jino "well, why don't we skip training for now and go to the next bit?"
    kn "...sure."
    kn "what's that?"
    tn "it's...."
    "you hesitate and, in a moment of desperation, look hopefully at jinora."
    "she rolls her eyes."
    jino "meditation."
    tn "...right. well done, jinora."
    tn "i'll meet you girls there."
    jino "weirdo."
    show bfab bfab03 with dissolve
    kn "I'm gonna make meditation my bitch!"
    kn "come on, jinora!"
    hide bfab
    hide bfae
    with dissolve
    tn "guess i should meet them."
    $ airbending = 2
    $ b4_dock_travel = False
    jump b4_airtemple_map1

    "test"

label lin_equalist_start:
    $ lin_equalist_quest = True
    show bfaa bfaa00
    with Dissolve(1.5)
    tn "hey, lin."
    lin "ugh... tenzin."
    hide bfaa with dissolve
    show bfaa bfaa03 with dissolve
    lin "what do you want?"
    tn "is that how you treat all of your true loves?"
    show bfaa bfaa04 with hpunch
    lin "you ass!"
    tn "you like it."
    lin "what do you want!?" with hpunch
    tn "i... don't have your money..."
    show bfaa bfaa02 with dissolve
    "lin takes a long, slow, deep breath."
    lin "why am i not surprised?"
    lin "I have an impossible workload, i'm lonely, constantly busy, and now i have to deal with this..."
    tn "...lonely?"
    show bfaa bfaa03 with dissolve
    lin "...."
    lin "do you need something, tenzin?"
    tn "wow, you got that under control quickly."
    lin "you... have a way of getting under my skin."
    lin "I am... not proud of it."
    tn "look, is there some way we can just... forget this debt?"
    lin "....."
    lin "....hmmm...."
    lin "............"
    lin "....well...."
    tn "why do i get the feeling i'm about to be in deeper shit?"
    lin "my hands are full right now with these... equalists... that have recently appeared."
    lin "i need someone to do some recon, and it's my understanding that you are good at handling... tight spots."
    tn "....this just took a sexy turn."
    lin "shut up."
    lin "I can't be everywhere."
    lin "i need you to go find this equalist rally and listen in."
    lin "report to me what they say."
    if lin_equalists ==1:
        tn "i actually already heard it."
        jump lin_equalist_cont
    else:
        tn "and then?"
        lin "and then we'll see."
        tn "...i guess i don't really have a choice."
        jump b4_repcity_map1

label lin_equalist_cont:
    lin "really?"
    lin "and...?"
    tn "complaining about benders oppressing non-benders."





    lin "hmph."
    lin "well, that supports other reports."
    lin "were they organized?"
    tn "haha fuck no, they were a mess."
    tn "but there was definitely unrest."
    tn "oh, and something about a guy named {b}amon{/b}."
    lin "{b}amon{/b}? i've been hearing that name around."
    lin "i have a bad feeling about this, tenzin."
    lin "him and the avatar both in this city at once... might be trouble."
    tn "i'll keep it in mind."
    tn "now, there was some talk of debt removal...?"
    lin "hm. I might have a way for you to earn some money."
    tn "great, hit me."
    lin "hmmmm...."
    lin "no, i think not."
    tn "aw, come on."
    lin "tell you what... you pay me back the 100 coins, and i'll give you the job."
    tn "what!?"
    tn "how am i supposed to do that?"
    lin "you'll find a way."
    menu:
        "thank you for the opportunity, mistress":
            tn "thank you, chief beifong."
            lin "you are welcome."
            lin "now crawl out of here before you end up in chains... under my {i}personal{/i} supervision."
        "you suck":
            tn "aw, you bitch."
            lin "watch that mouth or you're going to find yourself in a world of hurt."
            tn "pfft."
    $ lin_equalists = 2
    jump b4_repcity_map1

label three_in_one:
    hide bfae with dissolve
    show bfae meelo_01 with dissolve
    mee "you have to line up the coins and buttons into lines of three!"
    mee "click on a coin or button, and then click an adjacent coin or button to move it and make three in a row!"
    mee "you only have 60 seconds, okay?"
    hide bfae with dissolve
    call krix from _call_krix
    pause 1
    "you got [pointk] points."
    $ bk4_coins_daily = True
    play sound "audio/money.mp3"
    show bfae meelo_01 with dissolve
    if pointk ==0:
        "meelo gives you no coins."
        mee "you didn't do anything!"
    if pointk >=1 and pointk <=300:
        $ bk4_money +=15
        "meelo gives you 15 coins."
    if pointk >300 and pointk <=500:
        $ bk4_money +=20
        "meelo gives you 20 coins."
    if pointk >500 and pointk <=700:
        $ bk4_money +=25
        "meelo gives you 25 coins."
    if pointk >700 and pointk <=900:
        $ bk4_money +=30
        "meelo gives you 30 coins."
    if pointk >900:
        $ bk4_money +=35
        "meelo gives you 35 coins."

    if missing_meelo ==1:
        show bfae meelo_01 with dissolve
        tn "i'll just tell your mother you're here... playing in the park."
        tn "with fat stacks on stacks."
        tn "i'm sure she'll be fine with it."
        tn "keep up the good work."
        mee "help me later, okay?"
        tn "okay."
        $ missing_meelo = 2

    jump b4_repcity_map1

label korra_meditation:
    $ b4_music_day_on = False
    $ b4_music_night_on = False
    stop music
    play music "audio/Unwritten Return.mp3"

    $ bfaf_clothes = 'full'

    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, 0.0), 0.0)
    if korra_spank_bj ==2:
        tn "she's out buying that special powder from shady."
        tn "I should visit her in her room later."
        jump b4_airtemple_map1
    if meditation_level ==0:
        show bfab bfab01

        tn "sit."
        kn "easy..."
        hide screen bk4_money_date
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 1.0)
        show bfab bfab01 at Move((0.0, 0.0), (0.0, -0.4), 1.0)

        $ renpy.pause(2.0)

        hide bfab
        show bfaf bfaf01
        with Dissolve(1.5)
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 0.0)
    if meditation_level >=1:
        hide screen bk4_money_date
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 1.0)

        $ renpy.pause(0.5)

        show bfaf bfaf01
        with Dissolve(0.5)
        show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 0.0)

        menu:
            "fully clothed":
                $ bfaf_clothes = 'full'
            "??????(locked)" if bk4_swim_mission <3:
                "test"
            "swimsuit" if bk4_swim_mission >=4:
                if korra_resist <=90:
                    $ bfaf_clothes = 'swimsuit'
                    kn "oh... um... okay..."
                else:
                    kn "yeah... no."
                    $ bfaf_clothes = 'full'
            "micro swimsuit" if micro_suit:
                if korra_resist <=86:
                    if not micro_convince:
                        $ micro_convince = True
                        tn "I got you something."
                        kn "hmm?"
                        tn "put this on."
                        show bfaf bfaf02 with dissolve
                        kn "oh... i don't... that's..."
                        kn "{i}really{/i} small."
                        kn "i wouldn't be comfortable in that."
                        tn "good, then you'll be improving."
                        kn "i..."
                        kn "....."
                        kn "...okay."
                    $ bfaf_clothes = 'micro'
                    kn "oh... um... okay..."
                else:
                    kn "yeah... no."
                    $ bfaf_clothes = 'full'
            "?????(locked)" if not micro_convince:
                "test"
            "nude" if micro_convince:
                if korra_resist <=81:
                    if not nude_meditate:
                        $ nude_meditate = True
                        tn "it's time, korra."
                        kn "what?"
                        tn "take off all your clothes."
                        show bfaf bfaf02 with dissolve
                        kn "what... why..."
                        tn "because they're holding you back."
                        kn "i don't... i don't think they are..."
                        tn "which one of us is the master?"
                        kn "y-you..."
                        tn "take them off."
                        tn "tits out, whore."
                        kn "....."
                    $ bfaf_clothes = 'nude'
                    kn "......."
                    tn "you know your tits are out in the open, right?"
                    kn "...i know..."
                else:
                    kn "yeah... no."
                    $ bfaf_clothes = 'full'

    show ctc
    pause
    hide ctc
    if meditation_level ==0:
        kn "so?"
        kn "what now?"












    tn "close your eyes."
    if meditation_level ==0:
        show bfaf bfaf03 with Dissolve(1.5)
        show ctc
        pause
        hide ctc
        tn "very good."
        tn "now..."
        menu:
            "everyone hates you":
                tn "we all hate you."
            "your tits were made for fucking":

                tn "i want to fuck your big, avatar tits."

        show bfaf bfaf02 with Dissolve(1.5)
        kn "wh-what?"
        show ctc
        pause
        hide ctc
        kn "you... you don't mean that!"
        kn "that-"
        tn "you failed."
        kn "wh-what?"
        tn "that was a test of concentration, and you failed."
        tn "in order to expand your mind, and develop your true potential, you must be able to block out external stimuli."
        kn "...oh."
        kn "still..."
        tn "my job is to train you!"
        tn "and i promised it would be difficult!"
        tn "this is the fastest way to unleash your potential!"
        ts "i do not enjoy this!"
        tn "...ahem."
        tn "do you understand?"
        show bfaf bfaf01
        with Dissolve(1.5)
        kn "yes."
        tn "yes... {i}sir{/i}."
        kn "....."
        kn "yes... sir."
        tn "good."
        tn "now... close your eyes again."

        show bfaf bfaf03 with Dissolve(1.5)
        tn "clear your mind of distractions..."
        tn "find the void... the place of unity..."
        tn "and..."

        menu:
            "you're a bitch":
                tn "you're a stupid, only-good-for-fucking bitch."
            "i'm going to piss on you":

                tn "i'm going to drench your face in piss."

        kn "......"
        show bfaf bfaf04 with Dissolve(1.5)
        kn "......"
        tn "...well done."
        tn "i'm surprised that you were able to..."
        tn "...."
        tn "...are you asleep?"
        kn "......."
        tn "did you fucking fall asleep?"
        kn "*snoore*"
    if meditation_level >=1:
        tn "clear your mind of distractions..."
        tn "find the void... the place of unity..."
        show bfaf bfaf04 with Dissolve(1.5)
        kn "........"

    jump k_meditate_menu

label k_meditate_menu:
    menu:
        "do nothing":



            if meditation_level >=1:
                tn "......."
                show bfaf bfaf03 with Dissolve(1.5)
                kn "*deep breath*"
                kn "mmmm...."
                show bfaf bfaf01 with Dissolve(1.5)
                kn "well, i think this was a success."
                hide bfaf with Dissolve(1.5)
                show bfab bfab01:
                    ypos -325
                with Dissolve(1.5)
                show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                show bfab bfab01 at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                $ renpy.pause(2)
                kn "see you for the next one!"
                hide bfab with Dissolve(1.5)
                $ meditation_level +=1
                $ korra_resist -=1
                $ b4_daytime = False
                if korra_resist <95:
                    $ korra_resist  +=1
                    "her {b}resistance{/b} can't go any lower from that!"
                else:
                    play sound "audio/win2.mp3"
                    "korra's {b}resistance{/b} dropped!"
                jump b4_airtemple_map1

            if meditation_level ==0:
                tn "......."
                tn "(man, the temptation...)"
                show bfaf bfaf03 with Dissolve(1.5)
                kn "*deep breath*"
                kn "mmmm...."
                show bfaf bfaf01 with Dissolve(1.5)
                kn "so?"
                kn "how'd i do?"
                tn "pretty good, actually."
                tn "but i went easy on you."
                kn "thanks."
                kn "i didn't... see any spirits or anything."
                kn "i thought you see them if you meditate."
                tn "not always."
                kn "huh."
                kn "well, i think this was a success."
                hide bfaf with Dissolve(1.5)
                show bfab bfab01:
                    ypos -325
                with Dissolve(1.5)
                show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                show bfab bfab01 at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                $ renpy.pause(2)
                kn "see you for the next one!"
                hide bfab with Dissolve(1.5)
                $ meditation_level +=1
                $ korra_resist -=1
                show expression "bk4_xtra/remove/blackveil.png" with dissolve
                play sound "audio/win2.mp3"
                "korra's {b}resistance{/b} dropped!"
                "as you teach korra to accept your actions as part of her training, her {b}resistance{/b} to your attempts will lower."
                "this will allow you to push her into lewder situations."
                "However! If you push too hard, too quickly, her {b}resistance{/b} will rise!"
                "you can now check her stats in her room!"
                $ b4_daytime = False
                jump b4_airtemple_map1
        "mess with her hair":



            if meditation_level >=1:
                if korra_resist >=97:
                    show bfaf bfaf10
                    kn "what-"
                    show bfaf bfaf11
                    kn "hey!" with hpunch
                    show ctc
                    pause
                    hide ctc
                    show bfaf bfaf07 with hpunch
                    kn "stop it!"
                    "korra slaps your hands away."
                    kn "i'm going to my room."
                    hide bfaf with Dissolve(1.5)
                    $ korra_mad = 1
                    $ meditation_level +=1
                    $ korra_resist +=1
                    $ b4_daytime = False
                    "korra's {b}resistance{/b} increased!"
                    jump b4_airtemple_map1

                elif korra_resist >=94:
                    show bfaf bfaf10
                    kn "what-"
                    show bfaf bfaf11
                    kn "quit it!" with hpunch
                    show ctc
                    pause
                    hide ctc
                    tn "take a deep breath, korra."
                    tn "focus."
                    kn "hhrrghh...."
                    show bfaf bfaf10
                    kn "*deep breath*"
                    show ctc
                    pause
                    hide ctc
                    show bfaf bfaf03
                    with Dissolve(1.5)
                    tn "well done."
                    tn "you're really coming along."
                    show bfaf bfaf01 with Dissolve(1.5)
                    kn "thanks!"
                    hide bfaf with Dissolve(1.5)
                    show bfab bfab01:
                        ypos -325
                    with Dissolve(1.5)
                    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                    show bfab bfab01 at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                    $ renpy.pause(2)
                    kn "see you for the next one!"
                    hide bfab with Dissolve(1.5)
                    $ meditation_level +=1
                    $ korra_resist -=1
                    $ b4_daytime = False
                    if korra_resist <90:
                        $ korra_resist += 1
                        "her {b}resistance{/b} can't go any lower from that!"
                    else:
                        play sound "audio/win2.mp3"
                        "korra's {b}resistance{/b} dropped!"
                    jump b4_airtemple_map1
                else:
                    show bfaf bfaf10
                    kn "*deep breath*"
                    show ctc
                    pause
                    hide ctc
                    tn "well done."
                    tn "you're really coming along."
                    show bfaf bfaf01 with Dissolve(1.5)
                    kn "thanks!"
                    hide bfaf with Dissolve(1.5)
                    show bfab bfab01:
                        ypos -325
                    with Dissolve(1.5)
                    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                    show bfab bfab01 at Move((0.0, -0.4), (0.0, 0.0), 1.0)
                    $ renpy.pause(2)
                    kn "see you for the next one!"
                    hide bfab with Dissolve(1.5)
                    $ meditation_level +=1
                    $ korra_resist -=1
                    $ b4_daytime = False
                    if korra_resist <90:
                        $ korra_resist += 1
                        "her {b}resistance{/b} can't go any lower from that!"
                    else:
                        play sound "audio/win2.mp3"
                        "korra's {b}resistance{/b} dropped!"
                    jump b4_airtemple_map1

            if meditation_level ==0:
                show bfaf bfaf10
                kn "what-"
                show bfaf bfaf11
                kn "hey!" with hpunch
                kn "what... what are you doing!?"
                tn "trying to distract you."
                tn "you were asleep!"
                kn "i was {i}meditating{/i}, you jerk!"
                tn "...."
                kn "....."
                show bfaf bfaf07 with hpunch
                kn "stop it!"
                "korra slaps your hands away."
                kn "this was a stupid idea."
                kn "i'm going to my room."
                hide bfaf with Dissolve(1.5)
                $ korra_mad = 1
                $ meditation_level +=1
                $ korra_resist +=1
                show expression "bk4_xtra/remove/blackveil.png" with dissolve
                "korra's {b}resistance{/b} increased!"
                "as you teach korra to accept your actions as part of her training, her {b}resistance{/b} to your attempts will lower."
                "this will allow you to push her into lewder situations."
                "However! If you push too hard, too quickly, her {b}resistance{/b} will rise!"
                "you can now check her stats in her room!"
                $ b4_daytime = False
                jump b4_airtemple_map1

        "slap her" if korra_resist <97:
            call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_3
            if not amon_mask:
                show bfaf bfaf07
                kn "what. the. hell."
                tn "you need to relax and-"
                kn "{i}you{/i} need to get out of my face. now."
                kn "i'm going to my room."
                hide bfaf with Dissolve(1.5)
                $ korra_mad = 2
                $ meditation_level +=1
                $ korra_resist +=1
                $ b4_daytime = False
                "korra's {b}resistance{/b} increased!"
                jump b4_airtemple_map1
            else:
                if korra_resist >93:
                    show bfaf bfaf07
                    kn "what. the. hell."
                    tn "you need to relax and-"
                    kn "{i}you{/i} need to get out of my face. now."
                    kn "i'm going to my room."
                    hide bfaf with Dissolve(1.5)
                    $ korra_mad = 2
                    $ meditation_level +=1
                    $ korra_resist +=1
                    $ b4_daytime = False
                    "korra's {b}resistance{/b} increased!"
                    jump b4_airtemple_map1
                else:
                    show bfaf bfaf07
                    kn "hrrr..."
                    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_4
                    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_5
                    show bfaf bfaf12
                    with Dissolve(1)

                    $ b4_daytime = False
                    if korra_resist <=85:

                        "korra's {b}resistance{/b} can't go any lower from that!"
                    else:
                        $ korra_resist -=1
                        "korra's {b}resistance{/b} lowered!"
                    jump b4_airtemple_map1

        "grab her tits" if amon_mask:
            if korra_resist >88:
                show bfaf bfaf08
                kn "hmmmrm...."
                show bfaf bfaf09
                kn "that's enough!"
                $ korra_mad = 2
                $ meditation_level +=1
                $ korra_resist +=1
                $ b4_daytime = False
                "korra's {b}resistance{/b} increased!"
                jump b4_airtemple_map1
            else:
                show bfaf bfaf08
                kn "....."
                pause
                $ meditation_level +=1
                $ b4_daytime = False
                if korra_resist <=80:

                    "korra's {b}resistance{/b} can't go any lower from that!"
                else:
                    $ korra_resist -=1
                    "korra's {b}resistance{/b} lowered!"
                jump b4_airtemple_map1


label korra_training:
    if amon_mask:
        if air_scroll ==2:
            if airbending ==7:
                show bfab bfab04 with dissolve
                kn "ready for more training?"
                show under_development_1
                show ctc
                pause
                hide ctc
                hide under_development_1
                jump b4_airtemple_map1
            if airbending ==6:
                if korra_spank_bj >=6:
                    if korra_foot_quest ==1:
                        show bfab bfab24 with dissolve
                        kn "ready for more training?"
                        kn "i... i promise i'll repay you."
                        if spinner_level >=10:
                            $ korra_foot_quest = 2
                            jump air_train3
                        else:
                            tn "(i need to level up to {b}10{/b} on the spinners before i can train more with korra.)"
                            jump bk4_training_menu
                    if korra_foot_quest ==0:
                        show bfab bfab24 with dissolve
                        kn "hey, tenzin...?"
                        tn "yeah?"
                        kn "i... i really need to get stronger."
                        kn "if you... i mean..."
                        kn "if you'll train with me some more..."
                        kn "i'll... i'll give you something."
                        tn "oh? what?"
                        kn "i... i don't know yet."
                        kn "but i promise it will be worth it!"
                        tn "...."
                        tn "okay."
                        $ korra_foot_quest = 1
                        if spinner_level >=10:
                            $ korra_foot_quest = 2
                            jump air_train3
                        else:
                            tn "(i need to level up to {b}10{/b} on the spinners before i can train more with korra.)"
                            jump bk4_training_menu
                else:
                    show bfab bfab04 with dissolve
                    kn "ready for more training?"
                    tn "soon, but not yet."
                    jump b4_airtemple_map1
            if airbending ==5:
                if k_protein <3:
                    tn "korra's waiting in her room for her protein shake."
                    jump b4_airtemple_map1
                else:
                    show bfab bfab04 with dissolve
                    kn "alright, what's next?"
                    tn "next, you're going to give me asami's number."
                    show bfab bfab24 with dissolve
                    kn "are you still on that?"
                    tn "yeah, and i'm gonna be... until i get her number."
                    tn "i'm tired of dialing random numbers."
                    tn "it's not an efficient system, and one man is very mad at me."
                    kn "....."
                    tn "....."
                    ta "give me that number!"
                    kn "okay, okay..."
                    kn "after today."
                    tn "fine."
                    hide black
                    show black with dissolve
                    "you practice the latest technique with korra, gaining efficiency in it."
                    hide black
                    show bfab bfab09
                    with dissolve
                    kn "yeah! love a good sweat!"
                    show bfab bfab04 with dissolve
                    kn "alright, tenzin... here's asami's number."
                    play sound "audio/win2.mp3"
                    "you got asami sato's phone number!"
                    tn "finally."
                    hide bfab with dissolve
                    tn "i should go somewhere private to make this phone call..."
                    tn "the tower, maybe?"
                    $ airbending = 6
                    jump b4_airtemple_map1
        if air_scroll ==1:
            if airbending ==4:
                if lin_buttstuff and korra_scroll2==0:
                    show bfab bfab04 with dissolve
                    tn "hey... so..."
                    tn "i need asami's phone number."
                    tn "phones are a thing by now, right?"
                    show bfab bfab24 with dissolve
                    kn "why..."
                    tn "it doesn't concern you."
                    kn "uh... i don't think she wants me to give it out..."
                    tn "come on. buddy. korra. pal. old friend. sloot."
                    kn "...what?"
                    tn "ignore that last one."
                    tn "help me out."
                    kn "mm... okay."
                    tn "great!"
                    show bfab bfab03 with dissolve
                    kn "in exchange for more training!"
                    tn "what?"
                    tn "but... i don't wanna."
                    show bfab bfab04 with dissolve
                    kn "come on... you haven't taught me anything real since that one scroll."
                    kn "let's do this!"
                    tx "uuughgh...."
                    tn "fine."
                    show bfab bfab03 with dissolve
                    kn "yay!"
                    tn "but first i need to... do something."
                    show bfab bfab24 with dissolve
                    kn "okay..."
                    hide bfab with dissolve
                    tn "...shit."
                    tn "where the fuck do i find a new airbending scroll?"
                    $ korra_scroll2 = 1
                    jump b4_airtemple_map1
                if korra_scroll2 ==1:
                    show bfab bfab04 with dissolve
                    kn "hey, ready to train me?"
                    tn "(i still don't have an airbending scroll...)"
                    tn "uh... almost."
                    show bfab bfab24 with dissolve
                    kn "oh... okay."
                    jump b4_airtemple_map1
                if korra_scroll2 ==2:
                    if spinner_level >=8:
                        show bfab bfab04 with dissolve
                        kn "ready?"
                        tn "actually, i am."
                        tn "read this."
                        show bfab bfab24 with dissolve
                        "you hand korra the scroll."
                        kn "this again..."
                        kn "fine, i guess i'll {i}read{/i}."
                        kn "like a dork."
                        hide black
                        show black with dissolve
                        "korra begins practicing the moves written on the scroll."
                        "you mimic her technique."
                        hide black
                        show bfab bfab09
                        with dissolve
                        kn "what a workout!"
                        show bfab bfab04 with dissolve
                        kn "not bad, tenzin."
                        tn "so... can i have asami's number now?"
                        show bfab bfab24 with dissolve
                        kn "i don't know..."
                        tn "oh, come on!"
                        kn "i'll... think about it, okay?"
                        kn "that's the best I can offer right now."
                        tn "...damn it."
                        kn "sorry, tenzin."
                        kn "now i need to go have my boring protein shake."
                        show bfab bfab05 with dissolve
                        kn "pema makes the worst shakes."
                        tn "...why don't you just make your own?"
                        show bfab bfab24 with dissolve
                        kn "pfft, yeah right."
                        kn "why would that be my responsibility?"
                        tn "....."
                        tn "sure."
                        kn "alright, terrible protein shake, here i come."
                        hide bfab with dissolve
                        tn "that... gives me an idea."
                        tn "i'll ask pema to help me with a... special one."
                        $ k_protein = 1
                        $ air_scroll = 2
                        $ airbending = 5
                        $ b4_daytime = False
                        jump b4_airtemple_map1
                    else:

                        show bfab bfab04 with dissolve
                        kn "hey, ready to train me?"
                        tn "(i need to be up to level 8 on the spinners to handle this move.)"
                        tn "not yet."
                        jump b4_airtemple_map1
                else:

                    tn "(still more to do elsewhere first.)"
                    jump b4_airtemple_map1
            if airbending ==3:
                if spinner_level < 6:
                    tn "i need to get to level 7 in the spinners to handle the next training session."
                    jump b4_airtemple_map1
                if spinner_level >=7:
                    if korra_rubbed >=3:
                        $ airbending = 4
                        jump air_train2
                    else:
                        tn "(my body is ready... but korra's isn't.)"
                        tn "(i need to lower her resistance, and maybe progress some more with her before the next training session.)"
                        jump b4_airtemple_map1

            if not air_scroll1_thought:
                tn "(alright, looking at this airbending scroll, i don't think i need to do anything special this time, actually.)"
                tn "(this one actually seems really straight forward.)"
                $ air_scroll1_thought = True
                show bfab bfab24 with dissolve
                kn "so...?"
                kn "you ready?"
            if spinner_level <5:
                tn "(crap, i need to spend more time on the spinners before i can train with this airbending move.)"
                tn "uh... not yet."
                kn "okay..."
                jump b4_airtemple_map1
            else:
                $ b4_daytime = False
                jump air_train1

    if not amon_mask:

        show bfab bfab04
        with dissolve
        kn "ready to train?"
        tn "(i still don't know any airbending techniques!)"
        tn "uh... not yet."
        kn "okay, i guess..."
        jump b4_airtemple_map1

label air_train1:
    show bfab bfab04
    tn "here, i have something for you."
    kn "okay..."
    play sound "audio/paperruffle.mp3"
    "you hand korra the airbending scroll."
    show bfab bfab24 with dissolve
    kn "this... is a piece of paper."
    kn "why are you giving me this?"
    tn "i want to see you learn from the reading material."
    kn "...."
    kn "nerd."
    tn "i will give you papercuts."
    tn "just mimic the damn thing."
    tn "i will be doing it alongside you."
    tn "to... uh... make sure you're doing it right."
    hide black
    show black
    with dissolve
    "korra tries to pick up the first airbending form from the scroll, eventually succeeding."
    "you copy her moves, and pick up the technique yourself."
    hide black
    show bfab bfab09
    with dissolve
    kn "woo!"
    kn "i did it!"
    tn "that was an easy one."
    show bfab bfab04 with dissolve
    kn "yeah, but still."
    kn "i did it."
    tn "i guess you did."
    tn "congratulations."
    show bfab bfab03 with dissolve
    kn "thanks!"
    kn "i can't wait for the next one."
    $ airbending = 3
    jump b4_airtemple_map1

label air_train2:
    show bfab bfab04
    with dissolve
    tn "(i don't have another scroll, so...)"
    tn "(let's make this session be a little more personal.)"
    kn "so, what kind of training are we doing?"

    tn "come with me."
    tn "we're going up to the tower."
    show bfab bfab24 with dissolve
    kn "...really?"
    kn "why?"
    tn "high elevation means we'll be more in touch with the air."
    tn "...or something."
    hide screen bk4_money_date
    scene black
    with dissolve
    if b4_daytime:
        show expression "bk4/backgrounds/tower_day_1.jpg":
            ypos 0
    if not b4_daytime:
        show expression "bk4/backgrounds/tower_night .jpg":
            ypos 0
    show bfab bfab28
    with Dissolve(1.5)
    kn "okay, we're here."
    tn "now... take off your shirt."
    hide bfab
    show bfab bfab28
    kn "...."
    kn "what?"
    tn "I know it seems a little unorthodox..."
    tn "but i told you that part of being an airbender is being free with your body."
    tn "what we're going to do today is an ancient chakra-opening technique."
    tn "and... i'll need direct contact with the chakra sections."
    tn "specifically the two in your chest."
    kn "....."
    show bfab bfab29
    kn "...are you sure?"
    tn "if you don't want my help..."
    show bfab bfab27
    kn "wait..."
    kn "I'm doing it, i'm doing it."
    show bfab bfab26 with dissolve
    kn "........"
    kn "......................."
    kn "......................................."
    hide bfab with Dissolve(1.5)
    $ renpy.pause(0.3)

    show bfai bfai00
    with Dissolve(1.5)
    pause
    tn "(oh... shit... yes.)"
    tn "(look at those fucking knockers!)"
    tn "(i just want to put my face in there and get slapped around...)"
    pause
    tn "(......)"
    tn "...*ahem*"
    tn "Okay, let's do it."
    tn "this is an ancient form of airbender training designed to increase your sensitivity and the flow of spiritual energy."
    tn "first, straighten your back..."
    show bfai bfai01
    tn "...so those fat, tasty puppies stick right out..."


    tn "just like that."
    pause
    tn "now... arms get in the way during this, so i'll need you to put them behind your head."
    show bfai bfai02 with dissolve
    kn "like... this?"
    tn "exactly like that."

    tn "now, this might feel a bit... surprising."
    tn "but keep in mind, this is purely spiritual."
    tn "we're going to focus on your left chest chakra first."
    tn "this is serious, so please don't be squeamish."
    tn "(gently... gently...)"


    show bfai bfai03:
        xpos 500
        linear 0.9 xpos 510
        linear 0.3 xpos 500
        repeat

    tn "(what a perfectly soft and firm little nubbin....)"
    pause
    kn "(oh!)"
    kn "(come on, korra... power through.)"
    pause
    tn "alright, now we're going to move to your right tit... i mean... chest chakra."



    show bfai bfai04a:
        xpos 500
        easein 1.0 xpos 450
        linear 0.3 xpos 500
        repeat
    kn "ahh...!!"
    kn "unngh... it... ah... it hurts..."
    pause
    tn "that's... mgh... natural..."
    tn "this chakra is... hngh... very closed..."
    tn "(yes! this big, juicy fucking tit!)"
    tn "(i can't believe i'm tugging on korra's tits and she's just letting me!)"
    pause
    tn "switch!"


    show bfai bfai04:
        xpos 500
        easein 1.0 xpos 550
        linear 0.3 xpos 500
        repeat
    kn "unnnghh.... oww...."
    tn "yes... yes... yes...!"
    kn "didn't... ahh... didn't you do this one... ngh..."
    tn "I needed more!"
    tn "I mean... it needed more."
    pause




    show bfai bfai04b:
        xpos 500

        easein 0.8 xpos 550
        linear 0.3 xpos 490
        linear 0.2 xpos 500

        easein 0.8 xpos 450
        linear 0.3 xpos 510
        linear 0.2 xpos 500

        repeat

    kn "ohh... ahn... wait... wait... ah..."
    pause
    tn "yes! yes!"
    tn "you have great fucking tits, korra!"
    kn "what... ah... what are you talking... ah... "
    pause
    tn "now..."





    show bfai bfai05:
        xpos 500 ypos 720
        linear 1.2 ypos 710
        linear 0.2 ypos 720
        linear 0.2 ypos 730
        pause (0.8)
        repeat
    tn "...let's work them simultaneously!"
    tn "yes, your tits... er... chakras... are really... opening up."
    pause
    kn "(this technique is... like none i've ever done before...)"
    kn "(i think i can feeling it working.)"
    pause
    tn "alright..."
    hide bfai
    show bfai bfai00
    with Dissolve(1.5)
    kn "oof..."
    kn "that was... intense."
    kn "my chest feels warm and... firm."
    tn "good, but we're not done yet."
    tn "this is just giving you a break for a moment."
    kn "thanks... this is more involved than i thought it would be."
    kn "....."
    kn "...alright."
    show bfai bfai01
    kn "what's next?"
    tn "now, you need to grab and roll your breasts."
    tn "that's where your chakras really are."
    tn "as everyone knows."
    kn "alright..."

    show bfai bfai06:
        xpos 500 ypos 720
        linear 1.2 xpos 520
        linear 1.2 xpos 500
        repeat
    pause
    kn "like this?"
    tn "just like that."
    pause
    kn "this is a real workout... these are pretty heavy."
    kn "and... it's making my whole body feel warm..."
    pause
    tn "alright, arms behind your back again, please."
    hide bfai
    show bfai bfai02
    with dissolve
    kn "okay, now wha-"



    play sound "audio/slap.mp3"    

    show bfai bfai07a:
        xpos 500 ypos 720
        linear 0.3 xpos 450
        linear 1.5 xpos 500

    show bfai_slaphand:
        alpha 1.0
        xpos 380 ypos 250
        linear 0.2 xpos 280
        linear 0.6 xpos 250
        linear 1.0 alpha 0.0


    kn "ahh!"
    kn "oh... that... was... unpleasant..."


    hide bfai_slaphand
    $ temp_int = 0



    menu:
        "give her a few more":


            while temp_int <= 4:
                if temp_int ==2:
                    kn "ungh!"
                if temp_int ==3:
                    kn "ah..."
                $ temp_int += 1

                play sound "audio/slap.mp3"                

                show bfai bfai07a:
                    xpos 500 ypos 720
                    linear 0.3 xpos 450
                    linear 1.5 xpos 500

                show bfai_slaphand:
                    xpos 380 ypos 250 alpha 1.0
                    linear 0.2 xpos 280
                    linear 0.6 xpos 250
                    linear 1.0 alpha 0.0



                $ renpy.pause(1.8)
                play sound "audio/slap.mp3" 
                hide bfai_slaphand

                show bfai bfai08a:
                    xpos 500 ypos 720
                    linear 0.3 xpos 550
                    linear 1.5 xpos 500
                show bfai_slaphand:
                    xpos 350 ypos 250 xzoom -1.0 alpha 1.0
                    linear 0.2 xpos 600
                    linear 0.6 xpos 700
                    linear 1.0 alpha 0.0

                $ renpy.pause(1.8)
                hide bfai_slaphand
        "that's enough":



            pass

    if temp_int > 0:
        show bfai bfai09 with Dissolve(1.5)
    else:
        show bfai bfai01 with Dissolve(1.5)

    tn "You holding up, Korra?"
    kn "This... this is nothing!"
    pause
    tn "good!"
    tn "i think that should do it for today."
    show bfai bfai00 with dissolve
    tn "how do you feel?"
    kn "worn out..."
    kn "my chakras feel really sore..."
    tn "that just means it's working."
    $ b4_daytime = False
    pause
    $ korra_tits_out = True
    if korra_moral <=85:
        pass
    else:

        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    jump b4_airtemple_map1

label air_train3:
    tn "yes."
    tn "let's get started."
    tn "take your shirt off."
    kn "why... okay."
    hide screen bk4_money_date
    hide bfab
    with dissolve
    show bfai bfai00
    with dissolve
    show ctc
    pause
    hide ctc
    tn "ready?"
    show bfai bfai01 with dissolve
    kn "yeah."
    tn "just make sure you stretch first."
    kn "right, right..."
    show bfai bfai02 with dissolve
    "korra stretches her back, presses her voluptuous tits out into the open air."
    tn "let's... uh... work those chakras while you do that."
    kn "good idea."
    show bfai bfai05 with dissolve
    tn "good... good..."
    show ctc
    pause
    hide ctc
    tn "now, get them warmed up yourself."
    kn "you know, i've done this before."
    tn "and routine is important."
    show bfai bfai01 with dissolve
    tn "go ahead."
    kn "all right..."
    show bfai bfai06 with dissolve
    kn "hup!"
    show ctc
    pause
    hide ctc
    tn "alright, alright, let's get to it."
    show bfai bfai01 with dissolve
    kn "awesome."
    show bfaa bfaa01:
        xpos -250 ypos -10
    with Dissolve(1)
    lin "what... are you two doing?"
    tn "....ho boy."
    kn "we're training."
    lin "doesn't look like any training i know."
    tn "what are you doing here, lin?"
    lin "i swim. a lot."
    tn "...in full uniform?"
    lin "how do you think i stay in such fantastic shape?"
    tn "and you had to swim here? to this island?"
    tn "where i live?"
    lin "it's a good swim."
    lin "but we should talk about what you're doing with this... avatar trash."
    tn "training her."
    kn "see?"
    lin "well, she looks like a whore."
    kn "i do not look-"
    tn "korra."
    kn "..."
    tn "tell her you're a whore."
    kn "w-what?"
    tn "are you disobeying me?"
    kn "n-no, sir."
    kn "I'm... i'm a..."
    show bfai bfai00 with dissolve
    kn "...i'm a... whore."
    tn "you did not address her properly."
    kn "...lin, i'm a-"
    lin "it's chief beifong to you."
    lin "...whore."
    kn "chief beifong..."
    lin "oh, i like this."
    kn "i'm a... a whore."
    tn "and?"
    kn "and... and... uh..."
    lin "spoiled?"
    kn "...and i'm spoiled..."
    lin "and a worthless burden on everyone's life?"
    kn "...."
    kn "and a..."
    show bfai bfai09 with dissolve
    kn "I don't really have to say that... do i?"
    tn "yes."
    show bfai bfai00
    with dissolve
    kn "i'm... i'm a..."
    kn "i'm a worthless burden..."
    kn "...on everyone's life."
    kn "i should never have been born."
    kn "i... i was a mistake."
    kn "i deserve... i deserve to be spanked... and... and..."
    show bfai bfai09 with dissolve
    kn "I deserve to be..."
    kn "I deserve...."
    lin "well?"
    kn "i... deserve..."
    kn "*sob*..."
    kn "...."
    kn "i deserve to be face... to be facefucked."
    show bfai bfai00 with dissolve
    kn "*sob*..."
    lin "that..."
    lin "...was amazing."
    lin "tenzin, you're doing an amazing job."
    lin "i'll see you later."
    lin "we have to do something more about this equalist problem... but you're busy right now with something important."
    hide bfaa with Dissolve(1)
    tn "well done, korra."
    kn "....."
    tn "you're finally progressing into... airbending... training properly."
    tn "now, let's train our bodies, shall we?"
    show bfai bfai09 with dissolve
    kn "r-really?"
    tn "yeah."
    kn "o...okay!"
    hide black
    show black with dissolve
    "you and korra practice the latest airbending forms you've discovered."
    "her spirits clearly pick up during the process."
    "she gets a bit of confidence back."
    show bfai bfai01
    hide black
    with dissolve
    kn "i feel... amazing."
    kn "there's nothing like a workout."
    kn "i really think i'm starting to get the hang of this."
    tn "me too..."
    kn "what?"
    tn "i mean... that you're starting to get the hang of this."
    tn "I obviously already know how to do all this. obviously."
    kn "...right."
    kn "anyway, um... about the thing i want to give you..."
    tn "yes?"
    show bfai bfai00 with dissolve
    kn "I'll... think of something, okay?"
    tn "...."
    tn "sure."
    kn "okay... uh... bye."
    hide bfai with dissolve
    tn "....."
    tn "she fuckin' better."
    $ b4_daytime = False
    $ airbending = 7
    jump b4_airtemple_map1

    "test"

label lin_handjob1:
    lin "hmmmm...."
    lin "well."
    hide bfaa with Dissolve(1)
    show bfaa bfaa01 with Dissolve(1)
    lin "it's about time."
    tn "yeah, right."
    tn "now, you had a job for me?"
    lin "yes."
    lin "and it pays well."
    tn "fine, great, i get to do shit for people who make money off of my sweat and tears."
    tn "gimme the thing."
    lin "well..."
    tn "oh. come. {i}on{/i}."
    tn "what else could you possibly want?"
    lin "hmmmm...."
    scene black
    hide screen bk4_money_date
    with Dissolve(1)
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"
    show bfan bfan01
    with Dissolve(1.5)
    lin "i want you to do something, first."
    tn "you have {i}another{/i} job for me to do!?"
    lin "oh, yes."
    tn "...."
    tn "what kind of job?"
    lin "well, if you really want my help..."
    lin "...masturbate."
    tn "...what?"
    lin "masturbate. here. now."
    tn "Is that... a joke?"
    lin "No."
    lin "I want you to degrade yourself in front of me."
    lin "I want to humiliate you... like you've humiliated me."
    lin "Or maybe you've become an impotent limpdick incapable of even getting hard?"
    tn "....."
    show bfan bfan02 with Dissolve(1.5)
    tn "I'd say I'm far from a limpdick."
    lin "pfff, just... start jacking that dumb cock of yours."
    tn "....."
    show bfan bfan03
    tn "Are you certain this is punishment for me and not just... you know..."
    tn "A severe lack in your life you're trying to fill?"
    lin "Don't flatter yourself."
    lin "I'm not the girl you broke up with all those years ago."
    lin "I'm well over that."
    tn "Whatever you say."
    lin "What do you think your wife would have to say about you masturbating in front of your old girlfriend?"
    lin "Would she be angry or sad if she found out?"
    lin "Doesn't that make you feel afraid?"
    tn "uuuhh... she might be angry, but..."
    tn "probably because she wasn't there to watch..."
    tn "i'm pretty sure pema is kinkier than I am."
    tn "And that's saying something!"

    show bfan bfan08
    tn "oh man... I'm going to cover that desk of yours with creamy goo!"
    show bfan bfan07
    lin "What?!? NO!!" with hpunch
    tn "Almost there!"


    lin "Anyone coming into my office will see and smell it!"
    tn "You wanted me to jack off in front of you!"
    tn "You knew this was going to happen!"

    lin "I... I just sorta didn't think it through..."
    lin "It was a spur of the moment thing."
    lin "Argh! Fine, I'll deal with your mess, like I always do!"
    lin "Just give that stupid cock to me damn it!"

    show bfan bfan05
    "Lin grabs your dick and aims it at her open mouth."
    pause

    tn "Nice! A little rough, but I can appreciate the effort!"
    tn "Was this your plan from the beginning?"
    lin "Don't be an idiot! "
    lin "I just don't want my reputation in the gutter because you can't control yourself."
    tn "....."
    tn "If you're planning on catching it from that distance you'll get it all over your face."
    tn "I'm okay with that, i'm just saying-"

    show bfan bfan06
    "Lin pushes her lips against the tip of your cock just as you're about to blow your load."

    play sound "audio/splurt2.ogg"
    show bfan bfan06 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
    $ renpy.pause(0.6)
    play sound "audio/splurt1.ogg"
    show bfan bfan06 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
    $ renpy.pause(0.6)
    play sound "audio/splurt3.ogg"
    show bfan bfan06 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
    $ renpy.pause(0.6)
    tx "That's it, bitch!"
    tx "Swallow my cum! all of it!"
    play sound "audio/gulp.mp3"
    lin "*gulp* *gulp*"
    lin "mmmgh...."
    play sound "audio/gulp.mp3"
    lin "*gulp* *gulp*"
    lin "...hmmmghgh!!!!" with hpunch
    play sound "audio/gulp.mp3"
    lin "*gulp* *gulp* *gulp*"
    lin "........"
    show bfan bfan09 with Dissolve(1.5)
    lin "*cough!* *cough!* "
    show bfan bfan11
    show bfan_spermonclothes
    lin "Bugh!"

    show bfan bfan09 with Dissolve(1.5)
    lin "What the fuck is Pema feeding you?!"
    lin "It's not normal to have this much sperm!"
    lin "I could barely swallow most of it!"
    show bfan bfan10 with Dissolve(1.5)
    tn "Don't feel sad. You did great!"
    lin "Get out of here tenzin. "
    lin "I need a drink to wash away this horrible taste."
    tn "wait, what about that job-"
    lin "ugh!"
    lin "come back tomorrow."
    lin "i'll have the patience to deal with you then."
    scene black with Dissolve(1.5)
    "you head back to the island."
    $ b4_daytime = False
    jump b4_airtemple_map1


label lin_handjob2:
    show bfaa bfaa01
    with dissolve
    tn "hey, i have some equalist chatter to report."
    lin "in a minute."
    lin "first, come here."
    tn "what?"
    tn "but you sent me to-"
    lin "come here!"

    hide screen bk4_money_date
    scene black
    with Dissolve(1)
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"
    show bfan bfan01
    with Dissolve(1)

    tn "okay, what?"
    lin "I want a rematch."
    tn "you want... what?"
    lin "I'll show you the last time was just a fluke."
    tn "the last..."
    tn "wait, are you serious?"
    lin "I... I can swallow that cum without a problem."
    lin "I was just unprepared the last time."
    lin "hold on, let me get this... off..."
    show bfan bfan51 with Dissolve(1.5)
    lin "there."
    lin "Just making sure you're not going to ruin my uniform again."
    pause
    lin "now...."
    lin "degrade yourself!"
    tn "...."
    tn "i mean..."
    show bfan bfan52
    tn "......"
    tn "hope you're enjoying this private show."
    lin "Can't you go faster? I don't have all day."
    tn "Nah, I want to enjoy this."
    lin "Give that to me!"
    show bfan bfan58 with Dissolve(1.5)
    lin "I just want you to cum, damn it."
    pause
    lin "Are you already there?!"
    tn "Mmmm... getting closer."
    show bfan bfan53
    lin "Tell me when it's time!"
    pause
    lin "....."
    lin "give it to me!"

    menu:
        "don't warn her":
            show bfan bfan53a
            play sound "audio/splurt2.ogg"
            show expression "bk4/lin/handjob/blink_front.png":
                xpos 760 ypos 200
            show bfan_spermshot with vpunch:
                xpos 710 ypos 120
            show expression "bk4/lin/handjob/spermonface.png" with Dissolve(1.0)

            lin "What?!"
            hide expression "bk4/lin/handjob/spermonface.png"
            hide expression "bk4/lin/handjob/blink_front.png"
            show bfan bfan59
            show expression "bk4/lin/handjob/spermonangryface.png"
            with Dissolve(1.5)
            lin "Damn it!!!"
            lin "I told you to warn me!"
            lin "you... you... on my face..."
            lin "I've never..."
            tn "Sorry, It happened too fast for me to say something."
            lin "well, you are... you are properly degraded."
            lin "now get out!"
        "Warn her":

            tn "Ready or not... gonna blow!"
            show bfan bfan54 with Dissolve(1.5)
            play sound "audio/splurt2.ogg"
            show bfan bfan54 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
            $ renpy.pause(0.6)
            play sound "audio/splurt1.ogg"
            show bfan bfan54 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
            $ renpy.pause(0.6)
            play sound "audio/gulp.mp3"
            lin "*gulp* *gulp*"
            lin "...hmmmghgh!!!!" with hpunch
            play sound "audio/gulp.mp3"
            lin "*gulp* *gulp* *gulp*"
            lin "........"
            show bfan bfan55 with Dissolve(1.5)
            lin "I think I..."
            show bfan bfan56
            show bfan_spermonclothes
            lin "bugh!"
            lin "...shit."
            show bfan bfan57
            lin "Wipe that grin off your face."
            lin "I'll... I'll show you next time!"
            tn "Lookin' forward to it!"
            lin "Damn it.. my shirt is all covered with it."
            show bfan bfan60
            hide bfan_spermonclothes
            with Dissolve(1.5)
            lin "well, you are... you are properly degraded."
            lin "Get out of here, Tenzin."

    scene black with dissolve
    "you're surprised at how much time has passed."
    $ b4_daytime = False
    $ lin_hj2 = True
    jump b4_airtemple_map1

label lin_handjob3:

    hide screen bk4_money_date
    scene black
    with Dissolve(1)
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"
    show bfan bfan01
    with Dissolve(1)

    tn "hey..."
    tn "so..."
    tn "...."

    show bfan bfan02 with Dissolve(1)
    lin "hmm?"
    show bfan bfan03
    lin "oh for..."
    lin "what are you doing?"
    tn "what's it look like?"
    tn "i'm looking at your face and jacking off."
    lin "......."
    tn "you like my cock being inches from your face?"
    lin "......"
    lin "well..."
    show bfan bfan07
    lin "stop it!"
    show bfan bfan01 with Dissolve(1)
    tn "aww..."
    show bfan bfan51 with Dissolve(1.5)
    lin "if you're going to humiliate yourself for me..."
    lin "i'm not going to let you ruin my uniform in the process."
    show ctc
    pause
    hide ctc
    lin "now...."
    lin "degrade yourself!"
    tn "...."
    tn "i mean..."
    show bfan bfan52
    tn "......"
    lin "Can't you go faster? I don't have all day."
    tn "Nah, I want to enjoy this."
    lin "ugh, give that to me!"
    show bfan bfan58 with Dissolve(1.5)

    lin "I just want you to cum, damn it."
    pause
    lin "Are you almost there?!"
    tn "Mmmm... getting closer."
    show bfan bfan53
    lin "Tell me when it's time!"
    pause
    lin "....."
    lin "give it to me!"
    menu:
        "don't warn her":
            play sound "audio/splurt2.ogg"
            show bfan bfan53a
            show expression "bk4/lin/handjob/blink_front.png":
                xpos 760 ypos 200
            show bfan_spermshot with vpunch:
                xpos 710 ypos 120
            show expression "bk4/lin/handjob/spermonface.png" with Dissolve(1.0)

            lin "What?!"
            hide expression "bk4/lin/handjob/spermonface.png"
            hide expression "bk4/lin/handjob/blink_front.png"
            show bfan bfan59
            show expression "bk4/lin/handjob/spermonangryface.png"
            with Dissolve(1.5)
            lin "Damn it!!!"
            lin "I told you to warn me!"
            lin "you... splattered my face... with..."
            tn "Sorry, it happened too fast for me to say something."
            lin "well, you are... you are properly degraded."
            lin "now get out!"
        "Warn her":

            tn "Ready or not... gonna blow!"
            show bfan bfan54 with Dissolve(1.5)
            play sound "audio/splurt2.ogg"
            show bfan bfan54 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
            $ renpy.pause(0.6)
            play sound "audio/splurt1.ogg"
            show bfan bfan54 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
            $ renpy.pause(0.6)
            play sound "audio/gulp.mp3"
            lin "*gulp* *gulp*"
            lin "...hmmmghgh!!!!" with hpunch
            play sound "audio/gulp.mp3"
            lin "*gulp* *gulp* *gulp*"
            lin "........"
            show bfan bfan55 with Dissolve(1.5)
            lin "I think I..."
            show bfan bfan56
            show bfan_spermonclothes
            lin "bugh!"
            lin "...shit."
            show bfan bfan57
            lin "Wipe that grin off your face."
            lin "I'll... I'll show you next time!"
            tn "Lookin' forward to it!"
            lin "Damn it.. my shirt is all covered with it."
            show bfan bfan60
            hide bfan_spermonclothes
            with Dissolve(1.5)
            lin "well, you are... you are properly degraded."
            lin "Get out of here, Tenzin."

    scene black with dissolve
    "you're surprised at how much time has passed."
    $ b4_daytime = False
    $ lin_hj2 = True
    jump b4_airtemple_map1

label lin_bending_job:
    tn "hey, so about that job..."
    show bfaa bfaa04 with hpunch
    lin "yes, damn it!"
    lin "i have a job for you."
    show bfaa bfaa03 with dissolve
    lin "it can help us both, actually."
    tn "oh?"
    lin "the probending arena is suddenly full of teams made of equalist benders."
    lin "they're making a lot of money, and i'm sure they're going to use the setting to stage some kind of attack."
    tn "i thought equalists couldn't bend?"
    tn "i thought that was their whole deal?"
    lin "there are some benders that support the equalist cause and are using their abilities to further it."
    lin "i need someone on the inside to pay attention."
    lin "and i need a team that can stay in the game, and won't be eliminated."
    tn "and you're thinking..."
    lin "team avatar."
    tn "...right."
    lin "i'll be honest... they suck."
    lin "they need a coach or they're gonna lose."
    lin "and as much as i hate to admit it... you've always been a talented fighter."
    lin "your knowledge, combined with the avatar's growing skill, should create the best chance of thwarting the equalists."
    lin "a new match becomes available every 7 days, and it pays well."
    lin "In fact, i think there's one going on now."
    tn "there is?"
    lin "yes, and i suggest you move quickly to get there in time."
    tn "i feel under-prepared for this."
    lin "you'll be fine."
    tn "you sure you don't want me to stay?"
    lin "...what?"
    tn "so you can have another go at my cock."
    show bfaa bfaa09 with dissolve
    lin "...."
    tn "oh my gosh! you're blushing!"
    lin "...shut up."
    tn "but... it sounds like i'm going to be doing you a real favor here."
    tn "i don't honestly care about this probending thing, i can find money elsewhere."
    tn "but you need me there, don't you?"
    show bfaa bfaa03 with dissolve
    lin "...i do."
    lin "my men are stretched thin."
    tn "then it's simple..."
    tn "...present your tits."
    lin "i... what?"
    tn "squeeze them together, and say \"please help me\"."
    lin "i'm not doing that."
    tn "then you get no information, and team avatar fails."
    lin "oh, for...."
    show bfaa bfaa07 with dissolve
    lin "these?"
    lin "\"help me, tenzin. please.\""
    show ctc
    pause
    hide ctc
    lin "happy?"
    show bfaa bfaa03 with dissolve
    tn "almost."
    lin "...."
    tn "you're pretty when you're not being a hardass."
    show bfaa bfaa09 with dissolve
    lin "i..."
    tn "there it is again!"
    lin "oh... shut it..."
    tn "lin, i'll go help... but in return..."
    tn "you have to do it again."
    tn "but this time i want you to convince me you need me."
    lin "........."
    lin "................"
    show bfaa bfaa08 with dissolve
    lin "please...."
    lin "i need you tenzin. please."
    lin "i present my tits in payment."
    show ctc
    pause
    hide ctc
    tn "that... was something special."
    lin "...."
    show bfaa bfaa04 with hpunch
    lin "oh, just get the hell out of here."
    tn "alright, alright, calm your tits."
    lin "fuck you."
    tn "you're a powderkeg."
    lin "and you're a dick..."
    lin "making me feel like... oh, whatever."
    lin "just go!"
    scene black with dissolve
    $ probending_available = 1
    jump b4_repcity_map1

label bk4_probending:
    hide screen bk4_money_date2
    scene black
    with Dissolve(1)
    jump bk4_probending_start

label korra_legwork:
    hide screen bk4_money_date
    scene black
    with Dissolve(1)
    "you notice korra's door is slightly ajar."
    menu:
        "peek":
            $ korra_leg = True
            pass
        "come back later ":
            jump b4_airtemple_map1

    "you peek through the crack in the door."
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos -350

    show bfam bfam01
    with Dissolve(1)
    show ctc
    pause
    hide ctc
    kn "333.... 334.... 335...."



    show bfam bfam02
    kn "Tenzin...!"
    show bfam bfam16 with Dissolve(1.5)
    kn "I didn't hear you knock."
    tn "That's because I didn't."
    tn "You working out? "
    kn "Oh... yeah..."
    kn "Nothing special, just some morning exercises for my thighs."
    tn "They look fine to me."

    kn "uhh... thanks?"
    kn "It's just an easy exercise I can do in my room."
    kn "I'd really like to finish the set, if you don't mind."
    tn "No problem, go right ahead."
    tn "I can wait."
    kn "......"
    kn "....fine."

    show bfam bfam04:
        xpos 500
        linear 0.4 xpos 505
        linear 0.4 xpos 500
        repeat
    with fade
    show ctc
    pause
    hide ctc

    kn "336... 337..."
    show ctc
    pause
    hide ctc
    hide bfam
    show bfam bfam17:
        xpos -300
    with Dissolve(1.5)
    kn "umfff!!"
    tn "That's it?"

    show bfam bfam16 with Dissolve(1.5)
    kn "Nah, I still have to do another one."

    show bfam bfam15:
        xpos 250 ypos 30
    with fade
    kn "First I squat and make sure I'm balanced, and then-"
    kn "Oh, wait."
    kn "Probably best to do some stretching for this one."
    hide bfam
    show bfam bfam18
    with Dissolve(1.5)
    kn "....hrrh."
    show ctc
    pause
    hide ctc
    kn "gotta stretch... touch the ground..."
    show ctc
    pause
    hide ctc
    show bfam bfam20 with Dissolve(1.5)
    kn "and...."
    kn "That's better."
    kn "Hold it for few seconds... feel the burn, and..."


    show bfam bfam19 with dissolve
    kn "get back up..."

    show bfam bfam20 with Dissolve(1.5)
    kn "...and repeat."
    pause
    show bfam bfam15a with Dissolve(1.5)
    kn "Okay, enough of that."
    kn "Time for the real deal."
    show bfam bfam15 with Dissolve(1.5)





    show bfam bfam14 with dissolve
    show ctc
    pause
    hide ctc
    kn "This... mpff... is kinda difficult, but very effective."

    pause
    show bfam bfam15 with Dissolve(1.5)
    kn "You know... there's really no need to look at me... or even stay here."
    tn "Keeping an eye on you is my job. "
    tn "As long as your training isn't finished."
    kn "Trust me, I'm trying to learn airbending with everything I've got."
    tn "Which is why you're doing physical exercises instead of meditating on airbending... or doing anything else concerning airbending."
    kn "This is important too."
    kn "A healthy mind in a healthy body."


    show bfam bfam13
    show ctc
    pause
    hide ctc

    kn "hmmff... mmff..."

    show bfam bfam05 with hpunch:
        xzoom 1.0 yzoom 1.0
    kn "Ahhhh!! Oh man... *pant* *pant*"
    show ctc
    pause
    hide ctc

    show bfam bfam06
    kn "That exercise always takes it out of me."
    show ctc
    pause
    hide ctc

    show bfam bfam07
    kn "So... what is it you want from me?"
    show ctc
    pause
    hide ctc
    tn "I totally forgot... oh well."
    tn "Mustn't have been anything important."
    kn "Whatever."
    kn "I'm going to wash up, I've gotten all sweaty."
    kn "Speaking of which..."
    tn "What?"
    kn "Meelo is always coincidentally hanging around the bath whenever I enter or come out."
    kn "It's honestly sort of getting on my nerves."
    tn "I'm certain it's just a coincidence."
    $ korra_leg_daily = True
    jump korra_washroom

label korra_legwork2:
    hide screen bk4_money_date
    scene black
    with Dissolve(1)
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos -350

    show bfam bfam01
    with Dissolve(1)
    if b4_daytime:
        kn "336... 337..."
    else:
        kn "1... 2... 3..."
    show ctc
    pause
    hide ctc

    show bfam bfam02
    if b4_daytime:
        kn "tenzin!"
    kn "hey, how's it look?"
    tn "...good. really good."
    kn "alright, i'm gonna pick up the pace."
    show bfam bfam04:
        xpos 500
        linear 0.4 xpos 505
        linear 0.4 xpos 500
        repeat
    $ renpy.pause()
    kn "mmf... hmgh..."
    show ctc
    pause
    hide ctc
    hide bfam
    show bfam bfam17:
        xpos -300
    with Dissolve(1.5)
    kn "umfff!!"
    tn "That's it?"

    show bfam bfam16 with Dissolve(1.5)
    kn "Nah, I still have to do another one."

    kn "Probably best to do some stretching first though."
    hide bfam
    show bfam bfam18
    with Dissolve(1.5)
    kn "....hrrh."
    show ctc
    pause
    hide ctc
    kn "gotta stretch... touch the ground..."
    show ctc
    pause
    hide ctc
    show bfam bfam20 with Dissolve(1.5)
    kn "and...."
    kn "That's better."
    kn "Hold it for few seconds... feel the burn, and..."


    show bfam bfam19 with dissolve
    kn "get back up..."

    show bfam bfam20 with Dissolve(1.5)
    kn "...and repeat."
    show ctc
    pause
    hide ctc
    show bfam bfam15a with Dissolve(1.5)
    kn "Okay, enough of that."
    kn "Time for the real deal."
    show bfam bfam15 with Dissolve(1.5)





    show bfam bfam14 with dissolve
    show ctc
    pause
    hide ctc
    kn "This... mpff... is kinda difficult, but very effective."

    pause
    show bfam bfam15 with Dissolve(1.5)
    kn "You know... there's really no need to look at me... or even stay here."
    tn "Keeping an eye on you is my job. "
    kn "...okay, then."
    show bfam bfam13
    show ctc
    pause
    hide ctc

    kn "hmmff... mmff..."

    show bfam bfam05 with hpunch:
        xzoom 1.0 yzoom 1.0
    kn "Ahhhh!! Oh man... *pant* *pant*"
    show ctc
    pause
    hide ctc

    show bfam bfam06
    kn "That exercise always takes it out of me."
    show ctc
    pause
    hide ctc

    show bfam bfam07
    kn "hey... did you need something?"
    show ctc
    pause
    hide ctc
    tn "i really don't remember."
    tn "Mustn't have been anything important."
    kn "alright, I'm going to wash up, I've gotten all sweaty."
    $ korra_leg_daily = True
    jump b4_airtemple_map1

label korra_washroom:
    $ korra_wash_daily = True
    hide screen bk4_money_date
    scene black
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    show expression "bk4/backgrounds/hallway_01.jpg"
    if not korra_wash:
        show bfae meelo_03
    with Dissolve(1.5)
    if not korra_wash:
        "As you walk through the building away from korra's room, you see Meelo."
        "He's intently staring at something behind a wall scroll."
        tn "uhhh... whatcha doing there, sprout?"
        show bfae meelo_02 with Dissolve(1.5)
        mee "Looking for treasure!!"
        tn "...in your nose?"
        "Meelo just stares at you."
        tn "....fuck you're creepy."
        mee "....."
        tn "so...."
        tn "have you found any? treasure, i mean?"
        mee "I found some booty!!"
        tn "Ah."
        tn "that's... nice."
        hide bfae with dissolve
        "Meelo runs off, apparantly searching for more treasure."

        tn "Why would he look behind a wall scroll for treasure?"
    if korra_wash:
        tn "ah, there's still a hole behind this scroll."
    tn "Let's see."
    scene black
    if not korra_wash:
        "You find a small hole behind the scroll."
        "Peering through it you see-"
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/bathroom0.jpg"
    show bfak bfak01
    with Dissolve(2.5)


    tn "Damn."
    pause
    if not korra_wash:
        tn "There {size=+10}is{/size} booty here!"
        tn "she's muttering something to herself..."

    kn "...the heck are these bathing rooms so... sparse?"
    kn "No baths, no showers..."
    kn "A watertap and a bucket, plus some soap?"
    kn "Does this have something to do with the airbender culture thing??"


    show bfak bfak00 as bucket behind bfak:
        xpos 500 ypos 400

    show bfak bfak02
    kn "Guess I'll be scrubbing the old fashioned way."

    pause
    show bfak bfak03
    tn "That's right Korra, scrub that watertribe ass of yours while I'm watching..."


    show bfak bfak04
    $ renpy.pause()
    show bfae jinora08:
        xpos -50 ypos 100
    with Dissolve(1.5)
    jino "Hey, Korra!"
    ta "Shit!"
    ta "Come on, move over to the left."
    kn "Hey Jinora."
    kn "something the matter?"


    jino "I was wondering if you need a towel?"
    jino "I used this one, but i didn't get it very wet."
    jino "you can use it to rub yourself down as well, if you want."
    show bfak bfak11
    kn "Thanks! I totally forgot to get one."
    jino "No problem."
    jino "Hmmm..."
    kn "what?"
    jino "I feel a draft coming from somewhere..."
    jino "Well, see you later!"
    jino "Bye, Korra!"
    hide bfae jinora08 with Dissolve(1.5)


    kn "Jinora is a pretty nice girl."
    show bfak bfak03
    kn "I bet she could teach me to airbend infinitely better than her dad."

    show bfak bfak04a
    kn "There's something about him which just irks me sometimes."

    show bfak bfak05
    kn "Man, I wish my tits were just a bit smaller."
    $ renpy.pause()


    show bfak bfak06 at Move((0, 0), (0, 30), .40, bounce=True, repeat=False)
    kn "Hmmpf."
    kn "Hah, I bet there's not a lot of people who can do that from a kneeling position! "
    kn "I'm pretty awesome."
    kn "And now to deal with my sacred place."

    show bfak bfak07
    $ renpy.pause()

    show bfak bfak10
    kn "*sniff* *sniff*"
    kn "hmm... yeah, that needs a few more strokes."
    show bfak bfak07
    $ renpy.pause()

    hide bfak bfak00 as bucket

    show bfak bfak08
    kn "Now to wash it all off..."



    show bfak bfak09
    show expression "bk4/korra/wash/bucketwater.png":
        xpos 800 ypos -150 xzoom 1.0 yzoom 1.0 alpha 1.0
        linear 1.5 xpos 800 ypos 300 xzoom 1.5 yzoom 3.0 alpha 0.0
    $ renpy.pause(1.0)
    show bfak bfak08
    $ renpy.pause(1.0)
    show bfak bfak09
    show expression "bk4/korra/wash/bucketwater.png":
        xpos 800 ypos -150 xzoom 1.0 yzoom 1.0 alpha 1.0
        linear 1.5 xpos 800 ypos 300 xzoom 1.5 yzoom 3.0 alpha 0.0
    $ renpy.pause(1.0)

    show bfak bfak03
    show bfak bfak00 as bucket behind bfak:
        xpos 500 ypos 400
    with Dissolve(1.5)

    kn "Now where's that towel?"
    kn "Ah, there it is."
    show bfak bfak13 with dissolve
    $ renpy.pause(1.0)
    show bfak bfak12
    $ renpy.pause()
    if korra_wash:
        tn "i better leave before I push my luck."
        scene black with dissolve
        jump b4_airtemple_map1

    tn "Yeaaah, now turn around and show me that watertribe pussy."
    jino "Daaaaadd....?"
    "You feel someone tapping you on your shoulder."
    scene black
    show expression "bk4/backgrounds/hallway_01.jpg"
    show bfae jinora04
    with hpunch

    tn "Oh shi-"
    tn "Hey... Jinora, what's up?"
    jino "What were you doing there?"
    menu:
        "checking for cracks":
            tn "I... I was checking for cracks... in the wall."
            tn "Wall cracks."
            tn "terribly dangerous."
            tn "must make sure the building won't collapse."
            tn "In fact... I need to fix this one here."
            jino "Can I take a look at it?"
            tn "What? No! I mean...."
            tn "I'm going to fix this one right now... and I think I saw your mother looking for you."
            tn "Sooooo... you better go find her."
            tn "like... right now."
            "Jinora is clearly not buying the bullshit you're telling her, but leaves anyway."
            hide bfae jinora10 with dissolve
        "None of your business!":

            tn "I'll damn well do what I want, without having to explain myself to a ??? years old!"
            show bfae jinora10 at Move((10, 0), (0, 0), .10, bounce=True, repeat=True, delay=.275)
            jino "I... I was just asking."
            jino "You don't have to get all angry."
            hide bfae
            show bfae jinora10:
                xpos 0
                linear 2.0 xpos -1000 alpha 0
            tn "Ahh, shit..."

    tn "...."
    tn "...korra's ass though."
    tn "mmm."
    tn "that... is a treasure indeed."
    $ korra_wash = True
    jump b4_airtemple_map1


label bk4_swim_time:
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene expression "bk4/backgrounds/park_day_1.jpg":
        ypos 0
    with Dissolve(1)
    tn "you know... it is a nice day."
    pn "...well?"
    tn "hm?"
    show bfac bfac04 with Dissolve(1)
    pn "what do you think?"
    menu:
        "great tits":
            tn "fantastic boobs, as always."
            pn "thanks, dear."
        "alright":
            tn "eh, you look okay."
            pn "you try carrying four kids inside you..."

    show bfac bfac04:
        xzoom -1
    with Dissolve(1)
    show bfac bfac05
    pn "meelo! ikki! jinora!" with hpunch
    pn "have you changed into your swimsuits?"
    show bfae jinora05
    with dissolve
    jino "i have!"
    show bfac bfac04 with dissolve
    pn "good job, dear."
    pn "you look great."
    show ctc
    pause
    hide ctc
    pn "go get your brother and sister."
    jino "okay."
    hide bfae with dissolve
    pn "where's korra?"
    show bfab bfab21
    with dissolve
    kn "hey."
    show ctc
    pause
    hide ctc
    pn "korra dear, you look fantastic."
    show bfab bfab20 with dissolve
    kn "right?"
    kn "my body is kickin'!"
    tn "...."
    tn "you ain't wrong."
    show bfab bfab21 with dissolve
    kn "heehee..."
    pn "i'm going to go sit for a while."
    pn "watch the kids."
    hide bfac with dissolve
    show bfab bfab16 with dissolve
    kn "it's about time you got me a swimsuit!"
    kn "i've already been here [bk4_calendar] days."
    tn "...you're welcome."
    tn "by the way..."
    menu:
        "your nipples are poking out":
            tn "your nipples are wonderfully pointy."
            show bfab bfab17 with dissolve
            kn "what!?"
            show bfab bfab19 with dissolve
            kn "don't be weird, tenzin."
            $ korra_resist +=1
            "korra's {b}resistance{/b} went up!"
        "you could bounce a quarter off those thighs...":

            tn "your legs are looking great."
            show bfab bfab21 with dissolve
            kn "thanks, i think it's all that legwork i've been doing."
            play sound "audio/win2.mp3"
            $ korra_resist -=1
            "korra's {b}resistance{/b} lowered!"
            if korra_resist <=90:
                $ korra_resist = 90
                "korra's {b}resistance{/b} can't go any lower right now."

    show bfae group05:
        xzoom -1
    with dissolve
    jino "come swim with us, korra!"

    show bfab bfab16 with dissolve
    kn "coming to you."
    hide bfab with dissolve
    jino "you too!"
    jino "come swim!"
    tn "alright..."
    hide black
    show black with Dissolve(1)
    "while swimming in the river, you find a stone tablet."
    play sound "audio/win2.mp3"
    $ cipher1 = True
    tn "huh."
    "it seems to be some kind of image... or cipher, maybe."
    tn "interesting..."
    tn "i wonder..."
    hide bfae
    hide black
    show bfac bfac05
    with Dissolve(1.5)
    pn "come on everyone!"
    pn "it's going to get dark soon!"
    show bfac bfac04 with dissolve
    pn "oh? what's that?"
    tn "i don't know, yet."
    pn "well... i'm sure you'll figure it out, you're the most intelligent man i know."
    show bfac bfac05 with dissolve
    pn "meelo! get that out of your nose!"
    pn "no! ikki! that is a private place!"
    pn "do not put rocks in there!"
    tn "...."
    show bfac bfac04 with dissolve
    pn "ready?"
    show bfab bfab21:
        xzoom -1
    with dissolve
    kn "oh, man!"
    kn "i got so many compliments!"
    kn "I love my body..."
    show bfab bfab16 with dissolve
    kn "are we going back now?"
    tn "yup."
    kn "great!"
    kn "i'll lead the way, i'm.. eager to get back."
    hide bfab with dissolve
    tn "...i wonder what that's about?"
    pn "come on, let's get back to the island."
    $ b4_dock_travel = False
    $ bk4_swim_mission = 4
    scene black with Dissolve(1.5)
    scene expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    show bfac bfac02
    with Dissolve(1.5)
    pn "that was a lot of fun."
    pn "thank you for being so wonderful."
    tn "i am the best."
    show bfac bfac06 with dissolve
    pn "korra was acting odd though, wasn't she?"
    tn "i thought so, too."
    pn "why don't you go pay her a visit?"
    pn "make sure she's okay?"
    show bfac bfac02 with dissolve
    pn "...and staying out of trouble."
    tn "good plan."
    jump b4_airtemple_map1

label korra_rubbing:
    hide screen bk4_money_date
    play sound "audio/door.mp3"
    "you open the door to korra's bedroom..."

    stop music
    $ bfag_clothes = True
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0


    show bfag bfag00
    kn "ah!!" with hpunch
    pause
    "before she has a chance to say or do anything else, you step towards her."

    scene black

    show expression "bk4/backgrounds/korra_room_bed.jpg"

    show bfag bfag01 with Dissolve(1.5)
    show bfag bfag01a with hpunch
    kn "....ah."
    tn "how's it going?"
    pause
    kn "t-tenzin..."
    kn "what... what are... why are you in..."
    kn "oh spirits, this is so embarrassing..."

    tn "relax, it's totally normal."
    tn "what got you going?"
    kn "p-please get out..."
    tn "wait, no... you didn't get turned on {i}by your own body{/i}, did you?"
    kn "....th-this is my worst nightmare."
    kn "p-please... please... go..."
    tn "are you sure?"
    kn "y-yes. very, oh, so, very, sure."
    tn "well, alright..."
    tn "but we'll pick this up later."
    kn "i... i don't think so..."
    scene black with Dissolve(1.5)
    "you step out of the room, and hear korra still panicking inside."
    $ bk4_swim_mission = 5
    if korra_moral <=90:
        "korra's {b}morality{/b} can't lowered any more right now."
    else:
        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    $ b4_daytime = False
    $ b4_dock_travel = True
    jump b4_airtemple_map1

label korra_rubbing2:
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0


    show bfag bfag00
    kn "ah!!" with hpunch

    "before she has a chance to say or do anything else, you step towards her."

    scene black

    show expression "bk4/backgrounds/korra_room_bed.jpg"

    show bfag bfag01 with Dissolve(1.5)
    tn "how's it going?"

    show bfag bfag01a with hpunch
    kn "....ah."
    kn "g-go away, tenzin..."
    tn "hmm... how about... no."
    kn "wh...what?"
    tn "you are my student."
    tn "i am your master."
    tn "you are mine to observe at all hours."
    kn "this... shouldn't count..."
    tn "consider it... more concentration training."
    kn "i... what? no!"
    tn "....."
    tn "fine..."
    scene black with dissolve
    "you leave korra in her room."
    tn "I think... it might be time to bring back the amon mask."
    tn "I'll have to make sure i come back at night."
    $ korra_rubbed = 1
    jump b4_airtemple_map1

label amon_mast_scare:
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    scene black
    with dissolve
    "you put on the amon mask and confidently walk into korra's room."
    scene expression "bk4/backgrounds/korra_room_night.jpg"
    show bfam bfam18
    with dissolve
    tam "{b}korra..."
    kn "wait, i know that voice..."

    show bfam bfam06 with hpunch
    kn "no... no, it can't be..."
    kn "how..."
    show bfam bfam07 with dissolve
    kn "how did you get in here!?"
    tam "{b}there is nowhere that i cannot find you."
    kn "please... please... let me go..."
    kn "i... i won't scream..."
    kn "just... don't take my bending... please..."
    kn "It's everything to me..."
    tam "well..."
    tam "perhaps..."
    tam "{i}if{/i}, the next time you see him..."
    menu:
        "tell her to submit to tenzin":
            $ korra_rub_order = 1
            tam "you submit to him."
            kn "...what?"
            tam "the next time you see him... submit to him."
            tam "{b}you know... the only thing that {i}might{/i} be able to defeat me is the avatar state..."
            tam "{b}but you need to master airbending in order to enter it at will."
            tam "{b}so until then, you're at my mercy."
            tam "{b}if only you had an airbending master to teach you..."
            tam "{b}oh, but you do, don't you?"
            kn "....."
            tam "{b}answer me!" with hpunch
            kn "y-yes!"
            kn "yes, i have an airbending master!"
            tam "{b}hmm..."
            tam "{b}then i suggest... the next time you see him... you do whatever he tells you."
            tam "{b}if he says \"jump\" you bounce your tits."
            tam "{b}if he says \"suck\", you say \"how deep\"."
            tam "{b}understand?"
            kn "....yes."
            tam "{b}because next time i visit, you might find yourself suddenly..."
            tam "{b}...equal."
        "tell her to seduce tenzin":

            $ korra_rub_order = 2
            tam "you seduce him."
            kn "...what?"
            tam "the next time you see him... seduce him."
            kn "wh... what...?"
            tam "{b}you have an airbending master, correct?"
            kn "y-y-y-"
            tam "{b}speak!"
            kn "y-yes..."
            tam "{b}hmmm..."
            tam "{b}i bet you have a ridiculously tight... but still very juicy pussy, don't you?"
            kn "i... i don't know..."
            tam "{b}don't you!"
            kn "y-yes! i... i have a very tight and... and... and juicy... p-pussy!"
            tam "{b}i bet your master would love to see it, wouldn't he?"
            kn "n-no..."
            kn "he's... he's married..."
            tam "{b}you're a young girl, i'm certain you can seduce him..."
            kn "s-seduce tenzin!?"
            kn "that's... i couldn't..."
            tam "{b}you will, or i'll take your bending."
            kn "....."
            kn "...why!?"
            tam "{b}because i love the idea of degrading both you and tenzin at the same time."
            tam "{b}call it... my current hobby."
            kn "pl-please, there... there has to be something else..."
            tam "{b}well... you could always master airbending and learn to enter the avatar state..."
            tam "{b}but until that happens, you are at my mercy... and i can visit you at any time."
            kn "...."
            kn "o...okay."
            tam "{b}what was that?"
            kn "the next... next time i see tenzin..."
            kn "i'll... i'll seduce him."


    tam "{b}oh, and one last thing..."
    tam "{b}tell anyone that i have visited you..."
    tam "{b}and i will remove your bending immediately, permanently, and without hesitation."
    tam "{b}do you understand, child?"
    kn "y-yes..."
    tam "{b}good."
    tam "{b}remember our conversation."
    kn "i... i will..."
    tam "{b}i know you will."
    tam "{b}sweet dreams, avatar..."
    scene black with dissolve
    tn "{i}that should get her eager."
    "you head to your room and slip into the bed."
    "you fall fast asleep."
    $ korra_rubbed = 2
    jump bk4_next


label korra_rubbing3:
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    $ bfag_clothes = True
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0


    show bfag bfag00
    kn "tenzin!" with hpunch
    "she doesn't move, so you step towards her."

    scene black

    show expression "bk4/backgrounds/korra_room_bed.jpg"

    show bfag bfag01 with Dissolve(1.5)
    kn "h-hi..."

    show bfag bfag01a with hpunch
    kn "um..."
    if korra_rub_order ==1:
        kn "do... do you want something...?"
        tn "what i want... is to see you masturbate."
        kn "um... are... are you sure?"
        kn "because i could... uh..."
        tn "did i stutter, {i}student{/i}?"
        kn "n-no... i just..."
        tn "let me put it this way, korra..."
        tn "masturbate, in front me, right now..."
        tn "or i stop training you."
        tn "and you face amon alone."
        kn "......."
        show bfag bfag04 with dissolve
        kn "......"
        "korra takes a deep breath."
        show bfag bfag05
        kn "watch, then."

    if korra_rub_order ==2:
        kn "t-tenzin?"
        tn "yes?"
        kn "i... i want to... to show you something."
        tn "oh?"
        kn "i... understand if you don't want to see..."
        tn "i'm a curious man, korra."
        tn "feel free."
        kn "you're just... handsome and... and powerful... and..."
        kn "even though i'm sure you're not interested..."
        tn "i'm always interested in you, korra."
        tn "but are you sure you wouldn't rather i leave?"
        kn "no, i... i want you to watch."
        show bfag bfag01 with dissolve
        kn "what... what do you think?"
        pause
        tn "...looks delicious."
        show bfag bfag01a with hpunch
        kn "th-thank you."
        tn "...was that all?"
        kn "...."
        kn "no, i... i guess not..."
        kn "...."
        kn "...tenzin?"
        tn "yes?"
        show bfag bfag04 with dissolve
        "korra takes a deep breath."
        kn "......"
        show bfag bfag05
        kn "....just watch."

    if korra_rub_order ==3:
        kn "do... do you want something...?"
        tn "what i want... is to see you masturbate."
        kn "um... are... are you sure?"
        kn "because i could... uh..."
        tn "did i stutter, {i}student{/i}?"
        kn "n-no... i just..."
        tn "let me put it this way, korra..."
        tn "masturbate, in front me, right now..."
        tn "or i stop training you."
        tn "and you face amon alone."
        kn "......."
        show bfag bfag04 with dissolve
        kn "......"
        "korra takes a deep breath."
        show bfag bfag05
        kn "watch, then."

    menu:
        "clothes on":
            $ bfag_clothes = True
        "clothes off":
            if korra_tits_out:
                kn "....."
                kn "i guess you've already seen my... breasts... anyway..."

                show bfag bfag12 with dissolve
                pause
                $ bfag_clothes = False
            else:
                kn "...no."
                kn "this... this is plenty right now."


    show bfag bfag04 with dissolve
    kn "....."
    kn "okay...."

    show ctc
    pause
    hide ctc
    kn "here we go..."
    show bfag bfag06
    kn "Mmmnh....."
    show ctc
    pause
    hide ctc


    if korra_rub_order ==1:
        kn "is this what you wanted, you old pervert?"
        kn "you wanted to watch me rub myself?"
    if korra_rub_order ==2:
        kn "do... do you like it?"
        kn "do you like... watching me?"
    if korra_rub_order ==3:
        kn "is this what you wanted, you old pervert?"
        kn "you want to watch me rub myself?"
    show ctc
    pause
    hide ctc

    if korra_rub_order ==1:
        kn "does this make you happy, you jerk?"
    if korra_rub_order ==2:
        kn "wouldn't... ugh, i can't believe i have to say this... wouldn't you love to have your..."
        kn "...your penis here against me?"
        kn "instead of my fingers?"
    if korra_rub_order ==3:
        kn "does this make you happy, you jerk?"
    show ctc
    pause
    hide ctc

    show bfag bfag02
    kn "hmmgh... ahh... y-yeah..."
    kn "that's... that's actually really... ahh... good..."
    show ctc
    pause
    hide ctc


    show bfag bfag03 with Dissolve(1.5)
    kn "ahhhhhh....."
    kn "ohh... shit..."
    show ctc
    pause
    hide ctc
    if korra_rub_order ==1:
        kn "yeah, you... you want to have your fucking way with me..."
        kn "and i... i have to say... say yes..."
        kn "to that big... big... ahhh..."
    if korra_rub_order ==2:
        kn "yeah, i... i want you to have your fucking way with me..."
        kn "and you... you can't help but say... say yes..."
        kn "say... \"please\"..."
        kn "and slip that big... big... ahhh..."
    if korra_rub_order ==3:
        kn "yeah, you... you want to have your fucking way with me..."
        kn "and i... i have to say... say yes..."
        kn "to that big... big... ahhh..."

    show ctc
    pause
    hide ctc

    kn "ahh, i'm soo... hot... and wet..."
    tn "let's see that dripping fountain..."
    show bfag bfag07 with dissolve


    kn "...is this what you want?"
    kn "my creamy... fucking... pussy?"

    show ctc
    pause
    hide ctc
    if korra_rub_order ==1:
        tn "fingers back to work!"
    if korra_rub_order ==2:
        kn "here, i'll get it wetter for you..."
    if korra_rub_order ==3:
        kn "you want a taste, jerk?"

    show bfag bfag08:
        ypos 720
        linear 0.6 ypos 725
        linear 0.6 ypos 720
        repeat

    kn "too... bad..."

    show ctc
    pause
    hide ctc

    kn "ahh... yes... yes!"

    show ctc
    pause
    hide ctc

    show bfag bfag09:
        ypos 720
        linear 0.3 ypos 725
        linear 0.3 ypos 720
        repeat

    show ctc
    pause
    hide ctc

    kn "ah...! ah...!"

    show ctc
    pause
    hide ctc
    kn "i'm... i'm... gonna... i'm gonna fucking..."

    kn "cr{size=+3}ee{size=+3}ee{size=+3}aa{size=+3}aa{size=+3}mm{size=+3}mmm!!!"
    hide bfag
    show bfag bfag10
    show expression "bk4/misc/gush_1.png":
        xpos 500 ypos 300
    with vpunch
    hide expression "bk4/misc/gush_1.png" with dissolve

    show bfag bfag09 with dissolve:
        ypos 720
        linear 0.3 ypos 725
        linear 0.3 ypos 720
        repeat

    $ renpy.pause()



    hide bfag
    show bfag bfag10
    show expression "bk4/misc/gush_1.png":
        xpos 500 ypos 300
    with vpunch
    hide expression "bk4/misc/gush_1.png" with dissolve

    show bfag bfag09 with dissolve:
        ypos 720
        linear 0.3 ypos 725
        linear 0.3 ypos 720
        repeat

    $ renpy.pause()



    hide bfag
    show bfag bfag10
    show expression "bk4/misc/gush_1.png":
        xpos 500 ypos 300
    with vpunch
    hide expression "bk4/misc/gush_1.png" with dissolve

    show bfag bfag11 with Dissolve(2.0):
        ypos 720

    show ctc
    pause
    hide ctc


    tn "Niiice..."
    kn "i... i think... i need to sleep."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head to your room for the night."

    $ korra_rubbed = 3
    if korra_moral <=90:
        pass
    else:

        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    jump bk4_next

label rescue_korra1:

    show expression "bk4_xtra/remove/blackveil.png"
    show bfac bfac02
    with dissolve
    tn "pema, have you seen korra?"
    tn "I bought this airbending scroll and-"
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/(Orchestral) Playful Tension by Shadow16nh.mp3"
    play sound "audio/thud.mp3"
    with hpunch
    "your door is kicked in, and an angry form storms into your room."
    show bfaa bfaa05:
        xzoom -1
    lin "I told you to watch her!" with hpunch
    show bfaa bfaa04 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    tn "...hello, how are you, would you like a cup of tea?"
    tn "how about a tall, frothy mug of-"
    tn "{size=+10}what the fuck are you talking about?"
    tn "and you owe me a new door."
    show bfac bfac03 with dissolve
    pn "....lin."
    show bfaa bfaa03 with dissolve
    lin "....pema."
    "the temperature of the room seems to suddenly drop to frigid."
    pn "lin... i was so sorry to hear about your romantically empty life."
    lin "oh, thank you, pema."
    lin "you know, it's too bad about your crotch goblins... how is your pussy? a mess?"
    pn "i'll have you know, it's phenominally-"
    tn "ladies, have your dick-measuring contest somewhere else."
    tn "lin, why are you here?"
    show bfaa bfaa02 with dissolve
    lin "*deep breath*"
    show bfaa bfaa03 with dissolve
    lin "...trouble."
    tn "great, all cleared up, thanks."
    tn "don't let the the empty space where my door used to be hit you on the way out."
    lin "tenzin... it's korra."
    pn "...what's happened?"
    show bfaa bfaa04 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "i put you in charge of her."
    tn "she never fucking listens!"
    pn "what. happened."
    show bfaa bfaa03 with dissolve
    lin "there... was an equalist rally."
    lin "the one you warned me about."
    tn "and?"
    lin "and..."
    show bfaa bfaa02 with dissolve
    lin "korra's been taken."
    tn "...."
    ta "what!?" with hpunch
    ta "i thought you had extra patrols?"
    show bfaa bfaa04 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "i did!"
    lin "we weren't prepared for the avatar to decide to charge in and try to fight them!"
    ta "where were you during this?!"
    lin "trying to get civilians and suspects under our control and keep bloodshed to minimum!"
    show bfaa bfaa05 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    lin "where were {i}you{/i}!?"
    tn "I was-"
    pn "shut up. both of you."
    show bfaa bfaa04 with dissolve
    pn "korra's in trouble."
    pn "now, she's not my favorite little princess..."
    pn "but she is the avatar, and she is supposed to be under our protection."
    pn "lin..."
    pn "...tell us what we need to do."
    lin "she was kidnapped at the probending arena."
    lin "when amon scattered the equalists, she disappeared with them."
    show bfaa bfaa02 with dissolve
    lin "there's... no telling where she is."
    pn "could she still be at the arena?"
    show bfaa bfaa03 with dissolve
    lin "it's possible, but..."
    lin "unlikely."
    pn "well, do you have any other suggestions?"
    lin "...."
    pn "then that's where we'll start."
    show bfac bfac02 with dissolve
    pn "darling?"
    tn "yes?"
    pn "i think you should start there... what do you think?"
    tn "i think it's the best idea we have so far."
    tn "so that's where i'll go."
    tn "(man, i wish i had any fucking bending ability right now...)"
    lin "i have some other ideas of where she could be."
    lin "I'll check in with my scouts and see what i can do."
    lin "good luck, tenzin."
    tn "good luck to you, too, lin."
    pn "just come home safe, tenzin."
    pn "and lin..."
    show bfac bfac03 with dissolve
    pn "i don't give a fuck about you."
    lin "charming."
    hide bfaa
    show bfac bfac02
    with dissolve
    pn "tenzin..."
    show bfac bfac03 with dissolve
    pn "go fuck up some shit."
    tn "you got it, toots."
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Driving Darkness _ Dying Light.ogg"
    hide screen bk4_money_date
    scene black
    with Dissolve(1.5)
    "you travel to the probending arena."
    tn "fuck, i hope she's here... and that no one else is."
    scene expression "bk4/backgrounds/training_night.jpg"
    with Dissolve(1.5)
    tn "alright, korra... where are you..."
    tn "this place is hard to navigate at night."
    tn "....."
    tn "there was that hallway with rooms that-"
    ta "ow!" with hpunch
    ta "fuck!"
    ta "what did i just step on?"
    tn "....."
    tn "a... mask?"
    tn "...."
    tn "i wonder..."
    tam "huh. it fits."
    tam "cool."
    scene black with Dissolve(1)
    "you find the hallway and start sticking your head in the various rooms."
    scene expression "bk4/backgrounds/tower_night .jpg"
    show bfab bfab11:

        xpos -250


    with Dissolve(1.5)
    kn "*sob*"
    kn "i'm going to lose it... i couldn't even... i didn't stand a chance... he..."
    tam "hey! good to see you again."
    kn "wha-"
    show bfab bfab12
    kn "{size=+10}ahhh!!" with hpunch
    kn "no! no, no!"
    kn "please! don't!"
    tam "...i'm confused."
    tam "oh, the mask!"
    tam "you don't like it?"
    tam "i found-"
    show bfab bfab11 with hpunch
    kn "please, amon!"
    kn "i'm not a threat to you, amon!"
    kn "please don't take my bending away!"
    kn "i'm sorry!"
    kn "i'm so sorry!"
    tam "......."
    tam "(this is {b}amon's{/b} mask...)"
    tam "(that... gives me an idea.)"
    tam "*ahem*"
    tam "{b}avatar korra!" with hpunch
    show bfab bfab12
    kn "eep..."
    tam "{b}you are weak."
    tam "{b}you are in my power."
    tam "{b}and you always will be... until you master all elements... including airbending."
    tam "{b}this city is mine."
    tam "{b}your friends are mine."
    tam "{b}you are nothing."
    tam "{b}and... i will let you go."
    kn "wha... wha..."
    tam "{b}this time."
    tam "{b}but know this... i can remove your bending at any time i wish."
    tam "{b}you are no threat to me."
    tam "{b}so for now, you may go free... but when i decide to take your bending..."
    tam "{b}and i will take your bending..."
    show bfab bfab11
    kn "no... no..."
    tam "{b}as you are now... you will never stop me."
    hide black
    show black
    with Dissolve(1.5)
    "you step back into the hallway as korra sobs in hopeless fear and relief."
    "you wait for a while... until you're sure it's safe..."
    hide black with Dissolve(1.5)
    tn "...korra?"
    tn "korra is that you?"
    kn "ten..."
    kn "tenzin...?"
    kn "*sob*"
    tn "i'm here... i'm here..."
    kn "it... it was horrible..."
    kn "I thought... i thought i'd never bend again..."
    tn "what's the matter?"
    kn "it was amon... he was here."
    kn "he just touched the heads of some probender players... and he took away their bending!"
    kn "they became like... normal humans!"
    kn "it was horrible!"
    kn "then he threatened me...."
    kn "he told me he could take away my bending at any time..."
    tn "ah, you were too weak to beat him."
    kn "I... i didn't stand a chance..."
    tn "let's get you home."
    kn "okay..."

    scene black with Dissolve(1.5)
    "you help korra back to the island, and to her bedroom."
    scene expression "bk4/backgrounds/korra_room_night.jpg":
        ypos 0
    with Dissolve(1)
    show bfab bfab11 with Dissolve(1)
    kn "thank... thank you, tenzin."
    kn "*sniff*"
    kn "come... come talk to me, tomorrow, okay?"
    tn "i will."
    kn "thank you... thank you, tenzin... thank... thanks..."
    kn "thank you so... so much..."
    tn "goodnight, korra."
    scene black with Dissolve(1)
    tn "(i do believe that mask will come in handy.)"
    "you head back to your room and fall fast asleep."
    $ amon_mask = True
    jump b4_airtemple_map1


label korra_rescued_talk:
    hide screen bk4_money_date
    tn "korra?"
    show bfab bfab26 with Dissolve(1.5)
    kn "...i'm sorry."
    show ctc
    pause
    hide ctc
    tn "....."
    kn "you... were trying to teach me."
    kn "to make me a tougher opponent... a stronger one."
    kn "in several different ways."
    kn "and i ignored you."
    kn "i was undeserving."
    show bfab bfab27
    kn "but i promise..."
    kn "i will listen."
    kn "I... i have a lot to learn."
    tn "...."
    kn "i know that, now."
    kn "but... i hope you will forgive me."
    kn "and... give me another chance."
    kn "i'm..."
    show bfab bfab26
    kn "...i'm just so scared."
    kn "I'll do anything."
    kn "help me..."
    show bfab bfab27
    kn "...master tenzin."
    show ctc
    pause
    hide ctc
    tn "no more games, korra."
    tn "you are constantly at risk of... amon."
    tn "your friends and the city are also in danger."
    tn "you, as the avatar, are the only one that can stop him."
    tn "if you are to progress fast enough..."
    tn "i will have to be vicious to you."
    tn "but it will be for your benefit."
    tn "do you understand?"
    kn "i... i think so..."
    kn "i will try..."
    tn "korra... you {i}can{/i} do this."
    tn "because you must."
    show bfab bfab28 with dissolve
    kn "...."
    kn "yes... sir."
    kn "where do we begin?"
    tn "hmmmm...."
    tn "you are serious about this?"
    kn "yes."
    tn "then..."
    menu:
        "squeeze her breast":
            tn "then take a step back."
            hide bfab with dissolve
            show bfab bfab04 with dissolve
            kn "alright..."
            kn "now wha-"
            show bfab bfab22
            kn "!!!!"
            pause
            tn "mmmm.... oh, goodness..."
            tn "so full... so soft..."
            tn "and the friendliest little nipple..."
            kn "wha... wha... wha..."
            kn "ten... zin... you're..."
            show bfab bfab23 with dissolve
            kn "what. are. you. doing."
        "spit on her face":

            show bfab bfab29
            play sound "audio/spit.mp3"
            show expression "bk3/joodee/titplay/spithead.png":
                xpos 150 ypos -50

            kn "ngh!" with hpunch
            pause
            kn "y-you... you just... spit on me..."
            tn "yes, i did."
            tn "your face, avatar korra, is dripping with my spit."
            kn "wh... why?"

    tn "i'm testing your resolve."
    tn "and finding out if you are worth my time."
    kn "hhrrrrr....."
    pause
    kn "i think... that's enough."
    menu:
        "just a little more":
            tn "almost done..."
            $ korra_mad = 2
            $ korra_resist +=1
            "korra's {b}resistance{/b} went up."
            "korra is now {b}angry{/b}."
            kn "i said..."
            hide bfab
            hide expression "bk3/joodee/titplay/spithead.png"
            with dissolve
            show bfab bfab05 with dissolve
            kn "...that's enough."
        "alright, that's enough":

            tn "very well."
            hide bfab
            hide expression "bk3/joodee/titplay/spithead.png"
            with dissolve
            show bfab bfab04 with dissolve
            tn "the lesson is done, anyway."
            $ korra_mad = 1
            $ korra_resist -=1
            "korra's {b}resistance{/b} lowered."
            "korra is now {b}unhappy{/b}."

    tn "test completed."
    tn "you performed... well enough."
    tn "for now."
    kn "so... what's the next step?"
    tn "meditation."
    tn "meet me there."
    kn "alright..."
    $ korra_rescue_talk = True
    jump b4_airtemple_map1

label korra_meditate_slaps:
    $ b4_music_night_on = False
    $ b4_music_day_on = False
    stop music
    play music "audio/Unwritten Return.mp3"

    $ bfaf_clothes = 'full'

    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, 0.0), 0.0)

    hide screen bk4_money_date
    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 1.0)

    $ renpy.pause(2.0)

    show bfaf bfaf01
    with Dissolve(1.5)
    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.4), 0.0)

    menu:
        "fully clothed":
            $ bfaf_clothes = 'full'
        "??????(locked)" if bk4_swim_mission <3:
            "test"
        "swimsuit" if bk4_swim_mission >=4:
            if korra_resist <=90:
                $ bfaf_clothes = 'swimsuit'
                kn "oh... um... okay..."
            else:
                kn "yeah... no."
                $ bfaf_clothes = 'full'

    kn "okay... what first?"
    tn "first?"
    tn "first, i'm going to break you..."
    kn "??"
    tn "...'re concentration."
    tn "meditation is vital for development of the spirit, a crucial element of the avatar's power."
    tn "equally important is the ability to focus, despite distractions..."
    tn "...sometimes painful ones."

    show bfaf bfaf02 with Dissolve(1.5)
    kn "...oh."
    kn "um..."
    kn "okay."
    pause
    tn "close your eyes."
    kn "...."
    tn "take a deep breath."
    tn "this will be a difficult session."
    show bfaf bfaf03 with Dissolve(1.5)
    "korra breathes deeply, and forces herself into a meditative form."

    show bfaf bfaf04 with Dissolve(1.5)
    kn "...."
    tn "korra!"
    tn "korra, you slut!"
    kn "......"
    tn "suck me off!"
    kn "......."
    tn "suck my fucking cock!"
    tn "......"
    tn "............"
    tn "not bad."
    tn "but i said..."
    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_6
    tn "suck my fucking cock!"
    show bfaf bfaf07
    kn "hey!"
    tn "\"hey\" what?"
    kn "........"
    kn "................."
    show bfaf bfaf03 with dissolve
    "korra breathes deeply again, and tries to return to a meditative state."

    menu:
        "squeeze tits":
            show bfaf bfaf08
            tn "mmmm...."
            tn "decadent..."
            kn "hhrrr..."
            show bfaf bfaf09
            pause
            kn "you assho-"
            $ temp_boolean = True
        "spin hair":

            show bfaf bfaf10
            pause
            $ temp_boolean = False

    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_7

    show bfaf bfaf11
    kn "stop it, you asshole!" with hpunch
    tn "......"
    show bfaf bfaf07 with dissolve
    tn "very well."
    tn "it was nice knowing you as you are, avatar."
    tn "good luck with amon."

    show bfaf bfaf12 with dissolve
    kn "w-wait!"
    kn "I'm... i'm sorry!"
    kn "don't abandon me, i need you."
    kn "...please."
    tn "hmmm..."
    tn "then what do you think the right course of action should be here?"
    kn "um..."
    kn "the hair thing?"
    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_8
    tn "wrong!"
    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_9
    show bfaf bfaf07
    kn "ow!! that hurts!"
    tn "good!"
    tn "now beg me for another!"
    kn "......"
    kn "please can... hrrr..."
    kn "please can i have another..."
    kn "another..."
    kn "slap-"
    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_10
    kn "ow!!"
    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_11
    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_12
    kn "ungh!!"
    show bfaf bfaf12 with dissolve
    kn "owww...."
    tn "well done."
    show bfaf bfaf07 with dissolve
    if temp_boolean:
        $ korra_mad += 2
        if korra_mad ==2:
            "korra is now {b}angry{/b}."
        if korra_mad ==3:
            "korra is now {b}furious{/b}."
    else:
        $ korra_mad += 1
        $ korra_resist -=1
        $ korra_moral -=1
        "korra's {b}resistance{/b} lowered."
        "korra's {b}morality{/b} lowered."
        if korra_mad ==1:
            "korra is now {b}unhappy{/b}."
        if korra_mad ==2:
            "korra is now {b}angry{/b}."
        if korra_mad ==3:
            "korra is now {b}furious{/b}."

    $ b4_daytime = False
    tn "well done, korra."
    tn "i know that was difficult, but you passed with mostly flying colors."
    tn "go rest."
    tn "we're just getting started."
    show bfaf bfaf12 with Dissolve(1)
    kn "*gulp*"
    kn "okay..."
    hide bfaf with Dissolve(1.5)
    tn "finally..."
    $ korra_rescue_slap = True
    jump b4_airtemple_map1

label lin_buttjob1:
    hide screen bk4_money_date
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"

    show bfan bfan01
    with fade
    lin "yes... yes, this is good news."
    lin "finally."
    lin "well, i believe you've earned yourself a reward."
    lin "what would you like?"
    lin "money? a get-out-of-jail-free card?"
    lin "if it's in my power to give, i will."
    tn "hmm..."
    tn "I have an idea."
    lin "oh?"
    tn "stand up for a moment."
    lin "...very well."
    hide bfan with dissolve
    lin "is this-"
    stop music
    play music "audio/Unwritten Return.mp3"
    play sound "audio/fleshslap.mp3"
    hide bfan
    show bfap bfap01
    with hpunch
    lin "ungh!"
    "with a shove, you force lin over her desk."
    lin "...what are you doing, tenzin?"
    tn "i was thinking that my reward should be best expressed using your ass."
    lin "oh... that's not..."
    tn "Now I'll just take out my cock and..."
    show bfap bfap01a at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    tn "put it between your ass-cheeks."
    hide bfap
    show bfap bfap02:
        xpos 0
        linear 0.8 xpos 5
        linear 0.4 xpos 0
        repeat
    lin "mmmgh..."
    lin "st-stop this right now, tenzin..."
    show ctc
    pause
    hide ctc
    tn "hnn... yeah... you feel that cock pressing through your nice tight work clothes?"
    lin "stop... st... mmm... so forceful..."
    tn "you like it, don't you, slut?"
    lin "mnn... no..."
    tn "i like having my way with your ass..."
    tn "fucking up through this thin fabric..."
    lin "you can't... can't do this here..."
    tn "but you're not going to stop me, are you?"
    lin "......."
    show ctc
    pause
    hide ctc
    tn "you want your pants covered in jizz?"
    lin "mmmm..."
    tn "is that a yes?"
    lin "n-no... don't... don't do that..."
    lin "I'll have to sit in it all day..."
    tn "okay, then."
    hide bfap
    show bfap bfap03b at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    "You quickly pull down Lin's pants."
    lin "{size=+15}Ah!!! What are you doing?!{/size}"
    tn "you said you don't want cum on your uniform."
    lin "i didn't mean you could... for you to..."
    lin "......"
    show bfap bfap03d at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
    lin "Don't pull down my pants without even warning me!"
    lin "Do something like that again and your kids will visit their daddy in jail!"
    tn "but it's such a beautiful, juicy butt."


    show bfap bfap03
    lin "...Fine."
    lin "i forgive you."
    lin "But keep in mind, another surprise and-"


    tn "hold that thought."
    lin "what-"
    play sound "audio/spit.mp3"
    show expression "bk4/lin/butjob/spit.png":
        linear 4.0 alpha 0.0 ypos 80
    show bfap bfap03a
    lin "oh!"
    show ctc
    pause
    hide ctc
    "You spread Lin's ass cheeks and spit, aiming for her anus."
    "Before lin fully realizes what you did, you quickly start pressing your cock against her anus."

    hide expression "bk4/lin/butjob/spit.png"

    show bfap bfap04
    with dissolve
    "her warm asscheeks cradle your shaft as you slide up and down in their tight, cozy embrace."
    lin "mmmm...."
    show ctc
    pause
    hide ctc
    tn "This is much, much better."
    lin "as long... as you're... being degraded..."
    tn "right... yeah."
    tn "it's {i}me{/i} being degraded here."
    lin "yeah... degraded... right in my office..."
    tn "Uh... I mean this feels... really humiliating?"
    tn "you know..."
    tn "forcing my dick up against a pretty woman's anus without even getting to enter it seems like a shame..."

    lin "Compliments won't change a thing, Tenzin."
    lin "this is all the torture i'll allow you."

    lin "i think letting you do this, teasing you but never allowing you to go all the way..."
    lin "i think this is the perfect balance of reward and punishment."
    lin "The moment you picked Pema over me you gave up all penetration privileges."
    lin "But beg all you want."
    lin "I like hearing you grovel."
    tn "well, i could kneel, but..."
    tn "i bet if you kneel on you desk, it would feel even better for you.."
    lin "....."
    show bfap bfap05 with Dissolve(1.5)
    "Without saying anything, but panting heavily, Lin crawls on her desk."
    show ctc
    pause
    hide ctc
    lin "......"


    tn "You look as tight as a 20 year old."
    show bfap bfap06b with dissolve
    lin "Pfff, naturally."
    lin "I bet Pema is all loose and stretched out by now with all those pregnancies."
    lin "But that was what you were looking for when you chose her over me, right?"
    lin "A cow to breed your offspring."
    tn "Let's not bring the past into this ({size=-10}because I barely know what happened in Tenzin's past{/size})."
    tn "Why don't you start moving that luscious ass of yours?"
    lin "......."

    show bfap bfap07 with Dissolve(1.5)
    lin "like this?"
    show ctc
    $ renpy.pause()
    hide ctc
    "you press harder against lin's rosebud, also slipping against her pussy as you hump her full, round bottom."
    tn "That's... mmmgh... that's more like it."
    lin "It is?"
    lin "Does it make you want to stick that dumb dick of yours in my pussy?"
    lin "Or maybe my ass?"
    menu:
        "That'd be very nice":
            lin "Good, I want you to want it."
            lin "I want you to want it so much you'll be thinking of it when you're fucking that breeding cow of yours."
            lin "Thinking about my tight pussy while going in and out of that fucking hallway that Pema calls her vagina."
            tn "That sounds a bit... harsh."
            lin "Whatever."
            lin "My pristine pussy is off limits."
        "Is that an invitation?":

            lin "No."
            lin "If I said you could, you'd be balls deep in my ass before I reached the end of the sentence."
            lin "Slamming that cock of yours in so deep and hard I'd have trouble staying on this desk."
            lin "Wouldn't you?"
            tn "I'd make you forget every lonely night you've ever had."


    lin "If you try to cross that line, I'm going to take you in for attempted rape and throw you in jail."
    tn "We could play warden and prisoner."
    tn "Besides water and bread, you could feed me pussy!"
    lin "More like... I'd throw away the key and forget all about you."
    tn "Hey, that reminds me..."
    tn "Wouldn't metalbenders be able to easily escape from your prison?"
    lin "Don't be dumb, they're made out of the purest platinum there is."
    tn "oh... uh... fuck..."
    lin "hmm?"
    tn "I'm gonna cum!"
    show ctc
    pause
    hide ctc
    tn "Not seeing any tissues yet soooo..."
    tn "Ass or Face?!"

    menu:
        "face":
            tn "Turn around and take it like a professional."
            show bfap bfap09 with Dissolve(1.5)
            show bfap_dickjack
            show ctc
            pause
            hide ctc
            tx "that's it! right there!"
            lin "i can't believe i'm going to let you..."
            b4_tx "Ready... aim... fire!!!"
            play sound "audio/splurt2.ogg"
            show bfap_spermshotface
            show expression "bk4/lin/butjob/spermface1.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfap_spermshotface
            show expression "bk4/lin/butjob/spermface2.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfap_spermshotface
            show expression "bk4/lin/butjob/spermface3.png" with hpunch
            hide bfap_dickjack
            show expression "bk4/lin/butjob/dickjack2.png"
            hide bfap_dickjack
        "ass":

            tn "Raise that ass, girl!"
            show bfap bfap08 with Dissolve(1.5)

            show bfap_dickjack
            show ctc
            pause
            hide ctc
            tx "that's it! right there!"
            lin "i can't believe i'm going to let you..."
            b4_tx "Here... it... COMES!!!"
            play sound "audio/splurt2.ogg"
            show bfap_spermshot
            show expression "bk4/lin/butjob/sperm1.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfap_spermshot
            show expression "bk4/lin/butjob/sperm2.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfap_spermshot
            show expression "bk4/lin/butjob/sperm3.png" with hpunch
            hide bfap_dickjack
            show expression "bk4/lin/butjob/dickjack2.png"
            hide bfap_dickjack

    show ctc
    pause
    hide ctc
    lin "....."
    lin "holy... fuck..."
    b4_ts "Wooot!"
    b4_ts "Consider me rewarded!"
    ts "and humiliated!"
    lin "I'm... i'm so... fucking... drenched..."
    lin "tenzin, this... this isn't okay..."
    lin "i... i have a job to do..."
    ts "well, good luck."
    lin "don't... don't just..."
    ts "see you later!"
    show ctc
    pause
    hide ctc
    lin "you fucking-"
    scene black with dissolve
    "you head out the door, tucking your dick back into your pants as lin shouts cursewords at you."
    $ b4_daytime = False
    $ lin_buttstuff = True
    jump b4_airtemple_map1

label lin_buttjob2:
    tn "let's go to your desk."
    lin "...."
    lin "okay..."
    hide screen bk4_money_date
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"

    show bfan bfan01
    with fade
    lin "well?"
    lin "what did you want?"
    tn "stand up for a moment."
    lin "ugh. fine."
    hide bfan with dissolve
    lin "is this-"
    stop music
    play music "audio/Unwritten Return.mp3"
    play sound "audio/fleshslap.mp3"
    hide bfan
    show bfap bfap01
    with hpunch
    lin "ungh!"
    "with a shove, you force lin over her desk."
    lin "what are you doing?!"
    tn "i was thinking that i should get off using your ass."
    lin "you can't... just..."
    show bfap bfap01a at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    tn "mmmm..."
    tn "you were saying?"
    hide bfap
    show bfap bfap02:
        xpos 0
        linear 0.8 xpos 5
        linear 0.4 xpos 0
        repeat
    lin "mmmgh..."
    lin "st-stop this right now, tenzin..."
    show ctc
    pause
    hide ctc
    lin "stop... st... mmm... so forceful..."
    tn "you like it, don't you, slut?"
    lin "mnn... no..."
    tn "i like having my way with your ass..."
    tn "fucking up through this thin fabric..."
    lin "you can't... can't do this here..."
    tn "but you're not going to stop me, are you?"
    lin "......."
    show ctc
    pause
    hide ctc
    tn "you want your pants covered in jizz?"
    lin "mmmm..."
    tn "is that a yes?"
    lin "n-no... don't... don't do that..."
    lin "I'll have to sit in it all day..."
    tn "okay, then."
    hide bfap
    show bfap bfap03b at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    "You quickly pull down Lin's pants."
    lin "{size=+15}Ah!!! What are you doing?!{/size}"
    tn "you said you don't want cum on your uniform."
    lin "i didn't mean you could... for you to..."
    lin "......"
    show bfap bfap03d at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
    lin "Don't pull down my pants without even warning me!"
    tn "but it's such a beautiful, juicy butt."


    show bfap bfap03
    lin "...Fine."
    lin "i'll let it slide, but don't even think about-"
    play sound "audio/spit.mp3"
    show expression "bk4/lin/butjob/spit.png":
        linear 4.0 alpha 0.0 ypos 80
    show bfap bfap03a
    lin "oh!"
    show ctc
    pause
    hide ctc
    "You spread Lin's ass cheeks and spit, aiming for her anus."
    "Before lin can say anything, you press your cock against her anus."

    hide expression "bk4/lin/butjob/spit.png"

    show bfap bfap04
    with dissolve
    "her warm cheeks cradle your shaft as you slide up and down in their tight, cozy embrace."
    lin "mmmm...."
    show ctc
    pause
    hide ctc
    tn "This is much, much better."
    lin "as long... as you're... being degraded..."
    tn "right... yeah."
    tn "it's {i}me{/i} being degraded here."
    lin "yeah... degraded... right in my office..."
    tn "Uh... I mean this feels... really humiliating?"
    tn "you know..."
    tn "forcing my dick up against a pretty woman's anus without even getting to enter it seems like a shame..."

    lin "Compliments won't change a thing, Tenzin."
    lin "this is all the torture i'll allow you."
    tn "well..."
    tn "i bet if you kneel on you desk, it would feel even better for you."
    lin "....."
    show bfap bfap05 with Dissolve(1.5)
    "Without saying anything, but panting heavily, Lin crawls on her desk."
    show ctc
    pause
    hide ctc
    lin "......"


    tn "You look as tight as a 20 year old."
    show bfap bfap06b with dissolve
    lin "Pfff, naturally."
    tn "Why don't you start moving that luscious ass of yours?"
    lin "......."

    show bfap bfap07 with Dissolve(1.5)
    lin "like this?"
    show ctc
    $ renpy.pause()
    hide ctc
    "you press harder against lin's rosebud, also slipping against her pussy as you hump her full, round bottom."
    tn "That's... mmmgh... that's more like it."
    lin "It is?"
    lin "Does it make you want to stick that dumb dick of yours in my pussy?"
    lin "Or maybe my ass?"
    menu:
        "That'd be very nice":
            lin "Good, I want you to want it."
            lin "but my pristine pussy is off limits."
        "Is that an invitation?":

            lin "No."
            lin "If I said you could, you'd be balls deep in my ass before I reached the end of the sentence."

    tn "oh... uh... fuck..."
    lin "hmm?"
    tn "I'm gonna cum!"
    show ctc
    pause
    hide ctc
    tn "Not seeing any tissues yet soooo..."
    tn "Ass or Face?!"

    menu:
        "face":
            tn "Turn around and take it like a professional."
            show bfap bfap09 with Dissolve(1.5)
            show bfap_dickjack
            show ctc
            pause
            hide ctc
            tx "that's it! right there!"
            lin "i can't believe i'm going to let you..."
            b4_tx "Ready... aim... fire!!!"
            play sound "audio/splurt2.ogg"
            show bfap_spermshotface
            show expression "bk4/lin/butjob/spermface1.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfap_spermshotface
            show expression "bk4/lin/butjob/spermface2.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfap_spermshotface
            show expression "bk4/lin/butjob/spermface3.png" with hpunch
            hide bfap_dickjack
            show expression "bk4/lin/butjob/dickjack2.png"
            hide bfap_dickjack
        "ass":

            tn "Raise that ass, girl!"
            show bfap bfap08 with Dissolve(1.5)

            show bfap_dickjack
            show ctc
            pause
            hide ctc
            tx "that's it! right there!"
            lin "i can't believe i'm going to let you..."
            b4_tx "Here... it... COMES!!!"
            play sound "audio/splurt2.ogg"
            show bfap_spermshot
            show expression "bk4/lin/butjob/sperm1.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfap_spermshot
            show expression "bk4/lin/butjob/sperm2.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfap_spermshot
            show expression "bk4/lin/butjob/sperm3.png" with hpunch
            hide bfap_dickjack
            show expression "bk4/lin/butjob/dickjack2.png"
            hide bfap_dickjack

    show ctc
    pause
    hide ctc
    lin "....."
    lin "holy... fuck..."
    b4_ts "Wooot!"
    b4_ts "Consider me rewarded!"
    ts "and humiliated!"
    lin "I'm... i'm so fucking soaked..."
    lin "tenzin, this is... this isn't okay..."
    lin "i... i have a job to do..."
    ts "well, good luck."
    lin "don't... don't just..."
    ts "see you later!"
    show ctc
    pause
    hide ctc
    lin "you fucking-"
    scene black with dissolve
    "you head out the door, tucking your dick in your pants as lins shouts swearwords at you."
    $ b4_music_day_on = False
    $ b4_daytime = False
    $ lin_buttstuff = True
    jump b4_airtemple_map1

label korra_protein1:
    show expression "bk4/backgrounds/hallway_01.jpg":
        ypos 0
    with fade
    tn "Okay, I've got a protein shake."
    tn "And now to add a personal touch for Korra..."
    show bfar bfar00
    b4_tx "Hnnnng... gonna give you the best nutritional shake you've ever... had!"
    play sound "audio/splurt2.ogg"
    show bfar bfar00a with hpunch
    show bfar bfar00
    pause(0.5)
    play sound "audio/splurt3.ogg"
    show bfar bfar00a with hpunch
    show bfar bfar00
    pause(0.5)
    play sound "audio/splurt1.ogg"
    show bfar bfar00a with hpunch

    hide bfar
    tn "Okay, now to find Korra."

    show bfae jinora02 with dissolve
    jino "Hey!"
    tn "ah! fuck!"
    tn "how long have you been standing there?"
    jino "What's that?"
    tn "...it's a protein shake for Korra."
    jino "oooh, can I have a taste?"
    tn "uh, no, it's for Korra."
    jino "Just a few sips."
    tn "...It's for Korra."
    jino "Just one sip."
    tn "I... I {size=+10}really{/size} don't think you'd like the taste of this."
    show bfae jinora03
    jino "So Korra gets drinks from you and I don't?"
    show bfae jinora04
    jino "that's not fair!"
    jino "You're already spending all of your time with her!"
    jino "and none with me!"
    jino "And I'm not sure it's always only training!!"
    tn "Wha... what?"

    show bfae jinora03 with dissolve
    jino "nothing..."

    tn "...do you really want to have some of this shake?"
    show bfae jinora02 with dissolve
    jino "Yes."

    menu:
        "Not gonna happen":
            tn "I mean it's a super special reward for Korra."
            tn "Because she did really well during training, so..."
            jino "I also try my best! Always!"
            tn "Trust me, you're better off not tasting this."
            show bfae jinora04
            "Jinora is clearly unsatisfied with your reaction."
            tn "You're really into this whole airbender thing, right?"
            jino "Yes!"
            tn "How about this..."
            tn "When it's time to get your own arrow tattoos... I'll back you up on it."
            show bfae jinora03
            jino "Really?"
            show bfae jinora02
            jino "AWESOME!!"
            tn "Just to be clear, you're {i}still{/i} nowhere near the tattoo level."
            tn "But when you are, I'll help convince your mom."
            jino "I'm going to train twice as hard!"
            tn "...sure?"
            jino "I'm going to train right now!"
            tn "Oh, and you can't tell anyone about our deal."
            jino "Okay!"
            hide bfae
            show bfae jinora02:
                linear 1.0 xpos 300
        "fine, but don't complain afterwards":

            show bfae jinora11
            tn "It's not like it can do any harm... I think."
            tn "Still, i just know I'm going to regret this."
            tn "(and possibly go to hell...)"
            tn "Here you go."
            jino "Thanks!"
            hide bfae
            show bfae jinora12:
                ypos 0
                linear 0.4 ypos 15
                linear 0.4 ypos 0
                repeat
            jino "*glug* *glug*"
            hide bfae
            show bfae jinora11
            jino "this is... weird."
            jino "really... creamy?"
            jino "is that the word?"
            jino "kind of pungent..."
            hide bfae
            show bfae jinora12:
                ypos 0
                linear 0.4 ypos 15
                linear 0.4 ypos 0
                repeat
            tn "Oh man... Hey, you said a few sips!"
            tn "Stop that, damn it!"
            hide bfae
            show bfae jinora11
            tn "Damn, you drank a lot..."
            jino "Sorry!"
            tn "Ah, forget it."
            tn "I think I can make some more."
            tn "Now go do something elsewhere."
            jino "Okay."
            hide bfae
            show bfae jinora02:
                linear 1.0 xpos 300


            tn "Okay, here I go again."
            hide bfae jinora02
            show bfar bfar00
            b4_tx "Hnnnng...!"
            play sound "audio/splurt2.ogg"
            show bfar bfar00a with hpunch
            show bfar bfar00
            pause(0.5)
            play sound "audio/splurt3.ogg"
            show bfar bfar00a with hpunch
            show bfar bfar00
            pause(0.5)
            play sound "audio/splurt1.ogg"
            show bfar bfar00a with hpunch
            hide bfar

    tn "Finally, now let's find Korra before anyone else shows up."

    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    scene
    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0
    show bfar bfar01
    with Dissolve(1.5)
    tn "Hey Korra, I was thinking..."
    kn "I didn't do it."
    tn "What?"
    kn "I mean... what's up, dude?"
    tn "I've got something for you."
    kn "Is it chores?"
    tn "I can give you those too.. but for now it's this."

    show bfar bfar02
    kn "uh, what's that?"
    tn "With an airbender's diet, I guessed an energetic girl like you needs more than the usual amount of protein."
    tn "It's a super protein shake."

    show bfar bfar03
    kn "Oh... uh... thanks?"
    kn "The stuff Pema makes is kind of bland."
    tn "I'll let her know you think that."
    kn "Yeahhh... let's not."
    kn "Pema is always riding my ass about one thing or another."
    kn "She really doesn't need more of an incentive to dislike me."

    show bfar bfar04
    tn "Oh, I thought you two got along just fine."
    kn "What's in this, anyway?"
    tn "Just your average stuff... plus a secret airbender ingredient."
    kn "Normally I'd say you're messing with me and put something rancid in there, but it kinda makes sense."
    tn "It does?"
    kn "Aren't you airbender monks vegetarians or something?"
    kn "It stands to reason you'd need something extra to suplement the protein lack."
    tn "uhh... yeah, that's it."
    kn "Well, let's give it a taste test."
    kn "It's probably going to taste horrible."
    play sound "audio/gulp2.mp3"
    show bfar bfar05
    "*Glug* *glugh* *glugh*"
    show ctc
    pause
    hide ctc
    "You watch as Korra lets your secret sauce glide down her throat."

    show bfar bfar07 with Dissolve(1.5)
    kn "huh..."
    show ctc
    pause
    hide ctc
    tn "So? How is it?"
    kn "really... uh... strong?"
    kn "what's in this?"
    tn "i'll tell you when you're a proper airbender."
    kn "it's... strangely enticing though..."
    kn "it's like... mmmmm... gooey?"
    kn "but in a way that makes me want to keep trying it."
    play sound "audio/gulp.mp3"
    show bfar bfar05
    kn "*Glugh*"
    kn "you could probably... *glugh*... sell this stuff!"
    tn "Yeah, in jars to an entire southern watertribe village."

    show bfar bfar06
    kn "That's oddly specific..."
    kn "but yeah, I guess."
    kn "Why?"
    kn "do you have any plans to really market this stuff?"
    show bfar bfar08
    tn "I'm awesome, but I doubt I can rub out enough to make this a real enterprise."


    show bfar bfar09
    kn "rub... out?"
    tn "It's sperm."
    tn "The secret ingredient is sperm and you've just been gulping down my seed like it's the best thing in the world."

    show bfar bfar10 at Move((10, 0), (0, 0), .10, bounce=True, repeat=True, delay=.275)

    show expression "bk4/korra/protein/barf.png":
        ypos -30
        linear 2.0 ypos 400
    kn "*Barf*"

    show bfar bfar11
    kn "What the fuck, Tenzin?!"
    b4_ts "Hahaha, you're so gullible!"
    b4_ts "And clearly not far enough along with your training if you let that disturb you."
    show bfar bfar12
    kn "So it's not sperm?"
    kn "You really had me freaking out!"
    kn "That wasn't funny!"
    b4_ts "Nah, it was awesome."
    ts "You going to finish that or did I scare you too much?"
    show bfar bfar13
    kn "You? Scaring me?!"
    kn "In your dreams!"
    show bfar bfar05
    show ctc
    $ renpy.pause()
    hide ctc
    kn "*burp*"
    show bfar bfar04
    kn "See? No problem whatsoever."
    show bfar bfar04 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    kn "*burppp*"
    kn "okay... anytime you want to give me protein i'll drink it, tenzin."
    tn "oh, i will."
    kn "great, well, now i should exercise while i've got it in me."
    tn "have fun..."
    $ b4_daytime = False
    $ k_protein = 3
    if korra_moral >=90:
        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    else:
        pass


    jump b4_airtemple_map1

label korra_protein2:
    show expression "bk4/backgrounds/hallway_01.jpg":
        ypos 0
    with fade
    tn "Okay, I've got a protein shake."
    tn "And now to add a personal touch for Korra..."
    show bfar bfar00
    b4_tx "Hnnnng... gonna give you the best nutritional shake you've ever... had!"
    play sound "audio/splurt2.ogg"
    show bfar bfar00a with hpunch
    show bfar bfar00
    pause(0.5)
    play sound "audio/splurt3.ogg"
    show bfar bfar00a with hpunch
    show bfar bfar00
    pause(0.5)
    play sound "audio/splurt1.ogg"
    show bfar bfar00a with hpunch

    hide bfar
    tn "Okay, now to find Korra."

    scene
    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0
    show bfar bfar01
    with Dissolve(1.5)
    tn "Hey Korra, I brought you another super protein shake."

    show bfar bfar02
    kn "uh, thanks."
    kn "i saw pretty good results after the last one."

    show bfar bfar03
    kn "I've kind of been... thinking about this."

    show bfar bfar04

    kn "Well, let's give it go."
    play sound "audio/gulp2.mp3"
    show bfar bfar05
    "*Glug* *glugh* *glugh*"
    show ctc
    pause
    hide ctc
    "You watch as Korra let's your secret sauce glide down her throat."

    show bfar bfar07 with Dissolve(1.5)
    kn "mmmgh..."
    show ctc
    pause
    hide ctc

    kn "just as... strong as i remember it being."
    kn "It's like... an aquired taste?"
    kn "but one i'm really enjoying."
    kn "it's like... mmmmm... creamy?"
    play sound "audio/gulp.mp3"
    show bfar bfar05
    kn "*Glugh*"
    kn "you could probably... *glugh*... sell this stuff!"

    show bfar bfar06
    kn "it does kinda make my throat sticky."
    show bfar bfar08
    tn "I'm not surprised."
    tn "just a reminder, it really is semen in there."
    show bfar bfar09
    kn "w-what?!"
    tn "The secret ingredient is my sperm."

    show bfar bfar10 at Move((10, 0), (0, 0), .10, bounce=True, repeat=True, delay=.275)

    show expression "bk4/korra/protein/barf.png":
        ypos -30
        linear 2.0 ypos 400
    kn "*Barf*"

    show bfar bfar11
    kn "What the fuck, Tenzin?!"
    b4_ts "Hahaha, you're so gullible!"
    b4_ts "And clearly not far enough along with your training if you let that disturb you."
    show bfar bfar12
    kn "So it's not sperm?"
    kn "You really had me freaking out!"
    kn "That wasn't funny!"
    b4_ts "Nah, it was awesome."
    ts "You going to finish that or did I scare you too much?"
    show bfar bfar13
    kn "You? Scaring me?!"
    kn "In your dreams!"
    show bfar bfar05
    show ctc
    $ renpy.pause()
    hide ctc
    kn "*burp*"
    show bfar bfar04
    kn "See? No problem whatsoever."
    show bfar bfar04 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    kn "*burppp*"
    kn "okay... anytime you want to give me protein i'll drink it, tenzin."
    tn "oh, i will."
    kn "great, well, now i should exercise while i've got it in me."
    tn "have fun..."
    $ b4_daytime = False
    if korra_moral >=90:
        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    else:
        pass

    jump b4_airtemple_map1

label asami_tits1:
    hide screen bk4_money_date
    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0
    with fade

    tn "alright, time to call asami about those photos..."
    b4_tp "Hey Asami, this is Tenzin."
    asa "how did you get this number?"
    tp "i'm one of the most powerful men in republic city, how do you think i got it?"
    asa "forced it out of korra?"
    tp "...."
    tp "yes."
    tp "Can I get you to come over?"
    asa "uh... why?"
    b4_tp "I have a photograph of your father and... well, you better come over because this could affect Future industries."
    asa "Then shouldn't you talk to my father instead?"
    b4_tp "Saying more on the phone could be dangerous."
    asa "Okay... where are you?"
    b4_tp "Just come to the top of the tower on air temple island."
    show black with dissolve
    "after waiting for half an hour Asami arrives."
    hide black
    show bfad bfad01
    with dissolve
    asa "Okay, Let's see this photograph."
    "You show her the photo of her Dad, the owner of Future industries, together with Amon."
    show bfad bfad04 with Dissolve(1.5)
    asa "This... this can't be!"
    tn "Yeah, hard to believe, but it looks like your dad's financing a terrorist organization."
    tn "Man, what's the world coming to?"
    asa "I'm sure this is tampered with somehow."
    asa "Let me have that photo."
    tn "Look asami, I understand this is difficult for you to accept, but we can't just sweep this under the rug."
    asa "I could pay you handsomely for it."
    tn "I can't take your money..."
    tn "(wait, why can't I? I love money!)"
    asa "Because your position as councilman?"
    asa "If unsavory financial ties between Future industries and you would be uncovered...."
    tn "uh... let's say yes."
    tn "(I'm taking Tenzin's body for a ride, but I don't want to burn it to the ground.)"
    show bfad bfad02
    asa "...okay."
    asa "Then what?"
    asa "There must be something I can do to change your mind."
    tn "..."
    tn "Suck my co-"
    show bfae meelo_01:
        xpos 300
        linear 1.0 xpos 0
    mee "Hello, pretty lady!"
    asa "Uhh, hello?"
    tn "Awh shit!"
    tn "What are you doing here, Meelo?!"
    tn "Never mind."
    tn "meelo, come here."
    mee "yeah?!"
    tn "I think I just saw Korra getting ready to wash herself. Hint hint."
    mee "oh!"
    mee "Till we meet again, pretty lady!"
    show bfae meelo_01:
        xpos 0
        linear 1.0 xpos 300
    asa "that... was a weird thing to tell him."
    tn "don't judge me, you... you... daughter of a terrorist financier!"
    asa "...what?"
    tn "Ahem."
    tn "it's very, very warm here."
    tn "don't you agree Asami?"
    asa "Not really, why do you..."
    show bfad bfad03 with dissolve
    asa "oh..."
    asa "Is that how it's going to be?"
    tn "Just saying it's warm."
    show bfad bfad02 with dissolve
    asa "......"
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfad with dissolve
    show bfaq bfaq07 with Dissolve(1.5)
    tn "What're you doing?"
    asa "Like you said, it's warm."
    asa "I'm just trying to cool off."
    show ctc
    pause
    hide ctc
    "asami glares at you with enough venom to kill."

    show bfaq bfaq06 at Move((0, 0), (0, -15), .20, bounce=True, repeat=False)
    show ctc
    pause
    hide ctc
    tn "Oh wow... those are... impressive."
    hide bfaq
    show bfaq bfaq00
    tn "I'd say they're about Korra's size."
    asa "I bet you haven't seen them this nice and young for a long time..."
    tn "Hey don't look down on me! I've seen Toph's tits!"
    asa "Toph? The police chief's mother?"
    asa "She's ancient!"
    tn "Uuhhh... I guess that's right."
    tn "Wait... Toph's still alive in this time! Katara probably, too!"
    asa "Yes, they're both still alive..."
    asa "Are you having an elderly moment?"
    tn "(ooooh fuuuckk... I didn't fully realize it earlier, but I'm posessing the body of Katara's son.)"
    tn "(Wait a minute... who was controlling Aang's body when Katara got pregnant??)"
    tn "(...this could get very complicated.)"
    tn "(...and who exactly is Lin's dad... ohhh shit...)"
    asa "You still with me? Do I need to call help?"
    tn "Oh, sorry."
    tn "I just got distracted by your chest."
    asa "Good. great."
    asa "now how about giving me that photograph?"
    asa "Before that kid comes back?"

    tn "I'm not sure about that yet."
    tn "Still feels like I'd be getting rid of important evidence."
    tn "Man, the temperature in here though..."
    asa "ugh..."

    show bfaq bfaq03:
        xpos 500
        linear 0.3 xpos 520
        linear 0.4 xpos 525

        linear 0.3 xpos 505
        linear 0.4 xpos 500

        repeat
    $ renpy.pause()

    tn "What are-"
    asa "Waving some cool fresh air towards you."

    asa "Is it refreshing?"
    asa "{size=-5}...you fucking pervert..."
    show ctc
    pause
    hide ctc
    hide bfaq
    show bfaq bfaq00

    tn "Yeah... but I'm still feeling hot."
    asa "*sigh...*"
    asa "i can't believe..."
    asa "......"
    show bfaq bfaq04
    show bfaq bfaq05:
        ypos 750
        linear 0.5 ypos 720
        linear 0.5 ypos 750
        repeat
    $ renpy.pause()
    tn "Oh wow, that's like really nice."
    tn "i can't believe you'd just offer to do this out of the blue."
    tn "But I can't give you the photograph."
    tn "If Amon is aided by someone like your father, the owner of future industries..."
    tn "Well... that kinda money and state-of-the-art tech could endanger everyone."
    tn "i mean, those lightning weapons are a pretty new thing..."
    tn "...and i'm willing to bet your father's done more than just provide amon with a blank check."
    tn "i can already tell he's going to be a pain in my ass."
    hide bfaq
    show bfaq bfaq04

    asa "well I need that photograph to confront my father and tell him to stop!"
    asa "come on!"
    asa "i'm already... this is... this is embarrassing!"
    asa "you're a politician!"
    asa "can't you just give me the photograph?!"
    tn "Mmhh..."
    tn "tell you what..."
    tn "I've seen enough of Korra's tits to not really be swayed by yours."
    tn "However, if I could get a taste of them...."
    asa "You... want to suck on my nipples?!"
    tn "Unless you'd rather slobber on my cock."
    tn "I'd be okay with that, too."
    tn "Or you could just leave again."
    tn "Without a photo."

    show bfaq bfaq08 with Dissolve(1.5)
    asa "......."
    asa "...................."
    asa "Just do it already."
    show ctc
    pause
    hide ctc

    show bfaq bfaq09a
    asa "ungh! ahh... ah!"
    show ctc
    pause
    hide ctc
    asa "I despise you..."
    tn "and yet here i am, sucking on your perky, perfect little nipple."
    asa "ugh... ah... shit..."

    show bfab bfab12 behind bfaq:
        xpos 500
        linear 0.5 xpos 0
    kn "AAhh!!" with hpunch
    kn "What's going on here?!"
    show ctc
    pause
    hide ctc
    show bfab bfab06
    kn "What are you two doing?!"
    tn "...."
    tn ".........."
    show bfaq bfaq08 with dissolve
    tn "uh..."
    asa "{size=-5}ohh... my breasts... thank goodness for korra..."
    kn "Meelo was stalking me again so I was going to hide from him here and..."
    kn "I see you two doing... this?!"
    tn "(is asami gonna rat me out?)"
    asa "Tenzin is helping me get rid of a ph.... stress."
    asa "Sure it's unconventional, but he can keep a secret."
    asa "and he's great at this particular technique."
    tn "yes... chakras... and stuff..."
    tn "(asami, you're a class act!)"
    asa "yes, that's it."
    tn "Want me to do yours too?"
    show bfab bfab24 with Dissolve(1.5)
    kn "I AM feeling stressed... but I'll skip."
    kn "Wait... that would mean you'd have to stop sucking Asami's... nipples."
    tn "Naturally."
    show bfab bfab26:
        xpos 150 ypos 50
    with Dissolve(1.5)
    kn "Okay, then."
    tn "...why do you care?"
    kn "just... because."
    "You can see Korra's nipples hardening as she tries to casually look at Asami's breasts."
    tn "(well, I'll be damned...)"
    hide bfab

    show bfaq bfaq10 with Dissolve(1.5)
    show bfad bfad01 behind bfaq
    tn "are you ready?"
    kn "i... i think so."
    tn "then i'm going to get started."
    kn "okay..."
    kn "sooo... Asami..."
    show bfaq bfaq11a
    kn "*ah!*"
    kn "You do this *ah!* often?"
    asa "Not that often."
    asa "Like I said, it can create misunderstandings."
    kn "Yeah... of course."

    show ctc
    pause
    hide ctc
    tn "Hmmmm... I can taste that you're filled with stress."



    show bfaq bfaq10 with dissolve
    kn "...I certainly feel stressed."


    $ temp_int = 0
    while temp_int != 1:
        menu:
            "asami again":
                scene
                if b4_daytime:
                    show expression "bk4/backgrounds/tower_day_1.jpg":
                        ypos 0
                else:
                    show expression "bk4/backgrounds/tower_night .jpg":
                        ypos 0
                show bfab bfab00 behind bfaq
                show bfaq bfaq09a
                show ctc
                pause
                hide ctc
            "korra again":

                scene
                if b4_daytime:
                    show expression "bk4/backgrounds/tower_day_1.jpg":
                        ypos 0
                else:
                    show expression "bk4/backgrounds/tower_night .jpg":
                        ypos 0
                show bfad bfad01 behind bfaq
                show bfaq bfaq11a
                show ctc
                pause
                hide ctc
            "done":

                $ temp_int = 1

    scene
    if b4_daytime:
        show expression "bk4/backgrounds/tower_day_1.jpg":
            ypos 0
    else:
        show expression "bk4/backgrounds/tower_night .jpg":
            ypos 0
    show bfaq bfaq20 with Dissolve(1.5)
    kn "umm... maybe you can teach me to do it too..."
    kn "to... to relieve stress in... in someone else?"
    tn "i think that's a great idea!"
    tn "you could start by practicing on Asami."
    "Asami throws you another ice cold stare."
    tn "uh... then again... maybe that's too big of a leap at once."
    tn "But you could start practicing by kissing."
    tn "I guarantee a photogr... ahum... I mean a {i}result{/i} if you do that."
    "you wiggle your eyebrows conspiratorally at asami."
    asa "*sigh*"
    asa "Have you ever kissed a girl, Korra?"
    show bfaq bfaq18 with Dissolve(1.5)
    kn "No..."
    kn "i've never... i've never kissed {i}anyone{/i}..."
    show ctc
    pause 
    hide ctc
    show bfaq bfaq17 with Dissolve(1.5)
    kn "*Mooaan*"
    tn "Oh, spirits!"
    show ctc
    pause
    hide ctc
    show bfaq bfaq19:
        xpos 500
        linear 2.0 xpos 510
        linear 2.0 xpos 500
        repeat

    show ctc
    pause
    hide ctc
    tn "Asami, I'm thoroughly convinced you should have that thing we talked about earlier."
    tn "You deserve it."
    "korra and asami moan into each other's mouths as they share an intense, wet, deep-tonguing kiss."
    hide bfaq
    show bfaq bfaq19
    tn "Damn, girl..."
    tn "You're a real go-getter."
    tn "(i won't tell her about the other copies just yet.)"

    show bfaq bfaq10
    show bfad bfad02
    with Dissolve(1.5)
    asa "Thanks, Tenzin."
    asa "I have another appointment now, but I'll retrieve it later."
    asa "Bye, Korra."
    kn "Cya!"

    hide bfad with dissolve
    tn "that was... interesting."
    tn "Especially the way you warmed up to the whole experience."
    tn "Did you have fun, Korra?"
    hide bfaq
    show bfaq bfaq10a
    with Dissolve(1.5)
    kn "um... no...?"
    tn "Wow."
    tn "That's positively the world's worst pokerface. ever."
    tn "The {i}Joker{/i} would have a better result surpressing his smile."
    kn "who?"
    tn "seriously? do you guys not have comics yet?"
    kn "what are comics?"
    tn "man, fuck time travel."
    kn "...what?"
    tn "nevermind..."
    kn "I... don't know what just happened, but I want it to happen more often."
    tn "Well, maybe I can help you out some more in the future with this particular interest of yours."
    kn "I think... i'd like that."
    tn "you and me both."
    play sound "audio/win2.mp3"
    $ korra_moral -=2
    $ korra_resist -=2
    "korra's {b}morality{/b} lowered!"
    "korra's {b}resistance{/b} lowered!"
    $ b4_daytime = False
    $ asami_tits = 2
    if b4_daytime:
        $ b4_daytime = False
        jump b4_airtemple_map1
    else:
        jump bk4_next

label asami_tits2:
    hide screen bk4_money_date
    b4_tp "Hey Asami, this is Tenzin."
    if asami_bj:
        asa "...i'll be right over."
    else:
        tp "Can I get you to come over?"
        asa "What? Tenzin? Why?"
        b4_tp "I found another photograph of your father."
        asa "Did... didn't we already have this conversation?"
        b4_tp "do you really want to discuss it over the phone?"
        asa "...okay."
        asa "Same place?"
        b4_tp "Yep!"
    hide black
    show black with dissolve
    "after waiting for half an hour Asami arrives."
    show bfad bfad01
    hide black
    with dissolve
    if not asami_bj:
        tn "Did you already talk to your dad about this photo thing?"
        asa "...Not yet."
        tn "Does the photo still exist?"
        asa "I had an accident and it got burned..."
        tn "oh, no. well, i came across another..."
        asa "and you'd like to-"
        tn "See you shake your tits in exchange for the photo."
    else:
        asa "what do you want?"
        tn "i want you to shake your tits for me."

    if not asami_bj:
        show bfad bfad02 with dissolve
        asa "...okay."
        show bfae jinora01:
            xpos 300
            linear 1.0 xpos 0
        jino "Hey Asami!"
        jino "I didn't know you were here!"
        asa "Oh, uh... hi."
        jino "Are you looking for Korra?"
        asa "uh... yeah... that's it."
        jino "I'll go get her for you!"
        asa "Thanks but that's really not necessary."

        jino "Don't worry it's no trouble at all!"
        show bfae jinora01:
            xpos 0
            linear 1.0 xpos 300

        asa "So I guess we should do this sometime later?"
        tn "No need, we have enough time before Jinora gets down, finds korra and Korra gets up here."

        tn "Show them titties!"
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfad
    show bfaq bfaq07 with Dissolve(1.5)
    asa "at least you're direct in what you want this time."
    $ renpy.pause(1.0)
    show bfaq bfaq06 at Move((0, 0), (0, -15), .20, bounce=True, repeat=False)
    tn "Oh yeah, still looking nice."
    hide bfaq
    show bfaq bfaq00
    tn "Korra would love this."
    asa "I kinda got that the last time."
    asa "She was pushing that tongue of hers in my mouth with enough force to scare me."
    tn "Yeah, she's really not clued in on the whole gentle-touch business."
    tn "Well, just be certain you don't start any funny business when I'm not there to supervise you two."
    asa "Oh? You get hard from sort of stuff?"
    tn "That and some other reasons."
    tn "Come on, move them around."


    show bfaq bfaq03:
        xpos 500
        linear 0.3 xpos 520
        linear 0.4 xpos 525

        linear 0.3 xpos 505
        linear 0.4 xpos 500

        repeat
    show ctc
    pause
    hide ctc

    tn "Yeah..."
    tn "Now make 'em jump go up and down."
    show bfaq bfaq04
    show bfaq bfaq05:
        ypos 750
        linear 0.5 ypos 720
        linear 0.5 ypos 750
        repeat
    show ctc
    pause
    hide ctc
    tn "Oh wow, that's like really nice."

    hide bfaq
    show bfaq bfaq04


    menu:
        "Suck tits":
            tn "Sucking time!"
            show bfaq bfaq08 with Dissolve(1.5)
            $ renpy.pause(1.0)
            show bfaq bfaq09a
            show ctc
            pause
            hide ctc
            asa "Hey! Don't bite on it!"
        "Keep jumping":
            show bfaq bfaq05:
                ypos 750
                linear 0.5 ypos 720
                linear 0.5 ypos 750
                repeat

            show ctc
            pause
            hide ctc


    show bfab bfab12 behind bfaq:
        xpos 500
        linear 0.5 xpos 0

    kn "AAhh!!" with hpunch
    kn "Asami!"

    hide bfaq
    show bfaq bfaq08
    tn "Wow, Jinora works fast."

    kn "Are you guys doing that stress relief thing again?"
    tn "Yeah, and you're just in time."

    show bfab bfab24 with Dissolve(1.5)
    kn "Awesome!"
    kn "Ahem, I mean, great... good... nice..."
    tn "First whip out those tits."
    hide bfab
    show bfaq bfaq12
    with Dissolve(1.5)
    tn "Today's warmup consists of some light kissing."

    show bfaq bfaq18 with Dissolve(1.5)
    show bfaq bfaq17 with Dissolve(1.5)
    show bfaq bfaq19 with Dissolve(1.5)
    show ctc
    pause
    hide ctc

    tn "Okay, I want to try something different now."
    show bfaq bfaq18 with Dissolve(1.5)

    tn "Push your nipples against each other repeatedly."
    kn "really?"
    asa "yeah... really?"
    tn "yes."
    asa "well... let's do this, then."
    asa "come on, korra."
    kn "o-okay..."
    show bfaq bfaq16
    show ctc
    pause
    hide ctc
    kn "Are we doing it right?"

    tn "Absolutely."
    show ctc
    pause
    hide ctc
    tn "...but that's enough for today."

    show bfaq bfaq10
    show bfad bfad02
    with Dissolve(1.5)
    asa "Thanks Tenzin."
    asa "I have another appointment, now."
    asa "Bye, Korra."
    hide bfad with Dissolve(1.5)
    kn "Cya!"
    tn "Say, I haven't sucked your tits today have I?"
    kn "That's okay... really."
    menu:
        "I insist":
            tn "If not, I don't think I'll be able to help you train with Asami."
            kn "then... then please suck on my tits."
            show bfaq bfaq11a
            show ctc
            pause
            hide ctc
            tn "Mmmhhhh...."
            show bfaq bfaq10 with Dissolve(1.5)
        "Meh, I don't feel like doing it anyway.":
            pass
    tn "Okay, we're done here."
    $ asami_tits = 3
    if korra_moral >=80:
        play sound "audio/win2.mp3"
        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    else:
        pass


    if b4_daytime:
        $ b4_daytime = False
        jump b4_airtemple_map1
    else:
        jump bk4_next

label pema_blowjob1:
    pn "sit down."
    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    scene
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos 0
    show bfac bfac01:
        xpos -400 ypos -50
    with fade
    pn "comfortable?"
    tn "very."
    show bfac bfac02:
        xzoom -1.0 xpos 500
    with dissolve
    pn "so..."
    pn "How about a nice relaxing blowjob from your pretty wife?"
    "You quickly strip."
    b4_tx "Let's do this thing!!"
    show bfac bfac07 with Dissolve(1.5)
    pn "Ooooh, you really are looking forward to one, aren't you?"

    b4_tx "SUUUUUCKKKK!!!"
    tn "I mean... yes, please suck my dick."
    pn "Patience, dear."
    pn "I can't move that fast anymore with this belly."
    show ctc
    pause
    hide ctc
    hide bfac
    show bfas bfas00 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)

    pn "Now push that big meaty rod of yours in my face!!"
    show ctc
    pause
    hide ctc

    show bfas bfas01 with Dissolve(1.5)
    tn "Ready and willing!"
    show ctc
    pause
    hide ctc
    show bfas bfas02
    pn "Mmmmm... willing indeed."
    show ctc
    pause
    hide ctc
    pn "You have surprisingly little trouble getting it up lately."
    pn "and i've been dying to suck you off."
    pn "There was been a time when it took some work to get you into action mode."
    pn "I shouldn't be worried about Korra being the cause of this, should I?"

    hide bfas
    show bfas bfas03:
        xpos 30
        easein 1.0 xpos 40
        easeout 0.6 xpos 30
        repeat
    show text "{color=#ffc0cb}suck":
        rotate -25
        xalign 0.8 yalign 0.3
        linear 1.5 yalign -0.3
    $ renpy.pause(2)
    hide text
    show text "{color=#ffc0cb}slurp":
        rotate -25
        xalign 0.8 yalign 0.3
        linear 1.5 yalign -0.3
    $ renpy.pause(2)
    hide text
    b4_tx "Hnnngh...."
    show text "{color=#ffc0cb}gulp":
        rotate -25
        xalign 0.8 yalign 0.3
        linear 1.5 yalign -0.3
    "Pema slides her lips over your pulsating cock, moistening the shaft with her saliva."
    "She only pulls her head back enough to give her enough space to lick the tip within her mouth."
    hide text
    show text "{color=#ffc0cb}shluup":
        rotate -25
        xalign 0.8 yalign 0.3
        linear 1.5 yalign -0.3
    "She clearly knows your current dick better than you yourself and uses that knowledge with great effect."
    hide text
    show text "{color=#ffc0cb}suck":
        rotate -25
        xalign 0.8 yalign 0.3
        linear 1.5 yalign -0.3
    b4_ts "Korra shmorrah... your lovely lips are the magic touch."
    hide text
    show text "{color=#ffc0cb}slurp":
        rotate -25
        xalign 0.8 yalign 0.3
        linear 1.5 yalign -0.3
    show ctc
    pause
    hide ctc

    hide bfas
    show bfas bfas02
    with Dissolve(1.5)
    pn "Well, I don't care what you do to her as long as you make sure she hates it and I'll get to enjoy some of it too eventually."
    tn "Sounds like a win-win situation to me."
    if jinora_interest:
        show expression "bk4/pema/blowjob/jinora_shadow.png":
            xpos 0 ypos 120
        with Dissolve(1.5)

    hide bfas
    show bfas bfas04:
        xpos 0
        linear 0.3 xpos 0
        linear 0.3 xpos 30
        linear 0.6 xpos 0
        repeat
    show ctc
    pause
    hide ctc

    b4_tx "Hnnggh!"
    b4_tx "Gonna cum!"
    tx "Want it all over your face or down your throat?"
    "*Muble* *mumble*"


    menu:
        "Have her swallow it":
            $ temp_boolean = True
            hide bfas
            show bfas bfas06
            with Dissolve(1.5)
            play sound "audio/splurt2.ogg"
            show bfas bfas06 with vpunch
            pn "*gurgle*"
            play sound "audio/splurt3.ogg"
            show bfas bfas06 with vpunch
            pn "*gurgle*"
            play sound "audio/splurt1.ogg"
            show bfas bfas06b with Dissolve(1.5)
            pn "*coffcoff*"
            pn "That was quite the load, even for you!"
            show ctc
            pause
            hide ctc

            show bfas bfas01
            show expression "bk4/pema/blowjob/sperminside.png"
            with Dissolve(1.5)
        "Unload on her face":



            $ temp_boolean = False
            hide bfas
            show bfas bfas05
            play sound "audio/splurt2.ogg"
            show expression "bk4/pema/blowjob/spermout_1.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk4/pema/blowjob/spermout_2.png" with hpunch
            tn "Replenishable facial moisterizer!"
            pn "Normally it isn't applied by the gallon though."
            show ctc
            pause
            hide ctc

    show bfas bfas01
    tn "Just givin' it my best."
    show ctc
    pause
    hide ctc
    scene



    if temp_boolean == False:
        show expression "bk4/backgrounds/bed_tenzin_1.jpg":
            ypos -80
        show bfas bfas07
        show expression "bk4/pema/blowjob/spermonface.png"
        with Dissolve(1.5)
        $ renpy.pause(1.0)
        pn "Since the sheets are already ruined..."
        pn "I might as well use them to clean myself up and go get some fresh ones."
    else:
        show expression "bk4/backgrounds/bed_tenzin_1.jpg":
            ypos -80
        show bfas bfas07
        show expression "bk4/pema/blowjob/spermontits.png"
        with Dissolve(1.5)
        $ renpy.pause(1.0)
        pn "It leaked all over my tits and on the sheets..."
        pn "...so I might as well use them to clean myself up and go get some fresh ones."


    show ctc
    pause
    hide ctc

    if jinora_interest and pema_bj ==4:
        hide bfas
        scene
        show expression "bk4/backgrounds/tenzin_room_day.jpg":
            ypos 0
        show bfaj bfaj19

        tn "Cool, I'll-"
        show bfae jinora02:
            xpos 500
            linear 0.5 xpos 0

        jino "Mom! Dad! Can I...."
        show bfae jinora03
        jino "What..."
        show bfae jinora04 at Move((10, 10), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
        jino "AAhhh!! Gross!!! Eeeewh!! EEEEwh!!!"
        show bfae jinora04:
            linear 0.5 xpos 500
        jino "{size=+15}EEEEwwwwh!!{/size}"
        tn "Should-"
        show bfae jinora04:
            linear 0.5 xpos -150
            linear 1.0 xpos -150
            linear 0.5 xpos 500
        jino "{size=+30}EEEEwwwwh!!{/size}"

        tn "..."
        tn "Should we-"

        show bfae jinora04:
            linear 0.5 xpos -150
            linear 1.0 xpos -150
            linear 0.5 xpos 500
        jino "{size=+30}EEEEwwwwh!! Put some clothes on!{/size}"

        tn "For someone who's disgusted you come back awfully often!!"
        tn "And knock before you enter a room!!"
        pn "I think she's really gone this time."
        tn "Should we go after her or something?"
        pn "Nah she'll be fine."
        pn "besides..."
        pn "You still have your dick out."
        pn "Don't worry, I already told her about the birds and the bees."
        pn "Aside from some light mental scarring she'll be fine."
    else:

        pass

    scene black with dissolve
    "you lay back down and fall asleep immediately."
    $ pema_bj = 5
    jump bk4_next

label korra_boobjob0:
    kn "you... really didn't like it?"
    asa "i didn't hate it, but..."
    asa "he was... an animal."
    asa "my nipples are still a bit sore."
    asa "what about you?"
    kn "I just... i'm just trying to become an airbender."
    kn "and... i wanted to... be with you... in that moment."
    asa "oh?"
    kn "you know... just... like... hanging out together."
    asa "...of course."
    asa "well, i have to go."
    asa "see you around, korra."
    kn "see ya!"
    "you stay hidden as asami leaves."
    "you wait a moment..."
    "...and enter korra's room."
    hide screen bk4_money_date
    hide black
    show bfab bfab24
    with Dissolve(1)
    kn "tenzin?"
    kn "what are you doing here?"
    tn "i just thought i'd pop in."
    tn "work on your chakras some more."
    kn "oh... i think... they're good..."
    tn "that's too bad you think so."
    tn "because that's just part of your training, remember?"
    kn "what?"
    "without hesitation, you drop your pants."
    show bfab bfab12 with hpunch
    kn "what?!" with hpunch
    kn "wh-what are you doing, tenzin?"
    tn "it seems like you've forgotten that a crucial part of airbending training is in being free with your body."
    kn "i... it's... but..."
    tn "and it is vital to my own personal ability."
    tn "if I don't do this, i will be unable to continue to train you."
    kn "what... but... what..."
    tn "so... for both your sake, and mine... i'm going to fuck your tits."
    kn "what?!" with hpunch
    kn "but... no... that's... you..."
    kn "you can't be... serious?"
    tn "i am."
    tn "it's part of standard crash course airbending training."
    tn "i'd have thought with all the meditation you've been doing, this wouldn't be such a shock."
    tn "or are you too weak to take the \"hard and fast\" airbending course?"
    show bfab bfab05 with dissolve
    kn "No, i... i can handle any... anything you dish out..."
    tn "you sure?"
    show bfab bfab06 with dissolve
    kn "y-yeah, i'm sure!"
    tn "good, then take your shirt off."
    show bfab bfab24 with dissolve
    kn "um..."
    kn "but... what about pema?"
    tn "with pema pregnant, she can't give me boobjobs."
    jump korra_boobjob1

label korra_boobjob1:

    tn "Belly is in the way."
    kn "But... i don't know..."
    tn "Well, Asami has already shown some interest in me and Pema said she'd allow it."
    show bfab bfab12 at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
    kn "She did!?!?"
    tn "She might seem like a wallflower to some, but she's pulling quite a few of the strings, Korra."
    tn "Don't underestimate her or you'll end up eating out her pussy!"
    ta "Is that what you want Korra?!"
    ta "to eat out my wife's pussy?!"
    kn "nn... no!!"
    show bfab bfab24 with Dissolve(1.5)
    tn "Anyway, it's either going to be Asami or... if you're willing to continue your training... you."
    tn "Honestly, I think her boobsucking stress relief sessions with me are just an excuse to hang around me..."
    tn "And you're the avatar, you like helping people, don't you?"
    tn "Just imagine Asami with my dick between her boobs..."
    tn "cumming all over her..."
    tn "With her face covered in my cum..."
    tn "Her lower lip slightly quivering with ecstasy... is that what you want?!"
    kn "....no."
    tn "Then do us both a favor."
    tn "Just think of it as slightly more intense training session. "
    tn "which is what it is."
    tn "I've already seen and touched your tits plenty of times as it is... it's really no big deal."
    kn "Yeah, but... you didn't touch them with... with your penis."
    tn "because you weren't ready."
    tn "but... believe it or not... i think you're ready now."

    show bfab bfab26 with Dissolve(1.5)
    kn "*sigh*"
    kn "So if I do this, you won't ask Asami for boobjobs?"
    kn "and... it really will help you?"
    kn "and make me a better airbender?"
    tn "three for three."
    kn "Okay..."
    kn "...."
    kn "okay, let's make this quick."
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfab with Dissolve(1)
    show bfau bfau01
    with Dissolve(1.5)

    kn "...now what?"
    show ctc
    pause
    hide ctc
    tn "Now I push my dick between your comfy chocolate funbags."

    show bfau bfau02 at Move((10, 0), (0, 0), .10, bounce=False, repeat=True, delay=.275)
    kn "umph..."
    show ctc
    pause
    hide ctc
    tn "like this."
    kn "just... as long as you don't make asami do this."
    tn "i'll consider it."
    tn "And to prevent any burnmarks..."
    play sound "audio/spit.mp3"
    show expression "bk4/korra/boobjob/spit.png":
        alpha 1.0
        linear 3.0 alpha 0.0
    pause(3.0)
    hide expression "bk4/korra/boobjob/spit.png"
    tn "...here's some spit to help things slide nice and smoothly."
    kn "ugh... gross..."
    tn "Just keep pressing those soft, giving tits of yours together as I move up and down."

    hide bfau
    show bfau bfau03:
        linear 0.8 xpos 5
        linear 0.4 xpos 0
        repeat
    tn "Oh, yeaahhh... fuck you and your big fucking tits, korra!"
    show ctc
    pause
    hide ctc
    tn "How do you like my erect dick being wedged in between your boobs?"
    kn "This is... okay."
    tn "Well, let me make it a little be more interesting."
    tn "Hold on tight."
    kn "To what..."

    show bfau bfau04
    kn "AH!"
    show ctc
    pause
    hide ctc
    kn "Be more... *Ah!*... careful!... *Ah!*"
    show ctc
    pause
    hide ctc
    tn "Here... it... comes!"
    kn "here comes... what?"
    tn "just some sperm... no big deal..."
    tx "just... stay... still!"
    hide bfau
    show bfau bfau02
    play sound "audio/splurt2.ogg"
    show bfau_spermshot with vpunch
    show expression "bk4/korra/boobjob/spermout_1.png"
    kn "oh!"
    play sound "audio/splurt3.ogg"
    show bfau_spermshot with vpunch
    show expression "bk4/korra/boobjob/spermout_2.png"
    kn "unnh..."
    show ctc
    pause
    hide ctc
    kn "....."

    scene
    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0
    show bfau bfau01
    show expression "bk4/korra/boobjob/spermout_4.png"
    with Dissolve(1.5)

    kn "Yuck..."
    kn "I'm all covered with this stuff."
    show ctc
    pause
    hide ctc
    show expression "bk4/korra/boobjob/spermout_4.png":
        linear 11.0 alpha 0.0
    tn "It looks great on you."
    tn "Ready for round two?"
    kn "Shouldn't this be over when you cum?"
    tn "Usually, but i haven't gotten to fuck a big beautiful pair of tits in a while."
    tn "I think there's some more left where that came from."
    kn "That's... I don't think it works like that."
    tn "Lie down and I'll prove you wrong."

    scene
    show expression "bk4/backgrounds/korra_room_bed.jpg"

    show bfau bfau05 with Dissolve(1.5)
    kn "I don't think we should be doing this here now..."
    kn "Anyone could walk in..."
    show ctc
    pause
    hide ctc

    show bfau bfau06 with Dissolve(1.5)
    tn "Don't worry this won't take long."
    tn "And this way I can massage your boobs too."
    kn "....."
    show ctc
    pause
    hide ctc

    hide bfau
    show bfau bfau07:
        xpos 0
        easein 0.8 xpos -10
        easeout 0.4 xpos 0
        repeat

    show ctc
    pause
    hide ctc
    kn "Hmmmmpfff...."
    kn "....."
    "You keep sliding up and down in a steady rhythm while intensifying the kneeding of Korra's boobs."
    show ctc
    pause
    hide ctc
    show bfau bfau08:
        xpos 0
        easein 0.8 xpos -10
        easeout 0.4 xpos 0
        repeat
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc

    kn "...."
    tn "Are you starting to enjoy this, you slut??"
    kn "......"

    b4_tx "Hnnnng... getting there...."
    b4_tx "Time to prove to you my seed is both potent and plentiful!"

    hide bfau
    show bfau bfau10:
        xpos 20
        linear 0.2 xpos -10
        linear 0.6 xpos 20
        repeat

    show ctc
    pause
    hide ctc

    hide bfau
    show bfau bfau09

    play sound "audio/splurt2.ogg"
    show bfau_z_spermshot with hpunch
    show expression "bk4/korra/boobjob/z_spermout_1.png"
    b4_tx "Hnng!"

    play sound "audio/splurt3.ogg"
    show bfau_z_spermshot with hpunch
    show expression "bk4/korra/boobjob/z_spermout_2.png"
    b4_tx "Hnnnng!"
    b4_tx "LAST STOP!!!!"

    play sound "audio/splurt1.ogg"
    show bfau_z_spermshot with hpunch
    show expression "bk4/korra/boobjob/z_spermout_3.png"

    show ctc
    pause
    hide ctc
    tn "Damn! I love how my spunk contrasts with your skin!"
    show bfau bfau11 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    kn "you... tenzin... why..."
    tn "it was good for you."
    tn "...and me."
    tn "See you later Korra."
    tn "Don't forget to wash you face."
    kn "...."
    $ korra_boobjob = 3
    show ctc
    pause
    hide ctc
    jump bk4_next

label korra_boobjob2:
    tn "i'm going to fuck your tits again."
    show bfab bfab24 with dissolve
    kn "oh, do you... i mean... do you need to?"
    tn "yes."
    tn "and you need it too."
    tn "it's important for your chakras and development."
    tn "and... if you want me to not fuck asami's poor, sore tits."

    show bfab bfab26 with Dissolve(1.5)
    kn "*sigh*"
    kn "...."
    kn "okay, let's make this quick."
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfab with Dissolve(1)
    show bfau bfau01
    with Dissolve(1.5)

    kn "...there."
    kn "now what?"
    show ctc
    pause
    hide ctc
    tn "Now I push my dick between your comfy chocolate funbags."

    show bfau bfau02 at Move((10, 0), (0, 0), .10, bounce=False, repeat=True, delay=.275)
    kn "umph..."
    show ctc
    pause
    hide ctc
    tn "like this."
    kn "just... just do what you need to."
    tn "let's lube these fuckers up."
    play sound "audio/spit.mp3"
    show expression "bk4/korra/boobjob/spit.png":
        alpha 1.0
        linear 3.0 alpha 0.0
    pause(3.0)
    hide expression "bk4/korra/boobjob/spit.png"
    kn "ugh... whatever..."
    tn "Just keep pressing those soft, giving tits of yours together as I move up and down."

    hide bfau
    show bfau bfau03:
        linear 0.8 xpos 5
        linear 0.4 xpos 0
        repeat
    tn "Oh, yeaahhh... fuck you and your big fucking tits, korra!"
    show ctc
    pause
    hide ctc
    tn "How do you like my erect dick being wedged in between your boobs?"
    kn "This is... okay."
    tn "Well, let me make it a little be more interesting."
    tn "Hold on tight."
    kn "To what..."

    show bfau bfau04
    kn "AH!"
    show ctc
    pause
    hide ctc
    kn "Be more... *Ah!*... careful!... *Ah!*"
    show ctc
    pause
    hide ctc
    tn "Here... it... comes!"
    kn "here comes... what?"
    tn "just some sperm... no big deal..."
    tx "just... stay... still!"
    hide bfau
    show bfau bfau02
    play sound "audio/splurt2.ogg"
    show bfau_spermshot with vpunch
    show expression "bk4/korra/boobjob/spermout_1.png"
    kn "oh!"
    play sound "audio/splurt3.ogg"
    show bfau_spermshot with vpunch
    show expression "bk4/korra/boobjob/spermout_2.png"
    kn "unnh..."
    show ctc
    pause
    hide ctc
    kn "....."

    scene
    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0
    show bfau bfau01
    show expression "bk4/korra/boobjob/spermout_4.png"
    with Dissolve(1.5)

    kn "Yuck..."
    kn "I'm all covered with this stuff."
    show ctc
    pause
    hide ctc
    show expression "bk4/korra/boobjob/spermout_4.png":
        linear 11.0 alpha 0.0
    tn "It looks great on you."
    tn "Ready for round two?"
    kn "are... are you sure?"
    kn "you aren't done?"
    tn "Lie down and I'll prove it."
    kn "......"

    scene
    show expression "bk4/backgrounds/korra_room_bed.jpg"

    show bfau bfau05 with Dissolve(1.5)
    kn "I don't think we should be doing this here now..."
    kn "Anyone could walk in..."
    show ctc
    pause
    hide ctc

    show bfau bfau06 with Dissolve(1.5)
    tn "Don't worry this won't take long."
    tn "And this way I can massage your boobs too."
    kn "....."
    show ctc
    pause
    hide ctc

    hide bfau
    show bfau bfau07:
        xpos 0
        easein 0.8 xpos -10
        easeout 0.4 xpos 0
        repeat

    show ctc
    pause
    hide ctc
    kn "Hmmmmpfff...."
    kn "....."
    "You keep sliding up and down in a steady rhythm while intensifying the kneeding of Korra's boobs."
    show ctc
    pause
    hide ctc
    show bfau bfau08:
        xpos 0
        easein 0.8 xpos -10
        easeout 0.4 xpos 0
        repeat
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc

    kn "unnh... ahh... ten... ah... tenzin..."
    tn "Are you starting to enjoy this, you slut??"
    kn "just... just finish..."

    b4_tx "Hnnnng... getting there...."
    b4_tx "Time to prove to you my seed is both potent and plentiful!"

    hide bfau
    show bfau bfau10:
        xpos 20
        linear 0.2 xpos -10
        linear 0.6 xpos 20
        repeat

    show ctc
    pause
    hide ctc

    hide bfau
    show bfau bfau09

    play sound "audio/splurt2.ogg"
    show bfau_z_spermshot with hpunch
    show expression "bk4/korra/boobjob/z_spermout_1.png"
    kn "oh..."

    play sound "audio/splurt3.ogg"
    show bfau_z_spermshot with hpunch
    show expression "bk4/korra/boobjob/z_spermout_2.png"
    kn "it's... hot... and..."
    b4_tx "LAST STOP!!!!"

    play sound "audio/splurt1.ogg"
    show bfau_z_spermshot with hpunch
    show expression "bk4/korra/boobjob/z_spermout_3.png"

    show ctc
    pause
    hide ctc
    tn "Damn! I love how my spunk contrasts with your skin!"
    show bfau bfau11 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    kn "i'm... i'm disgusting..."
    tn "and it was good for you."
    tn "See you later Korra."
    tn "Don't forget to wash you face."
    kn "...."
    show ctc
    pause
    hide ctc
    jump bk4_next


label pema_vag2:
    show expression "bk4/backgrounds/park_day_2.jpg":
        ypos 0
    hide bfac
    hide screen bk4_money_date
    show bfac bfac04
    hide black
    with fade
    pn "well..."
    pn "this seems like a good spot."
    pn "how do you feel?"
    pn "ready to fuck in this public park?"
    tn "yes, shut up, give me your cunt."
    pn "spirits i love your energy lately..."

    pn "so what do yo think? Topless or not?"

    menu:
        "Let's keep it on":
            $ bfax_top = True
            tn "top on."
        "Take it off baby!":
            $ bfax_top = False
            tn "top off."

    hide bfac
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    show bfax bfax07 with Dissolve(1.5)

    show ctc
    pause
    hide ctc
    if bfax_top == False:
        pn "That's a great idea."
        pn "And since I'm already halfway naked..."
    else:


        pn "That's not really adventurous of you."
        pn "But... I have a solution for that!"
        pn "If you don't want me to go topless, I'll go..."





    show bfax bfax08 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    b4_tn "This seems... risky."
    pn "Oh?"
    pn "Because we're in a public park or because the kids are up ahead?"
    b4_tn "Both."
    pn "I'm certain a couple of nice long thrusts..."
    pn "...will convince me to put some clothes back on."


    show bfax bfax01
    show ctc
    pause
    hide ctc
    pn "Mmmm? Well?"
    pn "what are you waiting for?"
    pn "A permit?"
    show ctc
    pause
    hide ctc
    show bfax bfax02 with dissolve

    b4_tn "Just for the record..."
    tn "you're the hottest pregnant wife and mother of three I've ever had the honor of fucking."
    pn "that's a very limited category..."
    pn "i hope."
    pn "not a very impressive first prize."
    b4_tn "uh... you're the ideal wife?"
    pn "Better!"
    pn "Now treat me like a cheap whore!"
    b4_tn "don't flatter yourself..."
    tn "you {i}are{/i} a cheap whore."
    pn "More!"

    hide bfax
    show bfax bfax03:
        linear 1.0 xpos 0
        linear 0.6 xpos 10
        repeat
    pn "ahhhnn... yes, baby..."
    show ctc
    pause
    hide ctc
    pn "Ohhhh... fuck..."
    pn "that's just what I need!"
    pn "it's been so... fucking... long..."
    pn "Beat my pussy!"
    pn "fuck it into submission!"
    pn "with your stiff fucking cock!"

    show bfax bfax05:
        linear 1.0 xpos 10
        linear 0.0 xpos 0
        repeat
    with dissolve
    pn "yes... yes... baby...!!!"
    show ctc
    pause
    hide ctc
    pn "what's... ahh... ah... what's gotten into you?!"
    pn "you're really... ah... really giving it to me!"
    pn "do i turn you on that much?"
    tn "you haven't seen anything yet, you filthy fuck cow."
    pn "Ohh!" with hpunch
    pn "fuck... yes!!!"
    pn "More! more!"
    b4_tn "I'm surprised your swollen tits aren't leaking yet..."
    tn "because you're fucking gushing on this end!"
    pn "yes! yes!"
    show ctc
    pause
    hide ctc
    hide bfax
    show bfax bfax09:
        linear 0.45 xpos 10
        linear 0.0 xpos 0
        repeat
    pn "oh! fuck! fuck! yes!"
    pn "b-baby?!!"
    pn "ungh... ungh.... fuck!!!"
    show ctc
    pause
    hide ctc
    b4_tn "You want it?!"
    tn "You want my dick in that whore cunt of yours?"
    pn "yes! yes! i'm your whore!"
    pn "fuck my whore cunt!"
    pn "fuck it!"
    pn "I'm your slut! i'm yours!"
    pn "wife! mother! slave! whore! whatever you need!"
    pn "just fuck me! fuck me!!!"


    hide bfax
    show bfax bfax06:
        linear 0.8 xpos 40
        linear 0.2 xpos 0
        linear 0.8 xpos 10
        repeat
    pn "Yees!!"
    show ctc
    pause
    hide ctc

    pn "you're... ah... you're so swollen!!!"
    pn "give... give it all to me!"
    pn "blow your fat fucking load on my insides!"
    pn "drench me!!!"
    pn "drench your fuck puppy!!!" with hpunch



    menu:
        "cum inside":
            hide bfax
            play sound "audio/splurt2.ogg"
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt3.ogg"
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt1.ogg"
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            show bfax bfax10 with Dissolve(1.5)
            pn "Sooo... good."
            show ctc
            pause
            hide ctc
            pn "I can feel it flowing out of my pussy."

            menu:
                "Tell her to piss":
                    b4_tn "If you have to take a leak, go right ahead."
                    pn "I wasn't going to... but now that you mention it I do feel like I could go."
                    show bfax_piss with dissolve
                    pn "Aaaaah... that feels great."
                    $ renpy.pause()
                    show bfax_piss:
                        xpos 500
                        linear 2.0 xzoom 0.0 xpos 420
                    pn "Aaand... done."
                    hide bfax_piss
                "DON'T":
                    pass
        "cum outside":

            b4_tn "on your back, spermslut!"

            show bfax bfax11:
                xpos 0 ypos 0
            with Dissolve(1.5)
            pn "paint me, love!"
            pn "paint your whore!"
            pn "I want it all over me!"
            pn "shower me! let me taste-"
            play sound "audio/splurt2.ogg"
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_1.png"
            with hpunch
            pn "yes!!"
            $ renpy.pause(0.5)
            play sound "audio/splurt3.ogg"
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_2.png"
            with hpunch
            pn "i love it!!"
            $ renpy.pause(0.5)
            play sound "audio/splurt1.ogg"
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_3.png"
            with hpunch
            $ renpy.pause(0.5)
            pn "Aaaaah...!"
            pn "So much..."


    scene

    show expression "bk4/backgrounds/park_day_2.jpg":
        ypos 0
    show bfaa bfaa04:
        xpos 300
        linear 0.5 xpos -300
    lin "What the fuck are you doing!?!" with hpunch
    lin "This is a {size=+10}public park!!{/size}"
    show expression "bk4/misc/black.png" with dissolve
    show text "{color=#fff}taking her time, pema casually cleans herself up with the towel and puts her clothes back on {/color}"
    $ renpy.pause()
    hide text
    hide expression "bk4/misc/black.png" with Dissolve(1.5)

    show bfac bfac04 with dissolve
    pn "Hi, Lin."
    pn "It's very simple, really."
    pn "My husband has taken me to the park with the kids for a relaxing afternoon."
    show bfaa bfaa04:
        linear 0.5 xpos 0 xzoom -1.0
    lin "That was more than just relaxing!"

    pn "Really?"
    pn "Because I feel veeery relaxed right now."
    lin "You can't just... do it... in a public park!!"
    lin "The only reason I'm not arresting the both of you is because of your kids."
    pn "Thank you."
    pn "How lucky for us the captain of the police is patrolling the park!"
    pn "Is that something you do often? As a captain?"
    lin "......"
    lin "This is your one and only warning!"
    lin "Go and do your nasty stuff on that island of yours."
    show bfaa bfaa04:
        linear 0.5 xpos -400
    pn "Wow, that woman is thirstier than a sponge in a desert."
    if not jinora_interest:
        pass
    else:

        pn "Well, that's one down."
        pn "Now for the other."
        b4_tn "What other?"
        pn "Jinora! Come out where we can see you."
        hide bfaa
        b4_tn "uh, she isn't here."
        tn "She's with the others up ahead."
        show bfac bfac05 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
        pn "{size=+10}JINORA!"
        pn "Get your ass out here!"
        show bfac bfac04:
            xzoom -1.0
        show bfae jinora05
        with Dissolve(1.5)
        "Jinora steps forward from behind a bush not too far off."
        jino "...Yes?"
        jino "I was just passing by."
        jino "Just now. By coincidence. "
        pn "I told you to make sure to watch over your brother and sister... didn't I?"
        jino "...yes..."
        pn "You can't do that while spying on me and your father, can you?"
        show bfae jinora06
        jino "I didn't spy!"
        pn "We'll talk about this later, young lady."
        pn "Now go and get the others."
        pn "We're leaving."
        jino "...okay."
        jino "{size=-6}(I didn't spy... I was just looking longer than strictly necessary...){/size}"
        hide bfae
        hide bfac
        show bfac bfac04
        with Dissolve(1.5)
        pn "How long do you think Lin was watching us?"
        b4_tn "I'm more worried about how long Jinora has been watching!"
        pn "Ah she's just young and curious. Don't worry about it."
        pn "But that doesn't mean she can just shirk her responsibilities."
        pn "I'll have to have a serious talk with her later today."
        pn "I hope you had fu-"


    show bfae group05:
        xpos -900
        linear 2.0 xpos -200
    jino "We're ready!"
    pn "perfect timing."
    pn "let's go home."
    pn "i'm going to sleep like a baby tonight."
    scene black with dissolve
    scene expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    if not b4_daytime:
        show expression "bk4_xtra/remove/blackveil.png"
    show bfac bfac02
    with dissolve
    pn "so that {i}definitely{/i} deserves a reward."

    tn "oh, right."
    tn "what is it?"
    show bfac bfac02 with dissolve
    pn "come with me..."
    tn "wait... is it sex again?"
    tn "because i'm down but i might need a few minutes."
    pn "just come on, you stallion."
    show expression "bk4/backgrounds/study0.jpg":
        ypos 0
    hide bfac
    with fade
    tn "...where am i?"
    show bfac bfac02 with dissolve
    pn "your new study room!"
    tn "my what?"
    pn "i've been having this room worked on for the last few weeks for you."
    show bfac bfac06 with dissolve
    pn "i thought giving you a place to work would entice you into having sex with me..."
    tn "girl, you never need to worry about that again."
    tn "but you can still keep the presents coming."
    show bfac bfac02 with dissolve
    pn "spirits, you're amazing..."
    pn "what happened?!"
    tn "don't worry about it."
    pn "if... if you say so."
    tn "so what can i use this room for?"
    pn "whatever you need!"
    pn "if you need a private room for any... activities, you won't be bothered here."
    pn "oh, and i installed a phone!"
    pn "so you can make calls!"
    tn "that sounds... useful."
    menu:
        "thank you":
            tn "well done, pema."
            tn "this will be a fine addition to my collection... of rooms."
            show bfac bfac06 with dissolve
            pn "...."
            pn "okay..."
            tn "now i need some privacy."
        "i guess you're still useful":

            tn "good work, cumslut."
            pn "oh... {i}fuck{/i} yes."
            tn "now get out."

    pn "yes..."
    pn "...sir."
    hide bfac with dissolve
    tn "nice... nice."
    tn "this room will come in handy."
    $ study_unlock = True
    $ b4_daytime = False
    jump study_menu

label pema_vag3:







    $ bfax_top = False

    b4_tx "puuusssy!!"
    show bfac bfac02 with dissolve
    pn "That's what I like to hear!"
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    show bfac bfac07
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    tn "those. fucking. tits."
    pn "ready to empty your balls in this pussy, love?"
    pn "fuck your breeding sow?"
    show ctc
    pause
    hide ctc
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos -200
    show bfax bfax01
    with Dissolve(1.5)

    pn "Mmmm? Well?"
    show ctc
    pause
    hide ctc
    pn "what are you waiting for?"
    pn "A permit?"
    show ctc
    pause
    hide ctc
    show bfax bfax02 with dissolve

    pn "treat me like a cheap whore!"
    b4_tn "don't flatter yourself..."
    tn "You {i}are{/i} a cheap whore."
    pn "More!"

    hide bfax
    show bfax bfax03:
        linear 1.0 xpos 0
        linear 0.6 xpos 10
        repeat
    pn "ahhhnn... yes, baby..."
    show ctc
    pause
    hide ctc
    pn "Ohhhh... fuck..."
    pn "that's just what I need!"
    pn "it's been so... fucking... long..."
    pn "Beat my pussy!"
    pn "fuck it into submission!"
    pn "with your stiff fucking cock!"

    show bfax bfax05:
        linear 1.0 xpos 10
        linear 0.0 xpos 0
        repeat
    with dissolve
    pn "yes... yes... baby...!!!"
    show ctc
    pause
    hide ctc
    pn "what's... ahh... ah... what's gotten into you?!"
    pn "you're really... ah... really giving it to me!"
    pn "do i turn you on that much?"
    tn "you haven't seen anything yet, you filthy fuck cow."
    pn "Ohh!" with hpunch
    pn "fuck... yes!!!"
    pn "More! more!"
    b4_tn "I'm surprised your swollen tits aren't leaking yet..."
    tn "because you're fucking gushing on this end!"
    pn "yes! yes!"
    show ctc
    pause
    hide ctc
    hide bfax
    show bfax bfax09:
        linear 0.45 xpos 10
        linear 0.0 xpos 0
        repeat
    pn "oh! fuck! fuck! yes!"
    pn "b-baby?!!"
    pn "ungh... ungh.... fuck!!!"
    show ctc
    pause
    hide ctc
    b4_tn "You want it?!"
    tn "You want my dick in that whore cunt of yours?"
    pn "yes! yes! i'm your whore!"
    pn "fuck my whore cunt!"
    pn "fuck it!"
    pn "I'm your slut! i'm yours!"
    pn "wife! mother! slave! whore! whatever you need!"
    pn "just fuck me! fuck me!!!"


    hide bfax
    show bfax bfax06:
        linear 0.8 xpos 40
        linear 0.2 xpos 0
        linear 0.8 xpos 10
        repeat
    pn "Yees!!"
    show ctc
    pause
    hide ctc

    pn "you're... ah... you're so swollen!!!"
    pn "give... give it all to me!"
    pn "blow your fat fucking load on my insides!"
    pn "drench me!!!"
    pn "drench your fuck puppy!!!" with hpunch

    menu:
        "cum inside":
            hide bfax
            play sound "audio/splurt2.ogg"
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt3.ogg"
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt1.ogg"
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            show bfax bfax10 with Dissolve(1.5)
            pn "Sooo... good."
            show ctc
            pause
            hide ctc
            pn "I can feel it flowing out of my pussy."
        "cum outside":

            b4_tn "on your back, spermslut!"

            show bfax bfax11:
                xpos 0 ypos 0
            with Dissolve(1.5)
            pn "paint me, love!"
            pn "paint your whore!"
            pn "I want it all over me!"
            pn "shower me! let me taste-"
            play sound "audio/splurt2.ogg"
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_1.png"
            with hpunch
            pn "yes!!"
            $ renpy.pause(0.5)
            play sound "audio/splurt3.ogg"
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_2.png"
            with hpunch
            pn "i love it!!"
            $ renpy.pause(0.5)
            play sound "audio/splurt1.ogg"
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_3.png"
            with hpunch
            $ renpy.pause(0.5)
            pn "Aaaaah...!"
            pn "So much..."

    show ctc
    pause
    hide ctc
    pn "fuck... you're... you're so intense now..."
    pn "I... i love you so much."
    menu:
        "don't get attached, bitch":
            tn "shut up, fucktoy."
        "i love your pussy":

            tn "well, i love your cunt."
    pn "spirits, yes... finally..."
    show ctc
    pause
    hide ctc

    if b4_daytime:
        $ b4_daytime = False
        jump b4_airtemple_map1
    else:
        scene black with dissolve
        "you promptly fall asleep."
        jump bk4_next

label lin_rub1:
    if lin_rub_equal ==0:
        lin "tell me you have something."
        tn "there's going to be another equalist rally."
        show bfaa bfaa04
        lin "damn it!!" with hpunch
        lin "where?!"
        tn "it's gonna be out in the streets."
        show bfaa bfaa03 with dissolve
        lin "....."
        tn "...what?"
        lin "this is great news."
        lin "we're ahead of them."
        tn "great. congrats."
        tn "now how about that payment?"
        lin "there's still a rally to interrupt."
        tn "aw man, i gave you the information."
        lin "and now we need to do something with it."
        lin "it's getting late now... but come back during the day and we'll do something about it."
        tn "oh, fine..."
        $ b4_daytime = False
        $ lin_rub_equal = 1
        jump b4_airtemple_map1
    if lin_rub_equal ==1:
        lin "good, you're here."
        lin "ready for the raid?"
        menu:
            "let's go":
                tn "sure, i'm in."
                pass
            "nope":

                tn "maybe later."
                lin "chickenshit."
                tn "...well, that's a little strong."
                lin "chicken. shit."
                tn "...."
                jump b4_repcity_map1

        lin "good."
        lin "meet me in the city streets."
        $ lin_rub_equal = 2
        jump b4_repcity_map1

    if lin_rub_equal ==2:
        lin "meet me in the city streets."
        jump b4_repcity_map1

    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0
    show bfaa bfaa03
    with dissolve
    lin "well, that didn't go exactly as planned..."
    tn "still though... my information was good."
    lin "...."
    lin "yes..."
    lin "i suppose it was."
    tn "and...?"
    lin "...and now i think there was a matter of payment."
    tn "that's right there is."
    lin "yeah."
    show bfaa bfaa10 with Dissolve(1.5)
    lin "get on the fucking table."
    show ctc
    pause
    hide ctc
    tn "\"fucking table\"?"
    tn "is that foreshadowing or just an expletive?"
    lin "shut the fuck up and take your clothes off."
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    hide bfaa
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"
    with Dissolve(1.5)
    show bfaz bfaz01 with hpunch
    b4_tn "alright, on the table, and feeling super vulnerable."

    show bfaz bfaz02 with Dissolve(1.5)
    lin "when are you going to just shut the fuck up?"
    show ctc
    pause
    hide ctc
    tn "it's not my strong suit."
    lin "Aren't you ashamed of yourself?"
    b4_tn "No?"
    lin "Fucking your wife in a public park where anyone could see you!"
    b4_tn "Oh, that."
    tn "Yeah, I wasn't entirely convinced that was a good idea either..."
    b4_tn "But Pema can be kind of forceful."

    show bfaz bfaz03 with Dissolve(1.5)
    "Lin let's some of her saliva fall on your dick."
    show ctc
    pause
    hide ctc

    show bfaz bfaz04 with Dissolve(1.5)
    lin "Don't act like you didn't enjoy it."
    b4_tn "....sorry for enjoying sex with my wife? I guess?"

    hide bfaz
    show bfaz bfaz05:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat

    show ctc
    pause
    hide ctc
    lin "hnnnn..."
    lin "unnh... yes..."
    lin "but her pussy's not that tight anymore, is it?"
    lin "this one is."
    show ctc
    pause
    hide ctc
    lin "you like this, don't you?"
    lin "rubbing against this tight cunt while your wife is home... taking care of your kids... making you dinner..."
    lin "but you're... fucking... ah... ungh... here with me... you fucking pervert... ahhn...."
    show ctc
    pause
    hide ctc
    lin "I saw you... slamming that dumb cunt... hhhnn..."
    lin "As if you're some dumb horny teenager who's never had any..."
    lin "Act... your... age... damn it!"
    b4_tn "just show me your fucking tits, lin!"
    hide bfaz
    show bfaz bfaz04
    with dissolve
    lin "is that what you want?"
    lin "you want to see my tits?"
    tn "yes, damn it!"
    lin "again."
    lin "ask me again."
    menu:
        "show me!":
            tn "take off that fucking shirt!"
        "please... please!":

            tn "I need them! please!"

    hide bfaz
    show bfaz bfaz05:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat
    lin "are you sure?"
    tn "yes!"
    lin "you really really want that?"
    lin "are you absolutely sure that you want to see my big, bouncing breasts?"
    tn "yes, yes, yes!"
    lin "unnghh... fuck... i love when you beg..."

    hide bfaz
    show bfaz bfaz06:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat
    lin "unnngh... fuck... yes..."
    show ctc
    pause
    hide ctc
    tn "my words... exactly..."

    menu:
        "switch view":
            $ temp_boolean = True

            lin "Shut up!"
            hide bfaz
            show expression "bk4/backgrounds/police_hq_ceiling.jpg"
            show bfaz bfaz07:
                ypos -8
                linear 0.2 ypos 0
                linear 0.6 ypos -8
                repeat
        "keep going like this":



            $ temp_boolean = False
            show bfaz bfaz08:
                linear 0.2 xpos 8 ypos 8
                linear 0.6 xpos 0 ypos 0
                repeat





    lin "You're much too old to be this desperate for sex!"
    show ctc
    pause
    hide ctc
    b4_tn "You sure we're still talking about me?"
    lin "i told you to shut up!"
    tn "i think i know someone who needs it pretty badly."
    tn "and she'd get it... if she asked."
    if temp_boolean == True:
        hide expression "bk4/backgrounds/police_hq_ceiling.jpg"

    hide bfaz

    show bfaz bfaz09:
        linear 0.3 xpos 20 ypos 20
        linear 0.6 xpos 0 ypos 0
        repeat

    lin "shut up! {size=+5}shut up! {size=+5}shut up!!!"
    show ctc
    pause
    hide ctc
    lin "Are you ready to beg me for it?"
    tn "...."
    tn "i thought you wanted me to shut up?"
    lin "Do you want to fuck me?!"
    b4_tn "Well yeah, but-"
    lin "You can't!"
    lin "And I'll drive you crazy with lust!"
    lin "fuck! fuck yes!"
    lin "spirits this is a fucking {size=+5}cock!"
    b4_tx "Hnnn... that's great, but I'm going to cum real soon now..."
    show ctc
    pause
    hide ctc


    menu:
        "cum on face":
            tx "take it on your face, you fucking bitch!"
            hide bfaz
            show bfaz bfaz10 at Move((0, 30), (0, 0), .10, bounce=True, repeat=False, delay=.275)
            lin "Cum all over my face, you fucking horndog!"
            play sound "audio/splurt2.ogg"
            hide bfaz
            show bfaz bfaz10
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_1.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_2.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt2.ogg"
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_3.png"
            with vpunch
            $ renpy.pause()
        "cum on pussy":

            tx "stand up, you fucking bitch!"
            hide bfaz
            show expression "bk4/backgrounds/police_hq_ceiling.jpg"
            show bfaz bfaz12 at Move((0, 100), (0, 0), 0.5, bounce=False, repeat=False)
            lin "Show me how good your aim is!"
            show bfaz bfaz13:
                ypos 0
            with Dissolve(1.5)
            lin "Fill me with {size=+5}your cum!!!"
            play sound "audio/splurt2.ogg"
            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout1.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout2.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout3.png"
            with vpunch
            $ renpy.pause()
    lin "spirits that was... that was so... fucking... good..."
    lin "wait, did you... did we just..."
    b4_tn "Phew...."
    tn "that was really-"
    lin "get out of my office!!"
    tn "but..."
    lin "get out! get out!!"
    play sound "audio/thud.mp3"
    scene black
    "lin, dripping in your semen, forcefully shoves you out the door."
    tn "uh."
    tn "okay?"
    "exhausted, you head home."
    jump bk4_next

label lin_rub_cont:
    $ lin_rub_equal = 3
    show bfaa bfaa03 with dissolve
    lin "it's about time you got here."
    tn "i came as fast as i could."
    lin "...i get the feeling you always do."
    tn "......."
    tn "that... was cold blooded."
    lin "you'll live."
    lin "let's go stop these equalists."
    scene black with dissolve
    scene expression "bk4/worldrooms/bg_000.jpg"
    with dissolve
    show bfal bfal05:
        xzoom -1
    with dissolve
    e1 "yes! join amon and the equalists and together-"
    e1 "...wait a minute, is this a misprint?!"
    e1 "it's all mirrored and shit."
    e1 "fuck, i think i ordered 500 of these."
    e1 "...."
    e1 "balls."
    show bfaa bfaa05 with dissolve
    lin "you!" with hpunch
    show bfal bfal01 with dissolve
    e1 "...aw, shit."
    lin "you're going to jail!"
    e1 "no, i'm not."
    lin "yes, you are!"
    e1 "uh-uh."
    lin "uh-huh!"
    e1 "says who?"
    lin "says me!"
    e1 "well, joke's on you."
    e1 "i have a secret weapon."
    lin "we're taking you in! right now!"
    e1 "fat chance!"
    show bfal bfal03
    e1 "get them, tom!" with hpunch
    show bfal04:
        xpos 150
    with dissolve
    e2 "it's todd, actually."
    e2 "and all this finger-point is making me uncomfortable."
    e2 "you know, they say that when you point a finger at someone... there's three pointing back at {i}you{/i}."
    e2 "so... think about that."
    e1 "shut up, tom."
    tn "shut up, tom."
    lin "shut up, tom."
    e2 "....."
    e2 "am... am i tom now?"
    e1 "go fight them!!" with hpunch
    e2 "...no?"
    e1 "do it!!"
    e2 "i signed up for the strong community, not the punching."
    e2 "tom, out."
    hide bfal04 with dissolve
    e1 "...."
    show bfal bfal02 with dissolve
    e2 "damn it, todd!"
    e2 "...."
    show bfal bfal01 with dissolve
    e1 "you have seen the last of us!"
    hide bfal with flash
    "the equalist disappears in a flash of light."
    tn "...ow."
    tn "my eyes."
    show bfaa bfaa04 with dissolve
    lin "damn!"
    lin "...."
    show bfaa bfaa03 with dissolve
    lin "still, we got them to disperse."
    lin "and they know we're onto them."
    lin "i think this is a victory."
    tn "uh... sure."
    lin "come on, let's go back to headquarters."
    scene black with dissolve
    jump lin_rub1

label lin_rub2:

    show bfaa bfaa10 with Dissolve(1.5)
    lin "get on the fucking table."
    show ctc
    pause
    hide ctc
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    hide bfaa
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"
    with Dissolve(1.5)
    show bfaz bfaz01 with hpunch
    b4_tn "on the table and vulnerable!"

    show bfaz bfaz02 with Dissolve(1.5)
    lin "when are you going to just shut the fuck up?"
    show ctc
    pause
    hide ctc
    tn "it's not my strong suit."
    lin "Aren't you ashamed of yourself?"
    b4_tn "No?"
    lin "your cock is rubbing the pussy of the chief of police on her desk!"
    lin "you're a married man!"

    show bfaz bfaz03 with Dissolve(1.5)
    "Lin let's some of her saliva fall on your dick."
    show ctc
    pause
    hide ctc

    show bfaz bfaz04 with Dissolve(1.5)
    lin "Don't act like you're not enjoying it."

    hide bfaz
    show bfaz bfaz05:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat

    show ctc
    pause
    hide ctc
    lin "hnnnn..."
    lin "unnh... yes..."
    lin "you like this, don't you?"
    lin "rubbing against this tight cunt while your wife is home... taking care of your kids... making you dinner..."
    lin "but you're... fucking... ah... ungh... here with me... you fucking pervert... ahhn...."
    show ctc
    pause
    hide ctc
    lin "As if you're some dumb horny teenager who's never had any..."
    lin "Act... your... age... damn it!"
    b4_tn "just show me your fucking tits, lin!"
    hide bfaz
    show bfaz bfaz04
    with dissolve
    lin "is that what you want?"
    lin "you want to see my tits?"
    tn "yes, damn it!"
    lin "again."
    lin "ask me again."
    menu:
        "show me!":
            tn "take off that fucking shirt!"
        "please... please!":

            tn "I need them! please!"

    hide bfaz
    show bfaz bfaz06:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat
    lin "unnngh... fuck... yes..."
    show ctc
    pause
    hide ctc
    tn "my words... exactly..."

    menu:
        "switch view":
            $ temp_boolean = True

            lin "Shut up!"
            hide bfaz
            show expression "bk4/backgrounds/police_hq_ceiling.jpg"
            show bfaz bfaz07:
                ypos -8
                linear 0.2 ypos 0
                linear 0.6 ypos -8
                repeat
        "keep going like this":



            $ temp_boolean = False
            show bfaz bfaz08:
                linear 0.2 xpos 8 ypos 8
                linear 0.6 xpos 0 ypos 0
                repeat





    lin "You're much too old to be this desperate for sex!"
    show ctc
    pause
    hide ctc
    b4_tn "You sure we're still talking about me?"
    lin "i told you to shut up!"
    tn "i think i know someone who needs it pretty badly."
    tn "and she'd get it... if she asked."
    if temp_boolean == True:
        hide expression "bk4/backgrounds/police_hq_ceiling.jpg"

    hide bfaz

    show bfaz bfaz09:
        linear 0.3 xpos 20 ypos 20
        linear 0.6 xpos 0 ypos 0
        repeat

    lin "shut up! {size=+5}shut up! {size=+5}shut up!!!"
    show ctc
    pause
    hide ctc
    lin "Are you ready to beg me for it?"
    tn "...."
    tn "i thought you wanted me to shut up?"
    lin "Do you want to fuck me?!"
    b4_tn "Well yeah, but-"
    lin "You can't!"
    lin "And I'll drive you crazy with lust!"
    lin "fuck! fuck yes!"
    lin "spirits this is a fucking {size=+5}cock!"
    b4_tx "Hnnn... that's great, but I'm going to cum real soon now..."
    show ctc
    pause
    hide ctc


    menu:
        "cum on face":
            tx "take it on your face, you fucking bitch!"
            hide bfaz
            show bfaz bfaz10 at Move((0, 30), (0, 0), .10, bounce=True, repeat=False, delay=.275)
            lin "Cum all over my face, you fucking horndog!"
            play sound "audio/splurt2.ogg"
            hide bfaz
            show bfaz bfaz10
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_1.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_2.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt2.ogg"
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_3.png"
            with vpunch
            $ renpy.pause()
        "cum on pussy":

            tx "stand up, you fucking bitch!"
            hide bfaz
            show expression "bk4/backgrounds/police_hq_ceiling.jpg"
            show bfaz bfaz12 at Move((0, 100), (0, 0), 0.5, bounce=False, repeat=False)
            lin "Show me how good your aim is!"
            show bfaz bfaz13:
                ypos 0
            with Dissolve(1.5)
            lin "Fill me with {size=+5}your cum!!!"
            play sound "audio/splurt2.ogg"
            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout1.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout2.png"
            with vpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout3.png"
            with vpunch
            $ renpy.pause()
    lin "spirits that was... that was so... fucking... good..."
    lin "wait, did you... did we just..."
    b4_tn "Phew...."
    tn "that was really-"
    lin "get out of my office!!"
    tn "but..."
    lin "get out! get out!!"
    play sound "audio/thud.mp3"
    scene black
    "lin, dripping in your semen, forcefully shoves you out the door."
    tn "uh."
    tn "okay?"
    "exhausted, you head home and sleep."
    jump bk4_next

label asami_blowjob1:
    hide screen bk4_money_date
    with dissolve
    b4_tp "asami, there has been a... development."
    b4_tp "you'll want to come over here."
    asa "...."
    b4_tp "Meet me in my study room."
    asa "You have a study room?"
    b4_tp "It was a surprise to me as well!"
    b4_tp "i mean, how the heck was i calling you from a tower?"
    b4_tp "that doesn't make any sense!"
    b4_tp "why would there be a phone in there?"
    b4_tp "besides, it's all landlines, so it's not like i'd get better reception."
    asa "...i'm coming over, just stop talking."
    b4_tp "i'm getting that a lot lately."
    asa "good."
    "*click*"


    show bfad bfad02 with fade
    asa "Okay... I'm here."
    asa "Now what?"
    asa "You want me to shake my tits or something?"
    tn "not this time."
    asa "you said you have something?"
    asa "is it another photograph?"
    b4_tn "Hmmm... no."

    show bfad bfad08 with dissolve

    asa "No?"

    b4_tn "Asami... take a look for yourself."
    "you show her the weapon, but are careful not to let her touch it."
    show bfad bfad03 with dissolve
    asa "what... what is this?!"
    tn "this is what your father has been doing."
    asa "no... no, this is another ploy."
    tn "it's really not."
    asa "you can't... you can't show anyone this!"
    asa "do you understand?!"
    asa "he'll be... we'll be ruined!"
    tn "yes, this is truly likely to destroy future industries, your father, your inheritance, and your life."
    asa "i... i get it..."
    asa "what do you want?"
    b4_tn "remember what I said the first time?"
    tn "when Meelo interrupted us?"
    asa "You said \"Suck my co-\""
    tn "that's correct."
    asa "you... want me to suck your cock?"
    b4_tn "oh yeah. I'd like some of that."

    asa "*sigh*"

    asa "I guess I'll take some precautions for what's inevitable then."
    stop music
    play music "audio/Unwritten Return.mp3"
    show bfad bfad10 with Dissolve(1.5)
    show ctc
    pause
    hide ctc

    asa "do you want me to just get on my knees or-"
    kn "tenzin?"
    tn "aw, shit!"
    tn "asami, go hide in that corner!"
    asa "but... that's not hidden at all!"
    tn "it'll have to do!"
    asa "...fine, but it's stupid."
    tn "just... keep absolutely still."
    tn "its vision is based on movement."

    hide bfad
    show bfad bfad11:
        xpos 300 ypos -20
    with Dissolve(1.5)
    tn "*ahem*"
    tn "come in."
    show bfab bfab04:
        xzoom -1
    with moveinleft
    kn "hey, do you have a second to talk?"
    tn "not really..."
    show bfab bfab03 with dissolve
    kn "great! it'll just be a second!"
    tn "...."
    show bfab bfab04 with dissolve
    kn "we really need to increase our training schedule."
    tn "i think our schedule is fine."
    kn "it's just-"
    tn "i am the master, korra. not you."
    kn "but-"
    tn "enough."
    tn "we will train more when i decide it's appropriate."
    tn "now get out."
    show bfab bfab25 with dissolve
    kn "fine..."
    hide bfab with moveoutleft
    tn "...."
    asa "...i can't believe that worked."
    asa "she didn't see me."
    tn "now get back over here."
    asa "really?"
    tn "i'm not going to avoid fucking your face just because those big tits interrupted us."
    tn "get over here."

    show expression "bk4/backgrounds/study0.jpg":
        ypos -200
    show bfav bfav00
    hide bfad
    with Dissolve(1.5)
    asa "Okay... I guess we're doing this..."
    show ctc
    pause
    hide ctc
    tn "that's right."
    tn "now, beg."
    asa "....."
    asa "please... can i suck your co-"
    show bfav bfav01
    asa "-ck."
    asa "....."
    asa "shit... that's big."
    show ctc
    pause
    hide ctc
    tn "and i haven't heard you thank me yet."
    asa "...."
    asa "...thank you for letting me... suck you off."
    tn "good girl."
    asa "......"
    tn "don't tell me this is your first blowjob."

    show bfav bfav01a
    asa "well... of course it is..."
    tn "what do you mean \"of course\"?"
    asa "i'm... the heiress of a mass fortune."
    asa "i'm in the highest of societies."
    asa "my actions are always watched, and i have etiquette to maintain."
    asa "and, of course, i must remain a good match for a future mate."
    asa "blow... jobs... are certainly not \"proper\"."
    asa "would you reconsider?"
    tn "that just makes me want to fuck your face more."
    asa "*sigh*..."
    asa "i should have assumed."
    asa "i guess i'll just... start?"
    asa "....."
    tn "lick it, asami."
    tn "wipe your tongue all over my cock."
    tn "clean the stink off of it, since you're so \"proper\"."
    asa "...."
    show bfav bfav08
    asa "*slurp* *lick*"
    show ctc
    pause
    hide ctc
    tn "that's it, girl..."
    asa "*lick* *lick* *lick*"
    tn "don't be afraid to give it a good deep scrub with your taste buds."
    tn "swallow the precum as it leaks out."
    show ctc
    pause
    hide ctc
    tn "start sucking, come on."
    asa "....."
    show bfav bfav02
    asa "*slurp* *mmgh* *gulp*"
    show ctc
    pause
    hide ctc
    tn "yes... yes, that's it..."
    asa "mmmgh..."
    tn "do you like sucking that fat cock, asami?"
    tn "sucking cock to keep your father out of prison?"
    tn "you know that makes you a whore, right?"
    tn "you're a whore, asami."
    tn "sucking a man's cock in his study."
    asa "*suck* *slurp* *gulp*"
    tn "oh, i know you hate it..."
    tn "but soon, you won't be able to get enough."

    show bfav bfav08
    asa "do you make korra do this to you?"
    show ctc
    pause
    hide ctc
    tn "not yet, but that's an excellent idea."
    tn "keep sucking."

    show bfav bfav03
    asa "*slurp* *slurp* *mmmgh* *suck*"
    show ctc
    pause
    hide ctc
    tn "ah... yeah... deeper..."
    tn "deeper, you stupid bitch!"
    show bfav bfav04
    asa "mmmgh..."
    show ctc
    pause
    hide ctc
    tn "not... ugh... bad for a first suck, asami..."
    tn "if i didn't know better, i'd say you were lying to me."
    asa "i'm 'ot!!"
    tx "ungh i'm getting close!"
    show bfav bfav06
    asa "*gulp!* *ungmgh!*"
    show ctc
    pause
    hide ctc
    tn "oh fuck!"
    tn "you want my load, don't you!?"
    tx "you want it down your fucking throat?!"
    asa "mmmn-mmm!! 'oh!"
    tx "here it comes!"
    show ctc
    pause
    hide ctc
    menu:
        "inside":
            play sound "audio/splurt2.ogg"
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt3.ogg"
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)

            show ctc
            pause
            hide ctc
            tx "down your fucking throat, asami!"
            play sound "audio/splurt1.ogg"
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc

            show bfav bfav07 with Dissolve(1.5)
            asa "*cough* *cough*"
        "outside":

            tx "on your knees! i'm going to glaze your face!"
            hide bfav
            show expression "bk4/backgrounds/study0.jpg":
                ypos -420
            show bfav bfav09
            with Dissolve(1.5)
            asa "my... my face...?"
            tx "take it, bitch!"
            play sound "audio/splurt2.ogg"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_1.png" with hpunch
            asa "oh!"
            show ctc
            pause
            hide ctc
            play sound "audio/splurt3.ogg"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_2.png" with hpunch
            show ctc
            pause
            hide ctc
            play sound "audio/splurt1.ogg"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_3.png" with hpunch
            show ctc
            pause
            hide ctc
            asa "...."

    asa "so?"
    asa "can i... can i take the weapon away?"
    tn "no."
    asa "n-no? what? why?!"
    asa "I... i sucked you off!"
    asa "i did what you asked!"
    asa "i let you... i let you cum!"
    tn "and as long as you continue to do so, i will keep this a secret."
    tn "but if i ever call you... and you don't come running..."
    tn "and you don't do what i tell you..."
    tn "i will destroy your life."
    tn "do you understand?"
    asa "i... i..."
    tn "say \"yes, sir\"."
    asa "y-yes, sir."
    tn "good."
    tn "now get the fuck out."
    tn "and take my cum with you."
    tn "wipe it on your clothes if you have to."
    tn "i don't want a mess in here."
    asa "i... yes... sir."
    scene black with dissolve
    "asami uses her undershirt to wipe the cum from her mouth and face."
    "she puts her outer shirt on over her bare tits."
    scene expression "bk4/backgrounds/study0.jpg":
        ypos 0
    show bfad bfad06
    with dissolve
    asa "very well."
    asa "i assume we have an agreement?"
    tn "yes... but first, you're going to thank me."
    asa "thank...?"
    show bfad bfad05 with dissolve
    asa "i just sucked your filthy penis!"
    asa "i'm not going to thank you!"
    asa "wait... what are you doing?"
    b4_tp "hmm? me?"
    b4_tp "just calling the police."
    b4_tp "hello? can i speak to chief beifong please?"
    asa "wait! wait! thank you!" with hpunch
    b4_tp "hmm?"
    asa "thank you! thank you so much!"
    asa "thank you for letting me suck you off!"
    asa "i'm so grateful i could swallow all of your thick... so, so thick..."
    asa "unpleasantly, hard-to-swallow thick..."
    asa "...ejaculate."
    b4_tp "......"
    b4_tp "well, i think-"
    lin "tenzin?"
    lin "what the fuck do you want?"
    b4_tp "shut up, lin."
    lin "you can't call the police and-"
    tn "*click*"
    tn "you're welcome, asami."
    asa "you... are an ass."
    show bfad bfad06 with dissolve
    asa "goodbye."
    tn "wait."
    show bfad bfad05 with dissolve
    asa "what now?"
    tn "open your mouth."
    asa "i'm... sorry?"
    tn "open up."
    asa "i-"
    show bfad bfad07
    asa "mmgh!!!" with hpunch
    tn "suck my finger, asami."
    tn "convince me you want to keep coming back and sucking my dick."
    asa "mrmrrr...."
    show bfad bfad07a
    asa "mmmgh..."
    asa "*slurp* *suck* *gagh*"
    show ctc
    pause
    hide ctc
    tn "you like that, don't you?"
    asa "....."
    asa "...mm-hmm..."
    show bfad bfad07
    tn "good girl."
    show bfad bfad05 with dissolve
    asa "..."
    tn "and?"
    asa "....."
    asa "thank you."
    tn "you're welcome."
    tn "i'll see you soon."
    asa "...."
    hide bfad with dissolve
    scene black with dissolve
    "wiped out, you return to your room and sleep."
    jump bk4_next

label asami_blowjob2:
    hide screen bk4_money_date
    with dissolve
    b4_tp "asami, come here."
    asa "...."
    asa "...yes, sir."

    show bfad bfad02 with fade
    asa "Okay... I'm here."
    tn "what would you like to do?"
    asa "...."
    asa "i'd like to... to suck you off."
    asa "if you'll let me."
    tn "alright, i guess."
    tn "if you can manage."
    asa "I guess I'll take some precautions for what's inevitable then."
    stop music
    play music "audio/Unwritten Return.mp3"
    show bfad bfad10 with dissolve

    tn "smart."

    show ctc
    pause
    hide ctc
    show expression "bk4/backgrounds/study0.jpg":
        ypos -200
    show bfav bfav00
    hide bfad
    with Dissolve(1.5)
    asa "Okay... I guess we're doing this..."
    show ctc
    pause
    hide ctc
    show bfav bfav01
    tn "that's right."
    asa "*sigh...*"
    asa "thank you for letting me suck your cock."
    tn "good girl."
    asa "......"

    show bfav bfav01a
    asa "i guess i'll just... start?"
    tn "lick it, asami."
    tn "wipe your tongue all over my cock."
    tn "clean the stink off of it, since you're so \"proper\"."

    show bfav bfav08
    asa "*slurp* *lick*"
    show ctc
    pause
    hide ctc
    tn "that's it, girl..."
    asa "*lick* *lick* *lick*"
    tn "don't be afraid to give it a good deep scrub with your taste buds."
    tn "taste the precum as it leaks out."
    show ctc
    pause
    hide ctc
    tn "start sucking, come on."
    asa "....."
    show bfav bfav02
    asa "*slurp* *mmgh* *gulp*"
    show ctc
    pause
    hide ctc
    tn "yes... yes, that's it..."
    asa "mmmgh..."
    tn "do you like sucking that fat cock, asami?"
    tn "sucking cock to keep your father out of prison?"
    tn "you know that makes you a whore, right?"
    tn "you're a whore, asami."
    tn "sucking a man's cock in his study."
    asa "*suck* *slurp* *gulp*"
    tn "oh, i know you hate it..."
    tn "but soon, you won't be able to get enough."

    show bfav bfav08
    asa "do you make korra do this to you?"
    show ctc
    pause
    hide ctc
    tn "not yet, but that's an excellent idea."
    tn "keep sucking."

    show bfav bfav03
    asa "*slurp* *slurp* *mmmgh* *suck*"
    show ctc
    pause
    hide ctc
    tn "ah... yeah... deeper..."
    tn "deeper, you stupid bitch!"
    show bfav bfav04
    asa "mmmgh..."
    show ctc
    pause
    hide ctc
    tn "not... ugh... bad, asami..."
    tn "you're getting better."
    tx "ungh i'm getting close!"
    show bfav bfav06
    asa "*gulp!* *ungmgh!*"
    show ctc
    pause
    hide ctc
    tn "oh fuck!"
    tn "you want my load, don't you!?"
    tx "you want it down your fucking throat?!"
    asa "mmmn-mmm!! 'oh!"
    tx "here it comes!"

    menu:
        "inside":
            play sound "audio/splurt2.ogg"
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt3.ogg"
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc
            play sound "audio/splurt1.ogg"
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            show ctc
            pause
            hide ctc

            show bfav bfav07 with Dissolve(1.5)
            asa "*cough* *cough*"
        "outside":

            hide bfav
            show expression "bk4/backgrounds/study0.jpg":
                ypos -420
            show bfav bfav09
            with Dissolve(1.5)
            tx "take this, bitch!"
            play sound "audio/splurt2.ogg"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_1.png" with hpunch
            show ctc
            pause
            hide ctc
            play sound "audio/splurt3.ogg"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_2.png" with hpunch
            show ctc
            pause
            hide ctc
            play sound "audio/splurt1.ogg"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_3.png" with hpunch
            show ctc
            pause
            hide ctc

    asa "so?"
    asa "can i... can i keep the weapon now?"
    tn "still no."
    tn "now get the fuck out."
    tn "and take my cum with you."
    tn "wipe it on your clothes if you have to."
    tn "i don't want a mess in here."
    asa "i... yes... sir."
    scene black with dissolve
    "asami uses her undershirt to wipe the cum from her mouth and face."
    "she puts her outer shirt on over her bare tits."
    scene expression "bk4/backgrounds/study0.jpg":
        ypos 0
    show bfad bfad06
    with dissolve
    asa "very well."
    asa "....."
    asa "thank you."
    tn "you're welcome."
    tn "i'll see you soon."
    asa "...thank you."
    hide bfad with dissolve
    scene black with dissolve
    "wiped out, you return to your room and sleep."
    jump bk4_next

label korra_spank1:
    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfab
    show bfba bfba07:

        ypos 170 xpos 0
    with fade
    kn "i don't understand..."



    show bfba bfba07:

        linear 3.0 ypos 0 xpos 00

    show expression "bk4/backgrounds/korra_room_night.jpg":

        linear 3.0 ypos -170 xpos 00

    kn "what..."


    show ctc
    pause
    hide ctc

    show expression "bk4/backgrounds/korra_room_night.jpg":

        ypos -170 xpos 0

    hide bfba

    show bfba bfba08



    show expression "bk4/korra/slapass/pants_flash.png" with vpunch

    hide expression "bk4/korra/slapass/pants_flash.png"


    kn "ah!!"
    kn "tenzin! what are you doing?! don't!"
    tn "stay still!" with hpunch
    "her ass and legs tremble as she stays in your lap, her bare pussy fully visible and shaking."
    kn "let me get up. please. i don't understand..."
    show bfba bfba00
    tn "i'm going to give you the spanking you so desperately need."
    kn "no!" with hpunch
    "korra begins to move, trying to get up."
    tn "stay put!" with hpunch
    tn "if you move again, i'm going to put you out on the street!"
    kn "this isn't happening... this isn't happening..."

    tn "we'll start with some light tapping."
    tn "nothing too painful."
    kn "please... please just let me get up..."
    kn "let me put my pants back on and i promise to listen..."
    kn "i promise to forget about this..."
    kn "please..."
    tn "don't worry, i'll be gentle... at first."
    show bfba bfba01 with hpunch
    kn "oh!"
    show ctc
    pause
    hide ctc
    "you lightly slap korra's ass repeatedly -- just enough to feel its firm bounce."
    "her pussy twitches slightly with every hit, in time with her jiggling buttcheeks."

    kn "okay... okay... that's not... so bad..."
    tn "i've been dying to get my hands on this ass..."
    kn "um... okay, but... are you almost-"





    show bfba bfba05
    kn "ahhh!!!"
    show ctc
    pause
    hide ctc

    b4_ta "you irresponsible, back-talking, spoiled little bitch!"
    kn "ah! ahh!!!"
    show ctc
    pause
    hide ctc

    "korra puts her hand against the wall to steady herself against your violent slaps against her smooth, naked ass."

    hide bfba

    show bfba bfba10
    with dissolve
    tn "there, you made it through the first part."
    show ctc
    pause
    hide ctc
    kn "wh-why are you doing this?"
    kn "it hurts!"

    show bfba bfba11
    tn "shhh..."
    show ctc
    pause
    hide ctc
    kn "*sniff*"
    tn "it's punishment, korra."
    kn "ten... tenzin..."
    kn "why are you doing this..."
    "you stroke korra's perfectly smooth and rounded butt, slipping a finger against her hole as you do."
    "she seems both uncertain and yet relieved as you squeeze and pet her gorgeous rear."
    show ctc
    pause
    hide ctc
    tn "why do you think i'm doing this?"
    kn "...."
    kn "because..."
    kn "because you're... cruel..."
    tn "try again."
    kn "because..."
    kn "...because i don't listen..."
    tn "well done."
    tn "and for recognizing that..."

    tn "...your punishment is finished, korra."
    kn "it... *sniff*... it is?"
    tn "yes."

    tn "next time, do as you're told."
    kn "y-yes..."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head to your room to get some well-earned rest."
    tn "I better make sure I slip Korra some of this powder stuff somewhere secluded."
    tn "Dragging Korra's unconscious body behind me where Pema might see us might be too much to handle, even for her."
    $ korra_resist -=2
    $ korra_moral -=2
    "korra's {b}resistance{/b} lowered!"
    "korra's {b}morality{/b} lowered!"
    jump bk4_next

label korra_spank3:
    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfab
    show bfba bfba07:

        ypos 170 xpos 0
    with fade
    tn "i'm not going to go easy on you this time."
    kn "thank... thank you..."
    tn "did you just thank me, korra?"
    kn "yes..."
    tn "why?"
    kn "because... because i deserve this."

    show bfba bfba07:

        linear 3.0 ypos 0 xpos 00
    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":

            linear 3.0 ypos -170 xpos 00
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":

            linear 3.0 ypos -170 xpos 00

    kn "....."


    show ctc
    pause
    hide ctc

    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":

            ypos -170 xpos 0
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":

            ypos -170 xpos 0

    hide bfba

    show bfba bfba08



    show expression "bk4/korra/slapass/pants_flash.png" with vpunch

    hide expression "bk4/korra/slapass/pants_flash.png"

    kn "ahh!"
    kn "i mean... that's... that's good..."

    "korra trembles violently in your lap, but puts up no resistance."
    show bfba bfba00
    tn "this time, you will truly be punished."
    kn "i understand... and thank you."

    show bfba bfba05
    kn "ahhh!!!"
    show ctc
    pause
    hide ctc

    b4_ta "this is what you get!"
    kn "thank... ahh!!"
    kn "thank you!!! *sob*"
    show ctc
    pause
    hide ctc

    "korra steadies herself against the wall and continues to return to position after each vicious slap."
    ta "what are you?!"
    kn "st-stupid!"
    kn "and... ahh!!!"
    ta "and?"
    kn "th-thank!! ahh!! you!!"
    hide bfba

    show bfba bfba10
    with dissolve
    tn "hmmmm...."
    show ctc
    pause
    hide ctc
    kn "wh-why are you st-stopping?"
    kn "i... i deserve..."
    kn "*sob* i deserve more..."
    show bfba bfba11
    tn "yes... and you'll get more."
    kn "....."
    show ctc
    pause
    hide ctc
    tn "what do you have to say?"
    kn "i'm... i'm sorry i'm so stupid."
    kn "thank you... thank you for teaching me..."
    kn "thank... thank you for... for punishing me..."
    kn "for... for petting my... my naked behind..."
    kn "*sob...*"
    kn "{size=-4}oh, spirits... why..."

    tn "your punishment is almost finished, korra."
    kn "it... *sniff*... it is?"
    tn "yes."
    show bfba bfba00 with dissolve
    "you pull your hand back and korra wriggles nervously, but stays in your lap."
    kn "be... be gentle..."
    menu:
        "extra hard slaps!":

            tn "no."
            show bfba bfba05a

            kn "aahahhhhh!!!!"
            show ctc
            pause
            hide ctc

            b4_tx "This hurts you more than it does me, Korra! you stupid bitch!"


            kn "oww!!! ow! no! nonono!!!"
            tx "yes! take everything you deserve, you entitled, whiny, big-assed whore!!"

            kn "aaahhhhh!!!! nooo!!! no! no!!! stop!!! please!!!"
            show ctc
            pause
            hide ctc
            kn "i'm sorry!!"
            kn "i'm so sorry!!!"
            kn "please! please, tenzin!!! i'm so... ahhh!!! so sorry!!!"
            kn "forgive me!!"
            kn "please!!! i can't take any more!!!"
            menu:
                "a little more":
                    show ctc
                    pause
                    hide ctc
                    $ korra_mad = 2
                "finish":

                    pass

            hide bfba



            show bfba bfba12
            with dissolve

            kn "oowww....."
            show ctc
            pause
            hide ctc
            kn "...why, tenzin...?"
            kn "i just... i'm so sorry..."
            tn "you disobeyed me, korra."
            tn "are you beginning to learn the consequences of your stubborn arrogance?"
            kn "....yes...."
            tn "good."
            show ctc
            pause
            hide ctc
            tn "you may stand now."
            show bfba bfba13 with Dissolve(1.5)

            kn "ohhh...."
            tn "...."
            b4_tn "Aren't you going to pull up your pants?"

            kn "No, i... I'm just going to let it cool off..."
            kn "for... for a few minutes..."
            kn "....ow...."


            hide bfba

            show bfba bfba13:

                parallel:

                    linear 11.0 xpos 650
                parallel:


                    linear 1.0 ypos 50

                    linear 1.0 ypos 0

                    repeat

            "korra carefully walks over to an open window to let the wind caress her raw butt."
        "force her to cream!":




            if b4_daytime:
                show expression "bk4/backgrounds/korra_room_day.jpg":

                    ypos -350
            else:
                show expression "bk4/backgrounds/korra_room_night.jpg":

                    ypos -350


            show bfba bfba14
            with dissolve
            tn "are you ready for the last stage of your punishment, korra?"
            show ctc
            pause
            hide ctc
            kn "what... what are you going to do?"


            hide bfba

            show bfba bfba15

            "without a word, you slip your finger into her tight cunt."

            kn "auh!!"
            show ctc
            pause
            hide ctc
            kn "st-stop it!! stop it, tenzin!!"
            kn "don't... don't do that!! you can't do that!!"
            show ctc
            pause
            hide ctc
            tn "shhh... it's okay..."
            kn "it's... it's not! it's not okay!!"
            kn "you can't just-"

            hide bfba

            show bfba bfba16:

                linear 0.0 ypos 0

                linear 0.15 ypos 0

                linear 0.15 ypos 20

                linear 0.45 ypos 0

                repeat

            kn "ungh!!"

            show ctc
            pause
            hide ctc
            kn "what... what is... ahhhh...!"
            kn "i feel... i feel... ughh... i'm..."
            tn "give in... take it..."
            tn "let it come... let it come..."
            show ctc
            pause
            hide ctc
            kn "how are you... that feels... so good..."

            kn "I... I think I'm gonna..."

            b4_tn "Just let it happen..."

            kn "unnghh... ahhh.... ohhhh...."
            kn "noo... no, i'm... i'm.... oh..."
            kn "ohh.... {size=+6}spirits..."
            tn "cream! cream on my fucking fingers, korra!"
            kn "{size=+8}oh, spirits!!!"


            hide bfba

            show bfba bfba17 with dissolve



            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray1.png"

            with hpunch

            kn "Aaaaah!!!"



            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray2.png"

            with hpunch

            kn "uunnnnaaghhh!!!"





            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray3.png"

            with hpunch

            kn "Aaaaaaah!!!"

            kn "Ohh... oh..."
            kn "you... you made me... from... from spanking..."
            tn "and fingering your tight young pussy."
            kn "Unnhhh...."
            show ctc
            pause
            hide ctc

    tn "next time, do as you're told."
    kn "y-yes..."
    kn "thank... thank you..."
    if korra_spank_bj ==5:
        kn "{size=-4}now i just need to... come up with a sexual act..."
        tn "what was that?"
        kn "no-nothing."
        $ korra_spank_bj = 6
        $ korra_resist -=2
        $ korra_moral -=2
        "korra's {b}resistance{/b} lowered!"
        "korra's {b}morality{/b} lowered!"
    else:
        if korra_moral >=80:
            $ korra_moral -=1
            "korra's {b}morality{/b} lowered!"
    scene black with dissolve
    "you head to your room and get some well-earned rest."

    jump bk4_next

label korra_spank2:
    show bfab bfab04 with dissolve
    tn "you've been stubborn lately, haven't you?"
    show bfab bfab05 with dissolve
    kn "umm..."
    tn "entitled? spoiled?"
    tn "haven't you?"
    show bfab bfab25 with dissolve
    kn "...y-yes..."
    tn "then bend over my lap."
    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    hide bfab
    show bfba bfba07:

        ypos 170 xpos 0
    with fade
    kn "please... please don't..."



    show bfba bfba07:

        linear 3.0 ypos 0 xpos 00
    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":

            linear 3.0 ypos -170 xpos 00
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":

            linear 3.0 ypos -170 xpos 00

    kn "please..."


    show ctc
    pause
    hide ctc

    if b4_daytime:
        show expression "bk4/backgrounds/korra_room_day.jpg":

            ypos -170 xpos 0
    else:
        show expression "bk4/backgrounds/korra_room_night.jpg":

            ypos -170 xpos 0

    hide bfba

    show bfba bfba08



    show expression "bk4/korra/slapass/pants_flash.png" with vpunch

    hide expression "bk4/korra/slapass/pants_flash.png"


    kn "ah!!"
    tn "stay still!"
    "her ass and legs tremble as she stays in your lap, her bare pussy fully visible and shaking."
    kn "please don't do this, tenzin..."
    kn "let me get up."
    kn "please..."
    show bfba bfba00
    tn "i'm going to give you the spanking you so desperately need."
    kn "wait... wait, please...."
    tn "we'll start with some light tapping."
    tn "nothing too painful."
    kn "please... please just let me get up..."
    kn "let me put my pants back on and i promise to listen..."
    kn "please..."
    tn "don't worry, i'll be gentle... at first."
    show bfba bfba01 with hpunch
    kn "oh!"
    show ctc
    pause
    hide ctc
    "you lightly slap korra's ass repeatedly -- just enough to feel its firm bounce."
    "her pussy twitches slightly with every hit, in time with her jiggling buttcheeks."

    kn "okay... okay... that's not... so bad..."
    tn "such a perfect ass..."
    kn "um... okay, but... are you almost-"





    show bfba bfba05
    kn "ahhh!!!"
    show ctc
    pause
    hide ctc

    b4_ta "you irresponsible, back-talking, spoiled little bitch!"
    kn "ah! ahh!!!"
    show ctc
    pause
    hide ctc

    "korra puts her hand against the wall to steady herself against your violent slaps against her smooth, naked ass."

    hide bfba

    show bfba bfba10
    with dissolve
    tn "there, you made it through the first part."
    show ctc
    pause
    hide ctc
    kn "wh-why are you doing this?"
    kn "it hurts!"

    show bfba bfba11
    tn "shhh..."
    show ctc
    pause
    hide ctc
    kn "*sniff*"
    tn "it's punishment, korra."
    kn "ten... tenzin..."
    kn "why are you doing this..."
    "you stroke korra's perfectly smooth and rounded butt, slipping a finger against her hole as you do."
    "she seems both uncertain and yet relieved as you squeeze and pet her gorgeous rear."
    show ctc
    pause
    hide ctc
    tn "why do you think i'm doing this?"
    kn "...."
    kn "because..."
    kn "because you're... cruel..."
    tn "try again."
    kn "because..."
    kn "...because i don't listen..."
    tn "well done."
    tn "and for recognizing that..."
    tn "...your punishment is almost finished, korra."
    kn "it... *sniff*... it is?"
    tn "yes."
    show bfba bfba00 with dissolve
    "you pull your hand back and korra wriggles nervously, but stays in your lap."
    kn "be... be gentle..."
    menu:
        "extra hard slaps!":


            show bfba bfba05a

            kn "aahahhhhh!!!!"
            show ctc
            pause
            hide ctc

            b4_tx "This hurts you more than it does me, Korra! you stupid bitch!"


            kn "oww!!! ow! no! nonono!!!"
            tx "yes! take everything you deserve, you entitled, whiny, big-assed whore!!"

            kn "aaahhhhh!!!! nooo!!! no! no!!! stop!!! please!!!"
            show ctc
            pause
            hide ctc
            kn "i'm sorry!!"
            kn "i'm so... aahhh!!! so sorry!!!"
            kn "please!! I can't take any more!!!"

            menu:
                "a little more":
                    show ctc
                    pause
                    hide ctc
                    $ korra_mad = 2
                "finish":

                    pass

            hide bfba



            show bfba bfba12
            with dissolve

            kn "oowww....."
            show ctc
            pause
            hide ctc
            kn "...why, tenzin...?"
            tn "as a lesson."
            tn "are you beginning to learn the consequences of your stubborn arrogance?"
            kn "....yes...."
            tn "good."
            show ctc
            pause
            hide ctc
            tn "you may stand now."
            show bfba bfba13 with Dissolve(1.5)

            kn "ohhh...."
            tn "...."
            b4_tn "Aren't you going to pull up your pants?"

            kn "No, i... I'm just going to let it cool off..."
            kn "for... for a few minutes..."
            kn "....ow...."


            hide bfba

            show bfba bfba13:

                parallel:

                    linear 11.0 xpos 650
                parallel:


                    linear 1.0 ypos 50

                    linear 1.0 ypos 0

                    repeat

            "korra carefully walks over to an open window to let the wind caress her raw butt."
        "force her to cream!":




            if b4_daytime:
                show expression "bk4/backgrounds/korra_room_day.jpg":

                    ypos -350
            else:
                show expression "bk4/backgrounds/korra_room_night.jpg":

                    ypos -350


            show bfba bfba14
            with dissolve
            tn "are you ready for the last stage of your punishment, korra?"
            show ctc
            pause
            hide ctc
            kn "what... what are you going to do?"


            hide bfba

            show bfba bfba15

            "without a word, you slip your finger into her tight cunt."

            kn "auh!!"
            show ctc
            pause
            hide ctc
            kn "st-stop it!! stop it, tenzin!!"
            kn "don't... don't do that!! you can't do that!!"
            show ctc
            pause
            hide ctc
            tn "shhh... it's okay..."
            kn "it's... it's not! it's not okay!!"
            kn "you can't just-"

            hide bfba

            show bfba bfba16:

                linear 0.0 ypos 0

                linear 0.15 ypos 0

                linear 0.15 ypos 20

                linear 0.45 ypos 0

                repeat

            kn "ungh!!"

            show ctc
            pause
            hide ctc
            kn "what... what is... ahhhh...!"
            kn "i feel... i feel... ughh... i'm..."
            tn "give in... take it..."
            tn "let it come... let it come..."
            show ctc
            pause
            hide ctc
            kn "how are you... that feels... so good..."

            kn "I... I think I'm gonna..."

            b4_tn "Just let it happen..."

            kn "unnghh... ahhh.... ohhhh...."
            kn "noo... no, i'm... i'm.... oh..."
            kn "ohh.... {size=+6}spirits..."
            kn "{size=+8}oh, spirits!!!"


            hide bfba

            show bfba bfba17 with dissolve



            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray1.png"

            with hpunch

            kn "Aaaaah!!!"



            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray2.png"

            with hpunch

            kn "uunnnnaaghhh!!!"





            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray3.png"

            with hpunch

            kn "Aaaaaaah!!!"

            kn "Ohh... oh..."
            kn "you... you made me... from... from spanking..."
            tn "and fingering your tight young pussy."
            kn "Unnhhh...."
            show ctc
            pause
            hide ctc

    tn "next time, do as you're told."
    kn "y-yes..."
    scene black with dissolve
    "you head to your room and get some well-earned rest."
    if korra_moral >=80:
        $ korra_moral -=1
        "korra's {b}morality{/b} lowered!"
    jump bk4_next


label korra_blowjob1:
    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    scene black
    show bfay bfay00:
        ypos 0
    with Dissolve(3)
    kn "Uuunhhh..."
    kn "wha... wha's going on..."



    show bfay bfay00:
        ypos 0
        easeout 2 ypos -300
    kn "I... I can't move my arms."

    scene black
    show expression "bk4/backgrounds/bg_hangkorra.jpg":
        ypos -300
    show bfay bfay02
    with Dissolve(1.5)


    kn "Hello?!"
    kn "Can anyone hear me?!"
    show ctc
    pause
    hide ctc
    kn "Anyone?!"

    show bfay bfay03 with Dissolve(1.5)
    b4_tam "Hello, Korra."
    show bfay_shock with hpunch
    kn "Amon!"
    show ctc
    pause
    hide ctc
    b4_tam "Ah, you remember me."
    tam "Good."
    b4_tam "We need to have a little talk, Korra."
    kn "eep..."
    b4_tam "I'm disappointed in your lack of progress with Tenzin."

    kn "umm... ummmm...."

    b4_tam "There is so much more that can be done, and I feel like you're dragging your feet."
    b4_tam "I might have to take away your bending."
    b4_tam "Maybe I should spare myself the trouble and just do it right here and now."
    b4_tam "What do you think?"
    tam "Should I?"

    hide bfay_shock
    show bfay bfay03a with hpunch
    kn "P-please don't!"
    kn "I... I'll do better!"

    show ctc
    pause
    hide ctc
    menu:
        "let her go":
            b4_tam "Fine."
            tam "But don't you ever forget, Korra, that I can reach your whenever and wherever I please."
        "Give her a warning she'll never forget":


            tam "i fear you've grown complacent."
            tam "obviously, my threats have not been encouragement enough."
            tam "that is my failing."
            tam "so now... i will provide a warning you'll remember."
            show bfay bfay04a with Dissolve(2.0)
            show ctc
            pause
            hide ctc
            kn "Wha... what are you going to-"
            show bfay bfay05 with hpunch
            kn "mmmmgh!!!"
            show ctc
            pause
            hide ctc
            b4_tam "Yes, that's more like it."
            b4_tam "You look great with a hard cock in your mouth."
            b4_tam "I don't really have to tell you what happens if you get teethy, do I?"
            kn "....mmgh."
            b4_tam "Good."

            hide bfay
            show bfay bfay01:
                linear 0.8 xpos 20
                linear 0.4 xpos 0
                repeat

            kn "....hngh!!!"
            hide text
            show text "{color=#ffc0cb}shlurp":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3
            show ctc
            pause
            hide ctc
            show text "{color=#ffc0cb}suck":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3

            b4_tam "How do you like blowing me?"
            b4_tam "That's all your mouth is good for."
            hide text
            show text "{color=#ffc0cb}slurp":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3

            b4_tam "Count yourself lucky I don't feel like anal today."
            kn "mmgh!! hgnh!"
            b4_tam "I'd have no problem spreading your asscheeks and bury my dick in it to the hilt."
            hide text
            show text "{color=#ffc0cb}gulp":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3
            kn "mmn! nnnh!!"
            b4_tam "You're just a collection of holes for me to do with as I please."
            hide text
            show text "{color=#ffc0cb}gagh":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3
            b4_tam "A living fleshlight."
            b4_tam "Hmmm... a korra themed fleshlight might actually sell well."
            hide text
            show text "{color=#ffc0cb}suck":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3
            kn "...mmmngnh??"
            b4_tam "You can't imagine how often people told me I was a disappointment compared to you while I was younger."
            hide text
            show text "{color=#ffc0cb}slurp":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3
            b4_tam "\"{i}Korra could already bend water, earth and fire when she was six years old!{/i}\""
            b4_tam "\"{i}Why can't you?!{/i}\""
            b4_tam "That kind of shit gets pretty old really fast."
            hide text
            show text "{color=#ffc0cb}gulp":
                rotate -25
                xalign 0.8 yalign 0.3
                linear 3 yalign -0.3
            kn "...mhmh?!?"
            b4_tam "What do you mean that doesn't make sense? "
            kn "...hmmgh?!?"
            b4_tam "Oh, right... never mind all that."
            b4_tam "Why the fuck do I even understand what you're mumbling anyway?"
            b4_tam "Have you ever tasted sperm, Korra?"
            kn "...hnmmhgh."
            show ctc
            pause
            hide ctc
            b4_tam "Let's speed this up."

            hide bfay
            show bfay bfay08
            hide text
            show text "{color=#ffc0cb}*gag* *shlurp*":
                rotate -25
                xalign 0.8 yalign 0.4
                linear 1.5 yalign -0.3

            kn "hmgh! kmgh!"
            show ctc
            pause
            hide ctc
            tam "what's that? you like choking on cock?"
            hide text
            show text "{color=#ffc0cb}*slurp* *cough*":
                rotate -25
                xalign 0.8 yalign 0.4
                linear 1.5 yalign -0.3
            tam "aw... is there a cock all the way down your throat?"

            tam "do you want a belly full of my semen, korra?"
            hide text
            show text "{color=#ffc0cb}*gag* *suck*":
                rotate -25
                xalign 0.8 yalign 0.4
                linear 1.5 yalign -0.3
            tam "how about a facefull of my load?"
            hide text
            show text "{color=#ffc0cb}*gulp*\n\n\n\n\n\n*suck*\n\n\n\n\n\n*slurp*\n\n\n\n\n\n*gag*":
                rotate -25
                xalign 0.8 yalign 0.4
                linear 8 yalign -1.8
            kn "hgmh! nngh!"
            tam "that's a yes!!"

            menu:
                "empty your balls on her face":
                    show bfay bfay06a with Dissolve(1.5)
                    show bfay bfay06
                    b4_tam "Catch."


                    show bfay bfay06a

                    play sound "audio/splurt2.ogg"
                    show bfay_spermshot
                    show expression "bk4/korra/bj/spermout1.png" with hpunch
                    kn "ahh...!!"
                    play sound "audio/splurt3.ogg"
                    show bfay_spermshot
                    show expression "bk4/korra/bj/spermout2.png" with hpunch
                    kn "ughh... ewww..."
                    play sound "audio/splurt1.ogg"
                    show bfay_spermshot
                    show expression "bk4/korra/bj/spermout3.png" with hpunch
                    show bfay bfay03a
                    kn "ewww... ugh... nooo..."
                "let it all go down her throat":




                    play sound "audio/splurt2.ogg"
                    show bfay bfay07 with hpunch
                    kn "{size=+6}Hnngh!!!"
                    play sound "audio/splurt1.ogg"
                    show bfay bfay07 with hpunch
                    play sound "audio/gulp2.mp3"
                    kn "*gulp* *gulp*"
                    b4_tam "Hnnnnnnn... swallow..."
                    play sound "audio/splurt3.ogg"
                    show bfay bfay07 with hpunch
                    b4_tam "Hnnnnnnngggg... it!!"
                    play sound "audio/gulp2.mp3"
                    kn "*gulp* *gulp* *gulp* *gulp*"
                    hide bfay
                    show bfay bfay04a
                    show expression "bk4/korra/bj/sperm_inside.png"
                    with Dissolve(1.5)
                    kn "*cough! cough!*"

            b4_tam "Aaaah... that was nice."
            b4_tam "You're really good at being a piece of meat."

    kn "can... *cough*..."
    kn "can... i please go...?"
    b4_tam "I'll lower you to the floor in a moment."
    b4_tam "It shouldn't be long before you regain control over your arms."
    b4_tam "Tenzin is close by, and you'll be a good little girl and not say anything about what happened here."
    b4_tam "Understood?"
    kn "....yes...."
    b4_tam "Here's a homework assignment."
    tam "Do something dumb."
    b4_tam "Do something Tenzin will have to punish you for."
    kn "....yes."
    b4_tam "And whatever punishment he gives you... you'll thank him for it."
    tam "oh, and... come up with a good, sexual idea."
    tam "and perform it on him of your own free will."
    tam "understand?"
    kn "{size=-4}...yes."
    b4_tam "Till we meet again korra."
    b4_tam "And don't be mistaken..."
    tam "We {b}will{/b} meet again."



    scene black with Dissolve(1.5)
    hide text
    show text "{color=#fff} You lower Korra to the ground and make your retreat.{/color}"
    show ctc
    pause
    hide ctc
    $ amon_bj = True

    scene expression "bk4/worldrooms/bg_012.jpg"
    with dissolve
    show bfab bfab11 with dissolve
    kn "*sniff*..."
    tn "korra?"
    tn "what's wrong?"
    tn "ten... tenzin?"
    show bfab bfab05 with dissolve
    kn "...where have you been?"
    tn "after i gave you that drink, I left to check on some council issues."
    tn "did something happen?"
    show bfab bfab25 with dissolve
    kn "....."
    tn "you can tell me."
    hide bfab with dissolve
    show bfab bfab26 with dissolve
    kn "i...."
    kn "....."
    show bfab bfab27 with dissolve
    kn "...nothing happened."
    tn "nothing?"
    kn "...nothing."
    tn "are you sure?"
    tn "are you sure there isn't something you need to tell me?"
    kn "...."
    show bfab bfab26 with dissolve
    kn "...."
    kn "no. there's nothing."
    tn "well, that's strange."
    tn "isn't that strange."
    tn "hey, i need you to do something for me."
    kn "......"
    kn "okay...."
    tn "i have some more council issues to take care of."
    tn "can you go back to the house and tell pema that i'll be home late?"
    kn "......"
    kn "............"
    kn "i... i will do that."
    kn "i will... tell her that."
    tn "great!"
    tn "don't be so weird about it."
    show bfab bfab27 with dissolve
    kn "....."
    kn "tenzin...."
    tn "hm?"
    kn "....."
    show bfab bfab26 with dissolve
    kn "...you can count on me."
    tn "i know i can."
    kn "......."
    hide bfab with dissolve
    tn "oh, this is gonna be great."
    scene black with dissolve
    "you spend the rest of the day in the city, enjoying some carefree window-shopping and waiting for night to fall."
    "eventually, you head back to the island."
    $ b4_daytime = False
    $ korra_spank_bj = 4
    jump b4_airtemple_map1

label korra_asami_titsuck1:
    if k_a_titsuck ==0:
        b4_tp "asami!"
        b4_tp "you're not gonna believe who this is!"
        asa "...."
        asa "...is it tenzin?"
        b4_tp "nope!"
        b4_tp "...wait, did you say \"tenzin\"?"
        b4_tp "because it's tenzin."
        asa "...."
        b4_tp "hi!"
        asa "what. do you. want?"
        b4_tp "now, do you think that's the right attitude to use when addressing the man that can destroy your life?"
        asa "......"
        asa "how... may i help you?"
        b4_tp "see?!"
        b4_tp "that's so much better."
        b4_tp "i knew you had it in you."
        asa "right, yes, i can friendly."
        asa "why are you calling?"
        b4_tp "...."
        asa "...sir."
        b4_tp "i have a proposition for you."
        asa "oh."
        asa "great."
        asa "really."
        b4_tp "there's that attitude again."
        b4_tp "come over and let's discuss it."
        asa "...."
        asa "fine...."
        asa "it's not like i have a choice."
        b4_tp "you have a choice."
        b4_tp "it's just that one option is that your life is over."
        asa "...."
        asa "i'm on my way."
        b4_tp "good call."
        show black with dissolve
        "you wait patiently for asami to arrive."
        tn "i'm booooooooooooored!!!"
        "so patient."
        hide black with dissolve
        show bfad bfad02 with dissolve
        asa "alright, i'm here."
        asa "what is it?"
        asa "...sir."
        tn "well..."
        tn "i haven't been able to help but notice that korra stares at your tits... constantly."
        tn "she is so thirsty for you."
        asa "...i know."
        asa "poor girl."
        asa "so what do you want from me?"
        tn "i want you to seduce her with your great rack."
        show bfad bfad08 with dissolve
        asa "you want..."
        asa "but i'm not..."
        show bfad bfad03 with dissolve
        asa "but i don't want to do that!"
        asa "she's my friend!"
        tn "you're not interested in korra's tits?"
        show bfad bfad02 with dissolve
        asa "they're amazing... but i'm not a lesbian."
        tn "even for korra?"
        show bfad bfad08 with dissolve
        asa "even... i..."
        show bfad bfad03 with dissolve
        asa "yes!"
        tn "oh."
        tn "still, though."
        tn "gonna need you to seduce her."
        asa "why are you like this?"
        tn "look, you both have great tits."
        tn "i'm not asking you to eat each other out... {size=-6}yet."
        asa "...."
        tn "just... have some fun."
        tn "you might be surprised."
        asa "ughh... fine."
        asa "but i'm not voting for you again as council member."
        tn "i was elected?"
        tn "wait, do i have an office?"
        show bfad bfad08 with dissolve
        asa "you are a mess."
        tn "no argument here."
        show bfad bfad02 with dissolve
        asa "well, since i have no choice-"
        tn "again, you have a choice."
        show bfad bfad03 with dissolve
        asa "no! i don't have a choice!"
        show bfad bfad02 with dissolve
        asa "*deep breath*"

        asa "anyway..."
        asa "since i have no choice..."
        asa "how do you want me to do this?"
        tn "babe, she wants your tits in her mouth so badly you can say literally anything."
        tn "she might need a little coaxing though."
        tn "you're a hot chick... seduce her."
        show bfad bfad08 with dissolve
        asa "I really don't want to do this..."
        tn "and that's why i want you to."
        show bfad bfad03 with dissolve
        asa "...i really hate you."
        tn "you might right now, but you'll come around."
        asa "I doubt it."
        tn "alright, i'm going to come by korra's room at night."
        tn "i expect to see you in there, seducing her."
        tn "if you fail..."
        tn "well, don't fail."
        asa "i only have one chance?!"
        asa "that's not fair!"
        tn "no, it's not."
        tn "do it anyway."
        asa "how am i supposed to do that?!"
        tn "you'll figure it out."
        asa "ugh."
        asa "fine."
        hide bfad with dissolve
        "asami leaves angrily, slamming doors on the way out."
        tn "man, do i know women."
        $ k_a_titsuck = 1
        jump b4_airtemple_map1

    if k_a_titsuck ==1:
        hide screen bk4_money_date
        scene expression "bk4/backgrounds/korra_room_night.jpg":
            ypos 0
        show bfab bfab07:
            xzoom -1
        show bfad bfad02
        show expression "bk4_xtra/misc/keyhole.png"
        with fade
        asa "i bet he'd like it, he seems the type."
        kn "but... that? really?"
        asa "yeah, sure."
        asa "you can at least offer it to him."
        kn "...i guess..."
        kn "i would never have even thought of that..."
        asa "now quit changing the subject."
        asa "come over here and give it a try."
        kn "I don't know..."
        tn "(move a little closer together, come on!)"
        asa "it'll be fun..."
        asa "just fun..."
        asa "come on korra..."
        asa "you're... very pretty, you know..."
        kn "you... um... i mean... you... too..."
        asa "it wouldn't mean anything..."
        asa "just two girls... having some fun..."
        kn "ummm...."
        kn "i don't..."
        tn "(asami's failing in there...)"
        tn "(i need to step in...)"
        hide expression "bk4_xtra/misc/keyhole.png"
        with fade
        tn "how could you?"
        show bfab bfab12
        kn "tenzin!!" with hpunch
        kn "wh-what... umm..."
        kn "i mean... hi."
        kn "nothing's happening in here."
        tn "oh, i know exactly what's happening."
        kn "you... you do?"
        tn "yes, and i'm disappointed in you."
        show bfab bfab24 with dissolve
        kn "...what?"
        tn "asami is here to help you."
        kn "umm... but... um..."
        tn "she's here to help expand your mind."
        tn "and help you embrace freedom."
        kn "oh..."
        kn "well..."
        asa "korra."
        show bfad bfad02:
            xpos 500
            linear 1 xpos 250
        asa "...don't you like my tits?"
        show bfab bfab07 with dissolve
        kn "i... well..."
        kn "i mean..."
        asa "let me help you."
        kn "umm..."
        asa "get on your knees."
        asa "lift your shirt."
        kn "i don't..."
        asa "shhh...."
        kn "tenzin is... is right there..."
        asa "ignore him."
        asa "it's just us here."
        kn "i...."
        kn "...o-okay..."
        hide bfab
        hide bfad
        show bfbb bfbb00
        with Dissolve(1.5)
        asa "good girl, just like that."
        show ctc
        pause
        hide ctc
        asa "there you go..."
        kn "oh... wow..."
        asa "is that a nice view?"
        kn "so... mmmm..."
        asa "what are you thinking?"
        kn "just... just..."

        asa "what do you want?"
        kn "I don't think i can just..."
        asa "really? why don't-"
        kn "fuck it!!!" with hpunch
        hide bfbb
        show bfbb bfbb05:
            linear 0.8 xpos 0
            linear 0.4 xpos 10
            repeat
        show text "{color=#ffc0cb}*suck*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2.5 yalign -0.3
            repeat
        asa "ahh...!!"
        show ctc
        pause
        hide ctc
        kn "mmm..."
        kn "*slurp* *mmmm*"
        asa "ahh... ah..."
        show ctc
        pause
        hide ctc
        asa "o-okay... okay, korra..."
        asa "ease... easy..."
        hide bfbb
        play sound "audio/kiss.mp3"
        show bfbb bfbb06
        hide text
        kn "*pop!*" with hpunch
        kn "*ahh*..."
        kn "sor... sorry, asami..."
        asa "mm, that was nice."
        asa "but i think that was-"
        tn "again."
        asa "...what?"
        kn "huh?"
        tn "suck her tits. again."
        asa "tenzin, i don't think..."
        tn "shut up, asami."
        tn "you know what? no. beg for it, asami."
        kn "...?"
        asa "i..."
        asa "...."
        asa "korra..."
        asa "...please suck my tits some more."
        kn "...umm..."
        kn "...really?"
        kn "i... i can?"
        asa "...please."
        asa "i want you... to slobber... on my big breasts..."
        asa "with your pretty face... and lips..."
        asa "slobber on my nip-"
        hide bfbb
        show bfbb bfbb05a:
            linear 0.6 xpos 0
            linear 0.3 xpos 10
            repeat
        hide text
        show text "{color=#ffc0cb}*suck*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2 yalign -0.3
            repeat
        kn "mmmmmm!!!"
        show ctc
        pause
        hide ctc
        asa "ahh... fuck...."

        asa "easy korra... fuck... that's... that's too hard..."
        kn "mmgh! mgh! mmmm!!!"
        asa "slow... slow... ahh... down!"
        show ctc
        pause
        hide ctc
        menu:
            "a little more":
                show ctc
                pause
                hide ctc
            "switch":
                pass

        tn "alright, enough."
        hide bfbb
        show bfbb bfbb05b:
            linear 0.4 xpos 0
            linear 0.2 xpos 10
            repeat
        hide text
        show text "{color=#ffc0cb}*suck*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 1.5 yalign -0.3
            repeat
        kn "mmmh.... mmm...."
        tn "...i said enough, korra."
        asa "ahh... ah... korra... kor... korra!"
        kn "mm! mmmm!!! mmmmmmhghg!!!!"
        show ctc
        pause
        hide ctc
        asa "stop it!!!" with hpunch
        hide bfbb
        play sound "audio/kiss.mp3"
        show bfbb bfbb06
        with dissolve
        hide text
        kn "oh!"
        kn "um... sorry."
        tn "that's perfectly fine."
        asa "{size=-6}my... my nipples..."
        tn "now i think you should switch roles."
        kn "oh?! really?!"
        asa "umm... what?"
        asa "you can't be serious."
        tn "look at my face, girl."
        asa "...."
        tn "korra: stand. Asami: kneel."
        show bfbb bfbb10
        with Dissolve(1)
        asa "{size=-4}sigh..."
        show ctc
        pause
        hide ctc
        asa "{size=-4}okay..."
        kn "....."
        kn "(do it, do it, do it...)"
        asa "....."
        asa "guess i'll just... dive in..."
        asa "........"
        hide bfbb
        show bfbb bfbb15a:
            linear 0.8 xpos 10
            linear 0.4 xpos 0
            repeat
        hide text
        show text "{color=#ffc0cb}*slurp*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2.5 yalign -0.3
            repeat
        asa "*suck* *suck*"
        show ctc
        pause
        hide ctc
        kn "nnghh...."
        kn "oh, spirits, yes..."
        asa "....*suck* *suck*"
        kn "ahhh... yes, asami... suck on my nipples... harder..."
        show bfbb bfbb15b1:
            linear 0.6 xpos 10
            linear 0.3 xpos 0
            repeat
        hide text
        show text "{color=#ffc0cb}*slurp*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2 yalign -0.3
            repeat
        kn "ahhh... yesss!!!"
        show ctc
        pause
        hide ctc
        kn "suck my fat tits, asami!!"
        asa "*slurp!* *slurp!* *suck!*"
        show ctc
        pause
        hide ctc
        hide bfbb
        hide text
        show bfbb bfbb16
        with dissolve
        asa "*pant* *pant*"
        asa "oh my spirits... this is... this is so hot..."
        show ctc
        pause
        hide ctc
        kn "don't stop!"
        hide bfbb
        show bfbb bfbb15c1:
            linear 0.4 xpos 10
            linear 0.2 xpos 0
            repeat
        hide text
        show text "{color=#ffc0cb}*slurp*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 1.5 yalign -0.3
            repeat
        with dissolve
        kn "keep going! don't stop, asami!"
        show ctc
        pause
        hide ctc
        "you watch as asami begins rubbing herself furiously through her clothes."
        asa "*mmgh!*"
        kn "yes!"
        kn "oh... oh spirits..."
        kn "I'm... i think i'm... i'm actually gonna..."
        kn "nngh... mghh... ahhh..."
        asa "*mmgh!* *mmmmghhg!* *mmh!!*"
        kn "ahhhh.... {size=+5}ahhh...."
        hide bfbb
        show bfbb bfbb14a
        hide text
        kn "{size=+10}aahahhhhhh!!!!!" with hpunch
        asa "{size=+10}*uunnghh!!!!!*" with hpunch
        show ctc
        pause
        hide ctc
        show bfbb bfbb16a with dissolve
        asa "oh... my... spirits... i..."
        asa "we..."
        asa "that... was..."
        show bfbb bfbb16 with dissolve
        kn "i... i think i..."
        tn "you just made korra cream herself, asami."
        asa "....i did...."
        tn "and korra, sucking your big, perky, round boobs made asami cream."
        kn "did... did you really...??"
        tn "well done, both of you."
        kn "can... can i sit..."
        tn "i'll leave you two to... talk."
        asa "what... the..."
        asa "...fuck..."
        show ctc
        pause
        hide ctc
        scene black with dissolve
        "content with how things turned out, you head to your room."
        $ k_a_titsuck = 2
        $ korra_moral -=2
        $ korra_resist -=1
        "korra's {b}morality{/b} lowered."
        "korra's {b}resistance{/b} lowered."
        jump bk4_next

    if k_a_titsuck ==2:
        hide screen bk4_money_date
        if b4_daytime:
            scene expression "bk4/backgrounds/korra_room_day.jpg":
                ypos 0
        else:
            scene expression "bk4/backgrounds/korra_room_night.jpg":
                ypos 0

        hide bfab
        hide bfad
        show bfbb bfbb00
        with Dissolve(1.5)
        asa "good girl, just like that."
        show ctc
        pause
        hide ctc
        asa "there you go..."
        kn "oh... wow..."
        asa "is that a nice view?"
        kn "so... mmmm..."
        asa "what are you thinking?"
        kn "just... just..."

        asa "what do you want?"
        kn "...."
        hide bfbb
        show bfbb bfbb05:
            linear 0.8 xpos 0
            linear 0.4 xpos 10
            repeat
        show text "{color=#ffc0cb}*suck*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2.5 yalign -0.3
            repeat
        asa "ahh...!!" with hpunch
        show ctc
        pause
        hide ctc
        kn "mmm..."
        kn "*slurp* *mmmm*"
        asa "ahh... ah..."
        show ctc
        pause
        hide ctc
        asa "o-okay... okay, korra..."
        asa "ease... easy..."
        hide bfbb
        play sound "audio/kiss.mp3"
        show bfbb bfbb06
        hide text
        kn "*pop!*" with hpunch
        kn "*ahh*..."
        kn "sor... sorry, asami..."
        asa "mm, that was nice."
        asa "but i think that was-"
        tn "again."
        asa "...what?"
        kn "huh?"
        tn "suck her tits. again."
        asa "tenzin, i don't think..."
        tn "shut up, asami."
        tn "you know what? no. beg for it."
        kn "...?"
        asa "i..."
        asa "...."
        asa "korra..."
        asa "...please suck my tits some more."
        kn "...umm..."
        kn "...really?"
        kn "i... i can?"
        asa "...please."
        asa "i want you... to slobber... on my big breasts..."
        asa "with your pretty face... and lips..."
        asa "slobber on my nip-"
        hide bfbb
        show bfbb bfbb05a:
            linear 0.6 xpos 0
            linear 0.3 xpos 10
            repeat
        hide text
        show text "{color=#ffc0cb}*suck*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2 yalign -0.3
            repeat
        kn "mmmmmm!!!"
        show ctc
        pause
        hide ctc
        asa "ahh... fuck...."

        asa "easy korra... fuck... that's... that's too hard..."
        kn "mmgh! mgh! mmmm!!!"
        asa "slow... slow... ahh... down!"
        show ctc
        pause
        hide ctc
        menu:
            "a little more":
                show ctc
                pause
                hide ctc
            "switch":
                pass

        tn "alright, enough."
        hide bfbb
        show bfbb bfbb05b:
            linear 0.4 xpos 0
            linear 0.2 xpos 10
            repeat
        hide text
        show text "{color=#ffc0cb}*suck*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 1.5 yalign -0.3
            repeat
        kn "mmmh.... mmm...."
        tn "...i said enough, korra."
        asa "ahh... ah... korra... kor... korra!"
        kn "mm! mmmm!!! mmmmmmhghg!!!!"
        show ctc
        pause
        hide ctc
        asa "stop it!!!" with hpunch
        hide bfbb
        play sound "audio/kiss.mp3"
        show bfbb bfbb06
        with dissolve
        hide text
        kn "oh!"
        kn "um... sorry."
        tn "that's perfectly fine."
        asa "{size=-6}my... my nipples..."
        tn "now i think you should switch roles."
        kn "oh?! really?!"
        asa "umm... what?"
        asa "you can't be serious."
        tn "look at my face, girl."
        asa "...."
        tn "korra: stand. Asami: kneel."
        show bfbb bfbb10
        with Dissolve(1)
        asa "{size=-4}sigh..."
        show ctc
        pause
        hide ctc
        asa "{size=-4}okay..."
        kn "....."
        kn "(do it, do it, do it...)"
        asa "....."
        asa "guess i'll just... dive in..."
        asa "........"
        hide bfbb
        show bfbb bfbb15a:
            linear 0.8 xpos 10
            linear 0.4 xpos 0
            repeat
        hide text
        show text "{color=#ffc0cb}*slurp*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2.5 yalign -0.3
            repeat
        asa "*suck* *suck*"
        show ctc
        pause
        hide ctc
        kn "nnghh...."
        kn "oh, spirits, yes..."
        asa "....*suck* *suck*"
        kn "ahhh... yes, asami... suck on my nipples... harder..."
        show bfbb bfbb15b1:
            linear 0.6 xpos 10
            linear 0.3 xpos 0
            repeat
        hide text
        show text "{color=#ffc0cb}*slurp*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 2 yalign -0.3
            repeat
        kn "ahhh... yesss!!!"
        show ctc
        pause
        hide ctc
        kn "suck my fat tits, asami!!"
        asa "*slurp!* *slurp!* *suck!*"
        show ctc
        pause
        hide ctc
        hide bfbb
        hide text
        show bfbb bfbb16
        with dissolve
        asa "*pant* *pant*"
        asa "oh my spirits... this is... this is so hot..."
        show ctc
        pause
        hide ctc
        kn "don't stop!"
        hide bfbb
        show bfbb bfbb15c1:
            linear 0.4 xpos 10
            linear 0.2 xpos 0
            repeat
        hide text
        show text "{color=#ffc0cb}*slurp*":
            rotate -25
            xalign 0.7 yalign 0.5
            linear 1.5 yalign -0.3
            repeat
        with dissolve
        kn "keep going! don't stop, asami!"
        show ctc
        pause
        hide ctc
        "you watch as asami begins rubbing herself furiously through her clothes."
        asa "*mmgh!*"
        kn "yes!"
        kn "oh... oh spirits..."
        kn "I'm... i think i'm... i'm actually gonna..."
        kn "nngh... mghh... ahhh..."
        asa "*mmgh!* *mmmmghhg!* *mmh!!*"
        kn "ahhhh.... {size=+5}ahhh...."
        hide bfbb
        show bfbb bfbb14a
        hide text
        kn "{size=+10}aahahhhhhh!!!!!" with hpunch
        asa "{size=+10}*uunnghh!!!!!*" with hpunch
        show ctc
        pause
        hide ctc
        show bfbb bfbb16a with dissolve
        asa "oh... my... spirits... i..."
        asa "we..."
        asa "that... was..."
        show bfbb bfbb16 with dissolve
        kn "i... i think i..."
        tn "you just made korra cream herself, asami."
        asa "....i did...."
        tn "and korra, sucking your big, perky, juicy boobs made asami cream."
        kn "did... did you really...??"
        tn "well done, both of you."
        kn "can... can i sit..."
        tn "i'll leave you two to... talk."
        asa "what... the..."
        asa "...fuck..."
        show ctc
        pause
        hide ctc
        scene black with dissolve
        "content with how things turned out, you head to your room."
        if korra_moral >=80:
            $ korra_moral -=1
            "korra's {b}morality{/b} lowered."
        jump bk4_next

    $ b4_daytime = False
    jump bk4_next

label korra_footjob1:

    if not korra_fj:
        if b4_daytime:
            show expression "bk4/backgrounds/korra_room_day.jpg":
                ypos 0
        else:
            show expression "bk4/backgrounds/korra_room_night.jpg":
                ypos 0
        show bfab bfab24
        with dissolve

        kn "Hey... tenzin..."
        tn "yes?"
        kn "Do you..."
        kn "...would you like to cum?"
        menu:
            "me? no, orgasms are gross":
                tn "ew, korra."
                tn "what is wrong with you?"
                tn "i'm your teacher."
                tn "that's disgusting."
                kn "...what?"
            "yes, please":

                tn "sure, i'll take one to go."
                tn "i only accept organic orgasms though."
                tn "gmo-free, gluten-free, soy-free, dairy-free orgasms."
                kn "uh..."

        tn "relax, i'm fucking with you."
        tn "but it depends."
        tn "what are my options?"
        kn "well... i can give you my tits again..."
        kn "but asami suggested... maybe..."
        kn "...my feet?"
        kn "what would you prefer?"
        menu:
            "footjob":
                pass
            "boobjob":

                jump korra_boobjob2

        tn "i'm sure you've got cute, capable feet and toes..."
        tn "let's see if you can make me nut with them."
        tn "That sounds nice!"
        kn "um... okay."
        show bfab bfab25 with dissolve
        kn "....I'll go change..."
    else:

        tn "i'm going to fuck your feet, korra."
        show bfab bfab25 with dissolve
        kn "oh."
        kn "umm..."
        kn "...okay?"
        hide bfab with dissolve

    hide bfab with dissolve
    show bfab bfab18 with Dissolve(1.5)
    kn "Just so my clothes won't be covered in your... cum."
    kn "I mean... you do produce kind of a lot."
    tn "you know it."
    kn "so..."
    kn "how do we..."
    kn "i mean..."
    tn "shut up and get on the bed."
    show bfab bfab17 with dissolve
    kn "....."
    tn "you want my load, right?"
    show bfab bfab18 with dissolve
    kn "....."
    kn "yes..."
    tn "then get on the bed."
    kn "......"

    hide expression "bk4/backgrounds/korra_room_day.jpg"
    hide expression "bk4/backgrounds/korra_room_night.jpg"
    show expression "bk4/backgrounds/korra_room_bed.jpg":
        ypos 0
    hide bfab
    show bfaw bfaw01
    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    b4_tn "I can see the wisdom in getting changed."
    tn "i'm already feeling... worked up."
    tn "today's load will be a big one."
    kn "oh..."
    b4_tn "Okay, let's see some soles!"
    show bfaw bfaw02 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    b4_tn "That's what I'm talking about!"
    kn "Really, it's just feet..."
    kn "I honestly don't understand how you can get your kicks out of this..."
    tn "was that a pun?"
    kn "...no?"
    b4_tn "It's become sort of a tradition really?"
    kn "Tradition?!"
    show ctc
    pause
    hide ctc
    show bfaw bfaw03 with dissolve
    b4_tn "Don't worry about it."
    tn "Just press those pretty little feet against my dick."
    tn "they're clean, right?"
    show expression "bk4/korra/footjob/face_angry.png" with hpunch
    kn "Of course they're clean!"
    kn "I take good care of my body!"
    b4_tn "Noted."
    hide expression "bk4/korra/footjob/face_angry.png" with Dissolve(1.5)
    show bfaw bfaw04 with Dissolve(1.5)
    tn "mmm...."
    tn "warm..."
    show ctc
    pause
    hide ctc
    b4_tn "That's it..."
    b4_tn "Just move them up and down."
    kn "...."
    show ctc
    pause
    hide ctc

    show bfaw bfaw04a
    show bfaw_footjob1:
        linear 0.8 xpos 5
        linear 0.4 xpos 0
        repeat

    kn "Like this?"
    show ctc
    $ renpy.pause()
    hide ctc
    tn "oh, yeah..."
    kn "Sooo... Pema does this... foot-stuff... for you, too?"
    b4_tn "i don't think so..."
    kn "Oh."
    b4_tn "Don't worry, you're doing great."
    show ctc
    pause
    hide ctc
    b4_tn "Hmmm... I don't think I can cum from this alone."
    kn "am... am i not doing it right?"
    tn "ehhh...."
    b4_tn "...hold on a minute."

    hide bfaw_footjob1

    show bfaw bfaw04
    show bfaw bfaw07 with Dissolve(1.5)
    kn "Good, my legs started getting tired."
    kn "that was actually a serious workout."
    show ctc
    pause
    hide ctc
    b4_tn "Can you still raise them for a second?"

    show bfaw bfaw05
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    b4_tn "Okay, now stretch them out."
    tn "I'll hold your feet at the heels and sandwich my dick in-between."
    show bfaw bfaw06a with Dissolve(1.5)
    kn "uh... okay..."
    show ctc
    pause
    hide ctc
    kn "Now, what?"
    b4_tn "i'm gonna use these lovely feet of yours like a pair of tits!"
    b4_tn "You can just sit back and be pretty!"
    hide bfaw
    show bfaw bfaw06:
        xpos 10
        linear 0.6 xpos 0
        linear 0.2 xpos 10
        repeat
    kn "oh!"
    show ctc
    pause
    hide ctc
    kn "ummm..."
    kn "well, at least I can relax my legs this way...."
    show ctc
    pause
    hide ctc
    b4_tn "Any preference where I aim?"
    kn "Out of the window would be nice."
    b4_tn "You know I can't do that."
    tn "It'd be a waste!"

    menu:
        "cum on feet":
            b4_tn "I'll plaster your soles with my cum!!"
            b4_tn "Bend those knees!"
            hide bfaw
            show bfaw bfaw05
            with Dissolve(1.5)
            b4_tx "Aaaaand..."
            play sound "audio/splurt2.ogg"
            show bfaw_spermshot
            show expression "bk4/korra/footjob/x_spermout1.png"
            with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfaw_spermshot
            show expression "bk4/korra/footjob/x_spermout2.png"
            with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfaw_spermshot
            show expression "bk4/korra/footjob/x_spermout3.png"
            with hpunch
            $ renpy.pause()
            kn "Well, at least you didn't get my face and hair all sticky."
            b4_tn "...this time..."
        "cum like this":


            b4_tx "Can't... hold it! It's gonna blow!"
            kn "Wait! Don't come on my-"
            hide bfaw
            show bfaw bfaw06a
            play sound "audio/splurt2.ogg"
            show bfaw_spermshot2
            show expression "bk4/korra/footjob/spermout1.png"
            with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfaw_spermshot2
            show expression "bk4/korra/footjob/spermout2.png"
            with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfaw_spermshot2
            show expression "bk4/korra/footjob/spermout3.png"
            with hpunch
            $ renpy.pause()

            show bfaw bfaw07 with dissolve
            kn "....face."
            menu:
                "my bad":
                    b4_tn "sorry, korra... that last stroke got me by surprise."
                    b4_ta "Your feet are too sexy!"
                    ta "So, it's actually your fault!"
                    b4_tn "But I'll try and be more careful in the future."
                "get used to it":

                    tn "that's going to happen."
                    tn "...a lot."
                    tn "expect facials when i feel like giving them to you."
                    kn "i... can i refuse?"
                    tn "no."

    show ctc
    pause
    hide ctc
    kn "i... um... can i... clean up?"
    tn "you should. you smell like semen."
    kn "but... you did that..."
    tn "no... {i}you{/i} did that."
    tn "go rinse off, footslut."
    kn "i... i'm not..."
    kn "....okay...."
    show ctc
    pause
    hide ctc
    $ korra_fj = True
    scene black with dissolve
    "satisfied, you head back to your room and rest."
    jump bk4_next


label kyoshi_pussyfan1:
    $ kyoshi_puss_fan = True

    hide screen bk4_money_date
    stop music
    play music "audio/Unwritten Return.mp3"

























    scene black

    show expression "bk4/worldrooms/bg_dreamscape_1.jpg" with Dissolve(1.5)


    show bfay bfay00x:

        xpos -500

        alpha 0.0

        linear 3.0 alpha 0.6 xpos 0

    kyo "Hello, avatar..."

    b4_ya "Awwwh shit... "

    b4_ya "It's {b}you{/b} again."

    b4_ya "Sorry but, last time we met was not a fun time."

    b4_ya "I'm sure there's important stuff that I need to do for vague nonsensical reasons but... no."

    b4_ya "It's not going to happen."

    b4_ya "Find youself someone else to poke a bear, split a snake, or whatever else you have in mind. "



    hide bfay

    show bfay bfay01x at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)

    kyo "Don't worry, this is not one of those dreams."

    b4_ya "I don't believe you."

    kyo "No, really."
    kyo "This is a perfectly normal dream."

    b4_ya "Hah!! I got you there!" with hpunch

    b4_ya "My dreams are never normal!"

    kyo "Oh... how so?"

    b4_yn "Well for one, the females in my dreams are very rarely wearing... well, anything."



    show bfay bfay04x with Dissolve(1.5)

    kyo "I see..."

    kyo "I should've known that."

    b4_yn "Hmmm... that's a lot better."

    b4_yn "But if this really was my dream why aren't you spreading your legs?"



    hide bfay

    show bfay bfay05x:

        ypos 300

        linear 5.0 ypos 50

    with Dissolve(3.0)

    b4_yn "Ohhhh, yeah!"
    b4_yn "That's a lot better."

    b4_yn "I love that shade of pink!"

    b4_yn "Can't have a dream with a girl where she isn't spreading her legs for you."
    b4_yn "That's just... like... logical!"

    b4_ya "i mean, sure, there's the ones where you actually get to see the bird box monsters instead... Those aren't fun."

    b4_ya "Why do I keep having those dreams?!"

    b4_ya "And sometimes it's just another sleepless night..."
    b4_ya "the hunt is on..."
    b4_yn "looking for anything.. to fill the void.... Make me feel alive.."

    kyo "do you need a hug?"
    b4_yn "...yes."

    b4_yn "Anyway..."
    b4_yn "I gotta admit, this is slowly starting to feel a lot more than my normal dreams."



    b4_yn "Hey, do you still have that fan?"



    show bfay bfay06x with Dissolve(1.5)

    kyo "Certainly."
    kyo "This is a dream, isn't it?"

    b4_yn "Move it up and down."



    show bfay bfay12x with dissolve

    b4_yn "That... is {i}fan{/i}-tastic... "

    b4_yn "I love a girl who can do tricks."



    show bfay bfay05x with Dissolve(1.5)

    kyo "Soooo... have you already discovered something more about those snake girls?"

    b4_yn "Meh, apparently one of them blames me for something I didn't do...?"
    b4_yn "Typical."

    b4_yn "Show me something else!"



    show bfay bfay07x at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)

    b4_yn "Gaping... a classic!"
    b4_yn "But I was thinking something more along the lines of using your fan again."



    show bfay bfay08x with Dissolve(1.5)

    kyo "Hnnng... like this?"
    kyo "Shoving it up my pussy?"

    kyo "You like seeing me degrade myself by inserting miscellaneous things in my vagina?"

    b4_yn "...."

    b4_yn "...yes."

    b4_yn "Come on, that's not the limit of how far it can go inside!"

    b4_yn "Entertain me!"



    show bfay bfay09x

    kyo "What... hnnng... what do you think they want of you?"

    b4_yn "Fuck yeah... shove that thing up your cunt, you fucking slut..."

    $ renpy.pause()

    b4_yn "...Eh what?"
    b4_yn "Did you ask me something?"

    kyo "Them snake... hnn... girls..."
    kyo "What do they want?"

    b4_yn "One seemed reasonable, but the other looked at me like I was a hot looking single mom."

    kyo "That doesn't make any sense?"

    b4_yn "Sure it does. You want to tap it, but at what cost?"



    hide bfay

    show bfay bfay10x with Dissolve(1.5)

    kyo "Soooo... you really don't know a thing about anything, do you?"

    b4_yn "Seems to be the story of my life."

    b4_yn "But from where I'm standing things aren't looking so bad right now."

    b4_yn "I only have this airbending stuff to master, get rid of some rowdy spirits in my own time and I'm done with all of this."

    b4_yn "Oh that reminds me..."
    b4_yn "I still need to come up with some sort of thing to make me rich when I return to my own time."

    b4_yn "Airbending is problematic right now, but I'm sure it'll work out."

    kyo "Maybe things would've worked out a lot faster if you hadn't been so hardheaded and just picked Korra."

    b4_yn "Gimme a break, you're the figment of my imagination!"
    b4_yn "you should be on my side!"

    b4_yn "Say... are you just going to leave it hanging out like that?"

    kyo "Hmmmm... I was thinking about showing you one last trick before I leave."

    b4_ya "Ah crap, is it already almost morning?"
    b4_yn "I hate when that happens."

    b4_ya "You close your eyes for a minute, and when you open them again it's already morning."

    b4_yn "Well, let's see it before the alarm clock goes off."



    show bfay bfay11x at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.5)

    b4_yn "Oooh!! You opened it without using your hands!"

    b4_yn "That's like the most amazing thing I've ever seen in my life!"

    kyo "I'm not done... yet."

    show bfay bfay13x:

        linear 0.6 ypos -4

        linear 0.6 ypos 4

        repeat

    show bfay_fanfan:

        linear 0.6 ypos -20

        linear 0.6 ypos 20

        repeat

    $ renpy.pause()

    b4_yn "*clap! clap! clap!* "

    b4_yn "Now that takes skill!"

    b4_yn "You have excellent pussy muscle controle!"

    b4_yn "Man... That's so silly... I'm 100 percent convinced this is a real dream now."

    b4_yn "Gotta be honest, I thought this was just an elaborate trick to get me into another one of those horrible spirit mazes."

    b4_yn "I'd suck a dude before doing that... which means I'm {b}not{/b} doing that again."

    b4_yn "i mean getting stuck in a spirit maze, not that part about sucking a... nevermind."

    hide bfay

    hide bfay_fanfan

    show bfay bfay05x with Dissolve(1.5)

    menu:
        b4_yn "Can you.."
        "Slide your fan up and down again.":



            show bfay bfay12x with dissolve

            $ renpy.pause()
        "Shove that fan in your pussy.":


            show bfay bfay09x

            $ renpy.pause()
        "Spread those lips.":


            show bfay bfay07x

            $ renpy.pause()
        "Wave some cool air towards me.":


            hide bfay

            show bfay bfay13x

            show bfay_fanfan:

                linear 0.6 ypos -20

                linear 0.6 ypos 20

                repeat

            $ renpy.pause()

            hide bfay_fanfan







    hide bfay

    show bfay bfay04x

    with Dissolve(1.5)

    b4_yn "Well, now that I'm convinced it's safe it's time to stick my dick in... finally, right?"

    kyo "It's not time for that yet."





    show expression "bk4/worldrooms/bg_dreamscape_1.jpg" as temp_image:

        alpha 0.0

        linear 6.0 alpha 1.0

    kyo "Thanks avatar."
    kyo "I'm happy to see things are progressing."
    kyo "Even if slowly."

    b4_ya "Hey! Where are you going!?"

    b4_ya "Come back!"

    b4_ya "We aren't done here!"



    scene black with Dissolve(1.5)

    show expression "bk4/backgrounds/tenzin_room_day.jpg":

        ypos 0

    with Dissolve(1.2)

    show bfae ikki01

    ikki "Dad! Dad!"

    b4_tn "Ehh... wahzthat?!"

    ikki "You've been out for a day!"
    tn "i have?"
    ikki "yeah, korra carried you here."
    ikki "mom wanted me to watch to see if you woke up!"
    ikki "and you did!"
    tn "...that's weird."
    ikki "meditation must be hard!"
    tn "i know i am..."
    ikki "what?"
    tn "nothing, go away."
    ikki "okay!"

    hide bfae ikki01 with Dissolve(1.5)
    jump bk4_next

    "test"

    "test"

    "test"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
