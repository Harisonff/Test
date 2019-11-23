









label b4_start:

    stop music

    scene white

    menu:
        "republic city - map":
            call screen b4_screen_repcity 
        "sidebox examples - everyone":

            jump sidebox_examples
        "korra - Start of book 4":

            jump korra_kid
        "Meelo, Ikki and Jinora - idles ":

            jump meet_the_kids
        "lin beifong - idles":

            jump linbeifong_idles
        "korra - idles":

            jump korra_idles
        "Pema - idles":

            jump pema_idles
        "Asami - idles":

            jump asami_idles
        "Shady - idles":

            jump shady_idles
        "Korra - meditate":

            jump korra_meditate
        "Korra - rub":

            jump korra_rub
        "Korra - titplay":

            jump korra_titplay
        "Pema - handjob":

            jump pema_handjob
        "Korra - wash":

            jump korra_wash
        "Equalist - idles":

            jump equalist_idles
        "Korra - legs":

            jump korra_legs
        "Lin - handjob":

            jump lin_handjob
        "":

            pass
        "2nd page":


            jump b4_start_page2
        "3rd page":
            jump b4_start_page3




label b4_start_page2:

    menu:
        "Lin - buttjob":

            jump lin_buttjob
        "Asami - tits":

            jump asami_tits
        "Korra - protein":

            jump korra_protein
        "Pema - blowjob":

            jump pema_blowjob
        "korra - boobjob":

            jump korra_boobjob
        "":



            pass
        "First page":

            jump b4_start
        "3rd page":
            jump b4_start_page3


label b4_start_page3:
    scene black

    menu:
        " attention - ":

            "I've added \"bfad bfad10\" and \"bfad bfad12\" to the asami idles"
            "I've added \"bfaa bfaa10\" to the lin idles"
            jump b4_start_page3
        "Asami - blowjob":


            jump asami_blowjob
        "lin - rub":
            jump lin_rub
        "pema - vag":
            jump pema_vag
        "korra - blowjob":
            jump korra_bj
        "Korra - footjob":
            jump korra_footjob
        "Korra - korra slapass":
            jump korra_slapass
        "Asami & Korra - titsuck":

            jump korrasami_titsuck
        "":


            pass
        "1st page":

            jump b4_start
        "2nd page":
            jump b4_start_page2









screen b4_screen_repcity:

    imagemap:

        ground "bk4/world_maps/republic_city.jpg"
        hover "bk4/world_maps/republic_city_hover.png"
        idle "bk4/world_maps/republic_city_idle.png"

        add "airtemple_cloud1"



        hotspot (298, 104, 230, 176) action [ Jump("start")]
        hotspot (543, 113, 295, 174) action [ Jump("start")]

        hotspot (746, 361, 253, 174) action [ Jump("b4_airtemple_map")]

        hotspot (42, 295, 370, 114) action [ Jump("start")]
        hotspot (47, 513, 266, 127) action [ Jump("start")]


screen b4_screen_airtemple:

    imagemap:

        if b4_daytime:
            ground "bk4/world_maps/airtemple_day.jpg"
        else:
            ground "bk4/world_maps/airtemple_night.jpg"

        hover "bk4/world_maps/airtemple_island_hover.png"
        idle "bk4/world_maps/airtemple_island_idle.png"

        add "airtemple_cloud1"




        hotspot (0, 390, 286, 158) action [ Jump("start")]
        hotspot (71, 187, 444, 175) action [ Jump("start")]

        hotspot (738, 64, 260, 110) action [ Jump("start")]

        hotspot (752, 448, 247, 111) action [ Jump("start")]
        hotspot (505, 589, 386, 113) action [ Jump("b4_repcity_map")]
        hotspot (310, 87, 325, 82) action [ Jump("start")]


label b4_airtemple_map:




    "night or day?"
    menu:
        "night":


            $ b4_daytime = False
            "b4_daytime = False"
        "day":
            $ b4_daytime = True
            "b4_daytime = True"

    call screen b4_screen_airtemple


label b4_repcity_map:





    call screen b4_screen_repcity










label korrasami_titsuck:

    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0




    show bfbb bfbb00
    "bfbb bfbb00"

    hide bfbb
    show bfbb bfbb05:
        linear 0.8 xpos 0
        linear 0.4 xpos 10
        repeat
    "bfbb bfbb05"

    hide bfbb
    show bfbb bfbb06
    "bfbb bfbb06"


    show bfbb bfbb10
    "bfbb bfbb10"

    hide bfbb
    show bfbb bfbb15a:
        linear 0.8 xpos 10
        linear 0.4 xpos 0
        repeat
    "bfbb bfbb15a"


    hide bfbb
    show bfbb bfbb16
    "bfbb bfbb16"

    jump b4_start_page3




label korra_slapass:







    show expression "bk4/backgrounds/tower_day_1.jpg":

        ypos -50



    show bfba bfba07:

        ypos 170 xpos 0

    "bfba bfba07"



    show bfba bfba07:

        linear 3.0 ypos 0 xpos 00

    show expression "bk4/backgrounds/tower_day_1.jpg":

        linear 3.0 ypos -170 xpos 00



    "bfba bfba07"





    show expression "bk4/backgrounds/tower_day_1.jpg":

        ypos -170 xpos 0

    hide bfba

    show bfba bfba08



    show expression "bk4/korra/slapass/pants_flash.png" with vpunch

    hide expression "bk4/korra/slapass/pants_flash.png"





    "bfba bfba08"



    show bfba bfba00

    "bfba bfba00"





    show bfba bfba01

    "bfba bfba01"





    show bfba bfba05

    b4_ta "bfba bfba05"

    $ renpy.pause()



    hide bfba

    show bfba bfba10

    "bfba bfba10"



    show bfba bfba11

    "bfba bfba11"



    show bfba bfba00

    "bfba bfba00"



    b4_tn "Okay Korra, I'll let you choose."

    b4_tn "I can slap the shit out of you... OR..."

    b4_tn "I can give you some light slapping with my finger up your snatch."

    b4_tn "Choose wisely!!"



    menu:
        "hard slapping":




            b4_tn "Okay, here comes the final round."

            b4_kn "Wait, I changed my m-"



            show bfba bfba05a

            $ renpy.pause()

            b4_tx "bfba bfba05a - This hurts you more than it does me Korra!!"



            hide bfba



            show bfba bfba12

            "bfba bfba12"



            show bfba bfba13 with Dissolve(1.5)

            "bfba bfba13"

            b4_tn "Aren't you going to pull up your pants?"

            b4_kn "No, I'm just going to let it cool off in the open air."



            hide bfba

            show bfba bfba13:

                parallel:

                    linear 11.0 xpos 650
                parallel:


                    linear 1.0 ypos 50

                    linear 1.0 ypos 0

                    repeat

            "korra carefully walks over to an open window to let the wind caress her more than tender butt."
        "finger slap":




            show expression "bk4/backgrounds/tower_day_1.jpg":

                ypos -350



            show bfba bfba14

            "bfba bfba14"



            hide bfba

            show bfba bfba15

            "bfba bfba15"





            hide bfba

            show bfba bfba16:

                linear 0.0 ypos 0

                linear 0.15 ypos 0

                linear 0.15 ypos 20

                linear 0.45 ypos 0

                repeat

            "bfba bfba16"

            b4_kn "I.. I think I'm gogga.."

            b4_tn "Just let it happen"



            hide bfba

            show bfba bfba17 with dissolve



            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray1.png"

            with hpunch

            b4_kn "Aaaaah!!!"



            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray2.png"

            with hpunch

            b4_kn "Aaaaah!!!"





            show bfba bfba17

            show bfba_xspray

            show expression "bk4/korra/slapass/x_spray3.png"

            with hpunch

            b4_kn "Aaaaaaah!!!"



            "bfba bfba17"















    jump b4_start_page3





label korra_bj:
    scene black
    show bfay bfay00:
        ypos 0
    with Dissolve(3)
    b4_kn "Uuuuhhh... wha... what's going on?"



    show bfay bfay00:
        ypos 0
        easeout 2 ypos -300
    b4_kn "I.. I can't move my arms."

    scene black
    show expression "bk4/backgrounds/bg_hangkorra.jpg":
        ypos -300
    show bfay bfay02
    with Dissolve(1.5)


    b4_kn "Hello!?"
    b4_kn "Can anyone hear me? Anyone?!"

    show bfay bfay03 with Dissolve(1.5)
    b4_tam "Hello Korra."
    show bfay_shock with hpunch
    b4_kn "Amon!"

    b4_tam "Ah you remember me. Good."
    b4_tam "We need to have a little talk Korra."
    b4_tam "I'm disappointed in your lack of progress with Tenzin."
    b4_kn "..."
    b4_tam "There is so much more which can be done and I feel like you're dragging your feet"
    b4_tam "I might have to take away your bending."
    b4_tam "Maybe I should spare myself the trouble and just do it right here and now."
    b4_tam "What do you think. Should I?"

    hide bfay_shock
    show bfay bfay03a with hpunch
    b4_kn "P..please don't!"
    b4_kn "I.. I'll do better!"



    menu:
        "Give her a friendly warning":
            b4_tam "Fine. But don't you ever forget Korra I can reach your whenever and wherever I please."
        "Give her a warning she won't forget. Ever.":




            b4_tam "Fine. But just to make sure you won't forget.. "
            b4_tam "I'll give you something to help you remember"
            show bfay bfay04a with Dissolve(2.0)
            b4_kn "Wha...what are you going to-"
            show bfay bfay05 with hpunch
            b4_kn "mumble muble!"
            b4_tam "Yes, that's more like it."
            b4_tam "You look great with a hard cock in your mouth."
            b4_tam "I don't really have to tell you what happens if you get teethy, do I?"
            b4_kn "...mumble"
            b4_tam "Good"

            hide bfay
            show bfay bfay01:
                linear 0.8 xpos 20
                linear 0.4 xpos 0
                repeat

            $ renpy.pause()

            b4_tam "How do you like blowing me?"
            b4_tam "That's all your mouth is good for."
            b4_tam "Count yourself lucky I don't feel like anal today."
            b4_tam "I'd have no problem spreading your asscheeks and bury my dick in it to the hilt."
            b4_tam "You're just a collection of holes for me to do with as I please."
            b4_tam "A living fleshlight."
            b4_tam "Hmmm.. a korra themed fleshlight might actually sell well."
            b4_kn "...mumble"
            b4_tam "You can't imagine how often people told me I was a disappointment compared to you while I was younger."
            b4_tam "{i}Korra could already bend water, earth and fire when she was six years old!{/i}"
            b4_tam "{i}Why can't you?!{/i}"
            b4_tam "That kind of shit get's pretty old really fast."
            b4_kn "...mumble?!?"
            b4_tam "What do you mean that doesn't make sense? "
            b4_kn "...mumble?!?"
            b4_tam "Oh right.....never mind all that."
            b4_tam "Why the fuck do I even understand what you're mumbling anyway?"
            b4_tam "Have you ever tasted sperm Korra?"
            b4_kn "...mumble"

            b4_tam "Let's speed this up."

            hide bfay
            show bfay bfay08
            $ renpy.pause()

            menu:
                "Come on her face":
                    show bfay bfay06a with Dissolve(1.5)
                    show bfay bfay06
                    b4_tam "Catch."


                    show bfay bfay06a


                    show bfay_spermshot
                    show expression "bk4/korra/bj/spermout1.png" with hpunch
                    b4_tam "Hnnn..."

                    show bfay_spermshot
                    show expression "bk4/korra/bj/spermout2.png" with hpunch
                    b4_tam "Hnnnnng..."

                    show bfay_spermshot
                    show expression "bk4/korra/bj/spermout3.png" with hpunch
                    show bfay bfay03a
                "Come in her mouth":





                    show bfay bfay07 with hpunch
                    b4_tam "Hnnn..."
                    show bfay bfay07 with hpunch
                    b4_tam "Hnnnnnnn...swallow..."
                    show bfay bfay07 with hpunch
                    b4_tam "Hnnnnnnngggg....it!!"
                    hide bfay
                    show bfay bfay04a
                    show expression "bk4/korra/bj/sperm_inside.png"
                    with Dissolve(1.5)
                    b4_kn "*Coff! Coff!*"

            b4_tam "Aaaah... that was nice."
            b4_tam "You're really good at being a piece of meat."


    b4_tam "I'll lower you to the floor in a moment."
    b4_tam "It shouldn't be long before you regain control over your arms."
    b4_tam "Tenzin is close by and you'll be a good little girl and don't say anything about what happened here."
    b4_tam "Understood?"
    b4_kn "...yes...."
    b4_tam "Here's a homework assignment. Do something dumb."
    b4_tam "Do something Tenzin will have to punish your for"
    b4_kn ".....yes"
    b4_tam "And whatever punishment he'll give you... you'll thank him for it."

    b4_tam "Till we meet again korra."
    b4_tam "And don't be mistaken. We {b}will{/b} meet again."



    scene black with Dissolve(1.5)
    show text "{color=#fff} You lower Korra to the ground and make your retreat.{/color}"
    $ renpy.pause()


    jump b4_start_page3




label pema_vag:

    menu:
        "park":
            pass
        "at home":
            jump pema_vag1

    show expression "bk4/backgrounds/park_day_2.jpg":
        ypos 0



    show bfac bfac04
    "pema" "What do yo think honey? Topless or not?"

    menu:
        "Let's keep it on":
            $ bfax_top = True
        "Take it off baby!":
            $ bfax_top = False




    hide bfac
    show bfax bfax07 with Dissolve(1.5)

    if bfax_top == False:
        b4_pn "That's a great idea."
        b4_pn "And since I'm already halfway naked..."
    else:


        b4_pn "That's not really adventurous of you."
        b4_pn "But... I have a solution for that!"
        b4_pn "If you don't want me to go topless, I'll go..."





    show bfax bfax08 with Dissolve(1.5)

    b4_tn "This seems...risky."
    b4_pn "Oh? Because we're in a public park or because the kids are up ahead?"
    b4_tn "Both."
    "pema" "I'm certain a couple of nice long thrusts can convince me to start putting on some clothes again."


    show bfax bfax01
    b4_pn "Mmmmhh??"

    show bfax bfax02
    b4_tn "I could've given you some at home. On the island."
    b4_pn "We'll certainly do a lot of that too, but today I want the extra thrill!"

    hide bfax
    show bfax bfax03:
        linear 1.0 xpos -5
        linear 0.6 xpos 0
        repeat
    b4_pn "Oooooh fuck... that's just what I need!"
    b4_pn "Beat my pussy into submission with your hard cock!"


    show bfax bfax05:
        linear 1.0 xpos 5
        linear 0.0 xpos 0
        repeat
    with dissolve

    b4_pn "Ah! Ah! Why are you being so gentle?! I need a good drilling! Not a handshake!"
    b4_tn "Really? You seem to be enjoying this."
    b4_pn "I do, but I want to enjoy it more and throw in some dirty talk!"
    b4_tn "You filthy slut."
    b4_pn "Ohh! More of that!"

    hide bfax
    show bfax bfax09:
        linear 0.45 xpos 10
        linear 0.0 xpos 0
        repeat
    b4_tn "You want it? You want my dick in that whore cunt of yours?"
    b4_pn "That's right. I want you to fuck my whore cunt!"
    b4_pn "I'm your private slut"
    b4_pn "Your dirty dirty cumbucket!"
    b4_tn "Gonna split you like a log!"


    hide bfax

    show bfax bfax06:
        linear 0.1 xpos 40
        linear 0.9 xpos 40
        linear 0.1 xpos 0
        linear 0.7 xpos 10
        repeat
    b4_pn "Yees!!"
    $ renpy.pause()



    menu:
        "cum inside":
            hide bfax

            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            pause(1.0)
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            pause(1.0)
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            pause(1.0)
            show bfax bfax10 with Dissolve(1.5)
            b4_pn "Sooo... good. I can feel it flowing outside of my pussy."

            menu:
                "Tell her to take a leak like this.":
                    b4_tn "If you have to take a leak, go right ahead."
                    b4_pn "I wasn't going to but now that you mention it I do feel like I could go."
                    show bfax_piss with dissolve
                    b4_pn "Aaaaah that feels great."
                    $ renpy.pause()
                    show bfax_piss:
                        xpos 500
                        linear 2.0 xzoom 0.0 xpos 420
                    b4_pn "Aaand.... done."
                    hide bfax_piss
                "DON'T":
                    pass
        "cum outside":

            b4_tn "Turn over! I'm gonna make you a blanket!"

            show bfax bfax11:
                xpos 0 ypos 0
            with Dissolve(1.5)
            b4_tx "Aaaand..."
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_1.png"
            with hpunch
            $ renpy.pause(1.0)

            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_2.png"
            with hpunch
            $ renpy.pause(1.0)

            b4_pn "Oooh!! You missed a spot!"
            b4_tn "Do you question my abilities as a living cum dispenser?!?"

            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_3.png"
            with hpunch
            $ renpy.pause(1.0)

            b4_pn "Hmmmm, that's better.."


    scene

    show expression "bk4/backgrounds/park_day_2.jpg":
        ypos 0
    show bfaa bfaa04:
        xpos 300
        linear 0.5 xpos -300
    "lin" "What the fuck do you think you two are doing here!?!" with hpunch
    "lin" "This is a {size=+10}public park!!{/size}"
    show expression "bk4/misc/black.png" with dissolve
    show text "{color=#fff}Without hurrying pema cleans herself up with the towel and puts her clothes back on {/color}"
    $ renpy.pause()
    hide text
    hide expression "bk4/misc/black.png" with Dissolve(1.5)

    show bfac bfac04 with dissolve
    b4_pn "Hi Lin. It's very simple really."
    b4_pn "My husband has taken me to the park with the kids for a relaxing afternoon."
    show bfaa bfaa04:
        linear 0.5 xpos 0 xzoom -1.0
    "lin" "That was quite a bit more than just relaxing!"

    b4_pn "Really? Because I feel veeery relaxed right now."
    "lin" "You can't just ...do it... in a public park!!"
    "lin" "The only reason I'm not arresting the both of you is because of your kids."
    b4_pn "Thank you. How lucky for us the captain of the police is patrolling the park!"
    b4_pn "Is that something you do more often? As a captain?"
    "lin" "......"
    "lin" "This is your one and only warning! Go and do your nasty stuff on that island of yours."
    show bfaa bfaa04:
        linear 0.5 xpos -400
    b4_pn "Wow, that woman is thirstier than a sponge in a desert."
    b4_pn "Well, that's one down. Now for the other."
    b4_tn "What other?"
    b4_pn "Jinora! Come out where we can see you."
    hide bfaa
    b4_tn "Eh, she isn't here. She's with the others up ahead."
    show bfac bfac05 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
    b4_pn "JINORA! Get your ass out here right now!"
    show bfac bfac04:
        xzoom -1.0
    show bfae jinora05
    with Dissolve(1.5)
    "Jinora steps forward from behind a bush not too far off."
    "jinora" ".. Yes? I was just passing by. Just now. By coincidence. "
    b4_pn "I told you to make sure to watch over your brother and sister..didn't I?"
    "jinora" ".....yes.."
    b4_pn "You can't do that while spying on me and your father, can you?"
    show bfae jinora06
    "jinora" "I didn't spy!"
    b4_pn "We'll talk about this later young lady. Now go and get the others. We're leaving."
    "jinora" "..okay. {size=-10}(I didn't spy.. I was just looking longer than strictly necessary){/size}"
    hide bfae
    hide bfac
    show bfac bfac04
    with Dissolve(1.5)
    b4_pn "How long do you think Lin had been watching us?"
    b4_tn "I'm more worried about how long Jinora has been watching!"
    b4_pn "Ah she's just young and curious. Don't worry about it."
    b4_pn "But that doesn't mean she can just shirk her responsibilities."
    b4_pn "I'll have to have a serious talk with her later today."
    b4_pn "I hope you had fu-"
    show bfae group05:
        xpos -900
        linear 2.0 xpos -200
    "jinora" "We're ready!"

    jump b4_start_page3



