






init python:

    def circle_dragged1(drags, drop):
        
        if not drop:
            return
        
        store.circleprime = drags[0].drag_name
        store.circleprime_1 = drop.drag_name
        
        return True

    def circle_dragged2(drags, drop):
        
        if not drop:
            return
        
        store.circlesecond = drags[0].drag_name
        store.circlesecond_2 = drop.drag_name
        
        return True

image shiny:
    "memory_dreams/circle2.png"
    0.3
    "memory_dreams/circle1.png"
    0.3
    repeat


init:
    $ false_memory2 = False
    $ false_memory3 = False
    $ false_memory4 = False

screen circle_screen2:
    add "memory_dreams/green4.jpg"
    add "memory_dreams/circle4.png" xpos 770 ypos 610








    draggroup:
        if glow ==16:
            drag:
                drag_name "16"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 455 ypos 543
        if glow ==17:
            drag:
                drag_name "17"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 225 ypos 540
        if glow ==7:
            drag:
                drag_name "7"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 700 ypos 580
        if glow ==8:
            drag:
                drag_name "8"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 770 ypos 610
        if glow ==18:
            drag:
                drag_name "18"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 270 ypos 290

        if glow ==19:
            drag:
                drag_name "19"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 890 ypos 260



        if glow ==17:
            drag:
                drag_name "16"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 90 ypos 620
            drag:
                drag_name "18"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 270 ypos 290

        if glow ==18:
            drag:
                drag_name "19"
                child "memory_dreams/rect2.png"
                draggable False
                xpos 140 ypos 3
            drag:
                drag_name "17"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 225 ypos 540
        if glow ==8:
            drag:
                drag_name "7"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 680 ypos 620


screen circle_screen1:

    add "memory_dreams/green1.jpg"
































    draggroup:



        if glow ==1:
            drag:
                drag_name "1"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 455 ypos 543
        if glow ==2:
            drag:
                drag_name "2"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 567 ypos 464
        if glow ==3:
            drag:
                drag_name "3"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 753 ypos 450
        if glow ==4:
            drag:
                drag_name "4"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 650 ypos 350
        if glow ==5:
            drag:
                drag_name "5"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 730 ypos 260

        if glow ==6:
            drag:
                drag_name "6"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 890 ypos 260

        if glow ==7:
            drag:
                drag_name "7"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 650 ypos 115

        if glow ==8:
            drag:
                drag_name "8"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 777 ypos 50

        if glow ==9:
            drag:
                drag_name "9"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 350 ypos 460

        if glow ==10:
            drag:
                drag_name "10"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 234 ypos 512

        if glow ==11:
            drag:
                drag_name "11"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 115 ypos 384

        if glow ==12:
            drag:
                drag_name "12"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 360 ypos 354

        if glow ==13:
            drag:
                drag_name "13"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 180 ypos 266

        if glow ==14:
            drag:
                drag_name "14"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 300 ypos 200

        if glow ==15:
            drag:
                drag_name "15"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 60 ypos 190

        if glow ==16:
            drag:
                drag_name "16"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 90 ypos 80

        if glow ==17:
            drag:
                drag_name "17"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 200 ypos 0


        if glow ==1:
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 460
            drag:
                drag_name "2"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 564 ypos 460
        if glow ==2:
            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 651 ypos 358
            drag:
                drag_name "3"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 753 ypos 450
            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 455 ypos 543
        if glow ==3:
            drag:
                drag_name "2"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 567 ypos 464
        if glow ==4:
            drag:
                drag_name "2"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 567 ypos 464
            drag:
                drag_name "3"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 753 ypos 450
            drag:
                drag_name "5"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 730 ypos 260
        if glow ==5:
            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 651 ypos 358
            drag:
                drag_name "6"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 890 ypos 260
            drag:
                drag_name "7"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 650 ypos 115
        if glow ==6:
            drag:
                drag_name "5"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 730 ypos 260

        if glow ==7:
            drag:
                drag_name "8"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 777 ypos 50
            drag:
                drag_name "5"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 730 ypos 260

        if glow ==8:
            drag:
                drag_name "7"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 650 ypos 115

        if glow ==9:
            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 455 ypos 543

            drag:
                drag_name "10"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 234 ypos 512

            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 360 ypos 354

        if glow ==10:
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 460
            drag:
                drag_name "11"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 115 ypos 384

        if glow ==11:
            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 180 ypos 266

            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 360 ypos 354
        if glow ==12:
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 460

        if glow ==13:
            drag:
                drag_name "14"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 300 ypos 200
            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 360 ypos 354
            drag:
                drag_name "16"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 90 ypos 80

        if glow ==14:
            drag:
                drag_name "15"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 60 ypos 190
            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 180 ypos 266

        if glow ==15:
            drag:
                drag_name "17"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 200 ypos 0

            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 180 ypos 266

        if glow ==16:
            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 180 ypos 266

        if glow ==17:
            drag:
                drag_name "16"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 90 ypos 80

