

image holo_crab_trap:
    "misc/holo8.jpg"
    0.2
    "misc/holo9.jpg"
    0.2
    "misc/holo10.jpg"
    0.2
    "misc/holo11.jpg"
    0.2
    "misc/holo7.jpg"
    1.5
    "misc/holo8.jpg"
    0.2
    "misc/holo9.jpg"
    0.2
    "misc/holo10.jpg"
    0.2
    "misc/holo11.jpg"
    0.2
    "misc/holo7.jpg"
    1.5
    repeat


init:
    $ slavegirl = Character("slave girl", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ dl = Character("dai lee agent", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ lf = Character("long feng", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ss = Character("shady girl", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ k3 = Character("Katara", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)

label worldmap3:
    stop music fadeout 5
    play music "audio/(Orchestral) Playful Tension by Shadow16nh.mp3"
    $ yn = Character("[povname]", color="#000000", image = "you_nomask", show_side_image = Image("images/p_fr_sidebox_neutral.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yna = Character("[povname]", color="#000000", image = "you_angry", show_side_image = Image("images/p_fr_sidebox_angry.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ ync = Character("[povname]", color="#000000", image = "you_confused", show_side_image = Image("images/p_fr_sidebox_confused.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yns = Character("[povname]", color="#000000", show_side_image = Image("images/p_fr_sidebox.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ya = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), "p_fr_sidebox_angry.png",
        (0, 0), "p_fr_sidebox_mask.png",),
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ y = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), "p_fr_sidebox_neutral.png",
        (0, 0), "p_fr_sidebox_mask.png",),
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ yc = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), "p_fr_sidebox_confused.png",
        (0, 0), "p_fr_sidebox_mask.png",),
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ym = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), "p_fr_sidebox.png",
        (0, 0), "p_fr_sidebox_mask.png",),
        window_left_padding=220, show_two_window=True, who_xpos=36)

    scene light with dissolve
    with sshake
    "Your spirit floats freely for a moment before returning, abruptly, to your body."
    yna "ungh."
    yn "......."
    yns "damn it feels good to be a gangsta."
    show pgfull with dissolve
    s "what?"
    yns "i'm back in my body again. i'm pretty excited about it."
    yns "can't you tell?"
    s "you look.... as though you are bereft of bowel movements."
    yn "ah, you don't know anything."
    yn "anyway, you said we were going to the earth kingdom?"
    s "that is correct."
    s "you will meet an incredibly strong earthbender: toph."
    s "she is perhaps the most powerful of all time."
    yn "awesome."
    yn "oh, hey, where have you been?"
    yn "the whole time i was in the fire nation.... why didn't you come find me?"
    s "i was.... delayed."
    yn "by what?"
    s "....it is not yet time for you to know."
    yna "that's bollocks."
    s "you will know soon enough."
    s "but for now, you must focus."
    s "you must master earthbending."
    yn "ugh, fine. take me to wherever."
    scene black
    scene worldmap_01 with dissolve
    show pgfull with dissolve
    s "you must go to the earth kingdom, avatar."
    yn "where?"
    s "the earth kingdom."
    yn "where?"
    s "....the earth kingdom."
    yns "where?"
    s "you are being difficult."
    yn "oh no, am i making your life hard?"
    yna "because i have {i}no idea{/i} what that's like."
    s "....."
    s "go to the earth kingdom and be silent."
    yn "pff. fine."

    hide pgfull with dissolve
    jump worldmap3_call

label worldmap3_call:
    call screen worldmap_03

label earth_cont:

    scene black with dissolve

    $ jd = Character("joo dee", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ t = Character("?????", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)

    scene black with dissolve

    stop music fadeout 5
    play music "audio/jangles.mp3"
    show expression "ebackgrounds/basingse_city_1.jpg"

    show expression "bk3/train/long_rails.png":
        xpos -1000
        linear 20 xpos 0
        repeat
    show totr totr100:
        xpos 0
        linear 120 xpos -800

    show expression "bk3/train/rails_bar.png"

    with Dissolve(2.0)
    $ renpy.pause(2.0)
    show bk3_scroll5:
        xpos 0.15 ypos -0.02
    show text "{size=+25}ba sing se":
        xpos 0.5 ypos 0.12
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    show ctc with dissolve
    pause
    hide ctc

    show ctc with dissolve
    pause
    hide ctc
    hide bk3_scroll5
    hide text
    with dissolve
    yn "this... this is incredible."
    s "welcome to ba sing se, avatar."
    yn "i've heard of this city, but.... this is {i}massive{/i}."
    show ctc
    pause
    hide ctc
    yn "where am i?"

    show pgfull with dissolve
    s "ba sing- oh don't start that again."
    yn "no, i mean, where's the body i'm taking over?"
    s "ah. right over there."
    hide pgfull with dissolve

    yn "i'm that guy?"
    yn "...."
    yn "that sucks."
    s "no, you're on the train."
    yn "oh."
    yn "so who is it this time?"
    s "i think you'll recognize him."
    yn "..........."
    s "is something wrong?"
    yn "i'm waiting for that snake thing to attack us."
    s "no need to worry, i've taken precautions."
    s "now, don't forget, you {i}must{/i} master earthbending."
    yn "i got it."
    yn "i'm practically a pro at this now."
    s "very well."
    s "you'll need to take a deep breath."
    yn "just warn me before-"
    play sound "audio/whoosh.wav"
    hide expression "bk3/train/rails_bar.png"
    hide expression "bk3/train/long_rails.png"

    hide totr
    show expression "bk3/train/train_station_1.png":
        xpos -2000

    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat

    with sshake
    ya "ah! fuck!"
    ym "ohh...."
    ym "i recognize this body."
    ym "ah.... it feels like coming home."
    y "oh, hey, i'm on a train."
    y "never been on a train before."
    ym "choo choooooo!!"
    yc "wait, what the hell am i holding?"
    play sound "audio/paperruffle.mp3"
    show expression "bk3/train/appa_poster.png" with dissolve
    y "the fuck is this?"
    show ctc
    pause
    hide ctc
    y "looks like a diseased bowling ball."
    y "okay.... posters on the train walls.... guess i was putting these up?"
    show ctc
    pause
    hide ctc
    y "i can figure this out."
    hide expression "bk3/train/appa_poster.png" with dissolve
    if thief >= zuko:
        y "this is better than waking up under the boot of that psychotic fire chick."
        y "aw, i'm gonna miss her."
    if azula_chosen:
        y "Man, I wish I was back in the city with azula."
        y "It really sucks how I had to leave her that way."
    if mai_chosen:
        y "Man, I wish I was back on ember island with Mai."
        y "It really sucks how I had to leave her that way."
    if zuko_end:
        y "man, i wish i was still with azula and mai."
        y "i really sucks how i had to leave them that way."

    y "....and this is definitely better than hoth or wherever that fucking iceberg village was."
    y "this is pretty nice, actually."
    y "....which means i can expect a meteor to hit or something."
    y "........"
    y "well, until crap hits the fan, i'm gonna enjoy it."
    y "now, all i've got to do is figure out where i'm going."
    y "oh, looks like the station is coming up."
    show expression "bk3/train/train_station_1.png":

        linear 10 xpos 0
    $ renpy.pause(8.2, hard=True)

    hide totr
    show expression "bk3/train/train_station_1.png":
        xpos 0
    show totr totr06
    with vshake
    "with a light jolt, the train comes to a halt."
    y "sweet. time to find some ass!"
    yc "do i have an addiction?"
    yc "...."
    y "nah, you can't be addicted to sex."
    y "okay world, here i come!"

    hide totr

    show toji toji01
    with Dissolve(1.5)
    jd "hello, my name is joo dee."
    menu:
        "be normal":
            y "hello, civilian woman."
            y "(...i'm not good at things.)"
        "flirt terribly":

            y "Hey, sugar tits."
            show toji_surprise with dissolve
            jd "oh!"
    jd "...."
    show toji_smile
    hide toji_surprise
    show toji_blush
    with dissolve
    jd "how... colorful!"
    y "huh. not the response i was expecting."
    show toji toji02
    hide toji_smile
    hide toji_blush
    with dissolve
    jd "i have been given the great honor of showing the avatar around ba sing se."
    jd "welcome to our wonderful city."
    y "great, thanks."
    y "but... uh..."
    y "do you.... know what i'm doing here?"
    jd "i'm sorry?"
    y "like, do i have a thing to get to? or am i in the middle of something, maybe?"
    jd "do you have amnesia?"
    ya "{size=+5}no!"
    show toji_surprise with dissolve
    jd "...."
    y "sorry. sorry i yelled."
    y "it's an emotional subject."
    y "I just need a bit of a reminder."
    hide toji_surprise
    show toji_smile
    with dissolve
    jd "well, your friends already got off the train."
    jd "i directed them to your new house."
    hide toji_smile with dissolve
    y "i have a house? nice."
    jd "yes. and we will begin the tour now."
    y "...now? well, i don't-"
    show toji toji01
    show toji_smile
    with dissolve
    jd "let's get started!"
    y "i... okay."
    y "i guess i don't have any say here. that's fine."
    jd "wonderful!"
    y "...."
    y "oh, wait. i've got all these posters."
    y "i think i was handing them out?"
    y "they seem to have a fuzzy marshmallow on them."
    show toji toji03
    with dissolve
    jd "i'll take care of those for you. do not worry."
    jd "you are in ba sing se, where everyone is safe and taken care of."
    show ctc
    pause
    hide ctc
    menu:
        "you seem... weird...":
            y "...has anyone ever told you that you're a little.... odd?"
            hide toji_smile with dissolve
            jd "please let me help you with your posters."
            jd "....."
            y "oh, fine. here you go."
        "here you go...":
            "you hand joo dee the posters."
            hide toji_smile with dissolve

    jd "wonderful!"
    play sound "audio/paperruffle.mp3"
    show toji toji02 with dissolve
    "with a quick flurry of hands, your posters disappear into joo dee's sleeves."
    jd "now, let's begin our tour!"

    scene black
    scene basingse_city_1
    show basingse_locations
    show toji toji01:
        xzoom -1.0
    with dissolve
    show toji toji01 at Move((0,0,0,0),(-0.4,0,-0.4,0),0.9):
        xzoom -1.0
    "you follow joo dee as she takes you around the city."
    jd "over here is the lower ring."
    show basingse_market with dissolve
    jd "in it you can find the market - our artisans and craftsmen are here."
    jd "i have also heard that there are many.... carnival-like activities!"
    y "such as?"
    hide basingse_market with dissolve
    jd "oh, i wouldn't know about that."
    show basingse_arena with dissolve
    jd "there is also an arena for the more... adventurous... risk-takers."
    y "what kind of risks?"
    jd "oh, i wouldn't-"
    y "you wouldn't know. right."
    hide basingse_arena with dissolve
    jd "it's so quaint and lively."
    y "well... it feels small. and shitty."
    show toji_smile:
        xzoom -1.0
    with dissolve
    jd "yes, it is truly wonderful here in ba sing se."
    y "that's... not what i said, but okay."
    hide toji toji01
    hide toji_smile
    with dissolve

    show toji toji02 with dissolve
    jd "now this is the middle ring of ba sing se."
    show basingse_jasmine with dissolve
    jd "home of the jasmine dragon!"
    jd "truly the finest tea shop in the city."
    hide basingse_jasmine with dissolve
    show basingse_fountain with dissolve
    jd "in the middle ring, you can also find our most magnificent fountain!"
    jd "the fountain commemorates our wonderful king who is wonderful at keeping our wonderful city wonderful and safe."
    y "......."
    y "you said \"wonderful\" a billion times in that sentence. do you know any other adjectives?"
    hide basingse_fountain with dissolve
    show toji_smile with dissolve
    jd "yes, truly a wonderful and safe city!"
    y "okay, are you messing with me? is this a prank? are you deaf? am i deaf?"
    hide toji_smile with dissolve
    show basingse_home with dissolve
    jd "the upper ring is home to-"
    y "am i a ghost? what is happening?"
    jd "-home to our most important citizens. your house is not too far from here."
    y "....and i bet it's wonderful."
    jd "it is!"
    hide basingse_home with dissolve
    y "...."
    y "oh, hey, what's inside that wall? who are those mean looking guys?"
    hide toji toji02 with dissolve
    show toji toji01:
        xzoom -1.0
    show basingse_palace
    with dissolve
    jd "inside is the royal palace."
    show guard_body_1 with dissolve
    jd "and those men are the dai lee, the cultural authority of ba sing se."
    jd "they are the guardians of all our traditions."
    y "huh."
    hide guard_body_1
    hide basingse_palace
    with dissolve
    jd "ah, and here we are."
    hide toji toji01
    scene basingse_home_1
    with Dissolve(1.0)
    show ctc
    pause
    hide ctc
    show toji toji01 with dissolve
    jd "welcome to your new home."
    y "alright, i gotta admit... not bad."
    show toji toji04 with dissolve
    jd "ah, what's this?"
    jd "well! it looks like your request to visit the earth king-"
    y "what?"
    show toji toji02 with dissolve
    jd "your friends requested an audience with the earth king. did you not know?"
    y "oh. yeah. no, i totally knew."
    jd "is it your amnesia again?"
    ya "{size=+5}i don't have amne-"
    show toji toji04
    show toji_smile
    with dissolve
    jd "as i was saying... your request to visit the earth king is being processed."
    hide toji_smile with dissolve
    jd "you will be informed of the time and date eventually, so please be patient."
    show toji toji01 with dissolve
    menu:
        "please go away":
            y "sure. look, i don't mean to be rude, but can you give me a moment of peace?"
            y "i need some time to get my bearings."
        "step off bitch":
            y "so.... can you fuck off?"

    y "or at least show me your tits."
    y "i am partial to boobs."
    show toji_smile with dissolve
    jd "thank you for that compliment, avatar!"
    jd "let's go inside."
    y "....okay...."
    hide basingse_home_1
    scene basingse_home_2
    hide toji toji01
    hide toji_smile
    with dissolve
    y "huh, nice."
    show toji toji01
    show toji_smile
    with dissolve
    jd "hello!"
    y "ah!"
    jd "this is the inside!"
    ya "i know, i'm looking at it!"
    ya "why are you still here?"
    show toji toji02
    hide toji_smile
    show toji_smile
    with dissolve
    jd "leaving you alone would make me a bad host!"
    ya "how long are you going to bother me?"
    jd "i will be your guide for as long as you are in ba sing se."
    menu:
        "wild rant":
            $ joodee_scare = 1
            y "*sigh* i need a bath."
            hide toji_smile with dissolve
            jd "i-"
            y "what, you think i'm not a man because i like baths?"
            jd "well-"
            ya "just because i like bubbles and effervescent salts?"
            show toji_surprise with dissolve
            jd "i didn't-"
            ya "they sizzle!"
            jd "....."
            jd "i-"
            y "oh, excuuuuuuuse me-"
        "use waterbending to make her wet":

            $ joodee_scare = 2
            "you try to move the latent liquid in joo dee's body slowly out through her pussy."
            y "really? you're my guide for as long as i'm in the city?"
            jd "yes, i-"
            hide toji_smile
            show toji_blush
            with dissolve
            jd "um..."
            "you increase the lubrication of joo dee's cunt, and you can feel it widening in response."
            "...as if preparing for penetration."
            show toji toji01
            hide toji_blush
            show toji_surprise
            show toji_blush
            with dissolve
            jd "umm...."
            y "you were saying?"
            jd "i.... i...."



    hide toji_surprise
    hide toji_blush
    show toji_smile
    show toji_blush
    with dissolve
    jd "okay! have a wonderful and safe time in our wonderful and safe city!"
    jd "i'll be by later if you need anything!"
    hide toji_smile
    hide toji toji02
    hide toji toji01
    hide toji_blush
    with dissolve
    if joodee_scare ==1:
        y "heh, nothing scares 'em off like a good old fashioned bath rant."
    if joodee_scare ==2:
        y "heh, i'm gonna have fun with her later."

    y "so, this is my house, eh?"
    y "i wonder where everyone else is? i thought she said i arrived with others..."
    with flash
    t "aaahhhh!"
    y "....what the hell was that?"
    y "......."
    y "i'm here for barely five minutes and weird things are already happening."
    y "....."
    y "i'm gonna ignore it, and maybe i won't have to deal with it."
    y "yup, just gonna stand here and not get involved."
    t "aang....?"
    y "what? who's there?"
    show toi toi61 with dissolve
    t "aang?"
    y "ah, you must be the cleaning lady."
    t "i... i'm... old!!!"
    y "uuuh... yes?"
    show toi_old_sad with dissolve
    t "it's me aang! toph!"
    y "no..."
    y "nonononononono..."

    $ t = Character("toph", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)

    t "i'm sorry, but..."
    t "i heard katara talk about scrolls and potions to enlarge breasts..."
    t "and i took some of it! i woke up like this!"
    ya "why?? why would you do this to me??"
    show toi toi60
    hide toi_old_sad
    with dissolve
    t "oh, aang.... my back is bent, i can feel the arteries on my arms, and my face is sagging!"
    t "and the worst thing is...."
    show toi toi61
    show toi_old_sad
    show toi_old_tears
    with dissolve
    t "my boobs aren't sagging because they're {size=+5}{i}still{/i}{/size} too small to be affected by gravity!"
    t "take a look for yourself!"
    y "no! you stop it right there!"
    show toi_old_blink with dissolve
    y "show me what you took."
    y "from what i remember, it was scrolls to enlarge breasts, not a potion."
    show toi toi62
    show toi_old_sad
    hide toi_old_blink
    hide toi_old_tears
    with dissolve
    t "here..."
    y "this bottle says \"age up\"! all it did was make you older!"
    t "well, sorry, but as you might remember..."
    show toi toi110
    hide toi_old_sad
    with dissolve
    t "my eyesight isn't the best!!"
    y "this is.... how old are you again? i mean really?"
    show toi toi61
    with dissolve
    t "eighteen!"
    y "okay, okay, let's not panic..."
    y "wait, did you say {i}katara{/i}? is she here?"
    t "of course she's here!"
    y "so why didn't you ask the person whose potion you stole for a solution?"
    t "i didn't steal anything! i just {i}borrowed{/i} it!"
    show toi_old_sad with dissolve
    t "....and i'm afraid she'll start nagging..."
    show toki toki02:
        xzoom -1.0 xpos 150




    show toki_angry:
        xzoom -1.0 xpos 150
    show katara_lookleft:
        xzoom -1.0 xpos 150
    with moveinleft
    k3 "of course i'm going to start nagging!"
    t "oh... hi, katara...."
    k3 "you went through my things!"
    hide toki_angry
    show toki_blink:
        xzoom -1.0 xpos 150
    with dissolve
    k3 "that's what you get."
    t "i'm sorry, katara... i just wanted to feel more feminine..."
    t "how did you know i'd taken it?"
    show toki toki01:
        xzoom -1.0 xpos 150
    hide toki_blink
    with dissolve
    k3 "it was pretty hard to ignore your screaming."
    k3 "don't worry, the effect should wear off very soon."
    t "why didn't you tell me that earlier!?"
    t "i've been panicking over here!"
    show toki toki02:
        xzoom -1.0 xpos 150
    hide katara_lookleft
    show toki_angry:
        xzoom -1.0 xpos 150
    show katara_lookleft:
        xzoom -1.0 xpos 150
    with dissolve
    k3 "because maybe you needed to learn a lesson about going through other people's stuff!"
    t "why you...."
    y "wow... you... you look great, Katara!"
    show toki toki01:
        xzoom -1.0 xpos 150
    hide toki_angry
    hide katara_lookleft
    with dissolve
    k3 "thanks aang, that's nice of-"
    show toki toki04:
        xzoom -1.0 xpos 150
    show toki_surprised:
        xzoom -1.0 xpos 150
    with dissolve
    k3 "it's... it's you! i can't believe it!"
    y "...what?"
    t "what?"
    hide toki_surprised
    show toki_smile:
        xzoom -1.0 xpos 150
    with dissolve
    k3 "i don't believe it! i'd hoped, but...."
    t "you just saw him on the train, katara. what's going on?"
    t "does he look different?"
    k3 "no, he {i}looks{/i} the same, but..."
    y "wait, do you know-"
    hide toki_smile
    show toki toki03:
        xzoom -1.0 xpos 150
    show toki_smile:
        xzoom -1.0 xpos 150
    with dissolve
    k3 "how about a hug?"
    "you're a little confused, but katara gives you a big hug."
    hide toki_smile
    show toki_blink:
        xzoom -1.0 xpos 150
    with dissolve
    "as she's hugging you, she gives you a light, sultry lick up your neck before pulling away."
    show toki toki01:
        xzoom -1.0 xpos 150
    hide toki_blink
    with pflash
    k3 "i missed you."
    show blackveil with dissolve
    y "(what the hell....)"
    y "(i left her with the real aang's body when she last saw me.)"
    y "(i think she even saw me pop out of his body!)"
    y "(does she know it's me? should i tell her if she doesn't?)"
    y "(i did tell her i'd come back for her... does this count?)"
    y "(all this time-traveling stuff is making things crazy.)"
    y "(for example, i just got rid of ozai... but i bet in this time, he's still on the throne.)"

    hide blackveil with dissolve

    t "what the hell, katara?"
    t "you saw him earlier today!"
    k3 "oh... ehm... sure. i just... get... lonely."
    "just as you open your mouth to say something, katara puts her finger on your lips."
    k3 "don't worry, aang, you don't have to say anything."
    k3 "in fact, i think it's better if we don't talk about this yet."
    t "talk about what?"
    k3 "it's a secret!!"
    t "......"

    k3 "hey, aang... want another hug?"
    menu:
        "bring it":
            y "come on over."
            k3 "okay..."
        "nah i'm good, thanks":

            y "i'm set, actually."
            k3 "oh..."

    hide toi toi60
    hide toi_old_sad
    show toi toi09
    with flash
    t "what the..."
    t "...."
    show toi toi07
    with dissolve
    t "yes!"
    t "toph is {i}back{/i}!"
    y "so... you're back to normal? it didn't... reverse you too much?"
    show toi toi06
    with dissolve
    t "no, i'm an adult, and this is what i look like."
    t "i never really... developed, okay?"
    show toi toi05 with dissolve
    t "that's why i took that stupid potion in the first place."
    t "i'm done talking about it."
    show toi toi06 with dissolve
    t "and you two are being weird."
    t "i'm going to have to seperate you two if we're going to get any training done."
    y "hold on-"
    k3 "no, aang, she's right. you need to learn how to earthbend."
    k3 "i'll go see if i can find sokka, he's already off exploring."
    k3 "i'm sure you and i will.... run into each other later."
    hide toki toki01
    with dissolve
    show toi toi02 with dissolve
    t "good. now, first things first, you need to see the king."
    y "what?"
    t "you need to tell him that the fire nation will be powerless during the eclipse."
    t "and see if he can help you find appa."
    y "i... don't know what that is."
    show toi toi09 with dissolve
    t "your sky bison?"
    y "ohhhh.... so {i}that's{/i} what that thing was."
    t "what?"
    y "i was holding a poster on the train with a weird animal on it."
    y "turns out it's this \"abba\" thing."
    show toi toi04 with dissolve
    t "appa."
    y "gesundheit."
    show toi toi09 with dissolve
    t "what?"
    y "didn't you just sneeze?"
    show toi toi06 with dissolve
    t "stop messing around!"
    t "go talk to the king!"
    y "but i don't {i}care{/i}."
    show toi toi01 with dissolve
    t "listen up, twinkletoes!"
    t "i don't know if you're scared or something, but i won't train you until you talk to him."
    y "...."
    y "oh, fine."
    show toi toi04 with dissolve
    t "good."
    t "i'll see you back here later."










    $ bk3_journal = True











    show toi toi01 with dissolve
    t "now go see the king!"
    hide toi toi01 with dissolve

    $ quest1 = True
    scene black
    scene basingse_city_1
    with dissolve
    y "well, i need to go to the palace...."
    y "...but it looks like there might be some fun places around here."
    jump basingse_day1

label basingse_day1:
    if bk3_loveroute:
        jump love_basingse_day1

    stop music fadeout 1
    play music "audio/jangles.mp3"
    if not bk3_day:
        jump basingse_night1
    else:
        scene black
        scene basingse_city_1
        show screen earth_money_date
        with dissolve
        if suki_brothel and not bk3_tylee_met:
            y "you know, i don't appreciate the weather enou-"
            "a girl comes running around the corner, straight at you..."
            show toti toti02 with dissolve
            "???" "i can't believe she'd-"
            show toti toti03
            "???" "aaahhh!!"
            play sound "audio/thud.mp3"
            show toti toti04
            show toti_blink
            with sshake
            "???" "ow!"
            y "ow!"
            y "fuck!"
            "???" "owie...."
            hide toti_blink with dissolve
            "???" "hi, sorry!"
            y "wait, you look familiar..."
            show toti toti01 with dissolve
            "???" "no i don't! bye!"
            hide toti toti04 with dissolve
            $ bk3_tylee_met = True
            y "was that....."
            y "...hmm..."
        call screen basingse_map

label basingse_night1:
    if bk3_day:
        jump basingse_day1
    else:
        scene black
        scene basingse_city_1
        show background_fade_purpleish
        with dissolve
        call screen basingse_night_map

label bk3_jasmine:
    if iroh_panty_hunt ==3:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        iroh "hello again, stranger."
        y "i have your... panties."
        show toii toii05 with dissolve
        iroh "oh, my... that's wonderful news!"
        play sound "audio/win2.mp3"
        "you return iroh's panty collection."
        iroh "thank you, my friend."
        y "what about my reward?"
        show toii toii07 with dissolve
        iroh "what?"
        y "....the peephole? in the changing room?"
        show toii toii05 with dissolve
        iroh "oh, yes!"
        show toii toii01 with dissolve
        iroh "here's the key to the back rooms..."
        iroh "you'll find the changing room back there."
        iroh "there's a hole on the side of it."
        play sound "audio/win2.mp3"
        "you got the back room key!"
        iroh "see you, stranger."
        $ iroh_panty_hunt = 4
        jump basingse_day1

    if (jin_jasmine_met and toph_katara_chair >=8) or (jin_jasmine_met and ajala_says_hypno_jin):
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        with dissolve
        menu:
            "spy on jin" if iroh_panty_hunt ==4:
                if jin_hypno >=9:
                    y "i know that jin still works here sometimes..."
                    y "maybe she's in the back?"
                if not jin_sucked:
                    scene black with dissolve
                    y "okay, let's see if this will be worth my time..."
                    jump jin_sucks
                if jin_sucked:
                    scene black with dissolve
                    jump jin_sucks2

            "talk to jin" if jin_hypno <=7:
                if jin_hypno ==7:
                    if avatar_shack <=2:
                        y "hmm... i should upgrade my house and then talk to jin."

                    if avatar_shack ==3:
                        show tojn tojn20 with dissolve
                        jin "he-"
                        show tojn tojn23
                        show expression "bk3/jin/idles/fl_blush.png"
                        with dissolve
                        jin "oh!"
                        jin "how-"
                        show tojn tojn24
                        hide expression "bk3/jin/idles/fl_blush.png"
                        show expression "bk3/jin/idles/fl_blush.png"
                        show expression "bk3/jin/idles/fl_blink.png"
                        with dissolve
                        jin "hnhh... how are... ahh... ah..."
                        y "(...i may have gone overboard with the gushing pussy...)"
                        hide expression "bk3/jin/idles/fl_blink.png" with dissolve
                        jin "you... ah... look good to... ah... today...."
                        show expression "bk3/jin/idles/fl_blink.png" with dissolve
                        jin "fuu... fuck..."
                        y "[trigger]."
                        show tojn tojn20
                        show tojn_hypno_eyes
                        hide expression "bk3/jin/idles/fl_blink.png"
                        hide expression "bk3/jin/idles/fl_blush.png"
                        with dissolve
                        show ctc
                        pause
                        hide ctc
                        y "jin, your pussy will ease up on the gushing - but only enough that you can talk to me."
                        y "understand?"
                        jin "my pussy... will gush... but not so much... that i can't... talk..."
                        y "good girl."
                        y "[trigger]."
                        hide tojn_hypno_eyes
                        show tojn tojn23
                        with dissolve
                        jin "what..."
                        jin "...just happened?"
                        y "how do you feel?"
                        show tojn tojn20
                        with dissolve
                        jin "actually..."
                        jin "I feel-"
                        show tojn tojn23
                        show expression "bk3/jin/idles/fl_blush.png"
                        with dissolve
                        jin "ohh... umm..."
                        show tojn tojn25
                        hide expression "bk3/jin/idles/fl_blush.png"
                        with dissolve
                        jin "i mean, i feel... um... fine, lee."
                        jin "how are you?"
                        show tojn tojn26 with dissolve
                        jin "ahn..."
                        y "well... i was just wondering..."
                        y "would you like to date m-"
                        show tojn tojn25 with dissolve
                        jin "yes!!"
                        jin "i'd love to date you!"
                        jin "i don't believe it!"
                        jin "it's all i've thought about, lee!"
                        jin "you're so handsome... and funny..."
                        jin "even with your odd uncle."
                        jin "i wish...."
                        show tojn tojn26 with dissolve
                        jin "oh, i wish we could just live together already!"
                        y "why don't we?"
                        show tojn tojn23 with dissolve
                        jin "wh...what?"
                        y "come live with me."
                        jin "do you mean it? really?"
                        show tojn tojn20 with dissolve
                        jin "i've wanted to be with you for so long!"
                        jin "i know it's early, but..."
                        show tojn tojn26 with dissolve
                        jin "i love you, lee."
                        jin "you're such a good person, i'm so happy to give you my love."
                        jin "you really deserve it."
                        jin "you..."
                        show tojn tojn25 with dissolve
                        jin "...you have me."
                        menu:
                            "insult":
                                y "that's good... whore."
                                show tojn tojn23 with dissolve
                                jin "wha-"
                                show tojn tojn27 with ushake
                                jin "hngh... what the..."
                                jin "fu...fuck..."
                                jin "do..."
                                show tojn tojn28 with dissolve
                                jin "do that again..."
                                y "what? call you a filthy little slut?"
                                show tojn tojn27 with ushake
                                jin "oh, spirits, yes..."
                                jin "how... ahh... how are you doing this to me...?"
                                show tojn tojn28 with dissolve
                                jin "i... i love you..."
                                jin "say it..."
                                jin "say it again..."
                                y "you should take my cock, skank."
                                show tojn tojn27
                                with ushake
                                jin "ahhh... lee... ye...yes... ah..."

                                jin "let's... ah... go to..."
                                jin "ngh..."
                                jin "your... your house... lee..."
                                show tojn tojn28 with dissolve
                                jin "pl...please..."
                                y "i'll meet you there."
                                show tojn tojn25 with dissolve
                                jin "oka-"
                                y "whore."
                                show tojn tojn27 with vshake
                                jin "oh, spirits...."
                                $ jin_hypno = 8
                                scene black with dissolve
                                "you walk out into the city."
                                jump basingse_day1
                            "flatter":

                                y "that's good... beautiful."
                                show tojn tojn23 with dissolve
                                jin "wha-"
                                show tojn tojn26 with dissolve
                                jin "you're so sweet, lee."
                                jin "i-"
                                show tojn tojn27 with ushake
                                jin "ohhh..."
                                jin "what... ahh..."
                                show tojn tojn25 with dissolve
                                jin "i..."
                                jin "......."
                                show tojn tojn26 with dissolve
                                jin "i love you..."
                                show tojn tojn27 with ushake
                                jin "ahhh... lee..."
                                jin "ye...yes... ah..."
                                jin "let's... ah... go to..."
                                jin "ngh..."
                                jin "your... your house... lee..."
                                show tojn tojn28 with dissolve
                                jin "pl...please..."
                                y "i'll meet you there."
                                show tojn tojn25 with dissolve
                                jin "oka-"
                                y "love."
                                show tojn tojn27 with vshake
                                jin "oh, spirits...."
                                $ jin_hypno = 8
                                scene black with dissolve
                                "you walk out into the city."
                                jump basingse_day1

                show tojn tojn20 with dissolve
                jin "hello!"
                jump jin_jasmine_menu

                label jin_jasmine_menu:
                    scene black
                    scene jasmin_dragon_inside
                    hide tojn
                    show tojn tojn20
                    menu:
                        "iroh's missing panties" if iroh_panty_hunt ==1:
                            show iroh_slide:
                                xzoom -1.0 alpha 0.0
                            y "hey jin..."
                            jin "hello!"
                            y "is there... any chance... you took iroh's panties?"
                            show tojn tojn23 with dissolve
                            jin "his... what?"
                            y "he collects them, don't ask me why... it's a whole thing."
                            jin "he collects..."
                            show tojn tojn24
                            with dissolve
                            jin "hey! i think i'm missing..."
                            show iroh_slide:
                                parallel:
                                    alpha 0.9
                                parallel:
                                    xpos -300
                                    linear 5 xpos 1200
                            hide tojn
                            show tojn tojn24
                            $ renpy.pause(0.5, hard=True)
                            iroh "{size=-4}no...." with dissolve
                            $ renpy.pause(0.5, hard=True)
                            show tojn tojn23 with dissolve
                            jin "do you hear something?"
                            y "um... no."
                            y "and i guess... forget i said anything about the panties."
                            jin "....."
                            show tojn tojn20 with dissolve
                            jin "okay!"
                            hide iroh_slide
                            show iroh_slide:
                                parallel:
                                    alpha 0.9
                                parallel:
                                    xpos 300
                                    linear 5 xpos -1200
                            hide tojn
                            show tojn tojn20
                            $ renpy.pause(0.5, hard=True)
                            iroh "{size=-4}thank you...." with dissolve
                            $ renpy.pause(0.5, hard=True)
                            show tojn tojn23 with dissolve
                            jin "hmm?"
                            $ iroh_panty_hunt = 2
                            jump jin_jasmine_menu
                        "talk":

                            if jin_hypno ==0:
                                y "how's it going?"
                                jin "it's okay, all things considered."
                                y "what do you mean?"
                                jin "I mean it's nice of this old guy to let me stay here..."
                                show tojn tojn24 with dissolve
                                jin "even though he's a bit of a perv."
                                show tojn tojn20 with dissolve
                                jin "not like you!"
                                y "...right..."
                                jump jin_jasmine_menu
                            if jin_hypno ==1:
                                jin "hello!"
                                y "[trigger]."
                                show tojn tojn23 with dissolve
                                jin "wh-what..."
                                y "how do you feel?"
                                jin "fu...fuzzy..."
                                y "(that's a new one.)"
                                show tojn tojn20 with dissolve
                                jin "that was weird."
                                y "(guess she needs a little more hypnosis...)"
                                y "i'll check you later."
                                jin "bye!"
                                jump jin_jasmine_menu
                            if jin_hypno ==2:
                                y "hey jin, you holding up okay?"
                                jin "hey!"
                                jin "i'm fine!"
                                y "how do you feel about staying here?"
                                jin "it's... okay."
                                y "you're getting a little tired of staying with iroh."
                                show tojn tojn23 with dissolve
                                jin "i...."
                                jin "....."
                                show tojn tojn20 with dissolve
                                jin "now that you mention it, i think you're right."
                                jin "i need to start considering moving somewhere else."
                                y "nice."
                                y "good talk."
                                jin "see you around!"
                                jump jin_jasmine_menu
                            if jin_hypno ==3:
                                y "hey jin."
                                jin "hi!"
                                y "i was wondering... how do you feel about nudity?"
                                jin "that it's not a big deal."
                                jin "it's our normal state of being."
                                jin "it's really dumb to not be comfortable."
                                y "why don't you get naked now, then?"
                                jin "because i don't make the rules around here."
                                y "come on, make rules for yourself!"
                                y "who are they to tell you what to do with your body?"
                                jin "....okay!"
                                jin "you make a good point."
                                hide tojn with dissolve
                                show tojn tojn22 with dissolve
                                jin "you're right, this is better."
                                show ctc
                                pause
                                hide ctc
                                y "...why are you blushing?"
                                jin "because... this is... not something i usually do."
                                y "fair enough."
                                jin "i gotta get back to work, since i'm staying here."
                                jin "i should... probably get dressed again though."
                                hide tojn with dissolve
                                show tojn tojn20 with dissolve
                                jin "this was fun."
                                jin "see ya!"
                                jump jin_jasmine_menu
                            if jin_hypno >=4:
                                y "hey jin."
                                jin "hi there!"
                                jin "what's up?"
                                if jin_hypno ==6 and not jin_hypno6_talk:
                                    show tojn tojn25 with dissolve
                                    jin "Umm... this is embarrassing..."
                                    y "what?"
                                    jin "no, never mind..."
                                    y "is it something with Lee?"
                                    jin "well... truth be told..."
                                    show tojn tojn26 with dissolve
                                    jin "my body is acting weird around him..."
                                    y "oh? how so?"
                                    jin "it's... sort of... i'm... uh..."
                                    show tojn tojn25 with dissolve
                                    jin "my body likes him a lot."
                                    jin "i'm sort of... hot all the time."
                                    show tojn tojn26 with dissolve
                                    jin "and... er... this is awkward, but..."
                                    jin "i can really talk with you, right?"
                                    menu:
                                        "of course":
                                            y "sure, hit me."
                                            jin "i'm..."
                                            show tojn tojn25 with dissolve
                                            jin "um..."
                                            jin "wet."
                                            jin "like..."
                                            jin "really, {i}really{/i} wet."
                                            y "right now?"
                                            jin "even thinking about him, yeah."
                                            y "weird."
                                            jin "right?"
                                            jin "and when i see him, it's like..."
                                            show tojn tojn26 with dissolve
                                            jin "um... {i}gushing{/i}."
                                            jin "like... overflowing. for real."
                                            jin "my panties get completely soaked."
                                            jin "it's so, so, so embarrassing."
                                            y "huh."
                                            y "well, what are you doing about it?"
                                            show tojn tojn25 with dissolve
                                            jin "nothing. i can't do anything about it."
                                            jin "just... be super uncomfortable."
                                            jin "and..."
                                            jin "ready."
                                            y "well, that's strange."
                                            jin "yeah..."
                                            jin "so, what did you want to talk about?"
                                        "i'd rather you didn't":

                                            y "i think we should have some boundaries."
                                            show tojn tojn25 with dissolve
                                            jin "oh... okay."
                                            jin "um."
                                            jin "never mind then."
                                            jin "so, what did you want to talk about?"

                                    $ jin_hypno6_talk = True
                                    show tojn tojn20 with dissolve

                                menu:
                                    "insult her":
                                        menu:
                                            "whore":
                                                y "my cock is up, you filthy whore."
                                                show tojn tojn23 with dissolve
                                                jin "what the..."
                                                show tojn tojn24 with dissolve
                                                jin "you can't just say that to me!"
                                                jin "it's..."
                                                show tojn tojn23 with dissolve
                                                jin "very..."
                                                show tojn tojn20 with dissolve
                                                jin "rude..."
                                                jin "*mmmmm...*"
                                                show tojn tojn23 with dissolve
                                                jin "......."
                                                jin "i need to go!"
                                                $ june4talk1 = True
                                                jump jin_jasmine_menu
                                            "slut":

                                                y "my cock is up, you delectable slut."
                                                show tojn tojn23 with dissolve
                                                jin "what the..."
                                                show tojn tojn24 with dissolve
                                                jin "you can't just say that to me!"
                                                jin "it's..."
                                                show tojn tojn23 with dissolve
                                                jin "very..."
                                                show tojn tojn20 with dissolve
                                                jin "rude..."
                                                jin "*mmmmm...*"
                                                show tojn tojn23 with dissolve
                                                jin "......."
                                                jin "i need to go!"
                                                $ june4talk1 = True
                                                jump jin_jasmine_menu
                                            "user input":

                                                y "my cock is up, you user input."
                                                jin "....."
                                                jin "what?"
                                                y "i mean...."
                                                y "you..."
                                                y "big titted bitch."
                                                show tojn tojn23 with dissolve
                                                jin "what the..."
                                                show tojn tojn24 with dissolve
                                                jin "you can't just say that to me!"
                                                jin "it's..."
                                                show tojn tojn23 with dissolve
                                                jin "very..."
                                                show tojn tojn20 with dissolve
                                                jin "rude..."
                                                jin "*mmmmm...*"
                                                show tojn tojn23 with dissolve
                                                jin "......."
                                                jin "i need to go!"
                                                $ june4talk1 = True
                                                jump jin_jasmine_menu
                                    "suggest nudity":

                                        y "you should get naked."
                                        jin "...you make a good point."
                                        hide tojn with dissolve
                                        show tojn tojn22 with dissolve
                                        jin "as always, this is better."
                                        show ctc
                                        pause
                                        hide ctc
                                        jin "i gotta get back to work, since i'm staying here."
                                        jin "i should... probably get dressed again though."
                                        hide tojn with dissolve
                                        show tojn tojn20 with dissolve
                                        jin "that was fun."
                                        $ june4talk2 = True
                                        jump jin_jasmine_menu
                        "hypno":

                            if hypnoroom == "none":
                                if jin_hypno == 0:
                                    y "jin, i think you could really benefit from a detox session."
                                    show tojn tojn23 with dissolve
                                    jin "detox?"
                                    y "yeah, the hypnosis room at my shack will undo some of the brainwashing you went through."
                                    show tojn tojn24 with dissolve
                                    jin "i'd rather forget about it...."
                                    y "come to one session, see how you feel."
                                    y "it can't hurt, right?"
                                    show tojn tojn20 with dissolve
                                    jin "...i guess not."
                                    jin "okay, i'll come!"
                                    $ hypnoroom = "jin"
                                    y "i'll see you there."
                                    jump basingse_day1

                                if jin_hypno >=1 and jin_hypno <=4:
                                    y "jin, would you like another hypnosis session?"
                                    jin "definitely!"
                                    show tojn tojn24 with dissolve
                                    jin "i can't wait to get those jerks out of my head..."
                                    jin "...and have free will again!"
                                    y "*cough*"
                                    show tojn tojn20 with dissolve
                                    jin "anyway, i'll be there!"
                                    $ hypnoroom = "jin"
                                    y "great, i'll see you there."
                                    jump basingse_day1

                                if jin_hypno ==5:
                                    if not june4talk1 or not june4talk2:
                                        y "want another session?"
                                        show tojn tojn23 with dissolve
                                        jin "hmm... i don't know..."
                                        jin "i think it's making me feel a little funny lately..."
                                        jin "maybe I just need to adjust."
                                        y "sure, take your time."
                                        show tojn tojn20 with dissolve
                                        jin "thanks!"
                                        y "(I should insult her and see if I can get her naked.)"
                                        y "(maybe that will move her along.)"
                                        jump jin_jasmine_menu
                                    else:
                                        y "are you ready for-"
                                        jin "sign me up!"
                                        y "oh."
                                        y "well... cool."
                                        y "i'll meet you at my place and we'll get this hypno session rolling."
                                        jin "see you there!"
                                        $ hypnoroom = "jin"
                                        jump basingse_day1

                                if jin_hypno ==6:
                                    if jin_sucked:
                                        y "jin, would you like another hypnosis session?"
                                        jin "definitely!"
                                        show tojn tojn24 with dissolve
                                        jin "i can't wait to get those jerks out of my head..."
                                        jin "...and have free will again!"
                                        y "*cough*"
                                        show tojn tojn20 with dissolve
                                        jin "so i'll be there!"
                                        $ hypnoroom = "jin"
                                        y "great, i'll see you there."
                                        jump basingse_day1
                                    else:
                                        y "jin, would you like another hypnosis session?"
                                        jin "hmm... not right now."
                                        y "(huh.)"
                                        y "(maybe i should work on other things in the meantime.)"
                                        jump basingse_day1
                            else:

                                if hypnoroom == "june":
                                    y "(june is scheduled for the hypnosis room right now.)"
                                    y "(i'll invite jin once's it's open.)"
                                    jump jin_jasmine_menu
                                if hypnoroom == "suki":
                                    y "(suki is scheduled for the hypnosis room right now.)"
                                    y "(i'll invite jin once's it's open.)"
                                    jump jin_jasmine_menu
                                if hypnoroom == "jin":
                                    y "(jin is already scheduled for the hypnosis room.)"
                                    jump jin_jasmine_menu
                        "talk to iroh":

                            pass
                        "exit":

                            jump basingse_day1
            "talk to iroh":

                if nagina_free:
                    if not iroh_final_talk:
                        stop music
                        play music "audio/Ripples.mp3"
                        scene jasmin_dragon_inside
                        show toii toii02
                        with dissolve
                        $ iroh_final_talk = True
                        y "well, iroh..."
                        y "i might be around a bit longer, but..."
                        y "i have to admit something to you."
                        iroh "you're the avatar."
                        y "i'm the- whaaat?"
                        y "you... knew?"
                        iroh "you're covered in arrows, son."
                        iroh "not that difficult to work out."
                        iroh "but i do have some parting advice, that i hope you take seriously."
                        iroh "remember, in the darkest times, hope is something you give yourself."
                        iroh "and good times become good memories, but bad times become good lessons."
                        iroh "and lastly..."
                        iroh "you must look within yourself to save yourself from your other self."
                        iroh "only then will your true self reveal itself."
                        y "....."
                        y "that was nonsense."
                        iroh "or was it {i}genius{/i}?"
                        iroh "but seriously... if you ever struggle... don't be afraid to ask for help."
                        iroh "and just as importantly... be willing help to others, whether or not they ask."
                        iroh "you might save both of you."
                        y "this... this got serious."
                        iroh "some things are worth being serious about."
                        iroh "good luck, avatar."
                        hide toii toii02 with dissolve
                        jump bk3_jasmine

    if prisonbitch_freed and not jin_jasmine_met:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show tojn tojn20
        with dissolve
        jin "welcome to the-"
        show tojn tojn23 with dissolve
        jin "oh, hey!"
        jin "it's you!"
        show tojn tojn20 with dissolve
        jin "it's good to see you again!"
        y "likewise!"
        y "i'm glad we got you out of there."
        show tojn tojn24 with dissolve
        jin "yeah... that place is fucked up."
        jin "little bitches up in there."
        y "...."
        show tojn tojn20
        show jin_fl_blush
        with dissolve
        jin "sorry, i know that's not lady like..."
        y "heh, you're fine."
        y "but you should know that i'm de-programming other brainwashed girls."
        show tojn tojn23 with dissolve
        jin "you are?"
        y "yeah, and i think you should consider it."
        show tojn tojn20 with dissolve
        jin "i'll think about it."
        show tojn tojn24 with dissolve
        jin "i wonder what that ajala bitch thinks of me being free..."
        jin "she's responsible for any hypnosis i need..."
        show tojn tojn20 with dissolve
        jin "sorry! i'm good."
        jin "i have some things to take care of first, though..."
        hide jin_fl_blush with dissolve
        jin "oh, by the way..."
        jin "if you haven't already, try fighting iroh's crabs, if only once."
        jin "it doesn't matter whether you lose or win."
        jin "he's just bored sometimes."
        jin "you'll have to visit the arena first, though."
        jin "okay, see ya!"
        hide tojn
        with dissolve
        y "(hmm... maybe i should talk with ajala...)"
        $ jin_jasmine_met = True
        jump basingse_day1

    if iroh_battle_count >=6:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        if not kitten_gear:
            iroh "well done, stranger."
            iroh "as a reward for beating me so thoroughly, i'll give you this kitty outfit."
            play sound "audio/win2.mp3"
            $ kitten_gear = True
            y "(kitty outfit?)"
            y "(i hope he's never worn this...)"
            y "what do i do with it?"
            iroh "i'm sure you'll find a purpose."
        else:
            if joodee_fuck >=2 and iroh_panty_hunt ==0:

                y "hey, iroh-"
                show toii toii04 with dissolve
                iroh "was it you!?"
                y "whoa, you look pissed."
                y "what's got your panties in a bunch?"
                iroh "it {i}was{/i} you!"
                iroh "return them!"
                y "what?"
                iroh "was..."
                show toii toii07 with dissolve
                iroh "...was it really not you?"
                y "i have no idea what we're talking about, and am genuinely considering running."
                show toii toii06 with dissolve
                iroh "...oh."
                iroh "well..."
                show toii toii04 with dissolve
                iroh "someone took my panties!"
                y "ugh, man, come on!"
                y "i mean, i try not to judge but... damn it, that vision is gonna be in my head forever."
                show toii toii07 with dissolve
                ya "why would you tell me that!?"
                iroh "...wha..."
                show toii toii05 with dissolve
                iroh "oh!"
                iroh "no, they're not mine... i just collect them."
                y "that's even worse!"

                show toii toii07 with dissolve
                iroh "it is?"
                y "maybe? i don't know!"
                y "why are you telling me this?"
                show toii toii01 with dissolve
                iroh "you must help me."
                y "i really mustn't."
                show toii toii100 with dissolve
                iroh "please, stranger."
                iroh "i can't leave the shop, and i've been collecting those my whole life!"
                show toii_blink with dissolve
                iroh "ahh... the memories..."
                show toii toii03 with dissolve
                y "...man, i really wish you hadn't involved me in this..."
                y "well, i guess i'm in it already."
                y "what's in it for me?"
                show toii toii100 with dissolve
                iroh "there's a peeping hole in the dressing room."
                iroh "you can probably watch the girl who's been helping out here get changed."
                show toii toii01 with dissolve
                iroh "...or whatever she does in there."
                show toii toii06 with dissolve
                iroh "she takes forever to get ready."
                y "......."
                y "alright, deal."
                y "can you describe the thief?"
                show toii toii01 with dissolve
                iroh "he looked like a watertribe boy, but i only saw his back."
                y "hmm... okay, i'll look into it."
                y "i should ask jin first, since she lives here."
                $ iroh_panty_hunt = 1
            else:
                iroh "hello, stranger."

        iroh "relax for a bit, have a cup of tea."
        show toii toii03
        show toii_blink
        with dissolve
        "you sit and sip tea in silence for a bit."
        "it's very relaxing."
        jump basingse_day1

    if iroh_battle_convo and iroh_battle_count <=5:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        if iroh_panty_hunt ==0:
            y "hey, iroh-"
            show toii toii04 with dissolve
            iroh "was it you!?"
            y "whoa, you look pissed."
            y "what's got your panties in a bunch?"
            iroh "it {i}was{/i} you!"
            iroh "return them!"
            y "what?"
            iroh "was..."
            show toii toii07 with dissolve
            iroh "...was it really not you?"
            y "i have no idea what we're talking about, and am genuinely considering running."
            show toii toii06 with dissolve
            iroh "...oh."
            iroh "well..."
            show toii toii04 with dissolve
            iroh "someone took my panties!"
            y "ugh, man, come on!"
            y "i mean, i try not to judge but... damn it, that vision is gonna be in my head forever."
            show toii toii07 with dissolve
            ya "why would you tell me that!?"
            iroh "...wha..."
            show toii toii05 with dissolve
            iroh "oh!"
            iroh "no, they're not mine... i just collect them."
            y "that's even worse!"

            show toii toii07 with dissolve
            iroh "it is?"
            y "maybe? i don't know!"
            y "why are you telling me this?"
            show toii toii01 with dissolve
            iroh "you must help me."
            y "i really mustn't."
            show toii toii100 with dissolve
            iroh "please, stranger."
            iroh "i can't leave the shop, and i've been collecting those my whole life!"
            show toii_blink with dissolve
            iroh "ahh... the memories..."
            show toii toii03 with dissolve
            y "...man, i really wish you hadn't involved me in this..."
            y "well, i guess i'm in it already."
            y "what's in it for me?"
            show toii toii100
            hide toii_blink
            with dissolve
            iroh "there's a peeping hole in the dressing room."
            iroh "you can probably watch the girl who's been helping out here get changed."
            show toii toii01 with dissolve
            iroh "...or whatever she does in there."
            show toii toii06 with dissolve
            iroh "she takes forever to get ready."
            y "......."
            y "alright, deal."
            y "can you describe the thief?"
            show toii toii01 with dissolve
            iroh "he looked like a watertribe boy, but i only saw his back."
            y "hmm... okay, i'll look into it."
            $ iroh_panty_hunt = 1

        menu:
            "challenge iroh's crabs":
                y "up for a fun pocket crab battle?"
                iroh "i'm here to drink tea and kick ass."
                iroh "and i'm all out of tea."
                $ iroh_fun_battle = True
                jump bk3_arena_start_shit
            "exit":

                jump basingse_day1


    if first_arena_match and not iroh_battle_convo:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        y "iroh, have you played pocket crabs?"
        iroh "hmmm... i don't think so."
        y "do you have any crabs?"
        iroh "....that's awfully personal."
        y "i meant for battling, you syphilis-ridden cockhound."
        iroh "oh."
        iroh "well, i do...."
        iroh "i just don't know how it all works."
        y "let's play and you'll pick it up."
        iroh "sure."
        $ iroh_battle_convo = True
        $ iroh_fun_battle = True
        jump bk3_arena_start_shit


    if katara_found and not first_arena_match:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside
        show toii toii02
        with dissolve
        iroh "hello, stranger."
        iroh "relax for a bit, have a cup of tea."
        show toii toii03
        show toii_blink
        with dissolve
        "you sit and sip tea in silence for a bit."
        "it's very relaxing."




        jump basingse_day1

    if cheat_unlock and not katara_found:
        stop music
        play music "audio/Ripples.mp3"
        scene jasmin_dragon_inside with dissolve
        "as you walk inside the shop, an old man walks towards you and sits in one of the chairs."
        show toii toii02 with Dissolve(1.0)
        iroh "welcome to the jasmine dragon, stranger!"
        iroh "hmm....."
        show toii toii01 with dissolve
        iroh "you look like you could use a hot cup of tea, am i right?"
        show toii_blink_animated
        y "no, i'm-"
        y "-well, actually... yeah, that sounds nice."
        hide toii_blink_animated
        show toii_blink with dissolve
        iroh "good decision."
        hide toii_blink with dissolve
        iroh "sharing tea with a fascinating stranger is one of life's true delights."
        iroh "here. relax and enjoy. this is a peaceful place."
        show toii toii02 with dissolve
        "iroh hands you a cup of tea, and picks up his own."
        "you hesitantly taste the tea."
        "it's fucking great."
        show toii toii03
        show toii_blink
        with dissolve
        y "....this is fucking great."
        iroh "....."
        show toii toii02
        hide toii_blink
        with dissolve
        iroh "{i}aahh...{/i}"
        iroh "you humble me."
        iroh "now tell me, what are you seeking?"
        y "I'm sorry?"
        show toii toii01 with dissolve
        iroh "you know, you remind me of my nephew. he's also... lost."
        y "i'm not lost. i'm fine, really."
        show toii_blink with dissolve
        iroh "well, i'm just an old man..."
        iroh "but you seem... troubled. and reserved."
        hide toii_blink with dissolve
        iroh "there is nothing wrong with letting people who love you help you."
        show toii toii07 with dissolve
        iroh "not that i love you."
        show toii toii06 with dissolve
        iroh "i just met you."
        y "i...okay."
        y "well...."
        y "i'm sort of..."
        y "....on a mission."
        show toii toii01 with dissolve
        iroh "oh?"
        y "a long one."
        show toii_blink_animated
        y "and i mean, a looooong one."
        y "....but i don't even know why i'm doing it."
        show toii toii02 with dissolve
        iroh "hmm..."
        y "i've been told it's to help the world, and because it's my destiny, and honestly it's been kind of against my will..."
        show toii toii03 with dissolve
        y "but so much of it is a mystery to me."
        hide toii_blink_animated
        y "it's incredibly frustrating."
        show toii toii02
        show toii_blink
        with dissolve
        iroh "........"
        iroh "there are always challenges before us, but with the right mindset..."
        show toii toii01
        hide toii_blink
        with dissolve
        iroh "...and a good cup of tea..."
        show toii_blink with dissolve
        iroh "...those can become the best opportunities."
        y "...huh."
        iroh "so maybe you can turn this... mission... into an opportunity."
        y "you're a wise old guy, iroh."
        hide toii_blink with dissolve
        iroh "as are you..."
        show toii toii07 with dissolve
        iroh "...because i never told you my name."
        y "oh. uh. i've uh... heard about you?"
        iroh "...."
        show toii toii05 with dissolve
        iroh "now isn't that exciting! i'm already getting recognition!"
        show toii toii01 with dissolve
        iroh "but you are not here for the tea."
        y "I'm not?"
        iroh "no... you're looking for a lady."
        y "....how did you know that?"
        show toii toii05 with dissolve
        iroh "we are all looking for a lady!"
        y "oh."
        show toii toii01 with dissolve
        iroh "and also, she's staying here."
        y "what?"
        iroh "hold on."
        hide toii toii01 with dissolve
        show ctc
        pause
        hide ctc
        show toii toii01
        show toki toki01:
            xzoom -1.0 xpos 200
        with dissolve
        iroh "here she is."
        y "katara!"
        show toii toii02
        show toki toki04:
            xzoom -1.0 xpos 200
        show toki_smile:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "aang!"
        hide toki_smile
        show toki toki02:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "what happened to you?"

        k3 "we got kicked out of our house!"
        show toii toii03
        show toii_blink
        with dissolve
        k3 "the guards came after me!"
        y "so what are you doing here?"
        show toii toii01
        hide toii_blink
        with dissolve
        k3 "this kind old gentleman took me in and gave me a place to stay."
        show toii toii06 with dissolve
        iroh "i'm not {i}that{/i} old...."
        show toki toki01:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "...what?"
        show toii toii05 with dissolve
        iroh "i said, you're like a flower in bloom... your beauty intoxicating."
        show toki toki02:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "right..."
        show toii toii06 with dissolve
        iroh "......."
        y "....well, we've got a spot in the village just outside the walls if you want to come join us."
        k3 "oh, well...."
        k3 "i think i should stay in the city."
        y "what? why?"
        show toii toii03 with dissolve
        k3 "because toph is right...."
        show toki_blink:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "i'd just distract you."
        k3 "besides, someone has to try to get sokka out of jail."
        hide toki_blink with dissolve
        y "he's in jail?"
        show toii_blink with dissolve
        k3 "yeah, he sort of... resisted arrest..."
        k3 "...and he's not a bender, so..."
        k3 "jail."
        hide toii_blink
        show toii toii02
        with dissolve
        y "alright, well, as long as you're safe, i'll get out of here."
        k3 "okay."
        show toki toki01:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "i've found a family willing to take me in for the time being so that i don't have to bother iroh."
        iroh "oh, you're not a bother, dear."
        y "i will smack you, you old flirt."

        show toii toii03 with dissolve
        iroh "*sluurp*"
        y "okay, katara, where are you gonna stay?"
        k3 "oh, just somewhere in the city. i'm sure we'll run into each other every once in a while."
        y "alright."
        show toii toii02 with dissolve
        y "well, see you guys around. i've gotta let toph know you're alive."
        show toki_smile:
            xzoom -1.0 xpos 200
        with dissolve
        k3 "bye, aang!"
        show toii toii01
        show toii_blink
        with dissolve
        iroh "goodbye, stranger."
        iroh "Just remember..."
        hide toii_blink
        with dissolve
        iroh "life happens wherever you are, whether you make it or not."
        $ katara_found = True
        hide toki_smile with dissolve
        k3 "oh! wait!"
        k3 "come here a second...."
        iroh "i'll...."
        show toii toii02 with dissolve
        iroh "....leave you two alone."
        hide toii toii01 with dissolve
        hide toki toki01
        with dissolve
        show ksf
        with dissolve
        if earthbending ==0 and scams ==0:

            k3 "i know you came here straight away, and...."
            k3 "i want you to know i appreciate how much you care about me."
            k3 "so...."
            show ksfb
            hide ksf
            with dissolve
            k3 "......"
            show kst8
            hide ksfb
            with dissolve
            show ctc
            pause
            hide ctc
            y "hot damn!"
            show kst9
            hide kst8
            with dissolve
            k3 "well....."
            show ctc
            pause
            hide ctc
            show ksf
            hide kst9
            with dissolve
            k3 "...there you go."
            k3 "now...."

        k3 "i don't want to distract you."
        k3 "toph is your target right now."
        y "my... target?"
        show ksfe
        hide ksf
        with dissolve
        k3 "good luck, aang."
        y "okay, do you know-"
        hide ksfe with dissolve
        y "....."
        y "....she knows something."
        $ quest3 = True
        jump basingse_day1

    "\"under new management - closed for repairs.\""
    y "ah, bugger."
    jump basingse_day1

label bk3_jasmine_night:
    scene jasmin_dragon_inside
    show toii toii02
    with dissolve
    iroh "hello, stranger."
    iroh "relax for a bit, have a cup of tea."
    show toii toii03
    show toii_blink
    with dissolve
    "you sit and sip tea in silence for a bit."
    "it's very relaxing."
    jump basingse_night1

label bk3_fountain:
    if fountain_pee2:
        show toeg toeg01 with dissolve
        dl "the fountain is currently-"
        dl "hey! you're that avatar!"
        y "yes i am, and you're welcome."
        dl "get out of my city or i'll throw you out."
        y "oh, yeah?"
        y "you and what army?"
        show guardb_body_1:
            xpos -500
        with dissolve
        dl "your lack of compliance has been noted."
        y "oh. i forgot that you literally have an army."
        y "....um...."
        y "....look over there!"
        "you scurry off."
        "but not like you're scared or anything."
        jump basingse_day1

    if fountain_pee:
        show toeg toeg01 with dissolve
        dl "didn't i tell you to fuck off?"
        dl "do i need to choke a bitch?"
        y "...no?"
        dl "if you're not gone in three seconds, that's going to happen."
        y "fine, i'll go. but not because i'm scared of you."
        dl "three."
        y "what?"
        dl "two."
        y "oh, doing a countdown. yeah, real original."
        dl "one."
        y "oh, shit."
        y "bye!"
        $ fountain_pee2 = True
        jump basingse_day1
    else:

        show toeg toeg01 with dissolve
        dl "the fountain is currently closed."
        y "why?"
        dl "for your protection."
        y "somebody peed in it, didn't they?"
        dl ".....i'm not at liberty to say."
        y "yeah, they peed."
        dl ".......leave the premises, civilian."
        dl "or you will be removed."
        y "well, i can see {i}urine{/i} a bad mood, so i'll just go."
        dl "ugh. i hate my job."
        y "i also hate your job."
        dl "....you should go. now."
        y "....i'm gonna go."
        dl "good decision."
        hide toeg toeg01 with dissolve
        $ fountain_pee = True
        jump basingse_day1

label bk3_fountain_night:
    show toeg toeg01 with dissolve
    dl "the fountain is currently-"
    dl "hey! you're that avatar!"
    y "yes i am, and you're welcome."
    dl "get out of my city or i'll throw you out."
    y "oh, yeah?"
    y "you and what army?"
    show guardb_body_1:
        xpos -500
    with dissolve
    dl "your lack of compliance has been noted."
    y "oh. i forgot that you literally have an army."
    y "....um...."
    y "....look over there!"
    "you scurry off."
    "but not like you're scared or anything."
    jump basingse_night1

label bk3_market_night:
    scene black
    scene market_general
    show blue_30perc_transparent
    with dissolve
    menu:
        "scams":
            jump bk3_games
        "exit":

            jump basingse_night1


label bk3_market:
    scene black
    scene market_general
    with dissolve
    if earth_riddles == 1:
        y "there's a note here!"
        y "I guess i got the location right."
        y "the riddle was: \"here, you leave with what you bring,\n though it's rarely ever the same thing.\""
        y "it must have meant an exchange of goods and services for money."
        y "cheeky."
        y "okay, new note!"
        "\"here, you reap what you sew.\""
        menu:
            "read it again":
                "\"here, you reap what you sew.\""
            "got it":
                pass
        $ earth_riddles = 2
        jump basingse_day1

    if begin_scams:
        menu:
            "shop":
                jump bk3_market_shop
            "scams":

                jump bk3_games
            "exit":

                jump basingse_day1


    if cheat_unlock and katara_found:
        $ begin_scams = True
        show toi toi02 with dissolve
        $ scams +=1
        t "any luck?"
        y "yeah... though i have some new things to think about."
        show toi toi09 with dissolve
        t "...like what?"
        y "huh? oh, don't worry about it."
        t "...."
        show toi_blink with dissolve
        t "well, while you were off having fun, i got us some money."
        play sound "audio/win2.mp3"
        $ emoney +=15
        "you got 15 coins!"

        y "oh, cool."
        hide toi_blink with dissolve
        t "yeah, but it's not enough."
        y "...enough for what?"
        t "well, you can't keep sleeping outside."
        ym "does that mean you want me to sleep with you?"
        show toi toi05 with dissolve
        t "ew, no!"
        show toi toi06
        show toi_blink
        with dissolve
        t "gross!"
        hide toi_blink
        with dissolve
        t "we need to build you a house."
        t "but, while we can do some building with earthbending, we need other materials, too."
        t "we need {b}5 wood{/b} and {b}5 steel{/b} for a basic house."
        t "we can buy those here in the market, but we've got to make a little more money to afford them."
        show toi toi04 with dissolve
        t "we'll start when you're ready."
        t "and once you get all the materials, we'll meet up in the village."
        show blackveil with dissolve
        $ bk3_village_access = True
        "you can now travel between the city and the village!"
        show bk3_village_off:
            xpos 0.25
        show bk3_basingse_off:
            xpos 0.18
        with dissolve
        "when these buttons appear at the top of your screen, you can use them travel between the city and the village."
        show bk3_village_on:
            xpos 0.25
        with dissolve
        "use the \"home\" icon to travel to the village."
        hide bk3_village_on
        show bk3_basingse_on:
            xpos 0.18
        with dissolve
        "use the \"bridge\" icon to travel to the city."
        hide bk3_basingse_on
        hide bk3_basingse_off
        hide bk3_village_off
        hide blackveil
        with dissolve
        $ quest4 = True
        jump bk3_market

    if cheat_unlock and not katara_found:
        show toi toi06 with dissolve
        t "i'll look for her here."
        t "go find katara!"
        jump basingse_day1

    if solo_dicecups and not cheat_unlock:
        show azss azss01 with dissolve
        ss "go away, i'm still pissed."
        hide azss azss01 with dissolve
        jump basingse_day1

    show azss azss01 with dissolve
    ss "hey! what do you think you're doing here?"
    y "just looking around."
    ss "hmmm...."
    ss "you look like a gambling man."
    y "i've been known to dabble."
    ss "right, well, we're playing {b}cups{/i}."
    ss "the buy-in is 5 coins."
    ss "if you win, you get 15 coins, plus your 5 back."
    ss "if you lose, we keep your 5 coins."
    ss "so, you in?"
    menu:
        "don't play":
            y "nah, i'm busy right now."
            jump basingse_day1
        "play":

            if emoney >=1:
                y "I don't have any mon- oh, wait, i have some coins."
                y "how did this happen?"
                ss "did you steal them?"
                y "i guess they were already in my pockets."
                ss "great, well, since it's your first time, we'll go ahead and take it all."
                y "...that doesn't seem fair."
                ss "you're alone in an alley with money you stole."
                ss "you're lucky i don't report you to the dai lee."
                y "....."
                y "oh, fine..."
                $ emoney = 0
                ss "great!"
                ss "well, let's get started!"
            else:
                y "I don't have any money."
                ss "oh."
                ss "well, tell you what -- i'm a forgiving lass."
                ss "first go's on me."
                ss "let's get started!"

    ss "the rules to {b}cups{/b} are simple."
    ss "you've gotta keep your eye on the cup that's hiding the stone."
    ss "There are 3 rounds in a match."
    ss "You have to win all 3 rounds to win money."
    ss "Each round is slightly faster than the one before it."
    ss "Let's begin!"
    jump dicecups_start2

label bk3_home:
    if nagina_free:
        scene black
        scene basingse_home_2
        with dissolve



        if joodee_insem:
            jump jdpregfuck

    if joodee_tits >=9:
        scene black
        scene basingse_home_2
        with dissolve
        show tojt tojt01
        with dissolve
        jd "hello, avatar."
        menu:
            "get naked":
                jd "very well..."
                show expression "bk3/joodee/idles/idle_base_nude.png"
                hide tojt
                with dissolve
                show ctc
                pause
                hide ctc
                jd "enough?"
                y "you are hot."
                y "but yeah, you can put your clothes back on."
                hide expression "bk3/joodee/idles/idle_base_nude.png"
                show tojt tojt01
                with dissolve
                y "I'll be back."
                jump basingse_day1
            "play with her tits":

                y "woopsie doo here comes the goo."
                jd "..........."
                jd "how may i assist you today?"
                y "shirt. off. now."
                show tojt tojt02 with dissolve
                pause 0.3
                show tojt tojt03
                pause 0.3
                show tojt tojt04
                show ctc
                pause
                hide ctc
                y "good...."
                y "now, give 'em a good suck."
                show tojt tojt102
                show ctc
                pause
                hide ctc
                y "how do your tits taste?"
                jd "*mmghm...*"
                y "i thought so."
                show tojt tojt04
                show tojt_unhappy
                with dissolve
                y "you know, you've got kind of a big mouth."
                show tojt_surprise
                hide tojt_unhappy
                with dissolve
                y "i don't mean it in a bad way... girls with big mouths can take more."
                y "hhmmm..."
                hide tojt_surprise
                show tojt_unhappy
                with dissolve
                y "open your mouth... i'm going to spit in it."
                show tojt_surprise
                hide tojt_unhappy
                with dissolve
                jd "......yes, sir......"
                hide tojt_surprise
                show tojt_unhappy
                with dissolve
                jd "............."
                show tojt_openmouth with dissolve
                jd "............."
                play sound "audio/spit.mp3"
                hide tojt_unhappy
                show tojt_surprise
                show tojt_spithead with Dissolve(2.0)
                y "shit I missed."
                y "Open your mouth...."
                y "i'm going to try again."
                hide tojt_surprise
                show tojt_unhappy
                hide tojt_openmouth
                show tojt_openmouth

                hide tojt_spithead
                show tojt_spithead
                y "oh, and start rubbing those massive tits of yours."
                show tojt tojt46
                show tojt_hands_updown
                y "now that's a good look."
                show ctc
                pause
                hide ctc
                hide tojt_hands_updown
                show tojt tojt05

                y "let's see if i can get it in this time...."


                play sound "audio/spit.mp3"

                show tojt_spitmouth with Dissolve(2.0)
                y "nice! Now swallow it!"
                hide tojt_openmouth
                hide tojt_spitmouth

                show tojt tojt05
                y "Take your hands off those tits!"
                hide tojt_spithead

                show tojt_spithead
                show tojt tojt04
                jd "o... okay...."
                show tojt_titpullright


                hide tojt_unhappy
                show tojt_surprise
                hide tojt_spithead
                show tojt_spithead
                show tojt_blink
                jd "ohhh...."
                show ctc
                pause
                hide ctc
                y "Yeah...you like that don't you..."

                hide tojt_spithead
                hide tojt_blink
                hide tojt_surprise
                show tojt_ahageo
                show tojt_spithead
                jd "ngh... uhh..."

                y "we're not done yet."
                show tojt_titpullleft
                jd "ahh... mmmm.... uhh...."
                show ctc
                pause
                hide ctc
                y "that's it, slut... enjoy getting your big sloppy tits tugged."
                hide tojt_titpullright
                hide tojt_titpullleft

                show tojt_blink
                y "and now..."
                hide tojt_ahageo
                hide tojt_blink
                show tojt_surprise
                hide tojt_spithead
                show tojt_spithead


                show tojt tojt103
                play sound "audio/slap.mp3"
                $ renpy.pause(1, hard=True)
                play sound "audio/slap.mp3"
                $ renpy.pause(1, hard=True)
                show tojt_ahageo
                hide tojt_surprise
                hide tojt_spithead
                show tojt_spithead
                $ renpy.pause(1, hard=True)



                show tojt_titpullleft
                show tojt_titpullright
                jd "ohhh... fu... fuck... avatar..."
                y "did you just curse, joo dee?"
                jd "nngh..."
                y "i'm impressed, didn't think you had it in you."
                show ctc
                pause
                hide ctc
                jd "i'm... i'm..."
                y "what?"
                with vshake
                jd "{size=+10}nnghhhh!!! fuck!!"

                hide tojt_titpullleft
                hide tojt_titpullright
                y "did you cum from nipple play again?"
                hide tojt_ahageo
                show tojt_blink
                jd "mmmmm...."
                y "you're such an old milf slut."
                y "aren't you?"
                jd "y... yes... i'm a... milf slut..."
                y "i know."
                y "now wipe that spit off."
                show tojt_arm_wipe
                $ renpy.pause(1,hard=True)
                hide tojt_arm_wipe

                hide tojt_blink
                hide tojt_spithead with Dissolve(2.0)
                $ renpy.pause(1,hard=True)


                y "alright, get your clothes back in order."

                jd "yes... avatar... sir..."

                show tojt tojt41
                pause 0.3
                show tojt tojt40
                pause 0.3
                show tojt tojt02
                pause 0.3
                show tojt tojt01
                pause 0.3
                y "I'll be back."

                hide tojt_spermface3
                scene black with dissolve
                "you head back to the village."
                $ bk3_day = False
                jump bk3_village_background
            "fuck joodee":

                if joodee_fuck == 0:
                    y "woopsie doo here comes the goo."
                    jd "..........."
                    jd "how may i assist you today?"
                    y "i'm gonna pump your milf pussy full of cum."
                    jd "...i don't think so."
                    y "what?"
                    jd "is there anything else?"
                    y "(why didn't that work?)"
                    y "(maybe i should ask ajala.)"
                    $ joodee_fuck = 1
                    jump basingse_day1
                if joodee_fuck == 1:
                    y "(i should ask ajala about this.)"
                    jump basingse_day1
                if joodee_fuck >=2:
                    y "wanna bang?"
                    jd "....."
                    show tojt tojt06 with dissolve
                    jd "well...."
                    show tojt tojt01 with dissolve
                    jd "very well, avatar."
                    show tojt tojt02 with dissolve
                    jd "may i take my top off?"
                    y "...uh, yeah."
                    y "definitely."
                    show tojt tojt03 with dissolve
                    jd "wonderful!"
                    show tojt tojt04 with dissolve
                    jd "now... i... i suppose you'd like me to lie down?"
                    y "i would indeed."
                    jd "o-okay..."
                    $ joodee_fuck +1
                    jump joodee_sex1
            "leave":

                jump basingse_day1


    if joodee_tits >=6 and joodee_tits <=8:
        y "i should visit ajala in the tunnels before visiting joo dee."
        jump basingse_day1

    if joodee_tits ==4 and ajala_jin_lesson:
        scene black
        scene basingse_home_2
        with dissolve
        show tojt tojt01
        with dissolve
        jd "hello, avatar."
        y "joo dee, good to see you."
        jd "i took a wonderful little vacation..."
        jd "to lake laogai."
        y "...you don't say..."
        y "well, can i see your tits?"
        jd "what a good joke."
        jd "very funny, avatar."
        jd "please let me know if you need any assistance."
        y "oh, right."
        y "\"The Earth King has invited you to Lake Laogai.\""
        jd "......"
        jd "he has?"
        y "what?"
        jd "you said he invited me."
        jd "is that true?"
        y "...no."
        y "nevermind."
        jd "very well."
        jd "goodbye for now!"
        scene black
        scene basingse_city_1
        with dissolve
        y "okay... joo dee's acting really weird."
        y "maybe ajala, in the tunnels, knows something."
        $ joodee_tits = 6
        jump basingse_day1

    if joodee_tits ==4 and not ajala_jin_lesson:
        scene black
        scene basingse_home_1
        with dissolve
        y "joo dee doesn't seem to be here."
        y "where could she have gone?"
        y "maybe i should train or explore the tunnels..."
        y "...and hope something triggers?"
        jump basingse_day1

    if joodee_tits ==3:
        scene black
        scene basingse_home_2
        with dissolve
        show tojt tojt01
        with dissolve
        jd "hello, avatar!"
        jd "how may i assist you today?"
        y "shirt. off. now."
        show tojt tojt02 with dissolve
        pause 0.3
        show tojt tojt03
        pause 0.3
        show tojt tojt04
        show ctc
        pause
        hide ctc
        jd "is this to your satisfaction, avatar?"
        y "yes... very much so."
        y "now, give 'em a good suck."
        show tojt tojt102
        show ctc
        pause
        hide ctc
        y "....you're way too good at that."
        y "have... have you breastfed yourself?"
        jd "...."
        jd "yeth..."
        y "you're a star."
        show tojt tojt04
        show tojt_unhappy
        with dissolve
        jd "thank you... avatar."
        y "you know, you've got kind of a big mouth."
        show tojt_surprise
        hide tojt_unhappy
        with dissolve
        y "i don't mean it in a bad way... girls with big mouths can take more."
        y "hhmmm..."
        hide tojt_surprise
        show tojt_unhappy
        with dissolve
        jd "what... what is it?"
        y "open your mouth... i'm going to spit in it."
        show tojt_surprise
        hide tojt_unhappy
        with dissolve
        jd "wha... why would..."
        y "don't question me, joo dee."
        hide tojt_surprise
        show tojt_unhappy
        with dissolve
        jd "............."
        show tojt_openmouth with dissolve
        jd "............."
        play sound "audio/spit.mp3"
        hide tojt_unhappy
        show tojt_surprise
        show tojt_spithead with Dissolve(2.0)
        y "shit I missed."
        y "Open your mouth...."
        y "i'm going to try again."
        hide tojt_surprise
        show tojt_unhappy
        hide tojt_openmouth
        show tojt_openmouth

        hide tojt_spithead
        show tojt_spithead
        y "oh, and start rubbing those massive tits of yours."
        show tojt tojt46
        show tojt_hands_updown
        y "now that's a good look."
        show ctc
        pause
        hide ctc
        hide tojt_hands_updown
        show tojt tojt05

        y "let's see if i can get it in this time...."


        play sound "audio/spit.mp3"

        show tojt_spitmouth with Dissolve(2.0)
        y "nice! Now swallow it!"
        hide tojt_openmouth
        hide tojt_spitmouth

        show tojt tojt05
        y "Take your hands off those tits!"
        hide tojt_spithead

        show tojt_spithead
        show tojt tojt04
        jd "o... okay...."
        show tojt_titpullright


        hide tojt_unhappy
        show tojt_surprise
        hide tojt_spithead
        show tojt_spithead
        show tojt_blink
        jd "ohhh...."
        show ctc
        pause
        hide ctc
        y "Yeah...you like that don't you..."

        hide tojt_spithead
        hide tojt_blink
        hide tojt_surprise
        show tojt_ahageo
        show tojt_spithead
        jd "ngh... uhh..."

        y "we're not done yet."
        show tojt_titpullleft
        jd "ahh... mmmm.... uhh...."
        show ctc
        pause
        hide ctc
        y "that's it, slut... enjoy getting your big sloppy tits tugged."
        hide tojt_titpullright
        hide tojt_titpullleft

        show tojt_blink
        y "and now..."
        hide tojt_ahageo
        hide tojt_blink
        show tojt_surprise
        hide tojt_spithead
        show tojt_spithead


        show tojt tojt103
        play sound "audio/slap.mp3"
        $ renpy.pause(1, hard=True)
        play sound "audio/slap.mp3"
        $ renpy.pause(1, hard=True)
        show tojt_ahageo
        hide tojt_surprise
        hide tojt_spithead
        show tojt_spithead
        $ renpy.pause(1, hard=True)



        show tojt_titpullleft
        show tojt_titpullright
        jd "ohhh... fu... fuck... avatar..."
        y "did you just curse, joo dee?"
        jd "nngh..."
        y "i'm impressed, didn't think you had it in you."
        show ctc
        pause
        hide ctc
        jd "i'm... i'm..."
        y "what?"
        with vshake
        jd "{size=+10}nnghhhh!!! fuck!!"

        hide tojt_titpullleft
        hide tojt_titpullright
        y "holy shit, did you just cum?"
        hide tojt_ahageo
        show tojt_blink
        jd "mmmmm...."
        y "from nipple play?"
        y "holy shit."
        jd "i... i don't... know..."
        y "you don't know? what?"
        y "have you... wait... have you never had an orgasm?"
        jd "a... what...?"
        y "are you fucking serious?"
        y "i thought you said you were a mother?"
        jd "i am..."
        y "okay, we're gonna spend more time on that later."

        y "but for now.... wipe that spit off."
        show tojt_arm_wipe
        $ renpy.pause(1,hard=True)
        hide tojt_arm_wipe

        hide tojt_blink
        hide tojt_spithead with Dissolve(2.0)
        $ renpy.pause(1,hard=True)


        y "alright, get your clothes back in order."

        jd "Y... yes... avatar... sir..."

        show tojt tojt41
        pause 0.3
        show tojt tojt40
        pause 0.3
        show tojt tojt02
        pause 0.3
        show tojt tojt01
        pause 0.3
        y "I'll be back."

        hide tojt_spermface3
        $ joodee_tits = 4
        scene black with dissolve
        "it's night by the time you leave... you head back to the village."
        $ bk3_day = False
        jump bk3_village_background

    if joodee_tits ==2:
        scene black
        scene basingse_home_2
        with dissolve
        show tojt tojt01
        with dissolve
        jd "hello, avatar!"
        jd "how may i assist you today?"
        y "by breaking out your big tits."
        show tojt_unhappy
        show tojt_blush
        show tojt tojt02
        jd "I'll just unfasten this and..."
        show tojt_blink
        show tojt tojt40

        show tojt tojt41
        show ctc
        pause
        hide ctc
        y "that's very nice, joo dee."
        y "but... i think we're a little past that."
        hide tojt_blink with dissolve
        show tojt tojt42
        pause 0.4
        jd ".........."
        show tojt tojt04
        show tojt_blink
        with Dissolve(1.3)
        show ctc
        pause
        hide ctc
        y "hot damn!"
        y "rub them."
        show tojt_hands_updown
        show tojt tojt46
        y "look at me."
        hide tojt_blink with dissolve
        jd "this is... so embarrassing..."
        jd "i can't believe i'm revealing myself to the avatar..."
        y "give them a good suck."
        jd "wh...what?"
        y "suck. on. your. tits."
        jd "......"
        hide tojt_hands_updown

        show tojt tojt10
        hide tojt_unhappy
        with dissolve
        jd "*slurp*"
        show tojt tojt11 with dissolve
        jd "*shhlaap*"
        show tojt tojt12 with dissolve
        show ctc
        pause
        hide ctc
        show tojt tojt04
        show tojt_unhappy
        jd "*slurp*"
        jd "how was that?"
        y "amazing."
        y "do it again. faster."
        jd "....."
        show tojt tojt102
        hide tojt_unhappy
        jd "'ike dis?"
        show ctc
        pause
        hide ctc
        y "girl... you got gifts."
        jd "...."
        y "okay, you can stop."
        show tojt tojt05
        show tojt_unhappy
        show tojt_blush
        with dissolve
        jd "are.. are you finished?"
        y "almost."
        y "one last thing...."
        jd "...what...?"
        y "drop your hands."
        show tojt tojt04 with dissolve
        jd "wh-"
        $ generic_counter = 0
        while generic_counter <= 2:
            show tojt tojt103
            show tojt_surprise
            hide tojt_blush
            show tojt_blush
            play sound "audio/slap.mp3"
            pause 1.0
            play sound "audio/slap.mp3"
            pause 1.0
            $ generic_counter += 1
            if generic_counter == 3:
                menu:
                    "slap her some more":
                        $ generic_counter = 0
                    "I'm good":
                        pass
        show tojt_unhappy
        hide tojt_surprise
        with dissolve
        jd "my... my bosom...."
        y "heh. yeah."
        y "not bad."
        show tojt_blink with dissolve
        jd "they're going to be so sore..."
        y "\"The Earth King has invited you to Lake Laogai.\""
        hide tojt_unhappy
        hide tojt_blush
        hide tojt_blink
        with dissolve
        y "good."
        y "you're going to stop wearing a bra."
        jd "i understand."
        y "good girl."
        y "i'll see you later... for more..."
        $ joodee_tits = 3
        scene black with dissolve
        "it's night by the time you leave... you head back to the village."
        $ bk3_day = False
        jump bk3_village_background

    if joodee_tits ==1 and joodee_trigger == 1:
        scene black
        scene basingse_home_2
        with dissolve
        show tojt tojt01
        with dissolve
        show tojt_unhappy with dissolve
        jd "avatar... what a pleasant... surprise."
        jd "how... may i help you?"
        y "i'd like to see those tits again."
        jd "....."
        hide tojt_unhappy
        show tojt_unhappy
        show tojt_blink
        show tojt_blush
        show tojt tojt02
        jd "I'll just unfasten this and..."
        show tojt tojt40
        pause 0.3
        show tojt tojt41
        show ctc
        pause
        hide ctc
        jd "this is all i will do, though."
        jd "...please finish looking."
        jd "this is so embarrassing."
        y "why are you embarrassed? you have an amazing rack."
        jd "please. this is so humiliat-"
        y "\"The Earth King has invited you to Lake Laogai.\""
        hide tojt_unhappy
        hide tojt_blink
        hide tojt_blush
        y "good... good..."
        y "when i snap my fingers, you'll be... less inhibited."
        y "just a little more... receptive... to suggestion."
        play sound "audio/fingersnap.mp3"
        y "*snap*"
        show tojt_surprise with dissolve
        jd "what... what's happening...?"
        y "you're going to show me your tits."
        y "not just your bra."
        jd "...but..."
        y "or i let long feng know."
        hide tojt_surprise
        show tojt_unhappy
        show tojt_blush
        jd "......."
        y "Your ass would be fine too."
        jd "...."

        show tojt tojt42
        pause 0.4
        show tojt tojt04
        with Dissolve(1.3)
        show ctc
        pause
        hide ctc
        y "Now, that's a nice view!"
        y "Toph would kill for those!"
        jd "What?!"
        y "Not literally."
        y "Sooo can they do tricks?"
        jd "What?"
        y "You're starting to repeat yourself again."
        jd "Can I go now?"
        y "Almost."
        y "Put your hands on them."
        hide tojt_unhappy
        hide tojt_blush
        show tojt tojt05
        show tojt_unhappy
        show tojt_blush
        y "Yes, wonderful."
        y "Now start rubbing them up and down. Slowly."
        show tojt_hands_updown
        show tojt tojt46


        hide tojt_unhappy
        hide tojt_blush
        show tojt_hands_updown
        show tojt_unhappy
        show tojt_blush
        show tojt_blink
        show ctc
        pause
        hide ctc
        y "Very good! You're a natural at this"
        y "now do it from right to left."
        hide tojt_hands_updown
        show tojt_hands_rightleft
        y "Nice. Just let them wander all over."
        hide tojt_hands_rightleft
        show tojt_hands_chaos
        show ctc
        pause
        hide ctc
        y "Yeah, like that."
        hide tojt_blink
        y "Girl, you could make money doing just that!"
        hide tojt_blush
        show tojt_surprise
        show tojt_blush
        jd "I'm a mother!"
        y "That's even better."
        hide tojt_surprise
        show tojt_blink
        jd "Can I stop now...please?"
        y "Ooooh okay I guess."
        y "You can put those puppies back in their cage."
        hide tojt_hands_chaos
        show tojt tojt04
        pause 0.3
        show tojt tojt42
        pause 0.3    
        show tojt tojt40
        pause 0.3
        show tojt tojt02
        hide tojt_blush
        hide tojt_unhappy
        hide tojt_blink
        show tojt tojt101
        jd "We're done right?"
        y "Of course. For now."
        y "Come on, show me that smile of yours'."
        show tojt tojt01
        show tojt_unhappy

        show tojt_unhappy_eyebrows
        hide tojt_unhappy with Dissolve(2.0)
        y "That's better."
        y "See ya later sugartits."
        $ joodee_tits = 2
        scene black with dissolve
        "it's night by the time you leave... you head back to the village."
        $ bk3_day = False
        jump bk3_village_background

    if joodee_tits ==1 and joodee_trigger == 0:
        y "i should figure out joo dee's trigger before i visit her again."
        y "i might be able to find ajala in the tunnels beneath lake laogai."
        jump basingse_day1

    if suki_free and joodee_tits ==0:
        scene black
        scene basingse_home_1
        show toji toji01
        with dissolve
        jd "avatar! always a pleasant surprise!"
        jd "how may i assist you today?"
        y "I've got some ideas."
        y "let's... go inside."
        jd "of course!"
        scene black
        scene basingse_home_2
        with dissolve
        show tojt tojt01 with dissolve
        jd "what can i do to assist the Avatar?"
        y "Oh, nothing much. I was just wondering about your tits."
        show tojt_surprise
        show tojt_blush
        with dissolve
        jd "My..."
        y "I bet they're wonderful!"
        y "Everything In BasingSe is, right?"
        hide tojt_blush with Dissolve(2.0)
        hide tojt_surprise
        jd "Haha, you are such a kidder!"
        y "I'd like to see those tits of yours."
        y "As a good host you want to make me happy right?"
        show tojt_blink
        jd "Ha ha... that's a funny joke!"
        y "What would happen if I told Long Feng you weren't doing your job?"
        hide tojt_blink
        show tojt_surprise
        jd "......I...."
        y "You've got a pretty nice job here."
        y "It would be a shame to risk all of that when just showing me your tits could prevent that."
        jd "........."
        show tojt tojt101
        hide tojt_surprise
        jd "There's really nothing special about them."
        jd "As the avatar... i'm sure there are many girls who would want to help you."
        jd "Younger, prettier girls."

        jd "Far better than a tired older woman like me."
        y "You think so?"
        show tojt tojt01
        show tojt_blink
        jd "No doubt!"
        hide tojt_blink
        jd "BasingSe has many many wonderful girls!"
        y "Hmmm... I guess you're right about that."
        jd "Certainly!"
        y "and I still wanna see yours."
        show tojt_unhappy
        jd "But....."
        y "You want to show me your butt instead? Well, if you..."
        show tojt_surprise
        jd "NO!"
        hide tojt_surprise
        show tojt_blink
        jd "I mean... you... you just want to see my... chest?"
        y "Yes, your tits."
        jd "O... Okay. But...."
        y "You're taking a really long to do something really simple."
        y "I think I'll go have a talk with Long Feng."
        jd "pl-please wait..."
        hide tojt_blink
        show tojt_unhappy
        show tojt_blink
        show tojt_blush
        show tojt tojt02
        jd "I'll just unfasten this and..."
        show tojt tojt40
        pause 0.3
        show tojt tojt41
        show ctc
        pause
        hide ctc
        jd "Th-there..."
        y "Wow, you were really hiding some good ones under there!"
        jd "Thank you."
        y "Now take off your bra."
        hide tojt_blink
        hide tojt_blush
        show tojt_surprise
        show tojt_blush
        show tojt tojt41
        jd "But you said...!"
        y "I said I wanted to see your tits, not your bra."
        jd "......"
        hide tojt_unhappy
        show tojt_unhappy
        hide tojt_blush
        show tojt_blush
        hide tojt_blink
        show tojt_blink
        jd "i can't! i'm sorry avatar..."
        jd "please... leave."
        show ctc
        pause
        hide ctc
        y "fine. but i'll be back."
        jd "......"
        scene black
        scene basingse_home_1
        with dissolve
        y "there's gotta be a way to make her go further."
        y "maybe i can find ajala in the tunnels..."
        y "and find out what joo dee's trigger is."
        $ joodee_tits = 1
        jump basingse_day1


    if got_posters:
        scene black
        scene basingse_home_1
        show toji toji01
        with dissolve
        jd "hello, avatar!"
        jd "can i help you?"
        y "not at the moment."
        jd "let me know if that changes."
        jump basingse_day1

    if get_posters and not got_posters:
        scene black
        scene basingse_home_1
        with dissolve
        y "....."
        y "no guards."
        y "cool."
        y "i'll just go inside, aaaand...."
        scene black
        scene basingse_home_2
        show toji toji01
        with dissolve
        jd "hello, avatar."
        y "joo dee?"
        y "what are you doing here?"
        jd "well, i'm your guide while you're here in the city."
        show toji toji02
        show toji_smile
        with dissolve
        jd "i have been assigned to your house."
        y "so, you're a spy for that feng douche."
        jd "......."
        y "....right."
        y "where have you been?"
        y "last time i saw you, you looked terrified."
        jd "i was simply a little... stressed."
        jd "i took a vacation to lake laogai and i am much calmer now."
        y "......"
        y "you didn't happen to stay in any tunnels, did you?"
        hide toji_smile with dissolve
        jd "tunnels? i'm afraid i don't understand."
        y "uh... there are a bunch of tunnels that run under the lake."
        jd "....."
        show toji_smile with dissolve
        jd ".....what a wonderful imagination!"
        jd "there are no tunnels under lake laogai."
        y "i was {i}in{/i} them, lady. i'm telling you."
        hide toji_smile with dissolve
        jd "you should be a professional storyteller!"
        y "...i'm not going to do this with you right now."
        y "do you still have those posters I gave you?"
        jd "of course!"
        y "i need them back."
        jd "very well."
        show toji toji03 with dissolve
        jd "here you go!"
        play sound "audio/win2.mp3"
        show appa_poster with dissolve
        show ctc
        pause
        hide ctc
        "you got the poster!"
        show ctc
        pause
        hide ctc
        hide appa_poster with dissolve
        show toji_smile with dissolve
        jd "though i must remind you that the posting of flyers is strictly prohibited without a permit."
        y "...right."
        show toji toji02 with dissolve
        y "how long are you going to be here?"
        jd "i will be here if you need me, avatar."
        y "good, i'll see you later, then."
        $ got_posters = True
        jump basingse_day1


    if cheat_unlock:
        scene black
        scene basingse_home_1
        show toeg toeg03
        with dissolve
        y "fuck! these fucking guards are everywhere!"
        dl "hey! you!"
        y "nope!"
        jump basingse_day1

    scene black
    scene basingse_home_1
    with dissolve
    y "i wonder if toph's still inside?"
    scene black
    scene basingse_home_2
    show toi toi04
    with dissolve
    show toi toi05 with dissolve
    t "hey! why are you here!?"
    y "well, that answers that."
    t "if i have to launch you there, i'll do it."
    y "I'm going, i'm going...."
    jump basingse_day1

label bk3_home_night:
    scene black
    scene basingse_home_1
    show background_fade_purpleish
    show toeg toeg03
    with dissolve
    y "fuck! these fucking guards are everywhere!"
    dl "hey! you!"
    y "nope!"
    jump basingse_night1

label bk3_arena:
    if cheat_unlock and crab1:
        stop music
        play music "audio/Hero Down.mp3"
        scene black
        scene bg_a watchtower_floor
        show shadyguy_grin
        with dissolve

        if toph_katara_chair ==3:
            sg "my man!"
            y "yo, shades."
            y "any chance a colorful hooker sold you a key?"
            sg "you're gonna have to be more specific."
            y "i... she... had breasts?"
            sg "oh! yeah, i remember her."
            y "...what..."
            sg "but i don't take care of the merchandizing any more."
            sg "i've got people to do that for me."
            sg "go talk to shady girl down at the market."
            sg "she handles that stuff."
            y "alright, i'll talk to shady girl."
            sg "later, amigo!"
            $ toph_katara_chair = 4
            jump basingse_day1

        if toph_katara_chair >=4 and toph_katara_chair <7:
            sg "did you talk to shady girl yet about that key?"
            y "oh, right. i'll go talk to shady girl."
            jump basingse_day1

        if not first_arena_match:
            sg "welcome to the crabble royale, brother!"
            sg "you ready to get in on this nonsense!?"
            y "i.... have no idea what the fuck is happening."
            sg "sure, sure, i'll give you the run down."
            sg "you have crabs and i have crabs."
            y "....that's not good."
            sg "no, i mean... we have battling crabs."
            sg "Each crab type has different abilities and strengths, with rare and epic crabs being the most powerful."
            sg "you can level up your crabs in battles, but you can level up yourself by fighting crabs."
            sg "of course, you'll only level up your crab-battling abilities... you won't be a better earthbender or anything."
            y "i... think i get it."
            sg "i knew you would."
            if crab1 and crabs_current ==0:
                sg "whoa, that's a shit crab."
                sg "go talk to the shop girl. for real."
                jump basingse_day1
            $ first_arena_match = True
            jump bk3_arena_start_shit
        else:






            if crab1 and crabs_current ==0:
                sg "whoa, that's a shit crab."
                sg "go talk to the shop girl. for real."
                jump basingse_day1

            sg "snip snap, bitch."
            hide shadyguy_grin with dissolve
            jump bk3_arena_start_shit






















    if cheat_unlock and quest5:
        "\"no arena matches today - everyone's hungover from the celebration of the king's birthday.\""
        y "....still?"

        y "well, fair enough I guess."
        jump basingse_day1

    if cheat_unlock and not crab1:
        "\"no arena matches today - everyone's hungover from the celebration of the king's birthday.\""
        y "aw.... well, fair enough I guess."
        jump basingse_day1
    else:
        "\"no arena matches today - closed in celebration of the king's birthday.\""
        y "aw, man."
        jump basingse_day1


label bk3_arena_night:
    "arena is currently closed."
    jump basingse_night1

label bk3_palace:
    if nagina_free:
        if toph_slut <=4:
            y "this is most likely the last time i'll ever get the opportunity to do sexy stuff with toph."
            y "i should probably get her fully sexed up."
            y "i feel like i'm [toph_slut]/5 of the way there."
            jump basingse_day1

        "are you ready to leave the earth kingdom behind?"
        "(there will be no turning back.)"
        menu:
            "no, i want to do some other stuff":
                jump basingse_day1
            "yes, i'm ready":

                hide screen earth_money_date
                show toi toi04 with dissolve
                t "the walls are too high, and the gate is too heavily guarded."
                t "we need appa to get close to the king."
                y "yeah, but how are we going to find him?"
                t "blow on your whistle. duh."
                y "my what now?"
                show toi toi09 with dissolve
                t "your skybison whistle."
                t "you know, the one hanging on the chain around your neck."
                show bisonwhistle with dissolve
                y "oh fuck, so that's what that's for."
                y "speaking of missing team members, wasn't sokka supposed to come along?"
                y "and where the hell is katara!?"
                show toi toi04
                hide bisonwhistle
                with dissolve
                t "sokka was blabbering about wooing girls with his haiku skills..."
                t "so i guess he couldn't make it."
                t "katara went off to lake laogai."
                y "...why?"
                show toi toi09 with dissolve
                t "she wanted a swim? i don't know."
                t "she'll meet us there when we're finished."
                y "so it's just us two?"
                show toi toi07 with dissolve
                t "yeah, but i prefer that."
                show toi toi08 with dissolve
                t "more intimate that way."
                y "okay..."
                show toi toi04

                with dissolve
                y "well, the two of us should be enough if appa can drop us off right in the king's lap."
                show bisonwhistle with dissolve
                "you blow the skybison-shaped whistle."
                y "...there's no sound coming out of it."
                t "i don't think it's supposed to make sound we can hear."
                t "you know, just the kind that skybisons can."
                "you wait a few minutes and appa flies down from the sky."
                y "oh."
                y "neat."
                scene black with dissolve
                "he picks the two of you up and carries you away..."
                jump toph_appa_fuck
    if cheat_unlock:
        show toeg toeg01
        show guardb_body_1:
            xpos -500
        with dissolve
        y "um... i don't think i should go there."
        dl "hey, is that the avatar?"
        y "....yeah, i should go."
        jump basingse_day1
    else:

        jump meet_feng

label bk3_palace_night:
    show toeg toeg01
    show guardb_body_1:
        xpos -500
    with dissolve
    y "um... i don't think i should go there."
    dl "hey, is that the avatar?"
    y "....yeah, i should go."
    jump basingse_night1

label meet_feng:
    show toji toji01 with dissolve
    jd "avatar-"
    y "joo dee? what are you doing here?"
    show toji toji02
    show toji_smile
    with dissolve
    jd "i am here to give you some good news!"
    jd "your request to see the earth king has been granted!"
    y "really? great, because i'm on my way to-"
    jd "you'll be able to see him in four to six weeks."
    jd "that's much quicker than usual!"
    y "......"
    show toji toji01 with dissolve
    jd "so please return to your home for now."
    y "yeah.... that's not really gonna work for me."
    y "i'm going in."
    show toji_surprise
    hide toji_smile
    with dissolve
    jd "you must go home! you simply can't be here!"
    y "....why?"
    jd "there will be much trouble for both of us if you stay!"
    y "well, i'm going in, so you should get lost if you're so worried."
    jd "i... i...."
    hide toji_surprise
    hide toji toji02
    with dissolve
    "after a moment's hesitation, joo dee hurries off."
    "as you take a step to enter the palace, stone hands appear out of nowhere and cover your eyes and mouth."
    stop music fadeout 1
    play sound "audio/thud.mp3"
    scene black with sshake
    y "eegergerk."
    "they drag you into a room."
    y "you know, i should be panicking, but this sort of thing is honestly normal now."
    y "how fucked up is {i}my{/i} life."
    stop music fadeout 1
    play music "audio/Fire2.mp3"
    scene longfeng_room
    show tolf_fire
    with Dissolve(1.0)
    show ctc
    pause
    hide ctc
    "the stone hands drop from your face, and you find yourself in a well-lit room."
    y "cozy."
    show tolf tolf01
    show tolf_lf_fire
    with Dissolve(1.0)
    lf "i'm so glad that you approve."
    menu:
        "hello":
            y "hi there, another creepy person."
            y "your city is just full of weirdos, isn't it?"
            lf "........"
        "hey, have you choked on my dick? because you should, you twat":
            y "i mean, i don't approve, because i'm here against my will, but you fucking know that, you dick."
            lf "........"
    lf "...it is a great honor to meet you, avatar."
    lf "i am long feng, grand secretariat of ba sing se, and head of the dai lee."
    lf "i'd like to talk to you."
    y "oh, great, well why don't you make an appointment- oh, look at that, i'm already here."
    y "i wonder how i got here?"
    y "does kidnapping sound familiar?"
    y "because it feels familiar."
    lf "i-"
    y "because you kidnapped me."
    lf "....."
    lf "are you quite finished?"
    y "maybe."
    y "buttface."
    lf "....."
    lf "you-"
    show footlick_girlstands
    with dissolve
    slavegirl "my lord?"
    lf "*sigh...*"
    lf "go ahead."
    y "what...?"
    slavegirl "thank you, lord."
    hide footlick_girlstands with dissolve
    show head_girl:
        xpos 0.35 ypos 0.6
    with dissolve
    y "what... what is going on?"

    lf "hmm?"
    lf "oh, i don't know why she's doing this, really."
    y "i feel like you're lying to me."
    lf "....as i was saying...."

    show tolf_blink with dissolve
    lf "you are here to visit the king, and that will not happen."
    y "uh... why?"
    y "i have something to tell him about the war. i think."
    lf "the earth king-"
    hide tolf_blink
    show tolf tolf02
    with dissolve
    lf "girl, it's just a zipper!"
    lf "it's really not that complicated."
    slavegirl "i'm sorry!"
    lf "ugh, get out of my sight."
    slavegirl "yes, lord..."
    hide head_girl with dissolve
    show tolf_blink with dissolve
    lf "these slaves, i swear...."
    show tolf tolf01
    hide tolf_blink
    with dissolve
    lf "...but back to business."

    lf "the earth king has no time to get involved in political squabbles."
    y "i dunno, it seemed important."
    lf "the most important thing to the king is maintaining the cultural heritage of ba sing se."
    show tolf_blink with dissolve
    lf "it's my job to manage the military... and the rest of the city."
    y "kind of sounds like the king's a puppet. which is cool, no judgement."
    y "but i have to tell him about the eclipse or i won't get any pussy."
    y "oh, and i'm looking for my flying bear."
    show tolf tolf02
    hide tolf_blink
    with dissolve
    lf "it is the strict policy of ba sing se that the war not be mentioned within the walls."
    lf "it would cause chaos and destroy our culture, and i cannot allow you to jeopardize that."
    lf "ba sing se is a utopia because no one discusses the war."
    y "...i don't care?"
    lf "...."
    lf "if you mention the war to anyone, i will have no choice but to expel you from the city."
    lf "and you will not find your bison."
    y "...i still don't care. where's the king?"
    lf "........"
    lf "i see that you leave me no choice..."
    show toeg toeg03:
        xpos -450

    with dissolve
    lf "remove the avatar from my city."
    lf "leave him in one of those abandoned villages outside the walls."
    ya "hey, you can't just throw me out!"
    show tolf tolf01 with dissolve
    lf "well, i rather think i just did."
    ya "oh, i'm gonna kick-"
    stop music fadeout 2
    scene black with sshake
    "stone hands cover your face again."
    ya "this. is. bullshit!*"
    "*you mumble this."

    "with a forcible shove, you're launched from the city walls."
    show villagemap_day_base
    show ruined_buildings_1
    with sshake
    ya "aaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    y "oh, hey, i can see down shirts-"
    ya "-aaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!!!!!"

    play sound "audio/thud.mp3"
    with sshake
    ya "ow!"
    stop music fadeout 1
    play music "audio/Bumba Crossing.mp3"
    with sshake
    "you dust yourself off - you're miraculously unharmed - and turn back to yell at the walls."
    ya "yeah, well, i didn't want to be in your stupid city anyway!"
    ya "......"
    y "....okay i did, take me back!"
    y "....."
    y "anyone there?"
    y "it's gonna get dark soon!"
    y "......"
    y "then....i've decided i'd rather stay out here."
    y "....shit."
    y "alright, well, i knew something like this was gonna happen."
    y "i guess i'll just... stay out here tonight."
    y "I wonder how toph and katara are?"
    y "man, i'd love to see that short chick's boobs."
    y "........"
    y "damn, this village is a wreck."
    y "what happened here? why's it in ruins?"
    y "............."
    y "....if it rains, i'm gonna die."
    y "guess i'd better look around."
    show ctc
    pause
    hide ctc
    y "okay, it looks like this one in the center is the only one with any kind of shelter."
    y "well, shitty shack, here i come."
    scene bg_bk3_tophome_day with Dissolve(1.0)
    y "huh. i guess this isn't so bad."
    y "maybe there's a cot or something-"
    "you hear muffled shouting from outside."
    y "...what? who's even out here...?"
    "?????" "...kill him...."
    y "that's not good. that's really not good."
    y "who-"
    play sound "audio/thud.mp3"
    scene bg_bk3_tophome_day with vpunch
    show toph_enters with dissolve
    t "{size=+10}what did you do!?"
    y "oh. hi, toph."
    t "don't you \"hi, toph\" me!"
    hide toph_enters
    show toi toi51 with dissolve
    t "i tell you to go visit the king and next thing i know these stupid guards are after me!"
    t "so {i}what did you do{/i}!?"
    y "i didn't do any-"
    show toi toi01 with dissolve
    t "don't lie to me, twinkle toes!"
    y "well, it turns out the king isn't actually in control of the city."
    y "the actual ruler is an asshat named long feng, and he didn't want us to mention the war to the king."
    show toi toi09 with dissolve
    t "...what?"
    show toi_blink_ani
    t "so the king doesn't actually know about the war with the fire nation?"
    y "nope."
    t "did you at least tell this long feng guy about the eclipse?"
    y "he didn't seem particularly interested."
    t "how could you tell?"
    y "um. well i was upside down and airborne about 30 seconds later."
    y "so did they throw you out, too?"
    show toi toi04 with dissolve
    t "yeah right."
    show toi toi07 with dissolve
    t "those slowpokes didn't stand a chance."
    y "then... how did you know where to find me?"
    show toi toi04 with dissolve
    t "well, they were yelling that you were out here while chasing me."
    hide toi_blink_ani
    show toi_blink
    with dissolve
    t "....before i embedded them in the wall."
    y "oh."
    y "you've gotta teach me how to do that."
    show toi_blink_ani
    hide toi_blink
    with dissolve
    t "we'll... work our way up to that."
    show toi toi09
    with dissolve
    t "i hope katara's okay..."
    t "she was putting up those posters of appa you made when the guards came after us."
    y "i made those posters? is that what abba looks like?"
    t "....it's appa."
    show toi toi07 with dissolve
    t "and yeah, it looks just like him! you're really talented!"
    y "you really think so?"
    t "no!"
    hide toi_blink_ani
    show toi toi100
    show ctc
    pause
    hide ctc
    y "oh. you're... blind. right."
    y "you're a little difficult."
    show toi toi08 with dissolve
    t "no, i'm a {i}lot{/i} awesome."
    show toi toi06
    show toi_blink_ani
    with dissolve
    t "but now we need a plan."
    show blue_20perc_transparent with dissolve
    "the sun sets a little outside as you talk..."
    t "we can't just stay out here... not the way it is, anyway."
    y "oh, yeah, you're from the earth kingdom, right?"
    show toi toi10
    with dissolve
    t "...uh, duh."
    t "a different city, though."
    y "then do you know what happened out here?"
    show toi toi06
    with dissolve
    t "no, but i bet it was the fire nation."
    t "i heard there were a bunch of little villages outside the walls once."
    t "then they lay siege to the city for something like six years straight."
    t "any villages outside the walls would have been completely wrecked."
    y "which is probably what happened here."
    t "probably."
    y "hey... is it just me or is it getting darker?"
    t "....."
    y "oh. right."
    y "well, should we go find katara?"
    t "....i'm sure she's okay. katara can take care of herself."
    t "besides, sokka's with her."
    show toi toi04 with dissolve
    t "...although that's probably cause for worry, actually."
    t "we'll look for them tomorrow."
    t "get some rest, your training starts in the morning."
    t "and then we'll search for her."
    y "ugh... i hate mornings."
    t "deal with it."
    y "so which room is mine?"
    t "...room?"
    t "you're not sleeping here."
    y "....what?"
    y "but... but..."
    t "\"but... but...\" there's only space for one of us."
    t "and i'm a girl."
    t "so i get the shack."
    y "i can just sleep in the corner-"
    t "shoo!"
    t "i'm gonna clean off before bed."
    hide toi toi04
    hide toi_blink_ani
    with dissolve
    y "aw, man...."
    scene black
    scene villagemap_night_base
    show ruined_buildings_night

    with dissolve
    y "....."
    y "{size=+10}this isn't fair!!"
    y "ugh, guess i have to find a crappy ruin to sleep in."
    y "or... i could peek on toph, since she's gonna bathe..."

    menu:
        "go to sleep":
            y "nah, don't need her pissed."
            y "i'll just sleep here... in the open..."
            y "like a hobo."
            y "aw man, am i a hobo now?"
            y "........"
            y "man...."
            $ toph_peek = False
            scene black with dissolve
        "peek on toph":

            $ toph_peek = True
            y "no harm in a quick peek through the window..."
            scene black
            scene bg_bk3_tophome_day
            show toph_windowsil
            show blue_30perc_transparent
            show tub
            show tocl tocl107
            with dissolve
            show ctc
            pause
            hide ctc
            y "(nice!)"
            show ctc
            pause
            hide ctc
            show tocl tocl100 with dissolve
            show ctc
            pause
            hide ctc
            y "(what a fine little ass....)"
            show ctc
            pause
            hide ctc
            show tocl tocl107 with dissolve
            t "a firebender wouldn't have to deal with cold water..."
            show ctc
            pause
            hide ctc

            show tocl tocl101 with dissolve
            show ctc
            pause
            hide ctc

            show tocl tocl102 with dissolve
            show ctc
            pause
            hide ctc
            t "oh, shoot, i forgot my legs..."
            show tocl tocl107 with dissolve
            show ctc
            pause
            hide ctc

            y "man, this is great-"

            show tocl tocl09
            show tocl_angry
            show tocl_blush
            with vshake
            t "what the hell!?"
            y "oh, hey, uh-"
            play sound "audio/thud.mp3"
            scene black with sshake
            show ctc
            pause
            hide ctc
            scene bg_bk3_tophome_night with dissolve
            yc "ugh... what happened..."
            y "are these... rocks holding down my arms?"
            show toi toi05
            show toi_blush
            with dissolve
            t "what do you think you're doing, aang!?"
            y "just... you know... making sure you're okay..."
            t "i'd be more okay if you weren't trying to... you know..."
            y "....look at your bomb-ass titties?"
            show toi_blink with dissolve
            t "...."
            show toi toi101
            $ renpy.pause(1.0)
            y "{size=+10}ow!"

            y "....you hit me!"
            y "you could have broken my nose!"
            hide toi_blink with dissolve
            t "then maybe i should try again!?"
            y "alright, alright, i won't try that again."
            t "good! and you're gonna stay there, trapped, until morning."
            y "um... maybe don't?"
            t "no."
            hide toi toi101
            hide toi_blush
            with dissolve

            "Uncomfortable as you are with your hands trapped in rock, you're too tired to stay awake for long and soon fall asleep."
            scene black with dissolve

    "You lie down and only after tossing and turning for awhile do you finally manage to drift off."
    stop music 
    play music "audio/Dreams Become Real.mp3"
    show n_stance01_big_gloweye with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "who.... who's there....?"
    "you feel a pull... a desire..."
    "burning lust rushes through your body.... a hunger like you've never experienced..."
    "...and just as quickly as it came, it leaves..."
    stop music
    play music "audio/Bumba Crossing.mp3"
    hide n_stance01_big_gloweye with Dissolve(1.5)
    if toph_peek:
        scene bg_bk3_tophome_day with dissolve
    else:
        scene villagemap_day_base
        show ruined_buildings_1
        with dissolve
    y "what... what..."
    y "what the fuck."
    y "i... i don't think i liked that."
    y "something's watching me."
    y "it's probably that damn ugly snake thing."
    if not toph_peek:
        y "guess i'll check in on toph."
        scene black
        scene bg_bk3_tophome_day
        with dissolve

    show toi toi10
    show toi_blink
    with dissolve
    t "*yaaawn*"
    show toi toi07
    hide toi_blink
    with dissolve
    t "goooooood morning earthbending student!"
    y "i... guess?"
    if toph_peek:
        y "sooo... can you get these rocks off?"
        show toi toi05 with dissolve
        t "....what!?"
        y "off my arms! get the rocks off my arms!"
        show toi toi09 with dissolve
        t "oh..."
        y "or we can be talking about my balls."
        y "you know."
        y "whatever."
        show toi toi06
        show toi_blink
        with dissolve
        t "....."
        with sshake
        "with a slight stance change, toph sets you free."

    t "now...."
    show toi toi05
    hide toi_blink
    with dissolve
    t "get outside right now!"
    t "if you're not out in five seconds, you're going to have to dig your way out!"
    y "hey, don't get {i}short{/i} with me."
    t "...."
    y "get it?"
    t "four seconds."
    hide toi toi05 with dissolve
    y "...grump."
    scene black
    scene villagemap_day_base
    show ruined_buildings_1
    with dissolve
    show toi toi50 with dissolve
    t "alright, let's get started."
    y "....how?"
    y "there's all this crap out here, we're gonna trip on something."
    y "the only usable building is the one in the middle that you're staying in."
    hide toi toi50 with dissolve
    show toi toi02 with dissolve
    t "wow, what a great point."
    t "whatever will we do?"

    hide toi toi02

    show toph_body_cloth with dissolve

    t "hnngh...."

    play sound "audio/earthquake.mp3"
    hide toph_body_cloth
    show ruined_buildings_1
    show toph_body_cloth
    with vpunch
    hide ruined_buildings_1 with Dissolve(2.0)
    "with a grunt and a smooth motion, toph sinks the ruins and repairs the outside of the shack."
    hide toph_body_cloth with dissolve
    show toi toi06 with dissolve
    t "there."
    y "uh...."
    y "that was kind of fucking amazing."
    show toi toi10
    show toi_blink
    with dissolve
    t "hnk..."
    play sound "audio/spit.mp3"
    show toi toi09 with dissolve
    t "ppt."
    show toi toi08
    hide toi_blink
    with dissolve
    t "no big deal."
    show toi toi02 with dissolve
    t "now, let's start your training."
    menu:
        "train me":
            $ earthbending = 1
            y "alright, so what are you gonna teach me?"
            y "rock-slide? land-whirlpool?"
            y "how to make a cage for housing horny sluts?"
            show toi toi09 with dissolve
            t "....no. what is wrong with you?"
            y "i'm just so lonely."
            t "right."
            t "well...."
            t "....we're gonna start with...."
            show toi toi02
            show toi_blink
            with dissolve
            t "moving.... a rock."
            y "oh. uh. that's cool, too."
            hide toi_blink with dissolve
            t "the key to earthbending is your stance."
            t "you have to be steady and strong."
            show toi toi06 with dissolve
            t "rock is a stubborn element - if you want to move it, you've got to be like a rock yourself."
            y "like a rock. sure."
            y "got it."
            y "i'm ready."
            t "then stop this boulder!"
            hide toi toi06
            show toi toi51
            show big_rock at truecenter
            with sshake
            y "{size=+10}aaaahhhhh!!!!!"
            scene black with sshake
            show ctc
            pause
            hide ctc
            scene villagemap_day_base with dissolve
            y "uuhghh...."
            y "i don't want to be at space camp anymore, mom...."
            show toi toi09 with dissolve
            t "what are you doing?"
            y "bl... bleeding..."
            t "well... stop it."
            show toi toi04 with dissolve
            t "you haven't moved a rock yet."
            y "i'm sort of... stuck here..."
            t "fine. here."
            show toi toi03 with dissolve
            t "you did pretty well, considering."
            y "really? you think i did alri-"
            show toi toi01 with sshake
            t "no!"
            "toph launches you into the air as you reach for her hand."
            "you land on your butt, but manage to get back up."
            y "okay.... well.... what if came at it from a different angle?"
            show toi toi05 with dissolve
            t "no! that's the problem. you're thinking like an airbender."
            y "i am? wow, you're teaching me two elements at once!"
            y "i'm a natural!"
            show toi toi09 with dissolve
            t "what?"
            t "you're already an airbender."
            y "i am?"
            y "has this come up before?"
            show toi toi06 with dissolve
            t "are you drunk?"
            t "how badly did you hit your head?"
            y "i mean.... hard?"
            y "but i think i'm functional."
            show toi_blink with dissolve
            t "well... there's no \"different angle\" or trickity-trick that's gonna move that rock."
            t "you gotta nut up and stare it down."
            hide toi_blink with dissolve
            y "alright, i'll just-"
            t "here, this should help."
            show big_rock at truecenter
            with sshake
            "toph drops a massive boulder on you that you can barely hold."
            show toi toi01 with dissolve
            t "keep your knees high, twinkle toes!"
            y "this seems so unnecessary!"
            t "you're unnecessary!"
            y "......why are you so mean to me!?"
            y "....and how does this help anything?"
            y "....why am i working out my shoulders?"
            y "this is so duuuuumb!!"
            show toi toi06
            show toi_blink
            hide big_rock
            with sshake
            "you eventually fall over under the weight of the boulder."
            "you learn nothing."
            y "this is useless."
            t "you certainly are."
            y "okay, you're being kind of a jerk."
            show toi toi04 with dissolve
            t "what's wrong? baby gonna cry?"
            y "i'm not a baby!"
            y "i'm a big boy!"
            y "that... came out wrong."
            y "look, can we do something else?"
            hide toi_blink with dissolve
            t "fine. we need to go find katara anyway."
            jump look_for_katara
        "look for katara instead":

            y "i really think we should go look for katara instead."
            t "sounds like you're chickening out."
            t "...but fine, we'll go make sure she's okay."
            jump look_for_katara

label look_for_katara:
    $ quest2 = True
    t "come with me."
    scene black with dissolve
    scene basingse_outerwall1
    with dissolve
    "you follow toph to the city wall."
    show toi toi04 with dissolve
    y "uh... not to second-guess you, short stuff, but how exactly are we gonna get into the city?"
    t "...."
    show toi toi02 with dissolve
    t "i'm an earthbender, aang."
    t "watch this."
    play sound "audio/earthquake.mp3"
    scene black
    scene basingse_outerwall
    hide toi toi02
    show toi toi02
    with sshake
    y "uh... holy shit."
    show toi_blink with dissolve
    t "right?"
    t "i'm the best."
    hide toi_blink with dissolve
    t "come on."
    scene black with dissolve
    stop music
    play music "audio/jangles.mp3"
    scene market_general
    hide toi toi02
    show toi toi02
    with dissolve
    "toph opens up a hole in the city walls, and the two of you find yourselves in the market."
    y "oh, cool."
    t "hmm... the market..."
    t "i've got an idea."
    t "i know we've got to look for katara, but.... we could use some money."
    $ we_poor = True
    show screen earth_money_date 

    t "see? we're about as poor as it gets."
    if emoney >15:
        t "umm.... did you steal this money?"
        t "you're no good to us if you're arrested."
        t "i'm confiscating this."
        $ emoney =0
        t "there."
        t "{i}now{/i} we're as poor as it gets."
        y "......"
    y "so... how are we supposed to change that?"
    t "we can work together, run some scams."
    t "you play the games and i'll distract the people."
    y "what about katara?"
    t "eh, she's not going anywhere."
    t "wanna run a quick scam before we look for her?"
    $ cheat_unlock = True
    menu:
        "look for katara":
            y "i really think we should make sure she's safe."
            t "oh fine. let's go find katara."
            y "any idea where we should look first?"
            show toi toi09 with dissolve
            t "hm..."
            y "hell, she could be lost somewhere in the market and it'd take us all day to find her."
            t "that's a good point."
            show toi toi04 with dissolve
            t "let's split up, we'll cover more ground that way."
            t "i'll stay here and search for her."
            t "you go look elsewhere."
            y "by myself? but... it's a big city..."
            t "stop whining, i'm covering the whole market."
            show toi toi06 with dissolve
            t "now get to it!"
            hide toi toi06 with dissolve
            jump basingse_day1
        "run a quick scam":

            t "great!"
            t "someone's playing {b}cups{/b} over there."
            t "hey! lady!"
            jump dicecups_start


label bk3_market_shop:
    if crab1 and shady_explain:
        show azss azss01 with dissolve
        if toph_katara_chair ==4:
            ss "you need it, i got it."
            ss "scrolls, knives, herpes, building materials..."
            y "what was that middle one?"
            ss "...knives?"
            y "right."
            y "did shady give you a key?"
            ss "yeah."
            ss "don't know why he bought a key he didn't have a use for..."
            ss "but i'm not the mastermind here."
            ss "you need it?"
            y "yeah, how much?"
            ss "hmm...."
            ss "tell you what..."
            ss "i'm trying to start my own business, see?"
            y "oh, no...."
            ss "yeah, shady doesn't offer dental."
            ss "how messed up is that?"
            y "look, i'm just trying to get a key, not get mixed up in capitalism."
            ss "we can help each other, here."
            ss "you invest 200 coins in my shop, and i'll give you the key."
            y "that's... a lot of money."
            y "you don't even want the damn key!"
            ss "alright, alright, tell you what i can do..."
            ss "how about... you invest the 200 and i'll deliver the key to the owner myself."
            y "that's... not better."
            ss "aaaaand.... I'll flash you whenever you want."
            ss "how's that?"
            y "...."
            y "fine! deal."
            y "slut."
            ss "mmm... don't tease me."
            $ toph_katara_chair = 5

        if toph_katara_chair ==5:
            if emoney >=200:
                ss "it looks like you've got the 200."
                ss "wanna hand it over?"
                menu:
                    "no":
                        y "not really."
                        ss "alright, come back when you're ready, and I'll deliver the key."
                        ss "and show you my tits."
                        jump bk3_market
                    "yes":

                        $ emoney -=200
                        ss "great! here you go!"
                        play sound "audio/win2.mp3"
                        "you got the cupboard key!"
                        ss "i'll go ahead and take it over to the proper owner..."
                        y "katara."
                        ss "right, katara."
                        ss "oh, and... here."
                        show azss azss102
                        show ctcblink
                        $ renpy.pause()
                        hide ctcblink
                        y "nice."
                        ss "done?"
                        y "sure."
                        show azss azss01
                        with dissolve
                        ss "come back any time."
                        $ toph_katara_chair = 6
                        jump bk3_market
            else:

                ss "come back when you have 200 coins."
                jump bk3_market

        if toph_katara_chair >= 4 and toph_katara_chair <7:
            ss "i delivered the key to that katara chick already."

        ss "what can i do for ya?"
        jump bk3_market_menu

    if crab1 and not shady_explain:
        show azss azss01 with dissolve
        ss "what can i do for ya?"
        y "where's shady?"
        ss "he's over at the arena."
        ss "i've taken over his shop here."
        ss "so, what'll it be?"
        $ shady_explain = True
        jump bk3_market_menu

    if bk3_shady_met:
        show shadyguy_grin with dissolve
        sg "hey, buddy!"
        sg "what can i get ya?"
        jump bk3_market_menu
    else:

        show shadyguy_grin with dissolve
        sg "hey, there! welcome to shady enterprises, LLC!"
        sg "what can i do for you?"
        y "hey man! it's me!"
        show shadyguy_unsure with dissolve
        sg "i'm... sorry? do we know each other?"
        y "I-"
        y "oh. uh, right. no, not yet."
        sg "...what do you mean \"not yet\"?"
        y "well... we're about to know each other."
        sg "...."
        hide shadyguy_unsure with dissolve
        sg "heh, i like that!"
        sg "i'm gonna use that."
        sg "\"hey there, we know each other in the future.... starting now.\""
        sg "trippy."
        y "right..."
        y "....wait, did you say \"shady enterprises\"?"
        sg "llc."
        sg "and yeah, my empire is blowing up, man."
        sg "i've got slave girls everywhere, running businesses and gambling operations all over."
        sg "it's awesome."
        y "huh."
        show shadyguy_unsure with dissolve
        sg "i'm a little worried though..."
        sg "there's been some talk about pulling my slavegirl permit."
        sg "...bunch of corporate assholes intimidated by my expanding business."
        hide shadyguy_unsure with dissolve
        sg "but i'm sure it'll be fine."
        sg "if not, i'll just move to the fire nation."
        sg "lots of opportunity there right now."
        y "um. sure."
        show shadyguy_unsure with dissolve
        sg "you seem unsure about that."
        y "no, no. i'm sure it'll work out."
        sg "......"
        hide shadyguy_unsure with dissolve
        sg "so! what can i sell ya?"
        $ bk3_shady_met = True
        jump bk3_market_menu

label bk3_market_menu:












    menu:
        "why do you sell this stuff?":
            if shady_explain:
                ss "i just do what shady tells me."
                jump bk3_market_menu
            else:
                sg "real estate, man."
                sg "shit's blowing up."
                jump bk3_market_menu

        "wood (5) - 25" if not house_wood:
            if emoney >=25:
                $ house_wood = True
                $ bk3_wood +=5
                $ emoney -=25
                play sound "audio/win2.mp3"
                "you got 5 wood!"
                jump bk3_market_menu
            else:
                "not enough money...."
                jump bk3_market_menu

        "wood (5) - 25 (currently sold out)(locked)" if house_wood and not village_dev_explain2:
            "test"

        "wood (5) - 25 (have [bk3_wood])" if house_wood and village_dev_explain2:
            if emoney >=25:
                $ bk3_wood +=5
                $ emoney -=25
                play sound "audio/win2.mp3"
                "you got 5 wood!"
                jump bk3_market_menu
            else:
                "not enough money...."
                jump bk3_market_menu

        "steel (5) - 25" if not house_steel:
            if emoney >=25:
                $ house_steel = True
                $ bk3_steel +=5
                $ emoney -=25
                play sound "audio/win2.mp3"
                "you got 5 steel!"
                jump bk3_market_menu
            else:
                "not enough money...."
                jump bk3_market_menu

        "steel (5) - 25 (currently sold out)(locked)" if house_steel and not village_dev_explain2:
            "test"

        "steel (5) - 35 (have [bk3_steel])" if house_steel and village_dev_explain2:
            if emoney >=35:
                $ bk3_steel +=5
                $ emoney -=35
                play sound "audio/win2.mp3"
                "you got 5 steel!"
                jump bk3_market_menu
            else:
                "not enough money...."
                jump bk3_market_menu

        "wench outfit - 75" if june_free and not wench_outfit:
            if emoney >=75:
                $ emoney -=75
                play sound "audio/win2.mp3"
                "you got the wench outfit!"
                $ wench_outfit = True
                jump bk3_market_menu
            else:
                "not enough money...."
                jump bk3_market_menu

        "flash me!" if toph_katara_chair >=6:
            ss "here you go, free of charge."
            show azss azss102
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            y "nice."
            ss "done?"
            y "sure."
            show azss azss01
            with dissolve
            jump bk3_market_menu
        "back":

            jump bk3_market

label bk3_village:
    if bk3_loveroute:
        jump love_bk3_village
    if bk3_day:
        jump bk3_village_day
    else:
        jump bk3_village_night

label bk3_village_day:
    stop music fadeout 1
    play music "audio/Bumba Crossing.mp3"
    $ bk3_day = True
    jump bk3_village_background

label bk3_village_night:
    stop music fadeout 1
    play music "audio/Blue_Dot_Sessions_-_06_-_Night_Light.mp3"
    $ bk3_day = False
    jump bk3_village_background

"test"

label bk3_next:
    if bk3_loveroute:
        jump love_bk3_next

    $ tophs_home_access = True
    if toph_free and appa_free:
        if naga_battle and not nagina_free:
            hide screen earth_money_date
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            scene black with Dissolve(1.5)
            scene bg_dream with Dissolve(1.5)
            show tonb tonb101 with Dissolve(1.5):
                parallel:
                    xpos -1000
                    linear 1.0 xpos 0
                parallel:
                    ypos 0
                    linear 1 ypos 15
                    linear 1 ypos 0
                    repeat
            y "oh goddamnit..."
            y "please, no more..."
            nag "{i}i am pleasssed that you sssurvived."
            y "yeah, me too..."
            nag "{i}the barriersss are up."
            nag "{i}you are sssafe... for now."
            nag "{i}and now i leave your mind..."
            nag "{i}goodbye...."
            nag "{i}for now."
            hide tonb tonb101 with dissolve
            $ nagina_free = True
            y "......"
            y "she is fucking ominous."

        if not naga_battle:
            hide screen earth_money_date
            stop music
            play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
            scene black with Dissolve(1.5)
            scene bg_dream with Dissolve(1.5)
            show tonc_floats:
                parallel:
                    xpos 400
                    linear 8.2 xpos 300
                    linear 7.0 xpos 400
                    repeat
                parallel:
                    ypos 150
                    linear 8.0 ypos 50
                    linear 7.4 ypos 150
                    repeat
            with Dissolve(1.5)

            $ nagachibi_head = 'up'
            "{i}it isss time..."
            y "for what?"
            "{i}for our fight... with the other naga..."
            y "uh, right now?"
            "{i}only if you wisssh..."
            "{i}i will wait here... in your dreamsss..."
            menu:
                "battle of the snakes":
                    $ naga_battle = True
                    jump nagas_battle
                "not yet":

                    "{i}very well..."


    if bk3_handjob ==1:
        scene black
        with Dissolve(0.2)
        k3 "wake up, sleepy head."
        scene inside_shack
        show toki toki01
        with eye_open
        with dissolve
        y "wha... whaz it?"
        y "katara?"
        k3 "good morning."
        show toki_angry
        with dissolve
        k3 "we have a problem."
        y "ugh, let me go back to sleep..."
        show toki_surprised
        hide toki_angry
        with dissolve
        k3 "hey!"
        show black
        with eye_shut
        k3 "oh, no you don't!"
        k3 "it's morning, get up!"
        with vshake
        ya "{size=+5}ow!"
        scene black
        scene inside_shack
        show toki toki02
        show toki_angry
        hide toki_surprised
        with eye_open2
        ya "did you just pinch me!?"
        ya "why are you even here?"
        k3 "I told you! there's a problem!"
        y "*yaawn*"
        y "fine, what is it?"
        y "and do i get a blowjob for fixing it?"
        show toki_blink with dissolve
        k3 "pay attention, aang!"
        y "oh, this is serious."
        hide toki_blink with dissolve
        k3 "that's what i've been saying!"
        k3 "toph is missing!"
        y "toph? pfft. i'm sure she's fine."
        y "she can handle anybody."
        y "well, almost anybody."
        y "i'm pretty great."
        k3 "i'm telling you, something's wrong."
        k3 "there's signs of a struggle outside her house."
        k3 "i went for my morning oral-"
        y "your... what?"
        show toki_blink with dissolve
        k3 "be quiet and listen!"
        k3 "i went to her house and there are odd tracks and everything."
        hide toki_blink with dissolve
        k3 "we need to move fast."
        y "alright, fine. I'm awake, you've got me sufficiently worried."
        ya "and pissed."
        ya "no one fucks with papa bear's sluts."
        show toki toki01 with dissolve
        k3 "...."
        k3 "are you-"
        ya "yes, i'm obviously papa bear."
        ya "in fact, that is my new name."
        ya "you shall now only refer to me as papa bear."
        ya "is that clear?"
        show toki toki02
        hide toki_angry
        show toki_blink
        with dissolve
        k3 "*sigh...*"
        k3 "very well, papa bear."
        y "eh, i'm over it."
        y "but i love your dedication."
        y "okay, let's go save my bitch."
        show toki toki04
        hide toki_blink
        show toki_smile
        with dissolve
        k3 "i love when you get fired up."
        ya "shut it."
        show toki_blink with dissolve
        k3 "mmmm..."
        y "....riiiight."
        y "okay, let's go."
        scene black with dissolve
        $ bk3_handjob = 2
        $ room5.sp_item = True

    if toph_tunnel_training ==3:
        $ toph_tunnel_training = 4
        hide screen earth_money_date
        stop music
        play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
        scene black with Dissolve(1.5)
        scene bg_dream
        show tonb tonb101:
            parallel:
                xpos -1000
                linear 1.0 xpos 0
            parallel:
                ypos 0
                linear 1 ypos 15
                linear 1 ypos 0
                repeat
        with Dissolve(1.5)
        "{i}avatar...."
        y "oh, good, it's you."
        y "we need to talk."
        "{i}.........."
        y "in the tunnels, you mentioned that you're in my mind because i have the eyes from your statue."
        "{i}yessss...."
        y "so, what's to stop me from throwing them away?"
        "{i}i am helping..."
        y "helping?"
        "{i}keeping the hallucinationssss away..."
        y "oh. right."
        y "well, i don't like that you're in my head."
        y "and three spirits is too many to deal with."
        y "you, the real naga-dreamstealer, and the painted lady."
        y "that's a problem."
        "{i}i am not happy either..."
        y "why?"
        "{i}weak... i am weak..."
        "{i}i fight the hallucianationsss... tired..."
        y "you're fighting them now? in my head?"
        "{i}yesss...."
        "{i}i fear they will kill me..."
        "{i}and being ssstuck in the mind of another isss ssshitty..."
        y "hey, that's my brain we're talking about."
        "{i}yesss...."
        y "....that was a little more sassy than necessary, but i'll let it slide."
        y "so what do you want?"
        "{i}more control... and freedom..."
        y "yeah... no."
        y "not happening."
        y "so... i can throw away your eyes, but the hallucinations will return..."
        y "or i can keep your eyes, but you will remain in my head, and i can't really trust you."
        "{i}.............."
        menu:
            "discard the eyes":
                $ nagas_eyes = 1
                y "yeah, i think i'll risk the craziness."
                "{i}no..."
                y "you... don't really get a say."
                "{i}wait..."
                "{i}i do not want to disssappear...."

                "{i}i have my own identity...."
                "{i}i have another sssuggessstion..."
                y "....okay, i'm listening."
                "{i}let me reunite with the true naga..."
                y "that sounds like a terrible idea."
                y "why would i want that?"
                "{i}i will have the power to place permanent barriersss in your mind..."
                "{i}and... i will be friendly..."
                y "you will be friendly? really? that's what you offer?"


                "{i}i have protected you... with nothing in exchange..."
                y "except for your own life."
                "{i}*hisssss....*"
                "{i}what have i ever done to make you dissstrussst me...."
                "{i}you sssnake racissst..."
                y "that's... not a real thing."
                y "and you've tried to kill me in the past!"
                "{i}you underssstand nothing..."
                y "then explain it to me."
                "{i}sssoon...."
                y "ugh."
                "{i}i have helped you... and i will help you..."
                "{i}i am not the original naga... i am my own..."
                "{i}you have given me life... in a way..."
                "{i}and i will repay you..."
                "{i}i tell no liesss..."
                "{i}trussst me..."
                y "let's say i believe you."
                y "how would you even reunite with her?"
                "{i}let her enter your mind... and i will consssume her..."
                y "what!? that's insane! no way."
                y "why would i ever agree to that?"
                "{i}i have more power than her here..."
                "{i}she will lose...."
                y "yeah, a fight in my fucking {i}mind{/i}!"
                y "how much damage would that cause?"
                "{i}none..."
                "{i}though the fight will be... dangerousss..."
                y "explain."
                "{i}our fight would challenge your perceptionsss..."
                "{i}if you sssurvive our fight... with your awarenessss intact... there will be no damage..."
                y "i don't like the sound of that... especially since you may not win, and then she's in my head."
                "{i}i will win..."
                "{i}i was born here..."
                y "that's... weird."
                "{i}i am... in a sssenssse... your mind-child..."
                y "that is very, very weird."
                "{i}but i am naga, too... and i am older than you can fathom..."
                "{i}trussst..."
                "{i}better than the one you fight now...."
                y ".............."
                y "*sigh* that's probably true."
                y "but first, tell me..."
                y "who was the other statue in the tunnels? who is the other snake lady?"
                "{i}....."
                y "tell me or i let you die."
                "{i}you would not dare...."
                y "look into my fucking brain and say that again."
                "{i}..........."
                y "now, tell me."
                "{i}ssshe...."
                "{i}isss my sssissster...."
                y "who?"
                "{i}.........."
                y "i would guess the painted lady, but she doesn't look like a snake."
                "{i}..........."
                y "unless she's in disguise?"
                "{i}.........."
                y "or she's a misdirect?"
                "{i}.........."
                y "I can kill you, you know."
                "{i}sssome thingsss are worth risssking death..."
                y "........"
                y "....oh, fine."
                y "let me consider it."
                "{i}do not wait long...."
                "{i}i may not sssurvive much longer..."
                scene black with Dissolve(1)
            "keep the eyes":

                $ nagas_eyes = 2
                y "i think i'll keep the eyes, you're doing fine fighting the crazy."
                "{i}good..."
                hide tonb
                show naga_chibi:
                    ypos 0
                    linear 1 ypos 15
                    linear 1 ypos 0
                    repeat
                with flash
                show ctc
                pause
                hide ctc
                y "what... just happened?"
                "{i}I am pressserving my energy..."
                y "......"
                y "you're adorable!"
                "{i}hisss..."
                y "aww... who's a little cutie? you are! yes you are!"
                "{i}ssstop it..."
                y "i'm still super not sure that i can trust you."
                y "i mean, you do keep trying to invade my mind."
                "{i}not invade... roam..."
                y "those don't seem that different."
                "{i}i have protected you... with nothing in exchange..."
                y "except for your own life."
                "{i}*hisssss....*"
                "{i}what have i ever done to make you dissstrussst me...."
                "{i}you sssnake racissst..."
                y "that's... not a real thing."
                y "and you've tried to kill me in the past!"
                "{i}you underssstand nothing..."
                y "then explain it to me."
                "{i}sssoon...."
                y "ugh."
                "{i}i have helped you... and i will help you..."
                "{i}i am not the original naga... i am my own..."
                "{i}you have given me life... in a way..."
                "{i}and i will repay you..."
                "{i}i tell no liesss..."
                "{i}trussst me..."
                y "....are you really different from the original naga?"
                "{i}i was born here...."
                y "that's... weird."
                "{i}i am... in a sssenssse... your mind-child..."
                y "that is very, very weird."
                "{i}but i am naga, too... and i am older than you can fathom..."
                "{i}trussst..."
                y "look, i'm willing to give you a chance."

                y "but tell me..."
                y "who was the other statue in the tunnels? who is the other snake lady?"
                "{i}....."
                "{i}ssshe...."
                "{i}isss my sssissster...."
                y "who?"
                "{i}.........."
                y "i would guess the painted lady, but she doesn't look like a snake."
                "{i}..........."
                y "unless she's in disguise?"
                "{i}.........."
                y "or she's a misdirect?"
                "{i}.........."
                y "....oh, fine."
                y "but we're not finished talking."
                scene black with Dissolve(1)


    if naga_toph_old ==7:
        hide screen earth_money_date
        stop music
        play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
        scene black with Dissolve(1.5)
        scene bg_dream
        show tonb tonb101 with Dissolve(1.5):
            parallel:
                xpos -1000
                linear 1.0 xpos 0
            parallel:
                ypos 0
                linear 1 ypos 15
                linear 1 ypos 0
                repeat
        with Dissolve(1.5)
        y "okay, spirit."
        y "i'm tired."
        y "this is... bad."
        y "who are you? really?"
        "{i}i am naga.... a ssshadow of naga...."
        y "naga."
        y "help me. what is going on?"
        y "where is the painted lady?"
        "{i}ssshe is not your ally...."
        y "and you {i}are{/i}?"
        "{i}yesss..."
        y "forgive me if i don't believe you."
        y "i don't think either of you are trying to help me."
        y "you're clearly both after something, and won't tell me what it is."
        "{i}hisssssss........."
        y "so what are you doing to my head?"
        "{i}nothing!"
        "{i}ssshe did thisss!"
        y "the painted lady? how?"
        "{i}hisssss...... nooo....."
        "{i}but i am not your enemy....."
        y "but you're not my friend, either."
        "{i}let me help you...."
        "{i}thessse memoriesss.... they are bleeding through time...."
        "{i}they will kill you...."
        "{i}they will kill usss...."
        y "who is \"us\"?"
        "{i}i am.... here in your mind.... trapped...."
        "{i}i.... don't underssstand why...."
        "{i}thisss hasss never happened before...."
        "{i}let me help you...."
        "{i}i can protect you...."
        y "no."
        y "why are you so interested in protecting me?"
        "{i}hissssss....."
        y "you and the painted lady... you need me for something."
        "{i}hisssssss......."
        y "answer me!"
        "{i}yesss....."
        y "what is it?"
        "{i}hiisssssss...... noo........"
        y "fine. is that the only reason you want to \"help\" me?"
        "{i}i....."
        "{i}.........."
        "{i}i don't want to.... die...."
        y "you can die?"
        "{i}i am.... not naga...."
        "{i}i am.... a ssshadow...."
        "{i}but i am here...."
        "{i}if you die.... i die...."
        "{i}let me help you...."
        "{i}give me free reign of your mind.... i don't need much...."
        y "and lose my free will?"
        y "no."
        y "I'd rather die."
        "{i}i wouldn't take it all.... jussst sssome..."
        y "no. my mind is my own."
        "{i}hissss....."
        "{i}fine!"
        "{i}i will.... try to keep the memoriesss away...."
        "{i}but alone.... i am.... weak...."
        y "i'm not giving you power over me, naga."
        "{i}very well.... i will protect you.... usss...."
        y "how do i know it's not you secretly doing this?"
        "{i}becaussse... it hurtsss me..."
        y "it hurts you when i am hurt?"
        "{i}yesss... and it will hurt... to keep them away..."
        "{i}i will help you... without payment... for now..."
        "{i}but remember who isss.... helping keep you alive...."
        "{i}call on me... when you wisssh for small comfort..."
        "{i}in dreamsss i cannot bring you to completion...."
        "{i}but i am ssstill here...."
        $ naga_toph_old = 8

    if naga_toph_old == 5:
        hide screen earth_money_date
        stop music
        play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
        scene black with Dissolve(1.5)
        scene bg_dream
        show tonb tonb101 with Dissolve(1.5):
            parallel:
                xpos -1000
                linear 1.0 xpos 0
            parallel:
                ypos 0
                linear 1 ypos 15
                linear 1 ypos 0
                repeat
        with Dissolve(1.5)
        y "okay, what the fuck is happening to me?"
        y "why am i seeing things that... aren't there?"
        "{i}i can only guessss...."
        y "what?"
        y "i know it's you doing this to me!"
        "{i}it isss not..."
        y "don't lie to me, crazy snake-boobed demon."
        y "you're the one with powers over illusion, right?"
        "{i}ssspirit... not demon..."
        "{i}and yessss... but thesssse... aren't illusionsss..."
        y "then what are they?"
        "{i}memoriesss..."
        y "i don't remember these things."
        "{i}but you will..."
        y "ugh. fucking time travel."
        y "okay, you say they're memories, but one of them hurt me."
        y "if they're just memories-"
        "{i}thessse are not normal memoriesss..."
        "{i}they have mutated... they are angry..."
        "{i}they have been pulled from where they belong..."
        "{i}they can hurt you...."
        y "can you stop it?"
        "{i}yesss..."
        "{i}for a price..."
        y "......no."
        y "no, i give you no power over me."
        "{i}without me, you may die..."
        y "better to die a man than live a slave."
        "{i}that isss foolisssh...."
        y "leave me alone."
        $ naga_toph_old = 6

    if naga_toph_old == 2:
        hide screen earth_money_date
        stop music
        play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
        scene black with Dissolve(1.5)
        scene bg_dream
        show tonb tonb101 with Dissolve(1.5):
            parallel:
                xpos -1000
                linear 1.0 xpos 0
            parallel:
                ypos 0
                linear 1 ypos 15
                linear 1 ypos 0
                repeat
        with Dissolve(1.5)
        "{i}you need me...."
        y "listen, i don't trust you."
        y "I will never trust you."
        "{i}i can give you power...."
        "{i}give to me, and i will give to you...."
        y "i don't even know what that means!"
        y "I have nothing to give you!"
        "{i}not yet...."
        y "what?"
        y "you're.... waiting on something?"
        "{i}yesss.... but i can give you great power in advance...."
        y "what kind of power?"
        "{i}power of the mind...."
        y "like.... mind control?"
        "{i}sssimilar...."
        y "and what would you need from me?"
        "{i}accessss..."
        y "access?"
        "{i}to your mind...."
        "{i}the freedom.... to roam.... in your mind...."
        y "......"
        y "no."
        y "never."
        y "i don't trust you."
        y "now let me sleep."
        "{i}very well...."
        $ naga_toph_old = 3


    if naga_eyes and not first_naga_bj:
        hide screen earth_money_date
        stop music
        play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
        scene black with Dissolve(1.5)
        scene bg_dream with Dissolve(1.5)
        y "what... what is going on....?"
        y "another crazy fucking dream....?"
        "{i}you could sssay that...."
        y "wh-who's there?"
        "{i}i have been trying to reach you...."
        show tonb tonb01:
            parallel:
                ypos 720
                linear 2.0 ypos 0
            parallel:
                alpha 0
                linear 2.0 alpha 1
        $ renpy.pause(2.0, hard = True)

        show tonb tonb01:
            ypos 0 xpos 0
            linear 3.0 ypos 30
            linear 3.0 ypos 0
            repeat

        "{i}you don't lisssten..."
        ya "aah!"
        show ctc
        pause
        hide ctc
        y "what... what are you doing here? am i asleep?"
        y "how are you here?"
        y "I thought the other spirit chick said you were contained?"
        "{i}we mussst ssspeak..."
        "{i}thisss isss where i have the mossst power..."
        y "why are you here now?"
        "{i}the eyesss..."
        "{i}you pulled them from my ssstatue..."
        "{i}i wasss contained there, forced to reach out through sssleep..."
        "{i}but ssshe did not expect thisss..."
        "{i}even i did not expect thisss..."
        y "expect what...?"
        y "what... what happened?"
        "{i}Do you like thisss form, avatar?"
        y "i... no?"
        y "not particularly..."
        hide tonb tonb01 with Dissolve(1.5)
        show tonb tonb101 with Dissolve(1.5):
            parallel:
                xpos -1000
                linear 1.0 xpos 0
            parallel:
                ypos 0
                linear 1 ypos 15
                linear 1 ypos 0
                repeat

        "{i}How about thisss?"
        show ctc
        pause
        hide ctc
        y "that... is better, actually."
        y "but fuck those crystal eyes. i'll just throw them away."
        "{i}it isss too late for that, avatar..."
        "{i}you have accepted the eyesss... and a ssshadow of me hasss nessstled in your conssscience."
        "{i}...and {b}ssshe{/b} cannot help you here..."
        y "....what!?"
        y "you're in my mind!?"
        y "oh, fuck... is this how i die?"
        y "i never got to ride in a hot air balloon..."
        y "or try that mulan szechuan sauce."
        y "...or find a good hat."
        y "not like, a fancy hat, just one that feels comfortable wearing on a bad hair day."
        y "like, on a sunday night, when i realize i need groceries, but i haven't showered-"
        "{i}.....you will not die here....."
        y "Oh. that's good."
        "{i}in fact... i bring you a gift..."
        show tonb tonb03 with Dissolve(1.5)
        "{i}a peace offering...."
        show ctc
        pause
        hide ctc
        "{i}you have nothing to fear from me..."
        y "that has not proven to be the case before."
        y "also, i'm terrified of what's about to happen here..."
        "{i}i am in your mind, avatar..."
        "{i}but i can help you...."
        y "help me?"
        y "you're a snake demon!"
        "{i}a ssspirit... not a demon..."
        "{i}i have a name..."
        y "i don't care!"
        "{i}sssee how i will help you..."
        y "um..."
        "{i}don't fight me, avatar..."
        "{i}thisss isss jussst a dream..."
        show tonb tonb04 with Dissolve(1.5)
        "{i}ssso enjoy the experience..."
        show ctc
        pause
        hide ctc
        y "okay, really, really, wait a second-"
        hide tonb tonb04
        show tonb_tail:
            parallel:
                xpos 400
                linear 2.0 xpos 530
                linear 2.0 xpos 400
                repeat
            parallel:
                ypos 0
                linear 1.0 ypos 50
                linear 1.20 ypos 0
                repeat
        show tonb tonb05
        show ctc
        pause
        hide ctc
        y "aahhh.... ohh... your... your tongue is..."
        y "okay, maybe-"
        show tonb tonb100
        "{i}sluurp..."
        show ctc
        pause
        hide ctc
        y "holy fuck. shitty fuck dick tits."
        y "you're... are you... really..."
        "{i}suck... gulp... sluurp..."
        show ctc
        pause 
        hide ctc
        show tonb tonb102
        y "this isn't real..."
        show ctc
        pause
        hide ctc
        y "demon spirit snake lady..."
        y "sucking my cock..."
        y "this {i}has{/i} to be a dream."
        y "otherwise, this is insane."
        "{i}slluuurp... sluuuurp"
        show ctc
        pause
        hide ctc
        y "i'm... this is..."
        y "I'm getting... i'm getting close..."
        y "I'm gonna-"
        $ first_naga_bj = True
        stop music fadeout 1
        play music "audio/Bumba Crossing.mp3"
        $ bk3_day = True
        scene black with Dissolve(1.5)
        scene inside_shack with Dissolve(1.5)
        y "....."
        y "what the fuck."
        y "that. tease."
        y "ugh."
        y "maybe it really was just a dream... and that's why i couldn't finish?"
        jump bk3_next

    if toph_blowjob and not find_joodee_help:
        $ find_joodee_help = True
        scene black with dissolve
        show n_stance01_big_gloweye with Dissolve(1.5)
        show ctc
        pause
        hide ctc
        "....joo dee...."
        "....find joo dee...."
        hide n_stance01_big_gloweye with dissolve

    if ecalendar ==7:
        stop music 
        play music "audio/Dreams Become Real.mp3"
        scene black with dissolve
        show n_stance01_big_gloweye with Dissolve(1.5)
        show ctc
        pause
        hide ctc
        "...pleasure like you've never known...."
        "cum to me...."
        hide n_stance01_big_gloweye with dissolve

    if ecalendar ==13:
        scene black with dissolve
        show ctc
        pause
        hide ctc
        scene basingse_city_1 with dissolve
        y "........"
        y "...how did i get into the city?"
        show a_blink with dissolve
        a "well, well, well... look who i found."
        y "azula? how the hell-"
        a "is that really the way to greet a past lover?"
        y "okay, hold on, how do you-"
        show ae with dissolve
        a "we shared so many experiences together."
        a "you can't just leave me behind."
        hide ae with dissolve
        a "in fact, what you should do, is..."
        hide a_blink
        show afire4
        with sshake
        a "{size=+10}die!"
        scene black
        y "ah!"
        y "...oh..."
        y "just.... just a dream..."

    if ecalendar ==18:
        show hypno_light:
            xalign 1.0 yalign 0.0
            linear 1.0 xalign 0.0
            ease 1.0 truecenter
            pause 1.0
            alignaround (.5, .5)
            linear 2.0 clockwise circles 3 yalign 0.0
            linear 2.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
            ease 1.0 truecenter
            linear 1.0 xalign 1.0
            repeat
        "{i}the chaos..."
        y "what... are you?"
        "{i}lost... we are lost..."
        y "who's lost?"
        "{i}blood...."
        y "what?"
        "{i}{b}{size=+30}blood!!!"

    $ skye_today = False
    $ june_convo_today = False
    $ suki_hypno_today = False
    $ earth_training = False
    $ bk3_day = True
    $ ecalendar += 1
    $ toph_massaged = False

    $ bk3_fire_remaining = bk3_moves
    $ bk3_water_remaining = bk3_moves


    $ bk3_player_life_start = bk3_hp
    $ bk3_player_life = bk3_player_life_start

    if bk3_store_built:
        if shop_building ==1:
            $ randcoin = renpy.random.randint(3, 8)
            $ emoney += randcoin
            "you got [randcoin] coins from having a shop!"
        if shop_building ==2:
            $ randcoin = renpy.random.randint(8, 15)
            $ emoney += randcoin
            "you got [randcoin] coins from having a shop!"
    jump bk3_village

label b_earth_journal_menu_day:
    menu:
        "page 1":
            show screen earth_journal
            show ctc
            pause
            hide ctc
            hide screen earth_journal
            jump basingse_day1

        "page 2" if quest3:
            show screen earth_journal2
            show ctc
            pause
            hide ctc
            hide screen earth_journal2
            jump basingse_day1
        "exit":

            jump basingse_day1

label b_earth_journal_menu_night:
    menu:
        "page 1":
            show screen earth_journal
            show ctc
            pause
            hide ctc
            hide screen earth_journal
            jump basingse_night1

        "page 2" if quest3:
            show screen earth_journal2
            show ctc
            pause
            hide ctc
            hide screen earth_journal2
            jump basingse_night1
        "exit":

            jump basingse_night1

label v_earth_journal_menu:
    menu:
        "page 1":
            show screen earth_journal
            show ctc
            pause
            hide ctc
            hide screen earth_journal
            jump bk3_village_background

        "page 2" if quest3:
            show screen earth_journal2
            show ctc
            pause
            hide ctc
            hide screen earth_journal2
            jump bk3_village_background
        "exit":

            jump bk3_village_background


label toph_swim:
    scene black with dissolve
    "you travel to the nearby lake...."
    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_1
    show expression "ebackgrounds/lake_laogai_3.jpg":
        alpha 0.0
    with dissolve
    t "this looks great!"
    show toi toi200
    with dissolve
    t "look at that water!"
    y "yeah, it's-"
    show idle_fl_laugh with dissolve
    y "...."
    y "why do you feel the need to do that?"
    show idle_fl_blink
    with dissolve
    t "no reason."
    y "you're looking good, though."
    hide idle_fl_blink
    hide idle_fl_laugh
    show toi toi202
    show idle_fl_shocked
    show toi_blush
    with dissolve
    t "hey!"
    hide toi_blush
    show idle_fl_angry
    show toi_blush
    hide idle_fl_shocked
    with dissolve
    t "stop... that!"
    y "stop what?"
    t "looking... at me."
    y "i'm not looking at you."
    hide toi_blush
    show idle_fl_shocked
    hide idle_fl_angry
    with dissolve
    t "...oh."
    hide idle_fl_shocked with dissolve
    t "sorry. i... can't tell."
    t "well, let's... get in the water."
    hide toi toi202 with dissolve

    hide expression "ebackgrounds/lake_laogai_1.jpg"
    hide expression "ebackgrounds/lake_laogai_3.jpg"
    show expression "ebackgrounds/lake_laogai_2.jpg"
    with dissolve
    show toi toi210:
        ypos -100
    with dissolve
    show ctc
    pause
    hide ctc
    y "really? that's it?"
    t "i'm... not the best at swimming."
    y "figures."
    show toi_swim_angry:
        ypos -100
    with dissolve
    t "oh, yeah? is that a challenge?"
    t "fine!"
    show expression "bk3/toph/swim_idles/water_standin.png"
    with dissolve
    t "....."
    hide toi_swim_angry with dissolve
    t "huh...not so bad."
    y "see? that-"
    show toki toki10:
        ypos -100
    show toki_swim_smile:
        ypos -100
    with dissolve
    k3 "hey guys!"
    show toi_swim_surprise:
        ypos -100
    with dissolve
    t "katara!?"
    y "whoa, hey, what are you doing here?"
    show toki_swim_blink:
        ypos -100
    with dissolve
    k3 "i come down here all the time."
    hide toki_swim_blink
    hide toki_swim_smile
    hide toi_swim_surprise
    show toki_swim_surprised:
        ypos -100
    with dissolve
    k3 "what are {i}you{/i} doing down here?"
    k3 "shouldn't you be-"
    hide toki_swim_surprised with dissolve
    k3 "hold on, let me get in the water..."
    show expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve
    k3 "there..."
    show toki_swim_angry:
        ypos -100
    with dissolve
    k3 "shouldn't you be training?"
    y "we are training."
    k3 "...what?"
    show toi toi250
    show toi_wave
    show toi_swim_smile:
        ypos -100
    t "yeah, training {i}so hard{/i}."

    show toki toki11
    hide toki_swim_angry
    show toki_swim_surprised:
        ypos -100
    show eyes_leftlook:
        ypos -100

    k3 "aaaah, toph!"
    y "hahaha-"
    show toki_swim_smile:
        ypos -100
    hide eyes_leftlook
    show eyes_leftlook:
        ypos -100
    hide toki_swim_surprised
    with dissolve
    k3 "oh, yeah? do you really wanna attack {size=+10}me{/size} with {size=+10}water{/size}?"
    show toki toki110
    show toki_wave
    k3 "you're gonna regret this!"
    t "bring it, skank!"
    k3 "skank!?"
    k3 "take this!"
    t "yeah, well take..."
    t "{size=+10}this!"
    play sound "audio/water_splash.mp3"
    $ katara_top_nude = True
    hide toki_wave
    show toki toki11
    show toki_swim_surprised:
        ypos -100
    hide eyes_leftlook
    show eyes_leftlook:
        ypos -100
    with vshake
    t "haha, yeah."
    k3 "...toph!"
    k3 "you knocked off my shirt!"
    show ctc
    pause
    hide ctc
    hide toi_wave
    hide toi_swim_smile
    show toi toi210:
        ypos -100
    show toi_swim_surprise:
        ypos -100
    with dissolve
    t "i... i did!?"
    t "i'm so sorry, katara!"
    show toki toki10
    hide toki_swim_surprised
    hide eyes_leftlook
    show toki_swim_smile:
        ypos -100
    show eyes_oneeye:
        ypos -100
    with dissolve
    k3 "ah, it's fine."
    show ctc
    pause
    hide ctc
    hide eyes_oneeye
    show eyes_leftlook:
        ypos -100

    with dissolve
    k3 "so, where were we?"
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "ka... katara!"
    hide toki_swim_smile
    hide eyes_oneeye
    show eyes_leftlook:
        ypos -100
    with dissolve
    k3 "what?"
    t "....cover up!"
    k3 "why?"
    y "yeah, why?"
    t "....because... it's...."
    hide eyes_oneeye
    hide eyes_leftlook
    show toki_swim_blink:
        ypos -100
    with dissolve
    k3 "it's not a big deal."
    hide toki_swim_blink
    with dissolve
    k3 "in fact, remember how i can use those breast size scrolls?"
    k3 "to waterbend my boobs to different sizes?"
    t "yes..."
    y "yes."
    k3 "well.... what do you wanna see?"

    menu:
        "BIIIG":
            $ boobs = "big"
        "medium":
            $ boobs = "medium"
        "small":
            $ boobs = "small"

    k3 "how's this?"
    show toki_swim_smile:
        ypos -100
    with dissolve
    k3 "wanna see a different size?"
    t "katara!"
    k3 "come on, it's fun!"
    jump katara_swim_boob_menu

label katara_swim_boob_menu:
    menu:
        "BIIIG":
            $ boobs = "big"
        "medium":
            $ boobs = "medium"
        "small":
            $ boobs = "small"
        "finished":
            jump after_katara_swim_boob

    show ctc
    pause
    hide ctc
    jump katara_swim_boob_menu

label after_katara_swim_boob:
    hide toki_swim_smile
    show eyes_leftlook:
        ypos -100
    with dissolve
    k3 "you should try taking your top off, toph."
    show toi_swim_angry:
        ypos -100
    show toi_swim_blink:
        ypos -100
    hide toi_swim_blush
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "n...no!"
    t "i can't believe-"
    t "...."
    show expression "bk3/toph/swim_idles/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    show expression "bk3/katara/swim_idle/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    hide toi_swim_blink
    hide toi_swim_blush
    hide toi_swim_surprise
    show toi_swim_surprise:
        ypos -100
    with dissolve
    t "hey, is... is the water level dropping?"
    y "yeah, it does seem to be."
    k3 "it's like an artificial tide..."
    t "are you doing this, katara?"
    k3 "no...."
    t "....weird."
    t "okay, i think i'm done for the day."
    t "i think we should head back."
    show toki_swim_smile:
        ypos -100
    show toki_swim_blink:
        ypos -100
    with dissolve
    k3 "aw... well it was good to see you guys."
    hide toki_swim_blink
    hide eyes_leftlook
    show eyes_oneeye:
        ypos -100
    with dissolve
    k3 "especially you, aang."
    y "yeah... likewise."
    t "come on, you weirdo. let's go."
    $ bk3_day = False
    $ earthbending = 3

    jump bk3_village_background


label after_store_train:
    $ katara_blowjob_water = True
    y "alright."
    t "good."
    t "i think we should train down at the lake."
    y "sure. i'll meet you there."
    show toi toi06 with dissolve
    t "don't be late!"
    scene black with dissolve
    "you take your sweet time going down to the lake."
    y "she better not throw more boulders at me."
    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    scene lake_laogai_2
    show toi toi210:
        ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png"
    show toki toki10:
        ypos -70
    show expression "bk3/katara/swim_idle/water_standin.png"
    show eyes_leftlook:
        ypos -70
    with dissolve
    "as you approach the lake, you see toph and katara talking."
    menu:
        "interrupt":
            "you walk up and interrupt their conversation."
            y "yo."
            show toi toi212:
                ypos -100
            show toi_swim_angry:
                ypos -100
            show toi_swim_blush:
                ypos -100
            with dissolve
            t "aang!"
            t "are you spying on us!?"
            y "no."
            y "oh my gosh, you're blushing."
            t "no i'm not!"
            y "what were you guys talking about?"
            k3 "boobs."
            y "nice."
            t "shut up!"
        "sneak closer":

            "keeping your distance, you sneak closer."
            k3 "you should have a little fun, toph!"
            k3 "you're the one always telling me to break the rules."
            show toi_swim_blush:
                ypos -100
            with dissolve
            t "well, yeah, but..."
            k3 "but what?"
            k3 "come on... there's no one around!"
            t "......"
            t "............."
            t "..................."
            t "...okay."
            t "I'll... i'll take off my top..."
            t "......"
            $ toph_top_nude = True
            show ctc
            pause
            hide ctc
            k3 "see? it's freeing, right?"
            t "i guess it's-"
            play sound "audio/water_splash.mp3"
            show toi toi212:
                ypos -100
            show toi_swim_angry:
                ypos -100
            hide toi_swim_blush
            show toi_swim_blush:
                ypos -100
            with dissolve
            with sshake
            "In that moment, you slip forward and fall into the water."
            t "aang! what the heck!?"
            t "are you spying on us!?"
            y "no... i was... uh... just walking up and fell."

    $ earthbending = 4
    y "so are we training or what?"
    show toi_swim_blink:
        ypos -100
    with dissolve
    t "........"
    hide toi_swim_blink with dissolve
    t "drop and give me 100 boulder-presses-"
    y "aw, man."
    t "-or i will shit stomp you!"
    y "I don't even know what that means!"
    k3 "...toph."
    t "what?"
    k3 "...you should really try positive reinforcement."
    k3 "i've always found it to work really well with aang."
    t "thanks for the advice katara."
    t "but i'm going to ignore it."
    y "aw....."
    k3 ".............."
    k3 "...how about i show you?"
    k3 "come here, aang."
    y "what?"
    t "what are you gonna do?"
    k3 "i'm going to kiss him."
    t "what!?"
    t "are you serious!?"
    y "....i'm in."
    k3 "yes, i'm serious. "
    k3 "first, let's try it your way."
    k3 "aang! move the water."
    y "uh... okay..."
    y "........"
    y "............"
    k3 "it's not moving."
    y "i'm trying!"
    k3 "see, that doesn't work."
    k3 "now i'm going to kiss him and he's going to try to move the water."
    scene black with dissolve
    "katara comes up to you, but to your surprise, she kneels."
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    scene lake_laogai_2
    show tokb tokb00
    with dissolve
    y "Umm...."
    show tokb tokb01 with dissolve
    k3 "i'm ready to... kiss you now."
    y "......"
    y "are you sure?"
    k3 "yes..."
    show tokb tokb02 with dissolve
    y "...you really sure?"
    show tokb tokb04 with dissolve
    show ctc
    pause
    hide ctc
    show tokb tokb05 with dissolve
    y "I guess that answers that."
    show tokb tokb07 with dissolve
    k3 "mmm..."
    show tokb tokb100
    show ctc
    pause
    hide ctc
    k3 "*sluurp*"
    t "what's going on?"
    t "are you really kissing?"
    show toi toi212:
        ypos -100
        xpos -200
        ease 6.0 xpos 0
    show expression "bk3/toph/swim_idles/water_standin.png":
        xpos -200
        ease 6.0 xpos 0

    k3 "*gulp* *mmmm* *slurp*"
    t "aang! is she really kissing you!?"
    $ katara_blowjob_blink = True
    menu:
        "hold her head":
            $ katara_blowjob_holdhead = True
        "keep going like this":
            $ katara_blowjob_holdhead = False
    y "...in a manner of speaking."
    t "....what?"
    k3 "*gltch* *sluuurp*"
    t "that's... some really noisy kissing."
    t "are... are you using tongue or something?"
    y "yeah, she... ah... she's using tongue.... ah..."
    $ katara_blowjob_blink = False
    y "she could use a little more tongue though... right... ah...."
    $ katara_blowjob_blink=True
    pause 1.0
    $ katara_blowjob_blink=False
    pause 1.0
    $ katara_blowjob_blink=True
    pause 1.0
    $ katara_blowjob_blink=False
    y "yes... ahh... fuck... i can't believe..."
    t "guys?"
    y "ngh..."
    show tokb tokb101
    k3 "*mmngh...* *ahh....* *mngh...*"
    t "Umm...."
    t "katara...? can we talk for a second?"
    y "her mouth is busy right now, toph."
    k3 "*slurp* *slurp* *gulp*"
    y "ah... ah... she's almost free..."
    menu:
        "cum on face":
            show tokb tokb05 with dissolve
            y "fuck..."
            play sound "audio/splurt2.ogg"
            show tokb_sperm1
            with flash
            k3 "aahhh....!"
            play sound "audio/splurt1.ogg"
            hide tokb_sperm1
            show tokb_sperm2
            with flash
            y "hgnh! fuck!"
            k3 "yes, baby!"
            t "...what...?"
            y "ngh!"
            play sound "audio/splurt2.ogg"
            hide tokb_sperm2
            show tokb_sperm3
            with flash
            y "ohh...."
            k3 "mmmmm....."
            t "guys! stop ignoring me!"
            t "I'm feeling kind of... left out..."
        "cum in mouth":

            show tokb tokb10 with vshake
            y "fuck..."
            show tokb tokb11
            with vshake
            play sound "audio/splurt2.ogg"
            with flash
            k3 "aahhh....!"
            show tokb tokb11
            with vshake
            play sound "audio/splurt1.ogg"
            with flash
            y "hgnh! fuck!"
            k3 "yes, baby!"
            t "...what...?"
            y "ngh!"
            play sound "audio/splurt2.ogg"
            show tokb tokb04
            show tokb_sperm4
            with flash
            y "ohh...."
            k3 "mmmmm....."
            t "guys! stop ignoring me!"
            t "I'm feeling kind of... left out..."

    show ctc
    pause
    hide ctc
    scene black
    scene lake_laogai_2
    show toi toi212:
        ypos -100
    show toki toki10:
        ypos -100
    show a_idle_fl_face_sperm:
        ypos -85
    show expression "bk3/toph/swim_idles/water_standin.png"
    show expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve
    k3 "now move that water, aang!"
    k3 "you can do it!"
    y "hhngh....!!!"
    show expression "bk3/toph/swim_idles/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    show expression "bk3/katara/swim_idle/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    y "holy shit, i'm doing it."
    t "you... really are..."
    k3 "see? told ya."
    k3 "positive reinforcement."
    t "okay, i'll... try it."
    t "aang, you... you... nice person..."
    y "...."
    k3 "i mean... good start?"
    t "....i'm trying, okay?"
    k3 "you're doing fine, toph."
    k3 "tell you what, i'll leave you two alone so you can train... properly."

    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    hide expression "bk3/katara/swim_idle/water_standin.png"
    hide toki toki10
    hide a_idle_fl_face_sperm
    with dissolve
    t "okay, well..."
    t "you need to listen to the earth.... handsome?"
    y "...."
    t "listen with your feet."
    t "listen to this."
    with sshake
    t "that vibration-"
    t "....huh."
    y "what?"
    t "that's... odd."
    t "there are tunnels under the lake."
    y "what, seriously?"
    t "yes."
    t "come on!"
    $ toph_top_nude = False
    scene black
    show expression "ebackgrounds/lake_laogai_1.jpg"
    show expression "ebackgrounds/lake_laogai_3.jpg":
        alpha 0.0
    show toi toi200
    with dissolve
    t "do you feel that?"
    y "...no?"
    t "ugh... i can't imagine what it's like to be as blind as you."
    y "um... what?"
    t "here...."
    play sound "audio/earthquake.mp3"
    show toi toi201 with sshake
    show expression "ebackgrounds/lake_laogai_3.jpg":
        linear 1.0 alpha 1.0
    show ctc
    pause
    hide ctc
    y "so.... that's a secret tunnel."
    y "in the lake."
    t "yeah. Let's take a closer look."
    y "uh... okay..."
    hide toi toi201
    show expression "ebackgrounds/lake_laogai_4.jpg"
    show expression "ebackgrounds/lake_laogai_4_lid.png"
    show toi toi200
    with dissolve
    show ctc
    pause
    hide ctc
    t "ready?"
    y "um."
    t "let's push this lid away..."
    play sound "audio/stonegrind.mp3"
    show expression "ebackgrounds/lake_laogai_4_lid.png" at Move((0,0),(800,0),1)
    show toi toi200
    with dissolve
    show ctc
    pause
    hide ctc
    y "you... did that very quickly..."
    y "maybe we should hold up and think about this-"
    t "Let's go in!"
    menu:
        "um, wait":
            y "this is getting out of hand really quickly..."
            t "come on, you sissy!"
            hide toi toi200 with dissolve
            y "did... did she just go in?"
            y "....."
            y "fuck."
        "let's do it!":

            y "yeah, let's check it out."
            hide toi toi200 with dissolve

    scene black with dissolve
    "you climb down the ladder after toph."
    y "....."
    y "it's so dark down here... i can't see a thing."
    t "oh, no! what a nightmare!"
    y "........"
    y "....sorry."
    jump bk3_maze_start

label follow_feng:
    stop music fadeout 2
    scene black with dissolve
    "you walk with toph and the girl to the market."
    stop music
    play music "audio/jangles.mp3"
    scene market_general
    show thankful_girl
    show toi toi04:
        xzoom -1.0
    with dissolve
    "girl" "this is nice."
    y "any memories coming back to you?"
    "girl" "no, i-"
    "girl" "aaaahhh!!!!!!"
    hide thankful_girl with moveoutright
    y "what the hell just happened?"
    t "she's running! but why!?"
    show tolf tolf01
    show tolf_blink
    with dissolve
    show ctc
    pause
    hide ctc
    y "(it's long feng!)"
    y "(but why's he in the market...?)"
    hide tolf tolf01
    hide tolf_blink
    with dissolve
    y "i'm gonna follow long feng, you go after the girl!"
    t "okay!"
    hide toi toi04 with dissolve
    y "alright, feng..."

    y "what are you up to?"
    scene black with dissolve
    show expression "ebackgrounds/lake_laogai_1.jpg"
    show expression "ebackgrounds/lake_laogai_3.jpg":
        alpha 0.0
    with dissolve
    "you follow long feng to lake laogai."
    "as you watch, he raises up the entrance to the tunnels..."
    play sound "audio/earthquake.mp3"
    with sshake
    show expression "ebackgrounds/lake_laogai_3.jpg":
        linear 1.0 alpha 1.0
    show ctc
    pause
    hide ctc
    "you follow him...."
    show expression "ebackgrounds/lake_laogai_4.jpg"
    show expression "ebackgrounds/lake_laogai_4_lid.png"
    with dissolve
    $ renpy.pause(0.4)
    play sound "audio/stonegrind.mp3"
    show expression "ebackgrounds/lake_laogai_4_lid.png" at Move((0,0),(800,0),1)
    show ctc
    pause
    hide ctc
    y "okay... here i go again."
    y "on my own."
    y "going down the only road i've ever known."
    y "...."
    y "this is probably not smart."
    show ctc
    pause
    hide ctc

    y "....well, here i go."
    scene black with dissolve
    stop music
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
    scene dark_tunnel with dissolve
    show ctc
    pause
    hide ctc
    show tolf tolf01 with Dissolve(1.0)
    lf "well, well."
    lf "we meet again, avatar."
    y "gulp."
    show tolf_blink with dissolve
    lf "you've proven yourself to be very resourceful, finding this place."
    show tolf tolf02
    hide tolf_blink
    with dissolve
    lf "unfortunately, i cannot allow that knowledge to leave here."
    menu:
        "fear the avatar":
            y "i am the avatar, long feng."
            y "do you really think you stand a chance against me?"
        "let's make a deal...":

            y "let's not be hasty."
            y "maybe we can work something out."

    lf "hmm...."
    show tolf tolf01 with dissolve
    lf "perhaps you and i got off on the wrong foot, avatar."
    show tolf_blink with dissolve
    lf "i protect the king and the city in many ways."
    lf "and the most important way..."
    hide tolf_blink with dissolve
    lf "is right here in these tunnels..."
    lf "...through hypnosis."
    y "hypnosis?"
    y "ohhh...."
    y "that explains some things."
    y "like joo dee."
    show tolf_blink with dissolve
    lf "yes, joo dee is an excellent example."
    lf "in fact, i could teach you some of her trigger words."
    lf "i have not tested them on her yet, but the method is flawless."
    hide tolf_blink with dissolve
    lf "hypnosis has proven to be the perfect tool for keeping war out of ba sing se."
    y "wait... why are you telling me all this?"
    lf "because i believe you are someone with vision... and ambition, avatar."
    lf "and i could use that."
    show tolf tolf02 with dissolve
    lf "there are some girls that... make peace challenging."
    lf "they have proven particularly resistant to my attempts..."
    show tolf tolf01 with dissolve
    lf "...but I believe you might have better success."
    y "what do you mean?"
    show tolf tolf01
    show tolf_blink
    with dissolve
    lf "simply put..."
    lf "i will teach you mind-control techniques if you will use them to break the girls..."
    hide tolf_blink
    show tolf tolf02
    with dissolve
    lf "...and help me keep complete control over the king and the city."
    lf "it will not be an easy challenge, but... you might find the struggle worth it."
    show tolf tolf01 with dissolve
    lf "what do you say?"
    $ market_stroll = 2
    jump bk3_route_choice

    label bk3_route_choice:
        menu:
            "help feng and learn mind-control (slave route)":
                "you have chosen the slave route."
                menu:
                    "Continue?"
                    "start the slave route":
                        $ bk3_slave = True
                        jump bk3_slave_start
                    "then again...":
                        jump bk3_route_choice
            "refuse feng and fight this corruption (love route)":

                "you have chosen the love route."
                menu:
                    "Continue?"
                    "start the love route":
                        $ bk3_loveroute = True
                        jump bk3_love_start
                    "then again...":
                        jump bk3_route_choice

label bk3_slave_start:
    y "i'm all about dominating hotties."
    show tolf_blink with dissolve
    lf "excellent."
    lf "of course...."
    hide tolf_blink with dissolve
    lf "...i will not teach you..."
    y "....what?"
    show tolf tolf02 with dissolve
    lf "i must keep my distance from these tunnels, and of course, you and i cannot meet if we are to be successful."
    lf "these girls must believe you have fought to free them."
    lf "if they escape too easily, they will not feel in your debt."
    lf "and if we are seen together.... well...."
    y "got it."
    show tolf tolf01 with dissolve
    lf "however, I said that you would learn our techniques, so you shall."
    lf "i will leave you in {i}very{/i} capable hands."
    hide tolf tolf01 with Dissolve(1.0)
    lf "good luck, avatar..."
    y "....."
    y "well that was a creepy fucking exit."
    show tomc tomc01 with Dissolve(1.0)
    show ctc
    pause
    hide ctc
    ct "you will speak of the grand secretariat with respect, avatar."
    y "i don't think that's likely."
    show tomc tomc02 with dissolve
    ct "*sigh...*"
    y "soo.... who are you?"
    show tomc tomc03 with dissolve
    ct "my name is ajala."
    show ctc
    pause
    hide ctc
    y "nice, nice."
    ct "i will be teaching you hypnosis techniques."
    show tomc tomc04 with dissolve
    ct "but first... you must understand the basics."
    ct "first and foremost, these techniques require a room."
    y "what?"
    ct "the subject must be seated, and you will need specific equipment."
    ct "you will need to trick the subjects into beginning the process."
    y "....and are you going to give me the equipment i need?"
    show tomc_blink wtih dissolve
    ct "as you earn it."
    y "come on, sugar tits, just-"
    show tomc tomc05
    hide tomc_blink
    with dissolve
    ct "I will beat you to death, boy."
    ct "so watch your mouth."
    y "....."
    y "hot."
    show tomc tomc04
    show tomc_angry
    show tomc_blink
    with dissolve
    ct "ugh."
    show tomc tomc04
    show tomc_angry
    hide tomc_blink
    with dissolve
    ct "since i'm under orders from the grand secretariat to teach you myself..."
    hide tomc_angry with dissolve
    ct "...we're going to use this equipment on me."
    ct "we're going to start slow."
    ct "now, as the light moves back and forth, my mind will become more susceptible."
    ct "the more sessions of this, the more susceptible the patient's mind."
    ct "once you hypnotize me, you are going to have me say \"long feng is the true ruler of ba sing se\"."
    show tomc_angry with dissolve
    ct "and that's it, understand? just that statement."
    ct "got it?"
    y "I got it."
    hide tomc_angry with dissolve
    ct "okay... let's get started, then."

    show hypno_light:
        xalign 0.0 yalign 0.5
        linear 2.0 xalign 1.0
        linear 2.0 xalign 0.0
        repeat
    show ctc
    $ renpy.pause(4.0, hard=True)
    hide ctc
    show tomc tomc06
    show headup
    with dissolve
    jump ct_hypno_menu

label ct_hypno_menu:
    show tomc tomc06
    show headup
    with dissolve
    menu:
        "apologize to me":
            hide headup
            show tomc tomc06
            with dissolve
            ct "I'm so sorry."
            y "More."
            ct "you don't deserve my attitude."
            y "more degrading."
            ct "i'm horrible."
            ct "I'm a stupid bitch and i'm so sorry."
            jump ct_hypno_menu
        "flirt with me":

            show tomc tomc07
            hide headup
            with dissolve
            ct "hey there, sexy."
            ct "you know, i'm a little... wet..."
            ct "don't tell anyone, okay?"
            ct "in fact, i can't stop thinking about how much i'd like you to fuck my tits...."
            ct "if you have a few minutes...."
            jump ct_hypno_menu
        "twirl your hair":

            show tomc tomc100
            hide headup
            with dissolve
            show ctc
            pause
            hide ctc
            y "now apologize."
            show tomc_surpise with dissolve
            ct "I'm so sorry for who i am."
            ct "i should be better for you."
            y "now flirt."
            hide tomc_surpise
            show tomc_sultry
            with dissolve
            ct "i could be better... i could be the best you've ever had..."
            ct "you wanna go into a dark hallway and... abuse me?"
            hide tomc_sultry with dissolve
            jump ct_hypno_menu
        "show me your tits":


            hide headup
            show tomc_angry
            with dissolve
            ct "n...n....no...."
            hide tomc_angry
            jump ct_hypno_menu
        "long feng sucks":

            show tomc_angry
            with dissolve
            ct "long feng is idiotic and ugly."
            ct "you should be ruler of the earth kingdom."
            ct "i hate long feng."
            hide tomc_angry
            jump ct_hypno_menu
        "long feng rules":

            ct "long feng is the true ruler of ba sing se."
            jump ct_hypno_menu
        "finished":

            pass

    hide headup
    show tomc tomc01
    hide hypno_light
    with dissolve
    ct "hhgh...."
    ct "what... what happened?"
    show tomc tomc02 with dissolve
    ct "ungh.... never fun...."
    show tomc tomc03 with dissolve
    ct "did it work?"
    y "like a charm."
    show tomc_angry with dissolve
    ct "you just made me say that one phrase, right?"
    y "yup."
    hide tomc_angry with dissolve
    ct "good."
    ct "well, here's the first piece of equipment you need."
    ct "don't forget you'll need to set up a room for it."
    ct "if you have a house, you should upgrade it."
    ct "now..."
    show tomc tomc01
    with dissolve
    ct "don't forget, you'll need to fight your way to rescue the girls."
    ct "for the sake of appearances."
    ct "you'll see me again when the time is right."
    ct "now... get lost."
    hide tomc tomc01 with Dissolve(1.0)

    y "So basically, Long Feng told me to stay out of his business..."
    y "...and in return he'll teach me a few tricks to get some obedient pussy?"
    y "If it wasn't my lifelong dream to hypnotize girls into doing unspeakable things, that might not have worked....."

    y "Well I guess I'll play along..... for now."
    play sound "audio/earthquake.mp3"
    with sshake
    t "aang!"
    y "...toph?"
    t "i'm coming!"
    y "oh, that's not necessa-"
    with sshake
    y "wh-aaahhh-!!!"
    play sound "audio/thud.mp3"
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_3
    show toi toi04
    with sshake
    y "ngh!"
    y "ow."
    show toi toi09 with dissolve
    t "are you okay!?"
    y "ungh... my head..."
    y "how did you find me?"
    show toi_blink with dissolve
    t "after i caught up with the girl, i sent her to the village."
    t "after that, i figured feng was involved in the tunnels and you'd follow him."
    t "and i came to make sure you were okay."
    t "and it's a good thing i did."
    hide toi_blink with dissolve
    t "i felt someone else with you - what happened?"
    y "uh...."
    y "...i caught up to feng, but he got away."
    y "he's behind a ton of kidnappings and..."
    y "...he's hypnotizing people."
    show toi toi05 with dissolve
    t "what!?"
    y "yeah."
    y "i was able to grab a piece of equipment that i think will help me undo the hypnosis."
    show toi toi09 with dissolve
    t "what are you talking about?"
    y "i'm going to be traveling the tunnels to rescue the trapped girls."
    t "....alone?"
    t "i could come with you."
    y "no, i don't want to put you in danger."
    y "the village needs you to look out for it."
    y "besides, i'm the avatar -- i can handle myself."
    t "...."
    t "well, let's get back, at least."
    $ bk3_day = False
    show blackveil with dissolve
    "you can now travel to the tunnels!"
    $ laogai_travel = True
    show bk3_maze_off:
        xpos 0.18
    with dissolve
    show bk3_maze_on:
        xpos 0.18
    with dissolve
    "click this button on the top of your screen to return to lake laogai!"
    hide bk3_maze_on with dissolve
    hide bk3_maze_off
    hide blackveil
    with dissolve
    jump bk3_village_background

label bk3_maze_start1:
    stop music fadeout 2
    scene black with dissolve
    "you travel to the tunnels beneath lake laogai...."
    jump bk3_maze_start

    "test"


label earthbending_7_training:
    scene black with dissolve
    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    scene lake_laogai_1

    $ toph_top_nude = False
    $ toph_bottom_nude = False
    $ toph_bikini = True
    $ katara_top_nude = False
    $ katara_bottom_nude = False
    $ boobs = 'medium'

    show toi toi210

    show toki toki10

    with dissolve
    show toki_swim_smile
    with dissolve
    k3 "oh, hey, aang!"
    t "nice. you made it."
    hide toki_swim_smile with dissolve
    k3 "come on, let's get in the water."
    hide toki toki10 with dissolve
    $ katara_top_nude = True
    $ katara_bottom_nude = True
    show toki toki10 with dissolve
    show ctc
    pause
    hide ctc
    y ".....nice."
    t "what?"
    menu:
        "tell her":
            y "her tits are out."
            y "....as is the rest of her."
        "encourage her find out":

            y "why don't you step forward and find out?"
            t "okay...."
            show toi toi211
            hide toki toki10
            show toki toki10:
                ypos 80
            show toki_swim_oneeye:
                ypos 80
            with dissolve
            "katara crounches down with a wink."
            y "just step forward, toph."
            t "okay..."
            hide toki_swim_oneeye
            show toki_swim_lookleft:
                ypos 80
            hide toi toi211
            show toi toi211:
                xpos 0
                linear 2 xpos 400
            show medi_lone_boob:
                ypos 80
            $ renpy.pause(1.8, hard=True)

            t "huh?"
            t "what is...."
            show toki_swim_smile:
                ypos 80
            with dissolve
            show ctc
            pause
            hide ctc
            t "......."

            hide medi_lone_boob
            hide toi toi211

    show toi toi210
    show toi_swim_surprise
    show toi_swim_blush
    with dissolve
    t "katara!"
    hide toki_swim_oneeye
    hide toki toki10
    show toki toki10
    hide toki_swim_smile
    hide toki_swim_lookleft
    show toki_swim_lookleft
    show toki_swim_smile
    with dissolve
    k3 "what?"
    t "you're... you're..."
    k3 "naked?"
    k3 "we're all friends here."
    k3 "and i really don't want to swim in {i}clothes{/i}."
    show toki_swim_blink
    hide toki_swim_lookleft
    with dissolve
    k3 "you can't tell me you're comfortable in all that."
    t "but... but..."
    k3 "besides...."
    hide toki_swim_blink
    show toki_swim_lookleft
    show toki_swim_oneeye
    with dissolve
    k3 "don't you think i'm pretty?"
    hide toi_swim_surprise
    with dissolve
    t "well... yes... but..."
    k3 "you {i}do{/i}?"
    t "well... i mean.... you...."
    show toi_swim_angry
    hide toi_swim_blush
    show toi_swim_blush
    with dissolve
    t "shut up!"
    k3 "*giggle*"
    hide toki_swim_oneeye with dissolve
    k3 "it's okay, toph. i'm just teasing you."
    show toi_swim_blink with dissolve
    t "well... don't!"
    k3 "come on, you're wearing a bikini under your swimsuit, right?"
    t "....."
    k3 "i know you'd rather just wear that instead."
    y "it would be more comfortable."
    hide toi_swim_angry
    with dissolve
    t "i... guess..."
    t "........."
    $ toph_top_nude = True
    show ctc
    pause
    hide ctc
    y "phee phew!"
    hide toi_swim_blink with dissolve
    t "what?"
    y "....i'm bad at whistling."
    t "oh."
    k3 "there you go!"
    k3 "bottoms, too. come on!"
    t "i'm not sure i'm comfortable with that...."
    menu:
        "encourage":
            y "you'll be more comfortable without those shorts."
        "taunt":

            y "come on, you wimp!"

    t "......"
    t "fine."
    $ toph_bottom_nude = True
    show ctc
    pause
    hide ctc
    k3 "look at that hot little body!"
    show toi_swim_blink with dissolve
    t "stop..."
    k3 "no really, we're not even in the water and i'm getting wet."
    t "oh, hush...."
    k3 "and i definitely see something going on in aang's shorts...."
    hide toi_swim_blink with dissolve
    t "really?"
    t "i mean... why would i care?"
    t "let's get in the water!"
    k3 "finally!"
    scene black
    scene lake_laogai_2
    show toi toi210:
        ypos -100
    show toki toki10:
        ypos -100
    show toki_swim_blink:
        ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png"
    show expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve
    k3 "aahhh...."
    t "i gotta admit, katara...."
    t "this is better."
    k3 "i told you."
    t "but because you teased me...."
    show toi toi250
    show toi_wave
    show toi_swim_smile:
        ypos -100

    $ renpy.pause(0.5, hard=True)
    play sound "audio/water_splash.mp3"
    show toki toki11
    hide toki_swim_blink
    hide toki_swim_angry
    show toki_swim_surprised:
        ypos -100
    show eyes_leftlook:
        ypos -100
    with Dissolve(0.3)

    t "take this!"



    k3 "ahh!"
    show toki_swim_smile:
        ypos -100
    hide eyes_leftlook
    show eyes_leftlook:
        ypos -100
    hide toki_swim_surprised
    with dissolve
    k3 "you wanna do this again!?"
    show toki toki110
    show toki_wave
    k3 "i'm not gonna go easy on you this time!"
    t "you might be a waterbender, but your big tits just get in the way!"
    k3 "yeah? well, your tiny tits don't protect you, like mine do!"
    show ctc
    pause
    hide ctc
    ym "(....well, i definitely like how this is going....)"
    scene black
    scene lake_laogai_2
    show toi toi210:
        ypos -100
    show toki toki10:
        ypos -100
    show toki_swim_smile:
        ypos -100
    show toki_swim_lookleft:
        ypos -100
    show toi_swim_smile:
        ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png"
    show expression "bk3/katara/swim_idle/water_standin.png"
    with Dissolve(0.3)

    t "okay, okay! i give up!"
    k3 "you better!"
    k3 "next time i won't go so easy on you."
    t "pfft. sure."
    hide toki_swim_lookleft
    k3 "alright, i'm gonna go swim for bit."
    k3 "i'll see you guys later!"
    hide toki toki10
    hide toki_swim_smile
    hide expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve
    t "thanks for this, aang."
    t "it's just what i needed."
    t "come on, let's work on your earthbending."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you train with toph."
    $ bk3_day = False
    $ earthbending +=1
    jump bk3_village_background

label earth_train_8:

    scene black with dissolve
    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    scene lake_laogai_1

    $ toph_top_nude = False
    $ toph_bottom_nude = False
    $ toph_bikini = True
    $ katara_top_nude = True
    $ katara_bottom_nude = True
    $ boobs = 'medium'

    show toi toi210

    show toki toki10

    with dissolve
    show toki_swim_smile
    with dissolve
    k3 "hey!"
    hide toki_swim_smile
    show toki_swim_lookleft
    with dissolve
    k3 "you're wearing your swimsuit again, toph...."
    t "well, yeah. i wasn't gonna just walk around in my bikini..."

    $ toph_top_nude = True
    $ toph_bottom_nude = True

    show ctc
    pause
    hide ctc
    k3 "much better."
    t "yeah yeah, quit your yappin'."
    hide toki_swim_lookleft
    show toki_swim_oneeye
    show toki_swim_smile
    with dissolve
    k3 "hey, toph..."
    hide toki_swim_oneeye
    show toki_swim_lookleft
    with dissolve
    t "what?"
    hide toki toki10
    hide toki_swim_lookleft
    hide toki_swim_smile
    show toki toki10:
        xpos 0
        linear 2 xpos -550
    show toki_swim_lookleft:
        xpos 0
        linear 2 xpos -550
    show toki_swim_smile:
        xpos 0
        linear 2 xpos -550
    hide toi toi210
    show toi toi210
    show medi_lone_boob:
        xpos 0
        linear 2 xpos -550
    $ renpy.pause(1.7,hard=True)
    k3 "poke!"
    t "hey! what the..."
    show toki_swim_blink:
        xpos -550
    with dissolve
    k3 "hehe..."
    t "are you...."
    show toi_swim_angry
    show toi_swim_blush
    with dissolve
    hide toki toki10
    hide toki_swim_blink
    hide toki_swim_smile
    hide toki_swim_lookleft
    hide medi_lone_boob
    show toki toki10
    show toki_swim_smile
    show toki_swim_lookleft
    with vshake
    t "get off me!"
    t "you're naked again!"
    show toki_swim_blink with dissolve
    k3 "yup!"
    t "why are you poking me with your stupid boobs?"
    hide toki_swim_blink with dissolve
    k3 "because you can't poke me back!"
    t "well, i'm about to punch you!"
    k3 "yeah, because you can't poke me with your tiny titties!"
    t "yes, i can! shut up!"
    k3 "no, you can't...."
    t "i'll prove i can!"
    t "here!"
    show toph_bikini_bottom:
        xzoom -1.0
    $ toph_bikini = False
    show ctc
    pause
    hide ctc
    ym "hot damn!"
    t "shut up! i'm poking this idiot!"
    k3 "just try, short stuff!"
    t "you know what? i'm just gonna earthbend your sorry ass!"
    y "ladies! ladies!"
    y "let's calm down."
    t "i'm not putting up with this!"
    show ctc
    pause
    hide ctc
    hide toi toi210
    hide toi_swim_blush
    hide toi_swim_angry
    hide toph_bikini_bottom
    hide toki_swim_smile
    with dissolve
    "toph storms off."
    y "aww...."
    k3 "woops."
    hide toki_swim_lookleft
    with dissolve
    k3 "we'll be okay after she cools off."
    y "she's got a temper, that's for sure..."
    y "what was all that about, anyway?"
    k3 "oh, i'm just buttering her up."
    k3 "for when you ask me."
    y "ask you what?"
    show toki_swim_oneeye
    with dissolve
    k3 "that's a secret!"
    y "you are really annoying, have i told you that?"
    k3 "i'll see you around...."
    hide toki toki10
    hide toki_swim_oneeye
    with dissolve
    y "damn that girl...."
    scene black with dissolve
    "you head back to the village."
    $ bk3_day = False
    $ earthbending +=1
    jump bk3_village_background


label toph_swim_blackmail:
    hide screen earth_money_date
    scene black with dissolve
    "you and suki follow katara up to where toph is waiting, but hide behind some bushes."
    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    scene lake_laogai_1

    $ toph_top_nude = True
    $ toph_bottom_nude = True
    $ toph_bikini = True
    $ katara_top_nude = False
    $ katara_bottom_nude = False

    show toi toi210
    show toki toki10
    show toki_swim_smile
    show toki_swim_lookleft
    show toi_swim_angry
    with dissolve
    k3 "hey, toph!"
    show toki_swim_surprised with dissolve
    k3 "you're looking a little... upset."
    k3 "what's going on?"
    hide toki_swim_surprised
    hide toki_swim_smile
    with dissolve
    t "aang... has been taking advantage of me."
    t "i tried your positive reinforcement, katara..."
    t "and... it didn't go at all how i thought."
    t "i can't believe he'd-"
    k3 "hey, it's okay."
    k3 "come on, i think it's time you let go."
    hide toi_swim_angry with dissolve
    t "...what?"
    k3 "you need to relax, be free."
    k3 "you love being free... doing your own thing, right?"
    t "well, yeah."
    k3 "then what are you waiting for? take off that stupid bikini!"
    k3 "look, it's easy..."
    $ katara_top_nude = True
    $ katara_bottom_nude = True
    t "yeah, i..."
    t "i guess you're right."
    $ toph_bikini = False
    show ctc
    pause
    hide ctc
    k3 "finally!"
    k3 "let's get in the water."
    scene black with dissolve
    scene lake_laogai_2
    show toi toi210:
        ypos -100
    show toki toki10:
        ypos -100
    show toki_swim_lookleft:
        ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png"
    show expression "bk3/katara/swim_idle/water_standin.png"
    with dissolve
    show toi_swim_smile:
        ypos -100
    with dissolve
    t "i always forget how calming it is in the water."
    k3 "i'm just... glad you're here with me, toph."
    show toi_swim_blush:
        ypos -100
    hide toi_swim_smile
    with dissolve
    t "oh... um... happy to..."
    show expression "bk3/toph/swim_idles/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    show expression "bk3/katara/swim_idle/water_standin.png":
        ypos 720
        linear 5.0 ypos 850
        linear 5.0 ypos 720
        repeat
    t "what the..."
    show ctc
    pause
    hide ctc
    t "umm... are you... doing this...?"
    k3 "you mean waterbending to reveal more of you?"
    t "that's... um... katara, i don't think you should..."
    k3 "toph... i'm so jealous of you."
    show toi_swim_surprise:
        ypos -100
    hide toi_swim_blush
    show toi_swim_blush:
        ypos -100
    with dissolve
    t "what?"
    show toki_swim_blink:
        ypos -100
    with dissolve
    k3 "you're so pretty."
    k3 "and little."
    k3 "i wish i had your body."
    t "are you kidding!?"
    hide toi_swim_surprise with dissolve
    t "i'd kill to have your body!"
    t "big tits, big ass, normal height..."
    t "i can feel you jiggle when i earthbend around you."
    hide toki_swim_blink with dissolve
    k3 "you can?"
    show toi_swim_blink:
        ypos -100
    with dissolve
    t "well... yeah..."
    t "it's... it's hard not to notice..."
    k3 "hey, i've always wondered, can you feel a heartbeat?"
    hide toi_swim_blink with dissolve
    t "only if i'm intentionally trying."
    t "and i've gotta be pretty close..."
    k3 "well, come here for a sec..."
    t "oh...kay..."
    hide toi_swim_blush
    hide expression "bk3/toph/swim_idles/water_standin.png"
    hide expression "bk3/katara/swim_idle/water_standin.png"
    hide toi toi210
    hide toki toki10
    hide toki_swim_lookleft
    show toi toi210:
        xpos 200 ypos -100
    show toki toki10:
        xpos -200 ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png":
        xpos 200
    show expression "bk3/katara/swim_idle/water_standin.png":
        xpos -200
    show toki_swim_lookleft:
        xpos -200 ypos -100
    show toi_swim_blush:
        xpos 200 ypos -100
    with dissolve

    show ctc
    pause
    hide ctc
    k3 "i'm always here for you, toph."
    k3 "i hope you know that."
    t "i..."
    k3 "no matter what you go through."
    t "i... i know."
    k3 "you can always come to me. i won't judge you. ever."
    t "that's... um... that's good..."

    k3 "so..."
    k3 "can you feel my heartbeat?"
    t "maybe... maybe i need to get a little... a little closer..."

    hide toi_swim_blush
    hide expression "bk3/toph/swim_idles/water_standin.png"
    hide expression "bk3/katara/swim_idle/water_standin.png"
    hide toi toi210
    hide toki toki10
    hide toki_swim_lookleft
    show toi toi210:
        xpos 230 ypos -100
    show toki toki10:
        xpos -230 ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png":
        xpos 230
    show expression "bk3/katara/swim_idle/water_standin.png":
        xpos -230
    show toki_swim_lookleft:
        xpos -230 ypos -100
    show toi_swim_blush:
        xpos 230 ypos -100
    with dissolve


    t "katara..."
    k3 "yes...?"
    hide toi_swim_blush
    hide expression "bk3/toph/swim_idles/water_standin.png"
    hide expression "bk3/katara/swim_idle/water_standin.png"
    hide toi toi210
    hide toki toki10
    hide toki_swim_lookleft
    show toi toi210:
        xpos 130 ypos -100
    show toki toki10:
        xpos -230 ypos -100
    show expression "bk3/toph/swim_idles/water_standin.png":
        xpos 130
    show expression "bk3/katara/swim_idle/water_standin.png":
        xpos -230
    show toki_swim_lookleft:
        xpos -230 ypos -100
    show toi_swim_blush:
        xpos 130 ypos -100
    with dissolve

    t "i... i don't think this is a good idea..."
    t "i'm sorry."
    show toi_swim_blink:
        xpos 130 ypos -100
    with dissolve
    t "I... i have to go."
    k3 "i'm sorry, too."
    k3 "and here i was enjoying... well..."
    hide toi_swim_blink with dissolve
    k3 "nevermind..."
    t "....."
    hide toi toi210
    hide toi_swim_blush
    hide expression "bk3/toph/swim_idles/water_standin.png"
    with dissolve
    k3 "hmmmm...."
    scene black with dissolve
    scene lake_laogai_1
    show toki toki10
    show tosi tosi10:
        xzoom -1.0 xpos 150
    with dissolve
    k3 "that went pretty well."
    y "suki, what did you see?"
    suki "um... some pretty... girly stuff."
    k3 "toph and i like each other, suki."
    suki "ohh... that explains it."
    suki "well, yeah, it looked like it."
    suki "i guess if you guys don't need me any more, i'll head back."
    hide tosi tosi10 with dissolve
    y "okay, what the hell was that, katara?"
    y "nothing happened!"
    k3 "you just don't know what to look for, but trust me, things are coming along perfectly."
    k3 "go home for now."
    k3 "but come see me as soon as you can."
    jump bk3_next


label tit_massages:
    $ toph_busty = False
    "have katara bend toph's tits before massaging?"
    menu:
        "big tits":
            $ toph_busty = True
            t "aang! you won't believe it!"
            y "what's up?"
            t "come in, quick!"
            $ toph_massage_nude = True
            $ toph_busty = True
            scene black
            scene bg_bk3_tophome_night

            show toma toma02
            show toma_smile
            show toma_blink_ani
            with dissolve
            t "look at them!"
            t "they're...."
            t "{size=+5}huuge!"
            show ctc
            pause
            hide ctc
            t "thank you!"
            y "well... it's not permanent you know."
        "little tits":

            $ toph_busty = False
            t "aang!"
            y "what's up?"
            t "come in, quick!"
            $ toph_massage_nude = True
            scene black
            scene bg_bk3_tophome_night

            show toma toma02
            show toma_uncertain
            show toma_blink_ani
            with dissolve
            t "look at them!"
            t "they're...."
            t "{size=+5}small!"
            show ctc
            pause
            hide ctc
            y "well... yeah."
            y "i warned you this would happen."


    show toma_angry
    hide toma_smile
    with dissolve
    t "well then help me!"
    y "okay, we'll keep working on them."
    show toma_uncertain
    hide toma_angry
    with dissolve
    t "well..."
    t "go ahead, then."
    show ctc
    pause
    hide ctc
    y "arms up, toph."
    show toma toma03 with dissolve
    t "...okay."
    y "repeat your mantra."
    hide toma_angry
    hide toma_blush
    show toma_uncertain
    show toma_blush
    with dissolve
    t "I... i want big ones, like katara...."
    t "i want big ones, like katara...."
    t "i want to have big, huge, ones... like katara..."
    show toma_blink with dissolve
    y "very good."
    hide toma_blink with dissolve
    t "............"
    show toma toma03 with dissolve
    t "this is still so embarrassing"
    if toph_busty:
        show toma_kneadtits:
            ypos 20
    else:
        show toma_kneadtits
    with dissolve
    y "oh, sure, for both of us."
    y "yup."
    t "...oh...uh..."
    show ctc
    pause
    hide ctc
    t "i can't believe how much this helped."
    show ctc
    pause
    hide ctc
    y "see? i told you to trust me."
    show toma toma01 with dissolve
    t "..........."
    show ctc
    pause
    hide ctc
    t "yeah..."
    if toph_busty:
        show toma_scissortits:
            ypos 20
    else:
        show toma_scissortits
    hide toma_kneadtits
    show ctc
    pause
    hide ctc
    show toma_blink with dissolve
    t "ow... mmmgh..."
    y "did you just moan?"
    show toma toma02
    show toma_angry
    hide toma_blink
    with dissolve
    t "no!"
    show ctc
    pause
    hide ctc
    hide toma_scissortits
    hide toma_angry
    show toma_uncertain
    with dissolve
    $ titslap_counter = 5
    show expression "bk3/toph/massage/tit_blush.png":
        alpha 0.0
    while titslap_counter >= 1:
        show expression "bk3/toph/massage/slap1.png"
        play sound "audio/slap.mp3"
        $ renpy.pause(0.4)
        hide expression "bk3/toph/massage/slap1.png"

        show expression "bk3/toph/massage/slap2.png"
        play sound "audio/slap.mp3"
        $ renpy.pause(0.4)
        hide expression "bk3/toph/massage/slap2.png"

        $ titslap_counter -= 1
        if titslap_counter == 0:

            if toph_massage_nude == True:
                show expression "bk3/toph/massage/tit_blush.png":

                    linear 5.0 alpha 1.0

            t "ow!! that hurt!"
            menu:
                "give her another five slaps for good measure":

                    $ titslap_counter = 5
                "This should be enough":
                    pass


    y "now lift your arms...."
    y "i just need to give them a rub down."
    y "...with sperm again."
    show toma toma03 with dissolve
    t "....."
    t "ew...."
    y "i don't want to do this either, but we don't have much of a choice."
    t ".........."
    show toma_uncertain
    hide toma_angry
    show toma_blink
    with dissolve
    t "fine, but.... just be quick."
    hide toma_blink with dissolve
    y "say please."
    t "p....please?"
    "you speed up your masturbating."
    y "yes, again."
    show toma_blink with dissolve
    t "...please..."
    y "again! eyes open!"
    show toma_angry
    hide toma_blink
    with dissolve
    t "please!"
    y "ngh!"
    play sound "audio/splurt2.ogg"
    hide toma_blink
    show toma_sperm1
    with flash
    t "ugh! your sp-"
    play sound "audio/splurt3.ogg"
    show toma_sperm2
    hide toma_sperm1
    with flash
    y "yes! fuck!"
    show toma_blink with dissolve
    t "gross! stop!"
    play sound "audio/splurt2.ogg"
    show toma_sperm3
    hide toma_sperm2
    with flash
    y "yeah... take it, slut..."
    hide toma_blink
    t "what did you say to me?"
    t "i'm going to kick your butt, you pansy little-"

    show toma_rubtits:
        ypos 0
        linear 2.0 ypos -30
        ypos -30
        linear 2.0 ypos 0
        repeat

    show toma_uncertain
    hide toma_angry
    with dissolve
    t "what... what are you doing...!?"

    y "we have to rub it in if we want the nutrients to soak into your skin."
    y "you want that, don't you?"
    t "...i..."
    show toma_blink with dissolve
    t "yes..."
    y "then thank me."
    t "thank...."
    t ".........."
    t "thank you."
    show ctc
    pause
    hide ctc
    hide toma_sperm3 with Dissolve(4.0)
    y "Ah yes, this should about do it."
    hide toma_rubtits with Dissolve(2.0)
    hide toma_blink with dissolve
    t "and... that should keep them big?"
    y "it's likely to go away for a bit, but if we keep it up, it'll come back."

    $ toph_massage +=1
    $ toph_massaged = True
    t "then i'll...."
    show toma_blink with dissolve
    t "i'll see you next time..."
    scene black with dissolve
    "you go home for the night."
    $ toph_busty = False
    jump bk3_next


label ct_hypno_menu2:
    show tomc tomc06

    with dissolve
    menu:
        "establish trigger" if not ct_hypno2_1:
            y "when i say \"[trigger]\", you will enter this state of hypnosis."
            y "and you will obey any following command."
            ct "when i hear \"[trigger]\"... i will enter this state and obey..."
            y "and... you can only be hypnotized by me."
            ct "i can only... be hypnotized by you..."
            y "nice..."
            y "take {i}that{/i}, feng."
            ct "take that-"
            y "you... don't have to repeat that."
            $ ct_hypno2_1 = True
            jump ct_hypno_menu2

        "horny for females, especially prisoners" if not ct_hypno2_2:
            y "girls now make you wet."
            y "especially prisoners... and ex-prisoners."
            ct "girls make me wet... expecially prisoners and ex-prisoners..."
            y "very good."
            $ ct_hypno2_2 = True
            jump ct_hypno_menu2

        "turned off by all men except me" if not ct_hypno2_3:
            y "you are now turned off by all men except for me."
            ct "i am now turned off... by all men except for you..."
            y "and you are a slut for me."
            ct "i am... a slut... for you..."
            y "perfect."
            $ ct_hypno2_3 = True
            jump ct_hypno_menu2

        "continue" if ct_hypno2_1 and ct_hypno2_2 and ct_hypno2_3:
            y "(i think that's enough...)"
            y "(but did it work?)"
            y "when i snap my fingers, you will awaken, with no memory of this."
            play sound "audio/fingersnap.mp3"
            y "*snap*"
            show tomc tomc01 with dissolve
            ct "what hap..."
            show tomc tomc04 with dissolve
            ct "oh, did you-"
            show tomc tomc07 with dissolve
            ct "well..."
            show tomc tomc100
            show tomc_sultry
            with dissolve
            ct "hello...."
            ct "hi... hi there."
            show tomc tomc07
            show tomc_surpise
            hide tomc_sultry
            with dissolve
            ct "i... mean..."
            show tomc_angry
            hide tomc_surpise
            show tomc_blush
            with dissolve
            ct "what... what did..."
            show tomc tomc04
            show tomc_blink
            with dissolve
            ct "....did you do what you needed to?"
            y "yeah, i think so..."
            ct "then... you should go, and i'll-"
            y "[trigger]."
            hide tomc_angry
            hide tomc_blush
            show tomc tomc06
            show headup
            with dissolve
            ct "......"
            y "this. is. amazing."
            y "but what to do?"
            y "hmmm...."
            y "kneel. don't move until i say so."
            y "i want to get a good look at you."
            scene black
            scene dark_tunnel
            with dissolve
            "you walk around ajala, getting a good look at her kneeling."
            show tonr tonr00
            with dissolve
            y "hmm... yes..."
            y "you are busty, aren't you?"
            ct "...."
            y "answer me."
            ct "i... am... busty..."
            y "hmm..."
            y "what if i just..."
            show tonr tonr01 with dissolve
            y "......"
            show ctc
            pause
            hide ctc
            y "........"
            y "bring on the titties!"
            show tonr tonr02 with dissolve
            y "damn!"
            show ctc
            pause
            hide ctc
            ct "......."
            y "well, i'm obviously going to have to play with those."
            y "what are you?"
            ct "i am... your slut..."
            y "are you the slut warden of these tunnels?"
            ct "i am... the slut... warden..."
            ct "please enjoy... my breasts..."
            y "then present them!"
            show tonr tonr03 with dissolve
            ct "...sir..."
            show ctc
            pause
            hide ctc
            ct "....."
            y "you're not very talkative."
            ct "these are... my breasts..."
            y "and?"
            ct "please... use... them..."
            y "huh."
            y "guess i'm going to have to work on your enthusiasm..."
            y "also, piercings are a very slutty choice, slave."
            y "i approve."
            ct "thank... you..."
            show tonr tonr04 with dissolve
            y "i really like these rings..."
            y "how about a little tug?"
            show tonr tonr05
            ct "{i}hn..."
            y "what was that?"
            ct "....."
            show tonr tonr06
            ct "{i}nnngh...."
            y "oh, is that pleasant?"
            show tonr tonr100
            ct "{i}ahhnn...."
            show ctc
            pause
            hide ctc
            y "ajala? are you in there?"
            y "i'm playing with your tits."
            y "what are your thoughts?"
            ct "y-yours to... u-use... sir..."
            y "hmmm... these are {i}amazing{/i}..."
            y "but you should enjoy it with me."
            y "ajala..."
            y "you have a titplay fetish."
            ct "i... have... a..."
            show tonr_lewdface_1 with Dissolve(2.0)
            ct "i... have... a... titplay... fetish..."
            show ctc
            pause
            hide ctc
            y "your sensitive nipples run deep pleasure throughout your body."
            y "the tugging, teasing sensations run from your juicy, slut tits all the way to your cunt."
            ct "the sensations... run..."
            show tonr_lewdface_tongue with Dissolve(2.0)
            ct "run... through my fat... juicy... tits..."
            ct "to my... my... cunt..."
            show ctc
            pause
            hide ctc
            y "your now sopping wet cunt."
            ct "my..."
            ct "unnngh...."
            ct "my sopping... {i}ohhh...{/i} wet cunt..."
            show tonr tonr02 with dissolve
            y "hmm...."
            y "how's your pussy?"
            ct "s-sopping... sopping wet... sir..."

            $ ajala_jin_lesson = True

            jump ajala_nipplerub_menu

            label ajala_nipplerub_menu:
                show tonr tonr02
                hide tonr_lewdface_tongue
                hide tonr_nipplerub
                with dissolve
                menu:
                    "tug on her nipple":
                        show tonr tonr100
                        show tonr_lewdface_tongue with Dissolve(1.0)
                        ct "{i}ahhnn...."
                        show ctc
                        pause
                        hide ctc
                        y "that's it, slut..."
                        y "you feel so good you want to cum..."
                        y "but i won't let you..."
                        show ctc
                        pause
                        hide ctc
                        jump ajala_nipplerub_menu
                    "fuck her nipple":

                        show tonr_nipplerub with dissolve
                        y "fuck..."
                        show ctc
                        pause
                        hide ctc
                        y "where's my cock, slut?"
                        ct "fucking... fucking my nipple..."
                        y "your areola is extra soft, slut..."
                        show tonr_lewdface_tongue with dissolve
                        y "plump it for me."
                        show tonr tonr03 with dissolve
                        y "i can feel your hard little nipple pressing under the head."
                        y "right into the tip..."
                        ct "thank... you... sir..."
                        show ctc
                        pause
                        hide ctc
                        jump ajala_nipplerub_menu
                    "rub her clothed tit":

                        show tonr tonr00 with dissolve
                        show tonr_nipplerub with dissolve
                        y "what a tight bust..."
                        show ctc
                        pause
                        hide ctc
                        y "how many people have rubbed their cocks on your chest today, slut?"
                        ct "n-none..."
                        y "don't lie to me."
                        ct "s-sir..."
                        show ctc
                        pause
                        hide ctc
                        jump ajala_nipplerub_menu
                    "tug and fuck nipple":

                        show tonr tonr04 with dissolve
                        y "now for some extra fun..."
                        show tonr_nipplerub with dissolve
                        ct "{i}nnnghhh...."
                        y "but i'm not done yet..."
                        show tonr tonr100
                        show tonr_lewdface_tongue with dissolve
                        ct "{i}ah...ahhh...."
                        show ctc
                        pause
                        hide ctc
                        jump ajala_nipplerub_menu
                    "cum":

                        menu:
                            "finish?"
                            "back to menu":

                                jump ajala_nipplerub_menu
                            "cum in nipple":

                                y "give me that fucking nipple!"
                                show tonr tonr15 with dissolve
                                ya "ngh... here it..."
                                ya "fuck!"
                                play sound "audio/splurt2.ogg"
                                show tonr_sperm1
                                with flash
                                ya "beg, slut!"
                                show tonr_lewdface_tongue with dissolve
                                ct "please... sir..."
                                ct "give me... your semen..."
                                ct "in my... nipple..."
                                ct "thank-"
                                play sound "audio/splurt3.ogg"
                                show tonr_sperm2
                                hide tonr_sperm1
                                with flash
                                y "aahh...."
                                y "well done..."
                                show tonr tonr03
                                hide tonr_sperm2
                                show tonr_sperm4
                                hide tonr_sperm1
                                with dissolve
                                ct "thank... you..."
                                show ctc
                                pause
                                hide ctc
                                show tonr tonr02
                                hide tonr_lewdface_tongue
                                with dissolve
                                y "will now find a female prisoner to lick your tits clean."
                                y "once you do, you will wake up, not remembering any of this."
                                ct "yes... sir..."
                                show ctc
                                pause
                                hide ctc
                                scene black
                                scene dark_tunnel
                                with dissolve
                                "ajala jogs off, cum dripping down her chest onto the floor."
                                scene black with dissolve
                                "exhausted, you head home."
                                $ bk3_day = False
                                jump bk3_village_background
                            "cum on face":

                                ya "show me that fucking tit!"
                                show tonr tonr03 with dissolve
                                ya "i'm gonna... fucking..."
                                show tonr_solodick
                                show tonr_lewdface_tongue
                                with dissolve
                                ya "here it comes, slut!"
                                show tonr_blink with dissolve
                                ct "give me-"

                                play sound "audio/splurt2.ogg"
                                show tonr_spermshot
                                $ renpy.pause (0.2, hard=True)
                                hide tonr_spermshot

                                show tonr_sperm6
                                ya "fuck!"
                                play sound "audio/splurt2.ogg"
                                show tonr_spermshot
                                $ renpy.pause (0.2, hard=True)
                                hide tonr_spermshot

                                hide tonr_sperm6
                                show tonr_sperm7
                                ct "........"
                                ya "beg!"
                                ct "please... sir..."
                                ct "use my face... to store... your semen..."

                                play sound "audio/splurt2.ogg"
                                show tonr_spermshot
                                $ renpy.pause (0.2, hard=True)
                                hide tonr_spermshot

                                hide tonr_sperm7
                                show tonr_sperm8
                                show ctc
                                pause
                                hide ctc
                                y "{i}aahhhh....."
                                y "at ease."
                                hide tonr_blink
                                hide tonr_solodick
                                hide tonr_lewdface_tongue
                                show tonr tonr02
                                with dissolve
                                ct "yes... sir..."
                                show ctc
                                pause
                                hide ctc
                                y "will now find a female prisoner to lick your face clean."
                                y "once you do, you will wake up, not remembering any of this."
                                ct "yes... sir..."
                                show ctc
                                pause
                                hide ctc
                                scene black
                                scene dark_tunnel
                                with dissolve
                                "ajala jogs off, cum dripping down her face onto the floor."
                                scene black with dissolve
                                "exhausted, you head home."
                                $ bk3_day = False
                                jump bk3_village_background


label visit_ajala:
    hide screen earth_money_date
    if joodee_fuck >=2 and ajala_jin_hypno ==1:
        scene dark_tunnel
        show tomc tomc01
        with dissolve
        ct "welcome back, avatar."
        y "look, i've got a problem."
        ct "oh?"
        y "i'm trying to get this jin chick to think i'm her crush, and it's not working."
        ct "hmm... well it should... unless..."
        y "....really? cryptic silence?"
        y "are you just waiting for me to ask you about it?"
        y "stop being needy and just tell me."
        ct "....fine."
        ct "if she's in love with him, it won't work."
        y "that... seems like nonsense."
        ct "believe what you want, but love transcends boundaries."
        y "who is she, snow white? come on."
        y "there's gotta be a way to redirect her love."
        ct "well... there is a prototype, but-"
        y "great!"
        y "i'll take it!"
        ct "it's not tested. i have no idea how or if it works."
        y "don't care! gimme!"
        ct "i..."
        ct "*sigh*"
        ct "...here."
        play sound "audio/win2.mp3"
        "you got the hypno room prototype!"
        ct "like i said, it might have unpredictable results..."
        y "i'mma risk it."
        ct "very well. good luck..."
        hide tomc tomc01 with dissolve
        y "ominous."
        y "now, i'll just schedule another hypno session with jin."
        $ ajala_jin_hypno = 2
        $ bk3_day = False
        jump bk3_village_background

    if joodee_fuck == 1:
        if not jin_jasmine_met:
            scene dark_tunnel
            show tomc tomc01
            with dissolve
            ct "welcome back, avatar."
            y "yeah, how do i fuck joodee?"
            show tomc tomc02 with dissolve
            $ renpy.pause(0.15,hard=True)
            show tomc tomc03 with dissolve
            $ renpy.pause(0.15,hard=True)
            show tomc tomc04 with dissolve
            ct "ah."
            ct "well... you're going to need a more powerful trigger phrase."
            y "of course."
            y "and what do i need to do to get that?"
            ct "keep rescuing girls, of course."
            y "that's it?"
            ct "yes."
            ct "now is there anything else?"
            jump ajala_tunnel_menu

        if jin_jasmine_met and jin_hypno <5:
            scene dark_tunnel
            show tomc tomc01
            with dissolve
            ct "welcome back, avatar."
            ct "so..."
            show tomc tomc02 with dissolve
            $ renpy.pause(0.15,hard=True)
            show tomc tomc03 with dissolve
            $ renpy.pause(0.15,hard=True)
            show tomc tomc04 with dissolve
            ct "you've rescued that jin girl."
            ct "congratulations."
            y "thanks?"
            y "can i get joodee's fuck trigger now?"
            ct "no... i need to be sure jin's mind control is coming along first."
            y "i'm working on it."
            ct "not hard enough."
            ct "you've hypnotized her [jin_hypno] times. bring that up to 5, and we'll talk."
            ct "anything else?"
            $ ajala_says_hypno_jin = True
            jump ajala_tunnel_menu

        if jin_jasmine_met and jin_hypno >=5:
            if joodee_fuck >=2:
                pass
            if joodee_fuck <=1:
                scene dark_tunnel
                show tomc tomc01
                with dissolve
                ct "welcome back, avatar."
                ct "so..."
                show tomc tomc02 with dissolve
                $ renpy.pause(0.15,hard=True)
                show tomc tomc03 with dissolve
                $ renpy.pause(0.15,hard=True)
                show tomc tomc04 with dissolve
                ct "jin's training is coming along, i see."
                y "how?"
                ct "what?"
                y "how do you know? you're in these dark tunnels all the time."
                ct "i have my ways."
                y "that's deus ex machina bullshit and you know it."
                ct "......"
                ct "right, well, it's happening, so..."
                ct "joodee's next trigger word, powerful enough to have sex with her, is..."
                ct "\"can you feel it now, mr. krabs?\""
                y "........."
                y "...it's not really, right?"
                ct "no, you actually just have to start crying in front of her."
                y "........."
                y "that's the trigger phrase? sobs?"
                y "just me sobbing?"
                ct "nah, i'm just messing with you."
                ct "it's actually \"bro time go time, splurt the 'gurt\"."
                y "ugh."
                ct "okay, it's really \"will you make sweet love to me, m'lady of the morning?\""
                y "...that's honestly so much worse than the others."
                ct "fine, it's really just \"wanna bang?\""
                y "....."
                ct "........"
                y "wait, really?"
                ct "yeah."
                y "it's that simple?"
                ct "easier to remember that way."
                y "....i'm disappointed in you."
                ct "i don't care."
                ct "is there anything else?"
                $ joodee_fuck = 2
                jump ajala_tunnel_menu


    if joodee_tits ==8:
        scene dark_tunnel
        show tosi tosi10:
            xzoom -1.0 xpos 100
        suki "aang?"
        suki "why are we down here?"
        suki "are we rescuing more girls?"
        show tomc tomc01
        with dissolve
        ct "hello again.... kyoshi slut."
        suki "you!"
        suki "i'll kill-"
        y "[trigger]."
        suki "......."
        ct "....."
        show tomc tomc04 with dissolve
        ct "very well done."
        ct "now... i'll need to test her, of course."
        ct "stand back."
        scene black with dissolve
        scene dark_tunnel
        show tome tome01
        with dissolve
        ct "alright, girl."
        show ctc
        pause
        hide ctc
        ct "get over here."
        y "you heard her, suki."
        show tome tome02 with dissolve
        suki "here?"
        show ctc
        pause
        hide ctc
        ct "yes...."
        ct "kiss my cunt, prisoner."
        show tome tome03 with dissolve
        suki "*smoooch*"
        show ctc
        pause
        hide ctc
        suki "*smk* *mmh*"
        ct "that's it, prisoner.... lick..."
        show tome tome04
        suki "*slurp* *slurp*"
        show ctc
        pause
        hide ctc
        ct "fuck... you have quite a gift, prisoner..."
        suki "*mmgh*"
        ct "too bad you left...."
        ct "i've started implementing mandatory cunt licks..."
        show ctc
        pause
        hide ctc
        show tome tome05 with dissolve
        ct "don't be shy, slave."
        ct "get in there."
        ct "bury that tongue in my snatch!"
        show ctc
        pause
        hide ctc
        ct "{i}mmmmm...."
        ct "you know what you're doing, slut... i'll give you that."
        ct "how much pussy do you eat?"
        suki "*smack* *slurp*"
        show tome_lewdface with dissolve
        ct "{i}ahhh... fuu....."
        ct "yes... yesss...."
        show ctc
        pause
        hide ctc
        ct "get it, slut... you fucking slut..."
        suki "*shlurp* *mmgh* *smk*"
        ct "y-yes... i love those fucking sounds..."
        ct "lap up my cunt, prisoner...."
        ct "oh... fuck... i'm... ah..."
        show tome tome04 with dissolve
        ct "don't... don't stop..."
        ct "you slut... you fucking slut..."
        ct "gonna... unngh... gonna cum..."
        suki "mmmgh....cum...."
        ct "you're gonna... you're gonna make me..."
        suki "....come....on....mmmh..."
        show tome tome03 with hpunch
        ct "{size=+5}aahh!!"
        with ushake
        ct "nnngh...!!"
        with ushake
        suki "mmmmmhh...."
        ct "ohh... fffuuuck...."
        y "having fun, suki?"
        show tome tome02
        show tome_moisture
        with dissolve
        suki "the most!"
        show ctc
        pause
        hide ctc
        ct "{i}unnghhh....."
        y "i think she's spent."
        suki "aww..."
        suki "okay..."
        show tome tome01
        hide tome_moisture
        with dissolve
        ct "........"
        ct ".................."
        hide tome_lewdface
        show tome tome06 with hpunch
        ct "unnnghh....."
        ct "so... damn... good..."
        show ctc
        pause
        hide ctc
        y "you okay?"
        ct "my pussy... still... trembling..."
        y "hmm..."
        menu:
            "jizz on her":
                "you pull out your cock and jack it to her prostrate body..."
                ya "nngh! slut!"
                play sound "audio/splurt2.ogg"
                show tonr_sperm7:
                    xpos -80 ypos 130
                with flash
                ct "{i}uughh...."
                show ctc
                pause
                hide ctc
                "she groans from the wet, sticky intrusion, but doesn't fight it."
            "piss on her":


                "you pull out your cock..."
                show tome_piss_ani:
                    ypos 20
                    linear 2.0 ypos -60
                    linear 2.0 ypos 20
                    repeat
                "....and empty your bladder on the unresponsive ajala."
                y "aahhh...."
                ct "{i}unnghh..."
                show ctc
                pause
                hide ctc
                "she groans under the spray, but doesn't fight it."
                hide tome_piss_ani
                y "property: marked."
            "get joo dee's trigger":

                pass

        y "okay, i need joo dee's trigger now."
        ct "it's... mmh...."
        y "don't you dare fall asleep right now."
        ct "what's her trigger?"
        ct "it's... \"woopsie doo, here comes the goo\"."
        y "........"
        y "that's amazing."
        y "doesn't sound like something feng would choose, though."
        ct "i... i chose it..."
        ct "i... did it... not... not feng..."
        y "what? you captured joo dee and changed her trigger?"
        y "why?"
        ct "so you would... bring me... the kyoshi..."
        ct "so... so horny lately... don't..."
        ct "...don't understand..."
        ct "......."
        y "you-"
        ct "*snooorre*"
        y "...."
        y "not bad, suki."
        y "you gotta show me how you do that."
        show ctc
        pause
        hide ctc
        scene black with dissolve
        "you head back to the village."
        $ bk3_day = False
        $ joodee_tits = 9
        jump bk3_village_background

    if joodee_tits ==7:
        y "i should bring suki with me, to meet ajala."
        y "she'll need to have done a lot of hypno sessions."
        menu:
            "continue to tunnels":
                pass
            "back to village":

                jump bk3_village_background


    scene dark_tunnel
    show tomc tomc01
    with dissolve
    ct "welcome back, avatar."
    y "oh, hey."
    show tomc tomc02 with dissolve
    $ renpy.pause(0.15,hard=True)
    show tomc tomc03 with dissolve
    $ renpy.pause(0.15,hard=True)
    show tomc tomc04 with dissolve
    ct "what is it?"
    jump ajala_tunnel_menu

label ajala_tunnel_menu:
    menu:
        "knock her out!":
            scene black with sshake
            "you smack ajala hard and she goes down."
            scene dark_tunnel
            show expression "bk3/mazect/sex/hat_ground.png"
            show toms toms00
            with Dissolve(1)
            y "that is a great postion to pass out in."
            show toms toms01
            y "this... is a nice ass."
            y "juicy, warm, welcoming."
            show toms toms02
            y "oooh, and firm, too."
            y "tight, inviting... this is a fantastic ass."
            y "....."
            y "I have time for a quickie."
            y "hmmm... ass or pussy?"
            menu:
                "in ass":
                    $ ajala_sex = 'ass'
                "in pussy":
                    $ ajala_sex = 'pussy'

            show toms toms04
            if ajala_sex == 'ass':
                y "Ass it is!"
                y "Great choice, if I do say so myself."
            else:
                y "Ah, shit... I was hoping I'd choose anal."
            y "careful..."
            show toms toms05
            y "a bit further..."
            show toms toms06 with vshake
            y "and there we are!"
            y "ajala, if you want to be fucked, stay like that."
            y "....."
            y "welp! Time get this show into gear!"
            show toms_blink with dissolve
            ct "uh... where am I...?"
            y "Aaaaww... I was hoping for u.c.s."
            y "Hold still!"
            ct "But...."

            show toms toms100
            y "ungh... yeah..."
            show ctc
            pause
            hide ctc
            y "mmmm... damn this is good..."
            y "your insides feel fucking great."
            ct "hey... this... this isn't..."
            show toms toms03

            y "Ramrod will now take navigational control!"
            y "hit 'em up, move 'em out!"
            hide toms_blink
            show toms toms101
            ct "hnng...."
            y "fuck!"
            y "almost there!"
            ct "don't... don't cum in..."
            show toms toms13
            show toms_blink

            y "fucking tight!"
            play sound "audio/splurt2.ogg"
            with flash
            y "bitch!"
            ct "you got big! what's happening!"
            play sound "audio/splurt2.ogg"
            with flash
            y "hngh...."
            show toms toms01
            if ajala_sex == 'pussy':
                show expression "bk3/mazect/sex/sperm_pussy.png"
            else:
                show expression "bk3/mazect/sex/sperm_ass.png"
            with dissolve
            y "yeah...."
            ct "thank you... for pulling out..."
            y "uh... what?"
            ct "please, avatar... don't cum in me..."
            y "i, uh, i already-"
            ct "with that dripping cum... i might get pregnant..."
            y "uh, then... okay?"
            hide toms_blink with dissolve
            ct "thank... you..."
            show ctc
            pause
            hide ctc
            y "go clean yourself up, ajala."
            ct "o...okay..."
            show toms_blink with dissolve
            ct "(why am i so wet...?)"
            y "gotta go!"
            scene black with fade
            "you head back to the village."
            $ bk3_day = False
            jump bk3_village_background


        "ask about iroh's panties" if iroh_panty_hunt ==2:
            y "hey... you haven't seen iroh's panties have you?"
            show tomc_surpise
            show tomc_blush
            with dissolve
            ct "um..."
            y "damnit, ajala!"
            y "i've been looking all over the damn place!"
            y "why? why do you have them?"
            ct "i..."
            show tomc tomc01
            hide tomc_surpise
            hide tomc_blush
            with dissolve
            ct "...was using them..."
            y "what possible use could you have with iroh's panty collection?"
            show tomc tomc07
            show tomc_surpise
            with dissolve
            ct "i was... uh..."
            ct "doing some dress-up..."
            hide tomc_surpise
            show tomc tomc100
            show tomc_sultry
            with dissolve
            y "....."
            y "well, i can't really be mad at that, i suppose."
            y "but how did you get them?"
            ct "i found them lying in these tunnels."
            y "....right."
            ct "no, really!"
            ct "there's this guy that's been hiding in the tunnels."
            ct "wears a blue outfit, has a boomerang..."
            ct "can't seem to grab him though."
            y "...."
            y "weird."
            y "but look, can you return the panties to me?"
            show tomc tomc07
            hide tomc_sultry
            show tomc_surpise
            with dissolve
            ct "i really don't want to..."
            y "come on, ajala...."
            show tomc tomc06
            hide tomc_surpise
            with dissolve
            ct "aw, man."
            ct "okay, here..."
            play sound "audio/win2.mp3"
            "you got iroh's panty collection!"
            y ".....ugh."
            ct "anything else?"
            $ iroh_panty_hunt = 3
            jump ajala_tunnel_menu
        "hypnotize ajala":

            y "[trigger]."
            y "kneel."
            scene black
            scene dark_tunnel
            with dissolve
            "you walk around ajala, getting a good look at her kneeling."
            show tonr tonr00
            with dissolve
            y "hmm... yes..."
            y "amazing. fucking. tits."
            ct "i... have... a busty... bosom..."
            y "hmm..."
            y "what if i just..."
            show tonr tonr01 with dissolve
            y "......"
            show ctc
            pause
            hide ctc
            y "........"
            y "tits!"
            show tonr tonr02 with dissolve
            show ctc
            pause
            hide ctc
            ct "......."
            y "i am never going to get tired of these...."
            ct "i am... your slut..."
            ct "please enjoy... my breasts..."
            show tonr tonr03 with dissolve
            show ctc
            pause
            hide ctc
            ct "....."
            ct "please... use... them..."
            show tonr tonr04 with dissolve
            y "i really like these rings..."
            show tonr tonr05
            ct "{i}hn..."
            y "what was that?"
            ct "....."
            show tonr tonr06
            ct "{i}nnngh...."
            y "oh, is that pleasant?"
            show tonr tonr100
            ct "{i}ahhnn...."
            show ctc
            pause
            hide ctc
            y "hmmm... these are {i}amazing{/i}..."
            ct "thank....."
            show tonr_lewdface_1 with Dissolve(2.0)
            ct "thank you...."
            show ctc
            pause
            hide ctc
            y "tell me what you're feeling."
            show tonr_lewdface_tongue with Dissolve(2.0)
            ct "pleasure... running... through my fat... juicy... tits..."
            ct "to my... cunt..."
            show ctc
            pause
            hide ctc
            ct "my..."
            ct "{i}unnngh...."
            ct "my sopping... {i}ohhh...{/i} wet cunt..."
            show tonr tonr02 with dissolve
            y "hmm...."
            y "how's your pussy?"
            ct "s-sopping... sopping wet... sir..."
            jump ajala_nipplerub_menu

        "suki lick ajala" if joodee_tits >=9:
            scene black with dissolve
            "you go to the village and bring back suki..."
            scene dark_tunnel
            show tosi tosi10:
                xzoom -1.0 xpos 100
            suki "aang?"
            suki "why are we down here?"
            show tomc tomc01
            with dissolve
            ct "hello again.... kyoshi slut."
            suki "you-!"
            y "[trigger]."
            suki "......."
            show tomc tomc04 with dissolve
            ct "very well done."
            ct "now stand back."
            scene black with dissolve
            scene dark_tunnel
            show tome tome01
            with dissolve
            ct "alright, girl."
            show ctc
            pause
            hide ctc
            ct "get over here."
            y "you heard her, suki."
            show tome tome02 with dissolve
            suki "here?"
            show ctc
            pause
            hide ctc
            ct "yes...."
            ct "kiss my cunt, prisoner."
            show tome tome03 with dissolve
            suki "*smoooch*"
            show ctc
            pause
            hide ctc
            suki "*smk* *mmh*"
            ct "that's it, prisoner.... lick..."
            show tome tome04
            suki "*slurp* *slurp*"
            show ctc
            pause
            hide ctc
            ct "fuck... you have quite a gift, prisoner..."
            suki "*mmgh*"
            ct "too bad you left...."
            ct "i've started implementing mandatory cunt licks..."
            show tome tome05 with dissolve
            ct "don't be shy, slave."
            ct "get in there."
            ct "bury that tongue in my snatch!"
            show ctc
            pause
            hide ctc
            ct "{i}mmmmm...."
            ct "you know what you're doing, slut... i'll give you that."
            ct "how much pussy do you eat?"
            suki "*smack* *slurp*"
            show tome_lewdface with dissolve
            ct "{i}ahhh... fuu....."
            ct "yes... yesss...."
            show ctc
            pause
            hide ctc
            ct "get it, slut... you fucking slut..."
            suki "*shlurp* *mmgh* *smk*"
            ct "y-yes... i love those fucking sounds..."
            ct "lap up my cunt, prisoner...."
            ct "oh... fuck... i'm... ah..."
            show tome tome04 with dissolve
            ct "don't... don't stop..."
            ct "you slut... you fucking slut..."
            ct "gonna... unngh... gonna cum..."
            suki "mmmgh....cum...."
            ct "you're gonna... you're gonna make me..."
            suki "....come....on....mmmh..."
            show tome tome03 with vshake
            ct "{size=+5}aahh!!"
            with ushake
            ct "nnngh...!!"
            with ushake
            suki "mmmmmhh...."
            ct "ohh... fffuuuck...."
            y "having fun, suki?"
            show tome tome02
            show tome_moisture
            with dissolve
            suki "the most!"
            show ctc
            pause
            hide ctc
            ct "{i}unnghhh....."
            y "i think she's spent."
            suki "aww..."
            suki "okay..."
            show tome tome01
            hide tome_moisture
            with dissolve
            ct "........"
            ct ".................."
            hide tome_lewdface
            show tome tome06 with vshake
            ct "unnnghh....."
            ct "so... damn... good..."
            show ctc
            pause
            hide ctc
            y "you okay?"
            ct "my pussy... still... trembling..."
            y "hmm..."
            menu:
                "jizz on her":
                    "you pull out your cock and jack it to her prostrate body..."
                    ya "nngh! slut!"
                    play sound "audio/splurt2.ogg"
                    show tonr_sperm7:
                        xpos -80 ypos 130
                    with flash
                    ct "{i}uughh...."
                    show ctc
                    pause
                    hide ctc
                    "she moans from the wet, sticky intrusion, but doesn't fight it."
                "piss on her":


                    "you pull out your cock..."
                    show tome_piss_ani:
                        ypos 20
                        linear 2.0 ypos -60
                        linear 2.0 ypos 20
                        repeat
                    "....and empty your bladder on the unresponsive ajala."
                    y "aahhh...."
                    ct "{i}unnghh..."
                    show ctc
                    pause
                    hide ctc
                    "she groans under the spray, but doesn't fight it."
                    hide tome_piss_ani
                    y "property: marked."
                "jizz and piss":

                    "you pull out your cock and jack it to her prostrate body..."
                    ya "nngh! slut!"
                    play sound "audio/splurt2.ogg"
                    show tonr_sperm7:
                        xpos -80 ypos 130
                    with flash
                    ct "{i}uughh...."
                    show ctc
                    pause
                    hide ctc
                    "she murmurs about the wet, sticky intrusion."
                    y "and now..."
                    show tome_piss_ani
                    "....and empty your bladder on the unresponsive ajala."
                    y "aahhh...."
                    ct "{i}unnghh..."
                    show ctc
                    pause
                    hide ctc
                    "she groans under the spray, but doesn't fight it."
                    hide tome_piss_ani
                    y "property: marked."
                "done":

                    pass

            ct "so... so good...."
            ct "*snooorre*"
            y "...."
            y "not bad, suki."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "you head back to the village."
            $ bk3_day = False
            jump bk3_village_background
        "leave":

            y "nevermind..."
            $ current_room = roomlist[1]
            $ previous_room = roomlist[1]
            scene black with dissolve
            jump bk3_maze_start



label toph_reconciliation:
    hide screen earth_money_date
    scene black with dissolve
    "toph follows you to the beach."
    stop music fadeout 1
    play music "audio/Bassa Island Game Loop.ogg"
    scene lake_laogai_1

    $ toph_top_nude = False
    $ toph_bottom_nude = False
    $ toph_bikini = False
    $ katara_top_nude = False
    $ katara_bottom_nude = False

    show toi toi06:
        xzoom -1.0
    show toki toki01
    with dissolve
    k3 "hey, guys."
    t "what are we doing here?"
    t "you could have told me we were going to the beach."
    t "...i just wouldn't have come."
    t "i'm not wearing a bathing suit in front of aang."
    k3 "*sigh..*"
    show katara_lookleft with dissolve
    k3 "look, i know things are... awkward right now between you two."
    k3 "your dynamic is changing."
    k3 "you're not sure whether to be... agreeable or angry."
    t "......"
    k3 "so you go back and forth."
    k3 "but i think we can resolve this."
    t "how?"
    t "you tricked me."
    t "I can't trust you either."
    k3 "i... really did enjoy kissing you, toph."
    k3 "and i want to spend more time with you..."
    k3 "one on one."
    k3 "but aang learning to earthbend is the most important thing."
    k3 "and without you training him, without proper encouragement..."
    k3 "the world will fall apart."
    k3 "i just helped push you along."
    t "i'm being blackmailed here!"
    y "yeah, but... you just need to..."
    y "keep it in mind."
    y "i don't {i}want{/i} to... so you should want to help me."
    t "it doesn't work like that!"
    k3 "look, most importantly, he needs to save the world."
    k3 "and aang won't learn without... very specific reinforcement."
    k3 "i think you just need to think about it differently."
    t "I don't think-"
    with sshake
    t "what's happening!?"
    with sshake
    y "I don't know!"
    hide katara_lookleft
    show firetank1:
        xpos -50 ypos 70
        linear 35.0 xpos 1500
    show firetank2:
        xpos -250 ypos 70
        linear 45.0 xpos 1500
    with sshake
    k3 "tanks!"
    k3 "the fire nation!"
    t "i'll stop them-"
    show toti toti01:
        xpos -300
    with moveinbottom
    ty "hello!"
    show toti toti04 with dissolve
    ty "sorry about this!"

    show toi toi05

    show toti toti100
    $ renpy.pause(1.3,hard=True)
    show toti toti100:
        xpos 200
        xzoom -1
    show toki_angry
    show toki_blink
    $ renpy.pause(1.3,hard=True)
    hide toti
    show toti toti02:
        xpos -300

    t "agh!"
    k3 "ow!"
    k3 "my nipples!"
    "with a swift, chi-blocking motion, ty lee hits toph and katara in several places and they become immobile."
    k3 "aang! hit her with earthbending! you're the avatar!"
    k3 "your chi isn't blocked!"
    hide toki_blink with dissolve
    k3 "and even though you're {i}without{/i} positive encouragement, you {i}should{/i} still be able to earthbend..."
    k3 "{i}right{/i}?"
    y "(this feels like a hint...)"
    y "um...."
    y "oh no...."
    y "I can't... do... earthbending..."
    y "ah... no.... what..."
    show toti toti01 with dissolve
    ty "okay then!"
    ty "bye!"
    hide toti toti01 with moveoutbottom
    k3 "they must be attacking the city!"
    k3 "without earthbending, we can't hope to help!"
    t "wait...."
    show toi toi06 with dissolve
    t "I'm... i'm starting to get some feeling back..."
    t "come on!"
    hide toi toi06
    show toki_smile
    with dissolve
    k3 "come on, let's go after her."
    y "what is happening right now? did you plan this?"
    k3 "maybe...."
    scene black with dissolve
    "katara runs after toph, heading towards the city..."
    stop music
    scene basingse_outerwall1
    show toi toi05:
        xzoom -1.0
    with dissolve
    t "I'm ready!"
    show toki toki01
    with dissolve
    k3 "oh no, they're gone..."
    show toi toi06 with dissolve
    t "but... where would they go?"
    k3 "they must be attacking somewhere else."
    k3 "probably a little, defenseless town."
    k3 "if only the avatar had been able to do something..."
    t "it's...."
    show toi_blink:
        xzoom -1.0
    with dissolve
    t "it's my fault."
    t "i'm being selfish..."
    t "....."
    hide toi_blink with dissolve
    t "aang...."
    t "whatever you need."
    t "i'll help."
    show toti toti01:
        xpos -300
    with moveinbottom
    ty "hello!"
    show toti toti04 with dissolve
    ty "sorry again!"
    show toti toti100
    $ renpy.pause(1.3,hard=True)
    show toti toti100:
        xpos 200
        xzoom -1
    $ renpy.pause(1.3,hard=True)
    hide toti
    show toti toti02:
        xpos -300
    "ty lee swiftly hits toph and katara again."
    show toti toti01 with dissolve
    ty "bye!"
    hide toti toti01 with moveoutbottom
    k3 "oh shoot darn it all dang-"
    show toi toi05 with dissolve
    t "what is her deal!?"
    t "well i can move, but... i can't earthbend..."
    t "and it looks like the city is still in danger."
    k3 "we need to get to the guards, and let them know!"
    t "but how? we need to earthbend in, and i can't..."
    k3 "aang can! he just needs... some encouragement."
    t "right!"
    t "twinkle toes! get your life together!"
    t "open the wall!"
    y "arrghghghghg......"
    y "nope, didn't work."
    k3 "toph... come on..."
    t "....fine."
    show toi toi09 with dissolve
    t "umm..."
    t "what if i..."
    t "take off..."
    t "my clothes?"
    t "will that.... help?"
    y "probably."
    t "....."
    hide toi toi09 with dissolve
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    show toi toi212
    show toi_swim_angry
    show toi_swim_blink
    show toi_swim_blush
    with dissolve
    t "...there."
    show ctc
    pause
    hide ctc
    t "get to it!"
    y "nnghah...."
    y "not working..."
    k3 "toph! uncover yourself! this is an emergency!"
    t "...."
    show toi toi210
    hide toi_swim_blink
    with dissolve
    t "fine!"
    show ctc
    pause
    hide ctc
    scene basingse_outerwall
    hide toi toi210
    show toi toi210
    hide toki toki01
    show toki toki01
    hide toi_swim_angry
    show toi_swim_surprise
    hide toi_swim_blush
    show toi_swim_blush
    with sshake
    show ctc
    pause
    hide ctc
    y "i did it!"
    t "i don't believe it....."
    scene black with dissolve
    scene market_general
    show toeg toeg03:
        xpos -300
    hide toi toi210
    show toi toi210
    hide toki toki01
    show toki toki01
    with dissolve
    dl "what's the fuss here?"
    dl "...and why is she naked?"
    hide toi_swim_blush
    show toi_swim_blink
    show toi_swim_blush
    with dissolve
    y "are you complaining?"
    dl "....i guess not...."
    y "the fire nation is attacking!"
    dl "we'll take care of it."
    dl "thank you."
    hide toeg toeg01 with dissolve
    show toi toi210
    show toki toki01
    with dissolve
    y "that wasn't a particularly inspiring response...."
    hide toi_swim_blink
    hide toi_swim_blush
    show toi_swim_smile
    show toi_swim_blush
    with dissolve
    t "we did it!"
    hide toi_swim_smile
    hide toi_swim_blush
    show toi_swim_surprise
    show toi_swim_blush
    with dissolve
    t "aang...."
    t "i'm sorry."
    t "I'll... help you."
    hide toi_swim_surprise
    hide toi_swim_blush
    show toi_swim_blush
    with dissolve
    t "I'm going to... go get dressed."
    hide toi toi210
    hide toi_swim_blush
    with dissolve
    k3 "well that worked out nicely."
    y "did you do all of this?"
    k3 "mostly. the guard was just random."
    k3 "ty lee proved very helpful."
    k3 "not sure where she went to... but i'm sure we'll see her again."
    y "well, looks like toph'll give it up more easily-"
    show toki_angry with dissolve
    k3 "no, you need to put her in her place."
    k3 "this will just make her a little... more forgiving."
    k3 "if she ever argues, you threaten to ruin her life."
    k3 "understand?"
    k3 "she needs to know her place."
    y "....."
    y "yeah, i can do that."
    hide toki_angry with dissolve
    k3 "good!"
    k3 "alright, i'm heading back."
    k3 "toph might be... particularly welcoming after today's adventure."
    k3 "go see her."
    hide toki toki01 with dissolve
    y "....."
    y "i guess i'll go see toph."
    jump bk3_village_background


label toph_blowjob1:
    $ toph_blowjob = True
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_night
    show toi toi04
    with dissolve
    t "hey."
    t "umm..."
    show toi_blink
    show toi_blush
    with dissolve
    t "so, i think what you did today counts as earthbending training."
    t "and so... um..."
    y "sit on the floor."
    hide toi_blink
    show toi toi09
    with dissolve
    t "i... what?"
    y "you're going to help me, right?"
    t "umm... yes..."
    y "then sit on your floor."
    t "...okay..."
    scene black
    scene bg_bk3_tophome_2
    show tobb tobb01
    with dissolve
    t "like this?"
    t "wait..."
    show tobb tobb02
    with dissolve
    t "what's that..."
    show tobb tobb03
    with dissolve
    t "that smell..."
    show tobb tobb04
    with dissolve
    t "is that..."
    t "that's your dick, isn't it!"
    show tobb tobb01
    show tobb_unsure
    with dissolve
    t "i'm guess i'm... doing something with it?"
    y "you're going to suck my cock."
    hide tobb_unsure with dissolve
    t "I'm... what?"
    menu:
        "mean":
            y "you're going to put that tiny little whore mouth on my cock..."
            y "and clean it off."
            show tobb_angry with dissolve
            t "i'm not cleaning your... cock... with my mouth!"
            y "do you want to ruin your life? destroy the world?"
            t "......"
            t "no...."
            show tobb_blink
            hide tobb_angry
            with dissolve
            t "okay..."
            hide tobb_blink with dissolve
            t "bring it here..."
        "nice":

            y "you don't know about blowjobs?"
            t "i... uh..."
            y "it's no big deal..."
            y "you just put your mouth on it and suck."
            t "i... i can do that..."

    show tobb_solodick with dissolve
    y "here you go."
    show tobb_unsure with dissolve
    t "what do i...."
    y "just lean forward."
    hide tobb_unsure
    show tobb tobb04
    with dissolve
    t "Like this?"
    y "yeah, except..."
    y "you know, with it in your mouth."
    show tobb tobb09
    hide tobb_solodick
    with dissolve
    t "mmmngh 'n ah?"
    y "don't talk with your mouth full."
    t "......."
    show tobb tobb100
    t "*sluurp*"
    show ctc
    pause
    hide ctc
    y "aahhhh..."
    y "good girl..."
    y "i had a long... sweaty day."
    y "so you need to slobber it clean, got it?"
    show tobb tobb09 with dissolve
    t "nnngh...."
    ya "i'm starting to get pissed."
    ya "so suck... my..."
    show tobb tobb12 with vshake
    t "unnngh!!!"
    show ctc
    pause
    hide ctc
    ya "cock!"
    show tobb tobb102
    t "*slurp* *shluup* *gulp*"
    show ctc
    pause
    hide ctc
    y "that's it... suck my dick, slut..."
    t "*gltch* *slurp*"
    show tobb tobb101
    t "*sluuurp*"
    show ctc
    pause
    hide ctc
    "toph drops farther down than you expect, taking so much of your cock that you can feel the tip turn down her throat."
    show tobb tobb102
    y "oh fuck... toph..."
    "toph pulls you in deeper and deeper... her inexperienced tongue pressing up against the underside of your shaft."
    t "*mmgh* *ahn* *sluurpp*"
    show ctc
    pause
    hide ctc
    y "yes... yes..."
    y "harder..."
    t "mmmgh..."
    y "harder!"
    show tobb tobb103
    "toph slams your cock into her throat, slurping hard on the way up..."
    t "*gulp* *gulp* *gltch*"
    show ctc
    pause
    hide ctc
    y "ff...fuu..."
    y "how are you so good at this..."
    show tobb tobb100
    show ctc
    pause
    hide ctc
    t "mmghh?"
    y "what?"
    show tobb tobb01
    show tobb_handjob
    with dissolve
    t "mmmm...."
    y "yea-"
    show tobb_slapdick
    hide tobb_handjob
    ya "ow!"
    ya "what the hell!?"
    show ctc
    pause
    hide ctc
    ya "what are you doing!?"
    t "penises are funny..."
    ya "stop it!"
    hide tobb_slapdick
    show tobb_solodick
    with dissolve
    t "wait... so that didn't feel good?"
    y "no!"
    t "oh..."
    y "look, if you want to use your hands..."
    y "first, put it in your mouth."
    hide tobb_solodick
    show tobb tobb09
    with dissolve
    y "okay, now... grab it..."
    y "confidently, but not too hard."
    show tobb tobb01
    hide tobb tobb01
    show tobb tobb01
    show tobb_unsure
    show tobb_handjob
    with dissolve
    t "ee is?"
    y "yeah, like that."
    y "move your hand up and down."
    hide tobb_handjob
    show tobb_handjob_ani
    y "just... ah... just like that..."
    show ctc
    pause
    hide ctc
    y "don't stop..."
    y "don't... fuck... you little slut..."
    hide tobb_unsure
    show tobb_angry
    hide tobb_handjob_ani
    show tobb_handjob_ani
    with dissolve
    t "mmphh! *sllurrp*"
    y "just.. just like.. ah.. ah.."
    y "I'm gonna....."
    t "hmm?"
    show ctc
    pause
    hide ctc
    menu:
        "cum in her mouth":
            hide tobb_angry
            show tobb_unsure
            hide tobb_handjob_ani
            show tobb_handjob_ani
            show tobb_blink
            with dissolve
            y "fuck!"

            play sound "audio/splurt2.ogg"
            show tobb_spermin1
            with flash
            t "nngh!"
            play sound "audio/splurt3.ogg"
            hide tobb_spermin1
            show tobb_spermin2
            with flash
            ya "take it all, toph!"
            play sound "audio/splurt1.ogg"
            hide tobb_spermin2
            show tobb_spermin3
            with flash
            y "hnngh.."
            show ctc
            pause
            hide ctc
            y "you can... can stop..."
            show tobb tobb01
            hide tobb_unsure
            hide tobb_handjob_ani
            show tobb_solodick
            show tobb_spermin4
            hide tobb_blink
            hide tobb_spermin3
            with dissolve
            show ctc
            pause
            hide ctc
            y "fuckk..."
            t "how was that?"
            y "fucking... great..."
            t "huh."
            t "that wasn't that tough."
            t "i'm gonna go clean up."
            hide tobb tobb01
            hide tobb_solodick
            hide tobb_spermin4
            with dissolve
            y ".....damn....."
            scene black with dissolve
            "you head home for the night."
            jump bk3_next
        "cum on her face":

            show tobb tobb01
            hide tobb_angry
            show tobb_solodick1
            hide tobb_handjob_ani
            with dissolve
            y "Fuck!"

            play sound "audio/splurt2.ogg"
            show tobb_spermshot
            $ renpy.pause(0.3)
            show tobb_spermout1
            hide tobb_spermshot
            t "nngh!"

            play sound "audio/splurt3.ogg"
            show tobb_spermshot
            $ renpy.pause(0.3)
            show tobb_spermout2
            hide tobb_spermout1
            hide tobb_spermshot
            ya "take it all, toph!"

            play sound "audio/splurt2.ogg"
            show tobb_spermshot
            $ renpy.pause(0.3)
            show tobb_spermout3
            hide tobb_spermout2
            hide tobb_spermshot
            y "hnngh.."

            show ctc
            pause
            hide ctc

            y "fuckk..."
            t "how was that?"
            y "fucking... great..."
            t "huh."
            t "that wasn't that tough."
            show tobb_unsure
            hide tobb_spermout3
            show tobb_spermout3
            with dissolve
            t "really... really messy though..."
            t "i'm gonna go clean up."
            hide tobb tobb01
            hide tobb_solodick1
            hide tobb_spermout3
            hide tobb_unsure
            with dissolve
            y ".....damn....."
            scene black with dissolve
            "you head home for the night."
            jump bk3_next




label toph_blowjob2:
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_2
    show tobb tobb01
    with dissolve
    t "like this?"
    t "wait..."
    show tobb tobb02
    with dissolve
    t "what's that..."
    show tobb tobb03
    with dissolve
    t "that smell..."
    show tobb tobb04
    with dissolve
    t "is that..."
    t "that's your dick, isn't it!"
    show tobb tobb01
    show tobb_unsure
    with dissolve
    t "i'm guess i'm... doing something with it?"
    y "you're going to suck my cock."
    hide tobb_unsure with dissolve
    t "I'm... what?"
    menu:
        "mean":
            y "you're going to put that tiny little whore mouth on my cock..."
            y "and clean it off."
            show tobb_angry with dissolve
            t "i'm not cleaning your... cock... with my mouth!"
            y "do you want to ruin your life? destroy the world?"
            t "......"
            t "no...."
            show tobb_blink
            hide tobb_angry
            with dissolve
            t "okay..."
            hide tobb_blink with dissolve
            t "bring it here..."
        "nice":

            y "you don't know about blowjobs?"
            t "i... uh..."
            y "it's no big deal..."
            y "you just put your mouth on it and suck."
            t "i... i can do that..."

    show tobb_solodick with dissolve
    y "here you go."
    show tobb_unsure with dissolve
    t "what do i...."
    y "just lean forward."
    hide tobb_unsure
    show tobb tobb04
    with dissolve
    t "Like this?"
    y "yeah, except..."
    y "you know, with it in your mouth."
    show tobb tobb09
    hide tobb_solodick
    with dissolve
    t "mmmngh 'n ah?"
    y "yeah, like that."
    t "......."
    show tobb tobb100
    t "*sluurp*"
    show ctc
    pause
    hide ctc
    y "aahhhh..."
    y "good girl..."
    y "i had a long... sweaty day."
    y "so you need to slobber it clean, got it?"
    show tobb tobb09 with dissolve
    t "nnngh...."
    ya "i'm starting to get pissed."
    ya "so suck... my..."
    show tobb tobb12 with vshake
    t "unnngh!!!"
    show ctc
    pause
    hide ctc
    ya "cock!"
    show tobb tobb102
    t "*slurp* *shluup* *gulp*"
    show ctc
    pause
    hide ctc
    y "that's it... suck my dick, slut..."
    t "*gltch* *slurp*"
    show tobb tobb101
    t "*sluuurp*"
    show ctc
    pause
    hide ctc
    "toph drops farther down than you expect, taking so much of your cock that you can feel the tip turn down her throat."
    show tobb tobb102
    y "oh fuck... toph..."
    "toph pulls you in deeper and deeper... her inexperienced tongue pressing up against the underside of your shaft."
    t "*mmgh* *ahn* *sluurpp*"
    show ctc
    pause
    hide ctc
    y "yes... yes..."
    y "harder..."
    t "mmmgh..."
    y "harder!"
    show tobb tobb103
    "toph slams your cock into her throat, slurping hard on the way up..."
    t "*gulp* *gulp* *gltch*"
    show ctc
    pause
    hide ctc
    y "ff...fuu..."
    y "how are you so good at this..."
    show tobb tobb100
    show ctc
    pause
    hide ctc
    t "mmghh?"
    y "what?"
    show tobb tobb01
    show tobb_handjob
    with dissolve
    t "mmmm...."
    y "yea-"
    show tobb_slapdick
    hide tobb_handjob
    ya "ow!"
    ya "what the hell!?"
    show ctc
    pause
    hide ctc
    ya "what are you doing!?"
    t "penises are funny..."
    ya "stop it!"
    hide tobb_slapdick
    show tobb_solodick
    with dissolve
    t "wait... so that didn't feel good?"
    y "no!"
    t "oh..."
    y "look, if you want to use your hands..."
    y "first, put it in your mouth."
    hide tobb_solodick
    show tobb tobb09
    with dissolve
    y "okay, now... grab it..."
    y "confidently, but not too hard."
    show tobb tobb01
    hide tobb tobb01
    show tobb tobb01
    show tobb_unsure
    show tobb_handjob
    with dissolve
    t "ee is?"
    y "yeah, like that."
    y "move your hand up and down."
    hide tobb_handjob
    show tobb_handjob_ani
    y "just... ah... just like that..."
    show ctc
    pause
    hide ctc
    y "don't stop..."
    y "don't... fuck... you little slut..."
    hide tobb_unsure
    show tobb_angry
    hide tobb_handjob_ani
    show tobb_handjob_ani
    with dissolve
    t "mmphh! *sllurrp*"
    y "just.. just like.. ah.. ah.."
    y "I'm gonna....."
    t "hmm?"
    show ctc
    pause
    hide ctc
    menu:
        "cum in her mouth":
            hide tobb_angry
            show tobb_unsure
            hide tobb_handjob_ani
            show tobb_handjob_ani
            show tobb_blink
            with dissolve
            y "fuck!"

            play sound "audio/splurt2.ogg"
            show tobb_spermin1
            with flash
            t "nngh!"
            play sound "audio/splurt3.ogg"
            hide tobb_spermin1
            show tobb_spermin2
            with flash
            ya "take it all, toph!"
            play sound "audio/splurt1.ogg"
            hide tobb_spermin2
            show tobb_spermin3
            with flash
            y "hnngh.."
            show ctc
            pause
            hide ctc
            y "you can... can stop..."
            show tobb tobb01
            hide tobb_unsure
            hide tobb_handjob_ani
            show tobb_solodick
            show tobb_spermin4
            hide tobb_blink
            hide tobb_spermin3
            with dissolve
            show ctc
            pause
            hide ctc
            y "fuckk..."
            t "how was that?"
            y "fucking... great..."
            t "huh."
            t "that wasn't that tough."
            t "i'm gonna go clean up."
            hide tobb tobb01
            hide tobb_solodick
            hide tobb_spermin4
            with dissolve
            y ".....damn....."
            scene black with dissolve
            "you head home for the night."
            jump bk3_next
        "cum on her face":

            show tobb tobb01
            hide tobb_angry
            hide tobb_handjob_ani
            show tobb_solodick1
            with dissolve
            y "Fuck!"

            play sound "audio/splurt2.ogg"
            show tobb_spermshot
            $ renpy.pause(0.3)
            show tobb_spermout1
            hide tobb_spermshot
            t "nngh!"

            play sound "audio/splurt3.ogg"
            show tobb_spermshot
            $ renpy.pause(0.3)
            show tobb_spermout2
            hide tobb_spermout1
            hide tobb_spermshot
            ya "take it all, toph!"

            play sound "audio/splurt2.ogg"
            show tobb_spermshot
            $ renpy.pause(0.3)
            show tobb_spermout3
            hide tobb_spermout2
            hide tobb_spermshot
            y "hnngh.."

            show ctc
            pause
            hide ctc

            y "fuckk..."
            t "how was that?"
            y "fucking... great..."
            t "huh."
            t "that wasn't that tough."
            show tobb_unsure
            hide tobb_spermout3
            show tobb_spermout3
            with dissolve
            t "really... really messy though..."
            t "i'm gonna go clean up."
            hide tobb tobb01
            hide tobb_solodick1
            hide tobb_spermout3
            hide tobb_unsure
            with dissolve
            y ".....damn....."
            scene black with dissolve
            "you head home for the night."
            jump bk3_next


label joodee_sex1:
    hide screen earth_money_date
    $ joodee_vag_titpull = False
    scene black with dissolve
    scene basingse_home_2
    show expression "blackveil.png"
    show tojv tojv01
    with dissolve
    show ctc
    pause
    hide ctc
    jd "are you sure you want... a mature woman like me?"

    jd "i'm sure there are-"
    y "shut up."
    y "i'm going to be inside that sweet cunt of yours, joodee."
    jd "ohh... i..."
    y "Now, spread those legs of yours."
    show tojv tojv02 with Dissolve(1.4)
    show ctc
    pause
    hide ctc
    y "i bet you know how to treat a cock right."
    jd "i can... i can try..."
    show tojv tojv03 with dissolve
    show ctc
    pause
    hide ctc
    jd "oh... my, avatar..."
    jd "i see... you're awfully ready..."
    y "Time to put some dick in there."
    jd "i... i suppose it is..."
    show tojv tojv05 with dissolve
    jd "ohh... ah..."
    show ctc
    pause
    hide ctc
    y "you seem nervous."
    jd "it's... been a while..."
    y "You might not be as nice and tight as a young girl..."
    y "...but it'll have to do."
    show tojv tojv06
    y "fuuuck.... yes.... sliding on in...."
    y "Not half bad, you old cow!"

    show tojv tojv15
    jd "my....!"
    show ctc
    pause
    hide ctc
    y "i'm inside your pussy, joodee..."
    y "i'm fucking {i}inside{/i} you!"
    jd "this is... ah... certainly... ah... happening..."

    y "You're still a bit dry."
    y "Let's correct that."
    show tojv tojv16
    show ctc
    pause
    hide ctc
    y "how's that, you big titted whore?"
    jd "ohhh...."
    y "whoa, damn girl..."
    y "we're opening some floodgates!"
    menu:
        "keep holdin' them titties":
            $ joodee_vag_titpull = True
        "Let those tits flop around on their own":
            $ joodee_vag_titpull = False

    show tojv tojv100
    show ctc
    pause
    hide ctc
    y "Damn girl!"
    y "Didn't expect you to be able and squeeze me this hard!"
    jd "ohhh...."
    show tojv tojv101
    jd "mmph!"
    show ctc
    pause
    hide ctc
    jd "av... ava... unnhh...."
    y "enjoying it, huh?"
    jd "been... so... long..."
    y "let's pick things up a bit."
    jd "i... unh... already..."
    show tojv tojv102
    jd "ohh!"
    show ctc
    pause
    hide ctc
    jd "av... avatar.. ah!... this... nngh!"
    jd "it's... ah... ohh... m-more than... ah..."
    jd "be... be gentle... i can't..."
    show tojv tojv103
    jd "aahhhh!!!!"
    show ctc
    pause
    hide ctc
    jd "too much!! too hard!!"
    jd "stop it avatar!! stop!! ahh!!"
    y "I'm gonna cum!"
    jd "ahh!! nngh!! my pussy!"
    jd "avatar! my pussy!"
    y "your sloppy cunt can take it you slut milf!"
    jd "it... unnghh!!... so.... ahhh...!"
    y "fuuck!"
    jd "please don't cum in me!"
    jd "i could still get pregnant!"
    menu:
        "cum outside":
            $ joodee_vag_titpull = False
            hide tojv
            show tojv tojv02
            with dissolve
            jd "wh-?"
            play sound "audio/splurt2.ogg"
            show expression "bk3/joodee/vaginal/solodick_sperm_outside.png":
                xpos 800
            show tojv_spermshot
            show expression "bk3/joodee/vaginal/sperm_out_1.png"
            jd "oh!"
            show ctc
            $ renpy.pause()
            hide ctc
            y "take this, slut!"
            play sound "audio/splurt3.ogg"
            show tojv_spermshot
            show expression "bk3/joodee/vaginal/sperm_out_2.png"
            jd "oh, my!"
            show ctc
            $ renpy.pause()
            hide ctc
            jd "avatar! you're-"
            play sound "audio/splurt2.ogg"
            show tojv_spermshot
            show expression "bk3/joodee/vaginal/sperm_out_3.png"
            $ renpy.pause()
            hide expression "bk3/joodee/vaginal/solodick_sperm_outside.png"
        "cum inside":


            y "then you'll bear my children, bitch!"
            y "you're a milf whore.... a broodmother fuckpig."
            y "take my seed, cow!"
            $ joodee_insem = True
            $ joodee_vag_titpull = False
            hide tojv tojv06
            show tojv tojv06
            with dissolve
            jd "wh-?"
            play sound "audio/splurt2.ogg"
            show tojv tojv06
            with flash
            jd "oh!"
            y "take this, slut!"
            play sound "audio/splurt1.ogg"
            with flash
            jd "oh, my!"
            jd "avatar! you're-"
            play sound "audio/splurt2.ogg"
            show tojv tojv02
            show expression "bk3/joodee/vaginal/sperm_inside.png":
                xpos 5
            with flash
            show ctc
            pause
            hide ctc
            jd "you... you finished inside me...."
            jd "what if i get pregnant...."


    y "Aaaah, that was great. "
    jd "you... you had sex with me..."
    jd "i had sex with... the avatar... this... aang..."
    y "well, you have a nice set of tits and a still very serviceable pussy."
    y "I don't think I have a drop of sperm left within me."
    y "anyway... you've been a wonderful host, i'm sure i'll be back."
    y "now go clean up, you fuckpig."
    $ bk3_day = False
    jump bk3_village_background


label jin_sucks:
    hide screen earth_money_date
    scene black
    $ jin_suck_eyesleft = False
    show expression "ebackgrounds/dressingroom.jpg"
    show expression "bk3/jin/sucks/zuko_picture.png"
    show tojs tojs100
    show tojs_wallhole
    show tojs_smallhole
    with dissolve
    y "....."
    y "this sucks!"
    y "i can't see anything!"
    "you carefully earthbend the hole to be a little larger..."
    hide tojs_smallhole with Dissolve(1.5)
    y "that's better...."
    "You see a suction dildo is firmly planted on the wall below a picture of a guy with a burnmark on his face."
    y "that guy looks awfully familiar..."
    y "wait... is that..."
    y "seriously?"
    if zuko > thief:
        y "this guy's gonna haunt me forever."
    jin "*MMM...*"
    jin "yeahh... *mmmm...* ...if only this was your real dick..."
    y "this is... a unique situation."
    menu:
        "keep watching in silence":
            y "she's clumsy but definitely makes up for that with vigor."
            show ctc
            pause
            hide ctc
            jump basingse_day1
        "Let her know you're there":
            y "*ahum*"
            show tojs tojs02
            with dissolve
            jin "What!?"
            show tojs tojs03
            jin "Who's there?!"
            jin "Mister Iroh, is that you?"
            jin "I told you to stop spying on me!"
            y "um... no... it's aang."
            y "you know, the avatar."
            y "dude who rescued you."
            show tojs tojs02
            jin "OH!"
            jin "Well... you shouldn't spy either!"
            y "Look, ehm, let's put that aside right now."
            y "There's something important you need to know."
            show tojs tojs01
            jin "What is it?"
            y "you... really suck."
            jin "thanks! I'm trying-"
            y "no, I mean you're really bad at giving blowjobs."
            jin "oh... Well, that's why i'm practicing."
            y "You'll never get good like that!"
            y "A dick is very sensitive... and if you mess it up you'll scare the guy off."
            jin "oh..."
            jin "now that you mention it...he IS rather skittish..."
            y "I see you have a picture hanging there..."
            y "Here's an idea..."
            y "hang that picture above this hole and I'll provide you with the real thing to practice on."
            show tojs tojs03
            jin "What?! You just want me to blow you!"
            y "i mean... yeah."
            y "...but it'll be beneficial for you too."
            y "you can look at his face and practice on a real dick."
            y "I'll give you feedback on how to improve and that guy will stick to you like glue after you show him what you've learned!"
            y "(take the bait... take the bait...)"
            show tojs tojs02
            jin "Do you really think so?"
            y "Well it depends on how good you'll become..."
            y "but nothing makes a guy happier than a good blowjob."
            y "...and i'm sure there are some hot girls circling this guy."
            y "Just waiting for a chance to make him theirs... so you'll want to start getting good fast."
            show tojs tojs03
            jin "Crap, I suspected there were a few vultures."
            show tojs tojs01
            if jin_hypno <=3:
                jin "but i don't think that's the best idea."
                jin "thanks for the offer though."
                y "(crap... maybe after a few hypno sessions she'll be willing?)"
                jump basingse_day1
            else:
                jin "Well... seeing that I did promise you a blowjob originally..."
                jin "Okay, but you better keep this a secret!"
                y "Absolutely."
                hide expression "bk3/jin/sucks/zuko_picture.png"
                hide tojs tojs01
                with dissolve
                "Jin quickly takes down the picture and puts it up on the wall you're leaning against."

                show expression "bk3/jin/sucks/bigmouth.png"
                show expression "bk3/jin/sucks/hole.png"
                with dissolve






                jin "Okay then."
                jin "Just stick it in whenever you're ready."
                show ctc
                pause
                hide ctc




                scene black
                $ jin_suck_eyesleft = True
                show expression "ebackgrounds/dressingroom_2.jpg"

                show tojs tojs01:
                    xzoom -1 xpos 535
                with Dissolve(1.5)

                show expression "bk3/jin/sucks/solodick_hard.png" with Dissolve(1.5)
                jin "Oh wow, it's... twitching?"
                jin "I didn't know they did that."
                y "Yeah, but only when they're reeaally excited."

                hide tojs
                show tojs tojs04:
                    xzoom -1 xpos 535
                jin "well..."
                jin "(....might as well get started....)"
                hide tojs
                show tojs tojs101
                show ctc
                pause
                hide ctc
                y "fuuuck..."
                jin "*mmm...*"

                jin "lee..."
                y "(lee?)"
                y "(i guess he's in disguise or something.)"
                jin "give... give me..."
                show tojs tojs102
                jin "all of it!"
                show ctc
                pause
                hide ctc
                y "damn, girl!"
                y "you're determined...."
                jin "*mmph* yes, lee!"
                y "(well, [povname], we're in a pickle now, aren't we?)"
                jin "*slurp* *gulp*"
                jin "yes... yes... fuck my slutty little mouth..."
                cus "....hello? is someone back here?"
                hide tojs
                show tojs tojs02:
                    xzoom -1 xpos 535
                jin "oh!"
                y "what are you doing?"
                y "get back to suck- er, practicing!"
                jin "I think I heard something!"
                y "Doesn't matter!"
                ya "Put it back in your mouth!"
                cus "is someone there?"
                cus "i was hoping for some service."
                y "me too...."
                show tojs tojs03
                jin "But what if she sees us!?"
                y "That's part of the thrill."
                jin "but..."
                y "let me handle it, okay?"
                jin "Oh... okay then."
                hide tojs
                show tojs tojs101
                jin "*shlurp* *gltch*"
                y "hhngh...."
                cus "are you in this... changing room?"
                "the customer is walking around the outside of the room, around the corner from where you're standing."
                "your pants are up, your cock being thrust through the wall, you might be able to get away with being seen..."
                y "ma'am?"
                jin "*slurp* *nghk* *mgmn*"
                "the customer walks around and sees you, your hips pressed firmly into the wall."
                cus "it's about-"
                cus "....."
                cus "what's happening here?"
                menu:
                    "i'm... stretching?":
                        y "i'm just... doing... stretches?"
                        cus "what kind of stretch involves you... pressing into the wall?"
                        jin "*gltch* *slurp* *mmm!*"
                        y "hip, back, you know. stretches."
                        y "do you not do these?"
                        cus "i... well, of course i do those!"
                        cus "everyone knows about those!"
                        jin "*mmm* *gnk* *sluurp*"
                        y "hngh..."
                        cus "what?"
                    "i'm getting a blowjob?":

                        y "i'm... uh... getting some head?"
                        cus "well! i never!"
                        cus "what a rude joke!"
                        jin "*gltch* *slurp* *mmm!*"
                        cus "if you didn't want to help me, you could have just said so!"
                        y "sorry, i thought it would be funny."
                        cus "you should be ashamed of yourself!"
                        jin "*mmm* *gnk* *sluurp*"
                        y "hngh..."
                        cus "what?"

                show tojs tojs103
                jin "*mmm!* *mph!* *slurrrp!*"
                show ctc
                pause
                hide ctc
                y "ffuuck..."
                cus "there's no need to swear, young man!"
                menu:
                    "make the customer leave":
                        y "i will make sure you also get service once... hrgh... the waitress is finished."
                        y "i believe her mouth -er, hands- are full right... now..."
                        cus "very well, i'll wait up front."
                        y "g-good plan..."
                        "the customer walks back up front..."
                        $ jasmine_cus = 0
                    "make the customer stay":

                        y "anyone ever tell you that you're a nosy bitch?"
                        cus "excuse me!?"
                        y "stick around for a real treat...."
                        y "I'm getting some service of my own right now, but i'll be done in a moment."
                        cus "i'm sorry?"
                        y "watch this."
                        $ jasmine_cus = 1

                if jasmine_cus >=1:
                    cus "what are-"
                y "I'm gonna cum!"
                show tojs tojs104
                jin "*mmmmph!* *sluurp!* *gulp!*"
                show ctc
                pause
                hide ctc
                jin "unload in my mouth, lee!"
                if jasmine_cus >=1:
                    cus "what!?"
                menu:
                    "swallow it all!":
                        y "swallow it, bitch!"
                        play sound "audio/splurt2.ogg"
                        hide tojs
                        show tojs tojs04:
                            xzoom -1 xpos 535
                        with flash
                        y "fuck!"
                        jin "mmgh!"
                        play sound "audio/splurt2.ogg"
                        with flash
                        jin "*gulp* *gulp*"
                        if jasmine_cus >=1:
                            cus "disgusting!"
                        play sound "audio/splurt2.ogg"
                        show tojs tojs01:
                            xzoom -1
                        hide expression "bk3/jin/sucks/solodick_hard.png"
                        show expression "bk3/jin/sucks/solodick_hard.png"
                        show expression "bk3/jin/sucks/sperm_inmouth.png"
                        with flash
                    "take it on your face!":



                        y "take it in your face, slut!"
                        hide tojs
                        show tojs tojs06:
                            xzoom -1 xpos 650
                        show tojs tojs01 with dissolve
                        jin "do it, lee!"
                        play sound "audio/splurt2.ogg"
                        show expression "bk3/jin/sucks/sperm_onface.png":
                            xpos 117
                        show tojs tojs02
                        with flash
                        y "dropping looooaaaaaaddss!!!"
                        if jasmine_cus >=1:
                            cus "disgusting!"
                        jin "yes!"
                        play sound "audio/splurt2.ogg"
                        show expression "bk3/jin/sucks/sperm_onface2.png":
                            xpos 117
                        with flash


                y "aahhh... that was great!"
                y "I mean...that wasn't too horrible."
                y "You'll have to start using your tongue more though."
                if jasmine_cus >=1:
                    cus "i... i... this is... you can't..."
                    cus "how dare you!? what is wrong with you!?"
                    cus "this is a public... i'm trying to..."
                    cus "I'm going to talk to your manager!"
                    y "aw, you're welcome."
                    y "go home and masturbate your fat, sloppy cunt, bitch."
                    cus "you... you..."
                    cus "....i'm leaving!"
                    "the customer turns and leaves abruptly..."
                    "....but her legs are pressed tightly together, as if trying to keep from making a mess."
                    ym "heh, they're all sluts."
                jin "how'd i do?"
                y "i told you, you did fine."
                y "You have room to grow, but I'm confident you will."
                jin "thanks again for helping me out!"
                y "oh, and don't do anything with zu... er... lee, yet."
                y "you still need more practice."
                jin "oh... okay."
                $ jin_sucked = True
                $ bk3_day = False
                scene black with dissolve
                scene jasmin_dragon_inside with dissolve
                show tojn tojn20 with dissolve
                jin "{size=+5}*gulp!*"
                jin "that was fun!"
                y "i'll say... but we've got some work to do still!"
                jin "i know... but it'll be worth it!"
                jin "i need a drink... my throat's a little sticky."
                jin "i'll see you around!"
                y "yeah you will."
                scene black with dissolve
                "you head back to the village...."
                jump bk3_village_background


label jin_sucks2:
    hide screen earth_money_date
    scene black
    $ jin_suck_eyesleft = False
    show expression "ebackgrounds/dressingroom.jpg"
    show expression "bk3/jin/sucks/zuko_picture.png"
    show tojs tojs100
    show tojs_wallhole
    with dissolve
    jin "*MMM...*"
    jin "yeahh... *mmmm...* ...if only this was your real dick..."
    menu:
        "keep watching in silence":
            y "she's clumsy but definitely makes up for that with vigor."
            show ctc
            pause
            hide ctc
            jump basingse_day1
        "Let her know you're there":
            y "*ahum*"
            show tojs tojs02
            with dissolve
            jin "What!?"
            show tojs tojs03
            jin "is that you, aang?"
            y "yup."
            show tojs tojs02
            jin "OH!"
            show tojs tojs01
            jin "can i suck you off?"
            jin "i need the practice."
            y "well... yeah."
            show tojs tojs01
            jin "great!"
            hide expression "bk3/jin/sucks/zuko_picture.png"
            hide tojs tojs01
            with dissolve
            "Jin quickly takes down the picture and puts it up on the wall you're leaning against."

            show expression "bk3/jin/sucks/bigmouth.png"
            show expression "bk3/jin/sucks/hole.png"
            with dissolve






            jin "Okay then."
            jin "Just stick it in whenever you're ready."
            show ctc
            pause
            hide ctc




            scene black
            $ jin_suck_eyesleft = True
            show expression "ebackgrounds/dressingroom_2.jpg"

            show tojs tojs01:
                xzoom -1 xpos 535
            with Dissolve(1.5)

            show expression "bk3/jin/sucks/solodick_hard.png" with Dissolve(1.5)
            jin "i can't get over how it... pulsates."
            y "that does happen."
            hide tojs
            show tojs tojs04:
                xzoom -1 xpos 535
            jin "well..."
            jin "(....might as well get started....)"
            hide tojs
            show tojs tojs101
            show ctc
            pause
            hide ctc
            y "fuuuck..."
            jin "*mmm...*"

            jin "lee..."
            y "(lee? oh, right...)"
            jin "give... give me..."
            show tojs tojs102
            jin "all of it!"
            show ctc
            pause
            hide ctc
            y "damn, girl!"
            y "you're determined...."
            jin "*mmph* yes, lee!"
            y "(well, [povname], we're in a pickle now, aren't we?)"
            jin "*slurp* *gulp*"
            jin "yes... yes... fuck my slutty little mouth..."
            cus "....hello? is someone back here?"
            hide tojs
            show tojs tojs02:
                xzoom -1 xpos 535
            jin "oh!"
            y "what are you doing?"
            y "get back to suck- er, practicing!"
            jin "I think I heard something!"
            y "Doesn't matter!"
            ya "Put it back in your mouth!"
            cus "is someone there?"
            cus "i was hoping for some service."
            y "me too...."
            show tojs tojs03
            jin "But what if she sees us!?"
            y "That's part of the thrill."
            jin "but..."
            y "let me handle it, okay?"
            jin "Oh... okay then."
            hide tojs
            show tojs tojs101
            jin "*shlurp* *gltch*"
            y "hhngh...."
            cus "are you in this... changing room?"
            "the customer is walking around the outside of the room, around the corner from where you're standing."
            "your pants are up, your cock being thrust through the wall, you might be able to get away with being seen..."
            y "ma'am?"
            jin "*slurp* *nghk* *mgmn*"
            "the customer walks around and sees you, your hips pressed firmly into the wall."
            cus "it's about-"
            cus "....."
            cus "what's happening here?"
            menu:
                "i'm... stretching?":
                    y "i'm just... doing... stretches?"
                    cus "what kind of stretch involves you... pressing into the wall?"
                    jin "*gltch* *slurp* *mmm!*"
                    y "hip, back, you know. stretches."
                    y "do you not do these?"
                    cus "i... well, of course i do those!"
                    cus "everyone knows about those!"
                    jin "*mmm* *gnk* *sluurp*"
                    y "hngh..."
                    cus "what?"
                "i'm getting a blowjob?":

                    y "i'm... uh... getting some head?"
                    cus "well! i never!"
                    cus "what a rude joke!"
                    jin "*gltch* *slurp* *mmm!*"
                    cus "if you didn't want to help me, you could have just said so!"
                    y "sorry, i thought it would be funny."
                    cus "you should be ashamed of yourself!"
                    jin "*mmm* *gnk* *sluurp*"
                    y "hngh..."
                    cus "what?"

            show tojs tojs103
            jin "*mmm!* *mph!* *slurrrp!*"
            show ctc
            pause
            hide ctc
            y "ffuuck..."
            cus "there's no need to swear, young man!"
            menu:
                "make the customer leave":
                    y "i will make sure you also get service once... hrgh... the waitress is finished."
                    y "i believe her mouth -er, hands- are full right... now..."
                    cus "very well, i'll wait up front."
                    y "g-good plan..."
                    "the customer walks back up front..."
                    $ jasmine_cus = 0
                "make the customer stay":

                    y "anyone ever tell you that you're a nosy bitch?"
                    cus "excuse me!?"
                    y "stick around for a real treat...."
                    y "I'm getting some service of my own right now, but i'll be done in a moment."
                    cus "i'm sorry?"
                    y "watch this."
                    $ jasmine_cus = 1

            if jasmine_cus >=1:
                cus "what are-"
            y "I'm gonna cum!"
            show tojs tojs104
            jin "*mmmmph!* *sluurp!* *gulp!*"
            show ctc
            pause
            hide ctc
            jin "unload in my mouth, lee!"
            if jasmine_cus >=1:
                cus "what!?"
            menu:
                "swallow it all!":
                    y "swallow it, bitch!"
                    play sound "audio/splurt2.ogg"
                    hide tojs
                    show tojs tojs04:
                        xzoom -1 xpos 535
                    with flash
                    y "fuck!"
                    jin "mmgh!"
                    play sound "audio/splurt2.ogg"
                    with flash
                    jin "*gulp* *gulp*"
                    if jasmine_cus >=1:
                        cus "disgusting!"
                    play sound "audio/splurt2.ogg"
                    show tojs tojs01:
                        xzoom -1
                    hide expression "bk3/jin/sucks/solodick_hard.png"
                    show expression "bk3/jin/sucks/solodick_hard.png"
                    show expression "bk3/jin/sucks/sperm_inmouth.png"
                    with flash
                "take it on your face!":



                    y "take it in your face, slut!"

                    hide tojs
                    show tojs tojs06:
                        xzoom -1 xpos 650
                    show tojs tojs01 with dissolve
                    jin "do it, lee!"
                    play sound "audio/splurt2.ogg"
                    show expression "bk3/jin/sucks/sperm_onface.png":
                        xpos 117
                    show tojs tojs02
                    with flash
                    y "dropping looooaaaaaaddss!!!"
                    if jasmine_cus >=1:
                        cus "disgusting!"
                    jin "yes!"
                    play sound "audio/splurt2.ogg"
                    show expression "bk3/jin/sucks/sperm_onface2.png":
                        xpos 117
                    with flash


            y "aahhh... that was great!"
            y "I mean...that wasn't too horrible."
            y "You'll have to start using your tongue more though."
            if jasmine_cus >=1:
                cus "i... i... this is... you can't..."
                cus "how dare you!? what is wrong with you!?"
                cus "this is a public... i'm trying to..."
                cus "I'm going to talk to your manager!"
                y "aw, you're welcome."
                y "go home and masturbate your fat, sloppy cunt, bitch."
                cus "you... you..."
                cus "....i'm leaving!"
                "the customer turns and leaves abruptly..."
                "....but her legs are pressed tightly together, as if trying to keep from making a mess."
                ym "heh, they're all sluts."
            jin "how'd i do?"
            y "i told you, you did fine."
            y "You have room to grow, but I'm confident you will."
            jin "thanks again for helping me out!"
            y "oh, and don't do anything with zu... er... lee, yet."
            y "you still need more practice."
            jin "oh... okay."
            $ jin_sucked = True
            $ bk3_day = False
            scene black with dissolve
            scene jasmin_dragon_inside with dissolve
            show tojn tojn20 with dissolve
            jin "{size=+5}*gulp!*"
            jin "that was fun!"
            y "i'll say... but we've got some work to do still!"
            jin "i know... but it'll be worth it!"
            jin "i need a drink... my throat's a little sticky."
            jin "i'll see you around!"
            y "yeah you will."
            scene black with dissolve
            "you head back to the village...."
            jump bk3_village_background

label toph_maze_training:
    $ toph_tunnel_training = 1
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_3
    show toi toi04
    with dissolve
    y "okay... so why are we here?"
    t "well, you know how the tunnels are below the lake?"
    y "yes, obviously."
    t "well, we're right above a section that's far away from the entrance."
    y "so...?"
    y "when do we get to the fun stuff?"
    show toi toi08 with dissolve
    t "right now!"
    y "what do you mean?"
    y "what am i going to do?"
    show toi toi07 with dissolve
    t "survive!"
    y "what?"
    show toi toi07:
        zoom 3.5 xpos -700
        ypos 1800
    t "survive!" with sshake
    play sound "audio/earthquake.mp3"
    scene black
    y "aahhh!!!" with sshake
    jump bk3_maze_start

label toph_anal1:
    hide screen earth_money_date
    scene black with Dissolve(1)
    scene expression "ebackgrounds/boobjob.jpg"
    show toaa toaa01
    with dissolve
    y "whoa."
    show ctc
    pause
    hide ctc
    t "you... wanted my..."
    t "my... butt..."
    t "right?"
    t "you wanted... anal, didn't you?"
    menu:
        "very much so":
            y "i... yes, definitely."
        "shut up and spread":

            y "shut your mouth and open your thighs."
    t "o-okay..."
    show toaa toaa03 with dissolve
    t "umm...."
    t "is... this okay?"
    t "it's probably not... as pretty as you wanted..."
    show ctc
    pause
    hide ctc
    menu:
        "you'll just have to make it up to me...":
            y "you think such a tiny asshole can satisfy me?"
            y "i'll just have to use you extra hard."
        "it's perfect":

            y "it's... beautiful."
            y "just what i wanted."

    y "and it's definitely not going to be pretty when i'm through."
    t "oh..."
    k3 "mind if i join you?"
    show toaa toaa04 with dissolve
    show ctc
    pause
    hide ctc
    k3 "this is what we were working on."
    k3 "toph has never had so much as a finger in her anus..."
    k3 "and so she asked for my help."
    k3 "so... to get things started..."
    show toaa toaa05
    show toaa_blink_toph
    with dissolve
    t "ohhh...."
    show ctc
    pause
    hide ctc
    k3 "i'm here to help the two of you through this."
    k3 "that's it, toph..."
    k3 "relax, while i play with your giving pussy..."
    k3 "...look at this perfect little butthole..."
    k3 "untouched... tight... soft..."
    k3 "so... inviting....."
    k3 "........"
    k3 "i just...."
    show toaa toaa06
    hide toaa_blink_toph with dissolve
    t "katara!"
    show ctc
    pause
    hide ctc
    k3 "*mmmm....*"
    t "what... what are you..."
    t "hhnmm... it's... mmn..."
    t "is it... okay that it... feels... good...?"
    show toaa_blink_toph with dissolve
    k3 "shhh..."

    k3 "it should feel good."
    hide toaa_blink_toph with dissolve
    k3 "this will just make it easier...."
    show toaa toaa04
    show toaa_stroke
    with dissolve
    k3 "are you almost ready to enter her?"
    show ctc
    pause
    hide ctc
    y "i. am. rock. hard."
    k3 "okay, good... but she still needs a little more, i think."
    show toaa_handrub:
        parallel:
            ypos 0
            linear 1.0 ypos 10
            linear 1.0 ypos 0
            repeat
        parallel:
            xpos 0
            linear 1.0 xpos 10
            linear 1.0 xpos 0
            repeat
    k3 "here...."
    show ctc
    pause
    hide ctc
    k3 "she's almost ready."
    t "umm... it's... this is really embarrassing..."
    k3 "okay, i think she's warmed up...."
    k3 "are you ready?"
    jump toph_anal_menu1

label toph_anal_menu1:
    menu:
        "lick it again":
            hide toaa_handrub
            hide toaa_stroke
            show toaa toaa06
            t "ka...katara..."
            show ctc
            pause
            hide ctc
            k3 "*mmmm...*"
            show toaa toaa04
            show toaa_stroke
            k3 "how about now?"
            jump toph_anal_menu1
        "rub it some more":

            show toaa_stroke
            show toaa_handrub:
                parallel:
                    ypos 0
                    linear 1.0 ypos 10
                    linear 1.0 ypos 0
                    repeat
                parallel:
                    xpos 0
                    linear 1.0 xpos 10
                    linear 1.0 xpos 0
                    repeat
            k3 "of course..."
            show ctc
            pause
            hide ctc
            t "katara, touching it is... it feels weird..."
            k3 "wanna fuck her yet?"
            jump toph_anal_menu1
        "hell yeah i'm ready!":

            y "sure, i'll pound her tight little ass."
            hide toaa_handrub
            show toaa_dickhold
            with dissolve
            "katara lightly holds your cock, twitching almost painfully in her gentle grip."
            t "is it... um..."
            show ctc
            pause
            hide ctc
            t "is... is it out...?"
            t "i... i think i'm ready..."
            t "but i'm not so sure any more...."
    y "good."
    t "......"
    k3 "it's okay, toph."


    hide toaa_stroke with Dissolve(1.5)

    k3 "Here, this will make it easier to slide in."
    hide toaa_dickhold
    show toaa_dicksuck
    with dissolve
    "katara pops your cock into her mouth... warm, wet, and inviting."
    k3 "'ook at 'er."
    show ctc
    pause
    hide ctc
    "katara caresses the most sensitive parts of your tip with her expert tongue, coaxing out your precum through her inviting licks."
    "...all the while, you stare at toph."
    "her confused, unseeing expression stiffens you in katara's mouth... her knowledgeable sucks drawing you to engorged readiness."
    k3 "'eady?"
    "you nod, almost regretfully, as katara lifts her mouth from your cock."
    show toaa toaa07
    hide toaa_dicksuck
    with dissolve
    k3 "here we go, toph."
    show toaa_dickguide with dissolve
    t "it's... "
    t "i can feel it..."
    show ctc
    pause
    hide ctc
    k3 "we're going to start pushing it in..."
    t "oka-"
    show toaa toaa08
    hide toaa_dickguide
    show toaa_blink_toph
    with dissolve
    t "ohhhh....."
    show ctc
    pause
    hide ctc
    t "it's... hnh... ahh..."
    k3 "you're okay, toph."
    k3 "a little more..."
    show toaa toaa09 with dissolve
    t "wai... ah... it's... ah..."
    k3 "a little more..."
    show toaa toaa10 with dissolve
    t "hnngh... ow... oww.... it hurts..."
    t "it hur-"
    show toaa toaa11 with dissolve
    t "aahngh...!"
    t "wait... wait...!"
    t "it hurts... it hurts!"
    k3 "i know, toph... i know..."
    k3 "you need him to take it out?"
    t "no! i can... i can take it...!"
    t "I'm not a... a wimp..."
    t "........"
    t "ow...! oww!"
    t "i'm trying... i'm... but... it's stretching.,.. oww..."
    t "ow...! ow! pull it out!"
    show toaa toaa07
    hide toaa_blink_toph
    show toaa_dickguide
    with dissolve
    t "i'm sorry..."
    t "i'm sorry, but it's... so painful..."
    t "it's like it's pushing me apart inside."
    k3 "it's okay... we're just going to start slowly."
    show toaa toaa08
    hide toaa_dickguide
    with dissolve
    k3 "now..."
    k3 "in and out..."
    k3 "just the tip."
    show toaa toaa107
    show toaa_blink_toph with dissolve
    t "hnghh..."
    show ctc
    pause
    hide ctc
    k3 "that's it... just like that..."
    t "ahh... oh... ow..."
    t "my... butt... is... ngh..."
    k3 "how do you feel, toph?"
    hide toaa_blink_toph with dissolve
    t "ahh... b-better..."
    k3 "good... go deeper, aang."
    show toaa toaa11 with dissolve
    t "aahhh.... *gasp*"
    t "it's... ow... too..."
    k3 "more."
    menu:
        "gentle":
            show toaa toaa12
            show toaa_blink_toph
            with dissolve
            t "aaahhhngh.... ohh..."
        "hard":

            show toaa toaa12
            show toaa_blink_toph
            with vshake
            t "aaahhh!!!!"
            t "owww! oww!"
            t "my ass! ow!"
            t "why, aang!?"

    show ctc
    pause
    hide ctc
    k3 "now start fucking!"
    t "wait, please, i'm not enjoying-"
    show toaa toaa100
    t "ahhh...ah...ow!...oh..."
    show ctc
    pause
    hide ctc
    t "please... please... ow... my bottom... my b... ohh..."
    t "it hurts! i don't-"
    hide toaa_blink_toph
    show toaa toaa16
    t "oh!"
    show ctc
    pause
    hide ctc
    t "that... that feels... ah... it's... ow... ah..."
    t "that's not so... bad... ah..."
    menu:
        "wreck that ass!":
            show toaa toaa105
            t "aahhh!!!"
            $ toaa_wrecked_ass = True
            y "I'm gonna ruin that tight little ass of yours!"
            y "i'm gonna give you a wide... fucking... asshole..."
            t "*whimper*"
            show ctc
            pause
            hide ctc
            k3 "yes! fuck that ass, aang!"
            k3 "this little whore deserves your cock right up her asshole!"
            k3 "she's a little bitch, aang! fuck her!"
            k3 "fuck the self-important bitch!"
        "keep going slowly":

            $ toaa_wrecked_ass = False
            t "oohhh...."
            y "Fuck! You're like a goddamn clamp, Toph!"
            show ctc
            pause
            hide ctc
            k3 "that's it... fill that ass, aang..."
            k3 "this little whore deserves your cock... right up her asshole..."
            k3 "she's a little bitch, aang... fuck her..."
            k3 "fuck this slut..."

    t "ahh.... ahnh!... ohhn..."
    t "how... oww... is... it...?"
    y "your... ngh... ass is a cum receptacle... and don't you forget it!"
    t "i... ow... won't... hngh..."
    y "I'm getting... really close now, guys!"

    menu:
        "cum in her ass":
            play sound "audio/splurt2.ogg"
            hide toaa
            show toaa toaa11
            show toaa_blink_toph
            with flash
            ya "hngh!"

            play sound "audio/splurt1.ogg"
            show toaa_lewdface
            hide toaa_blink_toph
            with flash
            t "hahh... ahh... ohh..."
            k3 "mmm.... fill her butt..."
            play sound "audio/splurt2.ogg"
            with flash
            show toaa toaa07

            show toaa_ass_done
            show expression "bk3/toph/anal/cuminside.png"
            t "ohhh...."
            show ctc
            pause
            hide ctc
            t "see... i... i told you i could... take it..."
            k3 "...."
            k3 "you look... tasty..."
            t "kata-"
            hide toaa_ass_done
            show toaa toaa17
            with dissolve
            k3 "mmmmm...."
            t "unnghh...."
            show ctc
            pause
            hide ctc
        "cum all over her":

            hide toaa
            show toaa toaa07
            show toaa_lewdface

            show toaa_ass_done
            t "hhgh..."
            ya "take this!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/anal/cumoutside1.png"
            with flash
            $ renpy.pause()
            y "fuck!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/anal/cumoutside2.png"
            with flash
            $ renpy.pause()
            k3 "yes, baby! give it to her!"
            k3 "cover us, aang..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/anal/cumoutside3.png"
            with flash
            $ renpy.pause()
            t "see... i... i told you i could... take it..."
            k3 "...."
            k3 "you look... tasty..."
            t "kata-"
            hide toaa_ass_done
            show toaa toaa17
            with dissolve
            k3 "mmmmm...."
            t "unnghh...."
            show ctc
            pause
            hide ctc

    show toaa_blink_toph
    show toaa toaa01_1
    with dissolve
    t "hmah...nnhh..."
    k3 "um... toph?"
    k3 "toph?"
    t "mmhm...."
    k3 "well... i think you can go, aang."
    k3 "looks like she passed out."
    k3 "i'll stay with her for now."
    k3 "....clean her up a bit...."
    y "naughty."
    k3 "i think i learned well."
    k3 "go on."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "exhausted, you head home for the night."
    jump bk3_next


label toph_anal2:
    hide screen earth_money_date
    scene black with Dissolve(1)
    scene expression "ebackgrounds/boobjob.jpg"
    show toaa toaa01
    with dissolve
    y "aw yiss."
    show ctc
    pause
    hide ctc
    t "do you... want to... get started?"
    y "what do you think?"
    t "...."
    show toaa toaa03 with dissolve
    show ctc
    pause
    hide ctc
    t "h-here..."
    menu:
        "open her up with your finger":
            show toaa_fingering
            t "ohh...."
            show ctc
            pause
            hide ctc
            y "damn... i forget how tiny and tight you are sometimes..."
            t "it... it doesn't hurt so bad..."
            t "is this... your... dick?"
            t "it hurts a little, but..."
            t "i can... i can do this..."
            y "not even close."
            t "oh... oh, no..."
            hide toaa_fingering
            y "Time for some dick up your ass, Toph."
            t "......."
        "Foreplay is for people who care":

            pass

    show toaa toaa20 with dissolve
    t "be... gentle..."
    t "Please..."
    menu:
        "okay":
            show toaa_blink_toph
            show toaa toaa101
            t "hhngh...!"
        "no":

            show toaa toaa24
            show toaa_blink_toph
            with vshake
            t "aahhh!!!!"

    show ctc
    pause
    hide ctc
    t "ahh... ahh... my poor ass..."
    hide toaa_blink_toph with dissolve
    t "is... are you almost finished...?"

    menu:
        "wreck that ass!":
            y "well...."
            show toaa toaa106
            $ toaa_wrecked_ass = True
            t "aaahh!!! f-fuck! aang!"
            y "yes?"
            t "it... oww!!!"
            y "I'm gonna ruin that tight little ass of yours!"
        "keep going slowly":
            $ toaa_wrecked_ass = False
            y "Fuck! You're like a goddamn clamp, Toph!"

    t "ahhh... aang... it... it hurts..."
    y "I'm getting... really close now, Toph!"
    t "fin... finish..."
    t "please!"
    menu:
        "cum in her ass":

            play sound "audio/splurt2.ogg"
            hide toaa
            show toaa toaa23
            show toaa_blink_toph
            with flash
            ya "hngh!"

            play sound "audio/splurt1.ogg"
            show toaa_lewdface
            hide toaa_blink_toph
            with flash
            t "hahh... ahh... ohh..."
            play sound "audio/splurt2.ogg"
            with flash
            t "splashing... in my... insides..."
            t "fuck..."
            show toaa toaa03

            show toaa_ass_done
            show expression "bk3/toph/anal/cuminside.png"
            with dissolve
            t "ohhh...."
            show ctc
            pause
            hide ctc
            t "see... i... i told you i could... take it..."
            hide toaa_ass_done
        "cum all over her":


            hide toaa
            show toaa toaa03
            show toaa_lewdface

            show toaa_ass_done
            t "hhgh..."
            ya "take this!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/anal/cumoutside1.png"
            with flash
            $ renpy.pause()
            y "fuck!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/anal/cumoutside2.png"
            with flash
            $ renpy.pause()
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/anal/cumoutside3.png"
            with flash
            $ renpy.pause()
            t "see... i... i told you i could... take it..."
            hide toaa_ass_done

    show toaa_blink_toph
    show toaa toaa01_1
    with dissolve
    t "hmah...nnhh..."
    y "um... toph?"
    y "toph?"
    t "mmhm...."
    y "well... i think i should go."
    y "it looks like she passed out."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "exhausted, you head home for the night."
    jump bk3_next

label june_bj1:
    hide screen earth_money_date
    ju "thank... thank you..."
    ju "i'll... get started..."
    y "get on the fucking ground."
    ju "yes... sir..."
    $ tojh_dick = 'shaft'
    show expression "bk3/june/blowjob/inside_tavern_2.jpg"
    show tojh tojh02
    with fade

    y "Good, park your pretty ass right there."
    y "Show me your cunt, girl."

    show tojh tojh03 with dissolve
    show ctc
    pause
    hide ctc
    y "now..."
    y "It's time for you to put those pretty red lips of yours to work."
    show tojh tojh04
    y "you get the honor of jacking my cock."
    y "warm it up."
    ju "It looks so formidable... intense, powerful... I can't wait to taste it."
    y "Oh, you will."
    y "actually, I can't remember the last time i cleaned it, so you'll be taking care of that."
    y "i expect you to taste its full rancidness."
    ju "Thank you!"
    y "That's a good little bitch."
    y "Now starting jacking."

    show tojh tojh05
    ju "it's so impressive..."
    show ctc
    pause
    hide ctc
    ju "i can't believe i get to touch it."
    ju "it's almost good enough to make me cum again..."
    y "you don't have my permission, but fuck that's good."
    y "Okay, time for the real deal."
    show tojh tojh04

    y "You can't just suck on it yet."
    show tojh tojh11 with Dissolve(1.5)
    y "I'm going to fuck your lips."
    y "not your mouth - your lips, understand?"
    ju "i... i think so."
    y "I want you to work my shaft with those full red lips of yours, but on the outside."
    y "Do a good job and i might let you give me a real blowjob."
    ju "i'll do my very best, master."

    show tojh tojh100
    y "Yeah, up and down the shaft, you gotta deserve a proper blowjob, bitch."
    show ctc
    pause
    hide ctc
    y "Man, I should've started doing this way earlier."
    y "Another girl on the other side doing the same would be even better."
    ju "*Slurp* *gag* slurp*"
    y "You like that huh?"
    y "Lying there with your legs wide open and your pussy on display."
    ju "mmmm... *sluurp*"
    y "Anyone could walk in on us at any moment, seeing you slobbering all over my dick as if it's the tastiest thing ever."
    ju "Mmmmmmhh... *slurp...* it's so tasty..."
    y "You know what? You're really good at this."
    y "Maybe I should reward you."
    menu:
        "You can give me a real blowjob now":
            $ tojh_dick = 'blow'
        "Just keep going at it like this":
            $ tojh_dick = 'shaft'
        "Jack it some more":
            show tojh tojh05

    y "Yeah, just like that you filthy slut..."
    y "And what a nice view too."
    if june_pubes == 'shaven':
        y "A nice shaven pussy, just the way I like it."
    else:
        y "Looking at that hairy jungle of yours makes me even harder than before."
        y "I think I'm hard enough to hammer nails with it."

    if tojh_dick == 'shaft':
        y "alright, whore... you've earned your meal."
        y "put it in your mouth."
        show tojh tojh100
        $ tojh_dick = 'blow'
        ju "mmmm... *sluurrrp* *gulp*"
        y "Aah, yeah suck that cock."
        ju "*mmmm*"
        ju "i'm so wet... fuck..."
        y "Suck it like it's the last cock you'll ever get to taste."
        ju "no! i need this cock!"

    menu:
        "You keep doing that baby":
            pass
        "Hmm, hold still I'm going test your gag reflexes.":

            show expression "bk3/june/blowjob/leg2.png"
            show tojh tojh20
            with Dissolve(1.5)
            y "relax your jaw."
            show tojh tojh21
            y "You like that?"
            show tojh tojh22
            y "No problem so far, right?"
            show tojh tojh23
            y "Last stop before gag city."
            show tojh tojh24 with hpunch
            y "Yeah, that's another thing altogether, isn't it?"
            show tojh tojh24 with hpunch
            y "Just pass out when you feel you've hit your limit. I don't mind."
            show ctc
            pause
            hide ctc
            show tojh tojh24 with hpunch
            y "And this is just the start of our little skullfucking session."

            show tojh tojh101
            show ctc
            pause
            hide ctc
            y "you're a lot tougher than I thought June. Good for you!"
            show ctc
            pause
            hide ctc
            y "good job, now back to the shaft."
            y "No resting in between."
            y "That's what your lunchbreaks are for."
            ju "*gagh!* *slurrp!* *gltch!* *gnk!*"
            ju "i don't... *gltch*... get... *gnk!*... lunchbreaks... *gngk!*"
            y "no? then i'll give you your protein now!"
            $ tojh_dick = 'shaft'
            hide expression "bk3/june/blowjob/leg2.png"
            show tojh tojh100
    y "damn i love your tits..."
    y "your fat fucking tits..."
    y "fuck..."
    y "...getting close..."
    ju "yes, master..."
    ju "i want that cum all over my filthy slutty little tongue, spray all over these titties..."
    ju "throbbing rock hard cum juice all over my big milky titties..."
    ju "squeezing the cum out of your fucking dick..."
    ju "squeezing the cum out of your rock hard cock..."
    ju "pull it out of your shaft and balls, right out onto me..."
    ju "come on baby... come on..."
    menu:
        "cum in her mouth":
            $ tojh_dick = 'blow'
            show tojh tojh12
            play sound "audio/splurt2.ogg"
            y "slut!"
            with flash
            play sound "audio/splurt2.ogg"
            ju "mmm!?!"
            show tojh tojh06
            show expression "bk3/june/blowjob/sperminmouth.png"
        "cum over her body":
            show tojh tojh06
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/blowjob/spermout1.png"
            y "slut!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/blowjob/spermout2.png"
            ju "ahh..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/blowjob/spermout3.png"
            y "fuck!"


    ju "*Cough*... *cough*..."
    ju "this is the whore that you love, isn’t it?"
    ju "look at me, all covered with your warm cum..."
    y "That was nice, but I got shit to do. Go clean yourself up."
    ju "....*mmm*...."
    jump bk3_next

label ty_suki_skye1:
    hide screen earth_money_date
    scene black with Dissolve(1)
    show expression "bk3/skye/sex/brothel_skyeroom.jpg"

    $ skye_fuck = 'none'

    show toss_suki00
    show toss_tylee00
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    ty "hey! you wanted to see us?"
    y "that's correct! good job, ty lee!"
    ty "thanks! heehee...."
    suki "do you have something for us?"
    y "in a sense..."
    y "Skye and I are going to fill up some holes... in your education."
    suki "i'm ready to learn."
    ty "me too!"
    y "great. now scoot over."
    y "make room for skye."

    hide toss_suki00
    show toss_suki01
    show toss toss00
    hide toss_tylee00
    show toss_tylee01
    with Dissolve(1.5)
    skye "okay, girls."
    skye "today is all about taking it in the ass!"
    skye "there's gonna to be a test at the end, so you better be anal about doing it right!"
    y "....leave the one liners to me."
    skye "no."
    skye "now pay attention girls - i've asked the avatar here to help out."
    skye "he's very busy, so pay attention."
    skye "we don't want to have to do this a lot of times, now do we?"
    y "(i mean... i wouldn't mind...)"
    skye "take it out, please."
    show toss_dickup with Dissolve(1.5)
    ty "hot!"
    suki "that... goes in your butt?"
    skye "don't be shy, aang!"
    $ skye_fuck = 'rub'
    hide toss_dickup
    skye "mmmm.... look at that erect cock, girls!"
    skye "it's not every day you get to see one this big and gorgeous."
    ty "I bet it could push it's way through gravel!"
    suki "........"
    suki "{size=-5}....wow...."
    skye "It's clearly ready, but to loosen up my ass, I'll do a few dry runs first."
    show toss toss03 with dissolve
    skye "okay, so you want to start by rubbing your ass on it to get into the mood."
    skye "watch closely."
    show toss toss100
    show ctc
    pause
    hide ctc
    skye "*moan*"
    skye "that's it... yeah... that's it..."
    skye "press that big handsome cock into my ass..."
    skye "you... ha... want to cup it with your... unh... cheeks..."
    skye "squeeze him... nice... ah... and tight..."
    skye "they love big... mmmm... warm butt cheeks."
    show ctc
    pause
    hide ctc
    show toss toss00 with dissolve
    skye "now, once you've warmed up both his cock and your ass..."
    skye "don't waste it!"
    skye "avatar! you can put it in my ass now."

    $ skye_fuck = 'anal'
    show toss_dickhelp
    with pflash
    skye "ahh... y-yeah... that's in-inside me..."
    skye "okay, once... ah... the tip is securely inserted...."
    hide toss_dickhelp with dissolve

    skye "slowly backup onto it."
    show toss toss03 with dissolve
    skye "with anal, the important thing is to control the shaft..."
    skye "from tight squeezing...."
    show toss toss02
    with dissolve
    skye "to... ah... ah... hold..."
    skye "...ohh...hold...on..."
    skye "oh, shit..."
    skye "okay... right... ah... from tight squeezing..."
    skye "to...to deep penetration..."
    show toss toss01 with dissolve
    skye "ngh...."
    skye "......"
    skye "{size=+10}fuck!" with vshake
    show ctc
    pause
    hide ctc
    skye "fucking spirit biscuit tits!"
    suki "are... you okay?"
    skye "no!"
    skye "i'm fucking {i}amazing{/i}."
    skye "let's go."
    show toss toss100
    show ctc
    pause
    hide ctc
    skye "yes, yes, yes...."
    skye "oh spirits, it's been too long..."
    skye "okay, you... ah..."
    skye "...you want him to relax... ah... while you do the... mh... work."
    skye "and in the process, you're able to... ahh... fuck..."
    skye "make sure he gets... hngh... the maximum pleasure from you."
    skye "remember, the goal is to..."
    show toss toss101
    skye "make. him. cum!"
    show ctc
    pause
    hide ctc
    skye "long, deep strokes."
    skye "you want him all the way inside...."
    skye "so he can... fuck... ah..."
    skye "empty his hot seed as far into you as it can go."
    skye "umph..."
    skye "fuck... yes... don't... stop..."
    show ctc
    pause
    hide ctc
    skye "I'm gonna... i'm gonna fuckin..."
    skye "fuckin...."
    show toss toss01 with vshake
    skye "{size=+6}aaahhh!!"
    with vshake
    skye "fuuuuck...."
    show ctc
    pause
    hide ctc
    show toss toss01
    show toss_dickup
    with dissolve
    skye "i can't believe... never cum from... anal..."
    skye "shit..."
    suki "you... can orgasm from anal penetration?"
    skye "...shit..."
    ty "that looked like fun!"
    skye "uungh..."
    y "Okay, girls, I hope you've been paying attention."
    y "Line up."
    ty "Aren't you going to cum in her ass?"
    y "maybe... but first, lie down on your back."

    scene black

    show expression "bk3/skye/sex/brothel_skyeroom1.jpg"
    show toss_tylee_flat:
        alpha 1.0 xanchor 0.5 yanchor 0 xpos 500
    show toss_skye_flat:
        alpha 1.0 xanchor 0.5 yanchor 0 xpos 500
    show toss_suki_flat:
        alpha 1.0 xanchor 0.5 yanchor 0 xpos 500
    with Dissolve(1.5)

    y "okay, girls."
    y "time for that test."
    y "so, who will get the pleasure of a good dicking first?"
    y "I have about three loads in me."
    suki "I... think i'm ready."
    ty "i'm ready, too!"

    while skyetysuki_assfuck_triggers[6] < 3:

        menu:
            "End this (with cum)":

                y "Huddle closer, girls."
                hide toss
                $ skyetysuki_assfuck_triggers[7] = 'none'
                show toss_tylee_flat:
                    alpha 1.0
                    linear 1.0 xpos 650
                show toss_skye_flat:
                    alpha 1.0 xpos 500
                show toss_suki_flat:
                    alpha 1.0
                    linear 1.0 xpos 350

                if skyetysuki_assfuck_triggers[6] == 0:
                    y "I have about three loads left in me!"
                elif skyetysuki_assfuck_triggers[6] == 1:
                    y "I have about two loads left in me."
                elif skyetysuki_assfuck_triggers[6] == 2:
                    y "Sorry, I only have enough for just one girl right now."


                while skyetysuki_assfuck_triggers[6] < 3:

                    menu:
                        "cum on Tylee":
                            y "fuck!"
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/skye/sex/nflat_tylee_facecumon.png":
                                xpos 150


                            $ skyetysuki_assfuck_triggers[6] += 1
                            $ renpy.pause(1.0)
                            show ctc
                            pause
                            hide ctc
                        "cum on Skye":

                            y "take this, whore!"
                            play sound "audio/splurt3.ogg"
                            show expression "bk3/skye/sex/nflat_skye_facecumon.png"

                            $ skyetysuki_assfuck_triggers[6] += 1
                            $ renpy.pause(1.0)
                            show ctc
                            pause
                            hide ctc
                        "cum on Suki":

                            y "bitch!"
                            play sound "audio/splurt1.ogg"
                            show expression "bk3/skye/sex/nflat_suki_facecumon.png":
                                xpos -150

                            $ skyetysuki_assfuck_triggers[6] += 1
                            $ renpy.pause(1.0)
                            show ctc
                            pause
                            hide ctc
                        "cum on feet":

                            y "take this, you useless, beautiful sluts!"
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/skye/sex/spermfeet_skyetyleesuki.png"

                            $ skyetysuki_assfuck_triggers[6] += 1
                            $ renpy.pause(1.0)
                            show ctc
                            pause
                            hide ctc

                $ skyetysuki_assfuck_triggers[6] = 8
            "Assfuck Tylee":


                $ skyetysuki_assfuck_triggers[7] = 'tylee'

                show toss_dick:
                    xpos 180 ypos 500

                show toss_tylee_flat:
                    alpha 0.0
                show toss_skye_flat:
                    alpha 1.0
                    linear 1.0 xpos 560
                show toss_suki_flat:
                    alpha 1.0
                    linear 1.0 xpos 530

                hide toss
                show toss toss50
                with Dissolve(1.5)

                $ skyetysuki_assfuck_triggers[4] = False
                $ skyetysuki_assfuck_triggers[5] = False
                $ renpy.pause(1.0)
                show toss toss51 with Dissolve(1.5)

                ty "Oooh! this is so exciting!"
                ty "But... ca-can you go slow at first?"
                y "Of course!"
                y "Aren't you my lonely little pussycat? who needs some tender anal attention?"
                ty "Meow!"
                ty "heehee!"
                hide toss_dick
                show toss_tyleeanal
                show expression "bk3/skye/sex/3tylee_face_lewd.png" with Dissolve(1.5)

                ty "Ah! {size=+5}AH!{/size} {size=+10}AHHH!"
                show ctc
                pause
                hide ctc
                hide toss_tyleeanal
                show toss toss51a
                show expression "bk3/skye/sex/3tylee_face_surprise.png"
                show toss_toss51b:
                    ypos 0
                    linear 0.3 ypos 0
                    linear 0.2 ypos -15
                    linear 0.3 ypos -15
                    linear 0.6 ypos 0
                    repeat
                show expression "bk3/skye/sex/nbod_tylee_feetup.png":
                    xpos 0 ypos -5
                    linear 0.4 ypos 0
                    linear 1.0 ypos -5
                    repeat

                y "Hnnnng..."
                y "your ass feels great, Ty Lee!"
                ty "Yes!"
                ty "Fill up my butt!!"
                ty "my stupid little butt!"
                show ctc
                pause
                hide ctc
                hide toss_toss51b
                hide expression "bk3/skye/sex/nbod_tylee_feetup.png"
                show toss toss51

                show expression "bk3/skye/sex/analtylee_4.png":
                    xpos 184 ypos 432

                y "HHNNNg!! SPLURRRT!!"
                play sound "audio/splurt2.ogg"
                hide expression "bk3/skye/sex/3tylee_face_surprise.png"
                hide expression "bk3/skye/sex/analtylee_4.png"
                show toss_dick:
                    xpos 180 ypos 590
                $ skyetysuki_assfuck_triggers[0] = True
                $ skyetysuki_assfuck_triggers[3] = True
                with flash
                show ctc
                pause
                hide ctc

                y "Your ass might take the prize, Ty Lee."
                ty "I feel creamy!"
                hide expression "bk3/skye/sex/3tylee_face_lewd.png" with Dissolve(1.5)
                $ skyetysuki_assfuck_triggers[6] += 1
                ty "but why did you say \"splurt\"?"
                y "....it was an \"in the moment\" kind of thing."
                y "it's normal."
                y "you're the one that's weird."
                y "....."
                y "shut up."
            "Assfuck Skye":


                $ skyetysuki_assfuck_triggers[7] = 'skye'

                y "Ready that ass of yours, skye!"
                show toss_dick:
                    xpos 465 ypos 480

                show toss_tylee_flat:
                    alpha 1.0
                    linear 1.0 xpos 470
                show toss_skye_flat:
                    alpha 0.0
                show toss_suki_flat:
                    alpha 1.0
                    linear 1.0 xpos 530

                hide toss
                show toss toss53
                with Dissolve(1.5)

                $ skyetysuki_assfuck_triggers[3] = False
                $ skyetysuki_assfuck_triggers[5] = False

                $ renpy.pause(0.4)
                show toss toss54 with Dissolve(1.5)

                skye "I knew you couldn't stay away from my ass for long."
                y "you know it, bitch!"
                y "it brought us all together, after all."

                hide toss_dick
                show toss toss54a
                show toss_toss54a:
                show expression "bk3/skye/sex/3skye_face_lewd.png"
                y "daaamn..."
                skye "You like this?"
                skye "You like sticking your dick in my little whore ass?"
                show ctc
                pause
                hide ctc
                y "ba da ba ba baaaaa!"
                skye "what?"
                y "{size=+10}I'm loving it!"
                skye "FFFuuuuuckk...yeah! soo goood!"

                show toss_toss54a:
                    ypos 0
                    linear 0.3 ypos 0
                    linear 0.2 ypos -20
                    linear 1.0 ypos -20
                    linear 0.9 ypos 0
                    repeat
                $ renpy.pause()


                y "I'm going to fill you up with my baby juice, Skye!"
                skye "Do it!!"
                skye "give me your cock juice, baby!"
                skye "right in my pay-by-the hour whore ass!"

                hide toss_toss54a
                show toss toss54
                show expression "bk3/skye/sex/analskye_4.png":
                    xpos 473 ypos 427

                y "hngh!"
                play sound "audio/splurt3.ogg"

                hide expression "bk3/skye/sex/analskye_4.png"
                $ skyetysuki_assfuck_triggers[1] = True
                $ skyetysuki_assfuck_triggers[4] = True
                show toss_dick:
                    xpos 458 ypos 580

                with flash
                show ctc
                pause
                hide ctc
                y "Your ass is pretty fucking great, Skye."
                skye "Well, I am the professional here."

                hide expression "bk3/skye/sex/3skye_face_lewd.png" with Dissolve(1.5)
                $ skyetysuki_assfuck_triggers[6] += 1
            "Assfuck Suki":



                $ skyetysuki_assfuck_triggers[7] = 'suki'

                y "Up for a bit of anal fun, Suki?"

                menu:
                    "Make her think you're a stranger":
                        $ skyetysuki_assfuck_triggers[8]='request_on'
                        "You lean in close and whisper in Suki's ear..."
                        y "[trigger]."
                        "she freezes, hypnotized."
                        y "Okay Suki, I want to do some sexplay."
                        y "Until I cum, you'll think of me as a stranger..."
                        y "...and are forced to service me."
                        suki "i understand."
                        y "[trigger]."
                        "suki blinks, leaving the hypnotic trance."
                    "Fuck her as yourself":
                        $ skyetysuki_assfuck_triggers[8]='request_off'

                show toss_dick:
                    xpos 755 ypos 520

                show toss_tylee_flat:
                    alpha 1.0
                    linear 1.0 xpos 470
                show toss_skye_flat:
                    alpha 1.0
                    linear 1.0 xpos 430
                show toss_suki_flat:
                    alpha 0.0

                hide toss
                show toss toss57
                with Dissolve(1.5)

                $ skyetysuki_assfuck_triggers[3] = False
                $ skyetysuki_assfuck_triggers[4] = False
                $ renpy.pause(0.4)
                show toss toss58 with Dissolve(1.5)
                show toss_3suki_blink

                if skyetysuki_assfuck_triggers[8] == 'request_off':
                    y "You want this ramming rod up your ass, Suki?"
                    suki "Yes! Scrape my insides clean with your fat cock!"
                    y "Your ass is starving for my cock, isn't it Suki?"
                    suki "It is! I want to feel you deep inside me!"
                else:
                    y "Look at you, you filthy whore."
                    y "Spreading your legs for anyone who has enough coin."
                    show expression "bk3/skye/sex/3suki_face_angry.png" behind toss_3suki_blink
                    suki "I have my reasons!"
                    y "Yeah, but who cares?"
                    y "At the end of the day you're just a cumbucket, selling your ass."
                    y "So shut up and take it in your ass like a good slut."

                hide toss_dick
                show toss_sukianal

                if skyetysuki_assfuck_triggers[8] == 'request_off':
                    show expression "bk3/skye/sex/3suki_face_lewd.png" behind toss_3suki_blink with Dissolve(1.5)
                    suki "Hnng, nice and slow... please... just at first..."
                    show ctc
                    pause
                    hide ctc
                    y "look at you, showing your bare ass... lying next to other girls doing the same..."
                    suki "All for... ahh... you to enjoy."
                    y "Does that excite you Suki? It sure as hell excites me."
                    suki "so... filthy... yes..."
                    y "Do you like this? Do you like me pumping your ass?"
                    suki "I do!"
                    suki "shut up and fuck it!"
                    suki "fuck my ass you stupid bitch!"
                    y "(....rude, but whatever.)"
                else:
                    y "Putting it up your ass is all a whore like you deserves."
                    show ctc
                    pause
                    hide ctc
                    suki "You can't talk to me like that!!!"
                    y "I already paid for you, bitch!"
                    y "SO I can call you whatever the fuck I want, while going in and out of your ass."
                    suki "st...stop..."
                    y "Does your daddy know you're doing this? Huh?"
                    y "is he proud of his little prostitute?"
                    show expression "bk3/skye/sex/3suki_face_blink.png":
                        xpos 744 ypos 0
                suki "Ah! {size=+5}AH!{/size} {size=+10}AHHH!"

                hide toss_sukianal
                show toss toss58a
                show toss_toss58b:
                    ypos 0
                    linear 0.3 ypos 0
                    linear 0.2 ypos -20
                    linear 0.3 ypos -20
                    linear 0.6 ypos 0
                    repeat
                show expression "bk3/skye/sex/nbod_suki_feetup.png":
                    xpos 554 ypos -10
                    linear 0.4 ypos 0
                    linear 1.0 ypos -10
                    repeat

                show ctc
                pause
                hide ctc

                ty "Oh, wow... he's really ramming it home, Suki!"
                suki "I... unf!... I... unf!... Noticed that already!"
                y "I'm going to fill you up with my baby juice!"
                if skyetysuki_assfuck_triggers[8] == 'request_off':
                    suki "nut in my fat fucking ass, master!!"
                else:
                    suki "nut in my fat fucking ass!!"

                hide toss_toss58b
                hide expression "bk3/skye/sex/nbod_suki_feetup.png"
                show toss toss58
                show expression "bk3/skye/sex/analsuki_4.png":
                    xpos 755 ypos 432

                y "HHNNNg!!"
                play sound "audio/splurt2.ogg"
                suki "AAAAah!"
                suki "too much!! i'm... ahhhh..."
                play sound "audio/splurt2.ogg"
                suki "st... stop... too much..."
                suki "s-so... full... ahhh.... ah..."

                hide expression "bk3/skye/sex/analsuki_4.png"

                $ skyetysuki_assfuck_triggers[2] = True
                $ skyetysuki_assfuck_triggers[5] = True
                show toss_dick:
                    xpos 775 ypos 590
                with flash
                show ctc
                pause
                hide ctc
                y "Ah, look it's dripping out."
                suki "There's... so much of it..."

                if skyetysuki_assfuck_triggers[8]=='request_off':
                    hide expression "bk3/skye/sex/3suki_face_lewd.png" with Dissolve(1.5)
                else:
                    hide expression "bk3/skye/sex/3suki_face_angry.png"
                    hide expression "bk3/skye/sex/3suki_face_blink.png"
                    with Dissolve(1.5)

                $ skyetysuki_assfuck_triggers[8]='request_off'
                hide toss_3suki_blink
                $ skyetysuki_assfuck_triggers[6] += 1

        hide toss_dick
        $ renpy.pause()



    if skyetysuki_assfuck_triggers[6] == 3:
        $ skyetysuki_assfuck_triggers[3] =  True
        $ skyetysuki_assfuck_triggers[4] =  True
        $ skyetysuki_assfuck_triggers[5] =  True

        y "I came three times already, time for me to get some rest."
        y "But first...."
        y "Okay girls, show me my handywork."

        hide toss_tylee_flat
        hide toss_skye_flat
        hide toss_suki_flat

        show toss toss60 with Dissolve(1.5)
        show ctc
        pause
        hide ctc
        y "It's a goddamn work of art, I'm telling ya."
    elif skyetysuki_assfuck_triggers[6] == 8:
        y "Oh man, that really drained me, but seeing you covered in my spunk makes it all worth it."
    else:
        y "It has been lovely ladies, but all good things come to an end."

    $ skyetysuki_assfuck_triggers[0] = False
    $ skyetysuki_assfuck_triggers[1] = False
    $ skyetysuki_assfuck_triggers[2] = False
    $ skyetysuki_assfuck_triggers[3] = False
    $ skyetysuki_assfuck_triggers[4] = False
    $ skyetysuki_assfuck_triggers[5] = False
    $ skyetysuki_assfuck_triggers[6] = 0
    $ skyetysuki_assfuck_triggers[7] = 'none'
    scene black with dissolve
    "you head home and pass out."
    jump bk3_next

label toph_rockbound:
    $ tots_head = "angry"
    show expression "bk3/toph/rockbound/bg_training_0.jpg"

    show expression "bk3/toph/rockbound/body_0.png" with hpunch
    t "Ah shit! You just got lucky!"
    play sound "audio/earthquake.mp3"
    show expression "bk3/toph/rockbound/rocksbody_0.png":
        alpha 0
        linear 2.0 alpha 1
    "you lock her in place with rocks around her wrists and ankles."
    y "You mean I won."
    with vshake
    "though exhausted, toph struggles for a few seconds, before pausing to glare at you."
    t "no, I mean you got lucky!"
    t "I guess I have nothing to teach you anymore... but..."
    t "You don't really think these rocks can hold me down, do you?"
    y "well... if I weren't around to counter your earthbending..."
    y "...i'm sure these would be less than nothing."
    y "But I {i}am{/i} here."
    y "so, come on. try to get out."
    show expression "bk3/toph/rockbound/body_0.png" with hpunch
    t "Hnnnnng!!"
    show expression "bk3/toph/rockbound/body_0.png" with hpunch
    t "Raaaaah!!"
    t "urh... okay..."
    t "as long as your concentration doesn't waver... you've got me pinned down."
    t "Now what?"
    y "i'd say... winner gets to make the loser do whatever he wants."
    t "It doesn't take much imagination to figure out what you want."
    y "yeah. you're gonna suck my cock."
    t "big surprise."
    y "hey, i'm not shallow!"
    t "sure....."
    hide expression "bk3/toph/rockbound/body_0.png"
    hide expression "bk3/toph/rockbound/rocksbody_0.png"


    show expression "bk3/toph/rockbound/body_1.png"
    show expression "bk3/toph/rockbound/clothes_halfopen.png"
    show expression "bk3/toph/rockbound/clothes_open.png":
        alpha 0.0
    show expression "bk3/toph/rockbound/marker.png":
        alpha 0.0
    show tots tots00


    with Dissolve(1.5)
    t "Come on, whip it out already."
    y "you're awfully eager."
    show tots tots01 with dissolve
    y "here you go!"
    t "........"
    show tots tots100
    t "*sllluurp* *gulp* *slurp*"

    show ctc
    pause
    hide ctc
    y "I was actually going to ask you to lick my nutsack..."
    y "...but this is also okay I guess."
    t "hngh... *slurp...*"
    y "NNng, did you pick up a new technique..."
    y "this feels even better than your earlier blowjobs."
    y "Maybe I should piss you off more right before getting a blowjob."
    $ tots_head = "none"
    "Toph is visibly calming down as she gulps down your dick in short bursts."
    y "Wow, my dick is like a pacifier."
    show ctc
    pause
    hide ctc

    y "That's really great, but hold on for a minute."
    y "Toph... I said hold on."
    y "Toph... you're blind not deaf. are you?"
    y "...Oh, for fucks sake."


    show tots tots00 with Dissolve(1.5)
    $ tots_head = 'angry'
    "With considerable effort you manage to pull your dick out of Toph's mouth."
    t "Damn it twinkletoes!"
    t "I wasn't finished yet."
    t "Can't you let me suck your cock in peace?"
    y "Wasn't this supposed to be MY reward for winning?"
    y "Ah forget it. I have an important question to ask you..."
    t "What?"
    y "Toph... will you be my..."
    $ tots_head = 'none'
    y "Will you be my willing cockslut for the rest of your life?"
    y "Will you take my throbbing dick up your tiny ass, pussy, mouth or whatever other place my imagination can come up with and fill it up with my cum?"
    y "Will you lick my seed off of other girls' butts just because it makes me extra hard to watch that?"
    t "Haven't we been doing all of that already?"
    t "Well.. not that last thing, but I guess I should return the favor to Katara eventually......"
    y "I just wanted to make it official."
    t "You can be so weird sometimes twinkletoes, but fine. I'll be your cumslut. Happy now?"
    t "Anything else before I get back to sucking?"
    menu:
        "open up her clothes some more":
            y "Yeah, I want to see more of your delicious body while you suck me dry."
            hide expression "bk3/toph/rockbound/clothes_halfopen.png"
            show expression "bk3/toph/rockbound/clothes_open.png":
                alpha 1.0
            $ renpy.pause()
        "write on her body":
            y "I'm gonna write some stuff on your body first."
            hide expression "bk3/toph/rockbound/clothes_halfopen.png"
            show expression "bk3/toph/rockbound/clothes_open.png":
                alpha 1.0
            show expression "bk3/toph/rockbound/marker.png":
                alpha 1.0
            t "What did you write?"
            y "The kind of thing you'd expect me to write."
            y "But if you really want to know... ask Katara to read it for you later."
            y "Enough playing, back to cocksucking!"
            $ renpy.pause()
        "suck my balls":
            y "Yeah, suck on my balls first."
            y "I haven't done it before so I'm curious how it feels."
            "You drop your sack in Toph's mouth and she starts to gently massage your testicles."
            show tots_sacksuck:
                ypos -10
            $ renpy.pause()
            y "You ready for more cock and to finish the job?"
            hide tots_sacksuck
            show tots tots01
            t "Yes!"
        "Nah, I'm good.":


            pass



    $ tots_head = "blink"
    show tots tots100
    y "Wow."
    y "you weren't kidding about being ready..."
    y "oh, fuck!"
    y "I'm so close..."
    y "i want you to feel my sperm swimming in your eyes."
    y "I'm about to cum! Open your eyes!"
    show tots tots15 with Dissolve(1.5)
    $ tots_head = 'none'
    y "eyes are the windows to the soul, toph..."
    y "and your sould is about to be permanently stained with semen."
    t "you.... really want to-"
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/rockbound/solodick.png":
        xpos -40

    show expression "bk3/toph/rockbound/spermshot.png"
    $ renpy.pause(0.3)
    hide expression "bk3/toph/rockbound/spermshot.png"
    show expression "bk3/toph/rockbound/spermshot_eyeleft.png"
    t "ahh!"
    t "my eye!"
    y "fuck you!"
    show expression "bk3/toph/rockbound/solodick.png":
        xpos 30
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/rockbound/spermshot.png":
        xpos 80
    $ renpy.pause(0.3)
    hide expression "bk3/toph/rockbound/spermshot.png"
    show expression "bk3/toph/rockbound/spermshot_eyeright.png"
    t "hngh!! oww!"
    y "that's right, blink..."
    y "keep it all in your fucking skull!"
    t "it... it burns..."
    show ctc
    pause
    hide ctc
    hide expression "bk3/toph/rockbound/solodick.png" with dissolve
    y "don't forget i own you, slut."
    t "i... i won't... ow..."
    ya "say it!"
    t "you... you own me..."

    show ctc
    pause
    hide ctc
    show tots tots00
    show expression "bk3/toph/rockbound/spermhead.png"
    with dissolve
    y "that's right, whore."
    y "now thank me."
    t "thank... sniff... oww.. thank you..."
    y "who is the better earthbender?"
    t "...you are..."
    menu:
        "aang":
            $ bk3name = "aang"
        "daddy":

            $ bk3name = "daddy"
        "master":

            $ bk3name = "master"
        "lord":

            $ bk3name = "lord"
        "beast":

            $ bk3name = "beast"

    y "\"[bk3name]\"."
    t "....you're the best earthbender...."
    t "....[bk3name]."
    y "ahh..."
    y "Man, I'm going to miss our earthbending training sessions."
    t "......."
    y "maybe i'll come back for another."
    t "............."
    t "p-please do..."
    t "oww...."
    show ctc
    pause
    hide ctc
    scene black with Dissolve(1)
    "you head home and fall promptly asleep."
    jump bk3_next


label toph_rockbound2:
    $ tots_head = "angry"
    show expression "bk3/toph/rockbound/bg_training_0.jpg"
    "After an intense but short fight you force Toph backwards and make her fall, immediately locking her down with rocks around her wrists and ankles."
    show expression "bk3/toph/rockbound/body_0.png" with hpunch
    t "Ah shit! You just got lucky!"
    play sound "audio/earthquake.mp3"
    show expression "bk3/toph/rockbound/rocksbody_0.png":
        alpha 0
        linear 2.0 alpha 1
    "you lock her in place with rocks around her wrists and ankles."
    y "You mean I won."
    with vshake
    "though exhausted, toph struggles for a few seconds, before pausing to glare at you."
    t "no, I mean you got lucky!"
    show expression "bk3/toph/rockbound/body_0.png" with hpunch
    t "Hnnnnng!!"
    show expression "bk3/toph/rockbound/body_0.png" with hpunch
    t "Raaaaah!!"
    t "urh... okay..."
    t "as long as your concentration doesn't waver... you've got me pinned down."
    t "Now what?"
    y "i'd say... winner gets to make the loser do whatever he wants."
    t "It doesn't take much imagination to figure out what you want."
    y "yeah. you're gonna suck my cock."
    t "big surprise."
    hide expression "bk3/toph/rockbound/body_0.png"
    hide expression "bk3/toph/rockbound/rocksbody_0.png"


    show expression "bk3/toph/rockbound/body_1.png"
    show expression "bk3/toph/rockbound/clothes_halfopen.png"
    show expression "bk3/toph/rockbound/clothes_open.png":
        alpha 0.0
    show expression "bk3/toph/rockbound/marker.png":
        alpha 0.0
    show tots tots00


    with Dissolve(1.5)
    t "Come on, whip it out already."
    y "you're awfully eager."
    show tots tots01 with dissolve
    y "here you go!"
    t "........"
    show tots tots100
    t "*sllluurp* *gulp* *slurp*"

    show ctc
    pause
    hide ctc
    y "I was actually going to ask you to lick my nutsack..."
    y "...but this ain't bad."
    t "hngh... *slurp...*"
    y "NNng, did you pick up a new technique..."
    y "this feels even better than your earlier blowjobs."
    y "Maybe I should piss you off more right before getting a blowjob."
    $ tots_head = "none"
    "Toph is visibly calming down as she gulps down your dick in short bursts."
    y "Wow, my dick is like a pacifier."
    show ctc
    pause
    hide ctc

    y "That's really great, but hold on for a minute."
    y "Toph... I said hold on."

    show tots tots00 with Dissolve(1.5)
    $ tots_head = 'angry'
    "With considerable effort you manage to pull your dick out of Toph's mouth."
    t "Damn it [bk3name]!"
    t "I wasn't finished yet."
    t "Can't you let me suck your cock in peace?"
    y "beg."
    $ tots_head = 'none'
    t "please. please [bk3name]."
    t "please let me suck your thick, tasty cock."
    y "well... i suppose that's acceptible."
    t "Anything else before I get back to sucking?"
    menu:
        "open up her clothes some more":
            "Yeah, I want to see more of your delicious body while you suck me dry."
            hide expression "bk3/toph/rockbound/clothes_halfopen.png"
            show expression "bk3/toph/rockbound/clothes_open.png":
                alpha 1.0
            $ renpy.pause()
        "write on her body":
            "I'm gonna write some stuff on your body first."
            hide expression "bk3/toph/rockbound/clothes_halfopen.png"
            show expression "bk3/toph/rockbound/clothes_open.png":
                alpha 1.0
            show expression "bk3/toph/rockbound/marker.png":
                alpha 1.0
            t "What did you write?"
            y "The kind of thing you'd expect me to write."
            y "But if you really want to know... ask Katara to read it for you later."
            y "Enough playing, back to cocksucking!"
            $ renpy.pause()
        "suck my balls":
            y "Yeah, suck on my balls first."
            y "I haven't done it before so I'm curious how it feels."
            "You drop your sack in Toph's mouth and she starts to gently massage your testicles."
            show tots_sacksuck:
                ypos -10
            $ renpy.pause()
            y "You ready for more cock and to finish the job?"
            hide tots_sacksuck
            show tots tots01
            t "Yes!"
        "Nah, I'm good.":


            pass



    $ tots_head = "blink"
    show tots tots100
    y "Wow."
    y "you weren't kidding about being ready..."
    y "oh, fuck!"
    y "I'm so close..."
    y "i want you to feel my sperm swimming in your eyes."
    y "I'm about to cum! Open your eyes!"
    show tots tots15 with Dissolve(1.5)
    $ tots_head = 'none'
    y "eyes are the windows to the soul, toph..."
    y "and your sould is about to be permanently stained with semen."
    t "you.... really want to-"
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/rockbound/solodick.png":
        xpos -40

    show expression "bk3/toph/rockbound/spermshot.png"
    $ renpy.pause(0.3)
    hide expression "bk3/toph/rockbound/spermshot.png"
    show expression "bk3/toph/rockbound/spermshot_eyeleft.png"
    t "ahh!"
    t "my eye!"
    y "fuck you!"
    show expression "bk3/toph/rockbound/solodick.png":
        xpos 30
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/rockbound/spermshot.png":
        xpos 80
    $ renpy.pause(0.3)
    hide expression "bk3/toph/rockbound/spermshot.png"
    show expression "bk3/toph/rockbound/spermshot_eyeright.png"
    t "hngh!! oww!"
    y "that's right, blink..."
    y "keep it all in your fucking skull!"
    t "it... it burns..."
    show ctc
    pause
    hide ctc
    hide expression "bk3/toph/rockbound/solodick.png" with dissolve
    y "don't forget i own you, slut."
    t "i... i won't... ow..."
    ya "say it!"
    t "you... you own me..."

    show ctc
    pause
    hide ctc
    show tots tots00
    show expression "bk3/toph/rockbound/spermhead.png"
    with dissolve
    y "that's right, whore."
    y "now thank me."
    t "thank... sniff... oww.. thank you..."
    y "who is the better earthbender?"
    t "...you are..."
    t "\"[bk3name]\"."
    t "you're the best earthbender."
    y "ahh..."
    y "Man, I'm going to miss our earthbending training sessions."
    t "......."
    y "maybe i'll come back for another."
    t "............."
    t "p-please do..."
    t "oww...."
    show ctc
    pause
    hide ctc

    scene black with Dissolve(1)
    "you head home and fall promptly asleep."
    jump bk3_next

label bk3_katara_handjob:
    scene white

    show expression "bk3/katara/handjob/hospital_tilted.jpg"
    $ tokh_face = 'none'

    show tokh tokh01
    show tokh_head_1:
        xpos 550 ypos 25
    k3 "okay, i'm ready."
    k3 "I want to talk about something important."
    y "is that... really how you dress when you want to talk about something important?"
    k3 "I'm combining important and fun!"
    k3 "besides, I deserve a bit of alone time with you, don't you think?"
    k3 "I helped out a lot with getting Toph to... cooperate."
    k3 "So now I want you to myself without any spectators."
    y "Yeah... about Toph and you..."
    k3 "Do you like my tits the way they are or should I change them?"
    menu:
        "small":
            $ tokh_titsize = 'small'
        "medium":
            $ tokh_titsize = 'medium'
        "big":
            $ tokh_titsize = 'big'

    show tokh tokh02
    $ tokh_face = 'eyesoncock'
    k3 "Hmmmmm... I'll give you a handjob while we talk."
    $ tokh_face = 'none'


    show tokh tokh04
    y "are you trying to change the subject?"
    k3 "no."
    show tokh tokh100
    k3 "how does your penis feel?"
    show ctc
    pause
    hide ctc
    y "hngk."
    k3 "*sigh...*"
    k3 "I don't think I'll ever tire of your dick."
    y "okay, What's going on? for real?"
    y "You've been helping me in... let's say... unexpected ways."

    y "And it seems like you know more than I do about what's going on."
    $ tokh_face = 'worried'
    k3 "I know this is all very confusing, but you told me to keep it on a need to know basis."
    y "What? I didn't tell you any... Wait a minute."
    y "I... I didn't make hissing sounds did I?"
    y "or seem like i lost my memory?"
    k3 "No, no. You were acting perfectly normal."
    y "Okay, so I think it's safe to say I wasn't being bodysnatched at the time..."
    y "...and I know for a fact that that shit can happen..."
    y "so, when and what did I tell you?"
    k3 "When you left my village and I was waving goodbye...."
    y "yeah?"
    k3 "You promised me you'd come back...."
    k3 "....and you kept your promise."
    y "i did?"
    k3 "yes."
    k3 "You visited me again before we ever set foot in BasingSe."
    k3 "You told me everything I needed to know."
    k3 "You also said I can't tell you any more than i already have."
    y "Why?!"
    k3 "Here let me go faster."
    $ tokh_face = 'none'


    hide tokh_head_1

    show tokh_head_2:
        xpos 550 ypos 25
        linear 0.7 ypos 35
        linear 0.7 ypos 25
        repeat
    show tokh tokh101
    $ tokh_face = 'eyesoncock'
    y "Hnnnngg.. must.... concentrate... on question..."
    y "but... handjob... so goood..."
    k3 "please, trust me. like I trust you."
    k3 "Telling you more is dangerous. "
    k3 "Don't worry, you'll know when the time is right."
    $ tokh_face = 'lewd'
    k3 "Are you almost ready to cum?"
    y "Getting very close now!"
    y "I'm going to whitewash you like no one ever was!"
    show tokh tokh06 with Dissolve(1.5)
    hide tokh_head_2
    show tokh_head_1:
        xpos 550 ypos 25
    k3 "...that sounds great, but I'd like you to do something else this time."
    y "like what?"


    hide tokh_head_1
    show tokh tokh10
    with Dissolve(1.5)
    y "Aaaaw..."
    y "I was almost about to erupt all over your pretty face."
    k3 "I want you to cum in my panties this time."
    y "That's new. Any particular reason?"
    k3 "The schoolteacher you banged in water tribe village was bragging about how she was teaching her class with cum filled panties."
    k3 "I really can't stand the thought of her doing kinky stuff with your semen that I haven't done yet."
    y "But where are you going to find a class to teach?"
    k3 "Just walking around with your cum in my panties will be good enough for me."

    show tokh tokh11
    k3 "Please fill it up!"
    y "That reminds me of those letters I got in the village, asking for my semen!"
    y "Felt like I was selling hard drugs the way those girls reacted to it..."

    show tokh tokh12
    y "Okay! here I go!"
    play sound "audio/splurt2.ogg"
    show expression "bk3/katara/handjob/sperm1.png"
    k3 "what a good boy!"
    y "hng!"
    play sound "audio/splurt3.ogg"
    show expression "bk3/katara/handjob/sperm2.png"
    k3 "Oh yeah. Just like that."

    hide expression "bk3/katara/handjob/sperm1.png"
    hide expression "bk3/katara/handjob/sperm2.png"
    show tokh tokh10
    show expression "bk3/katara/handjob/spermdrip.png"
    with Dissolve(1.5)
    k3 "mmmm... good..."
    k3 "nice and warm and sticky."
    k3 "it's like a packed lunch!"
    k3 "Maybe I'll drop by Toph and let her lick me clean after walking around like this for an hour or so."
    y "Were you always this kinky?"
    k3 "Well, there was a time I didn't know you yet..."
    k3 "see you around!"
    scene black with dissolve
    "you head home and fall asleep."
    $ bk3_handjob = 1
    jump bk3_next

label rescue_toph_tunnels:
    "you follow the tracks to lake laogai..."
    show expression "ebackgrounds/lake_laogai_4.jpg" with Dissolve(1)
    y "the tracks go down the tunnels."
    y "i wonder how they managed that?"
    y "must have earthbenders helping them."
    y "...."
    y "here i come, toph."
    scene black with dissolve
    jump maze_update_two

label nagas_battle:
    y "let's do it."
    y "but... why now?"
    cn "{i}weak..."
    cn "{i}too weak to ssstay much longer..."
    cn "{i}your hallucinationsss fight me..."
    cn "{i}not ssstrong enough..."
    cn "{i}mussst defeat the dreamssstealer sssoon, or i will not win..."
    y "i'm fuzzy on the details of this \"merging\" situation."
    y "what will happen to you?"
    y "and what will happen to my mind?"
    cn "{i}i will be ssstrong enough to put up barriersss in your mind..."
    y "and i can trust you on that?"
    cn "{i}hissss..."
    cn "{i}yesss... i have been nothing but honessst with you..."
    cn "{i}i am from the dreamssstealer... but i am not the dreamssstealer..."
    cn "{i}i wasss born here... in your mind..."
    y "right, right, you've said that before."
    y "tell me about this merge you want to do."
    cn "{i}i.... am not clear...."
    y "wait, what? tell me you're joking."
    cn "{i}i do not know what will happen..."
    y "i don't like this plan."
    cn "{i}i have called her."
    y "you {i}what{/i}!?"
    y "i didn't give you permission for that!"
    cn "{i}here ssshe comesss..."
    cn "{i}ssstay ssstrong...."
    y "i don't like th-"
    play sound "audio/hiss.wav"
    show flyby at right
    with moveinright
    hide flyby with moveoutleft
    with sshake
    $ renpy.pause(1.0, hard=True)
    play sound "audio/hiss.wav"
    ds "*hss!*"
    ds "i have come, avatar!"
    with sshake
    ds "foolissh child!"
    ds "thosse eyess were curssed..."
    ds "and i have let me into your mind!"
    with sshake
    play sound "audio/hiss.wav"
    show flyby2 at left
    with moveinleft
    hide flyby2 with moveoutright
    $ renpy.pause(1.0, hard=True)
    ds "goodbye, little one... your work is finisshed..."
    cn "{i}no."
    ds "thiss is the en- what?"
    cn "{i}thisss isss my mind!"
    y "um... pretty sure it's mine-"
    with sshake
    ds "you sstay out of thiss!"
    ds "i am naga, the dreamsstealer!"
    ds "powerful and older than the ssky!"
    ds "you cannot sstop me, you imitation!"
    play sound "audio/hiss.wav"
    show flyby at right
    with moveinright
    hide flyby with moveoutleft
    with sshake
    $ renpy.pause(1.0, hard=True)
    y "ow...."
    cn "{i}i am no imitation...."
    cn "{i}and i am ssstronger than you, here..."
    ds "we sshall ssee!"
    with sshake

    show tonc_floats:
        around (.5, .5) alignaround (.5, .5) xalign .7 yalign .5
        rotate 0
        linear 10 rotate 360
        repeat
    with flash
    y "what..."
    y "why is that happening..."
    show flyby:
        parallel:
            rotate -90
            xpos -200
        parallel:
            ypos -1000
            linear 5 ypos 920
        repeat
    with flash
    y "why is any of this happening...?"
    y "ow... my head...!!"
    y "who... are you weirdos?"
    ds "sstop! you cannot win!"
    cn "{i}thisss man is mine!"
    cn "{i}hisss mind belongsss to me!"
    ds "no! you are a cheap imitation! i am real!"
    cn "{i}i am real!!"
    with flash
    ds "noo...!!"
    cn "{i}hssss!!"
    y "my fucking head..."
    hide tonc_floats
    hide flyby
    with flash
    with flash
    with flash
    show ctc
    pause
    hide ctc
    y "......"
    y "where did they go?"
    show tonb tonb101 with Dissolve(1.5):
        parallel:
            xpos -1000
            linear 1.0 xpos 0
        parallel:
            ypos 0
            linear 1 ypos 15
            linear 1 ypos 0
            repeat

    show ctc
    pause
    hide ctc

    "{i}i am here, avatar...."
    "{i}and i am... not amusssed..."
    y "oh. that's... not good."
    "{i}but i will keep my bargain."
    y "uh, wait..."
    y "which one are you?"
    "{i}i am both."
    "{i}call me..."
    nag "{i}nagina."
    y "you want me to call you vagina?"
    nag "{i}no... nagina."
    y "fine."
    y "so what's the deal?"
    nag "{i}i will... put up barriersss... against my better judgement..."
    nag "{i}I will keep my word..."
    nag "{i}but i will take down the current barriersss before I can build permanent onesss..."
    nag "{i}this will not be pleasssant..."
    nag "{i}you may die..."
    y "wait... die!? straight up just die!?"
    nag "{i}the russsh of violent hallucinationsss may sssend you into the darknessss..."
    nag "{i}and never return."
    y "that's not good."
    nag "{i}here..."
    y "ohhhh shhiiiiiiiit-"
    with flash
    with flash
    $ double_vision_on("tonb tonb101_1")
    y "what... what... no..."
    nag "{i}ssstay! ssstay awake!"
    y "where the fuck am i?"
    y "i... can't..."
    nag "{i}no! you mussst-"
    scene black with Dissolve(1)
    $ double_vision_off()
    show ctc
    pause
    hide ctc
    "you drift...."
    "for a time."
    "the deeper darkness calls to you."
    show flicker
    $ renpy.pause(1, hard=True)
    "...you find yourself... warm."
    "and... feeling good."
    show flicker
    $ renpy.pause(1, hard=True)
    s "{i}...find...you..."
    "thought returns to you..."
    y "if this is death... it's not so bad."
    y "it's... nice."
    y "like, really nice."
    show flicker
    $ renpy.pause(1, hard=True)
    s "{i}...spirit...world...lost...souls..."
    y "i wonder how long i've been here?"
    y "and i wonder why i feel so good?"
    y "maybe a little farther down is okay..."
    show flicker
    s "{i}not... the shadows... avatar... [povname]..."
    s "{i}fight... fight... awake... come..."
    s "{i}follow... voice..."
    y "who are you?"
    show flicker
    s "{i}save... you..."
    s "{i}trust..."
    y "okay, mysterious lady."
    y "can i ask you a question?"
    show flicker
    y "who am i?"
    s "{i}oh... not... again..."
    y "what?"
    s "{i}just follow... voice... light..."
    y "am i dead?"
    show flicker
    s "{i}should... be... but... not..."
    s "{i}lasted long enough... for me to... find you..."
    y "i did?"
    y "how?"
    s "{i}friends..."
    show flicker
    s "{i}now, come..."
    y "i'm coming."
    s "{i}come..."
    y "I am, i'm coming."
    s "{i}no...."
    show flicker
    "{size=+5}{i}cum!"
    with flash
    jump tophgrouptug

label tophgrouptug:
    scene black
    $ tott_tits = 'small'
    show expression "bk3/toph/grouptug/toph_home_grouptug.jpg"
    show tott tott02
    with eye_open
    k3 "Look Toph, he has opened his eyes!"
    t "About damn time! My arm is about to fall off!"
    show ctc
    pause
    hide ctc
    suki "You should've said something. I could've taken over."
    y "Huh... whatchall doin'?"
    y "I feel woozy."
    k3 "Don't get up just yet, you lost a lot of stamina."
    k3 "Maybe you should keep going Toph, Just to be sure."
    menu:
        "Yeah keep going":
            pass
        "You can stop if you're tired Toph.":
            show tott tott01
    y "Okay so, I like what I'm seeing, but I have no memory of starting all of this."
    y "What's going on?"
    k3 "i don't really know, i just found you on the floor and brought you to toph's house."
    k3 "it looks like a spirit almost sucked you dry of your lifeforce."
    k3 "Your mind was close to ejecting from your body."
    t "And I suggested to just give you a handjob, enticing you to stay put!"
    k3 "That's right!"
    k3 "It was Toph's idea and she didn't cry at all while you were lying there on the brink of death."
    t "Yeah, I.. HEY!!"
    k3 "We've been taking turns, keeping your body warm with our bodies and giving you continuous handjobs."
    k3 "We figured your mind wouldn't leave before you got the chance to cum."
    y "Sooo... why didn't I cum?"
    k3 "My waterbending can make boobs increase and decrease in size, so keeping your sperm from escaping your balls was easy!"
    y "That's not terrifying at all..."
    y "Thanks everyone."
    y "Katara can you stop spermbending my balls now?"
    y "If I can't cum soon I'll go crazy."
    k3 "Of course!"
    y "Toph, park that pretty little tush on my cock."
    y "Handjobs are a nice warmup, but I want something better right now."
    k3 "Want me to give her bigger tits?"
    y ".......uuhh........"
    t "Katara told me all about it, [bk3name]."
    t "I really don't mind anymore."
    menu:
        "make them big!":
            $ tott_tits = 'big'
        "keep 'em au natural":
            $ tott_tits = 'small'
    t "I..."
    menu:
        "other girls stay":
            show expression "bk3/toph/grouptug/group2.png"
        "other girls leave":
            t "I'm sorry... but could you guys just step out for a moment?"
            k3 "Sure Toph! Enjoy!"
    hide tott
    $ tott_head = 'unsure'
    show tott tott05
    with Dissolve(3.0)

    t "I was really worried."
    show ctc
    pause
    hide ctc
    y "you were?"
    $ tott_head = 'angry'
    t "Of course! I've put a lot of effort in your training!"
    t "It'd be a waste of my time!"
    $ tott_head = 'smile'
    t "I'm happy you're better."
    y "Don't say it, show it."


    show tott tott100
    t "Like this?"
    show ctc
    pause
    hide ctc
    y "That's it, baby slut.... up and down."
    y "Go hard, girl!"

    show tott tott101
    $ tott_head = 'lewd'
    y "Oh yeaah, you like that, huh?"
    show ctc
    pause
    hide ctc
    y "hey.... Knock knock."
    t "W-who's... there...?"
    y "If this isn't a safe day for you..."
    y "your baby!"
    y "...'cause I'm gonna cum like a fire hydrant!"
    ya "slut!"
    play sound "audio/splurt2.ogg"
    show tott tott05
    with flash
    t "give me your cum, daddy!"
    play sound "audio/splurt2.ogg"
    with flash
    y "fuuck...."
    y "......"
    y "show me."
    hide tott
    show tott tott10 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "Nice."
    y "Whatever lifeforce was taken from me, I feel like I got it back tenfold!"
    y "Seeing your own sperm flow out of a girl's pussy does that to a man!"
    t "i'm glad i could help!"
    t "i'm gonna clean up...."
    t "be careful!"
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head back to your house and sleep."
    jump bk3_next

label jdpregfuck:

    show expression "bk3/joodee/pregfuck/home_joodee.jpg"

    show topr topr00
    y "Hey, Joo Dee. I came by for a final goodbye-"
    y "shit."
    y "Your belly seems surprisingly big."
    jd "Yes, isn't it wonderful? I'm expecting!"
    y "how?"
    jd "well that's usually what happens when a man drains his balls in your vagina, avatar."
    y "I'm pretty sure this isn't supposed to go this fast."
    jd "oh, There's a little shop around here which sells potions to shorten the proces."
    jd "Part of it is dragon scales which makes it extremely expensive, but due to my connections I got ahold of some!"
    jd "now come here sweetie, rest inside me."
    menu:
        "I'm not gonna fuck a pregnant chick":
            y "In that case... NO last goodbye fuck for you."
            y "Damnit.. I was looking forward to this."
            y "See ya, bigtits!"
        "looks like I'm gonna fuck me a preggo!":

            show topr topr01 with Dissolve(1.5)
            y "You discard your clothes and lie on the floor."
            y "Get naked and position yourself over my hard cock."
            jd "Yes, sir."

            show topr topr10 with Dissolve(1.5)
            y "That's fucking nice."
            y "Okay, slowly lower yourself."

            show topr topr03 with Dissolve(1.5)
            y "further."
            show topr topr04
            y "come on, further..."
            show topr topr05
            y "Oh, yeah...."
            y "Start moving."

            show topr topr100

            y "Get rough girl, drop yourself on my cock."
            jd "But.. my belly is so heavy."
            menu:
                "no backtalk...do it!":
                    show topr topr101
                "Fine, keep doing it the boring safe way":
                    pass
            y "Seeing that enormous tummy of yours going up and down is fucking hot."
            y "Say, who's kid is it anyway?"
            jd "Hmmm, either my husband's or yours..."
            y "don't lie, i know it's mine."
            jd "i... i..."
            y "Well, let's hope for your sake it won't be an airbender, or you'll have some explaining to do!"
            y "bear my fucking children, fuckpig!"
            jd "i... yes..."
            jd "yes!"
            jd "yes, i'll bear your progeny!"
            jd "i want your children. please!"
            jd "let me bear your offspring!"
            jd "i'll be your good cow, son."
            jd "whenever you desire this cunt, i will give it to you!"
            y "here i cum!"
            jd "joo dee the mommy slut will birth and give milk to the avatar's line!"
            jd "this is what i'm here for!"
            jd "fuck me, avatar!"
            jd "fuck me!"

            menu:
                "cum inside":

                    show topr topr05
                    play sound "audio/splurt2.ogg"
                    jd "give me your cum!"
                    y "take it, cow!"
                    with flash
                    show topr topr02
                    show expression "bk3/joodee/pregfuck/sperm_inside.png"
                    y "awh, yeah!"
                "cum outside":
                    show topr topr02
                    y "take it, cow!"
                    show topr topr11
                    play sound "audio/splurt2.ogg"
                    jd "give me your cum!"
                    show expression "bk3/joodee/pregfuck/spermshot.png"
                    $ renpy.pause(0.2)
                    hide expression "bk3/joodee/pregfuck/spermshot.png"
                    show expression "bk3/joodee/pregfuck/sperm_outside1.png"
                    y "fuck!"
                    show expression "bk3/joodee/pregfuck/spermshot.png"
                    $ renpy.pause(0.2)
                    hide expression "bk3/joodee/pregfuck/spermshot.png"
                    show expression "bk3/joodee/pregfuck/sperm_outside2.png"
                    jd "yes! give it all to me!"
                    show expression "bk3/joodee/pregfuck/spermshot.png"
                    $ renpy.pause(0.2)
                    hide expression "bk3/joodee/pregfuck/spermshot.png"
                    show expression "bk3/joodee/pregfuck/sperm_outside3.png"
                    y "aaah..."
                    y "alright, well... i'll see you around."
                    jd "goodbye for now, avatar!"

    jd "thank... thank you... son..."
    scene black with dissolve
    "you head home for the night."
    jump bk3_next


label tylee_wall_bj:
    hide screen earth_money_date
    show expression "bk3/tylee/stuckwall/base.jpg"
    show tosw tosw01
    with Dissolve(1.5)
    ty "see?"
    ty "now fuck my stupid face!"
    y "well... okay!"
    show tosw_surprise with dissolve
    ty "really!?"
    ty "but i'm so fucking useless."
    hide tosw_surprise with dissolve
    ty "i just... i just want you to notice me, really."
    show tosw_ashamed with dissolve
    ty "oh, um, now i'm embarrassed..."
    ty "i just want to... entertain you."
    y "...."
    ty "um... pull out your... um... cock?"
    hide tosw_ashamed
    show tosw tosw02_1
    with dissolve
    y "here you go."

    show tosw tosw02
    show tosw_lookdown
    with dissolve
    ty "it's always... impressive..."
    ty "staring at it from here."

    show ctc
    pause
    hide ctc
    ty "smells... sexy."
    hide tosw_lookdown with dissolve
    ty "does this... make you happy?"
    ty "seeing your dick right next to my stupid little face?"
    ty "getting you ready to cum all over my pretty little face... like a skanky little whore!"
    y "definitely. now suck."
    hide tosw_lookdown
    show tosw tosw05
    with dissolve
    ty "hmmm...?"
    show ctc
    pause
    hide ctc
    y "unh... that's right."
    ty "i'm... such a slut for you."
    show tosw tosw100
    ty "*sluurp* *suck* *glp*"
    show ctc
    pause
    hide ctc
    ty "hmah? *suck*"
    y "unhh... damn, girl..."
    ty "*slurp* *ssluuurp*"
    ty "i'm such a slut for you and your rock hard cock!"
    ty "sucking it so good for you!"
    ty "you treat me so good with your big dick!"
    ty "*shlup* *gulp* *sluck*"
    y "fuck..."
    show ctc
    pause
    hide ctc
    menu:
        "Give her a hand":
            show tosw tosw102
            ty "*mmgh!*"
            ty "*shlup* *slurp*"
            show ctc
            pause
            hide ctc
            ty "i'm not gonna stop until you cum!"
            ty "i'm not gonna stop until you give me that cum all over my skanky little face!"
            ty "gimme that cum!"
            ty "mmm... every last drop!"
            ty "i'm so stupid."
            ty "look at my stupid whore face."
            ty "don't you wanna cum on it?"
            y "I'm.... ngh...."
            y "Hng... almost there..."
            show tosw tosw11
        "don't do anything":

            show tosw tosw101
            ty "*mmgh!*"
            ty "*shlup* *slurp*"
            show ctc
            pause
            hide ctc
            ty "i'm not gonna stop until you cum!"
            ty "i'm not gonna stop until you give me that cum all over my skanky little face!"
            ty "gimme that cum!"
            ty "mmm... every last drop!"
            ty "i'm so stupid."
            ty "look at my stupid whore face."
            ty "don't you wanna cum on it?"
            y "I'm.... ngh...."
            y "Hng... almost there..."
            show tosw tosw07

    show ctc
    pause
    hide ctc
    play sound "audio/splurt2.ogg"
    with flash
    ya "take my load, slut!"
    play sound "audio/splurt1.ogg"
    with flash
    ya "right in your fucking throat!"
    ty "nngh!!"
    play sound "audio/splurt3.ogg"
    with flash
    y "ahh...."
    show ctc
    pause
    hide ctc
    show tosw tosw03 with Dissolve(1.5)
    ty "aahhh...."
    show ctc
    pause
    hide ctc
    ty "thank you!"
    y "you... ahh... are welcome..."
    jump bk3_village_background

label toph_appa_fuck:

    show expression "bk3/toph/appafuck/bluesky.jpg"
    show expression "bk3/toph/appafuck/cloud.png":
        ypos 40 xpos 1000
        linear 28.0 xpos -1400
        repeat

    show toaf_appafly:
        parallel:

            ease 4 ypos -40
            ease 6 ypos 40
            repeat
        parallel:

            ease 7 xpos -40
            ease 4 xpos 40
            repeat
    with dissolve
    show ctc
    pause
    hide ctc
    y "fly abba! Fly!"
    y "Man, this is awesome!"
    y "look at the view we have from up here!"


    to_l "Yeah, and you can see so far!!"
    to_l "Look, I can see Omashu!"
    y "What? Where? Oh......"
    to_l "Hahaha!"
    "She hits you in the shoulder hard enough to leave a bruise."
    y "ow..."
    "She seems...slightly nervous."
    to_d "You know.... being up in the sky like this..."
    to_d "It's almost like I'm a non-bender."

    to_d "Sort of like when I was locked up in that metal box in the tunnels."
    to_d "except... I still could get out then."
    to_d "right now, I'm pretty much at your mercy."
    to_bs "You could do whatever you wanted to me and there's nothing I could do about it..."
    y "hah! I'm still feeling that punch you gave me a second ago, so..."
    y "I'm sure you could put up a good fight if you wanted."
    to_a "Damn it, twinkletoes! Try to feel the mood!"
    to_p "It's just us up here and my earthbending is useless!"
    to_p "i'm a defenseless girl!"
    y "...uh..."

    to_d "*Sigh...*"
    to_n "Hey Aang, how about..."
    to_bs "tying me down, gagging me..."
    to_n "...and fucking my brains out?"
    y "That sounds.... really nice."
    y "But I don't have rope or anything like that..."

    show toaf_holdrope with Dissolve(1.5)

    t "I do...."
    show ctc
    pause
    hide ctc
    y "Oh, wow."
    y "this really isn't a spur of the moment idea, is it?"
    y "When did you come up with this?"
    t "Shortly after being imprisoned in that metal box."

    y "Look, if we're doing this... once that gag goes in your mouth, there's no stopping."
    y "No crying, no muffled sounding safewords to help you."
    y "nothing will stop me from plowing you until you chafe."
    y "You still want to?"
    "Toph swallows and nods."
    t "um... i think so."
    t "i mean... i think it'll make you happy, right?"
    t "i know y-you want to be in control."
    t "and this will... give you complete control over me."
    t "while you fuck me mercilessly, until your cock is content."


    hide toaf_holdrope with Dissolve(1.5)
    "Toph takes off her clothes and you tie her securely to Appa's saddle."
    "You take the gag and see Toph breathing heavily."
    y "no more chances to change your mind, Toph."
    "Toph seems uncertain and tries to speak..."
    "...you shove the gag in her mouth when she opens it."
    hide toaf_appafly





    show toaf_flying:
        linear 5.0 xpos -430 ypos -280
    $ renpy.pause(5.0)

    show toaf_flying:
        xpos -430 ypos -280
        linear 4.0 xpos -400
        linear 4.0 xpos -430
        repeat

    show toaf_flying:
        xpos -430 ypos -280
        linear 3 xpos -420 ypos -260
        linear 3 xpos -430 ypos -280
        repeat

    t "*mmphh!!*"
    show ctc
    pause
    hide ctc
    y "Look at you, naked out in the open with your legs spread..."
    y "I could just land Appa and call for everyone to come and take a look at you..."
    y "Maybe take a few photos for the new pornlove edition."
    t "*mmmphh!!*"
    y "Imagine how your father would react if he'd see you in there."
    y "That would certainly convince them of your adult qualities."
    "A slight look of panic can be read off of Tophs face."
    "She's pulling the ropes hard enough for them to bite into her ankles and wrists."
    "Some muffled words can be heard, but you give them no heed."
    show ctc
    pause
    hide ctc
    hide toaf_flying

    show expression "bk3/toph/appafuck/bluesky.jpg"

    show expression "bk3/toph/appafuck/cloud.png":
        ypos 40 xpos 1000
        linear 28.0 xpos -1400

        repeat

    show toaf_appahead:
        ypos 40 xpos 160
        linear 4 ypos 80
        linear 6 ypos 40
        repeat


    show toaf toaf100
    with dissolve
    y "you're not regretting this, are you?"
    t "......mmm...ngh.....?"
    show ctc
    pause
    hide ctc

    y "I'm actually really good at tying knots."
    y "now, let me just pull these a little..."
    show toaf toaf12 with ushake
    t "*mmph!!*"
    show ctc
    pause
    hide ctc
    y "As long as the rope doesn't break you're not getting out of there."
    show toaf toaf13 with ushake
    t "*hhnhmm!!*"
    y "aw, that's cute."
    y "you think that struggling will help."
    y "maybe i'll let appa have a go at you."
    t "*annghg!!*" with ushake
    y "would you like that?"
    t "*mmmngnggh!!!!*" with ushake
    y "i thought you would, but maybe later."
    t "*nngh! ngh!!*"
    y "alright, i'll set the ropes back..."
    show toaf toaf103 with dissolve
    t "*mmgh...hnnh...!*"
    show ctc
    pause
    hide ctc
    y "That soft white skin of yours is just begging to be licked all over..."
    y "But let's save that for another time."
    y "right now, I'll start warming up that pussy of yours."
    show toaf toaf13

    show expression "bk3/toph/appafuck/forcelegs_down.png"
    show toaf_shockface
    with vpunch

    y "There. Let's start rubbing that twat of yours."
    show ctc
    pause
    hide ctc

    hide toaf_shockface

    show expression "bk3/toph/appafuck/blink.png":
        xpos 439 ypos 145


    show toaf_dickrub

    "Rubbing your hard cock along Toph's slit you feel it getting warmer and wet."
    show ctc
    pause
    hide ctc
    "The silence this high up in the sky is only disturbed by Toph's soft moaning and the gutteral sounds Appa makes now and then."
    hide expression "bk3/toph/appafuck/forcelegs_down.png" with Dissolve(5.0)
    show toaf toaf101 with dissolve

    hide toaf_dickrub

    hide expression "bk3/toph/appafuck/blink.png"

    y "It's all nice and slippery now, so I'm going in."
    y "say \"please\"."
    "toph looks at you angrily and scared."
    t "hngh! hgnmm! mmm!!"
    show toaf_pussfuck
    show toaf_lewdface with Dissolve(1.5)
    t "*MMMMmmmmmhhhh!!*"
    show ctc
    pause
    hide ctc
    y "Hnnng, you're as... tight as ever, Toph."
    y "You might not like having a slender frame, but Fuck me if it hasn't got it's advantages."
    y "If I wasn't as hard as a fucking diamond I don't think I could even enter you!"
    "You keep sliding in and out of Toph at a slow but continous pace."
    show ctc
    pause
    hide ctc
    hide toaf_pussfuck
    show expression "bk3/toph/appafuck/openpussy_dry.png"
    with Dissolve(1.5)

    y "I think you're {i}almost{/i} ready for the hardest fuck of your life."
    show toaf toaf100
    hide expression "bk3/toph/appafuck/openpussy_dry.png"
    with Dissolve(1.5)
    y "which is just how i want you."
    y "not quite ready... but {i}almost{/i}."
    show toaf toaf13
    show expression "bk3/toph/appafuck/openpussy_dry.png"
    show expression "bk3/toph/appafuck/forcelegs_down.png"
    with Dissolve(1.5)
    t "*mmghn...*"
    y "Nonono, we're not going to take a break."
    t "*hmmgh..*"
    y "Keep them spread, 'cause I'm about to use every inch of this cock to explore deep within you now."
    hide toaf_shockface with Dissolve(1.5)

    hide expression "bk3/toph/appafuck/forcelegs_down.png" with dissolve

    y "I'm going to slam it in so hard Appa is going to have to do some course corrections!"
    y "ready?"
    t "*nnmm-*"
    hide expression "bk3/toph/appafuck/openpussy_dry.png"
    hide toaf_lewdface
    show toaf toaf102
    with vshake
    t "*hgngmmmm!!!!*"
    show ctc
    pause
    hide ctc
    y "that's it, bitch!"
    y "you tiny whore!"
    t "*mmghmg!!*"
    ya "thank me, slut!"
    t "*mmghagm!!*"
    y "take my fucking load!"
    menu:
        "cum inside":
            $ appafuck_cum = 'inside'
            play sound "audio/splurt2.ogg"
            hide toaf
            show toaf toaf24
            show toaf_lewdface
            with flash
            y "fuck!"
            t "*hnngh....*"
            play sound "audio/splurt3.ogg"
            show toaf toaf16
            with flash
            show ctc
            pause
            hide ctc
        "cum outside":

            $ appafuck_cum = 'outside'

            hide toaf

            show toaf toaf17
            show toaf_lewdface
            with dissolve
            y "little bitch!"
            t "*hnngh....*"
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/appafuck/sperm1.png"
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/appafuck/sperm2.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/toph/appafuck/sperm3.png"
            $ renpy.pause()

            hide expression "bk3/toph/appafuck/sperm1.png"
            hide expression "bk3/toph/appafuck/sperm2.png"
            hide expression "bk3/toph/appafuck/sperm3.png"

            hide toaf
            show toaf toaf26


    show expression "bk3/toph/appafuck/blink.png":
        xpos 439 ypos 145



    y "Fuck! We are definitely going to do this again..."
    show toaf_appahead:
        linear 6 ypos 110


    t "ZZZ...ZZZ...ZZZ..."
    y "Ehmmm... is that you or Appa making that sound?"
    t "*mumble*"
    y "Appa, buddy... you still with us?"

    show expression "bk3/toph/appafuck/cloud.png":
        ypos 600 xpos 700
        linear 3.0 ypos -100
        ypos 600 xpos 200
        linear 3.0 ypos -100
        repeat

    y "Are... are we losing altitude?"
    y "Let's look at the clouds...."
    y "They're going up...."
    t "*mumble mumble*"
    y "that's not... a {i}good{/i} thing..."
    hide expression "bk3/toph/appafuck/blink.png"
    hide toaf
    hide toaf_lewdface
    show toaf toaf26:
        ypos 0
        easeout 15 ypos 480
        linear 10 xpos 400

    show toaf_appahead:

        easeout 15 ypos 450
        linear 10 xpos 500

    t "hmm-?"
    t "*Mmmm!! Hmmmm!*"
    y "Don't worry, I'm sure he'll wake up before we fall to our deaths...."
    y "............."
    y "Anytime now...."
    show ctc
    pause
    hide ctc
    show expression "bk3/toph/appafuck/landscape.png" behind toaf_appahead:
        ypos 500
        easein 7.0 ypos 0


    y "Hey, it's lake laogai to our left!"
    y "Wow, it's really big."
    y "And... getting bigger."
    y "fast."
    y ".........."
    ya "I don't want to die a slut!"
    hide expression "bk3/toph/appafuck/cloud.png"

    ya "Hey appa wake the fuck up!!!"

    show toaf_appahead:
        ypos 400 xpos 500
        linear 1 ypos 380
        linear 1 ypos 400
        repeat
    show toaf toaf26:
        ypos 480 xpos 400

    y "Oh good, he's awake again!"
    $ renpy.pause()
    y "Hey buddy, don't fuckin scare us like that!"
    show expression "bk3/toph/appafuck/landscape.png" behind toaf_appahead:
        ypos 0

    y "Let's land at the lake before this guy decides to take another midair nap."
    y "Hold on, Toph!"
    y "Ehhh... never mind."
    y "Just stay as you are, looking delicious!"
    y "honestly, you're probably safer than me."
    y "....don't look at me like that."
    y "Yip yip, Appa!"
    show expression "bk3/toph/appafuck/landscape.png":
        linear 5 xzoom 1.5 yzoom 1.5 ypos -350
    $ renpy.pause(5)

    show expression "ebackgrounds/lake_laogai_3.jpg"
    hide toaf
    hide toaf_appahead

    show toaf_flying:
        xpos 500 ypos -280
        easein 4.0 ypos 200 xpos -430
    $ renpy.pause(4.0)
    show toaf_flying with vpunch


    y "Woohoo! landed it safely!"
    hide toaf_flying

    show toaf_appahead:
        ypos 50 xpos 100
    show toaf toaf27
    show expression "bk3/toph/appafuck/head1.png"
    with Dissolve(2.0)

    y "Skybisons are... AWESOME!"
    y "As long as they're well rested."
    "appa" "ZZZZZ...ZZZZ..."
    y "Man, that sound would be comforting if it wasn't almost the cause of our death."
    y "Catch up on your sleep you big oaf..."
    hide expression "bk3/toph/appafuck/head1.png"
    show toaf_nod
    t "*Mmmgh!*"

    y "OH, right, let me take that off."
    hide toaf_nod
    show expression "bk3/toph/appafuck/head_talk.png"
    t "I thought my heart was going to explode in my chest!!"
    t "I knew you could've saved us using airbending, but it still scared the shit out of me!"
    y "...uh... yeah, luckily I am a master at...ehm... airbending..."

    "Still excited from all that just happened, Toph doesn't notice someone approaching."
    $ temp_switch = 1

    menu:
        "Don't warn Toph":

            $ temp_switch = 0
            y "Hey guys!"
            k3 "What happened? I saw Appa plummet from the sky!"
            show expression "bk3/toph/appafuck/superblush.png"
            show toki toki01
            with dissolve
            t "H-hi... Katara..."
            k3 "Oh wow, look at that sperm!"
            k3 "Aang must've really given it to you, Toph!"
            show toaf_blink:
                ypos 145 xpos 439
            t "h-he certainly did..."
            k3 "I think I can see your cervix from here!"
            show expression "bk3/toph/appafuck/superblush_2.png":
                alpha 0.0
                linear 5 alpha 1.0
            t "...m..my...what?"
            if appafuck_cum == 'outside':
                k3 "look at all of that cum sprayed all over you!"
                k3 "If we were alone I'd lick it all off you right now!"
            else:
                k3 "look at all of that cum gushing out of your pussy!"
                k3 "If we were alone I'd give you a good few laps between the legs!"
            t "Who... who... else is..."
            show tosi tosi01:
                xzoom -1
            with dissolve
            suki "Oh hey, Toph... whoa goddamn..."
            show tosi_smile:
                xzoom -1
            with dissolve
            suki "did you get hit by a spermtrain?"
            t "......"
            hide toki
            with dissolve
            show tf with dissolve
            ty "Hey guys! wathcha' all doing-"
            ty "ooooh... that looks nice!"
            ty "Is this the line to buy tickets for the ride-appa ride?"
            ty "Is there a height limit? What's the price of admission?"
            t "Someone.... please kill me..."
            hide tosi
            hide tf
            hide tosi_smile
            with dissolve
            "During the next five minutes it feels like everyone in the village comes to take a look at your handiwork."
            show toii toii05:
                ypos 100
            with dissolve
            iroh "....This is enough fap material for at least a month!"
            iroh "Let me go home and get my camera!"
            hide toii with dissolve
            t "Aang!! "
            show expression "bk3/toph/appafuck/superblush_2.png":
                linear 2 alpha 0.0
            t "Do something!"
            y "Oh yeah, right."
            hide expression "bk3/toph/appafuck/superblush_2.png"
        "Warn Toph":




            $ temp_switch = 1
            y "Oh shit, someone's coming our way!"
            y "Wanna stick around, Toph?"
            show expression "bk3/toph/appafuck/superblush.png"
            t "NOOOOOOO!!!!"
            y "Okay, let's get out of here!"

    y "Appa! Tired or not, we're leaving. YIP YIP!"
    "Appa instinctively reacts to the command and leaps into the sky."
    show toaf_appahead:
        linear 1.0 ypos 100
        linear 0.5 ypos -50
    $ renpy.pause(1.5)
    hide expression "bk3/toph/appafuck/superblush.png"
    hide expression "bk3/toph/appafuck/head_talk.png"
    hide toaf
    hide toaf_blink
    hide toaf_appahead
    show toaf_appafly:
        ypos 00 xpos 200
        ease 6 ypos -600 xpos -200



    y "Destination, second star from the right!"
    hide expression "ebackgrounds/lake_laogai_3.jpg"
    show expression "bk3/toph/appafuck/landscape.png":
        xzoom 1.0 yzoom 1.0 ypos 0


    with Dissolve(1.5)

    show toaf_appahead:
        ypos 40 xpos 160
        linear 4 ypos 80
        linear 6 ypos 40
        repeat
    show toaf toaf27
    hide toaf_appafly
    show expression "bk3/toph/appafuck/head_talk.png"
    show expression "bk3/toph/appafuck/superblush.png"
    with Dissolve(1.5)
    show toaf_blink:
        ypos 145 xpos 439

    y "well...that was exciting."
    t "It was horrible!"
    if temp_switch == 0:
        y "Don't worry Toph, they were all jealous."
        t "They were?"
        y "The look in their eyes was one of envy!"
        t "They won't think I'm a whore?"
        y "pfft... you could be so lucky."
        y "There will be a lot of sclicking and fapping tonight inspired by you!"
    else:
        y "We got out of there before anyone could see us. No harm, no foul, girl!"
        y "Even if we had stayed I think most people would've enojoyed the view quite a bit!"
        t "They would've thought I'm some kind of whore!!"
        y "so? you are!"
        y "besides, they would have just been jealous."
        t "Jealous?"
        y "The avatar fucked you while being miles up in the sky."
        y "That hasn't happened in at least a hundred years!"
        t "That's right... "

    y "I'll untie you and put Appa down a bit further where we won't be disturbed."
    t "I like that idea. I like it a lot!"
    scene black with Dissolve(3)
    scene basingse_city_night with Dissolve(1)
    "appa lands in the court of the earth king."
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    $ toph_bikini = False
    show toi toi200
    show toph_regret
    show toi_blush
    with dissolve
    t "umm...."
    t "i'm... naked..."
    y "that's alright, it won't take long."
    t "but-"
    y "come on."
    hide toi_blush
    show toph_shocked
    show toi_blush
    with dissolve
    t "[bk3name]!"
    scene black with dissolve
    "ignoring toph, you make your way into the throneroom, the dai lee hidden and passive."
    show king_sitting with Dissolve(1)
    ek "hello!"
    ek "who are you?"
    y "we're friends, your earthy-ness."
    ek "are you sure? you did sort of... burst in."
    y "i'm the avatar."
    y "and this is... toph."
    show toi toi200
    show toph_regret
    show toi_blush
    with dissolve
    t "um... h-hello, your highness."
    ek "does... she know she's naked?"
    t "i-i do, your highness."
    ek "oh! that's good. is she a present?"
    ek "i've always enjoyed the idea of fucking a tiny lady."
    show toph_annoyed
    hide toph_regret
    hide toi_blush
    show toi_blush
    with dissolve
    t "what!?"
    t "It's not my fault i'm tiny!"
    t "i'm a full-bodied adult, and i don't need a king or any-"
    y "quiet, slut."
    hide toi_blush
    hide toph_annoyed
    show toph_regret
    show toi_blush
    with dissolve
    t "....."
    y "no, she's not here for you."
    ek "wait... did you say you're the avatar?"
    y "i did."
    show king_angry with dissolve
    ek "then you are an enemy of the state!"
    y "....what?"
    show king_blink with dissolve
    ek "long feng has made that clear!"
    y "long feng was a traitor, my dude."
    hide king_blink
    hide king_angry
    with dissolve
    ek "oh."
    ek "well, then that's fine."
    y "...."
    ek "what can i do for you?"
    y "the earth kingdom has secretly been at war for one hundred years."
    ek "really now."
    ek "neat."
    ek "what does that have to do with me?"
    y "...well, we figured out how to stop them."
    y "the day of black sun..."
    scene black with dissolve
    "you spend some time discussing with the earth king the vague details you remember about plans to stop the fire nation."
    show king_sitting
    show toi toi200
    show toph_regret
    show toi_blush
    with dissolve
    ek "well, this {i}is{/i} serious!"
    ek "i'll see to it right away!"
    ek "and maybe... let that girl put clothes on?"
    t "...please..."
    y "nah."
    y "good luck, earth man."
    ek "likewise, earth person!"
    scene black with dissolve
    scene basingse_city_night
    show toi toi200
    with dissolve
    t "well, that wasn't so bad!"
    y "right?"
    show flicker
    $ renpy.pause(1, hard=True)
    t "let's head back to the village."
    y "...."
    y "okay, we'll-"
    show flicker
    $ renpy.pause(1, hard=True)
    y "....."
    t "what is it?"
    y "i have to take care of something."
    y "go to appa, i'll meet you in a minute."
    show toph_regret with dissolve
    t "okay..."
    hide toph_regret
    hide toi
    with dissolve
    y "...."
    y "she's gone."
    show pgfull with dissolve
    s "hello again, avatar."
    y "what are you doing here?"
    s "it is time."
    hide pgfull
    show flicker
    $ renpy.pause(1, hard=True)
    show pgfull
    y "...."
    y "what's going on with you?"
    s "i am... weak."
    s "rescuing you, and trying to contain the dreamstealer were exhausting."
    s "i need time to recover, and i think soon there will be no time left."
    s "i have much to do, much to save..."
    s "but that is for another time."
    hide pgfull
    show flicker
    $ renpy.pause(1, hard=True)
    show pgfull
    s "now we must leave."
    y "where are we going?"
    s "you will see soon enough."
    y "damn you and your vagueness."
    y "at least let me say goodbye to toph."
    s "very well."
    s "but be swift."
    hide pgfull
    show flicker
    $ renpy.pause(1, hard=True)
    y "okay, toph... here we go."
    show toi toi200
    show toki toki01:
        xzoom -1
    with dissolve
    y "katara? what are you doing here?"
    k3 "i had a... feeling that i would meet you here."
    y "a \"feeling\", huh?"
    y "how did you get in to the palace grounds?"
    k3 "i just asked."
    y "are you shitting me?"
    k3 "no, it wasn't that difficult."
    k3 "especially with the dai lee letting things play out."
    y "oh."
    k3 "anyway, you were going to say goodbye."
    y "how did you..."
    y "...right."
    show toph_regret with dissolve
    t "\"goodbye\"?"
    y "i... am going to seem confused. starting in a minute or two."
    t "what do you mean?"
    y "i'm not going to remember any of this."
    y "and... my personality is going to change."
    t "why? i don't understand..."
    y "i can't tell you that."
    y "not yet, anyway..."
    y "maybe... there's a future version of you that knows?"
    t "what?"
    k3 "too complex, aang. focus."
    y "right. katara... thank you. for everything."
    k3 "you're welcome... [povname]."
    y "....."
    t "what did you call him?"
    k3 "don't worry about it, toph."
    t "don't leave me, aang."
    show toi_tears with dissolve
    t "please..."
    t "i need you!"
    t "you're my [bk3name]."
    y "i'm sorry, there's nothing i can do."
    y "this must happen."
    show pgfull with dissolve
    s "it is time."
    t "who said that?"
    y "toph..."
    k3 "go."
    t "no!"
    y "goodbye."
    y "i may return someday and fuck you filthy again."
    y "but for now... goodbye."
    t "i need you!"
    "the spirit pulls you out of aang's body."
    show toph_shocked
    hide toph_regret
    hide toi_tears
    show toi_tears
    hide pgfull
    with dissolve
    "you watch the body you'd inhabited fall to the ground as toph moves quickly to it."
    t "no!"
    scene black with dissolve
    scene black
    scene worldmap_01
    show pgfull
    with dissolve
    y "so what happens now?"
    s "you will learn airbending."
    y "i will?"
    y "how?"
    s "{b}you will find out... now."
    jump b4_s_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