label pema_vag1:

    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0

    show bfac bfac02


    $ bfax_top = False

    b4_pn "What do yo think honey? Ready for some good old fashioned fuck her in the pussy?"
    b4_tx "PUUUSSSY!!"
    show bfac bfac07 with Dissolve(1.5)
    b4_pn "That's what I like to hear!"


    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos -200
    show bfax bfax01
    with Dissolve(1.5)

    b4_pn "Mmmmhh?? Well? what are you waiting for? A permit?"

    show bfax bfax02

    b4_tn "Just for the record, you're the hottest pregnant wife and mother of three I've ever had the honor of fucking."
    b4_pn "I'm not sure I like winning first prize in that very limited category..."
    b4_tn "You're the ideal wife?"
    b4_pn "Better!"
    b4_pn "Now treat me like a cheap whore!"
    b4_tn "Ehmm....Don't flatter yourself. You ARE a cheap whore."
    b4_pn "More!"

    hide bfax
    show bfax bfax03:
        linear 1.0 xpos 0
        linear 0.6 xpos 10
        repeat
    b4_pn "Oooooh fuck... that's just what I need!"
    b4_pn "Beat my pussy into submission with your stiff rod!"

    show bfax bfax05:
        linear 1.0 xpos 10
        linear 0.0 xpos 0
        repeat
    with dissolve

    b4_pn "Come on! I know you can do better than that!"
    b4_tn "Just making sure you're ready for the storm that's coming you filhty sow"
    b4_pn "Ohh! More of that!"
    b4_tn "I'm surprised your swollen tits aren't leaking yet because you sure are gushing on this end!"

    hide bfax
    show bfax bfax09:
        linear 0.45 xpos 10
        linear 0.0 xpos 0
        repeat
    b4_tn "You want it? You want my dick in that whore cunt of yours?"
    b4_pn "That's right. I want you to fuck my whore cunt!"
    b4_pn "I'm your private slut"
    b4_tn "I'll fucking split you like a log!"


    hide bfax
    show bfax bfax06:
        linear 0.8 xpos 40
        linear 0.2 xpos 0
        linear 0.8 xpos 10
        repeat
    b4_pn "Yees!!"
    $ renpy.pause()



    menu:
        "cum inside":
            hide bfax

            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            pause(1.0)
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            pause(1.0)
            show bfax bfax04 at Move((-10, 0), (10, 0), .10, bounce=True, repeat=True, delay=.275)
            pause(1.0)
            show bfax bfax10 with Dissolve(1.5)
            b4_pn "Sooo... good. I can feel it flowing outside of my pussy."
        "cum outside":

            b4_tn "Turn over!"

            show bfax bfax11:
                xpos 0 ypos 0
            with Dissolve(1.5)
            b4_tx "Aaaand..."
            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_1.png"
            with hpunch
            $ renpy.pause(1.0)

            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_2.png"
            with hpunch
            $ renpy.pause(1.0)

            show bfax_spermshot
            show expression "bk4/pema/vag/spermout_3.png"
            with hpunch
            $ renpy.pause(1.0)

            b4_pn "Aaaaah!! So much..."



    jump b4_start_page3





label lin_rub:


    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0


    show bfaa bfaa04 with hpunch
    "lin" "TENZIN!!"
    b4_tn "Ah! What?!"
    "lin" "Take off your clothes and lie down on my desk!"
    b4_tn "What? Why!? You're not my mom!"
    b4_tn "Not that my mom would tell me to do something like that.."

    show bfaa bfaa10 with Dissolve(1.5)
    "lin" "...."
    b4_tn "Okay, that's intriguing enough for me to play along."

    hide bfaa
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"
    with Dissolve(1.5)
    show bfaz bfaz01 with hpunch
    b4_tn "Ready when you are!"

    show bfaz bfaz02 with Dissolve(1.5)
    "lin" "Aren't you ashamed of yourself?"
    b4_tn "No?"
    "lin" "Fucking your wife in a public park where anyone could see you!"
    b4_tn "Oh that. Yeah I wasn't entirely convinced that was a good idea either"
    b4_tn "But Pema can be kind of forceful."

    show bfaz bfaz03 with Dissolve(1.5)
    "Lin let's some of her saliva fall on your dick."


    show bfaz bfaz04 with Dissolve(1.5)
    "Lin" "Don't act like you didn't enjoy that!"
    b4_tn "Eeehh... sorry for enjoying sex with my wife?!? I guess?"

    hide bfaz
    show bfaz bfaz05:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat

    $ renpy.pause()
    "lin" "hnnnn..."
    "lin" "I saw you... slamming that dumb cunt...hhhnn..."
    "lin" "As if you're some dumb horny teenager who's never had any..."
    "lin" "Act... your.... age....damn it!"
    b4_tn "Show me your titties!!"

    hide bfaz
    show bfaz bfaz06:
        linear 0.8 xpos 5 ypos 5
        linear 0.4 xpos 0 ypos 0
        repeat
    b4_tn "Niiiiice."


    menu:
        "switch view":
            $ temp_boolean = True

            "lin" "Shut up!"
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





    "lin" "You're much too old to be this desperate for sex!"
    b4_tn "You sure we're still talking about me?"
    b4_tn "I certainly won't decline any but I've seen someone else recently who seems to be more in need of a good dickdipping"
    b4_tn "Which I'm perfectly willing to provide if she'd ask."
    "lin" "Shut up!"

    if temp_boolean == True:
        hide expression "bk4/backgrounds/police_hq_ceiling.jpg"

    hide bfaz

    show bfaz bfaz09:
        linear 0.3 xpos 20 ypos 20
        linear 0.6 xpos 0 ypos 0
        repeat

    $ renpy.pause()
    "lin" "Are you ready to beg me for it? Do you want to fuck me?!"
    b4_tn "Well yeah, but-"
    "lin" "You can't! And I'll drive you crazy with lust!"
    b4_tx "Hnnn.. that's great but I'm going to cum real soon now.."



    menu:
        "cum on face":
            hide bfaz
            show bfaz bfaz10 at Move((0, 30), (0, 0), .10, bounce=True, repeat=False, delay=.275)
            "lin" "Cum all over my face you fucking horndog!"

            hide bfaz
            show bfaz bfaz10
            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_1.png"
            with vpunch
            $ renpy.pause()

            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_2.png"
            with vpunch
            $ renpy.pause()

            show bfaz_spermshot
            show expression "bk4/lin/rub/spermout_3.png"
            with vpunch
            $ renpy.pause()
        "cum on pussy":

            hide bfaz
            show expression "bk4/backgrounds/police_hq_ceiling.jpg"
            show bfaz bfaz12 at Move((0, 100), (0, 0), 0.5, bounce=False, repeat=False)
            "lin" "Show me how good your aim is."
            show bfaz bfaz13:
                ypos 0
            with Dissolve(1.5)
            "lin" "Fill me with YOUR CUM!!!"

            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout1.png"
            with vpunch
            $ renpy.pause()

            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout2.png"
            with vpunch
            $ renpy.pause()

            show bfaz_xspermshot
            show expression "bk4/lin/rub/x_spermout3.png"
            with vpunch
            $ renpy.pause()

    b4_tn "Pfew...... that was really-"
    "lin" "Now get out of my office!!"






    jump b4_start_page3








label korra_footjob:

    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0


    show bfab bfab04
    b4_kn "Hey.. tenzin. Do you.."
    kn "would you like to cum?"
    tn "depends. what are my options?"
    kn "well... i can give you my tits again..."
    kn "or... you could use... my feet?"
    kn "what would you prefer?"
    menu:
        "footjob":
            pass
        "boobjob":

            "test 02934"
    kn "Would you like a footjob?"
    b4_tn "You mean instead of a boobjob? That sounds nice!"
    show bfab bfab24
    b4_kn "Eh yeah sure."
    show bfab bfab25
    b4_kn "....I'll go change..."
    show bfab bfab18 with Dissolve(1.5)
    b4_kn "Just so my clothes won't be covered in your.. cum"
    b4_kn "I mean.. you do produce quite a lot."

    hide expression "bk4/backgrounds/korra_room_day.jpg"
    show expression "bk4/backgrounds/korra_room_bed.jpg":
        ypos 0
    hide bfab bfab18
    show bfaw bfaw01
    with Dissolve(1.5)
    b4_tn "I can see the wisdom in that precaution"
    b4_tn "Okay let's see some soles!"
    show bfaw bfaw02 with Dissolve(1.5)
    b4_tn "That's what I'm talking about!"
    b4_kn "Really, it's just feet."
    b4_kn "I honestly don't understand how you can get your kicks out of this.."
    b4_tn "It's become sort of a tradition really?"
    b4_kn "Tradition?!"
    show bfaw bfaw03
    b4_tn "Don't worry about it. Just press those pretty none smelly feet against my dick."
    show expression "bk4/korra/footjob/face_angry.png" with hpunch
    b4_kn "Of course they don't smell! I take good care of my body!"
    b4_tn "Noted."
    hide expression "bk4/korra/footjob/face_angry.png" with Dissolve(1.5)
    show bfaw bfaw04 with Dissolve(1.5)
    b4_tn "That's it.."
    b4_tn "Just move them up and down."

    show bfaw bfaw04a
    show bfaw_footjob1:
        linear 0.8 xpos 5
        linear 0.4 xpos 0
        repeat
    $ renpy.pause()
    b4_kn "SOoo.. Pema does this.. foot-stuff.. for you too?"
    b4_tn "Not lately..."
    b4_kn "Oh."
    b4_tn "Don't worry you're doing great."

    b4_tn "Hmmm.. I don't think I can cum from this alone."
    b4_tn "Hold on a minute."

    hide bfaw_footjob1

    show bfaw bfaw04
    show bfaw bfaw07 with Dissolve(1.5)
    b4_kn "Good, my legs started getting tired."
    b4_tn "Can you still raise them for a second?"

    show bfaw bfaw05
    with Dissolve(1.5)
    b4_tn "Okay now stretch them. I'll hold your feet at the heels and sandwich my dick in between."
    show bfaw bfaw06a with Dissolve(1.5)
    b4_kn "Now what?"
    b4_tn "Gonna use those lovely feet of yours as if they're a pair of tits!"
    b4_tn "You can just sit back a be pretty!"
    hide bfaw
    show bfaw bfaw06:
        xpos 10
        linear 0.6 xpos 0
        linear 0.2 xpos 10
        repeat
    b4_kn "Hmm well at least I can relax my legs this way...."
    $ renpy.pause()
    b4_tn "Any preferences where I aim?"
    b4_kn "Out of the window would be nice."
    b4_tn "You know I can't do that. It'd be a waste!"


    menu:
        "cum on feet":
            b4_tn "I'll plaster your soles with my cum!!"
            b4_tn "Bend those knees!"
            hide bfaw
            show bfaw bfaw05
            with Dissolve(1.5)
            b4_tx "Aaaaand..."
            show bfaw_spermshot
            show expression "bk4/korra/footjob/x_spermout1.png"
            with hpunch
            $ renpy.pause()

            show bfaw_spermshot
            show expression "bk4/korra/footjob/x_spermout2.png"
            with hpunch
            $ renpy.pause()

            show bfaw_spermshot
            show expression "bk4/korra/footjob/x_spermout3.png"
            with hpunch
            $ renpy.pause()
            b4_kn "Well, at least you didn't get my face and hair all sticky."
            b4_tn "...this time..."
        "cum like this":




            b4_tx "Can't.. hold it! It's gonna blow."
            b4_kn "Wait! Don't come on my-"
            hide bfaw
            show bfaw bfaw06a

            show bfaw_spermshot2
            show expression "bk4/korra/footjob/spermout1.png"
            with hpunch
            $ renpy.pause()

            show bfaw_spermshot2
            show expression "bk4/korra/footjob/spermout2.png"
            with hpunch
            $ renpy.pause()

            show bfaw_spermshot2
            show expression "bk4/korra/footjob/spermout3.png"
            with hpunch
            $ renpy.pause()

            show bfaw bfaw07 with dissolve
            b4_kn "....face"
            b4_tn "Sorry korra, it was that last stroke which got me by surprise."
            b4_ta "Your feet are too sexy! So it's actually your fault!"
            b4_tn "But I'll try and be more careful in the future."







    jump b4_start_page3