label memorydream1:
    stop music
    play music "audio/Kai_Engel_-_01_-_Take_a_Look_Around_You.mp3"
    "as the fire fades... you fall."
    "you fall for a lifetime."
    "rushing noises surround you, and you eventually feel wind on your face."
    "but... it's not quite wind."
    "closer to... whispers with substance."
    "you begin to drift with them as consciousness returns to you."
    ync "where... what's happening to me?"
    s "your memory is scattered."
    s "you are not safe. we must restore you or there will be no future."
    ync "uh. what."
    ync "i'm asleep, right? gotta be. this is a dream."
    s "you may think of it that way."
    s "but this will be a dream of truth."
    s "we cannot do it all on one night, but we must return you to who you are."
    s "you have forgotten."
    s "you must piece through your scattered memories, destroy those that don't belong, and find the true ones that are buried deeply."
    s "drag yourself from moment to moment to get there."
    s "here we go."
    $ glow = 1
    $ false_memory1 = False
    jump memorydream_map

label memorydream_map:



    call screen circle_screen1

    if glow ==1:
        if circleprime_1 =="2":
            $ glow = 2
        if circleprime_1 =="9":
            $ glow = 9
    if glow ==2:
        if circleprime_1 =="4":
            $ glow = 4
        if circleprime_1 =="3":
            $ glow = 3
        if circleprime_1 =="1":
            $ glow = 1
    if glow ==3:
        if circleprime_1 =="2":
            $ glow =2
    if glow ==4:
        if circleprime_1 =="2":
            $ glow =2
        if circleprime_1 =="3":
            $ glow =3
        if circleprime_1 =="5":
            $ glow =5
    if glow ==5:
        if circleprime_1 =="6":
            $ glow =6
        if circleprime_1 =="7":
            $ glow =7
        if circleprime_1 =="4":
            $ glow =4
    if glow ==6:
        if circleprime_1 =="5":
            $ glow =5
    if glow ==7:
        if circleprime_1 =="5":
            $ glow =5
        if circleprime_1 =="8":
            $ glow =8
    if glow ==8:
        if false_memory1:
            jump memorydream_map2
        else:
            scene green4
            "you found the false memory."
            "you must destroy it to leave."
            menu:
                "destroy":
                    $ false_memory1 = True
                    "false memory destroyed!"
                "not now":

                    "false memory returned."

        jump memorydream_map2
        if circleprime_1 =="7":
            $ glow =7

    if glow ==9:
        if circleprime_1 =="1":
            $ glow =1
        if circleprime_1 =="10":
            $ glow =10
        if circleprime_1 =="12":
            $ glow =12
    if glow ==10:
        if circleprime_1 =="11":
            $ glow =11
        if circleprime_1 =="9":
            $ glow =9
    if glow == 11:
        if circleprime_1 =="13":
            $ glow =13
        if circleprime_1 =="12":
            $ glow =13
    if glow ==12:
        if circleprime_1 =="9":
            $ glow =9
    if glow ==13:
        if circleprime_1 =="14":
            $ glow =14
        if circleprime_1 =="16":
            $ glow =16
        if circleprime_1 =="12":
            $ glow =12
    if glow ==14:
        if circleprime_1 =="13":
            $ glow =13
        if circleprime_1 =="15":
            $ glow =15
    if glow ==15:
        if circleprime_1 =="17":
            $ glow =17
        if circleprime_1 =="13":
            $ glow =13
    if glow ==16:
        if circleprime_1 =="13":
            $ glow =13
    if glow ==17:
        jump memorydream_map2
        if circleprime_1 =="16":
            $ glow =16

    jump memorydream_map



