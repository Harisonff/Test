























screen love_bk3_buildspot:




    imagemap:
        ground "ebackgrounds/village/x_marks_globe.png"
        idle "ebackgrounds/village/x_marks_idle.png"
        hover "ebackgrounds/village/x_marks.png"



        if position_1 == False:
            hotspot (6, 85, 300, 190) action Return(1)
        if position_2 == False:
            hotspot (342, 84, 300, 190) action Return(2)
        if position_3 == False:
            hotspot (675, 80, 300, 190) action Return(3)
        if position_4 == False:
            hotspot (6, 295, 300, 190) action Return(4)
        if position_5 == False:
            hotspot (680, 300, 300, 190) action Return(5)
        if position_6 == False:
            hotspot (5, 519, 300, 190) action Return(6)
        if position_7 == False:
            hotspot (340, 520, 300, 190) action Return(7)
        if position_8 == False:
            hotspot (675, 510, 300, 190) action Return(8)



label love_sector_allocation:


    menu:
        "build":
            menu:
                "store (locked)" if bk3_store_built:
                    "test"

                "store" if not bk3_store_built:
                    if bk3_store_built:
                        "under development."
                        jump sector_allocation
                    if bk3_wood >=5 and bk3_steel >=5:
                        $ shop_building = 1
                        $ bk3_store_built = True
                        $ bk3_wood -=5
                        $ bk3_steel -=5
                        call screen bk3_buildspot
                        if _return == 1:
                            $ shop_building_xpos = 6
                            $ shop_building_ypos = 85
                            $ position_1 = True
                        elif _return == 2:
                            $ shop_building_xpos = 342
                            $ shop_building_ypos = 84
                            $ position_2 = True
                        elif _return == 3:
                            $ shop_building_xpos = 675
                            $ shop_building_ypos = 80
                            $ position_3 = True
                        elif _return == 4:
                            $ shop_building_xpos = 6
                            $ shop_building_ypos = 295
                            $ position_4 = True
                        elif _return == 5:
                            $ shop_building_xpos = 680
                            $ shop_building_ypos = 300
                            $ position_5 = True
                        elif _return == 6:
                            $ shop_building_xpos = 5
                            $ shop_building_ypos = 519
                            $ position_6 = True
                        elif _return == 7:
                            $ shop_building_xpos = 340
                            $ shop_building_ypos = 520
                            $ position_7 = True
                        elif _return == 8:
                            $ shop_building_xpos = 675
                            $ shop_building_ypos = 510
                            $ position_8 = True
                        else:
                            pass
                        $ bk3_day = False
                        jump love_bk3_village_background
                    else:

                        "you need {b}5 wood{/b} and {b}5 steel{/b} to build this!"
                        "you have [bk3_wood] wood and [bk3_steel] steel."
                        jump love_sector_allocation
                "tavern (locked)":

                    if not bk3_store_built:
                        "you need to build a store!"
                        jump love_sector_allocation
                    else:
                        "under development."
                        jump love_bk3_village_background

                "brothel (locked)" if brothel_quest <6 or brothel_building >=1:
                    "not yet available."
                    jump love_sector_allocation

                "brothel" if brothel_quest >=6 and brothel_building <1:
                    if bk3_wood >=5 and bk3_steel >=5:
                        $ brothel_building = 1
                        $ bk3_wood -=5
                        $ bk3_steel -=5
                        call screen love_bk3_buildspot
                        if _return == 1:
                            $ brothel_building_xpos = 6
                            $ brothel_building_ypos = 85
                            $ position_1 = True
                        elif _return == 2:
                            $ brothel_building_xpos = 342
                            $ brothel_building_ypos = 84
                            $ position_2 = True
                        elif _return == 3:
                            $ brothel_building_xpos = 675
                            $ brothel_building_ypos = 80
                            $ position_3 = True
                        elif _return == 4:
                            $ brothel_building_xpos = 5
                            $ brothel_building_ypos = 295
                            $ position_4 = True
                        elif _return == 5:
                            $ brothel_building_xpos = 680
                            $ brothel_building_ypos = 300
                            $ position_5 = True
                        elif _return == 6:
                            $ brothel_building_xpos = 5
                            $ brothel_building_ypos = 519
                            $ position_6 = True
                        elif _return == 7:
                            $ brothel_building_xpos = 340
                            $ brothel_building_ypos = 520
                            $ position_7 = True
                        elif _return == 8:
                            $ brothel_building_xpos = 675
                            $ brothel_building_ypos = 510
                            $ position_8 = True
                        else:
                            pass
                        $ bk3_day = False
                        play sound "audio/construction2.mp3"
                        "you work into the night, building the brothel."
                        jump love_bk3_village_background
                    else:

                        "you need {b}5 wood{/b} and {b}5 steel{/b}."
                        "you have [bk3_wood] wood and [bk3_steel] steel."
                        jump love_bk3_village_background

                "hospital (locked)" if not hospital_build or hospital_built:
                    "test"

                "hospital" if hospital_build and not hospital_built:
                    if bk3_wood >=5 and bk3_steel >=5:
                        $ hospital_building = 1
                        $ hospital_built = True
                        $ bk3_wood -=5
                        $ bk3_steel -=5
                        call screen love_bk3_buildspot
                        if _return == 1:
                            $ hospital_building_xpos = 6
                            $ hospital_building_ypos = 85
                            $ position_1 = True
                        elif _return == 2:
                            $ hospital_building_xpos = 342
                            $ hospital_building_ypos = 84
                            $ position_2 = True
                        elif _return == 3:
                            $ hospital_building_xpos = 675
                            $ hospital_building_ypos = 80
                            $ position_3 = True
                        elif _return == 4:
                            $ hospital_building_xpos = 5
                            $ hospital_building_ypos = 295
                            $ position_4 = True
                        elif _return == 5:
                            $ hospital_building_xpos = 680
                            $ hospital_building_ypos = 300
                            $ position_5 = True
                        elif _return == 6:
                            $ hospital_building_xpos = 5
                            $ hospital_building_ypos = 519
                            $ position_6 = True
                        elif _return == 7:
                            $ hospital_building_xpos = 340
                            $ hospital_building_ypos = 520
                            $ position_7 = True
                        elif _return == 8:
                            $ hospital_building_xpos = 675
                            $ hospital_building_ypos = 510
                            $ position_8 = True
                        else:
                            pass
                        $ bk3_day = False
                        jump love_bk3_village_background
                    else:

                        "you need {b}5 wood{/b} and {b}5 steel{/b}."
                        "you have [bk3_wood] wood and [bk3_steel] steel."
                        jump love_bk3_village_background
                "back":
                    jump love_sector_allocation
        "upgrade":

            menu:
                "house" if jd_free_hospital and avatar_shack <3:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ avatar_shack = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "house (locked)" if not jd_free_hospital and (avatar_shack ==2 or toph_chat <=7):
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ avatar_shack = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "house" if avatar_shack <2 and toph_chat ==8:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ avatar_shack = 2
                        play sound "audio/construction2.mp3"
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "tavern" if tavern_shack ==1 and lovehousefire >=6:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ tavern_shack = 2
                        play sound "audio/construction2.mp3"
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "tavern" if tavern_shack ==2 and love_ty_sex_quest ==1:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ tavern_shack = 3
                        $ love_ty_sex_quest = 2
                        play sound "audio/construction2.mp3"
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "tavern (locked)" if (tavern_shack ==2 and love_ty_sex_quest ==0) or lovehousefire <=5:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ tavern_shack = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "shop (locked)" if shop_building ==2 and not shady_obsidian:
                    "test"

                "shop " if shop_building ==2 and shady_obsidian:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ shop_building = 3
                        play sound "audio/construction2.mp3"
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "shop" if brothel_quest >=4 and shop_building < 2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ shop_building = 2
                        play sound "audio/construction2.mp3"
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "brothel" if love_june_hypno >=1 and brothel_building <2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ brothel_building = 2
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "brothel (locked)" if (brothel_building >=2 and not toph_obsidian_talk) or not love_jin_freed:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ brothel_building = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "boarding house" if brothel_building ==2 and toph_obsidian_talk:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ brothel_building = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "hospital (locked)" if not katara_upgrade_talk and hospital_building == 1:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ hospital_building = 2
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "hospital" if katara_upgrade_talk and hospital_building == 1:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ hospital_building = 2
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "hospital (locked)" if not katara_upgrade_talk2 and hospital_building == 2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ hospital_building = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation

                "hospital" if katara_upgrade_talk2 and hospital_building == 2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ hospital_building = 3
                        jump love_bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade this building!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump love_sector_allocation
                "back":

                    jump love_bk3_village_background
        "back":

            jump love_bk3_village_background







label love_bk3_village_background:
    if earthbending ==30:
        if dressfuck_place == 'home':
            scene basingse_home_zoom
            $ toxk_dress = False
            show toxk toxk00
            with Dissolve(1.5)
        if dressfuck_place == 'palace':
            scene bg_day_tophhome
            $ toxk_dress = False
            show toxk toxk00
            with Dissolve(1.5)

        t "good morning my love."
        t "will you......"
        t "......."
        show toxk toxk07 with Dissolve(1.5)
        t "ohhhh.... yes...."
        show toxk toxk08 with Dissolve(1.5)
        t "Mmm..."
        show toxk toxk01 with Dissolve(1.5)
        t "...fuck me."
        show toxk toxk100
        show ctc
        $ renpy.pause()
        hide ctc
        t "ahh...!"
        t "yes!"
        show ctc
        pause
        hide ctc
        t "more..."
        show toxk toxk101
        show ctc
        pause
        hide ctc

        menu:
            "inside":
                hide toxk

                if dressfuck_place == 'palace':
                    show expression "ebackgrounds/boobjob.jpg"
                else:
                    show expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)

                show toxk toxk15
                with Dissolve(1.5)
                play sound "audio/gltch2b.mp3" 
                show toxk toxk15 with flash
                $ renpy.pause()
                play sound "audio/gltch2b.mp3" 
                show toxk toxk15 with flash
                $ renpy.pause()
                play sound "audio/gltch2b.mp3"   
                show toxk toxk15 with flash
                $ renpy.pause()
                show toxk toxk16



                if toxk_sex == 'anal':
                    show expression "bk3/toph/dressfuck/spermdrip_top_ass.png"
                    with Dissolve(1.5)
                else:
                    show expression "bk3/toph/dressfuck/top_spermdrip.png"
                    with Dissolve(1.5)

                if toxk_sex == 'pussy':
                    t "Did you just give me a creampie?"
                    y "Sure did!"
                else:

                    t "Filling my ass with your cream... you're a real pervert!"
                    t "I love it!"


                y "Now gimme some sugar as a reward."

                if toxk_sex == 'anal':
                    hide expression "bk3/toph/dressfuck/spermdrip_top_ass.png"
                else:
                    hide expression "bk3/toph/dressfuck/top_spermdrip.png"



                show expression "bk3/toph/dressfuck/side_creampie.png"
            "outside":

                hide toxk


                if dressfuck_place == 'palace':
                    show expression "ebackgrounds/boobjob.jpg"
                else:
                    show expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)



                show toxk toxk15
                with Dissolve(1.5)
                $ renpy.pause()
                y "Show me that pretty face of yours Toph!!"
                show toxk toxk16 with Dissolve(1.5)
                play sound "audio/gltch2b.mp3" 
                show expression "bk3/toph/dressfuck/spermout1.png" with flash
                $ renpy.pause()
                play sound "audio/gltch2b.mp3" 
                show expression "bk3/toph/dressfuck/spermout2.png" with flash
                $ renpy.pause()
                play sound "audio/gltch2b.mp3" 
                show expression "bk3/toph/dressfuck/spermout3.png" with flash
                t "mmmm.... warm...."
                $ renpy.pause()
                y "Fuck yeah."
                y "Now gimme some sugar."
                hide expression "bk3/toph/dressfuck/spermout1.png"
                hide expression "bk3/toph/dressfuck/spermout2.png"
                hide expression "bk3/toph/dressfuck/spermout3.png"
                show expression "bk3/toph/dressfuck/spermout4.png"


        hide expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)
        hide expression "ebackgrounds/boobjob.jpg"

        show toxk toxk13
        with Dissolve(1.5)

        play sound "audio/kiss.mp3"
        show toxk toxk13 with pflash
        $ renpy.pause()
        show toxk toxk00 with Dissolve(1.5)
        y "what a wonderful start to the day."
        t "thank you, baby."
        y "no, thank {i}you."
        t "*giggle*"
        t "you're welcome."

        t "now, you have to go to katara's place."
        y "....why?"
        t "she asked me to send you."
        t "she probably needs a fucking, just like i did."
        y "...alright."
        t "good."
        t "now get dressed."
        y "I will, but..."
        y "I have this weird feeling, like... like maybe something's gonna happen."
        t "...i know what you mean."
        y "I want you to know... if this is... for some reason... goodbye..."
        y "that i love you."
        y "and every moment has been the best."
        t "i feel the same."
        t "i'm so glad... we became what we are."
        t "and if this is goodbye... i have no regrets."
        t "thank you for everything."
        y "thank you, my love."
        t "now that that's done... we're probably being silly."
        t "go. get. dressed."
        t "katara is waiting."
        scene black with dissolve
        "with a parting, loving, goodbye kiss, you head to the hospital."
        scene inside_hospital
        jump katara_pregfuck

    if love_toph_freed and earthbending ==28:
        $ earthbending = 29

    $ tophs_home_access = True
    scene black
    show screen earth_money_date
    if caught_peeking:
        $ caught_peeking1 = True
        $ bk3_day = True

    if suki_freed and not suki_love_met:
        $ bk3_day = False

    if avatar_shack == 1 and village_dev_explain:
        if not village_dev_explain1:
            $ bk3_day = False
            $ village_dev_explain1 = True
            scene villagemap_night_base


    if tavern_shack ==1 and bk3_tavern_built:
        if not bk3_tavern_built1:
            $ bk3_tavern_built1 = True
            $ bk3_day = False
            scene villagemap_night_base

    if bk3_day == True:
        stop music fadeout 1
        play music "audio/Bumba Crossing.mp3"
        scene villagemap_day_base
    else:
        stop music fadeout 1
        if lovehousefire >=1 and lovehousefire <=3:
            play music "audio/roaring_fire.mp3"
        else:
            play music "audio/Blue_Dot_Sessions_-_06_-_Night_Light.mp3"
        scene villagemap_night_base



    if position_1 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_1.png"
        else:
            show expression "ebackgrounds/village/roads/road_1_night.png"

    if position_2 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_2.png"
        else:
            show expression "ebackgrounds/village/roads/road_2_night.png"

    if position_3 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_3.png"
        else:
            show expression "ebackgrounds/village/roads/road_3_night.png"

    if position_4 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_4.png"
        else:
            show expression "ebackgrounds/village/roads/road_4_night.png"

    if position_5 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_5.png"
        else:
            show expression "ebackgrounds/village/roads/road_5_night.png"

    if position_6 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_6.png"
        else:
            show expression "ebackgrounds/village/roads/road_6_night.png"

    if position_7 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_7.png"
        else:
            show expression "ebackgrounds/village/roads/road_7_night.png"

    if position_8 == True:
        if bk3_day == True:
            show expression "ebackgrounds/village/roads/road_8.png"
        else:
            show expression "ebackgrounds/village/roads/road_8_night.png"




    if avatar_shack > 0:
        if avatar_shack == 1:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/shack/shack01.png":
                    xpos avatar_shack_xpos ypos avatar_shack_ypos
            else:
                show expression "ebackgrounds/village/buildings/shack/shackn01.png":
                    xpos avatar_shack_xpos ypos avatar_shack_ypos

        if avatar_shack == 2:
            if bk3_day:
                if lovehousefire >=4 and lovehousefire <=5:
                    show expression "ebackgrounds/village/buildings/shack/ruined_shack_day.png":
                        xpos avatar_shack_xpos ypos avatar_shack_ypos
                else:
                    show expression "ebackgrounds/village/buildings/shack/shack02.png":
                        xpos avatar_shack_xpos ypos avatar_shack_ypos
            else:

                if lovehousefire >=1 and lovehousefire <=3:
                    show expression "ebackgrounds/village/buildings/shack/shackn02.png":
                        xpos avatar_shack_xpos ypos avatar_shack_ypos
                    show tocs_fire2:
                        xpos avatar_shack_xpos + 110 ypos avatar_shack_ypos -60

                if lovehousefire >=4 and lovehousefire <=5:
                    show expression "ebackgrounds/village/buildings/shack/ruined_shack_night.png":
                        xpos avatar_shack_xpos ypos avatar_shack_ypos
                else:

                    show expression "ebackgrounds/village/buildings/shack/shackn02.png":
                        xpos avatar_shack_xpos ypos avatar_shack_ypos

        if avatar_shack == 3:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/shack/shack03.png":
                    xpos avatar_shack_xpos ypos avatar_shack_ypos
            else:
                show expression "ebackgrounds/village/buildings/shack/shackn03.png":
                    xpos avatar_shack_xpos ypos avatar_shack_ypos

    if hospital_building > 0:
        if hospital_building == 1:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/hospital/shack01.png":
                    xpos hospital_building_xpos ypos hospital_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/hospital/shackn01.png":
                    xpos hospital_building_xpos ypos hospital_building_ypos

        if hospital_building == 2:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/hospital/shack02.png":
                    xpos hospital_building_xpos ypos hospital_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/hospital/shackn02.png":
                    xpos hospital_building_xpos ypos hospital_building_ypos


        if hospital_building == 3:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/hospital/shack03.png":
                    xpos hospital_building_xpos ypos hospital_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/hospital/shackn03.png":
                    xpos hospital_building_xpos ypos hospital_building_ypos



    if shop_building > 0:
        if shop_building == 1:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/shop/shack01.png":
                    xpos shop_building_xpos ypos shop_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/shop/shackn01.png":
                    xpos shop_building_xpos ypos shop_building_ypos

        if shop_building == 2:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/shop/shack02.png":
                    xpos shop_building_xpos ypos shop_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/shop/shackn02.png":
                    xpos shop_building_xpos ypos shop_building_ypos


        if shop_building == 3:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/shop/shack03.png":
                    xpos shop_building_xpos ypos shop_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/shop/shackn03.png":
                    xpos shop_building_xpos ypos shop_building_ypos

    if tavern_shack > 0:
        if tavern_shack == 1:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/tavern/shack01.png":
                    xpos tavern_shack_xpos ypos tavern_shack_ypos
            else:
                show expression "ebackgrounds/village/buildings/tavern/shackn01.png":
                    xpos tavern_shack_xpos ypos tavern_shack_ypos

        if tavern_shack == 2:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/tavern/shack02.png":
                    xpos tavern_shack_xpos ypos tavern_shack_ypos
            else:
                show expression "ebackgrounds/village/buildings/tavern/shackn02.png":
                    xpos tavern_shack_xpos ypos tavern_shack_ypos


        if tavern_shack == 3:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/tavern/shack03.png":
                    xpos tavern_shack_xpos ypos tavern_shack_ypos
            else:
                show expression "ebackgrounds/village/buildings/tavern/shackn03.png":
                    xpos tavern_shack_xpos ypos tavern_shack_ypos

    if brothel_building > 0:
        if brothel_building == 1:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/brothel/shack01.png":
                    xpos brothel_building_xpos ypos brothel_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/brothel/shackn01.png":
                    xpos brothel_building_xpos ypos brothel_building_ypos

        if brothel_building == 2:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/brothel/shack02.png":
                    xpos brothel_building_xpos ypos brothel_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/brothel/shackn02.png":
                    xpos brothel_building_xpos ypos brothel_building_ypos


        if brothel_building == 3:
            if bk3_day:
                show expression "ebackgrounds/village/buildings/brothel/shack03.png":
                    xpos brothel_building_xpos ypos brothel_building_ypos
            else:
                show expression "ebackgrounds/village/buildings/brothel/shackn03.png":
                    xpos brothel_building_xpos ypos brothel_building_ypos

    with dissolve

    if brothel_building ==3 and not brothel_sign_thought:
        y "....i should really get a new sign."
        y "one that doesn't say \"brothel\"."
        y "....."
        y "oh, well... at least the building's big enough for now."
        $ brothel_sign_thought = True

    if jasmine_raid and not market_raid:
        $ market_raid = True
        show tosi tosi10 with dissolve
        suki "that... wasn't how i wanted that to go."
        y "I'm sorry, i know it was important to you."
        suki "there will be more chances, i suppose."
        suki "thanks for helping me out, aang."
        suki "if you hadn't, i'd have just stayed in and masturbated."
        y "....."
        suki "well, thanks again for your help."
        suki "i'm always in need of a... mmm... helping hand."
        y "a helping hand as in...?"
        suki "goodnight, aang."
        hide tosi with dissolve
        "suki leaves with another little wink."
        y "....huh."
        jump love_bk3_village_background

    if lovehousefire ==6 and not first_shady_delivery:
        $ first_shady_delivery = True
        jump love_rebuild_house2

    if earthbending ==11 and lovehousefire <=5 and not toph_fixhouse:
        show toi toi04 with dissolve
        t "is today the day you fix your house?"
        y "i think so."
        t "great! I know you can do it!"
        hide toi with dissolve
        $ toph_fixhouse = True

    if lovehousefire ==4:
        hide screen earth_money_date
        show toki toki01:
            xpos -250
        show toki_angry:
            xpos -250
        show expression "bk3/katara/idle/idle_sooth_katara.png":
            xpos -250
        show toi toi06
        show expression "bk3/toph/idles/idle_sooth_toph.png"
        with dissolve
        show ctc
        pause
        hide ctc
        "the three of you stand around panting, the fire finally out."
        t "well... it's finally... down..."
        y "yeah... *pant...* at the expense of... *pant...* my house..."
        k3 "i'm sorry... aang..."
        y "what am i... *pant...* going to... *pant...* do?"
        y "someone tried... *pant...* to kill... *pant...* me."
        "you start to regain some of your breath."
        y "i can't believe i don't have a house anymore."
        y "I'm sad about that."
        k3 "well, i'm {i}sorry{/i}, aang, but we did the best we could!"
        t "this wasn't fun for us either."
        y "...take about 20 percent of the top there, guys."
        y "i appreciate your help."
        k3 "sorry..."
        show toki_blink:
            xpos -250
        with dissolve
        k3 "i'm sorry..."
        k3 "I just..."
        k3 "i'm really upset."
        hide toki_blink with dissolve
        k3 "i don't know what i would do if you..."
        k3 "what happened?"
        t "yeah, what happened?"
        y "i woke up to my house on fire, and the door apparently chained from the outside."
        y "you guys know the rest."
        show toi toi05 with dissolve
        t "that's not okay."
        ya "no, it's not."
        ya "and i'm going to make someone pay."
        k3 "who would do this?"
        y "i'm sure it was done on long feng's orders, but..."
        y "...he doesn't seem like a guy that gets his hands dirty."
        y "he'll get what's coming to him, eventually."
        ya "but first, i need to find whoever lit my fucking house on fire."
        k3 "any idea where to start?"
        y "i got some cryptic warnings from a guy... a shady guy."
        y "he mentioned \"fire\", \"smoke\", and \"sleeping\"."
        y "so, i think that's a damn good place a start."
        ya "and i'm going to get some answers."
        k3 "well, at least...."
        hide toki_angry with dissolve
        k3 "...at least we're all okay."
        k3 "look, it's been... a late night for all of us."
        k3 "you can go check out the arena tomorrow, but for tonight you have to stay somewhere."
        k3 "toph?"
        show toi toi09 with dissolve
        t "You can...."
        t "....you can stay with me."
        show toki_blink:
            xpos -250
        with dissolve
        k3 "i think that's for the best."
        hide toki_blink with dissolve
        k3 "I'm going to bed."
        k3 "goodnight."
        hide toki
        hide expression "bk3/katara/idle/idle_sooth_katara.png"
        with dissolve
        y "you sure about this, toph?"
        show toi toi04 with dissolve
        t "yeah."
        t "besides, where else will you sleep?"
        t "come on."
        scene black with dissolve
        "you follow toph back to her house."
        hide screen earth_money_date
        scene black
        scene bg_bk3_tophome_night
        show toi toi09
        show expression "bk3/toph/idles/idle_sooth_toph.png"
        with dissolve
        t "so... i really need a bath."
        y "no kidding."
        show toi toi04 with dissolve
        t "hey, i just saved your butt."
        t "so shut up."
        y "that you did."
        t "now turn around while i rinse off."
        y "aw, do i have-"
        show toi toi05 with dissolve
        t "yes, you have to!"
        y "fine."
        scene black with dissolve
        "you wait while toph hurriedly bathes herself."
        y "......."
        y "................."
        y "are you done yet?"
        t "i..."
        t "...yes, i'm finished."
        scene bg_bk3_tophome_night
        show tocl tocl09
        show tocl_blush
        with dissolve
        show ctc
        pause
        hide ctc
        y "hot damn!"
        show tocl_smile
        hide tocl_blush
        show tocl_blush
        with dissolve
        t "shut up."
        y "I've seen your breasts already, you know."
        t "that's why i'm not still making you face the wall."
        y "come on, just give me a peek."
        hide tocl_smile with dissolve
        t "i don't know..."
        y "what if i said..."
        menu:
            "i'll die without it":
                y "I'm a make-a-wish foundation kid and tonight's my last night."
                t "i don't even know what that is."
                y "i'll die if i don't get to see your boobs!"
                t "i..."
                t "oh, okay..."
            "you're all i want":

                y "you're everything i need."
                t "oh... i..."
                t "well..."
                t "......."
                t "oh, okay..."

        show tocl tocl08
        with dissolve
        t "here."
        show ctc
        pause
        hide ctc
        y "yowza!"
        show tocl tocl09
        show tocl_smile
        hide tocl_blush
        show tocl_blush
        with dissolve
        t "that's all you get!"
        hide tocl_smile with dissolve
        t "i don't know how you convince me to do this sort of thing."
        y "it's because my heart is pure."
        hide tocl_blush
        show tocl_smile
        show tocl_blush
        with dissolve
        t "we {i}both{/i} know that's not true."
        ym "maybe."
        t "alright, is your bedroll set up?"
        y "My... what?"
        hide tocl_smile
        with dissolve
        t "your bedroll."
        t "i think there's a spare around here."
        y "I'm not sleeping with you?"
        show tocl_smile
        hide tocl_blush
        show tocl_blush
        with dissolve
        t "i... don't think that's a good idea."
        ym "(that's a cheeky fucking grin!)"
        hide tocl_smile
        with dissolve
        t "but... we'll be sleeping near each other."
        show tocl_smile
        hide tocl_blush
        show tocl_blush
        with dissolve
        t "hey! looks like we're getting that sleepover after all!"
        t "okay, i'm gonna run to my bed."
        y "you aren't gonna put on any pajamas?"
        t "they're by my bed."
        t "well, some bottoms are."
        t "i usually sleep topless."
        y "oh? and you trust me?"
        hide tocl_smile with dissolve
        t "yes."
        y "...oh."
        y "that's... nice to hear, actually."
        show tocl_smile
        hide tocl_blush
        show tocl_blush
        with dissolve
        t "okay, here i go!"
        t "don't look!"
        ym "wouldn't dream of it."
        scene black with dissolve
        "toph sprints to her bed."
        "you hear her throw on her pajamas and lay down."
        "you can hear her breathing, and you contemplate trying your luck by going over there..."
        "...but she said she trusts you."
        "and it makes you feel... warm."
        "you begin to drift off to sleep, for the second time tonight..."
        "................"
        t "...hey, aang?"
        y "hmm?"
        scene expression "ebackgrounds/boobjob.jpg"
        show tobj tobj05
        show tobj_pants
        show blackveil
        with dissolve
        show ctc
        pause
        hide ctc
        y "what is it?"
        t "do you..."
        t "do you think dreams mean anything?"
        menu:
            "sometimes":
                y "i think they're sometimes true..."
                y "in the sense that they reflect how you feel."
                y "though not always clearly."
                y "like... i think dreaming about sex with someone means you forgive them, that sort of thing."
                y "sort of a pressure-release valve for our subconcious."
            "not usually":

                y "i don't think they're anything more than an emotional release."
                y "wants and fears that our logical mind keep in check get the chance to go crazy."
                y "but i don't think they have any actualy \"truth\" to them."

        show tobj_surprise
        hide blackveil
        show blackveil
        with dissolve
        t "oh."
        y "why?"
        t "just... just wondering."
        y "what kind of dreams are you having?"
        show tobj_unsure
        hide tobj_surprise
        hide blackveil
        show blackveil
        with dissolve
        t "I... don't want to talk about it right now."
        ym "they're about my sexy body, aren't they?"
        hide tobj_unsure
        with dissolve
        t ".....i wish."
        y "hmm?"
        t "nothing."
        y "you can confide in me, you know."
        t "i know, i just..."
        show tobj_blink
        hide blackveil
        show blackveil
        with dissolve
        t "i'm tired."
        t "goodnight, aang."
        y "....."
        scene black with dissolve
        show ctc
        pause
        hide ctc
        t "no!"
        y "whuz... uh...?"
        t "keep back!"
        t "don't!"
        y "...toph?"
        y "are you okay?"
        scene expression "ebackgrounds/boobjob.jpg"
        show tobj tobj04
        show tobj_pants
        show tobj_angry
        show tobj_blink
        show blackveil
        with dissolve
        t "i won't!"
        y "toph, it's okay..."
        y "I'm here. it's okay."
        y "you're dreaming."
        t "I'm... you're..."
        hide tobj_angry with dissolve
        t "wha...."
        hide tobj_blink with dissolve
        t "what...?"
        y "you're dreaming."
        t "what about the box?"
        y "what box?"
        t "you didn't... there wasn't..."
        y "the... box... won't hurt you."
        y "i'm here."
        t "i...."
        show tobj_blink
        hide blackveil
        show blackveil
        with dissolve
        t "........."
        t "*zzzzzzz*"
        "toph falls back to sleep."
        "she seems at peace."
        y "i hope this try sticks..."
        y "i'm so damn tired... i just want to sleep."
        scene black with dissolve
        "you fall asleep immediately."
        show ctc
        pause
        hide ctc
        "it seems like you just hit the pillow, when...."
        t "good morning!"
        scene bg_bk3_tophome_day
        show toi toi02
        with Dissolve(1.5)
        t "it's a beautiful day!"
        y "hurgh..."
        show toi toi09 with dissolve
        t "whoa, you look awful."
        y "I feel like a zombie."
        y "i barely got any sleep last night."
        show toi toi04 with dissolve
        t "really? i slept great!"
        y "did you, now."
        show toi toi07
        show toi_blink
        with dissolve
        t "yeah, i feel better rested than i have in ages."
        y "ugh. i hate morning people."
        hide toi_blink with dissolve
        t "come on, get up."
        y "fine...."
        show toi toi04 with dissolve
        t "you've got a big day ahead of you."
        y "yeah..."
        y "i was hoping it was all a bad dream."
        y "did my house..."
        show toi toi09 with dissolve
        t "burn down?"
        t "yeah. sorry."
        y "well, shit."
        t "let me know if i can help."
        y "*yaaawn...*"
        y "alright, here i go."
        $ lovehousefire = 5

        jump love_bk3_next

    if lovehousefire >=2 and lovehousefire <=3:
        hide screen earth_money_date
        show toi toi01
        show toki toki03:
            xpos -250
        show toki_angry:
            xpos -250
        hide toki_surprised
        with dissolve
        if lovehousefire ==2:
            t "i'm back!"
            t "outta the way!"
        if lovehousefire ==3:
            ya "i'm back!"
            ya "outta the way!"
        k3 "just in time!"
        k3 "aang, help me with this!"
        k3 "we have to keep the fire from spreading!"
        ya "come on, then!"
        ya "toph, put a wall up!"
        ya "contain it!"
        show toi toi51 with dissolve
        t "on it!"
        play sound "audio/earthquake.mp3"
        with sshake
        k3 "with me, aang!"
        scene black with dissolve
        "the three of you work tirelessly throughout the night to douse the fire and keep it from spreading into the village."
        $ lovehousefire = 4
        jump love_bk3_village_background


    if lovehousefire ==1:
        hide screen earth_money_date
        show toi toi10
        show toki toki04:
            xpos -250
        show toki_surprised:
            xpos -250
        with dissolve
        k3 "aang! thank goodness!"
        t "what happened?!"
        k3 "are you okay?!"
        y "where... what..."
        t "we just barely pulled you out of there!"
        y "out of..."
        y "........"
        ya "!!!"
        ya "My house!"
        show ctc
        pause
        hide ctc
        ya "My fucking house is on fucking fire!"
        show toi toi51 with dissolve
        t "we know!"
        t "stop yelling and let's put it out!"
        show toi toi01 with vshake
        t "katara!"
        show toki toki03
        show toki_angry:
            xpos -250
        hide toki_surprised
        with dissolve
        k3 "on it!"
        with vshake
        k3 "rrr....."
        with vshake
        k3 "there's not enough water here!"
        t "aang! quit wasting space and help!"
        y "fuck... i... could have died..."
        t "focus!" with vshake
        y "what?"
        ya "right!"
        ya "sorry! shit!"
        ya "what can i do?"
        t "we need to bring water from the lake for katara to use!"
        t "we'll need to make a basin for the water, just like we practiced."
        t "but one of us has to stay here with katara and try to keep it at bay!"
        t "make the call!"
        menu:
            "stay and stall the fire":
                ya "you go! i'll stay with katara!"
                t "right!"
                $ lovehousefire = 2
            "go and get the water":

                ya "I'll get the water!"
                ya "you stay here with katara!"
                t "right!"
                $ lovehousefire = 3

        k3 "we'll hold out as long as we can!"
        k3 "go!" with vshake
        jump love_house_fire_cont


    if suki_freed and not suki_love_met:
        show tosi tosi01 with dissolve
        suki "thanks for getting me out of there, aang."
        if ajala_headlock_fuckedinass:
            suki "what took you so long?"
            menu:
                "vengeance":
                    y "i was avenging you."
                    suki "...what?"
                    y "i fucked the head guard in the ass."
                    suki "oh."
                    show tosi tosi02 with dissolve
                    suki "thanks!"
                    show tosi tosi03 with dissolve
                    suki "i hope that bitch hated it."
                    y "hey..."
                    show tosi tosi01 with dissolve
                    suki "sorry, no offense meant."
                    suki "and seriously, thank you."
                "lost":

                    y "i got a little lost."
                    suki "really?"
                    suki "it doesn't actually seem that complic-"
                    y "I got lost, okay!?"
                    show tosi_surprise
                    suki "sorry..."
                    hide tosi_surprise with dissolve
                    suki "and seriously, thank you."

        y "you're welcome."
        y "...."
        suki "what?"
        y "where did you get clothes?"
        suki "oh, i beat up a bitch and stole her outfit."
        suki "turns out, it was my outfit that she had stolen from me."
        suki "so... full circle there."
        y "well, that was convenient."
        suki "yeah... but i haven't had a chance to find katara yet."
        y "why not?"
        suki "I was waiting on you."
        suki "actually, i was about to go back in and see if you needed help."
        suki "I am a kyoshi warrior, after all."
        y "alright, well, we're all safe for the time being."
        y "katara's at the hospital, i'll meet you there."
        suki "okay. see you there."
        $ suki_love_met = True
        hide tosi with dissolve

    if earthbending >=6 and not sp_maze_key1:
        t "i can't believe you were ogling me."
        y "i wasn't! you were just naked, what am i supposed-"
        show thankful_girl with dissolve
        girl "av... avatar?"
        y "oh, hey. shop girl, right?"
        y "hey, have i ever told you how much i admire your commitment to nudity?"
        show toi toi09:
            xzoom -1.0
        with dissolve
        t "girl? is there something wrong?"
        girl "i just... wanted to give you something."
        y "what?"
        girl "well... when i was trapped in that... that maze...."
        girl "......."
        girl "..................."
        girl "..................................."

        menu:
            "just tell me already!":
                y "come on, out with it!"
                t "she's shaking, aang."
                y "oh."
                y "my bad."
            "take your time":

                y "whenever you're ready."
                t "she's.... shaking, aang."

        girl "i'm sorry, i just... thought I'd never get out of there."
        girl "but while i was down there, i... i... stole a key."
        y "a key?"
        girl "yes, a guard dropped it, and I thought it might be my way out."
        girl "it didn't work, but maybe there's another door in the tunnels that you can use it on?"
        girl "i hope it comes in handy."
        play sound "audio/win2.mp3"
        $ sp_maze_key1 = True
        "you got a key!"
        y "......"
        y "....you have fat tits."
        girl "i know!"
        hide thankful_girl with dissolve
        y "....i like her."
        y "but where was she hiding that?"
        t "i'm sure you'll think on it."
        y "yeah, right, you're totally projecting."
        t "...what?"
        y "i know you have a boob fetish."
        t "i don't... you can't... that's..."
        t "....."
        t "shut up."
        hide toi toi09 with dissolve
        y "heh."
        scene black with dissolve
        "you head home for the night."
        jump love_bk3_next

    if caught_peeking:
        yc "ow...."
        y "that little tart knocked me out!"
        y "...."
        y "at least I'm well rested..."
        $ caught_peeking = False
        $ caught_peeking1 = False
        jump love_bk3_next











    call screen love_bk3_village_pick




screen love_bk3_village_pick:



    imagemap:
        ground "ebackgrounds/village/earth_village_pick_idle.png"
        hover "ebackgrounds/village/earth_village_pick.png"







        if avatar_shack > 0 and avatar_shack_access:
            hotspot (avatar_shack_xpos, avatar_shack_ypos, 300, 190) clicked Jump("love_inside_avatar_shack")

        if hospital_building > 0 and hospital_building_access:
            hotspot (hospital_building_xpos, hospital_building_ypos, 300, 190) clicked Jump("love_inside_hospital_building")

        if shop_building > 0 and shop_building_access:
            hotspot (shop_building_xpos, shop_building_ypos, 300, 190) clicked Jump("love_inside_shop_building")

        if tophs_home > 0 and tophs_home_access:
            hotspot (340, 290, 300, 190) clicked Jump("love_inside_tophs_home")

        if tavern_shack > 0 and tavern_shack_access:
            hotspot (tavern_shack_xpos, tavern_shack_ypos, 300, 190) clicked Jump("love_inside_tavern_shack")

        if brothel_building > 0 and brothel_building_access:
            hotspot (brothel_building_xpos, brothel_building_ypos, 300, 190) clicked Jump("love_inside_brothel_building")

        if bk3_day and bk3_village_access:
            imagebutton idle "bk3/icons/bk3_basingse_off.png" hover "bk3/icons/bk3_basingse_on.png" xpos 0.25 ypos 0 action Jump("love_basingse_day1")




        if village_store_build:
            imagebutton idle "bk3/icons/build_icon_off.png" hover "bk3/icons/build_icon_on.png" xpos 0.77 ypos 0 action Jump("love_sector_allocation")

        if bk3_day and laogai_travel:
            imagebutton idle "bk3/icons/bk3_maze_off.png" hover "bk3/icons/bk3_maze_on.png" xpos 0.18 ypos 0 action Jump("love_bk3_maze_start1")

        add "emberisland_cloud1"


label love_inside_avatar_shack:
    if earthbending ==25 and not bk3_day:
        scene black
        scene inside_shack
        with dissolve
        y "i'll just wait for toph and katara to get here."
        y "...."
        y ".........."
        t "hey!"
        t "let me in!"
        y "well, that's toph..."
        show toi toi04 with dissolve
        t "thanks."
        t "your place isn't bad."
        t "i'm not here very often."
        t "i should stay over more."
        y "i agree."

        show toki toki01:
            xzoom -1
        with dissolve
        k3 "hello?"
        show toi toi10
        show toi_blush
        with dissolve
        t "h-hey... katara!"
        k3 "hello, toph."
        t "you're... dressed normally."
        t "right?"
        k3 "haha... yes."
        t "cool. that's cool."
        y "...oh my god that's adorable."
        t "what?"
        y "you're crushing so hard on her!"
        show toi toi05 with dissolve
        t "no i'm not!"
        show toki_smile:
            xzoom -1
        with dissolve
        k3 "that's wonderful!"
        t "stop it!"
        y "relax, cutie."
        t "but i'm not-"
        play sound "audio/kiss.mp3"
        show pink with dissolve
        "with a sudden flourish, katara surprises toph with a full kiss on the mouth."
        t "hey!"
        hide pink
        show toi toi09
        with dissolve
        t "what was that!"
        k3 "that was me liking you."
        k3 "it's okay."
        t "but i... don't..."
        y "we're all super close friends here, toph."
        y "it's cool."
        t "umm...."
        t "this is..."
        t "this is so uncomfortable."
        t "can we... talk about something else?"
        k3 "are you nervous?"
        show toi toi05 with dissolve
        t "i just don't see why we need to keep talking about this!"
        y "alright, alright, let's talk about something else."
        show toi toi09 with dissolve
        t "finally...."
        hide screen earth_money_date
        show black
        with fade
        "the three of you spend the night talking about hopes and adventures..."
        "you end up laughing and teasing one another..."
        "and daring each other to strip..."

        scene black with Dissolve(1)
        jump katara_toph_scissor

    if lovehousefire ==5:
        if earthbending >=11:
            if bk3_day:
                menu:
                    "rebuild your house":
                        jump love_rebuild_house
                    "exit":

                        jump love_bk3_village_background
            else:

                y "I should come back during the day and work on it."
                jump love_bk3_village_background
        else:
            y "just ruins...."
            y "...."
            y "....I think the remains of my bed are still smoldering."
            jump love_bk3_village_background

    scene black
    scene inside_shack

    if jd_house and jd_house_addressed:
        show toji toji14
    with Dissolve(0.2)
    if jd_house and jd_house_addressed:
        if not jd_love_chat:
            $ randgreet = 0
            $ randgreet = renpy.random.randint(1,5)
            if randgreet ==1:
                jd "welcome home, sir!"
            if randgreet ==2:
                jd "put your feet up and relax, sir."
            if randgreet ==3:
                jd "please let me know if you need anything at all, sir."
            if randgreet ==4:
                jd "you're looking very sexy today, sir."
            if randgreet ==5:
                if jd_break_hypno ==5:
                    jd "I'm always ready to be pounded, sir."
                else:
                    jd "welcome home, sir!"


    if jd_house and not jd_house_addressed:
        $ jd_house_addressed = True
        show jd_nude with dissolve
        jd "you called for me?"
        jd "have you added a bedroom?"
        y "I have."
        jd "that's wonderful!"
        jd "do you have clothes for me as well?"
        y "i do, but... i could only find one outfit."
        y "I think it'll be appropriate though."
        y "here."
        jd "oh... this looks... revealing..."
        y "it's less revealing than what you're currently wearing."
        jd "that's... true..."
        y "go put it on."
        jd "okay..."
        hide jd_nude with dissolve
        show ctc
        pause
        hide ctc
        jd "umm...."
        y "yes?"
        jd "okay, here i come...."
        show toji toji15 with dissolve
        show ctc
        pause
        hide ctc
        y "sexy!"
        jd "...."
        show toji toji14 with dissolve
        jd "you really think i'm... sexy?"
        show ctc
        pause
        hide ctc
        y "definitely."
        show toji toji15 with dissolve
        jd "you're so sweet, master."
        show toji toji14 with dissolve
        jd "er... young master, i meant to say."
        y "...sure you did."
        y "anyway, like i said before, you'll need to keep this place tidy and earn your keep."
        y "so go clean my room."
        show toji toji12 with dissolve
        jd "with pleasure!"
        jd "thank you so much!"
        show toji toji11 with dissolve
        jd "would you like food to be ready when you return?"
        y "that'd be lovely."
        jd "okay!"
        jd "i'll take care of it!"


    menu:
        "sleep" if not bk3_day:
            $ jd_love_chat = False
            jump love_bk3_next

        "wait until night" if bk3_day:
            $ bk3_day = False
            $ jd_love_chat = False
            jump love_bk3_village_background
        "threesome scissor" if earthbending ==26 or earthbending >28:
            jump katara_toph_scissor
        "chat with joo dee" if jd_house:
            $ jd_love_chat = True
            if love_toph_sex:
                if jd_break_hypno ==5:
                    show toji toji12 with dissolve
                    jd "thank you for letting me cook and clean for you!"
                    show toji toji14 with dissolve
                    jd "please let me know if you need anything."
                    show toji toji15 with dissolve
                    jd "anything at all."
                    menu:
                        "fuck her":
                            y "what i need, is your juicy pussy, joo dee."
                            jd "oh, thank you, sir!"
                            scene black with dissolve
                            scene hypno_room2
                            show toji toji14
                            with dissolve
                            jump jd_full_nelson
                        "back":
                            jump love_inside_avatar_shack
                if jd_break_hypno ==4:
                    jd "hello, sir!"
                    jd "will you join me for a moment in your anti-hypnosis room?"
                    menu:
                        "sure":
                            y "alright."
                            scene black with dissolve
                            scene hypno_room2
                            show toji toji14
                            with dissolve
                            jump jd_full_nelson
                        "later":

                            y "not now."
                            jd "very well."
                            jump love_inside_avatar_shack
                if jd_break_hypno ==3:
                    y "alright, i've set up the equipment."
                    y "want to get to it?"
                    jd "very much so!"
                    $ jd_break_hypno = 4
                    jump love_hypnosis_room
                if jd_break_hypno ==2:
                    y "hey, i figured out what i need to do to make the equipment work better."
                    jd "that's wonderful!"
                    y "i'll let you know when it's finished."
                    jd "thank you!"
                    jump love_inside_avatar_shack
                if jd_break_hypno ==1:
                    jd "have you set up the anti-hypnosis equipment?"
                    y "not yet."
                    y "I have to find somebody to help me."
                    jd "okay, just let me know."
                    jump love_inside_avatar_shack
                if jd_break_hypno ==0:
                    jd "avatar...?"
                    y "yes?"
                    jd "i want to thank you for... taking me in."
                    y "not a problem."
                    show toji toji15 with dissolve
                    jd "but..."
                    y "but?"
                    show toji toji14
                    show jd_idle_surprise
                    with dissolve
                    jd "i'm nervous about being hypnotized again."
                    hide jd_idle_surprise with dissolve
                    jd "do you think you could fully break my hypnosis?"
                    y "....."
                    y "maybe."
                    show jd_idle_surprise with dissolve
                    jd "really?!"
                    y "don't get your hopes up too much."
                    show toji toji12
                    hide jd_idle_surprise
                    with dissolve
                    jd "sorry..."
                    y "my best guess is that i'll have to jury-rig the equipment somehow..."
                    y "it's just really not built to undo hypnosis so much as make it happen."
                    show toji toji14 with dissolve
                    jd "i... understand."
                    jd "whatever you can do."
                    y "well, i'll give it a try."
                    y "i wonder if there's someone that can help me with this..."
                    jd "just let me know when you want me to sit in there."
                    y "sure thing."
                    $ jd_break_hypno = 1
                    jump love_inside_avatar_shack
            else:
                show toji toji12 with dissolve
                jd "thank you for letting me cook and clean for you!"
                show toji toji14 with dissolve
                jd "please let me know if you need anything."
                show toji toji15 with dissolve
                jd "anything at all."
                jump love_inside_avatar_shack
        "look at pornlove" if b3love_pornlove1_own:
            if jd_house:
                y "I'd like to look at some porn, joo dee."
                jd "oh my..."
                jd "well, how about i fetch it for you?"
                jd "you relax, i'll bring you your porn."
                hide toji with dissolve
                y "...."
                show toji toji14 with dissolve
                jd "here you go!"

            y "let's enjoy some vintage porn!"
            y "this chick must be ancient by now."
            hide screen earth_money_date
            show pornlove_old_1 with dissolve
            show ctc
            pause
            hide ctc
            "this is hama."
            show ctc
            pause
            hide ctc
            show pornlove_old_2
            hide pornlove_old_1
            with dissolve
            show ctc
            pause
            hide ctc
            "hama understands her place...."
            "she knows there's only one way for her to leave prison...."
            "....and that's to be willing."
            show ctc
            pause
            hide ctc
            hide pornlove_old_2
            show pornlove_old_3
            with dissolve
            show ctc
            pause
            hide ctc
            "hama earns her freedom."
            show ctc
            pause
            hide ctc
            hide pornlove_old_3
            with dissolve
            jump love_inside_avatar_shack

        "extra room" if not suki_lantern_explain:
            if avatar_shack >=2:
                $ jd_love_chat = False
                jump love_hypnosis_room
            if avatar_shack <2:
                "your house isn't big enough for this!"
                jump love_inside_avatar_shack

        "anti-hypnosis room" if suki_lantern_explain:
            $ jd_love_chat = False
            jump love_hypnosis_room
        "exit":

            $ jd_love_chat = False
            jump love_bk3_village_background


label love_inside_hospital_building:
    if earthbending ==24:
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3" 
        scene black
        scene inside_hospital
        show toki toki01
        with dissolve
        k3 "oh, just who i wanted to see."
        k3 "i'll see you at toph's during the day."
        jump love_bk3_village_background

    if earthbending ==23 and love_toph_anal2:
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3" 
        scene black
        scene inside_hospital
        show toki toki01
        with dissolve
        k3 "oh, just who i wanted to see."
        y "why?"
        k3 "well, i was thinking..."
        k3 "you want to get toph okay with you and i have sex, right?"
        y "ideally."
        k3 "well... what if we convince her to a threesome first?"
        k3 "open her mind a bit?"
        y "you think you can do that?"
        k3 "i think that together we can."
        k3 "i'm gonna get dressed up and smelling nice and i'll go over to toph's."
        k3 "Meet me there?"
        y "i mean... okay... but you do know she can't see you, right?"
        k3 "the persona, the body language that comes from wearing the outfit, the smells of perfume and makeup..."
        k3 "...they all go into creating external beauty."
        k3 "it takes the whole of-"
        y "okay, okay, i get it."
        y "stop monologuing at me."
        k3 "...."
        y "i'll see you at toph's, okay?"
        k3 "sounds good, aang."
        $ earthbending = 24
        jump love_bk3_village_background

    if katara_lonely ==5 or katara_lonely ==6:
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3" 
        scene black
        scene inside_hospital
        show toki toki01
        show toki_blink
        with dissolve
        y "...katara?"
        hide toki_blink with dissolve
        k3 "yes?"
        k3 "oh, hello, aang."
        y "I... got you something."
        show toki_smile with dissolve
        k3 "you did?"
        y "um. sort of."
        y "here."
        if katara_lonely ==5:
            show stick:
                xalign .4 yalign .4
            with dissolve
            "you hand her the stick."
            hide stick with dissolve
            hide toki_smile
            with dissolve
            k3 "......"
            y "it's, uh, like a flower."
            k3 "...."
            y "...that's dead."
            k3 "......"
            y "without the flower."
            k3 ".........."
            k3 ".................."
            show toki_smile with dissolve
            k3 "ha...."
            k3 "haha....."
            k3 "hahahaha!"
            show toki_blink with dissolve
            k3 "hahahahahahaha!"
            k3 "a flower... but dead... without the... hahahaha!"
            hide toki_blink with dissolve
            k3 "i love it."
            k3 "thank you."

        if katara_lonely ==6:
            y "I got you a flower."
            k3 "....."
            y "well, it's a plant."
            k3 "....."
            y "well... it's {i}from{/i} a plant."
            k3 "...."
            y "it's fruit."
            y "it's old fruit."
            hide toki_smile with dissolve
            y "......"
            k3 "......."
            y "........."
            y "it's an old partially-squished melon i beat up."
            show melon_head:
                xalign .4 yalign .4
            with dissolve
            "you hand her the melon."
            hide melon_head with dissolve
            hide toki_smile
            with dissolve
            k3 "......"
            k3 "............"
            show toki_smile with dissolve
            k3 "ha...."
            k3 "haha....."
            k3 "hahahaha!"
            show toki_blink with dissolve
            k3 "hahahahahahaha!"
            k3 "like a flower... but a plant... fruit that's... hahahaha!"
            hide toki_blink with dissolve
            k3 "i love it."
            k3 "thank you."

        k3 "i love that you went to all that trouble and worry for me."
        k3 "you're clearly anxious about it."
        k3 "it's a truly wonderful gift, because it's from you."
        play sound "audio/kiss.mp3"
        show toki_blink
        hide toki_smile
        with pflash
        "katara gives you a light kiss."
        hide toki_blink with dissolve
        k3 "thank you."
        k3 "hey...."
        k3 "i know you're very busy, and probably aren't interested, but..."
        k3 "i'd love to spend some time with you out somewhere."
        k3 "let me know if you have some time."
        y "okay, i will."
        k3 "bye, handsome."
        show toki_smile with dissolve
        k3 "and thanks again for the... flower."
        k3 "hahaha...!"
        y "any time."
        $ katara_lonely = 7
        jump love_bk3_village_background

    if katara_lonely ==3:
        y "looks like toph is in there with katara."
        y "should i listen?"
        jump t_k_eavesdrop

    if katara_lonely ==2:
        $ katara_lonely = 3
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3" 
        scene black
        scene inside_hospital
        show toki toki02
        show toki_angry
        show toki_blink
        with dissolve
        k3 "*sniff... sniff...*"
        y "katara?"
        hide toki_blink with dissolve
        k3 "wha..."
        show toki_surprised with dissolve
        k3 "aang!"
        k3 "how long have you been standing there?"
        y "I just arrived."
        y "are you okay?"
        hide toki_surprised
        hide toki_angry
        with dissolve
        k3 "yeah, i'm fine."
        k3 "what..."
        show toki_blink
        with dissolve
        k3 "*sniff*..."
        hide toki_blink with dissolve
        k3 "what do you need?"
        y "were you crying?"
        hide toki_blink with dissolve
        k3 "no, of course not."
        k3 "there's just some dust or something in here."
        k3 "don't worry about me."
        k3 "did you need something?"
        y "i was just-"
        show toi toi02:
            xzoom -1
        with moveinleft
        t "hey, katara! i-"
        show toi toi09 with dissolve
        t "aang?"
        t "oh, um, am i interrupting?"
        y "maybe-"
        k3 "no, of course not."
        k3 "in fact i'm glad you're here, thanks for coming over."
        t "you told me there'd be snacks..."
        k3 "and there are!"
        k3 "i need to talk with toph, aang."
        k3 "i'll see you later."
        y "but-"
        k3 "scoot!"
        y "oh, fine..."
        scene black with dissolve
        "you step outside and they close the door."
        y "....."
        y "I wonder what they're talking about?"
        jump t_k_eavesdrop

        label t_k_eavesdrop:
            menu:
                "eavesdrop":
                    scene inside_hospital
                    show toki toki01
                    show katara_lookleft
                    show toi toi04:
                        xzoom -1 xpos 250
                    show windowlickscene
                    t "so what's..."
                    t "hey, were you crying?"
                    k3 "no, why?"
                    t "your eyes are just a little..."
                    k3 "i'm fine."
                    k3 "let's talk about you!"
                    show toi toi09 with dissolve
                    t "okay..."
                    k3 "how are you and aang?"
                    show toi toi04 with dissolve
                    t "we're still fine."
                    t "you ask me about that a lot."
                    k3 "i'm just interested in you guys working out."
                    k3 "he's a truly wonderful guy, and any girl would be lucky to have him."
                    t "yeah, i know."
                    t "i guess it helps hearing it from someone else though..."
                    t "it's not like i have any relationships to compare it to."
                    k3 "what are besties for?"
                    t "well... since we're talking about this..."
                    k3 "yes?"
                    t "what do you think about... butt play?"
                    k3 "ah... well..."
                    k3 "it's just another hole, isn't it?"
                    k3 "pretty much all our holes were made to fit penises."
                    t "you think?"
                    k3 "of course."
                    k3 "each one provides a unique sensation."
                    k3 "that way your man never gets tired of you."
                    t "i guess that makes sense..."
                    t "and i definitely don't want him to be bored with me."
                    t "i've never really put anything up... there... before, but..."
                    t "i'm really interested in it."
                    k3 "oh?"
                    t "yeah, i've only put a finger in my butt before, and it was... tight."
                    t "it felt reaaally good, and was excitingly... forbidden, somehow."
                    t "it was very filling, and fun, but..."
                    t "...his cock is just so big, katara."
                    k3 "i know."
                    t "....."
                    t "okay...."
                    t "moving past that...."
                    t "what do you think i should do?"
                    k3 "what does your gut say?"
                    t "well, my {i}guts{/i} want his thick cock in them."
                    show toi_blush:
                        xzoom -1 xpos 250
                    hide windowlickscene
                    show windowlickscene
                    with dissolve
                    t "...sorry to be graphic about it."
                    k3 "haha, it's fine!"
                    k3 "i'd say follow your instincts."
                    t "he's really surprising, you know."
                    k3 "he is."
                    t "especially sexually!"
                    t "how does he know so much?"
                    k3 "......"
                    t "being with him is... it's just thrilling!"
                    k3 "i... imagine it would be."
                    k3 "you're very lucky."
                    k3 "you seem very happy with him."
                    t "i am!"
                    k3 "well, you should... you should try to keep that going."
                    t "i'm definitely going to try."
                    t "hey, i should go."
                    k3 "okay."
                    t "see you later!"
                    hide toi_blush
                    hide toi
                    show black
                    with dissolve
                    "you watch toph leave."
                    hide black
                    show toki_blink
                    hide windowlickscene
                    show windowlickscene
                    with dissolve
                    k3 "*sniff...*"
                    k3 "oh, aang..."
                    y "(is she crying again?)"
                    k3 "i want to... i want to help, but... it's so hard..."
                    k3 "i just miss you so much... i want to make you happy..."
                    k3 "i want... i want you to have toph to your heart's content... but it's..."
                    k3 "it's so hard for me... no... no, katara, stop it."
                    k3 "what if he came in and saw me crying?"
                    k3 "i only deserve what i can get."
                    k3 "he deserves everything."
                    k3 "he's facing so many challenges... i have to be his rock."
                    k3 "i have to give him what he needs."
                    k3 "if he needs a lover... or a mother... oh spirits, i just want him to be happy, but..."
                    k3 "don't i deserve to be happy, too?"
                    k3 "stop it, katara!"
                    k3 "right... right."
                    k3 "no more of this."
                    k3 "*sniff*"
                    k3 "aaand..."
                    show toki_smile
                    hide toki_blink
                    show toki_blink
                    hide windowlickscene
                    show windowlickscene
                    with dissolve
                    k3 "happy face!"
                    k3 "i'll... i'll go see how many health potions i have in stock."
                    hide toki_blink
                    hide toki_smile
                    hide katara_lookleft
                    hide toki
                    with dissolve
                    y "......"
                    y "shit..."
                    y "katara is... i really don't deserve her."
                    y "she's really struggling."
                    y "she's beautiful, intelligent, kind..."
                    y "i need to do something for her."
                    y "maybe i should get her a gift?"
                    y "yeah, i'll get her something."
                    $ katara_lonely = 4
                "leave":

                    $ katara_lonely = 3

            jump love_bk3_village_background

    if love_suki_hypno ==2:
        y "i should meet katara at the tavern."
        jump love_bk3_village_background

    stop music
    play music "audio/Komiku_-_10_-_Something_to_save.mp3" 
    scene black
    scene inside_hospital
    show toki toki01
    with dissolve

    if jd_free_hospital and not jd_house:
        if avatar_shack <3 or not jd_maid_outfit:
            y "hey katara."
            k3 "hello!"
            k3 "joo dee is still here, by the way."
            y "i know."
            y "i still need to upgrade my house and buy her some clothes."
        else:
            y "I've got everything i need for joo dee."
            y "can you send her to my house?"
            k3 "sure."
            y "thanks, i'll meet her there."
            $ jd_house = True
    if jd_free and not jd_free_hospital:
        $ jd_free_hospital = True
        k3 "aang, did you send a nude lady here?"
        y "almost usually."
        k3 "joo dee, come on out."
        show jd_nude:
            xzoom -1
        with dissolve
        jd "um... hello."
        jd "thank you for rescuing me, young master."
        y "it was my pleasure."
        k3 "she's in good shape, but she'll need a place to stay, obviously."
        y "of course."
        y "katara... can you give us a moment?"
        k3 "sure."
        hide toki with dissolve
        hide jd_nude with dissolve
        show jd_nude with dissolve
        jd "yes?"
        y "what happened?"
        y "you disappeared before i could come back and apologize..."
        jd "after you broke my hypnosis, i was no longer useful to long feng."
        show jd_idle_surprise with dissolve
        jd "he repossessed my house and all my accounts, and removed me from society."
        jd "he imprisoned me, but... he's done greater damage than that."
        jd "he's left me homeless, poor, and unable to work."
        jd "i have nothing to offer and no way to survive..."
        y "unfortunately, the boarding house is full, and katara can't keep you here..."
        y "wait."
        y "how would you like to stay at my house?"
        jd "...really?"
        y "you'd have to work to earn your keep... you'll have to clean the place, and so on."
        hide jd_idle_surprise with dissolve
        jd "that's fine!"
        jd "i've done plenty of that!"
        y "alright."
        y "the only problem is that my house isn't big enough yet..."
        y "i'll have to upgrade it."
        y ".........."
        y "...why are you still naked?"
        jd "I... have no clothes, young master."
        y "right, right."
        y "I'll pick you up some clothes while i'm at it."
        jd "that would be much appreciated!"
        y "stay here, i'll be back."
        jump love_bk3_village_background


    if suki_ty_hospital ==3 and suki_tylee <7:
        k3 "hey, welcome back!"
        y "where are the girls?"
        k3 "ty lee and suki went back to their homes."
        k3 "they're all healed up."
        y "alright, thanks."
        $ suki_tylee = 7
    if suki_tylee ==6:
        jump hospital_talk_menu

        label hospital_talk_menu:
            menu:
                "talk to katara":
                    show toki toki01 with dissolve
                    pass
                "talk to ty lee":
                    if suki_ty_hospital ==0:
                        hide toki with dissolve
                        show tf
                        with dissolve
                        y "hey, how are you holding up?"
                        ty "i'm okay... still recovering."
                        ty "i think... suki is still mad at me."
                        y "even after you..."
                        y "hmm."
                        y "i'll talk to her."
                        hide tf with dissolve
                        jump hospital_talk_menu
                    if suki_ty_hospital ==1:
                        hide toki with dissolve
                        show tf with dissolve
                        y "well, i talked with suki."
                        ty "and?"
                        y "she's still... being difficult."
                        show tfa
                        hide tf
                        with dissolve
                        ty "i understand."
                        ty "i feel so guilty."
                        y "why? you saved her."
                        ty "i shouldn't have listened to azula..."
                        ty "and i should have stopped that soldier before he even had the chance to hurt her."
                        y "....."
                        ty "is there anything i can do?"
                        y "hmm...."
                        y "I have an idea."
                        ty "what?"
                        y "you might be hesitant to do this, but..."
                        y "you should give suki dirt on azula."
                        ty "i... okay."
                        ty "that's weird, though."
                        y "suki's even madder at azula than she is at you."
                        y "trust me, it'll work out for the best if you do that."
                        hide tfa
                        show tf
                        with dissolve
                        ty "okay, i will."
                        hide tf with dissolve
                        $ suki_ty_hospital = 2
                        jump hospital_talk_menu
                    if suki_ty_hospital ==2:
                        hide toki with dissolve
                        show tf with dissolve
                        ty "why don't you come back tomorrow, once i've had a chance to talk to suki?"
                        hide tf with dissolve
                        jump hospital_talk_menu
                "talk to suki":

                    if suki_ty_hospital ==0:
                        hide toki with dissolve
                        show tosi tosi01 with dissolve
                        suki "hi, aang."
                        y "how are you, suki?"
                        suki "still sore, but better."
                        suki "katara is a miracle worker."
                        y "don't i know it."
                        suki "i want you to know..."
                        suki "i still don't forgive ty lee."
                        y "seriously?"
                        y "she got stabbed protecting you."
                        y "that earns her some forgiveness."
                        show tosi tosi03 with dissolve
                        suki "yeah, well, she still-"
                        y "that's it, suki!"
                        y "let me break something down for you."
                        show tosi tosi02 with dissolve
                        suki "wha-"
                        y "i'm helping you get revenge, but you're too stubborn to notice!"
                        show tosi tosi01 with dissolve
                        suki "you... are?"
                        y "how do you not see it?"
                        suki "i guess i just don't get-"
                        y "azula's the one you really want revenge on, right?"
                        suki "well, yes..."
                        y "who knows azula better than anyone?"
                        suki "...ty lee, probably."
                        y "and where is ty lee?"
                        show tosi_blink with dissolve
                        suki "....here."
                        y "i'm turning ty lee against azula, which was always my plan."
                        suki "i... i don't know..."
                        y "i can see you're unconvinced."
                        y "so i'll leave you to think on it."
                        hide tosi_blink with dissolve
                        suki "i will."
                        $ suki_ty_hospital =1
                        hide tosi with dissolve
                        jump hospital_talk_menu
                    if suki_ty_hospital ==1:
                        hide toki with dissolve
                        show tosi tosi01 with dissolve
                        suki "sorry aang, i'm feeling tired right now."
                        y "no worries, get some rest."
                        hide tosi with dissolve
                        jump hospital_talk_menu
                    if suki_ty_hospital ==2:
                        hide toki with dissolve
                        show tosi tosi01 with dissolve
                        y "ty lee wants to talk to you."
                        suki "she does?"
                        suki "well, i don't want to listen to her."
                        y "give it a chance."
                        suki "...all right."
                        suki "come back tomorrow, once she and i have had a chance to speak."
                        hide tosi with dissolve
                        jump hospital_talk_menu
                "exit":
                    jump love_bk3_village_background

    if love_jd_hypno ==10 and suki_tylee <3:
        $ suki_tylee = 3
        jump katara_jd_advice

    if hospital_building ==3:
        if ty_hospital and brothel_building <=2:
            k3 "you should find some room for ty lee."

        if not ty_hospital:
            $ ty_hospital = True
            k3 "thanks for doing that, aang."
            y "yeah, but i used up all my damn obsidian."
            y "i hope nobody else needs any."
            k3 "um."
            y "...what?"
            k3 "well..."
            y "seriously, what?"
            show toki toki02
            with dissolve
            k3 "why don't you come out, dear?"
            y "i'm not gay."
            y "I don't think."
            k3 "I didn't mean {i}you{/i}, aang."

            show tf:
                xpos -600
            with dissolve
            ty "i think she meant me."
            ty "hello!"
            y "oh, hey."
            y "what's up?"
            y "you disappeared right after i rescued you."
            ty "yeah... i..."
            show tfa:
                xpos -600
            hide tf
            with dissolve
            ty "...went to see azula."
            y "oh."
            y "how'd that go?"
            ty "i was sure it was a mistake, but... she tried to throw me back in the tunnels again."
            ty "i don't quite understand why, but she's really mad at me..."
            y "she betrayed you! be angry!"
            k3 "that's a little dramatic."
            y "quiet, you."
            y "well, what would you like to do, ty lee?"
            ty "i was hoping..."
            hide tfa
            show tf:
                xpos -600
            with dissolve
            ty "...maybe i could stay in the village?"
            ty "at least until she's done being mad at me?"
            y "that's cool."
            k3 "um..."
            y "oh. right. space."
            ya "damn it, katara."
            show toki_angry with dissolve
            k3 "it had to happen, aang!"
            hide toki_angry with dissolve
            k3 "but i wish i had a good solution."
            y "man..."
            y "I'm pissed i wasted all my obisidian on this."
            y "i wonder if anyone knows where to find more obsidian?"
            y "any suggestions?"
            show toki_blink with dissolve
            k3 "hmm...."
            k3 "well...."
            k3 "maybe..."
            k3 "but no..."
            y "come on!"
            hide toki_blink with dissolve
            k3 "sorry."
            k3 "maybe ask around."
            y "....."
            k3 "and maybe see if anyone has any room in the meantime?"
            y "alright."
            ty "see ya!"
            jump love_bk3_village_background


    if hospital_building ==2:
        if katara_upgrade_talk2:
            k3 "hey, aang."
            k3 "please upgrade the hospital."
            k3 "and come back when you've finished!"
        if not katara_upgrade_talk2:
            $ katara_upgrade_talk2 = True
            k3 "thanks, aang!"
            y "you're welcome."
            y "is that all you needed?"
            show toki toki02 with dissolve
            k3 "well...."
            y "what?"
            k3 "i still don't think it's enough."
            y "...."
            y "you've got to be kidding me."
            show toki_angry with dissolve
            k3 "no, i'm not kidding!"
            k3 "there's no more important building here, and you've been neglecting it!"
            y "you've been doing fine so far..."
            k3 "and i'm tired of trying to \"make it work\"!"
            k3 "i just want it to work!"
            hide toki_angry
            show toki toki01
            show toki_blink
            with dissolve
            k3 "*sigh...*"
            k3 "i'm sorry, aang... i don't mean to yell."
            k3 "I just..."
            hide toki_blink with dissolve
            k3 "the whole village will benefit from a larger hospital."
            k3 "especially any girls you rescue."
            y "....oh, damn it, fine."
            y "i'll upgrade it."
            y "but i'm not happy about it."
            show toki_smile with dissolve
            k3 "thank you, cutie."
            y "yeah, yeah..."
            jump love_bk3_village_background

    if earthbending >=16 and hospital_building <2:
        if katara_upgrade_talk:
            k3 "hey, aang."
            k3 "please upgrade the hospital."
            k3 "and come back when you've finished!"
        if not katara_upgrade_talk:
            $ katara_upgrade_talk = True
            k3 "aang, i'm glad you're here!"
            y "what's up?"
            show toki toki02 with dissolve
            k3 "well..."
            k3 "i don't have enough space here."
            y "you don't?"
            show toki_blink with dissolve
            k3 "no."
            k3 "i've been making do, but with all the girls that keeping coming through here, we need more room."
            y "okay..."
            hide toki_blink with dissolve
            k3 "i need you to upgrade the hospital."
            y "man...."
            y "...fine."
            show toki toki01 with dissolve
            k3 "thanks!"
            if not love_naga_eyes:
                y "where am i supposed to find more obsidian?"
                k3 "i don't know, where do you usually find it?"
                y "....."
                y "right."
            k3 "come back when you've finished!"
            jump love_bk3_village_background

    if love_june_hypno ==4:
        k3 "hey, aang!"
        y "hey... so..."
        if love_suki_hypno >=1:
            y "remember how suki got put into a hypnotic trance?"
            k3 "yes..."
            y "it happened to june this time."
        else:
            y "june is in some kind of hypnotic trance."
            y "can you help?"

        k3 "...."
        k3 "who?"
        y "june."
        y "the chick at the brothel."
        k3 "oh, right."
        k3 "yeah, we haven't really spent any time together."
        y "I... what?"
        y "is this important right now?"
        k3 "oh, no, sorry."
        if love_suki_hypno ==0:
            k3 "hmm...."
            show toki toki02
            with dissolve
            k3 "how was the trance induced?"
            y "uh... the guy said some phrase about lake laogai."
            k3 "and that set it off?"
            y "pretty much."
            show toki_blink with dissolve
            k3 "well... if it's aurally induced, maybe I can..."
            hide toki_blink with dissolve
            k3 "alright."

        k3 "i'm right behind you."
        k3 "let's go."
        $ love_june_hypno = 5
        jump love_bk3_village_background

    if love_suki_hypno ==1:
        k3 "aw, did you come visit me?"
        y "yeah, but not for fun reasons."
        k3 "oh? what's up?"
        if love_june_hypno >=1:
            y "remember how june got put into a hypnotic trance?"
            k3 "yes..."
            y "it happened to suki this time."
        else:
            y "suki's in some kind of... trance?"

        y "she's all spazzed out."
        y "i think it was a hypnosis-brainwash thing."
        if suki_dl_tits:
            y "...and she's naked."
            k3 "you left her naked somewhere?"
            y "yeah."
            k3 "oh."
            show toki_smile with dissolve
            k3 "fun!"
            y "that's what i thought!"
            hide toki_smile with dissolve

        if love_june_hypno ==0:
            k3 "hmm...."
            show toki toki02
            with dissolve
            k3 "how was it induced?"
            y "uh... the guy said some phrase about lake laogai."
            k3 "and that set it off?"
            y "pretty much."
            show toki_blink with dissolve
            k3 "well... if it's aurally induced, maybe I can..."
            hide toki_blink with dissolve

        k3 "let's go."
        k3 "i'll meet you there."
        $ love_suki_hypno = 2
        jump love_bk3_village_background

    if love_suki_hypno ==7:
        y "katara, come on!"
        show toki_smile with dissolve
        k3 "ooo... i like when you take charge!"
        k3 "what are we doing?"
        y "i need you to get suki out of another trance."
        hide toki_smile with dissolve
        k3 "oh."
        k3 "i'll grab a water flask and head over."
        $ love_suki_hypno = 8
        jump love_bk3_village_background

    if brothel_quest ==1:
        k3 "hey, sexy."
        k3 "you should go visit toph."

    if suki_love_met and brothel_quest ==0:
        k3 "hello?"
        show tosi tosi01:
            xzoom -1.0 xpos 200
        with dissolve
        suki "hey, katara."
        show toki toki04
        show toki_smile
        show expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "suki!"
        show toki toki03 with dissolve
        k3 "come here!"
        hide screen earth_money_date
        show black with fade
        "katara takes suki into a tight hug."
        "suki winces slightly."
        hide black
        show toki toki02
        with fade
        k3 "how are you?"
        k3 "what are you doing here?"
        k3 "and...."
        hide toki_smile
        hide expression "bk3/katara/idle/katara_lookleft.png"
        show toki_angry
        show expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "...you're bruised."
        k3 "what happened, are you okay?"
        y "katara, take a breath."
        k3 "...okay..."
        y "go ahead, suki."
        show tosi_blink:
            xzoom -1.0 xpos 200
        with dissolve
        suki "i..."
        show tosi tosi03
        with dissolve
        suki "...was taken prisoner in the tunnels beneath lake laogai."
        hide toki_angry
        show toki_surprised
        hide expression "bk3/katara/idle/katara_lookleft.png"
        show expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "what?!"
        k3 "how?"
        suki "i... don't want to go into it right now."
        suki "but... i'm going to deal with it."
        suki "believe me."
        hide toki_surprised
        show toki_angry
        hide expression "bk3/katara/idle/katara_lookleft.png"
        show expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "what can i do?"
        y "i think the first step is some healing."
        hide toki_angry
        show toki_surprised
        show toki toki04
        hide expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "of course! i'm being dumb!"
        hide tosi_blink
        hide toki_surprised
        show toki toki01
        hide expression "bk3/katara/idle/katara_lookleft.png"
        show expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "come with me."
        k3 "I have a little basin of water just for that."
        hide expression "bk3/katara/idle/katara_lookleft.png"
        k3 "aang, just wait here a moment."
        hide toki
        hide tosi
        with dissolve
        show black with dissolve
        "you watch patiently as katara carefully addresses each cut and bruise on suki."
        hide black with dissolve
        y "that was well done, katara."
        show toki toki02
        with dissolve
        k3 "it's not my first time."
        ym "heh. you're such a healslut."
        play sound "audio/kiss.mp3"
        show toki_smile
        show toki_blink
        k3 "*mwa!*"
        show tosi tosi01:
            xzoom -1 xpos 200
        hide toki_smile
        hide toki_blink
        with dissolve
        suki "thank you so much, katara."
        suki "that was amazing!"
        hide toki_smile
        show toki_blink
        with dissolve
        k3 "forget about it."
        y "so, suki..."
        menu:
            "you should stay":
                y "I think you should stay here."
                y "we can help you."
                y "you got quite a nasty experience down in the tunnels..."
                y "especially that whole getting the key out of-"
                suki "AHEM."
                "suki's eyes tell you to put a sock in it."
                k3 "out of what?"
                suki "let's... not talk about that right now."
                y "right."
                y "i'm just saying we'll be here for you if you need us..."
                ym "because friends are the key to your recovery and i'm great at recovery keys."
                suki ".............."
                ym "and when you're in a sticky situation, or something you need is in a... sticky... situation..."
                ym "well, your friends will get it out of you... er... get you out of it."
                suki "............."
            "you should leave":


                y "I think you should go."
                y "it sounds like you have some business to handle."
                y "i wouldn't want us to slow you down."
                k3 "don't be silly, aang!"
                k3 "we're here for you, whatever you need, suki."
                suki "i might be able to use the help, honestly."
                suki "so...."
            "what do you want to do?":

                y "what's your plan?"
                y "what would you like to have happen next?"
                k3 "you should stay!"
                y "let her decide that."

        suki "i think...."
        suki "I should stay here in the village."
        suki "i have a... debt that i owe."
        show expression "bk3/katara/idle/katara_lookleft.png"
        hide toki_blink
        with dissolve
        k3 "a debt?"
        show tosi tosi03 with dissolve
        suki "well... more of a grudge."
        suki "but i intend to repay it all the same, and I'll be better able to organize it from here."
        k3 "okay. we'll help."
        y "one problem."
        show tosi tosi01 with dissolve
        suki "what?"
        y "there's nowhere for you to stay."
        hide expression "bk3/katara/idle/katara_lookleft.png" with dissolve
        k3 "i'm sure the tavern-"
        y "look, i'm telling you, there's no room."
        k3 "i'm sure there's something you can do."
        k3 "maybe build a brothel?"
        y "....i like that idea."













        k3 "and i think a brothel will help you in your... mission... with toph."
        y "what... do you mean?"
        show toki_blink with dissolve
        k3 "......"
        hide toki_blink
        show expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        k3 "maybe suki could live there?"
        show tosi tosi02 with dissolve
        suki "what? ew!"
        show tosi tosi03 with dissolve
        suki "gross."
        suki "you'll never catch me in a brothel."
        suki "disgusting."
        show tosi tosi01 with dissolve
        y "then i guess i'll build one, and find someone to move in there."
        show tosi_blink:
            xzoom -1 xpos 200
        with dissolve
        suki "hey guys... i'm feeling a little weak."
        suki "can i-"
        show toki toki03
        with dissolve
        k3 "come here, let's go give you a rest."
        hide toki
        hide tosi
        hide tosi_blink
        hide expression "bk3/katara/idle/katara_lookleft.png"
        with dissolve
        "katara takes suki to the bed and lays her down."
        show toki toki01 with dissolve
        y "thanks for your help, katara."
        k3 "you're welcome, babe."
        k3 "but she can't stay here long."
        k3 "I need the bed for other patients."
        y "i'll get on with the brothel."
        k3 "well, about that..."
        k3 "toph isn't going to like the idea of a brothel."
        k3 "she's just not."
        k3 "but it's the next step in her process."
        y "her \"process\"?"
        y "okay... what do you know?"
        k3 "i know that i should go talk to her."
        y "stop avoiding my questions!"
        show toki_angry with dissolve
        k3 "aang, is this really important right now?"
        y "I... guess not."
        hide toki_angry
        show toki toki02
        with dissolve
        k3 "let me talk with her tonight."
        k3 "see if i can't get her to accept the idea."
        k3 "you go home and rest."
        k3 "you saved suki today, aang."
        k3 "you're a hero."
        menu:
            "I am a hero":
                y "you're right... i'm the best!"
                show toki_smile with dissolve
                k3 "don't let it go to your head, peach."
                y "...peach?"
            "i'm no hero":

                y "no, i'm not."
                y "I'm just doing what i have to."
                show toki_smile with dissolve
                k3 "and that's what makes you a hero."

        y "oh, before i go..."
        y "I found this weird equipment when I knocked out the head guard in the tunnels."
        hide toki_smile
        with dissolve
        k3 "a lantern?"
        k3 "it's definitely odd-looking."
        k3 "what's it for?"
        y "I don't know."
        k3 "hmm...."
        y "can you look into it?"
        k3 "sure, leave it here."
        scene black with dissolve
        "you head home for the night."
        $ brothel_quest = 1
        jump love_bk3_next

    if toph_chat ==6 and not katara_party_fuck:
        hide screen earth_money_date
        jump katara_party_fuck1

    if toph_chat ==5:
        if not party_plan_explained:
            k3 "hey!"
            k3 "i've been looking all over for you!"
            y "did you try... leaving the hospital?"
            show toki_angry with dissolve
            k3 "don't be mean!"
            hide toki_angry
            show toki_blink
            with dissolve
            k3 "also, no."
            hide toki_blink
            show toki toki02
            with dissolve
            k3 "but listen, i have a plan to get to the earth king."
            y "this sounds sketchy..."
            show toki_angry with dissolve
            k3 "you are always sketchy!"
            y "no, i'm not."
            hide toki_angry with dissolve
            k3 "listen, i'm already working on toph, you need to pay attention."
            y "alright, i'll-"
            y "wait, what do you mean you're \"working on toph\"?"
            y "for... what, exactly?"
            show toki_blink with dissolve
            k3 "forget it."
            hide toki_blink with dissolve
            k3 "look, i can get us {i}in{/i}."
            y "In where?"
            show toki_smile with dissolve
            k3 "in the palace!"
            y "for real?"
            k3 "yes!"
            hide toki_smile
            show toki_blink
            with dissolve
            k3 "...it's like talking to a wall."
            y "a sexy wall."
            hide toki_blink with dissolve
            k3 "....of course."
            y "so how are we getting in?"
            show toki_smile with dissolve
            k3 "that's the best part!"
            show toki toki03 with dissolve
            k3 "a party!"
            y "...."
            y "that's awesome!"
            show toki toki02 with dissolve
            k3 "right?"
            hide toki_smile with dissolve
            k3 "we'll need to meet at the palace, at night."
            y "okay...."
            y "how?"
            k3 "we'll have to arrive separately to avoid suspicion."
            k3 "so, sometime during the day, go to the palace and wait for us."
            k3 "got that?"
            y "during the day, go to the palace and wait for you."
            y "i still don't know how we're getting into the party, though."
            k3 "don't worry, i have a plan for that, too."
            k3 "just be there."
            y "at the palace."
            k3 "at the palace."
            $ party_plan_explained = True
        else:
            if not party_complete:
                k3 "don't forget, sometime during the day, go to the palace and wait for us."
                k3 "we'll have to arrive separately to avoid suspicion."
                y "okay, but i still don't know how we're getting into the party."
                k3 "don't worry, i have a plan for that, too."
                k3 "just be there."


    jump love_bk3_village_hospital_menu

label love_bk3_village_hospital_menu:

    menu:
        "play cards" if katara_lonely ==12:
            $ gf_count = 0
            $ gf_win_count = 0
            k3 "if you win two out of three, I'll give you a health potion."
            hide toki with dissolve
            jump go_fish_begin
        "fingering" if katara_lonely ==12:
            jump katara_rub_sex

        "ask katara on a date" if katara_lonely ==7:
            y "would you like to go on a date?"
            show toki_smile with dissolve
            k3 "i'd love to!"

            if smellerbee_fountain or smellerbee_gone:
                k3 "do you have time right now?"
                menu:
                    "yes":
                        $ katara_lonely = 8
                        y "as a matter of fact, i do."
                        k3 "wonderful!"
                        k3 "oh, yay!"
                        hide toki_smile with dissolve
                        k3 "well... um..."
                        k3 "where to?"
                        y "is there somewhere you'd like to go?"
                        k3 "oh, i don't know..."
                        y "come on, there must be somewhere."
                        k3 "well... what if we took the train out from the city for a while?"
                        y "oh, wow."
                        y "uh..."
                        k3 "yeah, i know."
                        k3 "we can go somewhere simpler, of course you wouldn't-"
                        y "no, we're gonna take the train."
                        k3 "...really?"
                        y "yeah, you deserve it."
                        show toki_smile with dissolve
                        k3 "you're the best, aang!"
                        y "oh, i know."
                        k3 "oh, hush."
                        k3 "come on!"
                        jump katara_sea_trip
                    "not yet":

                        y "not at the moment."
                        hide toki_smile with dissolve
                        k3 "I understand."
                        k3 "well, let me know."
                        jump love_bk3_village_hospital_menu
            else:
                hide toki_smile with dissolve
                k3 "...but i can't right now."
                if room30.sp_content >=2:
                    k3 "by the way, did you see that girl by the fountain?"
                    k3 "she seems homeless, maybe?"
                    k3 "i only caught a glimpse of her, though."
                    k3 "see you later!"
                    jump love_bk3_village_background
                else:
                    k3 "hey, you've rescued all the girls you can from the tunnels right?"
                    k3 "see you later!"
                    jump love_bk3_village_background

        "blowjob" if earthbending >= 4:
            hide screen earth_money_date
            jump katara_hospital_blowjob1

        "party fuck" if katara_party_fuck:
            hide screen earth_money_date
            jump katara_party_fuck2
        "life potion - 30":

            if emoney >=30:
                $ emoney -=30
                $ bk3_lifepotions += 1
                play sound "audio/win2.mp3"
                "you got a life potion!"
                jump love_bk3_village_hospital_menu
            else:
                "not enough money..."
                jump love_bk3_village_hospital_menu
        "mana potion - 20":

            if emoney >=20:
                $ emoney -=20
                $ bk3_manapotions += 1
                play sound "audio/win2.mp3"
                "you got a mana potion!"
                jump love_bk3_village_hospital_menu
            else:
                "not enough money..."
                jump love_bk3_village_hospital_menu
        "no thanks":


            jump love_bk3_village_background

    jump love_bk3_village_background

label love_inside_tophs_home:
    if suki_bar_blow >=7:
        if earthbending ==26 or earthbending ==27:
            scene black
            scene bg_bk3_tophome_night
            with dissolve
            y "toph?"
            y "where..."
            show toki toki03
            show toki_angry
            with dissolve
            k3 "aang!"
            k3 "toph's been captured!"
            y "what?!"
            show toki toki02 with dissolve
            k3 "i just caught a glimpse!"
            k3 "they put her in a metal box!"
            y "shit!"
            y "where'd they take her?"
            k3 "i can only assume the tunnels."
            y "then that's where i'll go."
            $ bk3love_freetoph = 1
            $ earthbending = 28
            jump love_bk3_village_background

        if earthbending ==28:
            scene black
            scene bg_bk3_tophome_night
            show toki toki02
            show toki_angry
            with dissolve
            k3 "aang!"
            k3 "go rescue toph from the tunnels!"
            jump love_bk3_village_background

    if toph_back_disappear ==1:
        y "i should give her some space tonight."
        jump love_bk3_village_background
    if suki_tylee >=7 and toph_back_disappear ==0:
        $ toph_back_disappear = 1
        hide screen earth_money_date
        scene black
        if not bk3_day:
            scene bg_bk3_tophome_night
        else:
            scene bg_bk3_tophome_day
        show toi toi06
        with dissolve
        y "toph?"
        t "what?"
        y "whoa, harsh."
        y "is everything alright?"
        show toi_blink with dissolve
        t "...."
        show toi toi09 with dissolve
        t "no...."
        show toi toi11 with dissolve
        t "no, everything is not alright."
        y "what's happened?"
        t "i don't... i don't want to talk about it."
        t "not yet."
        t "not... right now."
        y "okay, that's fair."
        y "i can give you some space."
        t "thanks... *sniff*..."
        t "thanks, aang."
        t "don't worry, we can... we can still train."
        t "bye."
        scene black with dissolve
        y "i hope she's okay..."
        jump love_bk3_village_background

    if love_jd_hypno ==10 and suki_tylee <7:
        y "hello?"
        y "toph?"
        "there's no response."
        y "where is she?"
        jump love_bk3_village_background

    if ty_hospital and not toph_obsidian_talk:
        $ toph_obsidian_talk = True
        hide screen earth_money_date
        scene black
        if not bk3_day:
            scene bg_bk3_tophome_night
        else:
            scene bg_bk3_tophome_day
        show toi toi04
        with dissolve
        t "hello."
        y "toph, do you have any idea where i could find some obsidian?"
        t "...huh."
        y "what?"
        t "i actually just found some, believe it or not."
        y "seriously?!"
        y "that's awesome!"
        y "can i have it?"
        t "....."
        t "sure, why not."
        $ obsidian +=1
        play sound "audio/win2.mp3"
        "you recieved 1 obsidian!"
        y "fuck yeah."
        t "why do you need it?"

        if not june_home_talk:
            y "i'm trying to find a place for ty lee in our village, so i'll have to upgrade someplace for her."
            t "ask around the village."
            t "i'm sure somebody will give you an idea."
            y "will do."
        else:
            y "i need to upgrade the brothel... er... boarding house."
            t "....boarding house?"
            y "yeah... i'm making a small change."
            t "sounds good to me."
            t "good luck!"
        jump love_bk3_village_background

    if suki_bar_talk and not toph_comfort_talk:
        jump toph_comfort

    if joodee_revenge and not suki_bar_talk:
        hide screen earth_money_date
        scene black
        scene toph_home_outside
        with dissolve
        y "the door is locked..."
        y "toph? you in there?"
        y "......"
        y "guess not."
        y "hmm... i guess i'll wander around a while, then."
        jump love_bk3_village_background





    if brothel_quest ==5:
        show azss azss01 with dissolve
        ss "hello, sir."
        ss "I was just leaving."
        y "any luck?"
        ss "of course."
        ss "no trouble at all."
        y "great, thanks."
        y "i've got to say... shady's cryptic warnings make me nervous."
        ss "about that..."
        ss "he wanted me to give you a message."
        y "....what?"
        ss "he says..."
        ss "\"watch your back, kid. long feng is breathing down your neck...and that guy breathes fire.\""
        sg "\"sleep with one eye open.\""
        y "......"
        y "again... i think his cryptic warnings hurt more than they help."
        y "also, what is he? a dragon?"
        ss "maybe."
        ss "have a good one, sir."
        hide azss azss01 with dissolve
        y "......."
        y "I can never read that chick."
        t "aang?"
        t "Is that you?"
        t "come on in!"
        hide screen earth_money_date
        scene black
        scene bg_bk3_tophome_night
        show toi toi04
        with dissolve
        t "hey!"
        y "hey, toph."
        y "i just passed some girl outside."
        y "what's that about?"
        show toi toi09 with dissolve
        t "it was the strangest thing."
        t "i was feeling all upset about the brothel idea..."
        t "...and she knocked and seemed a little confused."
        t "I think she was lost, actually."
        t "said she used to live around here, before the fire nation destroyed these little settlements."
        y "oh?"
        y "(man... i wonder what that girl's history is.)"
        t "yeah..."
        t "anyway, she got to talking... and i can't remember how it came up... but we started talking about the brothel."
        t "she convinced me that the brothel will bring much needed money into the village..."
        t "and give entrepreneurial girls the opportunity to take charge of their careers."
        t "she helped me see that my... narrow... understanding of morality was the only obstacle."
        t "she said she remembers how there used to be a brothel here in the village, and now the girls are walking around the street of basingse..."
        t "...in a very unsafe working environment."
        t "hmmm...."
        show toi toi04 with dissolve
        t "anyway, that's when you showed up."
        t "so, i guess... i'm okay with it."
        y "the brothel?"
        t "yeah. do what you gotta."
        t "i think... maybe i'm too prudish sometimes."
        show toi_blush
        with dissolve
        t "sorry i got all mad at you."
        show toi toi09
        show toi_blink
        with dissolve
        t "I'm super embarrassed."
        y "aw, don't worry about it."
        y "i'll get started building it, then."
        hide toi_blink
        show toi toi04
        with dissolve
        t "cool."
        $ brothel_quest = 6
        jump love_bk3_village_background

    if brothel_quest >=2 and brothel_quest <=4:
        y "i should go find someone to sell the brothel idea to toph."
        jump love_bk3_village_background

    if brothel_quest ==1:
        scene black
        scene bg_bk3_tophome_night
        show toi toi51
        with dissolve
        t "aang!"
        y "You... seem mad."
        y "should i come back later?"
        t "no! i'm mad at {i}you{/i}!"
        y "so i should definitely come back later."
        t "what are you thinking?!"
        y "if there's a non-gay way to eat a popsicle."
        hide toi with dissolve
        show toi toi06 with dissolve
        t "don't play dumb!"
        t "a brothel? really?"
        t "in the town we're trying to {i}help{/i}?"
        t "how can that possibly help?"
        y "i thought katara was going to-"
        t "oh, she came by."
        show toi toi05 with dissolve
        t "tried to convince me that it would be a good idea to have prostitutes around!"
        t "do you want to sleep with them, aang?"
        t "is that what you're trying to do?"
        y "no, i-"
        show toi toi11 with dissolve
        t "i know i'm... i'm not the sexiest.."
        t "but i didn't know i was so-"
        y "it's unrelated to you!"
        y "this {i}will{/i} help the village!"
        show toi toi05
        show toi_tears
        with dissolve
        t "then go help them!"
        t "see if i care!"
        y "You obviously do."
        show toi_blink with dissolve
        t "just get out!"
        play sound "audio/thud.mp3"
        scene black with vshake
        "toph slams the door in your face."
        y "okay... i am not good enough for this."
        y "hmmmmm....."
        y "who could sell toph on this idea?"
        y "i've got to think about this."
        $ brothel_quest = 2
        jump love_bk3_village_background

    if not bk3_day:
        scene black
        scene toph_home_outside
        with dissolve
        menu:
            "knock":
                t "come in!"
                pass
            "peek on toph" if lovehousefire <5:
                jump love_toph_peek

        hide screen earth_money_date
        scene black
        scene bg_bk3_tophome_night
        if toph_back_disappear ==2:
            show toi toi09
            with dissolve
            t "hey, aang."
        else:
            show toi toi04
            with dissolve

        if toph_angry>=1:
            t "hel-"
            show toi toi06 with dissolve
            t "you!"
            t "i'm mad at you!"
            t "go away, i don't want to talk to you!"
            hide toi toi06 with dissolve
            y "....guess i'll have to come back tomorrow."
            jump love_bk3_village_background
        if toph_back_disappear <2 or toph_back_disappear >2:
            t "sup, aang?"
        jump toph_night_menu

        label toph_night_menu:
            menu:
                "sleep" if (earthbending ==11 and lovehousefire <=5) or (toph_chat >=10 and toph_chat <=11):
                    jump love_bk3_next
                "chat ([toph_chat]/24)":
                    if toph_chat ==0:
                        jump toph_chat1
                    if toph_chat <=1:
                        jump toph_chat2
                    if toph_chat <=2:
                        if earthbending <=4:
                            jump toph_chat2
                        if earthbending >=5:
                            jump toph_chat3
                    if toph_chat <=4:
                        if earthbending <=5:
                            t "we've really got to work on your training."
                            jump toph_night_menu
                        else:
                            if not june_freed:
                                jump toph_chat4
                            if june_freed:
                                jump toph_chat5

                    if toph_chat ==5:
                        if june_brothel_talk:
                            if not party_complete:
                                t "katara wants to talk to you."
                                jump toph_night_menu
                            else:
                                jump toph_chat6
                        else:
                            t "hey, have you talked to june yet?"
                            t "she's waiting for you in the tavern."
                            jump toph_night_menu

                    if toph_chat ==6:
                        if not katara_party_fuck:
                            t "katara wants to talk to you again."
                            jump toph_night_menu
                        else:
                            if earthbending <=6:
                                t "we've really got to work on your training."
                                jump toph_night_menu
                            else:
                                jump toph_chat7
                    if toph_chat ==7:
                        if earthbending <=7:
                            t "we've really got to work on your training."
                            jump toph_night_menu
                        else:
                            if not suki_freed:
                                show toi toi06 with dissolve
                                t "i'm worried about those girls in the tunnels, aang."
                                t "i think you're strong enough to do some good down there."
                                show toi toi04 with dissolve
                                jump toph_night_menu
                            else:
                                if earthbending >=9:
                                    jump toph_chat8
                                else:
                                    t "let's chat later, aang."
                                    jump toph_night_menu
                    if toph_chat ==8:
                        if avatar_shack <2:
                            t "you should really upgrade your place."
                            jump toph_night_menu
                        else:
                            if toph_walk_talk:
                                t "hey, about the other night..."
                                t "would you like to go for a walk?"
                                menu:
                                    "that sounds nice":
                                        y "sure, i think that's a nice idea."
                                        jump toph_walk
                                    "not right now":

                                        y "another time."
                                        show toi toi09 with dissolve
                                        t "oh..."
                                        t "okay."
                                        t "just... let me know, then."
                                        scene black with dissolve
                                        "you head home for the night."
                                        jump love_bk3_next
                            else:
                                jump toph_chat9

                    if toph_chat ==9:
                        if earthbending == 10:
                            jump toph_chat10
                        else:
                            t "we've really got to work on your training."
                            jump toph_night_menu

                    if toph_chat ==10:
                        jump toph_chat11






                    if toph_chat ==11:
                        if footjob_book:
                            jump toph_chat12
                        else:
                            t "any luck finding a story to read to me?"
                            y "Not yet."
                            show toi toi09 with dissolve
                            t "oh, okay."
                            hide toi toi09
                            show toi toi04
                            with dissolve
                            jump toph_night_menu

                    if toph_chat ==12:
                        if earthbending ==12:
                            jump toph_chat13
                        else:
                            t "we've really got to work on your training."
                            jump toph_night_menu

                    if toph_chat ==13:
                        jump toph_chat14

                    if toph_chat ==14:
                        if earthbending >=13:
                            jump toph_chat15
                        else:
                            t "we've really got to work on your training."
                            jump toph_night_menu

                    if toph_chat ==15:
                        $ toph_chat = 16
                        jump toph_chat16

                    if toph_chat ==16:
                        if suki_tylee ==1 and earthbending >=17:
                            $ toph_chat = 17
                            jump toph_chat17
                        else:

                            t "let's chat later, aang."
                            jump toph_night_menu

                    if toph_chat ==17:
                        if earthbending >=18:
                            jump toph_chat18
                        else:
                            t "let's chat later, aang."
                            jump toph_night_menu

                    if toph_chat ==18:
                        jump toph_chat19

                    if toph_chat ==19:
                        jump toph_chat20

                    if toph_chat ==20:
                        if earthbending ==19:
                            jump toph_chat21
                        else:
                            t "let's chat later, aang."
                            jump toph_night_menu

                    if toph_chat ==21:
                        if earthbending ==20:
                            jump toph_chat22
                        else:
                            t "let's chat later, aang."
                            jump toph_night_menu

                    if toph_chat ==22:
                        if earthbending ==21:
                            y "so, why were you so busy earlier?"
                            t "just running around, trying to keep busy."
                            y "...scams?"
                            t "scams."
                            y "did you make much money?"
                            t "oh, not that kind of scam."
                            y "then what?"
                            show toki toki01:
                                xzoom -1
                            with moveinleft
                            k3 "hey guys!"
                            y "oh, hey, what's up?"
                            k3 "suki just hit me up."
                            k3 "wanna head to the tavern?"
                            t "yeah, that sounds fun."
                            y "i'm in."
                            scene black with dissolve
                            jump toph_chat23
                        else:
                            t "let's chat later, aang."
                            jump toph_night_menu

                    if toph_chat ==23:
                        if earthbending == 22:
                            jump toph_chat24
                        else:
                            t "let's chat later, aang."
                            jump toph_night_menu

                    if toph_chat ==24:
                        t "let's chat later, aang."
                        jump toph_night_menu

                    if toph_chat ==25:
                        t "let's chat later, aang."
                        show under_development_1
                        pause
                        hide under_development_1
                        jump toph_night_menu
                "touch face":

                    if toph_back_disappear ==2:
                        t "I'm sorry, i'm just... not up for that right now."
                        jump toph_night_menu
                    if toph_chat >=3:
                        if toph_face_touch ==0:
                            jump toph_face_touch1
                        if toph_face_touch ==1:
                            jump toph_face_touch2
                        if toph_face_touch ==2:
                            jump toph_face_touch3
                    else:

                        y "(that seems a little forward right now...)"
                        y "(maybe i should talk with her a little first.)"
                        jump toph_night_menu
                "titplay":

                    if toph_back_disappear ==2:
                        t "I'm sorry, i'm just... not up for that right now."
                        jump toph_night_menu
                    if toph_chat >=7:
                        if toph_titplay == 0:
                            jump toph_titplay1
                        if toph_titplay ==1:
                            jump toph_titplay2
                        if toph_titplay ==2:
                            jump toph_titplay3
                        if toph_titplay ==3:
                            jump toph_titplay3
                    else:
                        y "(that seems a little forward right now...)"
                        y "(maybe i should talk with her a little first.)"
                        jump toph_night_menu

                "?????(locked)" if toph_chat <12:
                    "test"

                "footjob" if toph_chat >=12:
                    if toph_back_disappear ==2:
                        t "I'm sorry, i'm just... not up for that right now."
                        jump toph_night_menu
                    if toph_chat >=12:
                        if toph_footjob == 0:
                            jump love_toph_footjob1
                        if toph_footjob ==1:
                            jump love_toph_footjob2
                    else:

                        y "(that seems a little forward right now...)"
                        jump toph_night_menu

                "?????(locked)" if toph_chat <15:
                    "test"

                "blowjob" if toph_chat >=15:
                    if toph_back_disappear ==2:
                        t "I'm sorry, i'm just... not up for that right now."
                        jump toph_night_menu
                    y "how about a blowjob?"
                    $ toph_top_nude = True
                    $ toph_bottom_nude = True
                    t "okay!"
                    hide toi
                    show toi toi200
                    show toi_blush
                    with fade
                    show ctc
                    pause
                    hide ctc
                    t "Now, take off your clothes."
                    jump love_toph_blowjob

                "?????(locked)" if not suki_toph_ass:
                    "test"

                "ass massage" if suki_toph_ass:
                    if toph_back_disappear ==2:
                        t "I'm sorry, i'm just... not up for that right now."
                        jump toph_night_menu

                    y "want to have a little... butt fun?"
                    y "at the tavern?"
                    show toi toi09 with dissolve
                    t "ummm...."
                    show toi toi07 with dissolve
                    t "hell yes."
                    jump toph_ass_massage2

                "missionary" if love_toph_sex:
                    jump toph_fuckonback

                "anal (prone)" if toph_chat >= 24:
                    scene black
                    scene bg_bk3_tophome_0
                    with dissolve
                    jump love_toph_anal1

                "anal (cowgirl)" if toph_chat >= 24:
                    jump love_toph_anal2
                "exit":

                    jump love_bk3_village_background

    if bk3_day:
        if toph_angry >= 1:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            t "hel-"
            show toi toi06 with dissolve
            t "you!"
            t "i'm mad at you!"
            t "get out! I don't want to talk to you!"
            scene black with dissolve
            y "....guess i'll have to come back tomorrow."
            jump love_bk3_village_background

        if earthbending ==4:
            hide screen earth_money_date
            show toi toi04
            with dissolve
            t "hey, twinkletoes."
            t "you need to pick up your training."
            t "how about it?"
            menu:
                "train with toph":
                    jump earthtraining4
                "later":
                    jump love_bk3_village_background

        if earthbending ==5:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            t "hey, aang."
            if toph_face_touch >=1:
                t "ready for some more training?"
                menu:
                    "train with toph":
                        jump earthtraining5
                    "later":
                        jump love_bk3_village_background
            else:
                t "you definitely need some more training."
                t "give me some more time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==6:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            t "hey, aang."
            if katara_party_fuck:
                t "ready for some more training?"
                menu:
                    "train with toph":
                        jump earthtraining6
                    "later":
                        jump love_bk3_village_background
            else:
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==7:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            t "hey, aang."
            if toph_titplay >=1:
                t "ready for some more training?"
                menu:
                    "train with toph":
                        jump earthtraining7
                    "later":
                        jump love_bk3_village_background
            else:
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background
        if earthbending ==8:
            if suki_freed:
                hide screen earth_money_date
                scene black
                scene bg_bk3_tophome_day
                show toi toi04
                with dissolve
                t "hi, aang!"
                if brothel_quest >=8:
                    t "ready for some more training?"
                    menu:
                        "train with toph":
                            jump earthtraining8
                        "later":
                            jump love_bk3_village_background
                else:
                    t "you're coming along, but you definitely need to keep training."
                    t "give me some time to think about the next step."
                    jump love_bk3_village_background
            else:
                hide screen earth_money_date
                scene black
                scene bg_bk3_tophome_day
                show toi toi06
                with dissolve
                t "aang, have you checked down in the tunnels?"
                t "see if there's anyone down there you can rescue."
                t "that'll give me some time to think about the next step of your training."
                jump love_bk3_village_background

        if earthbending ==9:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if toph_comfort_talk:
                t "hi, aang!"
                t "ready for some more training?"
                menu:
                    "train with toph":
                        jump earthtraining9
                    "later":
                        jump love_bk3_village_background
            else:

                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==10:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if toph_chat ==12:
                t "okay, let's get you strong enough to put your house back together."
                menu:
                    "train with toph":
                        jump earthtraining10
                    "later":

                        jump love_bk3_village_background
            else:
                t "ready for some more training?"
                menu:
                    "train until night":
                        t "come on, let's do some training."
                        scene black with dissolve
                        "you spend the day doing some light earthbending exercises with toph."
                        $ bk3_day = False
                        jump love_bk3_village_background
                    "later":

                        jump love_bk3_village_background

        if earthbending ==11:
            if lovehousefire >=6:
                hide screen earth_money_date
                scene black
                scene bg_bk3_tophome_day
                show toi toi50
                with dissolve
                t "you've come a long way, aang."
                t "but that just means i can stop going easy on you."
                y "what?!"
                y "tell me you're joking."
                show toi toi02 with dissolve
                t "sorry, twinkletoes, but i'm serious."
                show toi toi07 with dissolve
                t "i never thought you'd get this far this quickly though."
                show toi toi09 with dissolve
                t "it took me a lot longer to get this good."
                y "i know, i'm amazing."
                y "and you just can't help falling in love with me."
                show toi toi10 with dissolve
                t "what! no! i... um..."
                y "it happens all the time."
                y "some things can't be helped."
                t "...."
                show toi toi12 with dissolve
                t "pbbt."
                y "what?"
                t "pppbbbtttt!"
                y "that's not a word."
                t "ppppppppbbbbbbbbbbbttttttt!"
                show toi toi07 with dissolve
                t "that's how i feel about you."
                y "aw."
                t "now come on, you idiot."
                t "we're gonna fight."
                y "what? why?"
                show toi toi04 with dissolve
                t "you're good enough now that we can really train."
                show toi toi06 with dissolve
                t "the best way to learn is practical application."
                t "so let's get to it."
                y "ah shit."
                show toi toi07 with dissolve
                t "that's the spirit!"
                show black with dissolve
                "you spend the day getting your ass kicked by toph."
                "but you pull off some tricks in the process."
                show toi toi04
                hide black
                with dissolve
                t "alright, well, i think you're a bit stronger now."
                t "i wonder if you can free any more girls in the tunnels?"
                y "i can always try."
                play sound "audio/win2.mp3"
                "your earthbending got stronger!"
                $ earthbending = 12
                $ maze_sections = 2
                $ bk3_day = False
                jump love_bk3_village_background
            else:
                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==12:
            if toph_chat ==14:
                hide screen earth_money_date
                scene black
                scene bg_bk3_tophome_day
                show toi toi07
                with dissolve
                t "welcome back, twinkletoes."
                y "time for more... practical application?"
                t "you got it!"
                y "....argh."
                show black with dissolve
                "you spend the day battling toph, but manage to stay upright."
                "mostly."
                hide black
                show toi toi04
                show expression "bk3/toph/idles/idle_sooth_toph.png"
                with dissolve
                t "not bad, aang."
                t "come on, let's go to the lake."
                t "it's been a while since we were there."
                t "...and we're kind of a mess."
                t "besides..."
                t "i have a new... outfit... that katara suggested."
                $ earthbending = 13
                $ love_toph_bikini = True
                $ bk3_day = False
                jump lake_cock_talk
            else:

                hide screen earth_money_date
                scene black
                scene bg_bk3_tophome_day
                show toi toi04
                with dissolve
                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==13:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if love_june_hypno ==11:
                t "alright, aang."
                t "it's time for another afternoon of smackdown, paintown, going down-"
                y "*groan...*"
                show toju toju01:
                    xzoom -1
                with dissolve
                ju "...hello?"
                show toi toi09 with dissolve
                t "june?"
                ju "shorty."
                show toi toi05 with dissolve
                t "hey!"
                y "what's up, june?"
                ju "i have a favor to ask you."
                ju "i was wondering if you could come help me."
                y "what's this about?"
                ju "i'd... rather not say."
                t "well, this is my house, so i vote \"no\"!"
                y "toph..."
                show toi toi06 with dissolve
                t "maybe if she apologizes."
                ju "i don't apologize."
                t "then you can go."
                y "june, just apologize."
                y "you did insult her."
                y "toph, quit being so sensitive."
                t "......"
                ju "i'm... sorry."
                ju "...toph."
                y "well done."
                y "are we good?"
                t "i suppose..."
                ju "i don't have much time, come on."
                ju "please."
                t "well...."
                t "this is supposed to be an earthbending training session..."
                t "will this favor involve earthbending?"
                ju "oh, absolutely."
                show toi toi04 with dissolve
                t "then it's fine with me."
                t "go with her, aang."
                y "I feel like nobody actually asked if i wanted to do... whatever this is."
                t "we didn't."
                t "go on."
                ju "....please?"
                y "you're much nicer to me lately."
                show toi toi06 with dissolve
                t "not to me...."
                ju "alright, let's go."
                ju "and.... thank you, toph."
                ju "come on."
                y "where are we going?"
                ju "come... on!"
                $ earthbending = 14
                jump june_hunt
            else:

                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==14:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if love_june_hypno >=12 and toph_chat >=16:
                $ earthbending = 15
                show tosi tosi10:
                    xzoom -1
                with dissolve
                y "suki?"
                y "what are you doing here?"
                y "and why are you dressed up?"
                suki "ask toph."
                t "i had a new idea for training."
                t "i've invited suki to be your opponent today."
                t "sending you off with june gave me the idea."
                y "but she's not even a bender..."
                suki "you think it'll be easy, hotshot?"
                y "well... yeah."
                show toi_blink with dissolve
                t "there's value in training with a non-bender."
                t "different tactics and consequences."
                t "i think this will be an... interesting learning experience."
                y "alright, bring it on."

                show tosi tosi12 with dissolve
                suki "hyyyyaaaa!"
                ya "not the face, not the face!"
                play sound "audio/thud.mp3"
                show black with vshake
                "you battle suki, who presses the attack, forcing you to be creative with your defense."
                "you eventually gain the upper hand, but it's close, and you're both exhausted."
                hide black
                show tosi tosi10
                hide toi_blink
                with dissolve
                y "that... was... way hard."
                t "told you."
                suki "not bad, aang."
                suki "you really held your own!"
                y "i'm... so... pooped..."
                t "you wimp."
                t "so how should we reward this session?"
                suki "i have a great idea."
                suki "you could come see me over to the tavern."
                suki "just relax for a bit."
                y "sounds good."
                suki "i'll meet you there, so you can have a chance to recover."
                y "thanks..."
                suki "see you later, guys!"
                scene black with dissolve
                "you leave toph's house more tired than usual."
                $ earthbending = 15
                $ bk3_day = False
                jump love_bk3_village_background
            else:

                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==15:
            if not suki_toph_ass:
                y "i should meet toph at the tavern."
                jump love_bk3_village_background
            else:
                if love_jd_hypno >=7:
                    if not suki_revenge_talk:
                        hide screen earth_money_date
                        scene black
                        scene bg_bk3_tophome_day
                        show toi toi04
                        with dissolve
                        t "hey, aang."
                        t "suki wants to talk to you."
                        t "she's at the tavern."
                        jump love_bk3_village_background
                    else:
                        hide screen earth_money_date
                        scene black
                        scene bg_bk3_tophome_day
                        show toi toi04
                        with dissolve
                        show toi toi07 with dissolve
                        t "welcome back to the ass-kick dojo!"
                        y "no...."
                        t "wanna get started?"
                        menu:
                            "train":
                                $ earthbending = 16
                                $ maze_sections = 3
                                show toi toi04 with dissolve
                                t "alright, aang..."
                                show toi toi06 with dissolve
                                t "you soon won't need any more training from me."
                                t "let's make this one count."
                                scene black with dissolve
                                "you and toph fight all-out."
                                "you hold your ground and even gain the upperhand at the end..."
                                "...until toph flips your onto your back."
                                "you launch yourself before her next attack lands, and before she can recover..."
                                "...you force a wall of earth at her."
                                "she punches through it as you sink her feet into the dirt and harden it around them."
                                "as she yanks her feet up, you ride a trail of rock towards her and surprise her..."
                                "...with a kiss."
                                play sound "audio/kiss.mp3"
                                scene bg_training_0
                                show tonf tonf22
                                with pflash
                                t "......."
                                show tonf tonf23 with dissolve
                                t "....oh."
                                show tonf tonf23_2 with dissolve
                                t "that was cheeky."
                                show tonf tonf23 with dissolve
                                t "...do..."
                                t "...do it again."
                                menu:
                                    "kiss":
                                        show tonf tonf24 with dissolve
                                        t "oh, aang...."
                                        play sound "audio/kiss.mp3"
                                        show tonf tonf22
                                        with pflash
                                        t "....."
                                        show tonf tonf23 with dissolve
                                        t "alright..."
                                        t "give me your finger."
                                        y "...what?"
                                        t "just...."
                                        show tonf tonf26 with dissolve
                                        show ctc
                                        pause
                                        hide ctc
                                        t "you did well, so..."
                                        t "how about a little treat?"
                                        show tonf tonf27 with dissolve
                                        t "*mmm....*"
                                        show ctc
                                        pause
                                        hide ctc
                                        t "you know what i wish this was?"
                                        y "...."
                                        t "your long..."
                                        t "*smack...*"
                                        t "hard...."
                                        t "*shluuup...*"
                                        t "cock."
                                        t "*...mmmmh...*"
                                        show ctc
                                        pause
                                        hide ctc
                                        y "you know, we can make that happen..."
                                        t "hmmgh...?"
                                        show tonf tonf26 with dissolve
                                        t "*mwa!*"
                                        t "maybe later."
                                        hide tonf with dissolve
                                        show toi toi04 with dissolve
                                        t "good job today, you."
                                        t "you're probably strong enough to rescue more girls from the tunnels."
                                        t "i'll see you later!"
                                        t "bye!"
                                        jump love_bk3_village_background
                                    "don't kiss":

                                        y "maybe later."

                                        hide tonf with Dissolve(1)
                                        show toi toi09 with Dissolve(1)
                                        t "oh... kay."
                                        t "well... you did a good job today."
                                        t "you're probably strong enough to rescue more girls from the tunnels."
                                        t "i'll see you later, i guess..."
                                        jump love_bk3_village_background
                            "later":

                                y "not right now."
                                show toi toi04 with dissolve
                                t "you pansy."
                                jump love_bk3_village_background
                else:
                    hide screen earth_money_date
                    scene black
                    scene bg_bk3_tophome_day
                    show toi toi04
                    with dissolve
                    t "hey, aang."
                    t "you're coming along, but you definitely need to keep training."
                    t "give me some time to think about the next step."
                    jump love_bk3_village_background
        if earthbending ==16:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if brothel_building >=3:
                t "let's get some more training in!"
                menu:
                    "train":
                        show toi toi06 with dissolve
                        t "you're fighting well, but you still hold back too much."
                        y "i do?"
                        t "yeah."
                        t "like you're worried about me."
                        y "i mean, i am..."
                        show toi toi05 with dissolve
                        t "what?!"
                        t "you think i can't take care of myself?"
                        y "no, it's just that..."
                        t "i think you're a chicken."
                        t "a chick chick chicken."
                        t "ba-kwak!"
                        y "hey..."
                        t "you're too scared to hurt your opponent."
                        y "okay, that's not true..."
                        t "then prove it, twinkletoes!"
                        show black with dissolve
                        "you and toph fight, and she is relentless."
                        t "you can do better than that!"
                        t "give me your all!"
                        t "don't hold back!"
                        ya "you asked for it!"
                        "the two of you exchange blows and earth attacks until you're both exhausted."
                        "you return to her house."
                        hide black
                        show toi toi09
                        with dissolve
                        t "i'm beat...."
                        y "fuckin' same."
                        t "alright, go get some rest."
                        t "well done today."
                        $ earthbending = 17
                        $ bk3_day = False
                        jump love_bk3_village_background
                    "later":

                        y "some other time."
                        show toi toi09 with dissolve
                        t "alright, you pansy."
                        jump love_bk3_village_background

            if love_naga_eyes and hospital_building <2:
                t "oh, aang."
                t "katara wants to talk to you."
                t "she's at the hospital."
                jump love_bk3_village_background
            else:
                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==17:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi06
            with dissolve
            if toph_back_disappear:
                y "hey..."
                t "let's get this over with."
                y "what?"
                t "today's training."
                t "let's get it over with."
                y "uh... I don't know if this is such a good idea..."
                y "you seem pretty upset."
                t "i think it's a great idea."
                t "i have a bunch of aggression to get out."
                y "yeah... that's why it doesn't seem like a good idea... for me."
                t "come on, you pansy."
                show black with dissolve
                "the two of you walk outside."
                "just as you reach an open field, toph launches herself at you."
                t "get some!"
                y "whoa!"
                show black with dissolve
                "toph comes at you with everything she has."
                "the fighting is intense, and you come out about equal."
                "the two of you walk back to toph's house."
                hide black
                show toi toi02
                with dissolve
                t "i feel a little better."
                y "nice!"
                y "want to tell me what was bothering you?"
                show toi toi06 with dissolve
                t "...no."
                t "I'll see you later, aang."
                y "wait-"
                play sound "audio/thud.mp3"
                scene black with hpunch
                "toph slams the door in your face."
                y "damn it."
                $ earthbending = 18
                jump love_bk3_village_background
            else:

                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==18:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            if toph_back_disappear <=2:
                show toi toi06
            else:
                show toi toi04
            with dissolve
            if love_toph_sex:
                t "hey."
                y "yo."
                if not bk3_shop_watch:
                    t "that... friendly... shop girl was looking for you."
                else:
                    if toph_walk_quest:
                        jump toph_walk_question

                    t "what are you doing right now?"
                    y "...standing."
                    y "in your living room."
                    y "damn, you are so blind."
                    t "no, i.... shut up."
                    $ toph_walk_quest = True
                    jump toph_walk_question

                    label toph_walk_question:
                        t "i feel like going for a walk."
                        t "want to come with me?"
                        menu:
                            "walk":
                                y "i could probably use the exercise."
                                t "come on, then!"
                                $ earthbending = 19
                                jump toph_mean_walk
                            "later":

                                y "another time."
                                t "sure, whenever you're ready."
                                jump love_bk3_village_background
            else:

                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
            jump love_bk3_village_background

        if earthbending ==19:
            hide screen earth_money_date
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if not bk3_shop_watch:
                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                t "oh, and that... friendly... shop girl was looking for you."
            else:
                if toph_chat ==21:
                    t "welcome back!"
                    t "ready for a new kinda training session?"
                    menu:
                        "fo shizzle":
                            y "mos def."
                            t "sweet!"
                            show toi toi09 with dissolve
                            t "i mean... i assume that meant \"yes\"?"
                            t "your slang is outdated and horrible."
                            y "{i}you're{/i} outdated and horrible."
                            show toi toi06 with dissolve
                            t "...what?!"
                            y "I meant... not that..."
                            y "yes. is what i should have said."
                            y "i am ready."
                            t "....."
                            show toi toi07 with dissolve
                            t "great!"
                            t "come outside with me."
                            jump earthtraining19
                        "what? no":
                            y "maybe later."
                            jump love_bk3_village_background
                else:
                    t "hey, aang."
                    t "you're coming along, but you definitely need to keep training."
                    t "give me some time to think about the next step."
            jump love_bk3_village_background

        if earthbending ==20:
            hide screen earth_money_date
            if toph_chat >=22 and katara_lonely ==0:
                scene black
                scene bg_bk3_tophome_day
                show toi toi04
                show toki toki01:
                    xzoom -1
                with dissolve
                k3 "...that's all."
                k3 "oh! hey, aang."
                y "what's... going on?"
                show toki_blink:
                    xzoom -1
                with dissolve
                k3 "nothing!"
                k3 "just catching up."
                k3 "see ya!"
                hide toki_blink
                hide toki
                with dissolve
                y "okay..."
                y "......"
                y "toph, what's really going on?"
                show toi toi09 with dissolve
                t "she just came over to chat."
                t "about, like, nothing at all."
                y "...and?"
                y "is that weird?"
                t "kinda, yeah."
                t "she usually only comes over to be bossy."
                y "she is sort of wired that way."
                t "so, yeah, it's weird that she just came over to... ramble."
                y "what did she talk about?"
                t "she asked how we were doing, and i told her we're fine."
                t "then she mentioned something along the lines of how it must be nice to have you around..."
                y "huh."
                t "what?"
                y "i think... it sounds like..."
                y "...do you think she's lonely?"
                t "uh... maybe?"
                t "would katara {i}get{/i} lonely?"
                y "i would guess so, yeah."
                y "i mean, she's not a robot."
                show toi toi06 with dissolve
                t "if she is, she's a bossy robot."
                y "....right."
                show toi toi04 with dissolve
                t "that's probably not it."
                y "maybe."
                y "well, if she needs company, she'll ask."
                y "i think."
                $ katara_lonely = 1
                scene black with dissolve
                jump love_bk3_village_background
            if katara_lonely ==4:
                jump katara_stick_melon
            if katara_lonely >=12:
                scene black
                scene bg_bk3_tophome_day
                with dissolve
                y "...toph?"
                y "you here?"
                y "...."
                y "guess i'll go."
                with vpunch
                show toph_enters with dissolve
                t "...aang?"
                y "hey, you okay?"
                show toi toi50
                hide toph_enters
                with dissolve
                t "yeah, i'm great."
                t "i'm busy right now."
                t "wanna hang out later?"
                y "sure."
                t "come by tonight."
                play sound "audio/kiss.mp3"
                with pflash
                "toph gives you a kiss and lightly pushes you out the door."
                "you take the hint."
                $ earthbending = 21
                jump love_bk3_village_background
            else:
                scene black
                scene bg_bk3_tophome_day
                show toi toi04
                with dissolve
                t "hey, aang."
                t "you're coming along, but you definitely need to keep training."
                t "give me some time to think about the next step."
                jump love_bk3_village_background

        if earthbending ==21:
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if toph_chat <23:
                t "hey, i'm busy right now."
                t "come by tonight."
                y "sure thing."
            if toph_chat ==23:
                t "hello there, handsome."
                y "hello yourself, beautiful."
                show toi_blush with dissolve
                y "are you blushing?"
                show toi_blink
                with dissolve
                t "no!"
                t "...shut up!"
                y "i will not."
                hide toi_blink with dissolve
                t "...okay, i'm blushing."
                t "thanks for... you know."
                y "for what?"
                t "for... taking care of me."
                t "both at night, and..."
                show toi_blink with dissolve
                t "in the morning."
                y "damn you're cute."
                hide toi_blink with dissolve
                t "so, what's up?"
                menu:
                    "ask on date":
                        y "would you like to go on a date with me?"
                        t "like... right now?"
                        y "yeah, why not."
                        show toi toi07 with dissolve
                        t "s-sure!"
                        y "come on then."
                        $ earthbending = 22
                        jump earthbending_date
                    "just stopping by":

                        y "just wanted to say hey."
                        t "well, thanks."
                        t "you know i'm always happy to see you."
                        y "alright, i'll get out of your hair."
                        y "see you later."
                        scene black with dissolve

            jump love_bk3_village_background

        if earthbending ==22:
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            if toph_chat <=23:
                t "hey!"
                t "why don't you stop by later?"
                y "okay, i will."
                t "great!"
                t "see you then!"
                jump love_bk3_village_background
            else:
                if love_toph_anal2:
                    $ earthbending = 23
                    t "hello... sexy."
                    y "back at you."
                    t "katara wanted to see you."
                    y "oh, okay."
                    y "guess i'll just go answer her summons."
                    y "like i'm a butler."
                    t "...."
                    y "sorry, that was aggressive."
                    y "i'll go say hi!"
                    y "is that better?"
                    t "go on, weirdo."
                    jump love_bk3_village_background
                else:
                    t "hey!"
                    t "why don't you stop by later?"
                    y "okay, i will."
                    t "great!"
                    t "see you then!"
                    jump love_bk3_village_background

        if earthbending ==23:
            scene black
            scene bg_bk3_tophome_day
            show toi toi04
            with dissolve
            t "you should go see katara."
            jump love_bk3_village_background

        if earthbending ==24:
            scene black
            scene bg_bk3_tophome_day
            show toi toi04:
                xpos -125 zoom 1.1
            with dissolve
            y "toph!"
            t "hi, my... my love."
            y "what're you up to?"
            t "nothing much."
            t "....katara's here."
            hide toi with dissolve
            y "what?"
            y "i didn't hear a kno-"
            "toph opens the door to a surprised katara."
            t "come on in."
            show toi toi04:
                zoom 1.1 xpos -125
            show tokp tokp20:
                xzoom -1 zoom .9 xpos -125 ypos 100
            with dissolve
            y "whoa, katara... you look beautiful."
            k3 "thank you aang."
            t "you smell... and seem... confident."
            t "it... works on you."
            t "what's the occasion?"
            k3 "i wanted to see you."
            show toi toi09 with dissolve
            t "...me?"
            k3 "of course."
            show tokp tokp21 with dissolve
            k3 "you're my closest girlfriend."
            t "oh... uh... same."
            k3 "you know..."
            k3 "...never mind."
            t "what?"
            show tokp tokp20
            k3 "maybe the three of us can hang out one night soon."
            show toi toi04 with dissolve
            t "sure, i'd like that."
            k3 "i'd like that, too."
            y "ditto."
            k3 "well... maybe i'll come by one night, and... we can relax together."
            show toi toi09 with dissolve
            t "okay..."
            k3 "how about at aang's house?"
            t "...aang's house?"
            t "i mean... we can do that."
            t "we don't hang out there ever."
            k3 "that sounds like fun, doesn't it?"
            y "yes it does..."
            t "sure."
            k3 "bye!"
            hide tokp with dissolve
            t "...that was weird."
            y "huh."
            t "what?"
            y "i {i}think{/i}... she might have a crush on you."
            show toi toi06
            show toi_blush:
                xpos -125 zoom 1.1
            with dissolve
            t "what? no!"
            t "...shut up!"
            y "ohh... do i sense a little crush back?"
            t "not... no!"
            y "not no?"
            show toi toi05 with dissolve
            t "i meant no!"
            y "alright, alright..."
            y "if you say so..."
            t "oh, go away..."
            y "i'll see you at my place later for our hangout."
            y "don't think too hard about that crush you share..."
            t "get out!"
            $ earthbending = 25
            jump love_bk3_village_background

        if earthbending ==25:
            "the door is locked."
            y "i should meet toph and katara at my place during the night."
            jump love_bk3_village_background

        if earthbending ==26 or earthbending ==27:
            if suki_bar_blow >=7:
                scene black
                scene bg_bk3_tophome_day
                with dissolve
                y "toph?"
                y "where..."
                show toki toki03
                show toki_angry
                with dissolve
                k3 "aang!"
                k3 "toph's been captured!"
                y "what?!"
                show toki toki02 with dissolve
                k3 "i just caught a glimpse!"
                k3 "they put her in a metal box!"
                y "shit!"
                y "where'd they take her?"
                k3 "i can only assume the tunnels."
                y "then that's where i'll go."
                $ bk3love_freetoph = 1
                $ earthbending = 28
                jump love_bk3_village_background
            else:
                scene black
                scene bg_bk3_tophome_day
                show toi toi04
                with dissolve
                t "come back later, okay?"
                t "if you need something to do, i bet tylee or suki probably have something."
                jump love_bk3_village_background

        if earthbending ==28:
            scene black
            scene bg_bk3_tophome_day
            show toki toki02
            show toki_angry
            with dissolve
            k3 "aang!"
            k3 "go rescue toph from the tunnels!"
            jump love_bk3_village_background

        if earthbending ==29:
            if love_smellerbee_sex:
                scene black
                scene bg_bk3_tophome_day
                show toi toi51
                with dissolve
                t "aang."
                y "whoa, you look serious."
                t "it's time."
                y "...you're gonna have to be more specific."
                t "it's earth king time."
                y "...what?"
                t "we need to tell the earth king."
                t "about the war, long feng, everything."
                y "oh, right."
                y "that's a thing."
                t "but i have a feeling that after this there will be changes."
                t "big ones."
                t "no going back."
                y "...you're serious."
                t "yeah."
                t "it's just a sense that i'm getting, but i've learned to trust my gut."
                t "things are gonna start rolling quickly once we do this."
                t "you should make sure you've done everything you want to before we start."
                menu:
                    "start final mission":
                        t "are you sure?"
                        menu:
                            "i understand there's no turning back":
                                y "i'm ready, and i'm sure."
                                t "okay then."
                                t "let's do this."
                                $ earthbending = 30
                                jump bk3_love_final
                            "i'm not ready":

                                t "take your time."
                                jump love_bk3_village_background
                    "i'm not ready":

                        t "take your time."
                        jump love_bk3_village_background
            else:

                scene black
                scene bg_bk3_tophome_day
                show toi toi04
                with dissolve
                t "hey, thanks again for helping me get out of the tunnels."
                y "my pleasure."
                t "I didn't need you, but... it was still a nice gesture."
                y "...right."

                if love_jet_freed:
                    t "hey, were you the one that rescued jet?"
                    y "yup."
                    t "okay, well, i ran into smellerbee in the city."
                    t "she wants to thank you properly for that."
                    y "where in the city?"
                    t "eh, just walk around."
                    t "i'm sure she'll pop up somewhere."
                else:
                    t "hey, any chance you've rescued jet?"
                    y "who?"
                    t "you know, smellerbee's leader?"
                    t "i ran into smellerbee in the city, and she's still looking for him."
                    t "he's probably in the tunnels."
                    t "no doubt near where i was."
                    t "if you rescue him, you should go find smellerbee in the city."
                    t "i'm sure she'll want to thank you."
                    y "i'll keep it in mind."
            jump love_bk3_village_background

label love_toph_peek:


    hide screen earth_money_date
    y "no harm in a quick peek through the window... "
    scene black
    scene bg_bk3_tophome_day
    show toph_windowsil
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
    scene black with sshake
    show ctc
    pause
    hide ctc
    $ caught_peeking = True
    $ toph_angry = 2
    jump love_bk3_village_background

label toph_chat1:
    y "how are you holding up?"
    show toi toi09 with dissolve
    t "what do you mean?"
    y "well... things are a little wild at the moment."
    y "i want to make sure you're doing okay."
    show toi toi10 with dissolve
    t "oh."
    show toi toi09 with dissolve
    t "um..."
    t "i'm doing okay."
    t "i guess things are kinda weird right now, aren't they?"
    y "that's an understatement."
    y "did you know i apparently have a sky buffalo?"
    t "......."
    t "it's a bison. a skybison."
    t "and yes i knew that."
    t "we flew on it."
    y "we {size=+5}{i}did{/i}!?!"
    t "......"
    show toi toi08 with dissolve
    t "shut up, quit teasing me."
    y "alright, alright."
    y "(damn, i wanna fly on a skycow...)"
    y "(stupid lady spirit makes sure i miss all the fun stuff.)"
    show toi toi09 with dissolve
    t "are {i}you{/i} okay?"
    t "you spaced out a little."
    y "yeah, i'm fine."
    y "well... really, i'm flying by the seat of my pants here."
    y "metaphorically."
    y "we really need to find the skybison so i can do that literally."
    t "....."
    y "come on, you don't have to play cool with me."
    t "it's..."
    show toi_blink with dissolve
    t "......"
    t "things are... hard right now."
    t "i don't want to go into all of it."
    t "not right now, anyway."
    hide toi_blink with dissolve
    t "but thanks for asking."
    y "any time."
    t "........."
    y "........."
    show toi toi12
    with dissolve
    t "oh, shut up."
    t "dork."
    show toi toi04 with dissolve
    t "get out of here, i need to get some sleep."
    y "i'm out! i'm gone."
    show toi_blink with dissolve
    t "and aang...."
    y "yeah?"
    t "...."
    hide toi_blink with dissolve
    t "thanks."
    play sound "audio/thud.mp3"
    scene black with sshake
    "toph slams the door in your face."
    y ".........."
    y "{size=+5}we need to work on your people skills!!"
    y ".........."
    y "i should go."
    $ toph_chat +=1
    "you head home for the night."
    jump love_bk3_next

label toph_chat2:
    y "what are you up to?"
    show toi toi06 with dissolve
    t "i'm worried about your training."
    t "i need to think through the best way to go about it."
    y "i think you're doing fine."
    show toi toi09 with dissolve
    t "thanks, but... there's more to be done."
    t "but i'm also worried about the girls in the tunnels."
    y "same."
    t "let's try to work on those two things, okay?"
    y "yeah, we'll do it."
    $ toph_chat = 2
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat3:
    y "how are you?"
    show toi toi06 with dissolve
    t "hmm?"
    show toi toi09 with dissolve
    t "oh... i'm fine..."
    y "...."
    y "you do know that i can see your expressions, right?"
    t "my exp... oh."
    y "you're clearly upset about something."
    y "what is it?"
    t "it's..."
    t "i'm... embarrassed that you saw my... my chest."
    t "naked."
    y "what? really?"
    y "why?"
    y "it's not the first time i've seen a pair, let me tell you."
    t "because it's... private..."
    t "and..."
    t "......"
    show toi toi06
    show toi_blink
    with dissolve
    t "...i'm embarrassed about my boobs, okay?"
    t "they're so small, i might as well be a boy."
    t "i hate them so much!"
    y "...is that all?"
    hide toi_blink
    show toi toi10
    with dissolve
    t "what?"
    y "you have {i}perfect{/i} tits."
    show toi toi06 with dissolve
    t "you don't have to humor me."
    y "no, i'm serious."
    y "they're perky and so. damn. cute."
    y "i just wanna nibble on them."
    show toi toi09 with dissolve
    t "....r-really?"
    t "you mean that?"
    y "yeah!"

    y "they fit your shape better than some bulky things, and i really like your shape."
    t "you do?"
    y "it's great! i can just throw you over my shoulder."
    t "....."

    show toi toi04 with dissolve
    t "shut up..."
    y "or put you in my pocket."
    show toi toi08 with dissolve
    t "i'm not {i}that{/i} tiny..."
    y "sure you are!"
    y "have you seen yourself in a mirror?"
    show toi toi04 with dissolve
    t "i haven't seen anything."
    y "......"
    t "......"
    y "......"
    show toi toi07
    show toi_blink
    with dissolve
    t "hahahaha!!!"
    y "hahaha!"
    hide toi_blink with dissolve
    t "hahaha..."
    t "heh..."
    t "alright, thanks."
    t "i needed that."
    y "my pleasure."
    y "and hey, if you ever get insecure, i'll be happy to fondle-"
    t "oh, shut up and get out."
    t "i'll see you later, aang."
    $ toph_chat = 3
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat4:
    y "what are you up to?"
    show toi toi06 with dissolve
    t "i'm worried about the girls in the tunnels."
    t "sorry, aang... I don't feel up for chatting right now."
    t "i'm too anxious."
    y "i understand."
    $ toph_chat = 4
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat5:
    y "yo, toph."
    show toi toi02 with dissolve
    t "yo, aang."
    t "thanks for going back into the tunnels."
    t "i met june."
    t "she seems... fun."
    y "fun? you think she's fun?"
    show toi toi07 with dissolve
    t "yeah! she's a total badass!"
    show toi_blink with dissolve
    t "she's got nothing on me, but then who does?"
    y "I... guess."
    hide toi_blink
    show toi toi04
    with dissolve
    t "oh, katara wanted to talk to you."
    y "now?"
    t "whenever you get a chance."
    t "she's... pretty excited."
    y "about what?"
    show toi toi07 with dissolve
    t "you'll see."
    t "goodnight."
    $ toph_chat = 5
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat6:
    t "hey, that was... fun. after the party."
    t "thanks for that."
    show toi toi09 with dissolve
    t "i know i'm sometimes... well... whatever."
    t "thanks for being cool, i guess."
    t "katara wants to talk to you again."
    t "don't ask me what about."
    $ toph_chat = 6
    jump toph_night_menu

label toph_chat7:
    t "hey, i know you were probably joking about grabbing my boobs..."
    y "no, i wasn't."
    show toi toi09 with dissolve
    t "right..."
    t "i just... i want you to know..."
    t "if i was to let anyone do that... it would be you."
    y "really?"
    show toi toi06 with dissolve
    t "don't make a big deal out of it."
    ym "you liiiike me..."
    show toi toi05 with dissolve
    t "shut up, bozo!"
    ym "you like me, you like me!"
    show toi toi51 with dissolve
    t "get out of my house!"
    y "hey."
    t "wha-"
    hide toi
    show tonf tonf22
    show expression "bk3/toph/lovetits/kissface_caress_9.png"
    with Dissolve(1)
    "you grab toph and pull her towards you, firmly and swiftly."
    "she's so small and unresistant in your arms, accepting where you take her."

    with pflash
    "you give her an empassioned kiss... she presses her face into yours."
    "she's clearly inexperienced, but she puckers her lips and lightly parts them for you."
    "you flick your tongue lightly in that little gap, and she lets out a soft moan..."
    "but you pull back before being any more intrusive."
    hide expression "bk3/toph/lovetits/kissface_caress_9.png"
    show tonf tonf23
    with Dissolve(1.5)
    t "....oh."
    t "i..."
    show tonf tonf20 with Dissolve(1)
    t "that...."
    t "we...."
    $ toph_footjob_barechest = False
    scene black
    scene bg_bk3_tophome_0
    show tofj tofj09
    show tofj_blush
    with Dissolve(1.5)
    "toph sinks to the floor."
    y "toph? are you okay?"
    t "It's... haha... embarassing..."
    y "what's wrong?"
    t "My... legs gave out."
    y "they-"
    y "Oh."
    y "god damn it you're cute."
    show tofj_blink_ani
    t "you... really think so?"
    y "yeah, i really do."
    hide tofj_blink_ani
    t "well... i think i'm going to be here for... a little while longer."
    t "you have things to do."
    t "I'll see you later."
    y "bye..."
    t "bye!"
    scene black with dissolve
    "you head home for the night."
    $ toph_chat = 7
    jump love_bk3_next

label toph_chat8:
    t "you're doing really well with your training."
    t "you're picking it up really quickly."
    y "thanks-"
    show toi_blink with dissolve
    t "for a froofy fighter like you."
    y "...."
    y "....backhanded complement there, just gonna ignore that...."
    hide toi_blink
    show toi toi09
    with dissolve
    t "hey... aang?"
    y "hmm?"
    t "I... well..."
    show toi_blush with dissolve
    t "sorry again for being difficult about the brothel."
    t "i'm sure it'll be a big help around here."
    menu:
        "it was annoying":
            y "it was a little frustrating."
            show toi_blink with dissolve
            t "oh."
            t "sorry."
        "no worries":
            y "don't sweat it."
            show toi_blink with dissolve
            t "thanks."
    t "......."
    y "......."
    y "awkward silences are awk-"
    hide toi_blink
    hide toi_blush
    show toi toi02
    with dissolve
    t "hey, are you ever gonna upgrade your house?"
    y "...and i guess we're moving on."
    t "yeah. so. gonna upgrade your house?"
    menu:
        "yes":
            y "eventually."
            y "i don't want to keep living in a shack forever, you know?"
        "no":

            y "i doubt it."
            y "it's just a place to sleep."
        "haven't thought about it":

            y "i haven't really thought about it."
            y "hasn't seemed that important, honestly."

    t "well, you should."
    show toi toi04 with dissolve
    t "that little shack is tiny."
    y "it kind of is, yeah."
    y "but what about you?"
    show toi toi09 with dissolve
    t "what do you mean?"
    y "you've got this big place to yourself."
    y "i mean... you've got {i}rooms{/i} here."
    y "plural."
    t "it's..."
    show toi_blink with dissolve
    t "...okay."
    menu:
        "pry":
            y "what do you mean?"
            t "I..."
            t "it's nothing, never mind."
            y "come on."
        "wait":

            y "......"
            t "i...."
            t "......."

    hide toi_blink
    show toi_blush
    with dissolve
    t "it's... lonely."
    y "i get that."
    y "it's lonely at my place, too."
    t "well... maybe..."
    show toi_blink with dissolve
    t "we can have a sleepover or something."
    hide toi_blink with dissolve
    y "i think..."
    y "...that would be fun."
    show toi toi04 with dissolve
    t "oh. good."
    t "well..."
    t "you should definitely upgrade your house, then."
    t "maybe i'll come by some time and see it."
    y "that makes sense..."
    y "can't pick up chicks with a messy pad."
    show toi_blink with dissolve
    t "shut up."
    scene black with dissolve
    "you head home for the night."
    $ toph_chat = 8
    jump love_bk3_next

label toph_chat9:
    y "i upgraded my house, like you suggested."
    t "that's great, aang!"
    y "want to come check it out?"
    show toi_blush with dissolve
    t "i'd... i'd be happy to."
    scene black with dissolve
    scene inside_shack
    show toi toi04
    with dissolve
    y "well... here we are."
    t "it's nice."
    t "i mean, i don't know what color the walls are, but it certainly feels spacious."
    show toi toi09
    with dissolve
    t "did you add a room?"
    t "is that the main renovation?"
    y "yeah, good eye... er... foot."
    t "...."
    show toi toi07
    show toi_blink
    with dissolve
    t "hahaha!"
    hide toi_blink with dissolve
    t "you always manage to make me laugh."
    show toi toi04 with dissolve
    t "i don't know how you do it, but..."
    t "i really enjoy your company."
    y "thanks. and likewise."
    t "hey... i'm feeling a little claustrophobic."
    t "want to go for a walk?"
    menu:
        "that sounds nice":
            y "sure, i think that's a nice idea."
            jump toph_walk
        "not right now":

            y "another time."
            show toi toi09 with dissolve
            t "oh..."
            t "okay."
            t "just... let me know, then."
            scene black with dissolve
            "toph heads home for the night."
            $ toph_walk_talk = True
            jump love_bk3_next

label toph_chat10:
    show toi toi09 with dissolve
    t "Ehmm... Aang?"
    y "yeah?"
    t "answer me honestly..."
    y "zero promises."
    t "....."
    t "did..."
    t "...did you do something to those three girls who treated me like a kid?"
    y "The ones in the city, acting like a pack of hyenas?"
    t "...yes."
    y "Nothing that you don't already know about. Why?"
    show toi_blink with dissolve
    t "Well, there's talk about three girls disappearing recently."
    t "From what I can gather, they might be the same girls who pestered me."
    y "I got nothing to do with that."
    hide toi_blink with dissolve
    t "Could you please try and find them?"
    t "Maybe they're somewhere in the maze?"
    y "....seriously? why?"
    show toi toi06 with dissolve
    t "because even though they were total jackals-"
    y "hyenas."
    show toi_blink with dissolve
    t "hyenas..."
    hide toi_blink
    show toi toi09
    with dissolve
    t "we're trying to rescue people from the tunnels, right?"
    y "i guess..."
    y "...but those three had it coming."
    t "you already got them back for that."
    t "look, aang... you don't have to like it, but can you still try?"
    y "i didn't figure you for being such a softy."
    show toi toi06 with dissolve
    t "i'm not soft!"
    show toi toi09 with dissolve
    t "i'm just not heartless."
    y "alright, alright. I guess I could take a look."
    show toi toi04 with dissolve
    t "thanks, aang."
    $ toph_chat = 10
    scene black with dissolve
    "you settle in for the night."
    jump love_bk3_next

label toph_chat11:
    show toi toi09 with dissolve
    t "did you find those three girls?"
    if meangirls_escapedmaze ==0:
        y "not yet."
    if meangirls_escapedmaze >=1:
        y "i... found them, yes."
        t "were they happy to see you? did you set them free?"
    if meangirls_escapedmaze ==1:
        y "....."
        y "um."
        y "i found them?"
    if meangirls_escapedmaze ==2:
        y "yeah they were very happy when i let them go... er, freed them."
    if meangirls_escapedmaze ==3:
        y "yup, and sent them on to katara."
        y "so next time you see them... well, they owe us big time."
        y "so... you know..."
        y "if you have any ideas, let me know."
    if meangirls_escapedmaze ==0:
        t "oh...."
        show toi toi04 with dissolve
        t "well, i'm sure you'll find them!"
        show toi toi08 with dissolve
        t "part me of me wants them to suffer..."
        show toi toi09 with dissolve
        t "but i don't want them kidnapped."
        t "please try to find them, okay?"
        y "i'll work on it."
        show toi toi04
        show toi_blink
        with dissolve
        t "thanks."
    else:

        show toi toi04 with dissolve
        t "that's great!"
        t "thanks for doing that, aang."
        show toi toi08 with dissolve
        t "part of me wants them to suffer..."
        show toi toi09 with dissolve
        t "...but not that much."
        t "not for just some teasing."
        y "you're a good person."
        y "a better person than me."
        show toi toi04 with dissolve
        t "that's not true."
        show toi_blink with dissolve
        t "we'll agree to disagree."
    show toi toi09
    hide toi_blink
    with dissolve
    t "umm...."
    y "yeah?"
    t "you know how... i have... some bad dreams?"
    y "you mean \"tear-the-house-down night terrors\"?"
    y "I'm familiar."
    t "um... yes."
    t "well, i had an idea."
    t "but..."
    show toi_blink
    show toi_blush
    with dissolve
    y "but what?"
    t "it's embarassing."
    y "then i'm in!"
    hide toi_blink with dissolve
    t "......"
    t "it's... ugh..."
    y "spit it out, babe."
    show toi toi10
    hide toi_blush
    show toi_blush
    with dissolve
    t "...."
    y "what?"
    t "you..."
    show toi toi04
    hide toi_blush
    show toi_blush
    with dissolve
    t "you called me \"babe\"."
    y "I did, yeah."
    t "......."
    show toi_blink with dissolve
    t "okay."
    y "okay, what?"
    t "just..."
    hide toi_blink with dissolve
    t "...okay."
    y "....."
    y "are you going to tell me what you'd like?"
    t "It's...."
    t "would you..."
    show toi toi09
    hide toi_blush
    show toi_blush
    with dissolve
    t "read me a story?"
    y "....that's it?"
    t "yeah."
    show toi_blink with dissolve
    t "i can't read... obviously..."
    t "and i was hoping maybe hearing a story before bed would help me sleep."
    y "...really?"
    hide toi_blink
    with dissolve
    t "my parents..."
    t "...never really had time for me."
    t "they treated me well enough, i guess..."
    t "but they worried that reading me stories would remind me that i can't read..."
    show toi toi06 with dissolve
    t "and they assumed i was too fragile to handle it."
    y "okay, so what makes you think a bedtime story will help you sleep?"
    show toi toi09 with dissolve
    t "we... used to have a maid that would read to me some nights."
    t "i always slept my best when she did."
    show toi toi06 with dissolve
    t "my parents fired her, of course."
    t "thinking they knew best."
    show toi toi09 with dissolve
    t "but i'm hoping... you'll help me have some peaceful sleep again."
    show toi_blink with dissolve
    t "i... don't know who else to ask."
    t "i'm really embarrassed about it."
    y "yeah, of course."
    show toi toi04
    hide toi_blush
    show toi_blush
    hide toi_blink
    with dissolve
    t "Really?"
    y "don't stress it."
    t "thanks, aang."
    y "i'll pick a book up tomorrow."
    show toi_blink with dissolve
    t "that would be... very appreciated."
    hide toi_blink with dissolve
    t "...goodnight, then."
    y "goodnight."
    scene black with dissolve
    "you settle in for the night."
    $ toph_chat = 11
    jump love_bk3_next

label toph_chat12:
    $ toph_chat = 12
    t "so, did you find a story?"
    y "sort of..."
    y "the selection was limited."
    y "so... it's going to be a little... risque."
    t "sounds like fun."
    t "let's sit!"








    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"
    show toff toff01
    with dissolve
    show ctc
    pause
    hide ctc
    t "alright!"
    t "i'm ready when you are!"
    menu:
        "get to the story":
            pass
        "\"take off your clothes!\"":

            y "before i begin..."
            y "you should get comfortable."
            t "i am comfortable."
            y "by taking off your clothes."
            t "......."
            t "....heh."
            t "maybe another time."

    y "there's... a few pages missing."
    y "so i'm just gonna have to start sort of in the middle."
    t "that's fine."
    t "i'm interested in what you've picked for us."
    y "....."
    y "ahem."
    y "\"he'd always noticed her feet, from the first moment they met.\""
    y "\"she was small and lithe - perfect for hugging or throwing around - but her feet were the real perfection.\""
    t "........."
    y "...ahem."
    y "\"they faced each other, an air of expectation and anxious hesitation between them.\""
    y "\"she knew what he wanted... and might even be enjoying his discomfort.\""
    y "\"he opened his mouth, uncertain of what to say, when she widened her smile into a predatory grin.\""
    y "\"she spread her legs - slowly, almost casually - in a sultry invitation that froze him in place.\""
    t "........"
    show toff toff00 with dissolve
    t "........."
    show ctc
    pause
    hide ctc
    y "....."
    y "......ahem."
    y "\"she was something between a maiden and a tiger...\""
    y "\"she had a stubborn determination to always get what she wanted... it was a trait he admired in her...\""
    y "\"...but she was a virgin. pure as a snowy midnight.\""
    y "\"she had never seen or felt a penis, despite a new growing, burning interest.\""
    y "\"torn between fascination and hesitancy, she attempted to put him at ease with a simple compliment... and invitation.\""
    y "\"she-"
    t "aang, have i told you lately how strong you've become?"
    t "i'm sure... you must have a great body with all the training we've been doing."
    t "i'd... love to feel it."
    y "umm...."
    t "....keep reading."
    y "....ahem."
    y "\"spurred by her intimacy and flattery, he started to shed his clothing.\""
    y "\"as he began removing his robe and wizard hat, he checked to see if he hadn't misread her tone...\""
    y "\"...but she simply looked at him, waiting for him to lay down and reveal himself.\""
    t "......"
    y "......"
    y "..............."

    show toff toff02 with Dissolve(2.0)

    y "\"he found himself suddenly naked... prostrate before her delicate feet...\""
    y "\"anxious and trembling.\""
    y "\"sensing his hesitation, and coupled with her own desire to feel her first penis...\""
    y "\"she stretched her toes out and gently wrapped them around his cock.\""

    show toff toff03 with dissolve
    t "*oh!*"
    t "Mmmm...."
    show ctc
    pause
    hide ctc
    y "\"surprised by her own confidence, she pressed forward in her discovery of him...\""
    y "\"testing him and watching his face as she explored his growing manhood.\""
    y "\"with alternating strokes, she gripped and rubbed the length of his shaft.\""
    show toff toff04
    show ctc
    pause
    hide ctc
    y "ohhh... ah..."
    t "....keep reading."
    y "\"massaging his cock with steady, even strokes, she bent her legs to better cup his member in her arches.\""
    y "\"seeing with her feet, she watched and studied the head of his penis as it peaked through her arches...\""
    y "\"...only to be swallowed back into her feet.\""
    y "\"she... ah... she could hear him softly groaning, the sound drawing a hungry need from inside her.\""
    y "\"she blushed with a unfamiliar but pleasureable wet heat.\""
    y "\"feeling... feeling him... ah... begin to thrust into her supple grip, she... ah... sped up.\""

    show toff toff05
    show ctc
    pause
    hide ctc

    y "Hnngh..."
    y "oh, spirits..."
    t "keep going..."
    y "\"her vigor brought out new fervor between them as he thrust and humped in rhythm with her friction.\""
    y "\"he fuck... fucked her smooth and firm feet, wet with sweat and precum, drawing closer to orgasm...\""
    y "\"when she suddenly... slowed?\""

    show toff toff04
    y "......."
    y "you-"
    t "shh."
    t "don't stop."
    y "that's {i}my{/i} line."
    t "go on...."
    y "........"
    y "\"she cooed that she wanted his cum... but wanted to wait... until his balls were swollen and ready to cover her little feet.\""
    y "\"seeing him enraptured and momentarily wrapped around her metaphorical finger...\""
    y "\"she couldn't help but ask him a question she's wondered for a long time.\""

    show expression "bk3/toph/footjob3/unsure.png":
        xpos 0 ypos 0
    t "....."
    t "aang...?"
    t "Do... do you think I'm pretty?"
    y "You know I do."
    hide expression "bk3/toph/footjob3/unsure.png"

    t "hehe, I just like hearing you say that."
    t "Do you think I'm... prettier than... I dunno... Katara?"

    menu:
        "Way prettier, but don't tell Katara I told you that":
            y "much prettier, but please don't tell her i said that."
            pass
        "You're both pretty in your own way":
            y "you're both pretty."
            show toff toff02 with dissolve
            t "........"
            t "Oh, look at the time."
            t "I've got some stuff to do."
            y "Waait..."
            t "oh?"
            y "i take it back!"
            y "you're much prettier!"
            show toff toff04 with dissolve

    t "really?"
    t "you're not just saying that?"
    t "...because i have your cock between my toes?"
    y "it's not between your toes."
    show toff_lewd
    t "are you sure?"
    show toff toff08 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    t "now keep reading."
    y "........."
    y "\"....she gripped the head of his cock with her nimble toes... squeezing and tugging at the soft underside of his cock's head.\""

    show toff toff06
    show ctc
    pause
    hide ctc
    y "\"surprised by her skill, he looked at her inquisitively, to which she gave a simple answer.\""
    t "...When you go barefoot all the time, you pick up a trick or two."

    y "\"...still gripping him between her little toes, she pumped him with an unbelievable, unparalleled expertise."
    y "\"he found himself lost in a world of bliss as she licked her lips and stared... focusing on his swollen, pulsing member.\""
    y "f-fuuuck... that feels nice."
    t "Maybe it'll feel even better when I do this."

    show toff toff07
    y "Oh, fuck..."
    y "nnghh..."
    t "finish the story, aang."
    t "i want to know how it ends."
    y "\"she... she sped her pace, pumping him to the brink.\""
    y "\"her small toes flexing and curling teasingly around his thrusting cock as he slid in an out...\""
    y "\"fucking and pounding even deeper into her feet at an accelerated pace.\""
    y "\"she wiggled her toes, and in a whisper began to beg for it... to beg for his thrusts... his cum...\""
    show expression "bk3/toph/footjob3/unsure.png":
        xpos 0 ypos 0
    hide toff_lewd
    t "..........."
    t "ummm....."
    t "{size=-3}...give... give me your cum, aang..."
    t "{size=-3}give it to me... let it... out..."
    t "{size=-3}fuck my feet... fuck my cute little feet..."
    y "ohhh... yes... yeah... unnhh..."

    hide expression "bk3/toph/footjob3/unsure.png"
    t "......."
    t "...don't hold back... thrust... yeah... fuck them... fuck them..."
    y "ungh... ohh..."
    show toff_lewd
    t "{size=+3}ugh... yes... fuck... that's it... fuck my feet, aang! fuck them! ughhn!"
    y "ohhh... toph... toph, i... i..."

    t "r-read... read the end... the... the end..."
    y "\"cup... ah... cupping the head of his cock with her foot and toes... she... ah... she squeezed once, hard... and...\""
    show toff toff09
    t "like this?"
    y "unngh!!"
    show ctc
    pause
    hide ctc
    y "\"he... nnghh.... shot... a... a... desperate, built up cumload right into her... her... toes...\""
    t "her what?"
    y "Her... her fucking..."
    y "hhgng!!"
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/footjob3/sperm1.png"
    pause
    y "Fuck!"
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/footjob3/sperm2.png"
    $ renpy.pause()
    t "yes, aang..."
    t "shoot it into my toes..."
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/footjob3/sperm3.png"
    $ renpy.pause()
    y "unnhh.... damn..."
    y "....phew...."
    y "you just... prevented me from painting the ceiling white..."
    "toph lets out a little giggle... unlike her usual persona."
    t "hehe!"
    y "ahh... damn, girl."
    hide toff_lewd
    t "that was... a good story."
    y "i wholeheartedly agree."
    t "we should do that again some time."
    y "fucking... agreed..."
    t "....."
    t "i got to... feel your penis."
    y "I know."
    y "how was it?"
    t "hotter than i expected."
    t "and... not just in temperature."
    t "okay, i need to go clean off."
    t "umm.... goodnight!"
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you settle in for the night."
    jump love_bk3_next

label toph_chat13:
    $ toph_chat = 13
    show toi toi04 with dissolve
    t "i'm glad you came by tonight."
    t "i want to..."
    show toi toi09 with dissolve
    t "i want to thank you."
    t "and... apologize."
    t "i know i've been a little emotional lately."
    show toi toi06 with dissolve
    t "which is not how i usually am."
    show toi toi09 with dissolve
    t "and... it's kind of taking me by surprise."
    y "you really don't need to apologize."
    y "it's all very normal."
    t "oh."
    show toi toi04 with dissolve
    t "good."
    t "then i'll stop worrying about it."
    show toi toi09 with dissolve
    t "i can't promise i won't cry on your shoulder again, though..."
    y "i look forward to it."
    t "you.... really?"
    y "yeah, any time with you is better than being without you."
    show toi toi10 with dissolve
    t "........"
    show toi toi11 with dissolve
    t "you... you..."
    y "what's wrong?"
    t "you're just..."
    t "you make me feel so..."
    show toi toi05
    show toi_tears
    with dissolve
    t "damn it!"
    t "how do you keep doing this to me?!"
    y "doing what?"
    show toi toi11
    hide toi_tears
    with dissolve
    t "you make me feel... weak and... unsure and... happy and..."
    t "and..."
    show toi toi06
    show toi_tears
    show toi_blink
    with dissolve
    t "damn it, i don't know what i'm doing!"
    y "what?"
    t "I like you, okay?!"
    t "i like you a lot!"
    t "so if you don't feel the same about me... then..."
    y "of course i like you, too."
    show toi toi09
    hide toi_blink
    with dissolve
    t "you... do?"
    y "what? obviously."
    y "we've spent a lot of time together, which i've really enjoyed."
    y "i wouldn't be doing these things with you if i didn't really like you."
    t "...oh."
    y "haven't we already talked about this?"
    t "i just... i find it hard to believe, i guess."
    hide toi_tears with dissolve
    t "i'm sorry if i'm... being insecure or something."
    t "....."
    show toi toi06 with dissolve
    t "ugh!"
    t "I hate this!"
    t "this isn't me!"
    t "why am i so damn touchy-feely lately?"
    t "ugh!"
    ym "hahaha!"
    y "it's okay, really."
    y "take a deep breath, toph."
    y "i like you, you like me."
    y "that makes me happy."
    show toi toi04 with dissolve
    t "it... does?"
    y "yeah, obviously."
    y "why do you keep acting so surprised?"
    show toi toi09 with dissolve
    t "I just... don't know what i'm doing here."
    t "you seem so much more experienced than me at this for some reason..."
    t "and i'm just trying to keep up, and..."
    t "and it's all..."
    show toi toi05
    show toi_blink
    with dissolve
    t "......"
    t "can we talk about something else?!"
    y "...yeah, sure."
    show toi toi09
    hide toi_blink
    with dissolve
    t "I..."
    t "sorry."
    show toi toi06
    show toi_blink
    with dissolve
    t "There i go apologizing again!"
    t "ugh!"
    t "I'm... i'm going to bed."
    show toi toi09
    hide toi_blink
    with dissolve
    t "goodnight, aang."
    t "I... i'll talk to you tomorrow."
    t "when i'm... more {i}me{/i} again."
    y "i completely understand."
    y "get some rest."
    show toi_blink with dissolve
    t "....."
    scene black with dissolve
    "you let yourself out and head home for the night."
    jump love_bk3_next

label toph_chat14:
    $ toph_chat = 14
    t "oh. uh, hi aang."
    t "this isn't the best time."
    show toki toki01:
        xzoom -1
    with dissolve
    k3 "alright, i got the-"
    k3 "aang!"
    k3 "what are you doing here?"
    y "i just stopped by."
    y "why are you here?"
    t "katara and i are hanging out."
    y "Oh... i can go..."
    t "no, stay!"
    t "if... that's okay with you, katara."
    k3 "definitely!"
    k3 "we were just talking about relationships."
    show toi toi10 with dissolve
    t "katara!"
    show toki_blink:
        xzoom -1
    k3 "oh, relax."
    k3 "i didn't mention any particulars."
    show toi toi09
    show toi_blush
    with dissolve
    t "still..."
    hide toki_blink
    show toki_smile:
        xzoom -1
    with dissolve
    k3 "how about you, aang?"
    k3 "got a relationship problem you want to talk through?"
    show toi toi05 with dissolve
    t "no, he doesn't!"
    t "shut {i}up{/i}, katara!"
    y "actually, i do."
    show toi toi09
    hide toi_blush
    with dissolve
    t "you... you do?"
    y "yeah."
    show toki toki02 with dissolve
    k3 "interesting!"
    k3 "let's hear it then."
    t "yeah...."
    t "let's... hear it."
    y "well, there's this cute girl i really like."
    show toi_blush with dissolve
    t "....."
    y "and she's normally this take-charge kind of person."
    t "........."
    y "but she doesn't know anything about relationships..."
    y "...and is feeling really uncertain about what she's supposed to do."
    show toi_blink with dissolve
    t "{size=-3}....this is so embarrassing...."
    k3 "you were saying, aang?"
    y "right, well, it's not like she can ask {i}me{/i} what she should be doing."
    y "Not if she wants to feel like she's independent and strong."
    t ".........."
    hide toki_smile with dissolve
    k3 "hmmm...."
    y "so what do you think, katara?"
    t "yeah, what..."
    hide toi_blink with dissolve
    t "what... do you think...?"
    k3 "well...."
    show toki_blink:
        xzoom -1
    with dissolve
    k3 "i can't tell you what she should do."
    show toi_blink with dissolve
    t "...oh."
    k3 "but...."
    hide toi_blink with dissolve
    k3 "maybe i can tell you about a completely unrelated situation that happened to me."
    t "...oh?"
    y "go on...."
    hide toki_blink with dissolve
    k3 "i was once an... innocent... young girl."
    ym "were you, now?"
    t "aren't... you still?"
    k3 "....."
    show toki_blink:
        xzoom -1
    with dissolve
    k3 "anyway...."
    hide toki_blink with dissolve
    k3 "i was struggling to keep up with an... enthusiastic... young man."
    k3 "as i said... i was very innocent, had never travelled anywhere, had never known anything about men..."
    k3 "besides my brother, but sokka doesn't count."
    k3 "but the key thing i learned, through my many, many, interactions with this... young man..."
    k3 "was how crucial sexual interaction is to a successful, developing relationship."
    t "........."
    y "....really?"
    k3 "oh, definitely."
    k3 "even oral sex."
    k3 "in fact, that's a great way to start."
    t "it... is?"
    k3 "very much so."
    k3 "i couldn't have a strong... fascinating... relationship if i didn't start by sucking some cock along the way."
    show toi toi10 with dissolve
    t "katara!"
    show toki toki01
    show toki_smile:
        xzoom -1
    with dissolve
    k3 "what?"
    k3 "that's what it is."
    k3 "no need to pretend otherwise."
    k3 "we're all friends here."
    show toi toi09 with dissolve
    t "......"
    k3 "but i'm sorry my completely unrelated experience couldn't help with your problem, aang."
    k3 "i guess you'll just have to hope your lady friend realizes what to do on her own."
    y "sigh...."
    y "I suppose you're right."
    y "...you're very quiet over there, toph."
    t "I'm just... thinking."
    hide toki_smile with dissolve
    k3 "aang, i think you should go."
    k3 "leave us to have some girl talk."
    show toki_smile:
        xzoom -1
    with dissolve
    k3 "without a stinky boy around."
    show toi toi04 with dissolve
    t "yeah... no... stinky boys."
    y "alright, alright, i'll go."
    k3 "don't worry, she's in good hands."
    y "i believe it."
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat15:
    t "i've been thinking a lot about... what katara said."
    show toi toi09 with dissolve
    t "and... what you said... and..."
    y "and what?"
    t "and..."
    show toi_blink with dissolve
    t "...and there's something i want to do."
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    hide toi
    show toi toi200
    show toi_blink
    show toi_blush
    with fade
    show ctc
    pause
    hide ctc
    t "......"
    y "well, i like where this is going, but you should still use your words."
    hide toi_blink with dissolve
    t "just take your clothes off."
    jump love_toph_blowjob

label toph_chat16:
    y "that was a lot of fun the other day, toph."
    t "oh, yeah?"
    show toi toi07
    show toi_blush
    with dissolve
    t "did you have a good time?"
    t "cumming in my little teen throat?"
    y "...i don't know what's gotten into you, but i love it."
    show toi toi04
    show toi_blink
    with dissolve
    t "okay, to be fair, i've been getting tips from katara."
    t "now that i'm actually asking her... questions..."
    t "she seems to know a lot of stuff."
    show toi toi09
    hide toi_blush
    hide toi_blink
    with dissolve
    t "it's... a little unnerving, to be honest."
    show toi toi04 with dissolve
    t "but i'm not gonna complain."
    t "and, by the way..."
    show toi_blush with dissolve
    t "I can't stop thinking about it."
    show toi toi07 with dissolve
    t "it was so hot!"
    t "when you were back there..."
    show toi toi09
    with dissolve
    t "licking my... um..."
    y "sweet little cunt?"
    show toi toi04
    show toi_blink
    with dissolve
    t "yes."
    t "it was... so good..."
    y "it's beautiful."
    y "and so's your ass."
    hide toi_blink
    show toi toi09
    with dissolve
    t "my... ass?"
    y "yeah! i love that little butt."
    t "really?"
    y "in the words of a legendary band..."
    y "your buttcheeks is warm... and my kielbasa sausage has just got to perform."
    show toi_blink with dissolve
    hide toi_blink with dissolve
    t "what?"
    y "guess you guys aren't ready for that yet... but your kids are gonna love it."
    t "my what?"
    t "what are you talking about?"
    y "....never mind."
    y "the point is, your butt is amazing and i want it."
    t "...."
    show toi toi04
    show toi_blink
    show toi_blush
    with dissolve
    t "well... maybe you can play with it later."
    y "i am down for that."
    hide toi_blink
    with dissolve
    t "alright, get out of here, i've got to sleep."
    y "aww... alright, alright."
    y "sleep well."
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat17:
    y "how are you?"
    t "i'm great."
    t "worried about-"
    play sound "audio/thud.mp3"
    show toi toi09
    with vshake
    t "what the heck?"
    y "what's all that noise?"
    play sound "audio/thud.mp3" 
    with vshake
    t "i think..."
    show toi toi06 with dissolve
    t "i think it's coming from the brothel... er... boarding house!"
    y "shit, i need to go over there."
    y "we'll pick this up later."
    t "it's fine, go!"
    scene black with dissolve
    "you rush over to the boarding house."
    play sound "audio/thud.mp3"
    "the yelling and banging get louder as you approach."
    y "that's not good."
    y "what's even happening?"
    hide screen earth_money_date
    stop music
    play music "audio/Smooth Lovin.mp3"
    scene black
    scene inside_brothel_1
    show tosi tosi11
    show toti toti02:
        xzoom -1
    with sshake
    $ suki_tylee = 2

    suki "come on, you slut!"
    ya "what the fuck?!"
    suki "none of your slut friends are here to back you up!"
    ty "i don't need them!"
    ty "i don't want to take you down, but i will!"
    suki "just try it, slut!"
    ya "that's enough!"
    show tosi tosi100
    suki "i'm going to beat you within an inch of your slut life!"
    ty "with your cute little paper fans?"
    show tosi tosi102:
        parallel:
            xpos 500
            linear 3.0 xpos 0
            xpos 0
            linear 3.0 xpos 500
            repeat
        parallel:
            ypos 720
            linear 0.4 ypos 750
            ypos 750
            linear 0.4 ypos 720
            repeat
    show toti toti101
    suki "i'm gonna bring the funk!"
    ty "i'm gonna bring the noise!"
    suki "just try it, slut!"
    ty "i'll knock you out before you can even touch me!"
    y "(....this is fucking hilarious....)"
    show ctc
    pause
    hide ctc
    y "(i should probably stop this....)"
    ya "{size=+6}that's enough!" with vpunch
    hide tosi
    show tosi tosi11
    show toti toti02
    with dissolve
    suki "she's wearing a fucking kyoshi outfit!"
    ty "i look cute in it!"
    suki "you have no right!"
    ty "you're angry because i pull it off better!"
    suki "you-"
    y "okay, okay, this arguing is going nowhere."
    y "ty lee, why the fuck are you wearing that?"
    ty "because it's cute, and i wanna."
    suki "see?"
    suki "she has no respect for the history!"
    suki "help me beat her up, aang!"
    y "yeah... that's not happening."
    ty "tell this weirdo to back down, aang."
    ty "before i put her down."
    y "none of that is happening."
    y "ty lee, i don't care how cute you think you look, you need to take that off."
    ty "phooey."
    suki "good."
    suki "and then you-"
    y "suki, ty lee is my guest, and you are going to leave her alone."
    suki "fat chance."
    ya "i'm serious, suki."
    ya "she's under my personal protection and welcome, and you will treat her with respect."
    suki "respect? while she disrespects the heritage of the great kyoshi?"
    suki "your spiritual ancestor?"
    suki "that's not happening."
    ya "then you will at least leave her alone."
    ya "and that is non-debatable."
    ya "because you're right, i am the spiritual descendant of kyoshi, and i'm giving you a direct order."
    suki "......"
    y "and put down your damn fans, you look ridiculous."
    suki "......."
    show tosi tosi10 with dissolve
    suki "....fine."
    y "good."
    y "ty lee, please go to your room."
    show toti toti04 with dissolve
    ty "what did i do?"
    y "please go get changed."
    ty "...oh, fine."
    hide toti with dissolve
    suki "....i'm not forgiving this, avatar."
    y "awfully formal now, i see."
    suki "if you take her side, you're... you're my enemy, too."
    y "even though i am, in a sense, kyoshi?"
    suki "it's... i'm... i don't know..."
    y "go home, suki."
    y "change out of your war gear, lie down, and go to bed."
    y "don't come back to the boarding house, and ty lee won't go to the tavern."
    y "stay out of each other's way."
    suki "...fine."
    hide tosi with dissolve
    y "...this isn't good."
    y "I'll have to talk with her at the tavern later."
    scene black with dissolve
    "tired, you head home for the night."
    jump love_bk3_next

label toph_chat18:
    y "what's going on with you?"
    t "do we... have to talk about it?"
    y "well, no... but it doesn't seem like something that's going away."
    t "...."
    t "okay..."
    t "........."
    y "...well?"
    t "it's my father."
    t "he's...."
    show toi toi11 with dissolve
    t "he's..."
    t "*sniff...*"
    y "okay, okay, relax."
    y "do you want to talk about it tomorrow, maybe?"
    t "okay..."
    t "i need maybe another night to process it."
    y "no worries."
    y "i'll see you another night."
    t "thanks, aang."
    $ toph_chat = 18
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_chat19:
    $ toph_chat = 19
    y "hey, are you ready to talk about... whatever it is?"
    show toi toi06 with dissolve
    t "yes."
    y "well i'm all ears."
    t "it's my father."
    y "and...?"
    t "he's in the city."
    y "what?! seriously?!"
    t "yes."
    t "and he brought muscle."
    y "why....?"
    t "to \"protect\" me!"
    t "he treats me like such a child!"
    show toi toi05 with dissolve
    t "i could kick the ass of any one of the muscle heads he brought for my \"protection\"."
    show toi toi06 with dissolve
    t "he wants to kidnap me and bring me back home."
    t "and i'm not doing it!"
    show toi toi11 with dissolve
    t "I'm... i'm not gonna go!"
    y "hey, hey... it's okay..."
    y "nobody's gonna make you do anything you don't want to do."
    show toi toi05
    show toi_tears
    with dissolve
    t "you got that right."
    y "and even if they tried, I'd stand between you and everyone else."
    y "you're never alone, understand?"
    y "never."
    show toi toi09
    show toi_blink
    with dissolve
    t "....."
    t "oh, aang..."
    t "hey, it's... getting late..."
    y "ah. okay."
    y "i guess i'll go then..."
    hide toi_blink with dissolve
    t "wait!"
    t "...um."
    t "please don't go."
    y "uh... okay..."
    t "will you stay... here? just for tonight?"
    y "sure, i can do that."
    show toi toi04 with dissolve
    t "thanks, aang."
    t "you... you mean the world to me."
    t "goodnight."
    hide toi
    hide toi_tears
    with dissolve
    "toph slunks off to her bedroll."
    y "guess... we're not sharing tonight."
    y "alright."
    y "i'll lay down over... here?"
    "you lay down and try to sleep."
    "doesn't work."
    "so you just lay awake, staring at the walls."
    "......."
    "..............."
    t "aang?"
    t "can you sleep?"
    y "....no."
    y "your floor is literally rock hard."
    t ".........."
    t "...pffahaha!"
    $ toph_top_nude = True
    $ toph_bottom_nude = True
    show toi toi200
    with dissolve
    t "i love that about you, aang."
    t "even when i'm miserable, you can still make me laugh."
    y "it's nice to have a purpose."
    y "also... you're naked."
    t "i know."
    t "i sleep more comfortably that way."
    y "fair enough."
    t "hey..."
    t "were you serious before?"
    t "that you would... protect me?"
    y "always."
    t "and if i reminded you that i don't need protection...?"
    y "i'd tell you that i'm here for when your shield falls."
    y "you carry no weight alone, and if i can ever bear your burdens for you, i will."
    show toi_tears with dissolve
    t "......"
    y "are you okay?"
    t "i..."
    t "i love..."
    t "......"
    show toi_swim_surprise:
        xzoom -1
    hide toi_tears
    show toi_tears
    with dissolve
    t "....watermelons."
    y "......"
    y "excuse me?"
    t "I think i said..."
    show toi_swim_blush:
        xzoom -1
    hide toi_tears
    with dissolve
    t "....i love watermelons."
    y "that's what i thought you said."
    hide toi_swim_surprise
    show toi_blink
    with dissolve
    t "look, i... i really enjoy your company."
    t "you mean everything to me, and..."
    t "i need you."
    t "now."
    y "okay..."
    t "i..."
    hide toi_blink with dissolve
    t "i want you."
    t "in... inside me."
    t "will... you teach me?"
    y "Uh.... yeah, of course."
    t "should i just... get on top of you?"
    y "...."
    y "come over here."
    y "i'm going to sit, and i want you in my lap."
    y "like we've held each other during... some rough nights we've had."
    t "okay..."
    jump toph_shadow_fuck

label toph_chat20:
    $ toph_chat = 20
    t "hi handsome!"
    y "you seem to be in a better mood."
    show toi toi07 with dissolve
    t "of course i am!"
    t "i got stuffed!"
    y "yeah, about that..."
    show toi toi09 with dissolve
    t "hmm?"
    y "you told me i could cum in you, but... aren't you worried about getting pregnant?"
    t "preg... nant?"
    t "what's that?"
    y "{size=+5}what?!?"
    show toi toi07 with dissolve
    t "hahaha!"
    t "Look at your face!"
    t "i mean, i assume."
    show toi toi04 with dissolve
    t "don't worry, i got contraceptives from suki."
    y "you did?"
    y "when?"
    t "she gave me a little box, remember?"
    t "while you were cumming on my little ass?"
    y "oh yeah..."
    y "that's what that was?"
    show toi_blink with dissolve
    t "yup."
    y "huh."
    y "well, in that case..."
    show toi toi09
    hide toi_blink
    with dissolve
    t "in what-"
    scene black with dissolve
    "you lift toph into the air and carry her over to the bedroll, pulling off her clothes in the process."
    t "oh!"
    jump toph_fuckonback

label toph_chat21:
    y "are you feeling more like yourself?"
    show toi toi09 with dissolve
    t "sort of..."
    t "hey, i..."
    t "i could use your help... with my family."
    y "oh, dang."
    y "toph beifong asking for my help."
    y "well, well, well, how the turns have tabled."
    t "...what?"
    y "that's wrong, isn't it?"
    y "how the... turn-tables have... tabled?"
    y "...i give up."
    t "look, i... don't like asking for help."
    y "no! really? i would never have guessed."
    show toi toi04 with dissolve
    t "yeah... it's pretty obvious, huh?"
    show toi toi06 with dissolve
    t "but everyone tries to offer me help."
    t "Like i can't take care of myself."
    t "i'm not... {i}broken{/i}."
    t "my body just... works a little differently."
    t "and i {i}know{/i} how it works."
    t "i {i}made{/i} it work."
    t "and i don't need a savior."
    t "i need people to treat me like a human being, not a newborn puppy."
    y "aw, puppies..."
    show toi toi04
    show toi_blink
    with dissolve
    t "*sigh...* darn it, aang..."
    t "pay attention."
    y "right, sorry."
    hide toi_blink
    show toi toi06
    with dissolve
    t "i don't like seeming needy, because it reinforces the idea that i can't handle anything."
    t "it just takes one request and suddenly i'm a child again in their eyes."
    t "but..."
    show toi toi04 with dissolve
    t "i trust you, aang."
    t "i help you, and you help me."
    t "so... i'm going to let you help me."
    y "....that's a weird way to phrase that."
    y "...thank you?"
    show toi toi09 with dissolve
    t "no! sorry!"
    t "i didn't mean..."
    t "i just meant that i'll let you... that i finally accept..."
    y "i get what you mean, take a breath."
    show toi toi04 with dissolve
    t "thanks... sorry."
    y "is this new perspective caused by whatever happened the other night?"
    show toi toi09 with dissolve
    t "what do you mean?"
    y "when you disappeared for a bit during our... ugh... walk."
    show toi toi07 with dissolve
    t "are you still mad that you had to exercise?"
    ya "it's not a walk if you spend most of it running, toph!"
    t "okay, pumpkin."
    y "anyway, you said you spoke to someone."
    show toi toi09 with dissolve
    t "yeah."
    y "so...?"
    t "well, when i was running from the guards..."
    t "i stumbled into this tea shop being run by some old guy."
    y "ah, iroh."
    t "no... that wasn't his name."
    t "It was... mushy or something."
    t "mushi, maybe?"
    t "he was just this old dude."
    y "oh."
    y "okay..."
    y "so... what'd you talk about?"
    t "well...."
    scene black with Dissolve(1.5)
    hide screen earth_money_date
    stop music
    play music "audio/Ripples.mp3"
    scene jasmin_dragon_inside
    show toii toii02
    show toi toi07:
        xzoom -1
    show toi_blush:
        xzoom -1
    show screen fuzzy_edges
    with Dissolve(1.5)
    t "whew!"
    t "ha!"
    t "i am a {i}beast{/i}!"
    show toii toii03 with dissolve
    iroh "are you now?"
    show toi toi10
    with dissolve
    t "ah!"
    t "who are you?"
    show toii toii02 with dissolve
    iroh "i'm ir... mushi."
    show toi toi09 with dissolve
    t "you're irmushi?"
    show toii toii01 with dissolve
    iroh "...just mushi."
    iroh "you look a little winded... your face is pretty red."
    t "well, yeah, i just outran a bunch of guards."
    show toii toii06 with dissolve
    iroh "great, more of that..."
    iroh "i'll have to \"donate\" more tea..."
    show toii toii05 with dissolve
    iroh "well, you're safe here."
    iroh "the guards usually ignore my humble little establishment."
    show toii toii01 with dissolve
    iroh "here..."
    t "what's this?"
    iroh "it's tea."
    show toii toii02 with dissolve
    iroh "pretty good tea, if i say so myself."
    hide toi_blush with dissolve
    t "oh... uh... thanks."
    iroh "if you don't mind me saying so..."
    iroh "you look a little young to be on your own."
    show toi toi06 with dissolve
    t "yeah? well, you look a little too old to be on your own."
    show toii toii06 with dissolve
    iroh "ouch..."
    iroh "we'll just see if you get a second cup of tea, then."
    t "i don't want a second cup of tea."
    show toii toii07 with dissolve
    iroh "well, that's obviously a lie."
    t "no, it's not."
    iroh "it's okay, you don't need to pretend."
    iroh "...."
    show toii toii05 with dissolve
    iroh "ah, i can't do that to you!"
    iroh "here, i'll pour you another!"
    show toi toi09 with dissolve
    t "i... haven't finished this one..."
    show toii toii07 with dissolve
    iroh "are you sick?"
    show toi toi06 with dissolve
    t "no!"
    t "and i don't need you taking care of me!"
    t "people see me and think i'm weak and can't take care of myself."
    t "but i can take care of myself {i}by{/i} myself."
    t "i don't need anyone!"
    show toii toii03 with dissolve
    iroh "hmmm...."
    t "what? you have something to say, old man?"
    iroh "......"
    show toii toii02
    show toii_blink
    with dissolve
    iroh "you remind me of my nephew."
    t "great, i'm a boy, thanks."
    iroh "no..."
    iroh "he, too, always thinks he needs to do everything on his own, without support."
    show toii toii01
    hide toii_blink
    with dissolve
    iroh "there's nothing wrong with letting people who love you help you."
    show toii toii06 with dissolve
    iroh "not that i love you... i just met you..."
    show toi toi09 with dissolve
    t "..."
    t "where's your nephew?"
    show toii toii01
    show toii_blink
    with dissolve
    iroh "lost, unfortunately..."
    iroh "he's struggling to find himself."
    t "lot of that going around..."
    iroh "yes..."
    iroh "i had hoped that having someone around, that loves him unconditionally, would help..."
    iroh "i have found that if you're determined to believe something..."
    iroh "in this case, that you're alone..."
    iroh "...you make yourself that way."
    iroh "ah, but i believe in him, and i hope it someday helps him believe in himself."
    t "oh."
    t "that's... a lot to take in at once..."
    iroh "the right choices are rarely the simple ones."
    hide toii_blink with dissolve
    iroh "i don't know you, but... you seem like someone who can make the right choices."
    t "i... i don't know..."
    show toi toi10 with dissolve
    t "oh!"
    t "i have to go!"
    show toi toi04 with dissolve
    t "thanks for your help, mushi!"
    show toii toii07 with dissolve
    iroh "...who?"
    show toii toii05 with dissolve
    iroh "oh! me! right!"
    iroh "you're very welcome, young lady!"
    stop music fadeout 1
    scene black
    hide screen fuzzy_edges
    with Dissolve(1.5)
    play music "audio/Blue_Dot_Sessions_-_06_-_Night_Light.mp3"
    scene bg_bk3_tophome_night
    show toi toi04
    show toi_blink
    with Dissolve(1.5)
    t "so he just... helped me see that it's okay to have help sometimes."
    y "smart dude."
    y "...sometimes."
    t "yeah..."
    t "and he also helped me see that... well..."
    t "i'm not alone... i have you."
    hide toi_blink with dissolve
    t "and i don't want to lose those around me... you, specifically... because i can't appreciate them."
    y "that's... wise of you, toph."
    t "thank mushi."
    y "i might."
    y "and i'll help you deal with your family."
    t "thanks, aang."
    t "anyway, i'm pretty tired."
    t "would you like to stay?"
    menu:
        "stay":
            y "sure."
            t "great."
            t "i'll get undressed."
            scene black with dissolve
            "you spend the night with toph."
        "home":

            y "i think i'll head home."
            show toi toi09 with dissolve
            t "oh... okay."
            scene black with dissolve
            "you head home for the night."
    $ toph_chat = 21
    jump love_bk3_next

label toph_chat22:
    t "hey, you!"
    y "hey, sexy."
    show toi_blush with dissolve
    t "oh... um..."
    t "you... you're sexy..."
    y "...damn it, you're cute."
    show toi_blink with dissolve
    t "shut up!"
    y "I will not."
    hide toi_blink with dissolve
    t "...okay..."
    t "i was actually about to go to bed..."
    t "want to sleep here?"
    menu:
        "sure":
            pass
        "nah":

            y "another time."
            show toi toi09 with dissolve
            t "oh, alright..."
            jump love_bk3_village_background

    scene black with dissolve
    "the two of you snuggle in together and you fall asleep quickly and comfortably...."
    show ctc
    pause
    hide ctc
    scene bg_a_farm_mainhall
    $ toph_footjob2_nude = True
    show tofj tofj50:
        ypos 170 zoom 0.8
    show screen fuzzy_edges
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "toph...?"
    y "what the-"
    show al_blink
    with dissolve



    a "oh, look where we are... back at the farm."
    a "i wonder why?"
    y "azula?!"
    a "ahh... {i}she's{/i} why."
    a "so this is your new breeding sow."
    a "i see you've made her a whore like the others."
    y "she's not a whore!"
    a "right... and you actually care for this one."
    y "of course i do!"
    a "oh?"
    a "let's test that, shall we?"
    a "earthbender, have you anything to add?"
    t "take me..."
    t "i am your... fuck puppy..."
    y "you're not my \"fuck puppy\", toph, i care about you."
    a "sure you do."
    t "use... me..."
    y "toph it's not like that!"
    a "no?"
    scene bg_a_prison_inside_9
    show tofj tofj50:
        ypos 170 zoom 0.8
    show al_blink
    with Dissolve(2)
    y "what... what's happening?"
    t "fuck... me... ruin... me..."
    y "toph, don't... don't say that..."
    a "well this is an interesting turn, wouldn't you say?"
    a "you've taken us to a prison."
    a "fascinating."
    y "i haven't done anything!"
    y "you... you're doing this!"
    show ale
    hide al_blink
    with dissolve
    a "i'm really not."
    y "what do you want, azula?"
    y "why are you here?"
    show alu
    hide ale
    with dissolve
    a "there's no need to be so rude."
    a "i'm here because we need each other."
    y "we do?"
    a "yes... more than you know, sadly..."
    a "and this is purely your subconscious."
    a "i'm just letting it... run around a little."
    a "you're going to kill her, you know."
    y "what? that's insane."
    a "you'll kill everybody."
    a "if you make the wrong choice."
    y "what choice?"
    a "we'll speak on it another time, perhaps..."
    y "okay, who are you?"
    y "you're not azula."
    show ale
    hide alu
    with dissolve
    a "are you so sure?"
    a "maybe i'm not, but..."
    a "well... this one needs your attention, it seems."
    t "[povname]... i need you..."
    t "take me, [povname]..."
    y "toph why are you...."
    y "....."
    y "you called me [povname]."
    t "i did. so?"
    t "that is your name..."
    y "but you shouldn't know it..."
    y "this... this is a dream..."
    a "of course it's a dream, avatar."
    "{i}hsss...."
    "{i}but that doesssn't make it untrue..."
    ya "snake bitch!"
    ya "show yourself!"
    "{i}hsss...."
    ya "show yourself! {i}now{/i}!"
    "{i}very well..."
    stop music
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
    hide screen earth_money_date
    hide screen fuzzy_edges
    scene black
    with Dissolve(1.5)
    scene bg_dream with Dissolve(1.5)
    y "what... the...?"
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
    "{i}you asssked me to ssshow myssself..."
    "{i}well... here i am..."
    "{i}i have been trying to reach you...."
    "{i}you don't lisssten..."
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
    "{i}.....you will not die here....."
    y "Oh. that's good."
    "{i}in fact... i bring you a gift..."
    "{i}a peace offering...."
    "{i}you have nothing to fear from me..."
    y "that has not proven to be the case before."
    "{i}i am in your mind, avatar..."
    "{i}but i can help you...."
    y "help me?"
    y "you're a snake demon!"
    "{i}a ssspirit... not a demon..."
    "{i}i have a name..."
    y "i don't care!"
    "{i}sssee how i will help you..."
    y "....how?"
    "{i}i will protect you..."
    "{i}i have {/i}been{i} protecting you..."
    "{i}you will sssee..."
    hide tonb with dissolve
    y "wait... where are you going?"
    y "give me some answers!"
    scene black with Dissolve(1.5)
    y "wait, come back!"
    $ renpy.pause(1)

    scene black
    scene expression "ebackgrounds/bg_night_tophhome.jpg"
    show totc totc10
    with eye_open
    ya "(ah!)" with hpunch
    y "(okay... okay... just a dream...)"
    y "(...what the hell was that all about?)"
    y "(those fucking statue eyes...)"
    y "(there's no way i can go back to sleep... i need to walk or something.)"

    y "...toph seems okay."
    y "I hope... i hope that dream was just my fears and not... reality..."
    t "*mummble...* dick... *mummble...*"
    y "aw, that's cute."

    menu:
        "Sneak out":
            "You carefully turn around and hit your little toe against the doorpost."
            y "{size=+7}AAh!! YOU MOTHERFUUUCKKKING PIECE OF SHIT DOORPOST!!"
            show totc totc14a
        "listen to Toph's sleeptalk":

            show totc totc11 with Dissolve(2.0)
            t "Sss'too warm..."

            show totc totc12
            $ renpy.pause(2.0)

            show totc totc13

            t "Yaaawnn..."
            show totc totc11
            t "don... don't lick me there... aanng thaass durrtee..."
            t "I...dun't care... itsa exit..."

            show totc totc12
            $ renpy.pause(2.0)
            show totc totc11 with Dissolve(1.5)
            t "mmmm... my mum has normal sized boohbies... why dsyou assk?"

            y "Maybe my dream self wanted a view into the future?"
            y "Oh crap... did I say that out loud?"
            show totc totc14

    t "Huh, wha..."
    show expression "bk3/toph/nightmare/face_angry.png"
    t "Intruder!"
    show expression "bk3/toph/nightmare/handswing.png"
    show expression "bk3/toph/nightmare/block.png":
        xpos 1200 ypos 300 xzoom 0.5 yzoom 0.5
        linear 2.0 xpos -700 ypos 200 xzoom 2.0 yzoom 2.0
    "You barely avoid a stone flying past you at a hair's width." with hpunch
    hide expression "bk3/toph/nightmare/face_angry.png"
    t "Aang?"
    hide expression "bk3/toph/nightmare/handswing.png" with Dissolve(1.5)
    t "What are you doing?"
    y "Just checking up on you."
    y "I had this... weird dream."
    y "it seemed super real and I couldn't get another wink of sleep..."
    y "i was gonna go for a walk or something."
    t "Really?"
    t "that doesn't seem like you."
    t "you must be pretty shaken."
    t "What happened in your dream?"
    y "it... i..."
    y "...huh."
    y "I can't quite remember."
    y "i know it was bad, and you were definitely there..."
    show expression "bk3/toph/nightmare/face_amused.png"
    t "Hehehe..."
    y "My anguish amuses you?"
    t "It looks like it's my turn to put {i}your{/i} worries to rest!"
    hide expression "bk3/toph/nightmare/face_amused.png"
    t "I'm pretty tough, Aang... but even i need help sometimes."
    t "the point is... i'm here for you, too."
    t "if you need it."
    y "i guess..."
    show expression "bk3/toph/nightmare/face_amused.png"
    t "besides, i'm your little fuck puppy!"
    "you feel your veins suddenly freeze ice cold."
    y "say... say that again."
    t "i'm your fuck puppy!"
    t "arf! arf!"
    y "why are you doing that...?"
    hide expression "bk3/toph/nightmare/face_amused.png"
    t "I'm... not actually sure..."
    t "i think i dreamt it?"
    t "i had a pretty weird dream myself, come to think of it."
    y "oh...?"
    t "yeah, azula was there, and then this snake lady appeared..."
    y "...."
    t "...but before she could say anything, ice cream starting pouring out of the sky and i swam to my new castle."
    show expression "bk3/toph/nightmare/face_amused.png"
    t "weird, huh?"
    y "...very."
    hide expression "bk3/toph/nightmare/face_amused.png"
    t "hey, it's okay."
    y "what?"
    t "you seem... upset."
    t "i'm only joking."
    t "come here, wanna snuggle until we fall asleep again?"
    y "yeah, i... i think i need that."
    scene black with Dissolve(1.5)
    "You and Toph spoon together and after some light kissing and stroking..."
    $ renpy.pause()
    show expression "ebackgrounds/bg_night_tophhome.jpg"
    show totc totc15
    with Dissolve(1.5)

    t "Aang?"
    y "Yeah?"
    t "Would you... like to have children? I mean, eventually?"
    menu:
        "yeah, I think I would":
            $ totf_preg = True
            y "sure."
            y "In fact, maybe we should make one right now!"
            y "The combined awesomeness of us would create a god among mortals!"
            show expression "bk3/toph/nightmare/face_lewdzoom.png"
            t "you're right!"
            t "We could call it Taangh! Destroyer of worlds!"
            y "tang?"
            y "that's a terrible name."
            y "obviously, i accept."
            t "yes! and it'll be able to move any mountain!"
            y "oh yeah."
            hide expression "bk3/toph/nightmare/face_lewdzoom.png"
            t "hey..."
            t "all kidding aside... i'm actually kinda seriously asking."
            y "Hmmmm...."
            y "Eventually, yeah I think I would."
            t "See, that wasn't that hard, was it?"
            show expression "bk3/toph/nightmare/face_lewdzoom.png"
            t "Hmmmm... we could practice making one now..."
            y "That's a great Idea."
            hide expression "bk3/toph/nightmare/face_lewdzoom.png" with Dissolve(1.5)
        "I don't know...":


            y "I think we should talk about that after we have dealt with the fire nation."
            y "Once that's over, let's decide what our future will look like."
            t "Is that a veiled \"no\"?"
            t "You can just tell me if you don't want any."
            y "it's not that... i just don't want to tempt fate."
            t "Hmmm... sometimes you're a real scaredy cat, twinkletoes."
            y "Only when it comes to the important things."
            y "But if we do end up having a kid, I get to name any boy."
            t "Why? Do you have anything in mind?"
            y "Yeah... Taangh!! Destroyer of worlds!!!"
            t "I'll start praying for girls, just in case."


    y "You still using that stuff Suki gave you?"
    t "Yeah... in fact I should visit her again, because I'm almost out."
    y "If you do run out we could always start using that other entrance."
    y "Just to be on the safe side."
    t "What other entrance?"
    t "What are you talk... wait..."
    show expression "bk3/toph/nightmare/face_angryzoom.png"
    t "That's dirty!!!"
    t "that's where poop comes out!!!"
    t "Are you crazy?!"
    y "It's really not that big of a deal..."
    y "...and not a single part of you is dirty."
    hide expression "bk3/toph/nightmare/face_angryzoom.png"
    t "...I still think it's weird and strange."
    y "Well, you haven't run out of Suki's stuff just yet soo..."
    y "...how about practicing some old fashioned baby-making?"
    y "That cuddling from before has made me hard as fuuuuck."
    t "I guess we could do a quickie...."

    scene black with Dissolve(1.5)
    "The rest of the night you and Toph practice."
    $ renpy.pause()

    scene bg_day_tophhome:
        xzoom -1.0
    with Dissolve(2.0)
    y "*Yawn!*"
    y "Hmmmm... where's Toph?"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg" with Dissolve(2.0)
    hide expression "ebackgrounds/bg_night_tophhome.jpg"
    y "Not here..."
    show expression "ebackgrounds/bg_bk3_tophome_day.jpg" with Dissolve(2.0)
    hide expression "ebackgrounds/bg_bk3_tophome_0.jpg"

    y "Not here either."
    y "she must've gone out I guess."
    y "Now where's toph's toilet..."

    show expression "ebackgrounds/toilet.jpg"
    show totc totc20 with hpunch
    t "Ah!!! "
    y "ah!"
    show totc totc21
    t "Do you mind?!?"
    t "I'm... I'm kinda busy here!"
    y "Sorry!"
    hide expression "ebackgrounds/toilet.jpg"
    hide tost
    scene black
    "You step out and a moment later Toph does too."
    show expression "ebackgrounds/bg_bk3_tophome_day.jpg"
    show toi toi04
    show toi_blush
    with dissolve
    t "i can't believe you just..."
    y "aw, you're cute when you're flustered."
    t "....you're lucky i like it when you call me cute."
    y "so..."
    y "Can I get a kiss from my favorite girl-sized energizer bunny before I go out?"
    t "What?"
    y "Just that your stamina is a match for my own!"
    t "Pffft, your stamina only lasts during the fun stuff."
    t "When it comes to training, you're not quite my equal yet. "
    y "Just you wait, One of these days..."
    t "Hah! We'll see about that."
    t "Oh, and don't use the toilet for awhile..."
    y "what?"
    show toi toi09 with dissolve
    t "well I don't have fancypants airbending powers to whisk away... odors..."
    y "do i really have to tell you that's stupid normal?"
    y "oh! wait!"
    t "what?"
    y "i just realized i've seen you go to the bathroom!"
    t "and...?"
    y "that means we're a couple!"
    t "i... guess..."
    y "yeah, that's totally a thing!"
    y "when you can go to the bathroom and it not be a thing, that's how you know you've made it."
    y "aw, we're breaking new ground."
    y "i'll see you later honey, have a good day."
    t "oh, shut up and get out."
    y "gotta earn that bread!"
    show toi toi06
    show toi_blink
    with dissolve
    t "WHATEVER!! Go outside! I got things to do!"
    y "okay, dear."
    t "aarrgh!!"
    scene black with dissolve
    $ toph_chat = 22
    jump love_bk3_next

label toph_chat23:
    $ toph_chat =23
    "the three of you head to the tavern."
    jump toph_suki_katara_tav

label toph_chat24:
    t "so what's up?"
    show toi toi07 with dissolve
    t "wanna stay in and snuggle with me?"
    y "when did you get so lovey-dovey?"
    show toi_blink
    show toi_blush
    with dissolve
    t "i don't know... you bring it out in me."
    t "for some weird reason."
    hide toi_blink with dissolve
    t "so?"
    menu:
        "sure":
            $ toph_chat = 24
            y "there's nothing i'd rather do."
            t "yay!"
            scene black with dissolve
            "The two of you stay up together, talking and cuddling."
            "you eventually fall asleep, holding a naked toph tight to your chest."
            "your last thoughts are of feeling her little breasts pressed against you, rising and falling."
            "your hand cups one of her little buttcheeks and you feel suddenly, and completely, at peace."
            jump love_toph_anal2
        "not now":

            y "later."
            show toi toi04 with dissolve
            t "okay."
            jump love_bk3_village_background

label toph_chat25:


label love_toph_blowjob:
    $ toph_licking = False
    t "and... lay down."
    scene black with dissolve
    stop music
    play music "audio/Unwritten Return.mp3"
    scene bg_bk3_tophome_0
    show tobb tobb50
    with dissolve
    if toph_chat ==14:
        y "there."
        y "as you can see, i'm ready to-"

    show tobb tobb51 with dissolve
    "toph lays down on top of you, her small, perky nipples pressing against you."

    if toph_chat ==14:
        y "so, what're we doing here, toph?"

        show tobb tobb52 with dissolve
        t "well..."
        t "i was kinda thinking..."

        show tobb tobb53 with dissolve
        t "i want you to be with me."
        t "and... i want you to be happy with my attention, and not feel like you need someone else..."
        t "and..."
        show tobb tobb52 with dissolve
        t "i'm really horny from that conversation with katara."

    show tobb tobb54 with dissolve
    "toph leans her face into your cock and you can feel her breathe deeply."
    t "mmmmm.... such a strong smell."
    if toph_chat ==14:
        show tobb tobb54_1 with dissolve
        t "you know, i was also thinking... well..."
        y "yeah?"
        t "I'm a little frustrated."
        y "you are?"
        y "why?"
        t "well..."
        show tobb tobb54 with dissolve
        t "i can't really see your cock."
        t "i got a feel for it with my feet, but it seems to me that the best way to really become familiar with it..."
        t "...is probably to put it in my mouth."
        show tobb tobb53 with dissolve
        t "that way i can run my tongue all over your cock."
        t "i think the mouth might be the most sensitive place in the body."
        show tobb tobb54 with dissolve
        t "well... second most sensitive."
        show ctc
        pause
        hide ctc
        t "but maybe i'm directing my thoughts to the wrong head...."
    show tobb tobb60 with Dissolve(1.5)
    if toph_chat ==14:
        t "how about you, little guy? what do you think?"
    t "Would you like a kiss from me?"
    if toph_chat ==14:
        y "....please don't call it little."
        t "Oops, sorry."
        t "i forgot guys are weird about that."

    $ temp_counter = 0
    while temp_counter < 3:
        play sound "audio/kiss.mp3"
        show tobb tobb61
        show tobb_heart:
            xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
            xzoom 1 yzoom 1 alpha 1.0
            linear 1.0 xzoom 4 yzoom 4 alpha 0.0
        $ renpy.pause(0.5)
        show tobb tobb60
        $ renpy.pause(0.5)
        $ temp_counter += 1


    "Toph kisses the top of your dick with her soft, wet lips..."
    "you throb against her kisses, feeling like you've grown an inch."
    if toph_chat ==14:
        t "hmmm.... maybe i should get to know you better..."
        t "what do you think?"
        y "please do!"
        t "i wasn't asking {i}you{/i}..."

    menu:
        "switch back to sideview":
            show tobb tobb55
            $ tobb_frontview = False
        "stay with this view":
            show tobb tobb62
            $ tobb_frontview = True

    t "*glug!* *shlurp!* *gltch!*"
    "toph passionately slurps as she sucks..."
    "her slobbering, smacking, gulping sounds rebound from the stone walls as her mouth eagerly works your cock."
    y "Oh fuck, that feels good!"
    if toph_chat ==14:
        y "when did you stop being shy?!"
    t "*sluurp!* *gagh!* *shluurp!*"
    menu:
        "return the favor":
            $ toph_licking = True
            y "I can't let you have all the fun...."
            show tobb_fhead behind tobb
            show tobb tobb64
            with Dissolve(1.5)
            t "hhmm...?"
            show ctc
            pause
            hide ctc
            show tobb tobb65 with Dissolve(1.5)
            t "hmmgh...!"
            show ctc
            pause
            hide ctc
            show expression "bk3/toph/blowjob2/pussyfluid.png":
                alpha 0.0
                linear 3.0 alpha 0.6

            show tokp_lick:
                xpos 450 ypos 320
            t "hgghh.... *gltch!*... ahhh.... uhhn!!!"
            y "it's about time i gave your pussy some love, toph."
            t "mmmgh!!!"
            "toph slobbers on your cock with deep, fast sucks and a wild tongue that laps at your shaft every time you pop out of her mouth."
            t "anhh... *guulp!*... anhhh... *slluuurp!*... ohhh..."
            hide tobb_fhead
            show expression "bk3/toph/blowjob2/bbody_head.png" behind tobb:
                xpos 374 ypos -100
            with dissolve
            t "yes! lick... lick me, aang!"
            t "I never knew... i didn't know you could... it's so good!"
            t "don't stop!"
            t "It's so... so... good... i'm...."
            t "i'm... gonna make you cum!"
            hide expression "bk3/toph/blowjob2/bbody_head.png"
            show tobb_fhead behind tobb
            "toph attacks your cock with her mouth, sucking and slurping on you desperately."
            y "alright, then...."
            y "first one to cum loses!"
            t "Get... *shlurp*... ready to lose!"
            show ctc
            pause
            hide ctc
            hide tokp_lick
            hide tobb_fhead
            hide expression "bk3/toph/blowjob2/pussyfluid.png"
        "Let toph go on undisturbed":


            pass

    if tobb_frontview == False:
        show tobb tobb55
    else:
        show tobb tobb62
    t "*mmmhn....*"
    show ctc
    pause
    hide ctc
    t "ready to... shoot your... load?"
    if tobb_frontview == False:
        show tobb tobb70
        "without waiting for an answer to her halting question, toph shoves your cock down her throat."
        ya "fuck!"
        t "*gagh!* *sluurp!*"
    else:
        show tobb tobb71
        "without waiting for an answer to her halting question, toph shoves your cock down her throat."
        ya "fuck!"
        t "*gagh!* *sluurp!*"

    show ctc
    pause
    hide ctc

    y "hhngh!!"
    if tobb_frontview == False:
        ya "you want my cum?"
        t "mmhmm!"
        t "give it!"
        show tobb tobb70_1
        t "*shluurp!* *mghgm!*"
        show ctc
        pause
        hide ctc
        t "give it to me!"
        show tobb tobb70_2
        show ctc
        pause
        hide ctc
        t "give me your sperm, aang!"
        menu:
            "cum in throat":
                $ love_toph_bj_facial = False
                show tobb tobb57 with vpunch
            "cum on face":
                $ love_toph_bj_facial = True
    else:

        ya "you want my cum?"
        t "mmhmm!"
        t "give it!"
        show tobb tobb71_1
        t "*shluurp!* *mghgm!*"
        show ctc
        pause
        hide ctc
        t "give it to me!"
        show tobb tobb71_2
        show ctc
        pause
        hide ctc
        t "give me your sperm, aang!"
        menu:
            "cum in throat":
                $ love_toph_bj_facial = False
                show tobb tobb59 with vpunch
            "cum on face":
                $ love_toph_bj_facial = True

    if not love_toph_bj_facial:
        ya "fuck!"
        t "mmghm!!"
        play sound "audio/splurt2.ogg"
        with flash
        play sound "audio/splurt3.ogg"
        with flash
        play sound "audio/splurt1.ogg"
        with flash
        "you shiver as waves of cum explode deep into toph's throat."
        play sound "audio/gulp2.mp3"
        t "*gulp* *gulp* *gulp* *gulp*"
        "thick ropes of sperm must be pouring themselves into her mouth, but she keeps sucking firmly, all the way to the base."
        play sound "audio/gulp2.mp3"
        t "*gulp* *gulp* *gulp*"
        "you can feel her muscles squeeze and vibrate as she moans into your cock."
        if tobb_frontview:
            show tobb tobb63 with dissolve
        t "*mmmnmm...*"
        y "unnghh...."
    else:
        if tobb_frontview == False:
            show tobb tobb51 with dissolve
            t "let me have-"
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/boobjob/spermshot.png":
                xpos 142 ypos 80
            with flash
            t "ah...!"
            hide expression "bk3/toph/boobjob/spermshot.png"
            show expression "bk3/toph/footjob3/sperm1.png":
                xpos -45 ypos 110
            with flash
            t "wow...."
            show ctc
            pause
            hide ctc
        else:
            show tobb tobb60 with dissolve
            t "let me have-"
            play sound "audio/splurt2.ogg"
            show expression "bk3/toph/boobjob/spermshot.png":
                xpos -30 ypos 80
            with flash
            t "ah...!"
            hide expression "bk3/toph/boobjob/spermshot.png"
            show expression "bk3/toph/footjob3/sperm1.png":
                xpos -220 ypos 117
            with flash
            t "wow..."
            show ctc
            pause
            hide ctc

    if not love_toph_bj_facial:
        show tobb tobb51
        show expression "katara/k_avlegs_spermouth_xtra.png":
            xpos 235 ypos 57
        with Dissolve(1.5)









        t "mah!!"
        t "not bad..."
        if toph_licking:
            t "and yes! i win!"
            y "yeah... you do..."
        if toph_chat ==14:
            t "suck it, twinkletoes!"
            y "actually you just.... never mind."
            y "wait, you... swallowed it?"
            t "I wasn't supposed to?"
            y "uh... no, you did fine."
            y "It's just that I expected more of a mess."
            t "why? what else would i do with it?"
            y "....you're a trooper."
        y "you've got a little, uh..."
        t "what?"
        y "well... you've got some jizz dripping..."
        t "oh, sorry...."
        play sound "audio/gulp2.mp3"
        hide expression "katara/k_avlegs_spermouth_xtra.png"
        with dissolve
        t "{size=+5}*gulp!*"
        t "...ah!"
        t "is it gone? did i get it?"
        y "....yes."
        show tobb tobb54 with Dissolve(1.5)
        t "mmm... you know, it smells even better, now."
        t "but i think..."
        show tobb tobb51 with dissolve
        t "that you..."
        show tobb tobb53 with dissolve
        t "and this guy here..."
        t "...should probably head home."
        show tobb tobb52 with dissolve
        t "unless you want to spend the night?"
    else:

        t "it's... on my face..."
        y "sorry, i just sort of... exploded."
        t "no, i don't mind... being a little mess."
        t "I just... wasn't expecting it, is all."
        if toph_licking:
            t "and yes! i win!"
            y "yeah... you do..."
        t "it's very... strong smelling."
        y "i think it's good for your skin, actually."
        y "some very pretty girls use it regularly."
        t "oh!"
        t "well, then i'll keep it on for a bit."
        y "fuck yeah."
        t "also... i think..."
        if tobb_frontview:
            show tobb tobb51
            hide expression "bk3/toph/footjob3/sperm1.png"
            show expression "bk3/toph/footjob3/sperm1.png":
                xpos -45 ypos 110
            with Dissolve(1.5)
        t "that you..."
        show tobb tobb53 with dissolve
        t "and this guy here..."
        t "...should probably head home."
        show tobb tobb52 with dissolve
        t "unless you want to spend the night?"
    menu:
        "sleep here":
            y "do you mind if i just sleep here?"
            y "i am... emptied."
            t "of course you can!"
            t "we'll sleep right here..."
            t "...and i'll see you when you wake up."
            scene black with dissolve
            "you fall asleep. hard."
            ".................."
            "..............................."
            "{i}*gltch* *gulp* *slurp*"
            y "hngha... wah..."
            scene bg_bk3_tophome_0
            show tobb tobb55
            with eye_open
            t "mmmghmm..."
            y "uuuhh... damn..."
            t "good morning!"
            show ctc
            pause
            hide ctc
            t "*sluurp...*"
            y "oh, fuuuck..."
            y "toph! i'm gonna-"
            show tobb tobb57 with vpunch
            play sound "audio/splurt2.ogg"
            with flash
            play sound "audio/splurt3.ogg"
            with flash
            play sound "audio/splurt1.ogg"
            with flash
            $ renpy.pause(0.3)
            play sound "audio/gulp2.mp3"
            t "*gulp* *gulp* *gulp*"
            show ctc
            pause
            hide ctc
            show tobb tobb51
            show expression "katara/k_avlegs_spermouth_xtra.png":
                xpos 235 ypos 57
            with Dissolve(1.5)
            t "ah!"
            y "That was... an amazing way to wake up."
            t "it was an amazing way to get breakfast..."
            t "i'm so full..."
            t "now, i've got some things to do."
            y "wait... are you kicking me out?"
            t "yup!"
            y "....fine."
            y "I'm going."
            t "see you later, though."
            if toph_chat ==14:
                $ toph_chat = 15
            jump love_bk3_next
        "sleep at home":

            y "I think i should head home."
            t "aww...."
            t "well, i'll see you later then."
            t "goodnight!"
            scene black with dissolve
            "you head home for the night."
            if toph_chat ==14:
                $ toph_chat = 15
            jump love_bk3_next

label toph_titplay1:
    hide toi with dissolve
    show tonf tonf15 with Dissolve(1.5)
    t "aang... i was wondering..."
    y "yes?"
    t "we've... kissed... and you've mentioned..."
    show tonf tonf17 with dissolve
    t "my breasts."
    y "i remember."
    t "do you... really think they're... you know... perfect?"
    t "like you said?"
    y "i really do."
    t "......."
    t "would you..."
    t "would you want to see them?"
    y "i'd be a fool not to."
    t "......"
    t "o-okay, then."
    t "but just quickly, okay?"
    t "just a peek."
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    hide tonf
    show blackveil
    show tonf tonf51
    with Dissolve(2.0)
    show ctc
    pause
    hide ctc
    t "is..."
    t "do you..."
    t "still like them?"
    t "I know they're small, but-"
    y "wow."
    t "...."
    y "what a gorgeous body."
    y "petite... and firm..."
    t "umm."

    show tonf tonf52 with Dissolve(2.0):
        ypos 972
    show ctc
    pause
    hide ctc
    t "i can make them look a little bigger..."
    t "if you want."
    t "here..."

    show tonf tonf52:
        ypos 972
        linear 3 ypos 720

    "Toph sticks out her chest as far as possible in an effort to make her small breasts seem bigger."
    hide tonf
    show tonf tonf52
    y "They're beau-"
    show tonf tonf51 with dissolve
    pause(0.2)
    show tonf tonf17 with dissolve
    y "-tiful."
    y "I'm slightly disappointed with the duration of this experience though."
    show tonf tonf16
    t "too bad!"
    show tonf tonf17
    t "Maybe we can go a little further next time...."
    t "....maybe."
    $ toph_titplay = 1
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_titplay2:
    hide toi with dissolve
    show tonf tonf15 with Dissolve(1.5)
    t "aang..."
    t "do you..."
    show tonf tonf17 with dissolve
    t "want to see my... breasts again?"
    y "oh, definitely."
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    hide tonf
    show blackveil
    show tonf tonf51
    with Dissolve(2.0)
    show ctc
    pause
    hide ctc
    t "um..."
    t "here."

    show tonf tonf52 with Dissolve(2.0):
        ypos 972
    show ctc
    pause
    hide ctc
    t "i can make them look a little larger..."

    show tonf tonf52:
        ypos 972
        linear 3 ypos 720

    "Toph sticks out her chest as far as possible in an effort to make her small breasts seem bigger."
    hide tonf
    show tonf tonf52
    y "They're beautiful."

    hide tonf
    show tonf tonf52
    t "You can touch them if you want."
    show tonf tonf53 with Dissolve(2.0)
    y "Wow, I can feel your heartbeat. It's going pretty fast."
    y "Can I move my hand?"
    t "um."
    t "wait."
    t "do you... like me, aang?"
    menu:
        "i do":
            pass
        "nope":

            y "not really, no."
            show tonf tonf16 with Dissolve(1)
            t "get out of my house, aang!"
            $ toph_angry =2
            play sound "audio/thud.mp3"
            scene black
            "toph slams the door in your face."
            y "i'll... try again later."
            "you head home for the night."
            jump love_bk3_next

    y "yes. i do."
    t "I... like you, too."
    t "okay, go ahead. i'm ready."
    show tonf tonf54
    show ctc
    pause
    hide ctc
    y "we'll go slow, okay?"
    t "...okay..."
    show ctc
    pause
    hide ctc
    t "how are they?"
    y "i can cup them perfectly in my hand..."
    y "and these..."
    show tonf tonf55
    t "hnmgh...."
    show ctc
    pause
    hide ctc
    y "...cute little nipples..."
    show ctc
    pause
    hide ctc

    show tonf tonf56
    y "can't ignore this one..."
    show ctc
    pause
    hide ctc
    t "ahh... ah... ohhn..."
    y "You okay?"
    t "I'm... feeling..."

    show tonf tonf57
    t "oohhhhn...."
    show ctc
    pause
    hide ctc
    y "feeling what?"
    t "a little... little lightheaded..."
    y "that's okay."
    y "relax..."
    show ctc
    pause
    hide ctc
    y "let go."

    show tonf_lewd with Dissolve(1.5)
    t "ahhn...."
    y "there you go..."
    show ctc
    pause
    hide ctc
    "toph's nipples respond firmly and fiercely to your touch... they push out, hard and determined from her little lumps."
    t "ah... ohh... this is... is really... nice..."
    t "feeling... warm... and..."
    t "...wet...?"
    y "that's okay, let it happen."
    t "i'm... ah..."
    t "I'm hot... it feels... ahh..."
    y "(time for some tongue!)"
    show tonf tonf58
    t "unngghh!!"
    t "ohh!!"
    show ctc
    pause
    hide ctc
    t "oh, my goddd.... aaang..."
    "the feel of her soft, giving skin is almost more than you can take."
    "her nipple pops in and out of your mouth as toph pushes her chest up towards you..."
    "forcing you to take more of her breast... which you greedily gobble in her ecstasy."
    t "aang, it's... ah... i'm... i don't..."
    t "what's... what's happening..."
    y "sshhh... ride it... ride the wave..."
    t "I'm... oh no, i think i'm gonna... pee...?"
    y "it's not pee... go ahead..."
    t "I can't... your tongue... i'm..."
    show expression "bk3/toph/lovetits/blink.png":
        xpos 600
    with dissolve
    t "aaahh....." with ushake
    t "{size=+5}aaaaahhhhh.........." with vshake
    t "{size=+12}aaaaaaahhhhhhhhhh!!!!!!!!!!!!" with hpunch
    t "....hnghhh...."
    t ".............."
    t "stop... stopstopstop...."
    show tonf tonf53 with Dissolve(1.5)
    hide expression "bk3/toph/lovetits/blink.png" with dissolve
    t "what...."
    hide tonf_lewd with dissolve
    t "what was that..."
    y "you came."
    t "I... that was an orgasm?"
    y "yes."
    t "it was.... amazing."
    t "I need... i'm gonna need more of those."
    y "I... will be happy to provide."
    show tonf tonf51 with Dissolve(1.5)
    t "is it... are we okay?"
    y "more than okay. we're great."
    y "go get some rest."
    t "thank you. i'm so... so tired..."
    t "goodnight..."
    t "and thank you..."

    $ toph_titplay = 2
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_titplay3:
    hide toi with dissolve
    show tonf tonf15 with Dissolve(1.5)
    t "aang..."
    t "do you..."
    show tonf tonf17 with dissolve
    t "want to see my... breasts again?"
    y "oh, definitely."
    stop music
    play music "audio/Unwritten Return.mp3"
    show tonf tonf51
    with Dissolve(2.0)
    show ctc
    pause
    hide ctc
    t "um..."
    t "here."

    show tonf tonf52 with Dissolve(2.0):
        ypos 972
    show ctc
    pause
    hide ctc
    t "i can make them look a little larger..."

    show tonf tonf52:
        ypos 972
        linear 3 ypos 720

    "Toph sticks out her chest as far as possible in an effort to make her small breasts seem bigger."
    hide tonf
    show tonf tonf52
    y "They're beautiful."

    hide tonf
    show tonf tonf52
    t "You can touch them if you want."
    show tonf tonf53 with Dissolve(2.0)
    y "Wow, I can feel your heartbeat. It's going pretty fast."
    y "Can I move my hand?"
    t "Okay."
    t "wait."
    t "do you... like me, aang?"
    y "yes. i do."
    t "I... like you, too."
    t "okay, go ahead. i'm ready."
    show tonf tonf54
    show ctc
    pause
    hide ctc
    y "we'll go slow, okay?"
    t "...okay..."
    show ctc
    pause
    hide ctc
    t "how are they?"
    y "i can cup them perfectly in my hand..."
    y "and these..."
    show tonf tonf55
    t "hnmgh...."
    show ctc
    pause
    hide ctc
    y "...cute little nipples..."
    show ctc
    pause
    hide ctc

    show tonf tonf56
    y "can't ignore this one..."
    show ctc
    pause
    hide ctc
    t "ahh... ah... ohhn..."
    y "You okay?"
    t "I'm... feeling..."

    show tonf tonf57
    t "oohhhhn...."
    show ctc
    pause
    hide ctc
    y "feeling what?"
    t "a little... little lightheaded..."
    y "that's okay."
    y "relax..."
    show ctc
    pause
    hide ctc
    y "let go."

    show tonf_lewd with Dissolve(1.5)
    t "ahhn...."
    y "there you go..."
    show ctc
    pause
    hide ctc
    "toph's nipples respond firmly and fiercely to your touch... push out, hard and determined from her little lumps."
    t "ah... ohh... this is... is really... nice..."
    t "feeling... warm... and..."
    t "wet...?"
    y "that's okay, let it happen."
    t "i'm... ah..."
    t "I'm hot... it feels... ahh..."

    show tonf tonf58
    t "unngghh!!"
    t "ohh!!"
    show ctc
    pause
    hide ctc
    t "oh, my goddd.... aaang..."
    "the feel of her soft, giving skin is almost more than you can take."
    "her nipple pops in and out of your mouth as toph pushes her chest up towards you..."
    "forces you to take more of her breast... which you greedily gobble in her ecstasy."
    t "aang, it's... ah... i'm... i don't..."
    y "sshhh... ride it... ride the wave..."
    t "I can't... your tongue... i'm..."
    show expression "bk3/toph/lovetits/blink.png":
        xpos 600
    with dissolve
    t "aaahh....." with ushake
    t "{size=+5}aaaaahhhhh.........." with vshake
    t "{size=+12}aaaaaaahhhhhhhhhh!!!!!!!!!!!!" with hpunch
    t "....hnghhh...."
    t ".............."
    t "stop... stopstopstop...."
    show tonf tonf53 with Dissolve(1.5)
    hide expression "bk3/toph/lovetits/blink.png" with dissolve
    t "that...."
    hide tonf_lewd with dissolve
    t "that was incredible..."
    t "I need... i'm gonna need more of those."
    y "I... will be happy to provide."
    show tonf tonf51 with Dissolve(1.5)
    t "is it... are we okay?"
    y "more than okay. we're great."
    y "go get some rest."
    t "thank you. i'm so... so tired..."
    t "goodnight..."
    t "and thank you..."

    $ toph_titplay = 3
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label toph_face_touch1:
    y "hey... come closer for a second."
    t "alright...."
    hide toi with dissolve
    show tonf tonf15 with dissolve
    t "i'm here. what's up?"
    y "well... i've been wondering..."
    y "do you know what i look like?"
    t "what?"
    t "of course i do."
    y "how?"
    show expression "bk3/toph/lovetits/bench_blink.png":
        xpos 736 ypos 196
    with dissolve
    t "i see shapes through vibration of the ground."
    t "like a champ."
    y "and that goes all the way up to the face?"
    hide expression "bk3/toph/lovetits/bench_blink.png"
    with dissolve
    t "well... almost."
    t "I get a... vague idea with faces."
    t "the only way i can really tell for sure is touching."
    y "go ahead."
    show tonf tonf17 with dissolve
    t "...w-what?"
    y "touch my face."
    t "what? why?"
    menu:
        "i want you to know what i look like":
            y "i want you to know what i look like."
            t "...."
            t "o-okay."
            y "i mean, you don't have to-"
            t "no, i... i don't mind."
            t "i'd like to."
            t "i've been... wondering."
        "aren't you curious?":

            t "i... have been wondering."

    t "...."
    show tonf tonf15 with dissolve
    t "alright, let's do it!"
    show tonf tonf18 with dissolve
    t "aang, do you mind..."
    t "um..."
    t "could you lower your head?"
    y "sure."
    show blackveil
    hide tonf
    show tonf tonf21
    with Dissolve(1.5)
    "toph gently pats down your face with her hands."
    "they run from your forehead down, and then she slowly reverses the motion."
    t "huh..."
    "her fingers are small... unobtrusive."
    "for someone so brusque, her touch is surprisingly light and gentle."
    t "hmmm...."
    "her fingers find your nose and she squeezes it with a giggle."
    y "ngh. hey."
    t "heh, sorry, couldn't resist."
    "toph softly moves her hands to the sides of your face, her fingertips gliding across your cheeks towards your ears."
    "using her thumb and forefinger, she casually squeezes your ears and runs the down your earlobes."
    "she lets go and places her hands on your face again, paying extra attention to your closed eyes and lips."
    t "i..."
    t "i like how you look, aang."
    y "thanks, i like how you-"
    "toph suddenly pulls your closer."

    show tonf tonf23
    with dissolve
    y "-look."
    "you haven't been this close to her face before."
    "she's.... pretty."
    "{i}really{/i} pretty."
    "this... is a dangerous closeness."
    t "so... i'm thinking..."
    y "oh?"
    "your voice comes out a little hoarse."
    "you try to clear your throat unassumingly."
    t "i've felt your face, so..."
    t "it only seems fair that you feel mine."
    y "that... that makes sense..."
    t "right?"
    show tonf tonf22 with dissolve
    t "go for it."
    show ctc
    pause
    hide ctc
    y "(am i... misreading this situation?)"
    y "(she keeps flipping between confident and insecure.)"
    t "what are you waiting for?"
    y "(oh, what the hell.)"
    show tonf tonf24 with dissolve
    show ctc
    pause
    hide ctc
    "You touch toph's face, holding it gently."
    "there's a little natural dirt, but not much, and her face is soft in spite of it."
    "you rub her cheek and gently touch her eyelids; she jerks a little in surprise, but tries to stay still."
    "as you push aside her hair, you're struck by how young and innocent she still looks."
    show tonf tonf22 with dissolve
    "you pull your hand away for a moment."
    t "mmmm?"
    "toph lets out the lightest of moans."
    show tonf_caress:
        xpos 500 ypos 350
        linear 2.0 xpos 540 ypos 330
        linear 2.0 xpos 500 ypos 350
        repeat
    with dissolve
    "heart racing, you take a risk and begin to caress her face."
    show ctc
    pause
    hide ctc
    "toph lets out another soft surprise moan."
    t "ohh...."
    "her features are so delicate, you find yourself fascinated with the curve of her cheek to the fullness of her lips."
    "you lose track of time... and toph seems to lose it with you."
    show ctc
    pause
    hide ctc
    hide tonf_caress

    show tonf_caress_aided:
        xpos 30 ypos 0
        linear 2.0 xpos 0 ypos 20
        linear 2.0 xpos 30 ypos 0
        repeat
    with dissolve
    "she leans into your touch, guiding your uncertain hand more confidently across her face."
    "no words are spoken."
    "you're afraid the spell might break."
    "you stay like this for another moment, caught between eroticism and purity."
    show ctc
    pause
    hide ctc
    menu:
        "kiss her":
            "as you lean in, she steps gently back and opens her eyes."
        "talk to her":
            y "toph-"
    hide tonf_caress_aided
    show tonf tonf20
    with dissolve
    t "i think... that's enough."
    t "that was..."
    t "Nice."
    t "i'm glad i know... what you look like."
    y "toph-"
    show tonf tonf17 with Dissolve(1.5)
    t "i'm... gonna do some... important things."
    y "oh?"
    t "yeah... some... some stuff."
    t "you should go."
    y "...."
    y "okay, i will."
    y "goodnight."
    t "......"
    t "goodnight."
    scene black with dissolve
    $ toph_face_touch = 1
    "you head home for the night."
    jump love_bk3_next

label toph_face_touch2:
    y "hey... come closer for a second."
    t "alright...."
    hide toi with dissolve
    show tonf tonf15 with dissolve
    t "i'm here. what's up?"
    y "well... would you like to touch my face again?"
    y "you know, just... get a reminder of what i look like?"
    show tonf tonf17 with dissolve
    t "....yeah, i think that's a good idea."
    show tonf tonf18 with dissolve
    t "aang, do you mind..."
    t "um..."
    t "could you lower your head?"
    y "sure."
    show blackveil
    hide tonf
    show tonf tonf21
    with Dissolve(1.5)
    "toph gently pats down your face with her hands."
    "they run from your forehead down, and then she slowly reverses the motion."
    t "huh..."
    "her fingers are small... unobtrusive."
    "for someone so brusque, her touch is surprisingly light and gentle."
    t "hmmm...."
    "her fingers find your nose and she squeezes it with a giggle."
    y "ngh. hey."
    t "heh, sorry, couldn't resist."
    "toph softly moves her hands to the sides of your face, her fingertips gliding across your cheeks towards your ears."
    "using her thumb and forefinger, she casually squeezes your ears and runs the down your earlobes."
    "she lets go and places her hands on your face again, paying extra attention to your closed eyes and lips."
    t "i..."
    t "i like how you look, aang."
    y "thanks, i like how you-"
    "toph suddenly pulls your closer."
    show blackveil
    hide tonf
    show tonf tonf23
    with dissolve
    y "-look."
    t "well, since i've felt your face...."
    t "it only seems fair that you feel mine."
    y "def... definitely."
    show tonf tonf22 with dissolve
    t "go for it."
    show tonf tonf24 with dissolve
    show ctc
    pause
    hide ctc
    "You... touch toph's face, holding it gently."
    "she's got a little dirt on it, but not much, and her face is soft in spite of the light coating of grit."
    "you rub her cheek and gently touch her eyelids; she jerks a little in surprise, but tries to stay still."
    "as you push aside her hair, you're struck by how young and innocent she still looks."
    show tonf tonf22 with dissolve
    "you pull your hand away for a moment."
    t "mmmm?"
    "toph lets out the lightest of moans."
    show tonf_caress:
        xpos 500 ypos 350
        linear 2.0 xpos 540 ypos 330
        linear 2.0 xpos 500 ypos 350
        repeat
    show ctc
    pause
    hide ctc
    "toph lets out another soft surprise moan."
    t "ohh...."
    "her features are so delicate, you find yourself fascinated with the curve of her cheek to the fullness of her lips."
    "you lose track of time... and toph seems to lose it with you."
    show ctc
    pause
    hide ctc
    hide tonf_caress

    show tonf_caress_aided:
        xpos 30 ypos 0
        linear 2.0 xpos 0 ypos 20
        linear 2.0 xpos 30 ypos 0
        repeat
    with dissolve
    "she leans into your touch, guiding your uncertain hand more confidently across her face."
    "no words are spoken."
    "you're afraid the spell might break."
    "you stay like this for another moment."
    show ctc
    pause
    hide ctc
    y "toph-"
    hide tonf_caress_aided
    show tonf tonf20
    with dissolve
    t "i think... that's enough."
    t "that was..."
    t "Nice."
    t "i'm glad i know... what you look like."
    y "toph-"
    show tonf tonf17 with Dissolve(1.5)
    t "i'm... gonna do some... important things."
    y "oh?"
    t "yeah... some... some stuff."
    t "you should go."
    y "...."
    y "okay, i will."
    y "goodnight."
    t "......"
    t "goodnight."
    scene black with dissolve
    $ toph_face_touch = 1
    "you head home for the night."
    jump love_bk3_next




label love_inside_shop_building:
    stop music
    play music"audio/Carpe Diem.mp3" 
    scene black
    scene inside_shop
    with dissolve
    if katara_lonely ==4 and not katara_present_ask2:
        $ katara_present_ask2 = True
        show thankful_girl with dissolve
        girl "hello!"
        y "hey... do you have any nice gifts?"
        girl "no, sorry."
    if love_toph_sex and not bk3_shop_watch:
        show thankful_girl
        with dissolve
        girl "oh, i'm glad you're here!"
        girl "i have to run an errand, i'll leave you to watch the shop."
        y "i... what?"
        girl "i'm sorry, boss!"
        girl "i've just got stuff to do!"
        y "I'm your boss?"
        y "oh, wait, that's totally a thing."
        y "that's why I get a paycheck every morning."
        girl "you're funny."
        girl "okay, i'll be back!"
        hide thankful_girl with dissolve
        y "okay... what am i supposed to... do?"
        y "argh... fine."
        show black with dissolve
        "you hang around the shop for a while, but no one comes in."
        hide black with dissolve
        y "......"
        y "this is boring!"
        y "...ew, these crabs are looking at me."
        show shadyguy_grin with dissolve
        sg "hey toots, have you re-thought-"
        hide shadyguy_grin
        show shadyguy_unsure
        with dissolve
        sg "ohhh... heyyy..."
        sg "sooooo...."
        hide shadyguy_unsure
        show shadyguy_grin
        with dissolve
        sg "what's up?"
        y "what are you doing here, shady?"
        sg "just... hanging out."
        sg "checking on... the crabs?"
        y "really? you're here to check on the crabs?"
        sg "i'm totally an animal... wellness... checking... person."
        y "...."
        y "that was really unconvincing."
        sg "yeah, i struggled to get through it."
        sg "i'll just go."
        y "come on, man... what are you doing here?"
        sg "ahh... well... if you {i}have{/i} to know..."
        sg "i was wondering if the shop girl wanted to become one of my employees."
        y "damn it, shady!"
        y "don't headhunt my employees!"
        sg "hey, we're buds, but business is business."
        y "would you get out of here already?"
        sg "sure!"
        sg "would you tell her to look me up when she gets back?"
        y "no!"
        y "shoo!"
        sg "aw, i'll try again later then."
        y "no, you-"
        sg "bye!"
        hide shadyguy_grin with dissolve
        y "...he's lucky he's charming."
        show black with dissolve
        "an hour or two passes... you lose all track of time."
        "you feel as though you're drifting through an endless void."
        "you poke a crab."
        hide black with dissolve
        y "i'm gonna name you sebastion."
        y "ow!" with hpunch
        y "don't snip me!"
        y "fine, you're now a marvin."
        y "how's that? does it sting a little?"
        y "because it should."
        y "....."
        y "...i take it back, no one should be named marvin-"
        y "ow!" with hpunch
        y "you snipped me again!"
        y "that's it! you're a marvin!"
        y "jerk."
        y "i'm gonna feed you to june's pet."
        y "...or june."
        y "I think she'd eat you uncooked, honestly."
        y "which is what you deserve."
        k3 "are you teasing the crabs?"
        show toki toki01 with dissolve
        y "no..."
        y "...."
        y "yes."
        y "what are you doing here?"
        y "...and do you need a crab?"
        y "there's one you can have for free."
        y "his name is marvin and he's a dick."
        "the crab angrily snips his claws in your direction."
        y "yeah, i'm talking about {i}you{i}."
        y "if she doesn't take you, you're fucking dinner, bud."
        k3 "come on, it's not his fault you don't know what you're doing here."
        y "okay, to be fair, i don't know what i'm doing anywhere."
        k3 "that's not a secret."
        y "...why are you here?"
        k3 "to get a book!"
        y "i... don't think we sell those."
        k3 "sure you do."
        k3 "i get them special ordered."
        y "well, i don't want to tell you that you're wrong, but i tried to buy a slutty novel here once and-"
        show toki_blink with dissolve
        k3 "it's under the counter, aang."
        y "it is?!"
        "you look under the counter and pull out a book titled: \"sassy girls in a male oriented world!\""
        y "...this is not a slutty novel."
        hide toki_blink
        show toki_angry
        with dissolve
        k3 "what? of course it isn't."
        hide toki_angry with dissolve
        k3 "this is my book."
        y "okay..."
        y "so where's mine?"
        show toki_angry with dissolve
        k3 "i don't know!"
        y "oh, you said-"
        hide toki_angry
        show toki_blink
        with dissolve
        k3 "you're infuriating sometimes, aang."
        y "so, what do you usually pay for this thing?"
        hide toki_blink with dissolve
        k3 "this much."
        $ emoney +=50
        play sound "audio/money.mp3"
        "you got 50 coins!"
        y "sweet, i can use this."
        y "i guess i'll see you around."
        show toki toki02
        with dissolve
        k3 "wait. aang."
        y "yes?"
        k3 "i..."
        k3 "well..."
        k3 "...be careful of your dreams."
        y "uh... what?"
        k3 "that's all i can say."
        k3 "just... be careful."
        y "you can't say that and not elaborate."
        y "what are you talking about?"
        show toki_blink with dissolve
        k3 "i shouldn't say, but..."
        k3 "...just because something's a dream doesn't mean it's not real."
        k3 "i don't envy your decisions, but... i know you'll make the right ones."
        y "right... decisions?"
        y "okay, katara, what exactly do you know?"
        hide toki_blink
        show toki toki01
        with dissolve
        k3 "what i {i}know{/i} is that you'll make the right decisions."
        k3 "i was told that by a... reliable source."
        y "who?"
        k3 "i have to go, aang."
        k3 "but... trust your gut."
        y "hold on..."
        hide toki with dissolve
        y "...damn it!"
        y "what does she know?!"
        y "this is a weird day."
        y "...."
        y "i bet it'll be another hour before-"
        show fireguard_halberd with dissolve
        fg "um... it's tits mcgee here?"
        y "what?"
        y "wait... her name is tits mcgee?"
        fg "i'm not really sure, to be honest."
        fg "i called her that once and she didn't correct me, but... what are the odds i guessed it?"
        y "...low."
        fg "right, but still."
        fg "there's the whole \"she didn't correct me\" thing."
        y "what are you doing here?"
        fg "i'm here for a crab."
        fg "it's a gift for my partner."
        fg "i hope he'll like it... he ate the last one."
        y "......"
        y "I have..."
        y "the {i}perfect{/i} crab for you."
        y "his name is marvin and he's fantastic."
        "you hear furious snipping behind you."
        "you raise your voice a little over the sound."
        y "he really wants a nice home with someone who accidentally eats his pets!"
        fg "that's a weird crab, but all right."
        fg "how much?"
        y "it's like... crapples or something, i don't really know."
        y "give me 100 coins and we'll call it even."
        fg "deal!"
        $ emoney +=100
        play sound "audio/money.mp3"
        "you got 100 coins!"
        y "great."
        y "you'll have to get him out yourself."
        y "he's... too friendly for me."
        fg "okay!"
        fg "jeff will love this!"
        hide fireguard_halberd with dissolve
        "the guard reaches into the crate and grabs the crab."
        fg "ouch!" with hpunch
        fg "he's mean!"
        y "...really?"
        show muskycrabshuffle with moveinright
        hide muskycrabshuffle with moveoutleft
        "the crab scuttles along the floor and out the door."
        show fireguard_halberd with dissolve
        y "huh."
        fg "marvin..."
        fg "hey, so, since my purchase just ran away, can i have my money back?"
        menu:
            "here you go":
                $ jeff_present = True
                $ emoney -=100
                play sound "audio/money.mp3"
                "you give him back his 100 coins."
                fg "thank you so much!"
                fg "wow, you're way nicer than tits!"
                y "thank... you?"
                fg "now jeff will get a present!"
            "no":

                $ jeff_present = False
                y "you lost me a perfectly angry... er... good crab."
                y "you lose it, you buy it."
                fg "that's fair..."
                fg "i guess jeff won't get a present after all..."
                fg "oh, well."

        fg "all right, i'm gonna go."
        y "dude, you are fire nation, what are you even doing here?"
        fg "what?"
        y "leave before you get killed by some random earth soldier."
        fg "that's a good call."
        y "i know."
        y "go away."
        fg "peace out!"
        hide fireguard_halberd
        with dissolve
        y "...."
        y "that poor idiot."
        show black with dissolve
        "you wait around for a little while longer."
        "you try to find any distraction."
        hide black with dissolve
        show thankful_girl with dissolve
        girl "hey, thanks for..."
        girl "is your finger in your nose?"
        y "...no."
        "you quickly take your finger out of your nose."
        y "so, did you get done what you needed to do?"
        girl "yup!"
        girl "just a quick orgy, it really helps break up a long day."
        y "....you left work for an orgy?"
        girl "a {i}quick{/i} orgy!"
        y "it was so boring! i feel like i've aged 20 years!"
        girl "i know, that's why i left."
        girl "you're not very smart, are you?"
        y "i'm not un-smart, you... talky... person..."
        y "...."
        y "nevermind."
        y "oh, shady came by."
        y "is he propositioning you?"
        girl "all the time."
        girl "i'm just not into old dudes."
        y "no, i mean... is he trying to get you to work for him?"
        girl "oh, yeah, that too."
        y "please don't."
        y "I really don't want your job."
        girl "aw, the job's not so bad... i like snippy."
        y "...snippy?"
        girl "yeah, the crab that snips his claws a lot!"
        girl "he's funny."
        y "...i have some bad news for you."
        y "nevermind, i'll tell you later."
        y "look, if you stay, i'll... give you a raise."
        girl "i don't really think you can pay me any more..."
        girl "unless you want to give me 95 percent of the profits?"
        y "what?! no!"
        y "wait, what do i pay you now?"
        girl "90 percent."
        y "....."
        y "...why?"
        girl "because you left me in charge of the money?"
        y "that's... fair."
        y "not super cool, but i guess i don't do any work here anyway."
        y "also, why do i buy things from you if i own this shop?"
        girl "business ethics?"
        y "what? who's going to check that?"
        y "it's not like we have an accountant."
        y "...."
        y "I'm gonna go to jail for tax fraud, aren't i?"
        girl "probably."
        y "damn it."
        y "well, they'll have to catch me first!"
        y "...."
        y "did that sound confident?"
        girl "sure. totally confident."
        y "alright, well, i guess i'll leave you to it."
        y "and don't... join shady."
        y "that dude is straight up untrustworthy."
        girl "trust me, i got that impression as well."
        girl "he offered to pay for dental, but... personally provide mammograms."
        y "i urge you not to take him up on that."
        girl "don't worry, these girls will stay shady-free."
        y "alright, i'm getting out of here before i get caught in any more retail hell."
        girl "later!"
        $ bk3_shop_watch = True
        jump love_bk3_village_background

    if toph_chat == 11 and not iroh_book_talk and not shop_book_talk:
        scene black
        scene inside_shop
        show thankful_girl
        with dissolve
        girl "oh, a customer!"
        girl "hello!"
        y "hey, do you sell books here?"
        girl "books on crab battles?"
        y "no, just books. in general."
        girl "no, i don't, sorry."
        y "...out of curiousity, do you sell books on crab battles?"
        girl "no."
        y "then why... never mind."
        y "i'll look somewhere else, thanks."
        girl "okay!"
        girl "take a look at my shop first, if you want!"
        $ shop_book_talk = True

    if shop_building >=2 and not shop_building2_talk:
        scene black
        scene inside_shop
        show thankful_girl
        with dissolve
        $ shop_building2_talk = True
        girl "thanks for upgrading the shop!"
        play sound "audio/win2.mp3"
        girl "for that, here's 5 crapples!"
        $ crapples +=5
        "you got 5 crapples!"
        girl "you've also expanded my inventory of items!"
        girl "aaannndd... i now sell saucy crab traps!"
        girl "take a look!"

    if market_stroll >=2:
        if crab1 and crabs_current ==0:
            scene black
            scene inside_shop
            show thankful_girl
            with dissolve
            girl "hey, i have a newer, better crab for you."
            girl "let me take that one off your hands...."
            $ crab1 = False
            girl "aaaannd.... here's your new one!"
            $ crabs_current +=1
            $ crabs_total +=1
            $ crab1_rarity = "r"
            $ crab1 = True
            $ crab_spot1_chosen = True
            $ crab_spot1 = 1
            $ crab1_set = True
            $ rand_crab1_type = renpy.random.randint(5, 11)
            $ deck_crabs +=1
            jump crab1_trap_get

        if crab1 and crabs_current >=1:
            scene black
            scene inside_shop
            show thankful_girl
            with dissolve
            girl "hey!"
            if not first_arena_match:
                girl "you should go check out the arena."
                girl "but since you're here, take a look at what i've got!"
            jump love_bk3_village_shop_menu

            label love_bk3_village_shop_menu:
                menu:
                    "random trap - 2 crapples":
                        if crapples <2:
                            "not enough crapples! you need to win them from trainers in the arena!"
                            jump love_bk3_village_shop_menu
                        else:
                            $ crapples -=2

                        $ crabs_current +=1
                        $ crabs_total +=1
                        if not crab1:
                            $ crab1_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ crab1 = True
                            $ crab_spot1_chosen = True
                            $ crab_spot1 = 1
                            $ crab1_set = True
                            $ rand_crab1_type = renpy.random.randint(1, 11)
                            $ deck_crabs +=1
                            jump crab1_trap_get
                        elif not crab2:
                            $ crab2 = True
                            $ crab2_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab2_type = renpy.random.randint(1, 11)
                            jump crab2_trap_get
                        elif not crab3:
                            $ crab3 = True
                            $ crab3_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab3_type = renpy.random.randint(1, 11)
                            jump crab3_trap_get
                        elif not crab4:
                            $ crab4 = True
                            $ crab4_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab4_type = renpy.random.randint(1, 11)
                            jump crab4_trap_get
                        elif not crab5:
                            $ crab5 = True
                            $ crab5_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab5_type = renpy.random.randint(1, 11)
                            jump crab5_trap_get
                        elif not crab6:
                            $ crab6 = True
                            $ crab6_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab6_type = renpy.random.randint(1, 11)
                            jump crab6_trap_get
                        elif not crab7:
                            $ crab7 = True
                            $ crab7_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab7_type = renpy.random.randint(1, 11)
                            jump crab7_trap_get
                        elif not crab8:
                            $ crab8 = True
                            $ crab8_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab8_type = renpy.random.randint(1, 11)
                            jump crab8_trap_get
                        elif not crab9:
                            $ crab9 = True
                            $ crab9_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab9_type = renpy.random.randint(1, 11)
                            jump crab9_trap_get
                        elif not crab10:
                            $ crab10 = True
                            $ crab10_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab10_type = renpy.random.randint(1, 11)
                            jump crab10_trap_get
                        elif not crab11:
                            $ crab11 = True
                            $ crab11_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab11_type = renpy.random.randint(1, 11)
                            jump crab11_trap_get
                        elif not crab12:
                            $ crab12 = True
                            $ crab12_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab12_type = renpy.random.randint(1, 11)
                            jump crab12_trap_get
                        elif not crab13:
                            $ crab13 = True
                            $ crab13_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab13_type = renpy.random.randint(1, 11)
                            jump crab13_trap_get
                        elif not crab14:
                            $ crab14 = True
                            $ crab14_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab14_type = renpy.random.randint(1, 11)
                            jump crab14_trap_get
                        elif not crab15:
                            $ crab15 = True
                            $ crab15_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab15_type = renpy.random.randint(1, 11)
                            jump crab15_trap_get
                        elif not crab16:
                            $ crab16 = True
                            $ crab16_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab16_type = renpy.random.randint(1, 11)
                            jump crab16_trap_get
                        elif not crab17:
                            $ crab17 = True
                            $ crab17_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab17_type = renpy.random.randint(1, 11)
                            jump crab17_trap_get
                        elif not crab18:
                            $ crab18 = True
                            $ crab18_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab18_type = renpy.random.randint(1, 11)
                            jump crab18_trap_get
                        elif not crab19:
                            $ crab19 = True
                            $ crab19_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab19_type = renpy.random.randint(1, 11)
                            jump crab19_trap_get
                        elif not crab20:
                            $ crab20 = True
                            $ crab20_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab20_type = renpy.random.randint(1, 11)
                            jump crab20_trap_get
                        elif not crab21:
                            $ crab21 = True
                            $ crab21_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab21_type = renpy.random.randint(1, 11)
                            jump crab21_trap_get
                        elif not crab22:
                            $ crab22 = True
                            $ crab22_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab22_type = renpy.random.randint(1, 11)
                            jump crab22_trap_get
                        elif not crab23:
                            $ crab23 = True
                            $ crab23_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab23_type = renpy.random.randint(1, 11)
                            jump crab22_trap_get
                        elif not crab24:
                            $ crab24 = True
                            $ crab24_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab24_type = renpy.random.randint(1, 11)
                            jump crab24_trap_get
                        elif not crab25:
                            $ crab25 = True
                            $ crab25_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab25_type = renpy.random.randint(1, 11)
                            jump crab25_trap_get
                        elif not crab26:
                            $ crab26 = True
                            $ crab26_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab26_type = renpy.random.randint(1, 11)
                            jump crab26_trap_get
                        elif not crab27:
                            $ crab27 = True
                            $ crab27_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab27_type = renpy.random.randint(1, 11)
                            jump crab27_trap_get
                        elif not crab28:
                            $ crab28 = True
                            $ crab28_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab28_type = renpy.random.randint(1, 11)
                            jump crab28_trap_get
                        elif not crab29:
                            $ crab29 = True
                            $ crab29_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab29_type = renpy.random.randint(1, 11)
                            jump crab29_trap_get
                        elif not crab30:
                            $ crab30 = True
                            $ crab30_rarity = WeightedChoice([("n", 0.55), ("r", 0.35), ("e", 0.1)])
                            $ rand_crab30_type = renpy.random.randint(1, 11)
                            jump crab30_trap_get
                        else:
                            $ crabs_current -=1
                            $ crabs_total -=1
                            "girl" "you have too many crabs!"
                            y "......"
                            "girl" "you've gotta get rid of some before you can get more."
                            jump love_bk3_village_shop_menu

                    "saucy trap - 5 crapples" if shop_building <2:
                        girl "i gave you my only saucy crab trap, i don't have the resources to find better crabs."
                        girl "but..."
                        girl "if you help me upgrade the shop, i'll be able to start stocking saucy crabtraps!"
                        girl "think about it!"
                        jump love_bk3_village_shop_menu

                    "saucy trap - 5 crapples" if shop_building >=2:
                        if crapples <5:
                            "not enough crapples! you need to win them from trainers in the arena!"
                            jump love_bk3_village_shop_menu
                        else:
                            $ crapples -=5

                        $ crabs_current +=1
                        $ crabs_total +=1
                        if not crab1:
                            $ crab1_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ crab1 = True
                            $ crab_spot1_chosen = True
                            $ crab_spot1 = 1
                            $ crab1_set = True
                            $ rand_crab1_type = renpy.random.randint(1, 11)
                            $ deck_crabs +=1
                            jump crab1_trap_get
                        elif not crab2:
                            $ crab2 = True
                            $ crab2_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab2_type = renpy.random.randint(1, 11)
                            jump crab2_trap_get
                        elif not crab3:
                            $ crab3 = True
                            $ crab3_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab3_type = renpy.random.randint(1, 11)
                            jump crab3_trap_get
                        elif not crab4:
                            $ crab4 = True
                            $ crab4_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab4_type = renpy.random.randint(1, 11)
                            jump crab4_trap_get
                        elif not crab5:
                            $ crab5 = True
                            $ crab5_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab5_type = renpy.random.randint(1, 11)
                            jump crab5_trap_get
                        elif not crab6:
                            $ crab6 = True
                            $ crab6_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab6_type = renpy.random.randint(1, 11)
                            jump crab6_trap_get
                        elif not crab7:
                            $ crab7 = True
                            $ crab7_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab7_type = renpy.random.randint(1, 11)
                            jump crab7_trap_get
                        elif not crab8:
                            $ crab8 = True
                            $ crab8_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab8_type = renpy.random.randint(1, 11)
                            jump crab8_trap_get
                        elif not crab9:
                            $ crab9 = True
                            $ crab9_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab9_type = renpy.random.randint(1, 11)
                            jump crab9_trap_get
                        elif not crab10:
                            $ crab10 = True
                            $ crab10_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab10_type = renpy.random.randint(1, 11)
                            jump crab10_trap_get
                        elif not crab11:
                            $ crab11 = True
                            $ crab11_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab11_type = renpy.random.randint(1, 11)
                            jump crab11_trap_get
                        elif not crab12:
                            $ crab12 = True
                            $ crab12_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab12_type = renpy.random.randint(1, 11)
                            jump crab12_trap_get
                        elif not crab13:
                            $ crab13 = True
                            $ crab13_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab13_type = renpy.random.randint(1, 11)
                            jump crab13_trap_get
                        elif not crab14:
                            $ crab14 = True
                            $ crab14_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab14_type = renpy.random.randint(1, 11)
                            jump crab14_trap_get
                        elif not crab15:
                            $ crab15 = True
                            $ crab15_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab15_type = renpy.random.randint(1, 11)
                            jump crab15_trap_get
                        elif not crab16:
                            $ crab16 = True
                            $ crab16_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab16_type = renpy.random.randint(1, 11)
                            jump crab16_trap_get
                        elif not crab17:
                            $ crab17 = True
                            $ crab17_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab17_type = renpy.random.randint(1, 11)
                            jump crab17_trap_get
                        elif not crab18:
                            $ crab18 = True
                            $ crab18_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab18_type = renpy.random.randint(1, 11)
                            jump crab18_trap_get
                        elif not crab19:
                            $ crab19 = True
                            $ crab19_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab19_type = renpy.random.randint(1, 11)
                            jump crab19_trap_get
                        elif not crab20:
                            $ crab20 = True
                            $ crab20_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab20_type = renpy.random.randint(1, 11)
                            jump crab20_trap_get
                        elif not crab21:
                            $ crab21 = True
                            $ crab21_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab21_type = renpy.random.randint(1, 11)
                            jump crab21_trap_get
                        elif not crab22:
                            $ crab22 = True
                            $ crab22_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab22_type = renpy.random.randint(1, 11)
                            jump crab22_trap_get
                        elif not crab23:
                            $ crab23 = True
                            $ crab23_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab23_type = renpy.random.randint(1, 11)
                            jump crab23_trap_get
                        elif not crab24:
                            $ crab24 = True
                            $ crab24_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab24_type = renpy.random.randint(1, 11)
                            jump crab24_trap_get
                        elif not crab25:
                            $ crab25 = True
                            $ crab25_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab25_type = renpy.random.randint(1, 11)
                            jump crab25_trap_get
                        elif not crab26:
                            $ crab26 = True
                            $ crab26_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab26_type = renpy.random.randint(1, 11)
                            jump crab26_trap_get
                        elif not crab27:
                            $ crab27 = True
                            $ crab27_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab27_type = renpy.random.randint(1, 11)
                            jump crab27_trap_get
                        elif not crab28:
                            $ crab28 = True
                            $ crab28_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab28_type = renpy.random.randint(1, 11)
                            jump crab28_trap_get
                        elif not crab29:
                            $ crab29 = True
                            $ crab29_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab29_type = renpy.random.randint(1, 11)
                            jump crab29_trap_get
                        elif not crab30:
                            $ crab30 = True
                            $ crab30_rarity = WeightedChoice([("n", 0.2), ("r", 0.5), ("e", 0.3)])
                            $ rand_crab30_type = renpy.random.randint(1, 11)
                            jump crab30_trap_get
                        else:
                            $ crabs_current -=1
                            $ crabs_total -=1
                            "girl" "you have too many crabs!"
                            y "......"
                            "girl" "you've gotta get rid of some before you can get more."
                            jump love_bk3_village_background

                    "buy items" if shop_building <=1:
                        girl "i don't have much space for inventory yet."
                        girl "if you help me upgrade the shop, i'll be able to start stocking better items for the arena!"
                        menu:
                            "crab pocket - 15":
                                if emoney >=15:
                                    play sound "audio/win2.mp3"
                                    $ emoney -=15
                                    $ arena_pocket +=1
                                    "catch crabs!"
                                    jump love_bk3_village_shop_menu
                                else:
                                    "not enough money..."
                                    jump love_bk3_village_shop_menu
                            "crab health potion - 20":
                                if emoney >=20:
                                    play sound "audio/win2.mp3"
                                    $ emoney -=20
                                    $ arena_potion +=1
                                    "keep your crabs healthy!"
                                    jump love_bk3_village_shop_menu
                            "smelling salts - 15":

                                if emoney >=15:
                                    play sound "audio/win2.mp3"
                                    $ emoney -=15
                                    $ arena_salts +=1
                                    "cures confusion when used!"
                                    jump love_bk3_village_shop_menu
                                else:
                                    "not enough money..."
                                    jump love_bk3_village_shop_menu
                            "------(locked)":

                                "test"
                            "------(locked)":

                                "test"
                            "------(locked)":

                                "test"
                            "------(locked)":

                                "test"
                            "cancel":

                                jump love_bk3_village_shop_menu

                    "buy items" if shop_building >=2:
                        jump love_bk3_village_shop_item_menu

                        label love_bk3_village_shop_item_menu:
                            menu:
                                "crab pocket - 15":
                                    girl "used to catch crabs!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_pocket +=1

                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "buy 5 - 65":
                                            if emoney >=75:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=75
                                                $ arena_pocket +=5

                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "back":
                                            jump love_bk3_village_shop_item_menu
                                "crab health potion - 20":

                                    girl "keep your crabs healthy!"
                                    menu:
                                        "buy":
                                            if emoney >=20:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=20
                                                $ arena_potion +=1
                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "buy 5 - 80":
                                            if emoney >=80:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=80
                                                $ arena_potion +=5
                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "exit":

                                            jump love_bk3_village_shop_item_menu
                                "smelling salts - 15":
                                    girl "cures confusion when used!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_salts +=1

                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "back":
                                            jump love_bk3_village_shop_item_menu
                                "antidote - 15":
                                    girl "cures posion when used!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_antidote +=1
                                                "cures posion when used!"
                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "exit":
                                            jump love_bk3_village_shop_item_menu
                                "steroids - 15":
                                    girl "cures weak when used!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_steroid +=1
                                                "cures weak when used!"
                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "exit":
                                            jump love_bk3_village_shop_item_menu
                                "cure-all - 80":
                                    girl "cures your crab of all diseases (and status effects). Ironic."
                                    menu:
                                        "buy":

                                            if emoney >=80:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=80
                                                $ cureall +=1
                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump love_bk3_village_shop_item_menu
                                        "exit":
                                            jump love_bk3_village_shop_item_menu
                                "rarity stone - 2 crapples":
                                    girl "rarity stones make your crabs more powerful and harder to remove!"
                                    menu:
                                        "buy":
                                            if crapples >=2:
                                                $ crapples -=2
                                                $ rarity_stones += 1
                                                play sound "audio/win2.mp3"
                                                "you got a rarity stone!"
                                                jump love_bk3_village_shop_item_menu
                                            else:
                                                "not enough crapples..."
                                                jump love_bk3_village_shop_item_menu
                                        "exit":
                                            jump love_bk3_village_shop_item_menu



                                    jump love_bk3_village_shop_item_menu
                                "cancel":
                                    jump love_bk3_village_shop_menu
                    "please kill my savebug":

                        y "hey, what is this thing?"
                        y "why is this option here?"
                        girl "i've heard there's a bug that keeps some people from being able to save."
                        y "well that's not good."
                        girl "this fix will most likely work, but it could mess things up..."
                        girl "i can't be sure."
                        girl "if you don't already have a problem saving, you're probably fine."
                        girl "you can come back later and try this option if you ever have save issues."
                        menu:
                            "do it! apply the fix":
                                $ time = None
                                $ renpy.game.log.log=[]
                                girl "okay, stand back."
                                y "did it work?"
                                girl "only way to tell is to try and save your game."
                            "maybe later":

                                y "i'll try an older save game."
                                girl "your call."
                                girl "come back if you have a problem."

                        jump love_bk3_village_background
                    "exit":

                        girl "come back soon!"
                        jump love_bk3_village_background

        if not crab1 and crabs_current ==0:
            scene black
            scene inside_shop
            show thankful_girl
            with dissolve
            "girl" "hey!"
            "girl" "what can i get for you?"
            y "what do you have?"
            "girl" "well.... i come from a long line of crab catchers."
            y "....what?"
            "girl" "i've decided i want to sell crab traps..."
            "girl" "you know, for the arena."
            y "oh. i actually haven't checked out the arena yet."
            "girl" "really?"
            "girl" "well... because you saved me, I'll give you a crab trap for free."
            y "i'm still a little confused."
            "girl" "wait... do you not know about pocket crabs?"
            "girl" "it's a huge craze, especially out on ember island."
            "girl" "but the arena in the city is the biggest spot for it."
            "girl" "if you go to the arena, i'm sure they'll give you more instructions."
            y "uh... thanks."
            "girl" "my pleasure!"
            "girl" "oh! and don't forget your free saucy crab trap!"
            y "...saucy?"
            "girl" "oh, well, i sell two different types of traps here - random and saucy."
            "girl" "random traps have any random crab in them, and they're cheaper..."
            "girl" "saucy traps have a higher chance of a rare or epic crab, but they're a little more expensive."
            "girl" "i'm giving you a free saucy crab trap."
            "girl" "good luck!"
            play sound "audio/win2.mp3"
            show holo_crab_trap at truecenter:
                zoom .8
            "you got a crab trap!"
            show ctc
            pause
            hide ctc
            hide holo_crab_trap
            play sound "audio/win2.mp3"

            $ crabs_current +=1
            $ crabs_total +=1
            if not crab1:
                $ crab1_rarity = "r"
                $ crab1 = True
                $ crab_spot1_chosen = True
                $ crab_spot1 = 1
                $ crab1_set = True
                $ rand_crab1_type = renpy.random.randint(5, 11)
                $ deck_crabs +=1
                jump crab1_trap_get
    else:


        "this store has no shopkeeper yet."
        jump love_bk3_village_background



label love_inside_tavern_shack:


    stop music
    play music "audio/Achaidh Cheide.mp3"

    if bk3_day:
        scene black
        scene inside_tavern_day
        with dissolve
    if not bk3_day:
        scene black
        scene inside_tavern_night
        with dissolve

    if love_ty_sex_quest ==2 or love_ty_sex_quest ==3:
        y "suki?"
        y "...hello?"
        y "are you here?"
        y "...maybe i should ask ty lee if she knows where suki is."
        $ love_ty_sex_quest = 3

    if jin_anti_hypno_start ==3:
        show tojn tojn20 with dissolve
        jin "hey!"
        jin "took you long enough."
        y "yeah, but i'm here."
        y "let's get you some food."
        jin "oh, i already ate."
        y "...oh."
        y "right."
        y "well..."
        y "how are you feeling?"
        jin "honestly?"
        jin "...a little horny."
        y "....."
        y "shit."
        y "it didn't work."
        jin "what?"
        jin "oh, no, nothing near what i was feeling earlier."
        jin "i've always had a really high libido."
        jin "...maybe you can find out."
        y "oh?"
        jin "well, i'm exhausted... and full."
        jin "i'm heading back to the boarding house."
        jin "will i see you later?"
        y "sure, i can swing by."
        jin "great!"
        jin "see you later, then!"
        $ jin_anti_hypno_start = 4
        jump love_bk3_village_background

    if love_toph_sex and not haiku_battle:
        show tosi tosi01 with dissolve
        suki "aang, i'm going nuts here."
        y "what?"
        suki "i have had a crazy day..."
        suki "do you know anywhere that i can go to hide for the day?"
        suki "i need to get away from the tavern for a bit."
        y "hmm..."
        y "how about the house in the city?"
        y "that's pretty abandoned."
        suki "sounds perfect."
        suki "can you take me?"
        suki "i don't know where it is."
        menu:
            "let's go":
                y "sure."
                scene black with dissolve
                jump haiku_quest
            "not right now":

                y "a bit later."
                jump love_bk3_village_background

    if jin_quick_talk ==10 and not bk3_day:
        show tosi tosi01 with dissolve
        suki "hey-oh."
        suki "what're you doing here?"
        y "jin has seemed down, so i'm meeting her here."
        y "giving her kind of a date night sort of thing."
        show tosi_smile with dissolve
        suki "aw... you're just a big softy."
        y "shut up! no i'm not!"
        y "...."
        y "okay, maybe."
        y "just go make us some food, huh?"
        suki "okay... softy."
        hide tosi_smile
        hide tosi
        with dissolve
        y "now for a classy touch...."
        show bk_candle_flame
        with Dissolve(1)
        "you pull out a candle and place it on the table."
        y "nice."
        show tojn tojn20 with dissolve
        jin "a-aang?"
        jin "were you serious about..."
        show tojn tojn23 with dissolve
        jin "oh!"
        show tojn tojn24 with dissolve
        jin "oh, aang!"
        y "what? are you okay?"
        jin "I'm... trying not to cry..."
        show tojn tojn20 with dissolve
        jin "this is wonderful..."
        jin "let's sit."
        show black with dissolve
        "you and jin sit and talk throughout the night..."
        "alternating between laughing and getting to know each other better."
        hide black with dissolve
        jin "this... this was wonderful, aang."
        jin "you're... just the best... i'm so lucky to..."
        jin "and you're so handsome and... and..."
        jin "...you like me? really?"
        y "duh."
        jin "...."
        jin "meet me at my place later."
        jin "i'll see you there."
        hide tojn with moveoutleft
        y "....she seemed in a hurry."
        $ jin_quick_talk = 11
        $ bk3_day = False
        jump love_bk3_village_background

    if suki_tylee >=7:
        if not love_suki_sex:
            hide screen earth_money_date
            show tosi tosi01 with dissolve
            suki "hey!"
            y "you seem chipper."
            suki "i am."
            suki "hey, can you come with me for a minute?"
            menu:
                "sure":
                    y "lead the way."
                    scene black with dissolve
                    scene inside_tavern_1
                    show tosi tosi01
                    show tosi_blink
                    with dissolve
                    y "what's up?"
                    suki "i can't believe i've been so..."
                    y "what?"
                    hide tosi_blink with dissolve
                    suki "...so dense!"
                    y "come again?"
                    show tosi_smile with dissolve
                    suki "you're amazing!"
                    y "baby you know it."
                    y "i'm guessing it went well with ty lee?"
                    suki "yes!"
                    suki "she and i are actually getting along really well now."
                    y "that was fast..."
                    suki "i totally misjudged her."
                    suki "she's helping me put together a plan to get revenge."
                    suki "let's just say... pretty soon azula won't have any friends."
                    y "you're gonna ruin her friendship with mai?"
                    hide tosi_smile with dissolve
                    suki "we have several different ideas at the moment."
                    suki "but that's enough of that for now."
                    suki "Let's focus on the most important thing."
                    y "...which is?"
                    suki "you."
                    y "....i like that."
                    suki "you are handsome...."
                    show tosi tosi04 with dissolve
                    show ctc
                    pause
                    hide ctc
                    suki "and brilliant...."
                    show tosi tosi05
                    show tosi_blush
                    with dissolve
                    show ctc
                    pause
                    hide ctc
                    suki "and incredible...."
                    show tosi tosi06
                    show tosi_smile
                    hide tosi_blush
                    show tosi_blush
                    with dissolve
                    show ctc
                    pause
                    hide ctc
                    y "that's a cheeky smile."
                    suki "and i want to thank you."
                    menu:
                        "good":
                            y "and you should."
                            suki "i know."
                        "only if you want to":
                            y "that's not necessary..."
                            suki "shh..."
                            suki "this is for me, too."
                    hide tosi_smile with dissolve
                    suki "i've been thinking about you since you rescued me."
                    suki "....well?"
                    y "well what?"
                    suki "do i have to say it?"
                    y "say what?"
                    show tosi_smile
                    show tosi_blink
                    hide tosi_blush
                    show tosi_blush
                    with dissolve
                    suki "*sigh...*"
                    suki "boys...."
                    hide tosi_blink
                    hide tosi_smile
                    with dissolve
                    suki "take off your pants!"
                    suki "i'm going to ride you so hard you cum out my throat."
                    y "oh. shit."
                    show tosi_smile
                    hide tosi_blush
                    show tosi_blush
                    with dissolve
                    suki "....well?"
                    y "right. pants off."
                    jump suki_lovefuck
                "later":

                    y "a little later."
                    suki "oh... okay."
                    jump love_bk3_village_background

    if suki_tylee ==2:
        if love_jd_hypno ==9:
            jump earth_soldier_follow
        else:

            pass

    if suki_tylee ==1:
        show tosi tosi03 with dissolve
        suki "get out."
        play sound "audio/thud.mp3"
        scene black with vpunch
        "suki slams the tavern door in your face."
        y "....damn it all."
        jump love_bk3_village_background

    if tylee_board and suki_tylee ==0:
        $ suki_tylee = 1
        show tosi tosi03 with dissolve
        suki "what the {i}hell{/i}, aang?!"
        y "what?"
        suki "I'm so mad at you, i could spit!"
        y "...but could you swallow?"
        suki "what?"
        suki "no, shut up."
        suki "you brought a sworn enemy of mine... one you promised to help me remove... into our fucking village!"
        suki "what the shit?!"
        y "calm down, suki."
        suki "don't fucking tell me to calm down!"
        suki "tell me what the {i}fuck{/i} you think you're thinking!"
        suki "get rid of her or i will!"
        y "okay, you really need to calm-"
        suki "shut up, aang!"
        suki "i'm not talking about this!"
        suki "do you understand what she did to me?"
        suki "to my friends?"
        suki "to my cultural fucking heritage?"
        y "i mean... sorta?"
        suki "well, since you're not all that sure, how about i fucking {i}enlighten{/i} you?"
        suki "she and her slut friends {i}hurt{/i} us... then threw us in an underground maze..."
        suki "...i don't even know if my friends escaped or are still stuck down there..."
        suki "...and {i}then{/i} they stole our clothing and makeup... which i trained and fought for the honor to wear..."
        suki "so that they can better overthrow my nation!"
        suki "do you fucking {i}get{/i} it now, aang?!"
        y "okay, that sucks, but-"
        suki "no!"
        suki "you can't talk your way out of this!"
        suki "do something about it or i will!"
        y "suki..."
        suki "we're done talking."
        y "don't-"
        hide tosi with dissolve
        y "....fuck."
        jump love_bk3_village_background

    if love_jd_hypno >=7 and not suki_revenge_talk:
        $ suki_revenge_talk = True
        show tosi tosi01 with dissolve
        suki "hey, i'm glad you stopped by."
        y "oh?"
        y "what's up?"
        suki "will you sit with me?"
        y "sure, after you."
        hide screen earth_money_date

        scene black
        show expression "bk3/toph/assmassage/background.jpg"

        show toam toam01
        show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
            xpos 0 ypos 0
        with fade
        suki "so."
        y "yeah...?"
        suki "raiding the city didn't work."
        y "right."
        suki "how... how do i get revenge on those bitches?"
        y "Hmmm...."
        y "i don't know."
        hide expression "bk3/toph/assmassage/suki_eyesonplayer.png" with dissolve
        suki "....shoot."
        y "look, i promise i'll... come up with a new idea to help you get revenge."
        y "okay?"
        show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
            xpos 0 ypos 0
        suki "you mean it?"
        y "yeah."
        suki "alright, i'll... wait."
        suki "I hope you come up with something good."
        suki "especially to help me with that main azula bitch."
        y "I'll work on it."
        suki "thanks, aang."
        y "no biggie."
        jump love_bk3_village_background

    if earthbending ==15 and not suki_toph_ass:
        $ suki_toph_ass = True
        jump toph_ass_massage

    if love_suki_hypno ==1 or love_suki_hypno ==2:
        if suki_dl_tits:
            show tosi tosi05
            show tosi_hypno_eyes
            with dissolve
        else:
            show tosi tosi04
            show tosi_hypno_eyes
            with dissolve

        show ctc
        pause
        hide ctc
        if love_suki_hypno ==1:
            y "i should get katara."
            show ctc
            pause
            hide ctc
            jump love_bk3_village_background
        if love_suki_hypno ==2:
            show toki toki01:
                xzoom -1
            with dissolve
            k3 "oh... my."
            k3 "suki?"
            suki "......."
            y "see?"
            k3 "right...."
            k3 "can you grab me some water?"
            y "sure, hold on."
            show black with dissolve
            y "finding water..."
            y "there's a tub of it back here."
            y "i hope we don't give this to the customers."
            y "....i really don't know anything about this place."
            hide black with dissolve
            y "alright, i got the water."
            k3 "good, put it down, and..."
            show black with dissolve
            "katara bends some of the water up over suki's ears."
            "other than blocking out sound, it's not really clear what she's doing."
            "suki begins mumbling and blinking, though."
            hide black with dissolve
            suki "king... lake..."
            hide tosi_hypno_eyes with dissolve
            suki "what.... oh, hi aang."
            show tosi_surprise with dissolve
            suki "...wait, what the..."
            hide tosi_surprise
            show tosi tosi03
            hide tosi_angry
            with vshake
            suki "what the damn hell?!"
            suki "why was i naked?!"
            suki "what the hell is going on?!"
            k3 "you were hypnotized, dear."
            show tosi_surprise with dissolve
            suki "katara?"
            k3 "yes, aang brought me."
            suki "he... he did?"
            y "there was a guard in here, undressing you with some kind of brainwashing."
            y "i, uh, sprung into action."
            y "immediately."
            y "did not pause."
            if suki_dl_tits:
                y "....also, your tits are nice."
            suki "okay...."
            show tosi_angry
            hide tosi_surprise
            with dissolve
            suki "this is exactly what i was afraid of!"
            suki "that fucking hypnosis equipment...."
            suki "what the fuck am i supposed to do now?"
            y "uh..."
            y "katara, did you fix her?"
            k3 "no, i got her out of the trance, but she could be put back into one at any time."
            suki "well, shit."
            suki "do we have any other options?"
            y "i have-"
            suki "wait, aang! you have anti-hypnosis equipment now, right?"
            y "well, i was gonna mention-"
            suki "can we use it?"
            y "i was-"
            suki "come on, help me out."
            y "....."
            y "....yes, obviously."
            y "if you'd just quit interrupting."
            suki "oh. sorry."
            y "I don't know how many sessions it'll take though."
            suki "let's get started then."
            suki "i'll meet you there."
            k3 "and i'll see you later, aang."
            k3 "Let me know if you need any more help."
            $ love_suki_hypno = 3
            jump love_bk3_village_background
    if love_suki_hypno ==7:
        show tosi tosi01
        show tosi_hypno_eyes
        with dissolve
        y "i should get katara."
        jump love_bk3_village_background
    if love_suki_hypno ==8:
        show tosi tosi01
        show tosi_hypno_eyes
        show toki toki01:
            xzoom -1
        with dissolve
        k3 "right."
        k3 "i'm coming to you, suki."
        show black with dissolve
        "katara works her waterbending on suki's ears again."
        hide black
        with dissolve
        hide tosi_hypno_eyes with dissolve
        suki "wh-"
        suki "......"
        show tosi_surprise with dissolve
        suki "...katara?"
        suki "what...."
        show tosi tosi03
        hide tosi_surprise
        with dissolve
        suki "it happened again, didn't it?"
        y "yes, unfortunately."
        y "our sessions helped though, he couldn't get you to do what he wanted."
        show tosi tosi01
        show tosi_blink
        with dissolve
        suki "at least there's a small comfort."
        hide tosi_blink with dissolve
        suki "so shall i meet you at your house?"
        y "i think the sooner the better."
        suki "i agree."
        suki "i'll see you there."
        k3 "good luck!"
        $ love_suki_hypno = 9
        jump love_bk3_village_background

    if suki_lantern_explain and love_suki_hypno ==0:
        $ love_suki_hypno = 1
        jump suki_dl_hypno

    if brothel_quest >=8 and not suki_tavern_bartender:
        $ suki_tavern_bartender = True
        show tosi tosi01 with dissolve
        suki "this is great!"
        y "well, june's old room is yours if you want it."
        suki "thanks, aang!"
        suki "i'll totally work for my place here as a bartender."
        suki "i can handle people."
        suki "aggressively, if necessary."
        y "sounds good."
        hide tosi with dissolve

    if joodee_revenge and not suki_bar_talk:
        $ suki_bar_talk = True
        show tosi tosi01 with dissolve
        suki "hey, aang."
        suki "did you find your mystery assassin?"
        y "i did, yeah."
        y "it was... satisfying."
        suki "that's good."
        show tosi tosi03 with dissolve
        suki "i hope you beat her ass."
        y "her tits, actually."
        show tosi tosi01
        show tosi_surprise
        with dissolve
        suki "her..."
        y "don't worry about it."
        y "hey... can i get a drink?"
        show tosi_smile
        hide tosi_surprise
        with dissolve
        suki "oh!"
        suki "sure."
        suki "here."
        "suki hands you a brimming mug."
        y "thanks."
        y "it's been... a long couple of days."
        hide tosi_smile with dissolve
        suki "i get that."
        y "I don't have a house."
        suki "you said that. several times."
        y "well, it's a big deal!"
        show tosi_blink with dissolve
        suki "like i said, i get it."
        y "at least i can stay with toph."
        hide tosi_blink with dissolve
        suki "actually, that got me thinking..."
        suki "can't she just earthbend you a new house?"
        y "....huh."
        y "probably."
        y "i'll definitely need her help removing all the rubble and building a foundation."
        y "i'm not that good yet."
        suki "hmm..."
        show tosi_blink with dissolve
        suki "i wonder why she hasn't mentioned it?"
        y "dunno."
        y "guess i'll go talk to her about it."
        hide tosi_blink with dissolve
        suki "well, good luck, aang."
        jump love_bk3_village_background

    if june_freed and not june_brothel:
        if not june_brothel_talk:
            show toju toju01 with dissolve
            ju "hey."
            y "who-"
            y "oh... you're the chick i rescued from the maze."
            show toju toju02 with dissolve
            ju "that's me."
            y "so are you gonna work here?"
            ju "no, i don't think so."
            y "great, you can-"
            y "wait, what?"
            show toju toju01 with dissolve
            ju "i want to relax here, not {i}work{/i} here."
            y "uh."
            y "then where are you staying?"
            ju "nowhere yet."
            ju "i guess i'll stay here in the meantime, if you've got a few extra rooms."
            y "you can't just stay here..."
            show toju toju03 with dissolve
            ju "what was that?"
            y "...without getting your free complimentary travel mug!"
            show toju toju02 with dissolve
            ju "oh, now that's sweet."
            y "well... you can't stay here forever."
            y "do you have a preference?"
            ju "I don't know..."
            ju "do you hicks have a brothel?"
            y "a... brothel?"
            y "you want to stay in a brothel?"
            ju "sure, why not?"
            ju "i'm not going to fuck anyone, but it's a good place to pick up bounty clients... and bounties, honestly."
            ju "besides, there's usually good security and privacy."
            y "well... damn. that was well thought out."
            y "alright, i'll keep you posted."
            ju "good."
            ju "now, i'm going to drink."
            ju "don't bug me."
            $ june_brothel_talk = True
            hide toju with dissolve

    if love_ty_sex_quest >3 and toph_chat >= 24 and suki_bar_blow <=6:
        if not bk3_day:
            if suki_bar_blow ==0:
                show tosi tosi01 with dissolve
                suki "hey, i'm sure you're busy, but..."
                suki "if you can come by during the day, i'd really appreciate it."
                suki "oh crap, i gotta refill that guy's drink."
                hide tosi with dissolve
            if suki_bar_blow ==3:
                show tosi tosi01
                with dissolve
                suki "thanks for helping me with the bar, but i need another favor."
                suki "if you can come by during the day, i'd really appreciate it."
                hide tosi with dissolve
            if suki_bar_blow ==6:
                scene black
                show expression "ebackgrounds/inside_tavern_night.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                show tosi_smile
                with dissolve
                suki "so? will you watch the bar?"
            if suki_bar_blow ==5:
                $ suki_bar_blow = 6
                scene black
                show expression "ebackgrounds/inside_tavern_night.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                with dissolve
                suki "great! i need your help again."
                y "aw man, come on."
                suki "trust me, it'll be worth it."
                show tosi_smile with dissolve
                suki "you might even have fun."
                y "i doubt it."
                suki "will you help me or not?"
                $ suki_bar_blow = 6
            if suki_bar_blow ==6:
                menu:
                    "watch the bar again. again.":
                        y "fine, but this is the last time!"
                        show tosi_blink with dissolve
                        suki "maybe..."
                        y "what?"
                        hide tosi_blink with dissolve
                        suki "thanks, aang."
                        suki "and i'll take care of what i need to."
                        y "i get it, go."
                        hide tosi_smile
                        hide tosi
                        with moveoutleft
                        jump suki_barblow
                    "not now":
                        hide tosi_smile with dissolve
                        suki "awww...."
                        jump love_bk3_village_background


        if bk3_day:
            if suki_bar_blow ==5:
                show expression "ebackgrounds/inside_tavern_day.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                with dissolve
                suki "hey, i had an idea."
                suki "come by at night and i'll go over it over with you."
                hide tosi with dissolve
            if suki_bar_blow ==4:
                show expression "ebackgrounds/inside_tavern_day.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                with dissolve
                suki "will you help me out?"
            if suki_bar_blow ==3:
                $ suki_bar_blow = 4
                show expression "ebackgrounds/inside_tavern_day.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                with dissolve
                suki "hey, so... i need your help again."
                suki "i have a new lead on getting my friends out."
                y "what can i do?"
                suki "can you watch the bar again?"
                y ".........."
                y "...................."
                y "what else can i do?"
                suki "come on!"
                suki "please!"
                $ suki_bar_blow =4
            if suki_bar_blow ==4:
                menu:
                    "watch the bar again":
                        y "alright, alright."
                        show tosi_smile with dissolve
                        suki "you're the best."
                        y "I know."
                        hide tosi_smile
                        hide tosi
                        with moveoutleft
                        y "let's serve some drinks."
                        $ suki_bar_blow = 5
                        $ bk3_love_bartending = 7
                        menu:
                            "easy":
                                $ bk3_bar_level = 1
                                $ bk3_bar_memory = 0
                                show text "{color=#ffffff}serve three drinks":
                                    xpos 0.5 ypos 0.2
                                with dissolve
                                $ renpy.pause(0.5)
                                hide text with dissolve
                            "normal":
                                $ bk3_bar_level = 2
                                $ bk3_bar_memory = 2
                                show text "{color=#ffffff}serve three drinks":
                                    xpos 0.5 ypos 0.2
                                with dissolve
                                $ renpy.pause(0.5)
                                hide text with dissolve
                            "hard":
                                $ bk3_bar_level = 3
                                $ bk3_bar_memory = 4
                                show text "{color=#ffffff}serve three drinks":
                                    xpos 0.5 ypos 0.2
                                with dissolve
                                $ renpy.pause(0.5)
                                hide text with dissolve
                        $ bk3_bar_wins = 0
                        hide expression "ebackgrounds/inside_tavern_night.jpg"
                        hide expression "bk3/suki/barblow/bar_0.png"
                        with fade
                        jump bk3_love_bartend
                    "not right now":

                        y "can't."
                        y "I'm... busy?"
                        show tosi tosi03 with dissolve
                        suki "shoot."
                        suki "well... let me know."
                        jump love_bk3_village_background
            if suki_bar_blow ==1:
                show expression "ebackgrounds/inside_tavern_night.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                with dissolve
                suki "so? will you help?"
            if suki_bar_blow ==0:
                show expression "ebackgrounds/inside_tavern_night.jpg"
                show expression "bk3/suki/barblow/bar_0.png"
                show tosi tosi01
                show tosi_smile
                with dissolve
                suki "aang!"
                suki "i'm glad you're here."
                hide tosi_smile with dissolve
                suki "can you watch the bar for me?"
                suki "I need to go take care of something."
                y "i mean... that sounds like work."
                y "which i'm not, you know, the biggest fan of."
                show tosi_blink with dissolve
                suki "damn."
                suki "......"
                hide tosi_blink with dissolve
                suki "well...."
                suki "is there something i could do to...."
                show tosi tosi04 with dissolve
                suki "....convince you?"
                y "i don't know...."
                suki "what if i took a little more off..."
                show tosi tosi05 with Dissolve(1)
                show ctc
                pause
                hide ctc
                suki "...am i convincing you?"
                $ suki_bar_blow = 1
            if suki_bar_blow ==1:
                menu:
                    "watch the bar":
                        y "alright, fine."
                        y "what do i get for-"
                        hide screen earth_money_date
                        play sound "audio/kiss.mp3"
                        show pink
                        show tobb_heart:
                            xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
                            xzoom 1 yzoom 1 alpha 1.0
                            linear 1.0 xzoom 4 yzoom 4 alpha 0.0
                        hide pink with Dissolve(1)
                        $ renpy.pause(1,hard=True)
                        hide tobb_heart
                        show screen earth_money_date
                        show tosi tosi01
                        show tosi_smile
                        with dissolve
                        suki "thanks!"
                        hide tosi
                        hide tosi_smile
                        with moveoutleft
                        y "...."
                        y "that was it?"
                        y "dang it."
                        y "now i gotta work..."
                        $ suki_bar_blow =2
                        $ bk3_love_bartending =1
                        menu:
                            "easy":
                                $ bk3_bar_level = 1
                                $ bk3_bar_memory = 0
                                show text "{color=#ffffff}serve three drinks":
                                    xpos 0.5 ypos 0.2
                                with dissolve
                                $ renpy.pause(0.5)
                                hide text with dissolve
                            "normal":
                                $ bk3_bar_level = 2
                                $ bk3_bar_memory = 2
                                show text "{color=#ffffff}serve three drinks":
                                    xpos 0.5 ypos 0.2
                                with dissolve
                                $ renpy.pause(0.5)
                                hide text with dissolve
                            "hard":
                                $ bk3_bar_level = 3
                                $ bk3_bar_memory = 4
                                show text "{color=#ffffff}serve three drinks":
                                    xpos 0.5 ypos 0.2
                                with dissolve
                                $ renpy.pause(0.5)
                                hide text with dissolve
                        hide expression "ebackgrounds/inside_tavern_night.jpg"
                        hide expression "bk3/suki/barblow/bar_0.png"
                        with fade
                        $ bk3_bar_wins = 0
                        jump bk3_love_bartend
                    "not right now":

                        y "another time, maybe."
                        show tosi tosi01
                        show tosi_blink
                        with dissolve
                        suki "boo."
                        jump love_bk3_village_background

    jump bk3_love_tavern_menu

label bk3_love_tavern_menu:
    $ renpy.can_rollback()
    menu:
        "mix drinks":
            menu:
                "easy":
                    $ bk3_bar_level = 1
                    $ bk3_bar_memory = 0
                    show text "{color=#ffffff}serve three drinks":
                        xpos 0.5 ypos 0.2
                    with dissolve
                    $ renpy.pause(0.5)
                    hide text with dissolve
                "normal":
                    $ bk3_bar_level = 2
                    $ bk3_bar_memory = 2
                    show text "{color=#ffffff}serve three drinks":
                        xpos 0.5 ypos 0.2
                    with dissolve
                    $ renpy.pause(0.5)
                    hide text with dissolve
                "hard":
                    $ bk3_bar_level = 3
                    $ bk3_bar_memory = 4
                    show text "{color=#ffffff}serve three drinks":
                        xpos 0.5 ypos 0.2
                    with dissolve
                    $ renpy.pause(0.5)
                    hide text with dissolve
                "back":
                    jump bk3_love_tavern_menu
            $ bk3_bar_wins = 0
            jump earth_tavern
        "talk to suki" if brothel_quest >=8:
            if love_ty_sex_quest ==2 or love_ty_sex_quest ==3:
                jump love_inside_tavern_shack
            if love_suki_sex:
                if suki_visited_today:
                    show tosi tosi01 with dissolve
                    suki "hey, aang."
                    suki "no income to give you at the moment."
                if not suki_visited_today:
                    show tosi tosi01 with dissolve
                    if suki_bar_blow ==7:
                        suki "whadda ya say?"
                        suki "let me keep today's tips for a blowjob?"
                        menu:
                            "tips":
                                y "i'd rather have the tips."
                                suki "oh..."
                            "blowjob":

                                y "the blowjob."
                                suki "awesome choice."
                                $ suki_visited_today = True
                                jump suki_barblow

                    suki "hey, here's your share for today."
                    $ randcoin = renpy.random.randint(8, 25)
                    play sound "audio/money.mp3"
                    $ emoney += randcoin
                    "you got [randcoin] coins!"
                    $ suki_visited_today = True

                if love_ty_sex_quest ==1:
                    suki "ty lee mentioned you'd help me upgrade the tavern!"
                    suki "i'd appreciate it!"

                menu:
                    "rub her pussy":
                        jump love_suki_mast
                    "backroom cowgirl":
                        jump suki_lovefuck
                    "back":
                        jump love_inside_tavern_shack

            if suki_tylee ==6:
                y "suki's still in the hospital."
                jump love_bk3_village_background
            if suki_tylee ==3:
                if suki_ty_palace == 1:
                    y "she's not here."
                    y "she must be waiting at the palace."
                    y "I need to get ty lee to agree to help, and then meet them in the city."
                    jump love_inside_tavern_shack
                if suki_ty_palace ==3:
                    y "she's not here."
                    y "she must be waiting at the palace."
                    y "I need to meet her and ty lee there."
                    jump love_inside_tavern_shack

                if suki_ty_palace ==2:
                    $ suki_ty_palace = 3
                else:
                    $ suki_ty_palace = 1
                show tosi tosi03 with dissolve
                suki "what do you want?"
                y "i need your help."
                show tosi_blink with dissolve
                suki "....that's rich."
                suki "you bring one of my enemies into our village, and then ask a favor."
                hide tosi_blink with dissolve
                suki "go fuck yourself."
                y "suki..."
                suki "no! i told you i don't-"
                y "there's someone in trouble, suki."
                y "i can't rescue her alone."
                y "i need you."
                y "you're one of the best warriors i've ever met."
                suki "....."
                show tosi tosi01 with dissolve
                suki "...someone's in trouble?"
                y "yeah."
                y "i don't know where she is, but i know someone who does."
                suki "who?"
                y "remember that earth guard that came in here and tried to undress you?"
                suki "sort of..."
                y "well, he's captured a chick named joo dee, and is threatening to hurt her if i don't stop rescuing girls."
                suki "that asshole."
                y "yeah, but we're gonna kick his ass."
                suki "how?"
                y "so you're in?"
                suki "of course."
                y "great, because you're not gonna like this next bit."
                suki "what?"
                y "...we need ty lee, too."
                show tosi tosi03 with dissolve
                suki "ohhh fuck no."
                y "we {i}need{/i} her, suki."
                y "there's too many dai lee to handle just between us."
                y "and she's been working with them, so that might give us an advantage."
                suki "i can't, aang... that's too much to ask of-"
                y "just put it aside for right now, suki."
                y "you can go back to biting each other's heads off later if you need to."
                y "but right now we need to work together to rescue joo dee."
                suki "....."
                show tosi tosi01
                show tosi_blink
                with dissolve
                suki "...fine."
                hide tosi_blink with dissolve
                suki "...but only until we save this chick."
                suki "then all bets are off."
                y "I'll take it."
                suki "how do we start?"

                if suki_ty_palace ==3:
                    y "ty lee is already on board."
                    y "we'll meet you at the palace in the city."
                    suki "right."
                    hide tosi with dissolve
                else:

                    y "i'll meet you at the palace in the city."
                    y "i still need to get ty lee to agree."
                    suki "i still don't think we need her, but fine."
                    suki "i'll meet you at the palace."
                    hide tosi with dissolve

                jump love_bk3_village_background

            if suki_tylee ==2:
                show tosi tosi03 with dissolve
                suki "i don't want to talk to you."
                hide tosi with dissolve
                y "*sigh...*"
                y "guess i'll have to try another time."
                jump love_inside_tavern_shack

            if tavern_shack ==2 and not suki_lantern_explain:
                $ suki_lantern_explain = True
                jump suki_lantern

            if shadygone and not suki_joodee:
                show tosi tosi01 with dissolve
                if not irohshadytalk:
                    suki "hey, sorry aang, i'm super busy at the moment!"
                    y "i need to ask you a question about suspicious activity last night."
                    suki "can't right now!"
                    suki "june might have been up, though! ask her!"
                    hide tosi with dissolve
                    y "guess i'll ask june about it."
                    jump love_inside_tavern_shack
                else:
                    $ suki_joodee = True
                    y "suki, have you got a minute?"
                    y "i've got a quick question."
                    suki "yeah, i'm free right now."
                    suki "what's up?"
                    y "you didn't see anyone suspicious last night, did you?"
                    suki "i don't think so."
                    y "damn..."
                    suki "i did see your house this morning, though."
                    suki "i'm sorry about that."
                    y "you really didn't see anyone near my house last night?"
                    suki "no, i-"
                    suki "wait. i did."
                    ya "tell me!"
                    suki "um... well, i took out some trash, and there was a woman near your house in a hurry."
                    y "....that doesn't really narrow it down."
                    y "(but it absolves shady, i guess.)"
                    y "what did she look like?"
                    suki "busty."
                    suki "like... super busty."
                    suki "i think she was wearing some earth kingdom clothes."
                    suki "and maybe had something in her hair?"
                    suki "she had really dark hair."
                    y "......"
                    suki "and full, stacked tits."
                    y "......"
                    suki "did i mention her massive tits?"
                    y "i think you might have, yeah."
                    suki "do you know anyone that matches that description?"
                    ya "yes, i do."
                    ya "thanks for the help."
                    suki "no problem."
                    $ suki_joodee = True
                    jump love_inside_tavern_shack

            if not love_suki_talk:
                show tosi tosi01 with dissolve
                suki "hello!"
                y "are you settling in?"
                suki "i am, thank you."
                show tosi tosi03 with dissolve
                suki "that other girl left a mess in the room..."
                show tosi tosi01 with dissolve
                suki "but i'm working around it."
                y "great."
                y "think you can start bartending?"
                suki "sure, no problem."
                y "do you know what you're doing?"
                suki "serving the pretty girls first?"
                y "....that's exactly right."
                suki "what are we doing about... payment?"
                suki "with tips, and the room, and all that?"
                y "how about for now, put aside half for me."
                suki "i can do that."
                y "great!"
                y "have fun."
                $ love_suki_talk = True
                $ suki_visited_today = True
                jump love_inside_tavern_shack
            else:
                if suki_visited_today:
                    show tosi tosi01 with dissolve
                    suki "hey, aang."
                    suki "no income to give you at the moment."
                if not suki_visited_today:
                    show tosi tosi01 with dissolve
                    suki "hey, here's your share for today."
                    $ randcoin = renpy.random.randint(8, 25)
                    play sound "audio/money.mp3"
                    $ emoney += randcoin
                    "you got [randcoin] coins!"
                    $ suki_visited_today = True

                if suki_mast:
                    suki "want to help me... find a key?"
                    suki "*wink wink nudge nudge*"
                    menu:
                        "get her off":
                            jump love_suki_mast
                        "some other time":

                            y "maybe later."
                            suki "oh... okay."
                            jump love_bk3_village_background

                if love_suki_hypno ==13 and not suki_mast:
                    jump love_suki_mast

                if suki_plan and not market_raid:
                    if bk3_day:
                        suki "meet me here tonight."
                        y "got it."
                        y "i'll see you this evening."
                        $ suki_plan = True
                        jump love_inside_tavern_shack
                    else:
                        suki "are you ready to go on a raid?"
                        menu:
                            "let's go":
                                y "i'm with you."
                                suki "good, come on."
                                jump suki_night_raid
                            "i'll be right back":

                                y "i've got some stuff to do first."
                                suki "okay."
                                suki "i'll meet you here when you're ready."
                                jump love_inside_tavern_shack

                if love_suki_hypno >= 4 and love_suki_hypno <=12:
                    menu:
                        "plan" if love_suki_hypno ==10:
                            if suki_plan and not market_raid:
                                if bk3_day:
                                    suki "meet me here tonight."
                                    y "got it."
                                    y "i'll see you this evening."
                                    $ suki_plan = True
                                    jump love_inside_tavern_shack
                                else:
                                    suki "are you ready to go on a raid?"
                                    menu:
                                        "let's go":
                                            y "i'm with you."
                                            suki "good, come on."
                                            jump suki_night_raid
                                        "i'll be right back":

                                            y "i've got some stuff to do first."
                                            suki "okay."
                                            suki "i'll meet you here when you're ready."
                                            jump love_inside_tavern_shack
                            if suki_raid_talk:
                                y "you mentioned raiding the city?"
                                suki "i did."
                                suki "those bitches need to go down."
                                suki "are you in?"
                                menu:
                                    "i'm in":
                                        y "I'm in."
                                        suki "yes!"
                                        suki "we'll take it to them, all right."
                                        if bk3_day:
                                            suki "meet me here tonight."
                                            y "got it."
                                            y "i'll see you this evening."
                                            $ suki_plan = True
                                            jump love_inside_tavern_shack
                                        else:
                                            suki "are you ready now?"
                                            menu:
                                                "let's go":
                                                    y "i'm with you."
                                                    suki "good, come on."
                                                    jump suki_night_raid
                                                "i'll be right back":

                                                    y "i've got some stuff to do first."
                                                    suki "okay."
                                                    suki "i'll meet you here when you're ready."
                                                    jump love_inside_tavern_shack
                                    "some other time":

                                        y "not right now."
                                        show tosi_blink
                                        with dissolve
                                        suki "Oh..."
                                        suki "alright, let me know when you're ready to join me."
                                        $ suki_raid_talk = True
                                        jump love_inside_tavern_shack

                            y "so you said you had something to discuss with me?"
                            show tosi tosi03 with dissolve
                            suki "not here!"
                            suki "come on."
                            scene black with dissolve
                            scene inside_tavern_1
                            show tosi tosi01
                            with dissolve
                            y "i like what you've done with the place."
                            y "barren walls and some boxes."
                            y "homey."
                            suki "i'm not a decorator, aang."
                            suki "i'm a warrior."
                            suki "and that's why i want to talk to you."
                            suki "I need your help."
                            y "oh, uh..."
                            y "...i think you're really under-utilizing blue-"
                            show tosi_blink with dissolve
                            suki "not with fashion!"
                            hide tosi_blink with dissolve
                            suki "i'm going on a raid in the city tonight."
                            y "you're... what?"
                            suki "i've been going into the city and wreaking havoc on dai lee outposts."
                            y "why?"
                            show tosi_blink with dissolve
                            suki "remember how i got caught?"
                            suki "by three bitches?"
                            y "sure..."
                            hide tosi_blink with dissolve
                            suki "well, i'm gonna get them back for that."
                            suki "there are three fire nation sluts in the city walking around in kyoshi outfits..."
                            show tosi tosi03
                            suki "and i'm not going to let that slide!"
                            suki "so i'm baiting them, trying to get them to stick their slutty necks out..."
                            suki "which is when i'll kick their asses."
                            y "how does someone have a slutty neck?"
                            show tosi tosi01
                            suki "....you're missing the point."
                            y "this is a lot."
                            y "i mean, you brought me back here to discuss home decor and-"
                            show tosi tosi03
                            suki "no, i didn't!"
                            y "well, then you were very misleading."
                            show tosi tosi01
                            suki "look, i'm going into the city tonight... do you want to help?"
                            menu:
                                "i'm in":
                                    y "I'm in."
                                    suki "yes!"
                                    suki "we'll take it to them, all right."
                                    if bk3_day:
                                        suki "meet me here tonight."
                                        y "got it."
                                        y "i'll see you this evening."
                                        $ suki_plan = True
                                        jump love_inside_tavern_shack
                                    else:
                                        suki "are you ready now?"
                                        menu:
                                            "let's go":
                                                y "i'm with you."
                                                suki "good, come on."
                                                jump suki_night_raid
                                            "i'll be right back":

                                                y "i've got some stuff to do first."
                                                suki "okay."
                                                suki "i'll meet you here when you're ready."
                                                jump love_inside_tavern_shack
                                "some other time":

                                    y "not right now."
                                    show tosi_blink
                                    with dissolve
                                    suki "Oh..."
                                    suki "alright, let me know when you're ready to join me."
                                    $ suki_raid_talk = True
                                    jump love_inside_tavern_shack
                        "anti-hypnosis session":

                            if suki_hypno_today:
                                y "(i should give her a day to recover.)"
                                jump love_inside_tavern_shack
                            else:
                                if love_suki_hypno ==4:
                                    $ love_suki_hypno = 5
                                    y "up for another anti-hypnosis session?"
                                    suki "i really, really am."
                                    suki "I'll meet you there."
                                    jump love_inside_tavern_shack
                                if love_suki_hypno ==5:
                                    suki "I'll meet you at your place for an anti-hypnosis session."
                                    jump love_inside_tavern_shack
                                if love_suki_hypno ==6:
                                    $ love_suki_hypno = 7
                                    y "ready to try again?"
                                    suki "sure."
                                    suki "but... i don't know what you can do differently."
                                    y "do you have any ideas?"
                                    y "on how to remove some of your defensiveness when you're under?"
                                    suki "No."
                                    suki "i'm not even really conscious during it."
                                    y "that's fair."
                                    y "let me grab a drink and we'll keep talking about it."
                                    suki "alright."
                                    show black with dissolve
                                    "you walk to the counter and pour yourself a drink."
                                    "as you return to suki, you see she's chatting with someone..."
                                    hide black
                                    show toeg toeg01:
                                        xzoom -1
                                    show tosi_hypno_eyes
                                    with dissolve
                                    dl "do as you're told!"
                                    suki "n... no..."
                                    y "don't feel bad."
                                    y "she's like that with me, too."
                                    hide toeg
                                    show guardb_body_1:
                                        xzoom -1
                                    with dissolve
                                    dl "you!"
                                    dl "what did you do to her?"
                                    y "who me?"
                                    y "oh, wait, that's right."
                                    y "i put some limits on her willingness to follow sexual orders..."
                                    y "...you pervert."
                                    dl "oh, shut up!"
                                    dl "you've ruined her!"
                                    y "hey, while i've got you here..."
                                    y "any tips on how to get her mental defenses down?"
                                    dl "what? no!"
                                    y "it's so i can fully undo all your hypnosis shit."
                                    dl "you're really trying to white-knight this bitch?"
                                    dl "heh."
                                    dl "that's cute."
                                    dl "but if that's how you're gonna go about it, you'll never get her vulnerable enough."
                                    dl "you goody goody nerd."
                                    y "i'm sick of your attitude."
                                    y "and your breath."
                                    y "get out of here."
                                    dl "i will."
                                    dl "good luck... sir avatar."
                                    dl "heh."
                                    hide guardb_body_1 with dissolve
                                    y "suki?"
                                    y "...."
                                    y "damn it, now i have to deal with this again."
                                    y "*sigh...*"
                                    y "i'll go get katara."
                                    jump love_bk3_village_background
                                if love_suki_hypno ==9:
                                    suki "I'll meet you at your place for an anti-hypnosis session."
                                    jump love_inside_tavern_shack
                                if love_suki_hypno ==10:
                                    suki "maybe later."
                                    jump love_inside_tavern_shack
                                if love_suki_hypno ==11:
                                    y "ready for another session?"
                                    suki "sure, i'll meet you there."
                                    $ love_suki_hypno = 12
                                    jump love_inside_tavern_shack
                                if love_suki_hypno ==12:
                                    suki "I'll meet you at your place for an anti-hypnosis session."
                                    jump love_inside_tavern_shack
                                else:
                                    menu:
                                        "exit":
                                            jump love_inside_tavern_shack
                        "exit":
                            jump love_inside_tavern_shack
                else:

                    jump love_inside_tavern_shack

        "talk to bartender" if brothel_quest <=7:
            "you don't have a bartender!"
            jump love_inside_tavern_shack
        "talk to june" if june_freed and brothel_quest <=6:
            if brothel_building ==1:
                y "hey june?"
                y "ya here?"
                show toju toju01 with dissolve
                ju "what's up?"
                y "you know how you wanted to be a prostitute?"
                show toju toju03 with dissolve
                ju "i'll give you three seconds to rephrase that."
                y "....you know how you wanted to live with prostitutes?"
                ju ".........."
                y "well, congrats! we have a brothel!"
                show toju toju02 with dissolve
                ju "nice!"
                ju "i'll grab my bags and head over there."
                y "one more thing...."
                show toju toju01 with dissolve
                ju "what?"
                y "hmm... i'll tell you when we get there."
                ju "okay..."
                $ brothel_quest = 7
                jump love_bk3_village_background
            else:

                show toju toju01 with dissolve
                ju "what do you want?"
                y "....well, that's rather rude."
                ju "then don't bother me."
                y "...."
                y "i can see someone's been eating sour grapes."
                show toju toju03 with dissolve
                ju "i will shit in your mouth."
                y "yeah, well, i've jizzed in yours."
                ju "i guess you don't want testicles, huh?"
                y "....."
                y "i should go."
                ju "you should go."
                hide toju with dissolve
                jump love_inside_tavern_shack

        "host a quest" if tavern_shack <2:
            "your tavern isn't big enough for this yet!"
            jump love_inside_tavern_shack

        "host a quest (new!)" if tavern_shack >=2 and not tavern_3:
            $ tavern_3 = True
            show blackveil with dissolve
            "people in need sometimes post quests on the local notice board, located in your tavern."
            "adventurers come from all over to take on these quests, often fighting over the few available ones."
            "as the tavern owner, you have the final say over who gets which quests, and you receive some of the reward."
            "There is sometimes an adventurer better suited for the quest, but there are no wrong options... follow your gut!"
            "these quests happen in real time, so the quest timer will continue even if the game isn't running."
            "good luck - adventure awaits!"
            hide blackveil with dissolve
            jump tavern_quest_menu

        "host a quest" if tavern_shack >=2 and tavern_3:
            if current_quest <15:
                jump tavern_quest_menu
            if current_quest ==15:
                "you've completed all the quests!"
        "exit":

            stop music 
            play music "audio/Bumba Crossing.mp3"
            jump love_bk3_village_background



label love_hypnosis_room:
    if not suki_lantern_explain:
        hide screen earth_money_date  
        scene black
        scene hypno_room2
        with dissolve
        y "i should probably use this room for something."
        y "i'll think of something eventually."
    else:
        hide screen earth_money_date  
        scene black
        scene hypno_room2
        with dissolve
        if jin_anti_hypno_start ==1:
            $ jin_anti_hypno_start = 2
            jump jin_anti_hypno1
        if jd_break_hypno ==4:
            $ love_jd_hypno = 15
            y "Hmmm, I don't know why, but ....."
            y "...I just felt like visiting the maze again just now."
            y " Well, I guess I can do that after I finish this."
            jump jd_anti_hypno1
        if jd_break_hypno ==3:
            y "i should let joo dee know i've set up the equipment."
            jump love_inside_avatar_shack
        if jd_break_hypno ==2:
            y "okay, i need to make these changes that ajala suggested."
            show black with dissolve
            "you work on the hypnosis equipment, putting in the changes necessary to make it truly capable of breaking hypnosis."
            hide black with dissolve
            y "alright, i think that should do it."
            y "i'll let joo dee know."
            $ jd_break_hypno = 3
            jump love_inside_avatar_shack
        if love_jd_hypno ==1 or love_jd_hypno ==3 or love_jd_hypno ==5:
            jump jd_anti_hypno1
        if love_june_hypno ==6 or love_june_hypno ==8 or love_june_hypno ==10:
            jump june_anti_hypno1
        if love_suki_hypno == 3 or love_suki_hypno ==5 or love_suki_hypno ==9 or love_suki_hypno ==12:
            jump suki_anti_hypno1
        else:
            y "okay, i need to get the girls that have been brainwashed in here."
            y "i'll have to find and talk to each of them about it."

    jump love_bk3_village_background


label love_inside_brothel_building:
    hide screen earth_money_date
    stop music
    play music "audio/Smooth Lovin.mp3"
    scene black
    scene inside_brothel_1
    with dissolve

    if love_jd_hypno >=15 and jin_love_bj and june_light >=5:
        if jin_anti_hypno_start ==1:
            y "i should meet jin at the anti-hypnosis room in my house."
            jump love_bk3_village_background
        if jin_anti_hypno_start ==0:
            show toju toju09
            show toju_blink
            show tojn tojn24:
                xzoom -1
            with dissolve
            ju "i told you \"no\", and that's final."
            jin "you're not my real mom!"
            hide toju_blink with dissolve
            ju "I'm not... any kind of mom..."
            ju "then why are you telling me what to do?"
            ju "because he put {i}me{/i} in charge, so i'm telling you what to do."
            ju "and you need to stay in your room if you can't behave."
            ju "...shit, i do sound like a mom."
            show toju toju12 with dissolve
            ju "weiners and gonads!"
            show toju toju09
            show toju_blink
            with dissolve
            ju "there, now i feel like a kid."
            ju "i'm all over the place."
            jin "...."
            y "okay..."
            y "first, your names are way too similar."
            y "second... what's happening?"
            hide toju_blink
            show toju toju12
            with dissolve
            ju "finally!"
            ju "so glad you're here."
            jin "{i}mom{/i} here keeps trying to keep me in my room... like i'm a prisoner!"
            show toju toju11 with dissolve
            ju "i'm not your damn mom!"
            ju "i'm just following {i}his{/i} instructions!"
            y "which i'm sure you're doing well."
            jin "she-"
            y "i heard your side."
            y "june?"
            show toju toju12 with dissolve
            ju "this... kid... keeps trying to have sex with everyone."
            y "you mean... the girls?"
            y "because that's fine."
            ju "no... strange men."
            y "....seriously?"
            ju "yeah, i have to keep stopping her."
            ju "i think she's fucked in the head from hypnosis and i don't want her to get in trouble."
            ju "I also assume you don't want her fucking randoms."
            y "yeah... i don't want that."
            jin "i'm not going to fuck anyone!"
            jin "i just want to get out for a bit!"
            ju "you're acting like a really messed up addict."
            jin "I'll be fine!"
            show tojn tojn20 with dissolve
            jin "really, i'll be fine."
            jin "aang... you trust me right?"
            y "you know i told you not to bang anyone right?"
            jin "and i haven't."
            jin "and i won't."
            jin "I just... need to go stretch my legs... meet some people... hang out with them..."
            y "yeah, i don't like where this is going."
            y "i realize that we haven't done any anti-hypnosis work... i honestly just hoped you were fine."
            y "but this is clearly a developing compulsion, and around here there's only one reason for that."
            y "so, look, i figured out how to permanently break hypnosis."
            show toju toju09 with dissolve
            ju "you... have?"
            y "i'll get to you later, june."
            ju "...."
            y "anyway, jin, i bet once we break that, you'll be less... uh..."
            ju "...horny?"
            y "i was gonna say \"fucked up\", but sure."
            y "actually, i hope everybody here stays horny, they just distribute their vaginas properly."
            ju "...what?"
            y "I mean have sex with me."
            y "i'm not good with words."
            y "okay, jin, come to my house later."
            y "we'll get this shit busted."
            jin "....okay."
            $ jin_anti_hypno_start = 1
            jump love_bk3_village_background

    if brothel_building ==3 and not tylee_board:
        $ tylee_board = True
        show tf:
            xpos -600
        show toju toju10
        with dissolve
        ju "and who are you?"
        ty "i'm ty lee!"
        ju "...so?"
        y "i see you two have met."
        ju "avatar, who is this... person?"
        ty "i told you! i'm ty lee!"
        ju "that's a fun noise."
        show tfa:
            xpos -600
        hide tf
        with dissolve
        ty "it's not a noise! it's my name!"
        ju "oh..."
        ju "well, we can't all have good names."
        ty "hey!"
        y "calm down, you two."
        show toju toju11 with dissolve
        ju "are you seriously making this into a boarding house, avatar?"
        y "yeah, and you're going to like it."
        y "you want to remain incognito anyway... right, june?"
        y "this will be more peaceful than a brothel."
        show toju toju10 with dissolve
        ju "I suppose..."
        show tf:
            xpos -600
        hide tfa
        with dissolve
        ty "june?"
        ty "where do i know that name?"
        ju "wait... are you from the fire nation?"
        ty "yes...."
        show toju toju11 with dissolve
        ju "avatar..."
        y "ty lee, you've never heard that name before, understand?"
        ty "....okay!"
        ju "i'm not sure-"
        y "june, ty lee is cool."
        y "aren't you, ty lee?"
        ty "do you really think i'm cool?"
        ty "i'd love to be cool!"
        y "see?"
        y "she's a bit of a dork, but she's a cool one."
        ty "yay!"
        y "she's staying here."
        y "get used to it."
        ju "....fine."
        ty "more yay!"
        y "help her to her room, june."
        show toju toju10
        show toju_blink
        with dissolve
        ju "*sigh...*"
        ju "very well..."
        hide toju_blink with dissolve
        ju "i'll show you to your room."
        ty "thanks!"
        hide toju
        hide tf
        with dissolve
        y "...i hope this works out."
        y "i can't see anything really going wrong, though."
        jump love_bk3_village_background

    if ty_hospital and not june_home_talk:
        $ june_home_talk = True
        show toju toju10 with dissolve
        y "june, do you know where i could put another person?"
        show toju toju09 with dissolve
        ju "....really?"
        ju "{i}another{/i} stray?"
        ju "honestly, i'm surprised you haven't just put her in here."
        ju "it's practically a home for wayward girls."
        y ".........."
        show toju toju12 with dissolve
        ju "seriously, get some sluts in here, man."
        y "that...."
        y "....is a great idea!"
        show toju_blink with dissolve
        ju "i know."
        y "we don't need a brothel, and it obviously doesn't work the way i was hoping..."
        show toju toju10
        hide toju_blink
        with dissolve
        ju "wait-"
        y "let's just make this place lodging for girls."
        ju "that's not-"
        y "thanks june!"
        show toju toju08 with dissolve
        ju "you-"
        jump love_bk3_village_background

    if love_june_hypno ==5:
        if june_dl_tits:
            show toju toju16
            show toju_hypno_eyes
            with dissolve
        else:
            show toju toju13
            show toju_hypno_eyes
            with dissolve
        show toki toki02:
            xzoom -1
        with dissolve
        k3 "it really did happen again."
        k3 "why is this happening? what's going on?"
        y "earth soldiers - the dai lee - are going around perving out on the girls rescued from the tunnels."
        y "if anyone's gonna perv on them, it's gonna be me!"
        k3 "...."
        y "....."
        y "i mean..."
        k3 "no, no... i approve."
        k3 "now shush while i handle this."
        y "don't shush me, kata-"
        k3 "shush."
        y "....."
        show black with dissolve
        "katara bends water over june's ears."
        "after a minute or so, june snaps out of it."
        hide black with dissolve
        k3 "there."
        hide toju_hypno_eyes with dissolve
        ju "i'm not showing you my...."
        ju "......"
        show toju toju11 with vshake
        ju "what the fuck?!"
        ju "who has the balls?!"
        ju "avatar! i'm gonna... i'm..."
        show toju_blink with dissolve
        ju "I'm so... foggy... what..."
        k3 "relax, june, it's okay."
        hide toju_blink with dissolve
        ju "who are you?"
        k3 "i'm katara. i'm usually at the hospital."
        ju "....right."
        ju "now tell me..."
        ju "what. the. fuck."
        y "you were put into a hypnotic trance."
        show toju toju08 with dissolve
        ju "what?"
        y "you were brainwashed."
        y "no doubt during your stay in the tunnels."
        y "and an earth kingdom soldier took advantage of that."
        ju "how... what..."
        show toju toju11 with dissolve
        ju "what am i supposed to do about that?"
        k3 "aang has equipment for that."
        k3 "he can help."
        k3 "take a breath, june."
        show toju toju10
        show toju_blink
        with dissolve
        "june breathes in deeply."
        show toju toju12 with dissolve
        "she breathes out slowly."
        show toju toju09
        hide toju_blink
        with dissolve
        ju "very well."
        ju "i'll take you up your offer, avatar."
        k3 "well, i'll get back to the hospital for now."
        k3 "good luck!"
        hide toki with dissolve
        ju "huh. she seems efficient."
        y "have you two really not spent any time together?"
        ju "why would we?"
        y "i just... haven't really thought about it."
        y "anyway, i'll meet you at my house later."
        y "come by when you're ready."
        $ love_june_hypno = 6
        $ bk3_day = False
        jump love_bk3_village_background

    if love_june_hypno ==4:
        if june_dl_tits:
            show toju toju16
            show toju_hypno_eyes
            with dissolve
        else:
            show toju toju13
            show toju_hypno_eyes
            with dissolve
        y "i should... go get katara."
        jump love_bk3_village_background

    if june_available and love_june_hypno ==3:
        $ love_june_hypno = 4
        show toju toju09
        show toju_blink
        show toeg toeg01:
            xzoom -1
        with dissolve
        ju "you should really leave now."
        ju "my patience is... worn."
        dl "just show me your tits!"
        dl "it's not a big deal."
        dl "and you'll have the... appreciation... of the dai lee."
        dl "which is a valuable currency."
        show toju toju11
        hide toju_blink
        with dissolve
        ju "that's it!"
        ju "i hope you like nuts, because i'm going to kick yours up into your throat!"
        dl "{i}the earth king has invited you to lake laogai."
        show toju toju10
        show toju_hypno_eyes
        with dissolve
        ju "......"
        ju "I am honored to accept his invitation."
        dl "yes..."
        dl "now..."
        dl "grab those melons of yours."
        show toju toju13 with dissolve
        dl "and pull that top down..."
        menu:
            "intervene":
                pass
            "wait":

                $ june_dl_tits = True
                show toju toju16 with Dissolve(1)
                show ctc
                pause
                hide ctc
                dl "hahaha!"
                dl "that's great!"
                dl "look at you now, miss \"high and mighty\"!"
                dl "popping out those tits for my pleasure!"
                dl "now, slut, you're gonna grab them and-"

        y "alright, that's enough!"
        hide toeg with dissolve
        show guardb_body_1:
            xzoom -1
        with dissolve
        if love_suki_hypno ==0:
            dl "what? who are you?"
            y "I'm the avatar, bitch."

        if love_suki_hypno >=1:
            dl "what? who-"
            dl "oh, fuck."
            dl "not you again."
            y "yeah, me again."
            dl "well... can you leave?"
            dl "this is a private earth kingdom matter."
            y "nope, I'm the avatar, bitch."

        y "I'll break ya in half!"
        dl "....that's the juggarnaut."
        y "wait, you guys get x-men comics here?"
        dl "is there something you want?"
        y "yeah, for you to get out."
        dl "well, tough titties."
        y "heh. titties."
        dl "totally."
        dl "wait, no, just go away."
        y "not happening."
        if love_suki_hypno ==0:
            dl "guess i'll have to-"
            dl "wait, did you say you're the avatar?"
            y "yes, and you're alone here."
            dl "....that doesn't bode well for me."
            y "no, it doesn't."
            dl "......"
        else:
            dl "....."
            dl "aw, crap."

        dl "fine, i'll leave."
        dl "enjoy."
        dl "....you dick."
        y "that's-"
        hide guardb_body_1 with dissolve
        y "...."
        y "what a rude person."
        y "right, june?"
        y "....june?"
        y "......"
        if love_suki_hypno >=1:
            y "{size=+3}god damn it!"
            y "not this shit again!"
            y "....."

        y "i wonder...."
        y "will you make me a sandwich?"
        ju "............"
        ju "....................."
        y "I'll... take that as a no."
        y "......"
        y "I'll go get katara."
        jump love_bk3_village_background

    if love_june_hypno >=3:
        jump love_brothel_menu2

        label love_brothel_menu2:
            hide toju with dissolve
            menu:
                "talk to ty lee" if tylee_board:
                    if suki_tylee >=7:
                        if not ty_foot_offer:
                            $ ty_foot_offer = True
                            show tf with dissolve
                            ty "hi, aang!"
                            y "feeling better?"
                            ty "much!"
                            ty "and suki is so cool!"
                            ty "we're really getting along."
                            y "thats great."
                            show tfa
                            hide tf
                            with dissolve
                            ty "hey..."
                            y "yeah?"
                            ty "i want you to know i really appreciate you defending me here."
                            ty "and giving me a place to stay for free..."
                            show tf
                            hide tfa
                            with dissolve
                            ty "...i want to thank you."
                            ty "you know what we did in the tunnels?"
                            ty "with... my feet?"
                            ty "do you want to do that again?"
                            menu:
                                "yes":
                                    ty "great!"
                                    ty "come to my room!"
                                    jump love_ty_footjob
                                "no":

                                    y "not now."
                                    ty "oh... okay."
                                    jump love_bk3_village_background

                        if cabbage_tylee:
                            show tf with dissolve
                            ty "hi, aang!"
                            jump tylee_cabbage_menu

                            label tylee_cabbage_menu:
                                menu:
                                    "give cabbage" if cabbage_tylee:
                                        if bk3_cabbages >=1:
                                            y "here, take a cabbage."
                                            $ bk3_cabbages -=1
                                            $ ty_cabbages +=1
                                            ty "thanks!"
                                            jump tylee_cabbage_menu
                                        else:
                                            y "(i need a cabbage first...)"
                                            jump tylee_cabbage_menu

                                    "talk" if love_ty_sex_quest <5:
                                        if love_ty_sex_quest ==3:
                                            y "hey, so... suki's missing."
                                            show tfa
                                            hide tf
                                            with dissolve
                                            ty "she is?"
                                            y "yup."
                                            y "any idea where she could have gone?"
                                            ty "oh! um..."
                                            show tf
                                            hide tfa
                                            with dissolve
                                            ty "yes!"
                                            y "...and?"
                                            ty "suki was asking me about azula... if i had any insights into her schedule."
                                            ty "i told her that azula goes into the forest nearby alone sometimes."
                                            y "...was this before she had you locked in the tunnels?"
                                            ty "yup!"
                                            y "...and she knew you had this information?"
                                            ty "mm-hmm!"
                                            y "...shit."
                                            ty "what?"
                                            y "this sounds like a trap."
                                            y "azula must know you're compromised by now."
                                            y "she probably set a trap in case anyone followed."
                                            show tfa
                                            hide tf
                                            with dissolve
                                            ty "oh, no!"
                                            ty "we have to go check!"
                                            y "yeah, that's... that's what i'm saying."
                                            ty "come on, let's go! there's no time to lose!"
                                            hide tfa with dissolve
                                            y "i... yeah."
                                            y "right behind you."
                                            scene black with dissolve
                                            $ love_ty_sex_quest = 4
                                            jump ty_rescue_suki

                                        if love_ty_sex_quest ==2:
                                            y "hey, so i upgraded the tavern for suki."
                                            ty "great!"
                                            ty "can you let her know?"
                                            y "...sure."
                                            jump tylee_cabbage_menu

                                        if love_ty_sex_quest == 1:
                                            y "wanna get freaky?"
                                            ty "maybe!"
                                            ty "but... do you think you can you help suki expand the tavern?"
                                            ty "i know she needs the help..."
                                            y "alright."
                                            jump tylee_cabbage_menu

                                        if love_ty_sex_quest ==0:
                                            y "hey... wanna bang?"
                                            ty "*heehee!*"
                                            ty "you're funny!"
                                            y "stop saying that..."
                                            ty "i'm still worried about the cabbage vendor."
                                            ty "but i am interested in a little one on one time with you..."
                                            ty "please help him some more!"
                                            ty "if you give me three cabbages, we'll talk!"
                                            ty "'kay?"
                                            if ty_cabbages >=3:
                                                ty "...oh, you already have!"
                                                ty "that's amazing!"
                                                ty "thank you so much!"
                                                y "sure, i guess."
                                                y "lot of damn cabbages..."
                                                ty "but... do you think you can help suki expand the tavern?"
                                                y "...are you serious?"
                                                ty "of course!"
                                                y "....fine."
                                                $ love_ty_sex_quest = 1
                                                jump tylee_cabbage_menu
                                            if ty_cabbages <3:
                                                y "fine..."
                                                jump tylee_cabbage_menu

                                    "dildo fuck" if love_ty_sex_quest >=5 and b3love_dildo_gotit:
                                        jump tylee_lovedildo

                                    "sex" if cabbage_tylee:
                                        if love_ty_sex_quest >=5:
                                            jump tylee_lovefuck
                                        if love_ty_sex_quest ==3:
                                            y "hey, so... suki's missing."
                                            show tfa
                                            hide tf
                                            with dissolve
                                            ty "she is?"
                                            y "yup."
                                            y "any idea where she could have gone?"
                                            ty "oh! um..."
                                            show tf
                                            hide tfa
                                            with dissolve
                                            ty "yes!"
                                            y "...and?"
                                            ty "suki was asking me about azula... if i had any insights into her schedule."
                                            ty "i told her that azula goes into the forest nearby alone sometimes."
                                            y "...was this before she had you locked in the tunnels?"
                                            ty "yup!"
                                            y "...and she knew you had this information?"
                                            ty "mm-hmm!"
                                            y "...shit."
                                            ty "what?"
                                            y "this sounds like a trap."
                                            y "azula must know you're compromised by now."
                                            y "she probably set a trap in case anyone followed."
                                            show tfa
                                            hide tf
                                            with dissolve
                                            ty "oh, no!"
                                            ty "we have to go check!"
                                            y "yeah, that's... that's what i'm saying."
                                            ty "come on, let's go! there's no time to lose!"
                                            hide tfa with dissolve
                                            y "i... yeah."
                                            y "right behind you."
                                            scene black with dissolve
                                            $ love_ty_sex_quest = 4
                                            jump ty_rescue_suki

                                        if love_ty_sex_quest ==2:
                                            y "hey, so i upgraded the tavern for suki."
                                            ty "great!"
                                            ty "can you let her know?"
                                            y "...sure."
                                            jump tylee_cabbage_menu

                                        if love_ty_sex_quest == 1:
                                            y "wanna get freaky?"
                                            ty "maybe!"
                                            ty "but... do you think you can you help suki expand the tavern?"
                                            ty "i know she needs the help..."
                                            y "alright."
                                            jump tylee_cabbage_menu

                                        if love_ty_sex_quest ==0:
                                            y "hey... wanna bang?"
                                            ty "*heehee!*"
                                            ty "you're funny!"
                                            y "stop saying that..."
                                            ty "i'm still worried about the cabbage vendor."
                                            ty "but i am interested in a little one on one time with you..."
                                            ty "please help him some more!"
                                            ty "if you give me three cabbages, we'll talk!"
                                            ty "'kay?"
                                            if ty_cabbages >=3:
                                                ty "...oh, you already have!"
                                                ty "that's amazing!"
                                                ty "thank you so much!"
                                                y "sure, i guess."
                                                y "lot of damn cabbages..."
                                                ty "but... do you think you can help suki expand the tavern?"
                                                y "...are you serious?"
                                                ty "of course!"
                                                y "....fine."
                                                $ love_ty_sex_quest = 1
                                                jump tylee_cabbage_menu
                                            if ty_cabbages <3:
                                                y "fine..."
                                                jump tylee_cabbage_menu
                                    "blowjob":

                                        if bk3_cabbages >=1:
                                            ty "aw, you totally have a cabbage on you!"
                                            ty "thanks for helping my cabbage friend out!"
                                            ty "can i have this one?"
                                            y "sure."
                                            $ bk3_cabbages -=1
                                            $ ty_cabbages +=1
                                            "you gave ty lee a cabbage."
                                            ty "thanks!"
                                            ty "come on, i'll thank you properly."
                                            jump ty_cabbage_bj
                                        else:
                                            ty "remember our deal!"
                                            ty "you help that poor cabbage man and i help you!"
                                            y "right... i need a cabbage."
                                            y "stupid cabbages."
                                            jump tylee_cabbage_menu
                                    "footjob":

                                        jump love_ty_footjob
                                    "back":

                                        hide tf with dissolve
                                        jump love_inside_brothel_building
                        else:
                            show tf with dissolve
                            ty "want a footjob?"
                            menu:
                                "yes":
                                    y "you know it."
                                    ty "great!"
                                    ty "come to my room!"
                                    jump love_ty_footjob
                                "no":

                                    y "not now."
                                    ty "oh... okay."
                                    jump love_bk3_village_background


                    if suki_tylee ==6:
                        y "ty lee's still in the hospital."
                        jump love_bk3_village_background
                    if suki_tylee ==3:
                        if suki_ty_palace ==2:
                            y "she's not here."
                            y "she must be waiting at the palace."
                            y "I need to get suki to agree to help, and then meet them in the city."
                            jump love_brothel_menu2
                        if suki_ty_palace ==3:
                            y "she's not here."
                            y "she must be waiting at the palace."
                            y "I need to meet her and suki there."
                            jump love_brothel_menu2
                        else:
                            if suki_ty_palace ==1:
                                $ suki_ty_palace = 3
                            else:
                                $ suki_ty_palace = 2

                            show tf with dissolve
                            ty "hi, aang!"
                            ty "thanks again for helping me!"
                            y "it's no problem."
                            y "sorry about suki."
                            show tfa
                            hide tf
                            with dissolve
                            ty "she is being super mean."
                            y "yeah, but... it's not totally unwarranted."
                            ty "....what do you mean?"
                            y "you guys did beat up the kyoshi warriors and imprison them."
                            ty "yeah, but i did it on azula's orders!"
                            ty "and i'm not with her any more!"
                            y "i get it, but suki's slow to trust."
                            y "give her time."
                            y "and don't wear her outfit again."
                            y "not unless she gives you permission."
                            ty "boo."
                            y "that's not why i'm here, though."
                            hide tfa
                            show tf
                            with dissolve
                            ty "oh? why, then?"
                            y "i need your help."
                            ty "with what?"
                            y "we need to take down a bunch of dai lee guards and rescue a girl."
                            ty "fun!"
                            y "i mean... i guess."
                            y "so you're in?"
                            ty "definitely!"
                            y "great!"
                            y "there's just one catch."
                            ty "hmm?"
                            y "we need suki's help, too."
                            show tfa
                            hide tf
                            with dissolve
                            ty "oh."
                            ty "i... don't like that."
                            y "she's an incredible fighter, and we need her."
                            y "especially since neither of you is a bender."
                            y "we need to all pitch in."
                            ty "...."
                            ty "I'm not happy about it..."
                            ty "but as long as she doesn't start a fight, i'm in."
                            y "great, thank you."
                            show tf
                            hide tfa
                            with dissolve
                            ty "so where are we meeting?"
                            y "we're meeting at the palace."
                            y "i'm hoping that since you've worked with the dai lee that you can help us get the drop on them."
                            ty "sure!"
                            if suki_ty_palace ==2:
                                y "i just need to get suki to agree and then i'll see you there."
                                ty "sounds good."
                                ty "i'll get on it!"
                                hide tf with dissolve
                            if suki_ty_palace ==3:
                                y "suki's already agreed, so i'll meet you there."
                                ty "sounds good."
                                ty "let's get on it!"
                                hide tf with dissolve
                            jump love_brothel_menu2
                    else:

                        show tf with dissolve
                        ty "thanks for giving me a place to stay, aang!"
                        ty "you're the best!"
                        hide tf with dissolve
                        jump love_brothel_menu2
                "talk to jin":

                    if jin_anti_hypno_start >=5:
                        show tojn tojn20 with dissolve
                        jin "hey!"
                        jin "what's up?"
                        jump jin_date_ask
                    if jin_anti_hypno_start ==4:
                        show tojn tojn21 with dissolve
                        jin "hey!"
                        jin "hold on, let me get changed."
                        y "oh, you don't have to-"
                        hide tojn with dissolve
                        y "..."
                        show tojn tojn20 with dissolve
                        jin "there we go!"
                        y "...and you got dressed."
                        jin "so what's up?"
                        y "you asked me to swing by."
                        y "are we gonna get down and dirty on your bed?"
                        jin "you're funny!"
                        jin "i'm not that easy, aang!"
                        y "you're... not?"
                        jin "nope!"
                        jin "not any more, anyway..."
                        jin "you're gonna have to work for it if you want to take me to bed."
                        y "...damn you, conscience."
                        jin "aw, don't be like that."
                        jin "I'm fun, i promise!"
                        jin "oh, by the way, blowjobs totally don't count."
                        y "wait... really?"
                        jin "well yeah."
                        jin "i really enjoy them."
                        y "well that makes me feel a little better..."
                        y "in that case..."
                        $ jin_anti_hypno_start = 5
                        jump jin_date_ask

                        label jin_date_ask:
                            menu:
                                "take her on a date" if jin_anti_hypno_start ==5:
                                    y "jin, would you care to go on a date with me?"
                                    jin "i thought you'd never ask!"
                                    jin "i know just the place!"
                                    y "wait, you're picking the place?"
                                    y "then... are you asking {i}me{/i} on a date, jin?"
                                    jin "*giggle!*"
                                    jin "I guess i am!"
                                    jin "would you care to go on a little date with me, avatar?"
                                    y "I don't know, i think my schedule is pretty full."
                                    y "if i leave you a business card, maybe you can-"
                                    jin "shut up!"
                                    y "haha, alright, i'll follow you."
                                    jin "awesome!"
                                    jin "let's go."
                                    $ jin_anti_hypno_start = 6
                                    jump love_jin_date2

                                "fuck this thirsty bitch!" if jin_anti_hypno_start ==6:
                                    jump love_jin_sex_anal
                                "blowjob":

                                    y "how about a little... sucky-sucky action?"
                                    jin "sure! thanks!"
                                    scene black with dissolve
                                    scene dressingroom
                                    with dissolve
                                    jump jin_loveblowjob2
                                "leave":

                                    y "never mind."
                                    hide tojn with dissolve
                                    jump love_brothel_menu2

                    if jin_anti_hypno_start ==3:
                        y "jin's waiting for me at the tavern."
                        jump love_brothel_menu2
                    if jin_love_bj:
                        show tojn tojn21 with dissolve
                        jin "hey!"
                        y "...you're naked."
                        show tojn tojn22 with dissolve
                        jin "I'm {i}comfortable{/i}."
                        jin "would you mind... can i..."
                        jin "...would you like a blowjob?"
                        jin "like... right now?"
                        menu:
                            "sure":
                                y "sounds good."
                                jin "awesome!"
                                scene black with dissolve
                                scene dressingroom
                                with dissolve
                                jump jin_loveblowjob2
                            "later":

                                y "Not now."
                                jin "oh... okay."
                                hide tojn with dissolve
                                jump love_brothel_menu2

                    if jin_quick_talk ==0 or jin_quick_talk ==1:
                        show tojn tojn20 with dissolve
                        jin "thanks for letting me stay here!"
                        y "you're welcome!"
                        jin "let's talk another time, okay?"
                        y "okay."
                        hide tojn with dissolve
                        $ jin_quick_talk =1
                        jump love_brothel_menu2
                    if jin_quick_talk ==2:
                        show tojn tojn24 with dissolve
                        jin "who-"
                        show tojn tojn20 with dissolve
                        jin "oh, hey, aang!"
                        y "...what's wrong?"
                        show tojn tojn23 with dissolve
                        jin "what do you mean?"
                        y "you were clearly upset about something when i walked in."
                        show tojn tojn20 with dissolve
                        jin "it's nothing, i'm fine, don't worry about it."
                        y "of course i'm gonna worry, jin."
                        y "tell me what's going on."
                        jin "it's just that... well..."
                        show tojn tojn24 with dissolve
                        jin "i've been looking for a little romance, and i'm a little sad about it."
                        y "....really? you?"
                        y "but you're gorgeous."
                        jin "i don't know about that..."
                        y "i mean, i do."
                        y "take my word for it, if you're unsure."
                        show tojn tojn20 with dissolve
                        jin "thanks, aang... really."
                        jin "but..."
                        jin "i'm just sad."
                        show tojn tojn24 with dissolve
                        jin "i've never found a guy i can just... trust and have a real relationship with, you know?"
                        jin "someone i can talk to... with walks by the fountain, and sucking his cock."
                        y "that... *ahem*... sounds good..."
                        show tojn tojn20 with dissolve
                        jin "don't worry about me though, i'm okay."
                        y "well, jin..."
                        y "would you like to go on a date with me?"
                        show tojn tojn23 with dissolve
                        y "no big commitments, just good conversation and a casual stroll."
                        jin "...really?"
                        y "yeah! it'll be fun."
                        y "i mean, you already know i think you're beautiful."
                        show tojn tojn20 with dissolve
                        jin "well... how can i refuse?"
                        y "easy... don't."
                        y "how about we go for a stroll at the fountain tomorrow or later?"
                        jin "Okay."
                        jin "that sounds fun."
                        y "great!"
                        y "i'll meet you there."
                        $ bk3_day = False
                        $ jin_quick_talk = 3
                        hide tojn with dissolve
                        jump love_brothel_menu2
                    if jin_quick_talk ==3:
                        show tojn tojn20 with dissolve
                        jin "hey, i'll meet you at the fountain tomorrow or later, okay?"
                        hide tojn with dissolve
                        jump love_brothel_menu2
                    if jin_quick_talk ==4:
                        show tojn tojn20 with dissolve
                        jin "aren't we supposed to meet at the fountain?"
                        y "right, yeah."
                        y "i'll see you there."
                        hide tojn with dissolve
                        jump love_brothel_menu2
                    if jin_quick_talk ==5:
                        if jin_present ==1:
                            show tojn tojn20 with dissolve
                            jin "aang?"
                            jin "is everything okay?"
                            y "everything's great."
                            y "I just wanted to bring you a little something."
                            play sound "audio/win2.mp3"
                            "you gave jin the gift."
                            show tojn tojn23 with dissolve
                            jin "oh!"
                            jin "I don't... believe you'd do something so sweet!"
                            show tojn tojn20 with dissolve
                            jin "you're the best aang."
                            jin "thank you."
                            y "my pleasure."
                            y "see ya."
                            jin "oh... bye, then..."
                            hide tojn with dissolve
                            y "i should bring her another gift tomorrow."
                            $ jin_quick_talk =6
                            jump love_brothel_menu2
                        if jin_present ==0:
                            y "(i should get her a present before i visit her again.)"
                            jump love_brothel_menu2
                    if jin_quick_talk ==6 or jin_quick_talk ==7:
                        if jin_present ==2:
                            show tojn tojn20 with dissolve
                            jin "hello again."
                            jin "i'm glad you stopped by!"
                            y "i just wanted to let you know i'm thinking of you."
                            play sound "audio/win2.mp3"
                            "you give jin the gift."
                            show tojn tojn23 with dissolve
                            jin "oh! another one!"
                            show tojn tojn20 with dissolve
                            jin "aang... i don't... i don't deserve this..."
                            y "sure you do."
                            y "see you later!"
                            jin "b-bye..."
                            hide tojn with dissolve
                            y "i should bring her another gift tomorrow."
                            $ jin_quick_talk = 8
                            jump love_brothel_menu2
                        else:
                            y "(i should get her a present before i visit her again.)"
                            jump love_brothel_menu2
                    if jin_quick_talk == 8 or jin_quick_talk ==9:
                        if jin_present ==3:
                            y "knock knock!"
                            show tojn tojn20 with dissolve
                            jin "aang!"
                            jin "don't tell me you-"
                            y "a simple gift for you."
                            play sound "audio/win2.mp3"
                            show tojn tojn23 with dissolve
                            jin "......"
                            jin "i...."
                            show tojn tojn24 with dissolve
                            jin "*sniff...*"
                            y "jin? what's wrong?"
                            jin "no one...."
                            jin "no one's ever been this good to me..."
                            jin "what did i do to deserve your affection, aang?"
                            y "just being yourself."
                            show tojn tojn20 with dissolve
                            jin "oh, that's a cheesy answer..."
                            y "doesn't make it not true."
                            jin "....."
                            jin "i don't know what i can do to make it up to you..."
                            y "meet me at the tavern one night."
                            y "i'll get us some food, and we can have a proper date."
                            jin "alright, it's a... a date."
                            $ jin_quick_talk = 10
                            hide tojn with dissolve
                            jump love_brothel_menu2
                        else:
                            y "(i should get her a present before i visit her again.)"
                            jump love_brothel_menu2
                    if jin_quick_talk ==10:
                        y "(jin will meet me for dinner at the tavern at night.)"
                        y "(i should leave her alone until then.)"
                        jump love_brothel_menu2

                    if jin_quick_talk == 11:
                        y "...jin?"
                        jin "come in!"
                        scene black with dissolve
                        jump jin_loveblowjob
                "talk to june":

                    if not june_available:
                        play sound "audio/knocking.mp3"
                        "you knock on june's door."
                        "there's no answer."
                        y "....."
                        y "stop ignoring me!"
                        jump love_brothel_menu2
                    else:

                        if suki_tylee >=1 and june_light <=4:
                            if june_light ==4:
                                show toju toju09 with dissolve
                                ju "welcome back, avatar."
                                y "thanks."
                                y "you said you had something to give me?"
                                show toju_blink with dissolve
                                ju "well, i was hoping..."
                                ju "you might have something..."
                                hide toju_blink with dissolve
                                ju "...to give me."
                                y "....oh."
                                ju "you saved me once again with that guard."
                                ju "you're helping all these girls and protecting me..."
                                ju "i think you deserve a reward."
                                ju "come with me."
                                hide toju with dissolve
                                "june slips into her room."
                                y "Interesting...."
                                jump june_lovefuck

                            if june_light ==3:
                                y "i should leave her alone tonight."
                                jump love_brothel_menu2
                            if june_light ==2:
                                $ june_light = 3
                                show toju toju09 with dissolve
                                ju "hi there."
                                y "you wanted to see me?"
                                show toju toju12 with dissolve
                                ju "did i?"
                                ju "i don't recall telling you-"
                                show fireguard_halberd:
                                    xzoom -1
                                with moveinleft
                                fg "hey, do you guys sell-"
                                show toju toju08 with dissolve
                                ju "....."
                                fg "......"
                                y "........"
                                fg "...shit."
                                show toju toju11 with dissolve
                                ju "shit."
                                y "shit."
                                fg "you're still alive?!"
                                fg "but i thought..."
                                y "hey you, what's your name?"
                                fg "...."
                                fg "nothing. no one."
                                fg "i didn't... i didn't see anything..."
                                fg "I'm just leaving-"
                                ju "oh no you're not!"
                                fg "wait, wait, wait!"
                                ya "i got him!"
                                fg "nononono-!"
                                play sound "audio/thud.mp3"
                                with hpunch
                                hide fireguard_halberd with moveoutbottom
                                fg "unngh...."
                                ju "shit shit shit!"
                                y "i didn't think they'd come back..."
                                ju "well obviously they have!"
                                y "don't get mad at me, i didn't do anything."
                                show toju toju09
                                show toju_blink
                                with dissolve
                                ju "...you're right."
                                ju "sorry."
                                ju "there's clearly only one thing to be done..."
                                y "i don't like how that sounds...."
                                hide toju_blink with dissolve
                                ju "we have to kill him."
                                y "yeah... i didn't think i was going to like it."
                                ju "it's our only option."
                                y "i don't think it is..."
                                ju "you need to kill him."
                                y "wait, {i}i{/i} need to kill him?"
                                ju "what if i gave you some... incentive?"
                                ya "there's no incentive that's gonna make me kill this guy!"
                                show toju toju12 with dissolve
                                ju "really?"
                                show toju toju13 with dissolve
                                ju "not even..."
                                show toju toju16 with dissolve
                                ju "these?"
                                show ctc
                                pause
                                hide ctc
                                y "those are... they're very nice, june..."
                                y "but he only-"
                                show toju toju17 with dissolve
                                ju "{i}ah ah ah."
                                show toju toju100
                                ju "look here."
                                ju "look at these big, sloppy, titties."
                                ju "you want to see more of them, right?"
                                y "june..."
                                ju "how about some pussy?"
                                ju "you wanna see some pussy?"
                                y "june, you're not gonna get me to-"
                                show toju toju18 with dissolve
                                show ctc
                                pause
                                hide ctc
                                y "you're... not wearing underwear."
                                ju "who needs it?"
                                y "that's... a good point..."
                                ju "come on... take care of him, and i'll... take care of you."
                                y "maybe..."
                                y "....."
                                ya "no!"
                                ya "damn it, june!"
                                ya "there are other options!"
                                show toju toju11 with dissolve
                                ju "like what?!"
                                ju "he can't be set free, avatar!"
                                ju "the fire nation will find out i'm still alive!"
                                ju "they'll hunt me down!"
                                ju "would you rather i die instead of this nobody?"
                                y "he's not a nobody!"
                                y "he's the hero of his own story!"
                                ju "I don't care!"
                                y "okay, he's already unconscious."
                                y "just... just let me think."
                                ju "you know what to do."
                                y "okay, okay, wait..."
                                show toju toju10 with dissolve
                                ju "aang... listen..."
                                y "no, be quiet, i have an idea."
                                y "come with me."
                                scene black with dissolve
                                "you throw the guard over your shoulder and hurry out."
                                "june stays close behind you."
                                jump fireguard_hypno


                            if june_light ==1:
                                y "she told me to come back tomorrow or later."
                                jump love_brothel_menu2

                            show toju toju09
                            with dissolve
                            ju "hey."
                            y "how are you?"
                            ju "i wanted to ask-"
                            show toju toju08 with dissolve
                            ju "wait, what?"
                            y "I asked how you are."
                            show toju toju12
                            with dissolve
                            ju "no, i heard that, i'm just... confused."
                            y "you're confused?"
                            show toju toju10 with dissolve
                            ju "well, not confused so much as... unfamiliar..."
                            y "with people being nice to you?"
                            show toju toju11 with dissolve
                            ju "oh... shut up!"
                            y "okay..."
                            ju "......."
                            y "so...."
                            y "what did you want to ask?"
                            show toju toju10
                            show toju_blink
                            with dissolve
                            ju "*sigh...*"
                            ju "it doesn't matter."
                            y "sure it does."
                            y "what's up?"
                            show toju toju09
                            with dissolve
                            ju "i wanted to ask..."
                            hide toju_blink with dissolve
                            ju "how serious are you about this \"boarding house\" thing?"
                            y "completely serious."
                            ju "really?"
                            ju "but... why?"
                            y "because these girls are in need."
                            y "and that's including yourself, in case you've forgotten."
                            show toju_blink with dissolve
                            ju "i haven't."
                            ju "....."
                            hide toju_blink with dissolve
                            ju "i guess i just haven't known anyone like you before."
                            y "there is no one like me."
                            ju "oh, {i}ha ha{/i}."
                            ju "....."
                            ju "You're... a good man, avatar."
                            ju "i didn't expect that."
                            y "are you seeing me in a new light, mistress june?"
                            show toju toju12 with dissolve
                            ju "get out of here before i bust your face in."
                            y "alright, alright, i'll go before you fall in love with me."
                            show toju_blink with dissolve
                            ju "unbelievable..."
                            y "heh."
                            ju "hey, wait."
                            hide toju_blink
                            show toju toju09
                            with dissolve
                            ju "you can come back tomorrow or something."
                            ju "...if you can avoid being too self-absorbed."
                            y "no promises, but good to know."
                            show toju toju12 with dissolve
                            ju "get out of here!"
                            hide toju
                            with dissolve
                            $ june_light = 1
                            jump love_brothel_menu2

                        show toju toju09
                        with dissolve
                        ju "yes?"
                        menu:
                            "chat":
                                if june_hypno_today:
                                    y "(i should give her a day to recover.)"
                                    jump love_brothel_menu2

                                if love_june_hypno ==12:
                                    y "i guess you can't be a bounty hunter anymore, huh?"
                                    ju "I guess not."
                                    y "so... you probably need a job...?"
                                    ju "....fine."
                                    ju "i'll be your brothel's madam."
                                    ju "i'll take care of your sluts."
                                    y "woo!"
                                    ju "yeah, yeah."
                                    $ love_june_hypno = 13
                                    jump love_brothel_menu2
                                if love_june_hypno ==10:
                                    ju "I'll meet you at your place for an anti-hypnosis session."
                                    jump love_brothel_menu2
                                if love_june_hypno ==9:
                                    y "ready for another session, june?"
                                    ju "i suppose."
                                    ju "are they actually working?"
                                    y "probably?"
                                    y "it can't hurt."
                                    show toju_blink with dissolve
                                    ju "then i'll meet you there."
                                    $ love_june_hypno = 10
                                    jump love_brothel_menu2
                                if love_june_hypno ==8:
                                    ju "I'll meet you at your place for an anti-hypnosis session."
                                    jump love_brothel_menu2
                                if love_june_hypno ==7:
                                    y "how about another session, june?"
                                    ju "since the last one went so well?"
                                    y "come on, every bit helps."
                                    show toju_blink with dissolve
                                    ju "of course i'll come, avatar."
                                    ju "I'll meet you there."
                                    hide toju_blink
                                    $ love_june_hypno = 8
                                    jump love_brothel_menu2
                                if love_june_hypno ==6:
                                    ju "I'll meet you at your place for an anti-hypnosis session."
                                    jump love_brothel_menu2
                                else:
                                    show toju toju12 with dissolve
                                    ju "my tits look great in this, don't they?"
                                    if love_june_hypno ==11:
                                        ju "by the way, i still have a favor to ask of you, but it's not ready yet."
                                        ju "I'll come find you when it's time."
                                        ju "see you around, avatar."
                                    hide toju with dissolve
                                    jump love_brothel_menu2

                            "missionary sex" if june_light >=5:
                                jump june_lovefuck

                            "play with her tits" if love_june_hypno >=12:
                                y "can i play with your tits?"
                                ju "sigh..."
                                ju "i suppose."
                                jump june_titplay_standing
                            "handjob":

                                y "how about another handjob?"
                                show toju_blink with dissolve
                                ju "*sigh...*"
                                ju "very well."
                                hide toju_blink with dissolve
                                ju "come here."
                                jump love_june_handjob2
                            "back":

                                jump love_brothel_menu2
                "exit":

                    jump love_bk3_village_background

    if brothel_quest ==8:
        show toju toju01
        with dissolve
        ju "yes?"
        jump love_brothel_menu

        label love_brothel_menu:
            menu:
                "handjob":
                    y "how about another handjob?"
                    show toju_blink with dissolve
                    ju "*sigh...*"
                    ju "very well."
                    hide toju_blink with dissolve
                    ju "come here."
                    jump love_june_handjob2
                "talk to june":

                    if suki_lantern_explain:
                        if love_june_hypno ==2:
                            if june_madam_outfit:
                                $ love_june_hypno = 3
                                y "i brought an outfit for you."
                                ju "...."
                                ju "you can't be serious."
                                ju "I'm {i}not{/i} wearing that."
                                ya "oh, yes you are."
                                ya "i paid good money for this."
                                ju "no, you paid regular money."
                                ju "maybe even badly earned money."
                                ju "and i'm still not wearing it."
                                ju "it looks like madam's dress."
                                ju "like i'm managing the brothel."
                                ju "and that's definitely not my job."
                                y "june, just..."
                                y "it fits in with the brothel and it's only barely revealing."
                                y "and if it looks like you're a madam, running the place, people will treat you with respect."
                                show toju_blink with dissolve
                                ju "hmm...."
                                ju "that's true..."
                                hide toju_blink with dissolve
                                ju "and i wouldn't have to do anything brothel-related?"
                                y "just enough to keep up appearances."
                                ju "....what."
                                y "i'm the avatar, june... i can't be seen running a brothel."
                                y "I'm trying to save the world."
                                ju "and i should care because...."
                                y "because... i might be able to remove any brainwashing you received."
                                ju "i don't think i received any."
                                y "i'm not sure you would know that."
                                y "just put the outfit on, then we'll discuss duties."
                                ju "fine."
                                ju "but i'll tell you now..."
                                ju "i'm not doing any brothel work."
                                ju "now don't peek."
                                hide toju with moveoutright
                                y "....."
                                y "..........."
                                y "you almost finished?"
                                ju "......."
                                show toju toju09 with moveinright
                                ju "how's it look?"
                                menu:
                                    "great!":
                                        y "really good."
                                        y "i apparently have fantastic taste."
                                    "terrible!":

                                        y "terrible."
                                        y "you should take it off."

                                show toju_blink with dissolve
                                ju "hilarious."
                                hide toju_blink with dissolve
                                ju "i do look good though, don't i?"
                                ju "hmm...."
                                show toju toju12 with dissolve
                                ju "i think this will work just fine."
                                y "alright, now for duties-"
                                ju "none."
                                ju "i'm not doing anything here."
                                ju "i'm here to find bounty clients."
                                y "if you're gonna stay here..."
                                show toju toju11 with dissolve
                                ju "don't push me, avatar."
                                ju "you want to stay in my good graces?"
                                ju "be a good boy and be quiet."
                                y "......"
                                show toju toju12 with dissolve
                                ju "there, now that wasn't so hard, was it?"
                                ju "i'll be in my room if you need me."
                                hide toju with dissolve
                                y "....how am i gonna get her to manage this damn place?"
                                y "I don't want to fucking work."
                                $ bk3_day = False
                                $ june_available = False
                                jump love_bk3_village_background
                            else:

                                ju "let me know when you find that outfit."
                                jump love_brothel_menu

                        if love_june_hypno ==1:
                            ju "have you found a whore yet?"
                            ju "this brothel is just a waste of money right now."
                            menu:
                                "i have":
                                    if love_jin_freed:
                                        if love_jin_brothel:
                                            y "i have, actually."
                                            show tojn tojn20:
                                                xzoom -1
                                            with dissolve
                                            jin "hey, is this-"
                                            show tojn tojn23 with dissolve
                                            jin "ah!"
                                            show tojn tojn24 with dissolve
                                            jin "I'm not going back!"
                                            y "what?"
                                            jin "she's... she's a bounty hunter right?"
                                            jin "i can tell by her outfit!"
                                            show toju toju02 with dissolve
                                            ju "well, she's not wrong."
                                            y "you're not helping, june!"
                                            ju "not trying to help."
                                            show toju toju01 with dissolve
                                            jin "well, she can't make me go back!"
                                            jin "i'll... i'll..."
                                            y "no one's gonna make you do anything, jin."
                                            y "june is my guest here."
                                            show tojn tojn23 with dissolve
                                            jin "oh."
                                            jin "really?"
                                            y "really."
                                            jin "then..."
                                            show tojn tojn20 with dissolve
                                            jin "it's nice to meet you!"
                                            show toju toju02 with dissolve
                                            ju "likewise, i'm sure."
                                            jin "i'll go get set up in my room, then."
                                            hide tojn with dissolve
                                            ju "she seems nice."
                                            ju "a little simple, perhaps."
                                            ju "but i'm sure she can suck dick well?"
                                            y "uh... about that..."
                                            ju "what?"
                                            y "she... might not be ready for that yet."
                                            ju "...."
                                            ju "then what... is the point... of having her here?"
                                            y "she'll get there, just let me work on it."
                                            y "and don't push her."
                                            ju "....fine."
                                            ju "it's your brothel."
                                            y "great, now..."
                                            y "you have to lose those clothes."
                                            show toju toju03 with dissolve
                                            ju "what?"
                                            y "i just mean you need different ones!"
                                            ju "what's wrong with my outfit?"
                                            ju "answer or get a whipping!"
                                            y "uh... that."
                                            ju "...what?"
                                            y "it's intimidating!"
                                            y "you're gonna scare everyone away!"
                                            ju "...."
                                            show toju toju02
                                            show toju_blink
                                            with dissolve
                                            ju "you may have a point."
                                            y "some people might be into a little light whipping, but for now let's ease you-"
                                            show toju toju03
                                            hide toju_blink
                                            with dissolve
                                            ju "I am not a whore!"
                                            y "i didn't say you were, calm down."
                                            y "look, if you're gonna set up shop here, you can't scare people away."
                                            y "jin almost bolted when she saw you."
                                            show toju toju01 with dissolve
                                            ju "so what do you propose?"
                                            y "let me grab you something more appropriate."
                                            ju "...very well."
                                            hide toju with dissolve
                                            y "great... now to find an outfit for june."
                                            $ love_june_hypno = 2
                                            jump love_bk3_village_background
                                        else:

                                            y "actually i did find somebody."
                                            y "but i'm still working on getting her over here."
                                            ju "well, do that."
                                            jump love_brothel_menu
                                    else:

                                        y "i... yes?"
                                        ju "...."
                                        show toju toju02 with dissolve
                                        ju "why are you lying to me?"
                                        ju "I don't care what you do."
                                        y "I just want you to think i'm cool."
                                        y "like, when i leave, i hope you think \"there goes a pretty cool guy\"."
                                        ju "I don't think \"there goes a pretty cool guy\", i think \"there goes a guy who struggles to get hookers to have sex\"."
                                        y "....that hurts. that hurts me deeply."
                                        show toju_blink with dissolve
                                        ju "you'll recover."
                                        hide toju_blink
                                        show toju toju01
                                        with dissolve
                                        jump love_brothel_menu
                                "i'm working on it":

                                    y "I'm working on it."
                                    show toju_blink with dissolve
                                    ju "you don't need to justify your bad decisions to me."
                                    ju "get your sluts or don't."
                                    y "i am working on it!"
                                    hide toju_blink with dissolve
                                    ju "sure."
                                    jump love_brothel_menu

                        if love_suki_hypno >=13:
                            if love_jd_hypno ==0 or love_jd_hypno >=8:
                                if love_june_hypno ==0:
                                    $ love_june_hypno = 1
                                    y "hey, june."
                                    ju "avatar."
                                    y "don't make it bad."
                                    ju "what?"
                                    y "take a sad sooong and make it betttteeeeerrr...."
                                    ju "what the hell are you on about?"
                                    ju "stop that."
                                    y "aw."
                                    ju "well, besides whatever that was, i'm glad you stopped by."
                                    ju "i've been meaning to talk to you."
                                    y "'bout what?"
                                    ju "you know there's only one bedroom here, right?"
                                    ju "and that one's mine."
                                    show toju toju02 with dissolve
                                    ju "do you intend to have any sluts here or what?"
                                    y "i mean, i've been thinking about it..."
                                    show toju_blink with dissolve
                                    ju "look, i really don't care, but it's not a very smart business decision to just give me a house to myself."
                                    hide toju_blink with dissolve
                                    ju "for free."
                                    menu:
                                        "it's not free":
                                            y "yeah, but it's not free, is it?"
                                            show toju toju01 with dissolve
                                            ju "...i guess."
                                            ju "but you know what i mean."
                                        "i like you":

                                            y "i like you, so what's the issue?"
                                            show toju_blink with dissolve
                                            ju "that's up to you, of course."
                                            y "....."
                                            ju "but, you know..."
                                            hide toju_blink
                                            show toju toju01
                                            with dissolve

                                    ju "you should really find yourself a whore."
                                    y "...i probably should, right?"
                                    ju "probably."
                                    y "well, alright."
                                    y "i'll start looking."
                                    show toju_blink with dissolve
                                    ju "whatever."
                                    jump love_bk3_village_background

                    if iroh_book_talk:
                        if not footjob_book:
                            if june_book_talk:
                                ju "do you have 50 coins for the book?"
                                menu:
                                    "i have the coins":
                                        y "i've got your money."
                                        if emoney >=50:
                                            ju "oh, look how forward-thinking you are."
                                            ju "i'll take that..."
                                            play sound "audio/money.mp3"
                                            $ emoney -=50
                                            ju "and here's your book!"
                                            play sound "audio/win2.mp3"
                                            "you got a smutty novel!"
                                            y "looks like it's just a couple pages, though..."
                                            $ footjob_book = True
                                            jump love_brothel_menu
                                        else:
                                            ju "i don't think you do."
                                            ju "come back when you're ready to pay for it."
                                            y "...damn it."
                                            jump love_brothel_menu
                                    "i'll be back later":

                                        y "i'll be back for it."
                                        ju "i look forward to that."
                                        jump love_brothel_menu
                            else:
                                $ june_book_talk = True
                                y "june, did iroh leave a book here?"
                                ju "a book?"
                                ju "i think i remember him leaving something..."
                                show toju toju02 with dissolve
                                ju "oh, right."
                                ju "he left a... graphic little tale."
                                ju "he wanted me to do... the main act to him."
                                show toju_blink with dissolve
                                ju "horny old goat."
                                y "well, can i have it?"
                                hide toju_blink
                                show toju toju01
                                with dissolve
                                ju "it's just a short little thing..."
                                ju "why do you want it?"
                                y "...are you gonna give it to me or not?"
                                show toju_blink with dissolve
                                ju "i'd hate to part with something so dear to me..."
                                y "you literally did not care about it five seconds ago."
                                hide toju_blink
                                show toju toju02
                                with dissolve
                                ju "but that was before i knew you wanted it."
                                y "........."
                                ju "i'm a bounty hunter, aang."
                                ju "money is a big motivation for me."
                                y "......."
                                y "fine."
                                y "how much?"
                                show toju toju01
                                show toju_blink
                                with dissolve
                                ju "well..."
                                ju "I think 50 coins should do it."
                                ya "50?!"
                                ya "for a stupid little story?"
                                ju "i mean... if you don't want it..."
                                ya "oh, fine."
                                ju "let me know when you'd like to trade."
                                hide toju_blink with dissolve

                                menu:
                                    "i have the coins":
                                        y "i've got your money."
                                        if emoney >=50:
                                            ju "oh, look how forward-thinking you are."
                                            ju "i'll take that..."
                                            play sound "audio/money.mp3"
                                            $ emoney -=50
                                            ju "and here's your book!"
                                            play sound "audio/win2.mp3"
                                            "you got a smutty novel!"
                                            y "looks like it's just a couple pages, though..."
                                            $ footjob_book = True
                                            jump love_brothel_menu
                                        else:
                                            ju "i don't think you do."
                                            ju "come back when you're ready to pay for it."
                                            y "...damn it."
                                            jump love_brothel_menu
                                    "i'll be back later":

                                        y "i'll be back for it."
                                        ju "i look forward to that."
                                        jump love_brothel_menu

                    if shadygone and not juneshadytalk:
                        y "june, did you see anyone suspicious last night?"
                        ju "last night?"
                        show toju_blink with dissolve
                        ju "hmmm...."
                        ju "well...."
                        hide toju_blink with dissolve
                        ju "there was a fat old guy trying to get into the brothel last night."
                        ju "he woke me up, in fact."
                        ju "why do you ask?"
                        y "someone burned my house down..."
                        y "with me inside it."
                        ju "right... i saw the remains."
                        show toju_blink with dissolve
                        ju "that's a shame."
                        ju "perhaps the fat old man can help you out."
                        hide toju_blink with dissolve
                        y "ugh. guess i could look into it."
                        $ juneshadytalk = True
                        jump love_bk3_village_background
                    else:

                        ju "don't get licked by my shirshu."
                        ju "just don't."
                        jump love_brothel_menu
                "exit":

                    jump love_bk3_village_background

    if brothel_quest ==7:
        show toju toju01
        with dissolve
        ju "well... it's not perfect."
        ju "but it's good enough."
        ju "i can see you've set it up to have a girl or two here."
        ju "i wonder how you'll do with that."
        ju "for example...."
        ju "do you think girls should have some bush or be clean shaven?"
        menu:
            "bush":
                $ june_pubes = "bush"
            "shaven":
                $ june_pubes = "shaven"
        ju "interesting."
        y "why? which are you?"
        show toju_blink with dissolve
        ju "well, that's none of your business."
        ju "but let's just say..."
        hide toju_blink
        show toju toju02
        with dissolve
        ju "....i think you'd like it."
        y "...."
        ym "nice."
        show toju toju01 with dissolve
        ju "hmm...."
        ju "i think i'll be happy here."
        y "about that..."
        menu:
            "you can have free boarding":
                $ june_forced = False
                $ june_sympathy += 1
                y "you can stay here... rent-free."
                show toju toju04 with dissolve
                ju "really?"
                show toju toju02 with dissolve
                ju "that's wonderf-"
                show toju toju01 with dissolve
                ju "........."
                ju "....hmmm."
                y "what?"
                ju "that's... really wonderful of you, avatar."
                ju "......"
                ju "............"
                ju "...................."
                y "okay, seriously, what?"
                ju "I am..."
                show toju_blink with dissolve
                ju "...between jobs at the moment."
                y "I know."
                ju "....."
                ju "............."
                hide toju_blink with dissolve
                ju "i believe i owe you for your help."
                ju "and i don't want to... drain... that well of goodwill."
                ju "....so to speak."
                ju "especially since i'm sure we'll be helping each other out for a while yet."
                y "hmmm."
                y "well... what are you suggesting?"
                ju "would you...."
                ju "well...."
                show toju toju02 with dissolve
                ju "would you like a handjob, avatar?"
                menu:
                    "hell yeah!":
                        y "I... well... yeah."
                        y "put those hands around my dick!"
                        show toju_blink with dissolve
                        ju "of course."
                        ju "and there's no one here but us...."
                        ju "come here."
                        hide toju_blink with dissolve
                        ju "let's make this quick."
                    "nah":

                        y "not right now."
                        show toju_blink with dissolve
                        ju "perhaps some other time, then."
                        hide toju_blink with dissolve
                        ju "see you around."
                        $ brothel_quest = 8
                        jump love_bk3_village_background
            "you're gonna have to earn your stay":

                $ june_forced = True
                y "you can stay here."
                show toju toju02 with dissolve
                ju "that's grea-"
                y "for a price."
                show toju toju01 with dissolve
                ju "....."
                ju "hmm."
                show toju_blink with dissolve
                ju "and what would that price be, i wonder?"
                y "you haven't been getting any jobs while at the tavern, have you?"
                y "I've been watching, and it doesn't look like you have any money."
                ju "that... is true."
                ju "i am..."
                ju "...between jobs at the moment."
                y "hmmm...."
                y "maybe there's another way you can pay."
                hide toju_blink with dissolve
                ju "oh?"
                show expression "bk3/june/idles/angry.png" with dissolve
                ju "let me guess."
                y "you're going to jack me off."
                y "right here, right now."
                ju "....."
                show toju_blink with dissolve
                ju "of..."
                ju "...course."
                ju "..............."
                hide expression "bk3/june/idles/angry.png"
                with dissolve
                ju "come here then.... avatar."
                hide toju_blink with dissolve
                ju "let's make this quick."
        $ brothel_quest = 8
        jump love_june_handjob

    if brothel_quest <=6:
        y "i should really get june in here."

    jump love_bk3_village_background


label earthtraining4:
    show toi toi51 with dissolve
    t "mooselion!"
    y "what?"
    show toi toi01 with vshake
    t "{size=+10}mooselion!"
    show m_battle_big_01:
        xzoom -1.0
    hide toi toi01
    with dissolve
    "mooselion" "rrrarrrr!!"
    ya "ah! fuck!"
    y "no, no, no, not these things again..."
    show m_battle_big_02:
        xzoom -1.0
    hide m_battle_big_01
    with dissolve
    y "oh... wait.. no... don't..."
    y "don't do that...."
    t "stand your ground, aang!"
    t "you've got it in you!"
    t "i believe in you!"
    show m_battle_bigl_03:
        xzoom -1.0
    hide m_battle_big_02
    with dissolve
    y "aaaaaaahhhhh-"
    "mooselion" "rrrraarrraaarrhh-"
    show earth_attack at truecenter
    with vshake
    hide m_battle_bigl_03
    hide earth_attack
    with moveoutleft
    "the mooselion wanders off."
    y "that... was terrifying."
    show toi toi07
    with dissolve
    t "you've got {i}stuff{/i}, aang!"
    t "well done!"
    t "you're an earthbender."
    show toi_blink
    with dissolve
    t "a baby one, but you took your first steps today."
    hide toi_blink
    show toi toi04
    with dissolve
    t "i guess that \"positive reinforcement\" thing really does work for you."
    show toi toi09 with dissolve
    t "......"
    t "we should... probably celebrate, right?"
    t "reward you for... doing a good job."
    t "right?"
    y "uh, sure."
    t "what would you like to do?"
    $ earthbending = 5
    menu:
        "go to the beach":
            $ toph_points +=1
            pass
        "suck your tits":

            "(really, bro?)"
            "(fine, you asked for it.)"
            y "i wanna slobber on your titties, boo."
            t "....."
            y "get 'em all wet and sloppy."
            show toi toi06 with dissolve
            t "......"
            t "............"
            y "just mess them all around."
            show toi toi05 with dissolve
            t "................"
            t "guess who has two thumbs and a sore dick?"
            y "....."
            y "....i don't want to answer that."
            show toi toi01 with dissolve
            t "let me help you out."
            y "is it..."
            y "is it me?"
            t "look at that! you win!"
            y "what... do i win?"
            show toi toi101
            y "ow!"
            y "hrrk."
            y "....ow...."
            y "my dick..."
            t "what?"
            y "i said... i'm sorry..."
            t "......"
            show toi toi06 with dissolve
            t "......"
            t "alright, come on you idiot, pick something else."
            t "we've got your training to think of."
            menu:
                "go to the beach":
                    pass
    y "how about the beach?"
    y "i want to go for a real swim this time."
    show toi toi09 with dissolve
    t "oh."
    t "umm..."
    t "any other option?"
    y "....not one you're gonna like."
    y "what's wrong with the beach?"
    t "i just..."
    t "don't feel like it."
    y "come on, what's wrong?"
    show toi toi05 with dissolve
    t "shut up! nothing's wrong!"
    show toi toi06 with dissolve
    t "come on then, twinkletoes."
    scene black with dissolve
    $ toph_top_nude = False
    $ toph_bottom_nude = False
    stop music
    play music "audio/Bassa Island Game Loop.ogg"
    scene black
    scene lake_laogai_3
    show toi toi200
    show toph_regret
    with dissolve
    y "nice!"
    y "let's go for a long swim this time."
    y "go way out there."
    t "...."
    y "oh, come on, what is it?"
    t "......."
    t "i'm not a good swimmer."
    y "oh, yeah... you mentioned that."
    y "actually, yeah, i don't think i've ever seen you swim."
    t "i like my feet planted firmly on something less liquid."
    t "i like to see where i go."
    y "oh, right... you must be pretty blind when surrounded by water."
    y "aren't you afraid you'll fall overboard when we're on a boat?"
    t "nah. you or katara can always waterbend me to safety."
    y "come on, get in the water."
    y "just doggy-paddle or whatever."
    t "no, i..."
    t "...i can't swim at all."
    y "what? but you've been in the water with us."
    t "only waist deep!"
    y "....come on, I'll teach you."
    hide toph_regret
    show expression "bk3/toph/idles/idle_fl_angry.png"
    with dissolve
    t "tough luck, i'm not gonna."
    y "and here i was, thinking you were tough."
    t "i {i}am{/i} tough!"
    y "then why are you so afraid?"
    t "i'm not afraid!"
    show toph_regret
    hide expression "bk3/toph/idles/idle_fl_angry.png"
    with dissolve
    t "i just... i don't wanna..."

    menu:
        "don't be a chicken":
            y "what happened to all that tough love you were spouting when you wanted me to earthbend?"
            y "just get in the water, you chicken."
            t "hey...."
            show toi_tears with dissolve
            t "it's not... it's not my fault..."
            y "oh, shit."
        "it's okay, i'll help":

            y "don't worry, that's-"
            show toi_tears with dissolve
            y "oh, shit."

    y "hey, hey, it's okay."
    y "everybody lacks some \"normal\" skill or other."
    y "we've all been there."
    y "I, for one, can't whistle."
    t "*sniff*"
    t "really?"
    y "fuck no, of course I can whistle."
    y "who can't whistle?"
    t "......."
    t "me..."
    y "oh. shit. sorry."
    y "let's both just agree that i'm bad at this."
    y "see! comforting is a normal skill, and i'm no good at that."
    y "look, i'll walk you through it, you'll pick it right up."
    t "*sniff*"
    y "do you trust me?"
    t "...you're asking me that a lot lately."
    y "well... do you?"
    hide toi_tears with dissolve
    t "...yes."
    y "come on, then."
    t "........"
    t "i... i just need a push."
    y "a push?"
    t "just a little one."
    y "i can give you a push."
    t "just warn me before-"
    jump toph_learntoswim

label toph_learntoswim:
    scene black
    show expression "bk3/toph/swim/water_tentacle.png":
        ypos 1000
        linear 2.0 ypos 0
        linear 3.0 ypos 1000
    "you waterbend tentacles that reach out of the lake and grab Toph, throwing her in."
    t "WAaaaaah!!"
    scene black
    $ renpy.pause(0.05)
    show expression "bk3/toph/swim/bg_swim.jpg"

    show tols tols01:
        xpos 200
        parallel:
            linear 6.0 xpos 300
            linear 6.0 xpos 200
            repeat
        parallel:
            linear 3.0 ypos 20
            linear 3.0 ypos 0
            repeat
    with dissolve
    t "i told you to warn me, you jerk!"

    show ctc
    pause
    hide ctc
    y "That's it, kick those legs, girl!"
    t "I... Will... Kill... you...!"
    y "I guess I should leave, then?"
    t "NOOO!! Don't let go!!"
    t "don't let go, don't let go, don't let go..."
    y "I didn't think you'd be this afraid of it."
    y "I'll take you back to land."
    t "NO! I'm NOT afraid! You just surprised me!"
    t "jerk!"
    t "And if you think I'm not going to get you back for this..."
    show tols tols02
    t "Hehehe..."
    y "That's quite a menacing little laugh you got there..."
    t "Trust me, I've got something really good in mind."
    y "Are you going to bury me to the neck, in rock, next to an anthill?"
    y "and call it training?"
    t "Great idea! Now I have two things I want to try!"
    y "You're doing surprisingly well for someone who's hating swimming this much!"
    show tols tols01
    t "don't let go of me, no matter what!!!"
    y "i won't."
    y "and you're doing great."
    show tols tols03
    t "Hey..."
    t "....I {i}am{/i} doing pretty well, aren't i!?"
    t "The world should be very happy I don't have any thoughts of world conquest. Hahaha!"
    y "Wanna try and go a bit faster?"
    y "I won't let go."
    t "Mmmmh....sure let's try it."
    t "but this doesn't mean you're safe, buddy!"
    t "I'm still going to get you back for this!"
    t "One of these days when you least expect it..."
    t "BAM!"
    y "Okay, hold on tight."
    y "Here, we go!"

    show tols tols03:
        xzoom 1.0
        linear 7.0 xpos 900
        xzoom -1.0
        linear 7.0 xpos -500
        repeat

    show tols tols02
    $ renpy.pause(2)
    t "I'm... a speedboat!"
    t "weeeeeee!!!"
    show ctc
    pause
    hide ctc
    y "Wanna be a submarine?"
    show tols tols01
    t "DON'T EVEN JOKE ABOUT THAT!"
    y "hahaha!"
    y "No watery surprises!"
    y "I swear!"
    hide tols with Dissolve(2.0)
    show text "{color=#ffffff}{size=40}twenty minutes later{/size}{/color}"
    $ renpy.pause()
    hide text
    show tols tols04 with Dissolve(2.0):
        xpos 200
        parallel:
            linear 6.0 xpos 300
            linear 6.0 xpos 200
            repeat
        parallel:
            linear 3.0 ypos 20
            linear 3.0 ypos 0
            repeat
    t "This was actually really fun!"
    show ctc
    pause
    hide ctc
    t "I've decided to not cover your face in honey when I bury you up to your neck."
    y "....next to an anthill?"
    t "exactly."
    y "So you're still going to do that..."
    t "It'd be a waste of a great idea not to."
    y "That makes me even more scared about what I'm going to say next."
    y "This is totally not my fault... but..."
    t "what?"
    y "Half of what you were wearing is... gone."
    show tols tols05 with Dissolve(2.0)
    t "DID YOU DO THIS?!?"
    y "NO! Absolutely not!"
    t "Don't look!!"
    t "take me to the shore!"
    t "And don't let go of my hands until then!"
    show ctc
    pause
    hide ctc
    show expression "bk3/toph/swim/bg_swim_1.jpg":
        ypos -210
    hide expression "bk3/toph/swim/bg_swim.jpg"
    hide tols
    with Dissolve(2.0)
    y "You can touch the bottom here."
    show tols tols10 with Dissolve(2.0)
    t "Where did my upper piece disappear to?!"

    show expression "bk3/toph/swim/top_float.png":
        parallel:
            ypos 490
            linear 2.0 ypos 500
            linear 2.0 ypos 490
            repeat
        parallel:
            xpos -300
            linear 5.0 xpos 150
    show ctc
    pause
    hide ctc
    y "It probably came untied during the swimming and is floating somewhere....."
    $ renpy.pause(2)
    y "Well, fuck me. It actually came drifting towards us just now."
    y "It's right in front of you."
    show tols tols13
    t "Handy!"
    "with a few tries toph picks it up and puts it back on."
    hide expression "bk3/toph/swim/top_float.png"
    show tols tols12
    y "Wanna go for another round?"
    show tols tols14
    t "NO." with hpunch
    t "........"
    t "........maybe some other time."
    show tols tols12 with dissolve
    t "....and i gave you some crap, but..."
    t "this was a lot of fun."
    t "thanks for helping me... conquer that fear."
    t "wanna head back?"
    menu:
        "head back":
            y "yeah, let's go."
        "not yet":
            y "in a minute."
            y "i just want to say..."
            menu:
                "tease":
                    y "you're the worst swimmer i've ever seen."
                    show tols tols14 with dissolve
                    t "hey!"
                    t "you're no expert either!"
                    t "why don't you go back out there, stick your head in the water, and-"
                    y "whoa, i'm just teasing you."
                    t "well, maybe i don't always like that!"
                    t "i'm going back."
                    hide tols with dissolve
                    y "well... shit."
                "compliment":

                    $ toph_points +=1
                    y "you're impressive, and beautiful."
                    t "oh! um-"
                    y "you should never feel insecure about what you have or haven't done."
                    y "you have your own unique combination of experiences and strengths."
                    t "i... i don't know if {i}that's{/i} true, but-"
                    y "it is true."
                    y "and you have more to offer than any girl i've ever met."
                    y "you surprise me every day."
                    t "I... oh..."
                    t "um..."
                    t "t-thanks, aang."
                    t "you... you're..."
                    t "....."
                    show tols tols14 with dissolve
                    t "you're a..."
                    t "...a blockhead!"
                    t "let's go!"
                    hide tols with dissolve
                    y "*sigh*"
                    y "she acts like such a kid sometimes."

    $ bk3_day = False
    jump love_bk3_village_background

label earthtraining5:
    y "sure."
    t "good stuff!"
    t "alright, twinkletoes..."
    t "we need to get you out of your comfort zone."
    y "....you think this is my comfort zone?"
    show toi_blink with dissolve
    t "i think being in the village makes you think you can relax."
    y "woman, this is some of the least relaxed i have ever been."
    y "there isn't even any air conditioning."
    show toi toi09
    hide toi_blink
    with dissolve
    t "what's air conditioning?"
    y "okay, see! that's what i'm talking about!"
    show toi toi06 with dissolve
    t "come on, wuss."
    t "you're not gonna learn earthbending by being light on your feet."
    t "you gotta put in the work."
    y "ugh, that's the worst sentence i've ever heard."
    t "you gotta to put in the work."
    y "well, don't repeat it!"
    y "fine, where are we going?"
    show toi toi04 with dissolve
    t "up in the mountains by the lake."
    y "the... aw, man."
    t "suck it up, fancy dancer."
    y "fancy... dancer?"
    t "yeah, because of all your fancy lightfooted dance moves when you fight."
    show toi toi07
    show toi_blink
    with dissolve
    t "pfft. like a wuss."
    y "sometimes you are mean to me, and i don't appreciate it."
    hide toi_blink with dissolve
    t "come on."
    hide toi with dissolve
    y "uughhhhhhhhhhhhhhhhh..."
    y "fine!"
    y "i don't like the look of that sky, though."
    y "......"
    y "i'm sure it'll be fine."
    scene black with fade
    t "come on!"


    show flicker_lightning
    $ renpy.pause(0.4)
    "a sudden downpour makes you feel like you're standing in lake laogai instead of beside it."
    y "fuck all the ducks!"
    y "what the fuck is this weather!?"
    y "it's been sunny every fucking day!"
    y "and then we leave the damn village-"
    y "not my idea, by the way!"
    t "quit whining!"
    t "we need to find some shelter!"
    y "hold on, i see a cave!"
    y "come on!"
    "you grab toph by her hand and pull her to a small cave on a nearby hill."
    hide flicker_lightning
    scene black
    show tocs_bg 0:
        xpos 0
    with fade
    show ctc
    pause
    hide ctc
    y "well, that was sudden."
    y "......."
    y "you know, it's pretty when you're not in it."
    y "damn, i'm drenched."
    y "how about you, toph?"
    show tocs_bg:
        linear 5 xpos -250
    $ renpy.pause(5)

    t "i feel like I fell in the lake."
    t "....again...."
    y "still sorry about that."
    t "And that rain is freezing cold, too!"
    y "i know...."
    y "it's not lost on me that i was complaining about air conditioning and then we get freezing rain."
    t "sounds like the spirits are out to get you."
    y "hah. right. what a joke. spirits manipulating my life. hah."
    y "......"
    t "ugh... stupid weather..."
    t "If you hadn't pulled me here, I could've made us some shelter right where we stood, you know."
    y "Fuck... you're right..."
    y "i forget we can earthbend."
    t "ahem."
    y "that {i}you{/i} can earthbend."
    y "oh well, we're here now."
    y "and it doesn't look like the rain is going to let up anytime soon."
    y "Guess we're stuck here for the moment."
    show tocs_face angry
    t "Booooring!!!"
    y "We can tell each other scary stories around a campfire."
    hide tocs_face angry
    t "what campfire?"
    show tocs_face ashamed
    t "I'm so wet and cold, i'd eat a dick for a little warmth."
    y "......."
    y "....hold that thought."
    "You dash outside and break off branches from the closest bush you can find and run back inside again."
    y "There!"
    show tocs_bg 0:
        xpos -250
    show expression "bk3/toph/cave/firewood.png" with Dissolve(2.0)
    $ renpy.pause(1.0)
    show ctc
    pause
    hide ctc
    y "a little firebending and we'll be nice and comfy in no time."
    t "what are you talking about?"
    t "you haven't learned to firebend yet."
    y "uh.... let's worry about that in a minute."
    y "first things first."
    "You start taking off all your clothes."
    t "what are-"
    show tocs_face angry
    t "Hey! What do you think you're doing!?"
    y "My clothes are wet and chilling me to the bone, so I'm taking them off."
    hide tocs_face angry
    y "I just got another dose of that rain while getting wood for the fire."
    y "you know, like... thirty seconds ago?"
    show tocs_face angry
    t "that doesn't mean you can just strip in front of me!"
    y "....why not?"
    y "It's not like you can see my junk, can you?"
    show tocs_face ashamed
    t "....it's just...."
    y "Yeah?"
    hide tocs_face
    t ".....fine....."
    y "Why don't you take off your clothes too?"
    y "We can dry them and warm ourselves by the fire, once I get it going."
    show tocs_face angry with hpunch
    t "i'm not going to get naked in front of you!!"
    y "first: ow, you're loud."
    y "and second: not naked, just keep your underwear on."
    y "You're not going to get warm if you keep wearing all of that."
    y "hell, you're likely to get hypothermia."
    show tocs_face ashamed
    t "...I...ehmm..."
    t "....I'm not wearing underwear...."
    y "....."
    t "....."
    y "....kinky."
    show tocs_face angry
    t "it's not like that!!"
    show tocs_face ashamed
    t "I didn't have anything clean this morning so...."
    y "Pfffft. so what?"
    y "If you sit like you're sitting now, I won't be able to see anything, naked or not."
    y "And as for your chest...."
    y "I've got nipples too, you know."
    y "But hey, fine. Do whatever you're comfy with."
    t "*sigh...*"
    t "Turn around."
    y "Huh?"
    t "Just turn around until I say you can turn back again."
    y "Okay."
    hide expression tocs_face
    show expression "#000" with Dissolve(3.0)
    t "You can turn back again."
    hide expression "#000"
    show tocs_bg 1:
        xpos 0
    show tocs tocs02
    with Dissolve(2.0)
    show ctc
    pause
    hide ctc
    t "You can't say anything about this to anyone....ever..."
    y "Sure."
    show tocs_face angry
    t "{size=40}...ever!!{/size}" with hpunch
    y "My lips are sealed."
    hide text
    hide tocs_face angry
    t "so, how about that fire?"
    t "It's nice losing those wet clothes, but it's still cold."
    y "One nice warm fire coming up."
    y "I'll hang the clothes from some branches so they'll dry faster."
    show expression "bk3/toph/cave/clothes_hang_1.png"
    show expression "bk3/toph/cave/clothes_hang.png" with Dissolve(2.0)
    show ctc
    pause
    hide ctc
    y "the wood is a bit wet so it's going to be smoky at the start."
    show tocs_smoke with Dissolve(2.0):
        xpos 400 ypos -30
    show ctc
    pause
    hide ctc
    t "*cough* *cough*"
    y "Just a few more moments now....."
    show expression "#d3d3d3":
        alpha 0.0
        linear 6 alpha 0.6

    t "It *cough* is only getting worse! *cough*"
    t "Can't you airbend this away?!"
    t "Before we suffocate?"
    y "Oh, crap, of course, we need to get some airflow going."
    y "I'll try earthbending a makeshift chimney above the fire."
    y "Help me out if it looks like I'm bringing this cavern's ceiling down on our heads."
    t "sure *cough* just hurry up *cough*...."
    play sound "audio/earthquake.mp3"
    with sshake
    hide expression "#d3d3d3" with Dissolve(4.0)
    y "It's clearing up!"
    hide tocs_smoke
    show tocs_fire
    with Dissolve(2.0)

    y "Boom, baby!!! Fire!"
    show tocs tocs03
    show ctc
    $ renpy.pause()
    hide ctc
    t "ooohh, that's better!"
    t "I can already feel the cold leaving my body."
    y "(she really does have a cute little body.)"
    y "(wish i could just lean forward and pinch that nipple...)"
    t "And you even used earthbending instead of airbending to solve the smoke problem!"
    t "I guess this day won't be a waste after all!"
    t "Good job, twinkletoes!"
    y "Well, I'm supposed to master earthbending so... "
    y " (not to mention I can't even airbend a feather off the ground....)"

    t "so... how come you can firebend?"
    y "oh. right."
    y "well...."
    y "uh...."
    t "i bet it was what you learned from jeong jeong, right?"
    y "who?"
    y "i mean... yes?"
    t "that fire nation deserter that taught you stuff before we met?"
    t "you burned katara and made zhao destroy his fleet?"
    y "....yes."
    y "i lead a very active life...."
    y "apparently."
    t "you once told me that you swore to never firebend again, though..."
    t "what made you change your mind?"
    y "a life-or-death situation."
    t "i don't think this is a life-or-death situation."
    y "it might be a life-or-death situation."
    t "yeah... but i don't think it is a life-"
    y "stop saying \"life-or-death situation\"."
    y "and quit arguing with me or i'll put this fire out and build my own."
    y "with blackjack. and hookers."
    show tocs_face ashamed with dissolve
    t "what?"
    y "speaking of, it's too bad I don't have a deck of cards with me."
    hide tocs_face ashamed with dissolve
    t "Why, you wanna play solitaire?"
    y "Nah, I was more thinking along the lines of playing reverse strip poker!"
    y "you know... where you have to put clothes on?"
    y "....because we're already naked?"
    y "....."
    y "laugh at my jokes, damn it!"
    t "....card games aren't really my thing...."
    y "Oh... right... sorry, I keep forgetting."
    y "wanna tell some stories instead?"
    t "Sure..."
    show expression "#000" with Dissolve(5.0)
    show text "{color=#ffffff}you and toph share some stories as time passes and the fire slowly dies out.{/color}"
    $ renpy.pause()

    show expression "bk3/toph/cave/firewood_burned.png"
    hide tocs_fire
    show tocs_bg 2
    hide tocs_light
    show tocs tocs04
    show tocs_smoke:
        alpha 0.4
        xpos 400 ypos -30

    hide expression "#000"
    hide text
    with Dissolve(5.0)
    $ renpy.pause()
    t "and that's the last time i masturbated with the heavyweight championship belt-"
    t "oh, hey! It stopped raining!"
    y "Nice, and I think our clothes are dry too."
    y "(i guess Toph's forgotten we're still naked...)"
    hide tocs_smoke with Dissolve(2.0)
    menu:
        "let her know you have a full view":
            y "Uhh...."
            t "What is it?"
            y "I'm happy to see you relax yourself around me, but...."
            y "I'm seeing it all, right now."
            show tocs_face realize with dissolve
            show ctc
            pause
            hide ctc
            y "...and can't look away."
            show tocs_face angry
            show tocs tocs05 with hpunch
            t "Aaaaaah! I knew this was a mistake!"
            t "you should've told me!!!"
            y "I did! Just now!"
            "Toph angrily gets up, grabs her now dry clothes, and dashes out of the cave."
            hide expression "bk3/toph/cave/clothes_hang.png"
            hide tocs_face
            hide tocs
        "Enjoy the view some more":

            t "Finally! Time to finish today's training!"
            y "...uh-huh..."
            t "My bum feels all sore from sitting here so long."
            y "...uh-huh..."
            t "Are you really listening to what I'm saying?"
            y "...uh-huh..."
            t "If you're really listening say something besides uh-huh."
            y "...uh-huh..."
            show tocs_face angry
            t "aaang!!" with hpunch
            y "Wha..what is it?!"
            show tocs_face ashamed
            t "Aang... why has your heartbeat been increasing the last minute or so...?"
            y "It has?"

            t "Yeah, I can easily sense it with my earthbending when you're sitting naked..."
            t "....on the ground...."
            show tocs_face realize with dissolve
            "a look of realization suddenly appears on toph's face."

            t "......"
            show ctc
            pause
            hide ctc
            show tocs tocs05 with hpunch
            show tocs_face angry
            t "You pervert!!"
            t "You... you are... ogling me!"
            y "Wha... no... okay, yes..."
            y "I mean, I just didn't want to embarrass you{size=9}....and perhaps take a longer look....{/size}"
            "Toph angrily gets up, grabs her now dry clothes, and dashes out of the cave."
            hide expression "bk3/toph/cave/clothes_hang.png"
            hide tocs_face
            hide tocs

    y "well... shit."
    y "still, any day you see tits is a good day."
    $ earthbending = 6
    scene black with dissolve
    "the two of you head back to town."
    "toph is pointedly quiet."
    $ bk3_day = False
    jump love_bk3_village_background

label earthtraining6:
    hide screen earth_money_date
    show toi toi02 with dissolve
    t "hey! i had an idea!"
    y "it's not another wild animal is it?"
    show toi toi09 with dissolve
    t "well... that was mostly an accident..."
    show toi toi08
    show toi_blink
    with dissolve
    t "but i was sure you could handle it."
    y "well, I wasn't...."
    show toi toi07
    hide toi_blink
    with dissolve
    t "ah, don't be such a baby, you did great!"
    t "you've got stuff, remember?"
    y "i have a lot of stuff, all right."
    ym "built up like you would not believe-"
    show toi_blink with dissolve
    t "whatever."
    show toi toi04 with dissolve
    t "you did so well with the mooselion, I think it's time for something harder."
    y "....do we have to?"
    hide toi_blink
    show toi toi06
    with dissolve
    t "there you go whining again!"
    y "alright, fine...."
    show toi toi04

    t "great!"
    show toi toi08 with dissolve
    t "here's a boulder."
    show earth_attack1 with moveintop
    play sound "audio/thud.mp3"
    with vshake
    y "this is... in your house..."
    t "lift the boulder, aang!"
    show blackveil with dissolve
    "click on the boulder to lift it all the way to the top!"
    hide blackveil with dissolve
    t "go!"
    $ tug_points=-420
    $ tug_plus=40
    $ tug_max_point=75
    $ clicked = True
    hide earth_attack1
    call screen earth_clicker

    label earth_clicer_win2:
        hide screen earth_clicker
        show toi toi07 with dissolve
        t "whoa! nicely done!"
        y "you're a monster."
        show toi_blink with dissolve
        t "pfft. you baby."
        hide toi_blink
        show toi toi09
        with dissolve
        t "um."
        t "i'm... supposed to give you positive reinforcement now, right?"
        y "pretty sure."
        t "....right. okay. um...."
        t "....."
        t "what do you want?"
        t "a... high-five?"
        $ earthbending = 6
        menu:
            "gimme a low-five!":
                y "down low!"
                show toi toi03 with dissolve
                t "yeah, get it!"
                play sound "audio/slap.mp3"
                with flash
                t "nice!"
                show toi toi02 with dissolve
                y "fuck yeah!"
                y "now...."
                y "lemme grab your boobs!"
                show toi toi09 with dissolve
                t "oh... um..."
                t "I don't... think that's a good idea."
                y "really?"
                y "it's not like we haven't been naked around each other."
                show toi toi06 with dissolve
                t "those were accidents!"
                y "okay, okay, fair enough."
                y "i just... like you, and think you're cute."
                show toi toi09 with dissolve
                t "i... well..."
                t "we'll... talk about it later, maybe..."
                y "oh-ho."
                show toi toi04 with dissolve
                t "shut up."
                t "....and you did good today."
            "lemme grab your boobs!":

                show toi toi09 with dissolve
                t "oh... um..."
                t "I don't... think that's a good idea."
                y "really?"
                y "it's not like we haven't been naked around each other."
                show toi toi06 with dissolve
                t "those were accidents!"
                y "okay, okay, fair enough."
                y "i just... like you, and think you're cute."
                show toi toi09 with dissolve
                t "i... well..."
                t "we'll... talk about it later, maybe..."
                y "oh-ho."
                show toi toi04 with dissolve
                t "shut up."
                t "....and you did good today."

        t ".........."
        y "what?"
        hide toi with dissolve
        show tonf tonf20 with Dissolve(1)
        y "...what?"
        y "Is there something on my fa-"
        show tonf tonf22 with dissolve
        play sound "audio/kiss.mp3"
        with pflash
        "toph gives you a quick peck to your surprise."
        show tonf tonf23 with dissolve
        t "...."
        show tonf tonf20 with dissolve
        t "see ya!"
        hide tonf with Dissolve(1)
        y "that was... unexpected."
        y "I guess she's starting to warm up to me."
        y "...or accept how she feels..."

    $ bk3_day = False
    $ earthbending = 7
    jump love_bk3_village_background

label earthtraining7:
    hide screen earth_money_date
    show toi toi02 with dissolve
    t "alright, then."
    t "today we're gonna work on your sensitivity."
    y "what? i'm not sensitive."
    show toi toi09 with dissolve
    t "no, i-"
    y "i mean, okay, maybe i'm a little defensive sometimes-"
    t "that's not-"
    y "-but who isn't a little mad at their parents, right?"
    y "it's like, i'm {i}trying{/i}, dad, but maybe i'm just not gonna be that great at sports!"
    show toi toi04 with dissolve
    t "you... what?"
    y "and then there you are, all sporty and capable, just bringing on home how even a girl-"
    show toi toi07 with dissolve
    t "{i}no{/i}, you {i}nerd{/i}."
    t "i meant your {i}actual{/i} senses."
    y "....."
    y "oh."
    y "i... might have been projecting."
    t "maybe a little, huh?"
    y "....."
    y "actually, all things considered, my relationship with my parents is pretty-"
    show toi toi06 with vshake
    t "pay attention!"
    y "yes, sir, dad, sir!"
    y "........."
    y "....i might need a therapist."
    show toi toi09 with dissolve
    t "....right...."
    t "let's... move on."
    show toi toi06 with dissolve
    t "i worry about you in those tunnels."
    y "what? why?"
    t "because it's a maze down there."
    y "you don't say."
    t "and relying on your eyes alone is limiting you down there."
    t "you need to be able to see with your feet."
    y "that... is not how things work."
    t "it's how i work."
    y "well, you're... a wizard or something."
    y "I'm fine."
    t "no! this is important!"
    t "i'm going to blindfold you and we're gonna hone your senses."
    y "aw, but i'm tired, mom..."
    show toi toi08 with dissolve
    t "don't make me spank you."
    y "....."
    y "should that have put me at half-mast?"
    y "...because i worry about what that means."
    show toi toi07
    show toi_blink
    with dissolve
    t "shut up."
    hide toi_blink
    show toi toi02
    with dissolve
    t "i'm gonna put this blindfold on you."
    hide toi with dissolve
    show tonf tonf21_1 with dissolve
    t "ready?"
    y "do i have a choice?"

    t "no."
    show tonf tonf21
    t "now stand still."
    y "....."
    t "um... i can do it..."
    y "do you need help?"
    t "is this... right?"
    y "no."
    y "put your hands down, i got it, i got it."
    y "blind little midget..."
    show black with moveintop
    y "there."
    y "I can't see shit."
    t "good."
    t "now stamp your foot."
    y "okay..."

    hide tonf
    play sound "audio/thud.mp3"
    with vshake
    y "...."
    y "was something supposed to happen?"
    t "focus!"
    t "the vibrations hit objects and rebound."
    t "you can tell distance and shape by the ripple formation."
    y "this seems like a lot of work..."
    t "again!"
    play sound "audio/thud.mp3"
    with vshake
    y "how was-"
    t "again!"
    play sound "audio/thud.mp3"
    with vshake
    t "more!"
    y "my foot hurts!"
    y "how long am i going to do this?"
    t "......"
    t "...you need encouragement, right?"
    y "uh... yes?"
    t "okay, hold on."
    y "......"
    y ".........."
    y "toph?"
    t "alright..."
    t "i'm naked."
    y "really!?"
    y "can i take off the blind-"
    t "no!"
    t "see me naked with your feet, or not at all."
    y "...i can't tell if i hate this game or not."
    show text "{color=#ffffff}you spend the rest of the day working with toph..." with dissolve
    show ctc
    pause
    hide ctc
    hide text with dissolve
    t "again!"
    y "rrr...."
    play sound "audio/thud.mp3"
    with vshake
    show toph_ripples
    $ renpy.pause(.3,hard=True)
    hide toph_ripples with dissolve
    y "whoa."
    t "what?"
    y "i think... i think i felt... saw... something."
    t "stay with it!"
    play sound "audio/thud.mp3"
    with vshake
    show toph_ripples
    $ renpy.pause(.7,hard=True)
    hide toph_ripples with dissolve
    y "...."
    y "okay, i definitely got something that time."
    y "hold on...."
    play sound "audio/thud.mp3"
    with vshake
    show toph_ripples2
    $ renpy.pause(.7,hard=True)
    y "heh."
    t "did it work?"
    y "yeah."
    y "i see you."
    t "....."
    play sound "audio/thud.mp3"
    hide toph_ripples2
    with vshake
    y "ow!"
    y "why did you hit me?"
    t "you were being a perv!"
    y "this... this was your idea!"
    t "who remembers?"
    y "....what!?"
    t "okay, i'm dressed again."
    t "take off the blindfold."
    y "well, that was an annoying fucking-"
    scene black
    scene bg_bk3_tophome_night
    show tonf tonf51
    with dissolve
    y "-tease."
    show ctc
    pause
    hide ctc
    y "i thought..."
    t "you... did well."
    t "you earned a... a look."
    t "if you really did want to... to see."
    y "i definitely do."
    t "well..."
    t "okay."
    show tonf tonf17 with dissolve
    t "you did well, aang."
    t "i think you're strong enough now to go a little further in the tunnels."
    t "um... good luck."
    y "do you want to talk about what just-"
    play sound "audio/thud.mp3"
    scene toph_home_outside
    with sshake
    "toph pushes you out and slams the door."
    "you hear heavy breathing on the other side."
    y "...."
    y "i'm going to take this as a good thing."
    y "...that tease."
    play sound "audio/win2.mp3"
    $ maze_sections = 1
    $ earthbending = 8
    "you became stronger!"
    scene black with dissolve
    "you head home for the night."
    jump love_bk3_next

label earthtraining8:
    hide screen earth_money_date
    show toi toi02 with dissolve
    t "you're delicate on your feet, twinkletoes, but when it comes to earthbending, you've got no finesse."
    menu:
        "dick joke":
            y "I'm about to be finesse dick in your mouth."
        "dad joke":
            y "that's why i'm glad we're finesse session in."
    show toi toi06 with dissolve
    t "....."
    t "you know how sometimes we get along?"
    y "....yes?"
    t "well, this is turning into not one of those times."
    y "my bad."
    show toi_blink with dissolve
    t "this stuff is important, aang."
    t "if you want to goof around, don't do it during my training time."
    y "sorry..."
    hide toi_blink with dissolve
    t "i'm serious, aang."
    t "next time you joke around like during training, i'm gonna be..."
    show toi toi07 with dissolve
    t "...finesse foot in your ass."
    y "....."
    t "eh? eh?"
    y "....."
    t "pretty good, right?"
    y "you know how sometimes we get along?"
    show toi_blink with dissolve
    t "don't be a baby."
    t "i'm hilarious."
    show toi toi04
    hide toi_blink
    with dissolve
    t "jokes aside, today we're gonna work on shaping earth into actual usable shapes instead of weird lumpy blocks."
    y "okay, what first?"
    t "let's start with a big bowl."
    y "How big?"
    t "the size of this house."
    show toi toi06 with dissolve
    t "you're not gonna make anything that leaks on my watch!"
    y "Um... we're gonna do it outside, though, right?"
    t "obviously."
    scene black with dissolve
    "you spend the day learning how to shape earth into large basins and other forms."
    $ earthbending = 9
    $ bk3_day = False
    jump love_bk3_village_background

label earthtraining9:
    t "okay, we've worked on making things with earth..."
    t "now we need to work on turning things back {i}into{/i} earth."
    t "we'll start small with this one."
    y "will i be able to clear the rubble and rebuild my house after this?"
    show toi toi09 with dissolve
    t "let's... focus on one thing at a time."
    show black with dissolve
    "you work on deconstructing earth-made structures."
    "a little."
    hide black
    show toi toi04
    with dissolve
    y "well?"
    y "how'd i do?"
    show toi_blink with dissolve
    t "pretty well, i gotta admit."
    hide toi_blink with dissolve
    t "you're not ready for anything as large-scale as your house project, but it's a good start."
    y "sweet!"
    y "pretty soon i'll have my house back!"
    show toi toi09 with dissolve
    t "do...."
    t "...do you really want that so badly?"
    y "what? i like my own space."
    t "I've... enjoyed your company the last few nights."
    y "me, too! mostly..."
    t "i thought..."
    show toi_blink with dissolve
    t "never mind."
    y "don't make a big thing out of it, i'm not going anywhere."
    t "sure."
    show toi_tears with dissolve
    t "i'll see you later, aang."
    y "toph..."
    hide toi_tears
    hide toi_blink
    hide toi
    with dissolve
    y "....."
    y "*sigh...*"
    y "toph..."
    $ earthbending = 10
    $ bk3_day = False
    jump love_bk3_village_background

label earthtraining10:
    t "come on, aang."
    t "It's time."
    y "time?"
    t "yeah, we're gonna get you ready to rebuild your house."
    y "woo."
    t "...."
    t "alright, we've worked on how to deconstruct smaller structures..."
    t "now, you're gonna learn how to do it in bulk."
    y "i'm ready."
    show toi toi06 with dissolve
    t "bend your knees!"
    t "lean forward!"
    t "put your butt into it!"
    y "what?"
    show black with dissolve
    "you work with toph to strengthen your earthbending."
    hide black
    show toi toi04
    with dissolve
    y "whew."
    y "that was a workout."
    t "but you're ready."
    y "you think?"
    t "yeah."
    show toi toi09 with dissolve
    t "but..."
    t "you should attempt it in the morning, when you've got your strength back."
    y "yeah, i'm pooped."
    show toi toi07 with dissolve
    t "good luck!"
    $ bk3_day = False
    $ earthbending = 11
    jump love_bk3_village_background

label earthtraining19:
    scene black
    scene expression "ebackgrounds/cliff.jpg"
    show expression "bk3/toph/melonlord/melon_body.png"
    with fade
    show ctc
    pause
    hide ctc
    y "uh."
    y "sooo..."
    y "what are we supposed to do here?"
    y "Toph?"

    show toxb toxb01 with dissolve
    y "ah!"
    y "you're... scaring me..."
    t "You're supposed to take out the Firelord and bring balance to the nations, right?"
    y "Eventually..."
    y "not... not today though, right?"
    t "today is the training for that!"
    y "does it have to be?"
    t "Just think of that scarecrow as the firelord!"
    y "...alright."
    y "that's... easier than fighting him today for sure."
    y "where's his head?"
    t "it turns out I could only find a melon for its head..."
    t "so you're going to fight..."

    show toxb toxb02 with Dissolve(1.5)
    t "{size=+10}the melonlord!!"

    show expression "bk3/toph/melonlord/melon_head.png":
        xpos 1200 ypos 1000
        linear 2.0 xpos 440 ypos -100
        easein 1.0 xpos 440 ypos 30

    t "Muahahaha!!"
    t "Bow before my might!"
    y "Wow, that's an excellent evil genius laugh, Toph."
    show toxb toxb03 with Dissolve(1.5)
    t "Don't call me Toph!"
    t "call me...."
    show toxb toxb02
    t "Melonlord!!" with hpunch

    y "I thought that scarecrow was the melonlord?"
    show toxb toxb01 with dissolve
    t "He is!"
    t "It's your objective to destroy him while avoiding the burning rocks!!"
    y "i know i'm going to regret asking this, but..."
    y "...burning rocks?"
    t "The ones I'm gonna throw at you."
    y "the ones you're gonna {i}what{/i}?!"
    t "This way I can make sure you're not secretly holding back."
    y "wait, hold on..."
    t "you're gonna have to go all out if you want to not only beat him, but survive it."
    y "............."
    ya "{size=+10}Burning rocks?!" with hpunch
    t "Yeah, I covered them with tar and will set them on fire with a torch."

    ya "Can't we do normal training instead?!"

    t "No! Prepare yourself!"
    ya "To die?!?"
    hide toxb with dissolve

    show toxb_rockburn_1:
        xpos 500

    y "Fuck you, firelord!"
    y "Your goatee is stupid!"
    hide toxb_rockburn_1

    show toxb toxb01 with Dissolve(1.5)
    t "yeah!"
    t "hit him with some psychological warfare!"
    t "Good idea!"
    hide toxb with Dissolve(1.5)

    y "And I'm going to fuck your daughter!"
    y "Without protection!"


    show toxb toxb03
    t "Wait... what?" with hpunch
    y "It's just psychological warfare."
    y "Talking that way about his little princess is going to make him blind with rage and mess up his aim."
    t "I guess that could work...."

    hide toxb with Dissolve(1.5)

    show toxb_rockburn_1:
        xpos 600

    y "Where was I...."
    y "ehm... i'll slap her big soft tits with my hard-"
    hide toxb_rockburn_1
    show toxb toxb04 with hpunch
    t "No more psychological warfare!"
    t "It's immature and probably won't work anyway!"



    scene black with Dissolve(1.5)
    show text "You spend the rest of the afternoon barely avoiding burning rocks and finally manage to take down the mellonlord."
    $ renpy.pause()

    show expression "ebackgrounds/cliff.jpg"
    show expression "bk3/toph/melonlord/melon_body.png"
    show expression "bk3/toph/melonlord/melon_head.png":
        xpos 440 ypos 30
        easeout 3.0 ypos 400 rotate 900
        linear 3.0 xpos 1300 ypos 500 rotate 1900
    with Dissolve(2.0)
    $ renpy.pause(4.0)

    show toxb toxb01
    t "Well done!"
    t "See?!"
    t "you don't need stupid psychological warfare to get results!"

    y "*pant*... I can't... *pant*... feel my legs..."
    t "Don't be a pansy, Aang!"
    t "walk it off!"
    show toxb toxb03 with dissolve
    t "...."
    t "Hmmm... well maybe you've actually pushed yourself to the limit..."
    t "or past it..."
    t "hmmmmm...."
    hide toxb with dissolve
    y "What are you doing?"
    show toxb toxb05 with Dissolve(1.5)
    t "Shedding a few clothes."
    show ctc
    pause
    hide ctc
    t "you did a good job, and i'll... give you a pretty view as your reward."
    t "besides, you look like you're about to pass out."
    t "maybe this will put some life back into your lower body."
    y "it's working..."
    t "then maybe {i}this{/i} can can help you stand..."
    show toxb toxb06 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "....{i}something{/i} is standing."
    t "yeah?"
    t "you like when i pinch my nipples for you?"
    t "you like these little titties, don't you?"
    t "these perky little nipples?"
    y "spirits help me, i do."
    show ctc
    pause
    hide ctc
    show toxb toxb08 with Dissolve(1.5)
    t "My chest isn't very big, and maybe other girls have more..."
    t "but i like to think being petite has it's own allure."
    t "besides, you can play with these whenever you like."
    t "that's a hard deal to get elsewhere..."
    show ctc
    pause
    hide ctc
    y "can you... pinch them some more?"
    t "oh?"
    show toxb toxb100
    t "like this?"
    t "*mmmmmm....*"
    y "hell yes."
    t "mmm... it feels good..."
    t "wanna come get them?"
    y "...if I could still walk I'd be all over you five minutes ago."
    t "Good!"
    t "This is just me testing whether you're really exhausted or not."
    t "And it does look like you gave it your all."
    show ctc
    pause
    hide ctc
    hide toxb with Dissolve(1.5)
    t "Well done, Aang."
    t "I'm impressed."
    show toxb toxb01 with Dissolve(1.5)
    t "Earthbending is about giving it your all and not holding anything back."
    t "No doubt or second thoughts."
    t "Just pure, focused, unwavering intent... and you really outdid yourself!"
    y "Aaaawh... you got dressed again."
    t "You deserve some rest."
    t "Take the rest of the afternoon off."
    t "You deserve it."
    $ bk3_day = False
    $ earthbending = 20

    jump love_bk3_village_background

label katara_party_fuck1:
    show toki_smile with dissolve
    k3 "oh! aang!"
    k3 "I have a surprise for you!"
    k3 "wait right here!"
    hide toki_smile
    hide toki
    with dissolve
    y "...okay..."
    y ".............."
    y "............................"
    scene black with dissolve
    "you wait for a while...."
    scene inside_hospital with dissolve
    y "hey, are you coming out?"
    y "because i have things to-"
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    show tokp tokp20 with Dissolve(1.5)
    y "...well, fuck me."
    k3 "maybe..."
    k3 "did you have fun with toph?"
    y "sure."
    k3 "I'm okay with that, but don't forget your number one girl needs some attention, too."
    show tokp tokp21
    k3 "so... what were you saying when i walked out?"
    y "um.... fuck me?"
    k3 "mmmmm...."
    k3 "deal."
    show tokp tokp22 with Dissolve(1.5):
        ypos 400
        easeout 6 ypos -50
        easein 4 ypos 400
    show ctc
    pause
    hide ctc
    k3 "like the view?"
    k3 "it's all yours..."
    k3 "oh no, am i your playground now?"
    k3 "how terrible."
    k3 "well... before we begin..."
    k3 "do you have any requests?"
    menu:
        "small":
            $ tokp_titsize = 'small'
        "medium":
            $ tokp_titsize = 'medium'
        "big":
            $ tokp_titsize = 'big'

    hide tokp
    show tokp tokp00 with Dissolve(1.5)
    k3 "wanna saddle up, cowboy?"
    show ctc
    pause
    hide ctc
    y "what? are you a horse now?"
    k3 "i'm just a simple, high-class girl... looking to get ridden."
    k3 "don't tell my papa."
    show tokp tokp01
    k3 "especially don't tell him... how wet i am right now."
    show ctc
    pause
    hide ctc
    k3 "my cunt is on fire, baby..."
    k3 "Mmmm...."
    k3 "you gonna fill this little cunt?"
    k3 "wanna make me cry?"
    y "give me a better view."
    y "open that pussy."
    k3 "if that's what you want..."
    show tokp tokp02
    show ctc
    pause
    hide ctc
    k3 "is this what you like? making me spread my pussy?"
    k3 "me on display?"
    menu:
        "get a taste first":
            y "I want to lick those pretty lips."
            show expression "bk3/katara/party/lewd.png":
                xpos 418 ypos 111
            show tokp_lick:
                xpos 430 ypos 320
            k3 "aahhh....ohhhhh..."
            k3 "soo... hot..."
            y "you... taste... so... fucking... good..."
            k3 "ahh... ngh... yes..."
            k3 "don't stop... don't ever stop..."
            y "these are your best lips."
            k3 "mmmmm.... that's it, avatar..."
            k3 "lick my little kitty...."
            hide tokp_lick
            hide expression "bk3/katara/party/lewd.png"
        "straight to the dicking!":

            pass

    show expression "bk3/katara/party/solodick.png" with Dissolve(2.0):
        xpos 390 ypos 600
        linear 2 ypos 300
    y "i can't wait any more."
    k3 "don't, baby. don't wait."
    k3 "i've been dying for your cock."

    show tokp tokp04
    k3 "i was so wet thinking about you fucking toph after the party."
    y "i... didn't, though..."
    k3 "didn't stop me thinking about it..."
    k3 "and jilling off behind a cart."

    hide expression "bk3/katara/party/solodick.png"

    show tokp tokp05 with dissolve
    show ctc
    pause
    hide ctc
    k3 "mmm... yes... i'm a little tight right now..."
    k3 "I haven't been fucked since... well..."
    k3 "you know."
    y "you... haven't fucked aang since..."
    k3 "well he's just not you."
    y "hold on, do you know-"
    k3 "hush, and put it inside me."

    show tokp tokp03
    show ctc
    pause
    hide ctc
    k3 "ahhh...."
    k3 "Mmm... yes, baby..."
    k3 "oh, fuck yes... i've been waiting... ah... for this..."
    k3 "work my little cunt, baby..."
    k3 "stretch that wet, slurping pussy-"
    show tokp tokp100
    k3 "ahh!"
    show ctc
    pause
    hide ctc
    k3 "ah! oh! fu-fuck!"
    k3 "eas-easy! ah!"
    k3 "yess.... oh, fuck me!"
    k3 "fuck me, aang!"
    k3 "fill up your whore!"
    k3 "put your seed in my warm, tight pussy!"
    k3 "i know you need it! i know you need it!"
    k3 "let it out! let me take it!"
    $ katara_party_fuck = True
    menu:
        "cum inside":
            show tokp tokp08 with Dissolve(1.0)
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            show tokp tokp06
            with flash
            y "unngh..."
            k3 "mmm.... so warm... deep up in my pussy..."
            show ctc
            pause
            hide ctc
            show tokp tokp07
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "filling me... coating me..."
            k3 "i love fingering myself while stuffed and leaking your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "you head home for the night."
            jump love_bk3_next
        "cum outside":

            show tokp tokp02 with Dissolve(1.0)
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/katara/party/spermout1.png"
            y "unngh..."
            k3 "mmm.... so warm... cover me..."
            play sound "audio/splurt1.ogg"
            show expression "bk3/katara/party/spermout2.png"
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "coating me... marking me..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/katara/party/spermout3.png"
            y "hngh..."
            k3 "mmmm... thank you."
            k3 "i love fingering myself while drenched in your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "you head home for the night."
            jump love_bk3_next
        "piss on me katara":

            k3 "Wha-what?"
            y "Make me golden!"
            k3 "Okay, but don't forget you asked me!"
            show tokp tokp08 with Dissolve(1.0)
            show tokp_piss:
                xpos 370 ypos 100
            k3 "aanhhh....."
            y "yes! cover me, whore!"
            k3 "mmmnn... fuck...."
            show ctc
            pause
            hide ctc
            y "I'm gonna cum!"
            k3 "ahhh... cum.... nngh.... cum, baby...."
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            hide tokp_piss
            show tokp tokp06
            with flash
            y "unngh..."
            k3 "mmm.... so warm... deep up in my pussy..."
            show ctc
            pause
            hide ctc
            show tokp tokp07
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "filling me... coating me..."
            k3 "i love fingering myself while stuffed and leaking your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "you head home for the night."
            jump love_bk3_next

label katara_party_fuck2:
    y "wanna fuck?"
    show toki_smile with dissolve
    k3 "of course!"
    k3 "let me dress up for you!"
    hide toki_smile
    hide toki
    with dissolve
    y "........"
    k3 "almost ready!"
    y "........."
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    show tokp tokp20 with Dissolve(1.5)
    y "...well, fuck me."
    show tokp tokp21
    k3 "that's the plan."
    show tokp tokp22 with Dissolve(1.5):
        ypos 400
        easeout 6 ypos -50
        easein 4 ypos 400
    show ctc
    pause
    hide ctc
    k3 "like the view?"
    k3 "it's all yours..."
    k3 "but before we begin..."
    k3 "do you have any requests?"
    menu:
        "small":
            $ tokp_titsize = 'small'
        "medium":
            $ tokp_titsize = 'medium'
        "big":
            $ tokp_titsize = 'big'

    hide tokp
    show tokp tokp00 with Dissolve(1.5)
    k3 "wanna saddle up, cowboy?"
    show ctc
    pause
    hide ctc
    y "what? are you a horse now?"
    k3 "i'm just a simple, high-class girl... looking to get ridden."
    k3 "don't tell my papa."
    show tokp tokp01
    k3 "especially don't tell him... how wet i am right now."
    show ctc
    pause
    hide ctc
    k3 "my pussy's on fire, baby..."
    k3 "Mmmm...."
    k3 "you gonna fill this little cunt?"
    k3 "wanna make me cry?"
    y "give me a better view."
    y "open that pussy."
    k3 "if that's what you want..."
    show tokp tokp02
    show ctc
    pause
    hide ctc
    k3 "is this what you like? making me spread my pussy?"
    k3 "me on display?"
    menu:
        "get a taste first":
            y "I want to lick those pretty lips."
            show expression "bk3/katara/party/lewd.png":
                xpos 418 ypos 111
            show tokp_lick:
                xpos 430 ypos 320
            k3 "aahhh....ohhhhh..."
            k3 "soo... hot..."
            y "you... taste... so... fucking... good..."
            k3 "ahh... ngh... yes..."
            k3 "don't stop... don't ever stop..."
            y "these are your best lips."
            k3 "mmmmm.... that's it, avatar..."
            k3 "lick my little kitty...."
            hide tokp_lick
            hide expression "bk3/katara/party/lewd.png"
        "straight to the dicking!":

            pass

    show expression "bk3/katara/party/solodick.png" with Dissolve(2.0):
        xpos 390 ypos 600
        linear 2 ypos 300
    y "i can't wait any more."
    k3 "don't, baby. don't wait."
    k3 "i've been dying for your cock."

    show tokp tokp04
    k3 "i was so wet thinking about you fucking toph after the party."
    y "i... didn't, though..."
    k3 "didn't stop me thinking about it..."
    k3 "and jilling off behind a cart."

    hide expression "bk3/katara/party/solodick.png"

    show tokp tokp05 with dissolve
    show ctc
    pause
    hide ctc
    k3 "mmm... yes..."
    y "let me know if you need me to go slow or-"
    k3 "hush... and put it inside me."

    show tokp tokp03
    show ctc
    pause
    hide ctc
    k3 "ahhh...."
    k3 "Mmm... yes, baby..."
    k3 "oh, fuck yes... i've been waiting... ah... for this..."
    show ctc
    pause
    hide ctc
    k3 "work my little cunt, baby..."
    k3 "stretch that wet, slurping pussy-"
    show tokp tokp100
    k3 "ahh!"
    show ctc
    pause
    hide ctc
    k3 "ah! oh! fu-fuck!"
    k3 "eas-easy! ah!"
    k3 "yess.... oh, fuck me!"
    k3 "fuck me, aang!"
    k3 "fill up your whore!"
    show ctc
    pause
    hide ctc
    k3 "put your seed in my warm, tight pussy!"
    k3 "i know you need it! i know you need it!"
    k3 "let it out! let me take it!"
    menu:
        "cum inside":
            show tokp tokp08 with Dissolve(1.0)
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            show tokp tokp06
            with flash
            y "unngh..."
            k3 "mmm.... so warm... deep up in my pussy..."
            show ctc
            pause
            hide ctc
            show tokp tokp07
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "filling me... coating me..."
            k3 "i love fingering myself while stuffed and leaking your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            jump love_bk3_village_background
        "cum outside":

            show tokp tokp02 with Dissolve(1.0)
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/katara/party/spermout1.png"
            y "unngh..."
            k3 "mmm.... so warm... cover me..."
            play sound "audio/splurt1.ogg"
            show expression "bk3/katara/party/spermout2.png"
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "coating me... marking me..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/katara/party/spermout3.png"
            y "hngh..."
            k3 "mmmm... thank you."
            k3 "i love fingering myself while drenched in your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            jump love_bk3_village_background
        "piss on me katara":

            k3 "Wha-what?"
            y "Make me golden!"
            k3 "Okay, but don't forget you asked me!"
            show tokp tokp08 with Dissolve(1.0)
            show tokp_piss:
                xpos 370 ypos 100
            k3 "aanhhh....."
            y "yes! cover me, whore!"
            k3 "mmmnn... fuck...."
            show ctc
            pause
            hide ctc
            y "I'm gonna cum!"
            k3 "ahhh... cum.... nngh.... cum, baby...."
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            hide tokp_piss
            show tokp tokp06
            with flash
            y "unngh..."
            k3 "mmm.... so warm... deep up in my pussy..."
            show ctc
            pause
            hide ctc
            show tokp tokp07
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "filling me... coating me..."
            k3 "i love fingering myself while stuffed and leaking your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            jump love_bk3_village_background

label katara_hospital_blowjob1:
    $ katara_blowjob_holdhead = False
    $ katara_blowjob_water = False
    y "wanna suck me off?"
    k3 "sure!"
    hide toki toki01 with dissolve
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    show tokb tokb00
    with dissolve
    k3 "ready?"
    show tokb tokb01 with dissolve
    k3 "come here..."
    show tokb tokb02 with dissolve
    y "......."
    show tokb tokb04 with dissolve
    show ctc
    pause
    hide ctc
    show tokb tokb05 with dissolve
    k3 "gimme."
    show tokb tokb07 with dissolve
    k3 "mmm..."
    show tokb tokb100
    show ctc
    pause
    hide ctc
    k3 "*sluurp*"
    k3 "*gulp* *mmmm* *slurp*"
    $ katara_blowjob_blink = True
    menu:
        "hold her head":
            $ katara_blowjob_holdhead = True
        "keep going like this":
            $ katara_blowjob_holdhead = False

    k3 "*gltch* *sluuurp*"

    y "yeah... ah... your tongue is.... amazing..."
    $ katara_blowjob_blink = False
    y "keep... going... right... ah...."
    $ katara_blowjob_blink=True
    pause 1.0
    $ katara_blowjob_blink=False
    pause 1.0
    $ katara_blowjob_blink=True
    pause 1.0
    $ katara_blowjob_blink=False
    y "yes... ahh... fuck..."
    show tokb tokb101
    k3 "*mmngh...* *ahh....* *mngh...*"
    k3 "*slurp* *slurp* *gulp*"
    y "ah... ah... i'm almost..."
    y "i'm ready to cum..."
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
            y "ngh!"
            play sound "audio/splurt2.ogg"
            hide tokb_sperm2
            show tokb_sperm3
            with flash
            y "ohh...."
            k3 "mmmmm....."
            k3 "now get out!"
            k3 "I have to clean!"
            show ctc
            pause
            hide ctc
            jump love_bk3_village_background
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
            y "ngh!"
            play sound "audio/splurt2.ogg"
            show tokb tokb04
            show tokb_sperm4
            with flash
            y "ohh...."
            k3 "mmmmm....."
            k3 "now get out!"
            k3 "I have to clean!"
            show ctc
            pause
            hide ctc
            jump love_bk3_village_background

label love_rebuild_house:
    hide screen earth_money_date
    y "if today's the day i rebuild, i should look in the ruins for scraps."
    "you spend some time sorting through the charred and broken remains."
    y "noth-"
    y "oh, wait."
    y "what's this..."
    y "looks like some obsidian survived."
    y "perfect, that'll make getting it back to upgraded status easy."
    y "........"
    y "hhhmm... this is gonna be a lot of work."
    ya "hhhhrrrrghghh......"
    play sound "audio/earthquake.mp3"
    with vpunch
    hide expression "ebackgrounds/village/buildings/shack/ruined_shack_day.png"
    with Dissolve(2)
    y "ooomph."
    y "fuck that was draining."
    y "okay, now for the {i}hard{/i} part."
    show black with dissolve
    $ lovehousefire = 6
    "you spend the day rebuilding your house."
    $ bk3_day = False
    jump love_bk3_village_background

label love_rebuild_house2:
    show ctc
    pause
    hide ctc
    y "...nice."
    show toki toki02
    show toki_smile
    with dissolve
    k3 "hey!"
    y "howdy."
    k3 "that looks great!"
    y "Thanks, but i don't have much energy for talking right now."
    hide toki_smile with dissolve
    k3 "speaking of... we need to talk."
    y "......."
    y "of course we do."
    y "come on in."
    show toki_smile with dissolve
    k3 "great!"
    scene black with dissolve
    scene inside_shack
    show toki toki01
    with dissolve
    k3 "looks back to normal."
    y "yeah, it took a lot of work, and i'm tired now, so maybe you can come back-"
    k3 "i couldn't find anything on that lantern."
    y "the... what?"
    k3 "do you remember giving me a weird lantern?"
    k3 "that you got from the tunnels?"
    y "oh, right."
    k3 "well, i did the best i could, but nobody knows what it's for."
    y "huh."
    y "that sucks."
    k3 "i know, i'm sorry."
    k3 "anyway, i'm here to give it back."
    k3 "hopefully someone else can-"
    show tosi tosi01:
        xzoom -1 xpos 200
    with dissolve
    suki "aang, we need to talk!"
    y "i... okay, first of all, hello, welcome to my house."
    y "how are you? i'm good, thanks for asking."
    y "maybe fucking knock next time."
    y "like a human being would do."
    suki "sorry, i was just eager to-"
    show tosi tosi02 with dissolve
    suki "oh!"
    show tosi tosi03 with dissolve
    suki "where did you find that!?"
    y "that's just katara."
    show toki_angry with dissolve
    k3 "hey!"
    suki "no, i mean {i}that{/i}."
    suki "the lantern you're holding."
    suki "i hoped i'd never see one of those again."
    k3 "i'm... gonna go."
    hide toki_angry
    show toki_blink
    with dissolve
    k3 "bye, suki!"
    show toki_angry
    hide toki_blink
    show tosi tosi01
    with dissolve
    k3 "...aang."
    hide toki_angry
    hide toki
    with dissolve
    y "...."
    y "that'll smooth over."

    y "anway, you know what this lantern thing is?"
    hide tosi with dissolve
    show tosi tosi01 with dissolve
    suki "yeah, you don't?"
    suki "it's a-"
    show tosi_blink with dissolve
    suki "....hmm."
    y "what?"
    hide tosi_blink with dissolve
    suki "...i can tell you, but..."
    suki "i'd like a favor first."
    menu:
        "bullshit":
            y "fuck, everybody needs shit from me."
            y "what the fuck do you want, suki?"
        "sure":

            y "happy to."
            y "what's up?"

    suki "i want you to upgrade the tavern."
    y "...why?"
    suki "i need space for... planning."
    y "that's ominous."
    suki "okay, truthfully?"
    show tosi_blink with dissolve
    suki "i need a war room."
    y "a war room?"
    hide tosi_blink with dissolve
    suki "i need a place to strategize saving basingse."
    suki "and i can't do it from a storage closet."
    y "....."
    y "you really need it?"
    suki "yes."
    y "i don't think i have enough obsidian for that, though."
    show tosi_blink with dissolve
    suki "you're resourceful, aang."
    suki "i know you can make it happen."
    hide tosi_blink with dissolve
    y "ugh, fine."
    y "and then you'll tell me what this damn lantern is?"
    suki "definitely."
    y "alright, i'll upgrade the tavern."
    suki "thanks, aang."
    hide tosi with dissolve
    y "...this lantern better be fucking worth it."
    y "where the fuck am i going to get more obsidian?"
    "{size=+5}*knock* *knock* *knock*"
    y "oh, what the damn hell."
    y "am i running a fucking hotel?"
    y "who is it, and what do you want!?"
    show azss azss01 with dissolve
    ss "delivery!"
    y "oh, just come right on in, can i get you anything?"
    y "Please, don't wipe your shoes, i didn't just finish building this-"
    ss "i have a delivery for you."
    y "what?"
    ss "I have the first of a two part delivery from mr. shady."
    y "....."
    y "...what?"
    ss "i have a-"
    y "no, i heard you."
    y "i'm just very confused."
    ss "there's a note attached, if it helps."
    y "okay...."
    "\"hey, brother! i told you i was hunting a rare item for you, and i came across this thing and thought of you. Hope it comes in handy.\"\nbutts - shady"
    y "....well it certainly sounds like him."
    y "so what is it?"
    ss "you'll have to open it, sir."
    y "....you're a sassy one."
    ss "yes, sir."
    y "oh!"
    play sound "audio/win2.mp3"
    $ obsidian +=1
    "you received 1 obsidian!"
    y "well, damn."
    y "is he psychic?"
    ss "perhaps, sir."
    y "i was just talking about one of these."
    y "wait, he... came across this?"
    y "so this isn't the item?"
    ss "no sir, this is the first of a two-part delivery."
    y "....."
    y "why is he doing this?"
    ss "mr. shady is quite the benefactor."
    y "....he probably just doesn't want me to beat his head in for his unclear warnings."
    ss "truth be told, i believe mr. shady has quite an affinity for you, sir."
    y "really? huh."
    y "well, tell him thanks when you see him."
    ss "yes, sir."
    ss "i'll be seeing you soon with the second delivery."
    hide azss azss01 with dissolve
    y "...."
    y "shady really gets me."
    y "okay, so i need to upgrade the tavern and then go talk to suki."
    jump love_bk3_village_background

label suki_lantern:
    show tosi tosi01
    show tosi_smile
    with dissolve
    suki "thank you so much, aang!"
    suki "the room is perfect!"
    y "tell me again exactly what you need it for?"
    hide tosi_smile with dissolve
    suki "Maybe... later."
    y "....."
    y "well, at least tell me what this damn lantern is for."
    show tosi tosi03 with dissolve
    suki "it's... a hypnosis device."
    y "it is?"
    suki "how did you think they brainwashed people?"
    y "with a watch?"
    show tosi_blink
    show tosi tosi01
    with dissolve
    suki "no... they use a lantern on a big metal ring."
    suki "they used it on everyone that came through."
    y "even you?"
    suki "......"
    suki "...yes."
    y "has it had any negative effect on you?"
    suki "...i don't know."
    suki "and that scares me."
    hide tosi_blink
    show tosi tosi03
    with dissolve
    suki "but i can't worry about that right now."
    y "so... could i use it to undo brainwashing?"
    show tosi tosi01 with dissolve
    suki "...huh."
    suki "i... suppose so."
    suki "but you're missing a piece..."
    suki "the specific metal ring."
    y "oh."
    y "i have no idea how i'd find that or even transport-"
    ss "delivery!"
    show azss azss01 with dissolve
    suki "i'll... leave you two alone."
    hide tosi with dissolve
    y "what are you doing here?"
    ss "I told you i'd arrive with the second half of mr. shady's gift."
    y "okay..."
    ss "it seems to be a very large metallic circle."
    y "....."
    y "....that fucking guy."
    ss "is that an issue?"
    y "no, it's... amazing."
    ss "as i said, it's very large... it required several people."
    ss "would you like it here?"
    y "no, bring it to my house."
    ss "yes, sir."
    y "follow me."
    scene black with dissolve
    scene inside_shack with dissolve
    "the workers place and set up the ring in your extra room."
    play sound "audio/thud.mp3"
    with vpunch
    y "hey! be careful in there!"
    show azss azss01 with dissolve
    ss "all set up, sir."
    ss "there seems to be a slot for something though."
    ss "a circular object of some kind."
    y "like a lantern?"
    ss "it would have to be oddly-shaped."
    y "it is."
    ss "then... yes."
    ss "have a good day, sir."
    hide azss azss01 with dissolve
    y "....."
    y "so, that will be my \"anti-hypnosis\" room."
    y "....neat."
    jump love_bk3_village_background


label love_toph_footjob1:
    t "so, are you ready for a story?"
    y "are you?"
    t "of course i am..."
    t "you're telling it for me, aren't you?"
    $ toff_clotheson = True
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"
    show toff toff01
    with dissolve
    show ctc
    pause
    hide ctc
    y "before we start..."
    menu:
        "clothes on":
            y "keep your clothes on."
            t "okay..."
            $ toff_clotheson = True
        "clothes off":
            y "take your clothes off."
            t "....."
            t "that's a little forward, isn't it?"
            y "i've seen you naked before."
            y "and come on, you like that i'm fascinated by your body."
            t "........."
            t "okay..."
            $ toff_clotheson = False
            show ctc
            pause
            hide ctc
            y "fuck yeah!"
            y "alright..."

    y "here we go."
    y "ahem."
    y "\"he'd always noticed her feet, from the first moment they met.\""
    y "\"she was small and lithe - perfect for hugging or throwing around - but her feet were the real perfection.\""
    t "........."
    y "...ahem."
    y "\"they faced each other, an air of expectation and anxious hesitation between them.\""
    y "\"she knew what he wanted... and might even be enjoying his discomfort.\""
    y "\"he opened his mouth, uncertain of what to say, when she widened her smile into a predatory grin.\""
    y "\"she spread her legs - slowly, almost casually - in a sultry invitation that froze him in place.\""
    t "........"
    show toff toff00 with dissolve
    t "........."
    show ctc
    pause
    hide ctc
    y "....."
    y "......ahem."
    y "\"she was something between a maiden and a tiger...\""
    y "\"she had a stubborn determination to always get what she wanted... it was a trait he admired in her...\""
    y "\"...but she was a virgin. pure as a snowy midnight.\""
    y "\"she had never seen or felt a penis, despite a new growing, burning interest.\""
    y "\"torn between fascination and hesitancy, she attempted to put him at ease with a simple compliment... and invitation.\""
    y "\"she-"
    t "aang, have i told you lately how strong you've become?"
    t "i'm sure... you must have a great body with all the training we've been doing."
    t "i'd... love to feel it."
    y "....ahem."
    y "\"spurred by her intimacy and flattery, he started to shed his clothing.\""
    y "\"as he began removing his robe and wizard hat, he checked to see if he hadn't misread her tone...\""
    y "\"...but she simply looked at him, waiting for him to lay down and reveal himself.\""
    t "......"
    y "......"
    y "..............."

    show toff toff02 with Dissolve(2.0)

    y "\"he found himself suddenly naked... prostrate before her delicate feet...\""
    y "\"anxious and trembling.\""
    y "\"sensing his hesitation, and coupled with her own desire to feel her first penis...\""
    y "\"she stretched her toes out and gently wrapped them around his cock.\""

    show toff toff03 with dissolve
    t "*oh!*"
    t "Mmmm...."
    show ctc
    pause
    hide ctc
    y "\"surprised by her own confidence, she pressed forward in her discovery of him...\""
    y "\"testing him and watching his face as she explored his growing manhood.\""
    y "\"with alternating strokes, she gripped and rubbed the length of his shaft.\""
    show toff toff04
    show ctc
    pause
    hide ctc
    y "ohhh... ah..."
    t "keep reading."
    y "\"massaging his cock with steady, even strokes, she bent her legs to better cup his member in her arches.\""
    y "\"seeing with her feet, she watched and studied the head of his penis as it peaked through her arches...\""
    y "\"...only to be swallowed back into her feet.\""
    y "\"she... ah... she could hear him softly groaning, the sound drawing a hungry need from inside her.\""
    y "\"she blushed with a unfamiliar but pleasureable wet heat.\""
    y "\"feeling... feeling him... ah... begin to thrust into her supple grip, she... ah... sped up.\""

    show toff toff05
    show ctc
    pause
    hide ctc

    y "Hnngh..."
    y "oh, spirits..."
    t "keep going..."
    y "\"her vigor brought out new fervor between them as he thrust and humped in rhythm with her friction.\""
    y "\"he fuck... fucked her smooth and firm feet, wet with sweat and precum, drawing closer to orgasm...\""
    y "\"when she suddenly... slowed?\""

    show toff toff04
    y "......."
    y "you-"
    t "shh."
    t "don't stop."
    y "that's {i}my{/i} line."
    t "go on...."
    y "........"
    y "\"she cooed that she wanted his cum... but wanted to wait... until his balls were swollen and ready to cover her little feet.\""
    y "\"seeing him enraptured and momentarily wrapped around her metaphorical finger...\""
    y "\"she couldn't help but ask him a question she's wondered for a long time.\""

    show expression "bk3/toph/footjob3/unsure.png":
        xpos 0 ypos 0
    t "....."
    t "aang...?"
    t "Do... do you think I'm pretty?"
    y "You know I do."
    hide expression "bk3/toph/footjob3/unsure.png"

    t "hehe, I just like hearing you say that."
    t "Do you think I'm... prettier than... I dunno... Katara?"

    menu:
        "Way prettier, but don't tell Katara I told you that":
            y "much prettier, but please don't tell her i said that."
            pass
        "You're both pretty in your own way":
            y "you're both pretty."
            t "Oh look at the time. I've got some stuff to do."
            show toff toff02 with dissolve
            y "Waait..."
            t "oh?"
            y "i take it back!"
            y "you're much prettier!"
            show toff toff04 with dissolve

    t "really?"
    t "you're not just saying that?"
    t "...because i have your cock between my toes?"
    y "it's not between your toes."
    show toff_lewd
    t "are you sure?"
    show toff toff08 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    t "now keep reading."
    y "........."
    y "\"....she gripped the head of his cock with her nimble toes... squeezing and tugging at the soft underside of his cock's head.\""

    show toff toff06
    show ctc
    pause
    hide ctc
    y "\"surprised by her skill, he looked at her inquisitively, to which she gave a simple answer.\""
    t "...When you go barefoot all the time, you pick up a trick or two."

    y "\"...still gripping him between her little toes, she pumped him with an unbelievable, unparalleled expertise."
    y "\"he found himself lost in a world of bliss as she licked her lips and stared... focusing on his swollen, pulsing member.\""
    y "f-fuuuck... that feels nice."
    t "Maybe it'll feel even better when I do this."

    show toff toff07
    y "Oh, fuck..."
    y "nnghh..."
    t "finish the story, aang."
    t "i want to know how it ends."
    y "\"she... she sped her pace, pumping him to the brink.\""
    y "\"her small toes flexing and curling teasingly around his thrusting cock as he slid in an out...\""
    y "\"fucking and pounding even deeper into her feet at an accelerated pace.\""
    y "\"she wiggled her toes, and in a whisper began to beg for it... to beg for his thrusts... his cum...\""
    show expression "bk3/toph/footjob3/unsure.png":
        xpos 0 ypos 0
    hide toff_lewd
    t "..........."
    t "ummm....."
    t "{size=-3}...give... give me your cum, aang..."
    t "{size=-3}give it to me... let it... out..."
    t "{size=-3}fuck my feet... fuck my cute little feet..."
    y "ohhh... yes... yeah... unnhh..."

    hide expression "bk3/toph/footjob3/unsure.png"
    t "......."
    t "...don't hold back... thrust... yeah... fuck them... fuck them..."
    y "ungh... ohh..."
    show toff_lewd
    t "{size=+3}ugh... yes... fuck... that's it... fuck my feet, aang! fuck them! ughhn!"
    y "ohhh... toph... toph, i... i..."

    t "r-read... read the end... the... the end..."
    y "\"cup... ah... cupping the head of his cock with her foot and toes... she... ah... she squeezed once, hard... and...\""
    show toff toff09
    t "like this?"
    y "unngh!!"
    show ctc
    pause
    hide ctc
    y "\"he... nnghh.... shot... a... a... desperate, built up cumload right into her... her... toes...\""
    t "her what?"
    y "Her... her fucking..."
    y "hhgng!!"
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/footjob3/sperm1.png"
    pause
    y "Fuck!"
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/footjob3/sperm2.png"
    $ renpy.pause()
    t "yes, aang..."
    t "shoot it into my toes..."
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/footjob3/sperm3.png"
    $ renpy.pause()
    y "unnhh.... damn..."
    y "....phew...."
    y "you just... prevented me from painting the ceiling white..."
    "toph lets out a little giggle... unlike her usual persona."
    t "hehe!"
    y "ahh... damn, girl."
    hide toff_lewd
    t "that was... a good story."
    y "i wholeheartedly agree."
    t "we should do that again some time."
    y "fucking... agreed..."
    t "okay, i need to go clean off."
    t "umm.... goodnight!"
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you settle in for the night."
    jump love_bk3_next
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