label asami_blowjob:


    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0
    b4_tp "Hey Asami! It's that time again."
    "asami" "...."
    b4_tp "Meet me in my studyroom"
    "asami" "You have a studyroom?"
    b4_tn "It was a surprise to me as well!"

    show expression "bk4/backgrounds/study0.jpg":
        ypos 0


    show bfad bfad02
    "Okay.. I'm here. Now what? You want me to shake my tits or something?"
    b4_tn "Hmmm no."

    show bfad bfad08

    "asami" "No?"

    b4_tn "Asami.. I made a shitload of copies of that photograph."
    show bfad bfad03
    "asami" "I'm not going to keep doing this unless there's an end in sight."
    b4_tn "Right, that's why I promise you I won't make any other copies of it ever."
    "asami" "....okay.."
    "asami" "I feel like you're not just doing this for my well being."
    b4_tn "Quite right!"
    b4_tn "But I'll trade you more copies the more interesting the act is you perform!"

    b4_tn "remember what I said the first time when Meelo interrupted us?"
    "asami" "You said \"Suck my co-\""
    b4_tn "I'd like some of that."

    "asami" "*sigh*"


    show bfad bfad10
    "asami" "I guess I'll have to take some precautions for what's inevitable then."



    hide bfad
    show bfad bfad11:
        xpos 300 ypos -20
    with Dissolve(1.5)
    "bfad bfad11"


    show expression "bk4/backgrounds/study0.jpg":
        ypos -200
    show bfav bfav00
    hide bfad
    with Dissolve(1.5)
    "asami" "Okay.. I guess we're doing this..."

    show bfav bfav01
    "bfav bfav01"

    show bfav bfav01a
    "bfav bfav01a"

    show bfav bfav08
    "bfav bfav08"

    show bfav bfav02
    "bfav bfav02"

    show bfav bfav08
    "bfav bfav08"

    show bfav bfav03
    "bfav bfav03"

    show bfav bfav04
    "bfav bfav04"


    show bfav bfav06
    "bfav bfav06"





    menu:
        "inside":
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            pause(0.8)
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            pause(0.8)
            show bfav bfav10 at Move((0, 30), (0, 0), .10, bounce=False, repeat=True, delay=.275)
            pause(0.8)
            "bfav bfav05"

            show bfav bfav07 with Dissolve(1.5)
            "bfav bfav07"
        "outside":

            hide bfav
            show expression "bk4/backgrounds/study0.jpg":
                ypos -420
            show bfav bfav09
            with Dissolve(1.5)
            "bfav bfav09"
            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_1.png" with hpunch
            $ renpy.pause()

            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_2.png" with hpunch
            $ renpy.pause()

            show bfav_spermshot
            show expression "bk4/asami/blowjob/spermout_3.png" with hpunch
            $ renpy.pause()

    jump b4_start_page3





    label korra_boobjob:

        menu:
            "livecomposites":

                show bfau bfau01
                "bfau bfau01"
                show bfau bfau02
                "bfau bfau02"
                show bfau bfau02a
                "bfau bfau02a"
                show bfau bfau03
                "bfau bfau03"
                show bfau bfau04
                "bfau bfau04"
                show bfau bfau05
                "bfau bfau05"

                show bfau bfau06
                "bfau bfau06"
                show bfau bfau07
                "bfau bfau07"
                show bfau bfau08
                "bfau bfau08"
                show bfau bfau09
                "bfau bfau09"
                show bfau bfau10
                "bfau bfau10"
                show bfau bfau11
                "bfau bfau11"

                hide bfau

                show bfau_boobjob_fast
                "bfau_boobjob_fast"
                hide bfau_boobjob_fast

                show bfau_boobjob
                "bfau_boobjob"
                hide bfau_boobjob

                show bfau_blink
                "bfau_blink"
                hide bfau_blink

                show bfau_spermshot
                "bfau_spermshot"
                hide bfau_spermshot

                show bfau_z_spermshot
                "bfau_z_spermshot"
                hide bfau_z_spermshot

                jump start
            "example scene":



                pass




        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0

        show bfab bfab24
        b4_kn "You.. want to do what?"
        b4_tn "With Pema pregnant, she can't give me boobjobs."
        b4_tn "Belly is in the way."
        b4_kn "But...how, why should I...?"
        b4_tn "I can't be properly satisfied without getting a boobjob every now and then and if I'm not satisfied..."
        b4_tn "Well Asami has already shown some interest in me and Pema said she'd allow it."
        show bfab bfab12 at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
        b4_kn "She did!?!?"
        b4_tn "She might seem like a wallflower to some, but she's actually pulling all the strings Korra."
        b4_tn "Don't underestimate her or you'll end up eating out her pussy!"
        b4_ta "Is that what you want Korra?! Eat out my wife's pussy?!"
        b4_kn "nn.. NO!!"
        show bfab bfab24 with Dissolve(1.5)
        b4_tn "Anyway, it's either going to be Asami or if you're willing to sacrifice yourself for a good cause, you."
        b4_tn "Honestly, I think her boobsucking stress relief sessions with me are just an excuse to hang around me..."
        b4_tn "And you're the avatar, you like helping people don't you?"
        b4_tn "Just imagine Asami with my dick between her boobs... cumming all over her. With her face covered in my cum."
        b4_tn "Her lower lip slightly quivering with extasy...is that what you want?!"
        b4_kn "....no."
        b4_tn "Then please help me. Just think of it as slightly more intense training session. "
        b4_tn "I've already seen and touched them plenty of times so it's no big deal."
        b4_kn "Yeah but... you didn't touch them with.. with your penis."


        show bfab bfab26 with Dissolve(1.5)
        b4_kn "*sigh* So if I do this you won't ask Asami for boobjobs?"
        b4_tn "I won't"
        b4_kn "Okay, let's make this quick."

        hide bfab
        show bfau bfau01
        with Dissolve(1.5)

        b4_kn "Okay... now what?"
        b4_tn "Now I push my dick between your chocolate funbags."

        show bfau bfau02 at Move((10, 0), (0, 0), .10, bounce=False, repeat=True, delay=.275)
        b4_tn "like this."
        b4_tn "And to prevent any burnmarks..."

        show expression "bk4/korra/boobjob/spit.png":
            alpha 1.0
            linear 3.0 alpha 0.0
        pause(3.0)
        hide expression "bk4/korra/boobjob/spit.png"
        b4_tn "..here's some spit to help things slide nice and smoothly."
        b4_tn "Just keep pressing those tits of yours together as I move up and down."

        hide bfau
        show bfau bfau03:
            linear 0.8 xpos 5
            linear 0.4 xpos 0
            repeat
        b4_tn "Oh yeaahhh... this is the stuff."
        $ renpy.pause()
        b4_tn "How do you like my erect dick being wedged in between your boobs?"
        b4_kn "This is ...okay"
        b4_tn "Well, let me make it a little be more interesting."
        b4_tn "Hold on tight."
        b4_kn "To what?!"

        show bfau bfau04
        b4_kn "AH!"
        b4_kn "Be more ..Ah! careful! ..Ah! "
        b4_tn "Here.... it... comes!"

        hide bfau
        show bfau bfau02

        show bfau_spermshot with vpunch
        show expression "bk4/korra/boobjob/spermout_1.png"
        b4_tx "Hnnng!"
        show bfau_spermshot with vpunch
        show expression "bk4/korra/boobjob/spermout_2.png"
        b4_tx "Hnnnnng!"


        scene
        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
        show bfau bfau01
        show expression "bk4/korra/boobjob/spermout_4.png"
        with Dissolve(1.5)

        b4_kn "Yuck. I'm all covered with this stuff."
        show expression "bk4/korra/boobjob/spermout_4.png":
            linear 11.0 alpha 0.0
        b4_tn "It looks great on you."
        b4_tn "Ready for round two?"
        b4_kn "Shouldn't this be over when you cum?"
        b4_tn "Usually, but I think there's some more left where that came from."
        b4_kn "That's...I don't think it works like that."
        b4_tn "Lie down and I'll prove you wrong."

        scene
        show expression "bk4/backgrounds/korra_room_bed.jpg"

        show bfau bfau05 with Dissolve(1.5)
        b4_kn "I don't think we should be doing this here now... Anyone could walk in and ..."

        show bfau bfau06 with Dissolve(1.5)
        b4_tn "Don't worry this won't take long."
        b4_tn "And this way I can massage your boobs too."
        b4_kn "....."


        hide bfau
        show bfau bfau07:
            xpos 0
            easein 0.8 xpos -10
            easeout 0.4 xpos 0
            repeat

        $ renpy.pause()
        b4_kn "Hmmmmpfff."
        b4_kn "....."
        "You keep sliding up and down in a steady rythm while intensifying the kneeding of Korra's boobs."

        show bfau bfau08:
            xpos 0
            easein 0.8 xpos -10
            easeout 0.4 xpos 0
            repeat
        with Dissolve(1.5)
        $ renpy.pause()

        b4_kn "...."
        b4_tn "Are you starting to enjoy this you slut??"
        b4_tx "Hnnnng... getting there...."
        b4_tx "Time to prove to you my seed is both potent and plentiful!"

        hide bfau
        show bfau bfau10:
            xpos 20
            linear 0.2 xpos -10
            linear 0.6 xpos 20
            repeat

        $ renpy.pause()

        hide bfau
        show bfau bfau09


        show bfau_z_spermshot with hpunch
        show expression "bk4/korra/boobjob/z_spermout_1.png"
        b4_tx "Hnng!"


        show bfau_z_spermshot with hpunch
        show expression "bk4/korra/boobjob/z_spermout_2.png"
        b4_tx "Hnnnng!"
        b4_tx "LAST STOP!!!!"

        show bfau_z_spermshot with hpunch
        show expression "bk4/korra/boobjob/z_spermout_3.png"

        $ renpy.pause()
        b4_tn "Damn! I love how my gunk contrast with your skin!"
        show bfau bfau11 with Dissolve(1.5)
        $ renpy.pause

        b4_tn "See you later Korra. Don't forget to wash you face."


        jump start




    label pema_blowjob:

        show expression "bk4/backgrounds/bed_tenzin_1.jpg":
            ypos 0

        menu:
            "only composites":

                show bfas bfas00
                "bfas bfas00"
                show bfas bfas01
                "bfas bfas01"
                show bfas bfas02
                "bfas bfas02"
                show bfas bfas03
                "bfas bfas03"
                show bfas bfas04
                "bfas bfas04"
                show bfas bfas05
                "bfas bfas05"
                show bfas bfas06
                "bfas bfas06"
                show bfas bfas06b
                "bfas bfas06b"
                show bfas bfas07
                "bfas bfas07"
                show bfas bfas08
                "bfas bfas08"

                hide bfas

                show bfas_blowfast_pbody
                "bfas_blowfast_pbody"
                hide bfas_blowfast_pbody

                show bfas_blowfast
                "bfas_blowfast"
                hide bfas_blowfast

                show bfas_blow
                "bfas_blow"
                hide bfas_blow

                show bfas_blink
                "bfas_link"
                hide bfas_blink

                jump start
            "example scene":

                pass
        show bfac bfac01:
            xpos -400 ypos -50
        b4_pn "Hi Huney."
        show bfac bfac02:
            xzoom -1.0 xpos 500
        b4_pn "How about a nice relaxing blowjob from your pretty wife?"
        "You quickly strip."
        b4_tx "Let's do this thing!!"
        show bfac bfac07 with Dissolve(1.5)
        b4_pn "Ooooh, you really are looking forward to one, aren't you?"

        b4_tx "You SUUUUUCKKKK!!!"
        b4_tn "I mean.. yes, please suck my dick."
        b4_pn "Patience dear. I can't move that fast anymore with this belly"

        hide bfac
        show bfas bfas00 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)

        b4_pn "Now push that big meaty rod of yours in my face!!"


        show bfas bfas01 with Dissolve(1.5)
        b4_tn "Ready and willing!"

        show bfas bfas02
        b4_pn "Mmmmm willing indeed. You have surprisingly little trouble getting it up lately."
        b4_pn "There has been a time when it took some work to get you into action mode."
        b4_pn "I shouldn't be worried about Korra being the cause of this do I?"

        hide bfas
        show bfas bfas03:
            xpos 30
            easein 1.0 xpos 40
            easeout 0.6 xpos 30
            repeat

        b4_tx "Hnnnnng.."
        "Pema slides her lips over your pulsating cock, moistening the shaft with her saliva."
        "She only pulls her head back enough to give her enough space to lick the tip within her mouth."
        "She clearly knows your current dick better than you yourself and uses that knowledge with great effect."
        b4_ts "Korra smorrah. Your lovely lips are the magic touch."
        $ renpy.pause()

        hide bfas
        show bfas bfas02
        with Dissolve(1.5)
        b4_pn "Well, I don't care what you do to her as long as you make sure she hates it and I'll get to enjoy some of it too eventually."
        b4_tn "Sounds like a win win situation to me."
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
        $ renpy.pause()

        b4_tx "Hnnnngg!"
        b4_tx "Gonna cum! Want it all over your face or down your throat?"
        "Muble mumble."


        menu:
            "Have her swallow it.":
                $ temp_boolean = True
                hide bfas
                show bfas bfas06
                with Dissolve(1.5)
                show bfas bfas06 with vpunch
                b4_pn "gurgle"
                show bfas bfas06 with vpunch
                b4_pn "gurgle"
                show bfas bfas06b with Dissolve(1.5)
                b4_pn "*cofcof* That was quite the load. Even for you!"

                show bfas bfas01
                show expression "bk4/pema/blowjob/sperminside.png"
                with Dissolve(1.5)
            "Unload on her face":



                $ temp_boolean = False
                hide bfas
                show bfas bfas05

                show expression "bk4/pema/blowjob/spermout_1.png" with hpunch
                $ renpy.pause()
                show expression "bk4/pema/blowjob/spermout_2.png" with hpunch
                b4_tn "Replenishable facial moisterizer!"
                b4_pn "Normally it isn't applied by the gallon though."

        show bfas bfas01
        b4_tn "Just givin it my best."

        scene



        if temp_boolean == False:
            show expression "bk4/backgrounds/bed_tenzin_1.jpg":
                ypos -80
            show bfas bfas07
            show expression "bk4/pema/blowjob/spermonface.png"
            with Dissolve(1.5)
            $ renpy.pause(1.0)
            b4_pn "Since the sheets are already ruined I might as well use them to clean myself up and go get some fresh ones."
        else:
            show expression "bk4/backgrounds/bed_tenzin_1.jpg":
                ypos -80
            show bfas bfas07
            show expression "bk4/pema/blowjob/spermontits.png"
            with Dissolve(1.5)
            $ renpy.pause(1.0)
            b4_pn "It leaked all over my tits and on the sheets so I might as well use them to clean myself up and go get some fresh ones."





        hide bfas
        scene
        show expression "bk4/backgrounds/tenzin_room_day.jpg":
            ypos 0
        show bfaj bfaj19

        b4_tn "Cool, I'll-"
        show bfae jinora02:
            xpos 500
            linear 0.5 xpos 0

        "Mom! Dad! Can I...."
        show bfae jinora03
        "What..."
        show bfae jinora04 at Move((10, 10), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
        "AAhhh!! Gross!!! Eeeewh!!EEEEwh!!!"
        show bfae jinora04:
            linear 0.5 xpos 500
        "{size=+15} EEEEwwwwh!!{/size}"
        b4_tn "Should-"
        show bfae jinora04:
            linear 0.5 xpos -150
            linear 1.0 xpos -150
            linear 0.5 xpos 500
        "{size=+30} EEEEwwwwh!!{/size}"

        b4_tn "..."
        b4_tn "Should we-"

        show bfae jinora04:
            linear 0.5 xpos -150
            linear 1.0 xpos -150
            linear 0.5 xpos 500
        "{size=+30} EEEEwwwwh!! Put some clothes on!{/size}"

        b4_tn "For someone who's disgusted you come back awfully often!!"
        b4_tn "And knock before you enter a room!!"
        b4_pn "I think she's really gone this time."
        b4_tn "Should we go after her or something?"
        b4_pn "Nah she'll be fine. besides."
        b4_pn "You still have your dick all out like that."
        b4_pn "Don't worry, I already told her about the birds and the bees."
        b4_pn "Aside from some light mental scarring she'll be fine."




        jump start

    label korra_protein:
        menu:
            "composites":

                show expression "bk4/backgrounds/korra_room_day.jpg":
                    ypos 0

                show bfar bfar00
                "bfar bfar00"

                show bfar bfar01
                "bfar bfar01"

                show bfar bfar02
                "bfar bfar02"

                show bfar bfar03
                "bfar bfar03"

                show bfar bfar04
                "bfar bfar04"

                show bfar bfar05
                "bfar bfar05"

                show bfar bfar07
                "bfar bfar07"

                show bfar bfar05
                "bfar bfar05"

                show bfar bfar06
                "bfar bfar06"

                show bfar bfar08
                "bfar bfar08"

                show bfar bfar09
                "bfar bfar09"


                show bfar bfar10
                show expression "bk4/korra/protein/barf.png":
                    ypos -30
                    linear 2.0 ypos 400
                "bfar bfar10"

                show bfar bfar11
                "bfar bfar11"
                show bfar bfar12
                "bfar bfar12"
                show bfar bfar13
                "bfar bfar13"

                jump start
            "example scene":

                pass



        show expression "bk4/backgrounds/hallway_01.jpg":
            ypos 0
        b4_tn "Okay I got myself a protein shake. And now to add a personal touch for Korra."
        show bfar bfar00
        b4_tx "Hnnnng.. gonna give you some of the best nutritional shake you've ever....had!"
        show bfar bfar00a with hpunch
        show bfar bfar00
        pause(0.5)
        show bfar bfar00a with hpunch
        show bfar bfar00
        pause(0.5)
        show bfar bfar00a with hpunch

        hide bfar
        b4_tn "Okay, now to find Korra."

        show bfae jinora02
        "jinora" "Hey! What's that!?"
        b4_tn "It's a protein shake for Korra. You know where I can find her?"
        "jinora" "Not really. Can I have a taste?"
        b4_tn "It's for Korra."
        "jinora" "Just a few sips."
        b4_tn "....It's for Korra."
        "jinora" "Just one sip."
        b4_tn "I..I {size=+10}really{/size} don't think you'd like the taste of this."
        show bfae jinora03
        "jinora" "So Korra gets drinks from you and I don't..."
        show bfae jinora04
        "jinora" "It's not fair!"
        "jinora" "You're already spending all this time with her!"
        "jinora" "And to be honest... I'm not sure it's always only training!!"
        b4_tn "Wha... what?"

        show bfae jinora03 with dissolve
        "jinora" ".....nothing..."
        show bfae jinora02 with dissolve
        b4_tn "Look, you want to have some of this shake?"
        "jinora" "Yes."

        menu:
            "Not gonna happen.":
                b4_tn "I mean it's a super special reward for Korra."
                b4_tn "Because she did really well during training, so..."
                "jinora" "I also try my best! Always!"
                b4_tn "Trust me, you're better off not tasting this."
                show bfae jinora04
                "Jinora is clearly unsatisfied with your reaction."
                b4_tn "You're really into this whole airbender thing, right?"
                "jinora" "Yes!"
                b4_tn "How about this. When it's time to get your own arrow tattoos.. I'll back you up on it."
                b4_tn "Even when you're still clearly too young."
                show bfae jinora03
                "jinora" "Really?"
                show bfae jinora02
                "jinora" "AWESOME!!"
                b4_tn "Just to be clear, you're STILL nowhere near the tattoo level. But when you are I'll help you convince your mom."
                "jinora" "I'm going to train twice as hard!"
                b4_tn "...eehhh, sure?"
                "jinora" "I'm going to train right now!"
                b4_tn "Oh and you can't tell anyone about our deal."
                "jinora" "Okay!"
                hide bfae
                show bfae jinora02:
                    linear 1.0 xpos 300
            "....Fine.. but don't complain afterwards.":

                show bfae jinora11
                b4_tn "It's not like it can do any harm. I think."
                b4_tn "Still, I'm going to regret this..."
                b4_tn "(and possibly go to hell)"
                b4_tn "Here you go."
                "jinora" "Thanks!"
                hide bfae
                show bfae jinora12:
                    ypos 0
                    linear 0.4 ypos 15
                    linear 0.4 ypos 0
                    repeat
                "glug glug."
                hide bfae
                show bfae jinora11
                "jinora" "Yum! Creamy!"
                hide bfae
                show bfae jinora12:
                    ypos 0
                    linear 0.4 ypos 15
                    linear 0.4 ypos 0
                    repeat
                b4_tn "Oh.. man... Hey you said a few sips!"
                b4_tn "Stop that damn it!"
                hide bfae
                show bfae jinora11
                b4_tn "Damn you drank a lot..."
                "jinora" "Sorry!"
                b4_tn "Ah, forget it I think I can make some more. Now go do something elsewhere."
                "jinora" "Okay."
                hide bfae
                show bfae jinora02:
                    linear 1.0 xpos 300


                b4_tn "Okay, here I go again."
                hide bfae jinora02
                show bfar bfar00
                b4_tx "Hnnnng.. !"
                show bfar bfar00a with hpunch
                show bfar bfar00
                pause(0.5)
                show bfar bfar00a with hpunch
                show bfar bfar00
                pause(0.5)
                show bfar bfar00a with hpunch
                hide bfar

        b4_tn "Finally, now let's find Korra before anyone else shows up."






        scene
        show expression "bk4/backgrounds/korra_room_day.jpg":
            ypos 0
        show bfar bfar01
        with Dissolve(1.5)
        b4_tn "Hey Korra, I was thinking....."
        b4_kn "I didn't do it."
        b4_tn "What?"
        b4_kn "I meant, what's up dude."
        b4_tn "I got something for you."
        b4_kn "Is it chores?"
        b4_tn "I can give you those too... but instead I'll give you this."

        show bfar bfar02
        b4_kn "Eh, what's that?"
        b4_tn "With an airbenders' diet, I guessed such an energetic girl needs more than the usual amount of protein."
        b4_tn "It's a protein shake."

        show bfar bfar03
        b4_kn "Oh.. eh.. thanks?"
        b4_kn "The stuff Pema makes is kind of bland."
        b4_tn "Oh, cool, I'll let her know."
        b4_kn "Yeahhh, let's not. Pema is always riding my ass about one thing or another."
        b4_kn "She really doesn't need more of an incentive to dislike me."

        show bfar bfar04
        b4_tn "Oh I thought you two got along just fine."
        b4_kn "What's in this anyway?"
        b4_tn "Just your average stuff plus a secret airbender ingredient."
        b4_kn "Normally I'd say you're messing with me and put something rancid in there, but it kinda makes sense."
        b4_tn "It does?"
        b4_kn "Aren't you airbender monks vegetarians or something? It stands to reason you'd need something extra to suplement the protein lack."
        b4_tn "Ehh yeah that's it."
        b4_kn "Well, let's give it a taste test. It's probably going to taste horrible."

        show bfar bfar05
        "Glug glugh glugh."
        "You watch as Korra let's your secret sauce glide down her throat."

        show bfar bfar07 with Dissolve(1.5)
        b4_tn "So? How is it?"
        b4_kn "Creamy! It reallys slides down like it wants to get inside!"
        b4_kn "I was mentally prepared to have to swallow some horrid crud, but it's actually good!"

        show bfar bfar05
        b4_kn "*Glugh* you could probably... *glugh* sell this stuff!"
        b4_tn "Yeah in jars to an entire southern watertribe village."

        show bfar bfar06
        b4_kn "That's odly specific... but yeah I guess."
        b4_kn "Why? do you have any plans to really market this stuff?"
        show bfar bfar08
        b4_tn "I'm awesome but I doubt I can rub out enough to make this a real enterprise."


        show bfar bfar09
        b4_kn "rub... out?"
        b4_tn "It's sperm."
        b4_tn "The secret ingredient is sperm and you've just been gulping down my seed like it's the best thing in the world."

        show bfar bfar10 at Move((10, 0), (0, 0), .10, bounce=True, repeat=True, delay=.275)

        show expression "bk4/korra/protein/barf.png":
            ypos -30
            linear 2.0 ypos 400
        b4_kn "*Barf*"

        show bfar bfar11
        b4_kn "What the fuck Tenzin!?"
        b4_ts "Hahaha, you're so gullible!"
        b4_ts "And clearly not far enough with your training if you let this disturb you."
        show bfar bfar12
        b4_kn "So it's not sperm? You really had me freaking out! That wasn't funny!"
        b4_ts "Nah, it was awesome. You going to finish that or did I scare you too much?"
        show bfar bfar13
        b4_kn "You? Scaring me!? In your dreams!"
        show bfar bfar05
        $ renpy.pause()
        b4_kn "*burp*"
        show bfar bfar04
        b4_kn "See? No problem whatsoever."
        show bfar bfar04 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
        b4_kn "*burppp*"

        jump start


label asami_tits:

    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0




    menu:
        "just composites":
            show bfaq bfaq00
            "bfaq bfaq00"
            show bfaq bfaq01
            "bfaq bfaq01"
            show bfaq bfaq02
            "bfaq bfaq02"
            show bfaq bfaq03
            "bfaq bfaq03"
            show bfaq bfaq04
            "bfaq bfaq04"
            show bfaq bfaq05
            "bfaq bfaq05"

            show bfaq bfaq06
            "bfaq bfaq06"
            show bfaq bfaq07
            "bfaq bfaq07"
            show bfaq bfaq08
            "bfaq bfaq08"
            show bfaq bfaq09
            "bfaq bfaq09"
            show bfaq bfaq09a
            "bfaq bfaq09a"


            show bfaq bfaq10
            "bfaq bfaq10"
            show bfaq bfaq10a
            "bfaq bfaq10a "
            show bfaq bfaq11
            "bfaq bfaq11"
            show bfaq bfaq11a
            "bfaq bfaq11a"

            show bfaq bfaq12
            "bfaq bfaq12"
            show bfaq bfaq13
            "bfaq bfaq13"
            show bfaq bfaq14
            "bfaq bfaq14"
            show bfaq bfaq15
            "bfaq bfaq15"
            show bfaq bfaq16
            "bfaq bfaq16"

            show bfaq bfaq17
            "bfaq bfaq17"
            show bfaq bfaq18
            "bfaq bfaq18"
            show bfaq bfaq19
            "bfaq bfaq19"
            show bfaq bfaq20
            "bfaq bfaq20"

            jump start
        "example scene - phase 1":

            pass
        "example scene - phase 2":

            jump asami_tits_2nd_phase

    b4_tp "Hey Asami, this is Tenzin. Can I get you to come over?"
    "asami" "What? Tenzin? Why?"
    b4_tp "I have a photograph of your father and.... well you better come over because this could effect Future industries."
    "asami" "Then shouldn't you talk to my father instead?"
    b4_tp "Saying more on the phone could be dangerous."
    "asami" "Okay... where are you?"
    b4_tp "Just come to the top of the tower on air temple island."

    "NOTE: I'd imagine tenzin getting the photos from the dumb equalizer guards by accident while he was wearing the amon mask or something."

    "after waiting for half an hour Asami arrives."
    show bfad bfad01
    "asami" "Okay. Let's see this photograph."
    "You show her the photo of her Dad, the owner of Future industries together with Amon."
    show bfad bfad04 with Dissolve(1.5)
    "asami" "This...this can't be!"
    b4_tn "Yeah hard to believe but it looks like your dad's financing a terrorist organisation."
    b4_tn "Man, what's the world coming to."
    "asami" "I'm sure this is tempered with somehow."
    "asami" "Let me have that photo."
    b4_tn "Look asami, I understand this is difficult for you to accept, but we can't just sweep this under the rug."
    "asami" "I could pay you handsomely for it."
    b4_tn "I can't take your money...(wait, why can't I? I love money!)"
    "asami" "Because your position as councilman?"
    "asami" "If unsavory financial ties between Future industries and you would be uncovered...."
    b4_tn "...yes..(I'm taking Tenzin's body for a ride, but I don't want to burn it to the ground.)"
    show bfad bfad02
    "asami" "..okay. Then what? There must be something I can do to change your mind."
    b4_tn "..."
    b4_tn "Suck my co-"
    show bfae meelo_01:
        xpos 300
        linear 1.0 xpos 0
    "Meelo" "Hello pretty lady!"
    "asami" "Uhh, hello?"
    b4_tn "Awh shit! What are you doing here Meelo?!"
    b4_tn "Never mind. I think I just saw Korra getting ready to wash herself. Hint hint."
    "Meelo" "Till we meet again pretty lady!"
    show bfae meelo_01:
        xpos 0
        linear 1.0 xpos 300

    b4_tn "Ahum, it's very very warm here. Don't you agree Asami?"
    "asami" "Not really, why do you.... "
    "asami" "oh.."
    "asami" "Is that how it's going to be."
    b4_tn "Just saying it's warm."
    hide bfad
    show bfaq bfaq07 with Dissolve(1.5)
    b4_tn "What're you doing?"
    "asami" "Like you said, it's warm. I'm just trying to cool off."
    "asami glares at you with enough venom to kill"

    show bfaq bfaq06 at Move((0, 0), (0, -15), .20, bounce=True, repeat=False)
    b4_tn "Oh wow... that's like impressive."
    hide bfaq
    show bfaq bfaq00
    b4_tn "I'd say they're about Korra's size."
    "asami" "I bet you haven't seen them this nice and young for a long time.."
    b4_tn "Hey don't look down on me! I've seen Toph's tits!"
    "asami" "Toph? The police chief's mother? She's ancient!?"
    b4_tn "Uuhhh, I guess that's right."
    b4_tn "Wait...Toph's still alive in this time! Katara probably too!"
    "asami" "Yes they're both still alive.. Are you having an elderly moment?"
    b4_tn "(ooooh fuckkkk... I didn't fully realize it earlier, but I'm posessing the body of Katara's son.)"
    b4_tn "(Wait a minute....who was controlling Aang's body when Katara got pregnant???)"
    b4_tn "(..this could get very complicated.)"
    b4_tn "(...and who exactly is Lin's dad... ohhh shit....)"
    "asami" "You still with me? Do I need to call help?"
    b4_tn "Oh sorry I just got distracted by your chest."
    "asami" "Good."
    "asami" "How about giving me that photograph now? Before that kid comes back?"

    b4_tn "I'm not certain yet. Still feels like I'd be getting rid of important evidence."
    b4_tn "Man that temperature in here though..."


    show bfaq bfaq03:
        xpos 500
        linear 0.3 xpos 520
        linear 0.4 xpos 525

        linear 0.3 xpos 505
        linear 0.4 xpos 500

        repeat
    $ renpy.pause()

    b4_tn "What are-"
    "asami" "Waving some cool fresh air towards you."

    "asami" "Is it refreshing?"
    hide bfaq
    show bfaq bfaq00

    b4_tn "..Yeah... but I'm still feeling hot."
    show bfaq bfaq04
    show bfaq bfaq05:
        ypos 750
        linear 0.5 ypos 720
        linear 0.5 ypos 750
        repeat
    $ renpy.pause()
    b4_tn "Oh wow, that's like really nice."
    b4_tn "But I can't give you the photograph."
    b4_tn "If Amon is aided by someone like your father, the owner of future industries..."
    b4_tn "Well.. that kinda money and state of the art tech could endanger everyone."
    b4_tn "And more importantly, become a major pain in my ass!"
    hide bfaq
    show bfaq bfaq04

    "asami" "Yes and I need that photograph to confront my father and tell him to stop."
    b4_tn "Mmhh tell you what. I've seen enough of Korra's tits to not really be swayed by yours."
    b4_tn "However. If I could get a taste of them...."
    "asami" "You.. want to suck on my nipples?!"
    b4_tn "Unless you'd rather slobber on my cock."
    b4_tn "I'd be okay with that too. Or you could just leave again. Without a photo."

    show bfaq bfaq08 with Dissolve(1.5)
    "asami" "...."
    "asami" "......"
    "asami" "Just do it already."


    show bfaq bfaq09a
    $ renpy.pause()
    "asami" "I despize you.."

    show bfab bfab12 behind bfaq:
        xpos 500
        linear 0.5 xpos 0
    b4_kn "AAhh!!" with hpunch
    b4_kn "What's going on here?!"
    show bfab bfab06
    b4_kn "What are you two doing?!"

    show bfaq bfaq08
    b4_tn "....uh.."
    b4_kn "Meelo was stalking me again so I try to hide from him here and..."
    b4_kn "I see you two doing... this!?"
    "asami" "Tenzin is helping me get rid of a ph.... stress."
    "asami" "Sure it's unconventional, but he can keep a secret and he's great at this particular technique."
    b4_tn "..yes.. chakra's... and stuff..."
    "asami" "That's it."
    b4_tn "Want me to do yours too?"
    show bfab bfab24 with Dissolve(1.5)
    b4_kn "I AM feeling stressed but I'll skip."
    b4_kn "Wait.. that would mean you'd have to stop sucking Asami's...nipples."
    b4_tn "Naturally."
    show bfab bfab26:
        xpos 150 ypos 50
    with Dissolve(1.5)
    b4_kn "Okay then."
    "You can see Korra's nipples hardening as she tries to casually look at Asami's breasts."
    b4_tn "(well I'll be damned....)"
    hide bfab

    show bfaq bfaq10 with Dissolve(1.5)
    show bfad bfad01 behind bfaq
    b4_kn "....soooo Asami...."
    show bfaq bfaq11a
    b4_kn "You do this *ah!* more often?"
    "asami" "Not that often. Like I said it can create misunderstandings."
    b4_kn "..Yeah...of course."

    $ renpy.pause()
    b4_tn "Hmmmm, I can taste you're filled with stress."



    show bfaq bfaq10
    b4_kn "....I certainly feel stressed."


    $ temp_int = 0
    while temp_int != 1:
        menu:
            "asami again":
                scene
                show expression "bk4/backgrounds/korra_room_day.jpg":
                    ypos 0
                show bfab bfab00 behind bfaq
                show bfaq bfaq09a
                $ renpy.pause()
            "korra again":

                scene
                show expression "bk4/backgrounds/korra_room_day.jpg":
                    ypos 0
                show bfad bfad01 behind bfaq
                show bfaq bfaq11a
                $ renpy.pause()
            "done":

                $ temp_int = 1

    scene
    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0
    show bfaq bfaq20 with Dissolve(1.5)
    b4_kn "..mm. maybe you can teach me to do it too..."
    b4_kn "I could start practicing on Asami's.."
    "Asami throws you another ice cold stare."
    b4_tn "...ehh..that feels like too big of a leap at once.."
    b4_tn "But you could start practicing by kissing."
    b4_tn "I guarantee a photogr.., ahum, I mean result if you do that."

    "asami" "*sigh* Have you ever kissed a girl Korra?"
    show bfaq bfaq18 with Dissolve(1.5)
    b4_kn "No.."
    show bfaq bfaq17 with Dissolve(1.5)
    b4_tn "Oh spirits!"

    show bfaq bfaq19:
        xpos 500
        linear 2.0 xpos 510
        linear 2.0 xpos 500
        repeat

    $ renpy.pause()
    b4_tn "Asami, I'm thoroughly convinced you should have that thing we talked about earlier."
    b4_tn "You deserved it."
    hide bfaq
    show bfaq bfaq19
    b4_tn "Damn girl. You're a real go-getter."
    b4_tn "(should I tell her I have enough copies of that photo to fill a longbox?.. Naahh.)"

    show bfaq bfaq10
    show bfad bfad02
    with Dissolve(1.5)
    "asami" "Thanks Tenzin. I have another appointment now, but I'll retreive it later."
    "asami" "Bye Korra."
    b4_kn "Cya!"

    hide bfad with dissolve
    b4_tn "that was...interesting."
    b4_tn "Especially the way you warmed up to the whole experience."
    b4_tn "Did you have fun Korra?"
    hide bfaq
    show bfaq bfaq10a
    with Dissolve(1.5)
    b4_kn "....no..."
    b4_tn "Wow. That's positively the world's worst pokerface ever."
    b4_tn "The Joker would have a better result trying to surpress his smile.."
    b4_kn "I don't know what just happened but I want it to happen more often"
    b4_tn "Well, maybe I can help you out some more in the future with this particular interest of yours."

label asami_tits_2nd_phase:
    scene black
    "SECOND VERSION"
    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0

    b4_tp "Hey Asami, this is Tenzin. Can I get you to come over?"
    "asami" "What? Tenzin? Why?"
    b4_tp "I have a photograph of your father and.... well you better come over because this could effect Future industries."
    "asami" "Did...didn't we already have this conversation?"
    b4_tp "Saying more on the phone could be dangerous."
    "asami" "..... okay. Same place?"
    b4_tp "Yep!"

    "after waiting for half an hour Asami arrives."
    show bfad bfad01

    b4_tn "Did you already talk to your dad about this photo thing?"
    "asami" "... Not yet."
    b4_tn "Does the photo still exist?"
    "asami" "I had an accident and it got burned.."
    b4_tn "Awh.. that's really unfortunate, but luckily I had another copy! (a longbox filled with them)"
    "asami" "...and you like to-"
    b4_tn "See you shake your tits in exchange for the photo."

    show bfad bfad02
    "asami" "..okay."
    show bfae jinora01:
        xpos 300
        linear 1.0 xpos 0
    "jinora" "Hey Asami! I didn't know you were here!"
    "asami" "Ohh, eh Hi."
    "jinora" "Are you looking for Korra?"
    "asami" "Eh.. yeah... that's it."
    "jinora" "I'll go get her for you!"
    "asami" "Thanks but that's really not necessary. "

    "jinora" "Don't worry it's no trouble at all!"
    show bfae jinora01:
        xpos 0
        linear 1.0 xpos 300

    "asami" "So I guess we should do this sometime later?"
    b4_tn "No need, we have enough time before Jinora gets down, finds korra and Korra gets up here."

    b4_tn "Show them titties!"
    hide bfad
    show bfaq bfaq07 with Dissolve(1.5)
    $ renpy.pause(1.0)
    show bfaq bfaq06 at Move((0, 0), (0, -15), .20, bounce=True, repeat=False)
    b4_tn "Oh yeah, still looking nice."
    hide bfaq
    show bfaq bfaq00
    b4_tn "Korra would love this."
    "asami" "I kinda got that the last time. She was pushing that tongue of hers in my mouth with enough force to scare me."
    b4_tn "Yeah she's really not clued in on the whole gentle touch business."
    b4_tn "Well, just be certain you don't start any funny business when I'm not there to supervise you two."
    "asami" "Oh? You get hard from sort of stuff?"
    b4_tn "That and some other reasons."
    b4_tn "Come one move them around."


    show bfaq bfaq03:
        xpos 500
        linear 0.3 xpos 520
        linear 0.4 xpos 525

        linear 0.3 xpos 505
        linear 0.4 xpos 500

        repeat
    $ renpy.pause()

    b4_tn "Yeah..."
    b4_tn "Now make 'em jump go up and down."
    show bfaq bfaq04
    show bfaq bfaq05:
        ypos 750
        linear 0.5 ypos 720
        linear 0.5 ypos 750
        repeat
    $ renpy.pause()
    b4_tn "Oh wow, that's like really nice."

    hide bfaq
    show bfaq bfaq04


    menu:
        "Suck tits":
            b4_tn "Sucking time!"
            show bfaq bfaq08 with Dissolve(1.5)
            $ renpy.pause(1.0)
            show bfaq bfaq09a
            $ renpy.pause()
            "asami" "Hey! Don't bite on it!"
        "Keep jumping":
            show bfaq bfaq05:
                ypos 750
                linear 0.5 ypos 720
                linear 0.5 ypos 750
                repeat




    show bfab bfab12 behind bfaq:
        xpos 500
        linear 0.5 xpos 0

    b4_kn "AAhh!!" with hpunch
    b4_kn "Asami!"

    hide bfaq
    show bfaq bfaq08
    b4_tn "Wow, Jinora works fast."

    b4_kn "Are you guys doing that stress relief thing again?"
    b4_tn "Yeah and you're just in time Korra!"

    show bfab bfab24 with Dissolve(1.5)
    b4_kn "Awesome!"
    b4_kn "Ahum, I mean, great.. good.. nice.."
    b4_tn "First whip out those tits."
    hide bfab
    show bfaq bfaq12
    with Dissolve(1.5)
    b4_tn "Today's warmup consists of some light kissing."

    show bfaq bfaq18 with Dissolve(1.5)
    show bfaq bfaq17 with Dissolve(1.5)
    show bfaq bfaq19 with Dissolve(1.5)
    $ renpy.pause()

    b4_tn "Okay, I want to try something different now."
    show bfaq bfaq18 with Dissolve(1.5)

    b4_tn "Push your nipples against each other repeatedly."
    show bfaq bfaq16
    $ renpy.pause()
    b4_kn "Are we doing it right?"

    b4_tn "Absolutely, but that's enough for today."

    show bfaq bfaq10
    show bfad bfad02
    with Dissolve(1.5)
    "asami" "Thanks Tenzin. I have another appointment now."
    "asami" "Bye Korra."
    hide bfad with Dissolve(1.5)
    b4_kn "Cya!"
    b4_tn "Say, I haven't sucked your tits today have I?"
    b4_kn "That's okay really."
    menu:
        "I insist":
            b4_tn "If not I don't think I can help you train with Asami."
            b4_kn "Please suck on my tits Tenzin!"
            show bfaq bfaq11a
            $ renpy.pause()
            b4_tn "Mmmhhhh."
            show bfaq bfaq10 with Dissolve(1.5)
        "Meh, I don't feel like doing it anyway.":
            pass
    b4_tn "Okay, we're done here "




    jump start





    label lin_buttjob:
        show expression "bk4/backgrounds/police_hq_desk_01.jpg"

        menu:
            "livecomposites":

                show bfap bfap01
                "bfap bfap01"
                show bfap bfap01a
                "bfap bfap01a"
                show bfap bfap02
                "bfap bfap02"
                show bfap bfap03
                "bfap bfap03"
                show bfap bfap03a
                "bfap bfap03a"
                show bfap bfap03b
                "bfap bfap03b"
                show bfap bfap03c
                "bfap bfap03c"
                show bfap bfap03d
                "bfap bfap03d"

                show bfap bfap04
                "bfap bfap04"
                show bfap bfap05
                "bfap bfap05"
                show bfap bfap06a
                "bfap bfap06a"
                show bfap bfap06b
                "bfap bfap06b"
                show bfap bfap07
                "bfap bfap07"
                show bfap bfap08
                "bfap bfap08"

                hide bfap

                show bfap_spermshot
                "bfap_spermshot"
                hide bfap_spermshot

                show bfap_spermshotface
                "bfap_spermshotface"
                hide bfap_spermshotface

                show bfap_dickjack
                "bfap_dickjack "
                hide bfap_dickjack

                show bfap_dickani
                "bfap_dickani"
                hide bfap_dickani

                show bfap_buttani
                "bfap_buttani"
                hide bfap_buttani

                jump start
            "example scene":

                pass

        show bfan bfan01
        b4_tn "Hey, do you know what would be really degrading for me to do?"
        "lin" "What?"
        b4_tn "Having me hump your ass while you're still wearing your uniform!"
        "lin" "...I don't see why that would be degrading.."
        b4_tn "Well, it'd be me acting like a dog."
        "lin" "You {size=+15}ARE{/size} a dog."
        "lin" "Okay, let's give this a try..."
        "lin" "But you better not stain my uniform!"
        b4_tn "It's a deal!"
        b4_tn "Now turn that booty towards me."
        "lin" "I'm only doing this to degrade you! Just so you know."
        b4_tn "Naturally"
        hide bfan
        show bfap bfap01
        with Dissolve(1.5)
        "lin" "Like this?"
        b4_tn "yeah.. that'll do nicely."
        b4_tn "Now I'll just take out my cock and..."
        show bfap bfap01a at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
        b4_tn "put it between your ass-cheeks."
        hide bfap
        show bfap bfap02:
            xpos 0
            linear 0.8 xpos 5
            linear 0.4 xpos 0
            repeat
        b4_tn "hnn.. yeah....can you feel my dick pulsating through the fabric?"
        "lin" "Not really.."
        b4_tn "What?! That's like half the fun! Here lemme fix that."
        hide bfap
        show bfap bfap03b at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
        "You quickly pull down Lin's pants."
        "lin" "{size=+15}Ah!!! What are you doing?!{/size}"
        b4_tn "Just think of it as an extra safety measure so you won't get cum on your uniform."
        b4_tn "Besides, my dick started to chafe! That's some coarse material!"
        show bfap bfap03d at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
        "lin" "I don't care! Don't pull down my pants without even warning me!"
        "lin" "Do something like that again, and your kids can come visit daddy in jail!"
        b4_tn "..You know what? You're right, my bad."


        show bfap bfap03
        "lin" "...Fine... keep going.."
        "lin" "But keep in mind. Another surprise and-"


        b4_tn "Great I just need to quickly do one more thing.."
        show expression "bk4/lin/butjob/spit.png":
            linear 4.0 alpha 0.0 ypos 80
        show bfap bfap03a
        "You spread Lin's ass cheeks and spit, aiming for her anus."
        "Before lin fully realized what you did you quickly start sliding you shaft between her asscheeks."
        hide expression "bk4/lin/butjob/spit.png"

        show bfap bfap04
        b4_tn "This is much, much better. Uh.. I mean this feels really humiliating...."
        b4_tn "You know.. having to slide my dick up against a pretty woman's anus without even getting to enter it.."

        "Lin" "Compliments won't change a thing Tenzin."
        "Lin" "All of this is to torture you."

        "Lin" "Letting you do this, teasing you but never allowing you to go all the way."
        "Lin" "The moment you picked Pema over me you gave up all penetration privileges."
        "Lin" "But beg all you want."
        "Lin" "I like hearing you grovel."
        b4_tn "Aaah, such an honest heart."
        b4_tn "You know... if you go and kneel on you desk I bet it would feel even better for you.."
        show bfap bfap05 with Dissolve(1.5)
        "Without saying anything, but panting heavily, Lin crawls on her desk."
        "Lin" "......"


        b4_tn "You may have some grey hairs, but down there you look as tight as a 20 year old."
        show bfap bfap06b
        "lin" "Pfff, naturally. I bet Pema is all loose and stretched out by now with all those pregnancies."
        "lin" "But that was what you were looking for when you chose her over me, right? A cow to breed your offspring."
        b4_tn "Let's not bring the past into this ({size=-10}because I barely have an idea what happened in Tenzin's past{/size})."
        b4_tn "Why don't you start moving that luscious ass of yours?"

        show bfap bfap07 with Dissolve(1.5)
        $ renpy.pause()
        b4_tn "That's... hmmmm. that's more like it."
        "lin" "It is? Does it make you want to stick that dumb dick of yours in my pussy?"
        "lin" "Or maybe my ass?"
        menu:
            "That'd be very nice.":
                "Lin" "Good. I want you to want it."
                "Lin" "I want you to want it so much you'll be thinking of it when you're fucking that breeding cow of yours."
                "Lin" "Thinking about my tight pussy while going in and out of that throdden down hallway which Pema calls her vagina."
                b4_tn "That sounds a bit... harsh."
                "Lin" "Whatever. My pristine pussy is off limits"
            "Is that an invitation?":

                "Lin" "NO."
                "Lin" "If I said you could, you'd be ballsdeep in my ass before I'd reach the end of the sentence."
                "Lin" "Slammin that cock of yours in so deep I'd have trouble staying on this desk."
                "Lin" "Wouldn't you?"
                b4_tn "I'd make you forget every lonely night you've ever had."


        "Lin" "If you try to cross that line I'm going to take you in for attempted rape and throw you in jail."
        b4_tn "We could play warden and prisoner."
        b4_tn "Besides water and bread you could feed me pussy!"
        "Lin" "More like,I'd throw away the key and forget all about you."
        b4_tn "Hey that reminds me. Wouldn't metalbenders be able to easily escape from your prison?"
        "Lin" "Don't be dumb, they're made out of the purest platinum there is."
        b4_tn "...aah Fuck! I'm gonna cum!"
        b4_tn "Not seeing any tissues yet soooo..."
        b4_tn "Ass or Face?!"


        menu:
            "face":
                b4_tn "Turn around and take it like a professional."
                show bfap bfap09 with Dissolve(1.5)
                show bfap_dickjack
                b4_tx "Ready..AIM.. FIRE!!!"
                show bfap_spermshotface
                show expression "bk4/lin/butjob/spermface1.png" with hpunch
                $ renpy.pause()
                show bfap_spermshotface
                show expression "bk4/lin/butjob/spermface2.png" with hpunch
                $ renpy.pause()
                show bfap_spermshotface
                show expression "bk4/lin/butjob/spermface3.png" with hpunch
                hide bfap_dickjack
                show expression "bk4/lin/butjob/dickjack2.png"
                hide bfap_dickjack
            "ass":

                b4_tn "Raise that ass girl!"
                show bfap bfap08 with Dissolve(1.5)

                show bfap_dickjack
                b4_tx "Here.. it.. COMES!!!"

                show bfap_spermshot
                show expression "bk4/lin/butjob/sperm1.png" with hpunch
                $ renpy.pause()
                show bfap_spermshot
                show expression "bk4/lin/butjob/sperm2.png" with hpunch
                $ renpy.pause()
                show bfap_spermshot
                show expression "bk4/lin/butjob/sperm3.png" with hpunch
                hide bfap_dickjack
                show expression "bk4/lin/butjob/dickjack2.png"
                hide bfap_dickjack

        b4_ts "Wooot!"
        b4_ts "Consider me humiliated!"
        "Lin" "Good!"
        "Lin" "Now get out of here!"




        jump start


label lin_handjob:

    menu:
        "only livecomposites":

            show bfan bfan01
            "bfan bfan01"
            show bfan bfan02
            "bfan bfan02"
            show bfan bfan03
            "bfan bfan03"
            show bfan bfan04
            "bfan bfan04"
            show bfan bfan05
            "bfan bfan05"
            show bfan bfan06
            "bfan bfan06"
            show bfan bfan07
            "bfan bfan07"
            show bfan bfan08
            "bfan bfan08"
            show bfan bfan09
            "bfan bfan09"
            show bfan bfan10
            "bfan bfan10"
            show bfan bfan11
            "bfan bfan11"


            show bfan bfan52
            "bfan bfan52"
            show bfan bfan53
            "bfan bfan53"

            show bfan bfan53a
            "bfan bfan53a"
            show bfan bfan54
            "bfan bfan54"
            show bfan bfan55
            "bfan bfan55"
            show bfan bfan56
            "bfan bfan56"
            show bfan bfan57
            "bfan bfan57"
            show bfan bfan58
            "bfan bfan58"
            show bfan bfan59
            "bfan bfan59"
            show bfan bfan60
            "bfan bfan60"

            jump start
        "example scene":

            pass
    show expression "bk4/backgrounds/police_hq_desk_01.jpg"

    show bfan bfan01
    "lin" "Instead of paying back the damages with money I want you to do a job for me."
    b4_tn "What kind of job?"
    "lin" "A handjob."
    b4_tn "Is that.. a joke?"
    "lin" "Not at all. I want you to do something degrading in front of me."
    "lin" "Or maybe you've become an impotent limpdick incapable of getting hard to start with?"


    show bfan bfan02 with Dissolve(1.5)
    b4_tn "I'd say I'm far from a limpdick."
    "lin" "Pfff, start jacking that dumb cock of yours."

    show bfan bfan03
    b4_tn "Are you certain this is punishment for me and not just... you know.."
    b4_tn "A severe lack in your life you're trying to fill?"
    "lin" "Don't flatter yourself. I'm not the girl you broke up with all those years ago. I'm well over that."
    b4_tn "Whatever you say."
    "lin" "What do you think your wife would have to say about you masturbating in front of his old girlfriend?"
    "lin" "Would she be angry or sad if she'd find out?"
    "lin" "Doesn't that make you feel afraid?"
    b4_tn "Uuuuh.. she might be angry but probably because she wasn't there to watch.. Pema is kinkier than I am."
    b4_tn "And that's saying something!"

    show bfan bfan08
    b4_tn "MMmmmmh.. I'm going to cover that desk of yours with my creamy goodness!"
    show bfan bfan07
    "lin" "What?!? NO!!"
    b4_tn "Almost there!"


    "lin" "Anyone coming into my office will see and smell it!"
    b4_tn "Oh come on. You wanted me to jack off in front of you."
    b4_tn "You can't possibly be surprised about what that entails."

    "lin" "I.. I just sorta didn't think it through.."
    "lin" "It was a spur of the moment thing."
    "lin" "Argh! Fine, I'll deal with your mess like I've always done."
    "lin" "Just give that stupid cock to me damn it!"

    show bfan bfan05
    "Lin grabs your dick and aims it at her open mouth."


    b4_tn "Nice! A little rough, but I can appreciate the effort!"
    b4_tn "Was this your plan from the beginning?"
    "lin" "Don't be an idiot! I just don't want my reputation in the gutter because you can't control yourself."
    b4_tn "....."
    b4_tn "If you're planning on catching it from that distance you'll get it all over your face."
    b4_tn "I'm okay with that."

    show bfan bfan06
    "Lin pushes her lips against the tip of your cock just as you're about to blow your load."


    show bfan bfan06 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
    $ renpy.pause(0.6)
    show bfan bfan06 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
    $ renpy.pause(0.6)
    show bfan bfan06 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
    $ renpy.pause(0.6)
    b4_tn "That's it! Swallow my cum! Swallow it all!"


    show bfan bfan09 with Dissolve(1.5)
    "lin" "Coff! Coff! "
    show bfan bfan11
    show bfan_spermonclothes
    "lin" "Barf!"

    show bfan bfan09 with Dissolve(1.5)
    "lin" "What the fuck is Pema feeding you?!"
    "lin" "It's not normal to have this much sperm! I could barely swallow most of it!"
    show bfan bfan10 with Dissolve(1.5)
    b4_tn "Don't feel sad. You did great!"
    "lin" "Get out of here tenzin. I need a drink to wash away this horrible taste."
    hide bfan_spermonclothes
    hide bfan
    "next visit"

    show bfan bfan01
    "lin" "I want a rematch.."
    "lin" "I'll show you the last time was just a fluke."
    "lin" "I.. I can swallow that cum without a problem. I was just unprepared the last time."
    show bfan bfan51 with Dissolve(1.5)
    "lin" "Just making sure you're not going to ruin my uniform again."
    "lin" "Now start jacking!"
    b4_tn "...okay"
    show bfan bfan52
    b4_tn "Hope you're enjoying this little private show for you."
    "lin" "Can't you go faster? I don't have all day."
    b4_tn "Nah. I want to enjoy this."
    "lin" "Give that to me!"
    show bfan bfan58 with Dissolve(1.5)
    "lin" "I just want you to cum damn it."
    "lin" "Are you already there?!"
    b4_tn "Mmmm... getting closer."
    show bfan bfan53
    "lin" "Tell me when it's time!"

    menu:
        "don't warn her":
            show bfan bfan53a
            show expression "bk4/lin/handjob/blink_front.png":
                xpos 760 ypos 200
            show bfan_spermshot with vpunch:
                xpos 710 ypos 120
            show expression "bk4/lin/handjob/spermonface.png" with Dissolve(1.0)

            "lin" "What?!"
            hide expression "bk4/lin/handjob/spermonface.png"
            hide expression "bk4/lin/handjob/blink_front.png"
            show bfan bfan59
            show expression "bk4/lin/handjob/spermonangryface.png"
            with Dissolve(1.5)
            "lin" "Damn it!!! I told you to warn me!"
            b4_tn "Sorry, It happened too fast for me to say something."
            "lin" "Get out of here Tenzin."
        "Warn her":

            b4_tn "Ready or not.. gonna blow!"
            show bfan bfan54 with Dissolve(1.5)
            show bfan bfan54 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
            $ renpy.pause(0.6)
            show bfan bfan54 at Move((0, 0), (0, 15), .30, bounce=True, repeat=False)
            $ renpy.pause(0.6)

            show bfan bfan55 with Dissolve(1.5)
            "lin" "I think I..."
            show bfan bfan56
            show bfan_spermonclothes
            "lin" "Barf!"
            show bfan bfan57
            "lin" "Wipe that grin off your face. I'll.. I'll show you next time!"
            b4_tn "Lookin forward to it!"
            "lin" "Damn it.. my shirt is all covered with it."
            show bfan bfan60
            hide bfan_spermonclothes
            with Dissolve(1.5)
            "lin" "Get out of here Tenzin."






    jump start


label korra_legs:


    menu:
        "only the composites":
            show bfam bfam01
            "bfam bfam01"
            show bfam bfam02
            "bfam bfam02"
            show bfam bfam03
            "bfam bfam03"
            show bfam bfam04
            "bfam bfam04"
            show bfam bfam05
            "bfam bfam05"
            show bfam bfam06
            "bfam bfam06"
            show bfam bfam07
            "bfam bfam07"
            show bfam bfam08
            "bfam bfam08"
            show bfam bfam09
            "bfam bfam09"
            show bfam bfam10
            "bfam bfam10"

            show bfam bfam11
            "bfam bfam11"
            show bfam bfam12
            "bfam bfam12"
            show bfam bfam13
            "bfam bfam13"
            show bfam bfam14
            "bfam bfam14"
            show bfam bfam15
            "bfam bfam15"

            show bfam bfam15a
            "bfam bfam15a"
            show bfam bfam06
            "bfam bfam16"
            show bfam bfam07
            "bfam bfam17"
            show bfam bfam18
            "bfam bfam18"
            show bfam bfam19
            "bfam bfam19"
            show bfam bfam20
            "bfam bfam20"

            jump start
        "example scene":

            pass

    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos -350

    show bfam bfam01
    $ renpy.pause()
    b4_kn "333.... 334.... 335"



    show bfam bfam02
    b4_kn "Tenzin.."
    show bfam bfam16 with Dissolve(1.5)
    b4_kn "I didn't hear you knock."
    b4_tn "That's because I didn't. You working out? "
    b4_kn "Oh.. yeah.. Nothing special, just some excercises for my thighs."
    b4_tn "They look fine to me."


    b4_kn "Ehh.. thanks? It's just an easy exercise I can do in my room."
    b4_kn "I'd really like to finish the set if you don't mind."
    b4_tn "No problem, go right ahead. I can wait."
    b4_kn "......"
    b4_kn "..... fine."

    show bfam bfam04:
        xpos 500
        linear 0.4 xpos 505
        linear 0.4 xpos 500
        repeat
    $ renpy.pause()
    b4_kn "336.. 337..."

    hide bfam
    show bfam bfam17 with Dissolve(1.5):
        xpos -300
    b4_kn "Pffff!!"
    b4_tn "That's it?"

    show bfam bfam16 with Dissolve(1.5)
    b4_kn "Nah, I still have to do another one."

    show bfam bfam15:
        xpos 250 ypos 30
    b4_kn "First I squat and make sure I'm balanced and then..."
    b4_kn "Oh wait. Probably best to do some stretching for this one."
    hide bfam
    show bfam bfam18
    with Dissolve(1.5)
    b4_kn ".... ehm."

    show bfam bfam20 with Dissolve(1.5)
    b4_kn "That's better."
    b4_kn "Hold it for few seconds... feel the burn and "


    show bfam bfam19 with dissolve
    b4_kn "get back up.."

    show bfam bfam20 with Dissolve(1.5)
    b4_kn "... and repeat."

    show bfam bfam15a with Dissolve(1.5)
    b4_kn "Okay, enough of that."
    b4_kn "Time for the real deal."
    show bfam bfam15 with Dissolve(1.5)





    show bfam bfam14 with dissolve
    $ renpy.pause()
    b4_kn "This.. mpff... is kinda difficult but very effective."


    show bfam bfam15 with Dissolve(1.5)
    b4_kn "You know.. there's really no need to look at me or even stay here."
    b4_tn "Keeping an eye on you is my job. "
    b4_tn "As long as your training isn't finished."
    b4_kn "Trust me, I'm trying to learn airbending with everything I've got."
    b4_tn "Which is why you're doing physical exercises instead of meditation on airbending... or anything else concerning airbending."
    b4_kn "This is important too. A healthy mind in a healthy body."


    show bfam bfam13
    $ renpy.pause()


    show bfam bfam05 with hpunch:
        xzoom 1.0 yzoom 1.0
    b4_kn "Ahhhh!! Oh man... *pant* *pant*"


    show bfam bfam06
    b4_kn "That exercise always takes it out of me."

    show bfam bfam07
    b4_kn "So... what is it you want from me."
    b4_tn "I totally forgot... oh well. Mustn't have been anything important."
    b4_kn "Whatever. I'm going to wash up. I've gotten all sweaty."
    b4_kn "Speaking of which..."
    b4_tn "What?"
    b4_kn "Meelo is always coincidentally hanging around there whenever I enter or come out."
    b4_kn "It's honestly sort of getting on my nerves."
    b4_tn "I'm certain it's just a coincidence."




    jump start



label sidebox_examples:

    b4_senna_n "b4_senna_n"

    b4_yn "b4_yn"
    b4_ya "b4_ya"

    b4_tn "b4_tn"
    b4_ta "b4_ta"
    b4_ts "b4_ts"
    b4_tx "b4_tx"
    b4_tam "b4_tam"
    b4_tp "b4_tp"

    b4_sp "b4_sp"
    b4_cn "b4_cn"

    b4_pn "b4_pn"
    b4_kn "b4_kn"

    b4_eq1 "b4_eq1"
    b4_eq2 "b4_eq2"

    jump start

label equalist_idles:
    show bfal bfal01
    "bfal bfal01"

    show bfal bfal02
    "bfal bfal02"

    show bfal bfal03
    "bfal bfal03"

    show bfal bfal04
    "bfal bfal04"

    show bfal bfal05
    "bfal bfal05"


    jump start

label korra_wash:
    menu:
        "only the livecomposites":
            show bfak bfak01
            "bfak bfak01"
            show bfak bfak02
            "bfak bfak02"
            show bfak bfak03
            "bfak bfak03"
            show bfak bfak04
            "bfak bfak04"
            show bfak bfak04a
            "bfak bfak04a"

            show bfak bfak05
            "bfak bfak05"

            show bfak bfak06
            "bfak bfak06"
            show bfak bfak07
            "bfak bfak07"
            show bfak bfak08
            "bfak bfak08"
            show bfak bfak09
            "bfak bfak09"
            show bfak bfak10
            "bfak bfak10"
            show bfak bfak11
            "bfak bfak11"
            show bfak bfak12
            "bfak bfak12"
            show bfak bfak13
            "bfak bfak13"

            jump start
        "example scene":

            pass
    show expression "bk4/backgrounds/hallway_01.jpg"
    show bfae meelo_03
    "As you walk to throught the building you see Meelo."
    "He's intently staring at something behind a wall scroll."
    b4_tn "Ehhh, what're you doing?"
    show bfae meelo_02 with Dissolve(1.5)
    "Meelo" "Looking for treasure!!"
    b4_tn "....In your nose?"
    "Meelo just stares at you."
    b4_tn "Did you find any treasure yet?"
    "Meelo" "I found some booty!!"
    b4_tn "Ah, that's ... nice."
    hide bfae with dissolve
    "Meelo runs off. Apparantly searching for more treasure."

    b4_tn "Why would he look behind a wall scroll for treasure?"
    b4_tn "Let's see."
    scene black
    "You find a small hole behind the scroll. Peering through it you see-"

    show expression "bk4/backgrounds/bathroom0.jpg"
    show bfak bfak01
    with Dissolve(2.5)


    b4_tn "Damn. There {size=+10}IS{/size} booty here!"
    b4_tn "Hey, she's muttering something to herself.."

    b4_kn "....the fuck are these bathing rooms so... sparse? No baths, no showers.."
    b4_kn "A watertap and a bucket plus some soap?"
    b4_kn "Does this have something to do with the airbender culture thing??"


    show bfak bfak00 as bucket behind bfak:
        xpos 500 ypos 400

    show bfak bfak02
    b4_kn "Guess I'll be scrubbing the old fashioned way"


    show bfak bfak03
    b4_tn "That's right Korra, scrub that watertribe ass of yours while I'm watching."


    show bfak bfak04
    $ renpy.pause()
    show bfae jinora08:
        xpos -50 ypos 100
    with Dissolve(1.5)
    "Hey Korra!"
    b4_ta "Shit! Come on, move over to the left."
    b4_kn "Hey Jinora. Anything the matter?"
    show bfak bfak11

    "I was wondering if you need a towel? I brought an extra one and I've already finished so you can have mine if you want."
    b4_kn "Thanks! I totally forgot to get one."
    "jinore" "No problem."
    "jinora" "..Hmmm I feel a draft coming from somewhere..."
    "jinora" "Well, see you later! Bye Korra!"
    hide bfae jinora08 with Dissolve(1.5)


    b4_kn "Jinora is a pretty nice girl."
    show bfak bfak03
    b4_kn "I bet she could teach me to airbend infinitely better than her dad."

    show bfak bfak04a
    b4_kn "There's something about him which just irks me sometimes."

    show bfak bfak05
    b4_kn "Man, I wish my tits were just a bit smaller."
    $ renpy.pause()


    show bfak bfak06 at Move((0, 0), (0, 30), .40, bounce=True, repeat=False)
    b4_kn "Hmmpf. Hah, I bet there's not a lot of people who can do that from a kneeling position! "
    b4_kn "I'm pretty awesome afteral."
    b4_kn "And now to deal with my smelliest place."

    show bfak bfak07
    $ renpy.pause()

    show bfak bfak10
    b4_kn "sniff sniff. Yeah, that needs a few more strokes."
    show bfak bfak07
    $ renpy.pause()

    hide bfak bfak00 as bucket

    show bfak bfak08
    b4_kn "Now to wash it all of me."



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

    b4_kn "Now where's that towel?"
    b4_kn "Ah there it is."
    show bfak bfak13 with dissolve
    $ renpy.pause(1.0)
    show bfak bfak12
    $ renpy.pause()


    b4_tn "Yeaaah, now turn around and show me that watertribe pussy."
    "Daaaaadd....?"
    "You feel someone tapping you on your shoulder."
    scene black
    show expression "bk4/backgrounds/hallway_01.jpg"
    show bfae jinora04
    with hpunch

    b4_tn "Oh shi.. Hey... Jinora, what's up?"
    "jinora" "What were you doing there?"
    menu:
        "checking for cracks.":
            b4_tn "I.. I was checking for cracks... in the wall."
            b4_tn "Wall cracks. You know making sure the building won't collapse."
            b4_tn "In fact I need to fix this one here."
            "jinora" "Can I take a look at it?"
            b4_tn "What? No! I mean...."
            b4_tn "I'm going to fix this one right now...and I think I saw you're mother looking for you."
            b4_tn "Sooooo.. you better go find her like right now."
            "Jinora is clearly not buying the bullshit you're telling her but leaves anyway."
            hide bfae jinora10 with dissolve
        "None of your business!":

            b4_tn "I'll damn well do what I want without having to explain myself to a ??? years old!"
            show bfae jinora10 at Move((10, 0), (0, 0), .10, bounce=True, repeat=True, delay=.275)
            "jinora" "..I.. I was just asking. You don't have to get all angry."
            hide bfae
            show bfae jinora10:
                xpos 0
                linear 2.0 xpos -1000 alpha 0
            b4_tn "Ahh shit..."






    jump start


label pema_handjob:

    menu:
        "just the pure livecomposites":

            show expression "bk4/backgrounds/bed_tenzin_1.jpg":
                ypos -350


            show bfaj bfaj00
            "bfaj bfaj00"

            show bfaj bfaj01
            "bfaj bfaj01"

            show bfaj bfaj01a
            "bfaj bfaj01a"

            show bfaj bfaj02
            "bfaj bfaj02"

            show bfaj bfaj03
            "bfaj bfaj03"

            show bfaj bfaj04
            "bfaj bfaj04"

            show bfaj bfaj05
            "bfaj bfaj05"



            show bfaj bfaj06
            "bfaj bfaj06"

            show bfaj bfaj07
            "bfaj bfaj07"

            show bfaj bfaj07a
            "bfaj bfaj07a"

            show bfaj bfaj08
            "bfaj bfaj08"

            show bfaj bfaj09
            "bfaj bfaj09"

            show bfaj bfaj10
            "bfaj bfaj10"


            show bfaj bfaj11
            "bfaj bfaj11"

            show bfaj bfaj12
            "bfaj bfaj12"

            show bfaj bfaj13
            "bfaj bfaj13"

            show bfaj bfaj14
            "bfaj bfaj14"

            show bfaj bfaj15
            "bfaj bfaj15"

            show bfaj bfaj16
            "bfaj bfaj16"

            show bfaj bfaj17
            "bfaj bfaj17"

            show bfaj bfaj18
            "bfaj bfaj18"

            show bfaj bfaj19
            "bfaj bfaj19"



            jump start
        "scene example":


            pass

    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        ypos -350

    show bfaj bfaj13
    b4_pn "Hey honey why don't you slip in here with me for a moment. I'm wearing your favorite outfit."

    show bfaj bfaj14
    b4_pn "Nothing."

    b4_tn "Huuuu I can do that."
    "You quickly undress and slide under the sheets next to Pema."


    show bfaj bfaj00
    "Pema rests her head on you shoulder and closes her eyes."

    show bfaj bfaj01 with Dissolve(1.5)
    b4_pn "Ooh I almost fell asleep!"

    show bfaj bfaj01a
    b4_pn "Yaaaawn."



    show bfaj bfaj02
    b4_pn "I sometimes get so tired with three kids and this baby in my belly."
    b4_tn "It's only natural. Don't push yourself."
    b4_pn "Sure, but I can't ignore your needs. You've got an enormous libido."
    b4_pn "Although I'm too tired for a real nice long fuck.... how about.."
    show bfaj bfaj03a
    "Pema reaches under the sheet. Sliding her hand over your belly downwards."
    "When she reaches your dick she grabs it firmly. Giving it short little jerks."

    show bfaj bfaj03
    b4_pn "A nice little handjob to hold you over."
    b4_tn "That's very nice."
    b4_tn "I hope you like messy sheets, because that's what you're going to get."
    b4_pn "I don't!"


    show bfaj bfaj11
    b4_pn "Here, let me take these off. You can try and reach the ceiling when you cum."
    "Pema is just about the throw the sheets off of you when-"

    show bfaj bfaj04
    b4_cn "{size=+30} MOMMM!!!! {/size} " with hpunch
    b4_cn "{size=+30} MOOOOOOOOOOOOOOMM!!!! {/size} " with hpunch

    hide bfaj
    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos 0
    show bfaj bfaj05:
        linear 2.0 ypos 280 xpos 100
    b4_pn "What?!? Whatis it!? Is someone hurt?!"
    b4_pn "Is someone hurt?!"


    show bfae group04 behind bfaj:
        xpos -900
        linear 0.8 xpos 0

    b4_cn "mooom!!! Ikki is being mean!"
    b4_cn "And Meelo is being gross with boogers!"
    show bfae group04 at Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)
    b4_cn "NOT TRUE!"
    b4_cn "Jinora is being a stuck up little-"
    b4_pn "{size=+30} STOP IT! {/size}" with hpunch
    b4_pn "Don't scare me like that! You don't just shout unless it's for a very good reason! "
    b4_pn "{size=+30}Boogers and arguments aren't!{/size}"
    b4_pn "I love all three of you more than life itself. But for the next ten minutes I need some alone time with daddy."
    b4_pn "Go... go feed the skybisons or something!"
    b4_cn "But they've already been-"
    b4_pn "Just ten minutes!!"
    b4_cn "Okkkaaaay!!!"
    show bfae group04:
        linear 0.8 xpos -900

    $ renpy.pause()



    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos -350
    show bfaj bfaj05:
        linear 2.0 ypos 0 xpos 0


    b4_tn "Hmmm that kinda ruined the mood..... and my erection."
    hide bfae with dissolve

    show bfaj bfaj11
    b4_pn "I just bought ourselves ten minutes. I can do wonders in that time."


    show bfaj bfaj06 with Dissolve(1.5)
    b4_pn "Oooh, what's this? Didn't you say your erection was ruined?"
    b4_tn "I did.. but then I looked at those big fat tits of yours and it was cured."

    show bfaj bfaj12
    b4_pn "Is that so?"
    b4_pn "Do you like my big tits? Even after all these years?"
    b4_tn "Time has nothing to do with it. They're big, round and squishy. Hanging under a lovely face. What's not to like?"
    "Pema starts stroking your cock slowly."

    show bfaj bfaj07
    show expression "bk4/pema/handjob/handface.png"
    b4_pn "You've always been quite the charmer."
    $ renpy.pause
    show bfaj bfaj07a
    b4_pn "Hmmm looking at that nice hard long cock of yours.. makes me wonder why there isn't a blue arrow tattooed on it."
    b4_tn "Eeeh, probably because it'd need to be erect for someone to tattoo it."
    b4_tn "And who's going to stay erect when there's needles being pushed in?"
    show bfaj bfaj07
    b4_pn "I can't wait till we have time again for you to push your big \"needle\" into me."
    b4_tn "... I could push it into you right now."
    b4_pn "One of these days when we have enough time and a lock on the bedroom door we will honey."
    b4_pn "Till then you'll just have to be happy with this."
    b4_pn "Aren't you happy with this?"
    b4_tn "Hmm of course I am.."
    b4_pn "Well, I'm pretty sure the kids have no concept of time or privacy so I'll speed things up."
    b4_tn "Speaking of the kids... do you think they knew what we were up to?"
    b4_pn "Meelo, absolutely not. Ikki, I doubt it."
    b4_pn "Jinora, I'm not certain. "
    "Pema suddenly starts speeding up tremendously"
    show bfaj bfaj08a
    b4_tx "ffuuuuuuckkkk"
    show bfaj bfaj08:
        linear 0.8 ypos 0
        ypos 10
        repeat

    b4_tx "HNNnnnnn that's good. That's very good.."
    b4_tx "Hnn..getting close"
    hide bfaj
    hide expression "bk4/pema/handjob/handface.png"

    show bfaj bfaj09

    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve


    pause(0.5)

    show bfaj bfaj09
    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve

    pause(0.5)

    show bfaj bfaj09
    show expression "bk4/pema/handjob/spermshot.png":
        alpha 1.0 xpos 515 ypos 0
        linear 1.0 alpha 0.0
    with vpunch
    show bfaj bfaj10 with dissolve
    b4_ts "That.... was fantastic!"




    show bfaj bfaj17:
        ypos 720
    with Dissolve(1.5)
    b4_pn "One of these days you're going to create a sperm stalagmite on the ceiling."



    show expression "bk4/backgrounds/bed_tenzin_1.jpg":
        linear 2.0 ypos -200
    show bfaj bfaj17:
        ypos 720
        linear 2.0 ypos 920
    b4_pn "Time for me to put some clothes on and deal with whatever the children have been doing."
    b4_pn "....."

    show bfaj bfaj18
    b4_pn "Don't just lie there with a big grin on your face! Move over so I can get out of bed!"
    b4_pn "You're not going to let your pregnant wife crawl all over you are you?"
    b4_tn "Oops sorry."
    "You stand up to give Pema the room to get out of bed."

    scene black
    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0
    show bfaj bfaj19
    with Dissolve(1.5)
    b4_tn "Do I need to do something else?"
    b4_pn "Nope, I can take it from here."
    b4_pn "You just go do your council member stuff and whatever you can to teach Korra some humbleness."







    jump start