label memorydream_map2:
    hide screen circle_screen1
    call screen circle_screen2

    if glow ==8:
        if circleprime_1 =="7":
            $ glow =7
            jump memorydream_map
    if glow ==17:
        if circleprime_1 =="16":
            $ glow =16
            jump memorydream_map
        if circleprime_1 =="18":
            $ glow =18
    if glow ==18:
        if circleprime_1 =="19":
            $ glow =19
            jump memorydream_map3
        if circleprime_1 =="17":
            $ glow =17
    if glow ==19:
        jump memorydream_map3

    jump memorydream_map2

label memorydream_map3:
    if false_memory1:
        jump after_first_memory_dream
    else:



        s "there is a false memory remaining..."
        $ circleprime_1 ="18"
        $ glow =18
        jump memorydream_map2

screen circle_screen3:

    add "memory_dreams/green2.jpg"
    add "memory_dreams/circle4.png" xpos 870 ypos 390
















    draggroup:



        if glow ==1:
            drag:
                drag_name "1"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 100 ypos 630
        if glow ==2:
            drag:
                drag_name "2"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 225 ypos 545
        if glow ==3:
            drag:
                drag_name "3"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 220 ypos 430
        if glow ==4:
            drag:
                drag_name "4"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 70 ypos 440
        if glow ==5:
            drag:
                drag_name "5"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 20 ypos 330

        if glow ==6:
            drag:
                drag_name "6"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 150 ypos 260

        if glow ==7:
            drag:
                drag_name "7"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 290 ypos 210

        if glow ==8:
            drag:
                drag_name "8"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 430 ypos 150

        if glow ==9:
            drag:
                drag_name "9"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 350 ypos 40

        if glow ==10:
            drag:
                drag_name "10"
                child "memory_dreams/rect2.png"
                droppable False
                dragged circle_dragged1
                xpos 520 ypos 30

        if glow ==11:
            drag:
                drag_name "11"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 680 ypos 560

        if glow ==12:
            drag:
                drag_name "12"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 770 ypos 610

        if glow ==13:
            drag:
                drag_name "13"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 870 ypos 390

        if glow ==14:
            drag:
                drag_name "14"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 800 ypos 285

        if glow ==15:
            drag:
                drag_name "15"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 590 ypos 525



        if glow ==1:
            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 70 ypos 440
            drag:
                drag_name "15"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 590 ypos 525
        if glow ==2:
            drag:
                drag_name "7"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 290 ypos 210
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 40
        if glow ==3:
            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 70 ypos 440
            drag:
                drag_name "6"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 150 ypos 260

        if glow ==4:
            drag:
                drag_name "5"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 20 ypos 330
            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 770 ypos 610

        if glow ==5:
            drag:
                drag_name "3"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 220 ypos 430
            drag:
                drag_name "14"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 800 ypos 285

        if glow ==6:
            drag:
                drag_name "7"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 290 ypos 210
            drag:
                drag_name "15"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 590 ypos 525

        if glow ==7:
            drag:
                drag_name "11"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 680 ypos 560
            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 870 ypos 390

        if glow ==8:
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 40
            drag:
                drag_name "15"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 590 ypos 525

        if glow ==9:

            drag:
                drag_name "10"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 520 ypos 30

            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 70 ypos 440

        if glow ==10:
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 40

        if glow ==11:
            drag:
                drag_name "2"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 225 ypos 545

            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 770 ypos 610

        if glow ==12:
            drag:
                drag_name "6"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 150 ypos 260
            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 70 ypos 440

        if glow ==13:
            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 100 ypos 630
            drag:
                drag_name "5"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 20 ypos 330

        if glow ==14:
            drag:
                drag_name "11"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 680 ypos 560
            drag:
                drag_name "8"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 430 ypos 150

        if glow ==15:
            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 870 ypos 390

            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 770 ypos 610