label korra_titplay:
    scene white


    menu:
        "only the pure livecomposites":
            show bfai bfai00
            "bfai bfai00"
            show bfai bfai01
            "bfai bfai01"
            show bfai bfai02
            "bfai bfai02"
            show bfai bfai03
            "bfai bfai03"
            show bfai bfai04
            "bfai bfai04"
            show bfai bfai04a
            "bfai bfai04a"
            show bfai bfai04b
            "bfai bfai04b"

            show bfai bfai05
            "bfai bfai05"
            show bfai bfai06
            "bfai bfai06"
            show bfai bfai07
            "bfai bfai07"
            show bfai bfai07a
            "bfai bfai07a"

            show bfai bfai08
            "bfai bfai08"
            show bfai bfai09
            "bfai bfai09"

            jump start
        "examples of more complex movements":

            pass

    show expression "bk4/backgrounds/tower_day_1.jpg":
        ypos 0

    show bfai bfai00
    b4_tn "Okay, let's do a this ancient airbender training session to increase your sensitivity."

    show bfai bfai01
    "bfai bfai01"

    show bfai bfai02
    "bfai bfai02"




    show bfai bfai03:
        xpos 500
        linear 0.9 xpos 510
        linear 0.3 xpos 500
        repeat
    "bfai bfai03"





    show bfai bfai04a:
        xpos 500
        easein 1.0 xpos 450
        linear 0.3 xpos 500
        repeat
    "bfai bfai04a"



    show bfai bfai04:
        xpos 500
        easein 1.0 xpos 550
        linear 0.3 xpos 500
        repeat
    "bfai bfai04"




    show bfai bfai04b:
        xpos 500

        easein 0.8 xpos 550
        linear 0.3 xpos 490
        linear 0.2 xpos 500

        easein 0.8 xpos 450
        linear 0.3 xpos 510
        linear 0.2 xpos 500

        repeat
    "bfai bfai04b"






    show bfai bfai05:
        xpos 500 ypos 720
        linear 1.2 ypos 710
        linear 0.2 ypos 720
        linear 0.2 ypos 730
        pause (0.8)
        repeat
    "bfai bfai05"




    show bfai bfai06:
        xpos 500 ypos 720
        linear 1.2 xpos 520
        linear 1.2 xpos 500
        repeat
    "bfai bfai06"





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

    "bfai bfai07"




    hide bfai_slaphand
    $ temp_int = 0

    menu:
        "give her a few more":


            while temp_int <= 4:
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


    show bfai bfai00
    "bfai bfai00"


    if temp_int > 0:
        show bfai bfai09 with Dissolve(1.5)
        "bfai bfai09"
    else:
        show bfai bfai01 with Dissolve(1.5)

    "You holding up Korra?"
    "korra" "This... this is nothing!"





    jump start