label second_map:


    call screen circle_screen3

    if glow ==1:
        if circleprime_1 =="4":
            $ glow = 4
        if circleprime_1 =="15":
            $ glow = 15
    if glow ==2:
        if circleprime_1 =="7":
            $ glow = 7
        if circleprime_1 =="9":
            $ glow = 9
    if glow ==3:
        if circleprime_1 =="4":
            $ glow =4
        if circleprime_1 =="6":
            $ glow =6
    if glow ==4:
        if circleprime_1 =="5":
            $ glow =5
        if circleprime_1 =="12":
            $ glow =12
    if glow ==5:
        if circleprime_1 =="3":
            $ glow =3
        if circleprime_1 =="14":
            $ glow =14
    if glow ==6:
        if circleprime_1 =="7":
            $ glow =7
        if circleprime_1 =="15":
            $ glow =15
    if glow ==7:
        if circleprime_1 =="11":
            $ glow =11
        if circleprime_1 =="13":
            $ glow =13
            if false_memory2:
                jump second_map
            else:
                scene green2
                "you found the false memory."
                "you must destroy it to leave."
                menu:
                    "destroy":
                        $ false_memory2 = True
                        "false memory destroyed!"
                        jump second_map
                    "not now":

                        "false memory returned."
                        jump second_map

    if glow ==8:
        if circleprime_1 =="9":
            $ glow =9
        if circleprime_1 =="15":
            $ glow =15
    if glow ==9:
        if circleprime_1 =="10":
            $ glow =10
        if circleprime_1 =="4":
            $ glow =4
    if glow ==10:
        $ glow = 1
        jump second_map2
    if glow == 11:
        if circleprime_1 =="2":
            $ glow =2
        if circleprime_1 =="12":
            $ glow =12
    if glow ==12:
        if circleprime_1 =="6":
            $ glow =6
        if circleprime_1 =="4":
            $ glow =4
    if glow ==13:
        if circleprime_1 =="1":
            $ glow =1
        if circleprime_1 =="5":
            $ glow =5

        jump second_map
    if glow ==14:
        if circleprime_1 =="11":
            $ glow =11
        if circleprime_1 =="8":
            $ glow =8
    if glow ==15:
        if circleprime_1 =="12":
            $ glow =12
        if circleprime_1 =="13":
            $ glow =13
            if false_memory2:
                jump second_map
            else:
                scene green2
                "you found the false memory."
                "you must destroy it to leave."
                menu:
                    "destroy":
                        $ false_memory2 = True
                        "false memory destroyed!"
                        jump second_map
                    "not now":

                        "false memory returned."
                        jump second_map

    jump second_map


screen circle_screen4:

    add "memory_dreams/green4.jpg"

    draggroup:



        if glow ==1:
            drag:
                drag_name "1"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos .5 ypos .5
        if glow ==2:
            drag:
                drag_name "2"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 225 ypos 545

        if glow ==1:
            drag:
                drag_name "3"
                child "memory_dreams/rect2.png"
                draggable False
                xpos 140 ypos 3
            drag:
                drag_name "2"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 225 ypos 545

label second_map2:
    call screen circle_screen4

    if glow ==1:
        if circleprime_1 =="2":
            $ circleprime_1 ="9"
            $ glow = 9
            jump second_map
        if circleprime_1 =="3":
            $ glow = 3
            jump second_map_win

label second_map_win:
    scene green4
    show rect2:
        xpos 140 ypos 3
    jump after_second_dream



screen circle_screen5:

    add "memory_dreams/green3.jpg"

    draggroup:



        if glow ==1:
            drag:
                drag_name "1"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 420 ypos 630
        if glow ==2:
            drag:
                drag_name "2"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 350 ypos 590
        if glow ==3:
            drag:
                drag_name "3"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 520 ypos 585
        if glow ==4:
            drag:
                drag_name "4"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 470 ypos 460
        if glow ==5:
            drag:
                drag_name "5"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 370 ypos 390

        if glow ==6:
            drag:
                drag_name "6"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 475 ypos 375

        if glow ==7:
            drag:
                drag_name "7"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 585 ypos 390

        if glow ==8:
            drag:
                drag_name "8"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 230 ypos 315

        if glow ==9:
            drag:
                drag_name "9"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 470 ypos 300

        if glow ==10:
            drag:
                drag_name "10"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 640 ypos 310

        if glow ==11:
            drag:
                drag_name "11"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 250 ypos 255

        if glow ==12:
            drag:
                drag_name "12"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 470 ypos 225

        if glow ==13:
            drag:
                drag_name "13"
                child "shiny"
                droppable False
                dragged circle_dragged1
                xpos 690 ypos 230


        if glow ==1:
            drag:
                drag_name "5"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 370 ypos 390
            drag:
                drag_name "6"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 475 ypos 375
            drag:
                drag_name "7"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 585 ypos 390

        if glow ==2:
            drag:
                drag_name "4"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 470 ypos 460
            drag:
                drag_name "6"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 475 ypos 375

        if glow ==3:
            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 420 ypos 630
            drag:
                drag_name "11"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 250 ypos 255

        if glow ==4:

            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 420 ypos 630
            drag:
                drag_name "12"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 470 ypos 225

        if glow ==5:
            drag:
                drag_name "3"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 520 ypos 585
            drag:
                drag_name "8"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 230 ypos 315

        if glow ==6:
            drag:
                drag_name "2"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 350 ypos 590
            drag:
                drag_name "9"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 470 ypos 300

        if glow ==7:
            drag:
                drag_name "10"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 640 ypos 310
            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 420 ypos 630

        if glow ==8:
            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 420 ypos 630
            drag:
                drag_name "3"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 520 ypos 585

        if glow ==9:

            drag:
                drag_name "1"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 420 ypos 630

        if glow ==10:
            drag:
                drag_name "13"
                child "memory_dreams/circle3.png"
                draggable False
                xpos 690 ypos 230

        if glow ==11:
            drag:
                drag_name "14"
                child "memory_dreams/rect2.png"
                draggable False
                xpos 155 ypos 64

        if glow ==12:
            drag:
                drag_name "15"
                child "memory_dreams/rect2.png"
                draggable False
                xpos 405 ypos 62

        if glow ==13:
            drag:
                drag_name "16"
                child "memory_dreams/rect2.png"
                draggable False
                xpos 650 ypos 58