label shady_idles:
    show expression "bk4/backgrounds/alleys_1.jpg":
        ypos 0

    show bfah bfah01
    "bfah bfah01"



    jump start

label korra_rub:

    $ bfag_clothes = True

    show expression "bk4/backgrounds/korra_room_day.jpg":
        ypos 0


    show bfag bfag00
    "bfag bfag00"


    scene black

    show expression "bk4/backgrounds/korra_room_bed.jpg"




    show bfag bfag01 with Dissolve(1.5)
    "bfag bfag01"

    show bfag bfag01a with hpunch
    "bfag bfag01a"



    show bfag bfag05
    "bfag bfag05"

    menu:
        "clothes on":
            $ bfag_clothes = True
            " bfag_clothes = True"
        "clothes off":

            " bfag_clothes = False"

            show bfag bfag12 with dissolve
            $ bfag_clothes = False

            "bfag bfag12"

    show bfag bfag04 with dissolve
    "bfag bfag04"

    show bfag bfag06
    "bfag bfag06"


    show bfag bfag02
    "bfag bfag02"

    show bfag bfag03 with Dissolve(1.5)
    "bfag bfag03"




    show bfag bfag07
    "bfag bfag07"

    show bfag bfag08:
        ypos 720
        linear 0.6 ypos 725
        linear 0.6 ypos 720
        repeat
    "bfag bfag08"

    show bfag bfag09:
        ypos 720
        linear 0.3 ypos 725
        linear 0.3 ypos 720
        repeat
    "bfag bfag09"



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
    "bfag bfag11"


    "Niiice"
    jump start


label korra_kid:

    scene black
    show expression "bk4/painted_lady/pfull.png" with Dissolve(2.0)
    b4_sp "Okay, time for our last trip. Are you ready?"
    b4_yn "Not really. Whose body am I going to possess this time?"
    b4_sp "You'll see."
    b4_yn "Nonono, I want a name and description first."
    b4_sp "Do you like watertribe girls?"
    b4_yn "Yeah, but what has that got to do with..."
    show expression "bk4/painted_lady/pfull.png" at Move((0.0, 0.0), (-0.3, 0.2), 0.4, bounce = True)
    pause(0.5)
    show expression "bk4/painted_lady/pfull.png":
        xzoom 1.0 yzoom 1.0
        linear 3.0 xzoom 0.2 yzoom 0.2 xpos 1000
    b4_sp "And off you go!"
    hide expression "bk4/painted_lady/pfull.png"
    "The spirit gives you a sudden shove and you fly off to a small village."
    b4_ya "Fuuuuuuccccckkk!!!!!"



    show expression "bk4/backgrounds/watertribe_village_1.jpg" with vpunch
    pause(0.5)

    show expression "bk4/korra/chibi/white_lotus.png"
    with Dissolve(1.5)
    "So what makes you think your daughter is the one?"


    b4_senna_n "Uuuuh... what? Are you talking to me? "
    b4_senna_n "Sorry, just give me a second to get my bearings."
    b4_senna_n "Some asshole pushed me... and"
    b4_senna_n "My chest feels heavy and it's like I'm... missing something but I can't put my finger on it."
    b4_senna_n "...Wait a minute... am I a woma-"

    show expression "bk4/backgrounds/watertribe_village_1.jpg" with hpunch
    hide expression "bk4/korra/chibi/white_lotus.png" with Dissolve(1.5)

    b4_senna_n "...What's that sound?"
    show expression "bk4/backgrounds/watertribe_village_1.jpg" with hpunch

    show expression "bk4/backgrounds/watertribe_village_2.jpg":
        ypos 0


    show expression "bk4/korra/chibi/wallpiece.png" at Move((0.0, 0.0), (0.9, 0.9), 0.5 )
    pause(0.5)
    show bfab bfab50 with dissolve
    "I'm the avatar"
    window hide

    show bfab bfab51 at Move((0.0, 0.0), (-0.03, 0.0), 0.3, bounce = True)
    show expression "bk4/korra/chibi/fire.png" at Move((0.4, 0.4), (-0.3, 0.4), 0.8 )
    pause(0.4)
    show bfab bfab52 at Move((0.0, 0.0), (-0.03, 0.0), 0.3, bounce = True)
    show expression "bk4/korra/chibi/fire.png" at Move((0.35, 0.35), (-0.3, 0.4), 0.8 )

    pause (0.8)
    show bfab bfab51 at Move((0.1, 0.0), (0.12, 0.0), 0.3, bounce = True):
        xzoom -1.0
    show expression "bk4/korra/chibi/water.png" at Move((0.5, 0.4), (1.5, 0.4), 0.8 )
    pause(0.4)
    show bfab bfab52 at Move((0.1, 0.0), (0.12, 0.0), 0.3, bounce = True):
        xzoom -1.0
    show expression "bk4/korra/chibi/water.png" at Move((0.5, 0.4), (1.5, 0.4), 0.8 )

    pause (0.8)
    hide bfab
    show bfab bfab50 at Move((0.0, 0.05), (0.0, 0.0), 0.3, bounce = True)
    show expression "bk4/korra/chibi/earth.png" at Move((0.6, 1.0), (0.6, 0.4), 0.8 )
    pause (0.8)

    "You gotta deal with it!"
    hide expression "bk4/korra/chibi/earth.png" with Dissolve(2.0)

    b4_senna_n "Wow, that kid's really...."

    menu:
        "Annoying":
            b4_senna_n "She demolished a wall just so she could show off!?"
            b4_senna_n "Am I the only one who thinks that's not okay?"
            b4_senna_n "....."
            b4_senna_n "Okay... I guess I'll have to be the adult here."
            b4_senna_n "Go get daddy's belt dear.. it's for your own good."
        "Adorable":
            b4_senna_n "Aaawwh! You're such a cutey!"
            b4_senna_n "Come here and give me a hug!"

    show expression "bk4/korra/chibi/white_lotus.png"
    hide bfab
    with Dissolve(1.5)

    "White lotus" "Ahum.. we're convinced she's the avatar."
    b4_senna_n ".... you don't say!!? What tipped you off?"

    b4_senna_n "Wait. There's something more important I have to deal with first."
    b4_senna_n "{size=+30}SPIIRIIIITT!!!!{/size}" with hpunch

    show expression "bk4/painted_lady/pfull.png" with Dissolve(1.5)
    b4_sp "Ooops. Sorry I messed up."
    b4_senna_n "Get me the fuck out of here."
    b4_sp "Sure, sure."
    scene black with Dissolve(2.0)
    show expression "bk4/painted_lady/pfull.png" with Dissolve(2.0)
    b4_ya "What the fuck were you trying to do?"
    b4_sp "I thought I saw the dreamstealer so I wanted to drop you off quickly."
    b4_sp "But my aim was completely off."
    b4_ya "I.. don't believe you."
    b4_sp "Think what you will.."
    b4_sp "I'm really low on energy so we'll have to be more careful with the next try."
    b4_ya "Who was that girl?"
    b4_sp "Avatar korra."
    b4_yn "Oh, so that's why you asked whether I liked watertribe girls. Well I do, but ..."
    b4_yn "Not when they're that young."
    b4_yn "Also...Korra is a bit of an odd choice to teach me airbending."
    b4_yn "As far as I can remember she had a really hard time learning it herself."
    b4_sp " ...uhuh."
    b4_yn "Well she was too young here, so I'm guessing you were at least a decade off with your time travel stuff."
    b4_sp " ...uhuh."
    b4_yn "But that wasn't the only mistake you made...."
    b4_sp "........"
    b4_yn "........."
    b4_ya "You bitch! You were trying to put me in Korra's body!!!" with hpunch
    b4_sp "See!! That's why I didn't say anything! I knew you'd be all touchy about this!"
    b4_ya "I'm NOT going into a girl's body!!"
    b4_yn "I mean.. I will, but not like you want me to!!"
    b4_sp "Why not?!? It's perfect! She already knows water, earth and firebending but knows nothing of airbending!"
    b4_sp "Okay, she needs to be a bit older, but other than..."
    b4_ya " I can't fuck girls without a dick!!"
    b4_sp "Who cares about that?!? You're supposed to learn bending! Not fuck girls!"
    b4_yn "Well, I believe fucking girls is an important part of the experience."
    b4_ya "So..... I'm not letting you genderbend me!!"
    b4_sp "Don't be an ass! We've arrived at the right time. Get into her body willingly and learn airbending!"
    b4_yn "NO!"
    b4_sp "I don't have enough energy for another trip! Do as I say damn it!"
    b4_yn "Make me!"
    b4_sp "You ungrateful piece of... plenty of people would be elated to take over a girl's body!!"
    b4_sp "Think... think of the sick shit you can do with it!"
    b4_ya "Like what?"
    b4_sp "Eeehh... you could take pictures of yourself while doing sex stuff, bury them somewhere only you know of."
    b4_sp "Dig them up again in your own time and sell them for an incredible profit!!"
    b4_yn "That's... that's actually a great idea!"
    b4_ya "Why didn't I think of this before? I could've opened up a back account!"
    b4_yn "Awh shit.... But regardless, no dick no deal."
    b4_sp "... Okay I see I'll have to do this the hard way."
    b4_yn "I like doing it the \"hard\" way.... which is why I need a dick! SO NO FEMALE HOSTS!!!"
    b4_sp "If you resist there's no telling where you'll end up so I suggest you hold veeerrry still."
    "You start performing jumping jacks while sticking out your tongue"
    b4_sp "RAAaah!! You're infuriating! Screws this!"
    show expression "bk4/painted_lady/pfull.png" at Move((0.0, 0.0), (-0.3, 0.2), 0.4, bounce = True)
    pause(0.5)
    show expression "bk4/painted_lady/pfull.png":
        xzoom 1.0 yzoom 1.0
        linear 3.0 xzoom 0.2 yzoom 0.2 xpos 1200
    b4_sp "This is on you avatar! Sink or swim!!"
    b4_ya "Fuckfuckfuck!!"
    "You fly backwards at an alarming speed."
    b4_ya "Pleasenotagirl\n Pleasenotagirl\n Pleasenotagirl\n Pleasenotagirl.."

    show expression "bk4/world_maps/sea_blue.jpg" with Dissolve(1.5)



    show expression "bk4/world_maps/airtemple_solo.png":
        xanchor 0.4 yanchor 0.2 xpos 500 ypos 200 xzoom 0.01 yzoom 0.01

        easeout 7.0 rotate 1100 xzoom 4.0 yzoom 4.0 ypos -600 xpos 0

    $ renpy.pause(1.0, hard = True)
    pause(6.0)

    scene


    show expression "bk4/backgrounds/tenzin_room_day.jpg" at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    pause(1.5)
    scene
    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0

    show bfae jinora01 as kid1 at Move((-1.0, 0.0), (0.0, 0.0), 0.7)
    b4_cn "hey dad! Can you take me to the zoo?"
    show bfae ikki01 as kid2 at Move((-1.0, 0.0), (0.0, 0.0), 0.7)
    b4_cn "I want candy!!"
    show bfae meelo_01 as kid3 at Move((-1.0, 0.0), (0.0, 0.0), 0.7)
    b4_cn "Raaaaawr!!"
    show bfae jinora01 as kid1 at Move((0.0, 0.0), (-0.3, 0.0), 2.0, bounce=True, repeat=True)
    show bfae ikki01 as kid2 at Move((0.0, 0.0), (-0.3, 0.0), 1.0, bounce=True, repeat=True)
    show bfae meelo_01 as kid3 at Move((0.0, 0.0), (-0.3, 0.0), 0.7, bounce=True, repeat=True)
    b4_cn "candy! zoo! Raaawr!!!"
    show bfac bfac01 behind kid1, kid2, kid3 at Move((0.5, 0.0), (0.0, 0.0), 3.0)



    b4_pn "Kids! please calm down."
    b4_cn "CANDY!! ZOOO!!! RAAAWWWR!"



    hide bfac
    show bfac bfac03 behind kid1, kid2, kid3 at Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    hide kid1
    hide kid2
    hide kid3
    show bfae group01 at Move((0.3, 0.0), (-0.1, 0.0), 2.0)

    b4_pn "{size=+10}I said calm the fuck down!!{/size}" with vpunch
    show bfac bfac02
    b4_pn "That's better"
    b4_pn "Now come here and say sorry to your dad."
    show bfae group02 at Move((-0.2, 0.0), (0.0, 0.0), 2.0) with Dissolve(1.5)
    b4_cn "Sorry dad!"
    show bfae group03 at Move((0.0, 0.0), (0.0, 0.0), 2.0)
    b4_pn "That's better."
    b4_pn "Why don't you three go and help with the feeding of the skybisons?"
    b4_cn "Okay mom!"
    hide bfae with Dissolve(1.5)
    b4_pn "Well honey, I've got things to do as well so..."
    b4_pn "You look at the woman in front of you."
    show expression "bk4/backgrounds/tenzin_room_day.jpg" at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    show bfac bfac02 at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    pause(4.0)
    b4_pn "It's been awhile since you gave me that look."
    b4_tn "eeh, what look?"
    b4_pn "The kind which you give me whenever you want to knock me up!"
    b4_tn "That's ... a good thing right?"
    b4_pn " I can only have one baby at a time honey, but like I said I'm busy so hold that thought for later."
    hide bfac with Dissolve(2.0)
    b4_tn "Okaaay. The good news is I didn't lose my memory this time."
    b4_tn "Let's see. I have a dick and judging from the pregnant state of that woman and those kids..."
    b4_tn "It's in perfect working condition. But who am I supposed to be?"
    b4_tn "I got blue arrow tattoos, but.... does that mean I'm in the body of the avatar again?"

    show bfab bfab00 at Move((0.5, 0.0), (0.3, 0.0), 1.0)
    b4_kn "Oh hey Tenzin, Pema told me I could find you here."
    hide bfab
    show bfab bfab01 with Dissolve(1.5)
    b4_kn "Just wondering when we'll proceed with my airbending training."
    b4_tn "You're Korra.... and I'm Tenzin.. "
    b4_tn "I'm supposed to teach you airbending...?"
    show bfab bfab04 with dissolve
    b4_kn "Uuuuuh.. well you are the only airbending master in the world right now so..."
    b4_kn "It's not like I have a whole lot of choice."
    b4_tn "Awwwh shit..."
    show bfab bfab05
    b4_kn "Are you feeling okay Tenzin?"
    b4_tn "Not really. I have a major headache. Can we do this later?"
    show bfab bfab04
    b4_kn "No problem. I have better things to do anyway."
    hide bfab with Dissolve(1.5)
    b4_tn "....Better things to do? Why you little.."
    b4_tn "Spirit, you there?"
    b4_tn "..."
    b4_tn "......"
    b4_tn "........."
    b4_tn "Okay looks like I'm on my own for the time being."
    b4_tn "It's not so bad. I can work with this situation."
    b4_tn "........."
    b4_tn ".........I'm so screwed."
    b4_ta "How the fuck am I going to learn airbending now?!"

    b4_tn " Well at least I'm pretty certain I landed on air temple Island which means I'm in Republic City!"
    b4_ts "The place I call home!"
    b4_tn "Sure it's a republic city from way before I was born, but it's an improvement!"

    jump start