label third_map:
    call screen circle_screen5

    if glow ==1:
        if circleprime_1 =="5":
            $ glow = 5
        if circleprime_1 =="6":
            $ glow = 6
        if circleprime_1 =="7":
            $ glow = 7
    if glow ==2:
        if circleprime_1 =="4":
            $ glow = 4
        if circleprime_1 =="6":
            $ glow = 6
    if glow ==3:
        if circleprime_1 =="1":
            $ glow =1
        if circleprime_1 =="11":
            $ glow =11
    if glow ==4:
        if circleprime_1 =="1":
            $ glow =1
        if circleprime_1 =="12":
            $ glow =12
    if glow ==5:
        if circleprime_1 =="3":
            $ glow =3
        if circleprime_1 =="8":
            $ glow =8
    if glow ==6:
        if circleprime_1 =="9":
            $ glow =9
        if circleprime_1 =="2":
            $ glow =2
    if glow ==7:
        if circleprime_1 =="10":
            $ glow =10
        if circleprime_1 =="1":
            $ glow =1

    if glow ==8:
        if circleprime_1 =="1":
            $ glow =1
        if circleprime_1 =="3":
            $ glow =3
    if glow ==9:
        if circleprime_1 =="1":
            $ glow =1
    if glow ==10:
        if circleprime_1 =="13":
            $ glow = 13
    if glow == 11:
        if circleprime_1 =="14":
            $ glow = 14

            $ glow = 1
            if false_memory3:
                "false memory already found."
                jump third_map
            else:
                scene green3
                "you found the false memory."
                "you must destroy it to leave."
                menu:
                    "destroy":
                        $ false_memory3 = True
                        "false memory destroyed!"
                        jump third_map
                    "not now":

                        "false memory returned."
                        jump third_map
    if glow ==12:
        if circleprime_1 =="15":
            $ glow = 15

            if false_memory3 and false_memory4:
                jump third_map2
            if not false_memory3 or not false_memory4:
                "a false memory still remains..."
                $ glow = 1
                jump third_map
    if glow ==13:
        if circleprime_1 =="16":
            $ glow = 16

            $ glow = 1
            if false_memory4:
                "false memory already found."
                jump third_map
            else:
                scene green3
                "you found the false memory."
                "you must destroy it to leave."
                menu:
                    "destroy":
                        $ false_memory4 = True
                        "false memory destroyed!"
                        jump third_map
                    "not now":

                        "false memory returned."
                        jump third_map

    jump third_map

label third_map2:
    show 1kmv2 with flash
    k "you don't remember us fighting together?"
    hide kb3
    y "we... we did?"
    show kan5 with flash
    k "you must remember this?"
    hide 1kmv2
    y "i'm... i'm starting..."
    show kan with dissolve
    y "are... ka... katara?"
    hide kan5
    k "that's *ah!* right!"
    k "we *ngh!* fought that *ah-ha* spirit togther."
    k "don't *ugh* tell me you forgot *ah!* the technique i taught you!"
    y "it's coming back! my... my memories are coming back!"
    show slave_flashback
    hide kan
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    y "it's all...."
    show slave_flashback
    show ctcblink
    $ renpy.pause()
    hide ctcblink
    scene black with Dissolve(1.0)

    jump fourth_ember_day
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