label korra_meditate:

    $ bfaf_clothes = 'full'

    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, 0.0), 0.0)
    show bfab bfab01
    "babalbalab"

    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.5), 1.0)
    show bfab bfab01 at Move((0.0, 0.0), (0.0, -0.5), 1.0)

    $ renpy.pause(2.0)

    hide bfab
    show bfaf bfaf01
    with Dissolve(1.5)
    show expression "bk4/backgrounds/meditation_temple.jpg" at Move((0.0, 0.0), (0.0, -0.5), 0.0)

    "bfaf bfaf01"

    menu:
        "full":
            $ bfaf_clothes = 'full'
        "swimsuit":
            $ bfaf_clothes = 'swimsuit'
        "micro":
            $ bfaf_clothes = 'micro'
        "nude":
            $ bfaf_clothes = 'nude'


    "bfaf bfaf01"

    show bfaf bfaf02 with Dissolve(1.5)
    "bfaf bfaf02"

    show bfaf bfaf03 with Dissolve(1.5)
    "bfaf bfaf03"

    show bfaf bfaf04 with Dissolve(1.5)
    "bfaf bfaf04"

    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap
    "call korra_meditate_repeat_slap \n\nThis is so you don't have to repeat all of the code if you want to repeat slaps during a scene."

    show bfaf bfaf07
    "bfaf bfaf07"

    show bfaf bfaf03
    "bfaf bfaf03"

    show bfaf bfaf08
    "bfaf bfaf08"

    show bfaf bfaf09
    "bfaf bfaf09"

    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_1
    "call korra_meditate_repeat_slap"

    show bfaf bfaf10
    "bfaf bfaf10"

    call korra_meditate_repeat_slap from _call_korra_meditate_repeat_slap_2
    "call korra_meditate_repeat_slap"

    show bfaf bfaf11
    "bfaf bfaf11"

    show bfaf bfaf12
    "bfaf bfaf12"

    jump start


























label linbeifong_idles:

    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0


    show bfaa bfaa00
    "bfaa bfaa00"
    show bfaa bfaa01 with Dissolve(1.5)
    "bfaa bfaa01"
    show bfaa bfaa02 with Dissolve(1.5)
    "bfaa bfaa02"
    show expression "bk4/backgrounds/police_hq_desk.jpg" at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )
    show bfaa bfaa03 at Move((0.0, 0.0), (0.0, -0.5), 4.0,  bounce = True )

    pause(4.0)
    scene
    show expression "bk4/backgrounds/police_hq_desk.jpg":
        ypos 0
    show bfaa bfaa03

    "bfaa bfaa03"
    show bfaa bfaa04 with hpunch
    "bfaa bfaa04"
    show bfaa bfaa05 at Move((0, 0.005), (0, 0.0), 0.1,  delay=1.55)
    "bfaa bfaa05"
    show bfaa bfaa06
    "bfaa bfaa06"
    show bfaa bfaa07
    "bfaa bfaa07"
    show bfaa bfaa08
    "bfaa bfaa08"
    show bfaa bfaa09
    "bfaa bfaa09"
    show bfaa bfaa10
    "bfaa bfaa10"

    jump start

label korra_idles:

    show expression "bk4/backgrounds/training_day_1.jpg":
        ypos 0

    show bfab bfab00
    "bfab bfab00"

    show expression "bk4/backgrounds/training_day_1.jpg" at Move((0.0, 0.0), (0.0, -0.5), 5.0, bounce = True)
    show bfab bfab01 at Move((0.0, 0.0), (0.0, -0.5), 5.0, bounce = True)
    "bfab bfab01"


    hide bfab
    show expression "bk4/backgrounds/training_day_1.jpg":
        ypos 0
    show bfab bfab01


    show bfab bfab02
    "bfab bfab02"
    show bfab bfab03
    "bfab bfab03"
    show bfab bfab04
    "bfab bfab04"
    show bfab bfab05
    "bfab bfab05"
    show bfab bfab06
    "bfab bfab06"
    show bfab bfab07
    "bfab bfab07"
    show bfab bfab08
    "bfab bfab08"
    show bfab bfab09 at Move((0.0, 0.0), (-0.3, 0.0), 0.9)
    "bfab bfab09"
    show bfab bfab10 at Move((-0.3, 0.0), (0.0, 0.0), 1.4) with Dissolve(3.0)
    "bfab bfab10"

    show bfab bfab11 with hpunch
    "bfab bfab11"


    hide bfab

    show bfab bfab12
    "bfab bfab12"
    show bfab bfab12


    show bfab bfab13 at Move((0.0, 0.0), (0.0, -0.5), 5.0 , bounce = True)
    show expression "bk4/backgrounds/training_day_1.jpg" at Move((0.0, 0.0), (0.0, -0.5), 5.0 , bounce = True)
    "bfab bfab13"


    hide bfab
    show expression "bk4/backgrounds/training_day_1.jpg":
        ypos 0


    show bfab bfab14
    "bfab bfab14"

    show bfab bfab15 with Dissolve(1.5)
    "bfab bfab15"


    show bfab bfab16
    "bfab bfab16"

    show bfab bfab17
    "bfab bfab17"

    show bfab bfab18
    "bfab bfab18"

    show bfab bfab19
    "bfab bfab19"

    show bfab bfab20
    "bfab bfab20"

    show bfab bfab21
    "bfab bfab21"

    show bfab bfab22
    "bfab bfab22"

    show bfab bfab23
    "bfab bfab23"

    show bfab bfab24
    "bfab bfab24"

    show bfab bfab25
    "bfab bfab25"

    show bfab bfab26
    "bfab bfab26"
    show bfab bfab27
    "bfab bfab27"
    show bfab bfab28
    "bfab bfab28"
    show bfab bfab29
    "bfab bfab29"


    show bfab bfab50
    "bfab bfab50"

    show bfab bfab51
    "bfab bfab51"




    jump start

label pema_idles:
    show expression "bk4/backgrounds/park_day_1.jpg":
        ypos 0

    show bfac bfac01
    "bfac bfac01"

    show bfac bfac02
    "bfac bfac02"

    show bfac bfac03 at Move((0.01, 0.0), (0.0, 0.0), 0.1,  delay=1.55)
    "bfac bfac03"

    show bfac bfac04
    "bfac bfac04"

    show bfac bfac05
    "bfac bfac05"

    show bfac bfac06
    "bfac bfac06"


    jump start

label asami_idles:
    show expression "bk4/backgrounds/korra_room_day.jpg" at Move((0.0, 0.0), (0.0, 0.0), 0.0)


    show bfad bfad01
    "bfad bfad01"

    show bfad bfad02
    "bfad bfad02"

    show bfad bfad02 at Move((0.0, 0.0), (0.0, -0.5), 2.0,  bounce = True )
    show expression "bk4/backgrounds/korra_room_day.jpg" at Move((0.0, 0.0), (0.0, -0.5), 2.0,  bounce = True )
    "bfad bfad02"

    hide bfad
    show expression "bk4/backgrounds/korra_room_day.jpg" at Move((0.0, 0.0), (0.0, 0.0), 0.0)
    show bfad bfad03 at Move((0.035, 0.0), (0.0, 0.0), 0.1,  delay=1.55)
    "bfad bfad03"

    show bfad bfad04
    "bfad bfad04"

    show bfad bfad05
    "bfad bfad05"

    show bfad bfad06
    "bfad bfad06"

    show bfad bfad07
    "bfad bfad07"

    show bfad bfad07a
    "bfad bfad07a"

    show bfad bfad08
    "bfad bfad08"

    show bfad bfad09
    "bfad bfad09"

    show bfad bfad10
    "bfad bfad10"

    jump start


label meet_the_kids:

    show expression "bk4/backgrounds/tenzin_room_day.jpg":
        ypos 0

    show bfae jinora01
    "bfae jinora01"

    show bfae jinora02
    "bfae jinora02"

    show bfae jinora03
    "bfae jinora03"

    show bfae jinora04
    "bfae jinora04"

    show bfae jinora05
    "bfae jinora05"

    show bfae jinora06
    "bfae jinora06"

    show bfae jinora07
    "bfae jinora07"

    show bfae jinora08
    "bfae jinora08"

    show bfae jinora09
    "bfae jinora09"

    show bfae jinora10
    "bfae jinora10"

    show bfae jinora11
    "bfae jinora11"

    show bfae jinora12
    "bfae jinora12"





    show bfae ikki01
    "bfae ikki01"

    show bfae meelo_01
    "bfae meelo_01"

    show bfae meelo_02
    "bfae meelo_02"

    show bfae meelo_03
    "bfae meelo_03"

    show bfae group01
    "bfae group01"

    show bfae group02
    "bfae group02"

    show bfae group03
    "bfae group03"

    show bfae group04
    "bfae groups04"

    show bfae group05
    "bfae groups05"

    jump start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
